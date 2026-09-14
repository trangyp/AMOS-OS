from dataclasses import dataclass
import unittest

from memory_lifecycle_runtime import MemoryLifecycleStore, MemoryOperationError, MemoryState


@dataclass(frozen=True)
class Auth:
    witness_id: str = "auth-1"
    scope: tuple[str, ...] = ()
    state_version: str = "v1"
    fresh: bool = True


def auth(*caps: str, fresh: bool = True, state_version: str = "v1") -> Auth:
    return Auth(scope=tuple(caps), fresh=fresh, state_version=state_version)


T0 = "2026-09-14T12:00:00+00:00"
T1 = "2026-09-14T13:00:00+00:00"
T2 = "2026-09-14T14:00:00+00:00"


class MemoryLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.store = MemoryLifecycleStore()

    def tearDown(self):
        self.store.close()

    def admit(self, memory_id="m1", content="alpha", scope="s1"):
        return self.store.admit(
            authority=auth(f"memory:admit:{scope}"),
            state_version="v1",
            memory_id=memory_id,
            origin_id="origin-1",
            scope=scope,
            content=content,
            valid_from=T0,
            valid_to=None,
            recorded_at=T1,
            provenance_ids=("prov-1",),
        )

    def test_admit_and_read_return_observation_not_knowledge(self):
        record = self.admit()
        self.assertEqual(record.version, 1)
        self.assertEqual(record.state, MemoryState.ACTIVE)
        self.assertEqual(record.epistemic_class, "OBSERVATION")
        read = self.store.get(
            authority=auth("memory:read:s1"), state_version="v1", memory_id="m1"
        )
        self.assertEqual(read.content, "alpha")
        self.assertEqual(self.store.verify_integrity(), ())

    def test_same_content_hash_does_not_collapse_memory_identity(self):
        a = self.admit("m1", "same")
        b = self.admit("m2", "same")
        self.assertEqual(a.content_hash, b.content_hash)
        self.assertNotEqual(a.memory_id, b.memory_id)

    def test_revision_creates_new_version_and_preserves_old_content(self):
        self.admit()
        revised = self.store.revise(
            authority=auth("memory:revise:s1"), state_version="v1", memory_id="m1",
            expected_version=1, content="beta", valid_from=T0, valid_to=None,
            recorded_at=T2, provenance_ids=("prov-2",),
        )
        self.assertEqual(revised.version, 2)
        self.assertEqual(revised.predecessor_version, 1)
        old = self.store.get(
            authority=auth("memory:forensic:s1"), state_version="v1", memory_id="m1", version=1, forensic=True
        )
        self.assertEqual(old.state, MemoryState.SUPERSEDED)
        self.assertEqual(old.content, "alpha")
        with self.assertRaises(MemoryOperationError):
            self.store.revise(
                authority=auth("memory:revise:s1"), state_version="v1", memory_id="m1",
                expected_version=1, content="stale", valid_from=T0, valid_to=None,
                recorded_at=T2, provenance_ids=("prov-3",),
            )

    def test_quarantine_is_excluded_from_default_retrieval(self):
        self.admit()
        quarantined = self.store.transition(
            authority=auth("memory:quarantine:s1"), state_version="v1", memory_id="m1",
            expected_version=1, target=MemoryState.QUARANTINED, recorded_at=T2,
        )
        self.assertEqual(quarantined.state, MemoryState.QUARANTINED)
        with self.assertRaises(MemoryOperationError):
            self.store.get(authority=auth("memory:read:s1"), state_version="v1", memory_id="m1")
        forensic = self.store.get(
            authority=auth("memory:forensic:s1"), state_version="v1", memory_id="m1", forensic=True
        )
        self.assertEqual(forensic.state, MemoryState.QUARANTINED)

    def test_expired_and_tombstoned_lineage_remain_forensic(self):
        for target in (MemoryState.EXPIRED, MemoryState.TOMBSTONED):
            store = MemoryLifecycleStore()
            try:
                store.admit(
                    authority=auth("memory:admit:s1"), state_version="v1", memory_id="m", origin_id="o",
                    scope="s1", content="x", valid_from=T0, valid_to=None, recorded_at=T1,
                    provenance_ids=("p",),
                )
                cap = "expire" if target is MemoryState.EXPIRED else "tombstone"
                store.transition(
                    authority=auth(f"memory:{cap}:s1"), state_version="v1", memory_id="m",
                    expected_version=1, target=target, recorded_at=T2,
                )
                forensic = store.get(
                    authority=auth("memory:forensic:s1"), state_version="v1", memory_id="m", forensic=True
                )
                self.assertEqual(forensic.state, target)
            finally:
                store.close()

    def test_event_valid_time_is_distinct_from_recorded_time(self):
        record = self.store.admit(
            authority=auth("memory:admit:s1"), state_version="v1", memory_id="m1", origin_id="o",
            scope="s1", content="x", valid_from=T0, valid_to=T1, recorded_at=T2,
            provenance_ids=("p",),
        )
        self.assertTrue(record.context_eligible("2026-09-14T12:30:00+00:00"))
        self.assertFalse(record.context_eligible("2026-09-14T13:30:00+00:00"))
        self.assertEqual(record.recorded_at, T2)

    def test_authority_scope_and_freshness_fail_closed(self):
        with self.assertRaises(MemoryOperationError):
            self.store.admit(
                authority=auth("memory:read:s1"), state_version="v1", memory_id="m1", origin_id="o",
                scope="s1", content="x", valid_from=T0, valid_to=None, recorded_at=T1,
                provenance_ids=("p",),
            )
        with self.assertRaises(MemoryOperationError):
            self.store.admit(
                authority=auth("memory:admit:s1", fresh=False), state_version="v1", memory_id="m1", origin_id="o",
                scope="s1", content="x", valid_from=T0, valid_to=None, recorded_at=T1,
                provenance_ids=("p",),
            )

    def test_integrity_detects_content_and_event_tampering(self):
        self.admit()
        self.assertEqual(self.store.verify_integrity(), ())
        self.store.conn.execute("UPDATE memory_versions SET content='tampered' WHERE memory_id='m1' AND version=1")
        self.store.conn.execute("UPDATE memory_events SET event_hash='bad' WHERE seq=1")
        failures = self.store.verify_integrity()
        self.assertTrue(any(item.startswith("CONTENT_HASH:") for item in failures))
        self.assertTrue(any(item.startswith("EVENT_CHAIN:") for item in failures))

    def test_time_and_transition_domains_fail_closed(self):
        with self.assertRaises(ValueError):
            self.store.admit(
                authority=auth("memory:admit:s1"), state_version="v1", memory_id="m1", origin_id="o",
                scope="s1", content="x", valid_from="2026-09-14T12:00:00", valid_to=None,
                recorded_at=T1, provenance_ids=("p",),
            )
        self.admit()
        with self.assertRaises(MemoryOperationError):
            self.store.transition(
                authority=auth("memory:quarantine:s1"), state_version="v1", memory_id="m1",
                expected_version=1, target=MemoryState.SUPERSEDED, recorded_at=T2,
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
