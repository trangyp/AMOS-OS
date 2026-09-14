import pytest

from cognitive_matrix_cell_runtime import (
    CellBinding,
    CellCoordinate,
    CellEvidence,
    CellRecord,
    CellStatus,
    EvidenceClass,
    TransformContract,
    independent_provenance_roots,
    validate_cell,
    validate_transform,
)


def coord(regime="r1"):
    return CellCoordinate("P01", "logic", "ctx", "t1", "L", "observer", regime)


def evidence(eid="e1", root="root1", *, fresh=True, execution=False, proof=False):
    return CellEvidence(
        eid,
        EvidenceClass.EXECUTION if execution else EvidenceClass.SOURCE,
        f"source:{eid}",
        root,
        "v1",
        fresh=fresh,
        execution_receipt=execution,
        formal_proof_receipt=proof,
    )


def binding(authority=None, runtime="runtime"):
    return CellBinding("cell", "semantic-owner", runtime, authority)


def test_unbound_cell_preserves_unknown_not_zero():
    record = CellRecord("cell", coord(), CellStatus.UNBOUND, None, None, None, None)
    result = validate_cell(record, binding(runtime=None))
    assert result.valid


def test_unbound_cell_rejects_numeric_zero_as_fabricated_value():
    record = CellRecord("cell", coord(), CellStatus.UNBOUND, 0, None, None, None)
    result = validate_cell(record, binding(runtime=None))
    assert not result.valid
    assert "UNBOUND_MUST_NOT_CARRY_VALUE" in result.errors


def test_bound_cell_requires_provenance_and_version():
    record = CellRecord("cell", coord(), CellStatus.AMOS_MODEL, 1.0, "u", None, None)
    result = validate_cell(record, binding())
    assert not result.valid
    assert "BOUND_CELL_REQUIRES_PROVENANCE" in result.errors
    assert "BOUND_CELL_REQUIRES_SOURCE_VERSION" in result.errors


def test_verified_bounded_requires_fresh_execution_or_formal_receipt():
    record = CellRecord("cell", coord(), CellStatus.VERIFIED_BOUNDED, True, None, "p", "v1", (evidence(),))
    result = validate_cell(record, binding())
    assert not result.valid
    assert "VERIFIED_BOUNDED_REQUIRES_FRESH_RECEIPT" in result.errors


def test_verified_bounded_accepts_fresh_execution_receipt():
    record = CellRecord("cell", coord(), CellStatus.VERIFIED_BOUNDED, True, None, "p", "v1", (evidence(execution=True),))
    result = validate_cell(record, binding())
    assert result.valid


def test_competing_requires_two_provenance_roots():
    record = CellRecord("cell", coord(), CellStatus.COMPETING, "x", None, "p", "v1", (evidence("e1", "same"), evidence("e2", "same")))
    result = validate_cell(record, binding())
    assert not result.valid
    assert "COMPETING_REQUIRES_AT_LEAST_TWO_PROVENANCE_ROOTS" in result.errors


def test_distinct_provenance_roots_are_counted_without_claiming_independence_proof():
    ev = (evidence("e1", "r1"), evidence("e2", "r2"))
    assert independent_provenance_roots(ev) == 2
    record = CellRecord("cell", coord(), CellStatus.COMPETING, "x", None, "p", "v1", ev)
    assert validate_cell(record, binding()).valid


def test_stale_evidence_blocks_active_cell_but_is_allowed_in_stale_state():
    ev = (evidence(fresh=False),)
    active = CellRecord("cell", coord(), CellStatus.DERIVED, "x", None, "p", "v1", ev)
    stale = CellRecord("cell", coord(), CellStatus.STALE, "x", None, "p", "v1", ev)
    assert "ACTIVE_CELL_CARRIES_STALE_EVIDENCE" in validate_cell(active, binding()).errors
    assert validate_cell(stale, binding()).valid


def test_runtime_capability_does_not_create_effect_authority():
    result = validate_cell(CellRecord("cell", coord(), CellStatus.AMOS_MODEL, "x", None, "p", "v1"), binding(authority=None, runtime="runtime"))
    assert result.valid
    assert result.effect_authority_bound is False


def test_explicit_authority_binding_is_separate_from_runtime_owner():
    result = validate_cell(CellRecord("cell", coord(), CellStatus.AMOS_MODEL, "x", None, "p", "v1"), binding(authority="control-plane", runtime="runtime"))
    assert result.valid
    assert result.effect_authority_bound is True


def test_transform_rejects_provenance_erasure_cross_regime_without_mapping_and_unknown_to_zero():
    errors = validate_transform(TransformContract("r1", "r2", False, False, True))
    assert "TRANSFORM_ERASES_PROVENANCE" in errors
    assert "CROSS_REGIME_MAPPING_UNDECLARED" in errors
    assert "UNKNOWN_TO_ZERO_FORBIDDEN" in errors


def test_tensor_coordinate_axes_are_required():
    with pytest.raises(ValueError):
        CellCoordinate("P01", "logic", "ctx", "t1", "", "observer", "r1")
