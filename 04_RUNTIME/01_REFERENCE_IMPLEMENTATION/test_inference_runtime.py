from classical_sat_firewall import BoolFormula, pairwise_compatible
from core19_runtime import LogicFragment, P02BindingRegistry, P02Candidate
from inference_runtime import InferenceRequest, InferenceStatus, Premise, evaluate_inference


def p(claim_id,formula,confidence=0.9): return Premise(claim_id,formula,f'test:{claim_id}',confidence)


def test_modus_ponens_is_verified_bounded():
    a=BoolFormula.atom('A'); b=BoolFormula.atom('B'); r=evaluate_inference(InferenceRequest(LogicFragment.CLASSICAL_PROPOSITIONAL,(p('p1',a,0.8),p('p2',BoolFormula.implies(a,b),0.7)),b)); assert r.status is InferenceStatus.VERIFIED_BOUNDED and r.entailed and r.confidence_ceiling==0.7


def test_non_entailment_preserves_countermodel_status():
    a=BoolFormula.atom('A'); b=BoolFormula.atom('B'); r=evaluate_inference(InferenceRequest(LogicFragment.CLASSICAL_PROPOSITIONAL,(p('p1',a),),b)); assert r.status is InferenceStatus.NOT_ENTAILED and r.entailed is False


def test_pairwise_compatibility_is_not_global_consistency():
    a=BoolFormula.atom('A'); b=BoolFormula.atom('B'); fs=(a,b,BoolFormula.not_(BoolFormula.and_(a,b))); assert pairwise_compatible(fs); r=evaluate_inference(InferenceRequest(LogicFragment.CLASSICAL_PROPOSITIONAL,tuple(p(f'p{i}',f) for i,f in enumerate(fs)))); assert r.status is InferenceStatus.INCONSISTENT_INPUT and r.globally_consistent is False


def test_specialist_subfragment_does_not_leak_into_classical_l09_abi():
    a=BoolFormula.atom('A')
    for fragment in (LogicFragment.TEMPORAL_LTL, LogicFragment.QUANTUM_LOGIC, LogicFragment.FIRST_ORDER_UNIFICATION):
        r=evaluate_inference(InferenceRequest(fragment,(p('p1',a),),a))
        assert r.status is InferenceStatus.UNKNOWN_GAP
        assert 'specialist checker' in r.reason


def test_p02_use_without_binding_is_competing():
    a=BoolFormula.atom('A'); r=evaluate_inference(InferenceRequest(LogicFragment.CLASSICAL_PROPOSITIONAL,(p('p1',a),),a,uses_p02=True)); assert r.status is InferenceStatus.COMPETING


def test_p02_resolved_namespace_allows_local_inference():
    a=BoolFormula.atom('A'); reg=P02BindingRegistry(); reg.bind('recovered_living_map','2026-09-14',P02Candidate.DISTINCTION); r=evaluate_inference(InferenceRequest(LogicFragment.CLASSICAL_PROPOSITIONAL,(p('p1',a),),a,uses_p02=True,p02_namespace='recovered_living_map',p02_version='2026-09-14'),p02_registry=reg); assert r.status is InferenceStatus.VERIFIED_BOUNDED


def test_causal_claim_without_causal_evidence_fails_closed():
    a=BoolFormula.atom('A'); r=evaluate_inference(InferenceRequest(LogicFragment.CLASSICAL_PROPOSITIONAL,(p('p1',a),),a,causal_claim=True,causal_evidence_bound=False)); assert r.status is InferenceStatus.UNKNOWN_GAP and 'causation' in r.reason


def test_missing_confidence_keeps_ceiling_unknown():
    a=BoolFormula.atom('A'); pr=Premise('p1',a,'test:p1',None); r=evaluate_inference(InferenceRequest(LogicFragment.CLASSICAL_PROPOSITIONAL,(pr,),a)); assert r.status is InferenceStatus.VERIFIED_BOUNDED and r.confidence_ceiling is None


def test_atom_bound_fails_closed_as_unknown_gap():
    ats=tuple(BoolFormula.atom(f'A{i}') for i in range(4)); r=evaluate_inference(InferenceRequest(LogicFragment.CLASSICAL_PROPOSITIONAL,tuple(p(f'p{i}',a) for i,a in enumerate(ats)),ats[0]),max_atoms=3); assert r.status is InferenceStatus.UNKNOWN_GAP and 'at most 3' in r.reason
