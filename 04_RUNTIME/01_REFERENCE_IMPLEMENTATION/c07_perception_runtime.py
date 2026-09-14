"""Bounded executable C07 Perception control-plane runtime.

Origin architect / steward: Trang Phan.

AMOS_MODEL reference implementation. C07 keeps modality availability, observer,
provenance, epistemic origin, feature typing, and confidence explicit. It does
not invent unavailable sensor data and does not promote cross-modal correlation
to causality.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import isfinite
from typing import Tuple


class PerceptOrigin(Enum):
    OBSERVED = "OBSERVED"
    USER_REPORTED = "USER_REPORTED"
    INFERRED = "INFERRED"
    SIMULATED = "SIMULATED"
    UNOBSERVED = "UNOBSERVED"


class PerceptionStatus(Enum):
    PERCEPT_VALID = "PERCEPT_VALID"
    FUSION_VALID = "FUSION_VALID"
    HOLD_UNOBSERVED = "HOLD_UNOBSERVED"
    BLOCK_ORIGIN = "BLOCK_ORIGIN"
    BLOCK_CONFIDENCE = "BLOCK_CONFIDENCE"
    BLOCK_OBSERVER = "BLOCK_OBSERVER"
    BLOCK_PROVENANCE = "BLOCK_PROVENANCE"


@dataclass(frozen=True)
class Percept:
    object_id: str
    modality: str
    feature: str
    observer: str
    provenance_ids: Tuple[str, ...]
    origin: PerceptOrigin
    available: bool
    confidence: float
    intensity: float | None = None
    valence: float | None = None
    arousal: float | None = None
    clarity: float | None = None

    def __post_init__(self) -> None:
        for value, name in ((self.object_id, "object_id"), (self.modality, "modality"), (self.feature, "feature"), (self.observer, "observer")):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be non-empty")
        if not self.provenance_ids or any(not isinstance(p, str) or not p.strip() for p in self.provenance_ids):
            raise ValueError("provenance_ids must contain non-empty strings")
        if len(set(self.provenance_ids)) != len(self.provenance_ids):
            raise ValueError("provenance_ids must be unique")
        if not isinstance(self.origin, PerceptOrigin):
            raise ValueError("origin must be PerceptOrigin")
        if type(self.available) is not bool:
            raise ValueError("available must be bool")
        if not isinstance(self.confidence, (int, float)) or not isfinite(float(self.confidence)) or not 0.0 <= float(self.confidence) <= 1.0:
            raise ValueError("confidence must be finite in [0,1]")
        for value, name in ((self.intensity, "intensity"), (self.valence, "valence"), (self.arousal, "arousal"), (self.clarity, "clarity")):
            if value is not None and (not isinstance(value, (int, float)) or not isfinite(float(value))):
                raise ValueError(f"{name} must be finite when present")
        if not self.available:
            if self.origin is not PerceptOrigin.UNOBSERVED:
                raise ValueError("unavailable modality must remain UNOBSERVED")
            if self.confidence != 0.0:
                raise ValueError("UNOBSERVED unavailable modality must have confidence 0")
        if self.available and self.origin is PerceptOrigin.UNOBSERVED:
            raise ValueError("available modality cannot be labeled UNOBSERVED")


@dataclass(frozen=True)
class FusionResult:
    status: PerceptionStatus
    object_id: str
    feature: str
    observers: Tuple[str, ...]
    modalities: Tuple[str, ...]
    confidence: float
    provenance_ids: Tuple[str, ...]
    causal_claim: bool
    reasons: Tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.reasons:
            raise ValueError("fusion result requires reasons")
        if self.causal_claim:
            raise ValueError("C07 fusion cannot mint a causal claim")


def validate_percept(percept: Percept) -> PerceptionStatus:
    if not percept.provenance_ids:
        return PerceptionStatus.BLOCK_PROVENANCE
    if not percept.observer.strip():
        return PerceptionStatus.BLOCK_OBSERVER
    if not percept.available:
        return PerceptionStatus.HOLD_UNOBSERVED
    return PerceptionStatus.PERCEPT_VALID


def fuse(percepts: Tuple[Percept, ...]) -> FusionResult:
    """Fuse same object/feature only; confidence <= weakest available channel."""
    if not percepts:
        raise ValueError("percepts must be non-empty")
    object_ids = {p.object_id for p in percepts}
    features = {p.feature for p in percepts}
    if len(object_ids) != 1 or len(features) != 1:
        raise ValueError("fusion requires one object and one feature")

    available = tuple(p for p in percepts if p.available)
    provenance = tuple(sorted({prov for p in percepts for prov in p.provenance_ids}))
    observers = tuple(sorted({p.observer for p in percepts}))
    modalities = tuple(sorted({p.modality for p in percepts}))
    object_id = percepts[0].object_id
    feature = percepts[0].feature

    if not available:
        return FusionResult(
            PerceptionStatus.HOLD_UNOBSERVED, object_id, feature, observers, modalities,
            0.0, provenance, False, ("NO_AVAILABLE_MODALITY",),
        )

    confidence = min(float(p.confidence) for p in available)
    return FusionResult(
        PerceptionStatus.FUSION_VALID,
        object_id,
        feature,
        observers,
        modalities,
        confidence,
        provenance,
        False,
        (
            "FUSION_CONFIDENCE_CAPPED_BY_WEAKEST_AVAILABLE_CHANNEL",
            "OBSERVED_USER_REPORTED_INFERRED_AND_SIMULATED_ORIGINS_REMAIN_DISTINCT_IN_INPUTS",
            "CROSS_MODAL_CORRELATION_IS_NOT_CAUSAL_EVIDENCE",
        ),
    )
