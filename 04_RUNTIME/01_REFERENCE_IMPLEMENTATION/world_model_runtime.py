"""Bounded executable L10 world-model contract for AMOS OS.

Origin architect / steward: Trang Phan.

This AMOS_MODEL reference runtime preserves representation class, provenance,
fidelity envelope, reality contact, and model-observation discrepancy. It does
not treat simulation consistency as real-world confirmation.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import FrozenSet, Optional


class RepresentationClass(Enum):
    OBSERVED_REALITY = "OBSERVED_REALITY"
    MEASURED_PROXY = "MEASURED_PROXY"
    MODEL_STATE = "MODEL_STATE"
    SIMULATION = "SIMULATION"
    COUNTERFACTUAL = "COUNTERFACTUAL"
    SYNTHETIC_DATA = "SYNTHETIC_DATA"
    DIGITAL_TWIN = "DIGITAL_TWIN"
    FORECAST = "FORECAST"
    DEPLOYED_OUTCOME = "DEPLOYED_OUTCOME"


class AssessmentStatus(Enum):
    VERIFIED_BOUNDED = "VERIFIED_BOUNDED"
    WITHIN_TOLERANCE = "WITHIN_TOLERANCE"
    EXCEEDS_TOLERANCE = "EXCEEDS_TOLERANCE"
    UNKNOWN_GAP = "UNKNOWN/GAP"


_REALITY_CONTACT_CLASSES = {
    RepresentationClass.OBSERVED_REALITY,
    RepresentationClass.MEASURED_PROXY,
    RepresentationClass.DEPLOYED_OUTCOME,
}

_MODEL_CLASSES = {
    RepresentationClass.MODEL_STATE,
    RepresentationClass.SIMULATION,
    RepresentationClass.COUNTERFACTUAL,
    RepresentationClass.DIGITAL_TWIN,
    RepresentationClass.FORECAST,
}


@dataclass(frozen=True)
class RepresentationRecord:
    object_id: str
    representation_class: RepresentationClass
    variable: str
    value: Optional[float]
    unit: str
    measurement_method: Optional[str]
    time_id: str
    regime: str
    provenance: str
    provenance_root: str
    scale: str = "unspecified"
    observer: str = "unspecified"
    validation_status: str = "UNKNOWN"
    consequence: str = "none"
    external_observation_present: bool = False
    generator_id: Optional[str] = None

    def __post_init__(self) -> None:
        required = {
            "object_id": self.object_id,
            "variable": self.variable,
            "unit": self.unit,
            "time_id": self.time_id,
            "regime": self.regime,
            "provenance": self.provenance,
            "provenance_root": self.provenance_root,
            "scale": self.scale,
            "observer": self.observer,
            "validation_status": self.validation_status,
            "consequence": self.consequence,
        }
        for name, value in required.items():
            if not value.strip():
                raise ValueError(f"{name} must be explicit and non-empty")


@dataclass(frozen=True)
class FidelityEnvelope:
    validated_variables: FrozenSet[str]
    validated_regimes: FrozenSet[str]
    validated_time_ids: FrozenSet[str]
    validated_measurement_methods: FrozenSet[str]

    def contains(self, record: RepresentationRecord) -> bool:
        method = record.measurement_method
        return (
            record.variable in self.validated_variables
            and record.regime in self.validated_regimes
            and record.time_id in self.validated_time_ids
            and method is not None
            and method in self.validated_measurement_methods
        )


@dataclass(frozen=True)
class TensorCoordinate:
    object_id: str
    representation_class: RepresentationClass
    variable: str
    scale: str
    time_id: str
    regime: str
    observer: str
    provenance: str
    validation_status: str
    consequence: str

    def __post_init__(self) -> None:
        for name in (
            "object_id",
            "variable",
            "scale",
            "time_id",
            "regime",
            "observer",
            "provenance",
            "validation_status",
            "consequence",
        ):
            if not getattr(self, name).strip():
                raise ValueError(f"tensor axis {name} must be explicit")


@dataclass(frozen=True)
class MismatchAssessment:
    status: AssessmentStatus
    reason: str
    absolute_error: Optional[float]
    tolerance: Optional[float]
    model_provenance: str
    observation_provenance: str


def reality_contact(record: RepresentationRecord, envelope: FidelityEnvelope) -> bool:
    """Bounded reality-contact gate for externally anchored records."""
    return (
        record.representation_class in _REALITY_CONTACT_CLASSES
        and record.external_observation_present
        and record.measurement_method is not None
        and bool(record.provenance.strip())
        and bool(record.provenance_root.strip())
        and envelope.contains(record)
    )


def independent_support(a: RepresentationRecord, b: RepresentationRecord) -> bool:
    """Conservative ancestry check; distinct files do not imply independence."""
    if a.provenance_root == b.provenance_root:
        return False
    if a.generator_id is not None and a.generator_id == b.generator_id:
        return False
    return True


def assess_numeric_mismatch(
    model: RepresentationRecord,
    observation: RepresentationRecord,
    envelope: FidelityEnvelope,
    *,
    tolerance: Optional[float] = None,
) -> MismatchAssessment:
    """Compare a model-like record with a reality-contact record when commensurate."""
    if model.representation_class not in _MODEL_CLASSES:
        return MismatchAssessment(
            AssessmentStatus.UNKNOWN_GAP,
            "first record is not a model/simulation/counterfactual/twin/forecast state",
            None,
            tolerance,
            model.provenance,
            observation.provenance,
        )
    if not reality_contact(observation, envelope):
        return MismatchAssessment(
            AssessmentStatus.UNKNOWN_GAP,
            "observation lacks adequate reality contact inside the declared fidelity envelope",
            None,
            tolerance,
            model.provenance,
            observation.provenance,
        )
    comparable = (
        model.object_id == observation.object_id
        and model.variable == observation.variable
        and model.unit == observation.unit
        and model.time_id == observation.time_id
        and model.regime == observation.regime
    )
    if not comparable:
        return MismatchAssessment(
            AssessmentStatus.UNKNOWN_GAP,
            "model and observation coordinates are not commensurate",
            None,
            tolerance,
            model.provenance,
            observation.provenance,
        )
    if model.value is None or observation.value is None:
        return MismatchAssessment(
            AssessmentStatus.UNKNOWN_GAP,
            "numeric mismatch requires both values",
            None,
            tolerance,
            model.provenance,
            observation.provenance,
        )
    if tolerance is not None and tolerance < 0:
        raise ValueError("tolerance must be non-negative")

    error = abs(model.value - observation.value)
    if tolerance is None:
        status = AssessmentStatus.VERIFIED_BOUNDED
        reason = "absolute discrepancy computed over commensurate coordinates"
    elif error <= tolerance:
        status = AssessmentStatus.WITHIN_TOLERANCE
        reason = "absolute discrepancy is within the caller-declared tolerance"
    else:
        status = AssessmentStatus.EXCEEDS_TOLERANCE
        reason = "absolute discrepancy exceeds the caller-declared tolerance and remains first-class evidence"

    return MismatchAssessment(
        status,
        reason,
        error,
        tolerance,
        model.provenance,
        observation.provenance,
    )
