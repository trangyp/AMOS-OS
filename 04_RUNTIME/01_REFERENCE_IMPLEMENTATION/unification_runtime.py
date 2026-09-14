"""Bounded first-order term unification for AMOS ULK ALU-02.

Origin architect / steward: Trang Phan.

This module implements only finite first-order term unification with occurs-check.
It is not quantifier inference, resolution, model finding, higher-order unification,
or a complete first-order theorem prover. It proposes a bounded logic result and
has no Canon-promotion or effect authority.

The source candidate/receipt is bound to the 2026-09-14 _00_AMOS_CANON ALU-02
checker. This runtime adds explicit resource bounds and a typed internal ABI while
preserving the source JSON term ABI at the boundary.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Iterable, Mapping, Optional, Tuple, Union


class UnificationStatus(Enum):
    UNIFIED = "UNIFIED"
    NOT_UNIFIABLE = "NOT_UNIFIABLE"
    REJECT_MALFORMED_REQUEST = "REJECT_MALFORMED_REQUEST"
    RESOURCE_BOUND_EXCEEDED = "RESOURCE_BOUND_EXCEEDED"
    INTERNAL_CHECK_FAILED = "INTERNAL_CHECK_FAILED"


class UnificationError(ValueError):
    pass


class ResourceBoundExceeded(UnificationError):
    pass


@dataclass(frozen=True)
class Var:
    name: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise UnificationError("variable name must be non-empty")


@dataclass(frozen=True)
class Const:
    symbol: str

    def __post_init__(self) -> None:
        if not self.symbol.strip():
            raise UnificationError("constant symbol must be non-empty")


@dataclass(frozen=True)
class Fun:
    symbol: str
    args: Tuple["Term", ...]

    def __post_init__(self) -> None:
        if not self.symbol.strip():
            raise UnificationError("function symbol must be non-empty")


Term = Union[Var, Const, Fun]
Substitution = Dict[str, Term]


@dataclass(frozen=True)
class UnificationBounds:
    max_nodes_per_term: int = 10_000
    max_depth: int = 256
    max_equation_steps: int = 100_000

    def __post_init__(self) -> None:
        if self.max_nodes_per_term <= 0 or self.max_depth <= 0 or self.max_equation_steps <= 0:
            raise ValueError("unification bounds must be positive")


@dataclass(frozen=True)
class UnificationResult:
    status: UnificationStatus
    substitution: Optional[Mapping[str, Any]]
    reason: str
    verified_scope: str = "finite_first_order_term_unification_with_occurs_check"
    canonical_fragment: str = "ULK_ALU02_FIRST_ORDER_LOGIC_UNIFICATION"
    source_profile: str = "ULK_ALU02_FIRST_ORDER_UNIFICATION_EXECUTABLE_PROFILE_V1_CANDIDATE"
    canon_promoted: bool = False
    effect_authority: bool = False


def parse_term(value: Any, *, bounds: UnificationBounds, _depth: int = 0, _counter: Optional[list[int]] = None) -> Term:
    if _counter is None:
        _counter = [0]
    _counter[0] += 1
    if _counter[0] > bounds.max_nodes_per_term:
        raise ResourceBoundExceeded("term node bound exceeded")
    if _depth > bounds.max_depth:
        raise ResourceBoundExceeded("term depth bound exceeded")
    if not isinstance(value, dict):
        raise UnificationError("term must be an object")
    keys = set(value)
    if keys == {"var"} and isinstance(value["var"], str) and value["var"].strip():
        return Var(value["var"])
    if keys == {"const"} and isinstance(value["const"], str) and value["const"].strip():
        return Const(value["const"])
    if keys == {"fun", "args"} and isinstance(value["fun"], str) and value["fun"].strip() and isinstance(value["args"], list):
        return Fun(
            value["fun"],
            tuple(parse_term(arg, bounds=bounds, _depth=_depth + 1, _counter=_counter) for arg in value["args"]),
        )
    raise UnificationError("malformed first-order term")


def term_to_json(term: Term) -> Dict[str, Any]:
    if isinstance(term, Var):
        return {"var": term.name}
    if isinstance(term, Const):
        return {"const": term.symbol}
    return {"fun": term.symbol, "args": [term_to_json(arg) for arg in term.args]}


def walk(term: Term, subst: Mapping[str, Term]) -> Term:
    seen = set()
    while isinstance(term, Var) and term.name in subst:
        if term.name in seen:
            raise UnificationError("cyclic substitution detected")
        seen.add(term.name)
        term = subst[term.name]
    return term


def apply_substitution(term: Term, subst: Mapping[str, Term]) -> Term:
    term = walk(term, subst)
    if isinstance(term, Fun):
        return Fun(term.symbol, tuple(apply_substitution(arg, subst) for arg in term.args))
    return term


def occurs(variable: str, term: Term, subst: Mapping[str, Term]) -> bool:
    term = walk(term, subst)
    if isinstance(term, Var):
        return term.name == variable
    if isinstance(term, Const):
        return False
    return any(occurs(variable, arg, subst) for arg in term.args)


def normalize_substitution(subst: Mapping[str, Term]) -> Substitution:
    out = {name: apply_substitution(term, subst) for name, term in subst.items()}
    return {name: term for name, term in out.items() if term != Var(name)}


def _bind(variable: str, term: Term, subst: Substitution) -> Substitution:
    term = walk(term, subst)
    if term == Var(variable):
        return subst
    if occurs(variable, term, subst):
        raise UnificationError(f"occurs-check failed for {variable}")
    out = dict(subst)
    out[variable] = term
    return normalize_substitution(out)


def unify(left: Term, right: Term, *, bounds: UnificationBounds = UnificationBounds()) -> Substitution:
    """Robinson/Martelli-Montanari style bounded first-order unification.

    The worklist orientation and decomposition are implementation choices; the
    semantic contract is to return a substitution sigma with sigma(left)=sigma(right)
    when the supported finite term fragment is unifiable, while enforcing occurs-check.
    """
    equations: list[Tuple[Term, Term]] = [(left, right)]
    subst: Substitution = {}
    steps = 0
    while equations:
        steps += 1
        if steps > bounds.max_equation_steps:
            raise ResourceBoundExceeded("equation-step bound exceeded")
        a, b = equations.pop()
        a = apply_substitution(a, subst)
        b = apply_substitution(b, subst)
        if a == b:
            continue
        if isinstance(a, Var):
            subst = _bind(a.name, b, subst)
            continue
        if isinstance(b, Var):
            subst = _bind(b.name, a, subst)
            continue
        if isinstance(a, Const) and isinstance(b, Const):
            raise UnificationError("constant mismatch")
        if isinstance(a, Fun) and isinstance(b, Fun):
            if a.symbol != b.symbol or len(a.args) != len(b.args):
                raise UnificationError("function symbol/arity mismatch")
            equations.extend(zip(a.args, b.args))
            continue
        raise UnificationError("term-constructor mismatch")
    subst = normalize_substitution(subst)
    if apply_substitution(left, subst) != apply_substitution(right, subst):
        raise AssertionError("internal unification soundness check failed")
    return subst


def substitution_to_json(subst: Mapping[str, Term]) -> Dict[str, Any]:
    return {name: term_to_json(term) for name, term in sorted(subst.items())}


def run_request(request: Any, *, bounds: UnificationBounds = UnificationBounds()) -> UnificationResult:
    if not isinstance(request, dict) or set(request) != {"left", "right"}:
        return UnificationResult(
            UnificationStatus.REJECT_MALFORMED_REQUEST,
            None,
            "request must contain exactly left and right",
        )
    try:
        left = parse_term(request["left"], bounds=bounds)
        right = parse_term(request["right"], bounds=bounds)
        subst = unify(left, right, bounds=bounds)
        if apply_substitution(left, subst) != apply_substitution(right, subst):
            return UnificationResult(UnificationStatus.INTERNAL_CHECK_FAILED, None, "returned substitution failed soundness check")
        return UnificationResult(UnificationStatus.UNIFIED, substitution_to_json(subst), "bounded first-order terms unified")
    except ResourceBoundExceeded as exc:
        return UnificationResult(UnificationStatus.RESOURCE_BOUND_EXCEEDED, None, str(exc))
    except UnificationError as exc:
        return UnificationResult(UnificationStatus.NOT_UNIFIABLE, None, str(exc))
