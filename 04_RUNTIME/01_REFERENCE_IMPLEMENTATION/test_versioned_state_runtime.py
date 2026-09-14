import unittest

import versioned_state_runtime as s


class VersionedStateRuntimeTests(unittest.TestCase):
    def test_cas_succeeds_only_on_exact_version(self):
        store = s.MVCCStateStore({"x": 1})
        self.assertFalse(store.compare_and_swap("x", 1, 2))
        self.assertEqual(store.get("x"), s.VersionedValue(1, 0))
        self.assertTrue(store.compare_and_swap("x", 0, 2))
        self.assertEqual(store.get("x"), s.VersionedValue(2, 1))
        self.assertEqual(store.epochs.state_epoch, 1)

    def test_snapshot_is_not_current_after_mutation(self):
        store = s.MVCCStateStore({"x": "a"})
        snap = store.snapshot(("x",))
        self.assertTrue(store.compare_and_swap("x", 0, "b"))
        self.assertEqual(snap.values["x"].value, "a")
        self.assertEqual(store.get("x").value, "b")
        self.assertNotEqual(snap.epochs, store.epochs)

    def test_transaction_preflight_is_atomic_on_conflict(self):
        store = s.MVCCStateStore({"a": 1, "b": 2})
        epochs = store.epochs
        self.assertTrue(store.compare_and_swap("b", 0, 3))
        tx = s.StateTransaction(
            "tx-conflict",
            {"a": 0, "b": 0},
            (
                s.WriteIntent("a", 0, 10),
                s.WriteIntent("b", 0, 20),
            ),
            store.epochs,
        )
        receipt = store.commit(tx)
        self.assertEqual(receipt.status, s.CommitStatus.CONFLICT)
        self.assertEqual(store.get("a"), s.VersionedValue(1, 0))
        self.assertEqual(store.get("b"), s.VersionedValue(3, 1))
        self.assertNotEqual(epochs, store.epochs)

    def test_successful_multiwrite_advances_versions_and_state_epoch_once(self):
        store = s.MVCCStateStore({"a": 1, "b": 2})
        before = store.epochs
        tx = s.StateTransaction(
            "tx-ok",
            {"a": 0, "b": 0},
            (s.WriteIntent("a", 0, 10), s.WriteIntent("b", 0, 20)),
            before,
        )
        receipt = store.commit(tx)
        self.assertEqual(receipt.status, s.CommitStatus.COMMITTED)
        self.assertEqual(store.get("a"), s.VersionedValue(10, 1))
        self.assertEqual(store.get("b"), s.VersionedValue(20, 1))
        self.assertEqual(store.epochs.state_epoch, before.state_epoch + 1)
        self.assertEqual(store.epochs.causal_epoch, before.causal_epoch)
        self.assertEqual(store.epochs.policy_epoch, before.policy_epoch)
        self.assertEqual(store.epochs.provenance_epoch, before.provenance_epoch)

    def test_stale_epoch_blocks_transaction_even_when_versions_match(self):
        store = s.MVCCStateStore({"x": 1})
        old = store.epochs
        store.advance_nonstate_epochs(policy_epoch=1)
        tx = s.StateTransaction("tx-stale-epoch", {"x": 0}, (s.WriteIntent("x", 0, 2),), old)
        receipt = store.commit(tx)
        self.assertEqual(receipt.status, s.CommitStatus.EPOCH_MISMATCH)
        self.assertEqual(store.get("x"), s.VersionedValue(1, 0))

    def test_nonstate_epochs_are_distinct_and_explicit(self):
        store = s.MVCCStateStore({"x": 1})
        store.advance_nonstate_epochs(causal_epoch=3, policy_epoch=5, provenance_epoch=7)
        self.assertEqual(store.epochs, s.EpochVector(0, 3, 5, 7))
        self.assertTrue(store.compare_and_swap("x", 0, 2))
        self.assertEqual(store.epochs, s.EpochVector(1, 3, 5, 7))
        with self.assertRaises(ValueError):
            store.advance_nonstate_epochs(policy_epoch=4)

    def test_external_effect_transaction_is_refused_by_state_kernel(self):
        store = s.MVCCStateStore({"x": 1})
        tx = s.StateTransaction(
            "tx-effect",
            {"x": 0},
            (s.WriteIntent("x", 0, 2),),
            store.epochs,
            external_effects=True,
        )
        receipt = store.commit(tx)
        self.assertEqual(receipt.status, s.CommitStatus.EXTERNAL_AUTHORITY_REQUIRED)
        self.assertEqual(store.get("x"), s.VersionedValue(1, 0))

    def test_transaction_replay_is_idempotent(self):
        store = s.MVCCStateStore({"x": 1})
        tx = s.StateTransaction("tx-replay", {"x": 0}, (s.WriteIntent("x", 0, 2),), store.epochs)
        first = store.commit(tx)
        second = store.commit(tx)
        self.assertEqual(first, second)
        self.assertEqual(store.get("x"), s.VersionedValue(2, 1))

    def test_transaction_id_reuse_with_different_payload_is_rejected(self):
        store = s.MVCCStateStore({"x": 1})
        epochs = store.epochs
        first = s.StateTransaction("tx-id", {"x": 0}, (s.WriteIntent("x", 0, 2),), epochs)
        store.commit(first)
        different = s.StateTransaction("tx-id", {"x": 1}, (s.WriteIntent("x", 1, 3),), store.epochs)
        with self.assertRaises(ValueError):
            store.commit(different)

    def test_new_key_uses_zero_as_absent_expected_version(self):
        store = s.MVCCStateStore()
        self.assertFalse(store.compare_and_swap("x", 1, "a"))
        self.assertTrue(store.compare_and_swap("x", 0, "a"))
        self.assertEqual(store.get("x"), s.VersionedValue("a", 1))


if __name__ == "__main__":
    unittest.main()
