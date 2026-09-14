"""Bounded finite-graph backend for the AMOS URK math substrate.

Origin architect / steward: Trang Phan.

Scope
-----
This module implements finite directed-graph structure only. It does not infer
causation, ontology, empirical truth, or Canon authority from graph topology.

Mathematical carrier
--------------------
For a finite node tuple V=(v_0,...,v_{n-1}) and edge relation E subset V x V,
A in {0,1}^{n x n} is defined by A[i][j] = 1 iff (v_i,v_j) in E.
Reachability uses the Boolean semiring (OR, AND). SCCs are equivalence classes
of mutual reachability. Condensation contracts SCCs and must be a DAG.
Transitive reduction is exposed only for DAGs.

External backend
----------------
NetworkX is optional. When available, its results are used only for bounded
differential validation against the portable implementation. Availability or
agreement does not promote Canon or change AMOS semantic types.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Set, Tuple

Node = str
Edge = Tuple[Node, Node]
BoolMatrix = Tuple[Tuple[bool, ...], ...]

NETWORKX_EXPECTED_VERSION = "3.6.1"
SOURCE_BINDINGS = {
    "networkx_scc": "NetworkX 3.6.1 strongly_connected_components documentation",
    "networkx_condensation": "NetworkX 3.6.1 condensation documentation",
    "networkx_dag": "NetworkX 3.6.1 DAG/transitive_reduction documentation",
    "graphblas": "GraphBLAS semiring-parametric sparse matrix specification (design boundary only)",
}


class GraphContractError(ValueError):
    """Raised when a finite graph violates the typed backend contract."""


@dataclass(frozen=True)
class FiniteDiGraph:
    nodes: Tuple[Node, ...]
    edges: Tuple[Edge, ...]

    def __post_init__(self) -> None:
        if not self.nodes:
            raise GraphContractError("nodes must be non-empty")
        if any(not isinstance(v, str) or not v for v in self.nodes):
            raise GraphContractError("every node must be a non-empty string")
        if len(set(self.nodes)) != len(self.nodes):
            raise GraphContractError("nodes must be unique")
        node_set = set(self.nodes)
        normalized: Set[Edge] = set()
        for e in self.edges:
            if not isinstance(e, tuple) or len(e) != 2:
                raise GraphContractError("each edge must be a 2-tuple")
            u, v = e
            if u not in node_set or v not in node_set:
                raise GraphContractError(f"edge endpoint outside node set: {e!r}")
            normalized.add((u, v))
        if len(normalized) != len(self.edges):
            raise GraphContractError("duplicate edges are not admitted")

    @classmethod
    def build(cls, nodes: Sequence[Node], edges: Iterable[Sequence[Node]]) -> "FiniteDiGraph":
        ns = tuple(nodes)
        idx = {v: i for i, v in enumerate(ns)}
        if len(idx) != len(ns):
            return cls(ns, tuple((str(e[0]), str(e[1])) for e in edges))
        raw: List[Edge] = []
        for e in edges:
            if not isinstance(e, (list, tuple)) or len(e) != 2:
                raise GraphContractError("each edge must have exactly two endpoints")
            raw.append((e[0], e[1]))
        raw.sort(key=lambda e: (idx.get(e[0], len(ns)), idx.get(e[1], len(ns)), repr(e)))
        return cls(ns, tuple(raw))

    @property
    def index(self) -> Dict[Node, int]:
        return {v: i for i, v in enumerate(self.nodes)}

    def successors(self) -> Dict[Node, Set[Node]]:
        out = {v: set() for v in self.nodes}
        for u, v in self.edges:
            out[u].add(v)
        return out

    def predecessors(self) -> Dict[Node, Set[Node]]:
        out = {v: set() for v in self.nodes}
        for u, v in self.edges:
            out[v].add(u)
        return out


def adjacency_matrix(g: FiniteDiGraph) -> BoolMatrix:
    idx = g.index
    rows = [[False] * len(g.nodes) for _ in g.nodes]
    for u, v in g.edges:
        rows[idx[u]][idx[v]] = True
    return tuple(tuple(row) for row in rows)


def graph_from_adjacency(nodes: Sequence[Node], matrix: Sequence[Sequence[bool]]) -> FiniteDiGraph:
    ns = tuple(nodes)
    n = len(ns)
    if len(matrix) != n or any(len(row) != n for row in matrix):
        raise GraphContractError("adjacency matrix must be square with shape |V| x |V|")
    edges: List[Edge] = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if not isinstance(value, bool):
                raise GraphContractError("adjacency entries must be bool")
            if value:
                edges.append((ns[i], ns[j]))
    return FiniteDiGraph.build(ns, edges)


def boolean_matmul(a: BoolMatrix, b: BoolMatrix) -> BoolMatrix:
    n = len(a)
    if n == 0 or len(b) != n or any(len(r) != n for r in a) or any(len(r) != n for r in b):
        raise GraphContractError("Boolean matrix product requires equal non-empty square matrices")
    return tuple(
        tuple(any(a[i][k] and b[k][j] for k in range(n)) for j in range(n))
        for i in range(n)
    )


def reflexive_transitive_closure(g: FiniteDiGraph) -> BoolMatrix:
    """Return I OR A OR ... over the Boolean semiring by Warshall closure."""
    r = [list(row) for row in adjacency_matrix(g)]
    n = len(g.nodes)
    for i in range(n):
        r[i][i] = True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    if r[k][j]:
                        r[i][j] = True
    return tuple(tuple(row) for row in r)


def reachable_nodes(g: FiniteDiGraph, start: Node, *, ignore_edge: Optional[Edge] = None) -> Set[Node]:
    if start not in g.index:
        raise GraphContractError("start node is outside graph")
    succ = g.successors()
    seen = {start}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in succ[u]:
            if ignore_edge is not None and (u, v) == ignore_edge:
                continue
            if v not in seen:
                seen.add(v)
                q.append(v)
    return seen


def strongly_connected_components(g: FiniteDiGraph) -> Tuple[Tuple[Node, ...], ...]:
    """Tarjan SCC partition with deterministic component/node ordering."""
    succ = g.successors()
    order = g.index
    next_index = 0
    stack: List[Node] = []
    on_stack: Set[Node] = set()
    index: Dict[Node, int] = {}
    low: Dict[Node, int] = {}
    comps: List[Tuple[Node, ...]] = []

    def visit(v: Node) -> None:
        nonlocal next_index
        index[v] = next_index
        low[v] = next_index
        next_index += 1
        stack.append(v)
        on_stack.add(v)
        for w in sorted(succ[v], key=order.__getitem__):
            if w not in index:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp: List[Node] = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                comp.append(w)
                if w == v:
                    break
            comp.sort(key=order.__getitem__)
            comps.append(tuple(comp))

    for v in g.nodes:
        if v not in index:
            visit(v)
    comps.sort(key=lambda c: min(order[x] for x in c))
    return tuple(comps)


@dataclass(frozen=True)
class Condensation:
    components: Tuple[Tuple[Node, ...], ...]
    component_of: Mapping[Node, int]
    edges: Tuple[Tuple[int, int], ...]


def condensation(g: FiniteDiGraph) -> Condensation:
    comps = strongly_connected_components(g)
    comp_of: Dict[Node, int] = {v: i for i, comp in enumerate(comps) for v in comp}
    c_edges = sorted({(comp_of[u], comp_of[v]) for u, v in g.edges if comp_of[u] != comp_of[v]})
    c = Condensation(comps, comp_of, tuple(c_edges))
    topological_order_components(c)
    return c


def topological_order_components(c: Condensation) -> Tuple[int, ...]:
    n = len(c.components)
    succ = {i: set() for i in range(n)}
    indeg = {i: 0 for i in range(n)}
    for u, v in c.edges:
        if v not in succ[u]:
            succ[u].add(v)
            indeg[v] += 1
    ready = [i for i in range(n) if indeg[i] == 0]
    ready.sort()
    out: List[int] = []
    while ready:
        u = ready.pop(0)
        out.append(u)
        for v in sorted(succ[u]):
            indeg[v] -= 1
            if indeg[v] == 0:
                ready.append(v)
                ready.sort()
    if len(out) != n:
        raise GraphContractError("condensation must be acyclic")
    return tuple(out)


def topological_order(g: FiniteDiGraph) -> Tuple[Node, ...]:
    succ = g.successors()
    indeg = {v: 0 for v in g.nodes}
    for _, v in g.edges:
        indeg[v] += 1
    order_idx = g.index
    ready = [v for v in g.nodes if indeg[v] == 0]
    ready.sort(key=order_idx.__getitem__)
    out: List[Node] = []
    while ready:
        u = ready.pop(0)
        out.append(u)
        for v in sorted(succ[u], key=order_idx.__getitem__):
            indeg[v] -= 1
            if indeg[v] == 0:
                ready.append(v)
                ready.sort(key=order_idx.__getitem__)
    if len(out) != len(g.nodes):
        raise GraphContractError("topological order requires a DAG")
    return tuple(out)


def transitive_reduction_dag(g: FiniteDiGraph) -> FiniteDiGraph:
    """Return the unique transitive reduction for a finite DAG."""
    topological_order(g)
    keep: List[Edge] = []
    for e in g.edges:
        u, v = e
        if v not in reachable_nodes(g, u, ignore_edge=e):
            keep.append(e)
    return FiniteDiGraph.build(g.nodes, keep)


def sink_sccs(g: FiniteDiGraph) -> Tuple[Tuple[Node, ...], ...]:
    c = condensation(g)
    out_degree = {i: 0 for i in range(len(c.components))}
    for u, _ in c.edges:
        out_degree[u] += 1
    return tuple(c.components[i] for i in range(len(c.components)) if out_degree[i] == 0)


def bfs_distance_to_targets(g: FiniteDiGraph, start: Node, targets: Iterable[Node]) -> Optional[int]:
    if start not in g.index:
        raise GraphContractError("start node is outside graph")
    target_set = set(targets)
    if not target_set <= set(g.nodes):
        raise GraphContractError("target node is outside graph")
    if not target_set:
        return None
    if start in target_set:
        return 0
    succ = g.successors()
    seen = {start}
    q = deque([(start, 0)])
    while q:
        u, d = q.popleft()
        for v in succ[u]:
            if v in target_set:
                return d + 1
            if v not in seen:
                seen.add(v)
                q.append((v, d + 1))
    return None


def networkx_binding_state() -> Dict[str, Any]:
    try:
        import networkx as nx  # type: ignore
    except Exception as exc:
        return {
            "available": False,
            "status": "UNAVAILABLE",
            "expected_version": NETWORKX_EXPECTED_VERSION,
            "observed_version": None,
            "reason": f"{type(exc).__name__}: {exc}",
        }
    observed = str(getattr(nx, "__version__", "UNKNOWN"))
    return {
        "available": True,
        "status": "BOUND_EXACT_VERSION" if observed == NETWORKX_EXPECTED_VERSION else "BOUND_VERSION_MISMATCH",
        "expected_version": NETWORKX_EXPECTED_VERSION,
        "observed_version": observed,
        "reason": None,
    }


def differential_networkx(g: FiniteDiGraph) -> Dict[str, Any]:
    """Differentially validate portable results against NetworkX when available."""
    state = networkx_binding_state()
    if not state["available"]:
        return {"success": False, "status": "UNAVAILABLE", "binding": state}
    import networkx as nx  # type: ignore

    G = nx.DiGraph()
    G.add_nodes_from(g.nodes)
    G.add_edges_from(g.edges)
    ours_scc = {frozenset(c) for c in strongly_connected_components(g)}
    nx_scc = {frozenset(c) for c in nx.strongly_connected_components(G)}
    ours_sink = {frozenset(c) for c in sink_sccs(g)}
    nx_sink = {frozenset(c) for c in nx.attracting_components(G)}
    checks = {
        "scc_partition": ours_scc == nx_scc,
        "sink_scc": ours_sink == nx_sink,
    }
    if nx.is_directed_acyclic_graph(G):
        tr = transitive_reduction_dag(g)
        nx_tr = nx.transitive_reduction(G)
        checks["transitive_reduction"] = set(tr.edges) == set(nx_tr.edges())
        topo = topological_order(g)
        pos = {v: i for i, v in enumerate(topo)}
        checks["topological_order"] = all(pos[u] < pos[v] for u, v in g.edges)
    return {
        "success": all(checks.values()),
        "status": "PASS" if all(checks.values()) else "MISMATCH",
        "binding": state,
        "checks": checks,
    }


def validate_backend_invariants(g: FiniteDiGraph) -> Tuple[str, ...]:
    failures: List[str] = []
    if graph_from_adjacency(g.nodes, adjacency_matrix(g)) != g:
        failures.append("RELATION_MATRIX_ROUNDTRIP")
    closure = reflexive_transitive_closure(g)
    if any(not closure[i][i] for i in range(len(g.nodes))):
        failures.append("CLOSURE_NOT_REFLEXIVE")
    for i in range(len(g.nodes)):
        for j in range(len(g.nodes)):
            if closure[i][j]:
                for k in range(len(g.nodes)):
                    if closure[j][k] and not closure[i][k]:
                        failures.append("CLOSURE_NOT_TRANSITIVE")
                        return tuple(failures)
    comps = strongly_connected_components(g)
    flat = [v for c in comps for v in c]
    if len(flat) != len(g.nodes) or set(flat) != set(g.nodes):
        failures.append("SCC_NOT_PARTITION")
    for comp in comps:
        for u in comp:
            ru = reachable_nodes(g, u)
            for v in comp:
                if v not in ru or u not in reachable_nodes(g, v):
                    failures.append("SCC_NOT_MUTUAL_REACHABILITY")
                    return tuple(failures)
    c = condensation(g)
    try:
        topological_order_components(c)
    except GraphContractError:
        failures.append("CONDENSATION_NOT_DAG")
    return tuple(failures)
