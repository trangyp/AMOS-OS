"""Bounded H/M/L scale contract for the AMOS Cognitive Matrix.

Origin architect / steward: Trang Phan.

The scale axis is typed and non-interchangeable. Similarity across H/M/L does not
establish equivalence, causation, mechanism identity, or a valid scale transform.
Cross-scale projection is admitted only with an explicit transform identity,
assumptions, invariant witnesses, provenance, and a bounded validation receipt.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Scale(Enum):
    H_HIGH = "H_HIGH_SCALE"
    M_MID = "M_MID_SCALE"
    L_LOW = "L_LOW_SCALE"


@dataclass(frozen=True)
class ScaleArtifact:
    artifact_id: str
    scale: Scale
    state_version: str
    scope: str
    regime: str
    provenance_ids: Tuple[str, ...]

    def __post_init__(self) -> None:
        for name, value in (
            ("artifact_id", self.artifact_id),
            ("state_version", self.state_version),
            ("scope", self.scope),
            ("regime", self.regime),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be explicit and non-empty")
        if not self.provenance_ids or any(not item.strip() for item in self.provenance_ids):
            raise ValueError("scale artifact requires non-empty provenance ids")
        if len(set(self.provenance_ids)) != len(self.provenance_ids):
            raise ValueError("provenance ids must be unique")


@dataclass(frozen=True)
class ScaleTransform:
    transform_id: str
    source_scale: Scale
    target_scale: Scale
    assumption_ids: Tuple[str, ...]
    invariant_ids: Tuple[str, ...]
    provenance_ids: Tuple[str, ...]
    validation_receipt_id: str

    def __post_init__(self) -> None:
        if self.source_scale is self.target_scale:
            raise ValueError("cross-scale transform requires different source and target scales")
        if not self.transform_id.strip() or not self.validation_receipt_id.strip():
            raise ValueError("transform and validation receipt identities must be explicit")
        for name, values in (
            ("assumption_ids", self.assumption_ids),
            ("invariant_ids", self.invariant_ids),
            ("provenance_ids", self.provenance_ids),
        ):
            if not values or any(not item.strip() for item in values):
                raise ValueError(f"{name} must contain non-empty identities")
            if len(set(values)) != len(values):
                raise ValueError(f"{name} must be unique")


@dataclass(frozen=True)
class ScaleTransformReceipt:
    transform_id: str
    source_scale: Scale
    target_scale: Scale
    structurally_bound: bool
    semantic_equivalence_proven: bool = False
    causal_equivalence_proven: bool = False
    conclusion_class: str = "AMOS_MODEL/BOUNDED_TRANSFORM_CONTRACT"


def validate_scale_transform(transform: ScaleTransform) -> ScaleTransformReceipt:
    """Validate scale-transform evidence shape without inventing equivalence."""
    return ScaleTransformReceipt(
        transform_id=transform.transform_id,
        source_scale=transform.source_scale,
        target_scale=transform.target_scale,
        structurally_bound=True,
        semantic_equivalence_proven=False,
        causal_equivalence_proven=False,
    )


def validate_scale_registry() -> Tuple[str, ...]:
    failures = []
    if len(Scale) != 3:
        failures.append("HML_SCALE_COUNT")
    if len({scale.value for scale in Scale}) != 3:
        failures.append("HML_SCALE_IDENTITY")
    return tuple(failures)
