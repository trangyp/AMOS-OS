"""Bounded executable C05 Representation control-plane runtime.

Origin architect / steward: Trang Phan.

AMOS_MODEL reference implementation. C05 validates an explicitly declared
representation transform and its information-loss boundary. Translation is not
assumed to be equivalence and never upgrades epistemic class.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Tuple


class EpistemicLevel(IntEnum):
    UNKNOWN_GAP = 0
    OBSERVATION = 1
    SOURCE_CLAIM = 2
    DERIVED = 3
    VERIFIED = 4


class RepresentationStatus(Enum):
    TRANSFORM_BOUNDED = "TRANSFORM_BOUNDED"
    HOLD_UNKNOWN = "HOLD_UNKNOWN"
    BLOCK_SCHEMA = "BLOCK_SCHEMA"
    BLOCK_SCOPE = "BLOCK_SCOPE"
    BLOCK_REGIME = "BLOCK_REGIME"
    BLOCK_OBSERVER = "BLOCK_OBSERVER"
    BLOCK_EPISTEMIC_UPGRADE = "BLOCK_EPISTEMIC_UPGRADE"
    BLOCK_DECISION_LOSS = "BLOCK_DECISION_LOSS"


@dataclass(frozen=True)
class RepresentationTransform:
    transform_id: str
    source_type: str
    target_type: str
    map_type: str
    scope: str
    regime: str
    observer: str
    source_schema_hash: str
    expected_source_schema_hash: str
    target_schema_hash: str
    expected_target_schema_hash: str
    source_epistemic: EpistemicLevel
    target_epistemic: EpistemicLevel
    preserved_features: Tuple[str, ...]
    lost_features: Tuple[str, ...]
    decision_required_features: Tuple[str, ...]
    provenance_ids: Tuple[str, ...]
    unknown_gaps: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for value, name in (
            (self.transform_id, "transform_id"),
            (self.source_type, "source_type"),
            (self.target_type, "target_type"),
            (self.map_type, "map_type"),
            (self.scope, "scope"),
            (self.regime, "regime"),
            (self.observer, "observer"),
            (self.source_schema_hash, "source_schema_hash"),
            (self.expected_source_schema_hash, "expected_source_schema_hash"),
            (self.target_schema_hash, "target_schema_hash"),
            (self.expected_target_schema_hash, "expected_target_schema_hash"),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        if not isinstance(self.source_epistemic, EpistemicLevel) or not isinstance(self.target_epistemic, EpistemicLevel):
            raise ValueError("epistemic levels must be EpistemicLevel")
        for values, name in (
            (self.preserved_features, "preserved_features"),
            (self.lost_features, "lost_features"),
            (self.decision_required_features, "decision_required_features"),
            (self.provenance_ids, "provenance_ids"),
            (self.unknown_gaps, "unknown_gaps"),
        ):
            if len(set(values)) != len(values):
                raise ValueError(f"{name} must be unique")
            if any(not isinstance(v, str) or not v.strip() for v in values):
                raise ValueError(f"{name} entries must be non-empty strings")
        if not self.provenance_ids:
            raise ValueError("representation output requires provenance")
        if set(self.preserved_features) & set(self.lost_features):
            raise ValueError("a feature cannot be both preserved and lost")


@dataclass(frozen=True)
class RepresentationResult:
    status: RepresentationStatus
    transform_id: str
    residual_features: Tuple[str, ...]
    provenance_ids: Tuple[str, ...]
    equivalent: bool
    reasons: Tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.reasons:
            raise ValueError("representation result requires reasons")
        if self.equivalent and self.residual_features:
            raise ValueError("equivalent result cannot have declared residual loss")
        if self.status is not RepresentationStatus.TRANSFORM_BOUNDED and self.equivalent:
            raise ValueError("blocked/held transform cannot claim equivalence")


def evaluate_representation(transform: RepresentationTransform) -> RepresentationResult:
    if transform.unknown_gaps:
        return RepresentationResult(
            RepresentationStatus.HOLD_UNKNOWN,
            transform.transform_id,
            tuple(sorted(set(transform.lost_features) | set(transform.unknown_gaps))),
            transform.provenance_ids,
            False,
            ("UNKNOWN_GAP_PRESENT",),
        )
    if transform.source_schema_hash != transform.expected_source_schema_hash or transform.target_schema_hash != transform.expected_target_schema_hash:
        return RepresentationResult(RepresentationStatus.BLOCK_SCHEMA, transform.transform_id, transform.lost_features,
                                    transform.provenance_ids, False, ("SCHEMA_FINGERPRINT_MISMATCH",))
    if transform.scope == "UNRESOLVED":
        return RepresentationResult(RepresentationStatus.BLOCK_SCOPE, transform.transform_id, transform.lost_features,
                                    transform.provenance_ids, False, ("SCOPE_UNRESOLVED",))
    if transform.regime == "UNRESOLVED":
        return RepresentationResult(RepresentationStatus.BLOCK_REGIME, transform.transform_id, transform.lost_features,
                                    transform.provenance_ids, False, ("REGIME_UNRESOLVED",))
    if transform.observer == "UNRESOLVED":
        return RepresentationResult(RepresentationStatus.BLOCK_OBSERVER, transform.transform_id, transform.lost_features,
                                    transform.provenance_ids, False, ("OBSERVER_UNRESOLVED",))
    if transform.target_epistemic > transform.source_epistemic:
        return RepresentationResult(RepresentationStatus.BLOCK_EPISTEMIC_UPGRADE, transform.transform_id,
                                    transform.lost_features, transform.provenance_ids, False,
                                    ("REPRESENTATION_TRANSFORM_CANNOT_UPGRADE_EPISTEMIC_CLASS",))

    residual = tuple(sorted(set(transform.lost_features)))
    load_bearing_loss = tuple(sorted(set(transform.decision_required_features) & set(residual)))
    if load_bearing_loss:
        return RepresentationResult(
            RepresentationStatus.BLOCK_DECISION_LOSS,
            transform.transform_id,
            residual,
            transform.provenance_ids,
            False,
            ("DECISION_REQUIRED_STRUCTURE_LOST", *load_bearing_loss),
        )

    equivalent = not residual and set(transform.decision_required_features).issubset(set(transform.preserved_features))
    return RepresentationResult(
        RepresentationStatus.TRANSFORM_BOUNDED,
        transform.transform_id,
        residual,
        transform.provenance_ids,
        equivalent,
        (
            "DECLARED_REPRESENTATION_GATES_SATISFIED",
            "TRANSLATION_IS_NOT_EQUIVALENCE_UNLESS_REQUIRED_STRUCTURE_IS_PRESERVED_AND_RESIDUAL_IS_EMPTY",
        ),
    )
