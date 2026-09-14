"""Bounded executable AMOS Cognitive Matrix registry and audit substrate.

Origin architect / steward: Trang Phan.

AMOS_MODEL reference implementation. This module does not promote canon or mint
external authority. It binds registry, evidence, authority, coverage threshold,
and audit semantics that were previously contract-only in 25_COGNITIVE_MATRIX.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, IntEnum
from math import isfinite
from typing import Dict, Iterable, Mapping, Optional, Tuple


class Maturity(IntEnum):
    PLACEHOLDER = 0
    SOURCE_BOUND = 1
    CONTRACT_COMPLETE = 2
    IMPLEMENTED = 3
    VALIDATED_BOUNDED = 4
    AUTHORIZED_BOUNDED = 5


class Condition(Enum):
    ACTIVE = "ACTIVE"
    STALE = "STALE"
    COMPETING = "COMPETING"
    QUARANTINED = "QUARANTINED"
    FALSIFIED = "FALSIFIED"


class EvidenceClass(Enum):
    SOURCE_CLAIM = "SOURCE_CLAIM"
    OBSERVATION = "OBSERVATION"
    DERIVED = "DERIVED"
    AMOS_MODEL = "AMOS_MODEL"
    EXECUTED_TEST = "EXECUTED_TEST"
    FORMAL_PROOF = "FORMAL_PROOF"


@dataclass(frozen=True)
class EvidenceRef:
    evidence_id: str
    evidence_class: EvidenceClass
    source_id: str
    state_version: str
    fresh: bool = True

    def __post_init__(self) -> None:
        for value, name in ((self.evidence_id, "evidence_id"), (self.source_id, "source_id"), (self.state_version, "state_version")):
            if not value.strip():
                raise ValueError(f"{name} must be non-empty")


@dataclass(frozen=True)
class AuthorityWitness:
    witness_id: str
    principal: str
    scope: Tuple[str, ...]
    policy_hash: str
    state_version: str
    fresh: bool = True

    def __post_init__(self) -> None:
        if not self.witness_id.strip() or not self.principal.strip():
            raise ValueError("authority witness identity must be explicit")
        if not self.policy_hash.strip() or not self.state_version.strip():
            raise ValueError("authority witness must bind policy and state version")

    def authorizes(self, required_scope: str, policy_hash: str, state_version: str) -> bool:
        return (
            self.fresh
            and required_scope in self.scope
            and self.policy_hash == policy_hash
            and self.state_version == state_version
        )


@dataclass(frozen=True)
class MatrixCellRecord:
    cell_id: str
    maturity: Maturity
    condition: Condition
    state_version: str
    source_ids: Tuple[str, ...] = ()
    evidence_ids: Tuple[str, ...] = ()
    authority_witness_id: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.cell_id.strip() or not self.state_version.strip():
            raise ValueError("cell_id and state_version must be non-empty")
        if len(set(self.source_ids)) != len(self.source_ids):
            raise ValueError("source_ids must be unique")
        if len(set(self.evidence_ids)) != len(self.evidence_ids):
            raise ValueError("evidence_ids must be unique")


class CellRegistry:
    """Exact-identity registry; same ID cannot silently change state version."""

    def __init__(self) -> None:
        self._cells: Dict[str, MatrixCellRecord] = {}

    def register(self, record: MatrixCellRecord) -> None:
        current = self._cells.get(record.cell_id)
        if current is not None and current != record:
            raise ValueError(f"cell {record.cell_id!r} already registered with different state")
        self._cells[record.cell_id] = record

    def get(self, cell_id: str) -> MatrixCellRecord:
        return self._cells[cell_id]

    def snapshot(self) -> Tuple[MatrixCellRecord, ...]:
        return tuple(self._cells[k] for k in sorted(self._cells))


class EvidenceRegistry:
    def __init__(self) -> None:
        self._evidence: Dict[str, EvidenceRef] = {}

    def register(self, ref: EvidenceRef) -> None:
        current = self._evidence.get(ref.evidence_id)
        if current is not None and current != ref:
            raise ValueError(f"evidence {ref.evidence_id!r} identity collision")
        self._evidence[ref.evidence_id] = ref

    def validate_cell_evidence(self, record: MatrixCellRecord) -> Tuple[bool, Tuple[str, ...]]:
        failures = []
        for evidence_id in record.evidence_ids:
            ref = self._evidence.get(evidence_id)
            if ref is None:
                failures.append(f"MISSING:{evidence_id}")
            elif ref.state_version != record.state_version:
                failures.append(f"STATE_VERSION_MISMATCH:{evidence_id}")
            elif not ref.fresh:
                failures.append(f"STALE:{evidence_id}")
        return not failures, tuple(failures)


@dataclass(frozen=True)
class CoverageVector:
    address: float
    source: float
    contract: float
    implementation: float
    validation: float
    authority: float

    def __post_init__(self) -> None:
        for value in self.as_tuple():
            if not isfinite(value) or not 0.0 <= value <= 1.0:
                raise ValueError("coverage values must be finite and in [0,1]")

    def as_tuple(self) -> Tuple[float, ...]:
        return (self.address, self.source, self.contract, self.implementation, self.validation, self.authority)


@dataclass(frozen=True)
class CoverageThresholds:
    source: float = 1.0
    contract: float = 1.0
    implementation: float = 1.0
    validation: float = 1.0
    authority: float = 1.0

    def __post_init__(self) -> None:
        for value in (self.source, self.contract, self.implementation, self.validation, self.authority):
            if not isfinite(value) or not 0.0 <= value <= 1.0:
                raise ValueError("thresholds must be finite and in [0,1]")


class AuditStatus(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    INCOMPLETE = "INCOMPLETE"


@dataclass(frozen=True)
class CoverageAudit:
    status: AuditStatus
    failed_dimensions: Tuple[str, ...]
    coverage: CoverageVector


def compute_coverage(records: Iterable[MatrixCellRecord]) -> CoverageVector:
    items = tuple(records)
    if not items:
        return CoverageVector(0, 0, 0, 0, 0, 0)
    n = float(len(items))
    def ratio(level: Maturity) -> float:
        return sum(r.maturity >= level for r in items) / n
    return CoverageVector(
        address=1.0,
        source=ratio(Maturity.SOURCE_BOUND),
        contract=ratio(Maturity.CONTRACT_COMPLETE),
        implementation=ratio(Maturity.IMPLEMENTED),
        validation=ratio(Maturity.VALIDATED_BOUNDED),
        authority=ratio(Maturity.AUTHORIZED_BOUNDED),
    )


def audit_coverage(coverage: CoverageVector, thresholds: CoverageThresholds) -> CoverageAudit:
    failed = []
    for name in ("source", "contract", "implementation", "validation", "authority"):
        if getattr(coverage, name) < getattr(thresholds, name):
            failed.append(name)
    status = AuditStatus.PASS if not failed else AuditStatus.INCOMPLETE
    return CoverageAudit(status, tuple(failed), coverage)


def validate_authority_binding(
    record: MatrixCellRecord,
    witnesses: Mapping[str, AuthorityWitness],
    required_scope: str,
    policy_hash: str,
) -> Tuple[bool, str]:
    if record.maturity < Maturity.AUTHORIZED_BOUNDED:
        return False, "CELL_NOT_AUTHORIZED_BOUNDED"
    if not record.authority_witness_id:
        return False, "MISSING_AUTHORITY_WITNESS"
    witness = witnesses.get(record.authority_witness_id)
    if witness is None:
        return False, "UNKNOWN_AUTHORITY_WITNESS"
    if not witness.authorizes(required_scope, policy_hash, record.state_version):
        return False, "AUTHORITY_SCOPE_POLICY_OR_FRESHNESS_MISMATCH"
    return True, "AUTHORIZED_BOUNDED"
