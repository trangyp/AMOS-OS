import unittest
import cognitive_matrix_routing_runtime as r


def cand(name="c", *, kinds=(r.QueryKind.GENERIC,), scopes=("s",), regimes=("r",), caps=(), state=r.ImplementationState.EXECUTABLE_BOUNDED, validated=True, priority=10, specialist=True, roots=("root",), epochs=()):
    return r.RouteCandidate(name,kinds,scopes,regimes,caps,state,validated,priority,specialist,"v1",roots,epochs)

def req(*, kind=r.QueryKind.GENERIC, scope="s", regime="r", caps=(), explicit=None, premise=r.PremiseState.PASS, epochs=(), min_roots=0, effectful=False, authority=False):
    return r.RouteRequest("q",kind,scope,regime,caps,explicit,premise,epochs,min_roots,effectful,authority)

class RoutingTests(unittest.TestCase):
    def test_specialist_beats_default_despite_registration_order(self):
        default=cand("default",priority=10,specialist=False)
        specialist=cand("specialist",priority=10,specialist=True)
        self.assertEqual(r.route(req(),(default,specialist)).target_id,"specialist")
        self.assertEqual(r.route(req(),(specialist,default)).target_id,"specialist")

    def test_explicit_missing_denies_no_fallback(self):
        d=r.route(req(explicit="missing"),(cand("default"),))
        self.assertEqual(d.status,r.RouteStatus.DENY)

    def test_equal_specialists_preserve_ambiguity(self):
        d=r.route(req(),(cand("a"),cand("b")))
        self.assertEqual(d.status,r.RouteStatus.AMBIGUOUS)

    def test_unknown_premise_fails_closed(self):
        self.assertEqual(r.route(req(premise=r.PremiseState.UNKNOWN_GAP),(cand(),)).status,r.RouteStatus.UNKNOWN_GAP)

    def test_failed_premise_denies(self):
        self.assertEqual(r.route(req(premise=r.PremiseState.FAIL),(cand(),)).status,r.RouteStatus.DENY)

    def test_wrong_regime_denied(self):
        self.assertEqual(r.route(req(regime="other"),(cand(),)).status,r.RouteStatus.DENY)

    def test_stale_load_bearing_epoch_denied(self):
        c=cand(epochs=(r.EpochBinding("policy","e1"),))
        d=r.route(req(epochs=(r.EpochBinding("policy","e2"),)),(c,))
        self.assertEqual(d.status,r.RouteStatus.DENY)
        self.assertIn("STALE_EPOCH",d.rejected[0][1])

    def test_unrelated_epoch_change_does_not_invalidate(self):
        c=cand(epochs=(r.EpochBinding("policy","e1"),))
        d=r.route(req(epochs=(r.EpochBinding("policy","e1"),r.EpochBinding("unrelated","e9"))),(c,))
        self.assertEqual(d.status,r.RouteStatus.ROUTED)

    def test_unvalidated_candidate_blocked(self):
        self.assertEqual(r.route(req(),(cand(validated=False),)).status,r.RouteStatus.DENY)

    def test_capability_without_authority(self):
        c=cand(caps=("write",))
        d=r.route(req(caps=("write",),effectful=True,authority=False),(c,))
        self.assertEqual(d.status,r.RouteStatus.AUTHORITY_REQUIRED)

    def test_authority_still_only_produces_proposal(self):
        c=cand(caps=("write",))
        d=r.route(req(caps=("write",),effectful=True,authority=True),(c,))
        self.assertEqual(d.status,r.RouteStatus.PROPOSAL_ONLY)
        self.assertFalse(d.commit_authorized)

    def test_shared_provenance_root_does_not_count_twice(self):
        c=cand(roots=("same","same"))
        d=r.route(req(min_roots=2),(c,))
        self.assertEqual(d.status,r.RouteStatus.DENY)

    def test_distinct_roots_satisfy_explicit_threshold(self):
        c=cand(roots=("a","b","b"))
        d=r.route(req(min_roots=2),(c,))
        self.assertEqual(d.status,r.RouteStatus.ROUTED)
        self.assertEqual(d.independent_evidence_roots,2)

    def test_incapable_fallback_denied(self):
        c=cand("fallback",caps=("read",),specialist=False)
        d=r.route(req(caps=("security",)),(c,))
        self.assertEqual(d.status,r.RouteStatus.DENY)

    def test_hard_scope_dominates_priority(self):
        high=cand("high",scopes=("other",),priority=999)
        low=cand("low",scopes=("s",),priority=1)
        self.assertEqual(r.route(req(),(high,low)).target_id,"low")

    def test_wildcard_candidate_rejected_at_construction(self):
        with self.assertRaises(ValueError): cand(scopes=("*",))

    def test_duplicate_target_registry_fails_closed(self):
        d=r.route(req(),(cand("same"),cand("same")))
        self.assertEqual(d.status,r.RouteStatus.UNKNOWN_GAP)

    def test_classical_reference_route(self):
        cs=r.reference_candidates()
        d=r.route(req(kind=r.QueryKind.CLASSICAL_INFERENCE,scope="reference",regime="active",caps=("ULK_CLASSICAL_PROPOSITIONAL",)),cs)
        self.assertEqual(d.status,r.RouteStatus.ROUTED)
        self.assertEqual(d.target_id,"classical-propositional-runtime")

    def test_alu02_bounded_unification_route(self):
        cs=r.reference_candidates()
        d=r.route(req(kind=r.QueryKind.FIRST_ORDER_TERM_UNIFICATION,scope="reference",regime="active",caps=("ULK_ALU02_UNIFICATION",)),cs)
        self.assertEqual(d.status,r.RouteStatus.ROUTED)
        self.assertEqual(d.target_id,"alu02-unification-runtime")

    def test_full_fol_theorem_proving_remains_unimplemented(self):
        cs=r.reference_candidates()
        d=r.route(req(kind=r.QueryKind.FIRST_ORDER_THEOREM_PROVING,scope="reference",regime="active"),cs)
        self.assertEqual(d.status,r.RouteStatus.DENY)

    def test_quantum_rebind_pending_visible(self):
        cs=r.reference_candidates()
        q=req(kind=r.QueryKind.QUANTUM_LOGIC,scope="reference",regime="active",caps=("ULK_ALU07_QUANTUM",),explicit="quantum-alu07-placeholder")
        self.assertEqual(r.route(q,cs).status,r.RouteStatus.REBIND_REQUIRED)

    def test_explicit_spec_only_target_does_not_fallback(self):
        spec=cand("spec",state=r.ImplementationState.SPECIFICATION_ONLY)
        fallback=cand("fallback",specialist=False)
        d=r.route(req(explicit="spec"),(spec,fallback))
        self.assertEqual(d.status,r.RouteStatus.DENY)
        self.assertEqual(d.target_id,None)

    def test_explicit_rebind_pending_returns_rebind_required_when_validated_profile_is_pending(self):
        c=cand("q",state=r.ImplementationState.REBIND_PENDING,validated=True)
        d=r.route(req(explicit="q"),(c,))
        self.assertEqual(d.status,r.RouteStatus.REBIND_REQUIRED)

    def test_higher_policy_priority_beats_specialist_flag(self):
        a=cand("a",priority=100,specialist=False)
        b=cand("b",priority=99,specialist=True)
        self.assertEqual(r.route(req(),(a,b)).target_id,"a")

if __name__=="__main__": unittest.main()
