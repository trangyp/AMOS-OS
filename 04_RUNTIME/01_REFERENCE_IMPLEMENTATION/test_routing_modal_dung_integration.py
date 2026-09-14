import unittest
import cognitive_matrix_routing_runtime as rt
import modal_kripke_runtime as mk
import dung_argumentation_runtime as da


class RoutingModalDungIntegrationTests(unittest.TestCase):
    def test_modal_subfragment_routes(self):
        req=rt.RouteRequest("m1",rt.QueryKind.MODAL_K_FINITE_MODEL_CHECK,"reference","active",("ULK_ALU04_MODAL_K_FINITE_KRIPKE",))
        dec=rt.route(req,rt.reference_candidates())
        self.assertEqual(dec.status,rt.RouteStatus.ROUTED)
        self.assertEqual(dec.target_id,"alu04-modal-k-finite-model-runtime")

    def test_generic_epistemic_modal_does_not_silently_use_K_subfragment(self):
        req=rt.RouteRequest("m2",rt.QueryKind.EPISTEMIC_MODAL,"reference","active")
        self.assertEqual(rt.route(req,rt.reference_candidates()).status,rt.RouteStatus.DENY)

    def test_modal_route_then_eval(self):
        payload={"model":{"worlds":["w0","w1"],"relations":{"a":[["w0","w1"]]},"valuations":{"w0":[],"w1":["p"]}},"formula":{"diamond":{"agent":"a","formula":{"atom":"p"}}},"world":"w0"}
        req=rt.RouteRequest("m3",rt.QueryKind.MODAL_K_FINITE_MODEL_CHECK,"reference","active",("ULK_ALU04_MODAL_K_FINITE_KRIPKE",),payload=payload)
        self.assertEqual(rt.route(req,rt.reference_candidates()).status,rt.RouteStatus.ROUTED)
        self.assertEqual(mk.run_request(payload).status,mk.ModalStatus.SATISFIED)

    def test_dung_subfragment_routes(self):
        req=rt.RouteRequest("d1",rt.QueryKind.DUNG_ABSTRACT_FRAMEWORK_CHECK,"reference","active",("ULK_ALU05_DUNG_ARGUMENTATION",))
        dec=rt.route(req,rt.reference_candidates())
        self.assertEqual(dec.status,rt.RouteStatus.ROUTED)
        self.assertEqual(dec.target_id,"alu05-dung-abstract-argumentation-runtime")

    def test_generic_nonmonotonic_does_not_silently_use_dung_subfragment(self):
        req=rt.RouteRequest("d2",rt.QueryKind.NON_MONOTONIC,"reference","active")
        self.assertEqual(rt.route(req,rt.reference_candidates()).status,rt.RouteStatus.DENY)

    def test_dung_route_then_grounded(self):
        payload={"arguments":["a","b","c"],"attacks":[["b","a"],["c","b"]]}
        req=rt.RouteRequest("d3",rt.QueryKind.DUNG_ABSTRACT_FRAMEWORK_CHECK,"reference","active",("ULK_ALU05_DUNG_ARGUMENTATION",),payload=payload)
        self.assertEqual(rt.route(req,rt.reference_candidates()).status,rt.RouteStatus.ROUTED)
        self.assertEqual(da.run_request(payload).grounded_extension,("a","c"))

    def test_effectful_logic_route_never_commits(self):
        req=rt.RouteRequest("d4",rt.QueryKind.DUNG_ABSTRACT_FRAMEWORK_CHECK,"reference","active",("ULK_ALU05_DUNG_ARGUMENTATION",),effectful=True,authority_bound=True)
        dec=rt.route(req,rt.reference_candidates())
        self.assertEqual(dec.status,rt.RouteStatus.PROPOSAL_ONLY)
        self.assertFalse(dec.commit_authorized)

if __name__=="__main__": unittest.main()
