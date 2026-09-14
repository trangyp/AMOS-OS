"""Executable bindings for remaining load-bearing Cognitive Matrix contracts.

Origin architect / steward: Trang Phan.

AMOS_MODEL bounded implementation for:
- CELL_BINDINGS;
- CELL_STATUS_REGISTRY projection;
- GAP_REGISTRY;
- GAP_PROMOTION / closure;
- dependency audit projection;
- invalidation audit projection.

This module does not promote canon or mint effect authority.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Dict, Mapping, Optional, Tuple

from cognitive_matrix_runtime import (
    Condition,
    DependencyGraph,
    GapKind,
    GapSignal,
    Maturity,
)
from matrix_registry_runtime import MatrixCellRecord


@dataclass(frozen=True)
class CellBinding:
    cell_id: str
    state_version: str
    source_ids: Tuple[str, ...] = ()
    evidence_ids: Tuple[str, ...] = ()
    authority_witness_id: Optional[str] = None
    dependency_ids: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.cell_id.strip() or not self.state_version.strip():
            raise ValueError("cell binding identity and state_version must be non-empty")
        for name, values in (
            ("source_ids", self.source_ids),
            ("evidence_ids", self.evidence_ids),
            ("dependency_ids", self.dependency_ids),
        ):
            if len(set(values)) != len(values):
                raise ValueError(f"{name} must be unique")
        if self.cell_id in self.dependency_ids:
            raise ValueError("cell cannot depend on itself")


class CellBindingRegistry:
    def __init__(self) -> None:
        self._bindings: Dict[str, CellBinding] = {}

    def register(self, binding: CellBinding) -> None:
        current = self._bindings.get(binding.cell_id)
        if current is not None and current != binding:
            raise ValueError(f"binding collision for {binding.cell_id!r}")
        self._bindings[binding.cell_id] = binding

    def get(self, cell_id: str) -> CellBinding:
        return self._bindings[cell_id]

    def validate_against_cell(self, binding: CellBinding, cell: MatrixCellRecord) -> Tuple[str, ...]:
        failures = []
        if binding.cell_id != cell.cell_id:
            failures.append("CELL_ID_MISMATCH")
        if binding.state_version != cell.state_version:
            failures.append("STATE_VERSION_MISMATCH")
        if binding.source_ids != cell.source_ids:
            failures.append("SOURCE_BINDING_MISMATCH")
        if binding.evidence_ids != cell.evidence_ids:
            failures.append("EVIDENCE_BINDING_MISMATCH")
        if binding.authority_witness_id != cell.authority_witness_id:
            failures.append("AUTHORITY_BINDING_MISMATCH")
        return tuple(failures)


@dataclass(frozen=True)
class CellStatus:
    cell_id: str
    state_version: str
    maturity: Maturity
    condition: Condition


def project_cell_status(cell: MatrixCellRecord) -> CellStatus:
    return CellStatus(
        cell_id=cell.cell_id,
        state_version=cell.state_version,
        maturity=Maturity(int(cell.maturity)),
        condition=Condition(cell.condition.value),
    )


class GapState(Enum):
    OPEN = "OPEN"
    RESOLUTION_PROPOSED = "RESOLUTION_PROPOSED"
    CLOSED = "CLOSED"


@dataclass(frozen=True)
class GapRecord:
    signal: GapSignal
    state_version: str
    state: GapState = GapState.OPEN
    resolution_evidence_id: Optional[str] = None
    revalidation_receipt_id: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.state_version.strip():
            raise ValueError("gap state_version must be non-empty")
        if self.state is GapState.OPEN and (
            self.resolution_evidence_id is not None or self.revalidation_receipt_id is not None
        ):
            raise ValueError("open gap cannot carry closure receipts")
        if self.state is GapState.RESOLUTION_PROPOSED and not self.resolution_evidence_id:
            raise ValueError("resolution proposal requires evidence identity")
        if self.state is GapState.CLOSED and (
            not self.resolution_evidence_id or not self.revalidation_receipt_id
        ):
            raise ValueError("closed gap requires resolution and revalidation receipts")


class GapRegistry:
    def __init__(self) -> None:
        self._records: Dict[str, GapRecord] = {}

    def register(self, record: GapRecord) -> None:
        gap_id = record.signal.gap_id
        current = self._records.get(gap_id)
        if current is not None and current != record:
            raise ValueError(f"gap identity collision for {gap_id!r}")
        self._records[gap_id] = record

    def get(self, gap_id: str) -> GapRecord:
        return self._records[gap_id]

    def replace(self, record: GapRecord) -> None:
        gap_id = record.signal.gap_id
        if gap_id not in self._records:
            raise KeyError(gap_id)
        current = self._records[gap_id]
        legal = {
            (GapState.OPEN, GapState.RESOLUTION_PROPOSED),
            (GapState.RESOLUTION_PROPOSED, GapState.CLOSED),
        }
        if (current.state, record.state) not in legal:
            raise ValueError(f"illegal gap transition {current.state.value}->{record.state.value}")
        if current.state_version != record.state_version:
            raise ValueError("gap state_version cannot silently change during closure")
        self._records[gap_id] = record


@dataclass(frozen=True)
class GapResolutionEvidence:
    evidence_id: str
    gap_id: str
    state_version: str
    source_resolved: bool = False
    semantics_typed: bool = False
    implementation_receipt: bool = False
    tests_executed: bool = False
    adversarial_tests_executed: bool = False
    authority_witness: bool = False
    dependency_audit_passed: bool = False
    dependencies_fresh: bool = False
    contradiction_resolved: bool = False

    def __post_init__(self) -> None:
        if not self.evidence_id.strip() or not self.gap_id.strip() or not self.state_version.strip():
            raise ValueError("resolution evidence identity must be explicit")


_REQUIREMENTS: Mapping[GapKind, Tuple[str, ...]] = {
    GapKind.SOURCE: ("source_resolved",),
    GapKind.SEMANTICS: ("semantics_typed",),
    GapKind.IMPLEMENTATION: ("implementation_receipt",),
    GapKind.VALIDATION: ("tests_executed", "adversarial_tests_executed"),
    GapKind.AUTHORITY: ("authority_witness",),
    GapKind.DEPENDENCY_CYCLE: ("dependency_audit_passed",),
    GapKind.STALENESS: ("dependencies_fresh",),
    GapKind.CONTRADICTION: ("contradiction_resolved",),
}


def propose_gap_resolution(record: GapRecord, evidence: GapResolutionEvidence) -> GapRecord:
    if record.state is not GapState.OPEN:
        raise ValueError("only OPEN gaps may receive a resolution proposal")
    if evidence.gap_id != record.signal.gap_id:
        raise ValueError("resolution evidence bound to different gap")
    if evidence.state_version != record.state_version:
        raise ValueError("resolution evidence state_version mismatch")
    missing = tuple(name for name in _REQUIREMENTS[record.signal.kind] if not getattr(evidence, name))
    if missing:
        raise ValueError(f"resolution evidence missing: {', '.join(missing)}")
    return replace(
        record,
        state=GapState.RESOLUTION_PROPOSED,
        resolution_evidence_id=evidence.evidence_id,
    )


@dataclass(frozen=True)
class RevalidationReceipt:
    receipt_id: str
    gap_id: str
    state_version: str
    revalidation_passed: bool
    dependencies_fresh: bool

    def __post_init__(self) -> None:
        if not self.receipt_id.strip() or not self.gap_id.strip() or not self.state_version.strip():
            raise ValueError("revalidation receipt identity must be explicit")


def close_gap(record: GapRecord, receipt: RevalidationReceipt) -> GapRecord:
    if record.state is not GapState.RESOLUTION_PROPOSED:
        raise ValueError("gap must have a resolution proposal before closure")
    if receipt.gap_id != record.signal.gap_id:
        raise ValueError("revalidation receipt bound to different gap")
    if receipt.state_version != record.state_version:
        raise ValueError("revalidation receipt state_version mismatch")
    if not receipt.revalidation_passed:
        raise ValueError("revalidation did not pass")
    if not receipt.dependencies_fresh:
        raise ValueError("dependencies are stale")
    return replace(
        record,
        state=GapState.CLOSED,
        revalidation_receipt_id=receipt.receipt_id,
    )


@dataclass(frozen=True)
class DependencyAuditResult:
    load_bearing_cycles: Tuple[Tuple[str, ...], ...]
    topological_order: Optional[Tuple[str, ...]]
    acyclic: bool


def audit_dependencies(graph: DependencyGraph) -> DependencyAuditResult:
    cycles = graph.load_bearing_cycles()
    if cycles:
        return DependencyAuditResult(cycles, None, False)
    return DependencyAuditResult((), graph.topological_order(), True)


def audit_selective_invalidation(
    graph: DependencyGraph,
    records: Mapping[str, object],
    invalidated_id: str,
) -> Tuple[object, Mapping[str, object]]:
    """Execute graph invalidation and return the root plus updated mapping.

    Delegates semantics to DependencyGraph.selective_invalidate; this wrapper exists
    so the contract surface can be bound without inventing a second invalidation law.
    """
    updated = graph.selective_invalidate(records, invalidated_id)  # type: ignore[arg-type]
    return updated[invalidated_id], updated
