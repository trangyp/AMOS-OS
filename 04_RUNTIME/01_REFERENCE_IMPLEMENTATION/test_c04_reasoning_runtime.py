from dataclasses import replace
import unittest
from unittest.mock import patch

from c04_reasoning_runtime import (
    ReasoningRequest,
    ReasoningStatus,
    evaluate_reasoning,
)
from matrix_registry_runtime import Condition
from ulk_fragment_execution_registry import ExecutionStatus, Fragment


class C04ReasoningTests(unittest.TestCase):
    def request(self, **changes):
        base = ReasoningRequest(
            request_id="reason-1",
            state_version="state-v1",
            provenance_ids=("src:claim-1", "obs:test-1"),
            requested_fragments=(Fragment.ALU01_CLASSICAL_PROPOSITIONAL,),
            input_schema_hash="in-v1",
            expected_input_schema_hash="in-v1",
            output_schema_hash="out-v1",
            expected_output_schema_hash="out-v1",
            observed_epoch="epoch-1",
            required_epoch="epoch-1",
        )
        return replace(base, **changes)

    def test_no_output_without_provenance(self):
        with self.assertRaises(ValueError):
            self.request(provenance_ids=())

    def test_unknown_gap_never_routes_as_pass(self):
        result = evaluate_reasoning(self.request(unknown_gaps=("proof-missing",)))
        self.assertEqual(result.status, ReasoningStatus.HOLD_UNKNOWN)
        self.assertFalse(result.bounded_route_ready)

    def test_schema_drift_fails_closed(self):
        for changes in ({"input_schema_hash": "in-v2"}, {"output_schema_hash": "out-v2"}):
            with self.subTest(changes=changes):
                result = evaluate_reasoning(self.request(**changes))
                self.assertEqual(result.status, ReasoningStatus.BLOCK_SCHEMA_DRIFT)

    def test_stale_or_epoch_mismatch_requires_revalidation(self):
        for request in (
            self.request(upstream_condition=Condition.STALE),
            self.request(observed_epoch="epoch-old"),
        ):
            with self.subTest(request=request):
                self.assertEqual(evaluate_reasoning(request).status, ReasoningStatus.REVALIDATE_STALE)

    def test_competing_and_invalid_upstream_are_preserved(self):
        self.assertEqual(
            evaluate_reasoning(self.request(upstream_condition=Condition.COMPETING)).status,
            ReasoningStatus.HOLD_COMPETING,
        )
        for condition in (Condition.QUARANTINED, Condition.FALSIFIED):
            with self.subTest(condition=condition):
                self.assertEqual(
                    evaluate_reasoning(self.request(upstream_condition=condition)).status,
                    ReasoningStatus.BLOCK_UPSTREAM,
                )

    def test_all_eight_fragments_route_through_current_registry(self):
        request = self.request(requested_fragments=tuple(Fragment))
        result = evaluate_reasoning(request)
        self.assertEqual(result.status, ReasoningStatus.ROUTE_BOUNDED)
        self.assertTrue(result.bounded_route_ready)
        self.assertEqual(tuple(route.fragment for route in result.routes), tuple(Fragment))
        self.assertTrue(all(route.checker for route in result.routes))
        self.assertTrue(all(route.execution_identity for route in result.routes))
        self.assertEqual(result.provenance_ids, request.provenance_ids)

    def test_specification_only_fragment_holds_gap(self):
        import c04_reasoning_runtime

        original = c04_reasoning_runtime.execution_binding
        real = original(Fragment.ALU02_FIRST_ORDER_UNIFICATION)
        fake = replace(real, status=ExecutionStatus.SPECIFICATION_ONLY, checker=None)

        def resolver(fragment):
            return fake if fragment is Fragment.ALU02_FIRST_ORDER_UNIFICATION else original(fragment)

        with patch("c04_reasoning_runtime.execution_binding", side_effect=resolver):
            result = evaluate_reasoning(
                self.request(requested_fragments=(Fragment.ALU02_FIRST_ORDER_UNIFICATION,))
            )
        self.assertEqual(result.status, ReasoningStatus.HOLD_FRAGMENT_GAP)
        self.assertEqual(result.gap_fragments, (Fragment.ALU02_FIRST_ORDER_UNIFICATION,))

    def test_duplicate_or_empty_fragment_request_is_invalid(self):
        with self.assertRaises(ValueError):
            self.request(requested_fragments=())
        with self.assertRaises(ValueError):
            self.request(
                requested_fragments=(
                    Fragment.ALU01_CLASSICAL_PROPOSITIONAL,
                    Fragment.ALU01_CLASSICAL_PROPOSITIONAL,
                )
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
