"""Evidence-bound routing projection for AMOS Cognitive Matrix.

Origin architect / steward: Trang Phan.

This router consumes the repository-owned ULK execution registry rather than
maintaining a second logic implementation-status table. It selects only explicit
bounded query subfragments. Generic full-fragment requests remain fail-closed.
It proposes routes only; it never mints commit authority or promotes Canon.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Any, Iterable, Mapping, Optional, Sequence, Tuple

from ulk_fragment_execution_registry import (
    ExecutionStatus,
    Fragment,
    execution_binding,
)


class RouteStatus(Enum):
    ROUTED = "ROUTED"
    PROPOSAL_ONLY = "PROPOSAL_ONLY"
    DENY = "DENY"
    AMBIGUOUS = "AMBIGUOUS"
    AUTHORITY_REQUIRED = "AUTHORITY_REQUIRED"
    REBIND_REQUIRED = "REBIND_REQUIRED"
    UNKNOWN_GAP = "UNKNOWN/GAP"


class QueryKind(Enum):
    CLASSICAL_INFERENCE = "CLASSICAL_INFERENCE"
    FIRST_ORDER_TERM_UNIFICATION = "FIRST_ORDER_TERM_UNIFICATION"
    FIRST_ORDER_THEOREM_PROVING = "FIRST_ORDER_THEOREM_PROVING"
    TEMPORAL_FINITE_TRACE_CHECK = "TEMPORAL_FINITE_TRACE_CHECK"
    TEMPORAL_MODEL_CHECK = "TEMPORAL_MODEL_CHECK"
    MODAL_K_FINITE_MODEL_CHECK = "MODAL_K_FINITE_MODEL_CHECK"
    EPISTEMIC_MODAL = "EPISTEMIC_MODAL"
    DUNG_ABSTRACT_FRAMEWORK_CHECK = "DUNG_ABSTRACT_FRAMEWORK_CHECK"
    NON_MONOTONIC = "NON_MONOTONIC"
    DEPENDENT_PI_TYPE_CHECK = "DEPENDENT_PI_TYPE_CHECK"
    DEPENDENT_TYPE = "DEPENDENT_TYPE"
    QUANTUM_FINITE_DIMENSIONAL_OPERATOR = "QUANTUM_FINITE_DIMENSIONAL_OPERATOR"
    QUANTUM_LOGIC = "QUANTUM_LOGIC"
    FINITE_CATEGORY_HEYTING_CHECK = "FINITE_CATEGORY_HEYTING_CHECK"
    CATEGORICAL_TOPOS = "CATEGORICAL_TOPOS"
    WORLD_MODEL = "WORLD_MODEL"
    GENERIC = "GENERIC"


class PremiseState(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNKNOWN_GAP = "UNKNOWN/GAP"


class Consequence(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass(frozen=True)
class EpochBinding:
    name: str
    value: str
    def __post_init__(self) -> None:
        if not self.name.strip() or not self.value.strip():
            raise ValueError("epoch binding name/value must be explicit")


@dataclass(frozen=True)
class RouteRequest:
    request_id: str
    query_kind: QueryKind
    scope: str
    regime: str
    required_capabilities: Tuple[str, ...] = ()
    explicit_target: Optional[str] = None
    premise_state: PremiseState = PremiseState.PASS
    current_epochs: Tuple[EpochBinding, ...] = ()
    min_independent_evidence_roots: int = 0
    effectful: bool = False
    authority_bound: bool = False
    consequence: Consequence = Consequence.LOW
    payload: Any = None
    def __post_init__(self) -> None:
        if not self.request_id.strip() or not self.scope.strip() or not self.regime.strip():
            raise ValueError("request_id, scope, and regime must be explicit")
        if self.explicit_target is not None and not self.explicit_target.strip():
            raise ValueError("explicit_target must be non-empty when supplied")
        if self.min_independent_evidence_roots < 0:
            raise ValueError("min_independent_evidence_roots must be nonnegative")
        if any(not cap.strip() for cap in self.required_capabilities):
            raise ValueError("required capabilities must be non-empty")


@dataclass(frozen=True)
class RouteCandidate:
    target_id: str
    query_kinds: Tuple[QueryKind, ...]
    scopes: Tuple[str, ...]
    regimes: Tuple[str, ...]
    capabilities: Tuple[str, ...]
    validated: bool
    policy_priority: int
    specialist: bool
    source_version: str
    ulk_fragment: Optional[Fragment] = None
    provenance_roots: Tuple[str, ...] = ()
    epoch_dependencies: Tuple[EpochBinding, ...] = ()
    def __post_init__(self) -> None:
        if not self.target_id.strip() or not self.source_version.strip():
            raise ValueError("target_id and source_version must be explicit")
        if not self.query_kinds or not self.scopes or not self.regimes:
            raise ValueError("candidate query kinds/scopes/regimes must be non-empty")
        if any(not x.strip() for x in (*self.scopes,*self.regimes,*self.capabilities,*self.provenance_roots)):
            raise ValueError("candidate string fields must be non-empty")
        if "*" in self.scopes or "*" in self.regimes:
            raise ValueError("wildcard scope/regime candidates are forbidden")


@dataclass(frozen=True)
class RoutingDecision:
    status: RouteStatus
    target_id: Optional[str]
    reason: str
    eligible_ids: Tuple[str, ...]
    rejected: Tuple[Tuple[str, str], ...]
    independent_evidence_roots: int
    effect_authority_bound: bool
    commit_authorized: bool = False


def _epoch_map(bindings: Iterable[EpochBinding]) -> Mapping[str,str]:
    out = {}
    for binding in bindings:
        if binding.name in out and out[binding.name] != binding.value:
            raise ValueError(f"conflicting current epoch binding for {binding.name}")
        out[binding.name] = binding.value
    return out


def _independent_root_count(roots: Iterable[str]) -> int:
    return len(set(roots))


def _execution_rejection(candidate: RouteCandidate) -> Optional[str]:
    if candidate.ulk_fragment is None:
        return None
    binding = execution_binding(candidate.ulk_fragment)
    if binding.canon_promoted:
        return "REGISTRY_CANON_AUTHORITY_LEAK"
    if binding.status in {
        ExecutionStatus.EXECUTABLE_BOUNDED,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
    }:
        return None
    if binding.status is ExecutionStatus.CANONICAL_BOUNDED_CLAIM_REBIND_PENDING:
        return "REBIND_PENDING"
    if binding.status is ExecutionStatus.SPECIFICATION_ONLY:
        return "SPECIFICATION_ONLY"
    return "IMPLEMENTATION_UNKNOWN"


def _candidate_rejection(candidate: RouteCandidate, request: RouteRequest, epochs: Mapping[str,str]) -> Optional[str]:
    if request.query_kind not in candidate.query_kinds: return "QUERY_KIND_UNSUPPORTED"
    if request.scope not in candidate.scopes: return "SCOPE_MISMATCH"
    if request.regime not in candidate.regimes: return "REGIME_MISMATCH"
    if not set(request.required_capabilities).issubset(candidate.capabilities): return "CAPABILITY_MISMATCH"
    execution_reason = _execution_rejection(candidate)
    if execution_reason is not None: return execution_reason
    if not candidate.validated: return "VALIDATION_REQUIRED"
    for dep in candidate.epoch_dependencies:
        if epochs.get(dep.name) != dep.value: return f"STALE_EPOCH:{dep.name}"
    if _independent_root_count(candidate.provenance_roots) < request.min_independent_evidence_roots:
        return "INSUFFICIENT_INDEPENDENT_EVIDENCE_ROOTS"
    return None


def audit_candidates(candidates: Sequence[RouteCandidate]) -> Tuple[str,...]:
    ids=[candidate.target_id for candidate in candidates]
    return ("DUPLICATE_TARGET_ID",) if len(ids)!=len(set(ids)) else ()


def route(request: RouteRequest, candidates: Sequence[RouteCandidate]) -> RoutingDecision:
    if audit_candidates(candidates):
        return RoutingDecision(RouteStatus.UNKNOWN_GAP,None,"candidate registry invalid",(),(),0,request.authority_bound)
    if request.premise_state is PremiseState.FAIL:
        return RoutingDecision(RouteStatus.DENY,None,"required routing premise failed",(),(),0,request.authority_bound)
    if request.premise_state is PremiseState.UNKNOWN_GAP:
        return RoutingDecision(RouteStatus.UNKNOWN_GAP,None,"required routing premise is UNKNOWN/GAP",(),(),0,request.authority_bound)

    epochs=_epoch_map(request.current_epochs)
    pool=list(candidates)
    if request.explicit_target is not None:
        pool=[c for c in pool if c.target_id==request.explicit_target]
        if not pool:
            return RoutingDecision(RouteStatus.DENY,None,"explicit target unresolved; silent fallback forbidden",(),(),0,request.authority_bound)

    eligible=[]; rejected=[]
    for candidate in pool:
        reason=_candidate_rejection(candidate,request,epochs)
        if reason is None: eligible.append(candidate)
        else: rejected.append((candidate.target_id,reason))

    if not eligible:
        if any(reason=="REBIND_PENDING" for _,reason in rejected): status=RouteStatus.REBIND_REQUIRED
        elif any(reason in {"IMPLEMENTATION_UNKNOWN","REGISTRY_CANON_AUTHORITY_LEAK"} for _,reason in rejected): status=RouteStatus.UNKNOWN_GAP
        else: status=RouteStatus.DENY
        prefix="explicit target rejected" if request.explicit_target is not None else "no candidate satisfies all hard constraints"
        return RoutingDecision(status,None,prefix,(),tuple(rejected),0,request.authority_bound)

    best_key=max((c.policy_priority,int(c.specialist)) for c in eligible)
    best=[c for c in eligible if (c.policy_priority,int(c.specialist))==best_key]
    if len(best)!=1:
        return RoutingDecision(RouteStatus.AMBIGUOUS,None,"materially equal eligible routes remain competing",tuple(sorted(c.target_id for c in eligible)),tuple(rejected),max((_independent_root_count(c.provenance_roots) for c in best),default=0),request.authority_bound)
    chosen=best[0]; roots=_independent_root_count(chosen.provenance_roots)
    if request.effectful and not request.authority_bound:
        return RoutingDecision(RouteStatus.AUTHORITY_REQUIRED,chosen.target_id,"capability/eligibility does not grant effect authority",tuple(sorted(c.target_id for c in eligible)),tuple(rejected),roots,False)
    if request.effectful:
        return RoutingDecision(RouteStatus.PROPOSAL_ONLY,chosen.target_id,"effect route remains a proposal for commit-time control-plane authorization",tuple(sorted(c.target_id for c in eligible)),tuple(rejected),roots,True,False)
    return RoutingDecision(RouteStatus.ROUTED,chosen.target_id,"single bounded route selected after hard gates",tuple(sorted(c.target_id for c in eligible)),tuple(rejected),roots,request.authority_bound,False)


def reference_candidates(scope: str="reference", regime: str="active") -> Tuple[RouteCandidate,...]:
    specs=(
        ("classical-propositional-runtime",QueryKind.CLASSICAL_INFERENCE,"ULK_ALU01_CLASSICAL",Fragment.ALU01_CLASSICAL_PROPOSITIONAL),
        ("alu02-unification-runtime",QueryKind.FIRST_ORDER_TERM_UNIFICATION,"ULK_ALU02_UNIFICATION",Fragment.ALU02_FIRST_ORDER_UNIFICATION),
        ("alu03-ltlf-finite-trace-runtime",QueryKind.TEMPORAL_FINITE_TRACE_CHECK,"ULK_ALU03_LTLF_FINITE_TRACE",Fragment.ALU03_TEMPORAL_LTL),
        ("alu04-modal-k-finite-model-runtime",QueryKind.MODAL_K_FINITE_MODEL_CHECK,"ULK_ALU04_MODAL_K_FINITE_KRIPKE",Fragment.ALU04_EPISTEMIC_MODAL),
        ("alu05-dung-abstract-argumentation-runtime",QueryKind.DUNG_ABSTRACT_FRAMEWORK_CHECK,"ULK_ALU05_DUNG_ARGUMENTATION",Fragment.ALU05_NON_MONOTONIC_DUNG),
        ("alu06-dependent-pi-runtime",QueryKind.DEPENDENT_PI_TYPE_CHECK,"ULK_ALU06_DEPENDENT_PI",Fragment.ALU06_DEPENDENT_TYPE),
        ("alu07-finite-dimensional-runtime",QueryKind.QUANTUM_FINITE_DIMENSIONAL_OPERATOR,"ULK_ALU07_FINITE_DIMENSIONAL",Fragment.ALU07_QUANTUM_LOGIC),
        ("alu08-finite-category-heyting-runtime",QueryKind.FINITE_CATEGORY_HEYTING_CHECK,"ULK_ALU08_FINITE_CATEGORY_HEYTING",Fragment.ALU08_CATEGORICAL_TOPOS),
    )
    return tuple(RouteCandidate(target,(kind,),(scope,),(regime,),(cap,),True,100,True,"registry-bound",fragment,("ulk-fragment-execution-registry",)) for target,kind,cap,fragment in specs)
