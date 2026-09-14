#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import math
import sys
import unittest
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[1] / "17_OBSERVABILITY" / "agent_trace_runtime.py"
spec = importlib.util.spec_from_file_location("amos_agent_trace_runtime", RUNTIME)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)

TRACE_ID = "1" * 32
ROOT_ID = "2" * 16
CHILD_ID = "3" * 16
EFFECT_ID = "4" * 16


def root_span(**overrides):
    data = dict(
        trace_id=TRACE_ID,
        span_id=ROOT_ID,
        parent_span_id=None,
        name="workflow root",
        kind=mod.SpanKind.WORKFLOW,
        start_time_ns=10,
        end_time_ns=100,
        status=mod.SpanStatus.OK,
        attributes={"amos.workflow.id": "wf-1"},
    )
    data.update(overrides)
    return mod.TraceSpan(**data)


def tool_span(**overrides):
    data = dict(
        trace_id=TRACE_ID,
        span_id=CHILD_ID,
        parent_span_id=ROOT_ID,
        name="execute_tool search",
        kind=mod.SpanKind.TOOL,
        start_time_ns=20,
        end_time_ns=40,
        status=mod.SpanStatus.OK,
        attributes={"gen_ai.operation.name": "execute_tool", "gen_ai.tool.name": "search"},
    )
    data.update(overrides)
    return mod.TraceSpan(**data)


class AgentTraceRuntimeTests(unittest.TestCase):
    def test_valid_trace_and_receipt(self):
        env = mod.TraceEnvelope(trace_id=TRACE_ID, spans=(root_span(), tool_span()), expected_span_count=2)
        env.validate()
        self.assertEqual(env.missingness_state(), "COMPLETE")
        self.assertEqual(env.coverage_ratio(), 1.0)
        self.assertRegex(env.receipt_sha256(), r"^[0-9a-f]{64}$")

    def test_invalid_trace_id_rejected(self):
        with self.assertRaises(mod.TraceContractError):
            root_span(trace_id="bad").validate()

    def test_missing_parent_rejected(self):
        child = tool_span(parent_span_id="9" * 16)
        env = mod.TraceEnvelope(trace_id=TRACE_ID, spans=(root_span(), child))
        with self.assertRaises(mod.TraceContractError):
            env.validate()

    def test_raw_content_requires_full_capture(self):
        span = tool_span(attributes={"gen_ai.tool.call.arguments": "secret"})
        with self.assertRaises(mod.TraceContractError):
            span.validate()

    def test_full_capture_requires_authority(self):
        span = tool_span(
            capture_mode=mod.CaptureMode.FULL,
            attributes={"gen_ai.tool.call.arguments": "sensitive"},
        )
        with self.assertRaises(mod.TraceContractError):
            span.validate()

    def test_hash_only_requires_digest(self):
        span = tool_span(capture_mode=mod.CaptureMode.HASH_ONLY)
        with self.assertRaises(mod.TraceContractError):
            span.validate()

    def test_committed_effect_requires_authority_and_receipt(self):
        effect = mod.TraceSpan(
            trace_id=TRACE_ID,
            span_id=EFFECT_ID,
            parent_span_id=ROOT_ID,
            name="external effect",
            kind=mod.SpanKind.EFFECT,
            start_time_ns=50,
            end_time_ns=70,
            status=mod.SpanStatus.OK,
            effect_state=mod.EffectState.COMMITTED,
            effect_id="effect-1",
        )
        with self.assertRaises(mod.TraceContractError):
            effect.validate()

    def test_committed_effect_with_authority_is_valid(self):
        effect = mod.TraceSpan(
            trace_id=TRACE_ID,
            span_id=EFFECT_ID,
            parent_span_id=ROOT_ID,
            name="external effect",
            kind=mod.SpanKind.EFFECT,
            start_time_ns=50,
            end_time_ns=70,
            status=mod.SpanStatus.OK,
            effect_state=mod.EffectState.COMMITTED,
            effect_id="effect-1",
            authority_decision_id="auth-1",
            receipt_ref="receipt-1",
        )
        effect.validate()

    def test_in_doubt_effect_requires_in_doubt_status(self):
        effect = mod.TraceSpan(
            trace_id=TRACE_ID,
            span_id=EFFECT_ID,
            parent_span_id=ROOT_ID,
            name="ambiguous effect",
            kind=mod.SpanKind.EFFECT,
            start_time_ns=50,
            end_time_ns=70,
            status=mod.SpanStatus.OK,
            effect_state=mod.EffectState.IN_DOUBT,
            effect_id="effect-2",
        )
        with self.assertRaises(mod.TraceContractError):
            effect.validate()

    def test_missingness_unknown_is_not_zero(self):
        env = mod.TraceEnvelope(trace_id=TRACE_ID, spans=(root_span(),))
        self.assertIsNone(env.coverage_ratio())
        self.assertEqual(env.missingness_state(), "UNKNOWN")

    def test_partial_missingness_is_explicit(self):
        env = mod.TraceEnvelope(
            trace_id=TRACE_ID,
            spans=(root_span(),),
            expected_span_count=3,
            dropped_span_count=1,
            sampling_applied=True,
        )
        self.assertEqual(env.missingness_state(), "PARTIAL")
        self.assertAlmostEqual(env.coverage_ratio(), 1.0 / 3.0)

    def test_receipt_changes_when_trace_changes(self):
        a = mod.TraceEnvelope(trace_id=TRACE_ID, spans=(root_span(), tool_span()))
        b = mod.TraceEnvelope(
            trace_id=TRACE_ID,
            spans=(root_span(), tool_span(attributes={"gen_ai.operation.name": "execute_tool", "x": 2})),
        )
        self.assertNotEqual(a.receipt_sha256(), b.receipt_sha256())

    def test_entropy_delta_may_be_positive_or_negative(self):
        uniform = [0.5, 0.5]
        concentrated = [0.9, 0.1]
        self.assertLess(mod.entropy_delta_bits(uniform, concentrated), 0.0)
        self.assertGreater(mod.entropy_delta_bits(concentrated, uniform), 0.0)

    def test_kl_divergence_is_nonnegative_on_valid_domain(self):
        value = mod.kl_divergence_bits([0.9, 0.1], [0.5, 0.5])
        self.assertGreaterEqual(value, 0.0)
        self.assertTrue(math.isfinite(value))

    def test_kl_zero_support_violation_rejected(self):
        with self.assertRaises(mod.TraceContractError):
            mod.kl_divergence_bits([1.0, 0.0], [0.0, 1.0])


if __name__ == "__main__":
    unittest.main()
