import hashlib
import pathlib
import unittest

from ulk_fragment_execution_registry import (
    ALU02_CHECKER_SHA256,
    ALU04_CHECKER_SHA256,
    ALU05_CHECKER_SHA256,
    ALU06_CHECKER_SHA256,
    ALU08_CHECKER_SHA256,
    ExecutionStatus,
    Fragment,
    execution_binding,
    validate_execution_registry,
)


class RegistryTests(unittest.TestCase):
    def test_standalone_checker_hashes_bind_exact_files(self):
        root = pathlib.Path(__file__).parent
        expected = {
            "amos_ulk_alu02_unification_reference_checker_v1.py": ALU02_CHECKER_SHA256,
            "amos_ulk_alu04_finite_kripke_checker_v1.py": ALU04_CHECKER_SHA256,
            "amos_ulk_alu05_dung_checker_v1.py": ALU05_CHECKER_SHA256,
            "amos_ulk_alu06_dependent_pi_checker_v1.py": ALU06_CHECKER_SHA256,
            "amos_ulk_alu08_finite_category_heyting_checker_v1.py": ALU08_CHECKER_SHA256,
        }
        for filename, expected_hash in expected.items():
            with self.subTest(filename=filename):
                actual_hash = hashlib.sha256((root / filename).read_bytes()).hexdigest()
                self.assertEqual(actual_hash, expected_hash, filename)

    def test_all_eight_namespaces_have_bounded_or_rebound_evidence(self):
        self.assertEqual(
            execution_binding(Fragment.ALU01_CLASSICAL_PROPOSITIONAL).status,
            ExecutionStatus.EXECUTABLE_BOUNDED,
        )
        for fragment in Fragment:
            if fragment is Fragment.ALU01_CLASSICAL_PROPOSITIONAL:
                continue
            self.assertEqual(
                execution_binding(fragment).status,
                ExecutionStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND,
            )

    def test_no_candidate_self_promotes_canon(self):
        for fragment in Fragment:
            self.assertFalse(execution_binding(fragment).canon_promoted)

    def test_registry_invariants(self):
        self.assertEqual(validate_execution_registry(), ())


if __name__ == "__main__":
    unittest.main()
