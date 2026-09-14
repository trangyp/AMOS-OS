import unittest

import ulk_semantic_fragments_runtime as f


class SemanticFragmentTests(unittest.TestCase):
    def test_ltlf_strong_next_boundary(self):
        p = f.LTLFormula.atom("p")
        trace = (frozenset({"p"}),)
        self.assertFalse(f.evaluate_ltlf(f.LTLFormula.next_(p), trace))
        self.assertTrue(f.evaluate_ltlf(f.LTLFormula.always(p), trace))

    def test_ltlf_eventually_always_until(self):
        p, q = f.LTLFormula.atom("p"), f.LTLFormula.atom("q")
        trace = (frozenset({"p"}), frozenset({"p"}), frozenset({"q"}))
        self.assertTrue(f.evaluate_ltlf(f.LTLFormula.eventually(q), trace))
        self.assertFalse(f.evaluate_ltlf(f.LTLFormula.always(p), trace))
        self.assertTrue(f.evaluate_ltlf(f.LTLFormula.until(p, q), trace))
        r = f.LTLFormula.atom("r")
        self.assertFalse(f.evaluate_ltlf(f.LTLFormula.until(q, r), trace, position=1))

    def test_ltlf_until_when_rhs_holds_now(self):
        p, q = f.LTLFormula.atom("p"), f.LTLFormula.atom("q")
        self.assertTrue(f.evaluate_ltlf(f.LTLFormula.until(p, q), (frozenset({"q"}),)))

    def test_ltlf_rejects_empty_trace_and_bad_position(self):
        p = f.LTLFormula.atom("p")
        with self.assertRaises(f.LogicDomainError):
            f.evaluate_ltlf(p, ())
        with self.assertRaises(f.LogicDomainError):
            f.evaluate_ltlf(p, (frozenset(),), position=1)

    def test_modal_box_diamond_general_kripke_semantics(self):
        model = f.KripkeModel(
            worlds=("w0", "w1"),
            valuation={"w0": ("p",), "w1": ()},
            accessibility={"a": (("w0", "w0"), ("w0", "w1"), ("w1", "w1"))},
        )
        p = f.ModalFormula.atom("p")
        self.assertFalse(f.evaluate_modal(f.ModalFormula.box("a", p), model, "w0"))
        self.assertTrue(f.evaluate_modal(f.ModalFormula.diamond("a", p), model, "w0"))
        self.assertFalse(model.relation_is_s5("a"))

    def test_modal_s5_relation_check(self):
        edges = tuple((u, v) for u in ("w0", "w1") for v in ("w0", "w1"))
        model = f.KripkeModel(
            worlds=("w0", "w1"),
            valuation={"w0": (), "w1": ()},
            accessibility={"a": edges},
        )
        self.assertTrue(model.relation_is_s5("a"))

    def test_modal_empty_successor_box_is_vacuously_true_diamond_false(self):
        model = f.KripkeModel(
            worlds=("w",), valuation={"w": ()}, accessibility={"a": ()}
        )
        p = f.ModalFormula.atom("p")
        self.assertTrue(f.evaluate_modal(f.ModalFormula.box("a", p), model, "w"))
        self.assertFalse(f.evaluate_modal(f.ModalFormula.diamond("a", p), model, "w"))

    def test_modal_unknown_agent_fails_closed(self):
        model = f.KripkeModel(
            worlds=("w",), valuation={"w": ()}, accessibility={"a": (("w", "w"),)}
        )
        with self.assertRaises(f.LogicDomainError):
            f.evaluate_modal(f.ModalFormula.box("b", f.ModalFormula.atom("p")), model, "w")

    def test_dung_grounded_chain(self):
        af = f.ArgumentationFramework(
            arguments=("A", "B", "C"), attacks=(("A", "B"), ("B", "C"))
        )
        self.assertEqual(af.grounded_extension(), frozenset({"A", "C"}))
        self.assertTrue(af.conflict_free(af.grounded_extension()))

    def test_dung_mutual_attack_grounded_is_empty(self):
        af = f.ArgumentationFramework(
            arguments=("A", "B"), attacks=(("A", "B"), ("B", "A"))
        )
        self.assertEqual(af.grounded_extension(), frozenset())

    def test_dung_self_attack_not_grounded(self):
        af = f.ArgumentationFramework(arguments=("A",), attacks=(("A", "A"),))
        self.assertEqual(af.grounded_extension(), frozenset())

    def test_dung_invalid_edges_and_unknown_sets_fail_closed(self):
        with self.assertRaises(f.LogicDomainError):
            f.ArgumentationFramework(arguments=("A",), attacks=(("A", "B"),))
        af = f.ArgumentationFramework(arguments=("A",), attacks=())
        with self.assertRaises(f.LogicDomainError):
            af.conflict_free(frozenset({"B"}))

    def test_provenance_is_explicit(self):
        self.assertEqual(
            set(f.ALGORITHM_PROVENANCE),
            {"ltlf_finite_trace_semantics", "dung_grounded_argumentation", "kripke_modal_semantics"},
        )

    def test_invariant_bundle(self):
        self.assertEqual(f.validate_semantic_fragment_invariants(), ())


if __name__ == "__main__":
    unittest.main()
