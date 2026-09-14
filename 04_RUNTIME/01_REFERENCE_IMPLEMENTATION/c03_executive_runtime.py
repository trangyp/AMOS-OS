"""Bounded executable C03 Executive control-plane runtime.

Origin architect / steward: Trang Phan.

AMOS_MODEL reference implementation. C03 selects among already-proposed
candidates under explicit hard gates and a declared lexicographic policy. It
never mints C01 governance authority and never dispatches C08 effects.

Decision order for admissible candidates:
  1. maximize declared priority,
  2. minimize declared risk_rank,
  3. minimize declared irreversibility_rank,
  4. minimize declared resource_cost.

If two or more candidates share the exact best decision vector, C03 preserves
COMPETING rather than inventing a tie-break. No weighted pseudo-score is used.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import isfinite
from typing import Tuple

from matrix_registry_runtime import Condition


class ExecutiveStatus(Enum):
    SELECT_PROPOSAL = "SELECT_PROPOSAL"
    HOLD_COMPETING = "HOLD_COMPETING"
    HOLD_UNKNOWN = "HOLD_UNKNOWN"
    HOLD_NO_ADMISSIBLE = "HOLD_NO_ADMISSIBLE"
    REVALIDATE_STALE = "REVALIDATE_STALE"
    BLOCK_SCHEMA_DRIFT = "BLOCK_SCHEMA_DRIFT"
    BLOCK_UPSTREAM = "BLOCK_UPSTREAM"


@dataclass(frozen=True)
class ExecutiveCandidate:
    candidate_id: str
    plan_id: str
    goal_id: str
    priority: int
    risk_rank: int
    irreversibility_rank: int
    resource_cost: float
    hard_constraints_pass: bool
    condition: Condition = Condition.ACTIVE
    provenance_ids: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for value, name in (
            (self.candidate_id, "candidate_id"),
            (self.plan_id, "plan_id"),
            (self.goal_id, "goal_id"),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        if not isinstance(self.priority, int) or not 0 <= self.priority <= 100:
            raise ValueError("priority must be an integer in [0,100]")
        if not isinstance(self.risk_rank, int) or self.risk_rank < 0:
            raise ValueError("risk_rank must be a non-negative integer")
        if not isinstance(self.irreversibility_rank, int) or self.irreversibility_rank < 0:
            raise ValueError("irreversibility_rank must be a non-negative integer")
        if not isinstance(self.resource_cost, (int, float)) or not isfinite(float(self.resource_cost)) or self.resource_cost < 0:
            raise ValueError("resource_cost must be finite and non-negative")
        if type(self.hard_constraints_pass) is not bool:
            raise ValueError("hard_constraints_pass must be bool")
        if not isinstance(self.condition, Condition):
            raise ValueError("condition must be a Condition")
        if not self.provenance_ids or any(not isinstance(x, str) or not x.strip() for x in self.provenance_ids):
            raise ValueError("candidate provenance_ids must contain non-empty strings")
        if len(set(self.provenance_ids)) != len(self.provenance_ids):
            raise ValueError("candidate provenance_ids must be unique")

    @property
    def decision_vector(self) -> tuple[int, int, int, float]:
        return (-self.priority, self.risk_rank, self.irreversibility_rank, float(self.resource_cost))


@dataclass(frozen=True)
class ExecutiveRequest:
    request_id: str
    state_version: str
    candidates: Tuple[ExecutiveCandidate, ...]
    input_schema_hash: str
    expected_input_schema_hash: str
    output_schema_hash: str
    expected_output_schema_hash: str
    observed_epoch: str
    required_epoch: str
    upstream_condition: Condition = Condition.ACTIVE
    unknown_gaps: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for value, name in (
            (self.request_id, "request_id"),
            (self.state_version, "state_version"),
            (self.input_schema_hash, "input_schema_hash"),
            (self.expected_input_schema_hash, "expected_input_schema_hash"),
            (self.output_schema_hash, "output_schema_hash"),
            (self.expected_output_schema_hash, "expected_output_schema_hash"),
            (self.observed_epoch, "observed_epoch"),
            (self.required_epoch, "required_epoch"),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        if not self.candidates:
            raise ValueError("candidates must be non-empty")
        ids = tuple(c.candidate_id for c in self.candidates)
        if len(set(ids)) != len(ids):
            raise ValueError("candidate_id values must be unique")
        if not isinstance(self.upstream_condition, Condition):
            raise ValueError("upstream_condition must be a Condition")
        if len(set(self.unknown_gaps)) != len(self.unknown_gaps):
            raise ValueError("unknown_gaps must be unique")
        if any(not isinstance(x, str) or not x.strip() for x in self.unknown_gaps):
            raise ValueError("unknown_gaps must contain non-empty strings")


@dataclass(frozen=True)
class ExecutiveResult:
    status: ExecutiveStatus
    request_id: str
    state_version: str
    selected_candidate_id: str | None
    competing_candidate_ids: Tuple[str, ...]
    rejected_candidate_ids: Tuple[str, ...]
    provenance_ids: Tuple[str, ...]
    reasons: Tuple[str, ...]
    requires_c01_authorization: bool = True
    execution_authorized: bool = False

    def __post_init__(self) -> None:
        if not self.request_id.strip() or not self.state_version.strip():
            raise ValueError("result identity must be explicit")
        if not self.reasons:
            raise ValueError("result requires at least one reason")
        if self.execution_authorized:
            raise ValueError("C03 cannot authorize execution")
        if not self.requires_c01_authorization:
            raise ValueError("C03 output must remain subject to C01 authorization")
        if self.status is ExecutiveStatus.SELECT_PROPOSAL and not self.selected_candidate_id:
            raise ValueError("SELECT_PROPOSAL requires selected_candidate_id")
        if self.status is ExecutiveStatus.HOLD_COMPETING and not self.competing_candidate_ids:
            raise ValueError("HOLD_COMPETING requires competing evidence or candidates")


def _result(request: ExecutiveRequest, status: ExecutiveStatus, *reasons: str,
            selected: str | None = None, competing: Tuple[str, ...] = (),
            rejected: Tuple[str, ...] = (), provenance: Tuple[str, ...] = ()) -> ExecutiveResult:
    return ExecutiveResult(
        status=status,
        request_id=request.request_id,
        state_version=request.state_version,
        selected_candidate_id=selected,
        competing_candidate_ids=competing,
        rejected_candidate_ids=rejected,
        provenance_ids=provenance,
        reasons=tuple(reasons),
    )


def evaluate_executive(request: ExecutiveRequest) -> ExecutiveResult:
    """Return a bounded executive proposal; never return execution authority."""
    if request.input_schema_hash != request.expected_input_schema_hash or request.output_schema_hash != request.expected_output_schema_hash:
        return _result(request, ExecutiveStatus.BLOCK_SCHEMA_DRIFT, "SCHEMA_FINGERPRINT_MISMATCH")
    if request.observed_epoch != request.required_epoch or request.upstream_condition is Condition.STALE:
        return _result(request, ExecutiveStatus.REVALIDATE_STALE, "FRESHNESS_EPOCH_MISMATCH_OR_STALE_UPSTREAM")
    if request.upstream_condition is Condition.COMPETING:
        return _result(request, ExecutiveStatus.HOLD_COMPETING, "UPSTREAM_COMPETING_PRESERVED",
                       competing=tuple(sorted(c.candidate_id for c in request.candidates)))
    if request.upstream_condition in (Condition.QUARANTINED, Condition.FALSIFIED):
        return _result(request, ExecutiveStatus.BLOCK_UPSTREAM, f"UPSTREAM_{request.upstream_condition.value}")
    if request.unknown_gaps:
        return _result(request, ExecutiveStatus.HOLD_UNKNOWN, "UNKNOWN_GAP_PRESENT", *request.unknown_gaps)

    admissible = []
    rejected = []
    for candidate in request.candidates:
        if not candidate.hard_constraints_pass or candidate.condition in (Condition.FALSIFIED, Condition.QUARANTINED, Condition.STALE):
            rejected.append(candidate.candidate_id)
            continue
        if candidate.condition is Condition.COMPETING:
            return _result(
                request,
                ExecutiveStatus.HOLD_COMPETING,
                "CANDIDATE_COMPETING_EVIDENCE_PRESERVED",
                competing=(candidate.candidate_id,),
                rejected=tuple(sorted(rejected)),
                provenance=candidate.provenance_ids,
            )
        admissible.append(candidate)

    if not admissible:
        return _result(request, ExecutiveStatus.HOLD_NO_ADMISSIBLE, "NO_CANDIDATE_PASSED_HARD_GATES",
                       rejected=tuple(sorted(rejected)))

    best_vector = min(candidate.decision_vector for candidate in admissible)
    best = tuple(sorted((c for c in admissible if c.decision_vector == best_vector), key=lambda c: c.candidate_id))
    provenance = tuple(sorted({p for c in best for p in c.provenance_ids}))

    if len(best) > 1:
        return _result(
            request,
            ExecutiveStatus.HOLD_COMPETING,
            "EXACT_DECISION_VECTOR_TIE_PRESERVED",
            competing=tuple(c.candidate_id for c in best),
            rejected=tuple(sorted(rejected)),
            provenance=provenance,
        )

    return _result(
        request,
        ExecutiveStatus.SELECT_PROPOSAL,
        "LEXICOGRAPHIC_POLICY_SELECTED_ONE_ADMISSIBLE_PROPOSAL",
        "SELECTION_IS_NOT_C01_AUTHORIZATION_OR_C08_EXECUTION",
        selected=best[0].candidate_id,
        rejected=tuple(sorted(rejected)),
        provenance=provenance,
    )
