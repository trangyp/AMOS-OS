"""Bounded executable C02 Metacognitive control-plane runtime.

Origin architect / steward: Trang Phan.

AMOS_MODEL reference implementation for the Cognitive Matrix C02 contract.
It implements only the bounded source-claimed surface that can be made
mechanically testable here: monitor identity, interrupt taxonomy, confidence
capping, unresolved-anomaly interruption, and explicit epistemic hold states.

Internet-derived algorithm capsule:
- two-sided tabular CUSUM for numeric-stream mean-shift monitoring;
- source family: NIST Engineering Statistics Handbook, CUSUM control charts;
- the recurrence is an established monitoring algorithm, not AMOS Canon;
- alarm validity remains conditional on the configured target/reference model.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import isfinite
from typing import Dict, Iterable, Tuple

from matrix_registry_runtime import Condition


CONFIDENCE_CAP = 0.95


class InterruptClass(Enum):
    REVIEW = "REVIEW"
    HALT = "HALT"


class MetacognitiveStatus(Enum):
    CONTINUE_BOUNDED = "CONTINUE_BOUNDED"
    HOLD_UNKNOWN = "HOLD_UNKNOWN"
    HOLD_COMPETING = "HOLD_COMPETING"
    REVALIDATE_STALE = "REVALIDATE_STALE"
    BLOCK_UPSTREAM = "BLOCK_UPSTREAM"
    BLOCK_MONITOR_REGISTRY = "BLOCK_MONITOR_REGISTRY"
    INTERRUPT_UNRESOLVED_ANOMALY = "INTERRUPT_UNRESOLVED_ANOMALY"


@dataclass(frozen=True)
class MonitorSpec:
    monitor_id: str
    signal_name: str
    interrupt_class: InterruptClass
    provenance_id: str
    active: bool = True

    def __post_init__(self) -> None:
        for value, name in (
            (self.monitor_id, "monitor_id"),
            (self.signal_name, "signal_name"),
            (self.provenance_id, "provenance_id"),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        if not isinstance(self.interrupt_class, InterruptClass):
            raise ValueError("interrupt_class must be an InterruptClass")
        if not isinstance(self.active, bool):
            raise ValueError("active must be bool")


class MonitorRegistry:
    """Exact-identity monitor registry; IDs cannot silently change meaning."""

    def __init__(self, specs: Iterable[MonitorSpec] = ()) -> None:
        self._specs: Dict[str, MonitorSpec] = {}
        for spec in specs:
            self.register(spec)

    def register(self, spec: MonitorSpec) -> None:
        if not isinstance(spec, MonitorSpec):
            raise ValueError("spec must be MonitorSpec")
        current = self._specs.get(spec.monitor_id)
        if current is not None and current != spec:
            raise ValueError(f"monitor {spec.monitor_id!r} already has different state")
        self._specs[spec.monitor_id] = spec

    def get(self, monitor_id: str) -> MonitorSpec:
        return self._specs[monitor_id]

    def snapshot(self) -> Tuple[MonitorSpec, ...]:
        return tuple(self._specs[key] for key in sorted(self._specs))


@dataclass(frozen=True)
class MonitorObservation:
    monitor_id: str
    anomaly_detected: bool
    resolved: bool
    evidence_id: str

    def __post_init__(self) -> None:
        if not isinstance(self.monitor_id, str) or not self.monitor_id.strip():
            raise ValueError("monitor_id must be a non-empty string")
        if not isinstance(self.evidence_id, str) or not self.evidence_id.strip():
            raise ValueError("evidence_id must be a non-empty string")
        if not isinstance(self.anomaly_detected, bool) or not isinstance(self.resolved, bool):
            raise ValueError("anomaly_detected and resolved must be bool")
        if self.resolved and not self.anomaly_detected:
            raise ValueError("resolved=True requires a detected anomaly")

    @property
    def unresolved(self) -> bool:
        return self.anomaly_detected and not self.resolved


@dataclass(frozen=True)
class MetacognitiveRequest:
    request_id: str
    state_version: str
    provenance_ids: Tuple[str, ...]
    reported_confidence: float
    observations: Tuple[MonitorObservation, ...] = ()
    upstream_condition: Condition = Condition.ACTIVE
    unknown_gaps: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for value, name in ((self.request_id, "request_id"), (self.state_version, "state_version")):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        if not self.provenance_ids:
            raise ValueError("C02 request requires provenance")
        if len(set(self.provenance_ids)) != len(self.provenance_ids):
            raise ValueError("provenance_ids must be unique")
        if any(not isinstance(item, str) or not item.strip() for item in self.provenance_ids):
            raise ValueError("provenance_ids must contain non-empty strings")
        confidence = float(self.reported_confidence)
        if not isfinite(confidence) or not 0.0 <= confidence <= 1.0:
            raise ValueError("reported_confidence must be finite and in [0,1]")
        if not isinstance(self.upstream_condition, Condition):
            raise ValueError("upstream_condition must be a Condition")
        if len(set(self.unknown_gaps)) != len(self.unknown_gaps):
            raise ValueError("unknown_gaps must be unique")
        if any(not isinstance(item, str) or not item.strip() for item in self.unknown_gaps):
            raise ValueError("unknown_gaps must contain non-empty strings")
        evidence_ids = tuple(obs.evidence_id for obs in self.observations)
        if len(set(evidence_ids)) != len(evidence_ids):
            raise ValueError("monitor observation evidence_ids must be unique")


@dataclass(frozen=True)
class MetacognitiveResult:
    status: MetacognitiveStatus
    request_id: str
    state_version: str
    provenance_ids: Tuple[str, ...]
    bounded_confidence: float
    unresolved_monitor_ids: Tuple[str, ...]
    interrupts: Tuple[Tuple[str, InterruptClass], ...]
    reasons: Tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.request_id.strip() or not self.state_version.strip():
            raise ValueError("result identity must be explicit")
        if not self.provenance_ids:
            raise ValueError("C02 result cannot lose provenance")
        if not isfinite(self.bounded_confidence) or not 0.0 <= self.bounded_confidence <= CONFIDENCE_CAP:
            raise ValueError("bounded_confidence violates C02 confidence cap")
        if not self.reasons:
            raise ValueError("C02 result requires at least one reason")
        if self.status is MetacognitiveStatus.INTERRUPT_UNRESOLVED_ANOMALY and not self.unresolved_monitor_ids:
            raise ValueError("anomaly interrupt requires unresolved monitor identity")

    @property
    def may_escalate(self) -> bool:
        return self.status is MetacognitiveStatus.CONTINUE_BOUNDED


def _merge_provenance(request: MetacognitiveRequest) -> Tuple[str, ...]:
    ordered = list(request.provenance_ids)
    seen = set(ordered)
    for observation in request.observations:
        if observation.evidence_id not in seen:
            ordered.append(observation.evidence_id)
            seen.add(observation.evidence_id)
    return tuple(ordered)


def _result(
    request: MetacognitiveRequest,
    status: MetacognitiveStatus,
    *reasons: str,
    unresolved_monitor_ids: Tuple[str, ...] = (),
    interrupts: Tuple[Tuple[str, InterruptClass], ...] = (),
) -> MetacognitiveResult:
    bounded_confidence = min(float(request.reported_confidence), CONFIDENCE_CAP)
    confidence_reason = (
        ("CONFIDENCE_CAPPED_AT_0_95",)
        if float(request.reported_confidence) > CONFIDENCE_CAP
        else ()
    )
    return MetacognitiveResult(
        status=status,
        request_id=request.request_id,
        state_version=request.state_version,
        provenance_ids=_merge_provenance(request),
        bounded_confidence=bounded_confidence,
        unresolved_monitor_ids=unresolved_monitor_ids,
        interrupts=interrupts,
        reasons=tuple(reasons) + confidence_reason,
    )


def evaluate_metacognitive(
    request: MetacognitiveRequest,
    registry: MonitorRegistry,
) -> MetacognitiveResult:
    """Evaluate the bounded C02 contract in deterministic fail-closed order."""
    if not isinstance(registry, MonitorRegistry):
        raise ValueError("registry must be MonitorRegistry")

    if request.upstream_condition is Condition.STALE:
        return _result(request, MetacognitiveStatus.REVALIDATE_STALE, "UPSTREAM_STALE")
    if request.upstream_condition is Condition.COMPETING:
        return _result(request, MetacognitiveStatus.HOLD_COMPETING, "UPSTREAM_COMPETING_PRESERVED")
    if request.upstream_condition in (Condition.QUARANTINED, Condition.FALSIFIED):
        return _result(
            request,
            MetacognitiveStatus.BLOCK_UPSTREAM,
            f"UPSTREAM_{request.upstream_condition.value}",
        )
    if request.unknown_gaps:
        return _result(
            request,
            MetacognitiveStatus.HOLD_UNKNOWN,
            "UNKNOWN_GAP_PRESENT",
            *request.unknown_gaps,
        )

    specs = {}
    for observation in request.observations:
        try:
            spec = registry.get(observation.monitor_id)
        except KeyError:
            return _result(
                request,
                MetacognitiveStatus.BLOCK_MONITOR_REGISTRY,
                f"UNKNOWN_MONITOR:{observation.monitor_id}",
            )
        if not spec.active:
            return _result(
                request,
                MetacognitiveStatus.BLOCK_MONITOR_REGISTRY,
                f"INACTIVE_MONITOR:{observation.monitor_id}",
            )
        specs[observation.monitor_id] = spec

    unresolved = tuple(sorted(obs.monitor_id for obs in request.observations if obs.unresolved))
    if unresolved:
        interrupts = tuple(
            (monitor_id, specs[monitor_id].interrupt_class)
            for monitor_id in unresolved
        )
        return _result(
            request,
            MetacognitiveStatus.INTERRUPT_UNRESOLVED_ANOMALY,
            "UNRESOLVED_ANOMALY_HALTS_ESCALATION",
            unresolved_monitor_ids=unresolved,
            interrupts=interrupts,
        )

    return _result(
        request,
        MetacognitiveStatus.CONTINUE_BOUNDED,
        "C02_BOUNDED_MONITOR_AND_CONFIDENCE_CHECKS_SATISFIED",
    )


@dataclass(frozen=True)
class CusumConfig:
    target_mean: float
    allowance: float
    decision_limit: float

    def __post_init__(self) -> None:
        for value, name in (
            (self.target_mean, "target_mean"),
            (self.allowance, "allowance"),
            (self.decision_limit, "decision_limit"),
        ):
            if not isfinite(float(value)):
                raise ValueError(f"{name} must be finite")
        if self.allowance < 0.0:
            raise ValueError("allowance must be >= 0")
        if self.decision_limit <= 0.0:
            raise ValueError("decision_limit must be > 0")


@dataclass(frozen=True)
class CusumState:
    positive: float = 0.0
    negative: float = 0.0
    samples: int = 0

    def __post_init__(self) -> None:
        if not isfinite(float(self.positive)) or not isfinite(float(self.negative)):
            raise ValueError("CUSUM state must be finite")
        if self.positive < 0.0 or self.negative < 0.0:
            raise ValueError("CUSUM state must be non-negative")
        if not isinstance(self.samples, int) or self.samples < 0:
            raise ValueError("samples must be a non-negative integer")


class ShiftDirection(Enum):
    NONE = "NONE"
    UP = "UP"
    DOWN = "DOWN"
    BOTH = "BOTH"


@dataclass(frozen=True)
class CusumUpdate:
    state: CusumState
    alarm: bool
    direction: ShiftDirection


def update_cusum(config: CusumConfig, state: CusumState, observation: float) -> CusumUpdate:
    """Apply a two-sided tabular CUSUM update.

    C_t+ = max(0, C_(t-1)+ + (x_t - mu_0) - k)
    C_t- = max(0, C_(t-1)- + (mu_0 - x_t) - k)
    alarm iff C_t+ >= h or C_t- >= h.

    ``target_mean`` (mu_0), ``allowance`` (k), ``decision_limit`` (h), and
    ``observation`` must share compatible units. The accumulated CUSUM values
    therefore carry the observation's units.
    """
    if not isinstance(config, CusumConfig) or not isinstance(state, CusumState):
        raise ValueError("config and state must be CusumConfig/CusumState")
    x = float(observation)
    if not isfinite(x):
        raise ValueError("observation must be finite")

    positive = max(0.0, state.positive + (x - config.target_mean) - config.allowance)
    negative = max(0.0, state.negative + (config.target_mean - x) - config.allowance)
    up = positive >= config.decision_limit
    down = negative >= config.decision_limit
    if up and down:
        direction = ShiftDirection.BOTH
    elif up:
        direction = ShiftDirection.UP
    elif down:
        direction = ShiftDirection.DOWN
    else:
        direction = ShiftDirection.NONE
    next_state = CusumState(positive=positive, negative=negative, samples=state.samples + 1)
    return CusumUpdate(next_state, up or down, direction)
