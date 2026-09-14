"""Evidence-bound ULK fragment execution registry.

Origin architect / steward: Trang Phan.

Canonical fragment ownership remains ULK_LOGIC_KERNEL.md v2.1.0. This registry
binds implementation evidence only; it cannot promote Canon or effect authority.
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


ALU02_CHECKER_SHA256 = "002a4c72adf0afaa7ad1b33792008ea6a525ca43b69ae4eff301c1b06a135275"

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
    Fragment.ALU07_QUANTUM_LOGIC: ExecutionBinding(
        Fragment.ALU07_QUANTUM_LOGIC,
        ExecutionStatus.CANONICAL_BOUNDED_CLAIM_REBIND_PENDING,
        None,
        None,
        "canonical bounded claim retained; current repository runtime identity not rebound here",
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
    if alu02.canon_promoted:
        failures.append("ALU02_CANDIDATE_MUST_NOT_SELF_PROMOTE_CANON")
    if alu02.checker_sha256 != ALU02_CHECKER_SHA256:
        failures.append("ALU02_CHECKER_HASH_MISMATCH")
    for frag in (
        Fragment.ALU03_TEMPORAL_LTL,
        Fragment.ALU04_EPISTEMIC_MODAL,
        Fragment.ALU05_NON_MONOTONIC_DUNG,
        Fragment.ALU06_DEPENDENT_TYPE,
        Fragment.ALU08_CATEGORICAL_TOPOS,
    ):
        if execution_binding(frag).status is not ExecutionStatus.SPECIFICATION_ONLY:
            failures.append(f"{frag.name}_UNSUPPORTED_EXECUTION_PROMOTION")
    return tuple(failures)
