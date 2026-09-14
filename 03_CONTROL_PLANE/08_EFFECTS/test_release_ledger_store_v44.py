import tempfile
import unittest
from pathlib import Path

import release_ledger_store_v44 as r


class ReleaseLedgerStoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "ledger.db"
        self.store = r.ReleaseLedgerStore(self.path)
        self.intent = r.EffectIntent("key-1", "digest-1", "tx-1", "auth-1", "Trang Phan")

    def tearDown(self):
        self.tmp.cleanup()

    def test_new_prepare_is_persisted_and_bumps_ledger_version(self):
        start = self.store.identity()
        out = self.store.prepare(self.intent)
        self.assertEqual(out.decision, r.LedgerDecision.PREPARED_NEW)
        self.assertEqual(out.record.state, r.ReleaseState.PREPARED)
        self.assertEqual(out.ledger.version, start.version + 1)
        reopened = r.ReleaseLedgerStore(self.path)
        self.assertEqual(reopened.get_by_key("key-1"), out.record)

    def test_same_key_different_digest_blocks(self):
        self.store.prepare(self.intent)
        out = self.store.prepare(r.EffectIntent("key-1", "digest-X", "tx-1", "auth-1", "Trang Phan"))
        self.assertEqual(out.decision, r.LedgerDecision.BLOCK_EFFECT_IDEMPOTENCY)

    def test_same_digest_different_key_blocks(self):
        self.store.prepare(self.intent)
        out = self.store.prepare(r.EffectIntent("key-X", "digest-1", "tx-1", "auth-1", "Trang Phan"))
        self.assertEqual(out.decision, r.LedgerDecision.BLOCK_EFFECT_IDEMPOTENCY)

    def test_same_key_and_digest_cannot_cross_lineage(self):
        self.store.prepare(self.intent)
        out = self.store.prepare(r.EffectIntent("key-1", "digest-1", "tx-2", "auth-1", "Trang Phan"))
        self.assertEqual(out.decision, r.LedgerDecision.BLOCK_EFFECT_LINEAGE)

    def test_duplicate_prepared_returns_existing_without_version_bump(self):
        first = self.store.prepare(self.intent)
        out = self.store.prepare(self.intent)
        self.assertEqual(out.decision, r.LedgerDecision.PREPARED_EXISTING)
        self.assertEqual(out.ledger.version, first.ledger.version)

    def test_legal_dispatch_commit_requires_receipt_and_is_idempotent_after_commit(self):
        prepared = self.store.prepare(self.intent)
        dispatch = self.store.transition(
            record_id=prepared.record.record_id,
            expected_record_version=1,
            expected_ledger_generation=prepared.ledger.generation,
            expected_ledger_version=prepared.ledger.version,
            to_state=r.ReleaseState.DISPATCHING,
        )
        self.assertEqual(dispatch.decision, r.LedgerDecision.TRANSITIONED)
        no_receipt = self.store.transition(
            record_id=dispatch.record.record_id,
            expected_record_version=dispatch.record.record_version,
            expected_ledger_generation=dispatch.ledger.generation,
            expected_ledger_version=dispatch.ledger.version,
            to_state=r.ReleaseState.COMMITTED,
        )
        self.assertEqual(no_receipt.decision, r.LedgerDecision.BLOCK_EFFECT_LEDGER)
        committed = self.store.transition(
            record_id=dispatch.record.record_id,
            expected_record_version=dispatch.record.record_version,
            expected_ledger_generation=dispatch.ledger.generation,
            expected_ledger_version=dispatch.ledger.version,
            to_state=r.ReleaseState.COMMITTED,
            committed_receipt="receipt-1",
        )
        self.assertEqual(committed.record.state, r.ReleaseState.COMMITTED)
        duplicate = self.store.prepare(self.intent)
        self.assertEqual(duplicate.decision, r.LedgerDecision.EFFECT_ALREADY_COMMITTED)

    def test_dispatching_duplicate_requires_reconciliation_not_redispatch(self):
        prepared = self.store.prepare(self.intent)
        dispatch = self.store.transition(
            record_id=prepared.record.record_id,
            expected_record_version=1,
            expected_ledger_generation=prepared.ledger.generation,
            expected_ledger_version=prepared.ledger.version,
            to_state=r.ReleaseState.DISPATCHING,
        )
        self.assertEqual(dispatch.record.state, r.ReleaseState.DISPATCHING)
        duplicate = self.store.prepare(self.intent)
        self.assertEqual(duplicate.decision, r.LedgerDecision.RECONCILE_EFFECT)

    def test_externalized_unknown_requires_reconciliation(self):
        p = self.store.prepare(self.intent)
        d = self.store.transition(
            record_id=p.record.record_id,
            expected_record_version=1,
            expected_ledger_generation=p.ledger.generation,
            expected_ledger_version=p.ledger.version,
            to_state=r.ReleaseState.DISPATCHING,
        )
        u = self.store.transition(
            record_id=d.record.record_id,
            expected_record_version=d.record.record_version,
            expected_ledger_generation=d.ledger.generation,
            expected_ledger_version=d.ledger.version,
            to_state=r.ReleaseState.EXTERNALIZED_UNKNOWN,
        )
        self.assertEqual(u.record.state, r.ReleaseState.EXTERNALIZED_UNKNOWN)
        self.assertEqual(self.store.prepare(self.intent).decision, r.LedgerDecision.RECONCILE_EFFECT)

    def test_stale_record_version_fails_cas(self):
        p = self.store.prepare(self.intent)
        d = self.store.transition(
            record_id=p.record.record_id,
            expected_record_version=1,
            expected_ledger_generation=p.ledger.generation,
            expected_ledger_version=p.ledger.version,
            to_state=r.ReleaseState.DISPATCHING,
        )
        stale = self.store.transition(
            record_id=d.record.record_id,
            expected_record_version=1,
            expected_ledger_generation=d.ledger.generation,
            expected_ledger_version=d.ledger.version,
            to_state=r.ReleaseState.COMMITTED,
            committed_receipt="r",
        )
        self.assertEqual(stale.decision, r.LedgerDecision.CAS_MISMATCH)

    def test_stale_ledger_version_fails_cas(self):
        p = self.store.prepare(self.intent)
        stale = self.store.transition(
            record_id=p.record.record_id,
            expected_record_version=1,
            expected_ledger_generation=p.ledger.generation,
            expected_ledger_version=p.ledger.version - 1,
            to_state=r.ReleaseState.DISPATCHING,
        )
        self.assertEqual(stale.decision, r.LedgerDecision.CAS_MISMATCH)

    def test_recreated_generation_forces_revalidation(self):
        p = self.store.prepare(self.intent)
        new_identity = self.store.recreate_generation()
        self.assertGreater(new_identity.generation, p.ledger.generation)
        stale = self.store.transition(
            record_id=p.record.record_id,
            expected_record_version=1,
            expected_ledger_generation=p.ledger.generation,
            expected_ledger_version=p.ledger.version,
            to_state=r.ReleaseState.DISPATCHING,
        )
        self.assertEqual(stale.decision, r.LedgerDecision.REVALIDATE_EFFECT_LEDGER)

    def test_illegal_transition_blocks(self):
        p = self.store.prepare(self.intent)
        out = self.store.transition(
            record_id=p.record.record_id,
            expected_record_version=1,
            expected_ledger_generation=p.ledger.generation,
            expected_ledger_version=p.ledger.version,
            to_state=r.ReleaseState.COMMITTED,
            committed_receipt="receipt-1",
        )
        self.assertEqual(out.decision, r.LedgerDecision.ILLEGAL_TRANSITION)


if __name__ == "__main__":
    unittest.main()
