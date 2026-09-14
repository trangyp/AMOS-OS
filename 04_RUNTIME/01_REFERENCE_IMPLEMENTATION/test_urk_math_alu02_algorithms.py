import hashlib
import pathlib
import random
import unittest

import amos_ulk_alu02_unification_reference_checker_v1 as alu02
from internet_algorithm_registry import eligible, missing_preconditions, choose_shortest_path
from ulk_fragment_execution_registry import (
    ALU02_CHECKER_SHA256,
    ExecutionStatus,
    Fragment,
    execution_binding,
    validate_execution_registry,
)
from urk_relation_algebra import (
    FiniteNamespace,
    boolean_compose,
    compose_relations,
    decode_relation,
    encode_relation,
    validate_closure_invariants,
)

V = lambda x: {"var": x}
C = lambda x: {"const": x}
F = lambda f, *xs: {"fun": f, "args": list(xs)}


class URKRelationAlgebraTests(unittest.TestCase):
    def test_encode_decode_roundtrip(self):
        ns = FiniteNamespace(("a", "b", "c"))
        relation = frozenset({("a", "b"), ("b", "c")})
        self.assertEqual(decode_relation(ns, encode_relation(ns, relation)), relation)

    def test_boolean_composition_matches_set_composition(self):
        rng = random.Random(20260914)
        for n in range(1, 9):
            ns = FiniteNamespace(tuple(range(n)))
            pairs = [(i, j) for i in range(n) for j in range(n)]
            for _ in range(80):
                r = frozenset(p for p in pairs if rng.random() < 0.3)
                s = frozenset(p for p in pairs if rng.random() < 0.3)
                via_matrix = decode_relation(
                    ns,
                    boolean_compose(encode_relation(ns, r), encode_relation(ns, s)),
                )
                self.assertEqual(via_matrix, compose_relations(ns, r, s))

    def test_closure_properties_randomized(self):
        rng = random.Random(7)
        for n in range(1, 12):
            ns = FiniteNamespace(tuple(range(n)))
            pairs = [(i, j) for i in range(n) for j in range(n)]
            for _ in range(50):
                relation = frozenset(p for p in pairs if rng.random() < 0.18)
                self.assertEqual(validate_closure_invariants(ns, relation), ())

    def test_boolean_product_is_not_path_count(self):
        a = (
            (False, True, True),
            (False, False, False),
            (False, False, False),
        )
        b = (
            (False, False, False),
            (False, False, True),
            (False, False, True),
        )
        self.assertIs(boolean_compose(a, b)[0][2], True)

    def test_invalid_matrix_fails_closed(self):
        ns = FiniteNamespace(("a", "b"))
        with self.assertRaises(ValueError):
            decode_relation(ns, ((True,),))
        with self.assertRaises(TypeError):
            decode_relation(ns, ((1, 0), (0, 1)))


class ALU02Tests(unittest.TestCase):
    def test_exact_receipt_hash(self):
        self.assertEqual(
            hashlib.sha256(pathlib.Path(alu02.__file__).read_bytes()).hexdigest(),
            ALU02_CHECKER_SHA256,
        )

    def assertUnifies(self, a, b):
        substitution = alu02.unify_terms(a, b)
        self.assertTrue(alu02.check_unifies(a, b, substitution))
        self.assertEqual(alu02.normalize_subst(substitution), substitution)
        return substitution

    def test_receipt_cases(self):
        self.assertUnifies(V("x"), C("a"))
        self.assertUnifies(F("f", V("x")), F("f", C("a")))
        with self.assertRaises(alu02.UnificationError):
            alu02.unify_terms(V("x"), F("f", V("x")))
        with self.assertRaises(alu02.UnificationError):
            alu02.unify_terms(F("f", C("a")), F("g", C("a")))
        with self.assertRaises(alu02.UnificationError):
            alu02.unify_terms(F("f", C("a")), F("f", C("a"), C("b")))
        self.assertUnifies(F("f", V("x"), V("x")), F("f", V("y"), C("a")))
        self.assertUnifies(
            F("f", F("g", V("x")), V("y")),
            F("f", F("g", C("a")), C("b")),
        )
        with self.assertRaises(alu02.UnificationError):
            alu02.unify_terms({"bad": "x"}, C("a"))
        self.assertEqual(
            alu02.run_request({"left": V("x")})["status"],
            "REJECT_MALFORMED_REQUEST",
        )

    def test_symmetry_and_idempotence_fuzz(self):
        rng = random.Random(20260914)
        atoms = [C("a"), C("b"), V("x"), V("y"), V("z")]

        def term(depth=0):
            if depth >= 3 or rng.random() < 0.55:
                return rng.choice(atoms)
            return F(
                rng.choice(["f", "g"]),
                *(term(depth + 1) for _ in range(rng.randint(1, 3))),
            )

        for _ in range(3000):
            a, b = term(), term()
            outcomes = []
            for left, right in ((a, b), (b, a)):
                try:
                    substitution = alu02.unify_terms(left, right)
                    outcomes.append(alu02.check_unifies(left, right, substitution))
                    self.assertEqual(
                        alu02.normalize_subst(substitution),
                        substitution,
                    )
                except alu02.UnificationError:
                    outcomes.append(False)
            self.assertEqual(outcomes[0], outcomes[1])


class RegistryTests(unittest.TestCase):
    def test_alu02_rebound_not_canon(self):
        binding = execution_binding(Fragment.ALU02_FIRST_ORDER_UNIFICATION)
        self.assertEqual(
            binding.status,
            ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        )
        self.assertFalse(binding.canon_promoted)
        self.assertEqual(validate_execution_registry(), ())

    def test_rebound_and_unbound_fragments_are_distinct(self):
        self.assertEqual(
            execution_binding(Fragment.ALU03_TEMPORAL_LTL).status,
            ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        )
        self.assertEqual(
            execution_binding(Fragment.ALU07_QUANTUM_LOGIC).status,
            ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
        )
        self.assertEqual(
            execution_binding(Fragment.ALU04_EPISTEMIC_MODAL).status,
            ExecutionStatus.SPECIFICATION_ONLY,
        )

    def test_algorithm_precondition_gates(self):
        self.assertTrue(
            eligible("dijkstra", frozenset({"graph", "nonnegative_weights"}))
        )
        self.assertFalse(eligible("dijkstra", frozenset({"graph"})))
        self.assertEqual(
            missing_preconditions("cp_sat", frozenset({"integer_model"})),
            ("typed_constraints",),
        )

    def test_shortest_path_selector(self):
        self.assertEqual(
            choose_shortest_path(
                weighted=False,
                negative_edges=False,
                all_pairs=False,
            ),
            "bfs",
        )
        self.assertEqual(
            choose_shortest_path(
                weighted=True,
                negative_edges=False,
                all_pairs=False,
            ),
            "dijkstra",
        )
        self.assertEqual(
            choose_shortest_path(
                weighted=True,
                negative_edges=True,
                all_pairs=False,
            ),
            "bellman_ford",
        )
        self.assertEqual(
            choose_shortest_path(
                weighted=True,
                negative_edges=True,
                all_pairs=True,
            ),
            "johnson",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
