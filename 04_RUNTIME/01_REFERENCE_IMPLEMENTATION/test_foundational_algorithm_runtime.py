import math
import unittest

import foundational_algorithm_runtime as a


class UnionFindTests(unittest.TestCase):
    def test_connectivity_is_only_declared_union_connectivity(self):
        uf = a.UnionFind(("a", "b", "c", "d"))
        uf.union("a", "b")
        uf.union("c", "d")
        self.assertTrue(uf.connected("a", "b"))
        self.assertFalse(uf.connected("a", "c"))
        self.assertEqual(
            {frozenset(component) for component in uf.components()},
            {frozenset(("a", "b")), frozenset(("c", "d"))},
        )
        with self.assertRaises(KeyError):
            uf.find("missing")


class BellmanFordTests(unittest.TestCase):
    def test_negative_edges_without_negative_cycle(self):
        result = a.bellman_ford(
            ("s", "a", "b", "z"),
            (("s", "a", 4.0), ("s", "b", 5.0), ("a", "b", -2.0)),
            "s",
        )
        self.assertEqual(result.status, a.ShortestPathStatus.OK)
        self.assertEqual(result.distances["s"], 0.0)
        self.assertEqual(result.distances["a"], 4.0)
        self.assertEqual(result.distances["b"], 2.0)
        self.assertTrue(math.isinf(result.distances["z"]))

    def test_only_reachable_negative_cycle_changes_status(self):
        reachable = a.bellman_ford(
            ("s", "a", "b"),
            (("s", "a", 1.0), ("a", "b", 1.0), ("b", "a", -3.0)),
            "s",
        )
        self.assertEqual(reachable.status, a.ShortestPathStatus.REACHABLE_NEGATIVE_CYCLE)

        unreachable = a.bellman_ford(
            ("s", "a", "c", "d"),
            (("s", "a", 2.0), ("c", "d", 1.0), ("d", "c", -2.0)),
            "s",
        )
        self.assertEqual(unreachable.status, a.ShortestPathStatus.OK)

    def test_invalid_weights_fail_closed(self):
        with self.assertRaises(ValueError):
            a.bellman_ford(("s", "a"), (("s", "a", float("nan")),), "s")
        with self.assertRaises(ValueError):
            a.bellman_ford(("s",), (("s", "x", 1.0),), "s")


class MaxFlowTests(unittest.TestCase):
    def test_classic_network_has_integral_max_flow_23(self):
        capacities = {
            ("s", "v1"): 16,
            ("s", "v2"): 13,
            ("v1", "v2"): 10,
            ("v2", "v1"): 4,
            ("v1", "v3"): 12,
            ("v3", "v2"): 9,
            ("v2", "v4"): 14,
            ("v4", "v3"): 7,
            ("v3", "t"): 20,
            ("v4", "t"): 4,
        }
        result = a.edmonds_karp_max_flow(capacities, "s", "t")
        self.assertEqual(result.value, 23)

    def test_capacity_contract_is_integral_nonnegative(self):
        with self.assertRaises(ValueError):
            a.edmonds_karp_max_flow({("s", "t"): -1}, "s", "t")
        with self.assertRaises(ValueError):
            a.edmonds_karp_max_flow({("s", "t"): True}, "s", "t")
        with self.assertRaises(ValueError):
            a.edmonds_karp_max_flow({("s", "t"): 1}, "s", "s")


class DPLLTests(unittest.TestCase):
    @staticmethod
    def _satisfies(clauses, assignment):
        return all(
            any(assignment[abs(literal)] == (literal > 0) for literal in clause)
            for clause in clauses
        )

    def test_sat_assignment_is_a_witness(self):
        clauses = ((1, 2), (-1, 2), (1, -2))
        result = a.dpll_sat(clauses)
        self.assertEqual(result.status, a.SatStatus.SAT)
        self.assertTrue(self._satisfies(clauses, result.assignment))

    def test_unsat_and_empty_clause(self):
        self.assertEqual(a.dpll_sat(((1,), (-1,))).status, a.SatStatus.UNSAT)
        self.assertEqual(a.dpll_sat(((),)).status, a.SatStatus.UNSAT)

    def test_tautological_clause_does_not_force_assignment_truth(self):
        result = a.dpll_sat(((1, -1),))
        self.assertEqual(result.status, a.SatStatus.SAT)
        self.assertIn(1, result.assignment)

    def test_literal_zero_and_boolean_are_rejected(self):
        with self.assertRaises(ValueError):
            a.dpll_sat(((0,),))
        with self.assertRaises(ValueError):
            a.dpll_sat(((True,),))


class AC3Tests(unittest.TestCase):
    def test_arc_consistency_prunes_without_claiming_global_solution(self):
        domains = {"x": {1, 2, 3}, "y": {1, 2, 3}}
        less = frozenset((x, y) for x in domains["x"] for y in domains["y"] if x < y)
        greater = frozenset((y, x) for x, y in less)
        result = a.ac3_arc_consistency(
            domains,
            {("x", "y"): less, ("y", "x"): greater},
        )
        self.assertTrue(result.consistent)
        self.assertEqual(result.domains["x"], frozenset({1, 2}))
        self.assertEqual(result.domains["y"], frozenset({2, 3}))

    def test_inconsistent_domain_is_explicit(self):
        result = a.ac3_arc_consistency(
            {"x": {1}, "y": {1}},
            {("x", "y"): frozenset()},
        )
        self.assertFalse(result.consistent)
        self.assertEqual(result.domains["x"], frozenset())

    def test_constraints_require_declared_variables_and_frozen_relation(self):
        with self.assertRaises(ValueError):
            a.ac3_arc_consistency({"x": {1}}, {("x", "y"): frozenset({(1, 1)})})
        with self.assertRaises(ValueError):
            a.ac3_arc_consistency({"x": {1}, "y": {1}}, {("x", "y"): {(1, 1)}})  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
