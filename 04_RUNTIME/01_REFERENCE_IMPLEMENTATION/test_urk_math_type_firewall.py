import unittest

import core19_runtime as c
import core19_tensor_topology as ct
from finite_topology_runtime import FiniteTopology


class URKMathTypeFirewallTests(unittest.TestCase):
    def test_coordinate_field_is_not_tensor_by_name(self):
        coord = c.CoordinateFieldCoordinate(
            c.Core19.P01_EXISTENCE,
            c.Core19.P05_INFORMATIONAL,
            "H",
            "ctx",
            "regime",
            "observer",
        )
        entry = ct.CoordinateFieldEntry(coord, "value", c.CellStatus.AMOS_MODEL)
        store = ct.URKCoordinateFieldStore[str]()
        store.bind(entry)
        self.assertEqual(store.get(coord), entry)
        self.assertIs(c.TensorCoordinate, c.CoordinateFieldCoordinate)
        self.assertIs(ct.TensorEntry, ct.CoordinateFieldEntry)
        self.assertIs(ct.URKTensorStore, ct.URKCoordinateFieldStore)

    def test_tensor_declaration_requires_all_algebraic_structure_witnesses(self):
        with self.assertRaises(ValueError):
            c.TensorDeclaration("", ("module-1",), "multi", "tensor-product")
        with self.assertRaises(ValueError):
            c.TensorDeclaration("scalar", (), "multi", "tensor-product")

    def test_tensor_axis_witness_count_must_match_declared_dimension(self):
        declaration = c.TensorDeclaration(
            "scalar-field",
            ("module-1", "module-2"),
            "multilinearity-proof-ref",
            "tensor-product-construction-ref",
        )
        with self.assertRaisesRegex(ValueError, "TENSOR_AXIS_MODULE_WITNESS_COUNT"):
            c.bind_tensor_structure(declaration, axis_count=3)
        receipt = c.bind_tensor_structure(declaration, axis_count=2)
        self.assertEqual(receipt.status, "STRUCTURALLY_TYPED_AMOS_MODEL")
        self.assertEqual(receipt.axis_count, 2)

    def test_coordinate_tensor_claim_requires_basis_witness(self):
        declaration = c.TensorDeclaration(
            "scalar-field",
            ("module-1", "module-2"),
            "multilinearity-proof-ref",
            "tensor-product-construction-ref",
        )
        with self.assertRaisesRegex(ValueError, "TENSOR_COORDINATE_BASIS_WITNESS"):
            c.bind_tensor_structure(declaration, axis_count=2, coordinates_used=True)
        with_basis = c.TensorDeclaration(
            "scalar-field",
            ("module-1", "module-2"),
            "multilinearity-proof-ref",
            "tensor-product-construction-ref",
            "basis-ref",
        )
        receipt = c.bind_tensor_structure(with_basis, axis_count=2, coordinates_used=True)
        self.assertTrue(receipt.coordinates_used)

    def test_structural_adjacency_is_not_point_set_topology(self):
        store = ct.StructuralAdjacencyStore()
        edge = c.StructuralAdjacencyEdge(
            c.Core19.P06_TOPOLOGICAL,
            c.Core19.P03_CAUSALITY,
            "typed-relation-not-cause",
            c.CellStatus.AMOS_MODEL,
        )
        cell = ct.StructuralAdjacencyCell(
            c.Core19.P06_TOPOLOGICAL,
            c.Core19.P03_CAUSALITY,
            edge,
        )
        store.bind(cell)
        self.assertIs(ct.TopologyMatrixStore, ct.StructuralAdjacencyStore)
        self.assertNotIsInstance(store, FiniteTopology)
        self.assertEqual(store.populated_count(), 1)

    def test_selective_invalidation_requires_every_runtime_gate(self):
        full = dict(
            dependency_orientation_bound=True,
            state_epoch_bound=True,
            closure_algorithm_bound=True,
            validation_receipt_bound=True,
        )
        self.assertTrue(c.SelectiveInvalidationGate(**full).enforceable())
        for key in full:
            missing = dict(full)
            missing[key] = False
            self.assertFalse(c.SelectiveInvalidationGate(**missing).enforceable(), key)

    def test_invariant_bundles(self):
        self.assertEqual(c.validate_runtime_invariants(), ())
        self.assertEqual(ct.validate_coordinate_topology_invariants(), ())
        self.assertEqual(ct.validate_tensor_topology_invariants(), ())


if __name__ == "__main__":
    unittest.main()
