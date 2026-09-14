import unittest

from cognitive_matrix_runtime import DependencyKind
from lifecycle_operation_runtime import (
    LifecycleDependency,
    LifecycleOperationId,
    LifecycleRequest,
    build_lifecycle_dependency_graph,
    lifecycle_spec,
    validate_lifecycle_registry,
    validate_lifecycle_request,
)
from primitive_contract_runtime import EpistemicClass


class LifecycleOperationRuntimeTests(unittest.TestCase):
    def request(self, operation=LifecycleOperationId.O07_INFERENCE, **overrides):
        data = dict(
            request_id="req-1",
            operation=operation,
            input_artifact_ids=("in-1",),
            output_artifact_id="out-1",
            input_epistemic_class=EpistemicClass.DERIVED,
            output_epistemic_class=EpistemicClass.DERIVED,
            state_version="s1",
            scope="test-scope",
            regime="test-regime",
            provenance_ids=("src-1",),
        )
        data.update(overrides)
        return LifecycleRequest(**data)

    def test_exact_17_operation_registry(self):
        self.assertEqual(len(LifecycleOperationId), 17)
        self.assertEqual(validate_lifecycle_registry(), ())

    def test_operation_order_does_not_create_dependency_edges(self):
        graph = build_lifecycle_dependency_graph()
        self.assertEqual(graph.edges(), ())

    def test_only_explicit_dependency_is_added(self):
        graph = build_lifecycle_dependency_graph((
            LifecycleDependency(
                LifecycleOperationId.O07_INFERENCE,
                LifecycleOperationId.O13_DECISION,
                DependencyKind.EVIDENCE,
            ),
        ))
        self.assertEqual(len(graph.edges()), 1)
        edge = graph.edges()[0]
        self.assertEqual(edge.dependency, LifecycleOperationId.O07_INFERENCE.value)
        self.assertEqual(edge.dependent, LifecycleOperationId.O13_DECISION.value)

    def test_epistemic_transition_requires_receipt(self):
        request = self.request(output_epistemic_class=EpistemicClass.MODEL)
        with self.assertRaisesRegex(ValueError, "epistemic class transition"):
            validate_lifecycle_request(request)
        request = self.request(
            output_epistemic_class=EpistemicClass.MODEL,
            epistemic_transition_receipt_id="epistemic-revalidation-1",
        )
        receipt = validate_lifecycle_request(request)
        self.assertTrue(receipt.epistemic_transition_bound)
        self.assertEqual(receipt.output_epistemic_class, EpistemicClass.MODEL)

    def test_consequential_effect_only_action_and_requires_authority_identity(self):
        with self.assertRaisesRegex(ValueError, "only on O14_ACTION"):
            validate_lifecycle_request(
                self.request(
                    operation=LifecycleOperationId.O12_PLAN,
                    consequential_effect_requested=True,
                    authority_witness_id="auth-1",
                )
            )
        with self.assertRaisesRegex(ValueError, "requires an authority witness"):
            validate_lifecycle_request(
                self.request(
                    operation=LifecycleOperationId.O14_ACTION,
                    consequential_effect_requested=True,
                )
            )
        receipt = validate_lifecycle_request(
            self.request(
                operation=LifecycleOperationId.O14_ACTION,
                consequential_effect_requested=True,
                authority_witness_id="auth-1",
            )
        )
        self.assertTrue(receipt.contract_valid)
        self.assertFalse(receipt.effect_authorized)

    def test_learning_never_grants_host_weight_mutation(self):
        spec = lifecycle_spec(LifecycleOperationId.O16_LEARNING)
        self.assertFalse(spec.host_weight_mutation_allowed)
        receipt = validate_lifecycle_request(self.request(operation=LifecycleOperationId.O16_LEARNING))
        self.assertFalse(receipt.host_weight_mutation_allowed)

    def test_memory_prediction_simulation_names_do_not_upgrade_semantics(self):
        for operation in (
            LifecycleOperationId.O05_MEMORY,
            LifecycleOperationId.O08_PREDICTION,
            LifecycleOperationId.O09_SIMULATION,
        ):
            receipt = validate_lifecycle_request(self.request(operation=operation))
            self.assertEqual(receipt.input_epistemic_class, receipt.output_epistemic_class)
            self.assertFalse(receipt.effect_authorized)

    def test_self_dependency_fails_closed(self):
        with self.assertRaises(ValueError):
            LifecycleDependency(LifecycleOperationId.O04_STATE, LifecycleOperationId.O04_STATE)


if __name__ == "__main__":
    unittest.main()
