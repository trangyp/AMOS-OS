"""Bounded finite-trace temporal logic runtime for AMOS ULK ALU-03.

Origin architect / steward: Trang Phan.

This module implements an explicit LTLf-style finite-trace subfragment with strong
NEXT plus EVENTUALLY, GLOBALLY, and UNTIL. It also provides bounded finite-state
path exploration. It is not standard infinite-trace LTL model checking, does not
prove an unbounded temporal property, and temporal ordering never implies causation.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from typing import Any, FrozenSet, Mapping, Optional, Sequence, Tuple


class TemporalStatus(Enum):
    SATISFIED = "SATISFIED"
    VIOLATED = "VIOLATED"
    COUNTEREXAMPLE_WITHIN_BOUND = "COUNTEREXAMPLE_WITHIN_BOUND"
    ALL_CHECKED_PATHS_SATISFY_BOUND = "ALL_CHECKED_PATHS_SATISFY_BOUND"
    REJECT_MALFORMED_REQUEST = "REJECT_MALFORMED_REQUEST"
    RESOURCE_BOUND_EXCEEDED = "RESOURCE_BOUND_EXCEEDED"


class FormulaKind(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
    ATOM = "ATOM"
    NOT = "NOT"
    AND = "AND"
    OR = "OR"
    NEXT = "NEXT"
    EVENTUALLY = "EVENTUALLY"
    GLOBALLY = "GLOBALLY"
    UNTIL = "UNTIL"


class TemporalError(ValueError):
    pass


class TemporalResourceBound(TemporalError):
    pass


@dataclass(frozen=True)
class Formula:
    kind: FormulaKind
    atom: Optional[str] = None
    children: Tuple["Formula", ...] = ()

    def __post_init__(self) -> None:
        if self.kind is FormulaKind.ATOM:
            if self.atom is None or not self.atom.strip() or self.children:
                raise TemporalError("ATOM requires one non-empty atom and no children")
        elif self.kind in {FormulaKind.TRUE, FormulaKind.FALSE}:
            if self.atom is not None or self.children:
                raise TemporalError(f"{self.kind.value} takes no payload")
        elif self.kind in {FormulaKind.NOT, FormulaKind.NEXT, FormulaKind.EVENTUALLY, FormulaKind.GLOBALLY}:
            if self.atom is not None or len(self.children) != 1:
                raise TemporalError(f"{self.kind.value} requires exactly one child")
        elif self.kind in {FormulaKind.AND, FormulaKind.OR, FormulaKind.UNTIL}:
            if self.atom is not None or len(self.children) != 2:
                raise TemporalError(f"{self.kind.value} requires exactly two children")


@dataclass(frozen=True)
class TemporalBounds:
    max_formula_nodes: int = 10_000
    max_formula_depth: int = 256
    max_trace_length: int = 10_000
    max_paths: int = 100_000
    max_path_steps: int = 256

    def __post_init__(self) -> None:
        if min(self.max_formula_nodes, self.max_formula_depth, self.max_trace_length, self.max_paths, self.max_path_steps) <= 0:
            raise ValueError("temporal bounds must be positive")


@dataclass(frozen=True)
class TraceResult:
    status: TemporalStatus
    value: Optional[bool]
    reason: str
    trace_length: int
    semantics: str = "LTLf_finite_trace_strong_next"
    canon_promoted: bool = False
    causal_claim: bool = False
    effect_authority: bool = False


@dataclass(frozen=True)
class TransitionSystem:
    states: Tuple[str, ...]
    initial_states: Tuple[str, ...]
    labels: Mapping[str, FrozenSet[str]]
    transitions: Mapping[str, Tuple[str, ...]]

    def __post_init__(self) -> None:
        if not self.states or len(self.states) != len(set(self.states)):
            raise TemporalError("states must be non-empty and unique")
        state_set = set(self.states)
        if not self.initial_states or not set(self.initial_states).issubset(state_set):
            raise TemporalError("initial states must be declared states")
        if set(self.labels) != state_set or set(self.transitions) != state_set:
            raise TemporalError("labels/transitions must cover exactly the declared states")
        for state in self.states:
            if not state.strip():
                raise TemporalError("state ids must be non-empty")
            if any((not atom.strip()) for atom in self.labels[state]):
                raise TemporalError("labels must contain non-empty atoms")
            if not set(self.transitions[state]).issubset(state_set):
                raise TemporalError("transition target is undeclared")


@dataclass(frozen=True)
class BoundedPathResult:
    status: TemporalStatus
    checked_paths: int
    bound_steps: int
    counterexample_states: Tuple[str, ...] = ()
    reason: str = ""
    semantics: str = "bounded_path_enumeration_over_LTLf_prefixes"
    unbounded_proof: bool = False
    causal_claim: bool = False
    effect_authority: bool = False


def parse_formula(value: Any, *, bounds: TemporalBounds, _depth: int = 0, _counter: Optional[list[int]] = None) -> Formula:
    if _counter is None:
        _counter = [0]
    _counter[0] += 1
    if _counter[0] > bounds.max_formula_nodes:
        raise TemporalResourceBound("formula node bound exceeded")
    if _depth > bounds.max_formula_depth:
        raise TemporalResourceBound("formula depth bound exceeded")
    if not isinstance(value, dict) or len(value) != 1:
        raise TemporalError("formula must be a single-key object")
    key, payload = next(iter(value.items()))
    if key == "true" and payload is True:
        return Formula(FormulaKind.TRUE)
    if key == "false" and payload is True:
        return Formula(FormulaKind.FALSE)
    if key == "atom" and isinstance(payload, str) and payload.strip():
        return Formula(FormulaKind.ATOM, atom=payload)
    unary = {"not": FormulaKind.NOT, "next": FormulaKind.NEXT, "eventually": FormulaKind.EVENTUALLY, "globally": FormulaKind.GLOBALLY}
    if key in unary:
        return Formula(unary[key], children=(parse_formula(payload, bounds=bounds, _depth=_depth + 1, _counter=_counter),))
    binary = {"and": FormulaKind.AND, "or": FormulaKind.OR, "until": FormulaKind.UNTIL}
    if key in binary and isinstance(payload, list) and len(payload) == 2:
        return Formula(binary[key], children=tuple(parse_formula(item, bounds=bounds, _depth=_depth + 1, _counter=_counter) for item in payload))
    raise TemporalError("unsupported or malformed finite-trace temporal formula")


def normalize_trace(value: Any, *, bounds: TemporalBounds) -> Tuple[FrozenSet[str], ...]:
    if not isinstance(value, list) or not value:
        raise TemporalError("finite trace must be a non-empty list")
    if len(value) > bounds.max_trace_length:
        raise TemporalResourceBound("trace length bound exceeded")
    out = []
    for state in value:
        if not isinstance(state, list) or any(not isinstance(atom, str) or not atom.strip() for atom in state):
            raise TemporalError("each trace position must be a list of non-empty atomic proposition names")
        out.append(frozenset(state))
    return tuple(out)


def evaluate(formula: Formula, trace: Sequence[FrozenSet[str]], position: int = 0) -> bool:
    """Evaluate explicit finite-trace semantics; NEXT is strong at the final state."""
    if not trace or position < 0 or position >= len(trace):
        raise TemporalError("evaluation position must be inside a non-empty trace")

    @lru_cache(maxsize=None)
    def ev(node: Formula, i: int) -> bool:
        kind = node.kind
        if kind is FormulaKind.TRUE: return True
        if kind is FormulaKind.FALSE: return False
        if kind is FormulaKind.ATOM:
            assert node.atom is not None
            return node.atom in trace[i]
        if kind is FormulaKind.NOT: return not ev(node.children[0], i)
        if kind is FormulaKind.AND: return ev(node.children[0], i) and ev(node.children[1], i)
        if kind is FormulaKind.OR: return ev(node.children[0], i) or ev(node.children[1], i)
        if kind is FormulaKind.NEXT: return i + 1 < len(trace) and ev(node.children[0], i + 1)
        if kind is FormulaKind.EVENTUALLY: return any(ev(node.children[0], j) for j in range(i, len(trace)))
        if kind is FormulaKind.GLOBALLY: return all(ev(node.children[0], j) for j in range(i, len(trace)))
        if kind is FormulaKind.UNTIL:
            left, right = node.children
            return any(ev(right, j) and all(ev(left, k) for k in range(i, j)) for j in range(i, len(trace)))
        raise AssertionError(f"unhandled formula kind: {kind}")

    return ev(formula, position)


def run_trace_request(request: Any, *, bounds: TemporalBounds = TemporalBounds()) -> TraceResult:
    if not isinstance(request, dict) or set(request) != {"formula", "trace"}:
        return TraceResult(TemporalStatus.REJECT_MALFORMED_REQUEST, None, "request must contain exactly formula and trace", 0)
    try:
        formula = parse_formula(request["formula"], bounds=bounds)
        trace = normalize_trace(request["trace"], bounds=bounds)
        value = evaluate(formula, trace)
        return TraceResult(TemporalStatus.SATISFIED if value else TemporalStatus.VIOLATED, value, "finite-trace temporal formula evaluated under explicit LTLf semantics", len(trace))
    except TemporalResourceBound as exc:
        return TraceResult(TemporalStatus.RESOURCE_BOUND_EXCEEDED, None, str(exc), 0)
    except TemporalError as exc:
        return TraceResult(TemporalStatus.REJECT_MALFORMED_REQUEST, None, str(exc), 0)


def _path_trace(ts: TransitionSystem, path: Sequence[str]) -> Tuple[FrozenSet[str], ...]:
    return tuple(ts.labels[state] for state in path)


def check_all_paths_bounded(ts: TransitionSystem, formula: Formula, *, max_steps: int, bounds: TemporalBounds = TemporalBounds()) -> BoundedPathResult:
    """Check all dead-end or max-bound paths; never upgrades finite bound to unbounded proof."""
    if max_steps < 0 or max_steps > bounds.max_path_steps:
        return BoundedPathResult(TemporalStatus.RESOURCE_BOUND_EXCEEDED, 0, max_steps, reason="path-step bound exceeded")
    checked = 0
    stack: list[Tuple[str, ...]] = [(s,) for s in reversed(sorted(ts.initial_states))]
    while stack:
        path = stack.pop()
        state = path[-1]
        steps = len(path) - 1
        successors = tuple(sorted(ts.transitions[state]))
        terminal_for_bound = steps >= max_steps or not successors
        if terminal_for_bound:
            checked += 1
            if checked > bounds.max_paths:
                return BoundedPathResult(TemporalStatus.RESOURCE_BOUND_EXCEEDED, checked - 1, max_steps, reason="path-count bound exceeded")
            if not evaluate(formula, _path_trace(ts, path)):
                return BoundedPathResult(TemporalStatus.COUNTEREXAMPLE_WITHIN_BOUND, checked, max_steps, tuple(path), "finite path violates the LTLf formula within the explored bound")
            continue
        for nxt in reversed(successors):
            stack.append(path + (nxt,))
    return BoundedPathResult(TemporalStatus.ALL_CHECKED_PATHS_SATISFY_BOUND, checked, max_steps, reason="all enumerated finite paths satisfy the formula within the declared bound")
