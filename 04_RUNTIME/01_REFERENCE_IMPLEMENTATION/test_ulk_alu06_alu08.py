import unittest

from amos_ulk_alu06_dependent_pi_checker_v1 import (
    App,
    Bound,
    Lam,
    NatLit,
    NatType,
    Pi,
    TypeCheckError,
    Universe,
    check,
    definitionally_equal,
    infer,
    normalize,
    validate_reference_invariants as validate_alu06,
)
from amos_ulk_alu08_finite_category_heyting_checker_v1 import (
    Arrow,
    FiniteCategory,
    FiniteHeytingAlgebra,
    validate_reference_invariants as validate_alu08,
)


class DependentPiTests(unittest.TestCase):
    def test_universe_hierarchy(self):
        self.assertEqual(infer(Universe(0)), Universe(1))

    def test_nat_identity(self):
        nat = NatType()
        identity = Lam(nat, Bound(0))
        self.assertEqual(infer(identity), Pi(nat, nat))
        self.assertTrue(check(identity, Pi(nat, nat)))

    def test_dependent_identity(self):
        term = Lam(Universe(0), Lam(Bound(0), Bound(0)))
        expected = Pi(Universe(0), Pi(Bound(0), Bound(1)))
        self.assertEqual(infer(term), expected)

    def test_beta_definitional_equality(self):
        nat = NatType()
        identity = Lam(nat, Bound(0))
        app = App(identity, NatLit(7))
        self.assertEqual(normalize(app), NatLit(7))
        self.assertTrue(definitionally_equal(app, NatLit(7)))
        self.assertEqual(infer(app), nat)

    def test_dependent_identity_application_preserves_dependency(self):
        dep_id = Lam(Universe(0), Lam(Bound(0), Bound(0)))
        at_nat = App(dep_id, NatType())
        self.assertEqual(infer(at_nat), Pi(NatType(), NatType()))
        self.assertEqual(normalize(at_nat), Lam(NatType(), Bound(0)))
        fully_applied = App(at_nat, NatLit(2))
        self.assertEqual(infer(fully_applied), NatType())
        self.assertEqual(normalize(fully_applied), NatLit(2))

    def test_ill_formed_pi_domain_rejected(self):
        with self.assertRaises(TypeCheckError):
            infer(Pi(NatLit(1), NatType()))

    def test_application_rejects_wrong_type(self):
        nat = NatType()
        identity = Lam(nat, Bound(0))
        with self.assertRaises(TypeCheckError):
            infer(App(identity, Universe(0)))

    def test_unbound_variable_rejected(self):
        with self.assertRaises(TypeCheckError):
            infer(Bound(0))

    def test_reference_invariants(self):
        self.assertEqual(validate_alu06(), ())


class CategoryHeytingTests(unittest.TestCase):
    def test_two_object_category(self):
        cat = FiniteCategory(
            objects=frozenset({"A", "B"}),
            arrows={
                "idA": Arrow("A", "A"),
                "idB": Arrow("B", "B"),
                "f": Arrow("A", "B"),
            },
            identities={"A": "idA", "B": "idB"},
            composition={
                ("idA", "idA"): "idA",
                ("idB", "idB"): "idB",
                ("idA", "f"): "f",
                ("f", "idB"): "f",
            },
        )
        self.assertEqual(cat.validate(), ())

    def test_missing_composition_fails(self):
        cat = FiniteCategory(
            objects=frozenset({"A"}),
            arrows={"idA": Arrow("A", "A")},
            identities={"A": "idA"},
            composition={},
        )
        failures = cat.validate()
        self.assertTrue(any(x.startswith("COMPOSITION_MISSING") for x in failures))

    def test_three_chain_heyting_implication(self):
        elems = frozenset({"0", "a", "1"})
        leq = frozenset({
            ("0", "0"),
            ("0", "a"),
            ("0", "1"),
            ("a", "a"),
            ("a", "1"),
            ("1", "1"),
        })
        alg = FiniteHeytingAlgebra(elems, leq)
        self.assertEqual(alg.validate(), ())
        self.assertEqual(alg.implication("a", "0"), "0")
        self.assertEqual(alg.implication("a", "a"), "1")
        self.assertEqual(alg.implication("1", "a"), "a")

    def test_associativity_failure_detected(self):
        cat = FiniteCategory(
            objects=frozenset({"A"}),
            arrows={
                "e": Arrow("A", "A"),
                "x": Arrow("A", "A"),
                "y": Arrow("A", "A"),
            },
            identities={"A": "e"},
            composition={
                ("e", "e"): "e",
                ("e", "x"): "x",
                ("e", "y"): "y",
                ("x", "e"): "x",
                ("y", "e"): "y",
                ("x", "x"): "y",
                ("x", "y"): "e",
                ("y", "x"): "y",
                ("y", "y"): "x",
            },
        )
        self.assertTrue(any(x.startswith("ASSOCIATIVITY_FAIL") for x in cat.validate()))

    def test_non_poset_rejected(self):
        alg = FiniteHeytingAlgebra(
            frozenset({"x", "y"}),
            frozenset({("x", "x"), ("y", "y"), ("x", "y"), ("y", "x")}),
        )
        self.assertTrue(any(x.startswith("ANTISYMMETRY_FAIL") for x in alg.validate()))

    def test_reference_invariants(self):
        self.assertEqual(validate_alu08(), ())


if __name__ == "__main__":
    unittest.main()
