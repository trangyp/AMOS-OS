import unittest

import algorithm_routing_runtime as ar
import internet_algorithm_registry as ir


class AlgorithmRoutingTests(unittest.TestCase):
    def test_exact_local_sat_routes_to_dpll(self):
        request = ar.AlgorithmRequest(
            ir.ProblemFamily.SAT,
            frozenset({"finite_boolean_cnf", "typed_signed_literals"}),
            require_exact=True,
            local_only=True,
        )
        route = ar.route_algorithm(request)
        self.assertEqual(route.status, ar.RouteStatus.ROUTED_LOCAL)
        self.assertEqual(route.algorithm, "dpll_cnf_sat")
        self.assertEqual(
            route.implementation_binding,
            "foundational_algorithm_runtime.py:dpll_sat",
        )
        self.assertFalse(route.grants_authority)

    def test_missing_precondition_is_unknown_gap_not_guess(self):
        request = ar.AlgorithmRequest(
            ir.ProblemFamily.SAT,
            frozenset({"finite_boolean_cnf"}),
            require_exact=True,
            local_only=True,
        )
        route = ar.route_algorithm(request)
        self.assertEqual(route.status, ar.RouteStatus.UNKNOWN_GAP)
        self.assertIsNone(route.algorithm)

    def test_external_capability_can_route_without_claiming_local_execution(self):
        request = ar.AlgorithmRequest(
            ir.ProblemFamily.EQUALITY_REASONING,
            frozenset({"ground_equalities", "uninterpreted_functions", "first_order_equality"}),
            require_exact=True,
        )
        route = ar.route_algorithm(request)
        self.assertEqual(route.status, ar.RouteStatus.ROUTED_EXTERNAL_CAPABILITY)
        self.assertEqual(route.algorithm, "euf_congruence_closure")
        self.assertIsNone(route.implementation_binding)
        self.assertFalse(route.grants_authority)

    def test_local_only_rejects_external_metadata(self):
        request = ar.AlgorithmRequest(
            ir.ProblemFamily.EQUALITY_REASONING,
            frozenset({"ground_equalities", "uninterpreted_functions", "first_order_equality"}),
            require_exact=True,
            local_only=True,
        )
        self.assertEqual(ar.route_algorithm(request).status, ar.RouteStatus.UNKNOWN_GAP)

    def test_finite_trace_never_routes_to_omega_backend(self):
        request = ar.AlgorithmRequest(
            ir.ProblemFamily.TEMPORAL_MODEL_CHECKING,
            frozenset({"finite_trace_semantics", "finite_trace", "supported_temporal_operators"}),
            require_exact=True,
            local_only=True,
        )
        route = ar.route_algorithm(request)
        self.assertEqual(route.algorithm, "finite_trace_ltl_direct_eval")
        self.assertNotEqual(route.algorithm, "omega_ltl_model_checking")

    def test_infinite_trace_request_does_not_use_finite_checker(self):
        request = ar.AlgorithmRequest(
            ir.ProblemFamily.TEMPORAL_MODEL_CHECKING,
            frozenset({"infinite_trace_semantics", "ltl_formula", "transition_system", "omega_automata_backend"}),
        )
        route = ar.route_algorithm(request)
        self.assertEqual(route.status, ar.RouteStatus.ROUTED_EXTERNAL_CAPABILITY)
        self.assertEqual(route.algorithm, "omega_ltl_model_checking")
        self.assertIsNone(route.implementation_binding)

    def test_named_external_algorithm_requires_runtime_binding_when_requested(self):
        pre = frozenset({"typed_terms", "semantics_preserving_rewrites", "resource_bound", "extraction_cost_model"})
        external = ar.route_named_algorithm("equality_saturation", pre)
        self.assertEqual(external.status, ar.RouteStatus.ROUTED_EXTERNAL_CAPABILITY)
        local_required = ar.route_named_algorithm("equality_saturation", pre, require_local=True)
        self.assertEqual(local_required.status, ar.RouteStatus.UNKNOWN_GAP)

    def test_unknown_named_algorithm_is_unknown_gap(self):
        route = ar.route_named_algorithm("invented-super-solver", frozenset())
        self.assertEqual(route.status, ar.RouteStatus.UNKNOWN_GAP)
        self.assertIsNone(route.algorithm)

    def test_route_object_cannot_be_constructed_with_authority(self):
        with self.assertRaises(ValueError):
            ar.AlgorithmRoute(
                ar.RouteStatus.ROUTED_LOCAL,
                "dpll_cnf_sat",
                "foundational_algorithm_runtime.py:dpll_sat",
                True,
                "invalid",
            )


if __name__ == "__main__":
    unittest.main()
