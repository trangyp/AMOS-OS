import itertools
import random
import unittest

import core19_runtime as c


class Core19RuntimeTests(unittest.TestCase):
    def test_core19_registry_has_exactly_19_semantic_positions(self):
        self.assertEqual(len(c.Core19), 19)
        self.assertEqual(c.matrix_coordinate_count(), 361)

    def test_p02_is_unresolved_without_explicit_namespace_version_binding(self):
        reg = c.P02BindingRegistry()
        binding = reg.resolve("historical-core19", "v1")
        self.assertFalse(binding.resolved)
        self.assertIsNone(binding.candidate)

    def test_p02_conflicting_rebind_fails_closed(self):
        reg = c.P02BindingRegistry()
        reg.bind("historical-core19", "v1", c.P02Candidate.NON_EXISTENCE)
        with self.assertRaises(ValueError):
            reg.bind("historical-core19", "v1", c.P02Candidate.DISTINCTION)

    def test_truth4_negation_is_involutive_for_full_domain(self):
        for value in c.TRUTH4_DOMAIN:
            self.assertEqual(value.neg().neg(), value)

    def test_truth4_information_join_is_commutative_associative_idempotent(self):
        for a, b, d in itertools.product(c.TRUTH4_DOMAIN, repeat=3):
            self.assertEqual(a.join_information(b), b.join_information(a))
            self.assertEqual(a.join_information(a), a)
            self.assertEqual(
                a.join_information(b).join_information(d),
                a.join_information(b.join_information(d)),
            )

    def test_truth4_information_order_is_explicit_not_python_lexicographic(self):
        self.assertTrue(c.TRUTH4_NEITHER.leq_information(c.TRUTH4_TRUE_ONLY))
        self.assertTrue(c.TRUTH4_NEITHER.leq_information(c.TRUTH4_FALSE_ONLY))
        self.assertTrue(c.TRUTH4_TRUE_ONLY.leq_information(c.TRUTH4_BOTH))
        self.assertTrue(c.TRUTH4_FALSE_ONLY.leq_information(c.TRUTH4_BOTH))
        self.assertFalse(c.TRUTH4_TRUE_ONLY.leq_information(c.TRUTH4_FALSE_ONLY))
        self.assertFalse(c.TRUTH4_FALSE_ONLY.leq_information(c.TRUTH4_TRUE_ONLY))
        with self.assertRaises(TypeError):
            _ = c.TRUTH4_TRUE_ONLY < c.TRUTH4_FALSE_ONLY

    def test_double_nlogic_is_checked_before_child_descent(self):
        x = c.UnaryExpr.atom("x")
        expr = c.UnaryExpr.nlogic(c.UnaryExpr.nlogic(x))
        self.assertEqual(c.normalize_unary(expr), x)

    def test_normalizer_is_idempotent_and_nlogic_involutive_on_random_trees(self):
        rng = random.Random(20260914)
        for i in range(50000):
            expr = c.UnaryExpr.atom(f"a{i % 17}")
            for _ in range(rng.randrange(0, 32)):
                expr = (
                    c.UnaryExpr.not_(expr)
                    if rng.getrandbits(1)
                    else c.UnaryExpr.nlogic(expr)
                )
            normalized = c.normalize_unary(expr)
            self.assertEqual(c.normalize_unary(normalized), normalized)
            self.assertEqual(
                c.normalize_unary(c.UnaryExpr.nlogic(c.UnaryExpr.nlogic(expr))),
                normalized,
            )

    def test_fragment_status_delegates_to_current_registry(self):
        self.assertEqual(
            c.implementation_status(c.LogicFragment.CLASSICAL_PROPOSITIONAL),
            c.ImplementationStatus.EXECUTABLE_BOUNDED,
        )
        for fragment in c.LogicFragment:
            if fragment is c.LogicFragment.CLASSICAL_PROPOSITIONAL:
                continue
            self.assertEqual(
                c.implementation_status(fragment),
                c.ImplementationStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
            )

    def test_tensor_coordinate_requires_explicit_six_axis_binding(self):
        with self.assertRaises(ValueError):
            c.TensorCoordinate(
                c.Core19.P01_EXISTENCE,
                c.Core19.P03_CAUSALITY,
                "H",
                "ctx",
                "r",
                "",
            )
        coord = c.TensorCoordinate(
            c.Core19.P01_EXISTENCE,
            c.Core19.P03_CAUSALITY,
            "H",
            "runtime",
            "active",
            "auditor",
        )
        self.assertEqual(coord.scale, "H")
        self.assertEqual(coord.observer, "auditor")

    def test_promotion_requires_every_gate(self):
        full = dict(
            source_resolved=True,
            semantics_typed=True,
            assumptions_bound=True,
            equations_checked=True,
            counterexamples_checked=True,
            implementation_receipt=True,
            canon_authority=True,
        )
        self.assertTrue(c.PromotionEvidence(**full).promotable())
        for key in full:
            missing = dict(full)
            missing[key] = False
            self.assertFalse(c.PromotionEvidence(**missing).promotable(), key)

    def test_runtime_invariant_bundle(self):
        self.assertEqual(c.validate_runtime_invariants(), ())


if __name__ == "__main__":
    unittest.main()
