from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]

CONTRACTS = {
    "05_CELL_REGISTRY": (
        "25_COGNITIVE_MATRIX/05_CELL_REGISTRY/COGNITIVE_MATRIX_CELL_REGISTRY_CONTRACT.md",
        ("matrix_registry_runtime.py",),
    ),
    "06_CELL_CONTRACTS": (
        "25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/COGNITIVE_MATRIX_CELL_CONTRACTS_CONTRACT.md",
        ("cognitive_matrix_contract_runtime.py",),
    ),
    "07_COVERAGE": (
        "25_COGNITIVE_MATRIX/07_COVERAGE/COGNITIVE_MATRIX_COVERAGE_CONTRACT.md",
        ("cognitive_matrix_runtime.py", "matrix_registry_runtime.py"),
    ),
    "08_STRUCTURAL_GAPS": (
        "25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/COGNITIVE_MATRIX_STRUCTURAL_GAPS_CONTRACT.md",
        ("cognitive_matrix_runtime.py", "cognitive_matrix_contract_runtime.py"),
    ),
    "09_DEPENDENCY_GRAPH": (
        "25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/COGNITIVE_MATRIX_DEPENDENCY_GRAPH_CONTRACT.md",
        ("cognitive_matrix_runtime.py", "urk_relation_algebra.py"),
    ),
    "10_ROUTING": (
        "25_COGNITIVE_MATRIX/10_ROUTING/COGNITIVE_MATRIX_ROUTING_CONTRACT.md",
        ("internet_algorithm_registry.py", "algorithm_routing_runtime.py"),
    ),
    "11_VALIDATION": (
        "25_COGNITIVE_MATRIX/11_VALIDATION/COGNITIVE_MATRIX_VALIDATION_CONTRACT.md",
        ("cognitive_matrix_runtime.py", "test_urk_math_type_firewall.py"),
    ),
}


class ContractReconciliationTests(unittest.TestCase):
    def _text(self, relative_path):
        return (REPO_ROOT / relative_path).read_text(encoding="utf-8")

    def test_parent_contracts_no_longer_claim_no_executor(self):
        for plane, (path, _) in CONTRACTS.items():
            with self.subTest(plane=plane):
                text = self._text(path)
                self.assertNotIn("No subsystem-local executor yet", text)
                self.assertNotIn("ceiling 0.95", text)

    def test_parent_contracts_name_current_bounded_owners(self):
        for plane, (path, owners) in CONTRACTS.items():
            with self.subTest(plane=plane):
                text = self._text(path)
                for owner in owners:
                    self.assertIn(owner, text)

    def test_dependency_sensitive_contracts_do_not_state_unconditional_invalidation_law(self):
        stale_sentence = "Selective invalidation — failure invalidates dependent descendants only"
        for plane, (path, _) in CONTRACTS.items():
            with self.subTest(plane=plane):
                self.assertNotIn(stale_sentence, self._text(path))

    def test_routing_contract_preserves_capability_authority_firewall(self):
        text = self._text(CONTRACTS["10_ROUTING"][0])
        self.assertIn("CAPABILITY != AUTHORITY", text)
        self.assertIn("NO_MATCH -> UNKNOWN/GAP", text)
        self.assertIn("finite-trace", text)
        self.assertIn("infinite-word", text)

    def test_validation_contract_preserves_test_truth_firewall(self):
        text = self._text(CONTRACTS["11_VALIDATION"][0])
        self.assertIn("TEST_PASS != TRUTH", text)
        self.assertIn("VALIDATION != AUTHORITY", text)
        self.assertIn("indexed fields are not automatically algebraic tensors", text)


if __name__ == "__main__":
    unittest.main()
