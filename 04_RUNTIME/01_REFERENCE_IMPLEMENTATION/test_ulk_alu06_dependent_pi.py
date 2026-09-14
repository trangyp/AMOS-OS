import hashlib
import pathlib
import unittest

import amos_ulk_alu06_dependent_pi_checker_v1 as d
from ulk_fragment_execution_registry import (
    ExecutionStatus,
    Fragment,
    execution_binding,
)


class DependentPiTests(unittest.TestCase):
    def test_universes(self):
        self.assertEqual(d.infer_type(d.Universe(0)), d.Universe(1))

    def test_dependent_identity_type(self):
        u = d.Universe(0)
        expr = d.Lam("A", u, d.Lam("x", d.Var("A"), d.Var("x")))
        expected = d.Pi("B", u, d.Pi("y", d.Var("B"), d.Var("B")))
        self.assertTrue(d.alpha_equal(d.infer_type(expr), expected))

    def test_application_substitutes_dependent_codomain(self):
        u = d.Universe(0)
        ident = d.Lam("A", u, d.Lam("x", d.Var("A"), d.Var("x")))
        ctx = {"A": u, "a": d.Var("A")}
        app = d.App(d.App(ident, d.Var("A")), d.Var("a"))
        self.assertTrue(d.definitional_equal(d.infer_type(app, ctx), d.Var("A")))

    def test_capture_avoiding_substitution(self):
        u = d.Universe(0)
        out = d.substitute(d.Lam("y", u, d.Var("x")), "x", d.Var("y"))
        self.assertNotEqual(out.var, "y")
        self.assertEqual(d.free_vars(out), frozenset({"y"}))

    def test_bound_rename_respects_nested_shadowing(self):
        u = d.Universe(0)
        body = d.Lam("x", u, d.Var("x"))
        self.assertEqual(d.rename_bound(body, "x", "z"), body)

    def test_beta_normalization(self):
        u = d.Universe(0)
        expr = d.App(d.Lam("x", u, d.Var("x")), d.Var("z"))
        self.assertEqual(d.normalize(expr), d.Var("z"))

    def test_alpha_equivalence(self):
        self.assertTrue(
            d.alpha_equal(
                d.Lam("x", d.Universe(0), d.Var("x")),
                d.Lam("y", d.Universe(0), d.Var("y")),
            )
        )

    def test_malformed_application_fails_closed(self):
        with self.assertRaises(d.TypeInvariantError):
            d.infer_type(d.App(d.Universe(0), d.Universe(0)))
        with self.assertRaises(d.TypeInvariantError):
            d.App("bad", d.Universe(0))

    def test_unbound_variable_fails_closed(self):
        with self.assertRaises(d.TypeInvariantError):
            d.infer_type(d.Var("x"))

    def test_context_validation(self):
        d.validate_context({"A": d.Universe(0), "a": d.Var("A")})
        with self.assertRaises(d.TypeInvariantError):
            d.validate_context({"x": d.Var("missing")})

    def test_normalization_budget_is_explicit(self):
        with self.assertRaises(d.TypeInvariantError):
            d.normalize(d.Universe(0), 0)

    def test_invariant_bundle(self):
        self.assertEqual(d.validate_alu06_invariants(), ())

    def test_registry_binding_and_exact_checker_hash(self):
        binding = execution_binding(Fragment.ALU06_DEPENDENT_TYPE)
        self.assertEqual(
            binding.status,
            ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        )
        self.assertFalse(binding.canon_promoted)
        self.assertEqual(
            hashlib.sha256(pathlib.Path(d.__file__).read_bytes()).hexdigest(),
            binding.checker_sha256,
        )


if __name__ == "__main__":
    unittest.main()
