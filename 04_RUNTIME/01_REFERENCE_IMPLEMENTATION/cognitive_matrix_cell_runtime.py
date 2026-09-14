"""Bounded typed cell contract for the AMOS Cognitive Matrix.

Origin architect / steward: Trang Phan.

This reference runtime centralizes cell state, evidence ancestry, typed axes,
semantic/runtime ownership, and authority separation. It validates cell objects;
it does not itself commit durable effects or promote canon.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional, Tuple


class CellStatus(Enum):
    UNBOUND = "UNBOUND"
    SOURCE_CLAIM = "SOURCE_CLAIM"
    AMOS_MODEL = "AMOS_MODEL"
    DERIVED = "DERIVED"
    VERIFIED_BOUNDED = "VERIFIED_BOUNDED"
    COMPETING = "COMPETING"
    FALSIFIED = "FALSIFIED"
    STALE = "STALE"
    QUARANTINED = "QUARANTINED"


class EvidenceClass(Enum):
    SOURCE = "SOURCE"
    OBSERVATION = "OBSERVATION"
    EXECUTION = "EXECUTION"
    FORMAL_PROOF = "FORMAL_PROOF"
    MODEL = "MODEL"
    DERIVED = "DERIVED"


@dataclass(frozen=True)
class CellCoordinate:
    primitive: str
    field: str
    context: str
    time_id: str
    scale: str
    observer: str
    regime: str

    def __post_init__(self) -> None:
        for name in ("primitive", "field", "context", "time_id", "scale", "observer", "regime"):
            if not getattr(self, name).strip():
                raise ValueError(f"cell axis {name} must be explicit")


@dataclass(frozen=True)
class CellEvidence:
    evidence_id: str
    evidence_class: EvidenceClass
    provenance: str
    provenance_root: str
    source_version: str
    fresh: bool = True
    execution_receipt: bool = False
    formal_proof_receipt: bool = False

    def __post_init__(self) -> None:
        for name in ("evidence_id", "provenance", "provenance_root", "source_version"):
            if not getattr(self, name).strip():
                raise ValueError(f"evidence field {name} must be explicit")


@dataclass(frozen=True)
class CellBinding:
    cell_id: str
    semantic_owner: str
    runtime_owner: Optional[str]
    authority_owner: Optional[str]

    def __post_init__(self) -> None:
        if not self.cell_id.strip() or not self.semantic_owner.strip():
            raise ValueError("cell_id and semantic_owner must be explicit")
        if self.runtime_owner is not None and not self.runtime_owner.strip():
            raise ValueError("runtime_owner must be non-empty when supplied")
        if self.authority_owner is not None and not self.authority_owner.strip():
            raise ValueError("authority_owner must be non-empty when supplied")

    @property
    def has_runtime_capability(self) -> bool:
        return self.runtime_owner is not None

    @property
    def has_effect_authority_binding(self) -> bool:
        return self.authority_owner is not None


@dataclass(frozen=True)
class CellRecord:
    cell_id: str
    coordinate: CellCoordinate
    status: CellStatus
    value: Any
    unit: Optional[str]
    provenance: Optional[str]
    source_version: Optional[str]
    evidence: Tuple[CellEvidence, ...] = ()
    dependencies: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.cell_id.strip():
            raise ValueError("cell_id must be explicit")
        if self.unit is not None and not self.unit.strip():
            raise ValueError("unit must be non-empty when supplied")
        for dep in self.dependencies:
            if not dep.strip():
                raise ValueError("dependency IDs must be non-empty")


@dataclass(frozen=True)
class CellValidation:
    valid: bool
    errors: Tuple[str, ...]
    independent_provenance_roots: int
    effect_authority_bound: bool


def independent_provenance_roots(evidence: Tuple[CellEvidence, ...]) -> int:
    return len({item.provenance_root for item in evidence})


def validate_cell(record: CellRecord, binding: CellBinding) -> CellValidation:
    errors = []

    if binding.cell_id != record.cell_id:
        errors.append("CELL_BINDING_ID_MISMATCH")

    if record.status is CellStatus.UNBOUND:
        if record.value is not None:
            errors.append("UNBOUND_MUST_NOT_CARRY_VALUE")
        if record.provenance is not None or record.source_version is not None:
            errors.append("UNBOUND_MUST_NOT_FAKE_SOURCE_BINDING")
    else:
        if record.provenance is None or not record.provenance.strip():
            errors.append("BOUND_CELL_REQUIRES_PROVENANCE")
        if record.source_version is None or not record.source_version.strip():
            errors.append("BOUND_CELL_REQUIRES_SOURCE_VERSION")

    if record.status is CellStatus.VERIFIED_BOUNDED:
        has_receipt = any(
            item.execution_receipt or item.formal_proof_receipt
            for item in record.evidence
            if item.fresh
        )
        if not has_receipt:
            errors.append("VERIFIED_BOUNDED_REQUIRES_FRESH_RECEIPT")

    if record.status is CellStatus.COMPETING:
        if independent_provenance_roots(record.evidence) < 2:
            errors.append("COMPETING_REQUIRES_AT_LEAST_TWO_PROVENANCE_ROOTS")

    if record.status not in {CellStatus.STALE, CellStatus.QUARANTINED, CellStatus.UNBOUND}:
        if any(not item.fresh for item in record.evidence):
            errors.append("ACTIVE_CELL_CARRIES_STALE_EVIDENCE")

    return CellValidation(
        valid=not errors,
        errors=tuple(errors),
        independent_provenance_roots=independent_provenance_roots(record.evidence),
        effect_authority_bound=binding.has_effect_authority_binding,
    )


@dataclass(frozen=True)
class TransformContract:
    source_regime: str
    target_regime: str
    preserves_provenance: bool
    explicit_regime_mapping: bool
    unknown_to_zero: bool = False

    def __post_init__(self) -> None:
        if not self.source_regime.strip() or not self.target_regime.strip():
            raise ValueError("transform regimes must be explicit")


def validate_transform(contract: TransformContract) -> Tuple[str, ...]:
    errors = []
    if not contract.preserves_provenance:
        errors.append("TRANSFORM_ERASES_PROVENANCE")
    if contract.source_regime != contract.target_regime and not contract.explicit_regime_mapping:
        errors.append("CROSS_REGIME_MAPPING_UNDECLARED")
    if contract.unknown_to_zero:
        errors.append("UNKNOWN_TO_ZERO_FORBIDDEN")
    return tuple(errors)
