import math
import random
import unittest

import logic_math_runtime as m


class LogicMathRuntimeTests(unittest.TestCase):
    def test_warshall_transitive_closure_and_reflexivity(self):
        a = (
            (False, True, False, False),
            (False, False, True, False),
            (False, False, False, True),
            (False, False, False, False),
        )
        r = m.transitive_closure(a)
        self.assertTrue(r[0][3])
        self.assertTrue(all(r[i][i] for i in range(4)))

    def test_warshall_non_reflexive_does_not_invent_empty_paths(self):
        a = ((False, True), (False, False))
        r = m.transitive_closure(a, reflexive=False)
        self.assertFalse(r[0][0])
        self.assertFalse(r[1][1])

    def test_tarjan_scc_partition(self):
        a = (
            (False, True, False, False, False),
            (True, False, True, False, False),
            (False, False, False, True, False),
            (False, False, True, False, True),
            (False, False, False, False, False),
        )
        self.assertEqual(m.strongly_connected_components(a), ((0, 1), (2, 3), (4,)))

    def test_kahn_topological_order_and_cycle_fail_closed(self):
        dag = (
            (False, True, True, False),
            (False, False, False, True),
            (False, False, False, True),
            (False, False, False, False),
        )
        order = m.topological_order(dag)
        position = {node: i for i, node in enumerate(order)}
        for i, row in enumerate(dag):
            for j, edge in enumerate(row):
                if edge:
                    self.assertLess(position[i], position[j])

        cyclic = ((False, True), (True, False))
        with self.assertRaises(m.MathInvariantError):
            m.topological_order(cyclic)

    def test_dijkstra_shortest_distances(self):
        I = math.inf
        graph = m.WeightedTopology(
            (
                (0, 1, 4, I, I),
                (I, 0, 2, 6, I),
                (I, I, 0, 1, 7),
                (I, I, I, 0, 3),
                (I, I, I, I, 0),
            )
        )
        self.assertEqual(graph.shortest_distances(0), (0.0, 1.0, 3.0, 4.0, 7.0))

    def test_dijkstra_rejects_negative_nonfinite_and_bad_diagonal(self):
        I = math.inf
        with self.assertRaises(m.MathInvariantError):
            m.WeightedTopology(((0, -1), (I, 0)))
        with self.assertRaises(m.MathInvariantError):
            m.WeightedTopology(((1, I), (I, 0)))
        with self.assertRaises(m.MathInvariantError):
            m.WeightedTopology(((0, math.nan), (I, 0)))

    def test_row_stochastic_mass_conservation(self):
        p = m.RowStochasticMatrix(((0.9, 0.1), (0.2, 0.8)))
        x = (0.3, 0.7)
        y = p.step(x)
        self.assertAlmostEqual(sum(y), 1.0)
        self.assertAlmostEqual(y[0], 0.41)
        self.assertAlmostEqual(y[1], 0.59)

    def test_row_stochastic_rejects_invalid_domains(self):
        with self.assertRaises(m.MathInvariantError):
            m.RowStochasticMatrix(((0.9, 0.2), (0.2, 0.8)))
        p = m.RowStochasticMatrix(((1.0, 0.0), (0.0, 1.0)))
        with self.assertRaises(m.MathInvariantError):
            p.step((0.5, 0.6))

    def test_sparse_tensor_is_typed_bounded_and_finite(self):
        t = m.SparseLogicTensor(
            axes=("row", "col", "scale", "regime"),
            shape=(19, 19, 3, 2),
            values={(0, 1, 2, 1): 3.0, (18, 18, 0, 0): 4.0},
        )
        self.assertEqual(t.rank, 4)
        self.assertEqual(t.get((0, 1, 2, 1)), 3.0)
        self.assertEqual(t.get((0, 0, 0, 0)), 0.0)
        self.assertEqual(t.frobenius_norm_sq(), 25.0)
        with self.assertRaises(TypeError):
            t.values[(0, 0, 0, 0)] = 1.0
        with self.assertRaises(m.MathInvariantError):
            m.SparseLogicTensor(axes=("x", "x"), shape=(2, 2))
        with self.assertRaises(m.MathInvariantError):
            m.SparseLogicTensor(axes=("x",), shape=(2,), values={(2,): 1.0})

    def test_core19_topology_is_exactly_19_by_19(self):
        a = m.core19_topology_matrix(((1, 2), (2, 19), (19, 1)))
        self.assertEqual(len(a), 19)
        self.assertTrue(all(len(row) == 19 for row in a))
        r = m.transitive_closure(a)
        self.assertTrue(r[0][18])
        self.assertTrue(r[18][1])
        with self.assertRaises(m.MathInvariantError):
            m.core19_topology_matrix(((0, 1),))

    def test_seeded_random_dags_topological_order_respects_every_edge(self):
        rng = random.Random(20260914)
        for n in range(2, 25):
            for _ in range(40):
                a = [[False] * n for _ in range(n)]
                for i in range(n):
                    for j in range(i + 1, n):
                        if rng.random() < 0.2:
                            a[i][j] = True
                order = m.topological_order(a)
                position = {node: i for i, node in enumerate(order)}
                for i in range(n):
                    for j in range(n):
                        if a[i][j]:
                            self.assertLess(position[i], position[j])

    def test_seeded_random_closure_is_transitive(self):
        rng = random.Random(9142026)
        for n in range(2, 18):
            for _ in range(30):
                a = [[rng.random() < 0.15 for _ in range(n)] for _ in range(n)]
                r = m.transitive_closure(a)
                for i in range(n):
                    for j in range(n):
                        if not r[i][j]:
                            continue
                        for k in range(n):
                            if r[j][k]:
                                self.assertTrue(r[i][k])

    def test_provenance_registry_contains_primary_algorithms(self):
        self.assertEqual(
            set(m.ALGORITHM_PROVENANCE),
            {
                "warshall_transitive_closure",
                "tarjan_scc",
                "dijkstra_shortest_path",
                "kahn_topological_sort",
            },
        )
        for record in m.ALGORITHM_PROVENANCE.values():
            self.assertEqual(record["status"], "ESTABLISHED_ALGORITHM")
            self.assertTrue(record["doi"])

    def test_invariant_bundle(self):
        self.assertEqual(m.validate_math_invariants(), ())


if __name__ == "__main__":
    unittest.main()
