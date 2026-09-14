"""Incremental load-bearing reachability index for AMOS dependency graphs.

Origin architect / steward: Trang Phan.

Algorithmic basis:
- transitive closure semantics for directed dependency reachability;
- insertion-local delta propagation, analogous to semi-naive/incremental dataflow:
  after adding u->v, only Pred(u) x Succ(v) can become newly reachable;
- Tarjan strongly connected components for explicit cycle localization.

This module treats graph edges as dependency relations, not causal claims. Edge
removal deliberately falls back to full recomputation rather than pretending
insertion-only deltas are deletion-correct.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, Mapping, Optional, Sequence, Set, Tuple


class IncrementalStatus(Enum):
    APPLIED = "APPLIED"
    NO_CHANGE = "NO_CHANGE"
    CYCLE_BLOCKED = "CYCLE_BLOCKED"
    RECOMPUTED = "RECOMPUTED"
    RECOMPUTE_REQUIRED = "RECOMPUTE_REQUIRED"
    UNKNOWN_NODE = "UNKNOWN_NODE"


@dataclass(frozen=True)
class UpdateResult:
    status: IncrementalStatus
    edge: Tuple[str, str]
    delta_pairs: Tuple[Tuple[str, str], ...]
    cycle_component: Tuple[str, ...] = ()


def tarjan_scc(nodes: Sequence[str], edges: Iterable[Tuple[str, str]]) -> Tuple[Tuple[str, ...], ...]:
    """Return deterministic strongly-connected components using Tarjan's algorithm."""
    ordered = tuple(dict.fromkeys(nodes))
    graph: Dict[str, Set[str]] = {n: set() for n in ordered}
    for src, dst in edges:
        if src in graph and dst in graph:
            graph[src].add(dst)
    index = 0
    stack: list[str] = []
    on_stack: Set[str] = set()
    indices: Dict[str, int] = {}
    low: Dict[str, int] = {}
    comps: list[Tuple[str, ...]] = []

    def strongconnect(v: str) -> None:
        nonlocal index
        indices[v] = index
        low[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)
        for w in sorted(graph[v]):
            if w not in indices:
                strongconnect(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                comp.append(w)
                if w == v:
                    break
            comps.append(tuple(sorted(comp)))

    for node in ordered:
        if node not in indices:
            strongconnect(node)
    return tuple(sorted(comps))


def full_closure(nodes: Sequence[str], edges: Iterable[Tuple[str, str]]) -> Mapping[str, frozenset[str]]:
    graph: Dict[str, Set[str]] = {n: set() for n in nodes}
    for src, dst in edges:
        if src in graph and dst in graph:
            graph[src].add(dst)
    result: Dict[str, frozenset[str]] = {}
    for src in nodes:
        seen: Set[str] = set()
        stack = list(graph[src])
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            stack.extend(graph[node] - seen)
        result[src] = frozenset(seen)
    return result


class IncrementalReachability:
    """Insertion-incremental exact reachability with fail-closed cycle policy."""

    def __init__(self, nodes: Sequence[str], edges: Iterable[Tuple[str, str]] = (), *, allow_cycles: bool = False):
        self.nodes = tuple(dict.fromkeys(nodes))
        if len(self.nodes) != len(tuple(nodes)):
            raise ValueError("node ids must be unique")
        if any(not n.strip() for n in self.nodes):
            raise ValueError("node ids must be non-empty")
        self._node_set = set(self.nodes)
        self.allow_cycles = allow_cycles
        self.edges: Set[Tuple[str, str]] = set()
        self.reach: Dict[str, Set[str]] = {n: set() for n in self.nodes}
        for src, dst in edges:
            result = self.add_edge(src, dst)
            if result.status in {IncrementalStatus.UNKNOWN_NODE, IncrementalStatus.CYCLE_BLOCKED}:
                raise ValueError(f"invalid initial edge {src}->{dst}: {result.status.value}")

    def snapshot(self) -> Mapping[str, frozenset[str]]:
        return {n: frozenset(self.reach[n]) for n in self.nodes}

    def _predecessors_including(self, node: str) -> Set[str]:
        return {p for p in self.nodes if node in self.reach[p]} | {node}

    def _successors_including(self, node: str) -> Set[str]:
        return set(self.reach[node]) | {node}

    def add_edge(self, src: str, dst: str) -> UpdateResult:
        if src not in self._node_set or dst not in self._node_set:
            return UpdateResult(IncrementalStatus.UNKNOWN_NODE, (src, dst), ())
        if (src, dst) in self.edges:
            return UpdateResult(IncrementalStatus.NO_CHANGE, (src, dst), ())
        if not self.allow_cycles and (src == dst or src in self.reach[dst]):
            proposed = self.edges | {(src, dst)}
            comp = next((c for c in tarjan_scc(self.nodes, proposed) if len(c) > 1 or (len(c)==1 and (c[0],c[0]) in proposed)), ())
            return UpdateResult(IncrementalStatus.CYCLE_BLOCKED, (src, dst), (), comp)

        predecessors = self._predecessors_including(src)
        successors = self._successors_including(dst)
        delta = {(p, s) for p in predecessors for s in successors if s not in self.reach[p]}
        self.edges.add((src, dst))
        for p, s in delta:
            self.reach[p].add(s)
        return UpdateResult(IncrementalStatus.APPLIED, (src, dst), tuple(sorted(delta)))

    def remove_edge(self, src: str, dst: str, *, full_recompute_on_delete: bool = False) -> UpdateResult:
        if src not in self._node_set or dst not in self._node_set:
            return UpdateResult(IncrementalStatus.UNKNOWN_NODE, (src, dst), ())
        if (src, dst) not in self.edges:
            return UpdateResult(IncrementalStatus.NO_CHANGE, (src, dst), ())
        if not full_recompute_on_delete:
            return UpdateResult(IncrementalStatus.RECOMPUTE_REQUIRED, (src, dst), ())
        before = {(a,b) for a in self.nodes for b in self.reach[a]}
        self.edges.remove((src, dst))
        new = full_closure(self.nodes, self.edges)
        self.reach = {n: set(new[n]) for n in self.nodes}
        after = {(a,b) for a in self.nodes for b in self.reach[a]}
        delta = before.symmetric_difference(after)
        return UpdateResult(IncrementalStatus.RECOMPUTED, (src, dst), tuple(sorted(delta)))
