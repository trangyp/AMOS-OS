#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SPAN_KINDS = {"WORKFLOW", "AGENT", "MODEL", "TOOL", "MEMORY", "EFFECT", "EVAL"}
TERMINAL = {"OK", "ERROR", "IN_DOUBT", "CANCELLED"}
SENSITIVE_KEY = re.compile(r"(?:password|passwd|secret|token|api[_-]?key|authorization|cookie|credential)", re.I)
BEARER = re.compile(r"\bBearer\s+[A-Za-z0-9._~+\-/]+=*", re.I)
APIKEY = re.compile(r"\b(?:sk|pk|rk|ak)-[A-Za-z0-9_-]{12,}\b")


def _json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _sha(value: Any) -> str:
    return hashlib.sha256(_json(value).encode("utf-8")).hexdigest()


def _now() -> float:
    return time.time()


def _redact(value: Any) -> Any:
    if isinstance(value, dict):
        out = {}
        for k, v in value.items():
            if SENSITIVE_KEY.search(str(k)):
                out[str(k)] = "[REDACTED]"
            else:
                out[str(k)] = _redact(v)
        return out
    if isinstance(value, list):
        return [_redact(v) for v in value]
    if isinstance(value, tuple):
        return [_redact(v) for v in value]
    if isinstance(value, str):
        value = BEARER.sub("Bearer [REDACTED]", value)
        value = APIKEY.sub("[REDACTED]", value)
        return value
    return value


@dataclass(frozen=True)
class SpanRef:
    trace_id: str
    span_id: str


class TraceContractError(RuntimeError):
    pass


class AgentTraceStore:
    """Local deterministic AMOS observability reference runtime.

    Scope: local SQLite semantics only. This store records observations; it never
    grants authority, proves causality, or certifies external effects.
    """

    def __init__(self, db_path: str | Path):
        self.path = str(db_path)
        self.db = sqlite3.connect(self.path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self._init_schema()

    def close(self) -> None:
        self.db.close()

    def _init_schema(self) -> None:
        self.db.executescript(
            """
            CREATE TABLE IF NOT EXISTS spans (
              trace_id TEXT NOT NULL,
              span_id TEXT PRIMARY KEY,
              parent_span_id TEXT,
              kind TEXT NOT NULL,
              name TEXT NOT NULL,
              subject TEXT NOT NULL,
              subject_version TEXT,
              event_time REAL NOT NULL,
              observed_at REAL NOT NULL,
              started_at REAL NOT NULL,
              ended_at REAL,
              status TEXT NOT NULL,
              input_hash TEXT,
              output_hash TEXT,
              input_redacted_json TEXT,
              output_redacted_json TEXT,
              capture_mode TEXT NOT NULL,
              authority_ref TEXT,
              effect_state TEXT NOT NULL,
              provenance_root TEXT NOT NULL,
              environment TEXT NOT NULL,
              correlation_id TEXT,
              error_type TEXT,
              error_message TEXT,
              FOREIGN KEY(parent_span_id) REFERENCES spans(span_id)
            );
            CREATE TABLE IF NOT EXISTS coverage (
              trace_id TEXT NOT NULL,
              signal_class TEXT NOT NULL,
              expected_count INTEGER NOT NULL DEFAULT 0,
              captured_count INTEGER NOT NULL DEFAULT 0,
              dropped_count INTEGER NOT NULL DEFAULT 0,
              dropped_reason TEXT,
              PRIMARY KEY(trace_id, signal_class)
            );
            CREATE TABLE IF NOT EXISTS ledger (
              seq INTEGER PRIMARY KEY AUTOINCREMENT,
              trace_id TEXT NOT NULL,
              event_type TEXT NOT NULL,
              payload_json TEXT NOT NULL,
              prev_hash TEXT,
              event_hash TEXT NOT NULL,
              recorded_at REAL NOT NULL
            );
            """
        )
        self.db.commit()

    def _ledger(self, trace_id: str, event_type: str, payload: dict[str, Any]) -> str:
        row = self.db.execute("SELECT event_hash FROM ledger ORDER BY seq DESC LIMIT 1").fetchone()
        prev = row[0] if row else None
        body = {"trace_id": trace_id, "event_type": event_type, "payload": payload, "prev_hash": prev}
        event_hash = _sha(body)
        self.db.execute(
            "INSERT INTO ledger(trace_id,event_type,payload_json,prev_hash,event_hash,recorded_at) VALUES(?,?,?,?,?,?)",
            (trace_id, event_type, _json(payload), prev, event_hash, _now()),
        )
        return event_hash

    def start_span(
        self,
        *,
        kind: str,
        name: str,
        subject: str,
        provenance_root: str,
        environment: str,
        trace_id: str | None = None,
        parent_span_id: str | None = None,
        subject_version: str | None = None,
        event_time: float | None = None,
        capture_mode: str = "METADATA_ONLY",
        input_value: Any = None,
        authority_ref: str | None = None,
        effect_state: str = "NONE",
        correlation_id: str | None = None,
    ) -> SpanRef:
        if kind not in SPAN_KINDS:
            raise TraceContractError(f"invalid span kind: {kind}")
        if capture_mode not in {"METADATA_ONLY", "REDACTED_CONTENT"}:
            raise TraceContractError("capture_mode must be METADATA_ONLY or REDACTED_CONTENT")
        if kind != "EFFECT" and effect_state != "NONE":
            raise TraceContractError("effect_state is only valid for EFFECT spans")
        trace_id = trace_id or uuid.uuid4().hex
        if parent_span_id:
            parent = self.db.execute("SELECT trace_id,status FROM spans WHERE span_id=?", (parent_span_id,)).fetchone()
            if not parent:
                raise TraceContractError("parent span not found")
            if parent["trace_id"] != trace_id:
                raise TraceContractError("parent trace mismatch")
            if parent["status"] != "STARTED":
                raise TraceContractError("cannot attach child to terminal parent")
        span_id = uuid.uuid4().hex[:16]
        observed = _now()
        event = observed if event_time is None else float(event_time)
        input_hash = _sha(input_value) if input_value is not None else None
        input_json = None
        if capture_mode == "REDACTED_CONTENT" and input_value is not None:
            input_json = _json(_redact(input_value))
        self.db.execute(
            """INSERT INTO spans(trace_id,span_id,parent_span_id,kind,name,subject,subject_version,event_time,observed_at,started_at,status,input_hash,input_redacted_json,capture_mode,authority_ref,effect_state,provenance_root,environment,correlation_id)
               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (trace_id, span_id, parent_span_id, kind, name, subject, subject_version, event, observed, observed, "STARTED", input_hash, input_json, capture_mode, authority_ref, effect_state, provenance_root, environment, correlation_id),
        )
        self._ledger(trace_id, "SPAN_STARTED", {"span_id": span_id, "kind": kind, "name": name})
        self.db.commit()
        return SpanRef(trace_id, span_id)

    def end_span(
        self,
        ref: SpanRef,
        *,
        status: str,
        output_value: Any = None,
        effect_state: str | None = None,
        error: BaseException | None = None,
    ) -> None:
        if status not in TERMINAL:
            raise TraceContractError(f"invalid terminal status: {status}")
        row = self.db.execute("SELECT * FROM spans WHERE trace_id=? AND span_id=?", (ref.trace_id, ref.span_id)).fetchone()
        if not row:
            raise TraceContractError("span not found")
        if row["status"] != "STARTED":
            raise TraceContractError("span already terminal")
        final_effect = row["effect_state"] if effect_state is None else effect_state
        if row["kind"] != "EFFECT" and final_effect != "NONE":
            raise TraceContractError("non-effect span cannot carry effect_state")
        if row["kind"] == "EFFECT" and final_effect not in {"PROPOSED", "COMMITTED", "REJECTED", "IN_DOUBT", "COMPENSATED", "NONE"}:
            raise TraceContractError("invalid effect_state")
        output_hash = _sha(output_value) if output_value is not None else None
        output_json = None
        if row["capture_mode"] == "REDACTED_CONTENT" and output_value is not None:
            output_json = _json(_redact(output_value))
        err_type = type(error).__name__ if error else None
        err_msg = _redact(str(error)) if error else None
        self.db.execute(
            "UPDATE spans SET ended_at=?,status=?,output_hash=?,output_redacted_json=?,effect_state=?,error_type=?,error_message=? WHERE span_id=?",
            (_now(), status, output_hash, output_json, final_effect, err_type, err_msg, ref.span_id),
        )
        self._ledger(ref.trace_id, "SPAN_ENDED", {"span_id": ref.span_id, "status": status, "effect_state": final_effect})
        self.db.commit()

    def record_coverage(self, trace_id: str, signal_class: str, *, expected: int = 0, captured: int = 0, dropped: int = 0, reason: str | None = None) -> None:
        if min(expected, captured, dropped) < 0:
            raise TraceContractError("coverage counts must be non-negative")
        self.db.execute(
            """INSERT INTO coverage(trace_id,signal_class,expected_count,captured_count,dropped_count,dropped_reason)
               VALUES(?,?,?,?,?,?)
               ON CONFLICT(trace_id,signal_class) DO UPDATE SET
                 expected_count=expected_count+excluded.expected_count,
                 captured_count=captured_count+excluded.captured_count,
                 dropped_count=dropped_count+excluded.dropped_count,
                 dropped_reason=COALESCE(excluded.dropped_reason,dropped_reason)""",
            (trace_id, signal_class, expected, captured, dropped, reason),
        )
        self._ledger(trace_id, "COVERAGE", {"signal_class": signal_class, "expected": expected, "captured": captured, "dropped": dropped, "reason": reason})
        self.db.commit()

    def trace(self, trace_id: str) -> list[dict[str, Any]]:
        rows = self.db.execute("SELECT * FROM spans WHERE trace_id=? ORDER BY started_at,span_id", (trace_id,)).fetchall()
        return [dict(r) for r in rows]

    def receipt(self, trace_id: str) -> dict[str, Any]:
        spans = self.trace(trace_id)
        if not spans:
            raise TraceContractError("trace not found")
        coverage = [dict(r) for r in self.db.execute("SELECT * FROM coverage WHERE trace_id=? ORDER BY signal_class", (trace_id,))]
        complete = all(r["dropped_count"] == 0 and (r["expected_count"] == 0 or r["captured_count"] >= r["expected_count"]) for r in coverage)
        open_spans = [s["span_id"] for s in spans if s["status"] == "STARTED"]
        effect_states = [s["effect_state"] for s in spans if s["kind"] == "EFFECT"]
        status = "INCOMPLETE" if open_spans else "OBSERVED"
        if any(s == "IN_DOUBT" for s in effect_states):
            status = "IN_DOUBT"
        payload = {
            "trace_id": trace_id,
            "subject_roots": sorted({s["subject"] for s in spans}),
            "subject_versions": sorted({s["subject_version"] for s in spans if s["subject_version"]}),
            "environments": sorted({s["environment"] for s in spans}),
            "span_count": len(spans),
            "open_spans": open_spans,
            "coverage": coverage,
            "coverage_complete": complete,
            "effect_states": effect_states,
            "status": status,
            "authority_semantics": "OBSERVED_REFERENCE_ONLY",
            "causal_semantics": "TRACE_EDGE_IS_NOT_CAUSAL_PROOF",
        }
        payload["receipt_hash"] = _sha(payload)
        return payload

    def verify_integrity(self) -> list[str]:
        errors: list[str] = []
        prev = None
        for row in self.db.execute("SELECT * FROM ledger ORDER BY seq"):
            body = {"trace_id": row["trace_id"], "event_type": row["event_type"], "payload": json.loads(row["payload_json"]), "prev_hash": row["prev_hash"]}
            expected = _sha(body)
            if row["prev_hash"] != prev:
                errors.append(f"ledger prev_hash mismatch at seq {row['seq']}")
            if row["event_hash"] != expected:
                errors.append(f"ledger event_hash mismatch at seq {row['seq']}")
            prev = row["event_hash"]
        for row in self.db.execute("SELECT * FROM spans"):
            if row["input_redacted_json"] is not None and row["capture_mode"] != "REDACTED_CONTENT":
                errors.append(f"raw input capture policy mismatch span {row['span_id']}")
            if row["output_redacted_json"] is not None and row["capture_mode"] != "REDACTED_CONTENT":
                errors.append(f"raw output capture policy mismatch span {row['span_id']}")
        return errors

    def otel_projection(self, trace_id: str) -> list[dict[str, Any]]:
        """Return an OpenTelemetry-compatible conceptual projection.

        This is not an OTLP exporter and does not claim semantic-convention conformance.
        """
        out = []
        for s in self.trace(trace_id):
            attrs = {
                "amos.span.kind": s["kind"],
                "amos.subject": s["subject"],
                "amos.provenance.root": s["provenance_root"],
                "amos.effect.state": s["effect_state"],
                "amos.capture.mode": s["capture_mode"],
            }
            if s["authority_ref"]:
                attrs["amos.authority.ref"] = s["authority_ref"]
            out.append({
                "trace_id": s["trace_id"],
                "span_id": s["span_id"],
                "parent_span_id": s["parent_span_id"],
                "name": s["name"],
                "status": s["status"],
                "attributes": attrs,
            })
        return out
