import unittest

from c05_representation_runtime import (
    EpistemicLevel,
    RepresentationStatus,
    RepresentationTransform,
    evaluate_representation,
)


def transform(**overrides):
    base = dict(
        transform_id="t1",
        source_type="source",
        target_type="target",
        map_type="semantic",
        scope="domain-a",
        regime="r1",
        observer="obs-1",
        source_schema_hash="s1",
        expected_source_schema_hash="s1",
        target_schema_hash="s2",
        expected_target_schema_hash="s2",
        source_epistemic=EpistemicLevel.DERIVED,
        target_epistemic=EpistemicLevel.DERIVED,
        preserved_features=("identity", "units", "decision-key"),
        lost_features=(),
        decision_required_features=("decision-key",),
        provenance_ids=("p1",),
        unknown_gaps=(),
    )
    base.update(overrides)
    return RepresentationTransform(**base)


class RepresentationRuntimeTests(unittest.TestCase):
    def test_lossless_required_structure_can_claim_bounded_equivalence(self):
        result = evaluate_representation(transform())
        self.assertEqual(result.status, RepresentationStatus.TRANSFORM_BOUNDED)
        self.assertTrue(result.equivalent)
        self.assertEqual(result.residual_features, ())

    def test_noncritical_loss_allows_transform_but_not_equivalence(self):
        result = evaluate_representation(
            transform(lost_features=("styling",), preserved_features=("identity", "decision-key"))
        )
        self.assertEqual(result.status, RepresentationStatus.TRANSFORM_BOUNDED)
        self.assertFalse(result.equivalent)
        self.assertEqual(result.residual_features, ("styling",))

    def test_decision_changing_loss_blocks(self):
        result = evaluate_representation(
            transform(lost_features=("decision-key",), preserved_features=("identity",))
        )
        self.assertEqual(result.status, RepresentationStatus.BLOCK_DECISION_LOSS)
        self.assertFalse(result.equivalent)

    def test_epistemic_upgrade_is_forbidden(self):
        result = evaluate_representation(
            transform(source_epistemic=EpistemicLevel.OBSERVATION, target_epistemic=EpistemicLevel.VERIFIED)
        )
        self.assertEqual(result.status, RepresentationStatus.BLOCK_EPISTEMIC_UPGRADE)

    def test_schema_scope_regime_observer_and_unknown_fail_closed(self):
        self.assertEqual(
            evaluate_representation(transform(expected_source_schema_hash="other")).status,
            RepresentationStatus.BLOCK_SCHEMA,
        )
        self.assertEqual(evaluate_representation(transform(scope="UNRESOLVED")).status, RepresentationStatus.BLOCK_SCOPE)
        self.assertEqual(evaluate_representation(transform(regime="UNRESOLVED")).status, RepresentationStatus.BLOCK_REGIME)
        self.assertEqual(evaluate_representation(transform(observer="UNRESOLVED")).status, RepresentationStatus.BLOCK_OBSERVER)
        self.assertEqual(evaluate_representation(transform(unknown_gaps=("mapping-gap",))).status, RepresentationStatus.HOLD_UNKNOWN)

    def test_output_requires_provenance(self):
        with self.assertRaises(ValueError):
            transform(provenance_ids=())

    def test_feature_cannot_be_both_preserved_and_lost(self):
        with self.assertRaises(ValueError):
            transform(preserved_features=("x",), lost_features=("x",))

    def test_bidirectional_equivalence_is_not_inferred(self):
        forward = evaluate_representation(
            transform(map_type="one-way", lost_features=("styling",), preserved_features=("identity", "decision-key"))
        )
        self.assertFalse(forward.equivalent)
        self.assertNotIn("reverse", " ".join(forward.reasons).lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
