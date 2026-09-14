"""Bounded executable contract substrate for AMOS lifecycle operations O00-O16.

Origin architect / steward: Trang Phan.

This module implements the generic lifecycle-operation contract. It does not
claim complete semantic implementations for distinction, object formation,
reasoning, learning, or any other operation merely because the registry exists.

Hard boundaries include:
- operation identity/order != dependency or causality;
- memory != knowledge;
- prediction != causation;
- simulation != deployment;
- action/capability != effect authority;
- learning mutates governed external AMOS state, not host model neural weights.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Mapping, Optional, Tuple

from cognitive_matrix_runtime import DependencyGraph, DependencyKind
from primitive_contract_runtime import EpistemicClass


class LifecycleOperationId(Enum):
    O00_DISTINCTION = "O00_DISTINCTION"
    O01_OBJECT = "O01_OBJECT"
    O02_RELATION = "O02_RELATION"
    O03_BINDING = "O03_BINDING"
    O04_STATE = "O04_STATE"
    O05_MEMORY = "O05_MEMORY"
    O06_MODEL = "O06_MODEL"
    O07_INFERENCE = "O07_INFERENCE"
    O08_PREDICTION = "O08_PREDICTION"
    O09_SIMULATION = "O09_SIMULATION"
    O10_VALUE = "O10_VALUE"
    O11_GOAL = "O11_GOAL"
    O12_PLAN = "O12_PLAN"
    O13_DECISION = "O13_DECISION"
    O14_ACTION = "O14_ACTION"
    O15_OBSERVATION = "O15_OBSERVATION"
    O16_LEARNING = "O16_LEARNING"


@dataclass(frozen=True)
class LifecycleOperationSpec:
    operation: LifecycleOperationId
    semantic_executor: Optional[str] = None
    implementation_status: str = "CONTRACT_BOUND_SEMANTIC_EXECUTOR_GAP"

    @property
    def effect_authority(self) -> bool:
        return False

    @property
    def host_weight_mutation_allowed(self) -> bool:
        return False


LIFECYCLE_CATALOG: Mapping[LifecycleOperationId, LifecycleOperationSpec] = {
    operation: LifecycleOperationSpec(operation) for operation in LifecycleOperationId
}


@dataclass(frozen=True)
class LifecycleRequest:
    request_id: str
    operation: LifecycleOperationId
    input_artifact_ids: Tuple[str, ...]
    output_artifact_id: str
    input_epistemic_class: EpistemicClass
    output_epistemic_class: EpistemicClass
    state_version: str
    scope: str
    regime: str
    provenance_ids: Tuple[str, ...]
    epistemic_transition_receipt_id: Optional[str] = None
    authority_witness_id: Optional[str] = None
    consequential_effect_requested: bool = False

    def __post_init__(self) -> None:
        strings = {
            "request_id": self.request_id,
            "output_artifact_id": self.output_artifact_id,
            "state_version": self.state_version,
            "scope": self.scope,
            "regime": self.regime,
        }
        for name, value in strings.items():
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be explicit and non-empty")
        if not self.input_artifact_ids:
            raise ValueError("lifecycle request requires at least one input artifact")
        if any(not item.strip() for item in self.input_artifact_ids):
            raise ValueError("input artifact ids must be non-empty")
        if len(set(self.input_artifact_ids)) != len(self.input_artifact_ids):
            raise ValueError("input artifact ids must be unique")
        if not self.provenance_ids or any(not item.strip() for item in self.provenance_ids):
            raise ValueError("lifecycle request requires non-empty provenance ids")
        if len(set(self.provenance_ids)) != len(self.provenance_ids):
            raise ValueError("provenance ids must be unique")
        if self.epistemic_transition_receipt_id is not None and not self.epistemic_transition_receipt_id.strip():
            raise ValueError("epistemic transition receipt id must be non-empty when supplied")
        if self.authority_witness_id is not None and not self.authority_witness_id.strip():
            raise ValueError("authority witness id must be non-empty when supplied")


@dataclass(frozen=True)
class LifecycleContractReceipt:
    request_id: str
    operation: LifecycleOperationId
    state_version: str
    input_epistemic_class: EpistemicClass
    output_epistemic_class: EpistemicClass
    contract_valid: bool
    epistemic_transition_bound: bool
    effect_authorized: bool = False
    host_weight_mutation_allowed: bool = False
    conclusion_class: str = "AMOS_MODEL/BOUNDED_CONTRACT"


def validate_lifecycle_request(request: LifecycleRequest) -> LifecycleContractReceipt:
    """Validate structural transition semantics without executing a domain effect."""
    if request.operation not in LIFECYCLE_CATALOG:
        raise ValueError("lifecycle operation is not registered")

    changed_epistemic = request.output_epistemic_class is not request.input_epistemic_class
    if changed_epistemic and request.epistemic_transition_receipt_id is None:
        raise ValueError("epistemic class transition requires an explicit transition receipt")

    if request.consequential_effect_requested:
        if request.operation is not LifecycleOperationId.O14_ACTION:
            raise ValueError("consequential effect request is valid only on O14_ACTION")
        if request.authority_witness_id is None:
            raise ValueError("consequential action request requires an authority witness identity")

    # Even a structurally valid O14 request is only a non-authoritative contract
    # receipt here. Commit/effect authority belongs to the control plane.
    return LifecycleContractReceipt(
        request_id=request.request_id,
        operation=request.operation,
        state_version=request.state_version,
        input_epistemic_class=request.input_epistemic_class,
        output_epistemic_class=request.output_epistemic_class,
        contract_valid=True,
        epistemic_transition_bound=(not changed_epistemic or request.epistemic_transition_receipt_id is not None),
        effect_authorized=False,
        host_weight_mutation_allowed=False,
    )


@dataclass(frozen=True)
class LifecycleDependency:
    dependency: LifecycleOperationId
    dependent: LifecycleOperationId
    kind: DependencyKind = DependencyKind.HARD

    def __post_init__(self) -> None:
        if self.dependency is self.dependent:
            raise ValueError("lifecycle self-dependency is not permitted")


def build_lifecycle_dependency_graph(
    dependencies: Iterable[LifecycleDependency] = (),
) -> DependencyGraph:
    """Build only explicitly admitted operation dependencies.

    O00..O16 numbering is not converted into dependency, causality, or execution
    sequencing by this contract.
    """
    graph = DependencyGraph(operation.value for operation in LifecycleOperationId)
    for edge in dependencies:
        graph.add_edge(edge.dependency.value, edge.dependent.value, edge.kind)
    return graph


def lifecycle_spec(operation: LifecycleOperationId) -> LifecycleOperationSpec:
    return LIFECYCLE_CATALOG[operation]


def validate_lifecycle_registry() -> Tuple[str, ...]:
    failures = []
    if len(LifecycleOperationId) != 17:
        failures.append("LIFECYCLE_OPERATION_COUNT")
    if len(LIFECYCLE_CATALOG) != 17:
        failures.append("LIFECYCLE_CATALOG_COUNT")
    if set(LIFECYCLE_CATALOG) != set(LifecycleOperationId):
        failures.append("LIFECYCLE_CATALOG_COVERAGE")
    if any(spec.effect_authority for spec in LIFECYCLE_CATALOG.values()):
        failures.append("LIFECYCLE_MUST_NOT_MINT_EFFECT_AUTHORITY")
    if any(spec.host_weight_mutation_allowed for spec in LIFECYCLE_CATALOG.values()):
        failures.append("LIFECYCLE_MUST_NOT_MUTATE_HOST_WEIGHTS")
    if build_lifecycle_dependency_graph().edges():
        failures.append("LIFECYCLE_ORDER_MUST_NOT_IMPLY_DEPENDENCY")
    return tuple(failures)
