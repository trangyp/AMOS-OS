import unittest

import canon_admission_gate as g


def good_evidence(**overrides):
    data = dict(
        candidate_id="c-1",
        source_id="drive:reasoning-kernel",
        source_version="rev-1",
        source_hash="src-h1",
        source_resolved=True,
        provenance_traceable=True,
        semantics_typed=True,
        assumptions_bound=True,
        contradiction_free=True,
        math_claim=True,
        equations_checked=True,
        counterexamples_checked=True,
        implementation_claim=True,
        implementation_receipt="receipt-1",
        confidence=0.99,
    )
    data.update(overrides)
    return g.CandidateEvidence(**data)


def context(policy="policy-h1", baseline_hash="base-h1"):
    return g.AdmissionContext(policy, "AMOS_CORE:v4.4", baseline_hash)


def authority(policy="policy-h1", scopes=None, authority_id="auth-1"):
    return g.AuthorityWitness(
        authority_id=authority_id,
        principal="Trang Phan",
        scopes=frozenset(scopes or {g.CANON_PROMOTE_SCOPE}),
        policy_hash=policy,
    )


class CanonAdmissionGateTests(unittest.TestCase):
    def test_high_confidence_never_compensates_for_missing_evidence(self):
        ev = good_evidence(provenance_traceable=False, confidence=1.0)
        r = g.prepare_admission(ev, context(), authority())
        self.assertEqual(r.decision, g.AdmissionDecision.HOLD_FOR_EVIDENCE)
        self.assertIn("provenance_traceable", r.reasons)

    def test_competing_claim_is_preserved_before_promotion(self):
        r = g.prepare_admission(good_evidence(unresolved_competing=True), context(), authority())
        self.assertEqual(r.decision, g.AdmissionDecision.COMPETING)

    def test_unresolved_contradiction_quarantines(self):
        r = g.prepare_admission(good_evidence(contradiction_free=False), context(), authority())
        self.assertEqual(r.decision, g.AdmissionDecision.QUARANTINE)

    def test_math_claim_requires_equation_and_counterexample_checks(self):
        r = g.prepare_admission(
            good_evidence(equations_checked=False, counterexamples_checked=False),
            context(),
            authority(),
        )
        self.assertEqual(r.decision, g.AdmissionDecision.HOLD_FOR_EVIDENCE)
        self.assertEqual(set(r.reasons), {"equations_checked", "counterexamples_checked"})

    def test_implementation_claim_requires_receipt(self):
        r = g.prepare_admission(good_evidence(implementation_receipt=None), context(), authority())
        self.assertEqual(r.decision, g.AdmissionDecision.HOLD_FOR_EVIDENCE)
        self.assertIn("implementation_receipt", r.reasons)

    def test_evidence_without_authority_cannot_prepare_promotion(self):
        r = g.prepare_admission(good_evidence(), context(), None)
        self.assertEqual(r.decision, g.AdmissionDecision.BLOCK_AUTHORITY)

    def test_authority_must_bind_current_policy(self):
        r = g.prepare_admission(good_evidence(), context("policy-h2"), authority("policy-h1"))
        self.assertEqual(r.decision, g.AdmissionDecision.BLOCK_AUTHORITY)

    def test_full_prepare_then_commit_is_committable(self):
        ctx = context()
        auth = authority()
        prepared = g.prepare_admission(good_evidence(), ctx, auth)
        self.assertEqual(prepared.decision, g.AdmissionDecision.PREPARED_FOR_COMMIT)
        r = g.commit_guard(
            prepared.prepared,
            current_source_hash="src-h1",
            current_context=ctx,
            current_authority=auth,
        )
        self.assertEqual(r.decision, g.AdmissionDecision.COMMITTABLE)

    def test_source_change_after_prepare_forces_revalidation(self):
        ctx = context()
        auth = authority()
        prepared = g.prepare_admission(good_evidence(), ctx, auth).prepared
        r = g.commit_guard(
            prepared,
            current_source_hash="src-h2",
            current_context=ctx,
            current_authority=auth,
        )
        self.assertEqual(r.decision, g.AdmissionDecision.REVALIDATE_SOURCE)

    def test_policy_change_after_prepare_forces_revalidation(self):
        ctx = context()
        auth = authority()
        prepared = g.prepare_admission(good_evidence(), ctx, auth).prepared
        r = g.commit_guard(
            prepared,
            current_source_hash="src-h1",
            current_context=context("policy-h2"),
            current_authority=authority("policy-h2"),
        )
        self.assertEqual(r.decision, g.AdmissionDecision.REVALIDATE_POLICY)

    def test_baseline_change_after_prepare_forces_revalidation(self):
        ctx = context()
        auth = authority()
        prepared = g.prepare_admission(good_evidence(), ctx, auth).prepared
        r = g.commit_guard(
            prepared,
            current_source_hash="src-h1",
            current_context=context(baseline_hash="base-h2"),
            current_authority=auth,
        )
        self.assertEqual(r.decision, g.AdmissionDecision.REVALIDATE_BASELINE)

    def test_authority_change_after_prepare_forces_revalidation(self):
        ctx = context()
        auth = authority()
        prepared = g.prepare_admission(good_evidence(), ctx, auth).prepared
        r = g.commit_guard(
            prepared,
            current_source_hash="src-h1",
            current_context=ctx,
            current_authority=authority(authority_id="auth-2"),
        )
        self.assertEqual(r.decision, g.AdmissionDecision.REVALIDATE_AUTHORITY)


if __name__ == "__main__":
    unittest.main()
