import unittest

import internet_algorithm_registry as r


class InternetAlgorithmRegistryTests(unittest.TestCase):
    def test_registry_entries_are_typed_and_bounded(self):
        self.assertGreaterEqual(len(r.REGISTRY), 15)
        for name, spec in r.REGISTRY.items():
            self.assertEqual(name, spec.name)
            self.assertTrue(spec.source)
            self.assertTrue(spec.boundary)
            self.assertIsInstance(spec.preconditions, frozenset)
            self.assertIsInstance(spec.family, r.ProblemFamily)
            self.assertIsInstance(spec.guarantee, r.GuaranteeClass)
            self.assertIsInstance(spec.determinism, r.DeterminismClass)

    def test_dijkstra_and_astar_preconditions_fail_closed(self):
        self.assertTrue(r.eligible("dijkstra", frozenset({"graph", "nonnegative_weights"})))
        self.assertFalse(r.eligible("dijkstra", frozenset({"graph"})))
        astar_partial = frozenset({"graph", "weighted", "source_target", "heuristic"})
        self.assertFalse(r.eligible("astar", astar_partial))
        self.assertEqual(r.missing_preconditions("astar", astar_partial), ("admissible_heuristic",))
        self.assertTrue(
            r.eligible(
                "astar",
                frozenset({"graph", "weighted", "source_target", "heuristic", "admissible_heuristic"}),
            )
        )

    def test_graph_structure_algorithms_require_correct_domains(self):
        self.assertFalse(r.eligible("tarjan_scc", frozenset({"graph"})))
        self.assertTrue(r.eligible("tarjan_scc", frozenset({"directed_graph"})))
        self.assertFalse(r.eligible("topological_sort", frozenset({"directed_graph"})))
        self.assertTrue(r.eligible("topological_sort", frozenset({"directed_graph", "acyclic"})))
        self.assertFalse(r.eligible("minimum_spanning_tree", frozenset({"weighted"})))
        self.assertTrue(r.eligible("minimum_spanning_tree", frozenset({"undirected_graph", "weighted"})))

    def test_flow_and_cut_require_capacity_contract(self):
        partial = frozenset({"graph", "source", "sink"})
        self.assertEqual(r.missing_preconditions("maximum_flow", partial), ("capacities",))
        self.assertEqual(r.missing_preconditions("minimum_cut", partial), ("capacities",))

    def test_shortest_path_router_never_uses_astar_without_admissibility(self):
        self.assertEqual(
            r.choose_shortest_path(
                weighted=True,
                negative_edges=False,
                all_pairs=False,
                source_target=True,
                heuristic_available=True,
                heuristic_admissible=False,
            ),
            "dijkstra",
        )
        self.assertEqual(
            r.choose_shortest_path(
                weighted=True,
                negative_edges=False,
                all_pairs=False,
                source_target=True,
                heuristic_available=True,
                heuristic_admissible=True,
            ),
            "astar",
        )
        self.assertEqual(
            r.choose_shortest_path(
                weighted=True,
                negative_edges=True,
                all_pairs=False,
                source_target=True,
                heuristic_available=True,
                heuristic_admissible=True,
            ),
            "bellman_ford",
        )

    def test_unknown_algorithm_fails_closed(self):
        with self.assertRaises(KeyError):
            r.algorithm_spec("does-not-exist")


if __name__ == "__main__":
    unittest.main()
