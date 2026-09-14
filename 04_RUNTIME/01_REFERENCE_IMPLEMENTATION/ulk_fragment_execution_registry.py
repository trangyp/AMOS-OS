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


# Exact SHA-256 values are execution identities for the repository files named
# in the corresponding bindings. Any checker-byte mutation invalidates its
# receipt until this registry is explicitly rebound after regression testing.
ALU02_CHECKER_SHA256 = "d85590549de8efb76ffb0b929fc7a53a036f21c34fcc3327527d08462d826b7c"
ALU04_CHECKER_SHA256 = "d54bcc3d6eecd4a07a1f4174b3c36f6fe928d2683f01b98269da64e0e2797bbd"
ALU05_CHECKER_SHA256 = "966f687c902988e5127a8e38df9984dbff3da6f6eeda22db25f92120b7faeec1"
ALU06_CHECKER_SHA256 = "72cb28e12874d01144f2035049a1f88ea0ffdb4eea736b4355c119d1b29cd82c"
ALU08_CHECKER_SHA256 = "644dd74e15718920a8885a0a4265acb3a1638fdf0797ac4db9e3ab0b974df895"
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
    Fragment.ALU04_EPISTEMIC_MODAL: ExecutionBinding(
        Fragment.ALU04_EPISTEMIC_MODAL,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu04_finite_kripke_checker_v1.py",
        ALU04_CHECKER_SHA256,
        "finite Kripke-model propositional modal semantics for NOT/AND/OR/IMPLIES/BOX/DIAMOND; no dynamic/common-knowledge/probabilistic/infinite-model completeness claim",
    ),
    Fragment.ALU05_NON_MONOTONIC_DUNG: ExecutionBinding(
        Fragment.ALU05_NON_MONOTONIC_DUNG,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu05_dung_checker_v1.py",
        ALU05_CHECKER_SHA256,
        "finite Dung abstract argumentation: conflict-free, defence, characteristic function, grounded extension, admissibility, bounded preferred enumeration",
    ),
    Fragment.ALU06_DEPENDENT_TYPE: ExecutionBinding(
        Fragment.ALU06_DEPENDENT_TYPE,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu06_dependent_pi_checker_v1.py",
        ALU06_CHECKER_SHA256,
        "bounded de-Bruijn dependent Pi calculus with predicative universes, lambda/application, Nat, beta normalization and definitional equality; not full Calculus of Constructions or Lean/Coq",
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
    Fragment.ALU08_CATEGORICAL_TOPOS: ExecutionBinding(
        Fragment.ALU08_CATEGORICAL_TOPOS,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu08_finite_category_heyting_checker_v1.py",
        ALU08_CHECKER_SHA256,
        "finite small-category law validation plus finite Heyting-algebra semantics; does not certify finite limits, Cartesian closure, a subobject classifier, or elementary-topos status",
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
    rebound = tuple(
        execution_binding(fragment)
        for fragment in (
            Fragment.ALU02_FIRST_ORDER_UNIFICATION,
            Fragment.ALU03_TEMPORAL_LTL,
            Fragment.ALU04_EPISTEMIC_MODAL,
            Fragment.ALU05_NON_MONOTONIC_DUNG,
            Fragment.ALU06_DEPENDENT_TYPE,
            Fragment.ALU07_QUANTUM_LOGIC,
            Fragment.ALU08_CATEGORICAL_TOPOS,
        )
    )
    for binding in rebound:
        if binding.canon_promoted:
            failures.append(f"{binding.fragment.name}_CANDIDATE_MUST_NOT_SELF_PROMOTE_CANON")
        if binding.status is not ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND:
            failures.append(f"{binding.fragment.name}_REBOUND_STATUS_MISMATCH")

    expected_hashes = {
        Fragment.ALU02_FIRST_ORDER_UNIFICATION: ALU02_CHECKER_SHA256,
        Fragment.ALU04_EPISTEMIC_MODAL: ALU04_CHECKER_SHA256,
        Fragment.ALU05_NON_MONOTONIC_DUNG: ALU05_CHECKER_SHA256,
        Fragment.ALU06_DEPENDENT_TYPE: ALU06_CHECKER_SHA256,
        Fragment.ALU08_CATEGORICAL_TOPOS: ALU08_CHECKER_SHA256,
    }
    for fragment, expected in expected_hashes.items():
        if execution_binding(fragment).checker_sha256 != expected:
            failures.append(f"{fragment.name}_CHECKER_HASH_MISMATCH")

    alu03 = execution_binding(Fragment.ALU03_TEMPORAL_LTL)
    alu07 = execution_binding(Fragment.ALU07_QUANTUM_LOGIC)
    if alu03.source_revision_id != UNIFIED_BRAIN_CURRENT_REVISION or alu03.source_method_ast_sha256 != ALU03_SOURCE_METHOD_AST_SHA256:
        failures.append("ALU03_SOURCE_BINDING_MISMATCH")
    if alu07.source_revision_id != UNIFIED_BRAIN_CURRENT_REVISION or alu07.source_method_ast_sha256 != ALU07_SOURCE_METHOD_AST_SHA256:
        failures.append("ALU07_SOURCE_BINDING_MISMATCH")
    return tuple(failures)
