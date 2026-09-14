from cognitive_matrix_coverage_runtime import (
    ArtifactKind,
    CompletionStatus,
    CoverageRecord,
    CoverageScope,
    CoverageStage,
    Criticality,
    GapReason,
    ScopeRequirement,
    evaluate_coverage,
)
from cognitive_matrix_dependency_runtime import (
    DependencyGraph,
    GraphNode,
    NodeState,
    RelationEdge,
    RelationType,
    dependency_map,
)


def n(node_id):
    return GraphNode(node_id, NodeState.ACTIVE, "scope", "regime", "v1", f"repo:{node_id}")


def e(edge_id, src, relation, dst):
    return RelationEdge(edge_id, src, dst, relation, f"repo:{edge_id}", "v1")


def graph():
    return DependencyGraph(
        "g", "scope", "regime",
        tuple(n(x) for x in ("a", "b", "c")),
        (
            e("e1", "b", RelationType.NECESSARY, "a"),
            e("e2", "c", RelationType.DERIVED_FROM, "b"),
        ),
    )


def requirements_from_graph(g):
    deps = dependency_map(g)
    return tuple(
        ScopeRequirement(node.node_id, ArtifactKind.RUNTIME, CoverageStage.CONTRACT_ONLY,
                         Criticality.DECISION_RELEVANT, deps[node.node_id])
        for node in g.nodes
    )


def record(node_id):
    return CoverageRecord(node_id, CoverageStage.CONTRACT_ONLY, f"repo:{node_id}", "v1")


def test_dependency_map_drives_coverage_dependency_closure():
    g = graph()
    scope = CoverageScope("s", "regime", "v1", requirements_from_graph(g))
    result = evaluate_coverage(scope, tuple(record(x) for x in ("a", "b", "c")))
    assert result.status is CompletionStatus.COMPLETE_FOR_SCOPE


def test_missing_upstream_dependency_propagates_through_coverage():
    g = graph()
    scope = CoverageScope("s", "regime", "v1", requirements_from_graph(g))
    result = evaluate_coverage(scope, (record("b"), record("c")))
    gaps = {(gap.requirement_id, gap.reason) for gap in result.gaps}
    assert result.status is CompletionStatus.INCOMPLETE
    assert ("a", GapReason.MISSING) in gaps
    assert ("b", GapReason.DEPENDENCY_GAP) in gaps
    assert ("c", GapReason.DEPENDENCY_GAP) in gaps


def test_support_relation_is_not_silently_promoted_to_required_coverage_dependency():
    g = DependencyGraph(
        "g", "scope", "regime",
        (n("support"), n("claim")),
        (e("e", "support", RelationType.SUPPORTING, "claim"),),
    )
    deps = dependency_map(g)
    assert deps == {"claim": (), "support": ()}
