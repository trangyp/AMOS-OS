import itertools
import cognitive_matrix_routing_runtime as r


def req(kind, **kw):
    base=dict(request_id='q',query_kind=kind,scope='reference',regime='active')
    base.update(kw)
    return r.RouteRequest(**base)


def test_all_eight_bounded_subfragments_route_from_registry():
    kinds=(
        r.QueryKind.CLASSICAL_INFERENCE,
        r.QueryKind.FIRST_ORDER_TERM_UNIFICATION,
        r.QueryKind.TEMPORAL_FINITE_TRACE_CHECK,
        r.QueryKind.MODAL_K_FINITE_MODEL_CHECK,
        r.QueryKind.DUNG_ABSTRACT_FRAMEWORK_CHECK,
        r.QueryKind.DEPENDENT_PI_TYPE_CHECK,
        r.QueryKind.QUANTUM_FINITE_DIMENSIONAL_OPERATOR,
        r.QueryKind.FINITE_CATEGORY_HEYTING_CHECK,
    )
    cands=r.reference_candidates()
    for kind in kinds:
        out=r.route(req(kind),cands)
        assert out.status is r.RouteStatus.ROUTED, (kind,out)


def test_generic_full_fragments_do_not_inherit_subfragment_execution():
    cands=r.reference_candidates()
    for kind in (
        r.QueryKind.FIRST_ORDER_THEOREM_PROVING,
        r.QueryKind.TEMPORAL_MODEL_CHECK,
        r.QueryKind.EPISTEMIC_MODAL,
        r.QueryKind.NON_MONOTONIC,
        r.QueryKind.DEPENDENT_TYPE,
        r.QueryKind.QUANTUM_LOGIC,
        r.QueryKind.CATEGORICAL_TOPOS,
    ):
        assert r.route(req(kind),cands).status is r.RouteStatus.DENY


def test_effect_authority_firewall():
    cands=r.reference_candidates()
    noauth=r.route(req(r.QueryKind.CLASSICAL_INFERENCE,effectful=True),cands)
    assert noauth.status is r.RouteStatus.AUTHORITY_REQUIRED
    auth=r.route(req(r.QueryKind.CLASSICAL_INFERENCE,effectful=True,authority_bound=True),cands)
    assert auth.status is r.RouteStatus.PROPOSAL_ONLY and not auth.commit_authorized


def test_explicit_target_no_fallback():
    cands=r.reference_candidates()
    out=r.route(req(r.QueryKind.CLASSICAL_INFERENCE,explicit_target='missing'),cands)
    assert out.status is r.RouteStatus.DENY


def test_scope_regime_and_validation_are_hard_gates():
    cands=r.reference_candidates()
    assert r.route(r.RouteRequest('q',r.QueryKind.CLASSICAL_INFERENCE,'wrong','active'),cands).status is r.RouteStatus.DENY
    c=cands[0]
    bad=r.RouteCandidate(c.target_id,c.query_kinds,c.scopes,c.regimes,c.capabilities,False,c.policy_priority,c.specialist,c.source_version,c.ulk_fragment,c.provenance_roots,c.epoch_dependencies)
    assert r.route(req(r.QueryKind.CLASSICAL_INFERENCE),(bad,)).status is r.RouteStatus.DENY


def test_epoch_selective_freshness():
    c=r.RouteCandidate('x',(r.QueryKind.GENERIC,),('reference',),('active',),(),True,1,True,'v',None,('root',),(r.EpochBinding('state','1'),))
    assert r.route(req(r.QueryKind.GENERIC,current_epochs=(r.EpochBinding('state','1'),)),(c,)).status is r.RouteStatus.ROUTED
    assert r.route(req(r.QueryKind.GENERIC,current_epochs=(r.EpochBinding('policy','1'),)),(c,)).status is r.RouteStatus.DENY


def test_independent_roots_are_unique():
    c=r.RouteCandidate('x',(r.QueryKind.GENERIC,),('reference',),('active',),(),True,1,True,'v',None,('same','same'))
    assert r.route(req(r.QueryKind.GENERIC,min_independent_evidence_roots=2),(c,)).status is r.RouteStatus.DENY


def test_registration_order_is_nonsemantic():
    cands=r.reference_candidates()
    baseline=r.route(req(r.QueryKind.CLASSICAL_INFERENCE),cands)
    for perm in itertools.islice(itertools.permutations(cands),50):
        out=r.route(req(r.QueryKind.CLASSICAL_INFERENCE),perm)
        assert (out.status,out.target_id)==(baseline.status,baseline.target_id)


def test_equal_best_routes_remain_ambiguous():
    base=r.reference_candidates()[0]
    alt=r.RouteCandidate('alt',base.query_kinds,base.scopes,base.regimes,base.capabilities,True,base.policy_priority,base.specialist,'v',base.ulk_fragment,('other',))
    out=r.route(req(r.QueryKind.CLASSICAL_INFERENCE),(base,alt))
    assert out.status is r.RouteStatus.AMBIGUOUS
