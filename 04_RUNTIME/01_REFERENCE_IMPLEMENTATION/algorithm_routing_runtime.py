"""Deterministic routing over the provenance-bound AMOS algorithm registry.

Origin architect / steward: Trang Phan.

This module makes ``internet_algorithm_registry.py`` the routing owner for
algorithm capability selection. It does not download, install, or execute an
external solver. A selected external-only algorithm is capability metadata and
must still be bound to an authorized tool/runtime before execution.

Hard boundaries:
- ELIGIBLE != CORRECT_FOR_UNSTATED_OBJECTIVE
- ROUTED != EXECUTED
- EXECUTED != VERIFIED_OUTSIDE_CONTRACT
- CAPABILITY != AUTHORITY
- NO_MATCH -> UNKNOWN/GAP, never guessed fallback
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import FrozenSet, Optional, Tuple

from internet_algorithm_registry import (
    REGISTRY,
    AlgorithmSpec,
    GuaranteeClass,
    ProblemFamily,
    eligible,
)


class RouteStatus(Enum):
    ROUTED_LOCAL = "ROUTED_LOCAL"
    ROUTED_EXTERNAL_CAPABILITY = "ROUTED_EXTERNAL_CAPABILITY"
    UNKNOWN_GAP = "UNKNOWN/GAP"


@dataclass(frozen=True)
class AlgorithmRequest:
    family: ProblemFamily
    supplied_preconditions: FrozenSet[str]
    require_exact: bool = False
    local_only: bool = False
    prefer_local: bool = True

    def __post_init__(self) -> None:
        if any(not item.strip() for item in self.supplied_preconditions):
            raise ValueError("supplied preconditions must be non-empty strings")


@dataclass(frozen=True)
class AlgorithmRoute:
    status: RouteStatus
    algorithm: Optional[str]
    implementation_binding: Optional[str]
    grants_authority: bool
    reason: str
    alternatives: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.grants_authority:
            raise ValueError("algorithm routing may not grant authority")
        if self.status is RouteStatus.UNKNOWN_GAP and self.algorithm is not None:
            raise ValueError("UNKNOWN/GAP route may not name an executable algorithm")
        if self.status is not RouteStatus.UNKNOWN_GAP and not self.algorithm:
            raise ValueError("routed result requires an algorithm identity")


_EXACT_GUARANTEES = frozenset(
    {GuaranteeClass.EXACT, GuaranteeClass.EXACT_IF_PRECONDITIONS}
)

_GUARANTEE_RANK = {
    GuaranteeClass.EXACT: 0,
    GuaranteeClass.EXACT_IF_PRECONDITIONS: 1,
    GuaranteeClass.SOLVER_STATUS_BOUND: 2,
    GuaranteeClass.HEURISTIC: 3,
}


def eligible_candidates(request: AlgorithmRequest) -> Tuple[AlgorithmSpec, ...]:
    candidates = []
    for name, spec in REGISTRY.items():
        if spec.family is not request.family:
            continue
        if request.local_only and spec.implementation_binding is None:
            continue
        if request.require_exact and spec.guarantee not in _EXACT_GUARANTEES:
            continue
        if not eligible(name, request.supplied_preconditions):
            continue
        candidates.append(spec)

    def key(spec: AlgorithmSpec) -> tuple[int, int, str]:
        locality = 0 if spec.implementation_binding is not None else 1
        if not request.prefer_local:
            locality = 0
        return locality, _GUARANTEE_RANK[spec.guarantee], spec.name

    candidates.sort(key=key)
    return tuple(candidates)


def route_algorithm(request: AlgorithmRequest) -> AlgorithmRoute:
    candidates = eligible_candidates(request)
    if not candidates:
        qualifiers = []
        if request.local_only:
            qualifiers.append("local implementation")
        if request.require_exact:
            qualifiers.append("exact guarantee")
        qualifier_text = ", ".join(qualifiers) if qualifiers else "declared preconditions"
        return AlgorithmRoute(
            RouteStatus.UNKNOWN_GAP,
            None,
            None,
            False,
            f"no {request.family.value} candidate satisfies {qualifier_text}",
            (),
        )

    selected = candidates[0]
    status = (
        RouteStatus.ROUTED_LOCAL
        if selected.implementation_binding is not None
        else RouteStatus.ROUTED_EXTERNAL_CAPABILITY
    )
    return AlgorithmRoute(
        status,
        selected.name,
        selected.implementation_binding,
        False,
        "candidate selected from typed family + explicit preconditions + routing policy",
        tuple(spec.name for spec in candidates[1:]),
    )


def route_named_algorithm(
    name: str,
    supplied_preconditions: FrozenSet[str],
    *,
    require_local: bool = False,
) -> AlgorithmRoute:
    """Fail-closed route for a caller-requested algorithm identity."""
    spec = REGISTRY.get(name)
    if spec is None:
        return AlgorithmRoute(RouteStatus.UNKNOWN_GAP, None, None, False, "unknown algorithm identity")
    if require_local and spec.implementation_binding is None:
        return AlgorithmRoute(
            RouteStatus.UNKNOWN_GAP,
            None,
            None,
            False,
            "algorithm is registered as external capability metadata only",
        )
    if not eligible(name, supplied_preconditions):
        return AlgorithmRoute(
            RouteStatus.UNKNOWN_GAP,
            None,
            None,
            False,
            "declared preconditions do not satisfy algorithm contract",
        )
    status = (
        RouteStatus.ROUTED_LOCAL
        if spec.implementation_binding is not None
        else RouteStatus.ROUTED_EXTERNAL_CAPABILITY
    )
    return AlgorithmRoute(status, name, spec.implementation_binding, False, "named algorithm contract satisfied")
