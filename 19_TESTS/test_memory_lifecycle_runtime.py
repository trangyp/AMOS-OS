import importlib.util
import pathlib
import sys
import tempfile
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "10_MEMORY" / "memory_lifecycle_runtime.py"
spec = importlib.util.spec_from_file_location("amos_memory_runtime", MODULE)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)

MemoryStore = mod.MemoryStore
AuthorityError = mod.AuthorityError
IntegrityError = mod.IntegrityError
ACTIVE = mod.ACTIVE
QUARANTINED = mod.QUARANTINED
SUPERSEDED = mod.SUPERSEDED
EXPIRED = mod.EXPIRED
TOMBSTONED = mod.TOMBSTONED

ALL_WRITE = {"memory.admit", "memory.revise", "memory.quarantine", "memory.expire", "memory.tombstone"}
READ = {"memory.read"}


class MemoryLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = pathlib.Path(self.tmp.name) / "m.db"
        self.s = MemoryStore(self.db)

    def tearDown(self):
        self.s.close()
        self.tmp.cleanup()

    def admit(self, **kw):
        base = dict(scope="project:A", subject="preference", content="Use exact equations",
                    provenance="chat:1", capabilities=ALL_WRITE, now=100.0)
        base.update(kw)
        return self.s.admit(**base)

    def test_admission_is_observation(self):
        r = self.admit()
        self.assertEqual(r.epistemic_class, "OBSERVATION")
        self.assertEqual(r.state, ACTIVE)

    def test_write_requires_authority(self):
        with self.assertRaises(AuthorityError):
            self.s.admit(scope="x", subject="s", content="c", provenance="p", capabilities=set())

    def test_retrieval_scope_isolation(self):
        self.admit(scope="project:A")
        self.admit(scope="project:B", origin_id="o2")
        got = self.s.retrieve(scope="project:A", query="equations", capabilities=READ)
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0].scope, "project:A")

    def test_revision_is_new_version_not_in_place(self):
        r1 = self.admit()
        self.s.revise(r1.memory_id, content="Use verified equations", provenance="chat:2", capabilities=ALL_WRITE, now=110)
        hist = self.s.history(r1.origin_id, capabilities=READ)
        self.assertEqual([x.version for x in hist], [1, 2])
        self.assertEqual(hist[0].state, SUPERSEDED)
        self.assertEqual(hist[1].state, ACTIVE)

    def test_quarantine_excluded_from_default_retrieval(self):
        r = self.admit()
        self.s.quarantine(r.memory_id, reason="conflict", capabilities=ALL_WRITE, now=101)
        self.assertEqual(self.s.retrieve(scope="project:A", query="equations", capabilities=READ), [])
        self.assertEqual(self.s.get(r.memory_id, capabilities=READ, include_nonactive=True).state, QUARANTINED)

    def test_expire_and_tombstone_states(self):
        r = self.admit()
        self.s.expire(r.memory_id, reason="stale", capabilities=ALL_WRITE, now=101)
        self.assertEqual(self.s.get(r.memory_id, capabilities=READ, include_nonactive=True).state, EXPIRED)
        self.s.tombstone(r.memory_id, reason="superseded elsewhere", capabilities=ALL_WRITE, now=102)
        self.assertEqual(self.s.get(r.memory_id, capabilities=READ, include_nonactive=True).state, TOMBSTONED)

    def test_bitemporal_validity(self):
        self.admit(valid_from=10, valid_to=20)
        self.assertEqual(len(self.s.retrieve(scope="project:A", query="equations", capabilities=READ, valid_at=15)), 1)
        self.assertEqual(len(self.s.retrieve(scope="project:A", query="equations", capabilities=READ, valid_at=25)), 0)

    def test_recorded_at_cutoff(self):
        r1 = self.admit(now=100)
        self.s.revise(r1.memory_id, content="new", provenance="chat:2", capabilities=ALL_WRITE, now=200)
        old = self.s.retrieve(scope="project:A", query="equations", capabilities=READ, recorded_at=150, include_nonactive=True)
        self.assertEqual(len(old), 1)
        self.assertEqual(old[0].version, 1)

    def test_context_never_promotes_to_truth(self):
        self.admit()
        ctx = self.s.assemble_context(scope="project:A", query="equations", capabilities=READ)
        self.assertEqual(ctx[0]["epistemic_class"], "OBSERVATION")

    def test_identical_content_can_be_distinct_memories(self):
        a = self.admit(origin_id="o1")
        b = self.admit(origin_id="o2")
        self.assertNotEqual(a.memory_id, b.memory_id)
        self.assertEqual(a.content_hash, b.content_hash)

    def test_integrity_detects_content_tamper(self):
        r = self.admit()
        self.s.db.execute("UPDATE memories SET content='tampered' WHERE memory_id=?", (r.memory_id,))
        self.s.db.commit()
        with self.assertRaises(IntegrityError):
            self.s.verify_integrity()

    def test_integrity_detects_ledger_tamper(self):
        self.admit()
        self.s.db.execute("UPDATE ledger SET payload='{}' WHERE seq=1")
        self.s.db.commit()
        with self.assertRaises(IntegrityError):
            self.s.verify_integrity()


if __name__ == "__main__":
    unittest.main(verbosity=2)
