from dataclasses import replace
import math
import unittest

from c02_metacognitive_runtime import (
    CONFIDENCE_CAP,
    CusumConfig,
    CusumState,
    InterruptClass,
    MetacognitiveRequest,
    MetacognitiveStatus,
    MonitorObservation,
    MonitorRegistry,
    MonitorSpec,
    ShiftDirection,
    evaluate_metacognitive,
    update_cusum,
)
from matrix_registry_runtime import Condition


class C02MetacognitiveTests(unittest.TestCase):
    def registry(self):
        return MonitorRegistry((
            MonitorSpec("drift", "residual_shift", InterruptClass.HALT, "src:nist-cusum"),
            MonitorSpec("cal", "confidence_reliability", InterruptClass.REVIEW, "src:calibration"),
        ))

    def request(self, **changes):
        base = MetacognitiveRequest(
            request_id="meta-1",
            state_version="state-v1",
            provenance_ids=("src:canon-c02",),
            reported_confidence=0.8,
        )
        return replace(base, **changes)

    def test_confidence_cap_is_mechanical(self):
        result = evaluate_metacognitive(self.request(reported_confidence=1.0), self.registry())
        self.assertEqual(result.status, MetacognitiveStatus.CONTINUE_BOUNDED)
        self.assertEqual(result.bounded_confidence, CONFIDENCE_CAP)
        self.assertIn("CONFIDENCE_CAPPED_AT_0_95", result.reasons)

    def test_confidence_domain_fails_closed(self):
        for value in (-0.01, 1.01, math.inf, math.nan):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    self.request(reported_confidence=value)

    def test_unresolved_anomaly_halts_escalation(self):
        obs = MonitorObservation("drift", True, False, "obs:drift-1")
        result = evaluate_metacognitive(self.request(observations=(obs,)), self.registry())
        self.assertEqual(result.status, MetacognitiveStatus.INTERRUPT_UNRESOLVED_ANOMALY)
        self.assertFalse(result.may_escalate)
        self.assertEqual(result.unresolved_monitor_ids, ("drift",))
        self.assertEqual(result.interrupts, (("drift", InterruptClass.HALT),))
        self.assertIn("obs:drift-1", result.provenance_ids)

    def test_review_class_still_holds_when_anomaly_unresolved(self):
        obs = MonitorObservation("cal", True, False, "obs:cal-1")
        result = evaluate_metacognitive(self.request(observations=(obs,)), self.registry())
        self.assertEqual(result.status, MetacognitiveStatus.INTERRUPT_UNRESOLVED_ANOMALY)
        self.assertEqual(result.interrupts, (("cal", InterruptClass.REVIEW),))

    def test_resolved_anomaly_can_continue_bounded(self):
        obs = MonitorObservation("drift", True, True, "obs:drift-resolved")
        result = evaluate_metacognitive(self.request(observations=(obs,)), self.registry())
        self.assertEqual(result.status, MetacognitiveStatus.CONTINUE_BOUNDED)
        self.assertTrue(result.may_escalate)

    def test_unknown_or_inactive_monitor_fails_closed(self):
        unknown = MonitorObservation("missing", True, False, "obs:missing")
        result = evaluate_metacognitive(self.request(observations=(unknown,)), self.registry())
        self.assertEqual(result.status, MetacognitiveStatus.BLOCK_MONITOR_REGISTRY)

        registry = MonitorRegistry((MonitorSpec("off", "x", InterruptClass.REVIEW, "src:x", active=False),))
        inactive = MonitorObservation("off", True, False, "obs:off")
        result = evaluate_metacognitive(self.request(observations=(inactive,)), registry)
        self.assertEqual(result.status, MetacognitiveStatus.BLOCK_MONITOR_REGISTRY)

    def test_registry_identity_collision_fails_closed(self):
        registry = MonitorRegistry()
        registry.register(MonitorSpec("m", "x", InterruptClass.REVIEW, "src:1"))
        with self.assertRaises(ValueError):
            registry.register(MonitorSpec("m", "y", InterruptClass.HALT, "src:2"))

    def test_epistemic_states_preserved(self):
        cases = (
            (Condition.STALE, MetacognitiveStatus.REVALIDATE_STALE),
            (Condition.COMPETING, MetacognitiveStatus.HOLD_COMPETING),
            (Condition.QUARANTINED, MetacognitiveStatus.BLOCK_UPSTREAM),
            (Condition.FALSIFIED, MetacognitiveStatus.BLOCK_UPSTREAM),
        )
        for condition, expected in cases:
            with self.subTest(condition=condition):
                result = evaluate_metacognitive(self.request(upstream_condition=condition), self.registry())
                self.assertEqual(result.status, expected)
                self.assertFalse(result.may_escalate)

    def test_unknown_gap_never_passes(self):
        result = evaluate_metacognitive(
            self.request(unknown_gaps=("monitor-baseline-missing",)),
            self.registry(),
        )
        self.assertEqual(result.status, MetacognitiveStatus.HOLD_UNKNOWN)
        self.assertFalse(result.may_escalate)

    def test_observation_contract_rejects_impossible_resolution(self):
        with self.assertRaises(ValueError):
            MonitorObservation("drift", False, True, "obs:bad")


class CusumTests(unittest.TestCase):
    def test_baseline_stays_quiet(self):
        cfg = CusumConfig(target_mean=0.0, allowance=0.5, decision_limit=3.0)
        state = CusumState()
        for _ in range(20):
            update = update_cusum(cfg, state, 0.0)
            state = update.state
            self.assertFalse(update.alarm)
            self.assertEqual(update.direction, ShiftDirection.NONE)

    def test_upward_and_downward_shift_are_symmetric(self):
        cfg = CusumConfig(target_mean=0.0, allowance=0.5, decision_limit=3.0)
        up_state = CusumState()
        down_state = CusumState()
        for _ in range(2):
            up = update_cusum(cfg, up_state, 2.0)
            down = update_cusum(cfg, down_state, -2.0)
            up_state = up.state
            down_state = down.state
        self.assertTrue(up.alarm)
        self.assertTrue(down.alarm)
        self.assertEqual(up.direction, ShiftDirection.UP)
        self.assertEqual(down.direction, ShiftDirection.DOWN)
        self.assertAlmostEqual(up_state.positive, down_state.negative)

    def test_invalid_cusum_domain_fails_closed(self):
        for kwargs in (
            {"target_mean": 0.0, "allowance": -0.1, "decision_limit": 1.0},
            {"target_mean": 0.0, "allowance": 0.1, "decision_limit": 0.0},
            {"target_mean": math.inf, "allowance": 0.1, "decision_limit": 1.0},
        ):
            with self.subTest(kwargs=kwargs):
                with self.assertRaises(ValueError):
                    CusumConfig(**kwargs)
        with self.assertRaises(ValueError):
            update_cusum(CusumConfig(0.0, 0.1, 1.0), CusumState(), math.nan)

    def test_replay_is_deterministic(self):
        cfg = CusumConfig(target_mean=1.0, allowance=0.2, decision_limit=2.0)
        values = (1.0, 1.1, 1.8, 1.9, 0.2, 0.1)

        def run():
            state = CusumState()
            trace = []
            for x in values:
                update = update_cusum(cfg, state, x)
                state = update.state
                trace.append((state, update.alarm, update.direction))
            return tuple(trace)

        self.assertEqual(run(), run())


if __name__ == "__main__":
    unittest.main(verbosity=2)
