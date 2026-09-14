from dataclasses import replace
import unittest

from c09_kernel_control_runtime import (
    KernelControlRequest,
    KernelControlStatus,
    evaluate_kernel_control,
)
from matrix_registry_runtime import AuthorityWitness, Condition


class C09KernelControlTests(unittest.TestCase):
    def request(self, **changes):
        base = KernelControlRequest(
            request_id="req-1",
            operation="evaluate",
            state_version="state-v1",
            provenance_ids=("src:canon", "obs:test"),
            input_schema_hash="in-v1",
            expected_input_schema_hash="in-v1",
            output_schema_hash="out-v1",
            expected_output_schema_hash="out-v1",
            observed_epoch="epoch-7",
            required_epoch="epoch-7",
        )
        return replace(base, **changes)

    def authority(self, **changes):
        base = AuthorityWitness(
            witness_id="c01-witness-1",
            principal="governance",
            scope=("effect:write",),
            policy_hash="policy-v1",
            state_version="state-v1",
            fresh=True,
        )
        return replace(base, **changes)

    def test_non_effect_validates_bounded_without_commit_authority(self):
        result = evaluate_kernel_control(self.request())
        self.assertEqual(result.status, KernelControlStatus.VALIDATED_BOUNDED)
        self.assertFalse(result.commits_effect)
        self.assertEqual(result.provenance_ids, ("src:canon", "obs:test"))

    def test_unprovenanced_request_is_rejected_before_output(self):
        with self.assertRaises(ValueError):
            self.request(provenance_ids=())

    def test_input_or_output_schema_drift_fails_closed(self):
        for changes in (
            {"input_schema_hash": "in-v2"},
            {"output_schema_hash": "out-v2"},
        ):
            with self.subTest(changes=changes):
                result = evaluate_kernel_control(self.request(**changes))
                self.assertEqual(result.status, KernelControlStatus.BLOCK_SCHEMA_DRIFT)
                self.assertFalse(result.commits_effect)

    def test_stale_epoch_or_condition_requires_revalidation(self):
        cases = (
            self.request(observed_epoch="epoch-6"),
            self.request(upstream_condition=Condition.STALE),
        )
        for request in cases:
            with self.subTest(request=request):
                result = evaluate_kernel_control(request)
                self.assertEqual(result.status, KernelControlStatus.REVALIDATE_STALE)

    def test_competing_state_is_preserved_not_collapsed(self):
        result = evaluate_kernel_control(
            self.request(upstream_condition=Condition.COMPETING)
        )
        self.assertEqual(result.status, KernelControlStatus.HOLD_COMPETING)
        self.assertNotEqual(result.status, KernelControlStatus.VALIDATED_BOUNDED)

    def test_quarantined_or_falsified_upstream_is_blocked(self):
        for condition in (Condition.QUARANTINED, Condition.FALSIFIED):
            with self.subTest(condition=condition):
                result = evaluate_kernel_control(
                    self.request(upstream_condition=condition)
                )
                self.assertEqual(result.status, KernelControlStatus.BLOCK_UPSTREAM)

    def test_unknown_gap_never_becomes_pass(self):
        result = evaluate_kernel_control(
            self.request(unknown_gaps=("equation-proof-missing",))
        )
        self.assertEqual(result.status, KernelControlStatus.HOLD_UNKNOWN)
        self.assertNotEqual(result.status, KernelControlStatus.VALIDATED_BOUNDED)

    def test_effect_without_c01_authority_is_blocked(self):
        request = self.request(
            effect_requested=True,
            effect_scope="effect:write",
            policy_hash="policy-v1",
        )
        result = evaluate_kernel_control(request)
        self.assertEqual(result.status, KernelControlStatus.BLOCK_AUTHORITY)
        self.assertFalse(result.commits_effect)

    def test_wrong_policy_or_stale_authority_is_blocked(self):
        request = self.request(
            effect_requested=True,
            effect_scope="effect:write",
            policy_hash="policy-v1",
        )
        cases = (
            self.authority(policy_hash="policy-other"),
            self.authority(fresh=False),
            self.authority(state_version="state-other"),
        )
        for witness in cases:
            with self.subTest(witness=witness):
                result = evaluate_kernel_control(request, witness)
                self.assertEqual(result.status, KernelControlStatus.BLOCK_AUTHORITY)

    def test_valid_c01_authority_only_forwards_never_commits(self):
        request = self.request(
            effect_requested=True,
            effect_scope="effect:write",
            policy_hash="policy-v1",
        )
        result = evaluate_kernel_control(request, self.authority())
        self.assertEqual(result.status, KernelControlStatus.FORWARD_TO_C01)
        self.assertEqual(result.authority_witness_id, "c01-witness-1")
        self.assertFalse(result.commits_effect)

    def test_effect_metadata_without_effect_request_is_invalid(self):
        with self.assertRaises(ValueError):
            self.request(effect_scope="effect:write")
        with self.assertRaises(ValueError):
            self.request(policy_hash="policy-v1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
