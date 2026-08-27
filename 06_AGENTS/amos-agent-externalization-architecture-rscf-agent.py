from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set
import hashlib
import json
import logging
import time


# ============================================================
# AMOS AGENT EXTERNALIZATION ARCHITECTURE RSCF AGENT
# ============================================================
#
# Author / Steward: Trang Phan
#
# Primary skill:
#   amos-agent-externalization-architecture-rscf
#
# Source architecture:
#
#   CONTEXT
#       One-off transient information.
#
#   MEMORY
#       Persistent state and continuity across time.
#
#   SKILL
#       Reusable procedural expertise.
#
#   PROTOCOL
#       Cross-agent / cross-tool interaction contracts.
#
#   CODE
#       Deterministic repeatable computation.
#
#   TOOL
#       External executable capability accessed through
#       a governed interface.
#
#   HARNESS_POLICY
#       Permissions, approval, sandboxing, execution isolation,
#       authority constraints, and governance.
#
# Core target-selection model:
#
#   Target(x) =
#       argmin_a [
#           ExpectedFailure(x,a)
#           + MaintenanceCost(a)
#           + DriftRisk(a)
#       ]
#
# subject to:
#   - safety
#   - provenance
#   - latency
#   - context budget
#   - authority
#   - lifecycle
#   - invalidation semantics
#
# Critical invariant:
#   Capability packaging != authority.
#
# ============================================================


AGENT_ID = "amos-agent-externalization-architecture-rscf-agent"
AGENT_VERSION = "1.0.0"


# ============================================================
# ENUMS
# ============================================================

class EpistemicClass(str, Enum):
    SOURCE_CLAIM = "SOURCE_CLAIM"
    OBSERVATION = "OBSERVATION"
    DERIVED = "DERIVED"
    MODEL = "MODEL"
    DECISION = "DECISION"
    COMPETING = "COMPETING"
    UNKNOWN = "UNKNOWN/GAP"


class ConclusionClass(str, Enum):
    VERIFIED = "VERIFIED"
    DERIVED = "DERIVED"
    MODEL = "MODEL"
    CONDITIONAL = "CONDITIONAL"
    COMPETING = "COMPETING"
    UNKNOWN = "UNKNOWN/GAP"


class ExecutionStatus(str, Enum):
    VERIFIED = "VERIFIED"
    DERIVED = "DERIVED"
    MODEL = "MODEL"
    CONDITIONAL = "CONDITIONAL"
    COMPETING = "COMPETING"
    UNKNOWN = "UNKNOWN/GAP"
    REJECTED = "REJECTED"


class SideEffect(str, Enum):
    READ = "read"
    WRITE = "write"


class ArtifactType(str, Enum):
    CONTEXT = "CONTEXT"
    MEMORY = "MEMORY"
    SKILL = "SKILL"
    PROTOCOL = "PROTOCOL"
    CODE = "CODE"
    TOOL = "TOOL"
    HARNESS_POLICY = "HARNESS_POLICY"


class ArtifactStatus(str, Enum):
    PROPOSED = "PROPOSED"
    STAGED = "STAGED"
    ACTIVE = "ACTIVE"
    STALE = "STALE"
    INVALIDATED = "INVALIDATED"
    QUARANTINED = "QUARANTINED"
    RETIRED = "RETIRED"


class BurdenClass(str, Enum):
    STATE = "STATE"
    PROCEDURE = "PROCEDURE"
    INTERACTION = "INTERACTION"
    CONTROL = "CONTROL"
    COMPUTATION = "COMPUTATION"
    TOOL_USE = "TOOL_USE"
    TRANSIENT = "TRANSIENT"
    MIXED = "MIXED"
    UNKNOWN = "UNKNOWN/GAP"


class InvariantStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNKNOWN = "UNKNOWN"


class ExternalizationDecision(str, Enum):
    KEEP_IN_CONTEXT = "KEEP_IN_CONTEXT"
    EXTERNALIZE_TO_MEMORY = "EXTERNALIZE_TO_MEMORY"
    EXTERNALIZE_TO_SKILL = "EXTERNALIZE_TO_SKILL"
    EXTERNALIZE_TO_PROTOCOL = "EXTERNALIZE_TO_PROTOCOL"
    EXTERNALIZE_TO_CODE = "EXTERNALIZE_TO_CODE"
    EXTERNALIZE_TO_TOOL = "EXTERNALIZE_TO_TOOL"
    EXTERNALIZE_TO_HARNESS_POLICY = "EXTERNALIZE_TO_HARNESS_POLICY"
    REQUIRE_MORE_EVIDENCE = "REQUIRE_MORE_EVIDENCE"
    ESCALATE = "ESCALATE"
    BLOCK = "BLOCK"


class FreshnessState(str, Enum):
    FRESH = "FRESH"
    AGING = "AGING"
    STALE = "STALE"
    UNKNOWN = "UNKNOWN"


# ============================================================
# ERRORS
# ============================================================

class ExternalizationArchitectureError(RuntimeError):
    pass


class ValidationError(ExternalizationArchitectureError):
    pass


class AuthorizationError(ExternalizationArchitectureError):
    pass


class GapError(ExternalizationArchitectureError):
    pass


class InvariantViolation(ExternalizationArchitectureError):
    pass


# ============================================================
# DATA CONTRACTS
# ============================================================

@dataclass(frozen=True)
class ProvenanceRef:
    source: str
    path: Optional[str] = None
    content_hash: Optional[str] = None
    claim_id: Optional[str] = None
    source_version: Optional[str] = None
    timestamp: Optional[str] = None


@dataclass
class CapabilityContract:
    name: str
    description: str
    side_effect: SideEffect


@dataclass
class HardInvariant:
    invariant_id: str
    description: str
    status: InvariantStatus
    evidence: List[str] = field(default_factory=list)
    reason: Optional[str] = None


@dataclass
class WorkItem:
    item_id: str
    description: str

    recurring: bool
    deterministic: bool
    cross_agent: bool
    cross_tool: bool
    permission_sensitive: bool
    requires_persistence: bool
    transient: bool
    external_capability_required: bool

    lifetime: float
    mutability: float
    cognitive_burden: float
    context_cost: float

    authority_required: float
    latency_sensitivity: float
    safety_sensitivity: float

    provenance: List[ProvenanceRef] = field(default_factory=list)

    current_location: Optional[ArtifactType] = None


@dataclass
class ExternalizationCandidate:
    """
    A[
        module,
        artifact_type,
        cognitive_burden,
        lifetime,
        mutability,
        authority,
        budget,
        provenance,
        status
    ]
    """

    module: str
    artifact_type: ArtifactType

    cognitive_burden: float
    lifetime: float
    mutability: float
    authority: float
    budget: float

    expected_failure: float
    maintenance_cost: float
    drift_risk: float

    latency_cost: float
    provenance_risk: float
    safety_risk: float
    authority_risk: float

    provenance: List[ProvenanceRef] = field(default_factory=list)

    status: ArtifactStatus = ArtifactStatus.PROPOSED

    def objective_score(self) -> float:
        """
        AMOS MODEL:

        Target(x) =
            argmin [
                ExpectedFailure
                + MaintenanceCost
                + DriftRisk
            ]

        Hard constraints are enforced separately.
        """

        return (
            _nonnegative(self.expected_failure)
            + _nonnegative(self.maintenance_cost)
            + _nonnegative(self.drift_risk)
        )

    def extended_cost(self) -> float:
        """
        Diagnostic score only.

        This does not replace the source target equation.
        """

        return (
            self.objective_score()
            + _nonnegative(self.latency_cost)
            + _nonnegative(self.provenance_risk)
            + _nonnegative(self.safety_risk)
            + _nonnegative(self.authority_risk)
        )


@dataclass
class ArtifactRecord:
    artifact_id: str
    artifact_type: ArtifactType

    owner_module: str
    scope: str

    lifetime: float
    mutability: float

    authority_scope: List[str]

    created_at_epoch: float
    freshness_timestamp_epoch: float

    freshness_ttl_seconds: Optional[float]

    invalidation_conditions: List[str]
    dependencies: List[str]

    provenance: List[ProvenanceRef]

    rollback_path: Optional[str]

    status: ArtifactStatus = ArtifactStatus.PROPOSED

    def freshness_state(
        self,
        now: Optional[float] = None,
    ) -> FreshnessState:

        if self.freshness_ttl_seconds is None:
            return FreshnessState.UNKNOWN

        now = now or time.time()

        age = (
            now
            - self.freshness_timestamp_epoch
        )

        ttl = self.freshness_ttl_seconds

        if age <= ttl * 0.75:
            return FreshnessState.FRESH

        if age <= ttl:
            return FreshnessState.AGING

        return FreshnessState.STALE


@dataclass
class InterfaceContract:
    interface_id: str

    producer: str
    consumer: str

    input_schema: Dict[str, Any]
    output_schema: Dict[str, Any]

    authority_boundary: str
    permission_requirements: List[str]

    failure_behavior: str

    provenance_requirements: List[str]
    invalidation_behavior: str

    version: Optional[str] = None


@dataclass
class CoordinateState:
    """
    X[
        item,
        layer,
        scale,
        time,
        regime,
        observer,
        provenance,
        status
    ]
    """

    item: str
    layer: str
    scale: str
    time: str
    regime: str
    observer: str
    provenance: List[ProvenanceRef]
    status: str


@dataclass
class ClaimEvidence:
    """
    E[
        claim,
        source,
        family,
        independence,
        freshness,
        scope,
        confidence
    ]
    """

    claim: str
    source: str
    family: str

    independence: bool
    freshness: float

    scope: str
    confidence: float


@dataclass
class DependencyEdge:
    """
    D[
        parent,
        child,
        type,
        load_bearing,
        condition
    ]
    """

    parent: str
    child: str
    edge_type: str
    load_bearing: bool
    condition: Optional[str] = None


@dataclass
class ExternalizationHypothesis:
    hypothesis_id: str
    target: ArtifactType
    statement: str

    confidence: float

    supporting_evidence: List[str] = field(default_factory=list)
    conflicting_evidence: List[str] = field(default_factory=list)

    falsifiers: List[str] = field(default_factory=list)


@dataclass
class RSCFCapsule:
    claim: str
    epistemic_class: EpistemicClass
    conclusion_class: ConclusionClass

    scope: str
    regime: str

    premises: Dict[str, float]

    dependencies: List[str]

    coordinate_state: CoordinateState
    evidence: List[ClaimEvidence]

    competing_hypotheses: List[ExternalizationHypothesis]

    provenance: List[ProvenanceRef]

    falsifiers: List[str]

    confidence_ceiling: float

    decision: ExternalizationDecision
    selected_target: Optional[ArtifactType]

    repair_path: Optional[str] = None
    rollback_path: Optional[str] = None


@dataclass
class DependencyGraph:
    descendants: Dict[str, Set[str]] = field(
        default_factory=dict
    )

    def add_edge(
        self,
        parent: str,
        child: str,
    ) -> None:

        self.descendants.setdefault(
            parent,
            set(),
        ).add(child)

    def closure(
        self,
        node_id: str,
    ) -> Set[str]:

        visited: Set[str] = set()
        stack = [node_id]

        while stack:

            current = stack.pop()

            for child in self.descendants.get(
                current,
                set(),
            ):

                if child in visited:
                    continue

                visited.add(child)
                stack.append(child)

        return visited


@dataclass
class ExecutionContext:
    query: str
    capability: str

    inputs: Dict[str, Any] = field(
        default_factory=dict
    )

    # Capability does not imply authority.
    authorized_write: bool = False
    authority_witness: Optional[str] = None

    correlation_id: Optional[str] = None


@dataclass
class AgentResult:
    status: ExecutionStatus
    capability: str
    summary: str

    data: Dict[str, Any] = field(
        default_factory=dict
    )

    gaps: List[str] = field(
        default_factory=list
    )

    warnings: List[str] = field(
        default_factory=list
    )

    confidence_ceiling: float = 0.95

    provenance: List[ProvenanceRef] = field(
        default_factory=list
    )


# ============================================================
# CONFIGURATION
# ============================================================

AGENT_CONFIG: Dict[str, Any] = {
    "name": AGENT_ID,

    "display_name": (
        "Agent Externalization Architecture Rscf"
    ),

    "description": (
        "Agent Externalization Architecture RSCF — "
        "governs where cognitive and execution burden "
        "should live across context, memory, skills, "
        "protocols, code, tools, and harness policy."
    ),

    "version": AGENT_VERSION,

    "author": "Trang Phan",
    "steward": "Trang Phan",

    "system": "AMOS_OS",

    "role": (
        "Externalization architecture specialist for "
        "state persistence, procedural packaging, interaction "
        "protocols, deterministic computation, tool interfaces, "
        "and execution-control placement."
    ),

    "skill_binding": {
        "primary_skill": (
            "amos-agent-externalization-architecture-rscf"
        ),
        "skill_path": (
            ".devin/skills/"
            "amos-agent-externalization-architecture-rscf/"
            "SKILL.md"
        ),
    },

    "depends_on_workflows": [
        (
            "amos-agent-externalization-"
            "architecture-rscf-workflow.md"
        )
    ],

    "epistemic_class": "AMOS_MODEL",

    "claim_ceiling": 0.95,

    "lifecycle": {
        "status": "active",
        "deprecated": False,
        "deprecation_date": None,
        "successor": None,
    },

    "governance": {
        "owner_team": "AMOS_CORE",
        "business_domain": "runtime",
        "risk_tier": "medium",
        "observability": (
            "structured_logs+content_hash"
        ),
        "approval_mode": "steward_review",
        "promotion_state": "production",
    },

    "content_hash": "f4d12f99949029ed",
}


CAPABILITIES: Dict[str, CapabilityContract] = {

    "runtime.execute": CapabilityContract(
        name="runtime.execute",
        description=(
            "Classify cognitive burden, select an externalization "
            "target, bind provenance/lifecycle/invalidation, define "
            "interfaces, budget context, and produce an RSCF decision."
        ),
        side_effect=SideEffect.WRITE,
    ),

    "runtime.validate": CapabilityContract(
        name="runtime.validate",
        description=(
            "Validate externalization architecture against routing, "
            "authority, lifecycle, provenance, progressive disclosure, "
            "module isolation, and rollback invariants."
        ),
        side_effect=SideEffect.READ,
    ),

    "runtime.trace_provenance": CapabilityContract(
        name="runtime.trace_provenance",
        description=(
            "Trace artifacts and externalization decisions through "
            "A/X/E/D structures and dependency lineage."
        ),
        side_effect=SideEffect.READ,
    ),

    "runtime.assess_claim": CapabilityContract(
        name="runtime.assess_claim",
        description=(
            "Assess externalization claims against epistemic class, "
            "scope, freshness, regime, provenance, falsifiers, and "
            "confidence ceilings."
        ),
        side_effect=SideEffect.READ,
    ),
}


# ============================================================
# AGENT
# ============================================================

class AmosAgentExternalizationArchitectureRSCFAgent:
    """
    Production-oriented runtime adapter for:

        amos-agent-externalization-architecture-rscf

    Authoritative Skill invariants:

    1. Persistent state -> MEMORY.
    2. Reusable procedure -> SKILL / CODE.
    3. Interaction contract -> PROTOCOL.
    4. Permissions / isolation -> HARNESS_POLICY.
    5. Externalization may not hide decision-critical state.
    6. Persistent artifacts require lifecycle, freshness,
       provenance, and invalidation semantics.
    7. Modules may not silently override each other.
    8. Progressive disclosure loads only necessary artifacts.
    9. Capability packaging does not grant authority.
    10. Self-evolving infrastructure requires governance + rollback.

    Mandatory RSCF:

        X[item,layer,scale,time,regime,observer,provenance,status]

        E[claim,source,family,independence,freshness,scope,confidence]

        D[parent,child,type,load_bearing,condition]

        Conf(C) <= min Conf(load-bearing premises)

        Invalid(p) => Invalidate(descendants(p))

        ValidNow(C) =
            ScopeMatch
            AND RegimeMatch
            AND FreshEnough
            AND NOT FalsifierTriggered
    """

    def __init__(
        self,
        repo_root: str | Path = ".",
        claim_ceiling: float = 0.95,
    ) -> None:

        self.repo_root = Path(
            repo_root
        ).resolve()

        self.skill_path = (
            self.repo_root
            / ".devin"
            / "skills"
            / "amos-agent-externalization-architecture-rscf"
            / "SKILL.md"
        )

        self.source_map_path = (
            self.skill_path.parent
            / "references"
            / "source-map.md"
        )

        self.claim_ceiling = min(
            max(
                float(claim_ceiling),
                0.0,
            ),
            0.95,
        )

        self.logger = logging.getLogger(
            AGENT_ID
        )

        self.handlers: Dict[
            str,
            Callable[
                [ExecutionContext],
                AgentResult,
            ],
        ] = {

            "runtime.execute":
                self._execute_externalization,

            "runtime.validate":
                self._validate_architecture,

            "runtime.trace_provenance":
                self._trace_provenance,

            "runtime.assess_claim":
                self._assess_claim,
        }

    # ========================================================
    # PUBLIC API
    # ========================================================

    def run(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        ctx.correlation_id = (
            ctx.correlation_id
            or self._new_correlation_id()
        )

        self._load_skill()

        self._validate_context(
            ctx
        )

        capability = CAPABILITIES.get(
            ctx.capability
        )

        if capability is None:

            raise ValidationError(
                f"Unsupported capability: "
                f"{ctx.capability}"
            )

        self._check_authority(
            capability=capability,
            ctx=ctx,
        )

        result = self.handlers[
            ctx.capability
        ](ctx)

        result.confidence_ceiling = min(
            result.confidence_ceiling,
            self.claim_ceiling,
        )

        return result

    # ========================================================
    # SKILL / SOURCE
    # ========================================================

    def _load_skill(
        self,
    ) -> str:

        if not self.skill_path.exists():

            raise GapError(
                "UNKNOWN/GAP: authoritative skill unavailable: "
                f"{self.skill_path}"
            )

        text = self.skill_path.read_text(
            encoding="utf-8"
        )

        if not text.strip():

            raise GapError(
                "UNKNOWN/GAP: authoritative skill is empty."
            )

        return text

    def load_source_map(
        self,
    ) -> str:
        """
        Required before source-specific claims.

        The Skill explicitly requires references/source-map.md
        before source-specific claims.
        """

        if not self.source_map_path.exists():

            raise GapError(
                "UNKNOWN/GAP: references/source-map.md "
                "is unavailable."
            )

        text = self.source_map_path.read_text(
            encoding="utf-8"
        )

        if not text.strip():

            raise GapError(
                "UNKNOWN/GAP: source-map.md is empty."
            )

        return text

    # ========================================================
    # CONTEXT / AUTHORITY
    # ========================================================

    def _validate_context(
        self,
        ctx: ExecutionContext,
    ) -> None:

        if not ctx.query.strip():

            raise ValidationError(
                "query must not be empty"
            )

    def _check_authority(
        self,
        capability: CapabilityContract,
        ctx: ExecutionContext,
    ) -> None:

        if (
            capability.side_effect
            != SideEffect.WRITE
        ):
            return

        if not ctx.authorized_write:

            raise AuthorizationError(
                f"{capability.name} is write-classified. "
                "Capability packaging does not grant authority."
            )

        if not ctx.authority_witness:

            raise AuthorizationError(
                "Write-classified architecture operation "
                "requires an explicit authority_witness."
            )

    # ========================================================
    # EXECUTION WORKFLOW
    # ========================================================

    def _execute_externalization(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:
        """
        Skill workflow:

        identify recurring burden
        -> classify state/expertise/interaction/control
        -> estimate lifetime and failure mode
        -> choose externalization target
        -> bind provenance and invalidation
        -> define interfaces
        -> test module interactions
        -> budget context
        -> RSCF audit
        """

        # ----------------------------------------------------
        # 1. Parse work item
        # ----------------------------------------------------

        work_item = self._parse_work_item(
            ctx.inputs.get(
                "work_item"
            )
        )

        # ----------------------------------------------------
        # 2. Classify burden
        # ----------------------------------------------------

        burden_class = (
            self._classify_burden(
                work_item
            )
        )

        # ----------------------------------------------------
        # 3. Determine routing target
        # ----------------------------------------------------

        routed_target = (
            self._route_target(
                work_item=work_item,
                burden_class=burden_class,
            )
        )

        # ----------------------------------------------------
        # 4. Build candidate implementations
        # ----------------------------------------------------

        candidates = (
            self._build_candidates(
                work_item=work_item,
                raw_candidates=ctx.inputs.get(
                    "candidate_artifacts",
                    [],
                ),
            )
        )

        if not candidates:

            raise GapError(
                "UNKNOWN/GAP: no externalization candidates "
                "could be constructed."
            )

        # ----------------------------------------------------
        # 5. Evaluate hard invariants
        # ----------------------------------------------------

        invariants = (
            self._build_invariants(
                work_item=work_item,
                routed_target=routed_target,
                inputs=ctx.inputs,
            )
        )

        invariant_gate = (
            self._evaluate_invariants(
                invariants
            )
        )

        if (
            invariant_gate["status"]
            == InvariantStatus.FAIL
        ):

            return AgentResult(
                status=ExecutionStatus.REJECTED,
                capability=ctx.capability,
                summary=(
                    "Externalization rejected because "
                    "a hard architecture invariant failed."
                ),
                data={
                    "work_item": asdict(
                        work_item
                    ),
                    "burden_class": (
                        burden_class.value
                    ),
                    "routed_target": (
                        routed_target.value
                    ),
                    "invariants": [
                        asdict(i)
                        for i in invariants
                    ],
                    "decision": (
                        ExternalizationDecision.BLOCK.value
                    ),
                    "artifact_committed": False,
                },
                gaps=invariant_gate[
                    "reasons"
                ],
                warnings=[
                    (
                        "Objective-score optimization cannot "
                        "override a hard invariant."
                    )
                ],
                confidence_ceiling=(
                    self.claim_ceiling
                ),
                provenance=(
                    self._default_provenance()
                ),
            )

        if (
            invariant_gate["status"]
            == InvariantStatus.UNKNOWN
        ):

            return AgentResult(
                status=ExecutionStatus.UNKNOWN,
                capability=ctx.capability,
                summary=(
                    "Externalization is UNKNOWN/GAP because "
                    "a load-bearing architecture condition "
                    "is unresolved."
                ),
                data={
                    "work_item": asdict(
                        work_item
                    ),
                    "burden_class": (
                        burden_class.value
                    ),
                    "routed_target": (
                        routed_target.value
                    ),
                    "invariants": [
                        asdict(i)
                        for i in invariants
                    ],
                    "decision": (
                        ExternalizationDecision
                        .REQUIRE_MORE_EVIDENCE
                        .value
                    ),
                    "artifact_committed": False,
                },
                gaps=invariant_gate[
                    "reasons"
                ],
                confidence_ceiling=min(
                    0.50,
                    self.claim_ceiling,
                ),
                provenance=(
                    self._default_provenance()
                ),
            )

        # ----------------------------------------------------
        # 6. Select candidate
        # ----------------------------------------------------

        selected = (
            self._select_target(
                routed_target=(
                    routed_target
                ),
                candidates=(
                    candidates
                ),
            )
        )

        if selected is None:

            return AgentResult(
                status=ExecutionStatus.UNKNOWN,
                capability=ctx.capability,
                summary=(
                    "No candidate satisfies the target "
                    "and hard-constraint envelope."
                ),
                data={
                    "routed_target": (
                        routed_target.value
                    ),
                    "candidate_scores": {
                        (
                            candidate
                            .artifact_type
                            .value
                        ): (
                            candidate
                            .objective_score()
                        )
                        for candidate
                        in candidates
                    },
                },
                gaps=[
                    "no_admissible_candidate"
                ],
                confidence_ceiling=min(
                    0.50,
                    self.claim_ceiling,
                ),
                provenance=(
                    self._default_provenance()
                ),
            )

        # ----------------------------------------------------
        # 7. Bind artifact lifecycle
        # ----------------------------------------------------

        artifact = (
            self._build_artifact_record(
                work_item=work_item,
                selected=selected,
                raw=ctx.inputs.get(
                    "artifact_record",
                    {},
                ),
            )
        )

        # ----------------------------------------------------
        # 8. Define interfaces
        # ----------------------------------------------------

        interfaces = (
            self._parse_interfaces(
                ctx.inputs.get(
                    "interfaces",
                    [],
                )
            )
        )

        interface_issues = (
            self._test_module_interactions(
                selected=selected,
                interfaces=interfaces,
                inputs=ctx.inputs,
            )
        )

        if interface_issues:

            return AgentResult(
                status=(
                    ExecutionStatus.CONDITIONAL
                ),
                capability=ctx.capability,
                summary=(
                    "Target selected but module interfaces "
                    "require correction."
                ),
                data={
                    "selected_target": (
                        selected
                        .artifact_type
                        .value
                    ),
                    "artifact": asdict(
                        artifact
                    ),
                    "interfaces": [
                        asdict(i)
                        for i in interfaces
                    ],
                    "interface_issues": (
                        interface_issues
                    ),
                    "artifact_committed": False,
                },
                gaps=interface_issues,
                confidence_ceiling=min(
                    0.70,
                    self.claim_ceiling,
                ),
                provenance=(
                    self._default_provenance()
                ),
            )

        # ----------------------------------------------------
        # 9. Budget context
        # ----------------------------------------------------

        context_budget = (
            self._budget_context(
                work_item=work_item,
                selected=selected,
                budget=_clamp01(
                    ctx.inputs.get(
                        "context_budget",
                        1.0,
                    )
                ),
            )
        )

        # ----------------------------------------------------
        # 10. Mandatory X / E / D
        # ----------------------------------------------------

        coordinate = (
            self._build_coordinate_state(
                work_item=work_item,
                selected=selected,
                inputs=ctx.inputs,
            )
        )

        evidence = (
            self._parse_evidence(
                ctx.inputs.get(
                    "evidence",
                    [],
                )
            )
        )

        dependency_edges = (
            self._parse_dependency_edges(
                ctx.inputs.get(
                    "dependencies",
                    [],
                )
            )
        )

        graph = (
            self._build_dependency_graph(
                dependency_edges
            )
        )

        # ----------------------------------------------------
        # 11. Competing targets
        # ----------------------------------------------------

        hypotheses = (
            self._build_competing_hypotheses(
                work_item=work_item,
                candidates=candidates,
            )
        )

        # ----------------------------------------------------
        # 12. Confidence ceiling
        # ----------------------------------------------------

        premises = {
            str(key): _clamp01(value)
            for key, value
            in ctx.inputs.get(
                "premise_confidences",
                {},
            ).items()
        }

        confidence = (
            self._confidence_ceiling(
                premises
            )
        )

        # ----------------------------------------------------
        # 13. Decision
        # ----------------------------------------------------

        decision = (
            self._decision_for_target(
                selected.artifact_type
            )
        )

        conclusion_class = (
            ConclusionClass.COMPETING
            if self._has_material_competition(
                hypotheses
            )
            else ConclusionClass.MODEL
        )

        # ----------------------------------------------------
        # 14. RSCF
        # ----------------------------------------------------

        rscf = RSCFCapsule(
            claim=str(
                ctx.inputs.get(
                    "claim",
                    (
                        f"{work_item.item_id} should be "
                        f"externalized to "
                        f"{selected.artifact_type.value}."
                    ),
                )
            ),

            epistemic_class=(
                EpistemicClass.MODEL
            ),

            conclusion_class=(
                conclusion_class
            ),

            scope=str(
                ctx.inputs.get(
                    "scope",
                    work_item.item_id,
                )
            ),

            regime=str(
                ctx.inputs.get(
                    "regime",
                    "default",
                )
            ),

            premises=premises,

            dependencies=[
                edge.parent
                for edge
                in dependency_edges
                if edge.load_bearing
            ],

            coordinate_state=coordinate,

            evidence=evidence,

            competing_hypotheses=(
                hypotheses
            ),

            provenance=(
                self._default_provenance()
            ),

            falsifiers=list(
                ctx.inputs.get(
                    "falsifiers",
                    [],
                )
            ),

            confidence_ceiling=(
                confidence
            ),

            decision=decision,

            selected_target=(
                selected.artifact_type
            ),

            repair_path=ctx.inputs.get(
                "repair_path"
            ),

            rollback_path=ctx.inputs.get(
                "rollback_path"
            ),
        )

        # ----------------------------------------------------
        # 15. Return proposal only
        # ----------------------------------------------------

        status = (
            ExecutionStatus.COMPETING
            if conclusion_class
            == ConclusionClass.COMPETING
            else ExecutionStatus.MODEL
        )

        return AgentResult(
            status=status,

            capability=ctx.capability,

            summary=(
                f"Externalization target selected: "
                f"{selected.artifact_type.value}."
            ),

            data={
                "work_item": asdict(
                    work_item
                ),

                "burden_class": (
                    burden_class.value
                ),

                "routing_matrix_target": (
                    routed_target.value
                ),

                "selected_candidate": (
                    asdict(selected)
                ),

                "candidate_scores": {
                    (
                        candidate
                        .artifact_type
                        .value
                    ): {
                        "source_objective": (
                            candidate
                            .objective_score()
                        ),
                        "diagnostic_extended_cost": (
                            candidate
                            .extended_cost()
                        ),
                    }
                    for candidate
                    in candidates
                },

                "artifact_record": (
                    asdict(artifact)
                ),

                "artifact_freshness": (
                    artifact
                    .freshness_state()
                    .value
                ),

                "interfaces": [
                    asdict(i)
                    for i in interfaces
                ],

                "context_budget": (
                    context_budget
                ),

                "invariants": [
                    asdict(i)
                    for i in invariants
                ],

                "X": asdict(
                    coordinate
                ),

                "E": [
                    asdict(e)
                    for e in evidence
                ],

                "D": [
                    asdict(edge)
                    for edge in dependency_edges
                ],

                "dependency_graph": {
                    parent: sorted(
                        list(children)
                    )
                    for parent, children
                    in graph.descendants.items()
                },

                "rscf": asdict(
                    rscf
                ),

                "artifact_committed": False,

                "authority_granted_by_packaging": False,
            },

            warnings=[
                (
                    "Externalization must reduce cognitive "
                    "burden without hiding decision-critical state."
                ),
                (
                    "Capability packaging does not grant execution "
                    "or persistence authority."
                ),
                (
                    "Target selection is an AMOS MODEL architecture "
                    "decision rule, not a universal empirical law."
                ),
                (
                    "Persistent artifacts require freshness and "
                    "invalidation checks before reuse."
                ),
            ],

            confidence_ceiling=confidence,

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # WORK ITEM PARSER
    # ========================================================

    def _parse_work_item(
        self,
        raw: Any,
    ) -> WorkItem:

        if not isinstance(
            raw,
            dict,
        ):

            raise GapError(
                "UNKNOWN/GAP: work_item dictionary required."
            )

        item_id = raw.get(
            "item_id"
        )

        description = raw.get(
            "description"
        )

        if not item_id:

            raise GapError(
                "UNKNOWN/GAP: work_item.item_id required."
            )

        if not description:

            raise GapError(
                "UNKNOWN/GAP: work_item.description required."
            )

        current_location = None

        if raw.get(
            "current_location"
        ):

            try:

                current_location = (
                    ArtifactType(
                        raw[
                            "current_location"
                        ]
                    )
                )

            except ValueError as exc:

                raise ValidationError(
                    "invalid current_location"
                ) from exc

        return WorkItem(
            item_id=str(
                item_id
            ),

            description=str(
                description
            ),

            recurring=bool(
                raw.get(
                    "recurring",
                    False,
                )
            ),

            deterministic=bool(
                raw.get(
                    "deterministic",
                    False,
                )
            ),

            cross_agent=bool(
                raw.get(
                    "cross_agent",
                    False,
                )
            ),

            cross_tool=bool(
                raw.get(
                    "cross_tool",
                    False,
                )
            ),

            permission_sensitive=bool(
                raw.get(
                    "permission_sensitive",
                    False,
                )
            ),

            requires_persistence=bool(
                raw.get(
                    "requires_persistence",
                    False,
                )
            ),

            transient=bool(
                raw.get(
                    "transient",
                    False,
                )
            ),

            external_capability_required=bool(
                raw.get(
                    "external_capability_required",
                    False,
                )
            ),

            lifetime=_clamp01(
                raw.get(
                    "lifetime",
                    0.0,
                )
            ),

            mutability=_clamp01(
                raw.get(
                    "mutability",
                    0.0,
                )
            ),

            cognitive_burden=_clamp01(
                raw.get(
                    "cognitive_burden",
                    0.0,
                )
            ),

            context_cost=_clamp01(
                raw.get(
                    "context_cost",
                    0.0,
                )
            ),

            authority_required=_clamp01(
                raw.get(
                    "authority_required",
                    0.0,
                )
            ),

            latency_sensitivity=_clamp01(
                raw.get(
                    "latency_sensitivity",
                    0.0,
                )
            ),

            safety_sensitivity=_clamp01(
                raw.get(
                    "safety_sensitivity",
                    0.0,
                )
            ),

            provenance=(
                self._parse_provenance(
                    raw.get(
                        "provenance",
                        [],
                    )
                )
            ),

            current_location=(
                current_location
            ),
        )

    # ========================================================
    # BURDEN CLASSIFICATION
    # ========================================================

    def _classify_burden(
        self,
        item: WorkItem,
    ) -> BurdenClass:

        flags = []

        if item.permission_sensitive:
            flags.append(
                BurdenClass.CONTROL
            )

        if (
            item.cross_agent
            or item.cross_tool
        ):
            flags.append(
                BurdenClass.INTERACTION
            )

        if item.deterministic:
            flags.append(
                BurdenClass.COMPUTATION
            )

        if item.requires_persistence:
            flags.append(
                BurdenClass.STATE
            )

        if item.recurring:
            flags.append(
                BurdenClass.PROCEDURE
            )

        if item.external_capability_required:
            flags.append(
                BurdenClass.TOOL_USE
            )

        if item.transient:
            flags.append(
                BurdenClass.TRANSIENT
            )

        unique = list(
            dict.fromkeys(
                flags
            )
        )

        if len(unique) == 0:
            return BurdenClass.UNKNOWN

        if len(unique) == 1:
            return unique[0]

        # Some combinations have an explicit dominant class.
        if BurdenClass.CONTROL in unique:
            return BurdenClass.CONTROL

        if BurdenClass.INTERACTION in unique:
            return BurdenClass.INTERACTION

        if (
            BurdenClass.COMPUTATION in unique
            and BurdenClass.PROCEDURE in unique
        ):
            return BurdenClass.COMPUTATION

        if BurdenClass.STATE in unique:
            return BurdenClass.STATE

        return BurdenClass.MIXED

    # ========================================================
    # ROUTING
    # ========================================================

    def _route_target(
        self,
        work_item: WorkItem,
        burden_class: BurdenClass,
    ) -> ArtifactType:

        if (
            burden_class
            == BurdenClass.STATE
        ):
            return ArtifactType.MEMORY

        if (
            burden_class
            == BurdenClass.PROCEDURE
        ):

            if work_item.deterministic:
                return ArtifactType.CODE

            return ArtifactType.SKILL

        if (
            burden_class
            == BurdenClass.INTERACTION
        ):
            return ArtifactType.PROTOCOL

        if (
            burden_class
            == BurdenClass.CONTROL
        ):
            return ArtifactType.HARNESS_POLICY

        if (
            burden_class
            == BurdenClass.COMPUTATION
        ):
            return ArtifactType.CODE

        if (
            burden_class
            == BurdenClass.TOOL_USE
        ):
            return ArtifactType.TOOL

        if (
            burden_class
            == BurdenClass.TRANSIENT
        ):
            return ArtifactType.CONTEXT

        if (
            burden_class
            == BurdenClass.MIXED
        ):

            # Mixed burden needs decomposition unless a dominant
            # external requirement is explicitly present.

            if work_item.permission_sensitive:
                return ArtifactType.HARNESS_POLICY

            if (
                work_item.cross_agent
                or work_item.cross_tool
            ):
                return ArtifactType.PROTOCOL

            if work_item.requires_persistence:
                return ArtifactType.MEMORY

            if work_item.deterministic:
                return ArtifactType.CODE

            if work_item.recurring:
                return ArtifactType.SKILL

        # Do not invent persistence.
        return ArtifactType.CONTEXT

    # ========================================================
    # CANDIDATES
    # ========================================================

    def _build_candidates(
        self,
        work_item: WorkItem,
        raw_candidates: Any,
    ) -> List[ExternalizationCandidate]:

        if raw_candidates:

            if not isinstance(
                raw_candidates,
                list,
            ):

                raise ValidationError(
                    "candidate_artifacts must be a list"
                )

            result: List[
                ExternalizationCandidate
            ] = []

            for raw in raw_candidates:

                if not isinstance(
                    raw,
                    dict,
                ):
                    continue

                try:

                    artifact_type = (
                        ArtifactType(
                            raw.get(
                                "artifact_type"
                            )
                        )
                    )

                except Exception:
                    continue

                result.append(
                    ExternalizationCandidate(
                        module=str(
                            raw.get(
                                "module",
                                work_item.item_id,
                            )
                        ),

                        artifact_type=(
                            artifact_type
                        ),

                        cognitive_burden=_clamp01(
                            raw.get(
                                "cognitive_burden",
                                work_item
                                .cognitive_burden,
                            )
                        ),

                        lifetime=_clamp01(
                            raw.get(
                                "lifetime",
                                work_item.lifetime,
                            )
                        ),

                        mutability=_clamp01(
                            raw.get(
                                "mutability",
                                work_item.mutability,
                            )
                        ),

                        authority=_clamp01(
                            raw.get(
                                "authority",
                                work_item
                                .authority_required,
                            )
                        ),

                        budget=_clamp01(
                            raw.get(
                                "budget",
                                0.50,
                            )
                        ),

                        expected_failure=_nonnegative(
                            raw.get(
                                "expected_failure",
                                0.50,
                            )
                        ),

                        maintenance_cost=_nonnegative(
                            raw.get(
                                "maintenance_cost",
                                0.50,
                            )
                        ),

                        drift_risk=_nonnegative(
                            raw.get(
                                "drift_risk",
                                0.50,
                            )
                        ),

                        latency_cost=_nonnegative(
                            raw.get(
                                "latency_cost",
                                0.0,
                            )
                        ),

                        provenance_risk=_nonnegative(
                            raw.get(
                                "provenance_risk",
                                0.0,
                            )
                        ),

                        safety_risk=_nonnegative(
                            raw.get(
                                "safety_risk",
                                0.0,
                            )
                        ),

                        authority_risk=_nonnegative(
                            raw.get(
                                "authority_risk",
                                0.0,
                            )
                        ),

                        provenance=(
                            self._parse_provenance(
                                raw.get(
                                    "provenance",
                                    [],
                                )
                            )
                        ),
                    )
                )

            return result

        # Fallback candidate set.
        #
        # Scores are deliberately neutral. They are placeholders for
        # runtime evidence, not claimed empirically calibrated values.

        return [
            ExternalizationCandidate(
                module=work_item.item_id,
                artifact_type=artifact_type,

                cognitive_burden=(
                    work_item.cognitive_burden
                ),

                lifetime=(
                    work_item.lifetime
                ),

                mutability=(
                    work_item.mutability
                ),

                authority=(
                    work_item.authority_required
                ),

                budget=0.50,

                expected_failure=0.50,
                maintenance_cost=0.50,
                drift_risk=0.50,

                latency_cost=0.25,

                provenance_risk=(
                    0.20
                    if work_item.provenance
                    else 0.80
                ),

                safety_risk=(
                    work_item
                    .safety_sensitivity
                ),

                authority_risk=(
                    work_item
                    .authority_required
                ),

                provenance=(
                    work_item.provenance
                ),
            )
            for artifact_type
            in ArtifactType
        ]

    # ========================================================
    # TARGET SELECTION
    # ========================================================

    def _select_target(
        self,
        routed_target: ArtifactType,
        candidates: List[
            ExternalizationCandidate
        ],
    ) -> Optional[
        ExternalizationCandidate
    ]:

        matching = [
            candidate
            for candidate
            in candidates
            if candidate.artifact_type
            == routed_target
        ]

        if matching:

            admissible = [
                candidate
                for candidate
                in matching
                if self._candidate_admissible(
                    candidate
                )
            ]

            if not admissible:
                return None

            return min(
                admissible,
                key=lambda x:
                    x.objective_score(),
            )

        # If routing-specific candidate is missing, do not silently
        # substitute another substrate when semantics matter.

        return None

    def _candidate_admissible(
        self,
        candidate: ExternalizationCandidate,
    ) -> bool:

        if candidate.safety_risk > 0.75:
            return False

        if candidate.provenance_risk > 0.75:
            return False

        if candidate.authority_risk > 0.75:
            return False

        return True

    # ========================================================
    # HARD INVARIANTS
    # ========================================================

    def _build_invariants(
        self,
        work_item: WorkItem,
        routed_target: ArtifactType,
        inputs: Dict[str, Any],
    ) -> List[HardInvariant]:

        invariants: List[
            HardInvariant
        ] = []

        # ----------------------------------------------------
        # I1 Persistent state -> MEMORY
        # ----------------------------------------------------

        if work_item.requires_persistence:

            invariants.append(
                HardInvariant(
                    invariant_id=(
                        "I_PERSISTENT_STATE_MEMORY"
                    ),

                    description=(
                        "Persistent state belongs in memory, "
                        "not implicit conversational recollection."
                    ),

                    status=(
                        InvariantStatus.PASS
                        if routed_target
                        == ArtifactType.MEMORY
                        else InvariantStatus.FAIL
                    ),
                )
            )

        # ----------------------------------------------------
        # I2 Reusable procedures -> SKILL/CODE
        # ----------------------------------------------------

        if work_item.recurring:

            invariants.append(
                HardInvariant(
                    invariant_id=(
                        "I_REUSABLE_PROCEDURE"
                    ),

                    description=(
                        "Reusable procedures belong in "
                        "skills/code, not repeated free-form "
                        "regeneration."
                    ),

                    status=(
                        InvariantStatus.PASS
                        if routed_target
                        in {
                            ArtifactType.SKILL,
                            ArtifactType.CODE,
                        }
                        else InvariantStatus.FAIL
                    ),
                )
            )

        # ----------------------------------------------------
        # I3 Interaction -> PROTOCOL
        # ----------------------------------------------------

        if (
            work_item.cross_agent
            or work_item.cross_tool
        ):

            invariants.append(
                HardInvariant(
                    invariant_id=(
                        "I_INTERACTION_PROTOCOL"
                    ),

                    description=(
                        "Cross-agent/tool interaction contracts "
                        "belong in protocols."
                    ),

                    status=(
                        InvariantStatus.PASS
                        if routed_target
                        == ArtifactType.PROTOCOL
                        else InvariantStatus.FAIL
                    ),
                )
            )

        # ----------------------------------------------------
        # I4 Permission -> HARNESS_POLICY
        # ----------------------------------------------------

        if work_item.permission_sensitive:

            invariants.append(
                HardInvariant(
                    invariant_id=(
                        "I_PERMISSION_HARNESS"
                    ),

                    description=(
                        "Permissions, sandboxing, approval, "
                        "and execution isolation belong in "
                        "harness policy."
                    ),

                    status=(
                        InvariantStatus.PASS
                        if routed_target
                        == ArtifactType.HARNESS_POLICY
                        else InvariantStatus.FAIL
                    ),
                )
            )

        # ----------------------------------------------------
        # I5 Critical state must remain visible
        # ----------------------------------------------------

        hidden = bool(
            inputs.get(
                "hides_decision_critical_state",
                False,
            )
        )

        invariants.append(
            HardInvariant(
                invariant_id=(
                    "I_DECISION_STATE_VISIBLE"
                ),

                description=(
                    "Externalization must not hide "
                    "decision-critical state."
                ),

                status=(
                    InvariantStatus.FAIL
                    if hidden
                    else InvariantStatus.PASS
                ),

                reason=(
                    "decision-critical state becomes hidden"
                    if hidden
                    else None
                ),
            )
        )

        # ----------------------------------------------------
        # I6 Persistent artifact lifecycle
        # ----------------------------------------------------

        if (
            routed_target
            != ArtifactType.CONTEXT
        ):

            lifecycle_defined = bool(
                inputs.get(
                    "lifecycle_defined",
                    False,
                )
            )

            freshness_defined = bool(
                inputs.get(
                    "freshness_defined",
                    False,
                )
            )

            invalidation_defined = bool(
                inputs.get(
                    "invalidation_defined",
                    False,
                )
            )

            provenance_defined = bool(
                work_item.provenance
            )

            complete = all(
                (
                    lifecycle_defined,
                    freshness_defined,
                    invalidation_defined,
                    provenance_defined,
                )
            )

            invariants.append(
                HardInvariant(
                    invariant_id=(
                        "I_ARTIFACT_LIFECYCLE"
                    ),

                    description=(
                        "Persistent artifacts require lifecycle, "
                        "freshness, provenance, and invalidation "
                        "semantics."
                    ),

                    status=(
                        InvariantStatus.PASS
                        if complete
                        else InvariantStatus.UNKNOWN
                    ),

                    reason=(
                        None
                        if complete
                        else (
                            "persistent artifact lifecycle "
                            "metadata incomplete"
                        )
                    ),
                )
            )

        # ----------------------------------------------------
        # I7 No silent override
        # ----------------------------------------------------

        override = bool(
            inputs.get(
                "silent_cross_module_override",
                False,
            )
        )

        invariants.append(
            HardInvariant(
                invariant_id=(
                    "I_NO_SILENT_OVERRIDE"
                ),

                description=(
                    "Memory, skills, protocols, and harness "
                    "policies cannot silently override one another."
                ),

                status=(
                    InvariantStatus.FAIL
                    if override
                    else InvariantStatus.PASS
                ),
            )
        )

        # ----------------------------------------------------
        # I8 Progressive disclosure
        # ----------------------------------------------------

        progressive = bool(
            inputs.get(
                "progressive_disclosure",
                True,
            )
        )

        invariants.append(
            HardInvariant(
                invariant_id=(
                    "I_PROGRESSIVE_DISCLOSURE"
                ),

                description=(
                    "Load only the artifact required for "
                    "the current decision."
                ),

                status=(
                    InvariantStatus.PASS
                    if progressive
                    else InvariantStatus.FAIL
                ),
            )
        )

        # ----------------------------------------------------
        # I9 Packaging != authority
        # ----------------------------------------------------

        packaging_grants_authority = bool(
            inputs.get(
                "packaging_grants_authority",
                False,
            )
        )

        invariants.append(
            HardInvariant(
                invariant_id=(
                    "I_CAPABILITY_NOT_AUTHORITY"
                ),

                description=(
                    "Capability packaging does not grant authority."
                ),

                status=(
                    InvariantStatus.FAIL
                    if packaging_grants_authority
                    else InvariantStatus.PASS
                ),
            )
        )

        # ----------------------------------------------------
        # I10 Self evolution governance
        # ----------------------------------------------------

        if bool(
            inputs.get(
                "self_evolving_infrastructure",
                False,
            )
        ):

            governance_defined = bool(
                inputs.get(
                    "evolution_governance_defined",
                    False,
                )
            )

            rollback_defined = bool(
                inputs.get(
                    "rollback_defined",
                    False,
                )
            )

            invariants.append(
                HardInvariant(
                    invariant_id=(
                        "I_SELF_EVOLUTION_GOVERNED"
                    ),

                    description=(
                        "Self-evolving infrastructure requires "
                        "explicit governance and rollback."
                    ),

                    status=(
                        InvariantStatus.PASS
                        if (
                            governance_defined
                            and rollback_defined
                        )
                        else InvariantStatus.FAIL
                    ),
                )
            )

        return invariants

    def _evaluate_invariants(
        self,
        invariants: List[HardInvariant],
    ) -> Dict[str, Any]:

        failed = [
            i
            for i
            in invariants
            if i.status
            == InvariantStatus.FAIL
        ]

        if failed:

            return {
                "status":
                    InvariantStatus.FAIL,

                "reasons": [
                    i.reason
                    or i.description
                    for i in failed
                ],
            }

        unknown = [
            i
            for i
            in invariants
            if i.status
            == InvariantStatus.UNKNOWN
        ]

        if unknown:

            return {
                "status":
                    InvariantStatus.UNKNOWN,

                "reasons": [
                    i.reason
                    or i.description
                    for i in unknown
                ],
            }

        return {
            "status":
                InvariantStatus.PASS,

            "reasons": [],
        }

    # ========================================================
    # ARTIFACT LIFECYCLE
    # ========================================================

    def _build_artifact_record(
        self,
        work_item: WorkItem,
        selected: ExternalizationCandidate,
        raw: Any,
    ) -> ArtifactRecord:

        if not isinstance(
            raw,
            dict,
        ):
            raw = {}

        now = time.time()

        invalidation_conditions = list(
            raw.get(
                "invalidation_conditions",
                [],
            )
        )

        if not invalidation_conditions:

            invalidation_conditions = [
                "source evidence changes",
                "scope changes",
                "regime changes",
                "interface/schema changes",
                "authority changes",
                "dependency invalidation",
                "falsifier triggers",
            ]

        return ArtifactRecord(
            artifact_id=str(
                raw.get(
                    "artifact_id",
                    (
                        f"{work_item.item_id}:"
                        f"{selected.artifact_type.value.lower()}"
                    ),
                )
            ),

            artifact_type=(
                selected.artifact_type
            ),

            owner_module=str(
                raw.get(
                    "owner_module",
                    work_item.item_id,
                )
            ),

            scope=str(
                raw.get(
                    "scope",
                    work_item.item_id,
                )
            ),

            lifetime=(
                selected.lifetime
            ),

            mutability=(
                selected.mutability
            ),

            authority_scope=list(
                raw.get(
                    "authority_scope",
                    [],
                )
            ),

            created_at_epoch=float(
                raw.get(
                    "created_at_epoch",
                    now,
                )
            ),

            freshness_timestamp_epoch=float(
                raw.get(
                    "freshness_timestamp_epoch",
                    now,
                )
            ),

            freshness_ttl_seconds=(
                float(
                    raw[
                        "freshness_ttl_seconds"
                    ]
                )
                if raw.get(
                    "freshness_ttl_seconds"
                ) is not None
                else None
            ),

            invalidation_conditions=(
                invalidation_conditions
            ),

            dependencies=list(
                raw.get(
                    "dependencies",
                    [],
                )
            ),

            provenance=(
                selected.provenance
                or work_item.provenance
            ),

            rollback_path=(
                raw.get(
                    "rollback_path"
                )
            ),

            status=(
                ArtifactStatus.PROPOSED
            ),
        )

    # ========================================================
    # INTERFACES
    # ========================================================

    def _parse_interfaces(
        self,
        raw: Any,
    ) -> List[InterfaceContract]:

        if not isinstance(
            raw,
            list,
        ):

            raise ValidationError(
                "interfaces must be a list"
            )

        result: List[
            InterfaceContract
        ] = []

        for index, item in enumerate(
            raw
        ):

            if not isinstance(
                item,
                dict,
            ):
                continue

            result.append(
                InterfaceContract(
                    interface_id=str(
                        item.get(
                            "interface_id",
                            f"IF{index + 1}",
                        )
                    ),

                    producer=str(
                        item.get(
                            "producer",
                            "",
                        )
                    ),

                    consumer=str(
                        item.get(
                            "consumer",
                            "",
                        )
                    ),

                    input_schema=dict(
                        item.get(
                            "input_schema",
                            {},
                        )
                    ),

                    output_schema=dict(
                        item.get(
                            "output_schema",
                            {},
                        )
                    ),

                    authority_boundary=str(
                        item.get(
                            "authority_boundary",
                            "",
                        )
                    ),

                    permission_requirements=list(
                        item.get(
                            "permission_requirements",
                            [],
                        )
                    ),

                    failure_behavior=str(
                        item.get(
                            "failure_behavior",
                            "",
                        )
                    ),

                    provenance_requirements=list(
                        item.get(
                            "provenance_requirements",
                            [],
                        )
                    ),

                    invalidation_behavior=str(
                        item.get(
                            "invalidation_behavior",
                            "",
                        )
                    ),

                    version=item.get(
                        "version"
                    ),
                )
            )

        return result

    def _test_module_interactions(
        self,
        selected: ExternalizationCandidate,
        interfaces: List[InterfaceContract],
        inputs: Dict[str, Any],
    ) -> List[str]:

        issues: List[str] = []

        interface_required = (
            selected.artifact_type
            in {
                ArtifactType.PROTOCOL,
                ArtifactType.TOOL,
                ArtifactType.HARNESS_POLICY,
            }
        )

        if (
            interface_required
            and not interfaces
        ):

            issues.append(
                "selected substrate requires explicit interface contract"
            )

        for interface in interfaces:

            if not interface.producer:

                issues.append(
                    f"{interface.interface_id}:"
                    f"missing_producer"
                )

            if not interface.consumer:

                issues.append(
                    f"{interface.interface_id}:"
                    f"missing_consumer"
                )

            if not interface.failure_behavior:

                issues.append(
                    f"{interface.interface_id}:"
                    f"missing_failure_behavior"
                )

            if not interface.invalidation_behavior:

                issues.append(
                    f"{interface.interface_id}:"
                    f"missing_invalidation_behavior"
                )

            if (
                selected.artifact_type
                == ArtifactType.HARNESS_POLICY
                and not interface.authority_boundary
            ):

                issues.append(
                    f"{interface.interface_id}:"
                    f"missing_authority_boundary"
                )

        if bool(
            inputs.get(
                "interface_cycle_without_boundary",
                False,
            )
        ):

            issues.append(
                "cross-module cycle lacks explicit authority "
                "or invalidation boundary"
            )

        return issues

    # ========================================================
    # CONTEXT BUDGET
    # ========================================================

    def _budget_context(
        self,
        work_item: WorkItem,
        selected: ExternalizationCandidate,
        budget: float,
    ) -> Dict[str, Any]:

        before = (
            work_item.context_cost
        )

        if (
            selected.artifact_type
            == ArtifactType.CONTEXT
        ):

            after = before

        else:

            # MODEL estimate only.
            after = before * 0.35

        return {
            "budget": budget,

            "context_cost_before": before,

            "modeled_context_cost_after": after,

            "within_budget": (
                after <= budget
            ),

            "progressive_disclosure_required": True,

            "classification": "AMOS_MODEL",
        }

    # ========================================================
    # X — COORDINATE STATE
    # ========================================================

    def _build_coordinate_state(
        self,
        work_item: WorkItem,
        selected: ExternalizationCandidate,
        inputs: Dict[str, Any],
    ) -> CoordinateState:

        return CoordinateState(
            item=(
                work_item.item_id
            ),

            layer=str(
                inputs.get(
                    "layer",
                    selected
                    .artifact_type
                    .value,
                )
            ),

            scale=str(
                inputs.get(
                    "scale",
                    "M",
                )
            ),

            time=str(
                inputs.get(
                    "time",
                    "current",
                )
            ),

            regime=str(
                inputs.get(
                    "regime",
                    "default",
                )
            ),

            observer=str(
                inputs.get(
                    "observer",
                    AGENT_ID,
                )
            ),

            provenance=(
                selected.provenance
                or work_item.provenance
            ),

            status=(
                selected.status.value
            ),
        )

    # ========================================================
    # E — EVIDENCE
    # ========================================================

    def _parse_evidence(
        self,
        raw: Any,
    ) -> List[ClaimEvidence]:

        if not isinstance(
            raw,
            list,
        ):

            raise ValidationError(
                "evidence must be a list"
            )

        result: List[
            ClaimEvidence
        ] = []

        for item in raw:

            if not isinstance(
                item,
                dict,
            ):
                continue

            result.append(
                ClaimEvidence(
                    claim=str(
                        item.get(
                            "claim",
                            "",
                        )
                    ),

                    source=str(
                        item.get(
                            "source",
                            "",
                        )
                    ),

                    family=str(
                        item.get(
                            "family",
                            "",
                        )
                    ),

                    independence=bool(
                        item.get(
                            "independence",
                            False,
                        )
                    ),

                    freshness=_clamp01(
                        item.get(
                            "freshness",
                            0.0,
                        )
                    ),

                    scope=str(
                        item.get(
                            "scope",
                            "",
                        )
                    ),

                    confidence=_clamp01(
                        item.get(
                            "confidence",
                            0.0,
                        )
                    ),
                )
            )

        return result

    # ========================================================
    # D — DEPENDENCIES
    # ========================================================

    def _parse_dependency_edges(
        self,
        raw: Any,
    ) -> List[DependencyEdge]:

        if not isinstance(
            raw,
            list,
        ):

            raise ValidationError(
                "dependencies must be a list"
            )

        result: List[
            DependencyEdge
        ] = []

        for item in raw:

            if not isinstance(
                item,
                dict,
            ):
                continue

            parent = item.get(
                "parent"
            )

            child = item.get(
                "child"
            )

            if not parent or not child:
                continue

            result.append(
                DependencyEdge(
                    parent=str(
                        parent
                    ),

                    child=str(
                        child
                    ),

                    edge_type=str(
                        item.get(
                            "type",
                            "dependency",
                        )
                    ),

                    load_bearing=bool(
                        item.get(
                            "load_bearing",
                            False,
                        )
                    ),

                    condition=item.get(
                        "condition"
                    ),
                )
            )

        return result

    def _build_dependency_graph(
        self,
        edges: List[DependencyEdge],
    ) -> DependencyGraph:

        graph = DependencyGraph()

        for edge in edges:

            graph.add_edge(
                edge.parent,
                edge.child,
            )

        return graph

    def invalidate_premise(
        self,
        graph: DependencyGraph,
        premise_id: str,
    ) -> Dict[str, Any]:
        """
        Invalid(p) => Invalidate(descendants(p))
        """

        descendants = (
            graph.closure(
                premise_id
            )
        )

        return {
            "invalid_premise": (
                premise_id
            ),

            "invalidated_descendants": (
                sorted(
                    descendants
                )
            ),

            "unaffected_state_preserved": True,
        }

    # ========================================================
    # COMPETING TARGETS
    # ========================================================

    def _build_competing_hypotheses(
        self,
        work_item: WorkItem,
        candidates: List[
            ExternalizationCandidate
        ],
    ) -> List[
        ExternalizationHypothesis
    ]:

        ranked = sorted(
            candidates,
            key=lambda candidate:
                candidate.objective_score(),
        )

        result: List[
            ExternalizationHypothesis
        ] = []

        for index, candidate in enumerate(
            ranked[:3]
        ):

            confidence = min(
                (
                    1.0
                    / (
                        1.0
                        + candidate
                        .objective_score()
                    )
                ),
                self.claim_ceiling,
            )

            result.append(
                ExternalizationHypothesis(
                    hypothesis_id=(
                        f"H_EXT_{index + 1}"
                    ),

                    target=(
                        candidate.artifact_type
                    ),

                    statement=(
                        f"Externalizing "
                        f"{work_item.item_id} "
                        f"to "
                        f"{candidate.artifact_type.value} "
                        f"may minimize expected failure, "
                        f"maintenance cost, and drift risk "
                        f"under current assumptions."
                    ),

                    confidence=(
                        confidence
                    ),

                    supporting_evidence=[
                        (
                            "objective_score="
                            f"{candidate.objective_score():.4f}"
                        )
                    ],

                    conflicting_evidence=[],

                    falsifiers=[
                        (
                            "Observed maintenance, failure, or drift "
                            "cost exceeds a competing target."
                        ),
                        (
                            "The target violates routing, lifecycle, "
                            "authority, or provenance invariants."
                        ),
                    ],
                )
            )

        return result

    def _has_material_competition(
        self,
        hypotheses: List[
            ExternalizationHypothesis
        ],
    ) -> bool:

        if len(hypotheses) < 2:
            return False

        ranked = sorted(
            hypotheses,
            key=lambda x:
                x.confidence,
            reverse=True,
        )

        return (
            abs(
                ranked[0].confidence
                - ranked[1].confidence
            )
            <= 0.10
        )

    # ========================================================
    # CONFIDENCE
    # ========================================================

    def _confidence_ceiling(
        self,
        premises: Dict[
            str,
            float,
        ],
    ) -> float:
        """
        Conf(C) <= min Conf(load-bearing premises)
        unless independently revalidated.
        """

        if not premises:

            return min(
                0.50,
                self.claim_ceiling,
            )

        weakest = min(
            _clamp01(value)
            for value
            in premises.values()
        )

        return min(
            weakest,
            self.claim_ceiling,
        )

    # ========================================================
    # VALID NOW
    # ========================================================

    @staticmethod
    def valid_now(
        *,
        scope_match: bool,
        regime_match: bool,
        fresh_enough: bool,
        falsifier_triggered: bool,
    ) -> bool:
        """
        ValidNow(C) =
            ScopeMatch
            AND RegimeMatch
            AND FreshEnough
            AND NOT FalsifierTriggered
        """

        return (
            scope_match
            and regime_match
            and fresh_enough
            and not falsifier_triggered
        )

    # ========================================================
    # DECISION
    # ========================================================

    @staticmethod
    def _decision_for_target(
        target: ArtifactType,
    ) -> ExternalizationDecision:

        mapping = {

            ArtifactType.CONTEXT:
                ExternalizationDecision
                .KEEP_IN_CONTEXT,

            ArtifactType.MEMORY:
                ExternalizationDecision
                .EXTERNALIZE_TO_MEMORY,

            ArtifactType.SKILL:
                ExternalizationDecision
                .EXTERNALIZE_TO_SKILL,

            ArtifactType.PROTOCOL:
                ExternalizationDecision
                .EXTERNALIZE_TO_PROTOCOL,

            ArtifactType.CODE:
                ExternalizationDecision
                .EXTERNALIZE_TO_CODE,

            ArtifactType.TOOL:
                ExternalizationDecision
                .EXTERNALIZE_TO_TOOL,

            ArtifactType.HARNESS_POLICY:
                ExternalizationDecision
                .EXTERNALIZE_TO_HARNESS_POLICY,
        }

        return mapping[
            target
        ]

    # ========================================================
    # VALIDATION CAPABILITY
    # ========================================================

    def _validate_architecture(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        architecture = (
            ctx.inputs.get(
                "architecture"
            )
        )

        if not isinstance(
            architecture,
            dict,
        ):

            raise GapError(
                "UNKNOWN/GAP: architecture dictionary required."
            )

        issues: List[str] = []

        if not architecture.get(
            "selected_target"
        ):
            issues.append(
                "missing_selected_target"
            )

        if bool(
            architecture.get(
                "persistent_state_in_context",
                False,
            )
        ):
            issues.append(
                "persistent_state_should_be_memory"
            )

        if bool(
            architecture.get(
                "reusable_procedure_regenerated_freely",
                False,
            )
        ):
            issues.append(
                "reusable_procedure_should_be_skill_or_code"
            )

        if bool(
            architecture.get(
                "interaction_contract_undocumented",
                False,
            )
        ):
            issues.append(
                "interaction_contract_should_be_protocol"
            )

        if bool(
            architecture.get(
                "permissions_in_user_facing_prose",
                False,
            )
        ):
            issues.append(
                "permission_control_should_be_harness_policy"
            )

        if bool(
            architecture.get(
                "decision_critical_state_hidden",
                False,
            )
        ):
            issues.append(
                "externalization_hides_decision_critical_state"
            )

        if bool(
            architecture.get(
                "persistent_artifact",
                False,
            )
        ):

            for key in (
                "lifecycle",
                "freshness",
                "provenance",
                "invalidation",
            ):

                if not architecture.get(
                    key
                ):

                    issues.append(
                        f"persistent_artifact_missing_{key}"
                    )

        if bool(
            architecture.get(
                "silent_cross_module_override",
                False,
            )
        ):
            issues.append(
                "silent_cross_module_override"
            )

        if bool(
            architecture.get(
                "loads_all_artifacts",
                False,
            )
        ):
            issues.append(
                "violates_progressive_disclosure"
            )

        if bool(
            architecture.get(
                "capability_packaging_grants_authority",
                False,
            )
        ):
            issues.append(
                "capability_packaging_does_not_grant_authority"
            )

        if bool(
            architecture.get(
                "self_evolving",
                False,
            )
        ):

            if not architecture.get(
                "governance"
            ):
                issues.append(
                    "self_evolution_missing_governance"
                )

            if not architecture.get(
                "rollback"
            ):
                issues.append(
                    "self_evolution_missing_rollback"
                )

        # This agent proposes architecture.
        # Durable commit belongs to the external control plane.

        if bool(
            architecture.get(
                "artifact_committed",
                False,
            )
        ):
            issues.append(
                "architecture_agent_must_not_self_commit"
            )

        return AgentResult(
            status=(
                ExecutionStatus.VERIFIED
                if not issues
                else ExecutionStatus.CONDITIONAL
            ),

            capability=ctx.capability,

            summary=(
                "Externalization architecture validation completed."
            ),

            data={
                "pass": (
                    not issues
                ),
                "issues": issues,
            },

            gaps=issues,

            confidence_ceiling=(
                self.claim_ceiling
            ),

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # TRACE PROVENANCE
    # ========================================================

    def _trace_provenance(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        records = ctx.inputs.get(
            "records"
        )

        if not isinstance(
            records,
            list,
        ):

            raise GapError(
                "UNKNOWN/GAP: records list required."
            )

        traced: List[
            Dict[str, Any]
        ] = []

        gaps: List[str] = []

        for index, record in enumerate(
            records
        ):

            if not isinstance(
                record,
                dict,
            ):

                gaps.append(
                    f"record[{index}]:invalid"
                )

                continue

            provenance = (
                record.get(
                    "provenance"
                )
            )

            dependencies = (
                record.get(
                    "dependencies",
                    []
                )
            )

            if not provenance:

                gaps.append(
                    f"record[{index}]:missing_provenance"
                )

            traced.append({
                "index": index,

                "record_id": (
                    record.get(
                        "artifact_id"
                    )
                    or record.get(
                        "item_id"
                    )
                    or record.get(
                        "claim_id"
                    )
                    or record.get(
                        "id"
                    )
                ),

                "artifact_type": (
                    record.get(
                        "artifact_type"
                    )
                ),

                "provenance": provenance,

                "dependencies": (
                    dependencies
                ),

                "traceable": bool(
                    provenance
                ),
            })

        return AgentResult(
            status=(
                ExecutionStatus.VERIFIED
                if not gaps
                else ExecutionStatus.CONDITIONAL
            ),

            capability=ctx.capability,

            summary=(
                "Externalization provenance tracing completed."
            ),

            data={
                "records": traced,
            },

            gaps=gaps,

            confidence_ceiling=(
                self.claim_ceiling
            ),

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # CLAIM ASSESSMENT
    # ========================================================

    def _assess_claim(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        claim = ctx.inputs.get(
            "claim"
        )

        if not isinstance(
            claim,
            dict,
        ):

            raise GapError(
                "UNKNOWN/GAP: claim dictionary required."
            )

        issues: List[str] = []

        if not claim.get(
            "scope"
        ):
            issues.append(
                "missing_scope"
            )

        if not claim.get(
            "provenance"
        ):
            issues.append(
                "missing_provenance"
            )

        if bool(
            claim.get(
                "persistent_state_can_rely_on_conversation",
                False,
            )
        ):
            issues.append(
                "persistent_state_requires_explicit_memory"
            )

        if bool(
            claim.get(
                "reusable_procedure_should_be_regenerated",
                False,
            )
        ):
            issues.append(
                "reusable_procedure_should_be_externalized"
            )

        if bool(
            claim.get(
                "interaction_contract_can_remain_implicit",
                False,
            )
        ):
            issues.append(
                "interaction_contract_should_be_protocol"
            )

        if bool(
            claim.get(
                "capability_equals_authority",
                False,
            )
        ):
            issues.append(
                "capability_does_not_equal_authority"
            )

        if bool(
            claim.get(
                "externalization_always_reduces_failure",
                False,
            )
        ):
            issues.append(
                "externalization_requires_scope_specific_validation"
            )

        if bool(
            claim.get(
                "selection_equation_is_empirical_law",
                False,
            )
        ):
            issues.append(
                "selection_equation_is_amos_model"
            )

        if bool(
            claim.get(
                "silent_module_override_is_safe",
                False,
            )
        ):
            issues.append(
                "modules_cannot_silently_override_each_other"
            )

        premise_confidences = {
            str(key): _clamp01(
                value
            )
            for key, value
            in claim.get(
                "premise_confidences",
                {},
            ).items()
        }

        confidence = (
            self._confidence_ceiling(
                premise_confidences
            )
        )

        valid_now = (
            self.valid_now(
                scope_match=bool(
                    claim.get(
                        "scope_match",
                        False,
                    )
                ),

                regime_match=bool(
                    claim.get(
                        "regime_match",
                        False,
                    )
                ),

                fresh_enough=bool(
                    claim.get(
                        "fresh_enough",
                        False,
                    )
                ),

                falsifier_triggered=bool(
                    claim.get(
                        "falsifier_triggered",
                        False,
                    )
                ),
            )
        )

        if not valid_now:

            issues.append(
                "claim_not_valid_now"
            )

        epistemic = str(
            claim.get(
                "epistemic_class",
                "MODEL",
            )
        )

        return AgentResult(
            status=(
                ExecutionStatus.CONDITIONAL
                if issues
                else ExecutionStatus.DERIVED
            ),

            capability=ctx.capability,

            summary=(
                "Externalization claim assessment completed."
            ),

            data={
                "issues": issues,

                "valid_now": (
                    valid_now
                ),

                "classification": (
                    epistemic
                ),

                "confidence_ceiling": (
                    confidence
                ),
            },

            gaps=issues,

            confidence_ceiling=(
                confidence
            ),

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # PROVENANCE
    # ========================================================

    @staticmethod
    def _parse_provenance(
        raw: Any,
    ) -> List[ProvenanceRef]:

        if not isinstance(
            raw,
            list,
        ):
            return []

        result: List[
            ProvenanceRef
        ] = []

        for item in raw:

            if not isinstance(
                item,
                dict,
            ):
                continue

            result.append(
                ProvenanceRef(
                    source=str(
                        item.get(
                            "source",
                            "",
                        )
                    ),

                    path=item.get(
                        "path"
                    ),

                    content_hash=item.get(
                        "content_hash"
                    ),

                    claim_id=item.get(
                        "claim_id"
                    ),

                    source_version=item.get(
                        "source_version"
                    ),

                    timestamp=item.get(
                        "timestamp"
                    ),
                )
            )

        return result

    def _default_provenance(
        self,
    ) -> List[ProvenanceRef]:

        return [
            ProvenanceRef(
                source=(
                    "AMOS Agent Externalization Architecture "
                    "RSCF source skill"
                ),

                path=(
                    ".devin/skills/"
                    "amos-agent-externalization-architecture-rscf/"
                    "SKILL.md"
                ),

                content_hash=(
                    AGENT_CONFIG[
                        "content_hash"
                    ]
                ),
            )
        ]

    # ========================================================
    # UTILS
    # ========================================================

    @staticmethod
    def _new_correlation_id(
    ) -> str:

        raw = (
            f"{AGENT_ID}:"
            f"{time.time_ns()}"
        ).encode()

        return hashlib.sha256(
            raw
        ).hexdigest()[:16]

    @staticmethod
    def result_to_dict(
        result: AgentResult,
    ) -> Dict[str, Any]:

        return asdict(
            result
        )


# ============================================================
# HELPERS
# ============================================================

def _clamp01(
    value: Any,
) -> float:

    return max(
        0.0,
        min(
            1.0,
            float(value),
        ),
    )


def _nonnegative(
    value: Any,
) -> float:

    return max(
        0.0,
        float(value),
    )


# ============================================================
# EXAMPLE
# ============================================================

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO
    )

    agent = (
        AmosAgentExternalizationArchitectureRSCFAgent(
            repo_root="."
        )
    )

    context = ExecutionContext(
        query=(
            "Determine where this recurring deterministic "
            "repository validation procedure should live."
        ),

        capability=(
            "runtime.execute"
        ),

        authorized_write=True,

        authority_witness=(
            "steward_review:example"
        ),

        inputs={

            # ------------------------------------------------
            # Work item
            # ------------------------------------------------

            "work_item": {

                "item_id": (
                    "repository-release-check"
                ),

                "description": (
                    "Repeated deterministic repository "
                    "validation performed before release."
                ),

                "recurring": True,

                "deterministic": True,

                "cross_agent": False,

                "cross_tool": False,

                "permission_sensitive": False,

                "requires_persistence": False,

                "transient": False,

                "external_capability_required": False,

                "lifetime": 0.90,

                "mutability": 0.25,

                "cognitive_burden": 0.85,

                "context_cost": 0.70,

                "authority_required": 0.15,

                "latency_sensitivity": 0.25,

                "safety_sensitivity": 0.20,

                "provenance": [
                    {
                        "source": (
                            "repository-release-policy"
                        ),
                        "path": (
                            "docs/release-policy.md"
                        ),
                    }
                ],
            },

            # ------------------------------------------------
            # Candidate implementations
            # ------------------------------------------------

            "candidate_artifacts": [

                {
                    "module": (
                        "repository-release-check"
                    ),

                    "artifact_type": "CODE",

                    "cognitive_burden": 0.20,

                    "lifetime": 0.90,

                    "mutability": 0.25,

                    "authority": 0.15,

                    "budget": 0.30,

                    "expected_failure": 0.10,

                    "maintenance_cost": 0.20,

                    "drift_risk": 0.10,

                    "latency_cost": 0.05,

                    "provenance_risk": 0.10,

                    "safety_risk": 0.10,

                    "authority_risk": 0.10,

                    "provenance": [
                        {
                            "source": (
                                "repository-release-policy"
                            )
                        }
                    ],
                },

                {
                    "module": (
                        "repository-release-check"
                    ),

                    "artifact_type": "SKILL",

                    "cognitive_burden": 0.35,

                    "lifetime": 0.90,

                    "mutability": 0.30,

                    "authority": 0.15,

                    "budget": 0.35,

                    "expected_failure": 0.25,

                    "maintenance_cost": 0.25,

                    "drift_risk": 0.25,

                    "latency_cost": 0.10,

                    "provenance_risk": 0.10,

                    "safety_risk": 0.10,

                    "authority_risk": 0.10,

                    "provenance": [
                        {
                            "source": (
                                "repository-release-policy"
                            )
                        }
                    ],
                },
            ],

            # ------------------------------------------------
            # Required lifecycle semantics
            # ------------------------------------------------

            "lifecycle_defined": True,

            "freshness_defined": True,

            "invalidation_defined": True,

            # ------------------------------------------------
            # Other invariants
            # ------------------------------------------------

            "progressive_disclosure": True,

            "silent_cross_module_override": False,

            "hides_decision_critical_state": False,

            "packaging_grants_authority": False,

            "self_evolving_infrastructure": False,

            # ------------------------------------------------
            # Artifact metadata
            # ------------------------------------------------

            "artifact_record": {

                "artifact_id": (
                    "code:repository-release-check"
                ),

                "owner_module": "release",

                "scope": "repository-release",

                "authority_scope": [
                    "read",
                    "local-validation",
                ],

                "freshness_ttl_seconds": (
                    60 * 60 * 24 * 30
                ),

                "invalidation_conditions": [
                    "release policy changes",
                    "validator schema changes",
                    "build system changes",
                ],

                "dependencies": [
                    "release-policy"
                ],

                "rollback_path": (
                    "restore prior validation workflow"
                ),
            },

            # CODE does not require an explicit
            # cross-module protocol in this example.

            "interfaces": [],

            # ------------------------------------------------
            # Context budget
            # ------------------------------------------------

            "context_budget": 0.30,

            # ------------------------------------------------
            # X tensor
            # ------------------------------------------------

            "layer": "CODE",

            "scale": "M",

            "time": "current",

            "regime": (
                "repository-release"
            ),

            "observer": AGENT_ID,

            # ------------------------------------------------
            # E tensor
            # ------------------------------------------------

            "evidence": [

                {
                    "claim": (
                        "The release procedure is recurring."
                    ),

                    "source": (
                        "repository-release-policy"
                    ),

                    "family": "repository",

                    "independence": True,

                    "freshness": 0.95,

                    "scope": (
                        "repository-release"
                    ),

                    "confidence": 0.95,
                },

                {
                    "claim": (
                        "The validation steps are deterministic."
                    ),

                    "source": (
                        "existing-validator-tests"
                    ),

                    "family": "runtime",

                    "independence": True,

                    "freshness": 0.90,

                    "scope": (
                        "repository-release"
                    ),

                    "confidence": 0.91,
                },
            ],

            # ------------------------------------------------
            # Confidence
            # ------------------------------------------------

            "premise_confidences": {

                "procedure-recurring": 0.95,

                "procedure-deterministic": 0.91,

                "provenance-valid": 0.90,

                "lifecycle-defined": 0.94,
            },

            # ------------------------------------------------
            # D tensor
            # ------------------------------------------------

            "dependencies": [

                {
                    "parent": (
                        "release-policy"
                    ),

                    "child": (
                        "repository-release-check"
                    ),

                    "type": "governs",

                    "load_bearing": True,

                    "condition": (
                        "policy version unchanged"
                    ),
                }
            ],

            # ------------------------------------------------
            # RSCF
            # ------------------------------------------------

            "claim": (
                "The recurring deterministic release "
                "validation should be externalized to CODE."
            ),

            "falsifiers": [

                (
                    "The workflow becomes substantially "
                    "judgment-based rather than deterministic."
                ),

                (
                    "Observed code maintenance or drift cost "
                    "exceeds a skill-based implementation."
                ),
            ],

            "repair_path": (
                "migrate procedure to SKILL if "
                "judgment requirements materially increase"
            ),

            "rollback_path": (
                "retain previous release-validation "
                "workflow until replacement passes regression"
            ),
        },
    )

    try:

        result = agent.run(
            context
        )

        print(
            json.dumps(
                agent.result_to_dict(
                    result
                ),
                indent=2,
                ensure_ascii=False,
                default=str,
            )
        )

    except ExternalizationArchitectureError as exc:

        print(
            json.dumps(
                {
                    "status": (
                        "FAILED_CLOSED"
                    ),

                    "agent": AGENT_ID,

                    "error": str(
                        exc
                    ),
                },
                indent=2,
                ensure_ascii=False,
            )
        )