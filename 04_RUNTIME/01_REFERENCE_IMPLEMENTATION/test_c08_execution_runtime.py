import unittest

from c03_executive_runtime import ExecutiveStatus
from c08_execution_runtime import (
    ExecutionStageRequest,
    ExecutionStageStatus,
    evaluate_execution_stage,
)
from matrix_registry_runtime import AuthorityWitness, Condition


EFFECT_DIGEST = "a" * 64


def authority(*, fresh=True, scope=("effect:stage",), policy_hash="policy", state_version="v1"):
    return AuthorityWitness(
        witness_id="auth-1",
        principal="principal-1",
        scope=scope,
        policy_hash=policy_hash,
        state_version=state_version,
        fresh=fresh,
    )


def request(**overrides):
    base = dict(
        request_id="req-1",
        state_version="v1",
        selected_candidate_id="candidate-1",
        executive_status=ExecutiveStatus.SELECT_PROPOSAL,
        kernel_condition=Condition.ACTIVE,
        effect_digest=EFFECT_DIGEST,
        idempotency_key="idem-1",
        transaction_id="tx-1",
        authority=authority(),
        required_scope="effect:stage",
        policy_hash="policy",
        observed_epoch="e1",
        required_epoch="e1",
        input_schema_hash="in",
        expected_input_schema_hash="in",
        output_schema_hash="out",
        expected_output_schema_hash="out",
        provenance_ids=("prov-1",),
        unknown_gaps=(),
    )
    base.update(overrides)
    return ExecutionStageRequest(**base)


class ExecutionStageTests(unittest.TestCase):
    def test_valid_request_stages_but_never_externalizes(self):
        first = evaluate_execution_stage(request())
        second = evaluate_execution_stage(request())
        self.assertEqual(first.status, ExecutionStageStatus.STAGE_EFFECT)
        self.assertIsNotNone(first.staged_intent)
        self.assertEqual(first.staged_intent.intent_hash, second.staged_intent.intent_hash)
        self.assertFalse(first.staged_intent.dispatched)
        self.assertFalse(first.staged_intent.externalized)
        self.assertTrue(first.requires_infrastructure_commit)

    def test_nonselected_executive_output_is_blocked(self):
        result = evaluate_execution_stage(request(executive_status=ExecutiveStatus.HOLD_COMPETING))
        self.assertEqual(result.status, ExecutionStageStatus.BLOCK_EXECUTIVE)
        self.assertIsNone(result.staged_intent)

    def test_stale_or_invalid_authority_blocks(self):
        self.assertEqual(
            evaluate_execution_stage(request(authority=authority(fresh=False))).status,
            ExecutionStageStatus.BLOCK_AUTHORITY,
        )
        self.assertEqual(
            evaluate_execution_stage(request(authority=authority(scope=("other",)))).status,
            ExecutionStageStatus.BLOCK_AUTHORITY,
        )
        self.assertEqual(
            evaluate_execution_stage(request(authority=authority(policy_hash="other"))).status,
            ExecutionStageStatus.BLOCK_AUTHORITY,
        )
        self.assertEqual(
            evaluate_execution_stage(request(authority=authority(state_version="v0"))).status,
            ExecutionStageStatus.BLOCK_AUTHORITY,
        )

    def test_kernel_conditions_are_fail_closed(self):
        self.assertEqual(
            evaluate_execution_stage(request(kernel_condition=Condition.STALE)).status,
            ExecutionStageStatus.REVALIDATE_STALE,
        )
        self.assertEqual(
            evaluate_execution_stage(request(kernel_condition=Condition.COMPETING)).status,
            ExecutionStageStatus.HOLD_COMPETING,
        )
        self.assertEqual(
            evaluate_execution_stage(request(kernel_condition=Condition.QUARANTINED)).status,
            ExecutionStageStatus.BLOCK_KERNEL,
        )
        self.assertEqual(
            evaluate_execution_stage(request(kernel_condition=Condition.FALSIFIED)).status,
            ExecutionStageStatus.BLOCK_KERNEL,
        )

    def test_schema_epoch_and_unknown_gap_block_staging(self):
        self.assertEqual(
            evaluate_execution_stage(request(expected_input_schema_hash="other")).status,
            ExecutionStageStatus.BLOCK_SCHEMA_DRIFT,
        )
        self.assertEqual(
            evaluate_execution_stage(request(observed_epoch="old")).status,
            ExecutionStageStatus.REVALIDATE_STALE,
        )
        self.assertEqual(
            evaluate_execution_stage(request(unknown_gaps=("gap",))).status,
            ExecutionStageStatus.HOLD_UNKNOWN,
        )

    def test_effect_digest_domain_is_strict(self):
        with self.assertRaises(ValueError):
            request(effect_digest="not-a-sha")
        with self.assertRaises(ValueError):
            request(effect_digest="A" * 64)

    def test_intent_hash_binds_effect_identity_and_authority(self):
        base = evaluate_execution_stage(request()).staged_intent.intent_hash
        changed_key = evaluate_execution_stage(request(idempotency_key="idem-2")).staged_intent.intent_hash
        changed_tx = evaluate_execution_stage(request(transaction_id="tx-2")).staged_intent.intent_hash
        changed_auth = evaluate_execution_stage(
            request(authority=AuthorityWitness(
                witness_id="auth-2",
                principal="principal-1",
                scope=("effect:stage",),
                policy_hash="policy",
                state_version="v1",
                fresh=True,
            ))
        ).staged_intent.intent_hash
        self.assertEqual(len({base, changed_key, changed_tx, changed_auth}), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
