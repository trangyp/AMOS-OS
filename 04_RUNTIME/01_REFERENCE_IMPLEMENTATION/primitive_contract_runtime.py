"""Bounded executable contract substrate for AMOS Cognitive Matrix primitives L00-L29.

Origin architect / steward: Trang Phan.

This module closes the generic primitive-contract implementation gap without
pretending that every primitive has a complete domain-semantic executor. It owns:
- exact primitive identity/registry;
- typed artifact admission requirements;
- provenance/scope/regime/epistemic preservation;
- explicit dependency binding;
- authority and effect firewalls.

It does NOT infer dependencies from L00..L29 numbering, promote Canon, turn an
artifact into current world state, or authorize external effects.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, Mapping, Tuple

from cognitive_matrix_runtime import DependencyGraph, DependencyKind


class PrimitiveId(Enum):
    L00_REALITY_ENVIRONMENT = "L00_REALITY_ENVIRONMENT"
    L01_SENSING_OBSERVATION = "L01_SENSING_OBSERVATION"
    L02_ATTENTION = "L02_ATTENTION"
    L03_PERCEPT_FORMATION = "L03_PERCEPT_FORMATION"
    L04_OBJECT_ENTITY_FORMATION = "L04_OBJECT_ENTITY_FORMATION"
    L05_BINDING = "L05_BINDING"
    L06_WORKING_STATE = "L06_WORKING_STATE"
    L07_MEMORY = "L07_MEMORY"
    L08_REPRESENTATION = "L08_REPRESENTATION"
    L09_INFERENCE = "L09_INFERENCE"
    L10_WORLD_MODELING = "L10_WORLD_MODELING"
    L11_CAUSAL_MODELING = "L11_CAUSAL_MODELING"
    L12_COUNTERFACTUAL_SIMULATION = "L12_COUNTERFACTUAL_SIMULATION"
    L13_PREDICTION = "L13_PREDICTION"
    L14_VALUATION = "L14_VALUATION"
    L15_GOAL_FORMATION = "L15_GOAL_FORMATION"
    L16_PLANNING = "L16_PLANNING"
    L17_DECISION = "L17_DECISION"
    L18_ACTION = "L18_ACTION"
    L19_OUTCOME_OBSERVATION = "L19_OUTCOME_OBSERVATION"
    L20_CREDIT_ASSIGNMENT = "L20_CREDIT_ASSIGNMENT"
    L21_LEARNING = "L21_LEARNING"
    L22_CONSOLIDATION = "L22_CONSOLIDATION"
    L23_METACOGNITION = "L23_METACOGNITION"
    L24_SELF_REGULATION = "L24_SELF_REGULATION"
    L25_IDENTITY_CONTINUITY = "L25_IDENTITY_CONTINUITY"
    L26_SOCIAL_COGNITION = "L26_SOCIAL_COGNITION"
    L27_MULTI_AGENT_COGNITION = "L27_MULTI_AGENT_COGNITION"
    L28_GOVERNANCE = "L28_GOVERNANCE"
    L29_EVOLUTION = "L29_EVOLUTION"


class EpistemicClass(Enum):
    OBSERVATION = "OBSERVATION"
    SOURCE_CLAIM = "SOURCE_CLAIM"
    DERIVED = "DERIVED"
    MODEL = "MODEL"
    DECISION = "DECISION"
    COMPETING = "COMPETING"
    UNKNOWN_GAP = "UNKNOWN/GAP"


@dataclass(frozen=True)
class PrimitiveSpec:
    primitive: PrimitiveId
    semantic_executor: str | None = None
    implementation_status: str = "CONTRACT_BOUND_SEMANTIC_EXECUTOR_GAP"

    @property
    def effect_authority(self) -> bool:
        return False


PRIMITIVE_CATALOG: Mapping[PrimitiveId, PrimitiveSpec] = {
    primitive: PrimitiveSpec(primitive) for primitive in PrimitiveId
}


@dataclass(frozen=True)
class PrimitiveArtifact:
    artifact_id: str
    primitive: PrimitiveId
    artifact_type: str
    epistemic_class: EpistemicClass
    state_version: str
    scope: str
    regime: str
    provenance_ids: Tuple[str, ...]

    def __post_init__(self) -> None:
        strings = {
            "artifact_id": self.artifact_id,
            "artifact_type": self.artifact_type,
            "state_version": self.state_version,
            "scope": self.scope,
            "regime": self.regime,
        }
        for name, value in strings.items():
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be explicit and non-empty")
        if not self.provenance_ids:
            raise ValueError("primitive artifact requires provenance")
        if any(not isinstance(item, str) or not item.strip() for item in self.provenance_ids):
            raise ValueError("provenance ids must be non-empty strings")
        if len(set(self.provenance_ids)) != len(self.provenance_ids):
            raise ValueError("provenance ids must be unique")

    @property
    def effect_authorized(self) -> bool:
        """Primitive membership/capability never grants effect authority."""
        return False


@dataclass(frozen=True)
class PrimitiveContractReceipt:
    artifact_id: str
    primitive: PrimitiveId
    state_version: str
    epistemic_class: EpistemicClass
    contract_valid: bool
    effect_authorized: bool = False
    conclusion_class: str = "AMOS_MODEL/BOUNDED_CONTRACT"


def validate_primitive_artifact(artifact: PrimitiveArtifact) -> PrimitiveContractReceipt:
    """Validate the generic primitive envelope without epistemic promotion."""
    if artifact.primitive not in PRIMITIVE_CATALOG:
        raise ValueError("primitive is not registered")
    return PrimitiveContractReceipt(
        artifact_id=artifact.artifact_id,
        primitive=artifact.primitive,
        state_version=artifact.state_version,
        epistemic_class=artifact.epistemic_class,
        contract_valid=True,
        effect_authorized=False,
    )


@dataclass(frozen=True)
class PrimitiveDependency:
    dependency: PrimitiveId
    dependent: PrimitiveId
    kind: DependencyKind = DependencyKind.HARD

    def __post_init__(self) -> None:
        if self.dependency is self.dependent:
            raise ValueError("primitive self-dependency is not permitted")


def build_primitive_dependency_graph(
    dependencies: Iterable[PrimitiveDependency] = (),
) -> DependencyGraph:
    """Build only explicitly declared dependencies.

    Numeric/lexical primitive order is deliberately NOT converted into edges.
    """
    graph = DependencyGraph(primitive.value for primitive in PrimitiveId)
    for edge in dependencies:
        graph.add_edge(edge.dependency.value, edge.dependent.value, edge.kind)
    return graph


def primitive_spec(primitive: PrimitiveId) -> PrimitiveSpec:
    return PRIMITIVE_CATALOG[primitive]


def validate_primitive_registry() -> Tuple[str, ...]:
    failures = []
    if len(PrimitiveId) != 30:
        failures.append("PRIMITIVE_COUNT")
    if len(PRIMITIVE_CATALOG) != 30:
        failures.append("PRIMITIVE_CATALOG_COUNT")
    if set(PRIMITIVE_CATALOG) != set(PrimitiveId):
        failures.append("PRIMITIVE_CATALOG_COVERAGE")
    if any(spec.effect_authority for spec in PRIMITIVE_CATALOG.values()):
        failures.append("PRIMITIVE_MUST_NOT_MINT_EFFECT_AUTHORITY")
    empty_graph = build_primitive_dependency_graph()
    if empty_graph.edges():
        failures.append("PRIMITIVE_ORDER_MUST_NOT_IMPLY_DEPENDENCY")
    return tuple(failures)
