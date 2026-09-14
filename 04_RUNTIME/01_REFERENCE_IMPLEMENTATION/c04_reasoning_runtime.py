"""Bounded executable C04 Reasoning control-plane runtime.

Origin architect / steward: Trang Phan.

AMOS_MODEL reference implementation. C04 validates a reasoning request and routes
it to already-bound ULK fragment executors. It does not redefine fragment logic,
promote Canon, mint authority, or interpret UNKNOWN/GAP as success.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Tuple

from matrix_registry_runtime import Condition
from ulk_fragment_execution_registry import (
    ExecutionStatus,
    Fragment,
    execution_binding,
)


class ReasoningStatus(Enum):
    ROUTE_BOUNDED = "ROUTE_BOUNDED"
    HOLD_UNKNOWN = "HOLD_UNKNOWN"
    HOLD_COMPETING = "HOLD_COMPETING"
    REVALIDATE_STALE = "REVALIDATE_STALE"
    BLOCK_SCHEMA_DRIFT = "BLOCK_SCHEMA_DRIFT"
    BLOCK_UPSTREAM = "BLOCK_UPSTREAM"
    HOLD_FRAGMENT_GAP = "HOLD_FRAGMENT_GAP"


@dataclass(frozen=True)
class FragmentRoute:
    fragment: Fragment
    checker: str
    scope: str
    execution_identity: str

    def __post_init__(self) -> None:
        if not isinstance(self.fragment, Fragment):
            raise ValueError("fragment must be a Fragment")
        if not self.checker.strip() or not self.scope.strip() or not self.execution_identity.strip():
            raise ValueError("fragment route must bind checker, scope, and execution identity")


@dataclass(frozen=True)
class ReasoningRequest:
    request_id: str
    state_version: str
    provenance_ids: Tuple[str, ...]
    requested_fragments: Tuple[Fragment, ...]
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
        if not self.provenance_ids:
            raise ValueError("C04 cannot emit output without provenance")
        if len(set(self.provenance_ids)) != len(self.provenance_ids):
            raise ValueError("provenance_ids must be unique")
        if any(not isinstance(item, str) or not item.strip() for item in self.provenance_ids):
            raise ValueError("provenance_ids must contain non-empty strings")
        if not self.requested_fragments:
            raise ValueError("requested_fragments must be non-empty")
        if any(not isinstance(fragment, Fragment) for fragment in self.requested_fragments):
            raise ValueError("requested_fragments must contain Fragment values")
        if len(set(self.requested_fragments)) != len(self.requested_fragments):
            raise ValueError("requested_fragments must be unique")
        if not isinstance(self.upstream_condition, Condition):
            raise ValueError("upstream_condition must be a Condition")
        if len(set(self.unknown_gaps)) != len(self.unknown_gaps):
            raise ValueError("unknown_gaps must be unique")
        if any(not isinstance(item, str) or not item.strip() for item in self.unknown_gaps):
            raise ValueError("unknown_gaps must contain non-empty strings")


@dataclass(frozen=True)
class ReasoningResult:
    status: ReasoningStatus
    request_id: str
    state_version: str
    provenance_ids: Tuple[str, ...]
    routes: Tuple[FragmentRoute, ...]
    gap_fragments: Tuple[Fragment, ...]
    reasons: Tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.request_id.strip() or not self.state_version.strip():
            raise ValueError("result identity must be explicit")
        if not self.provenance_ids:
            raise ValueError("C04 result cannot lose provenance")
        if not self.reasons:
            raise ValueError("C04 result requires at least one reason")
        if self.status is ReasoningStatus.ROUTE_BOUNDED and not self.routes:
            raise ValueError("ROUTE_BOUNDED requires at least one route")
        if self.status is ReasoningStatus.HOLD_FRAGMENT_GAP and not self.gap_fragments:
            raise ValueError("HOLD_FRAGMENT_GAP requires fragment identities")

    @property
    def bounded_route_ready(self) -> bool:
        return self.status is ReasoningStatus.ROUTE_BOUNDED


def _result(
    request: ReasoningRequest,
    status: ReasoningStatus,
    *reasons: str,
    routes: Tuple[FragmentRoute, ...] = (),
    gap_fragments: Tuple[Fragment, ...] = (),
) -> ReasoningResult:
    return ReasoningResult(
        status=status,
        request_id=request.request_id,
        state_version=request.state_version,
        provenance_ids=request.provenance_ids,
        routes=routes,
        gap_fragments=gap_fragments,
        reasons=tuple(reasons),
    )


def _binding_identity(binding) -> str:
    if binding.checker_sha256:
        return f"sha256:{binding.checker_sha256}"
    if binding.source_revision_id and binding.source_method_ast_sha256:
        return f"source:{binding.source_revision_id}:ast:{binding.source_method_ast_sha256}"
    return f"registry:{binding.status.value}:{binding.checker}"


def evaluate_reasoning(request: ReasoningRequest) -> ReasoningResult:
    """Validate C04 and route only to bounded executable ULK fragments."""
    if (
        request.input_schema_hash != request.expected_input_schema_hash
        or request.output_schema_hash != request.expected_output_schema_hash
    ):
        return _result(request, ReasoningStatus.BLOCK_SCHEMA_DRIFT, "SCHEMA_FINGERPRINT_MISMATCH")

    if request.observed_epoch != request.required_epoch or request.upstream_condition is Condition.STALE:
        return _result(request, ReasoningStatus.REVALIDATE_STALE, "FRESHNESS_EPOCH_MISMATCH_OR_STALE_UPSTREAM")

    if request.upstream_condition is Condition.COMPETING:
        return _result(request, ReasoningStatus.HOLD_COMPETING, "UPSTREAM_COMPETING_PRESERVED")

    if request.upstream_condition in (Condition.QUARANTINED, Condition.FALSIFIED):
        return _result(
            request,
            ReasoningStatus.BLOCK_UPSTREAM,
            f"UPSTREAM_{request.upstream_condition.value}",
        )

    if request.unknown_gaps:
        return _result(
            request,
            ReasoningStatus.HOLD_UNKNOWN,
            "UNKNOWN_GAP_PRESENT",
            *request.unknown_gaps,
        )

    routes = []
    gaps = []
    executable_statuses = {
        ExecutionStatus.EXECUTABLE_BOUNDED,
        ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
    }
    for fragment in request.requested_fragments:
        binding = execution_binding(fragment)
        if binding.status not in executable_statuses or not binding.checker:
            gaps.append(fragment)
            continue
        routes.append(
            FragmentRoute(
                fragment=fragment,
                checker=binding.checker,
                scope=binding.scope,
                execution_identity=_binding_identity(binding),
            )
        )

    if gaps:
        return _result(
            request,
            ReasoningStatus.HOLD_FRAGMENT_GAP,
            "REQUESTED_FRAGMENT_LACKS_BOUNDED_EXECUTABLE_BINDING",
            gap_fragments=tuple(gaps),
        )

    return _result(
        request,
        ReasoningStatus.ROUTE_BOUNDED,
        "C04_PROVENANCE_FRESHNESS_SCHEMA_AND_FRAGMENT_GATES_SATISFIED",
        "ROUTE_BOUNDED_IS_NOT_PASS_OR_CANON_PROMOTION",
        routes=tuple(routes),
    )
