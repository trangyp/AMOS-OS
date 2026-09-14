import unittest
import cognitive_matrix_routing_runtime as rt
import unification_runtime as u

class RoutingUnificationIntegration(unittest.TestCase):
    def _request(self,payload):
        return rt.RouteRequest(
            "u1", rt.QueryKind.FIRST_ORDER_TERM_UNIFICATION,
            "reference", "active", ("ULK_ALU02_UNIFICATION",),
            payload=payload,
        )

    def test_route_then_unify(self):
        payload={"left":{"fun":"f","args":[{"var":"x"}]},"right":{"fun":"f","args":[{"const":"a"}]}}
        d=rt.route(self._request(payload),rt.reference_candidates())
        self.assertEqual(d.status,rt.RouteStatus.ROUTED)
        self.assertEqual(d.target_id,"alu02-unification-runtime")
        result=u.run_request(payload)
        self.assertEqual(result.status,u.UnificationStatus.UNIFIED)
        self.assertEqual(result.substitution,{"x":{"const":"a"}})

    def test_router_does_not_upgrade_full_fol(self):
        q=rt.RouteRequest("q",rt.QueryKind.FIRST_ORDER_THEOREM_PROVING,"reference","active")
        self.assertEqual(rt.route(q,rt.reference_candidates()).status,rt.RouteStatus.DENY)

    def test_unification_failure_is_not_routing_failure(self):
        payload={"left":{"const":"a"},"right":{"const":"b"}}
        d=rt.route(self._request(payload),rt.reference_candidates())
        self.assertEqual(d.status,rt.RouteStatus.ROUTED)
        self.assertEqual(u.run_request(payload).status,u.UnificationStatus.NOT_UNIFIABLE)

    def test_malformed_payload_is_executor_level_fail_closed(self):
        payload={"left":{"var":"x"}}
        d=rt.route(self._request(payload),rt.reference_candidates())
        self.assertEqual(d.status,rt.RouteStatus.ROUTED)
        self.assertEqual(u.run_request(payload).status,u.UnificationStatus.REJECT_MALFORMED_REQUEST)

    def test_effectful_unification_is_not_committed(self):
        q=rt.RouteRequest("q",rt.QueryKind.FIRST_ORDER_TERM_UNIFICATION,"reference","active",("ULK_ALU02_UNIFICATION",),effectful=True,authority_bound=True)
        d=rt.route(q,rt.reference_candidates())
        self.assertEqual(d.status,rt.RouteStatus.PROPOSAL_ONLY)
        self.assertFalse(d.commit_authorized)

if __name__=="__main__": unittest.main()
