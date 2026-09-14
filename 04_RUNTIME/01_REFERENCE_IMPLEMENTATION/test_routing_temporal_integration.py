import unittest

import cognitive_matrix_routing_runtime as rt
import finite_trace_temporal_runtime as ft


class RoutingTemporalIntegrationTests(unittest.TestCase):
    def temporal_request(self, payload=None, *, effectful=False, authority=False):
        return rt.RouteRequest(
            "t1",
            rt.QueryKind.TEMPORAL_FINITE_TRACE_CHECK,
            "reference",
            "active",
            ("ULK_ALU03_LTLF_FINITE_TRACE",),
            effectful=effectful,
            authority_bound=authority,
            payload=payload,
        )

    def test_route_then_evaluate_finite_trace(self):
        payload={"formula":{"globally":{"atom":"p"}},"trace":[["p"],["p"]]}
        decision=rt.route(self.temporal_request(payload),rt.reference_candidates())
        self.assertEqual(decision.status,rt.RouteStatus.ROUTED)
        self.assertEqual(decision.target_id,"alu03-ltlf-finite-trace-runtime")
        result=ft.run_trace_request(payload)
        self.assertEqual(result.status,ft.TemporalStatus.SATISFIED)

    def test_bounded_counterexample_is_not_unbounded_ltl_proof(self):
        ts=ft.TransitionSystem(
            ("s0","bad"),("s0",),
            {"s0":frozenset({"p"}),"bad":frozenset()},
            {"s0":("bad",),"bad":()},
        )
        formula=ft.parse_formula({"globally":{"atom":"p"}},bounds=ft.TemporalBounds())
        result=ft.check_all_paths_bounded(ts,formula,max_steps=1)
        self.assertEqual(result.status,ft.TemporalStatus.COUNTEREXAMPLE_WITHIN_BOUND)
        self.assertFalse(result.unbounded_proof)
        self.assertFalse(result.causal_claim)

    def test_standard_temporal_model_check_is_not_upgraded(self):
        request=rt.RouteRequest("t2",rt.QueryKind.TEMPORAL_MODEL_CHECK,"reference","active")
        decision=rt.route(request,rt.reference_candidates())
        self.assertEqual(decision.status,rt.RouteStatus.DENY)

    def test_effectful_temporal_route_still_only_proposal(self):
        decision=rt.route(self.temporal_request(effectful=True,authority=True),rt.reference_candidates())
        self.assertEqual(decision.status,rt.RouteStatus.PROPOSAL_ONLY)
        self.assertFalse(decision.commit_authorized)

    def test_temporal_ordering_does_not_create_causal_claim(self):
        result=ft.run_trace_request({"formula":{"eventually":{"atom":"q"}},"trace":[[],["q"]]})
        self.assertEqual(result.status,ft.TemporalStatus.SATISFIED)
        self.assertFalse(result.causal_claim)


if __name__=="__main__": unittest.main()
