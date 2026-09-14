#!/usr/bin/env python3
"""Bounded AMOS reference runtime for agent/workflow trace contracts.

This module validates trace structure, content-capture policy, effect-state evidence,
missingness, and receipt identity. It does not provide deployment authority and does
not treat trace-parent edges as causal proof.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Sequence

TRACE_ID_RE = re.compile(r"^[0-9a-f]{32}$")
SPAN_ID_RE = re.compile(r"^[0-9a-f]{16}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

RAW_CONTENT_KEYS = {
    "input",
    "output",
    "prompt",
    "completion",
    "tool.arguments",
    "tool.result",
    "gen_ai.input.messages",
    "gen_ai.output.messages",
    "gen_ai.tool.call.arguments",
    "gen_ai.tool.call.result",
}


class TraceContractError(ValueError):
    """Raised when a trace violates the bounded AMOS observability contract."""


class SpanKind(str, Enum):
    WORKFLOW = "WORKFLOW"
    AGENT = "AGENT"
    MODEL = "MODEL"
    TOOL = "TOOL"
    MEMORY = "MEMORY"
    EVALUATION = "EVALUATION"
    EFFECT = "EFFECT"
    OTHER = "OTHER"


class SpanStatus(str, Enum):
    UNSET = "UNSET"
    OK = "OK"
    ERROR = "ERROR"
    IN_DOUBT = "IN_DOUBT"


class EffectState(str, Enum):
    NONE = "NONE"
    PROPOSED = "PROPOSED"
    COMMITTED = "COMMITTED"
    REJECTED = "REJECTED"
    IN_DOUBT = "IN_DOUBT"


class CaptureMode(str, Enum):
    NONE = "NONE"
    METADATA = "METADATA"
    HASH_ONLY = "HASH_ONLY"
    REDACTED = "REDACTED"
    FULL = "FULL"


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _valid_trace_id(value: str) -> bool:
    return bool(TRACE_ID_RE.fullmatch(value)) and value != "0" * 32


def _valid_span_id(value: str) -> bool:
    return bool(SPAN_ID_RE.fullmatch(value)) and value != "0" * 16


def _contains_raw_content(attributes: Mapping[str, Any]) -> list[str]:
    hits: list[str] = []
    for key in attributes:
        lowered = str(key).strip().lower()
        if lowered in RAW_CONTENT_KEYS or lowered.startswith("raw."):
            hits.append(str(key))
    return sorted(hits)


@dataclass(frozen=True)
class TraceSpan:
    trace_id: str
    span_id: str
    parent_span_id: str | None
    name: str
    kind: SpanKind
    start_time_ns: int
    end_time_ns: int
    status: SpanStatus = SpanStatus.UNSET
    attributes: dict[str, Any] = field(default_factory=dict)
    capture_mode: CaptureMode = CaptureMode.METADATA
    capture_authority_id: str | None = None
    payload_digest: str | None = None
    effect_state: EffectState = EffectState.NONE
    effect_id: str | None = None
    authority_decision_id: str | None = None
    receipt_ref: str | None = None
    state_epoch: str | None = None
    provenance_root: str | None = None

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "TraceSpan":
        return cls(
            trace_id=str(data["trace_id"]),
            span_id=str(data["span_id"]),
            parent_span_id=(None if data.get("parent_span_id") in (None, "") else str(data["parent_span_id"])),
            name=str(data["name"]),
            kind=SpanKind(str(data["kind"])),
            start_time_ns=int(data["start_time_ns"]),
            end_time_ns=int(data["end_time_ns"]),
            status=SpanStatus(str(data.get("status", "UNSET"))),
            attributes=dict(data.get("attributes", {})),
            capture_mode=CaptureMode(str(data.get("capture_mode", "METADATA"))),
            capture_authority_id=data.get("capture_authority_id"),
            payload_digest=data.get("payload_digest"),
            effect_state=EffectState(str(data.get("effect_state", "NONE"))),
            effect_id=data.get("effect_id"),
            authority_decision_id=data.get("authority_decision_id"),
            receipt_ref=data.get("receipt_ref"),
            state_epoch=data.get("state_epoch"),
            provenance_root=data.get("provenance_root"),
        )

    @property
    def duration_ns(self) -> int:
        return self.end_time_ns - self.start_time_ns

    def to_dict(self) -> dict[str, Any]:
        return {
            "trace_id": self.trace_id,
            "span_id": self.span_id,
            "parent_span_id": self.parent_span_id,
            "name": self.name,
            "kind": self.kind.value,
            "start_time_ns": self.start_time_ns,
            "end_time_ns": self.end_time_ns,
            "status": self.status.value,
            "attributes": self.attributes,
            "capture_mode": self.capture_mode.value,
            "capture_authority_id": self.capture_authority_id,
            "payload_digest": self.payload_digest,
            "effect_state": self.effect_state.value,
            "effect_id": self.effect_id,
            "authority_decision_id": self.authority_decision_id,
            "receipt_ref": self.receipt_ref,
            "state_epoch": self.state_epoch,
            "provenance_root": self.provenance_root,
        }

    def validate(self) -> None:
        if not _valid_trace_id(self.trace_id):
            raise TraceContractError("trace_id must be non-zero 32-character lowercase hex")
        if not _valid_span_id(self.span_id):
            raise TraceContractError("span_id must be non-zero 16-character lowercase hex")
        if self.parent_span_id is not None and not _valid_span_id(self.parent_span_id):
            raise TraceContractError("parent_span_id must be null or non-zero 16-character lowercase hex")
        if not self.name.strip():
            raise TraceContractError("span name is required")
        if self.start_time_ns < 0 or self.end_time_ns < 0 or self.end_time_ns < self.start_time_ns:
            raise TraceContractError("span timestamps must be non-negative and end_time_ns >= start_time_ns")
        try:
            _canonical_json(self.attributes)
        except (TypeError, ValueError) as exc:
            raise TraceContractError(f"attributes must be JSON-serializable: {exc}") from exc

        raw_keys = _contains_raw_content(self.attributes)
        if raw_keys and self.capture_mode is not CaptureMode.FULL:
            raise TraceContractError(
                "raw prompt/tool/input/output content requires capture_mode FULL; offending keys: "
                + ", ".join(raw_keys)
            )
        if self.capture_mode is CaptureMode.FULL and not self.capture_authority_id:
            raise TraceContractError("FULL content capture requires explicit capture_authority_id")
        if self.capture_mode is CaptureMode.HASH_ONLY:
            if not self.payload_digest or not SHA256_RE.fullmatch(str(self.payload_digest)):
                raise TraceContractError("HASH_ONLY capture requires a lowercase SHA-256 payload_digest")
        elif self.payload_digest is not None and not SHA256_RE.fullmatch(str(self.payload_digest)):
            raise TraceContractError("payload_digest must be lowercase SHA-256 when present")

        if self.kind is SpanKind.EFFECT:
            if self.effect_state is EffectState.NONE:
                raise TraceContractError("EFFECT span requires an explicit effect_state")
            if not self.effect_id:
                raise TraceContractError("EFFECT span requires effect_id")
            if self.effect_state is EffectState.COMMITTED:
                if not self.authority_decision_id:
                    raise TraceContractError("COMMITTED effect requires authority_decision_id")
                if not self.receipt_ref:
                    raise TraceContractError("COMMITTED effect requires receipt_ref")
            if self.effect_state is EffectState.IN_DOUBT and self.status is not SpanStatus.IN_DOUBT:
                raise TraceContractError("IN_DOUBT effect must use span status IN_DOUBT")
        else:
            if self.effect_state is not EffectState.NONE:
                raise TraceContractError("non-EFFECT span cannot carry effect_state")
            if self.effect_id or self.authority_decision_id:
                raise TraceContractError("non-EFFECT span cannot carry effect authority fields")

        if self.status is SpanStatus.IN_DOUBT and not (
            self.kind is SpanKind.EFFECT and self.effect_state is EffectState.IN_DOUBT
        ):
            raise TraceContractError("span status IN_DOUBT is reserved for ambiguous effect outcome")


@dataclass(frozen=True)
class TraceEnvelope:
    trace_id: str
    spans: tuple[TraceSpan, ...]
    expected_span_count: int | None = None
    dropped_span_count: int = 0
    sampling_applied: bool = False
    collector_gap: bool = False
    known_uninstrumented_paths: tuple[str, ...] = ()
    resource: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "TraceEnvelope":
        expected = data.get("expected_span_count")
        return cls(
            trace_id=str(data["trace_id"]),
            spans=tuple(TraceSpan.from_dict(x) for x in data.get("spans", [])),
            expected_span_count=(None if expected is None else int(expected)),
            dropped_span_count=int(data.get("dropped_span_count", 0)),
            sampling_applied=bool(data.get("sampling_applied", False)),
            collector_gap=bool(data.get("collector_gap", False)),
            known_uninstrumented_paths=tuple(str(x) for x in data.get("known_uninstrumented_paths", [])),
            resource=dict(data.get("resource", {})),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "trace_id": self.trace_id,
            "spans": [s.to_dict() for s in self.spans],
            "expected_span_count": self.expected_span_count,
            "dropped_span_count": self.dropped_span_count,
            "sampling_applied": self.sampling_applied,
            "collector_gap": self.collector_gap,
            "known_uninstrumented_paths": list(self.known_uninstrumented_paths),
            "resource": self.resource,
        }

    def validate(self) -> None:
        if not _valid_trace_id(self.trace_id):
            raise TraceContractError("envelope trace_id must be non-zero 32-character lowercase hex")
        if not self.spans:
            raise TraceContractError("trace must contain at least one span")
        if self.dropped_span_count < 0:
            raise TraceContractError("dropped_span_count cannot be negative")
        if self.expected_span_count is not None and self.expected_span_count < 1:
            raise TraceContractError("expected_span_count must be positive when known")
        try:
            _canonical_json(self.resource)
        except (TypeError, ValueError) as exc:
            raise TraceContractError(f"resource must be JSON-serializable: {exc}") from exc

        by_id: dict[str, TraceSpan] = {}
        roots: list[TraceSpan] = []
        for span in self.spans:
            span.validate()
            if span.trace_id != self.trace_id:
                raise TraceContractError("all spans must match envelope trace_id")
            if span.span_id in by_id:
                raise TraceContractError(f"duplicate span_id: {span.span_id}")
            by_id[span.span_id] = span
            if span.parent_span_id is None:
                roots.append(span)
        if len(roots) != 1:
            raise TraceContractError(f"AMOS reference trace requires exactly one root span; found {len(roots)}")

        for span in self.spans:
            if span.parent_span_id is not None and span.parent_span_id not in by_id:
                raise TraceContractError(f"missing parent span: {span.parent_span_id}")
            if span.parent_span_id == span.span_id:
                raise TraceContractError("span cannot parent itself")

        for span in self.spans:
            seen: set[str] = set()
            current = span
            while current.parent_span_id is not None:
                if current.span_id in seen:
                    raise TraceContractError("cycle detected in trace parent relation")
                seen.add(current.span_id)
                current = by_id[current.parent_span_id]

        observed = len(self.spans)
        if self.expected_span_count is not None:
            if observed > self.expected_span_count:
                raise TraceContractError("observed span count cannot exceed expected_span_count")
            if observed + self.dropped_span_count > self.expected_span_count:
                raise TraceContractError("observed + dropped spans cannot exceed expected_span_count")

    def coverage_ratio(self) -> float | None:
        self.validate()
        if self.expected_span_count is None:
            return None
        return len(self.spans) / self.expected_span_count

    def missingness_state(self) -> str:
        self.validate()
        if self.expected_span_count is None:
            return "UNKNOWN"
        complete = (
            len(self.spans) == self.expected_span_count
            and self.dropped_span_count == 0
            and not self.sampling_applied
            and not self.collector_gap
            and not self.known_uninstrumented_paths
        )
        return "COMPLETE" if complete else "PARTIAL"

    def receipt_sha256(self) -> str:
        self.validate()
        return hashlib.sha256(_canonical_json(self.to_dict()).encode("utf-8")).hexdigest()


def shannon_entropy_bits(probabilities: Sequence[float]) -> float:
    """Return Shannon entropy in bits for a normalized discrete distribution."""
    if not probabilities:
        raise TraceContractError("probability vector cannot be empty")
    values = [float(x) for x in probabilities]
    if any((not math.isfinite(x)) or x < 0.0 for x in values):
        raise TraceContractError("probabilities must be finite and non-negative")
    total = sum(values)
    if not math.isclose(total, 1.0, rel_tol=0.0, abs_tol=1e-9):
        raise TraceContractError(f"probabilities must sum to 1; got {total}")
    return -sum(p * math.log2(p) for p in values if p > 0.0)


def entropy_delta_bits(prior: Sequence[float], posterior: Sequence[float]) -> float:
    """Definition: H(posterior) - H(prior). The result may have either sign."""
    return shannon_entropy_bits(posterior) - shannon_entropy_bits(prior)


def kl_divergence_bits(p: Sequence[float], q: Sequence[float]) -> float:
    """Return D_KL(p || q) in bits; non-negative on its valid probability domain."""
    if len(p) != len(q) or not p:
        raise TraceContractError("p and q must be non-empty vectors of equal length")
    p_values = [float(x) for x in p]
    q_values = [float(x) for x in q]
    shannon_entropy_bits(p_values)
    shannon_entropy_bits(q_values)
    total = 0.0
    for pi, qi in zip(p_values, q_values):
        if pi == 0.0:
            continue
        if qi <= 0.0:
            raise TraceContractError("D_KL(p || q) is infinite/undefined when p_i > 0 and q_i = 0")
        total += pi * math.log2(pi / qi)
    if total < -1e-12:
        raise TraceContractError("numerical KL divergence fell below zero tolerance")
    return max(total, 0.0)
