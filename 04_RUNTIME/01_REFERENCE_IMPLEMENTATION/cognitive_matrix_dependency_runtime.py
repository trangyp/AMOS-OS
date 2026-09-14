"""Typed dependency graph and selective invalidation for the AMOS Cognitive Matrix.

Origin architect / steward: Trang Phan.

Relations are semantic graph relations, not causal claims. Only explicitly load-bearing
relations participate in dependency closure. The runtime computes proposals/state
classification only; it does not authorize durable effects or Canon promotion.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Set, Tuple


class RelationType(Enum):
    NECESSARY = "NECESSARY"
    SUFFICIENT = "SUFFICIENT"
    SUPPORTING = "SUPPORTING"
    ALTERNATIVE = "ALTERNATIVE"
    CONTRADICTING = "CONTRADICTING"
    DERIVED_FROM = "DERIVED_FROM"
    OBSERVED_BY = "OBSERVED_BY"
    SUPERSEDES = "SUPERSEDES"
    INVALIDATES = "INVALIDATES"
    CONDITIONED_ON = "CONDITIONED_ON"
    CORRELATED_WITH = "CORRELATED_WITH"


class NodeState(Enum):
    ACTIVE = "ACTIVE"
    STALE = "STALE"
    FALSIFIED = "FALSIFIED"
    QUARANTINED = "QUARANTINED"
    SUPERSEDED = "SUPERSEDED"
    UNKNOWN_GAP = "UNKNOWN/GAP"


class GraphStatus(Enum):
    VALID_BOUNDED = "VALID_BOUNDED"
    INVALID = "INVALID"
    UNKNOWN_GAP = "UNKNOWN/GAP"


_LOAD_BEARING = {
    RelationType.NECESSARY,
    RelationType.DERIVED_FROM,
    RelationType.CONDITIONED_ON,
}
_REVIEW_ON_SOURCE_LOSS = {RelationType.SUPPORTING, RelationType.SUFFICIENT}
_NON_DEPENDENCY = {
    RelationType.ALTERNATIVE,
    RelationType.CONTRADICTING,
    RelationType.OBSERVED_BY,
    RelationType.SUPERSEDES,
    RelationType.INVALIDATES,
    RelationType.CORRELATED_WITH,
}


@dataclass(frozen=True)
class GraphNode:
    node_id: str
    state: NodeState
    scope: str
    regime: str
    source_version: str
    provenance: str

    def __post_init__(self) -> None:
        for name in ("node_id", "scope", "regime", "source_version", "provenance"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must be explicit")


@dataclass(frozen=True)
class RelationEdge:
    edge_id: str
    src: str
    dst: str
    relation: RelationType
    provenance: str
    source_version: str
    active: bool = True

    def __post_init__(self) -> None:
        for name in ("edge_id", "src", "dst", "provenance", "source_version"):
            if not getattr(self, name).strip():
                raise ValueError(f"edge field {name} must be explicit")


@dataclass(frozen=True)
class DependencyGraph:
    graph_id: str
    scope: str
    regime: str
    nodes: Tuple[GraphNode, ...]
    edges: Tuple[RelationEdge, ...]

    def __post_init__(self) -> None:
        if not self.graph_id.strip() or not self.scope.strip() or not self.regime.strip():
            raise ValueError("graph_id, scope, and regime must be explicit")


@dataclass(frozen=True)
class GraphTopology:
    ordered_ids: Tuple[str, ...]
    adjacency: Tuple[Tuple[int, ...], ...]
    closure: Tuple[Tuple[int, ...], ...]
    cycle_nodes: Tuple[str, ...]

    def dependencies_of(self, node_id: str) -> Tuple[str, ...]:
        i = self.ordered_ids.index(node_id)
        return tuple(self.ordered_ids[j] for j, bit in enumerate(self.closure[i]) if bit and j != i)

    def descendants_of(self, node_id: str) -> Tuple[str, ...]:
        j = self.ordered_ids.index(node_id)
        return tuple(self.ordered_ids[i] for i, row in enumerate(self.closure) if row[j] and i != j)


@dataclass(frozen=True)
class GraphAudit:
    status: GraphStatus
    errors: Tuple[str, ...]
    topology: Optional[GraphTopology]
    contradiction_pairs: Tuple[Tuple[str, str], ...]
    invalidation_proposals: Tuple[Tuple[str, str], ...]
    supersession_pairs: Tuple[Tuple[str, str], ...]


@dataclass(frozen=True)
class InvalidationResult:
    blocked: bool
    reason: Optional[str]
    seed_ids: Tuple[str, ...]
    stale_ids: Tuple[str, ...]
    review_ids: Tuple[str, ...]
    preserved_ids: Tuple[str, ...]


def is_load_bearing(relation: RelationType) -> bool:
    return relation in _LOAD_BEARING


def build_load_bearing_topology(graph: DependencyGraph) -> GraphTopology:
    ids = tuple(node.node_id for node in graph.nodes)
    index = {node_id: i for i, node_id in enumerate(ids)}
    n = len(ids)
    adjacency = [[0] * n for _ in range(n)]
    for edge in graph.edges:
        if edge.active and edge.relation in _LOAD_BEARING and edge.src in index and edge.dst in index:
            adjacency[index[edge.src]][index[edge.dst]] = 1
    closure = [row[:] for row in adjacency]
    for k in range(n):
        for i in range(n):
            if closure[i][k]:
                for j in range(n):
                    closure[i][j] = int(bool(closure[i][j] or closure[k][j]))
    cycle_nodes = tuple(ids[i] for i in range(n) if closure[i][i])
    return GraphTopology(ids, tuple(map(tuple, adjacency)), tuple(map(tuple, closure)), cycle_nodes)


def audit_graph(graph: DependencyGraph) -> GraphAudit:
    errors: List[str] = []
    node_ids = [node.node_id for node in graph.nodes]
    edge_ids = [edge.edge_id for edge in graph.edges]
    node_set = set(node_ids)
    if len(node_ids) != len(node_set):
        errors.append("DUPLICATE_NODE_ID")
    if len(edge_ids) != len(set(edge_ids)):
        errors.append("DUPLICATE_EDGE_ID")
    for edge in graph.edges:
        if edge.src not in node_set:
            errors.append(f"UNKNOWN_EDGE_SOURCE:{edge.edge_id}:{edge.src}")
        if edge.dst not in node_set:
            errors.append(f"UNKNOWN_EDGE_TARGET:{edge.edge_id}:{edge.dst}")
    topology = build_load_bearing_topology(graph) if len(node_ids) == len(node_set) else None
    if topology and topology.cycle_nodes:
        errors.append("LOAD_BEARING_CYCLE_REQUIRES_FIXED_POINT_SEMANTICS")
    contradictions = tuple(sorted(
        (edge.src, edge.dst) for edge in graph.edges
        if edge.active and edge.relation is RelationType.CONTRADICTING
    ))
    invalidations = tuple(sorted(
        (edge.src, edge.dst) for edge in graph.edges
        if edge.active and edge.relation is RelationType.INVALIDATES
    ))
    supersessions = tuple(sorted(
        (edge.src, edge.dst) for edge in graph.edges
        if edge.active and edge.relation is RelationType.SUPERSEDES
    ))
    if any(err.startswith("UNKNOWN_EDGE_") or err.startswith("DUPLICATE_") for err in errors):
        status = GraphStatus.INVALID
    elif topology and topology.cycle_nodes:
        status = GraphStatus.UNKNOWN_GAP
    else:
        status = GraphStatus.VALID_BOUNDED
    return GraphAudit(status, tuple(errors), topology, contradictions, invalidations, supersessions)


def dependency_map(graph: DependencyGraph) -> Mapping[str, Tuple[str, ...]]:
    """Export direct load-bearing dependencies for coverage-scope construction."""
    node_ids = {node.node_id for node in graph.nodes}
    out: Dict[str, Set[str]] = {node_id: set() for node_id in node_ids}
    for edge in graph.edges:
        if edge.active and edge.relation in _LOAD_BEARING and edge.src in node_ids and edge.dst in node_ids:
            out[edge.src].add(edge.dst)
    return {node_id: tuple(sorted(deps)) for node_id, deps in sorted(out.items())}


def propagate_invalidation(graph: DependencyGraph, invalidated_ids: Iterable[str]) -> InvalidationResult:
    """Compute selective stale/review proposals; never commits state or truth changes."""
    audit = audit_graph(graph)
    node_ids = {node.node_id for node in graph.nodes}
    seeds = tuple(sorted(set(invalidated_ids)))
    unknown_seeds = tuple(seed for seed in seeds if seed not in node_ids)
    if audit.status is GraphStatus.INVALID:
        return InvalidationResult(True, "INVALID_GRAPH", seeds, (), (), tuple(sorted(node_ids)))
    if audit.status is GraphStatus.UNKNOWN_GAP:
        return InvalidationResult(True, "LOAD_BEARING_CYCLE", seeds, (), (), tuple(sorted(node_ids)))
    if unknown_seeds:
        return InvalidationResult(True, "UNKNOWN_INVALIDATION_SEED:" + ",".join(unknown_seeds), seeds, (), (), tuple(sorted(node_ids)))

    stale: Set[str] = set()
    review: Set[str] = set()
    queue = list(seeds)
    seen = set(seeds)

    reverse_load: Dict[str, Set[str]] = {node_id: set() for node_id in node_ids}
    reverse_review: Dict[str, Set[str]] = {node_id: set() for node_id in node_ids}
    for edge in graph.edges:
        if not edge.active:
            continue
        if edge.relation in _LOAD_BEARING:
            reverse_load[edge.dst].add(edge.src)
        elif edge.relation in _REVIEW_ON_SOURCE_LOSS:
            reverse_review[edge.src].add(edge.dst)

    for seed in seeds:
        review.update(reverse_review.get(seed, ()))

    while queue:
        lost = queue.pop(0)
        for dependent in sorted(reverse_load.get(lost, ())):
            if dependent not in seen:
                seen.add(dependent)
                stale.add(dependent)
                queue.append(dependent)
            review.update(reverse_review.get(dependent, ()))

    stale.difference_update(seeds)
    review.difference_update(seeds)
    review.difference_update(stale)
    preserved = node_ids.difference(seeds).difference(stale).difference(review)
    return InvalidationResult(False, None, seeds, tuple(sorted(stale)), tuple(sorted(review)), tuple(sorted(preserved)))


def apply_supersession_proposal(graph: DependencyGraph, superseder_id: str) -> Tuple[str, ...]:
    """Return predecessors proposed for SUPERSEDED state; no durable mutation occurs."""
    audit = audit_graph(graph)
    if audit.status is GraphStatus.INVALID:
        return ()
    return tuple(sorted(dst for src, dst in audit.supersession_pairs if src == superseder_id))


def contradiction_partners(graph: DependencyGraph, node_id: str) -> Tuple[str, ...]:
    partners: Set[str] = set()
    for edge in graph.edges:
        if edge.active and edge.relation is RelationType.CONTRADICTING:
            if edge.src == node_id:
                partners.add(edge.dst)
            if edge.dst == node_id:
                partners.add(edge.src)
    return tuple(sorted(partners))
