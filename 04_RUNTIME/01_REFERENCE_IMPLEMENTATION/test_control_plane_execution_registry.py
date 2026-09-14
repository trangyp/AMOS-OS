import unittest

from control_plane_execution_registry import BINDINGS, coverage_vector, validate_control_plane_registry


class ControlPlaneExecutionRegistryTests(unittest.TestCase):
    def test_exactly_nine_control_planes_are_bound(self):
        self.assertEqual(tuple(sorted(BINDINGS)), tuple(f"C{i:02d}" for i in range(1, 10)))

    def test_every_plane_has_implementation_and_test_artifact(self):
        self.assertEqual(coverage_vector(), (9, 9, 9))
        self.assertEqual(validate_control_plane_registry(), ())

    def test_implementation_evidence_never_self_promotes_canon(self):
        self.assertTrue(all(not binding.canon_promoted for binding in BINDINGS.values()))

    def test_memory_plane_is_bound_to_memory_subsystem_not_duplicated_reference_file(self):
        self.assertTrue(BINDINGS["C06"].implementation_path.startswith("10_MEMORY/"))
        self.assertTrue(BINDINGS["C06"].test_path.startswith("10_MEMORY/"))

    def test_execution_plane_is_staging_not_commit_authority(self):
        self.assertEqual(BINDINGS["C08"].role, "EXECUTION_STAGING")


if __name__ == "__main__":
    unittest.main(verbosity=2)
