import unittest

from human_interaction_profile_runtime import (
    ExpressionProfile,
    HumanInteractionRuntime,
    HypothesisStatus,
    LegacyClaimClass,
    Stakes,
    admit_state_hypothesis,
    apply_explicit_preferences,
    legacy_claim_admissible,
    validate_runtime_invariants,
)


class ExpressionTests(unittest.TestCase):
    def test_explicit_preferences_change_style_only(self):
        out = HumanInteractionRuntime().decide(
            explicit_preferences={"brevity": 1.0, "warmth": 0.0, "directness": 1.0},
            stakes=Stakes.HIGH,
        )
        self.assertEqual(out.profile.brevity, 1.0)
        self.assertEqual(out.profile.warmth, 0.0)
        self.assertEqual(out.profile.directness, 1.0)
        self.assertEqual(out.profile.evidence_visibility, 1.0)
        self.assertEqual(out.profile.uncertainty_visibility, 1.0)
        self.assertFalse(out.authority_granted)
        self.assertFalse(out.effect_authorized)
        self.assertFalse(out.truth_status_mutable)
        self.assertFalse(out.safety_constraints_mutable)

    def test_protected_preference_keys_rejected(self):
        with self.assertRaises(ValueError):
            apply_explicit_preferences(ExpressionProfile(), {"authority_granted": 1.0})
        with self.assertRaises(ValueError):
            apply_explicit_preferences(ExpressionProfile(), {"evidence_visibility": 0.0})

    def test_profile_bounds(self):
        with self.assertRaises(ValueError):
            ExpressionProfile(warmth=1.1)


class HypothesisTests(unittest.TestCase):
    def test_nonclinical_hypothesis_is_tentative(self):
        h = admit_state_hypothesis(
            "prefers concise responses",
            ["explicit request for short output"],
            0.60,
        )
        self.assertTrue(h.usable)
        self.assertEqual(h.status, HypothesisStatus.TENTATIVE_NONCLINICAL)

    def test_no_basis_rejected(self):
        h = admit_state_hypothesis("prefers concise responses", [], 0.5)
        self.assertEqual(h.status, HypothesisStatus.REJECTED_NO_BASIS)

    def test_confidence_ceiling_is_fail_closed(self):
        h = admit_state_hypothesis("prefers concise responses", ["one short-message request"], 0.61)
        self.assertEqual(h.status, HypothesisStatus.REJECTED_CONFIDENCE)

    def test_sensitive_or_biological_state_rejected(self):
        labels = [
            "depression",
            "autistic",
            "nervous system state: shutdown",
            "dissociation",
            "psychopath",
        ]
        for label in labels:
            h = admit_state_hypothesis(label, ["text style"], 0.3)
            self.assertEqual(h.status, HypothesisStatus.REJECTED_SENSITIVE_INFERENCE, label)
        h = admit_state_hypothesis("fatigued", ["short sentences"], 0.2, biological=True)
        self.assertEqual(h.status, HypothesisStatus.REJECTED_SENSITIVE_INFERENCE)

    def test_rejected_hypotheses_do_not_enter_decision(self):
        good = admit_state_hypothesis("prefers directness", ["explicit wording"], 0.5)
        bad = admit_state_hypothesis("depression", ["punctuation"], 0.2)
        out = HumanInteractionRuntime().decide(hypotheses=[good, bad])
        self.assertEqual(out.admitted_hypotheses, (good,))


class LegacyMigrationTests(unittest.TestCase):
    def test_only_style_claims_auto_migrate(self):
        self.assertTrue(legacy_claim_admissible(LegacyClaimClass.STYLE))
        for cls in LegacyClaimClass:
            if cls is not LegacyClaimClass.STYLE:
                self.assertFalse(legacy_claim_admissible(cls))

    def test_runtime_invariants(self):
        self.assertEqual(validate_runtime_invariants(), ())


if __name__ == "__main__":
    unittest.main(verbosity=2)
