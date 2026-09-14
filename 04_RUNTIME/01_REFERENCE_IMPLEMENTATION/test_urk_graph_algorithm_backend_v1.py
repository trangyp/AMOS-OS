#!/usr/bin/env python3
"""Exhaustive/adversarial tests for urk_graph_algorithm_backend_v1.

Origin architect / steward: Trang Phan.
"""
from __future__ import annotations

import itertools
import random

import networkx as nx

from urk_graph_algorithm_backend_v1 import (
    FiniteDiGraph,
    GraphContractError,
    adjacency_matrix,
    bfs_distance_to_targets,
    condensation,
    differential_networkx,
    graph_from_adjacency,
    networkx_binding_state,
    reflexive_transitive_closure,
    sink_sccs,
    strongly_connected_components,
    topological_order,
    topological_order_components,
    transitive_reduction_dag,
    validate_backend_invariants,
)


def check(cond, msg):
    if not cond:
        raise AssertionError(msg)


def all_directed_graphs_3():
    nodes = ("a", "b", "c")
    possible = tuple((u, v) for u in nodes for v in nodes)
    for mask in range(1 << len(possible)):
        edges = tuple(e for i, e in enumerate(possible) if (mask >> i) & 1)
        yield FiniteDiGraph.build(nodes, edges)


def all_forward_dags_5():
    nodes = tuple("abcde")
    possible = tuple((nodes[i], nodes[j]) for i in range(len(nodes)) for j in range(i + 1, len(nodes)))
    for mask in range(1 << len(possible)):
        edges = tuple(e for i, e in enumerate(possible) if (mask >> i) & 1)
        yield FiniteDiGraph.build(nodes, edges)


def nx_reachability(g):
    G = nx.DiGraph()
    G.add_nodes_from(g.nodes)
    G.add_edges_from(g.edges)
    return tuple(tuple(i == j or nx.has_path(G, g.nodes[i], g.nodes[j]) for j in range(len(g.nodes))) for i in range(len(g.nodes)))


def main():
    binding = networkx_binding_state()
    check(binding["available"], binding)
    check(binding["observed_version"] == "3.6.1", binding)

    count = 0
    for g in all_directed_graphs_3():
        count += 1
        check(validate_backend_invariants(g) == (), ("invariants", g))
        check(graph_from_adjacency(g.nodes, adjacency_matrix(g)) == g, ("roundtrip", g))
        check(reflexive_transitive_closure(g) == nx_reachability(g), ("closure", g))
        check(differential_networkx(g)["success"], ("networkx", g, differential_networkx(g)))
        c = condensation(g)
        topological_order_components(c)
        ours_scc = {frozenset(x) for x in strongly_connected_components(g)}
        G = nx.DiGraph(); G.add_nodes_from(g.nodes); G.add_edges_from(g.edges)
        check(ours_scc == {frozenset(x) for x in nx.strongly_connected_components(G)}, ("scc", g))
        check({frozenset(x) for x in sink_sccs(g)} == {frozenset(x) for x in nx.attracting_components(G)}, ("sink", g))

    dag_count = 0
    for g in all_forward_dags_5():
        dag_count += 1
        order = topological_order(g)
        pos = {v: i for i, v in enumerate(order)}
        check(all(pos[u] < pos[v] for u, v in g.edges), ("topo", g))
        reduced = transitive_reduction_dag(g)
        G = nx.DiGraph(); G.add_nodes_from(g.nodes); G.add_edges_from(g.edges)
        check(set(reduced.edges) == set(nx.transitive_reduction(G).edges()), ("reduction", g, reduced.edges))
        check(reflexive_transitive_closure(reduced) == reflexive_transitive_closure(g), ("reduction_closure", g))

    cyclic = FiniteDiGraph.build(("a", "b"), (("a", "b"), ("b", "a")))
    try:
        transitive_reduction_dag(cyclic)
        raise AssertionError("cyclic transitive reduction must fail closed")
    except GraphContractError:
        pass

    dist = FiniteDiGraph.build(("a", "b", "c", "d"), (("a", "b"), ("b", "c")))
    check(bfs_distance_to_targets(dist, "a", {"c"}) == 2, "distance")
    check(bfs_distance_to_targets(dist, "a", {"a"}) == 0, "zero_distance")
    check(bfs_distance_to_targets(dist, "a", {"d"}) is None, "unreachable")

    rng = random.Random(206)
    random_checks = 0
    nodes = tuple(str(i) for i in range(8))
    possible = tuple((u, v) for u in nodes for v in nodes)
    for _ in range(500):
        edges = tuple(e for e in possible if rng.random() < 0.12)
        g = FiniteDiGraph.build(nodes, edges)
        check(validate_backend_invariants(g) == (), ("random_invariants", g))
        check(reflexive_transitive_closure(g) == nx_reachability(g), ("random_closure", g))
        random_checks += 1

    print({
        "status": "PASS",
        "networkx_version": binding["observed_version"],
        "directed_graphs_3": count,
        "forward_dags_5": dag_count,
        "random_graphs_8": random_checks,
        "semantic_boundary": "TOPOLOGY_NOT_CAUSATION",
    })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
