"""Bounded mathematical substrate for AMOS logic/topology runtime.

Origin architect / steward: Trang Phan.
Implementation class: AMOS_MODEL / executable bounded reference.

This module does not redefine Canon. It provides typed, testable mathematics for
matrix topology, graph closure, graph decomposition, probabilistic transitions,
and sparse tensor state. Established algorithms are independently implemented
from their mathematical definitions; provenance is recorded in
``ALGORITHM_PROVENANCE``.
"""
from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from math import inf, isfinite, isclose
from types import MappingProxyType
from typing import Dict, Iterable, Mapping, Sequence, Tuple


ALGORITHM_PROVENANCE = {
    "warshall_transitive_closure": {
        "author": "Stephen Warshall",
        "year": 1962,
        "doi": "10.1145/321105.321107",
        "status": "ESTABLISHED_ALGORITHM",
    },
    "tarjan_scc": {
        "author": "Robert Tarjan",
        "year": 1972,
        "doi": "10.1137/0201010",
        "status": "ESTABLISHED_ALGORITHM",
    },
    "dijkstra_shortest_path": {
        "author": "E. W. Dijkstra",
        "year": 1959,
        "doi": "10.1007/BF01386390",
        "status": "ESTABLISHED_ALGORITHM",
    },
    "kahn_topological_sort": {
        "author": "A. B. Kahn",
        "year": 1962,
        "doi": "10.1145/368996.369025",
        "status": "ESTABLISHED_ALGORITHM",
    },
}


class MathInvariantError(ValueError):
    """Raised when a mathematical domain or invariant is violated."""


BoolMatrix = Tuple[Tuple[bool, ...], ...]
FloatMatrix = Tuple[Tuple[float, ...], ...]


def _bool_matrix(matrix: Sequence[Sequence[bool]]) -> BoolMatrix:
    rows = tuple(tuple(row) for row in matrix)
    if not rows:
        raise MathInvariantError("matrix must be non-empty")
    n = len(rows)
    if any(len(row) != n for row in rows):
        raise MathInvariantError("matrix must be square")
    if any(type(value) is not bool for row in rows for value in row):
        raise MathInvariantError("boolean adjacency matrix requires bool entries")
    return rows


def transitive_closure(
    adjacency: Sequence[Sequence[bool]], *, reflexive: bool = True
) -> BoolMatrix:
    """Return Boolean reachability using Warshall's recurrence.

    Let R^(k)[i,j] denote whether j is reachable from i using intermediate
    vertices only from {0,...,k}. Then

        R^(k)[i,j] = R^(k-1)[i,j]
                     OR (R^(k-1)[i,k] AND R^(k-1)[k,j]).

    ``reflexive=True`` computes the reflexive-transitive closure.
    """
    a = _bool_matrix(adjacency)
    n = len(a)
    reach = [list(row) for row in a]
    if reflexive:
        for i in range(n):
            reach[i][i] = True
    for k in range(n):
        for i in range(n):
            if not reach[i][k]:
                continue
            for j in range(n):
                if reach[k][j]:
                    reach[i][j] = True
    return tuple(tuple(row) for row in reach)


def strongly_connected_components(
    adjacency: Sequence[Sequence[bool]],
) -> Tuple[Tuple[int, ...], ...]:
    """Return SCCs using Tarjan's depth-first low-link algorithm.

    Components and vertices within components are sorted for deterministic
    receipts; component ordering is by each component's minimum vertex.
    """
    a = _bool_matrix(adjacency)
    n = len(a)
    index = 0
    indices = [-1] * n
    lowlink = [0] * n
    stack: list[int] = []
    on_stack = [False] * n
    components: list[Tuple[int, ...]] = []

    def visit(v: int) -> None:
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w, connected in enumerate(a[v]):
            if not connected:
                continue
            if indices[w] == -1:
                visit(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            component: list[int] = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == v:
                    break
            components.append(tuple(sorted(component)))

    for v in range(n):
        if indices[v] == -1:
            visit(v)

    return tuple(sorted(components, key=lambda c: c[0]))


def topological_order(adjacency: Sequence[Sequence[bool]]) -> Tuple[int, ...]:
    """Return a deterministic Kahn topological order; fail closed on cycles."""
    a = _bool_matrix(adjacency)
    n = len(a)
    indegree = [0] * n
    for i in range(n):
        for j, connected in enumerate(a[i]):
            if connected:
                indegree[j] += 1

    ready: list[int] = []
    for i, degree in enumerate(indegree):
        if degree == 0:
            heappush(ready, i)

    order: list[int] = []
    while ready:
        v = heappop(ready)
        order.append(v)
        for w, connected in enumerate(a[v]):
            if connected:
                indegree[w] -= 1
                if indegree[w] == 0:
                    heappush(ready, w)

    if len(order) != n:
        raise MathInvariantError("topological order undefined for cyclic graph")
    return tuple(order)


@dataclass(frozen=True)
class WeightedTopology:
    """Square directed weighted topology with non-negative edge weights.

    ``inf`` denotes no edge. Diagonal entries must be zero. Dijkstra is valid
    because negative weights are rejected at construction time.
    """

    weights: FloatMatrix

    def __init__(self, weights: Sequence[Sequence[float]]) -> None:
        rows = tuple(tuple(float(value) for value in row) for row in weights)
        if not rows:
            raise MathInvariantError("weight matrix must be non-empty")
        n = len(rows)
        if any(len(row) != n for row in rows):
            raise MathInvariantError("weight matrix must be square")
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                if value != inf and not isfinite(value):
                    raise MathInvariantError("weights must be finite or +inf")
                if value < 0:
                    raise MathInvariantError("Dijkstra topology forbids negative weights")
                if i == j and value != 0.0:
                    raise MathInvariantError("weight matrix diagonal must be zero")
        object.__setattr__(self, "weights", rows)

    @property
    def size(self) -> int:
        return len(self.weights)

    def adjacency(self) -> BoolMatrix:
        n = self.size
        return tuple(
            tuple(i != j and self.weights[i][j] != inf for j in range(n))
            for i in range(n)
        )

    def shortest_distances(self, source: int) -> Tuple[float, ...]:
        """Return shortest-path distances from ``source`` via Dijkstra."""
        n = self.size
        if not 0 <= source < n:
            raise MathInvariantError("source index out of bounds")
        distance = [inf] * n
        distance[source] = 0.0
        visited = [False] * n
        queue: list[Tuple[float, int]] = [(0.0, source)]

        while queue:
            dist_v, v = heappop(queue)
            if visited[v]:
                continue
            visited[v] = True
            if dist_v != distance[v]:
                continue
            for w, weight in enumerate(self.weights[v]):
                if w == v or weight == inf:
                    continue
                candidate = dist_v + weight
                if candidate < distance[w]:
                    distance[w] = candidate
                    heappush(queue, (candidate, w))
        return tuple(distance)


@dataclass(frozen=True)
class RowStochasticMatrix:
    """Finite row-stochastic transition matrix P.

    For row-state probability vector x, ``step(x)`` returns xP.
    Invariant: P_ij >= 0 and sum_j P_ij = 1 for every row i.
    """

    values: FloatMatrix
    tolerance: float = 1e-12

    def __init__(
        self, values: Sequence[Sequence[float]], *, tolerance: float = 1e-12
    ) -> None:
        if tolerance <= 0 or not isfinite(tolerance):
            raise MathInvariantError("tolerance must be finite and positive")
        rows = tuple(tuple(float(value) for value in row) for row in values)
        if not rows:
            raise MathInvariantError("transition matrix must be non-empty")
        n = len(rows)
        if any(len(row) != n for row in rows):
            raise MathInvariantError("transition matrix must be square")
        for row in rows:
            if any((not isfinite(v)) or v < 0.0 or v > 1.0 for v in row):
                raise MathInvariantError("transition probabilities must lie in [0,1]")
            if not isclose(sum(row), 1.0, rel_tol=0.0, abs_tol=tolerance):
                raise MathInvariantError("each transition row must sum to one")
        object.__setattr__(self, "values", rows)
        object.__setattr__(self, "tolerance", tolerance)

    @property
    def size(self) -> int:
        return len(self.values)

    def step(self, state: Sequence[float]) -> Tuple[float, ...]:
        x = tuple(float(v) for v in state)
        if len(x) != self.size:
            raise MathInvariantError("state dimension must match transition matrix")
        if any((not isfinite(v)) or v < 0.0 or v > 1.0 for v in x):
            raise MathInvariantError("state probabilities must lie in [0,1]")
        if not isclose(sum(x), 1.0, rel_tol=0.0, abs_tol=self.tolerance):
            raise MathInvariantError("state probability vector must sum to one")
        result = tuple(
            sum(x[i] * self.values[i][j] for i in range(self.size))
            for j in range(self.size)
        )
        if not isclose(sum(result), 1.0, rel_tol=0.0, abs_tol=10 * self.tolerance):
            raise MathInvariantError("probability mass conservation failed")
        return result


@dataclass(frozen=True)
class SparseLogicTensor:
    """Finite sparse tensor with explicit named axes and bounded coordinates."""

    axes: Tuple[str, ...]
    shape: Tuple[int, ...]
    values: Mapping[Tuple[int, ...], float]

    def __init__(
        self,
        *,
        axes: Sequence[str],
        shape: Sequence[int],
        values: Mapping[Sequence[int], float] | None = None,
    ) -> None:
        axis_tuple = tuple(str(axis).strip() for axis in axes)
        shape_tuple = tuple(int(size) for size in shape)
        if not axis_tuple or any(not axis for axis in axis_tuple):
            raise MathInvariantError("tensor axes must be explicit non-empty names")
        if len(set(axis_tuple)) != len(axis_tuple):
            raise MathInvariantError("tensor axis names must be unique")
        if len(axis_tuple) != len(shape_tuple):
            raise MathInvariantError("tensor axes and shape must have equal rank")
        if any(size <= 0 for size in shape_tuple):
            raise MathInvariantError("tensor dimensions must be positive finite integers")

        normalized: Dict[Tuple[int, ...], float] = {}
        for raw_coord, raw_value in (values or {}).items():
            coord = tuple(int(i) for i in raw_coord)
            if len(coord) != len(shape_tuple):
                raise MathInvariantError("tensor coordinate rank mismatch")
            if any(i < 0 or i >= shape_tuple[d] for d, i in enumerate(coord)):
                raise MathInvariantError("tensor coordinate out of bounds")
            value = float(raw_value)
            if not isfinite(value):
                raise MathInvariantError("tensor values must be finite")
            normalized[coord] = value

        object.__setattr__(self, "axes", axis_tuple)
        object.__setattr__(self, "shape", shape_tuple)
        object.__setattr__(self, "values", MappingProxyType(normalized))

    @property
    def rank(self) -> int:
        return len(self.shape)

    def get(self, coordinate: Sequence[int]) -> float:
        coord = tuple(int(i) for i in coordinate)
        if len(coord) != self.rank:
            raise MathInvariantError("tensor coordinate rank mismatch")
        if any(i < 0 or i >= self.shape[d] for d, i in enumerate(coord)):
            raise MathInvariantError("tensor coordinate out of bounds")
        return self.values.get(coord, 0.0)

    def frobenius_norm_sq(self) -> float:
        """Return ||T||_F^2 = sum over stored coordinates of |T_i|^2."""
        return sum(value * value for value in self.values.values())


def core19_topology_matrix(
    edges: Iterable[Tuple[int, int]], *, reflexive: bool = False
) -> BoolMatrix:
    """Build a 19 x 19 adjacency matrix from one-based Core-19 coordinates."""
    n = 19
    matrix = [[False] * n for _ in range(n)]
    if reflexive:
        for i in range(n):
            matrix[i][i] = True
    for src, dst in edges:
        if not (1 <= src <= n and 1 <= dst <= n):
            raise MathInvariantError("Core-19 edge indices must lie in 1..19")
        matrix[src - 1][dst - 1] = True
    return tuple(tuple(row) for row in matrix)


def validate_math_invariants() -> Tuple[str, ...]:
    """Execute bounded mathematical invariants; empty tuple means pass."""
    failures: list[str] = []

    chain = ((False, True, False), (False, False, True), (False, False, False))
    closure = transitive_closure(chain)
    if not closure[0][2] or not all(closure[i][i] for i in range(3)):
        failures.append("TRANSITIVE_CLOSURE")

    cyclic = ((False, True, False), (True, False, True), (False, False, False))
    components = strongly_connected_components(cyclic)
    flattened = sorted(v for component in components for v in component)
    if flattened != [0, 1, 2] or len(flattened) != len(set(flattened)):
        failures.append("SCC_PARTITION")

    transition = RowStochasticMatrix(((0.75, 0.25), (0.5, 0.5)))
    stepped = transition.step((0.4, 0.6))
    if not isclose(sum(stepped), 1.0, rel_tol=0.0, abs_tol=1e-12):
        failures.append("STOCHASTIC_MASS")

    matrix = core19_topology_matrix(((1, 2), (2, 3)))
    if len(matrix) != 19 or any(len(row) != 19 for row in matrix):
        failures.append("CORE19_TOPOLOGY_SHAPE")

    return tuple(dict.fromkeys(failures))
