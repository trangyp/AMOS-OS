import unittest

from scale_contract_runtime import (
    Scale,
    ScaleArtifact,
    ScaleTransform,
    validate_scale_registry,
    validate_scale_transform,
)


class ScaleContractRuntimeTests(unittest.TestCase):
    def test_exact_hml_registry(self):
        self.assertEqual(len(Scale), 3)
        self.assertEqual(validate_scale_registry(), ())

    def test_scale_artifact_requires_scope_regime_version_and_provenance(self):
        with self.assertRaises(ValueError):
            ScaleArtifact("a", Scale.H_HIGH, "s1", "scope", "regime", ())
        with self.assertRaises(ValueError):
            ScaleArtifact("a", Scale.H_HIGH, "", "scope", "regime", ("src",))

    def test_cross_scale_transform_requires_explicit_evidence(self):
        with self.assertRaises(ValueError):
            ScaleTransform(
                "t",
                Scale.H_HIGH,
                Scale.M_MID,
                (),
                ("inv",),
                ("src",),
                "receipt",
            )
        transform = ScaleTransform(
            "t",
            Scale.H_HIGH,
            Scale.M_MID,
            ("assumption",),
            ("inv",),
            ("src",),
            "receipt",
        )
        receipt = validate_scale_transform(transform)
        self.assertTrue(receipt.structurally_bound)
        self.assertFalse(receipt.semantic_equivalence_proven)
        self.assertFalse(receipt.causal_equivalence_proven)

    def test_same_scale_is_not_cross_scale_transform(self):
        with self.assertRaises(ValueError):
            ScaleTransform(
                "t",
                Scale.L_LOW,
                Scale.L_LOW,
                ("assumption",),
                ("inv",),
                ("src",),
                "receipt",
            )


if __name__ == "__main__":
    unittest.main()
