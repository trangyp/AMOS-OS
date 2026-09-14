import random

from cognitive_matrix_dependency_runtime import (
    DependencyGraph,
    GraphNode,
    GraphStatus,
    NodeState,
    RelationEdge,
    RelationType,
    apply_supersession_proposal,
    audit_graph,
    build_load_bearing_topology,
    contradiction_partners,
    dependency_map,
    is_load_bearing,
    propagate_invalidation,
)


def node(node_id):
    return GraphNode(node_id, NodeState.ACTIVE, "scope", "regime", "v1", f"repo:{node_id}")


def edge(eid, src, relation, dst, active=True):
    return RelationEdge(eid, src, dst, relation, f"repo:{eid}", "v1", active)


def graph(nodes, edges):
    return DependencyGraph("g", "scope", "regime", tuple(node(x) for x in nodes), tuple(edges))


def test_relation_type_load_bearing_boundary_is_explicit():
    assert is_load_bearing(RelationType.NECESSARY)
    assert is_load_bearing(RelationType.DERIVED_FROM)
    assert is_load_bearing(RelationType.CONDITIONED_ON)
    assert not is_load_bearing(RelationType.SUPPORTING)
    assert not is_load_bearing(RelationType.CORRELATED_WITH)
    assert not is_load_bearing(RelationType.INVALIDATES)


def test_load_bearing_matrix_direction_means_source_depends_on_destination():
    g = graph(["a", "b", "c"], [
        edge("e1", "b", RelationType.NECESSARY, "a"),
        edge("e2", "c", RelationType.DERIVED_FROM, "b"),
    ])
    t = build_load_bearing_topology(g)
    assert t.adjacency == ((0, 0, 0), (1, 0, 0), (0, 1, 0))
    assert t.dependencies_of("c") == ("a", "b")
    assert t.descendants_of("a") == ("b", "c")


def test_support_correlation_and_observation_do_not_enter_dependency_closure():
    g = graph(["a", "b", "c", "d"], [
        edge("e1", "a", RelationType.SUPPORTING, "b"),
        edge("e2", "b", RelationType.CORRELATED_WITH, "c"),
        edge("e3", "c", RelationType.OBSERVED_BY, "d"),
    ])
    assert build_load_bearing_topology(g).closure == ((0, 0, 0, 0),) * 4


def test_unknown_edge_endpoint_makes_graph_invalid():
    g = graph(["a"], [edge("e", "a", RelationType.NECESSARY, "missing")])
    audit = audit_graph(g)
    assert audit.status is GraphStatus.INVALID
    assert any(x.startswith("UNKNOWN_EDGE_TARGET") for x in audit.errors)


def test_duplicate_node_and_edge_ids_are_invalid():
    g = DependencyGraph("g", "scope", "regime", (node("a"), node("a")), (
        edge("e", "a", RelationType.SUPPORTING, "a"),
        edge("e", "a", RelationType.ALTERNATIVE, "a"),
    ))
    audit = audit_graph(g)
    assert audit.status is GraphStatus.INVALID
    assert "DUPLICATE_NODE_ID" in audit.errors
    assert "DUPLICATE_EDGE_ID" in audit.errors


def test_load_bearing_cycle_is_unknown_gap_not_silently_solved():
    g = graph(["a", "b"], [
        edge("e1", "a", RelationType.NECESSARY, "b"),
        edge("e2", "b", RelationType.NECESSARY, "a"),
    ])
    audit = audit_graph(g)
    assert audit.status is GraphStatus.UNKNOWN_GAP
    assert set(audit.topology.cycle_nodes) == {"a", "b"}
    result = propagate_invalidation(g, ["a"])
    assert result.blocked and result.reason == "LOAD_BEARING_CYCLE"


def test_necessary_dependency_loss_stales_only_transitive_descendants():
    g = graph(["root", "mid", "leaf", "other"], [
        edge("e1", "mid", RelationType.NECESSARY, "root"),
        edge("e2", "leaf", RelationType.CONDITIONED_ON, "mid"),
    ])
    result = propagate_invalidation(g, ["root"])
    assert not result.blocked
    assert result.stale_ids == ("leaf", "mid")
    assert result.preserved_ids == ("other",)


def test_derived_from_is_load_bearing_for_selective_invalidation():
    g = graph(["source", "derived"], [edge("e", "derived", RelationType.DERIVED_FROM, "source")])
    assert propagate_invalidation(g, ["source"]).stale_ids == ("derived",)


def test_support_loss_requests_review_but_does_not_stale_target():
    g = graph(["support", "claim"], [edge("e", "support", RelationType.SUPPORTING, "claim")])
    result = propagate_invalidation(g, ["support"])
    assert result.stale_ids == ()
    assert result.review_ids == ("claim",)


def test_sufficient_source_loss_requests_review_not_falsity():
    g = graph(["witness", "claim"], [edge("e", "witness", RelationType.SUFFICIENT, "claim")])
    result = propagate_invalidation(g, ["witness"])
    assert result.review_ids == ("claim",)
    assert result.stale_ids == ()


def test_alternative_and_correlation_loss_do_not_propagate():
    g = graph(["a", "b", "c"], [
        edge("e1", "a", RelationType.ALTERNATIVE, "b"),
        edge("e2", "a", RelationType.CORRELATED_WITH, "c"),
    ])
    result = propagate_invalidation(g, ["a"])
    assert result.stale_ids == ()
    assert result.review_ids == ()
    assert result.preserved_ids == ("b", "c")


def test_invalidates_relation_is_proposal_not_automatic_effect():
    g = graph(["rule", "claim"], [edge("e", "rule", RelationType.INVALIDATES, "claim")])
    audit = audit_graph(g)
    assert audit.invalidation_proposals == (("rule", "claim"),)
    result = propagate_invalidation(g, ["rule"])
    assert result.stale_ids == ()
    assert result.preserved_ids == ("claim",)


def test_supersession_is_separate_state_proposal():
    g = graph(["new", "old"], [edge("e", "new", RelationType.SUPERSEDES, "old")])
    assert apply_supersession_proposal(g, "new") == ("old",)
    assert build_load_bearing_topology(g).closure == ((0, 0), (0, 0))


def test_contradiction_tracks_competing_relation_without_truth_promotion():
    g = graph(["h1", "h2"], [edge("e", "h1", RelationType.CONTRADICTING, "h2")])
    assert contradiction_partners(g, "h1") == ("h2",)
    assert contradiction_partners(g, "h2") == ("h1",)
    assert propagate_invalidation(g, ["h1"]).stale_ids == ()


def test_dependency_map_exports_only_direct_load_bearing_edges():
    g = graph(["a", "b", "c"], [
        edge("e1", "b", RelationType.NECESSARY, "a"),
        edge("e2", "c", RelationType.SUPPORTING, "a"),
        edge("e3", "c", RelationType.CONDITIONED_ON, "b"),
    ])
    assert dependency_map(g) == {"a": (), "b": ("a",), "c": ("b",)}


def test_inactive_edge_is_not_operational_dependency():
    g = graph(["a", "b"], [edge("e", "b", RelationType.NECESSARY, "a", active=False)])
    assert build_load_bearing_topology(g).closure == ((0, 0), (0, 0))
    assert dependency_map(g) == {"a": (), "b": ()}


def test_unknown_invalidation_seed_fails_closed():
    g = graph(["a"], [])
    result = propagate_invalidation(g, ["missing"])
    assert result.blocked
    assert result.reason == "UNKNOWN_INVALIDATION_SEED:missing"


def test_random_dag_closure_matches_independent_dfs():
    rng = random.Random(20260914)
    for _ in range(1000):
        n = rng.randint(2, 9)
        ids = [f"n{i}" for i in range(n)]
        edges = []
        direct = {x: set() for x in ids}
        eid = 0
        for i in range(n):
            for j in range(i):
                if rng.random() < 0.25:
                    eid += 1
                    rel = rng.choice([RelationType.NECESSARY, RelationType.DERIVED_FROM, RelationType.CONDITIONED_ON])
                    edges.append(edge(f"e{eid}", ids[i], rel, ids[j]))
                    direct[ids[i]].add(ids[j])
        g = graph(ids, edges)
        topology = build_load_bearing_topology(g)
        for src in ids:
            seen = set()
            stack = list(direct[src])
            while stack:
                cur = stack.pop()
                if cur in seen:
                    continue
                seen.add(cur)
                stack.extend(direct[cur])
            assert set(topology.dependencies_of(src)) == seen


def test_selective_invalidation_random_dag_equals_reverse_reachability():
    rng = random.Random(9142026)
    for _ in range(500):
        n = rng.randint(2, 8)
        ids = [f"n{i}" for i in range(n)]
        edges = []
        reverse = {x: set() for x in ids}
        eid = 0
        for i in range(n):
            for j in range(i):
                if rng.random() < 0.3:
                    eid += 1
                    edges.append(edge(f"e{eid}", ids[i], RelationType.NECESSARY, ids[j]))
                    reverse[ids[j]].add(ids[i])
        g = graph(ids, edges)
        seed = rng.choice(ids)
        expected = set()
        stack = list(reverse[seed])
        while stack:
            cur = stack.pop()
            if cur in expected:
                continue
            expected.add(cur)
            stack.extend(reverse[cur])
        result = propagate_invalidation(g, [seed])
        assert not result.blocked
        assert set(result.stale_ids) == expected
