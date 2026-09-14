import random
import unittest

from cognitive_matrix_runtime import (
    ALGORITHM_REGISTRY,
    CellRecord,
    Condition,
    DependencyCycleError,
    DependencyGraph,
    DependencyKind,
    GapKind,
    GapSignal,
    Maturity,
    PromotionEvidence,
    RouteTarget,
    apply_promotion,
    compute_coverage,
    deterministic_shortest_path_nonnegative,
    evaluate_promotion,
    prioritize_gaps,
    route_gap,
    score_gap,
    validate_algorithm_preconditions,
)


class PromotionTests(unittest.TestCase):
    def test_cannot_skip_maturity_stage(self):
        record = CellRecord("x")
        decision = evaluate_promotion(record, Maturity.IMPLEMENTED, PromotionEvidence(implementation_receipt=True))
        self.assertFalse(decision.allowed)

    def test_confidence_does_not_mint_source_or_authority(self):
        record = CellRecord("x", confidence=1.0)
        source = evaluate_promotion(record, Maturity.SOURCE_BOUND, PromotionEvidence())
        self.assertFalse(source.allowed)
        self.assertEqual(set(source.missing), {"source_resolved", "provenance_traceable"})

    def test_staged_promotion_requires_stage_evidence(self):
        record = CellRecord("x")
        record = apply_promotion(record, Maturity.SOURCE_BOUND, PromotionEvidence(source_resolved=True, provenance_traceable=True))
        record = apply_promotion(record, Maturity.CONTRACT_COMPLETE, PromotionEvidence(semantics_typed=True, assumptions_bound=True, contract_complete=True))
        record = apply_promotion(record, Maturity.IMPLEMENTED, PromotionEvidence(implementation_receipt=True))
        record = apply_promotion(record, Maturity.VALIDATED_BOUNDED, PromotionEvidence(tests_executed=True, adversarial_tests_executed=True))
        blocked = evaluate_promotion(record, Maturity.AUTHORIZED_BOUNDED, PromotionEvidence(authority_witness=True))
        self.assertFalse(blocked.allowed)
        self.assertEqual(blocked.missing, ("freshness_bound",))
        record = apply_promotion(record, Maturity.AUTHORIZED_BOUNDED, PromotionEvidence(authority_witness=True, freshness_bound=True))
        self.assertEqual(record.maturity, Maturity.AUTHORIZED_BOUNDED)

    def test_nonactive_condition_blocks_promotion(self):
        record = CellRecord("x", condition=Condition.COMPETING)
        decision = evaluate_promotion(record, Maturity.SOURCE_BOUND, PromotionEvidence(source_resolved=True, provenance_traceable=True))
        self.assertFalse(decision.allowed)


class DependencyTests(unittest.TestCase):
    def make_graph(self):
        graph = DependencyGraph(["source", "contract", "impl", "unrelated"])
        graph.add_edge("source", "contract", DependencyKind.EVIDENCE)
        graph.add_edge("contract", "impl", DependencyKind.HARD)
        return graph

    def test_topological_order_dependency_precedes_dependent(self):
        graph = self.make_graph()
        order = graph.topological_order()
        self.assertLess(order.index("source"), order.index("contract"))
        self.assertLess(order.index("contract"), order.index("impl"))

    def test_tarjan_detects_cycle_and_topological_sort_fails_closed(self):
        graph = DependencyGraph(["a", "b", "c"])
        graph.add_edge("a", "b")
        graph.add_edge("b", "c")
        graph.add_edge("c", "a")
        self.assertEqual(graph.load_bearing_cycles(), (("a", "b", "c"),))
        with self.assertRaises(DependencyCycleError):
            graph.topological_order()

    def test_soft_cycle_does_not_block_load_bearing_order(self):
        graph = DependencyGraph(["a", "b"])
        graph.add_edge("a", "b", DependencyKind.SOFT)
        graph.add_edge("b", "a", DependencyKind.SOFT)
        self.assertEqual(graph.load_bearing_cycles(), ())
        self.assertEqual(set(graph.topological_order()), {"a", "b"})

    def test_selective_invalidation_marks_descendants_stale_not_false(self):
        graph = self.make_graph()
        records = {node: CellRecord(node, maturity=Maturity.IMPLEMENTED) for node in graph.nodes}
        updated = graph.selective_invalidate(records, "source")
        self.assertEqual(updated["source"].condition, Condition.QUARANTINED)
        self.assertEqual(updated["contract"].condition, Condition.STALE)
        self.assertEqual(updated["impl"].condition, Condition.STALE)
        self.assertEqual(updated["unrelated"].condition, Condition.ACTIVE)
        self.assertNotEqual(updated["impl"].condition, Condition.FALSIFIED)

    def test_random_dags_preserve_edge_order(self):
        rng = random.Random(9142026)
        for n in range(2, 40):
            graph = DependencyGraph(str(i) for i in range(n))
            for i in range(n):
                for j in range(i + 1, n):
                    if rng.random() < 0.08:
                        graph.add_edge(str(i), str(j))
            order = graph.topological_order()
            pos = {node: idx for idx, node in enumerate(order)}
            for edge in graph.edges():
                if edge.kind.propagates_staleness:
                    self.assertLess(pos[edge.dependency], pos[edge.dependent])


class CoverageAndGapTests(unittest.TestCase):
    def test_coverage_is_multidimensional_not_fake_100_percent(self):
        records = [
            CellRecord("a", Maturity.CONTRACT_COMPLETE),
            CellRecord("b", Maturity.IMPLEMENTED),
            CellRecord("c", Maturity.VALIDATED_BOUNDED),
            CellRecord("d", Maturity.AUTHORIZED_BOUNDED),
        ]
        coverage = compute_coverage(records)
        self.assertEqual(coverage.address, 1.0)
        self.assertEqual(coverage.source, 1.0)
        self.assertEqual(coverage.contract, 1.0)
        self.assertEqual(coverage.implementation, 0.75)
        self.assertEqual(coverage.validation, 0.5)
        self.assertEqual(coverage.authority, 0.25)
        self.assertFalse(coverage.complete)

    def test_gap_score_is_bounded_and_safety_override_is_critical(self):
        gap = GapSignal("g", GapKind.VALIDATION, 0.95, 1, 1, 1, 1, 1, 1)
        priority = score_gap(gap)
        self.assertEqual(priority.tier, 0)
        self.assertGreaterEqual(priority.urgency, 0.0)
        self.assertLessEqual(priority.urgency, 1.0)
        self.assertGreaterEqual(priority.efficiency, 0.0)
        self.assertLessEqual(priority.efficiency, 1.0)

    def test_prioritize_gaps_puts_critical_before_noncritical(self):
        critical = GapSignal("critical", GapKind.AUTHORITY, .95, 0, 0, 0, 0, 0, 1)
        normal = GapSignal("normal", GapKind.IMPLEMENTATION, .2, 1, 1, 1, 1, 1, 0)
        ordered = prioritize_gaps([normal, critical])
        self.assertEqual(ordered[0].gap_id, "critical")

    def test_route_never_grants_authority(self):
        gap = GapSignal("auth", GapKind.AUTHORITY, 1, 1, 1, 1, 1, 1, 1)
        decision = route_gap(gap)
        self.assertEqual(decision.target, RouteTarget.AUTHORITY_CONTROL_PLANE)
        self.assertFalse(decision.grants_authority)


class AlgorithmContractTests(unittest.TestCase):
    def test_registry_has_explicit_preconditions(self):
        self.assertTrue(ALGORITHM_REGISTRY["dijkstra"].preconditions)
        ok, missing = validate_algorithm_preconditions("dijkstra", ["weighted_graph"])
        self.assertFalse(ok)
        self.assertEqual(missing, ("nonnegative_edge_weights",))

    def test_dijkstra_reference_path(self):
        graph = {
            "a": {"b": 4.0, "c": 1.0},
            "b": {"d": 1.0},
            "c": {"b": 1.0, "d": 5.0},
            "d": {},
        }
        distance, path = deterministic_shortest_path_nonnegative(graph, "a", "d")
        self.assertEqual(distance, 3.0)
        self.assertEqual(path, ("a", "c", "b", "d"))

    def test_dijkstra_rejects_negative_weight(self):
        graph = {"a": {"b": -1.0}, "b": {}}
        with self.assertRaises(ValueError):
            deterministic_shortest_path_nonnegative(graph, "a", "b")


if __name__ == "__main__":
    unittest.main()
