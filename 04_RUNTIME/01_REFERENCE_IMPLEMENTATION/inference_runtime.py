"""Bounded executable L09 inference contract for AMOS OS.

Origin architect / steward: Trang Phan.

This module binds the repaired URK/Core-19 substrate to the Cognitive Matrix
L09_INFERENCE package. It is an AMOS_MODEL reference implementation, not canon
promotion and not evidence that every ULK fragment is executable.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Sequence, Tuple

from classical_sat_firewall import BoolFormula, conjunction, globally_consistent, is_satisfiable
from core19_runtime import (
    ImplementationStatus,
    LogicFragment,
    P02BindingRegistry,
    implementation_status,
)


class InferenceStatus(Enum):
    VERIFIED_BOUNDED = "VERIFIED_BOUNDED"
    NOT_ENTAILED = "NOT_ENTAILED"
    INCONSISTENT_INPUT = "INCONSISTENT_INPUT"
    COMPETING = "COMPETING"
    UNKNOWN_GAP = "UNKNOWN/GAP"


@dataclass(frozen=True)
class Premise:
    claim_id: str
    formula: BoolFormula
    provenance: str
    confidence: Optional[float] = None

    def __post_init__(self) -> None:
        if not self.claim_id.strip():
            raise ValueError("premise claim_id must be non-empty")
        if not self.provenance.strip():
            raise ValueError("premise provenance must be non-empty")
        if self.confidence is not None and not (0.0 <= self.confidence <= 1.0):
            raise ValueError("premise confidence must be within [0, 1]")


@dataclass(frozen=True)
class InferenceRequest:
    fragment: LogicFragment
    premises: Tuple[Premise, ...]
    conclusion: Optional[BoolFormula] = None
    scope: str = "bounded_core19_classical"
    regime: str = "reference_runtime"
    source_version: str = "2026-09-14"
    uses_p02: bool = False
    p02_namespace: Optional[str] = None
    p02_version: Optional[str] = None
    causal_claim: bool = False
    causal_evidence_bound: bool = False

    def __post_init__(self) -> None:
        if not self.scope.strip() or not self.regime.strip() or not self.source_version.strip():
            raise ValueError("scope, regime, and source_version must be explicit")


@dataclass(frozen=True)
class InferenceResult:
    status: InferenceStatus
    reason: str
    fragment_status: ImplementationStatus
    dependency_claim_ids: Tuple[str, ...]
    provenance: Tuple[str, ...]
    scope: str
    regime: str
    source_version: str
    confidence_ceiling: Optional[float]
    globally_consistent: Optional[bool]
    entailed: Optional[bool]


def _confidence_ceiling(premises: Sequence[Premise]) -> Optional[float]:
    """AMOS RSCF conjunctive-premise ceiling; not a Bayesian aggregator."""
    values = [premise.confidence for premise in premises if premise.confidence is not None]
    if len(values) != len(premises) or not values:
        return None
    return min(values)


def _result(
    request: InferenceRequest,
    *,
    status: InferenceStatus,
    reason: str,
    fragment_status: ImplementationStatus,
    globally_consistent_state: Optional[bool] = None,
    entailed: Optional[bool] = None,
) -> InferenceResult:
    return InferenceResult(
        status=status,
        reason=reason,
        fragment_status=fragment_status,
        dependency_claim_ids=tuple(p.claim_id for p in request.premises),
        provenance=tuple(p.provenance for p in request.premises),
        scope=request.scope,
        regime=request.regime,
        source_version=request.source_version,
        confidence_ceiling=_confidence_ceiling(request.premises),
        globally_consistent=globally_consistent_state,
        entailed=entailed,
    )


def evaluate_inference(
    request: InferenceRequest,
    *,
    p02_registry: Optional[P02BindingRegistry] = None,
    max_atoms: int = 20,
) -> InferenceResult:
    """Evaluate the bounded L09 inference contract fail-closed.

    Rules enforced in order:
    1. logic fragment must have local executable evidence;
    2. P02 use requires explicit namespace/version resolution;
    3. causal conclusions require separately bound causal evidence;
    4. all premises must be globally consistent, not merely pairwise compatible;
    5. classical entailment is checked as UNSAT(Premises AND NOT(Conclusion)).

    The result is scoped to this bounded reference runtime only.
    """
    fragment_state = implementation_status(request.fragment)

    if fragment_state is not ImplementationStatus.EXECUTABLE_BOUNDED:
        if fragment_state is ImplementationStatus.CANONICAL_BOUNDED_CLAIM_REBIND_PENDING:
            reason = "fragment has a canonical bounded claim but local executable checker/receipt is rebind-pending"
        else:
            reason = "fragment is specification-only in this repair surface"
        return _result(
            request,
            status=InferenceStatus.UNKNOWN_GAP,
            reason=reason,
            fragment_status=fragment_state,
        )

    if request.uses_p02:
        if p02_registry is None or request.p02_namespace is None or request.p02_version is None:
            return _result(
                request,
                status=InferenceStatus.COMPETING,
                reason="P02 is cross-lineage COMPETING and requires explicit namespace/version binding",
                fragment_status=fragment_state,
            )
        binding = p02_registry.resolve(request.p02_namespace, request.p02_version)
        if not binding.resolved:
            return _result(
                request,
                status=InferenceStatus.COMPETING,
                reason="P02 namespace/version is unresolved; no cross-lineage winner may be fabricated",
                fragment_status=fragment_state,
            )

    if request.causal_claim and not request.causal_evidence_bound:
        return _result(
            request,
            status=InferenceStatus.UNKNOWN_GAP,
            reason="logical implication/association does not establish causation without a bound causal model/evidence contract",
            fragment_status=fragment_state,
        )

    premise_formulas = tuple(p.formula for p in request.premises)
    try:
        consistent = globally_consistent(premise_formulas, max_atoms=max_atoms)
    except ValueError as exc:
        return _result(
            request,
            status=InferenceStatus.UNKNOWN_GAP,
            reason=str(exc),
            fragment_status=fragment_state,
        )

    if not consistent:
        return _result(
            request,
            status=InferenceStatus.INCONSISTENT_INPUT,
            reason="premise set is globally inconsistent; contradiction remains inspectable and no explosion-based conclusion is promoted",
            fragment_status=fragment_state,
            globally_consistent_state=False,
        )

    if request.conclusion is None:
        return _result(
            request,
            status=InferenceStatus.VERIFIED_BOUNDED,
            reason="premise set is globally consistent within the bounded classical fragment",
            fragment_status=fragment_state,
            globally_consistent_state=True,
        )

    try:
        countermodel_query = BoolFormula.and_(
            conjunction(premise_formulas),
            BoolFormula.not_(request.conclusion),
        )
        entailed = not is_satisfiable(countermodel_query, max_atoms=max_atoms)
    except ValueError as exc:
        return _result(
            request,
            status=InferenceStatus.UNKNOWN_GAP,
            reason=str(exc),
            fragment_status=fragment_state,
            globally_consistent_state=True,
        )

    if entailed:
        return _result(
            request,
            status=InferenceStatus.VERIFIED_BOUNDED,
            reason="conclusion follows by bounded classical entailment: premises AND NOT(conclusion) is unsatisfiable",
            fragment_status=fragment_state,
            globally_consistent_state=True,
            entailed=True,
        )

    return _result(
        request,
        status=InferenceStatus.NOT_ENTAILED,
        reason="a satisfying countermodel exists; conclusion is not entailed by the declared premises",
        fragment_status=fragment_state,
        globally_consistent_state=True,
        entailed=False,
    )
