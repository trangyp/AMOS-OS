from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "04_RUNTIME" / "01_REFERENCE_IMPLEMENTATION" / "durable_workflow_runtime.py"
spec = importlib.util.spec_from_file_location("durable_runtime", MODULE)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)

AmbiguousEffect = mod.AmbiguousEffect
DurableWorkflowStore = mod.DurableWorkflowStore
IntegrityViolation = mod.IntegrityViolation
ReplayDivergence = mod.ReplayDivergence
StepKind = mod.StepKind
VersionMismatch = mod.VersionMismatch
WorkflowError = mod.WorkflowError


class DurableWorkflowRuntimeTests(unittest.TestCase):
    def make_db(self) -> Path:
        tmp = tempfile.NamedTemporaryFile(suffix=".sqlite3", delete=False)
        tmp.close()
        return Path(tmp.name)

    def test_pure_step_receipt_prevents_reexecution(self):
        db = self.make_db()
        store = DurableWorkflowStore(db)
        ref = store.start("wf-pure", "v1", {"n": 1})
        calls = {"n": 0}

        def pure(x):
            calls["n"] += 1
            return {"y": x["x"] + 1}

        self.assertEqual(
            store.execute_step(ref, "s1", StepKind.PURE, {"x": 2}, pure),
            {"y": 3},
        )
        self.assertEqual(
            store.execute_step(ref, "s1", StepKind.PURE, {"x": 2}, pure),
            {"y": 3},
        )
        self.assertEqual(calls["n"], 1)
        store.close()

    def test_pure_started_step_can_retry_after_restart(self):
        db = self.make_db()
        store = DurableWorkflowStore(db)
        ref = store.start("wf-pure-retry", "v1", {})
        with self.assertRaises(WorkflowError):
            store.execute_step(
                ref,
                "s1",
                StepKind.PURE,
                {"x": 1},
                lambda x: x,
                simulate_interrupt_after_start=True,
            )
        store.close()

        store = DurableWorkflowStore(db)
        out = store.execute_step(
            ref,
            "s1",
            StepKind.PURE,
            {"x": 1},
            lambda x: {"ok": True},
        )
        self.assertEqual(out, {"ok": True})
        self.assertEqual(store.snapshot(ref)["steps"][0]["attempt"], 2)
        store.close()

    def test_effect_requires_explicit_key(self):
        db = self.make_db()
        store = DurableWorkflowStore(db)
        ref = store.start("wf-effect-key", "v1", {})
        with self.assertRaises(ValueError):
            store.execute_step(
                ref,
                "charge",
                StepKind.EFFECT,
                {"amount": 1},
                lambda x: x,
            )
        store.close()

    def test_repeated_identical_effects_are_distinct_without_shared_key(self):
        db = self.make_db()
        store = DurableWorkflowStore(db)
        ref = store.start("wf-repeat", "v1", {})
        calls = {"n": 0}

        def effect(x):
            calls["n"] += 1
            return {"receipt": calls["n"], "payload": x}

        a = store.execute_step(
            ref,
            "e1",
            StepKind.EFFECT,
            {"x": 7},
            effect,
            effect_key="op-1",
        )
        b = store.execute_step(
            ref,
            "e2",
            StepKind.EFFECT,
            {"x": 7},
            effect,
            effect_key="op-2",
        )
        self.assertEqual(calls["n"], 2)
        self.assertNotEqual(a["receipt"], b["receipt"])
        store.close()

    def test_same_effect_key_reuses_receipt(self):
        db = self.make_db()
        store = DurableWorkflowStore(db)
        ref = store.start("wf-idem", "v1", {})
        calls = {"n": 0}

        def effect(x):
            calls["n"] += 1
            return {"receipt": calls["n"], "payload": x}

        first = store.execute_step(
            ref,
            "e1",
            StepKind.EFFECT,
            {"x": 7},
            effect,
            effect_key="external-op",
        )
        second = store.execute_step(
            ref,
            "e2",
            StepKind.EFFECT,
            {"x": 7},
            effect,
            effect_key="external-op",
        )
        self.assertEqual(calls["n"], 1)
        self.assertEqual(first, second)
        store.close()

    def test_same_effect_key_different_input_fails_closed(self):
        db = self.make_db()
        store = DurableWorkflowStore(db)
        ref = store.start("wf-idem-conflict", "v1", {})
        store.execute_step(
            ref,
            "e1",
            StepKind.EFFECT,
            {"x": 7},
            lambda x: x,
            effect_key="external-op",
        )
        with self.assertRaises(ReplayDivergence):
            store.execute_step(
                ref,
                "e2",
                StepKind.EFFECT,
                {"x": 8},
                lambda x: x,
                effect_key="external-op",
            )
        store.close()

    def test_interrupted_effect_becomes_ambiguous_and_requires_reconciliation(self):
        db = self.make_db()
        store = DurableWorkflowStore(db)
        ref = store.start("wf-ambiguous", "v1", {})
        with self.assertRaises(WorkflowError):
            store.execute_step(
                ref,
                "send",
                StepKind.EFFECT,
                {"msg": "x"},
                lambda x: {"ok": True},
                effect_key="send-1",
                simulate_interrupt_after_start=True,
            )
        store.close()

        store = DurableWorkflowStore(db)
        with self.assertRaises(AmbiguousEffect):
            store.execute_step(
                ref,
                "send",
                StepKind.EFFECT,
                {"msg": "x"},
                lambda x: {"ok": True},
                effect_key="send-1",
            )
        store.reconcile_effect(ref, "send", "NOT_APPLIED")
        calls = {"n": 0}

        def effect(x):
            calls["n"] += 1
            return {"ok": True}

        self.assertEqual(
            store.execute_step(
                ref,
                "send",
                StepKind.EFFECT,
                {"msg": "x"},
                effect,
                effect_key="send-1",
            ),
            {"ok": True},
        )
        self.assertEqual(calls["n"], 1)
        store.close()

    def test_effect_exception_is_ambiguous(self):
        db = self.make_db()
        store = DurableWorkflowStore(db)
        ref = store.start("wf-effect-exc", "v1", {})

        def effect(_):
            raise OSError("transport reset")

        with self.assertRaises(AmbiguousEffect):
            store.execute_step(
                ref,
                "send",
                StepKind.EFFECT,
                {},
                effect,
                effect_key="send-1",
            )
        self.assertEqual(store.snapshot(ref)["steps"][0]["status"], "AMBIGUOUS")
        store.close()

    def test_code_version_change_requires_explicit_patch(self):
        db = self.make_db()
        store = DurableWorkflowStore(db)
        ref = store.start("wf-version", "v1", {})
        with self.assertRaises(VersionMismatch):
            store.resume(ref, "v2")
        store.register_patch("wf-version", "v1", "v2", "patch-v1-v2")
        snap = store.resume(ref, "v2")
        self.assertEqual(snap["code_version"], "v2")
        store.close()

    def test_event_tampering_is_detected(self):
        db = self.make_db()
        store = DurableWorkflowStore(db)
        ref = store.start("wf-integrity", "v1", {})
        store.execute_step(ref, "s1", StepKind.PURE, 1, lambda x: x + 1)
        store.conn.execute(
            "UPDATE workflow_events SET payload_json='{}' "
            "WHERE workflow_id=? AND run_id=? AND seq=2",
            (ref.workflow_id, ref.run_id),
        )
        store.conn.commit()
        with self.assertRaises(IntegrityViolation):
            store.verify_integrity(ref)
        store.close()

    def test_continue_as_new_carries_explicit_state_not_step_cache(self):
        db = self.make_db()
        store = DurableWorkflowStore(db)
        ref1 = store.start("wf-can", "v1", {"phase": 1})
        calls = {"n": 0}

        def pure(x):
            calls["n"] += 1
            return x + 1

        store.execute_step(ref1, "s1", StepKind.PURE, 1, pure)
        ref2 = store.continue_as_new(ref1, "v1", {"phase": 2})
        self.assertEqual(store.snapshot(ref2)["steps"], [])
        self.assertEqual(store.snapshot(ref2)["explicit_state"], {"phase": 2})
        store.execute_step(ref2, "s1", StepKind.PURE, 1, pure)
        self.assertEqual(calls["n"], 2)
        store.close()

    def test_continue_as_new_blocks_unresolved_effect(self):
        db = self.make_db()
        store = DurableWorkflowStore(db)
        ref = store.start("wf-can-block", "v1", {})
        with self.assertRaises(WorkflowError):
            store.execute_step(
                ref,
                "e1",
                StepKind.EFFECT,
                {},
                lambda x: x,
                effect_key="effect-1",
                simulate_interrupt_after_start=True,
            )
        with self.assertRaises(AmbiguousEffect):
            store.continue_as_new(ref, "v1", {})
        store.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
