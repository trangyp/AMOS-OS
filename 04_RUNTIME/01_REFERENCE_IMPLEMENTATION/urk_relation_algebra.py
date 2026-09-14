"""Finite relation algebra for the AMOS URK mathematical substrate candidate v1.1.

Origin architect / steward: Trang Phan.

This module implements only the established finite mathematics admitted by the
2026-09-14 URK candidate:
  URK-E1 relation <-> Boolean adjacency encoding,
  URK-E2 Boolean-semiring relation composition,
  URK-E3 reflexive-transitive closure on finite directed relations.

It does not turn reachability into entailment or causation and it does not
promote the URK candidate to Canon.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet, Hashable, Iterable, Sequence, Tuple

Node = Hashable
Relation = FrozenSet[Tuple[Node, Node]]
BoolMatrix = Tuple[Tuple[bool, ...], ...]


@dataclass(frozen=True)
class FiniteNamespace:
    items: Tuple[Node, ...]

    def __post_init__(self) -> None:
        if not self.items:
            raise ValueError("finite namespace must be non-empty")
        if len(set(self.items)) != len(self.items):
            raise ValueError("finite namespace items must be unique")

    @property
    def index(self):
        return {node: i for i, node in enumerate(self.items)}

    def validate_relation(self, relation: Iterable[Tuple[Node, Node]]) -> Relation:
        rel = frozenset(relation)
        allowed = set(self.items)
        invalid = [(a, b) for a, b in rel if a not in allowed or b not in allowed]
        if invalid:
            raise ValueError(f"relation contains nodes outside namespace: {invalid[:3]}")
        return rel


def encode_relation(namespace: FiniteNamespace, relation: Iterable[Tuple[Node, Node]]) -> BoolMatrix:
    """URK-E1: Enc(R)[i,j] = 1 iff (k_i,k_j) is in R."""
    rel = namespace.validate_relation(relation)
    return tuple(
        tuple((a, b) in rel for b in namespace.items)
        for a in namespace.items
    )


def decode_relation(namespace: FiniteNamespace, matrix: Sequence[Sequence[bool]]) -> Relation:
    """Inverse of encode_relation on n x n Boolean matrices."""
    n = len(namespace.items)
    if len(matrix) != n or any(len(row) != n for row in matrix):
        raise ValueError(f"matrix must have exact shape {n}x{n}")
    if any(type(v) is not bool for row in matrix for v in row):
        raise TypeError("relation matrix entries must be bool")
    return frozenset(
        (namespace.items[i], namespace.items[j])
        for i in range(n)
        for j in range(n)
        if matrix[i][j]
    )


def compose_relations(namespace: FiniteNamespace, r: Iterable[Tuple[Node, Node]], s: Iterable[Tuple[Node, Node]]) -> Relation:
    """Set relation composition matching Boolean product A_R odot A_S.

    (x,z) is in R;S iff there exists y with (x,y) in R and (y,z) in S.
    """
    rr = namespace.validate_relation(r)
    ss = namespace.validate_relation(s)
    return frozenset(
        (x, z)
        for x in namespace.items
        for z in namespace.items
        if any((x, y) in rr and (y, z) in ss for y in namespace.items)
    )


def boolean_compose(a: BoolMatrix, b: BoolMatrix) -> BoolMatrix:
    """URK-E2 Boolean-semiring matrix product: OR_y(A[x,y] AND B[y,z])."""
    n = len(a)
    if n == 0 or len(b) != n or any(len(row) != n for row in a) or any(len(row) != n for row in b):
        raise ValueError("Boolean composition requires equally sized non-empty square matrices")
    if any(type(v) is not bool for row in a for v in row) or any(type(v) is not bool for row in b for v in row):
        raise TypeError("Boolean composition entries must be bool")
    return tuple(
        tuple(any(a[i][k] and b[k][j] for k in range(n)) for j in range(n))
        for i in range(n)
    )


def reflexive_transitive_closure(namespace: FiniteNamespace, relation: Iterable[Tuple[Node, Node]]) -> Relation:
    """URK-E3: finite reflexive-transitive closure to a fixed point.

    Warshall-style closure. Reachability here is graph reachability only.
    """
    matrix = [list(row) for row in encode_relation(namespace, relation)]
    n = len(namespace.items)
    for i in range(n):
        matrix[i][i] = True
    for k in range(n):
        for i in range(n):
            if not matrix[i][k]:
                continue
            for j in range(n):
                matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
    return decode_relation(namespace, matrix)


def is_reflexive(namespace: FiniteNamespace, relation: Iterable[Tuple[Node, Node]]) -> bool:
    rel = namespace.validate_relation(relation)
    return all((x, x) in rel for x in namespace.items)


def is_transitive(namespace: FiniteNamespace, relation: Iterable[Tuple[Node, Node]]) -> bool:
    rel = namespace.validate_relation(relation)
    for x, y in rel:
        for y2, z in rel:
            if y == y2 and (x, z) not in rel:
                return False
    return True


def validate_closure_invariants(namespace: FiniteNamespace, base: Iterable[Tuple[Node, Node]]) -> Tuple[str, ...]:
    base_rel = namespace.validate_relation(base)
    closure = reflexive_transitive_closure(namespace, base_rel)
    failures = []
    if not base_rel.issubset(closure):
        failures.append("CLOSURE_MUST_CONTAIN_BASE_RELATION")
    if not is_reflexive(namespace, closure):
        failures.append("CLOSURE_MUST_BE_REFLEXIVE")
    if not is_transitive(namespace, closure):
        failures.append("CLOSURE_MUST_BE_TRANSITIVE")
    if reflexive_transitive_closure(namespace, closure) != closure:
        failures.append("CLOSURE_MUST_BE_IDEMPOTENT")
    return tuple(failures)