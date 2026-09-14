"""Bounded deterministic foundational algorithms for AMOS OS.

Origin architect / steward: Trang Phan.

These implementations are intentionally small, dependency-free reference
executors. They establish algorithm behavior only for the declared mathematical
contracts below. They do not establish semantic truth, causality, canon status,
or effect authority.

Implemented bounded surfaces:
- disjoint-set union / union-find over explicit finite element identities;
- Bellman-Ford single-source shortest paths with reachable negative-cycle status;
- Edmonds-Karp integral maximum flow;
- DPLL satisfiability for finite propositional CNF;
- AC-3 arc-consistency propagation for finite binary CSPs.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from enum import Enum
from math import inf, isfinite
from typing import Dict, FrozenSet, Hashable, Iterable, Mapping, MutableMapping, Optional, Sequence, Tuple


class UnionFind:
    """Disjoint-set union over explicit finite hashable elements.

    Set membership here means connectivity under submitted ``union`` operations.
    It does not establish semantic identity or ontology equivalence.
    """

    def __init__(self, elements: Iterable[Hashable] = ()) -> None:
        self._parent: Dict[Hashable, Hashable] = {}
        self._rank: Dict[Hashable, int] = {}
        for element in elements:
            self.add(element)

    def add(self, element: Hashable) -> None:
        if element not in self._parent:
            self._parent[element] = element
            self._rank[element] = 0

    def find(self, element: Hashable) -> Hashable:
        if element not in self._parent:
            raise KeyError(element)
        parent = self._parent[element]
        if parent != element:
            self._parent[element] = self.find(parent)
        return self._parent[element]

    def union(self, left: Hashable, right: Hashable) -> Hashable:
        if left not in self._parent or right not in self._parent:
            missing = left if left not in self._parent else right
            raise KeyError(missing)
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return root_left
        rank_left = self._rank[root_left]
        rank_right = self._rank[root_right]
        if rank_left < rank_right:
            root_left, root_right = root_right, root_left
            rank_left, rank_right = rank_right, rank_left
        self._parent[root_right] = root_left
        if rank_left == rank_right:
            self._rank[root_left] += 1
        return root_left

    def connected(self, left: Hashable, right: Hashable) -> bool:
        return self.find(left) == self.find(right)

    def components(self) -> Tuple[FrozenSet[Hashable], ...]:
        groups: Dict[Hashable, set[Hashable]] = {}
        for element in self._parent:
            groups.setdefault(self.find(element), set()).add(element)
        frozen = [frozenset(values) for values in groups.values()]
        frozen.sort(key=lambda group: tuple(sorted((repr(x) for x in group))))
        return tuple(frozen)


class ShortestPathStatus(Enum):
    OK = "OK"
    REACHABLE_NEGATIVE_CYCLE = "REACHABLE_NEGATIVE_CYCLE"


@dataclass(frozen=True)
class BellmanFordResult:
    status: ShortestPathStatus
    distances: Mapping[str, float]
    predecessors: Mapping[str, Optional[str]]


def bellman_ford(
    nodes: Iterable[str],
    edges: Iterable[Tuple[str, str, float]],
    source: str,
) -> BellmanFordResult:
    """Exact finite Bellman-Ford reference for supplied edge weights.

    A negative cycle is reported only when reachable from ``source``. Distances
    are meaningful only when status is ``OK``.
    """
    ordered_nodes = tuple(dict.fromkeys(nodes))
    if not ordered_nodes or any(not node for node in ordered_nodes):
        raise ValueError("nodes must be non-empty strings")
    if source not in ordered_nodes:
        raise KeyError(source)
    edge_list = tuple(edges)
    node_set = set(ordered_nodes)
    for u, v, weight in edge_list:
        if u not in node_set or v not in node_set:
            raise ValueError("edge endpoint outside declared node set")
        if not isfinite(weight):
            raise ValueError("edge weights must be finite")

    distance: Dict[str, float] = {node: inf for node in ordered_nodes}
    predecessor: Dict[str, Optional[str]] = {node: None for node in ordered_nodes}
    distance[source] = 0.0

    for _ in range(len(ordered_nodes) - 1):
        changed = False
        for u, v, weight in edge_list:
            if distance[u] != inf and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                predecessor[v] = u
                changed = True
        if not changed:
            break

    for u, v, weight in edge_list:
        if distance[u] != inf and distance[u] + weight < distance[v]:
            return BellmanFordResult(
                ShortestPathStatus.REACHABLE_NEGATIVE_CYCLE,
                dict(distance),
                dict(predecessor),
            )
    return BellmanFordResult(ShortestPathStatus.OK, dict(distance), dict(predecessor))


@dataclass(frozen=True)
class MaxFlowResult:
    value: int
    flow: Mapping[Tuple[str, str], int]


def edmonds_karp_max_flow(
    capacities: Mapping[Tuple[str, str], int],
    source: str,
    sink: str,
) -> MaxFlowResult:
    """Integral Edmonds-Karp maximum flow on an explicit directed network."""
    if not source or not sink or source == sink:
        raise ValueError("source and sink must be distinct non-empty identities")
    nodes = {source, sink}
    for (u, v), capacity in capacities.items():
        if not u or not v or u == v:
            raise ValueError("capacity edges require distinct non-empty endpoints")
        if not isinstance(capacity, int) or isinstance(capacity, bool) or capacity < 0:
            raise ValueError("capacities must be non-negative integers")
        nodes.update((u, v))

    residual: Dict[str, Dict[str, int]] = {node: {} for node in nodes}
    for (u, v), capacity in capacities.items():
        residual[u][v] = residual[u].get(v, 0) + capacity
        residual[v].setdefault(u, 0)

    flow_value = 0
    net_flow: Dict[Tuple[str, str], int] = {edge: 0 for edge in capacities}

    while True:
        parent: Dict[str, Optional[str]] = {source: None}
        queue = deque([source])
        while queue and sink not in parent:
            u = queue.popleft()
            for v in sorted(residual[u]):
                if v not in parent and residual[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        break
        if sink not in parent:
            break

        bottleneck: Optional[int] = None
        v = sink
        while v != source:
            u = parent[v]
            assert u is not None
            cap = residual[u][v]
            bottleneck = cap if bottleneck is None else min(bottleneck, cap)
            v = u
        assert bottleneck is not None and bottleneck > 0

        v = sink
        while v != source:
            u = parent[v]
            assert u is not None
            residual[u][v] -= bottleneck
            residual[v][u] = residual[v].get(u, 0) + bottleneck
            if (u, v) in net_flow:
                net_flow[(u, v)] += bottleneck
            elif (v, u) in net_flow:
                net_flow[(v, u)] -= bottleneck
            v = u
        flow_value += bottleneck

    return MaxFlowResult(flow_value, dict(net_flow))


class SatStatus(Enum):
    SAT = "SAT"
    UNSAT = "UNSAT"


@dataclass(frozen=True)
class SatResult:
    status: SatStatus
    assignment: Mapping[int, bool]


def _normalize_cnf(clauses: Iterable[Iterable[int]]) -> Tuple[Tuple[FrozenSet[int], ...], FrozenSet[int]]:
    normalized = []
    variables = set()
    for raw in clauses:
        clause = frozenset(raw)
        if any(not isinstance(lit, int) or isinstance(lit, bool) or lit == 0 for lit in clause):
            raise ValueError("CNF literals must be non-zero integers")
        variables.update(abs(lit) for lit in clause)
        if any(-lit in clause for lit in clause):
            continue
        normalized.append(clause)
    return tuple(normalized), frozenset(variables)


def _simplify_cnf(
    clauses: Sequence[FrozenSet[int]],
    assignment: Mapping[int, bool],
) -> Optional[Tuple[FrozenSet[int], ...]]:
    out = []
    for clause in clauses:
        satisfied = False
        remainder = set()
        for literal in clause:
            variable = abs(literal)
            if variable not in assignment:
                remainder.add(literal)
                continue
            value = assignment[variable]
            if value == (literal > 0):
                satisfied = True
                break
        if satisfied:
            continue
        if not remainder:
            return None
        out.append(frozenset(remainder))
    return tuple(out)


def _dpll(
    clauses: Sequence[FrozenSet[int]],
    assignment: MutableMapping[int, bool],
) -> Optional[Dict[int, bool]]:
    simplified = _simplify_cnf(clauses, assignment)
    if simplified is None:
        return None
    if not simplified:
        return dict(assignment)

    while True:
        units = sorted((next(iter(clause)) for clause in simplified if len(clause) == 1), key=lambda x: (abs(x), x < 0))
        if not units:
            break
        literal = units[0]
        variable = abs(literal)
        value = literal > 0
        existing = assignment.get(variable)
        if existing is not None and existing != value:
            return None
        assignment[variable] = value
        simplified = _simplify_cnf(simplified, assignment)
        if simplified is None:
            return None
        if not simplified:
            return dict(assignment)

    variable = min(abs(literal) for clause in simplified for literal in clause)
    for value in (False, True):
        child = dict(assignment)
        child[variable] = value
        solved = _dpll(simplified, child)
        if solved is not None:
            return solved
    return None


def dpll_sat(clauses: Iterable[Iterable[int]]) -> SatResult:
    """Exact finite propositional SAT for CNF encoded by signed integer literals."""
    normalized, variables = _normalize_cnf(clauses)
    if any(len(clause) == 0 for clause in normalized):
        return SatResult(SatStatus.UNSAT, {})
    solved = _dpll(normalized, {})
    if solved is None:
        return SatResult(SatStatus.UNSAT, {})
    full = {variable: solved.get(variable, False) for variable in sorted(variables)}
    return SatResult(SatStatus.SAT, full)


@dataclass(frozen=True)
class AC3Result:
    consistent: bool
    domains: Mapping[str, FrozenSet[Hashable]]


def ac3_arc_consistency(
    domains: Mapping[str, Iterable[Hashable]],
    allowed_pairs: Mapping[Tuple[str, str], FrozenSet[Tuple[Hashable, Hashable]]],
) -> AC3Result:
    """AC-3 for explicit finite directed binary-constraint relations.

    Arc consistency is a local consistency property. A consistent result does
    not prove that the full CSP has a global satisfying assignment.
    """
    current: Dict[str, set[Hashable]] = {name: set(values) for name, values in domains.items()}
    if not current or any(not name for name in current):
        raise ValueError("domains require explicit variable identities")
    if any(not values for values in current.values()):
        return AC3Result(False, {name: frozenset(values) for name, values in current.items()})

    incoming: Dict[str, set[str]] = {name: set() for name in current}
    for (left, right), relation in allowed_pairs.items():
        if left not in current or right not in current or left == right:
            raise ValueError("constraint arcs must reference distinct declared variables")
        if not isinstance(relation, frozenset):
            raise ValueError("allowed-pair relations must be frozenset values")
        incoming[right].add(left)

    queue = deque(sorted(allowed_pairs))
    while queue:
        left, right = queue.popleft()
        relation = allowed_pairs[(left, right)]
        revised = False
        remove = []
        for x in current[left]:
            if not any((x, y) in relation for y in current[right]):
                remove.append(x)
        if remove:
            revised = True
            current[left].difference_update(remove)
        if not current[left]:
            return AC3Result(False, {name: frozenset(values) for name, values in current.items()})
        if revised:
            for neighbor in sorted(incoming[left]):
                if neighbor != right:
                    queue.append((neighbor, left))

    return AC3Result(True, {name: frozenset(values) for name, values in current.items()})
