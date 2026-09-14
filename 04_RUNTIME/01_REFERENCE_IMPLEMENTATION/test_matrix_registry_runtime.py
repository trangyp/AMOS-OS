import unittest
from matrix_registry_runtime import (
    AuditStatus, AuthorityWitness, CellRegistry, Condition, CoverageThresholds,
    EvidenceClass, EvidenceRef, EvidenceRegistry, MatrixCellRecord, Maturity,
    audit_coverage, compute_coverage, validate_authority_binding,
)

class RegistryTests(unittest.TestCase):
    def test_cell_registry_rejects_identity_collision(self):
        reg = CellRegistry()
        reg.register(MatrixCellRecord("c", Maturity.SOURCE_BOUND, Condition.ACTIVE, "v1"))
        with self.assertRaises(ValueError):
            reg.register(MatrixCellRecord("c", Maturity.SOURCE_BOUND, Condition.ACTIVE, "v2"))

    def test_evidence_requires_matching_state_version_and_freshness(self):
        er = EvidenceRegistry()
        er.register(EvidenceRef("e1", EvidenceClass.EXECUTED_TEST, "test.py", "v1", True))
        record = MatrixCellRecord("c", Maturity.VALIDATED_BOUNDED, Condition.ACTIVE, "v1", evidence_ids=("e1",))
        self.assertEqual(er.validate_cell_evidence(record), (True, ()))
        stale = EvidenceRegistry()
        stale.register(EvidenceRef("e1", EvidenceClass.EXECUTED_TEST, "test.py", "v1", False))
        self.assertEqual(stale.validate_cell_evidence(record), (False, ("STALE:e1",)))

class AuthorityTests(unittest.TestCase):
    def test_authority_requires_exact_scope_policy_state_and_freshness(self):
        record = MatrixCellRecord("c", Maturity.AUTHORIZED_BOUNDED, Condition.ACTIVE, "v4", authority_witness_id="w")
        w = AuthorityWitness("w", "principal", ("matrix:commit",), "p1", "v4", True)
        self.assertEqual(validate_authority_binding(record, {"w": w}, "matrix:commit", "p1"), (True, "AUTHORIZED_BOUNDED"))
        self.assertFalse(validate_authority_binding(record, {"w": w}, "canon:promote", "p1")[0])
        stale = AuthorityWitness("w", "principal", ("matrix:commit",), "p1", "v4", False)
        self.assertFalse(validate_authority_binding(record, {"w": stale}, "matrix:commit", "p1")[0])

    def test_capability_without_authorized_maturity_fails(self):
        record = MatrixCellRecord("c", Maturity.VALIDATED_BOUNDED, Condition.ACTIVE, "v4", authority_witness_id="w")
        w = AuthorityWitness("w", "principal", ("matrix:commit",), "p1", "v4", True)
        self.assertEqual(validate_authority_binding(record, {"w": w}, "matrix:commit", "p1")[1], "CELL_NOT_AUTHORIZED_BOUNDED")

class CoverageTests(unittest.TestCase):
    def test_coverage_audit_does_not_turn_address_coverage_into_completion(self):
        records = [
            MatrixCellRecord("a", Maturity.CONTRACT_COMPLETE, Condition.ACTIVE, "v1"),
            MatrixCellRecord("b", Maturity.IMPLEMENTED, Condition.ACTIVE, "v1"),
        ]
        coverage = compute_coverage(records)
        self.assertEqual(coverage.address, 1.0)
        audit = audit_coverage(coverage, CoverageThresholds())
        self.assertEqual(audit.status, AuditStatus.INCOMPLETE)
        self.assertEqual(audit.failed_dimensions, ("implementation", "validation", "authority"))

    def test_custom_thresholds_are_explicit_and_bounded(self):
        records = [MatrixCellRecord("a", Maturity.VALIDATED_BOUNDED, Condition.ACTIVE, "v1")]
        coverage = compute_coverage(records)
        audit = audit_coverage(coverage, CoverageThresholds(authority=0.0))
        self.assertEqual(audit.status, AuditStatus.PASS)
        with self.assertRaises(ValueError):
            CoverageThresholds(validation=1.1)

if __name__ == "__main__":
    unittest.main()
