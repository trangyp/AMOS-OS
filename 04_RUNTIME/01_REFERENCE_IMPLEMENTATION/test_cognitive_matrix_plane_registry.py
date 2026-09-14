from pathlib import Path
import unittest

import cognitive_matrix_plane_registry as r


REPO_ROOT = Path(__file__).resolve().parents[2]


class CognitiveMatrixPlaneRegistryTests(unittest.TestCase):
    def test_exact_12_plane_coverage(self):
        self.assertEqual(len(r.PLANE_BINDINGS), 12)
        self.assertEqual(r.execution_coverage(), (12, 12, 12))
        self.assertEqual(r.validate_plane_registry(REPO_ROOT), ())

    def test_registry_never_claims_semantic_completion_or_authority(self):
        for plane_id, binding in r.PLANE_BINDINGS.items():
            self.assertFalse(binding.semantic_completion, plane_id)
            self.assertFalse(binding.canon_authority, plane_id)
            self.assertFalse(binding.effect_authority, plane_id)

    def test_generator_plane_is_guarded_not_complete(self):
        binding = r.PLANE_BINDINGS["12_GENERATORS"]
        self.assertEqual(binding.status, r.PlaneStatus.BOUNDED_GENERATOR_GUARDED)
        self.assertIn("25_COGNITIVE_MATRIX/12_GENERATORS/fill_matrix.py", binding.executor_paths)
        self.assertIn(
            "04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_cognitive_matrix_generator_guard.py",
            binding.test_paths,
        )

    def test_control_plane_registry_keeps_memory_owner_separate(self):
        binding = r.PLANE_BINDINGS["03_CONTROL_PLANES"]
        self.assertIn("10_MEMORY/memory_lifecycle_runtime.py", binding.executor_paths)
        self.assertIn("10_MEMORY/test_memory_lifecycle_runtime.py", binding.test_paths)

    def test_partial_planes_are_not_promoted_by_coverage(self):
        expected_partial = {
            "01_PRIMITIVES",
            "02_LIFECYCLE_OPERATIONS",
            "04_SCALES",
            "06_CELL_CONTRACTS",
            "10_ROUTING",
            "11_VALIDATION",
        }
        actual = {
            plane_id
            for plane_id, binding in r.PLANE_BINDINGS.items()
            if binding.status is r.PlaneStatus.BOUNDED_PARTIAL
        }
        self.assertEqual(actual, expected_partial)


if __name__ == "__main__":
    unittest.main()
