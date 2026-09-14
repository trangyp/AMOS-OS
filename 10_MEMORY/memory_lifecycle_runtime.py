#!/usr/bin/env python3
"""Deterministic AMOS memory lifecycle reference runtime.

Scope: local SQLite reference semantics only. Retrieval returns observations;
it does not validate truth or confer action authority.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

ACTIVE = "ACTIVE"
QUARANTINED = "QUARANTINED"
SUPERSEDED = "SUPERSEDED"
EXPIRED = "EXPIRED"
TOMBSTONED = "TOMBSTONED"
VISIBLE_STATES = {ACTIVE}
ALL_STATES = {ACTIVE, QUARANTINED, SUPERSEDED, EXPIRED, TOMBSTONED}
READ_CAP = "memory.read"


def _canon(x: Any) -> str:
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _hash(x: Any) -> str:
    return hashlib.sha256(_canon(x).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class MemoryRecord:
    memory_id: str
    origin_id: str
    version: int
    scope: str
    subject: str
    content: str
    content_hash: str
    state: str
    epistemic_class: str
    valid_from: float | None
    valid_to: float | None
    observed_at: float
    recorded_at: float
    predecessor_id: str | None
    superseded_by: str | None
    provenance: str


class MemoryRuntimeError(RuntimeError):
    pass


class AuthorityError(MemoryRuntimeError):
    pass


class ConflictError(MemoryRuntimeError):
    pass


class IntegrityError(MemoryRuntimeError):
    pass


class MemoryStore:
    def __init__(self, db_path: str | Path):
        self.db_path = str(db_path)
        self.db = sqlite3.connect(self.db_path)
        self.db.row_factory = sqlite3.Row
        self._init_schema()

    def close(self) -> None:
        self.db.close()

    def _init_schema(self) -> None:
        self.db.executescript(
            """
            PRAGMA foreign_keys=ON;
            CREATE TABLE IF NOT EXISTS memories (
                memory_id TEXT PRIMARY KEY,
                origin_id TEXT NOT NULL,
                version INTEGER NOT NULL,
                scope TEXT NOT NULL,
                subject TEXT NOT NULL,
                content TEXT NOT NULL,
                content_hash TEXT NOT NULL,
                state TEXT NOT NULL,
                epistemic_class TEXT NOT NULL,
                valid_from REAL,
                valid_to REAL,
                observed_at REAL NOT NULL,
                recorded_at REAL NOT NULL,
                predecessor_id TEXT,
                superseded_by TEXT,
                provenance TEXT NOT NULL,
                UNIQUE(origin_id, version)
            );
            CREATE TABLE IF NOT EXISTS ledger (
                seq INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT NOT NULL,
                memory_id TEXT NOT NULL,
                payload TEXT NOT NULL,
                prev_hash TEXT NOT NULL,
                event_hash TEXT NOT NULL,
                recorded_at REAL NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_mem_scope_state ON memories(scope, state);
            CREATE INDEX IF NOT EXISTS idx_mem_origin_ver ON memories(origin_id, version);
            """
        )
        self.db.commit()

    @staticmethod
    def _require_cap(capabilities: Iterable[str], cap: str) -> None:
        if cap not in set(capabilities):
            raise AuthorityError(f"missing capability: {cap}")

    def _append_event(self, event_type: str, memory_id: str, payload: dict[str, Any], now: float) -> None:
        row = self.db.execute("SELECT event_hash FROM ledger ORDER BY seq DESC LIMIT 1").fetchone()
        prev_hash = row[0] if row else "0" * 64
        body = {"event_type": event_type, "memory_id": memory_id, "payload": payload, "prev_hash": prev_hash, "recorded_at": now}
        event_hash = _hash(body)
        self.db.execute(
            "INSERT INTO ledger(event_type,memory_id,payload,prev_hash,event_hash,recorded_at) VALUES(?,?,?,?,?,?)",
            (event_type, memory_id, _canon(payload), prev_hash, event_hash, now),
        )

    def admit(self, *, scope: str, subject: str, content: str, provenance: str,
              capabilities: Iterable[str], valid_from: float | None = None,
              valid_to: float | None = None, observed_at: float | None = None,
              origin_id: str | None = None, epistemic_class: str = "OBSERVATION",
              now: float | None = None) -> MemoryRecord:
        self._require_cap(capabilities, "memory.admit")
        if not scope or not subject or not content or not provenance:
            raise ValueError("scope, subject, content, and provenance are required")
        if epistemic_class != "OBSERVATION":
            raise ValueError("memory admission must enter as OBSERVATION")
        if valid_from is not None and valid_to is not None and valid_to < valid_from:
            raise ValueError("valid_to precedes valid_from")
        now = float(time.time() if now is None else now)
        observed_at = now if observed_at is None else float(observed_at)
        origin_id = origin_id or str(uuid.uuid4())
        existing = self.db.execute("SELECT MAX(version) FROM memories WHERE origin_id=?", (origin_id,)).fetchone()[0]
        if existing is not None:
            raise ConflictError("origin_id already exists; use revise()")
        memory_id = str(uuid.uuid4())
        content_hash = _hash({"content": content})
        with self.db:
            self.db.execute(
                """INSERT INTO memories(memory_id,origin_id,version,scope,subject,content,content_hash,state,epistemic_class,
                   valid_from,valid_to,observed_at,recorded_at,predecessor_id,superseded_by,provenance)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (memory_id, origin_id, 1, scope, subject, content, content_hash, ACTIVE, epistemic_class,
                 valid_from, valid_to, observed_at, now, None, None, provenance),
            )
            self._append_event("ADMIT", memory_id, {"origin_id": origin_id, "version": 1, "scope": scope, "content_hash": content_hash}, now)
        return self.get(memory_id, capabilities={READ_CAP}, include_nonactive=True)

    def revise(self, memory_id: str, *, content: str, provenance: str,
               capabilities: Iterable[str], valid_from: float | None = None,
               valid_to: float | None = None, observed_at: float | None = None,
               now: float | None = None) -> MemoryRecord:
        self._require_cap(capabilities, "memory.revise")
        current = self._row(memory_id)
        if current["state"] not in {ACTIVE, QUARANTINED, EXPIRED}:
            raise ConflictError(f"cannot revise state {current['state']}")
        if valid_from is not None and valid_to is not None and valid_to < valid_from:
            raise ValueError("valid_to precedes valid_from")
        now = float(time.time() if now is None else now)
        observed_at = now if observed_at is None else float(observed_at)
        new_id = str(uuid.uuid4())
        version = int(current["version"]) + 1
        content_hash = _hash({"content": content})
        with self.db:
            self.db.execute("UPDATE memories SET state=?, superseded_by=? WHERE memory_id=?", (SUPERSEDED, new_id, memory_id))
            self.db.execute(
                """INSERT INTO memories(memory_id,origin_id,version,scope,subject,content,content_hash,state,epistemic_class,
                   valid_from,valid_to,observed_at,recorded_at,predecessor_id,superseded_by,provenance)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (new_id, current["origin_id"], version, current["scope"], current["subject"], content, content_hash,
                 ACTIVE, "OBSERVATION", valid_from, valid_to, observed_at, now, memory_id, None, provenance),
            )
            self._append_event("SUPERSEDE", memory_id, {"superseded_by": new_id}, now)
            self._append_event("REVISE", new_id, {"origin_id": current["origin_id"], "version": version, "content_hash": content_hash}, now)
        return self.get(new_id, capabilities={READ_CAP}, include_nonactive=True)

    def _transition(self, memory_id: str, target: str, reason: str, cap: str,
                    capabilities: Iterable[str], now: float | None) -> None:
        self._require_cap(capabilities, cap)
        if target not in ALL_STATES:
            raise ValueError(target)
        row = self._row(memory_id)
        if row["state"] in {SUPERSEDED, TOMBSTONED}:
            raise ConflictError(f"cannot transition terminal state {row['state']}")
        now = float(time.time() if now is None else now)
        with self.db:
            self.db.execute("UPDATE memories SET state=? WHERE memory_id=?", (target, memory_id))
            self._append_event(target, memory_id, {"reason": reason}, now)

    def quarantine(self, memory_id: str, *, reason: str, capabilities: Iterable[str], now: float | None = None) -> None:
        self._transition(memory_id, QUARANTINED, reason, "memory.quarantine", capabilities, now)

    def expire(self, memory_id: str, *, reason: str, capabilities: Iterable[str], now: float | None = None) -> None:
        self._transition(memory_id, EXPIRED, reason, "memory.expire", capabilities, now)

    def tombstone(self, memory_id: str, *, reason: str, capabilities: Iterable[str], now: float | None = None) -> None:
        self._transition(memory_id, TOMBSTONED, reason, "memory.tombstone", capabilities, now)

    def _row(self, memory_id: str) -> sqlite3.Row:
        row = self.db.execute("SELECT * FROM memories WHERE memory_id=?", (memory_id,)).fetchone()
        if row is None:
            raise KeyError(memory_id)
        return row

    @staticmethod
    def _to_record(row: sqlite3.Row) -> MemoryRecord:
        return MemoryRecord(**dict(row))

    def get(self, memory_id: str, *, capabilities: Iterable[str], include_nonactive: bool = False) -> MemoryRecord:
        self._require_cap(capabilities, READ_CAP)
        row = self._row(memory_id)
        if not include_nonactive and row["state"] not in VISIBLE_STATES:
            raise KeyError(memory_id)
        return self._to_record(row)

    def retrieve(self, *, scope: str, query: str, capabilities: Iterable[str],
                 valid_at: float | None = None, recorded_at: float | None = None,
                 limit: int = 10, include_nonactive: bool = False) -> list[MemoryRecord]:
        self._require_cap(capabilities, READ_CAP)
        states = ALL_STATES if include_nonactive else VISIBLE_STATES
        placeholders = ",".join("?" for _ in states)
        params: list[Any] = [scope, *sorted(states)]
        sql = f"SELECT * FROM memories WHERE scope=? AND state IN ({placeholders})"
        if recorded_at is not None:
            sql += " AND recorded_at<=?"
            params.append(float(recorded_at))
        rows = list(self.db.execute(sql, params))
        qterms = {t.lower() for t in query.split() if t.strip()}
        out: list[tuple[int, float, sqlite3.Row]] = []
        for row in rows:
            if valid_at is not None:
                vf, vt = row["valid_from"], row["valid_to"]
                if vf is not None and valid_at < vf:
                    continue
                if vt is not None and valid_at >= vt:
                    continue
            text = f"{row['subject']} {row['content']}".lower()
            score = sum(1 for t in qterms if t in text)
            if qterms and score == 0:
                continue
            out.append((score, float(row["recorded_at"]), row))
        out.sort(key=lambda x: (x[0], x[1]), reverse=True)
        return [self._to_record(x[2]) for x in out[: max(0, int(limit))]]

    def assemble_context(self, *, scope: str, query: str, capabilities: Iterable[str],
                         limit: int = 8, valid_at: float | None = None) -> list[dict[str, Any]]:
        records = self.retrieve(scope=scope, query=query, capabilities=capabilities, limit=limit, valid_at=valid_at)
        return [{"memory_id": r.memory_id, "origin_id": r.origin_id, "version": r.version,
                 "content": r.content, "epistemic_class": "OBSERVATION", "provenance": r.provenance,
                 "state": r.state, "valid_from": r.valid_from, "valid_to": r.valid_to} for r in records]

    def history(self, origin_id: str, *, capabilities: Iterable[str]) -> list[MemoryRecord]:
        self._require_cap(capabilities, READ_CAP)
        rows = self.db.execute("SELECT * FROM memories WHERE origin_id=? ORDER BY version", (origin_id,)).fetchall()
        return [self._to_record(r) for r in rows]

    def verify_integrity(self) -> None:
        for row in self.db.execute("SELECT * FROM memories"):
            if row["content_hash"] != _hash({"content": row["content"]}):
                raise IntegrityError(f"content hash mismatch: {row['memory_id']}")
        prev = "0" * 64
        for row in self.db.execute("SELECT * FROM ledger ORDER BY seq"):
            if row["prev_hash"] != prev:
                raise IntegrityError(f"ledger predecessor mismatch at seq {row['seq']}")
            body = {"event_type": row["event_type"], "memory_id": row["memory_id"],
                    "payload": json.loads(row["payload"]), "prev_hash": row["prev_hash"],
                    "recorded_at": row["recorded_at"]}
            expected = _hash(body)
            if expected != row["event_hash"]:
                raise IntegrityError(f"ledger hash mismatch at seq {row['seq']}")
            prev = row["event_hash"]


__all__ = ["MemoryStore", "MemoryRecord", "MemoryRuntimeError", "AuthorityError", "ConflictError", "IntegrityError",
           "ACTIVE", "QUARANTINED", "SUPERSEDED", "EXPIRED", "TOMBSTONED"]
