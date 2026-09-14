"""Bounded explicit Dung abstract argumentation runtime for AMOS ULK ALU-05.

Origin architect / steward: Trang Phan.

Implements a finite abstract argumentation framework AF=(A,R) directly. It does
not infer attacks from confidence, similarity, contradiction labels, or language.
Those are upstream modeling choices and must remain separate from Dung semantics.
Attack edges are formal argumentation edges, not causal or empirical relations.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, FrozenSet, Iterable, Tuple


class ArgumentationStatus(Enum):
    VERIFIED_BOUNDED = "VERIFIED_BOUNDED"
    REJECT_MALFORMED_REQUEST = "REJECT_MALFORMED_REQUEST"
    RESOURCE_BOUND_EXCEEDED = "RESOURCE_BOUND_EXCEEDED"


class ArgumentationError(ValueError):
    pass


@dataclass(frozen=True)
class ArgumentationBounds:
    max_arguments: int = 10_000
    max_attacks: int = 200_000
    max_iterations: int = 10_001

    def __post_init__(self) -> None:
        if min(self.max_arguments, self.max_attacks, self.max_iterations) <= 0:
            raise ValueError("argumentation bounds must be positive")


@dataclass(frozen=True)
class ArgumentationFramework:
    arguments: Tuple[str, ...]
    attacks: Tuple[Tuple[str, str], ...]

    def validate(self, bounds: ArgumentationBounds = ArgumentationBounds()) -> None:
        if len(self.arguments) > bounds.max_arguments:
            raise ArgumentationError("argument count bound exceeded")
        if len(self.attacks) > bounds.max_attacks:
            raise ArgumentationError("attack count bound exceeded")
        if len(self.arguments) != len(set(self.arguments)):
            raise ArgumentationError("argument ids must be unique")
        if any(not a.strip() for a in self.arguments):
            raise ArgumentationError("argument ids must be non-empty")
        aset = set(self.arguments)
        for src, dst in self.attacks:
            if src not in aset or dst not in aset:
                raise ArgumentationError("attack references undeclared argument")


@dataclass(frozen=True)
class GroundedResult:
    status: ArgumentationStatus
    grounded_extension: Tuple[str, ...]
    iterations: int
    reason: str
    method: str = "DUNG_CHARACTERISTIC_FUNCTION_LEAST_FIXED_POINT"
    attacks_generated_by_runtime: bool = False
    causal_claim: bool = False
    effect_authority: bool = False
    canon_promoted: bool = False



def attackers(af: ArgumentationFramework, argument: str) -> FrozenSet[str]:
    return frozenset(src for src, dst in af.attacks if dst == argument)


def attacked_by(af: ArgumentationFramework, extension: Iterable[str]) -> FrozenSet[str]:
    ext = frozenset(extension)
    return frozenset(dst for src, dst in af.attacks if src in ext)


def conflict_free(af: ArgumentationFramework, extension: Iterable[str]) -> bool:
    ext = frozenset(extension)
    return not any(src in ext and dst in ext for src, dst in af.attacks)


def defended_by(af: ArgumentationFramework, argument: str, extension: Iterable[str]) -> bool:
    ext_attacks = attacked_by(af, extension)
    return attackers(af, argument).issubset(ext_attacks)


def characteristic(af: ArgumentationFramework, extension: Iterable[str]) -> FrozenSet[str]:
    return frozenset(a for a in af.arguments if defended_by(af, a, extension))


def admissible(af: ArgumentationFramework, extension: Iterable[str]) -> bool:
    ext = frozenset(extension)
    aset = set(af.arguments)
    return ext.issubset(aset) and conflict_free(af, ext) and all(defended_by(af, a, ext) for a in ext)


def complete_extension(af: ArgumentationFramework, extension: Iterable[str]) -> bool:
    ext = frozenset(extension)
    return admissible(af, ext) and characteristic(af, ext) == ext


def stable_extension(af: ArgumentationFramework, extension: Iterable[str]) -> bool:
    ext = frozenset(extension)
    if not ext.issubset(set(af.arguments)) or not conflict_free(af, ext):
        return False
    return (set(af.arguments) - set(ext)).issubset(attacked_by(af, ext))


def grounded_extension(af: ArgumentationFramework, *, bounds: ArgumentationBounds = ArgumentationBounds()) -> GroundedResult:
    try:
        af.validate(bounds)
    except ArgumentationError as exc:
        status = ArgumentationStatus.RESOURCE_BOUND_EXCEEDED if "bound exceeded" in str(exc) else ArgumentationStatus.REJECT_MALFORMED_REQUEST
        return GroundedResult(status, (), 0, str(exc))
    current: FrozenSet[str] = frozenset()
    for iteration in range(1, bounds.max_iterations + 1):
        nxt = characteristic(af, current)
        if nxt == current:
            if not complete_extension(af, current):
                return GroundedResult(ArgumentationStatus.REJECT_MALFORMED_REQUEST, (), iteration, "internal fixed-point invariant failed")
            return GroundedResult(ArgumentationStatus.VERIFIED_BOUNDED, tuple(sorted(current)), iteration, "least fixed point of Dung characteristic function reached")
        if not current.issubset(nxt):
            return GroundedResult(ArgumentationStatus.REJECT_MALFORMED_REQUEST, (), iteration, "characteristic iteration lost monotonic chain invariant")
        current = nxt
    return GroundedResult(ArgumentationStatus.RESOURCE_BOUND_EXCEEDED, (), bounds.max_iterations, "fixed-point iteration bound exceeded")


def adjacency_matrix(af: ArgumentationFramework, *, bounds: ArgumentationBounds = ArgumentationBounds()) -> Tuple[Tuple[int, ...], ...]:
    af.validate(bounds)
    idx = {a: i for i, a in enumerate(af.arguments)}
    matrix = [[0] * len(af.arguments) for _ in af.arguments]
    for src, dst in af.attacks:
        matrix[idx[src]][idx[dst]] = 1
    return tuple(tuple(row) for row in matrix)


def run_request(request: Any, *, bounds: ArgumentationBounds = ArgumentationBounds()) -> GroundedResult:
    if not isinstance(request, dict) or set(request) != {"arguments", "attacks"}:
        return GroundedResult(ArgumentationStatus.REJECT_MALFORMED_REQUEST, (), 0, "request must contain exactly arguments and attacks")
    try:
        arguments = tuple(request["arguments"])
        attacks = tuple(tuple(edge) for edge in request["attacks"])
        if any(not isinstance(a, str) for a in arguments) or any(len(edge) != 2 for edge in attacks):
            raise ArgumentationError("arguments must be strings and attacks must be pairs")
        af = ArgumentationFramework(arguments, attacks)
        return grounded_extension(af, bounds=bounds)
    except (ArgumentationError, TypeError, ValueError) as exc:
        return GroundedResult(ArgumentationStatus.REJECT_MALFORMED_REQUEST, (), 0, str(exc))
