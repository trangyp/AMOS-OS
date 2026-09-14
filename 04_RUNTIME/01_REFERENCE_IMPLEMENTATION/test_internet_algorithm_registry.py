import unittest

import internet_algorithm_registry as r


class InternetAlgorithmRegistryTests(unittest.TestCase):
    def test_registry_entries_are_typed_and_bounded(self):
        self.assertGreaterEqual(len(r.REGISTRY), 25)
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

    def test_bellman_ford_local_binding_has_stricter_finite_contract(self):
        spec = r.algorithm_spec("bellman_ford")
        self.assertEqual(spec.implementation_binding, "foundational_algorithm_runtime.py:bellman_ford")
        self.assertFalse(r.eligible("bellman_ford", frozenset({"weighted"})))
        self.assertTrue(
            r.eligible(
                "bellman_ford",
                frozenset({"finite_graph", "weighted", "finite_weights"}),
            )
        )
        self.assertIn("negative-cycle", spec.boundary)

    def test_graph_structure_algorithms_require_correct_domains(self):
        self.assertFalse(r.eligible("tarjan_scc", frozenset({"graph"})))
        self.assertTrue(r.eligible("tarjan_scc", frozenset({"directed_graph"})))
        self.assertFalse(r.eligible("topological_sort", frozenset({"directed_graph"})))
        self.assertTrue(r.eligible("topological_sort", frozenset({"directed_graph", "acyclic"})))
        self.assertFalse(r.eligible("minimum_spanning_tree", frozenset({"weighted"})))
        self.assertTrue(r.eligible("minimum_spanning_tree", frozenset({"undirected_graph", "weighted"})))

    def test_reflexive_transitive_closure_has_exact_finite_contract(self):
        name = "warshall_reflexive_transitive_closure"
        partial = frozenset({"finite_namespace", "boolean_relation"})
        self.assertEqual(r.missing_preconditions(name, partial), ("reflexive_closure",))
        supplied = frozenset({"finite_namespace", "boolean_relation", "reflexive_closure"})
        self.assertTrue(r.eligible(name, supplied))
        spec = r.algorithm_spec(name)
        self.assertEqual(spec.family, r.ProblemFamily.TRANSITIVE_CLOSURE)
        self.assertEqual(spec.guarantee, r.GuaranteeClass.EXACT)
        self.assertIn("REACHABLE != ENTAILS", spec.boundary)
        self.assertIn("REACHABLE != CAUSES", spec.boundary)
        self.assertEqual(
            spec.implementation_binding,
            "urk_relation_algebra.py:reflexive_transitive_closure",
        )

    def test_flow_and_cut_require_capacity_contract(self):
        partial = frozenset({"graph", "source", "sink"})
        self.assertEqual(r.missing_preconditions("maximum_flow", partial), ("capacities",))
        self.assertEqual(r.missing_preconditions("minimum_cut", partial), ("capacities",))
        exact = r.algorithm_spec("edmonds_karp_integer_max_flow")
        self.assertEqual(exact.guarantee, r.GuaranteeClass.EXACT)
        self.assertEqual(
            exact.implementation_binding,
            "foundational_algorithm_runtime.py:edmonds_karp_max_flow",
        )

    def test_sat_constraint_and_disjoint_set_local_bindings_are_narrow(self):
        sat = r.algorithm_spec("dpll_cnf_sat")
        self.assertEqual(sat.family, r.ProblemFamily.SAT)
        self.assertEqual(sat.guarantee, r.GuaranteeClass.EXACT)
        self.assertIn("does not establish first-order", sat.boundary)
        self.assertEqual(sat.implementation_binding, "foundational_algorithm_runtime.py:dpll_sat")

        ac3 = r.algorithm_spec("ac3_arc_consistency")
        self.assertIn("does not prove existence of a global CSP solution", ac3.boundary)
        self.assertEqual(ac3.implementation_binding, "foundational_algorithm_runtime.py:ac3_arc_consistency")

        uf = r.algorithm_spec("union_find")
        self.assertIn("!= semantic identity", uf.boundary)
        self.assertEqual(uf.implementation_binding, "foundational_algorithm_runtime.py:UnionFind")

    def test_external_equality_algorithms_do_not_claim_local_embedding(self):
        euf = r.algorithm_spec("euf_congruence_closure")
        self.assertEqual(euf.family, r.ProblemFamily.EQUALITY_REASONING)
        self.assertIsNone(euf.implementation_binding)
        self.assertIn("EUF theory", euf.boundary)

        egg = r.algorithm_spec("equality_saturation")
        self.assertEqual(egg.family, r.ProblemFamily.TERM_REWRITING)
        self.assertIsNone(egg.implementation_binding)
        self.assertIn("rewrite rules", egg.boundary)
        self.assertIn("cost model", egg.boundary)

    def test_temporal_router_never_collapses_finite_and_infinite_semantics(self):
        self.assertEqual(
            r.choose_temporal_backend(finite_trace_semantics=True),
            "finite_trace_ltl_direct_eval",
        )
        self.assertEqual(
            r.choose_temporal_backend(finite_trace_semantics=False),
            "omega_ltl_model_checking",
        )
        finite = r.algorithm_spec("finite_trace_ltl_direct_eval")
        omega = r.algorithm_spec("omega_ltl_model_checking")
        self.assertIsNotNone(finite.implementation_binding)
        self.assertIsNone(omega.implementation_binding)
        self.assertIn("!= ordinary infinite-word LTL", finite.boundary)
        self.assertIn("infinite words", omega.boundary)

    def test_cp_sat_preserves_solver_status_and_integer_domain(self):
        spec = r.algorithm_spec("cp_sat")
        self.assertIn("integer models", spec.boundary)
        self.assertIn("UNKNOWN", spec.boundary)
        self.assertEqual(spec.guarantee, r.GuaranteeClass.SOLVER_STATUS_BOUND)

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
