import unittest

import causal_claim_runtime as c


class CausalClaimRuntimeTests(unittest.TestCase):
    def profile(self, classes, reverse=False):
        return c.CausalEvidenceProfile(
            frozenset(classes),
            ("e1",),
            "domain-a",
            "regime-1",
            "v1",
            reverse,
        )

    def claim(self, claim_class):
        return c.CausalClaim("X", "Y", claim_class, "domain-a", "regime-1", "v1")

    def test_association_does_not_license_mechanism(self):
        evidence = self.profile({
            c.CausalEvidenceClass.OBSERVATIONAL_ASSOCIATION,
            c.CausalEvidenceClass.SCALE_REGIME_BOUND,
        })
        association = c.validate_causal_claim(self.claim(c.CausalClaimClass.ASSOCIATION), evidence)
        mechanism = c.validate_causal_claim(self.claim(c.CausalClaimClass.MECHANISM), evidence)
        self.assertTrue(association.supported)
        self.assertFalse(mechanism.supported)
        self.assertIn("MECHANISM_EVIDENCE", mechanism.missing)

    def test_temporal_precedence_does_not_license_effect(self):
        evidence = self.profile({
            c.CausalEvidenceClass.TEMPORAL_ORDER,
            c.CausalEvidenceClass.SCALE_REGIME_BOUND,
        })
        self.assertTrue(
            c.validate_causal_claim(self.claim(c.CausalClaimClass.TEMPORAL_PRECEDENCE), evidence).supported
        )
        self.assertFalse(
            c.validate_causal_claim(self.claim(c.CausalClaimClass.INTERVENTION_EFFECT), evidence).supported
        )

    def test_graph_reachability_alone_is_explicitly_rejected(self):
        evidence = self.profile({c.CausalEvidenceClass.GRAPH_REACHABILITY_ONLY})
        result = c.validate_causal_claim(self.claim(c.CausalClaimClass.ASSOCIATION), evidence)
        self.assertFalse(result.supported)
        self.assertIn("GRAPH_REACHABILITY_IS_NOT_CAUSAL_EVIDENCE", result.blockers)

    def test_model_fit_alone_is_not_causal_identification(self):
        evidence = self.profile({c.CausalEvidenceClass.MODEL_FIT_ONLY})
        result = c.validate_causal_claim(self.claim(c.CausalClaimClass.MECHANISM), evidence)
        self.assertFalse(result.supported)
        self.assertIn("MODEL_FIT_IS_NOT_CAUSAL_IDENTIFICATION", result.blockers)

    def test_mechanism_requires_direction_and_identification(self):
        evidence = self.profile({
            c.CausalEvidenceClass.TEMPORAL_ORDER,
            c.CausalEvidenceClass.MECHANISM_EVIDENCE,
            c.CausalEvidenceClass.DIRECTION_DISCRIMINATION,
            c.CausalEvidenceClass.IDENTIFICATION_ASSUMPTIONS,
            c.CausalEvidenceClass.SCALE_REGIME_BOUND,
        })
        self.assertTrue(c.validate_causal_claim(self.claim(c.CausalClaimClass.MECHANISM), evidence).supported)

    def test_reverse_causation_blocks_effectish_claim_even_with_other_evidence(self):
        evidence = self.profile({
            c.CausalEvidenceClass.TEMPORAL_ORDER,
            c.CausalEvidenceClass.MECHANISM_EVIDENCE,
            c.CausalEvidenceClass.DIRECTION_DISCRIMINATION,
            c.CausalEvidenceClass.IDENTIFICATION_ASSUMPTIONS,
            c.CausalEvidenceClass.SCALE_REGIME_BOUND,
        }, reverse=True)
        result = c.validate_causal_claim(self.claim(c.CausalClaimClass.MECHANISM), evidence)
        self.assertFalse(result.supported)
        self.assertIn("REVERSE_CAUSATION_UNRESOLVED", result.blockers)

    def test_intervention_effect_requires_intervention_or_natural_experiment(self):
        base = {
            c.CausalEvidenceClass.DIRECTION_DISCRIMINATION,
            c.CausalEvidenceClass.IDENTIFICATION_ASSUMPTIONS,
            c.CausalEvidenceClass.SCALE_REGIME_BOUND,
        }
        missing_design = c.validate_causal_claim(
            self.claim(c.CausalClaimClass.INTERVENTION_EFFECT), self.profile(base)
        )
        self.assertFalse(missing_design.supported)
        self.assertIn("INTERVENTION_OR_NATURAL_EXPERIMENT_REQUIRED", missing_design.blockers)

        interventional = c.validate_causal_claim(
            self.claim(c.CausalClaimClass.INTERVENTION_EFFECT),
            self.profile(base | {c.CausalEvidenceClass.INTERVENTION}),
        )
        self.assertTrue(interventional.supported)

        natural = c.validate_causal_claim(
            self.claim(c.CausalClaimClass.INTERVENTION_EFFECT),
            self.profile(base | {c.CausalEvidenceClass.NATURAL_EXPERIMENT}),
        )
        self.assertTrue(natural.supported)

    def test_necessary_and_sufficient_are_separate_not_total_order(self):
        necessary_evidence = self.profile({
            c.CausalEvidenceClass.NECESSITY_TEST,
            c.CausalEvidenceClass.DIRECTION_DISCRIMINATION,
            c.CausalEvidenceClass.SCALE_REGIME_BOUND,
        })
        licensed = c.licensed_claim_classes(necessary_evidence)
        self.assertIn(c.CausalClaimClass.NECESSARY_CONDITION, licensed)
        self.assertNotIn(c.CausalClaimClass.SUFFICIENT_CONDITION, licensed)

    def test_mediator_and_confounder_roles_require_distinct_evidence(self):
        mediator_evidence = self.profile({
            c.CausalEvidenceClass.MEDIATION_ASSESSMENT,
            c.CausalEvidenceClass.IDENTIFICATION_ASSUMPTIONS,
            c.CausalEvidenceClass.SCALE_REGIME_BOUND,
        })
        licensed = c.licensed_claim_classes(mediator_evidence)
        self.assertIn(c.CausalClaimClass.MEDIATOR, licensed)
        self.assertNotIn(c.CausalClaimClass.CONFOUNDER, licensed)

    def test_scope_regime_and_state_version_mismatch_fail_closed(self):
        evidence = self.profile({
            c.CausalEvidenceClass.OBSERVATIONAL_ASSOCIATION,
            c.CausalEvidenceClass.SCALE_REGIME_BOUND,
        })
        mismatched = c.CausalClaim("X", "Y", c.CausalClaimClass.ASSOCIATION, "other", "regime-1", "v2")
        result = c.validate_causal_claim(mismatched, evidence)
        self.assertFalse(result.supported)
        self.assertIn("SCOPE_MISMATCH", result.blockers)
        self.assertIn("STATE_VERSION_MISMATCH", result.blockers)

    def test_validation_result_never_contains_authority(self):
        evidence = self.profile({
            c.CausalEvidenceClass.OBSERVATIONAL_ASSOCIATION,
            c.CausalEvidenceClass.SCALE_REGIME_BOUND,
        })
        result = c.validate_causal_claim(self.claim(c.CausalClaimClass.ASSOCIATION), evidence)
        self.assertFalse(hasattr(result, "authority"))


if __name__ == "__main__":
    unittest.main()
