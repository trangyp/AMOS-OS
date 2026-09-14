"""Evidence-bound ULK fragment execution registry.

Origin architect / steward: Trang Phan.

Canonical fragment ownership remains ULK_LOGIC_KERNEL.md v2.1.0. This registry
binds implementation evidence only; it cannot promote Canon or effect authority.
A monolithic source-file hash is not used where a fragment can be bound more
precisely to its callable AST identity and source revision.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional


class Fragment(Enum):
    ALU01_CLASSICAL_PROPOSITIONAL = "ClassicalPropositional"
    ALU02_FIRST_ORDER_UNIFICATION = "FirstOrderUnification"
    ALU03_TEMPORAL_LTL = "TemporalLTL"
    ALU04_EPISTEMIC_MODAL = "EpistemicModal"
    ALU05_NON_MONOTONIC_DUNG = "NonMonotonicDung"
    ALU06_DEPENDENT_TYPE = "DependentType"
    ALU07_QUANTUM_LOGIC = "QuantumLogic"
    ALU08_CATEGORICAL_TOPOS = "CategoricalTopos"


class ExecutionStatus(Enum):
    EXECUTABLE_BOUNDED = "EXECUTABLE_BOUNDED"
    EXECUTABLE_BOUNDED_CANDIDATE_REBOUND = "EXECUTABLE_BOUNDED_CANDIDATE_REBOUND"
    CANONICAL_BOUNDED_CLAIM_REBIND_PENDING = "CANONICAL_BOUNDED_CLAIM_REBIND_PENDING"
    SPECIFICATION_ONLY = "SPECIFICATION_ONLY"


@dataclass(frozen=True)
class ExecutionBinding:
    fragment: Fragment
    status: ExecutionStatus
    checker: Optional[str]
    checker_sha256: Optional[str]
    scope: str
    canon_promoted: bool = False
    source_revision_id: Optional[str] = None
    source_method_ast_sha256: Optional[str] = None


ALU02_CHECKER_SHA256 = "002a4c72adf0afaa7ad1b33792008ea6a525ca43b69ae4eff301c1b06a135275"
UNIFIED_BRAIN_CURRENT_REVISION = "0B_FlOTCuYcaFdVpKNEFLOTNHcFM3Q01GVGx4TmpVTTBHVytrPQ"
ALU03_SOURCE_METHOD_AST_SHA256 = "9eecefbdc60faa0fe70ff758400174130ac536fc92debe7d85f22d55759c7f9f"
ALU07_SOURCE_METHOD_AST_SHA256 = "754402e1a342f4eee7d4bf6c19c155a0ff6257cab82bcaf1f1e3bedbcec98410"

_BINDINGS: Dict[Fragment, ExecutionBinding] = {
    Fragment.ALU01_CLASSICAL_PROPOSITIONAL: ExecutionBinding(
        Fragment.ALU01_CLASSICAL_PROPOSITIONAL,
        ExecutionStatus.EXECUTABLE_BOUNDED,
        "core19_runtime.py/classical_sat_firewall.py",
        None,
        "bounded classical propositional/Core-19 subset",
    ),
    Fragment.ALU02_FIRST_ORDER_UNIFICATION: ExecutionBinding(
        Fragment.ALU02_FIRST_ORDER_UNIFICATION,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu02_unification_reference_checker_v1.py",
        ALU02_CHECKER_SHA256,
        "finite first-order term unification over variables/constants/function terms with occurs-check",
    ),
    Fragment.ALU03_TEMPORAL_LTL: ExecutionBinding(
        Fragment.ALU03_TEMPORAL_LTL,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu03_finite_trace_ltl_checker_v1.py",
        None,
        "finite-trace Boolean temporal semantics for ATOM/NOT/AND/OR/IMPLIES/X/F/G/U; not infinite-trace LTL model checking",
        source_revision_id=UNIFIED_BRAIN_CURRENT_REVISION,
        source_method_ast_sha256=ALU03_SOURCE_METHOD_AST_SHA256,
    ),
    Fragment.ALU07_QUANTUM_LOGIC: ExecutionBinding(
        Fragment.ALU07_QUANTUM_LOGIC,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu07_reference_checker_current.py",
        None,
        "bounded classical finite-dimensional numerical reference checker over 20 explicitly enumerated operator surfaces; no quantum hardware or universal ALU-07 completion",
        source_revision_id=UNIFIED_BRAIN_CURRENT_REVISION,
        source_method_ast_sha256=ALU07_SOURCE_METHOD_AST_SHA256,
    ),
}


def execution_binding(fragment: Fragment) -> ExecutionBinding:
    return _BINDINGS.get(
        fragment,
        ExecutionBinding(
            fragment,
            ExecutionStatus.SPECIFICATION_ONLY,
            None,
            None,
            "no repository-bound executable evidence",
        ),
    )


def validate_execution_registry() -> tuple[str, ...]:
    failures = []
    alu02 = execution_binding(Fragment.ALU02_FIRST_ORDER_UNIFICATION)
    alu03 = execution_binding(Fragment.ALU03_TEMPORAL_LTL)
    alu07 = execution_binding(Fragment.ALU07_QUANTUM_LOGIC)

    for binding in (alu02, alu03, alu07):
        if binding.canon_promoted:
            failures.append(f"{binding.fragment.name}_CANDIDATE_MUST_NOT_SELF_PROMOTE_CANON")
        if binding.status is not ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND:
            failures.append(f"{binding.fragment.name}_REBOUND_STATUS_MISMATCH")

    if alu02.checker_sha256 != ALU02_CHECKER_SHA256:
        failures.append("ALU02_CHECKER_HASH_MISMATCH")
    if alu03.source_revision_id != UNIFIED_BRAIN_CURRENT_REVISION or alu03.source_method_ast_sha256 != ALU03_SOURCE_METHOD_AST_SHA256:
        failures.append("ALU03_SOURCE_BINDING_MISMATCH")
    if alu07.source_revision_id != UNIFIED_BRAIN_CURRENT_REVISION or alu07.source_method_ast_sha256 != ALU07_SOURCE_METHOD_AST_SHA256:
        failures.append("ALU07_SOURCE_BINDING_MISMATCH")

    for frag in (
        Fragment.ALU04_EPISTEMIC_MODAL,
        Fragment.ALU05_NON_MONOTONIC_DUNG,
        Fragment.ALU06_DEPENDENT_TYPE,
        Fragment.ALU08_CATEGORICAL_TOPOS,
    ):
        if execution_binding(frag).status is not ExecutionStatus.SPECIFICATION_ONLY:
            failures.append(f"{frag.name}_UNSUPPORTED_EXECUTION_PROMOTION")
    return tuple(failures)
