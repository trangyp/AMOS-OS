import unittest

from c01_governance_runtime import (
    GovernanceRequest,
    GovernanceStatus,
    evaluate_governance,
)


def request(**overrides):
    base = dict(
        request_id="req-1",
        principal="principal-1",
        scopes=("effect:stage",),
        policy_hash="policy-v1",
        state_version="state-v1",
        enforcement_root_id="root-1",
        enforcement_root_attested=True,
        enforcement_root_agent_write_excluded=True,
        precedence_version="prec-v1",
        expected_precedence_version="prec-v1",
        decision_receipt_id="receipt-1",
        observed_epoch="epoch-1",
        required_epoch="epoch-1",
    )
    base.update(overrides)
    return GovernanceRequest(**base)


class GovernanceRuntimeTests(unittest.TestCase):
    def test_valid_request_emits_bounded_authority_and_receipt(self):
        result = evaluate_governance(request())
        self.assertEqual(result.status, GovernanceStatus.AUTHORIZE_BOUNDED)
        self.assertIsNotNone(result.authority)
        self.assertEqual(result.authority.principal, "principal-1")
        self.assertTrue(result.authority.authorizes("effect:stage", "policy-v1", "state-v1"))
        self.assertEqual(len(result.governance_receipt_hash), 64)
        self.assertIn("BOUNDED_AUTHORITY_IS_NOT_EFFECT_COMMIT", result.reasons)

    def test_receipt_hash_is_deterministic_and_scope_order_normalized(self):
        a = evaluate_governance(request(scopes=("b", "a")))
        b = evaluate_governance(request(scopes=("a", "b")))
        self.assertEqual(a.governance_receipt_hash, b.governance_receipt_hash)
        self.assertEqual(a.authority.scope, ("a", "b"))

    def test_root_attestation_and_agent_write_exclusion_are_both_required(self):
        self.assertEqual(
            evaluate_governance(request(enforcement_root_attested=False)).status,
            GovernanceStatus.BLOCK_ENFORCEMENT_ROOT,
        )
        self.assertEqual(
            evaluate_governance(request(enforcement_root_agent_write_excluded=False)).status,
            GovernanceStatus.BLOCK_ENFORCEMENT_ROOT,
        )

    def test_precedence_drift_and_epoch_staleness_fail_closed(self):
        self.assertEqual(
            evaluate_governance(request(precedence_version="old")).status,
            GovernanceStatus.BLOCK_PRECEDENCE,
        )
        self.assertEqual(
            evaluate_governance(request(observed_epoch="old")).status,
            GovernanceStatus.REVALIDATE_STALE,
        )

    def test_receipt_policy_and_scope_are_mandatory_gates(self):
        self.assertEqual(
            evaluate_governance(request(decision_receipt_id="")).status,
            GovernanceStatus.BLOCK_RECEIPT,
        )
        self.assertEqual(
            evaluate_governance(request(policy_hash="")).status,
            GovernanceStatus.BLOCK_POLICY,
        )
        self.assertEqual(
            evaluate_governance(request(scopes=())).status,
            GovernanceStatus.BLOCK_SCOPE,
        )

    def test_duplicate_or_malformed_scope_fails_at_boundary(self):
        with self.assertRaises(ValueError):
            request(scopes=("x", "x"))
        with self.assertRaises(ValueError):
            request(scopes=("",))

    def test_receipt_identity_changes_when_load_bearing_authority_inputs_change(self):
        base = evaluate_governance(request()).governance_receipt_hash
        variants = {
            evaluate_governance(request(principal="p2")).governance_receipt_hash,
            evaluate_governance(request(policy_hash="policy-v2")).governance_receipt_hash,
            evaluate_governance(request(state_version="state-v2")).governance_receipt_hash,
            evaluate_governance(request(enforcement_root_id="root-2")).governance_receipt_hash,
            evaluate_governance(request(decision_receipt_id="receipt-2")).governance_receipt_hash,
        }
        self.assertNotIn(base, variants)
        self.assertEqual(len(variants), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
