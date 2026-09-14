"""Bounded ALU-08 categorical / Heyting structural checker.

Origin architect / steward: Trang Phan.

Executable scope:
- finite small-category law validation;
- finite-poset Heyting implication and bounded lattice validation.

This does NOT certify an elementary topos. In particular it does not establish
finite limits, Cartesian closure/exponentials, or a subobject classifier.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import FrozenSet, Mapping, Optional, Tuple


@dataclass(frozen=True)
class Arrow:
    source: str
    target: str


@dataclass(frozen=True)
class FiniteCategory:
    objects: FrozenSet[str]
    arrows: Mapping[str, Arrow]
    identities: Mapping[str, str]
    composition: Mapping[Tuple[str, str], str]

    def composable(self, f: str, g: str) -> bool:
        return self.arrows[f].target == self.arrows[g].source

    def compose(self, f: str, g: str) -> str:
        if f not in self.arrows or g not in self.arrows:
            raise KeyError("unknown arrow")
        if not self.composable(f, g):
            raise ValueError("arrows are not composable")
        try:
            return self.composition[(f, g)]
        except KeyError as exc:
            raise ValueError(f"missing composition for {(f, g)!r}") from exc

    def validate(self) -> tuple[str, ...]:
        failures = []
        for name, arrow in self.arrows.items():
            if arrow.source not in self.objects or arrow.target not in self.objects:
                failures.append(f"ARROW_ENDPOINT_UNKNOWN:{name}")
        for obj in self.objects:
            ident = self.identities.get(obj)
            if ident is None:
                failures.append(f"IDENTITY_MISSING:{obj}")
                continue
            arrow = self.arrows.get(ident)
            if arrow != Arrow(obj, obj):
                failures.append(f"IDENTITY_ENDPOINT_MISMATCH:{obj}")

        for f, af in self.arrows.items():
            for g, ag in self.arrows.items():
                if af.target != ag.source:
                    continue
                h = self.composition.get((f, g))
                if h is None:
                    failures.append(f"COMPOSITION_MISSING:{f}:{g}")
                    continue
                ah = self.arrows.get(h)
                if ah != Arrow(af.source, ag.target):
                    failures.append(f"COMPOSITION_ENDPOINT_MISMATCH:{f}:{g}")

        for f, arrow in self.arrows.items():
            left = self.identities.get(arrow.source)
            right = self.identities.get(arrow.target)
            if left in self.arrows and self.composition.get((left, f)) != f:
                failures.append(f"LEFT_IDENTITY_FAIL:{f}")
            if right in self.arrows and self.composition.get((f, right)) != f:
                failures.append(f"RIGHT_IDENTITY_FAIL:{f}")

        names = tuple(self.arrows)
        for f, g, h in product(names, repeat=3):
            if not self.composable(f, g) or not self.composable(g, h):
                continue
            fg = self.composition.get((f, g))
            gh = self.composition.get((g, h))
            if fg is None or gh is None:
                continue
            left = self.composition.get((fg, h))
            right = self.composition.get((f, gh))
            if left != right:
                failures.append(f"ASSOCIATIVITY_FAIL:{f}:{g}:{h}")
        return tuple(sorted(set(failures)))


@dataclass(frozen=True)
class FiniteHeytingAlgebra:
    elements: FrozenSet[str]
    leq_pairs: FrozenSet[Tuple[str, str]]

    def leq(self, a: str, b: str) -> bool:
        self._require(a)
        self._require(b)
        return (a, b) in self.leq_pairs

    def _require(self, x: str) -> None:
        if x not in self.elements:
            raise KeyError(x)

    def lower_bounds(self, a: str, b: str) -> FrozenSet[str]:
        return frozenset(x for x in self.elements if self.leq(x, a) and self.leq(x, b))

    def upper_bounds(self, a: str, b: str) -> FrozenSet[str]:
        return frozenset(x for x in self.elements if self.leq(a, x) and self.leq(b, x))

    def _greatest(self, candidates: FrozenSet[str]) -> Optional[str]:
        winners = [x for x in candidates if all(self.leq(y, x) for y in candidates)]
        return winners[0] if len(winners) == 1 else None

    def _least(self, candidates: FrozenSet[str]) -> Optional[str]:
        winners = [x for x in candidates if all(self.leq(x, y) for y in candidates)]
        return winners[0] if len(winners) == 1 else None

    def meet(self, a: str, b: str) -> str:
        value = self._greatest(self.lower_bounds(a, b))
        if value is None:
            raise ValueError(f"meet undefined or non-unique for {a},{b}")
        return value

    def join(self, a: str, b: str) -> str:
        value = self._least(self.upper_bounds(a, b))
        if value is None:
            raise ValueError(f"join undefined or non-unique for {a},{b}")
        return value

    def bottom(self) -> str:
        value = self._least(self.elements)
        if value is None:
            raise ValueError("bottom undefined or non-unique")
        return value

    def top(self) -> str:
        value = self._greatest(self.elements)
        if value is None:
            raise ValueError("top undefined or non-unique")
        return value

    def implication(self, a: str, b: str) -> str:
        candidates = frozenset(x for x in self.elements if self.leq(self.meet(x, a), b))
        value = self._greatest(candidates)
        if value is None:
            raise ValueError(f"Heyting implication undefined or non-unique for {a},{b}")
        return value

    def validate(self) -> tuple[str, ...]:
        failures = []
        if not self.elements:
            return ("EMPTY_HEYTING_CARRIER",)
        for a in self.elements:
            if not self.leq(a, a):
                failures.append(f"REFLEXIVITY_FAIL:{a}")
        for a, b in product(self.elements, repeat=2):
            if self.leq(a, b) and self.leq(b, a) and a != b:
                failures.append(f"ANTISYMMETRY_FAIL:{a}:{b}")
        for a, b, c in product(self.elements, repeat=3):
            if self.leq(a, b) and self.leq(b, c) and not self.leq(a, c):
                failures.append(f"TRANSITIVITY_FAIL:{a}:{b}:{c}")
        if failures:
            return tuple(sorted(set(failures)))
        try:
            self.bottom()
            self.top()
            for a, b in product(self.elements, repeat=2):
                self.meet(a, b)
                self.join(a, b)
                imp = self.implication(a, b)
                for x in self.elements:
                    if self.leq(x, imp) != self.leq(self.meet(x, a), b):
                        failures.append(f"HEYTING_ADJUNCTION_FAIL:{x}:{a}:{b}")
        except ValueError as exc:
            failures.append(f"LATTICE_STRUCTURE_FAIL:{exc}")
        return tuple(sorted(set(failures)))


def validate_reference_invariants() -> tuple[str, ...]:
    failures = []
    bool_alg = FiniteHeytingAlgebra(
        frozenset({"0", "1"}),
        frozenset({("0", "0"), ("0", "1"), ("1", "1")}),
    )
    failures.extend(bool_alg.validate())
    if bool_alg.implication("1", "0") != "0":
        failures.append("BOOLEAN_IMPL_1_0_FAIL")
    if bool_alg.implication("0", "1") != "1":
        failures.append("BOOLEAN_IMPL_0_1_FAIL")
    return tuple(failures)
