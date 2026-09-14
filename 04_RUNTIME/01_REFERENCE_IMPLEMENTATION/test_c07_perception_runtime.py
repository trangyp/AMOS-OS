import unittest

from c07_perception_runtime import (
    FusionResult,
    Percept,
    PerceptOrigin,
    PerceptionStatus,
    fuse,
    validate_percept,
)


def percept(modality="vision", *, origin=PerceptOrigin.OBSERVED, available=True, confidence=0.8,
            observer="obs", object_id="obj", feature="f", provenance=("p",)):
    return Percept(
        object_id=object_id,
        modality=modality,
        feature=feature,
        observer=observer,
        provenance_ids=provenance,
        origin=origin,
        available=available,
        confidence=confidence,
        intensity=0.5 if available else None,
        clarity=0.7 if available else None,
    )


class PerceptionRuntimeTests(unittest.TestCase):
    def test_unavailable_modality_must_remain_unobserved(self):
        p = percept(origin=PerceptOrigin.UNOBSERVED, available=False, confidence=0.0)
        self.assertEqual(validate_percept(p), PerceptionStatus.HOLD_UNOBSERVED)
        with self.assertRaises(ValueError):
            percept(origin=PerceptOrigin.OBSERVED, available=False, confidence=0.0)
        with self.assertRaises(ValueError):
            percept(origin=PerceptOrigin.UNOBSERVED, available=False, confidence=0.1)

    def test_available_modality_cannot_be_labeled_unobserved(self):
        with self.assertRaises(ValueError):
            percept(origin=PerceptOrigin.UNOBSERVED, available=True, confidence=0.0)

    def test_origins_remain_distinct(self):
        origins = [PerceptOrigin.OBSERVED, PerceptOrigin.USER_REPORTED, PerceptOrigin.INFERRED, PerceptOrigin.SIMULATED]
        items = tuple(percept(modality=f"m{i}", origin=origin, confidence=0.9 - i * 0.1) for i, origin in enumerate(origins))
        self.assertEqual(tuple(p.origin for p in items), tuple(origins))
        result = fuse(items)
        self.assertEqual(result.status, PerceptionStatus.FUSION_VALID)
        self.assertFalse(result.causal_claim)

    def test_fusion_confidence_never_exceeds_weakest_available_channel(self):
        items = (
            percept("vision", confidence=0.9, provenance=("p1",)),
            percept("audio", confidence=0.4, provenance=("p2",)),
            percept("text", confidence=0.7, provenance=("p3",)),
        )
        result = fuse(items)
        self.assertEqual(result.confidence, 0.4)
        self.assertLessEqual(result.confidence, min(p.confidence for p in items))
        self.assertEqual(result.provenance_ids, ("p1", "p2", "p3"))

    def test_unavailable_channels_do_not_inflate_or_depress_available_fusion(self):
        items = (
            percept("vision", confidence=0.8),
            percept("biosignal", origin=PerceptOrigin.UNOBSERVED, available=False, confidence=0.0),
        )
        result = fuse(items)
        self.assertEqual(result.confidence, 0.8)

    def test_all_unavailable_is_hold_not_zero_evidence_pass(self):
        result = fuse((
            percept("vision", origin=PerceptOrigin.UNOBSERVED, available=False, confidence=0.0),
            percept("audio", origin=PerceptOrigin.UNOBSERVED, available=False, confidence=0.0),
        ))
        self.assertEqual(result.status, PerceptionStatus.HOLD_UNOBSERVED)
        self.assertEqual(result.confidence, 0.0)
        self.assertFalse(result.causal_claim)

    def test_fusion_requires_same_object_and_feature(self):
        with self.assertRaises(ValueError):
            fuse((percept(object_id="a"), percept(object_id="b")))
        with self.assertRaises(ValueError):
            fuse((percept(feature="a"), percept(feature="b")))

    def test_confidence_domain_is_bounded(self):
        with self.assertRaises(ValueError):
            percept(confidence=-0.1)
        with self.assertRaises(ValueError):
            percept(confidence=1.1)
        with self.assertRaises(ValueError):
            percept(confidence=float("nan"))

    def test_fusion_result_cannot_mint_causality(self):
        with self.assertRaises(ValueError):
            FusionResult(
                status=PerceptionStatus.FUSION_VALID,
                object_id="o",
                feature="f",
                observers=("obs",),
                modalities=("m",),
                confidence=0.5,
                provenance_ids=("p",),
                causal_claim=True,
                reasons=("bad",),
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
