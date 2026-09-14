import importlib.util
import json
import tempfile
import unittest
import sys
from pathlib import Path

P = Path(__file__).parents[1] / "17_OBSERVABILITY" / "agent_trace_runtime.py"
spec = importlib.util.spec_from_file_location("agent_trace_runtime", P)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class TraceRuntimeTests(unittest.TestCase):
    def setUp(self):
        f = tempfile.NamedTemporaryFile(suffix=".sqlite3", delete=False)
        f.close()
        self.store = mod.AgentTraceStore(f.name)

    def tearDown(self):
        self.store.close()

    def root(self, **kw):
        args = dict(kind="WORKFLOW", name="wf", subject="s", provenance_root="p", environment="test")
        args.update(kw)
        return self.store.start_span(**args)

    def test_metadata_only_default_hashes_but_does_not_store_content(self):
        r = self.root(input_value={"prompt":"hello","api_key":"secret"})
        self.store.end_span(r, status="OK", output_value={"answer":"world"})
        s = self.store.trace(r.trace_id)[0]
        self.assertIsNotNone(s["input_hash"])
        self.assertIsNone(s["input_redacted_json"])
        self.assertIsNone(s["output_redacted_json"])

    def test_explicit_content_capture_redacts_secrets(self):
        r = self.root(capture_mode="REDACTED_CONTENT", input_value={"authorization":"Bearer abc.def.ghi","x":"sk-1234567890abcdef"})
        self.store.end_span(r, status="OK", output_value={"token":"raw", "text":"Bearer zzz.yyy.xxx"})
        s = self.store.trace(r.trace_id)[0]
        self.assertIn("[REDACTED]", s["input_redacted_json"])
        self.assertNotIn("abc.def.ghi", s["input_redacted_json"])
        self.assertNotIn('"raw"', s["output_redacted_json"])

    def test_parent_child_topology(self):
        root = self.root()
        child = self.store.start_span(kind="TOOL", name="read", subject="tool", provenance_root="p", environment="test", trace_id=root.trace_id, parent_span_id=root.span_id)
        self.store.end_span(child, status="OK")
        self.store.end_span(root, status="OK")
        spans = self.store.trace(root.trace_id)
        self.assertEqual(spans[1]["parent_span_id"], root.span_id)

    def test_orphan_parent_rejected(self):
        with self.assertRaises(mod.TraceContractError):
            self.store.start_span(kind="TOOL", name="x", subject="s", provenance_root="p", environment="e", trace_id="t", parent_span_id="missing")

    def test_cross_trace_parent_rejected(self):
        root = self.root()
        with self.assertRaises(mod.TraceContractError):
            self.store.start_span(kind="TOOL", name="x", subject="s", provenance_root="p", environment="e", trace_id="other", parent_span_id=root.span_id)

    def test_terminal_parent_rejects_late_child(self):
        root = self.root()
        self.store.end_span(root, status="OK")
        with self.assertRaises(mod.TraceContractError):
            self.store.start_span(kind="TOOL", name="x", subject="s", provenance_root="p", environment="e", trace_id=root.trace_id, parent_span_id=root.span_id)

    def test_effect_state_is_observation_not_authority(self):
        root = self.root()
        e = self.store.start_span(kind="EFFECT", name="commit", subject="target", provenance_root="p", environment="e", trace_id=root.trace_id, parent_span_id=root.span_id, authority_ref="auth-17", effect_state="PROPOSED")
        self.store.end_span(e, status="OK", effect_state="COMMITTED")
        self.store.end_span(root, status="OK")
        receipt = self.store.receipt(root.trace_id)
        self.assertEqual(receipt["authority_semantics"], "OBSERVED_REFERENCE_ONLY")
        self.assertIn("COMMITTED", receipt["effect_states"])

    def test_in_doubt_effect_dominates_receipt_status(self):
        root = self.root()
        e = self.store.start_span(kind="EFFECT", name="send", subject="target", provenance_root="p", environment="e", trace_id=root.trace_id, parent_span_id=root.span_id, effect_state="PROPOSED")
        self.store.end_span(e, status="IN_DOUBT", effect_state="IN_DOUBT")
        self.store.end_span(root, status="OK")
        self.assertEqual(self.store.receipt(root.trace_id)["status"], "IN_DOUBT")

    def test_coverage_missingness_is_first_class(self):
        root = self.root()
        self.store.record_coverage(root.trace_id, "tool", expected=3, captured=2, dropped=1, reason="buffer_overflow")
        self.store.end_span(root, status="OK")
        receipt = self.store.receipt(root.trace_id)
        self.assertFalse(receipt["coverage_complete"])
        self.assertEqual(receipt["coverage"][0]["dropped_reason"], "buffer_overflow")

    def test_event_time_distinct_from_observation_time(self):
        root = self.root(event_time=10.0)
        s = self.store.trace(root.trace_id)[0]
        self.assertEqual(s["event_time"], 10.0)
        self.assertGreater(s["observed_at"], 10.0)

    def test_ledger_tamper_detected(self):
        root = self.root()
        self.store.end_span(root, status="OK")
        self.assertEqual(self.store.verify_integrity(), [])
        self.store.db.execute("UPDATE ledger SET payload_json='{}' WHERE seq=1")
        self.store.db.commit()
        self.assertTrue(self.store.verify_integrity())

    def test_otel_projection_keeps_amos_extensions_explicit(self):
        root = self.root()
        self.store.end_span(root, status="OK")
        p = self.store.otel_projection(root.trace_id)[0]
        self.assertEqual(p["attributes"]["amos.span.kind"], "WORKFLOW")
        self.assertIn("amos.provenance.root", p["attributes"])


if __name__ == "__main__":
    unittest.main()
