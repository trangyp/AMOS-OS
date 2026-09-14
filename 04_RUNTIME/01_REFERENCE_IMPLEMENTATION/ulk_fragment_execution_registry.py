"""Evidence-bound ULK fragment execution registry.

Origin architect / steward: Trang Phan.

Canonical fragment ownership remains ULK_LOGIC_KERNEL.md v2.1.0. This registry
binds bounded implementation evidence only. It cannot promote Canon, empirical
truth, or effect authority. Fragment semantic identity is bound by callable AST
hash where available; whole-file revision identity is recorded as provenance but
does not invalidate an unchanged fragment merely because unrelated source bytes
changed.
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
ALU04_CHECKER_SHA256 = "d54bcc3d6eecd4a07a1f4174b3c36f6fe928d2683f01b98269da64e0e2797bbd"
ALU05_CHECKER_SHA256 = "966f687c902988e5127a8e38df9984dbff3da6f6eeda22db25f92120b7faeec1"
ALU06_CHECKER_SHA256 = "12a0907cfce261d5b9dd2fea46ee9496994663735bf4bee7f8006f9b43e6fec3"
ALU08_CHECKER_SHA256 = "d7ecd0cd5358b374c49a722e2fe084eb957b7719d903f386e263928625e1cd83"

# Last explicitly revalidated source revision in the V206 handoff. This is
# provenance, not a forever-current claim. Newer revisions are admitted when the
# fragment AST remains identical under a fresh observation.
UNIFIED_BRAIN_REVALIDATED_REVISION = (
    "0B_FlOTCuYcaFNWxxSWNxRWVxSktrSkp3S2NaditUZzAyRFdFPQ"
)
ALU03_SOURCE_METHOD_AST_SHA256 = (
    "797c881ad2e3c8aa746740025445efcba48e2e76eaa1efe64bc1ac3e4fd1aa69"
)
ALU07_SOURCE_METHOD_AST_SHA256 = (
    "f645bedd808bba01d512ec139a4b9e5d7d00043abf532672490eca9b7d0ab664"
)

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
        "finite first-order term unification with occurs-check",
    ),
    Fragment.ALU03_TEMPORAL_LTL: ExecutionBinding(
        Fragment.ALU03_TEMPORAL_LTL,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu03_finite_trace_ltl_checker_v1.py",
        None,
        "finite-trace ATOM/NOT/AND/OR/IMPLIES/X/F/G/U; not infinite-trace LTL model checking",
        source_revision_id=UNIFIED_BRAIN_REVALIDATED_REVISION,
        source_method_ast_sha256=ALU03_SOURCE_METHOD_AST_SHA256,
    ),
    Fragment.ALU04_EPISTEMIC_MODAL: ExecutionBinding(
        Fragment.ALU04_EPISTEMIC_MODAL,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu04_finite_kripke_checker_v1.py",
        ALU04_CHECKER_SHA256,
        "finite propositional Kripke satisfaction over explicit accessibility relations",
    ),
    Fragment.ALU05_NON_MONOTONIC_DUNG: ExecutionBinding(
        Fragment.ALU05_NON_MONOTONIC_DUNG,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu05_dung_checker_v1.py",
        ALU05_CHECKER_SHA256,
        "finite Dung abstract argumentation with bounded extension enumeration",
    ),
    Fragment.ALU06_DEPENDENT_TYPE: ExecutionBinding(
        Fragment.ALU06_DEPENDENT_TYPE,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu06_dependent_pi_checker_v1.py",
        ALU06_CHECKER_SHA256,
        "bounded de-Bruijn dependent Pi calculus; not Lean/Coq or full Calculus of Constructions",
    ),
    Fragment.ALU07_QUANTUM_LOGIC: ExecutionBinding(
        Fragment.ALU07_QUANTUM_LOGIC,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu07_reference_checker_current.py",
        None,
        "bounded classical finite-dimensional numerical quantum-logic reference operations; no quantum hardware",
        source_revision_id=UNIFIED_BRAIN_REVALIDATED_REVISION,
        source_method_ast_sha256=ALU07_SOURCE_METHOD_AST_SHA256,
    ),
    Fragment.ALU08_CATEGORICAL_TOPOS: ExecutionBinding(
        Fragment.ALU08_CATEGORICAL_TOPOS,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        "amos_ulk_alu08_finite_category_heyting_checker_v1.py",
        ALU08_CHECKER_SHA256,
        "finite category-law and Heyting-algebra reference checks; elementary-topos status not established",
    ),
}


def execution_binding(fragment: Fragment) -> ExecutionBinding:
    return _BINDINGS[fragment]


def _is_sha256(value: Optional[str]) -> bool:
    return bool(
        isinstance(value, str)
        and len(value) == 64
        and all(ch in "0123456789abcdef" for ch in value)
    )


def validate_fragment_observation(
    fragment: Fragment,
    observed_method_ast_sha256: str,
    observed_revision_id: Optional[str] = None,
) -> Dict[str, object]:
    """Validate a fresh source observation without whole-file false invalidation.

    A changed file revision with an unchanged callable AST is reported as
    REVISION_CHANGED_FRAGMENT_STABLE. A changed AST is STALE_REVALIDATE. This
    function does not grant Canon or effect authority.
    """
    binding = execution_binding(fragment)
    expected = binding.source_method_ast_sha256
    if expected is None:
        return {
            "success": False,
            "status": "NOT_FRAGMENT_SOURCE_BOUND",
            "fragment": fragment.value,
            "authority_granted": False,
        }
    if not _is_sha256(observed_method_ast_sha256):
        return {
            "success": False,
            "status": "ILL_TYPED_AST_HASH",
            "fragment": fragment.value,
            "authority_granted": False,
        }
    if observed_method_ast_sha256 != expected:
        return {
            "success": False,
            "status": "STALE_REVALIDATE",
            "fragment": fragment.value,
            "expected_ast_sha256": expected,
            "observed_ast_sha256": observed_method_ast_sha256,
            "observed_revision_id": observed_revision_id,
            "authority_granted": False,
        }
    revision_state = (
        "SAME_REVALIDATED_REVISION"
        if observed_revision_id == binding.source_revision_id
        else "REVISION_CHANGED_FRAGMENT_STABLE"
    )
    return {
        "success": True,
        "status": "FRAGMENT_SEMANTIC_IDENTITY_MATCH",
        "revision_state": revision_state,
        "fragment": fragment.value,
        "method_ast_sha256": observed_method_ast_sha256,
        "observed_revision_id": observed_revision_id,
        "authority_granted": False,
        "canon_promoted": False,
    }


def validate_execution_registry() -> tuple[str, ...]:
    failures = []
    expected_values = (
        "ClassicalPropositional",
        "FirstOrderUnification",
        "TemporalLTL",
        "EpistemicModal",
        "NonMonotonicDung",
        "DependentType",
        "QuantumLogic",
        "CategoricalTopos",
    )
    if tuple(fragment.value for fragment in Fragment) != expected_values:
        failures.append("ULK_EIGHT_FRAGMENT_IDENTITY_MISMATCH")
    if len(_BINDINGS) != 8 or set(_BINDINGS) != set(Fragment):
        failures.append("ULK_BINDING_CARDINALITY_OR_COVERAGE_MISMATCH")

    for fragment in Fragment:
        binding = execution_binding(fragment)
        if binding.fragment is not fragment:
            failures.append(f"{fragment.name}_BINDING_IDENTITY_MISMATCH")
        if binding.canon_promoted:
            failures.append(f"{fragment.name}_MUST_NOT_SELF_PROMOTE_CANON")
        if not isinstance(binding.scope, str) or not binding.scope.strip():
            failures.append(f"{fragment.name}_EMPTY_SCOPE")
        if fragment is Fragment.ALU01_CLASSICAL_PROPOSITIONAL:
            if binding.status is not ExecutionStatus.EXECUTABLE_BOUNDED:
                failures.append("ALU01_STATUS_MISMATCH")
        elif binding.status is not ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND:
            failures.append(f"{fragment.name}_REBOUND_STATUS_MISMATCH")

    expected_hashes = {
        Fragment.ALU02_FIRST_ORDER_UNIFICATION: ALU02_CHECKER_SHA256,
        Fragment.ALU04_EPISTEMIC_MODAL: ALU04_CHECKER_SHA256,
        Fragment.ALU05_NON_MONOTONIC_DUNG: ALU05_CHECKER_SHA256,
        Fragment.ALU06_DEPENDENT_TYPE: ALU06_CHECKER_SHA256,
        Fragment.ALU08_CATEGORICAL_TOPOS: ALU08_CHECKER_SHA256,
    }
    for fragment, expected in expected_hashes.items():
        if not _is_sha256(expected):
            failures.append(f"{fragment.name}_INVALID_EXPECTED_CHECKER_HASH")
        if execution_binding(fragment).checker_sha256 != expected:
            failures.append(f"{fragment.name}_CHECKER_HASH_MISMATCH")

    for fragment in (Fragment.ALU03_TEMPORAL_LTL, Fragment.ALU07_QUANTUM_LOGIC):
        binding = execution_binding(fragment)
        if not binding.source_revision_id:
            failures.append(f"{fragment.name}_SOURCE_REVISION_MISSING")
        if not _is_sha256(binding.source_method_ast_sha256):
            failures.append(f"{fragment.name}_SOURCE_AST_HASH_INVALID")

    return tuple(failures)
