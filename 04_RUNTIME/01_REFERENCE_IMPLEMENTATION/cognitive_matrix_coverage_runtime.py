"""Bounded structural coverage/gap accounting for the AMOS Cognitive Matrix.

Origin architect / steward: Trang Phan.
Dependency edges mean "requires" only; they are not causal edges.
This runtime evaluates scoped structural completeness, not truth, Canon, or authority.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


class CompletionStatus(Enum):
    COMPLETE_FOR_SCOPE = "COMPLETE_FOR_SCOPE"
    CONDITIONAL = "CONDITIONAL"
    INCOMPLETE = "INCOMPLETE"
    CONTRADICTORY = "CONTRADICTORY"
    UNKNOWN_GAP = "UNKNOWN/GAP"


class ArtifactKind(Enum):
    CELL = "CELL"
    INTERFACE = "INTERFACE"
    DEPENDENCY = "DEPENDENCY"
    FAILURE_PATH = "FAILURE_PATH"
    RUNTIME = "RUNTIME"
    VALIDATOR = "VALIDATOR"
    GOVERNANCE = "GOVERNANCE"
    DOCUMENTATION = "DOCUMENTATION"


class CoverageStage(Enum):
    UNBOUND = "UNBOUND"
    CONTRACT_ONLY = "CONTRACT_ONLY"
    IMPLEMENTED_BOUNDED = "IMPLEMENTED_BOUNDED"
    VALIDATED_BOUNDED = "VALIDATED_BOUNDED"
    GOVERNED_BOUNDED = "GOVERNED_BOUNDED"
    STALE = "STALE"
    COMPETING = "COMPETING"
    FALSIFIED = "FALSIFIED"
    QUARANTINED = "QUARANTINED"


class Criticality(Enum):
    CRITICAL = "CRITICAL"
    DECISION_RELEVANT = "DECISION_RELEVANT"
    EXPLANATORY = "EXPLANATORY"
    COSMETIC = "COSMETIC"


class GapReason(Enum):
    MISSING = "MISSING"
    BELOW_REQUIRED_STAGE = "BELOW_REQUIRED_STAGE"
    DEPENDENCY_GAP = "DEPENDENCY_GAP"
    UNDECLARED_DEPENDENCY = "UNDECLARED_DEPENDENCY"
    INVALID_RECORD = "INVALID_RECORD"
    DUPLICATE_RECORD = "DUPLICATE_RECORD"
    CYCLE = "CYCLE"
    STALE = "STALE"
    COMPETING = "COMPETING"
    FALSIFIED = "FALSIFIED"
    QUARANTINED = "QUARANTINED"
    UNBOUND = "UNBOUND"


_STAGE_RANK = {
    CoverageStage.CONTRACT_ONLY: 1,
    CoverageStage.IMPLEMENTED_BOUNDED: 2,
    CoverageStage.VALIDATED_BOUNDED: 3,
    CoverageStage.GOVERNED_BOUNDED: 4,
}
_CRIT_RANK = {
    Criticality.COSMETIC: 1,
    Criticality.EXPLANATORY: 2,
    Criticality.DECISION_RELEVANT: 3,
    Criticality.CRITICAL: 4,
}
_REASON_RANK = {
    GapReason.FALSIFIED: 12,
    GapReason.CYCLE: 11,
    GapReason.DUPLICATE_RECORD: 10,
    GapReason.UNDECLARED_DEPENDENCY: 9,
    GapReason.DEPENDENCY_GAP: 8,
    GapReason.MISSING: 7,
    GapReason.INVALID_RECORD: 6,
    GapReason.STALE: 5,
    GapReason.COMPETING: 4,
    GapReason.QUARANTINED: 3,
    GapReason.UNBOUND: 2,
    GapReason.BELOW_REQUIRED_STAGE: 1,
}
_UNKNOWN_REASONS = {
    GapReason.CYCLE,
    GapReason.DUPLICATE_RECORD,
    GapReason.UNDECLARED_DEPENDENCY,
    GapReason.INVALID_RECORD,
    GapReason.STALE,
    GapReason.COMPETING,
    GapReason.QUARANTINED,
}
_SPECIAL_REASON = {
    CoverageStage.UNBOUND: GapReason.UNBOUND,
    CoverageStage.STALE: GapReason.STALE,
    CoverageStage.COMPETING: GapReason.COMPETING,
    CoverageStage.FALSIFIED: GapReason.FALSIFIED,
    CoverageStage.QUARANTINED: GapReason.QUARANTINED,
}


@dataclass(frozen=True)
class ScopeRequirement:
    requirement_id: str
    kind: ArtifactKind
    required_stage: CoverageStage
    criticality: Criticality = Criticality.DECISION_RELEVANT
    dependencies: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.requirement_id.strip():
            raise ValueError("requirement_id must be explicit")
        if self.required_stage not in _STAGE_RANK:
            raise ValueError("required_stage must be an active coverage stage")
        if any(not dep.strip() for dep in self.dependencies):
            raise ValueError("dependency IDs must be non-empty")


@dataclass(frozen=True)
class CoverageScope:
    scope_id: str
    regime: str
    source_version: str
    requirements: Tuple[ScopeRequirement, ...]

    def __post_init__(self) -> None:
        if any(not value.strip() for value in (self.scope_id, self.regime, self.source_version)):
            raise ValueError("scope_id, regime, and source_version must be explicit")
        ids = [r.requirement_id for r in self.requirements]
        if len(ids) != len(set(ids)):
            raise ValueError("scope requirement IDs must be unique")


@dataclass(frozen=True)
class CoverageRecord:
    requirement_id: str
    stage: CoverageStage
    provenance: Optional[str]
    source_version: Optional[str]
    implementation_receipt: bool = False
    validation_receipt: bool = False
    governance_receipt: bool = False

    def __post_init__(self) -> None:
        if not self.requirement_id.strip():
            raise ValueError("requirement_id must be explicit")
        if self.provenance is not None and not self.provenance.strip():
            raise ValueError("provenance must be non-empty when supplied")
        if self.source_version is not None and not self.source_version.strip():
            raise ValueError("source_version must be non-empty when supplied")


@dataclass(frozen=True)
class RecordValidation:
    valid: bool
    errors: Tuple[str, ...]


@dataclass(frozen=True)
class DependencyTopology:
    ordered_ids: Tuple[str, ...]
    adjacency: Tuple[Tuple[int, ...], ...]
    closure: Tuple[Tuple[int, ...], ...]
    cycle_nodes: Tuple[str, ...]

    def downstream_fanout(self, requirement_id: str) -> int:
        j = self.ordered_ids.index(requirement_id)
        return sum(self.closure[i][j] for i in range(len(self.ordered_ids)) if i != j)


@dataclass(frozen=True)
class Gap:
    requirement_id: str
    reason: GapReason
    criticality: Criticality
    required_stage: CoverageStage
    current_stage: Optional[CoverageStage]
    downstream_fanout: int
    detail: str


@dataclass(frozen=True)
class CoverageEvaluation:
    status: CompletionStatus
    scope_id: str
    topology: DependencyTopology
    gaps: Tuple[Gap, ...]
    satisfied_requirements: Tuple[str, ...]
    required_count: int
    satisfied_count: int


@dataclass(frozen=True)
class PromotionResult:
    allowed: bool
    record: CoverageRecord
    errors: Tuple[str, ...]


def validate_record(record: CoverageRecord) -> RecordValidation:
    errors: List[str] = []
    if record.stage is CoverageStage.UNBOUND:
        if record.provenance is not None or record.source_version is not None:
            errors.append("UNBOUND_MUST_NOT_FAKE_SOURCE_BINDING")
        if record.implementation_receipt or record.validation_receipt or record.governance_receipt:
            errors.append("UNBOUND_MUST_NOT_CARRY_PROMOTION_RECEIPTS")
        return RecordValidation(not errors, tuple(errors))
    if record.provenance is None:
        errors.append("BOUND_RECORD_REQUIRES_PROVENANCE")
    if record.source_version is None:
        errors.append("BOUND_RECORD_REQUIRES_SOURCE_VERSION")
    if record.stage in _STAGE_RANK:
        rank = _STAGE_RANK[record.stage]
        if rank >= 2 and not record.implementation_receipt:
            errors.append("IMPLEMENTED_STAGE_REQUIRES_IMPLEMENTATION_RECEIPT")
        if rank >= 3 and not record.validation_receipt:
            errors.append("VALIDATED_STAGE_REQUIRES_VALIDATION_RECEIPT")
        if rank >= 4 and not record.governance_receipt:
            errors.append("GOVERNED_STAGE_REQUIRES_GOVERNANCE_RECEIPT")
    return RecordValidation(not errors, tuple(errors))


def build_dependency_topology(requirements: Sequence[ScopeRequirement]) -> DependencyTopology:
    ids = tuple(r.requirement_id for r in requirements)
    index = {rid: i for i, rid in enumerate(ids)}
    n = len(ids)
    adjacency = [[0] * n for _ in range(n)]
    for req in requirements:
        i = index[req.requirement_id]
        for dep in req.dependencies:
            if dep in index:
                adjacency[i][index[dep]] = 1
    closure = [row[:] for row in adjacency]
    for k in range(n):
        for i in range(n):
            if closure[i][k]:
                for j in range(n):
                    closure[i][j] = int(bool(closure[i][j] or closure[k][j]))
    cycles = tuple(ids[i] for i in range(n) if closure[i][i])
    return DependencyTopology(ids, tuple(map(tuple, adjacency)), tuple(map(tuple, closure)), cycles)


def prioritize_gaps(gaps: Iterable[Gap]) -> Tuple[Gap, ...]:
    """Lexicographic structural triage; not a causal or utility score."""
    return tuple(sorted(gaps, key=lambda g: (
        -_CRIT_RANK[g.criticality], -g.downstream_fanout,
        -_REASON_RANK[g.reason], g.requirement_id,
    )))


def evaluate_coverage(scope: CoverageScope, records: Iterable[CoverageRecord]) -> CoverageEvaluation:
    reqs = {r.requirement_id: r for r in scope.requirements}
    topology = build_dependency_topology(scope.requirements)
    by_id: Dict[str, List[CoverageRecord]] = {}
    for record in records:
        by_id.setdefault(record.requirement_id, []).append(record)
    gaps: List[Gap] = []
    base: Dict[str, bool] = {}

    def gap(req: ScopeRequirement, reason: GapReason, current: Optional[CoverageStage], detail: str) -> None:
        gaps.append(Gap(req.requirement_id, reason, req.criticality, req.required_stage,
                        current, topology.downstream_fanout(req.requirement_id), detail))

    for req in scope.requirements:
        undeclared = sorted(dep for dep in req.dependencies if dep not in reqs)
        if undeclared:
            gap(req, GapReason.UNDECLARED_DEPENDENCY, None, "undeclared: " + ", ".join(undeclared))
    for rid in topology.cycle_nodes:
        gap(reqs[rid], GapReason.CYCLE, None, "dependency cycle intersects requirement")

    for req in scope.requirements:
        candidates = by_id.get(req.requirement_id, [])
        if not candidates:
            gap(req, GapReason.MISSING, None, "required artifact has no record")
            base[req.requirement_id] = False
            continue
        if len(candidates) > 1:
            gap(req, GapReason.DUPLICATE_RECORD, None, "multiple unresolved records")
            base[req.requirement_id] = False
            continue
        record = candidates[0]
        validation = validate_record(record)
        if not validation.valid:
            gap(req, GapReason.INVALID_RECORD, record.stage, "; ".join(validation.errors))
            base[req.requirement_id] = False
            continue
        if record.stage in _SPECIAL_REASON:
            gap(req, _SPECIAL_REASON[record.stage], record.stage, f"record state is {record.stage.value}")
            base[req.requirement_id] = False
            continue
        if _STAGE_RANK[record.stage] < _STAGE_RANK[req.required_stage]:
            gap(req, GapReason.BELOW_REQUIRED_STAGE, record.stage,
                f"requires {req.required_stage.value}, has {record.stage.value}")
            base[req.requirement_id] = False
            continue
        base[req.requirement_id] = True

    satisfied = dict(base)
    changed = True
    while changed:
        changed = False
        for req in scope.requirements:
            if satisfied.get(req.requirement_id, False) and any(not satisfied.get(dep, False) for dep in req.dependencies):
                satisfied[req.requirement_id] = False
                current = by_id[req.requirement_id][0].stage if len(by_id.get(req.requirement_id, [])) == 1 else None
                gap(req, GapReason.DEPENDENCY_GAP, current, "declared dependency is unsatisfied")
                changed = True

    gaps = list({(g.requirement_id, g.reason, g.detail): g for g in gaps}.values())
    high = lambda g: g.criticality in {Criticality.CRITICAL, Criticality.DECISION_RELEVANT}
    if any(g.reason is GapReason.FALSIFIED for g in gaps):
        status = CompletionStatus.CONTRADICTORY
    elif any(high(g) and g.reason in _UNKNOWN_REASONS for g in gaps):
        status = CompletionStatus.UNKNOWN_GAP
    elif any(high(g) for g in gaps):
        status = CompletionStatus.INCOMPLETE
    elif gaps:
        status = CompletionStatus.CONDITIONAL
    else:
        status = CompletionStatus.COMPLETE_FOR_SCOPE
    satisfied_ids = tuple(r.requirement_id for r in scope.requirements if satisfied.get(r.requirement_id, False))
    return CoverageEvaluation(status, scope.scope_id, topology, prioritize_gaps(gaps), satisfied_ids,
                              len(scope.requirements), len(satisfied_ids))


def promote_record(record: CoverageRecord, target_stage: CoverageStage) -> PromotionResult:
    """Promote active stages only; exception states require re-evidencing."""
    if target_stage not in _STAGE_RANK:
        return PromotionResult(False, record, ("TARGET_STAGE_NOT_PROMOTABLE",))
    if record.stage not in _STAGE_RANK:
        return PromotionResult(False, record, ("CURRENT_STAGE_REQUIRES_REEVIDENCING",))
    if _STAGE_RANK[target_stage] < _STAGE_RANK[record.stage]:
        return PromotionResult(False, record, ("PROMOTION_MUST_NOT_DECREASE_STAGE",))
    candidate = replace(record, stage=target_stage)
    validation = validate_record(candidate)
    return PromotionResult(validation.valid, candidate if validation.valid else record, validation.errors)
