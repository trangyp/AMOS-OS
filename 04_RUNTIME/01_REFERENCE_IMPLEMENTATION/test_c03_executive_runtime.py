import itertools
import unittest

from c03_executive_runtime import (
    ExecutiveCandidate,
    ExecutiveRequest,
    ExecutiveStatus,
    evaluate_executive,
)
from matrix_registry_runtime import Condition


def candidate(
    candidate_id: str,
    *,
    priority: int = 50,
    risk: int = 1,
    irreversibility: int = 1,
    cost: float = 1.0,
    hard: bool = True,
    condition: Condition = Condition.ACTIVE,
):
    return ExecutiveCandidate(
        candidate_id=candidate_id,
        plan_id=f"plan-{candidate_id}",
        goal_id="goal-1",
        priority=priority,
        risk_rank=risk,
        irreversibility_rank=irreversibility,
        resource_cost=cost,
        hard_constraints_pass=hard,
        condition=condition,
        provenance_ids=(f"prov-{candidate_id}",),
    )


def request(candidates, **overrides):
    base = dict(
        request_id="req-1",
        state_version="v1",
        candidates=tuple(candidates),
        input_schema_hash="in",
        expected_input_schema_hash="in",
        output_schema_hash="out",
        expected_output_schema_hash="out",
        observed_epoch="e1",
        required_epoch="e1",
        upstream_condition=Condition.ACTIVE,
        unknown_gaps=(),
    )
    base.update(overrides)
    return ExecutiveRequest(**base)


class ExecutiveRuntimeTests(unittest.TestCase):
    def test_lexicographic_policy_is_deterministic_across_input_permutations(self):
        items = (
            candidate("a", priority=90, risk=3, irreversibility=0, cost=1),
            candidate("b", priority=90, risk=2, irreversibility=4, cost=9),
            candidate("c", priority=80, risk=0, irreversibility=0, cost=0),
        )
        for permutation in itertools.permutations(items):
            result = evaluate_executive(request(permutation))
            self.assertEqual(result.status, ExecutiveStatus.SELECT_PROPOSAL)
            self.assertEqual(result.selected_candidate_id, "b")
            self.assertFalse(result.execution_authorized)
            self.assertTrue(result.requires_c01_authorization)

    def test_hard_constraints_filter_before_ranking(self):
        result = evaluate_executive(
            request((
                candidate("unsafe", priority=100, risk=0, hard=False),
                candidate("safe", priority=10, risk=9, hard=True),
            ))
        )
        self.assertEqual(result.selected_candidate_id, "safe")
        self.assertEqual(result.rejected_candidate_ids, ("unsafe",))

    def test_exact_best_vector_tie_preserves_competing(self):
        result = evaluate_executive(
            request((candidate("a"), candidate("b")))
        )
        self.assertEqual(result.status, ExecutiveStatus.HOLD_COMPETING)
        self.assertEqual(result.competing_candidate_ids, ("a", "b"))
        self.assertIsNone(result.selected_candidate_id)

    def test_candidate_competing_evidence_is_not_collapsed(self):
        result = evaluate_executive(
            request((candidate("a", condition=Condition.COMPETING), candidate("b", priority=1)))
        )
        self.assertEqual(result.status, ExecutiveStatus.HOLD_COMPETING)
        self.assertEqual(result.competing_candidate_ids, ("a",))

    def test_stale_schema_unknown_and_falsified_upstream_fail_closed(self):
        self.assertEqual(
            evaluate_executive(request((candidate("a"),), observed_epoch="old")).status,
            ExecutiveStatus.REVALIDATE_STALE,
        )
        self.assertEqual(
            evaluate_executive(request((candidate("a"),), expected_input_schema_hash="other")).status,
            ExecutiveStatus.BLOCK_SCHEMA_DRIFT,
        )
        self.assertEqual(
            evaluate_executive(request((candidate("a"),), unknown_gaps=("g1",))).status,
            ExecutiveStatus.HOLD_UNKNOWN,
        )
        self.assertEqual(
            evaluate_executive(request((candidate("a"),), upstream_condition=Condition.FALSIFIED)).status,
            ExecutiveStatus.BLOCK_UPSTREAM,
        )

    def test_no_admissible_candidate_is_not_pass(self):
        result = evaluate_executive(
            request((
                candidate("a", hard=False),
                candidate("b", condition=Condition.QUARANTINED),
            ))
        )
        self.assertEqual(result.status, ExecutiveStatus.HOLD_NO_ADMISSIBLE)
        self.assertEqual(result.rejected_candidate_ids, ("a", "b"))

    def test_duplicate_identity_and_invalid_math_domains_rejected(self):
        with self.assertRaises(ValueError):
            request((candidate("a"), candidate("a")))
        with self.assertRaises(ValueError):
            candidate("a", priority=101)
        with self.assertRaises(ValueError):
            candidate("a", risk=-1)
        with self.assertRaises(ValueError):
            candidate("a", cost=float("inf"))

    def test_result_cannot_be_constructed_as_authorized(self):
        selected = evaluate_executive(request((candidate("a"),)))
        self.assertEqual(selected.status, ExecutiveStatus.SELECT_PROPOSAL)
        self.assertFalse(selected.execution_authorized)
        self.assertIn("SELECTION_IS_NOT_C01_AUTHORIZATION_OR_C08_EXECUTION", selected.reasons)


if __name__ == "__main__":
    unittest.main(verbosity=2)
