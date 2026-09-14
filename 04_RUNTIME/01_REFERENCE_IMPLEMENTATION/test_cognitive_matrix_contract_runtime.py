import unittest

from cognitive_matrix_runtime import (
    CellRecord,
    Condition,
    DependencyGraph,
    DependencyKind,
    GapKind,
    GapSignal,
    Maturity,
)
from matrix_registry_runtime import MatrixCellRecord
from cognitive_matrix_contract_runtime import (
    CellBinding,
    CellBindingRegistry,
    GapRecord,
    GapRegistry,
    GapResolutionEvidence,
    GapState,
    RevalidationReceipt,
    audit_dependencies,
    audit_selective_invalidation,
    close_gap,
    project_cell_status,
    propose_gap_resolution,
)


def gap(kind=GapKind.VALIDATION):
    return GapSignal("g", kind, 0, 0, 0, 0, 0, 0, 0)


class CellBindingTests(unittest.TestCase):
    def test_binding_must_match_cell_state(self):
        cell = MatrixCellRecord(
            "c", Maturity.VALIDATED_BOUNDED, Condition.ACTIVE, "v1",
            source_ids=("s",), evidence_ids=("e",), authority_witness_id="w",
        )
        binding = CellBinding("c", "v1", ("s",), ("e",), "w", ("upstream",))
        registry = CellBindingRegistry()
        registry.register(binding)
        self.assertEqual(registry.validate_against_cell(binding, cell), ())
        wrong = CellBinding("c", "v2", ("s",), ("e",), "w", ("upstream",))
        self.assertIn("STATE_VERSION_MISMATCH", registry.validate_against_cell(wrong, cell))

    def test_binding_identity_collision_fails_closed(self):
        registry = CellBindingRegistry()
        registry.register(CellBinding("c", "v1"))
        with self.assertRaises(ValueError):
            registry.register(CellBinding("c", "v2"))

    def test_status_projection_preserves_orthogonal_axes(self):
        cell = MatrixCellRecord("c", Maturity.IMPLEMENTED, Condition.STALE, "v1")
        status = project_cell_status(cell)
        self.assertEqual(status.maturity, Maturity.IMPLEMENTED)
        self.assertEqual(status.condition, Condition.STALE)


class GapLifecycleTests(unittest.TestCase):
    def test_validation_gap_requires_positive_and_adversarial_tests(self):
        record = GapRecord(gap(), "v1")
        with self.assertRaises(ValueError):
            propose_gap_resolution(
                record,
                GapResolutionEvidence("e", "g", "v1", tests_executed=True),
            )
        proposed = propose_gap_resolution(
            record,
            GapResolutionEvidence(
                "e", "g", "v1", tests_executed=True, adversarial_tests_executed=True
            ),
        )
        self.assertEqual(proposed.state, GapState.RESOLUTION_PROPOSED)

    def test_gap_cannot_close_without_revalidation_and_fresh_dependencies(self):
        proposed = propose_gap_resolution(
            GapRecord(gap(), "v1"),
            GapResolutionEvidence(
                "e", "g", "v1", tests_executed=True, adversarial_tests_executed=True
            ),
        )
        with self.assertRaises(ValueError):
            close_gap(proposed, RevalidationReceipt("r", "g", "v1", False, True))
        with self.assertRaises(ValueError):
            close_gap(proposed, RevalidationReceipt("r", "g", "v1", True, False))
        closed = close_gap(proposed, RevalidationReceipt("r", "g", "v1", True, True))
        self.assertEqual(closed.state, GapState.CLOSED)

    def test_kind_specific_resolution_gate(self):
        cases = {
            GapKind.SOURCE: dict(source_resolved=True),
            GapKind.SEMANTICS: dict(semantics_typed=True),
            GapKind.IMPLEMENTATION: dict(implementation_receipt=True),
            GapKind.AUTHORITY: dict(authority_witness=True),
            GapKind.DEPENDENCY_CYCLE: dict(dependency_audit_passed=True),
            GapKind.STALENESS: dict(dependencies_fresh=True),
            GapKind.CONTRADICTION: dict(contradiction_resolved=True),
        }
        for kind, kwargs in cases.items():
            record = GapRecord(gap(kind), "v1")
            proposed = propose_gap_resolution(
                record, GapResolutionEvidence("e", "g", "v1", **kwargs)
            )
            self.assertEqual(proposed.state, GapState.RESOLUTION_PROPOSED)

    def test_gap_registry_allows_only_legal_monotonic_closure(self):
        registry = GapRegistry()
        opened = GapRecord(gap(), "v1")
        registry.register(opened)
        proposed = propose_gap_resolution(
            opened,
            GapResolutionEvidence(
                "e", "g", "v1", tests_executed=True, adversarial_tests_executed=True
            ),
        )
        registry.replace(proposed)
        closed = close_gap(proposed, RevalidationReceipt("r", "g", "v1", True, True))
        registry.replace(closed)
        with self.assertRaises(ValueError):
            registry.replace(proposed)


class DependencyContractTests(unittest.TestCase):
    def test_dependency_audit_detects_cycle(self):
        graph = DependencyGraph(["a", "b"])
        graph.add_edge("a", "b")
        graph.add_edge("b", "a")
        audit = audit_dependencies(graph)
        self.assertFalse(audit.acyclic)
        self.assertEqual(audit.topological_order, None)
        self.assertEqual(audit.load_bearing_cycles, (("a", "b"),))

    def test_invalidation_is_selective_and_stale_not_false(self):
        graph = DependencyGraph(["a", "b", "soft"])
        graph.add_edge("a", "b", DependencyKind.HARD)
        graph.add_edge("a", "soft", DependencyKind.SOFT)
        records = {node: CellRecord(node, Maturity.IMPLEMENTED) for node in graph.nodes}
        root, updated = audit_selective_invalidation(graph, records, "a")
        self.assertEqual(root.condition, Condition.QUARANTINED)
        self.assertEqual(updated["b"].condition, Condition.STALE)
        self.assertEqual(updated["soft"].condition, Condition.ACTIVE)
        self.assertNotEqual(updated["b"].condition, Condition.FALSIFIED)


if __name__ == "__main__":
    unittest.main()
