import pytest

from world_model_runtime import (
    AssessmentStatus,
    FidelityEnvelope,
    RepresentationClass,
    RepresentationRecord,
    TensorCoordinate,
    assess_numeric_mismatch,
    independent_support,
    reality_contact,
)


def env():
    return FidelityEnvelope(
        validated_variables=frozenset({"temperature"}),
        validated_regimes=frozenset({"lab"}),
        validated_time_ids=frozenset({"t1"}),
        validated_measurement_methods=frozenset({"sensor-v1"}),
    )


def record(cls, *, value=10.0, unit="C", regime="lab", time_id="t1", method="sensor-v1", external=False, provenance="p1", root="root1", generator=None):
    return RepresentationRecord(
        object_id="obj",
        representation_class=cls,
        variable="temperature",
        value=value,
        unit=unit,
        measurement_method=method,
        time_id=time_id,
        regime=regime,
        provenance=provenance,
        provenance_root=root,
        scale="local",
        observer="test",
        validation_status="BOUNDED",
        consequence="none",
        external_observation_present=external,
        generator_id=generator,
    )


def test_observation_inside_fidelity_envelope_has_reality_contact():
    obs = record(RepresentationClass.OBSERVED_REALITY, external=True)
    assert reality_contact(obs, env())


def test_simulation_never_becomes_reality_contact_by_flag_alone():
    sim = record(RepresentationClass.SIMULATION, external=True)
    assert not reality_contact(sim, env())


def test_missing_measurement_method_blocks_reality_contact():
    obs = record(RepresentationClass.MEASURED_PROXY, external=True, method=None)
    assert not reality_contact(obs, env())


def test_numeric_mismatch_is_exact_absolute_difference():
    model = record(RepresentationClass.MODEL_STATE, value=12.5, provenance="model", root="model-root")
    obs = record(RepresentationClass.OBSERVED_REALITY, value=10.0, external=True, provenance="obs", root="obs-root")
    result = assess_numeric_mismatch(model, obs, env())
    assert result.status is AssessmentStatus.VERIFIED_BOUNDED
    assert result.absolute_error == 2.5


def test_tolerance_classification_preserves_discrepancy():
    model = record(RepresentationClass.FORECAST, value=12.5, provenance="model", root="model-root")
    obs = record(RepresentationClass.OBSERVED_REALITY, value=10.0, external=True, provenance="obs", root="obs-root")
    result = assess_numeric_mismatch(model, obs, env(), tolerance=2.0)
    assert result.status is AssessmentStatus.EXCEEDS_TOLERANCE
    assert result.absolute_error == 2.5


def test_unit_mismatch_returns_unknown_gap():
    model = record(RepresentationClass.MODEL_STATE, unit="K", provenance="model", root="model-root")
    obs = record(RepresentationClass.OBSERVED_REALITY, external=True, provenance="obs", root="obs-root")
    result = assess_numeric_mismatch(model, obs, env())
    assert result.status is AssessmentStatus.UNKNOWN_GAP
    assert result.absolute_error is None


def test_regime_mismatch_returns_unknown_gap():
    model = record(RepresentationClass.MODEL_STATE, regime="field", provenance="model", root="model-root")
    obs = record(RepresentationClass.OBSERVED_REALITY, external=True, provenance="obs", root="obs-root")
    result = assess_numeric_mismatch(model, obs, env())
    assert result.status is AssessmentStatus.UNKNOWN_GAP


def test_shared_provenance_root_is_not_independent_support():
    a = record(RepresentationClass.MODEL_STATE, provenance="a", root="shared")
    b = record(RepresentationClass.MEASURED_PROXY, external=True, provenance="b", root="shared")
    assert not independent_support(a, b)


def test_shared_generator_is_not_independent_support():
    a = record(RepresentationClass.MODEL_STATE, provenance="a", root="r1", generator="g")
    b = record(RepresentationClass.SYNTHETIC_DATA, provenance="b", root="r2", generator="g")
    assert not independent_support(a, b)


def test_tensor_coordinate_requires_explicit_axes():
    with pytest.raises(ValueError):
        TensorCoordinate(
            object_id="obj",
            representation_class=RepresentationClass.MODEL_STATE,
            variable="temperature",
            scale="",
            time_id="t1",
            regime="lab",
            observer="test",
            provenance="p",
            validation_status="MODEL",
            consequence="none",
        )
