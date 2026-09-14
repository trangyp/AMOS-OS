from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
CONTRACT = REPO_ROOT / "02_KERNEL/02_KERNEL_CONTRACT.md"
README = REPO_ROOT / "02_KERNEL/02_KERNEL_README.md"


class KernelContractIntegrityTests(unittest.TestCase):
    def test_kernel_parent_no_longer_makes_universal_runtime_guarantees(self):
        text = CONTRACT.read_text(encoding="utf-8")
        forbidden = (
            "All computation is deterministic for given inputs",
            "All failures are detected, classified, and recovered",
            "Authority is validated before every consequential operation",
            "Canon compliance is verified at every inference step",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, text)

    def test_kernel_parent_preserves_math_and_authority_firewalls(self):
        text = CONTRACT.read_text(encoding="utf-8")
        self.assertIn("indexed records", text)
        self.assertIn("point-set topology", text)
        self.assertIn("logical implication", text)
        self.assertIn("causality", text)
        self.assertIn("capability and validation never mint authority", text)
        self.assertIn("TEST_PASS != TRUTH", text)

    def test_kernel_parent_preserves_logic_namespace_separation(self):
        text = CONTRACT.read_text(encoding="utf-8")
        self.assertIn("canonical ULK ALUs", text)
        self.assertIn("ULMK Atomic Logic Units", text)
        self.assertIn("Core-19 semantic primitives", text)
        self.assertIn("executable AMOS_CORE AST constructors", text)
        self.assertIn("P02 remains `COMPETING`", text)

    def test_readme_does_not_collapse_specification_to_validation(self):
        text = README.read_text(encoding="utf-8")
        for boundary in (
            "SPECIFICATION != IMPLEMENTATION",
            "IMPLEMENTATION != VALIDATION",
            "VALIDATION != TRUTH",
            "CAPABILITY != AUTHORITY",
            "REACHABILITY != ENTAILMENT != CAUSALITY",
            "INDEXED FIELD != ALGEBRAIC TENSOR",
        ):
            self.assertIn(boundary, text)

    def test_readme_keeps_four_logic_namespaces_distinct(self):
        text = README.read_text(encoding="utf-8")
        self.assertIn("Canonical root ULK", text)
        self.assertIn("ULMK", text)
        self.assertIn("Core-19 semantic registry", text)
        self.assertIn("Executable AMOS_CORE AST", text)


if __name__ == "__main__":
    unittest.main()
