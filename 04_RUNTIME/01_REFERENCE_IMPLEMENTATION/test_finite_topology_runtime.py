import unittest

import finite_topology_runtime as t


class FiniteTopologyRuntimeTests(unittest.TestCase):
    def test_valid_finite_topology_and_specialization_preorder(self):
        space = t.FiniteTopology(
            (0, 1, 2),
            ((), (0,), (0, 1), (0, 1, 2)),
        )
        self.assertTrue(space.is_open((0, 1)))
        self.assertFalse(space.is_open((1,)))
        self.assertEqual(
            space.specialization_matrix(),
            (
                (True, False, False),
                (True, True, False),
                (True, True, True),
            ),
        )
        self.assertTrue(space.is_t0())

    def test_invalid_union_closure_fails_closed(self):
        with self.assertRaises(t.TopologyInvariantError):
            t.FiniteTopology(
                (0, 1, 2),
                ((), (0,), (1,), (0, 1, 2)),
            )

    def test_invalid_intersection_closure_fails_closed(self):
        with self.assertRaises(t.TopologyInvariantError):
            t.FiniteTopology(
                (0, 1, 2),
                ((), (0, 1), (1, 2), (0, 1, 2)),
            )

    def test_points_outside_carrier_and_duplicate_carrier_fail_closed(self):
        with self.assertRaises(t.TopologyInvariantError):
            t.FiniteTopology((0, 1), ((), (0, 1), (2,)))
        with self.assertRaises(t.TopologyInvariantError):
            t.FiniteTopology((0, 0), ((), (0,)))

    def test_indiscrete_space_not_t0_when_multiple_points(self):
        space = t.FiniteTopology((0, 1), ((), (0, 1)))
        self.assertFalse(space.is_t0())
        self.assertEqual(
            space.specialization_matrix(),
            ((True, True), (True, True)),
        )

    def test_invariant_bundle(self):
        self.assertEqual(t.validate_finite_topology_invariants(), ())


if __name__ == "__main__":
    unittest.main()
