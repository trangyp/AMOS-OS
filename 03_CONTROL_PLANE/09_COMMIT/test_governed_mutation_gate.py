import unittest

import governed_mutation_gate as g


def profile(**overrides):
    data = dict(
        mutation_class=g.MutationClass.M3,
        allowed_targets=frozenset({"reasoning-policy"}),
        evidence_threshold=g.EvidenceLevel.ET3,
        approval_authority=g.AuthorityLevel.HA3,
        propagation_limit=frozenset({"shadow", "canary"}),
        rollback_required=True,
        monitoring_window="24h",
        policy_hash="policy-h1",
    )
    data.update(overrides)
    return g.MutationPermissionProfile(**data)


def candidate(**overrides):
    data = dict(
        change_id="chg-1",
        change_hash="chg-h1",
        parent_hash="parent-h1",
        mutation_class=g.MutationClass.M3,
        target="reasoning-policy",
        current_state=g.Lifecycle.GOVERNANCE_REVIEW,
        proposed_state=g.Lifecycle.APPROVED_LIMITED,
        evidence_level=g.EvidenceLevel.ET3,
        invariants_passed=True,
        safety_passed=True,
        audit_complete=True,
        rollback_parent_hash="parent-h1",
        requested_propagation=frozenset({"canary"}),
        modifies_governance_boundary=False,
    )
    data.update(overrides)
    return g.MutationCandidate(**data)


def authority(**overrides):
    data = dict(
        authority_id="auth-1",
        level=g.AuthorityLevel.HA3,
        scopes=frozenset({g.MUTATION_APPROVE_SCOPE}),
        policy_hash="policy-h1",
    )
    data.update(overrides)
    return g.MutationAuthority(**data)


class GovernedMutationGateTests(unittest.TestCase):
    def test_m0_cannot_autonomously_mutate(self):
        r = g.prepare_mutation(
            candidate(mutation_class=g.MutationClass.M0),
            profile(mutation_class=g.MutationClass.M0),
            authority(level=g.AuthorityLevel.HA5),
        )
        self.assertEqual(r.decision, g.MutationDecision.ESCALATE_CONSTITUTIONAL)

    def test_candidate_cannot_rewrite_governance_used_to_judge_it(self):
        r = g.prepare_mutation(candidate(modifies_governance_boundary=True), profile(), authority())
        self.assertEqual(r.decision, g.MutationDecision.ESCALATE_CONSTITUTIONAL)

    def test_hidden_lifecycle_jump_blocks(self):
        r = g.prepare_mutation(
            candidate(current_state=g.Lifecycle.PROPOSED, proposed_state=g.Lifecycle.PRODUCTION_GENERAL),
            profile(),
            authority(),
        )
        self.assertEqual(r.decision, g.MutationDecision.BLOCK)
        self.assertIn("illegal_lifecycle_transition", r.reasons)

    def test_evidence_below_threshold_blocks(self):
        r = g.prepare_mutation(candidate(evidence_level=g.EvidenceLevel.ET2), profile(), authority())
        self.assertEqual(r.decision, g.MutationDecision.BLOCK)

    def test_senior_authority_and_high_evidence_do_not_compensate_safety_failure(self):
        r = g.prepare_mutation(
            candidate(evidence_level=g.EvidenceLevel.ET5, safety_passed=False),
            profile(),
            authority(level=g.AuthorityLevel.HA5),
        )
        self.assertEqual(r.decision, g.MutationDecision.BLOCK)
        self.assertIn("safety_gate_failed", r.reasons)

    def test_propagation_cannot_self_expand(self):
        r = g.prepare_mutation(
            candidate(requested_propagation=frozenset({"canary", "global"})),
            profile(),
            authority(),
        )
        self.assertEqual(r.decision, g.MutationDecision.BLOCK)
        self.assertIn("propagation_outside_envelope", r.reasons)

    def test_rollback_target_required(self):
        r = g.prepare_mutation(candidate(rollback_parent_hash=None), profile(), authority())
        self.assertEqual(r.decision, g.MutationDecision.BLOCK)
        self.assertIn("rollback_target_missing", r.reasons)

    def test_authority_level_and_scope_are_required(self):
        low = g.prepare_mutation(candidate(), profile(), authority(level=g.AuthorityLevel.HA2))
        self.assertEqual(low.decision, g.MutationDecision.HOLD)
        no_scope = g.prepare_mutation(candidate(), profile(), authority(scopes=frozenset()))
        self.assertEqual(no_scope.decision, g.MutationDecision.HOLD)

    def test_valid_prepare_and_fresh_commit_is_committable(self):
        auth = authority()
        p = g.prepare_mutation(candidate(), profile(), auth)
        self.assertEqual(p.decision, g.MutationDecision.PREPARED)
        r = g.commit_guard(
            p.prepared,
            current_change_hash="chg-h1",
            current_parent_hash="parent-h1",
            current_policy_hash="policy-h1",
            current_authority=auth,
        )
        self.assertEqual(r.decision, g.MutationDecision.COMMITTABLE)

    def test_candidate_change_after_prepare_forces_revalidation(self):
        auth = authority()
        p = g.prepare_mutation(candidate(), profile(), auth).prepared
        r = g.commit_guard(
            p,
            current_change_hash="chg-h2",
            current_parent_hash="parent-h1",
            current_policy_hash="policy-h1",
            current_authority=auth,
        )
        self.assertEqual(r.decision, g.MutationDecision.REVALIDATE)
        self.assertIn("change_hash_changed", r.reasons)

    def test_parent_or_policy_change_forces_revalidation(self):
        auth = authority()
        p = g.prepare_mutation(candidate(), profile(), auth).prepared
        r1 = g.commit_guard(
            p,
            current_change_hash="chg-h1",
            current_parent_hash="parent-h2",
            current_policy_hash="policy-h1",
            current_authority=auth,
        )
        self.assertEqual(r1.decision, g.MutationDecision.REVALIDATE)
        r2 = g.commit_guard(
            p,
            current_change_hash="chg-h1",
            current_parent_hash="parent-h1",
            current_policy_hash="policy-h2",
            current_authority=auth,
        )
        self.assertEqual(r2.decision, g.MutationDecision.REVALIDATE)

    def test_authority_downgrade_after_prepare_forces_revalidation(self):
        p = g.prepare_mutation(candidate(), profile(), authority()).prepared
        r = g.commit_guard(
            p,
            current_change_hash="chg-h1",
            current_parent_hash="parent-h1",
            current_policy_hash="policy-h1",
            current_authority=authority(level=g.AuthorityLevel.HA2),
        )
        self.assertEqual(r.decision, g.MutationDecision.REVALIDATE)
        self.assertIn("authority_level_downgraded", r.reasons)


if __name__ == "__main__":
    unittest.main()
