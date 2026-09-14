import importlib.util
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
GENERATOR_PATH = REPO_ROOT / "25_COGNITIVE_MATRIX" / "12_GENERATORS" / "fill_matrix.py"
sys.path.insert(0, str(GENERATOR_PATH.parent))
_spec = importlib.util.spec_from_file_location("amos_fill_matrix", GENERATOR_PATH)
assert _spec is not None and _spec.loader is not None
fill_matrix = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fill_matrix)


class CognitiveMatrixGeneratorGuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payloads = fill_matrix.load_payloads()

    def test_placeholder_is_fillable_but_runtime_bound_repair_is_protected(self):
        self.assertTrue(fill_matrix.should_fill("PLACEHOLDER / UNVALIDATED", force=False))
        protected = "PLACEHOLDER / UNVALIDATED\nIMPLEMENTED / VALIDATED_BOUNDED"
        self.assertFalse(fill_matrix.should_fill(protected, force=False))
        self.assertFalse(fill_matrix.should_fill(protected, force=True))

    def test_force_only_rewrites_generator_owned_content(self):
        generated = f"{fill_matrix.GENERATED_MARKER}\ncontract text"
        manual = "manually repaired contract text"
        self.assertFalse(fill_matrix.should_fill(generated, force=False))
        self.assertTrue(fill_matrix.should_fill(generated, force=True))
        self.assertFalse(fill_matrix.should_fill(manual, force=True))

    def test_dependency_render_does_not_infer_numbering_order(self):
        payload = self.payloads["L00"]
        rendered = fill_matrix.build_body(
            "L00",
            "REALITY_ENVIRONMENT",
            "01_PRIMITIVES",
            "DEPENDENCIES",
            payload,
            "L00_REALITY_ENVIRONMENT_PRIMITIVES_COGNITIVE_MATRIX_DEPENDENCIES.md",
        )
        self.assertNotIn("Dependency direction follows the primitive flow order", rendered)
        self.assertIn("PACKAGE_NUMBERING != DEPENDENCY", rendered)
        self.assertIn("PACKAGE_NUMBERING != CAUSALITY", rendered)
        self.assertIn("Only explicitly declared payload dependencies are emitted", rendered)

    def test_rscf_render_does_not_mint_arbitrary_numeric_confidence(self):
        rendered = fill_matrix.build_body(
            "L00",
            "REALITY_ENVIRONMENT",
            "01_PRIMITIVES",
            "RSCF",
            self.payloads["L00"],
            "L00_REALITY_ENVIRONMENT_PRIMITIVES_COGNITIVE_MATRIX_RSCF.md",
        )
        self.assertNotIn("confidence_ceiling: 0.6", rendered)
        self.assertIn("confidence_ceiling: UNCALIBRATED", rendered)
        self.assertIn("authoritative_source_contradiction", rendered)
        self.assertIn("executed_evidence_contradiction", rendered)

    def test_equation_render_carries_math_type_firewalls(self):
        rendered = fill_matrix.build_body(
            "L00",
            "REALITY_ENVIRONMENT",
            "01_PRIMITIVES",
            "EQUATIONS",
            self.payloads["L00"],
            "L00_REALITY_ENVIRONMENT_PRIMITIVES_COGNITIVE_MATRIX_EQUATIONS.md",
        )
        self.assertIn("INDEXED_FIELD != ALGEBRAIC_TENSOR", rendered)
        self.assertIn("STRUCTURAL_ADJACENCY != POINT_SET_TOPOLOGY", rendered)
        self.assertIn("Generated equation text remains `DERIVED / AMOS_MODEL`", rendered)

    def test_rendered_output_cannot_mint_source_claim(self):
        with self.assertRaisesRegex(ValueError, "SOURCE_CLAIM"):
            fill_matrix.validate_rendered_output(
                "claim_class: SOURCE_CLAIM\n" + "\n".join(fill_matrix.GLOBAL_HARD_BOUNDARIES)
            )

    def test_all_loaded_payloads_satisfy_generator_schema(self):
        self.assertGreater(len(self.payloads), 0)
        for key, payload in self.payloads.items():
            fill_matrix.validate_payload(key, payload)


if __name__ == "__main__":
    unittest.main()
