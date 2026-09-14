"""Bounded ALU-08 categorical-core checker for finite categories.

Origin architect / steward: Trang Phan.
Epistemic class: AMOS_MODEL / executable bounded candidate.

The checker implements only the ordinary finite-category axioms: typed source
and target, total composition on composable pairs, identity morphisms, and
associativity. It does not implement or claim elementary/Grothendieck topos
structure, limits, exponentials, subobject classifiers, adjunctions, or
categorical completeness beyond the supplied finite category.

Established source lineage:
- Eilenberg & Mac Lane, "General Theory of Natural Equivalences" (1945),
  DOI 10.1090/S0002-9947-1945-0013131-6.
"""
from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import FrozenSet, Mapping, Tuple


SOURCE_PROVENANCE = {
    "category_axioms": {
        "authors": "Samuel Eilenberg; Saunders Mac Lane",
        "year": 1945,
        "doi": "10.1090/S0002-9947-1945-0013131-6",
        "status": "ESTABLISHED_MATHEMATICS",
    }
}


class CategoryInvariantError(ValueError):
    pass


@dataclass(frozen=True)
class Morphism:
    name: str
    source: str
    target: str

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.source.strip() or not self.target.strip():
            raise CategoryInvariantError("morphism name/source/target must be non-empty")


@dataclass(frozen=True)
class FiniteCategory:
    objects: FrozenSet[str]
    morphisms: Mapping[str, Morphism]
    identities: Mapping[str, str]
    composition: Mapping[Tuple[str, str], str]

    def __init__(
        self,
        objects: FrozenSet[str],
        morphisms: Mapping[str, Morphism],
        identities: Mapping[str, str],
        composition: Mapping[Tuple[str, str], str],
    ) -> None:
        objs = frozenset(objects)
        if any(not obj.strip() for obj in objs):
            raise CategoryInvariantError("object names must be non-empty")

        morphs = dict(morphisms)
        for key, morphism in morphs.items():
            if key != morphism.name:
                raise CategoryInvariantError("morphism mapping key must equal morphism name")
            if morphism.source not in objs or morphism.target not in objs:
                raise CategoryInvariantError("morphism endpoint outside object set")

        ids = dict(identities)
        if set(ids) != set(objs):
            raise CategoryInvariantError("identities must bind exactly one identity per object")
        for obj, morphism_name in ids.items():
            if morphism_name not in morphs:
                raise CategoryInvariantError("identity morphism is missing")
            identity = morphs[morphism_name]
            if identity.source != obj or identity.target != obj:
                raise CategoryInvariantError("identity morphism must be an endomorphism of its object")

        comp = dict(composition)
        expected = {
            (g_name, f_name)
            for f_name, f in morphs.items()
            for g_name, g in morphs.items()
            if f.target == g.source
        }
        if set(comp) != expected:
            missing = expected - set(comp)
            extra = set(comp) - expected
            raise CategoryInvariantError(
                f"composition table must bind exactly all composable pairs; missing={sorted(missing)}, extra={sorted(extra)}"
            )
        for (g_name, f_name), h_name in comp.items():
            if h_name not in morphs:
                raise CategoryInvariantError("composition result morphism is missing")
            f = morphs[f_name]
            g = morphs[g_name]
            h = morphs[h_name]
            if h.source != f.source or h.target != g.target:
                raise CategoryInvariantError("composition result has wrong source/target")

        for f_name, f in morphs.items():
            if comp[(ids[f.target], f_name)] != f_name:
                raise CategoryInvariantError("left identity law failed")
            if comp[(f_name, ids[f.source])] != f_name:
                raise CategoryInvariantError("right identity law failed")

        for f_name, f in morphs.items():
            for g_name, g in morphs.items():
                if f.target != g.source:
                    continue
                for h_name, h in morphs.items():
                    if g.target != h.source:
                        continue
                    gf = comp[(g_name, f_name)]
                    hg = comp[(h_name, g_name)]
                    left = comp[(h_name, gf)]
                    right = comp[(hg, f_name)]
                    if left != right:
                        raise CategoryInvariantError(
                            f"associativity failed for ({h_name},{g_name},{f_name})"
                        )

        object.__setattr__(self, "objects", objs)
        object.__setattr__(self, "morphisms", MappingProxyType(morphs))
        object.__setattr__(self, "identities", MappingProxyType(ids))
        object.__setattr__(self, "composition", MappingProxyType(comp))

    def hom(self, source: str, target: str) -> Tuple[str, ...]:
        if source not in self.objects or target not in self.objects:
            raise KeyError((source, target))
        return tuple(
            sorted(
                name
                for name, morphism in self.morphisms.items()
                if morphism.source == source and morphism.target == target
            )
        )

    def compose(self, g: str, f: str) -> str:
        if g not in self.morphisms or f not in self.morphisms:
            raise KeyError((g, f))
        key = (g, f)
        if key not in self.composition:
            raise CategoryInvariantError("morphisms are not composable")
        return self.composition[key]

    def is_thin(self) -> bool:
        return all(
            len(self.hom(source, target)) <= 1
            for source in self.objects
            for target in self.objects
        )

    def thin_preorder_matrix(self, order: Tuple[str, ...]) -> Tuple[Tuple[bool, ...], ...]:
        """Return reachability-by-morphism only when the category is thin.

        For a thin category this relation is reflexive and transitive by the
        identity and composition laws. It is a preorder; antisymmetry is an
        additional property, not assumed.
        """
        if set(order) != set(self.objects) or len(order) != len(self.objects):
            raise CategoryInvariantError("order must enumerate every object exactly once")
        if not self.is_thin():
            raise CategoryInvariantError("preorder projection requires a thin category")
        return tuple(
            tuple(bool(self.hom(source, target)) for target in order)
            for source in order
        )


def validate_category_invariants() -> Tuple[str, ...]:
    failures = []
    objects = frozenset({"0", "1"})
    morphisms = {
        "id0": Morphism("id0", "0", "0"),
        "id1": Morphism("id1", "1", "1"),
        "f": Morphism("f", "0", "1"),
    }
    composition = {
        ("id0", "id0"): "id0",
        ("id1", "id1"): "id1",
        ("f", "id0"): "f",
        ("id1", "f"): "f",
    }
    category = FiniteCategory(objects, morphisms, {"0": "id0", "1": "id1"}, composition)
    if category.compose("id1", "f") != "f":
        failures.append("LEFT_IDENTITY")
    if category.compose("f", "id0") != "f":
        failures.append("RIGHT_IDENTITY")
    matrix = category.thin_preorder_matrix(("0", "1"))
    if matrix != ((True, True), (False, True)):
        failures.append("THIN_PREORDER")
    return tuple(failures)
