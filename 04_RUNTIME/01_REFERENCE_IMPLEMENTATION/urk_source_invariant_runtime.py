"""Executable repair bindings for tautological URK source invariant labels.

Origin architect / steward: Trang Phan.

The Drive repair specification historically declared several invariants as
`Prop := True`. This module compiles those labels into bounded executable
predicates over the current reference runtime. Passing these checks is bounded
implementation evidence, not Canon promotion or a universal theorem.
"""
from __future__ import annotations

from dataclasses import dataclass, fields
from enum import Enum
from typing import Callable, Dict, Tuple

from core19_runtime import (
    CellStatus,
    Core19,
    P02BindingRegistry,
    P02Candidate,
    TRUTH4_BOTH,
    TRUTH4_FALSE_ONLY,
    TRUTH4_NEITHER,
    TRUTH4_TRUE_ONLY,
    TensorCoordinate,
    TopologyEdge,
)
from core19_tensor_topology import validate_tensor_topology_invariants
from matrix_registry_runtime import EvidenceClass
from ulk_fragment_execution_registry import Fragment, execution_binding


class InvariantStatus(Enum):
    VERIFIED_BOUNDED = "VERIFIED_BOUNDED"
    FAILED = "FAILED"


@dataclass(frozen=True)
class InvariantResult:
    invariant_id: str
    status: InvariantStatus
    evidence: str

    @property
    def passed(self) -> bool:
        return self.status is InvariantStatus.VERIFIED_BOUNDED


@dataclass(frozen=True)
class CausalPromotionEvidence:
    temporal_admissible: bool
    domain_semantics_bound: bool
    evidence_id: str

    def __post_init__(self) -> None:
        if not self.evidence_id.strip():
            raise ValueError("causal promotion requires evidence identity")


@dataclass(frozen=True)
class CausalAssertion:
    cause: Core19
    effect: Core19
    source_relation_id: str
    evidence_id: str


def promote_relation_to_cause(edge: TopologyEdge, evidence: CausalPromotionEvidence) -> CausalAssertion:
    """A topology relation cannot become causal without extra typed evidence."""
    if not evidence.temporal_admissible:
        raise ValueError("causal promotion requires temporal admissibility")
    if not evidence.domain_semantics_bound:
        raise ValueError("causal promotion requires typed domain causal semantics")
    return CausalAssertion(edge.src, edge.dst, edge.relation_id, evidence.evidence_id)


def _pass(invariant_id: str, evidence: str) -> InvariantResult:
    return InvariantResult(invariant_id, InvariantStatus.VERIFIED_BOUNDED, evidence)


def _fail(invariant_id: str, evidence: str) -> InvariantResult:
    return InvariantResult(invariant_id, InvariantStatus.FAILED, evidence)


def check_typed_axes() -> InvariantResult:
    invariant_id = "INV_TYPED_AXES"
    failures = validate_tensor_topology_invariants()
    expected = ("row", "col", "scale", "context", "regime")
    actual = tuple(field.name for field in fields(TensorCoordinate))
    if failures or actual != expected:
        return _fail(invariant_id, f"tensor_failures={failures}; fields={actual}")
    return _pass(invariant_id, "typed coordinate axes are distinct and runtime tensor invariants pass")


def check_p02_conflict_preserved() -> InvariantResult:
    invariant_id = "INV_P02_CONFLICT_PRESERVED"
    candidates = set(P02Candidate)
    expected = {P02Candidate.NON_EXISTENCE, P02Candidate.DISTINCTION}
    reg = P02BindingRegistry()
    unresolved = reg.resolve("cross-lineage", "unbound")
    if candidates != expected or unresolved.resolved:
        return _fail(invariant_id, "candidate set changed or unbound cross-lineage registry resolved a winner")
    return _pass(invariant_id, "NonExistence and Distinction remain distinct candidates; no default global winner")


def check_p02_requires_namespace_binding() -> InvariantResult:
    invariant_id = "INV_P02_REQUIRES_NAMESPACE_BINDING"
    reg = P02BindingRegistry()
    try:
        reg.resolve("", "v1")
        return _fail(invariant_id, "empty namespace unexpectedly accepted")
    except ValueError:
        pass
    try:
        reg.resolve("ns", "")
        return _fail(invariant_id, "empty version unexpectedly accepted")
    except ValueError:
        pass
    reg.bind("ns", "v1", P02Candidate.DISTINCTION)
    try:
        reg.bind("ns", "v1", P02Candidate.NON_EXISTENCE)
        return _fail(invariant_id, "conflicting namespace-local rebind unexpectedly accepted")
    except ValueError:
        pass
    return _pass(invariant_id, "namespace/version are mandatory and conflicting local rebinds fail closed")


def check_no_1einfinity_dimension() -> InvariantResult:
    invariant_id = "INV_NO_1EINFINITY_DIMENSION"
    actual = tuple(field.name for field in fields(TensorCoordinate))
    forbidden_structural_fields = {"dimension", "dimensions", "shape", "cardinality"}
    if forbidden_structural_fields.intersection(actual):
        return _fail(invariant_id, f"untyped dimension field present: {actual}")
    if actual != ("row", "col", "scale", "context", "regime"):
        return _fail(invariant_id, f"unexpected coordinate contract: {actual}")
    return _pass(
        invariant_id,
        "tensor coordinates use typed row/col/scale/context/regime indices; no numeric infinity-cardinality dimension is encoded",
    )


def check_paradox_not_collapsed_to_classical_boolean() -> InvariantResult:
    invariant_id = "INV_PARADOX_NOT_CLASSICAL_CONTRADICTION"
    if not TRUTH4_BOTH.is_paradox:
        return _fail(invariant_id, "Truth4 BOTH is not recognized as the bounded paradox evidence state")
    if len({TRUTH4_NEITHER, TRUTH4_TRUE_ONLY, TRUTH4_FALSE_ONLY, TRUTH4_BOTH}) != 4:
        return _fail(invariant_id, "Truth4 evidence states collapsed")
    if TRUTH4_BOTH in (TRUTH4_TRUE_ONLY, TRUTH4_FALSE_ONLY):
        return _fail(invariant_id, "both-support state collapsed into classical one-sided truth state")
    return _pass(invariant_id, "four-valued evidence keeps BOTH distinct from true-only/false-only/neither")


def check_relation_ne_causation() -> InvariantResult:
    invariant_id = "INV_RELATION_NE_CAUSATION"
    edge = TopologyEdge(Core19.P01_EXISTENCE, Core19.P03_CAUSALITY, "rel", CellStatus.AMOS_MODEL)
    try:
        promote_relation_to_cause(edge, CausalPromotionEvidence(False, True, "e1"))
        return _fail(invariant_id, "relation promoted without temporal admissibility")
    except ValueError:
        pass
    try:
        promote_relation_to_cause(edge, CausalPromotionEvidence(True, False, "e2"))
        return _fail(invariant_id, "relation promoted without domain causal semantics")
    except ValueError:
        pass
    promoted = promote_relation_to_cause(edge, CausalPromotionEvidence(True, True, "e3"))
    if promoted.source_relation_id != edge.relation_id:
        return _fail(invariant_id, "causal promotion lost source relation provenance")
    return _pass(invariant_id, "topology relation requires temporal + domain-semantic evidence before causal promotion")


def check_canon_ne_implementation() -> InvariantResult:
    invariant_id = "INV_CANON_NE_IMPLEMENTATION"
    for fragment in Fragment:
        binding = execution_binding(fragment)
        if binding.canon_promoted:
            return _fail(invariant_id, f"runtime binding self-promoted canon: {fragment.name}")
    return _pass(invariant_id, "all current executable fragment bindings preserve canon_promoted=false")


def check_model_ne_verified_math() -> InvariantResult:
    invariant_id = "INV_MODEL_NE_VERIFIED_MATH"
    if EvidenceClass.AMOS_MODEL in (EvidenceClass.EXECUTED_TEST, EvidenceClass.FORMAL_PROOF):
        return _fail(invariant_id, "AMOS_MODEL evidence class collapsed into execution/proof")
    if len({EvidenceClass.AMOS_MODEL, EvidenceClass.EXECUTED_TEST, EvidenceClass.FORMAL_PROOF}) != 3:
        return _fail(invariant_id, "model/execution/proof evidence classes are not distinct")
    return _pass(invariant_id, "AMOS_MODEL, EXECUTED_TEST, and FORMAL_PROOF remain distinct evidence classes")


SOURCE_INVARIANT_CHECKERS: Dict[str, Callable[[], InvariantResult]] = {
    "INV_TYPED_AXES": check_typed_axes,
    "INV_P02_CONFLICT_PRESERVED": check_p02_conflict_preserved,
    "INV_P02_REQUIRES_NAMESPACE_BINDING": check_p02_requires_namespace_binding,
    "INV_NO_1EINFINITY_DIMENSION": check_no_1einfinity_dimension,
    "INV_PARADOX_NOT_CLASSICAL_CONTRADICTION": check_paradox_not_collapsed_to_classical_boolean,
    "INV_RELATION_NE_CAUSATION": check_relation_ne_causation,
    "INV_CANON_NE_IMPLEMENTATION": check_canon_ne_implementation,
    "INV_MODEL_NE_VERIFIED_MATH": check_model_ne_verified_math,
}


def evaluate_source_invariants() -> Tuple[InvariantResult, ...]:
    return tuple(SOURCE_INVARIANT_CHECKERS[name]() for name in SOURCE_INVARIANT_CHECKERS)


def validate_source_invariants() -> Tuple[str, ...]:
    return tuple(result.invariant_id for result in evaluate_source_invariants() if not result.passed)
