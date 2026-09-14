import unittest

import ulk_fragment_execution_registry as registry


class FragmentExecutionRegistryTests(unittest.TestCase):
    def test_bounded_semantic_fragments_are_bound_without_canon_promotion(self):
        for fragment in (
            registry.Fragment.ALU03_TEMPORAL_LTL,
            registry.Fragment.ALU04_EPISTEMIC_MODAL,
            registry.Fragment.ALU05_NON_MONOTONIC_DUNG,
        ):
            binding = registry.execution_binding(fragment)
            self.assertIs(
                binding.status,
                registry.ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
            )
            self.assertEqual(
                binding.checker_sha256,
                registry.SEMANTIC_FRAGMENT_CHECKER_SHA256,
            )
            self.assertFalse(binding.canon_promoted)

    def test_unimplemented_fragments_remain_specification_only(self):
        for fragment in (
            registry.Fragment.ALU06_DEPENDENT_TYPE,
            registry.Fragment.ALU08_CATEGORICAL_TOPOS,
        ):
            self.assertIs(
                registry.execution_binding(fragment).status,
                registry.ExecutionStatus.SPECIFICATION_ONLY,
            )

    def test_registry_invariants(self):
        self.assertEqual(registry.validate_execution_registry(), ())


if __name__ == "__main__":
    unittest.main()
