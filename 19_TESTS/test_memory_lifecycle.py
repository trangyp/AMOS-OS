import importlib.util
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "07_SKILLS" / "amos-agent-memory-dynamics-rscf-engine" / "scripts" / "memory_lifecycle.py"
spec = importlib.util.spec_from_file_location("amos_memory_lifecycle", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
assert spec.loader is not None
spec.loader.exec_module(module)

MemoryLifecycleStore = module.MemoryLifecycleStore
MemoryAuthorityError = module.MemoryAuthorityError
MemoryConflictError = module.MemoryConflictError
MemoryStateError = module.MemoryStateError


class MemoryLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "memory.sqlite"
        self.store = MemoryLifecycleStore(self.db)

    def tearDown(self):
        self.store.close()
        self.tmp.cleanup()

    def admit(self, memory_id="m1", content="alpha beta", scope="team:read", **kwargs):
        return self.store.admit(
            memory_id=memory_id,
            namespace="n1",
            content=content,
            provenance_id=kwargs.pop("provenance_id", f"src-{memory_id}"),
            required_scope=scope,
            recorded_at=kwargs.pop("recorded_at", "2026-09-14T00:00:00Z"),
            **kwargs,
        )

    def test_admit_and_retrieve_never_promotes_to_knowledge(self):
        view = self.admit(source_class="SOURCE_CLAIM")
        self.assertEqual(view.epistemic_class, "OBSERVATION")
        self.assertEqual(view.source_class, "SOURCE_CLAIM")

    def test_provenance_is_required(self):
        with self.assertRaises(ValueError):
            self.store.admit(
                memory_id="x",
                namespace="n1",
                content="x",
                provenance_id="",
                required_scope="team:read",
            )

    def test_scope_is_required_for_read(self):
        self.admit()
        with self.assertRaises(MemoryAuthorityError):
            self.store.get("m1", scopes={"other:read"})
        self.assertEqual(self.store.get("m1", scopes={"team:read"}).content, "alpha beta")

    def test_revision_requires_optimistic_version_match(self):
        self.admit()
        self.store.revise(
            memory_id="m1",
            expected_revision=1,
            content="alpha gamma",
            provenance_id="src-2",
            effective_at="2026-09-14T01:00:00Z",
            recorded_at="2026-09-14T01:00:00Z",
        )
        with self.assertRaises(MemoryConflictError):
            self.store.revise(
                memory_id="m1",
                expected_revision=1,
                content="stale write",
                provenance_id="src-stale",
            )

    def test_temporal_history_returns_prior_revision(self):
        self.admit()
        self.store.revise(
            memory_id="m1",
            expected_revision=1,
            content="new fact",
            provenance_id="src-2",
            effective_at="2026-09-14T01:00:00Z",
            recorded_at="2026-09-14T01:00:00Z",
        )
        old = self.store.get(
            "m1", scopes={"team:read"}, as_of="2026-09-14T00:30:00Z"
        )
        new = self.store.get(
            "m1", scopes={"team:read"}, as_of="2026-09-14T01:30:00Z"
        )
        self.assertEqual((old.revision, old.content), (1, "alpha beta"))
        self.assertEqual((new.revision, new.content), (2, "new fact"))

    def test_expired_memory_is_retained_but_hidden_by_default(self):
        self.admit(expires_at="2026-09-14T01:00:00Z")
        with self.assertRaises(MemoryStateError):
            self.store.get(
                "m1", scopes={"team:read"}, as_of="2026-09-14T02:00:00Z"
            )
        visible = self.store.get(
            "m1",
            scopes={"team:read"},
            as_of="2026-09-14T02:00:00Z",
            include_expired=True,
        )
        self.assertEqual(visible.content, "alpha beta")

    def test_quarantine_excludes_memory_from_retrieval(self):
        self.admit()
        self.store.quarantine("m1", expected_revision=1, reason="conflict")
        self.assertEqual(
            self.store.search(namespace="n1", query="alpha", scopes={"team:read"}), []
        )
        with self.assertRaises(MemoryStateError):
            self.store.get("m1", scopes={"team:read"})

    def test_tombstone_preserves_lineage_and_blocks_normal_read(self):
        self.admit()
        self.store.tombstone("m1", expected_revision=1, reason="superseded")
        with self.assertRaises(MemoryStateError):
            self.store.get("m1", scopes={"team:read"})
        historical = self.store.get(
            "m1", scopes={"team:read"}, include_tombstoned=True
        )
        self.assertEqual(historical.content, "alpha beta")
        events = [e["event_type"] for e in self.store.events("m1")]
        self.assertEqual(events, ["ADMIT", "TOMBSTONE"])

    def test_declared_conflict_quarantines_both_without_choosing_truth(self):
        self.admit("m1", "sky is blue")
        self.admit("m2", "sky is green")
        conflict_id = self.store.declare_conflict(
            left_memory_id="m1",
            left_expected_revision=1,
            right_memory_id="m2",
            right_expected_revision=1,
            reason="incompatible source claims",
            recorded_at="2026-09-14T02:00:00Z",
        )
        self.assertTrue(conflict_id.startswith("conf-"))
        for mid in ("m1", "m2"):
            with self.assertRaises(MemoryStateError):
                self.store.get(mid, scopes={"team:read"})

    def test_search_score_is_relevance_not_epistemic_promotion(self):
        self.admit("m1", "alpha beta")
        self.admit("m2", "alpha gamma")
        out = self.store.search(namespace="n1", query="alpha", scopes={"team:read"})
        self.assertEqual(len(out), 2)
        self.assertTrue(all(v.epistemic_class == "OBSERVATION" for v in out))
        self.assertTrue(all(v.retrieval_score == 1.0 for v in out))

    def test_context_snapshot_is_reproducible_and_marks_stale_revision(self):
        self.admit("m1", "alpha beta")
        snap = self.store.assemble_context(
            namespace="n1",
            query="alpha",
            scopes={"team:read"},
            max_chars=100,
            as_of="2026-09-14T00:30:00Z",
        )
        self.store.revise(
            memory_id="m1",
            expected_revision=1,
            content="alpha gamma",
            provenance_id="src-2",
            effective_at="2026-09-14T01:00:00Z",
            recorded_at="2026-09-14T01:00:00Z",
        )
        replay = self.store.replay_context_snapshot(
            snap["snapshot_id"], scopes={"team:read"}
        )
        self.assertTrue(replay["snapshot_stale"])
        self.assertEqual(replay["memories"][0]["content"], "alpha beta")
        self.assertEqual(replay["memories"][0]["epistemic_class"], "OBSERVATION")

    def test_context_snapshot_replay_fails_closed_after_quarantine(self):
        self.admit("m1", "alpha beta")
        snap = self.store.assemble_context(
            namespace="n1",
            query="alpha",
            scopes={"team:read"},
            max_chars=100,
            as_of="2026-09-14T00:30:00Z",
        )
        self.store.quarantine("m1", expected_revision=1, reason="new conflict")
        with self.assertRaises(MemoryStateError):
            self.store.replay_context_snapshot(
                snap["snapshot_id"], scopes={"team:read"}
            )

    def test_integrity_detects_revision_content_tamper(self):
        self.admit()
        self.store.conn.execute(
            "UPDATE memory_revisions SET content = 'tampered' WHERE memory_id = 'm1' AND revision = 1"
        )
        self.store.conn.commit()
        result = self.store.verify_integrity()
        self.assertEqual(result["status"], "QUARANTINE")
        self.assertIn("CONTENT_HASH:m1@1", result["issues"])

    def test_integrity_detects_event_chain_tamper(self):
        self.admit()
        self.store.conn.execute(
            "UPDATE memory_events SET payload_json = '{}' WHERE event_id = 1"
        )
        self.store.conn.commit()
        result = self.store.verify_integrity()
        self.assertEqual(result["status"], "QUARANTINE")
        self.assertTrue(any(issue.startswith("EVENT_HASH:") for issue in result["issues"]))

    def test_no_physical_delete_api(self):
        self.assertFalse(hasattr(self.store, "delete"))
        self.assertTrue(hasattr(self.store, "tombstone"))


if __name__ == "__main__":
    unittest.main()
