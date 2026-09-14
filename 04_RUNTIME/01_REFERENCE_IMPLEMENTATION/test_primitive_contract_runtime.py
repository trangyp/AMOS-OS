import unittest

from cognitive_matrix_runtime import DependencyKind
from primitive_contract_runtime import (
    EpistemicClass,
    PrimitiveArtifact,
    PrimitiveDependency,
    PrimitiveId,
    build_primitive_dependency_graph,
    primitive_spec,
    validate_primitive_artifact,
    validate_primitive_registry,
)


class PrimitiveContractRuntimeTests(unittest.TestCase):
    def artifact(self, primitive=PrimitiveId.L09_INFERENCE, epistemic=EpistemicClass.DERIVED):
        return PrimitiveArtifact(
            artifact_id="a1",
            primitive=primitive,
            artifact_type="claim",
            epistemic_class=epistemic,
            state_version="s1",
            scope="test-scope",
            regime="test-regime",
            provenance_ids=("src-1",),
        )

    def test_exact_30_primitive_registry(self):
        self.assertEqual(len(PrimitiveId), 30)
        self.assertEqual(validate_primitive_registry(), ())

    def test_artifact_requires_provenance_scope_regime_and_version(self):
        base = dict(
            artifact_id="a1",
            primitive=PrimitiveId.L01_SENSING_OBSERVATION,
            artifact_type="observation",
            epistemic_class=EpistemicClass.OBSERVATION,
            state_version="s1",
            scope="scope",
            regime="regime",
            provenance_ids=("sensor-1",),
        )
        for key in ("artifact_id", "artifact_type", "state_version", "scope", "regime"):
            broken = dict(base)
            broken[key] = ""
            with self.assertRaises(ValueError, msg=key):
                PrimitiveArtifact(**broken)
        broken = dict(base)
        broken["provenance_ids"] = ()
        with self.assertRaises(ValueError):
            PrimitiveArtifact(**broken)

    def test_validation_preserves_epistemic_class(self):
        for epistemic in EpistemicClass:
            artifact = self.artifact(epistemic=epistemic)
            receipt = validate_primitive_artifact(artifact)
            self.assertEqual(receipt.epistemic_class, epistemic)
            self.assertTrue(receipt.contract_valid)

    def test_action_primitive_does_not_mint_effect_authority(self):
        artifact = self.artifact(primitive=PrimitiveId.L18_ACTION, epistemic=EpistemicClass.DECISION)
        self.assertFalse(artifact.effect_authorized)
        self.assertFalse(primitive_spec(PrimitiveId.L18_ACTION).effect_authority)
        self.assertFalse(validate_primitive_artifact(artifact).effect_authorized)

    def test_numeric_primitive_order_does_not_create_dependencies(self):
        graph = build_primitive_dependency_graph()
        self.assertEqual(graph.edges(), ())
        self.assertEqual(graph.topological_order(), tuple(sorted(p.value for p in PrimitiveId)))

    def test_only_explicit_dependency_is_added(self):
        edge = PrimitiveDependency(
            PrimitiveId.L01_SENSING_OBSERVATION,
            PrimitiveId.L03_PERCEPT_FORMATION,
            DependencyKind.EVIDENCE,
        )
        graph = build_primitive_dependency_graph((edge,))
        edges = graph.edges()
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges[0].dependency, PrimitiveId.L01_SENSING_OBSERVATION.value)
        self.assertEqual(edges[0].dependent, PrimitiveId.L03_PERCEPT_FORMATION.value)
        self.assertEqual(edges[0].kind, DependencyKind.EVIDENCE)

    def test_self_dependency_fails_closed(self):
        with self.assertRaises(ValueError):
            PrimitiveDependency(PrimitiveId.L07_MEMORY, PrimitiveId.L07_MEMORY)


if __name__ == "__main__":
    unittest.main()
