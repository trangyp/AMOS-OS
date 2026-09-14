import hashlib
import pathlib
import unittest

import amos_ulk_alu08_finite_category_checker_v1 as alu08
from amos_ulk_alu08_finite_category_checker_v1 import (
    CategoryInvariantError,
    FiniteCategory,
    Morphism,
    validate_category_invariants,
)
from ulk_fragment_execution_registry import (
    ALU08_CHECKER_SHA256,
    ExecutionStatus,
    Fragment,
    execution_binding,
)


class FiniteCategoryTests(unittest.TestCase):
    def chain_category(self):
        morphisms = {
            "id0": Morphism("id0", "0", "0"),
            "id1": Morphism("id1", "1", "1"),
            "id2": Morphism("id2", "2", "2"),
            "f01": Morphism("f01", "0", "1"),
            "f12": Morphism("f12", "1", "2"),
            "f02": Morphism("f02", "0", "2"),
        }
        comp = {}
        ids = {"0": "id0", "1": "id1", "2": "id2"}
        for f_name, f in morphisms.items():
            for g_name, g in morphisms.items():
                if f.target != g.source:
                    continue
                if g_name == ids[f.target]:
                    comp[(g_name, f_name)] = f_name
                elif f_name == ids[f.source]:
                    comp[(g_name, f_name)] = g_name
                elif (g_name, f_name) == ("f12", "f01"):
                    comp[(g_name, f_name)] = "f02"
                else:
                    raise AssertionError((g_name, f_name))
        return FiniteCategory(frozenset({"0", "1", "2"}), morphisms, ids, comp)

    def test_exact_checker_hash_and_registry_binding(self):
        self.assertEqual(
            hashlib.sha256(pathlib.Path(alu08.__file__).read_bytes()).hexdigest(),
            ALU08_CHECKER_SHA256,
        )
        binding = execution_binding(Fragment.ALU08_CATEGORICAL_TOPOS)
        self.assertEqual(
            binding.status,
            ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        )
        self.assertFalse(binding.canon_promoted)
        self.assertIn("no topos-structure completion claim", binding.scope)

    def test_chain_is_thin_category_and_preorder_projection(self):
        category = self.chain_category()
        self.assertTrue(category.is_thin())
        self.assertEqual(category.compose("f12", "f01"), "f02")
        self.assertEqual(
            category.thin_preorder_matrix(("0", "1", "2")),
            (
                (True, True, True),
                (False, True, True),
                (False, False, True),
            ),
        )

    def test_empty_category_is_valid(self):
        category = FiniteCategory(frozenset(), {}, {}, {})
        self.assertTrue(category.is_thin())
        self.assertEqual(category.thin_preorder_matrix(()), ())

    def test_non_string_identities_fail_closed(self):
        with self.assertRaises(CategoryInvariantError):
            Morphism("f", "x", 1)
        with self.assertRaises(CategoryInvariantError):
            FiniteCategory(frozenset({"x", 1}), {}, {}, {})

    def test_missing_composable_pair_fails_closed(self):
        morphisms = {"id": Morphism("id", "x", "x")}
        with self.assertRaises(CategoryInvariantError):
            FiniteCategory(frozenset({"x"}), morphisms, {"x": "id"}, {})

    def test_noncomposable_or_wrong_typed_composition_fails_closed(self):
        morphisms = {
            "id0": Morphism("id0", "0", "0"),
            "id1": Morphism("id1", "1", "1"),
            "f": Morphism("f", "0", "1"),
        }
        ids = {"0": "id0", "1": "id1"}
        comp = {
            ("id0", "id0"): "id0",
            ("id1", "id1"): "id1",
            ("f", "id0"): "f",
            ("id1", "f"): "id1",
        }
        with self.assertRaises(CategoryInvariantError):
            FiniteCategory(frozenset({"0", "1"}), morphisms, ids, comp)

    def test_nonassociative_one_object_structure_fails_closed(self):
        morphisms = {
            "e": Morphism("e", "x", "x"),
            "a": Morphism("a", "x", "x"),
            "b": Morphism("b", "x", "x"),
        }
        table = {
            ("e", "e"): "e", ("e", "a"): "a", ("e", "b"): "b",
            ("a", "e"): "a", ("b", "e"): "b",
            ("a", "a"): "e", ("a", "b"): "e",
            ("b", "a"): "e", ("b", "b"): "e",
        }
        with self.assertRaisesRegex(CategoryInvariantError, "associativity"):
            FiniteCategory(frozenset({"x"}), morphisms, {"x": "e"}, table)

    def test_non_thin_category_blocks_preorder_projection(self):
        morphisms = {
            "e": Morphism("e", "x", "x"),
            "a": Morphism("a", "x", "x"),
        }
        table = {
            ("e", "e"): "e",
            ("e", "a"): "a",
            ("a", "e"): "a",
            ("a", "a"): "e",
        }
        category = FiniteCategory(frozenset({"x"}), morphisms, {"x": "e"}, table)
        self.assertFalse(category.is_thin())
        with self.assertRaises(CategoryInvariantError):
            category.thin_preorder_matrix(("x",))

    def test_invariant_bundle(self):
        self.assertEqual(validate_category_invariants(), ())


if __name__ == "__main__":
    unittest.main()
