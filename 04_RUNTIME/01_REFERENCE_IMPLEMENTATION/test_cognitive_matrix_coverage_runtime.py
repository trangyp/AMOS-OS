import pytest

from cognitive_matrix_coverage_runtime import (
    ArtifactKind,
    CompletionStatus,
    CoverageRecord,
    CoverageScope,
    CoverageStage,
    Criticality,
    GapReason,
    ScopeRequirement,
    build_dependency_topology,
    evaluate_coverage,
    promote_record,
    validate_record,
)


def req(rid, stage=CoverageStage.CONTRACT_ONLY, criticality=Criticality.DECISION_RELEVANT, deps=()):
    return ScopeRequirement(rid, ArtifactKind.RUNTIME, stage, criticality, tuple(deps))


def rec(rid, stage, *, impl=False, valid=False, governed=False, provenance="repo:path", version="v1"):
    return CoverageRecord(
        rid,
        stage,
        provenance,
        version,
        implementation_receipt=impl,
        validation_receipt=valid,
        governance_receipt=governed,
    )


def scope(*requirements):
    return CoverageScope("cm-scope", "repair-2026-09-14", "v1", tuple(requirements))


def test_complete_for_scope_requires_stage_and_dependency_closure():
    s = scope(
        req("contract", CoverageStage.CONTRACT_ONLY),
        req("runtime", CoverageStage.IMPLEMENTED_BOUNDED, deps=("contract",)),
        req("validator", CoverageStage.VALIDATED_BOUNDED, deps=("runtime",)),
    )
    result = evaluate_coverage(s, (
        rec("contract", CoverageStage.CONTRACT_ONLY),
        rec("runtime", CoverageStage.IMPLEMENTED_BOUNDED, impl=True),
        rec("validator", CoverageStage.VALIDATED_BOUNDED, impl=True, valid=True),
    ))
    assert result.status is CompletionStatus.COMPLETE_FOR_SCOPE
    assert result.satisfied_count == 3
    assert result.gaps == ()


def test_contract_only_does_not_satisfy_implemented_requirement():
    result = evaluate_coverage(scope(req("runtime", CoverageStage.IMPLEMENTED_BOUNDED)),
                               (rec("runtime", CoverageStage.CONTRACT_ONLY),))
    assert result.status is CompletionStatus.INCOMPLETE
    assert result.gaps[0].reason is GapReason.BELOW_REQUIRED_STAGE


def test_missing_critical_requirement_is_known_incomplete():
    result = evaluate_coverage(scope(req("authority", CoverageStage.VALIDATED_BOUNDED, Criticality.CRITICAL)), ())
    assert result.status is CompletionStatus.INCOMPLETE
    assert result.gaps[0].reason is GapReason.MISSING


def test_stale_critical_requirement_preserves_unknown_gap():
    s = scope(req("authority", CoverageStage.VALIDATED_BOUNDED, Criticality.CRITICAL))
    result = evaluate_coverage(s, (rec("authority", CoverageStage.STALE),))
    assert result.status is CompletionStatus.UNKNOWN_GAP
    assert result.gaps[0].reason is GapReason.STALE


def test_falsified_requirement_makes_scope_contradictory():
    result = evaluate_coverage(scope(req("law", criticality=Criticality.EXPLANATORY)),
                               (rec("law", CoverageStage.FALSIFIED),))
    assert result.status is CompletionStatus.CONTRADICTORY


def test_only_cosmetic_gap_yields_conditional_not_complete():
    s = scope(
        req("runtime", CoverageStage.IMPLEMENTED_BOUNDED, Criticality.CRITICAL),
        req("readme", criticality=Criticality.COSMETIC),
    )
    result = evaluate_coverage(s, (rec("runtime", CoverageStage.IMPLEMENTED_BOUNDED, impl=True),))
    assert result.status is CompletionStatus.CONDITIONAL
    assert result.satisfied_requirements == ("runtime",)


def test_dependency_matrix_and_transitive_closure_are_directed_and_non_symmetric():
    topology = build_dependency_topology((req("a"), req("b", deps=("a",)), req("c", deps=("b",))))
    assert topology.adjacency == ((0, 0, 0), (1, 0, 0), (0, 1, 0))
    assert topology.closure == ((0, 0, 0), (1, 0, 0), (1, 1, 0))
    assert topology.downstream_fanout("a") == 2
    assert topology.downstream_fanout("c") == 0


def test_dependency_cycle_is_unknown_gap_not_silently_complete():
    s = scope(req("a", deps=("b",)), req("b", deps=("a",)))
    result = evaluate_coverage(s, (rec("a", CoverageStage.CONTRACT_ONLY), rec("b", CoverageStage.CONTRACT_ONLY)))
    assert result.status is CompletionStatus.UNKNOWN_GAP
    assert {gap.reason for gap in result.gaps} >= {GapReason.CYCLE}
    assert set(result.topology.cycle_nodes) == {"a", "b"}


def test_undeclared_dependency_blocks_scope_closure():
    result = evaluate_coverage(scope(req("runtime", deps=("external-authority",))),
                               (rec("runtime", CoverageStage.CONTRACT_ONLY),))
    assert result.status is CompletionStatus.UNKNOWN_GAP
    assert any(gap.reason is GapReason.UNDECLARED_DEPENDENCY for gap in result.gaps)


def test_dependency_gap_propagates_to_dependent_requirement():
    s = scope(req("base", CoverageStage.IMPLEMENTED_BOUNDED), req("dependent", deps=("base",)))
    result = evaluate_coverage(s, (rec("dependent", CoverageStage.CONTRACT_ONLY),))
    by_id = {(gap.requirement_id, gap.reason) for gap in result.gaps}
    assert result.status is CompletionStatus.INCOMPLETE
    assert ("base", GapReason.MISSING) in by_id
    assert ("dependent", GapReason.DEPENDENCY_GAP) in by_id


def test_validated_record_requires_implementation_and_validation_receipts():
    result = validate_record(rec("x", CoverageStage.VALIDATED_BOUNDED, impl=False, valid=True))
    assert not result.valid
    assert "IMPLEMENTED_STAGE_REQUIRES_IMPLEMENTATION_RECEIPT" in result.errors


def test_governed_record_requires_all_three_receipts():
    result = validate_record(rec("x", CoverageStage.GOVERNED_BOUNDED, impl=True, valid=True, governed=False))
    assert not result.valid
    assert "GOVERNED_STAGE_REQUIRES_GOVERNANCE_RECEIPT" in result.errors


def test_unbound_record_cannot_fake_source_or_receipts():
    record = CoverageRecord("x", CoverageStage.UNBOUND, "fake", "v1", implementation_receipt=True)
    result = validate_record(record)
    assert not result.valid
    assert "UNBOUND_MUST_NOT_FAKE_SOURCE_BINDING" in result.errors
    assert "UNBOUND_MUST_NOT_CARRY_PROMOTION_RECEIPTS" in result.errors


def test_duplicate_records_are_unresolved_not_double_evidence():
    s = scope(req("x"))
    result = evaluate_coverage(s, (
        rec("x", CoverageStage.CONTRACT_ONLY),
        rec("x", CoverageStage.IMPLEMENTED_BOUNDED, impl=True),
    ))
    assert result.status is CompletionStatus.UNKNOWN_GAP
    assert result.gaps[0].reason is GapReason.DUPLICATE_RECORD


def test_gap_priority_uses_criticality_then_fanout_not_file_order():
    s = scope(
        req("root", CoverageStage.IMPLEMENTED_BOUNDED, Criticality.CRITICAL),
        req("child", criticality=Criticality.CRITICAL, deps=("root",)),
        req("cosmetic", criticality=Criticality.COSMETIC),
    )
    result = evaluate_coverage(s, ())
    assert result.gaps[0].requirement_id == "root"
    assert result.gaps[0].downstream_fanout == 1


def test_promotion_fails_closed_without_required_receipts():
    record = rec("x", CoverageStage.CONTRACT_ONLY)
    result = promote_record(record, CoverageStage.VALIDATED_BOUNDED)
    assert not result.allowed
    assert "IMPLEMENTED_STAGE_REQUIRES_IMPLEMENTATION_RECEIPT" in result.errors
    assert result.record.stage is CoverageStage.CONTRACT_ONLY


def test_promotion_succeeds_when_required_receipts_are_already_bound():
    record = rec("x", CoverageStage.CONTRACT_ONLY, impl=True, valid=True)
    result = promote_record(record, CoverageStage.VALIDATED_BOUNDED)
    assert result.allowed
    assert result.record.stage is CoverageStage.VALIDATED_BOUNDED


def test_special_state_cannot_be_erased_by_promotion():
    result = promote_record(rec("x", CoverageStage.STALE, impl=True, valid=True), CoverageStage.VALIDATED_BOUNDED)
    assert not result.allowed
    assert result.errors == ("CURRENT_STAGE_REQUIRES_REEVIDENCING",)


def test_required_stage_must_be_active_not_special_state():
    with pytest.raises(ValueError):
        req("x", CoverageStage.STALE)
