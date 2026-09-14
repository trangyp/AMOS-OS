"""Exact bounded topology semantics for finite AMOS carriers.

Origin architect / steward: Trang Phan.
Epistemic class: AMOS_MODEL using established finite-topology mathematics.

For a finite carrier X, a family tau subset P(X) is a topology iff it contains
empty and X and is closed under binary union and binary intersection. Because
P(X) is finite, arbitrary unions reduce to finite unions of distinct opens.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet, Hashable, Iterable, Sequence, Tuple


class TopologyInvariantError(ValueError):
    pass


@dataclass(frozen=True)
class FiniteTopology:
    carrier: Tuple[Hashable, ...]
    opens: FrozenSet[FrozenSet[Hashable]]

    def __init__(
        self,
        carrier: Sequence[Hashable],
        opens: Iterable[Iterable[Hashable]],
    ) -> None:
        carrier_tuple = tuple(carrier)
        if len(set(carrier_tuple)) != len(carrier_tuple):
            raise TopologyInvariantError("carrier points must be unique")
        carrier_set = frozenset(carrier_tuple)
        open_family = frozenset(frozenset(u) for u in opens)
        if frozenset() not in open_family:
            raise TopologyInvariantError("empty set must be open")
        if carrier_set not in open_family:
            raise TopologyInvariantError("whole carrier must be open")
        for u in open_family:
            if not u.issubset(carrier_set):
                raise TopologyInvariantError("open set contains point outside carrier")
        for u in open_family:
            for v in open_family:
                if (u | v) not in open_family:
                    raise TopologyInvariantError("open family is not closed under union")
                if (u & v) not in open_family:
                    raise TopologyInvariantError(
                        "open family is not closed under finite intersection"
                    )
        object.__setattr__(self, "carrier", carrier_tuple)
        object.__setattr__(self, "opens", open_family)

    def is_open(self, subset: Iterable[Hashable]) -> bool:
        return frozenset(subset) in self.opens

    def specialization_matrix(self) -> Tuple[Tuple[bool, ...], ...]:
        """Return the specialization preorder matrix.

        Matrix entry M[i][j] is true exactly when x_i <= x_j, where
        x <= y iff every open set containing x also contains y.
        This is a topological relation, not a causal relation.
        """
        rows = []
        for x in self.carrier:
            row = []
            containing_x = tuple(u for u in self.opens if x in u)
            for y in self.carrier:
                row.append(all(y in u for u in containing_x))
            rows.append(tuple(row))
        return tuple(rows)

    def is_t0(self) -> bool:
        """A finite space is T0 iff its specialization preorder is antisymmetric."""
        matrix = self.specialization_matrix()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i != j and matrix[i][j] and matrix[j][i]:
                    return False
        return True


def validate_finite_topology_invariants() -> Tuple[str, ...]:
    failures = []
    topology = FiniteTopology(
        (0, 1, 2),
        ((), (0,), (0, 1), (0, 1, 2)),
    )
    matrix = topology.specialization_matrix()
    if any(not matrix[i][i] for i in range(3)):
        failures.append("SPECIALIZATION_REFLEXIVITY")
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if matrix[i][j] and matrix[j][k] and not matrix[i][k]:
                    failures.append("SPECIALIZATION_TRANSITIVITY")
                    return tuple(dict.fromkeys(failures))
    if not topology.is_t0():
        failures.append("EXPECTED_T0")
    return tuple(dict.fromkeys(failures))
