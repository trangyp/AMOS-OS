import unittest

from core19_runtime import CellStatus, Core19, TensorCoordinate, TopologyEdge
from core19_tensor_topology import (
    CoordinateConflictError,
    TensorEntry,
    TopologyCell,
    TopologyMatrixStore,
    URKTensorStore,
    validate_tensor_topology_invariants,
)


class TensorTests(unittest.TestCase):
    def test_axes_do_not_alias(self):
        store = URKTensorStore[str]()
        h = TensorCoordinate(Core19.P01_EXISTENCE, Core19.P03_CAUSALITY, "H", "ctx", "normal", "observer-a")
        m = TensorCoordinate(Core19.P01_EXISTENCE, Core19.P03_CAUSALITY, "M", "ctx", "normal", "observer-a")
        o = TensorCoordinate(Core19.P01_EXISTENCE, Core19.P03_CAUSALITY, "H", "ctx", "normal", "observer-b")
        store.bind(TensorEntry(h, "high", CellStatus.AMOS_MODEL))
        store.bind(TensorEntry(m, "mid", CellStatus.DERIVED))
        store.bind(TensorEntry(o, "other-observer", CellStatus.DERIVED))
        self.assertEqual(len(store), 3)
        self.assertEqual(store.get(h).value, "high")
        self.assertEqual(store.get(m).value, "mid")
        self.assertEqual(store.get(o).value, "other-observer")

    def test_unbound_is_unbound_not_zero(self):
        store = URKTensorStore[int]()
        coord = TensorCoordinate(Core19.P05_INFORMATIONAL, Core19.P19_NULL_LOGIC, "L", "ctx", "normal", "observer")
        self.assertIsNone(store.get(coord))
        self.assertEqual(store.status(coord), CellStatus.UNBOUND)

    def test_conflicting_rebind_fails_closed(self):
        store = URKTensorStore[int]()
        coord = TensorCoordinate(Core19.P01_EXISTENCE, Core19.P01_EXISTENCE, "H", "ctx", "normal", "observer")
        store.bind(TensorEntry(coord, 1, CellStatus.AMOS_MODEL, "s1"))
        with self.assertRaises(CoordinateConflictError):
            store.bind(TensorEntry(coord, 2, CellStatus.AMOS_MODEL, "s1"))


class TopologyTests(unittest.TestCase):
    def test_full_index_has_361_coordinates_but_starts_unbound(self):
        matrix = TopologyMatrixStore()
        self.assertEqual(matrix.coordinate_count(), 361)
        self.assertEqual(matrix.populated_count(), 0)
        self.assertEqual(matrix.unbound_count(), 361)

    def test_edge_must_match_matrix_coordinate(self):
        edge = TopologyEdge(Core19.P01_EXISTENCE, Core19.P03_CAUSALITY, "rel", CellStatus.AMOS_MODEL)
        with self.assertRaises(ValueError):
            TopologyCell(Core19.P01_EXISTENCE, Core19.P04_TEMPORAL, edge)

    def test_bound_relation_does_not_change_other_coordinates(self):
        matrix = TopologyMatrixStore()
        cell = TopologyCell(
            Core19.P06_TOPOLOGICAL,
            Core19.P03_CAUSALITY,
            TopologyEdge(Core19.P06_TOPOLOGICAL, Core19.P03_CAUSALITY, "relation-not-cause", CellStatus.AMOS_MODEL),
        )
        matrix.bind(cell)
        self.assertEqual(matrix.populated_count(), 1)
        self.assertEqual(matrix.unbound_count(), 360)
        self.assertEqual(matrix.status(Core19.P03_CAUSALITY, Core19.P06_TOPOLOGICAL), CellStatus.UNBOUND)

    def test_conflicting_topology_rebind_fails_closed(self):
        matrix = TopologyMatrixStore()
        a = TopologyCell(
            Core19.P01_EXISTENCE,
            Core19.P07_IDENTITY,
            TopologyEdge(Core19.P01_EXISTENCE, Core19.P07_IDENTITY, "r1", CellStatus.SOURCE_CLAIM),
        )
        b = TopologyCell(
            Core19.P01_EXISTENCE,
            Core19.P07_IDENTITY,
            TopologyEdge(Core19.P01_EXISTENCE, Core19.P07_IDENTITY, "r2", CellStatus.AMOS_MODEL),
        )
        matrix.bind(a)
        with self.assertRaises(CoordinateConflictError):
            matrix.bind(b)

    def test_invariant_suite(self):
        self.assertEqual(validate_tensor_topology_invariants(), ())


if __name__ == "__main__":
    unittest.main()
