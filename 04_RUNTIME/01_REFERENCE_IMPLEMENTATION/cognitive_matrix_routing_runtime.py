"""Bounded routing runtime for the AMOS Cognitive Matrix.

Origin architect / steward: Trang Phan.

This runtime turns tested routing-policy invariants into executable proposal logic.
It never commits external effects, never promotes Canon, and never converts missing
validation into permission. Hard constraints are applied before semantic priority;
registration order is never a ranking signal.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Iterable, Mapping, Optional, Sequence, Tuple


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
    DEPENDENT_TYPE = "DEPENDENT_TYPE"
    QUANTUM_LOGIC = "QUANTUM_LOGIC"
    CATEGORICAL_TOPOS = "CATEGORICAL_TOPOS"
    WORLD_MODEL = "WORLD_MODEL"
    CELL_VALIDATION = "CELL_VALIDATION"
    COVERAGE = "COVERAGE"
    DEPENDENCY = "DEPENDENCY"
    GENERIC = "GENERIC"


class ImplementationState(Enum):
    EXECUTABLE_BOUNDED = "EXECUTABLE_BOUNDED"
    EXECUTABLE_BOUNDED_SUBFRAGMENT = "EXECUTABLE_BOUNDED_SUBFRAGMENT"
    REBIND_PENDING = "REBIND_PENDING"
    SPECIFICATION_ONLY = "SPECIFICATION_ONLY"
    UNKNOWN = "UNKNOWN"


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
    implementation_state: ImplementationState
    validated: bool
    policy_priority: int
    specialist: bool
    source_version: str
    provenance_roots: Tuple[str, ...] = ()
    epoch_dependencies: Tuple[EpochBinding, ...] = ()

    def __post_init__(self) -> None:
        if not self.target_id.strip() or not self.source_version.strip():
            raise ValueError("target_id and source_version must be explicit")
        if not self.query_kinds or not self.scopes or not self.regimes:
            raise ValueError("candidate query kinds/scopes/regimes must be non-empty")
        if any(not x.strip() for x in (*self.scopes, *self.regimes, *self.capabilities, *self.provenance_roots)):
            raise ValueError("candidate string fields must be non-empty")
        if "*" in self.scopes or "*" in self.regimes:
            raise ValueError("wildcard scope/regime candidates are forbidden in the bounded router")


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


def _epoch_map(bindings: Iterable[EpochBinding]) -> Mapping[str, str]:
    out = {}
    for binding in bindings:
        if binding.name in out and out[binding.name] != binding.value:
            raise ValueError(f"conflicting current epoch binding for {binding.name}")
        out[binding.name] = binding.value
    return out


def _independent_root_count(roots: Iterable[str]) -> int:
    return len(set(roots))


def _candidate_rejection(candidate: RouteCandidate, request: RouteRequest, epochs: Mapping[str, str]) -> Optional[str]:
    if request.query_kind not in candidate.query_kinds:
        return "QUERY_KIND_UNSUPPORTED"
    if request.scope not in candidate.scopes:
        return "SCOPE_MISMATCH"
    if request.regime not in candidate.regimes:
        return "REGIME_MISMATCH"
    if not set(request.required_capabilities).issubset(set(candidate.capabilities)):
        return "CAPABILITY_MISMATCH"
    if candidate.implementation_state is ImplementationState.REBIND_PENDING:
        return "REBIND_PENDING"
    if candidate.implementation_state is ImplementationState.SPECIFICATION_ONLY:
        return "SPECIFICATION_ONLY"
    if candidate.implementation_state is ImplementationState.UNKNOWN:
        return "IMPLEMENTATION_UNKNOWN"
    if not candidate.validated:
        return "VALIDATION_REQUIRED"
    for dep in candidate.epoch_dependencies:
        if epochs.get(dep.name) != dep.value:
            return f"STALE_EPOCH:{dep.name}"
    if _independent_root_count(candidate.provenance_roots) < request.min_independent_evidence_roots:
        return "INSUFFICIENT_INDEPENDENT_EVIDENCE_ROOTS"
    return None


def audit_candidates(candidates: Sequence[RouteCandidate]) -> Tuple[str, ...]:
    ids = [candidate.target_id for candidate in candidates]
    errors = []
    if len(ids) != len(set(ids)):
        errors.append("DUPLICATE_TARGET_ID")
    return tuple(errors)


def route(request: RouteRequest, candidates: Sequence[RouteCandidate]) -> RoutingDecision:
    """Return a bounded route proposal under hard-gate/semantic-priority rules."""
    if audit_candidates(candidates):
        return RoutingDecision(RouteStatus.UNKNOWN_GAP, None, "candidate registry invalid", (), (), 0, request.authority_bound)
    if request.premise_state is PremiseState.FAIL:
        return RoutingDecision(RouteStatus.DENY, None, "required routing premise failed", (), (), 0, request.authority_bound)
    if request.premise_state is PremiseState.UNKNOWN_GAP:
        return RoutingDecision(RouteStatus.UNKNOWN_GAP, None, "required routing premise is UNKNOWN/GAP", (), (), 0, request.authority_bound)

    epochs = _epoch_map(request.current_epochs)
    pool = list(candidates)
    if request.explicit_target is not None:
        pool = [candidate for candidate in pool if candidate.target_id == request.explicit_target]
        if not pool:
            return RoutingDecision(RouteStatus.DENY, None, "explicit target is unresolved; silent fallback forbidden", (), (), 0, request.authority_bound)

    eligible = []
    rejected = []
    for candidate in pool:
        reason = _candidate_rejection(candidate, request, epochs)
        if reason is None:
            eligible.append(candidate)
        else:
            rejected.append((candidate.target_id, reason))

    if not eligible:
        if request.explicit_target is not None and rejected:
            reason = rejected[0][1]
            if reason == "REBIND_PENDING":
                status = RouteStatus.REBIND_REQUIRED
            elif reason in {"IMPLEMENTATION_UNKNOWN"}:
                status = RouteStatus.UNKNOWN_GAP
            else:
                status = RouteStatus.DENY
            return RoutingDecision(status, None, f"explicit target rejected: {reason}", (), tuple(rejected), 0, request.authority_bound)
        if any(reason == "REBIND_PENDING" for _, reason in rejected):
            return RoutingDecision(RouteStatus.REBIND_REQUIRED, None, "only matching route is rebind-pending", (), tuple(rejected), 0, request.authority_bound)
        if any(reason == "IMPLEMENTATION_UNKNOWN" for _, reason in rejected):
            return RoutingDecision(RouteStatus.UNKNOWN_GAP, None, "matching implementation state is unknown", (), tuple(rejected), 0, request.authority_bound)
        return RoutingDecision(RouteStatus.DENY, None, "no candidate satisfies all hard constraints", (), tuple(rejected), 0, request.authority_bound)

    # Semantic policy priority dominates registration order. Specialist is a tie-breaker
    # only after explicit numeric policy priority; no performance score can bypass gates.
    best_key = max((candidate.policy_priority, int(candidate.specialist)) for candidate in eligible)
    best = [candidate for candidate in eligible if (candidate.policy_priority, int(candidate.specialist)) == best_key]
    if len(best) != 1:
        return RoutingDecision(
            RouteStatus.AMBIGUOUS,
            None,
            "materially equal eligible routes remain competing",
            tuple(sorted(candidate.target_id for candidate in eligible)),
            tuple(rejected),
            max((_independent_root_count(candidate.provenance_roots) for candidate in best), default=0),
            request.authority_bound,
        )

    chosen = best[0]
    root_count = _independent_root_count(chosen.provenance_roots)
    if request.effectful and not request.authority_bound:
        return RoutingDecision(
            RouteStatus.AUTHORITY_REQUIRED,
            chosen.target_id,
            "capability/eligibility does not grant effect authority",
            tuple(sorted(candidate.target_id for candidate in eligible)),
            tuple(rejected),
            root_count,
            False,
        )
    if request.effectful:
        return RoutingDecision(
            RouteStatus.PROPOSAL_ONLY,
            chosen.target_id,
            "effect route is eligible but remains a proposal for commit-time control-plane authorization",
            tuple(sorted(candidate.target_id for candidate in eligible)),
            tuple(rejected),
            root_count,
            True,
            commit_authorized=False,
        )
    return RoutingDecision(
        RouteStatus.ROUTED,
        chosen.target_id,
        "single eligible route selected after hard gates and semantic policy priority",
        tuple(sorted(candidate.target_id for candidate in eligible)),
        tuple(rejected),
        root_count,
        request.authority_bound,
        commit_authorized=False,
    )


def reference_candidates(scope: str = "reference", regime: str = "active") -> Tuple[RouteCandidate, ...]:
    """Current bounded runtime capability registry; source/canon status stays external."""
    return (
        RouteCandidate(
            "classical-propositional-runtime",
            (QueryKind.CLASSICAL_INFERENCE,),
            (scope,),
            (regime,),
            ("ULK_CLASSICAL_PROPOSITIONAL",),
            ImplementationState.EXECUTABLE_BOUNDED,
            True,
            100,
            True,
            "2026-09-14",
            ("core19-local-repair",),
        ),
        RouteCandidate(
            "alu02-unification-runtime",
            (QueryKind.FIRST_ORDER_TERM_UNIFICATION,),
            (scope,),
            (regime,),
            ("ULK_ALU02_UNIFICATION",),
            ImplementationState.EXECUTABLE_BOUNDED_SUBFRAGMENT,
            True,
            100,
            True,
            "2026-09-14-candidate",
            ("alu02-drive-checker", "alu02-local-integration"),
        ),
        RouteCandidate(
            "alu03-ltlf-finite-trace-runtime",
            (QueryKind.TEMPORAL_FINITE_TRACE_CHECK,),
            (scope,),
            (regime,),
            ("ULK_ALU03_LTLF_FINITE_TRACE",),
            ImplementationState.EXECUTABLE_BOUNDED_SUBFRAGMENT,
            True,
            100,
            True,
            "ULK-v2.1/LTLf-bounded-repair-2026-09-14",
            ("ulk-v2.1-ltlf-local-repair",),
        ),
        RouteCandidate(
            "alu04-modal-k-finite-model-runtime",
            (QueryKind.MODAL_K_FINITE_MODEL_CHECK,),
            (scope,),
            (regime,),
            ("ULK_ALU04_MODAL_K_FINITE_KRIPKE",),
            ImplementationState.EXECUTABLE_BOUNDED_SUBFRAGMENT,
            True,
            100,
            True,
            "ULK-v2.1/modal-K-bounded-repair-2026-09-14",
            ("modal-k-primary-semantics", "alu04-local-repair"),
        ),
        RouteCandidate(
            "alu05-dung-abstract-argumentation-runtime",
            (QueryKind.DUNG_ABSTRACT_FRAMEWORK_CHECK,),
            (scope,),
            (regime,),
            ("ULK_ALU05_DUNG_ARGUMENTATION",),
            ImplementationState.EXECUTABLE_BOUNDED_SUBFRAGMENT,
            True,
            100,
            True,
            "ULK-v2.1/Dung-bounded-repair-2026-09-14",
            ("dung-semantics-source", "alu05-local-repair"),
        ),
        RouteCandidate(
            "quantum-alu07-placeholder",
            (QueryKind.QUANTUM_LOGIC,),
            (scope,),
            (regime,),
            ("ULK_ALU07_QUANTUM",),
            ImplementationState.REBIND_PENDING,
            False,
            100,
            True,
            "ULK-v2.1-claim/rebind-pending",
            ("ulk-v2.1-source",),
        ),
    )
