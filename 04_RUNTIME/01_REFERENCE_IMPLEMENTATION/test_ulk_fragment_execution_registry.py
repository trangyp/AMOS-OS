import hashlib
import pathlib
import unittest

from ulk_fragment_execution_registry import (
    ALU06_CHECKER_SHA256,
    ALU08_CHECKER_SHA256,
    ExecutionStatus,
    Fragment,
    execution_binding,
    validate_execution_registry,
)


class RegistryTests(unittest.TestCase):
    def test_new_checker_hashes_bind_exact_files(self):
        root = pathlib.Path(__file__).parent
        self.assertEqual(
            hashlib.sha256((root / "amos_ulk_alu06_dependent_pi_checker_v1.py").read_bytes()).hexdigest(),
            ALU06_CHECKER_SHA256,
        )
        self.assertEqual(
            hashlib.sha256((root / "amos_ulk_alu08_finite_category_heyting_checker_v1.py").read_bytes()).hexdigest(),
            ALU08_CHECKER_SHA256,
        )

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
