from classical_sat_firewall import BoolFormula, pairwise_compatible
from core19_runtime import LogicFragment, P02BindingRegistry, P02Candidate
from inference_runtime import (
    InferenceRequest,
    InferenceStatus,
    Premise,
    evaluate_inference,
)


def p(claim_id: str, formula: BoolFormula, confidence: float = 0.9) -> Premise:
    return Premise(claim_id, formula, f"test:{claim_id}", confidence)


def test_modus_ponens_is_verified_bounded():
    a = BoolFormula.atom("A")
    b = BoolFormula.atom("B")
    req = InferenceRequest(
        fragment=LogicFragment.CLASSICAL_PROPOSITIONAL,
        premises=(p("p1", a, 0.8), p("p2", BoolFormula.implies(a, b), 0.7)),
        conclusion=b,
    )
    result = evaluate_inference(req)
    assert result.status is InferenceStatus.VERIFIED_BOUNDED
    assert result.entailed is True
    assert result.globally_consistent is True
    assert result.confidence_ceiling == 0.7


def test_non_entailment_preserves_countermodel_status():
    a = BoolFormula.atom("A")
    b = BoolFormula.atom("B")
    req = InferenceRequest(
        fragment=LogicFragment.CLASSICAL_PROPOSITIONAL,
        premises=(p("p1", a),),
        conclusion=b,
    )
    result = evaluate_inference(req)
    assert result.status is InferenceStatus.NOT_ENTAILED
    assert result.entailed is False


def test_pairwise_compatibility_is_not_global_consistency():
    a = BoolFormula.atom("A")
    b = BoolFormula.atom("B")
    formulas = (a, b, BoolFormula.not_(BoolFormula.and_(a, b)))
    assert pairwise_compatible(formulas)
    req = InferenceRequest(
        fragment=LogicFragment.CLASSICAL_PROPOSITIONAL,
        premises=tuple(p(f"p{i}", f) for i, f in enumerate(formulas)),
    )
    result = evaluate_inference(req)
    assert result.status is InferenceStatus.INCONSISTENT_INPUT
    assert result.globally_consistent is False


def test_specification_only_fragment_fails_closed():
    a = BoolFormula.atom("A")
    req = InferenceRequest(
        fragment=LogicFragment.TEMPORAL_LTL,
        premises=(p("p1", a),),
        conclusion=a,
    )
    result = evaluate_inference(req)
    assert result.status is InferenceStatus.UNKNOWN_GAP
    assert "specification-only" in result.reason


def test_quantum_fragment_reports_rebind_pending():
    a = BoolFormula.atom("A")
    req = InferenceRequest(
        fragment=LogicFragment.QUANTUM_LOGIC,
        premises=(p("p1", a),),
        conclusion=a,
    )
    result = evaluate_inference(req)
    assert result.status is InferenceStatus.UNKNOWN_GAP
    assert "rebind-pending" in result.reason


def test_p02_use_without_binding_is_competing():
    a = BoolFormula.atom("A")
    req = InferenceRequest(
        fragment=LogicFragment.CLASSICAL_PROPOSITIONAL,
        premises=(p("p1", a),),
        conclusion=a,
        uses_p02=True,
    )
    result = evaluate_inference(req)
    assert result.status is InferenceStatus.COMPETING


def test_p02_resolved_namespace_allows_local_inference():
    a = BoolFormula.atom("A")
    registry = P02BindingRegistry()
    registry.bind("recovered_living_map", "2026-09-14", P02Candidate.DISTINCTION)
    req = InferenceRequest(
        fragment=LogicFragment.CLASSICAL_PROPOSITIONAL,
        premises=(p("p1", a),),
        conclusion=a,
        uses_p02=True,
        p02_namespace="recovered_living_map",
        p02_version="2026-09-14",
    )
    result = evaluate_inference(req, p02_registry=registry)
    assert result.status is InferenceStatus.VERIFIED_BOUNDED


def test_causal_claim_without_causal_evidence_fails_closed():
    a = BoolFormula.atom("A")
    req = InferenceRequest(
        fragment=LogicFragment.CLASSICAL_PROPOSITIONAL,
        premises=(p("p1", a),),
        conclusion=a,
        causal_claim=True,
        causal_evidence_bound=False,
    )
    result = evaluate_inference(req)
    assert result.status is InferenceStatus.UNKNOWN_GAP
    assert "causation" in result.reason


def test_missing_confidence_keeps_ceiling_unknown():
    a = BoolFormula.atom("A")
    premise = Premise("p1", a, "test:p1", None)
    req = InferenceRequest(
        fragment=LogicFragment.CLASSICAL_PROPOSITIONAL,
        premises=(premise,),
        conclusion=a,
    )
    result = evaluate_inference(req)
    assert result.status is InferenceStatus.VERIFIED_BOUNDED
    assert result.confidence_ceiling is None


def test_atom_bound_fails_closed_as_unknown_gap():
    atoms = tuple(BoolFormula.atom(f"A{i}") for i in range(4))
    req = InferenceRequest(
        fragment=LogicFragment.CLASSICAL_PROPOSITIONAL,
        premises=tuple(p(f"p{i}", atom) for i, atom in enumerate(atoms)),
        conclusion=atoms[0],
    )
    result = evaluate_inference(req, max_atoms=3)
    assert result.status is InferenceStatus.UNKNOWN_GAP
    assert "at most 3" in result.reason
