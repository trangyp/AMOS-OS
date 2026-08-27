from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Set, Tuple
import hashlib
import json
import logging
import time
import uuid


# ============================================================
# AMOS WORKFLOW BUILDER AGENT
# ============================================================

AGENT_ID = "amos-workflow-builder-agent"
AGENT_VERSION = "1.0.0"

# No canonical amos-workflow-builder Skill exists in the
# currently available Skill registry.
#
# Therefore this agent binds to amos-skill-builder as its
# governing construction/runtime Skill and classifies its
# workflow-specific architecture as DERIVED / AMOS_MODEL.

PRIMARY_SKILL = "amos-skill-builder"
PRIMARY_SKILL_PATH = ".devin/skills/amos-skill-builder/SKILL.md"

CLAIM_CEILING = 0.95


# ============================================================
# ENUMS
# ============================================================

class EpistemicClass(str, Enum):
    SOURCE_CANON = "SOURCE_CANON"
    SOURCE_CLAIM = "SOURCE_CLAIM"
    SOURCE_MODEL = "SOURCE_MODEL"
    DOMAIN_EMPIRICAL = "DOMAIN_EMPIRICAL"
    ESTABLISHED_MATH = "ESTABLISHED_MATH"
    AMOS_MODEL = "AMOS_MODEL"
    EXECUTED_OBSERVATION = "EXECUTED_OBSERVATION"
    DERIVED = "DERIVED"
    DECISION = "DECISION"
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


class WorkflowLifecycle(str, Enum):
    DRAFT = "DRAFT"
    VALIDATING = "VALIDATING"
    READY = "READY"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    CHECKPOINTED = "CHECKPOINTED"
    RECOVERING = "RECOVERING"
    COMPENSATING = "COMPENSATING"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    QUARANTINED = "QUARANTINED"
    RETIRED = "RETIRED"


class StepState(str, Enum):
    PENDING = "PENDING"
    READY = "READY"
    RUNNING = "RUNNING"
    PASS = "PASS"
    FAIL = "FAIL"
    GAP = "GAP"
    BLOCKED = "BLOCKED"
    SKIPPED = "SKIPPED"
    CANCELLED = "CANCELLED"
    COMPENSATED = "COMPENSATED"
    IN_DOUBT = "IN_DOUBT"


class StepType(str, Enum):
    READ = "READ"
    ANALYZE = "ANALYZE"
    DECIDE = "DECIDE"
    TRANSFORM = "TRANSFORM"
    EXECUTE = "EXECUTE"
    VALIDATE = "VALIDATE"
    APPROVE = "APPROVE"
    WAIT = "WAIT"
    BRANCH = "BRANCH"
    FAN_OUT = "FAN_OUT"
    FAN_IN = "FAN_IN"
    CHECKPOINT = "CHECKPOINT"
    COMMIT = "COMMIT"
    COMPENSATE = "COMPENSATE"
    PACKAGE = "PACKAGE"


class EffectClass(str, Enum):
    NONE = "NONE"
    READ_ONLY = "READ_ONLY"
    LOCAL_WRITE = "LOCAL_WRITE"
    DURABLE_WRITE = "DURABLE_WRITE"
    EXTERNAL_EFFECT = "EXTERNAL_EFFECT"
    IRREVERSIBLE = "IRREVERSIBLE"


class GateStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNKNOWN = "UNKNOWN"


class DependencyType(str, Enum):
    DATA = "DATA"
    CONTROL = "CONTROL"
    AUTHORITY = "AUTHORITY"
    EVIDENCE = "EVIDENCE"
    TEMPORAL = "TEMPORAL"
    RESOURCE = "RESOURCE"
    PROVENANCE = "PROVENANCE"


class GapClass(str, Enum):
    CRITICAL = "CRITICAL"
    DECISION_RELEVANT = "DECISION_RELEVANT"
    EXPLANATORY = "EXPLANATORY"
    COSMETIC = "COSMETIC"


class DriftType(str, Enum):
    SCOPE = "SCOPE_DRIFT"
    CONTRACT = "CONTRACT_DRIFT"
    DEPENDENCY = "DEPENDENCY_DRIFT"
    AUTHORITY = "AUTHORITY_DRIFT"
    ENVIRONMENT = "ENVIRONMENT_DRIFT"
    PROVENANCE = "PROVENANCE_DRIFT"
    SCHEMA = "SCHEMA_DRIFT"
    CONFIDENCE = "CONFIDENCE_DECAY"
    NONE = "NONE"


class WorkflowDecision(str, Enum):
    ADMIT = "ADMIT"
    ADMIT_WITH_BOUNDS = "ADMIT_WITH_BOUNDS"
    REQUIRE_APPROVAL = "REQUIRE_APPROVAL"
    REQUIRE_REPAIR = "REQUIRE_REPAIR"
    ESCALATE = "ESCALATE"
    BLOCK = "BLOCK"
    UNKNOWN = "UNKNOWN/GAP"


# ============================================================
# ERRORS
# ============================================================

class WorkflowBuilderError(RuntimeError):
    pass


class ValidationError(WorkflowBuilderError):
    pass


class AuthorizationError(WorkflowBuilderError):
    pass


class GapError(WorkflowBuilderError):
    pass


class WorkflowCycleError(WorkflowBuilderError):
    pass


class CommitAuthorityError(WorkflowBuilderError):
    pass


# ============================================================
# CORE CONTRACTS
# ============================================================

@dataclass(frozen=True)
class ProvenanceRef:
    source: str
    path: Optional[str] = None
    content_hash: Optional[str] = None
    claim_id: Optional[str] = None
    version: Optional[str] = None
    timestamp: Optional[str] = None


@dataclass
class CapabilityContract:
    name: str
    description: str
    side_effect: SideEffect


@dataclass
class AuthorityWitness:
    principal: str
    task: str
    resource: str
    allowed_effects: List[EffectClass]

    policy: Optional[str] = None
    environment: Optional[str] = None

    issued_at: Optional[float] = None
    expires_at: Optional[float] = None

    provenance: List[ProvenanceRef] = field(
        default_factory=list
    )

    def is_fresh(
        self,
        now: Optional[float] = None,
    ) -> bool:

        now = now or time.time()

        if self.expires_at is None:
            return True

        return now <= self.expires_at

    def allows(
        self,
        effect: EffectClass,
    ) -> bool:

        return effect in self.allowed_effects


@dataclass
class WorkflowGate:
    gate_id: str
    description: str

    status: GateStatus

    hard: bool = True

    evidence: List[str] = field(
        default_factory=list
    )

    reason: Optional[str] = None


@dataclass
class RetryPolicy:
    max_attempts: int = 1
    backoff_seconds: float = 0.0

    retry_on: List[str] = field(
        default_factory=list
    )

    idempotent_required: bool = True


@dataclass
class CompensationContract:
    enabled: bool

    action: Optional[str] = None

    preconditions: List[str] = field(
        default_factory=list
    )

    expected_effect: Optional[str] = None

    verified: bool = False


@dataclass
class WorkflowStep:
    step_id: str
    name: str

    step_type: StepType

    description: str

    depends_on: List[str]

    input_contract: Dict[str, Any]
    output_contract: Dict[str, Any]

    effect_class: EffectClass

    required_capabilities: List[str]

    gates: List[WorkflowGate]

    retry_policy: RetryPolicy

    compensation: CompensationContract

    timeout_seconds: Optional[float]

    owner: Optional[str]

    provenance: List[ProvenanceRef]

    epistemic_class: EpistemicClass

    state: StepState = StepState.PENDING

    attempt: int = 0

    started_at: Optional[float] = None
    finished_at: Optional[float] = None

    output: Dict[str, Any] = field(
        default_factory=dict
    )

    errors: List[str] = field(
        default_factory=list
    )


@dataclass
class WorkflowDependency:
    parent: str
    child: str

    dependency_type: DependencyType

    load_bearing: bool

    condition: Optional[str] = None


@dataclass
class WorkflowInvariant:
    invariant_id: str
    description: str

    passed: Optional[bool]

    evidence: List[str] = field(
        default_factory=list
    )

    reason: Optional[str] = None


@dataclass
class WorkflowClaim:
    claim_id: str
    claim: str

    epistemic_class: EpistemicClass

    premises: Dict[str, float]

    dependencies: List[str]

    scope: str
    regime: str

    freshness: float

    falsifiers: List[str]

    provenance: List[ProvenanceRef]

    confidence_ceiling: float


@dataclass
class CompetingWorkflow:
    hypothesis_id: str
    description: str

    workflow_variant: str

    confidence: float

    supporting_evidence: List[str] = field(
        default_factory=list
    )

    conflicting_evidence: List[str] = field(
        default_factory=list
    )

    falsifiers: List[str] = field(
        default_factory=list
    )


@dataclass
class WorkflowRSCF:
    claim: str

    epistemic_class: EpistemicClass

    premises: Dict[str, float]

    evidence: List[str]

    provenance: List[ProvenanceRef]

    dependencies: List[str]

    scope: str
    regime: str

    freshness: float

    falsifiers: List[str]

    competing_workflows: List[
        CompetingWorkflow
    ]

    confidence_ceiling: float

    consequence: Dict[str, Any]

    decision: WorkflowDecision

    repair_path: Optional[str]
    rollback_path: Optional[str]


@dataclass
class WorkflowGap:
    gap_id: str
    gap_class: GapClass

    description: str

    blocking: bool

    affected_steps: List[str]

    repair_action: Optional[str]

    confidence_impact: float


@dataclass
class WorkflowDrift:
    drift_type: DriftType

    description: str

    severity: float

    affected_steps: List[str]

    invalidates: List[str]

    repair_required: bool


@dataclass
class WorkflowExecutionRecord:
    run_id: str

    step_id: str

    attempt: int

    input_hash: str

    environment_hash: str

    authority_hash: Optional[str]

    started_at: float
    finished_at: Optional[float]

    state_before: str
    state_after: Optional[str]

    output_hash: Optional[str]

    error: Optional[str]

    effect_committed: bool

    provenance: List[ProvenanceRef]


@dataclass
class WorkflowCheckpoint:
    checkpoint_id: str

    workflow_id: str

    lifecycle: WorkflowLifecycle

    step_states: Dict[str, str]

    completed_steps: List[str]

    pending_steps: List[str]

    artifacts: Dict[str, Any]

    state_hash: str

    created_at: float


@dataclass
class WorkflowDefinition:
    workflow_id: str

    name: str
    description: str

    version: str

    scope: str
    regime: str

    steps: Dict[str, WorkflowStep]

    dependencies: List[WorkflowDependency]

    invariants: List[WorkflowInvariant]

    claims: List[WorkflowClaim]

    authority_policy: Dict[str, Any]

    resource_budget: Dict[str, Any]

    rollback_policy: Dict[str, Any]

    lifecycle: WorkflowLifecycle

    provenance: List[ProvenanceRef]

    created_at: float
    updated_at: float


@dataclass
class WorkflowRuntimeState:
    workflow: WorkflowDefinition

    executions: List[
        WorkflowExecutionRecord
    ]

    checkpoints: List[
        WorkflowCheckpoint
    ]

    gaps: List[
        WorkflowGap
    ]

    drifts: List[
        WorkflowDrift
    ]

    rscf: Optional[
        WorkflowRSCF
    ] = None

    artifacts: Dict[str, Any] = field(
        default_factory=dict
    )


@dataclass
class ExecutionContext:
    query: str
    capability: str

    inputs: Dict[str, Any] = field(
        default_factory=dict
    )

    authorized_write: bool = False

    authority_witness: Optional[
        AuthorityWitness
    ] = None

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

    confidence_ceiling: float = CLAIM_CEILING

    provenance: List[ProvenanceRef] = field(
        default_factory=list
    )


# ============================================================
# AGENT CONFIG
# ============================================================

AGENT_CONFIG: Dict[str, Any] = {
    "name": AGENT_ID,

    "display_name": (
        "AMOS Workflow Builder"
    ),

    "description": (
        "Build, validate, analyze, govern, checkpoint, recover, "
        "repair, and package executable AMOS workflows as typed "
        "dependency graphs and governed state machines."
    ),

    "version": AGENT_VERSION,

    "author": "Trang Phan",
    "steward": "Trang Phan",

    "system": "AMOS_OS",

    "role": (
        "Workflow design, dependency orchestration, authority gating, "
        "failure recovery, compensation, validation, provenance, "
        "and lifecycle specialist."
    ),

    "skill_binding": {
        "primary_skill": PRIMARY_SKILL,

        "skill_path": PRIMARY_SKILL_PATH,

        "binding_status": (
            "DERIVED until dedicated workflow-builder "
            "Skill is created and admitted"
        ),
    },

    "epistemic_class": "AMOS_MODEL",

    "claim_ceiling": CLAIM_CEILING,

    "governance": {
        "owner_team": "AMOS_CORE",
        "business_domain": "runtime",
        "risk_tier": "medium",
        "observability": (
            "structured_logs+workflow_state_hash"
        ),
        "approval_mode": "steward_review",
        "promotion_state": "derived",
    },
}


CAPABILITIES: Dict[str, CapabilityContract] = {

    "workflow.design":
        CapabilityContract(
            name="workflow.design",
            description=(
                "Design a governed workflow graph from objective, "
                "steps, contracts, dependencies, gates, authority, "
                "retries, compensation, and rollback."
            ),
            side_effect=SideEffect.WRITE,
        ),

    "workflow.validate":
        CapabilityContract(
            name="workflow.validate",
            description=(
                "Validate workflow topology, gates, contracts, "
                "authority boundaries, cycles, retries, rollback, "
                "and promotion readiness."
            ),
            side_effect=SideEffect.READ,
        ),

    "workflow.analyze":
        CapabilityContract(
            name="workflow.analyze",
            description=(
                "Analyze workflow topology, critical path, fan-out, "
                "fan-in, risk concentration, authority surface, "
                "failure propagation, and repair targets."
            ),
            side_effect=SideEffect.READ,
        ),

    "workflow.plan_execution":
        CapabilityContract(
            name="workflow.plan_execution",
            description=(
                "Produce the next executable frontier without "
                "committing effects."
            ),
            side_effect=SideEffect.READ,
        ),

    "workflow.execute_step":
        CapabilityContract(
            name="workflow.execute_step",
            description=(
                "Stage execution of one workflow step under explicit "
                "authority and gate validation."
            ),
            side_effect=SideEffect.WRITE,
        ),

    "workflow.checkpoint":
        CapabilityContract(
            name="workflow.checkpoint",
            description=(
                "Create a deterministic workflow checkpoint."
            ),
            side_effect=SideEffect.WRITE,
        ),

    "workflow.recover":
        CapabilityContract(
            name="workflow.recover",
            description=(
                "Recover from the nearest valid checkpoint while "
                "preserving unaffected work."
            ),
            side_effect=SideEffect.WRITE,
        ),

    "workflow.compensate":
        CapabilityContract(
            name="workflow.compensate",
            description=(
                "Propose or stage compensation for completed durable "
                "steps after partial failure."
            ),
            side_effect=SideEffect.WRITE,
        ),

    "workflow.detect_drift":
        CapabilityContract(
            name="workflow.detect_drift",
            description=(
                "Detect workflow scope, dependency, authority, schema, "
                "environment, provenance, and confidence drift."
            ),
            side_effect=SideEffect.READ,
        ),

    "workflow.trace_provenance":
        CapabilityContract(
            name="workflow.trace_provenance",
            description=(
                "Trace workflow decisions, steps, effects, and claims "
                "to evidence and source lineage."
            ),
            side_effect=SideEffect.READ,
        ),

    "workflow.assess_claim":
        CapabilityContract(
            name="workflow.assess_claim",
            description=(
                "Assess workflow claims for scope, regime, freshness, "
                "premises, provenance, falsifiers, and confidence."
            ),
            side_effect=SideEffect.READ,
        ),

    "workflow.escalate_gaps":
        CapabilityContract(
            name="workflow.escalate_gaps",
            description=(
                "Classify workflow gaps and escalate blocking unknowns."
            ),
            side_effect=SideEffect.WRITE,
        ),

    "workflow.package":
        CapabilityContract(
            name="workflow.package",
            description=(
                "Package the complete validated workflow definition "
                "and execution contract."
            ),
            side_effect=SideEffect.WRITE,
        ),
}


# ============================================================
# WORKFLOW BUILDER AGENT
# ============================================================

class AmosWorkflowBuilderAgent:
    """
    Workflow runtime model.

    Core construction flow:

        ORIENT
        -> DEFINE
        -> DECOMPOSE
        -> TYPE
        -> CONNECT
        -> GATE
        -> AUTHORIZE
        -> PLAN
        -> VALIDATE
        -> SIMULATE
        -> CHALLENGE
        -> REPAIR
        -> CHECKPOINT
        -> PACKAGE

    Execution flow:

        PENDING
        -> READY
        -> RUNNING
        -> PASS | FAIL | GAP | IN_DOUBT

    Durable-effect rule:

        capability != authority

    A write/external effect must be separately authorized.
    """

    def __init__(
        self,
        repo_root: str | Path = ".",
        claim_ceiling: float = CLAIM_CEILING,
    ) -> None:

        self.repo_root = Path(
            repo_root
        ).resolve()

        self.skill_path = (
            self.repo_root
            / ".devin"
            / "skills"
            / "amos-skill-builder"
            / "SKILL.md"
        )

        self.claim_ceiling = min(
            max(
                float(
                    claim_ceiling
                ),
                0.0,
            ),
            CLAIM_CEILING,
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

            "workflow.design":
                self._design,

            "workflow.validate":
                self._validate,

            "workflow.analyze":
                self._analyze,

            "workflow.plan_execution":
                self._plan_execution,

            "workflow.execute_step":
                self._execute_step,

            "workflow.checkpoint":
                self._checkpoint,

            "workflow.recover":
                self._recover,

            "workflow.compensate":
                self._compensate,

            "workflow.detect_drift":
                self._detect_drift,

            "workflow.trace_provenance":
                self._trace_provenance,

            "workflow.assess_claim":
                self._assess_claim,

            "workflow.escalate_gaps":
                self._escalate_gaps,

            "workflow.package":
                self._package,
        }

    # ========================================================
    # ENTRYPOINT
    # ========================================================

    def run(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        ctx.correlation_id = (
            ctx.correlation_id
            or self._new_id(
                "corr"
            )
        )

        self._load_primary_skill()

        if not ctx.query.strip():

            raise ValidationError(
                "query must not be empty"
            )

        capability = CAPABILITIES.get(
            ctx.capability
        )

        if capability is None:

            raise ValidationError(
                f"Unsupported capability: "
                f"{ctx.capability}"
            )

        self._check_agent_capability_authority(
            capability,
            ctx,
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
    # GOVERNING SKILL
    # ========================================================

    def _load_primary_skill(
        self,
    ) -> str:

        if not self.skill_path.exists():

            raise GapError(
                "UNKNOWN/GAP: governing Skill unavailable: "
                f"{self.skill_path}"
            )

        content = self.skill_path.read_text(
            encoding="utf-8"
        )

        if not content.strip():

            raise GapError(
                "UNKNOWN/GAP: governing Skill is empty."
            )

        return content

    # ========================================================
    # AGENT CAPABILITY AUTHORITY
    # ========================================================

    def _check_agent_capability_authority(
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
                "Capability does not confer authority."
            )

        if ctx.authority_witness is None:

            raise AuthorizationError(
                "Write-classified workflow capability "
                "requires an authority witness."
            )

        if not ctx.authority_witness.is_fresh():

            raise AuthorizationError(
                "Authority witness is stale."
            )

    # ========================================================
    # DESIGN
    # ========================================================

    def _design(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        raw = ctx.inputs

        workflow_id = str(
            raw.get(
                "workflow_id",
                self._new_id(
                    "workflow"
                ),
            )
        )

        steps = self._parse_steps(
            raw.get(
                "steps",
                [],
            )
        )

        if not steps:

            raise GapError(
                "UNKNOWN/GAP: workflow requires at least one step."
            )

        dependencies = (
            self._parse_dependencies(
                raw.get(
                    "dependencies",
                    [],
                )
            )
        )

        # Add explicit depends_on edges.
        dependencies.extend(
            self._dependencies_from_steps(
                steps
            )
        )

        dependencies = (
            self._deduplicate_dependencies(
                dependencies
            )
        )

        invariants = (
            self._parse_invariants(
                raw.get(
                    "invariants",
                    [],
                )
            )
        )

        if not invariants:

            invariants = (
                self._default_invariants(
                    steps
                )
            )

        claims = (
            self._parse_claims(
                raw.get(
                    "claims",
                    [],
                )
            )
        )

        now = time.time()

        workflow = WorkflowDefinition(
            workflow_id=workflow_id,

            name=str(
                raw.get(
                    "name",
                    "AMOS Workflow",
                )
            ),

            description=str(
                raw.get(
                    "description",
                    ctx.query,
                )
            ),

            version=str(
                raw.get(
                    "version",
                    "1.0.0",
                )
            ),

            scope=str(
                raw.get(
                    "scope",
                    workflow_id,
                )
            ),

            regime=str(
                raw.get(
                    "regime",
                    "default",
                )
            ),

            steps={
                step.step_id:
                    step
                for step in steps
            },

            dependencies=dependencies,

            invariants=invariants,

            claims=claims,

            authority_policy=dict(
                raw.get(
                    "authority_policy",
                    {},
                )
            ),

            resource_budget=dict(
                raw.get(
                    "resource_budget",
                    {},
                )
            ),

            rollback_policy=dict(
                raw.get(
                    "rollback_policy",
                    {},
                )
            ),

            lifecycle=(
                WorkflowLifecycle.DRAFT
            ),

            provenance=(
                self._parse_provenance(
                    raw.get(
                        "provenance",
                        [],
                    )
                )
                or self._default_provenance()
            ),

            created_at=now,

            updated_at=now,
        )

        issues = (
            self._validate_definition(
                workflow
            )
        )

        if issues:

            decision = (
                WorkflowDecision.REQUIRE_REPAIR
            )

            status = (
                ExecutionStatus.CONDITIONAL
            )

        else:

            workflow.lifecycle = (
                WorkflowLifecycle.READY
            )

            decision = (
                WorkflowDecision.ADMIT
            )

            status = (
                ExecutionStatus.DERIVED
            )

        hypotheses = (
            self._build_competing_workflows(
                raw.get(
                    "competing_workflows",
                    [],
                )
            )
        )

        premise_confidences = {
            str(key):
                self._clamp01(
                    value
                )
            for key, value
            in raw.get(
                "premise_confidences",
                {},
            ).items()
        }

        confidence = (
            self._confidence_ceiling(
                premise_confidences
            )
        )

        rscf = WorkflowRSCF(
            claim=str(
                raw.get(
                    "claim",
                    (
                        "The workflow is structurally admissible "
                        "within its declared scope and regime."
                    ),
                )
            ),

            epistemic_class=(
                EpistemicClass.AMOS_MODEL
            ),

            premises=(
                premise_confidences
            ),

            evidence=list(
                raw.get(
                    "evidence",
                    [],
                )
            ),

            provenance=(
                workflow.provenance
            ),

            dependencies=[
                dependency.parent
                for dependency
                in dependencies
                if dependency.load_bearing
            ],

            scope=workflow.scope,

            regime=workflow.regime,

            freshness=self._clamp01(
                raw.get(
                    "freshness",
                    0.5,
                )
            ),

            falsifiers=list(
                raw.get(
                    "falsifiers",
                    [],
                )
            ),

            competing_workflows=(
                hypotheses
            ),

            confidence_ceiling=(
                confidence
            ),

            consequence=dict(
                raw.get(
                    "consequence",
                    {},
                )
            ),

            decision=decision,

            repair_path=raw.get(
                "repair_path"
            ),

            rollback_path=raw.get(
                "rollback_path"
            ),
        )

        runtime = WorkflowRuntimeState(
            workflow=workflow,
            executions=[],
            checkpoints=[],
            gaps=[
                WorkflowGap(
                    gap_id=self._new_id(
                        "gap"
                    ),
                    gap_class=(
                        GapClass.DECISION_RELEVANT
                    ),
                    description=issue,
                    blocking=True,
                    affected_steps=[],
                    repair_action=(
                        "repair workflow definition and revalidate"
                    ),
                    confidence_impact=0.15,
                )
                for issue in issues
            ],
            drifts=[],
            rscf=rscf,
            artifacts={},
        )

        return AgentResult(
            status=status,

            capability=ctx.capability,

            summary=(
                "Workflow designed."
                if not issues
                else (
                    "Workflow designed with "
                    "validation issues."
                )
            ),

            data={
                "workflow": (
                    self._serialize_workflow(
                        workflow
                    )
                ),

                "rscf": asdict(
                    rscf
                ),

                "validation_issues": (
                    issues
                ),

                "decision": (
                    decision.value
                ),

                "runtime_state": (
                    self._serialize_runtime(
                        runtime
                    )
                ),

                "durable_effect_committed": False,
            },

            gaps=issues,

            warnings=[
                (
                    "Workflow design does not itself authorize "
                    "durable or external effects."
                ),
                (
                    "Workflow-specific architecture is DERIVED / "
                    "AMOS_MODEL until a dedicated workflow-builder "
                    "Skill is created and admitted."
                ),
            ],

            confidence_ceiling=(
                confidence
            ),

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # VALIDATE
    # ========================================================

    def _validate(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        workflow = (
            self._workflow_from_dict(
                ctx.inputs.get(
                    "workflow"
                )
            )
        )

        issues = (
            self._validate_definition(
                workflow
            )
        )

        gate_results = (
            self._evaluate_invariants(
                workflow.invariants
            )
        )

        if gate_results[
            "hard_failures"
        ]:

            issues.extend(
                gate_results[
                    "hard_failures"
                ]
            )

        if gate_results[
            "unknowns"
        ]:

            issues.extend(
                gate_results[
                    "unknowns"
                ]
            )

        return AgentResult(
            status=(
                ExecutionStatus.VERIFIED
                if not issues
                else ExecutionStatus.CONDITIONAL
            ),

            capability=ctx.capability,

            summary=(
                "Workflow validation completed."
            ),

            data={
                "pass": not issues,

                "issues": issues,

                "invariant_gate": (
                    gate_results
                ),

                "topological_order": (
                    self._topological_order(
                        workflow
                    )
                    if not self._has_cycle(
                        workflow
                    )
                    else []
                ),
            },

            gaps=issues,

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # ANALYZE
    # ========================================================

    def _analyze(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        workflow = (
            self._workflow_from_dict(
                ctx.inputs.get(
                    "workflow"
                )
            )
        )

        graph = (
            self._adjacency(
                workflow
            )
        )

        reverse = (
            self._reverse_adjacency(
                workflow
            )
        )

        roots = [
            step_id
            for step_id
            in workflow.steps
            if not reverse.get(
                step_id
            )
        ]

        leaves = [
            step_id
            for step_id
            in workflow.steps
            if not graph.get(
                step_id
            )
        ]

        fanout = {
            step_id:
                len(
                    graph.get(
                        step_id,
                        set(),
                    )
                )
            for step_id
            in workflow.steps
        }

        authority_surface = [
            step.step_id
            for step
            in workflow.steps.values()
            if step.effect_class
            in {
                EffectClass.DURABLE_WRITE,
                EffectClass.EXTERNAL_EFFECT,
                EffectClass.IRREVERSIBLE,
            }
        ]

        uncompensated_effects = [
            step.step_id
            for step
            in workflow.steps.values()
            if (
                step.effect_class
                in {
                    EffectClass.DURABLE_WRITE,
                    EffectClass.EXTERNAL_EFFECT,
                }
                and not step.compensation.enabled
            )
        ]

        return AgentResult(
            status=ExecutionStatus.DERIVED,

            capability=ctx.capability,

            summary=(
                "Workflow topology analysis completed."
            ),

            data={
                "step_count": (
                    len(
                        workflow.steps
                    )
                ),

                "dependency_count": (
                    len(
                        workflow.dependencies
                    )
                ),

                "roots": roots,

                "leaves": leaves,

                "fanout": fanout,

                "authority_surface": (
                    authority_surface
                ),

                "uncompensated_effects": (
                    uncompensated_effects
                ),

                "cycle": (
                    self._has_cycle(
                        workflow
                    )
                ),

                "topological_order": (
                    []
                    if self._has_cycle(
                        workflow
                    )
                    else self._topological_order(
                        workflow
                    )
                ),
            },

            gaps=[
                (
                    f"uncompensated_effect:{step_id}"
                )
                for step_id
                in uncompensated_effects
            ],

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # PLAN EXECUTION FRONTIER
    # ========================================================

    def _plan_execution(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        workflow = (
            self._workflow_from_dict(
                ctx.inputs.get(
                    "workflow"
                )
            )
        )

        ready = (
            self._ready_frontier(
                workflow
            )
        )

        return AgentResult(
            status=ExecutionStatus.DERIVED,

            capability=ctx.capability,

            summary=(
                f"{len(ready)} workflow step(s) are ready."
            ),

            data={
                "ready_steps": ready,

                "no_effect_committed": True,
            },

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # EXECUTE ONE STEP
    # ========================================================

    def _execute_step(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        workflow = (
            self._workflow_from_dict(
                ctx.inputs.get(
                    "workflow"
                )
            )
        )

        step_id = str(
            ctx.inputs.get(
                "step_id",
                "",
            )
        )

        if step_id not in workflow.steps:

            raise GapError(
                f"UNKNOWN/GAP: step not found: "
                f"{step_id}"
            )

        step = workflow.steps[
            step_id
        ]

        # ----------------------------------------------------
        # Dependency readiness
        # ----------------------------------------------------

        blockers = [
            parent
            for parent
            in step.depends_on
            if (
                parent not in workflow.steps
                or workflow.steps[
                    parent
                ].state
                != StepState.PASS
            )
        ]

        if blockers:

            return AgentResult(
                status=ExecutionStatus.CONDITIONAL,

                capability=ctx.capability,

                summary=(
                    "Step blocked by unresolved dependencies."
                ),

                data={
                    "step_id": step_id,
                    "blockers": blockers,
                    "effect_committed": False,
                },

                gaps=blockers,

                provenance=(
                    self._default_provenance()
                ),
            )

        # ----------------------------------------------------
        # Gates
        # ----------------------------------------------------

        gate = (
            self._evaluate_step_gates(
                step
            )
        )

        if gate[
            "failed"
        ]:

            step.state = (
                StepState.BLOCKED
            )

            return AgentResult(
                status=ExecutionStatus.REJECTED,

                capability=ctx.capability,

                summary=(
                    "Step rejected by hard gate."
                ),

                data={
                    "step": (
                        asdict(
                            step
                        )
                    ),
                    "failed_gates": (
                        gate[
                            "failed"
                        ]
                    ),
                    "effect_committed": False,
                },

                gaps=gate[
                    "failed"
                ],

                provenance=(
                    self._default_provenance()
                ),
            )

        if gate[
            "unknown"
        ]:

            step.state = (
                StepState.GAP
            )

            return AgentResult(
                status=ExecutionStatus.UNKNOWN,

                capability=ctx.capability,

                summary=(
                    "Step gate is UNKNOWN/GAP."
                ),

                data={
                    "step": (
                        asdict(
                            step
                        )
                    ),
                    "unknown_gates": (
                        gate[
                            "unknown"
                        ]
                    ),
                    "effect_committed": False,
                },

                gaps=gate[
                    "unknown"
                ],

                provenance=(
                    self._default_provenance()
                ),
            )

        # ----------------------------------------------------
        # Effect authority
        # ----------------------------------------------------

        if step.effect_class not in {
            EffectClass.NONE,
            EffectClass.READ_ONLY,
        }:

            witness = (
                ctx.authority_witness
            )

            if witness is None:

                raise CommitAuthorityError(
                    "Effect-bearing step requires "
                    "authority witness."
                )

            if not witness.is_fresh():

                raise CommitAuthorityError(
                    "Authority witness expired."
                )

            if not witness.allows(
                step.effect_class
            ):

                raise CommitAuthorityError(
                    f"Authority does not permit "
                    f"{step.effect_class.value}."
                )

        # ----------------------------------------------------
        # Stage execution result supplied by host runtime
        # ----------------------------------------------------

        execution = ctx.inputs.get(
            "execution_result"
        )

        if not isinstance(
            execution,
            dict,
        ):

            raise GapError(
                "UNKNOWN/GAP: execution_result required. "
                "The Workflow Builder does not fabricate runtime execution."
            )

        actually_executed = bool(
            execution.get(
                "executed",
                False,
            )
        )

        if not actually_executed:

            step.state = (
                StepState.GAP
            )

            raise GapError(
                "EXECUTION_GAP: host runtime did not execute step."
            )

        step.attempt += 1

        step.started_at = (
            execution.get(
                "started_at",
                time.time(),
            )
        )

        success = bool(
            execution.get(
                "success",
                False,
            )
        )

        step.finished_at = (
            execution.get(
                "finished_at",
                time.time(),
            )
        )

        effect_committed = bool(
            execution.get(
                "effect_committed",
                False,
            )
        )

        if success:

            step.state = (
                StepState.PASS
            )

            step.output = dict(
                execution.get(
                    "output",
                    {},
                )
            )

        else:

            step.state = (
                StepState.FAIL
            )

            step.errors.append(
                str(
                    execution.get(
                        "error",
                        "unknown execution failure",
                    )
                )
            )

        record = (
            WorkflowExecutionRecord(
                run_id=self._new_id(
                    "run"
                ),

                step_id=step.step_id,

                attempt=step.attempt,

                input_hash=str(
                    execution.get(
                        "input_hash",
                        "",
                    )
                ),

                environment_hash=str(
                    execution.get(
                        "environment_hash",
                        "",
                    )
                ),

                authority_hash=(
                    self._hash_object(
                        asdict(
                            ctx.authority_witness
                        )
                    )
                    if ctx.authority_witness
                    else None
                ),

                started_at=(
                    step.started_at
                ),

                finished_at=(
                    step.finished_at
                ),

                state_before=(
                    "READY"
                ),

                state_after=(
                    step.state.value
                ),

                output_hash=(
                    self._hash_object(
                        step.output
                    )
                    if step.output
                    else None
                ),

                error=(
                    step.errors[-1]
                    if step.errors
                    else None
                ),

                effect_committed=(
                    effect_committed
                ),

                provenance=(
                    self._parse_provenance(
                        execution.get(
                            "provenance",
                            [],
                        )
                    )
                ),
            )
        )

        return AgentResult(
            status=(
                ExecutionStatus.VERIFIED
                if success
                else ExecutionStatus.CONDITIONAL
            ),

            capability=ctx.capability,

            summary=(
                f"Step {step.step_id} "
                f"{step.state.value}."
            ),

            data={
                "step": (
                    asdict(
                        step
                    )
                ),

                "execution_record": (
                    asdict(
                        record
                    )
                ),

                "workflow_effect_committed": (
                    effect_committed
                ),
            },

            gaps=(
                step.errors
                if not success
                else []
            ),

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # CHECKPOINT
    # ========================================================

    def _checkpoint(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        workflow = (
            self._workflow_from_dict(
                ctx.inputs.get(
                    "workflow"
                )
            )
        )

        completed = [
            step_id
            for step_id, step
            in workflow.steps.items()
            if step.state
            == StepState.PASS
        ]

        pending = [
            step_id
            for step_id, step
            in workflow.steps.items()
            if step.state
            not in {
                StepState.PASS,
                StepState.COMPENSATED,
                StepState.CANCELLED,
            }
        ]

        payload = (
            self._serialize_workflow(
                workflow
            )
        )

        checkpoint = (
            WorkflowCheckpoint(
                checkpoint_id=self._new_id(
                    "checkpoint"
                ),

                workflow_id=(
                    workflow.workflow_id
                ),

                lifecycle=(
                    WorkflowLifecycle.CHECKPOINTED
                ),

                step_states={
                    step_id:
                        step.state.value
                    for step_id, step
                    in workflow.steps.items()
                },

                completed_steps=completed,

                pending_steps=pending,

                artifacts=dict(
                    ctx.inputs.get(
                        "artifacts",
                        {},
                    )
                ),

                state_hash=(
                    self._hash_object(
                        payload
                    )
                ),

                created_at=(
                    time.time()
                ),
            )
        )

        return AgentResult(
            status=ExecutionStatus.VERIFIED,

            capability=ctx.capability,

            summary=(
                "Workflow checkpoint created."
            ),

            data={
                "checkpoint": (
                    asdict(
                        checkpoint
                    )
                ),
            },

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # RECOVER
    # ========================================================

    def _recover(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        checkpoint = (
            ctx.inputs.get(
                "checkpoint"
            )
        )

        if not isinstance(
            checkpoint,
            dict,
        ):

            raise GapError(
                "UNKNOWN/GAP: checkpoint required."
            )

        expected_hash = (
            checkpoint.get(
                "state_hash"
            )
        )

        if not expected_hash:

            raise GapError(
                "UNKNOWN/GAP: checkpoint lacks state_hash."
            )

        invalidated = list(
            ctx.inputs.get(
                "invalidated_steps",
                [],
            )
        )

        completed = list(
            checkpoint.get(
                "completed_steps",
                [],
            )
        )

        preserved = [
            step_id
            for step_id
            in completed
            if step_id
            not in invalidated
        ]

        rerun = list(
            dict.fromkeys(
                invalidated
                + checkpoint.get(
                    "pending_steps",
                    [],
                )
            )
        )

        return AgentResult(
            status=ExecutionStatus.DERIVED,

            capability=ctx.capability,

            summary=(
                "Workflow recovery plan created."
            ),

            data={
                "preserved_completed_steps":
                    preserved,

                "steps_to_revalidate_or_rerun":
                    rerun,

                "recovery_rule": (
                    "invalidate only failed premises/edges and "
                    "their descendants; preserve unaffected work"
                ),
            },

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # COMPENSATE
    # ========================================================

    def _compensate(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        workflow = (
            self._workflow_from_dict(
                ctx.inputs.get(
                    "workflow"
                )
            )
        )

        failed_step = str(
            ctx.inputs.get(
                "failed_step",
                "",
            )
        )

        if failed_step not in workflow.steps:

            raise GapError(
                "UNKNOWN/GAP: failed_step not found."
            )

        completed_effect_steps = [
            step
            for step
            in workflow.steps.values()
            if (
                step.state
                == StepState.PASS
                and step.effect_class
                in {
                    EffectClass.LOCAL_WRITE,
                    EffectClass.DURABLE_WRITE,
                    EffectClass.EXTERNAL_EFFECT,
                }
            )
        ]

        plan = []

        gaps = []

        for step in reversed(
            completed_effect_steps
        ):

            if not step.compensation.enabled:

                gaps.append(
                    (
                        f"step:{step.step_id}:"
                        f"no_compensation_contract"
                    )
                )

                continue

            if not step.compensation.verified:

                gaps.append(
                    (
                        f"step:{step.step_id}:"
                        f"compensation_unverified"
                    )
                )

            plan.append({
                "step_id": step.step_id,

                "compensation_action":
                    step.compensation.action,

                "verified":
                    step.compensation.verified,
            })

        return AgentResult(
            status=(
                ExecutionStatus.CONDITIONAL
                if gaps
                else ExecutionStatus.DERIVED
            ),

            capability=ctx.capability,

            summary=(
                "Compensation plan generated."
            ),

            data={
                "failed_step": (
                    failed_step
                ),

                "compensation_plan": (
                    plan
                ),

                "partial_rollback_is_not_atomic_rollback":
                    True,

                "effect_committed":
                    False,
            },

            gaps=gaps,

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # DRIFT
    # ========================================================

    def _detect_drift(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        baseline = ctx.inputs.get(
            "baseline",
            {}
        )

        current = ctx.inputs.get(
            "current",
            {}
        )

        if not isinstance(
            baseline,
            dict,
        ) or not isinstance(
            current,
            dict,
        ):

            raise GapError(
                "UNKNOWN/GAP: baseline/current dictionaries required."
            )

        mappings = {
            "scope":
                DriftType.SCOPE,

            "contract_hash":
                DriftType.CONTRACT,

            "dependency_hash":
                DriftType.DEPENDENCY,

            "authority_epoch":
                DriftType.AUTHORITY,

            "environment_hash":
                DriftType.ENVIRONMENT,

            "provenance_hash":
                DriftType.PROVENANCE,

            "schema_hash":
                DriftType.SCHEMA,
        }

        drifts: List[
            WorkflowDrift
        ] = []

        for key, drift_type in mappings.items():

            if baseline.get(
                key
            ) != current.get(
                key
            ):

                drifts.append(
                    WorkflowDrift(
                        drift_type=(
                            drift_type
                        ),

                        description=(
                            f"{key} changed"
                        ),

                        severity=self._clamp01(
                            ctx.inputs.get(
                                f"{key}_severity",
                                0.5,
                            )
                        ),

                        affected_steps=list(
                            ctx.inputs.get(
                                f"{key}_affected_steps",
                                [],
                            )
                        ),

                        invalidates=list(
                            ctx.inputs.get(
                                f"{key}_invalidates",
                                [],
                            )
                        ),

                        repair_required=True,
                    )
                )

        baseline_conf = self._clamp01(
            baseline.get(
                "confidence",
                1.0,
            )
        )

        current_conf = self._clamp01(
            current.get(
                "confidence",
                baseline_conf,
            )
        )

        if current_conf < baseline_conf:

            drifts.append(
                WorkflowDrift(
                    drift_type=(
                        DriftType.CONFIDENCE
                    ),

                    description=(
                        "workflow confidence decayed"
                    ),

                    severity=(
                        baseline_conf
                        - current_conf
                    ),

                    affected_steps=list(
                        ctx.inputs.get(
                            "confidence_affected_steps",
                            [],
                        )
                    ),

                    invalidates=list(
                        ctx.inputs.get(
                            "confidence_invalidates",
                            [],
                        )
                    ),

                    repair_required=True,
                )
            )

        return AgentResult(
            status=(
                ExecutionStatus.CONDITIONAL
                if drifts
                else ExecutionStatus.VERIFIED
            ),

            capability=ctx.capability,

            summary=(
                f"{len(drifts)} workflow drift condition(s) detected."
            ),

            data={
                "drifts": [
                    asdict(
                        drift
                    )
                    for drift
                    in drifts
                ],
            },

            gaps=[
                drift.description
                for drift in drifts
            ],

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # PROVENANCE
    # ========================================================

    def _trace_provenance(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        records = ctx.inputs.get(
            "records",
            []
        )

        if not isinstance(
            records,
            list,
        ):

            raise ValidationError(
                "records must be a list"
            )

        traced = []
        gaps = []

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

            provenance = record.get(
                "provenance"
            )

            if not provenance:

                gaps.append(
                    f"record[{index}]:missing_provenance"
                )

            traced.append({
                "index": index,

                "record_id": (
                    record.get(
                        "step_id"
                    )
                    or record.get(
                        "workflow_id"
                    )
                    or record.get(
                        "claim_id"
                    )
                    or record.get(
                        "id"
                    )
                ),

                "provenance": (
                    provenance
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
                "Workflow provenance tracing completed."
            ),

            data={
                "records": traced,
            },

            gaps=gaps,

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

        issues = []

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

        if claim.get(
            "capability_equals_authority"
        ) is True:

            issues.append(
                "capability_does_not_equal_authority"
            )

        if claim.get(
            "successful_step_equals_successful_workflow"
        ) is True:

            issues.append(
                "local_success_does_not_prove_workflow_success"
            )

        if claim.get(
            "partial_rollback_is_atomic"
        ) is True:

            issues.append(
                "partial_rollback_is_not_atomic_rollback"
            )

        if claim.get(
            "retry_is_safe_without_idempotency"
        ) is True:

            issues.append(
                "retry_requires_idempotency_or_equivalent_guard"
            )

        premises = {
            str(key):
                self._clamp01(
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
                premises
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
                "Workflow claim assessment completed."
            ),

            data={
                "issues": issues,

                "confidence_ceiling":
                    confidence,

                "epistemic_class":
                    claim.get(
                        "epistemic_class",
                        "AMOS_MODEL",
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
    # GAP ESCALATION
    # ========================================================

    def _escalate_gaps(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        raw_gaps = ctx.inputs.get(
            "gaps",
            []
        )

        if not isinstance(
            raw_gaps,
            list,
        ):

            raise ValidationError(
                "gaps must be a list"
            )

        gaps = []

        for raw in raw_gaps:

            if not isinstance(
                raw,
                dict,
            ):
                continue

            gap_class = GapClass(
                raw.get(
                    "gap_class",
                    "DECISION_RELEVANT",
                )
            )

            gaps.append(
                WorkflowGap(
                    gap_id=str(
                        raw.get(
                            "gap_id",
                            self._new_id(
                                "gap"
                            ),
                        )
                    ),

                    gap_class=(
                        gap_class
                    ),

                    description=str(
                        raw.get(
                            "description",
                            "",
                        )
                    ),

                    blocking=bool(
                        raw.get(
                            "blocking",
                            gap_class
                            == GapClass.CRITICAL,
                        )
                    ),

                    affected_steps=list(
                        raw.get(
                            "affected_steps",
                            [],
                        )
                    ),

                    repair_action=(
                        raw.get(
                            "repair_action"
                        )
                    ),

                    confidence_impact=self._clamp01(
                        raw.get(
                            "confidence_impact",
                            0.1,
                        )
                    ),
                )
            )

        priority = {
            GapClass.CRITICAL: 0,
            GapClass.DECISION_RELEVANT: 1,
            GapClass.EXPLANATORY: 2,
            GapClass.COSMETIC: 3,
        }

        gaps.sort(
            key=lambda gap:
                priority[
                    gap.gap_class
                ]
        )

        base_conf = self._clamp01(
            ctx.inputs.get(
                "base_confidence",
                self.claim_ceiling,
            )
        )

        penalty = sum(
            gap.confidence_impact
            for gap in gaps
            if gap.gap_class
            in {
                GapClass.CRITICAL,
                GapClass.DECISION_RELEVANT,
            }
        )

        confidence = max(
            0.0,
            base_conf - penalty,
        )

        blocking = [
            gap
            for gap in gaps
            if gap.blocking
        ]

        return AgentResult(
            status=(
                ExecutionStatus.UNKNOWN
                if blocking
                else ExecutionStatus.CONDITIONAL
            ),

            capability=ctx.capability,

            summary=(
                "Workflow gaps classified and escalated."
            ),

            data={
                "ordered_gaps": [
                    asdict(
                        gap
                    )
                    for gap
                    in gaps
                ],

                "blocking_count":
                    len(
                        blocking
                    ),

                "confidence_after_downgrade":
                    confidence,
            },

            gaps=[
                gap.description
                for gap in gaps
            ],

            confidence_ceiling=(
                confidence
            ),

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # PACKAGE
    # ========================================================

    def _package(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        workflow = (
            self._workflow_from_dict(
                ctx.inputs.get(
                    "workflow"
                )
            )
        )

        issues = (
            self._validate_definition(
                workflow
            )
        )

        if issues:

            return AgentResult(
                status=ExecutionStatus.REJECTED,

                capability=ctx.capability,

                summary=(
                    "Workflow cannot be packaged."
                ),

                data={
                    "issues": issues,
                    "packaged": False,
                },

                gaps=issues,

                provenance=(
                    self._default_provenance()
                ),
            )

        package = {
            "workflow.json":
                self._serialize_workflow(
                    workflow
                ),

            "workflow.md":
                self._render_workflow_markdown(
                    workflow
                ),

            "manifest": {
                "workflow_id":
                    workflow.workflow_id,

                "version":
                    workflow.version,

                "content_hash":
                    self._hash_object(
                        self._serialize_workflow(
                            workflow
                        )
                    ),

                "epistemic_class":
                    "AMOS_MODEL",

                "primary_builder_skill":
                    PRIMARY_SKILL,

                "dedicated_workflow_skill":
                    None,

                "status":
                    "DERIVED",
            },
        }

        return AgentResult(
            status=ExecutionStatus.DERIVED,

            capability=ctx.capability,

            summary=(
                "Workflow package prepared."
            ),

            data={
                "package": package,

                "packaged": True,

                "installed": False,
            },

            warnings=[
                (
                    "Packaging is not installation."
                )
            ],

            provenance=(
                self._default_provenance()
            ),
        )

    # ========================================================
    # STEP PARSING
    # ========================================================

    def _parse_steps(
        self,
        raw_steps: Any,
    ) -> List[WorkflowStep]:

        if not isinstance(
            raw_steps,
            list,
        ):

            raise ValidationError(
                "steps must be a list"
            )

        steps = []

        for index, raw in enumerate(
            raw_steps
        ):

            if not isinstance(
                raw,
                dict,
            ):
                continue

            step_id = str(
                raw.get(
                    "step_id",
                    f"step-{index + 1}",
                )
            )

            gates = []

            for gate_raw in raw.get(
                "gates",
                [],
            ):

                if not isinstance(
                    gate_raw,
                    dict,
                ):
                    continue

                gates.append(
                    WorkflowGate(
                        gate_id=str(
                            gate_raw.get(
                                "gate_id",
                                self._new_id(
                                    "gate"
                                ),
                            )
                        ),

                        description=str(
                            gate_raw.get(
                                "description",
                                "",
                            )
                        ),

                        status=GateStatus(
                            gate_raw.get(
                                "status",
                                "UNKNOWN",
                            )
                        ),

                        hard=bool(
                            gate_raw.get(
                                "hard",
                                True,
                            )
                        ),

                        evidence=list(
                            gate_raw.get(
                                "evidence",
                                [],
                            )
                        ),

                        reason=(
                            gate_raw.get(
                                "reason"
                            )
                        ),
                    )
                )

            retry_raw = raw.get(
                "retry_policy",
                {}
            )

            if not isinstance(
                retry_raw,
                dict,
            ):
                retry_raw = {}

            comp_raw = raw.get(
                "compensation",
                {}
            )

            if not isinstance(
                comp_raw,
                dict,
            ):
                comp_raw = {}

            steps.append(
                WorkflowStep(
                    step_id=step_id,

                    name=str(
                        raw.get(
                            "name",
                            step_id,
                        )
                    ),

                    step_type=StepType(
                        raw.get(
                            "step_type",
                            "ANALYZE",
                        )
                    ),

                    description=str(
                        raw.get(
                            "description",
                            "",
                        )
                    ),

                    depends_on=list(
                        raw.get(
                            "depends_on",
                            [],
                        )
                    ),

                    input_contract=dict(
                        raw.get(
                            "input_contract",
                            {},
                        )
                    ),

                    output_contract=dict(
                        raw.get(
                            "output_contract",
                            {},
                        )
                    ),

                    effect_class=EffectClass(
                        raw.get(
                            "effect_class",
                            "NONE",
                        )
                    ),

                    required_capabilities=list(
                        raw.get(
                            "required_capabilities",
                            [],
                        )
                    ),

                    gates=gates,

                    retry_policy=(
                        RetryPolicy(
                            max_attempts=max(
                                int(
                                    retry_raw.get(
                                        "max_attempts",
                                        1,
                                    )
                                ),
                                1,
                            ),

                            backoff_seconds=max(
                                float(
                                    retry_raw.get(
                                        "backoff_seconds",
                                        0.0,
                                    )
                                ),
                                0.0,
                            ),

                            retry_on=list(
                                retry_raw.get(
                                    "retry_on",
                                    [],
                                )
                            ),

                            idempotent_required=bool(
                                retry_raw.get(
                                    "idempotent_required",
                                    True,
                                )
                            ),
                        )
                    ),

                    compensation=(
                        CompensationContract(
                            enabled=bool(
                                comp_raw.get(
                                    "enabled",
                                    False,
                                )
                            ),

                            action=(
                                comp_raw.get(
                                    "action"
                                )
                            ),

                            preconditions=list(
                                comp_raw.get(
                                    "preconditions",
                                    [],
                                )
                            ),

                            expected_effect=(
                                comp_raw.get(
                                    "expected_effect"
                                )
                            ),

                            verified=bool(
                                comp_raw.get(
                                    "verified",
                                    False,
                                )
                            ),
                        )
                    ),

                    timeout_seconds=(
                        float(
                            raw[
                                "timeout_seconds"
                            ]
                        )
                        if raw.get(
                            "timeout_seconds"
                        ) is not None
                        else None
                    ),

                    owner=raw.get(
                        "owner"
                    ),

                    provenance=(
                        self._parse_provenance(
                            raw.get(
                                "provenance",
                                [],
                            )
                        )
                    ),

                    epistemic_class=(
                        self._parse_epistemic(
                            raw.get(
                                "epistemic_class",
                                "AMOS_MODEL",
                            )
                        )
                    ),

                    state=StepState(
                        raw.get(
                            "state",
                            "PENDING",
                        )
                    ),

                    attempt=int(
                        raw.get(
                            "attempt",
                            0,
                        )
                    ),

                    output=dict(
                        raw.get(
                            "output",
                            {},
                        )
                    ),

                    errors=list(
                        raw.get(
                            "errors",
                            [],
                        )
                    ),
                )
            )

        return steps

    # ========================================================
    # DEPENDENCY PARSING
    # ========================================================

    def _parse_dependencies(
        self,
        raw: Any,
    ) -> List[WorkflowDependency]:

        if not isinstance(
            raw,
            list,
        ):

            raise ValidationError(
                "dependencies must be a list"
            )

        result = []

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
                WorkflowDependency(
                    parent=str(
                        parent
                    ),

                    child=str(
                        child
                    ),

                    dependency_type=(
                        DependencyType(
                            item.get(
                                "dependency_type",
                                "CONTROL",
                            )
                        )
                    ),

                    load_bearing=bool(
                        item.get(
                            "load_bearing",
                            True,
                        )
                    ),

                    condition=(
                        item.get(
                            "condition"
                        )
                    ),
                )
            )

        return result

    def _dependencies_from_steps(
        self,
        steps: Iterable[
            WorkflowStep
        ],
    ) -> List[
        WorkflowDependency
    ]:

        dependencies = []

        for step in steps:

            for parent in step.depends_on:

                dependencies.append(
                    WorkflowDependency(
                        parent=str(
                            parent
                        ),

                        child=(
                            step.step_id
                        ),

                        dependency_type=(
                            DependencyType.CONTROL
                        ),

                        load_bearing=True,
                    )
                )

        return dependencies

    @staticmethod
    def _deduplicate_dependencies(
        dependencies: List[
            WorkflowDependency
        ],
    ) -> List[
        WorkflowDependency
    ]:

        seen = set()

        result = []

        for dependency in dependencies:

            key = (
                dependency.parent,
                dependency.child,
                dependency.dependency_type.value,
            )

            if key in seen:
                continue

            seen.add(
                key
            )

            result.append(
                dependency
            )

        return result

    # ========================================================
    # INVARIANTS
    # ========================================================

    def _parse_invariants(
        self,
        raw: Any,
    ) -> List[WorkflowInvariant]:

        if not isinstance(
            raw,
            list,
        ):

            raise ValidationError(
                "invariants must be a list"
            )

        result = []

        for item in raw:

            if not isinstance(
                item,
                dict,
            ):
                continue

            result.append(
                WorkflowInvariant(
                    invariant_id=str(
                        item.get(
                            "invariant_id",
                            self._new_id(
                                "inv"
                            ),
                        )
                    ),

                    description=str(
                        item.get(
                            "description",
                            "",
                        )
                    ),

                    passed=(
                        item.get(
                            "passed"
                        )
                    ),

                    evidence=list(
                        item.get(
                            "evidence",
                            [],
                        )
                    ),

                    reason=(
                        item.get(
                            "reason"
                        )
                    ),
                )
            )

        return result

    def _default_invariants(
        self,
        steps: Iterable[
            WorkflowStep
        ],
    ) -> List[
        WorkflowInvariant
    ]:

        return [

            WorkflowInvariant(
                invariant_id=(
                    "I_NO_AUTHORITY_ESCALATION"
                ),

                description=(
                    "A workflow step may not gain authority "
                    "merely through dependency or capability."
                ),

                passed=True,

                evidence=[
                    "workflow builder control rule"
                ],
            ),

            WorkflowInvariant(
                invariant_id=(
                    "I_NO_UNKNOWN_DEPENDENCY"
                ),

                description=(
                    "Load-bearing dependencies must resolve "
                    "to declared workflow steps."
                ),

                passed=True,

                evidence=[
                    "topology validation"
                ],
            ),

            WorkflowInvariant(
                invariant_id=(
                    "I_DURABLE_EFFECT_GATED"
                ),

                description=(
                    "Durable/external effects require "
                    "explicit fresh authority."
                ),

                passed=True,

                evidence=[
                    "commit-time authority rule"
                ],
            ),

            WorkflowInvariant(
                invariant_id=(
                    "I_RETRY_SAFETY"
                ),

                description=(
                    "Retryable effect-bearing steps require "
                    "idempotency or equivalent protection."
                ),

                passed=True,

                evidence=[
                    "retry contract validation"
                ],
            ),

            WorkflowInvariant(
                invariant_id=(
                    "I_RECOVERY_DEFINED"
                ),

                description=(
                    "Effect-bearing workflows require rollback "
                    "or compensation semantics."
                ),

                passed=True,

                evidence=[
                    "workflow recovery contract"
                ],
            ),
        ]

    def _evaluate_invariants(
        self,
        invariants: Iterable[
            WorkflowInvariant
        ],
    ) -> Dict[str, Any]:

        failures = []

        unknowns = []

        for invariant in invariants:

            if invariant.passed is False:

                failures.append(
                    invariant.reason
                    or invariant.description
                )

            elif invariant.passed is None:

                unknowns.append(
                    invariant.reason
                    or invariant.description
                )

        return {
            "hard_failures": failures,

            "unknowns": unknowns,

            "pass": (
                not failures
                and not unknowns
            ),
        }

    # ========================================================
    # CLAIM PARSING
    # ========================================================

    def _parse_claims(
        self,
        raw: Any,
    ) -> List[
        WorkflowClaim
    ]:

        if not isinstance(
            raw,
            list,
        ):

            raise ValidationError(
                "claims must be a list"
            )

        result = []

        for item in raw:

            if not isinstance(
                item,
                dict,
            ):
                continue

            premises = {
                str(key):
                    self._clamp01(
                        value
                    )
                for key, value
                in item.get(
                    "premises",
                    {},
                ).items()
            }

            result.append(
                WorkflowClaim(
                    claim_id=str(
                        item.get(
                            "claim_id",
                            self._new_id(
                                "claim"
                            ),
                        )
                    ),

                    claim=str(
                        item.get(
                            "claim",
                            "",
                        )
                    ),

                    epistemic_class=(
                        self._parse_epistemic(
                            item.get(
                                "epistemic_class",
                                "AMOS_MODEL",
                            )
                        )
                    ),

                    premises=(
                        premises
                    ),

                    dependencies=list(
                        item.get(
                            "dependencies",
                            [],
                        )
                    ),

                    scope=str(
                        item.get(
                            "scope",
                            "",
                        )
                    ),

                    regime=str(
                        item.get(
                            "regime",
                            "default",
                        )
                    ),

                    freshness=self._clamp01(
                        item.get(
                            "freshness",
                            0.5,
                        )
                    ),

                    falsifiers=list(
                        item.get(
                            "falsifiers",
                            [],
                        )
                    ),

                    provenance=(
                        self._parse_provenance(
                            item.get(
                                "provenance",
                                [],
                            )
                        )
                    ),

                    confidence_ceiling=(
                        self._confidence_ceiling(
                            premises
                        )
                    ),
                )
            )

        return result

    # ========================================================
    # VALIDATION
    # ========================================================

    def _validate_definition(
        self,
        workflow: WorkflowDefinition,
    ) -> List[str]:

        issues = []

        # ----------------------------------------------------
        # Unique nodes already enforced by dict construction.
        # ----------------------------------------------------

        if not workflow.steps:

            issues.append(
                "workflow_has_no_steps"
            )

        # ----------------------------------------------------
        # Dependency references
        # ----------------------------------------------------

        for dependency in workflow.dependencies:

            if (
                dependency.parent
                not in workflow.steps
            ):

                issues.append(
                    f"missing_parent_step:"
                    f"{dependency.parent}"
                )

            if (
                dependency.child
                not in workflow.steps
            ):

                issues.append(
                    f"missing_child_step:"
                    f"{dependency.child}"
                )

        # ----------------------------------------------------
        # Cycles
        # ----------------------------------------------------

        if self._has_cycle(
            workflow
        ):

            issues.append(
                "workflow_contains_cycle"
            )

        # ----------------------------------------------------
        # Retry safety
        # ----------------------------------------------------

        for step in workflow.steps.values():

            if (
                step.retry_policy.max_attempts
                > 1
                and step.effect_class
                in {
                    EffectClass.LOCAL_WRITE,
                    EffectClass.DURABLE_WRITE,
                    EffectClass.EXTERNAL_EFFECT,
                    EffectClass.IRREVERSIBLE,
                }
                and step.retry_policy.idempotent_required
                is False
            ):

                issues.append(
                    (
                        f"unsafe_retry:"
                        f"{step.step_id}"
                    )
                )

        # ----------------------------------------------------
        # Compensation / rollback
        # ----------------------------------------------------

        for step in workflow.steps.values():

            if (
                step.effect_class
                in {
                    EffectClass.DURABLE_WRITE,
                    EffectClass.EXTERNAL_EFFECT,
                }
                and not step.compensation.enabled
                and not workflow.rollback_policy
            ):

                issues.append(
                    (
                        f"missing_recovery_path:"
                        f"{step.step_id}"
                    )
                )

        # ----------------------------------------------------
        # Irreversible effects
        # ----------------------------------------------------

        for step in workflow.steps.values():

            if (
                step.effect_class
                == EffectClass.IRREVERSIBLE
            ):

                approval_gate = any(
                    gate.hard
                    and (
                        "approval"
                        in gate.description.lower()
                        or "authority"
                        in gate.description.lower()
                    )
                    for gate in step.gates
                )

                if not approval_gate:

                    issues.append(
                        (
                            "irreversible_step_missing_"
                            f"approval_gate:{step.step_id}"
                        )
                    )

        return list(
            dict.fromkeys(
                issues
            )
        )

    # ========================================================
    # GRAPH HELPERS
    # ========================================================

    def _adjacency(
        self,
        workflow: WorkflowDefinition,
    ) -> Dict[
        str,
        Set[str],
    ]:

        graph = {
            step_id: set()
            for step_id
            in workflow.steps
        }

        for edge in workflow.dependencies:

            if (
                edge.parent
                in graph
            ):

                graph[
                    edge.parent
                ].add(
                    edge.child
                )

        return graph

    def _reverse_adjacency(
        self,
        workflow: WorkflowDefinition,
    ) -> Dict[
        str,
        Set[str],
    ]:

        reverse = {
            step_id: set()
            for step_id
            in workflow.steps
        }

        for edge in workflow.dependencies:

            if (
                edge.child
                in reverse
            ):

                reverse[
                    edge.child
                ].add(
                    edge.parent
                )

        return reverse

    def _has_cycle(
        self,
        workflow: WorkflowDefinition,
    ) -> bool:

        graph = (
            self._adjacency(
                workflow
            )
        )

        indegree = {
            node: 0
            for node
            in graph
        }

        for children in graph.values():

            for child in children:

                if child in indegree:

                    indegree[
                        child
                    ] += 1

        queue = [
            node
            for node, degree
            in indegree.items()
            if degree == 0
        ]

        visited = 0

        while queue:

            node = queue.pop()

            visited += 1

            for child in graph.get(
                node,
                set(),
            ):

                indegree[
                    child
                ] -= 1

                if (
                    indegree[
                        child
                    ]
                    == 0
                ):

                    queue.append(
                        child
                    )

        return (
            visited
            != len(
                graph
            )
        )

    def _topological_order(
        self,
        workflow: WorkflowDefinition,
    ) -> List[str]:

        if self._has_cycle(
            workflow
        ):

            raise WorkflowCycleError(
                "Workflow contains a cycle."
            )

        graph = (
            self._adjacency(
                workflow
            )
        )

        reverse = (
            self._reverse_adjacency(
                workflow
            )
        )

        queue = [
            node
            for node in workflow.steps
            if not reverse.get(
                node
            )
        ]

        order = []

        while queue:

            node = queue.pop(
                0
            )

            order.append(
                node
            )

            for child in sorted(
                graph.get(
                    node,
                    set(),
                )
            ):

                reverse[
                    child
                ].discard(
                    node
                )

                if not reverse[
                    child
                ]:

                    queue.append(
                        child
                    )

        return order

    def _ready_frontier(
        self,
        workflow: WorkflowDefinition,
    ) -> List[str]:

        ready = []

        for step_id, step in workflow.steps.items():

            if step.state not in {
                StepState.PENDING,
                StepState.READY,
            }:
                continue

            dependencies_passed = all(
                (
                    parent
                    in workflow.steps
                    and workflow.steps[
                        parent
                    ].state
                    == StepState.PASS
                )
                for parent
                in step.depends_on
            )

            if dependencies_passed:

                gate_state = (
                    self._evaluate_step_gates(
                        step
                    )
                )

                if (
                    not gate_state[
                        "failed"
                    ]
                    and not gate_state[
                        "unknown"
                    ]
                ):

                    ready.append(
                        step_id
                    )

        return ready

    # ========================================================
    # STEP GATES
    # ========================================================

    def _evaluate_step_gates(
        self,
        step: WorkflowStep,
    ) -> Dict[str, Any]:

        failed = []

        unknown = []

        for gate in step.gates:

            if not gate.hard:
                continue

            if (
                gate.status
                == GateStatus.FAIL
            ):

                failed.append(
                    gate.reason
                    or gate.description
                )

            elif (
                gate.status
                == GateStatus.UNKNOWN
            ):

                unknown.append(
                    gate.reason
                    or gate.description
                )

        return {
            "failed": failed,

            "unknown": unknown,

            "pass": (
                not failed
                and not unknown
            ),
        }

    # ========================================================
    # COMPETING WORKFLOWS
    # ========================================================

    def _build_competing_workflows(
        self,
        raw: Any,
    ) -> List[
        CompetingWorkflow
    ]:

        if not isinstance(
            raw,
            list,
        ):

            return []

        result = []

        for index, item in enumerate(
            raw
        ):

            if not isinstance(
                item,
                dict,
            ):
                continue

            result.append(
                CompetingWorkflow(
                    hypothesis_id=str(
                        item.get(
                            "hypothesis_id",
                            f"H-WF-{index + 1}",
                        )
                    ),

                    description=str(
                        item.get(
                            "description",
                            "",
                        )
                    ),

                    workflow_variant=str(
                        item.get(
                            "workflow_variant",
                            "",
                        )
                    ),

                    confidence=self._clamp01(
                        item.get(
                            "confidence",
                            0.5,
                        )
                    ),

                    supporting_evidence=list(
                        item.get(
                            "supporting_evidence",
                            [],
                        )
                    ),

                    conflicting_evidence=list(
                        item.get(
                            "conflicting_evidence",
                            [],
                        )
                    ),

                    falsifiers=list(
                        item.get(
                            "falsifiers",
                            [],
                        )
                    ),
                )
            )

        return result

    # ========================================================
    # SERIALIZATION / RECONSTRUCTION
    # ========================================================

    def _serialize_workflow(
        self,
        workflow: WorkflowDefinition,
    ) -> Dict[str, Any]:

        return asdict(
            workflow
        )

    def _serialize_runtime(
        self,
        runtime: WorkflowRuntimeState,
    ) -> Dict[str, Any]:

        return asdict(
            runtime
        )

    def _workflow_from_dict(
        self,
        raw: Any,
    ) -> WorkflowDefinition:

        if not isinstance(
            raw,
            dict,
        ):

            raise GapError(
                "UNKNOWN/GAP: workflow dictionary required."
            )

        steps_raw = raw.get(
            "steps",
            {}
        )

        if isinstance(
            steps_raw,
            dict,
        ):

            step_list = list(
                steps_raw.values()
            )

        elif isinstance(
            steps_raw,
            list,
        ):

            step_list = steps_raw

        else:

            raise ValidationError(
                "workflow.steps must be dict or list"
            )

        steps = (
            self._parse_steps(
                step_list
            )
        )

        dependencies = (
            self._parse_dependencies(
                raw.get(
                    "dependencies",
                    [],
                )
            )
        )

        invariants = (
            self._parse_invariants(
                raw.get(
                    "invariants",
                    [],
                )
            )
        )

        claims = (
            self._parse_claims(
                raw.get(
                    "claims",
                    [],
                )
            )
        )

        return WorkflowDefinition(
            workflow_id=str(
                raw.get(
                    "workflow_id",
                    self._new_id(
                        "workflow"
                    ),
                )
            ),

            name=str(
                raw.get(
                    "name",
                    "workflow",
                )
            ),

            description=str(
                raw.get(
                    "description",
                    "",
                )
            ),

            version=str(
                raw.get(
                    "version",
                    "1.0.0",
                )
            ),

            scope=str(
                raw.get(
                    "scope",
                    "",
                )
            ),

            regime=str(
                raw.get(
                    "regime",
                    "default",
                )
            ),

            steps={
                step.step_id:
                    step
                for step in steps
            },

            dependencies=(
                dependencies
            ),

            invariants=(
                invariants
            ),

            claims=(
                claims
            ),

            authority_policy=dict(
                raw.get(
                    "authority_policy",
                    {},
                )
            ),

            resource_budget=dict(
                raw.get(
                    "resource_budget",
                    {},
                )
            ),

            rollback_policy=dict(
                raw.get(
                    "rollback_policy",
                    {},
                )
            ),

            lifecycle=(
                WorkflowLifecycle(
                    raw.get(
                        "lifecycle",
                        "DRAFT",
                    )
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

            created_at=float(
                raw.get(
                    "created_at",
                    time.time(),
                )
            ),

            updated_at=float(
                raw.get(
                    "updated_at",
                    time.time(),
                )
            ),
        )

    # ========================================================
    # WORKFLOW MARKDOWN
    # ========================================================

    def _render_workflow_markdown(
        self,
        workflow: WorkflowDefinition,
    ) -> str:

        lines = [
            f"# {workflow.name}",
            "",
            workflow.description,
            "",
            f"- Workflow ID: `{workflow.workflow_id}`",
            f"- Version: `{workflow.version}`",
            f"- Scope: `{workflow.scope}`",
            f"- Regime: `{workflow.regime}`",
            f"- Lifecycle: `{workflow.lifecycle.value}`",
            "",
            "## Steps",
            "",
        ]

        for step_id in (
            self._topological_order(
                workflow
            )
            if not self._has_cycle(
                workflow
            )
            else list(
                workflow.steps.keys()
            )
        ):

            step = workflow.steps[
                step_id
            ]

            lines.extend([
                f"### {step.step_id} — {step.name}",
                "",
                f"- Type: `{step.step_type.value}`",
                f"- Effect: `{step.effect_class.value}`",
                f"- State: `{step.state.value}`",
                (
                    "- Depends on: "
                    + (
                        ", ".join(
                            f"`{dep}`"
                            for dep in step.depends_on
                        )
                        if step.depends_on
                        else "none"
                    )
                ),
                "",
                step.description,
                "",
            ])

        lines.extend([
            "## Invariants",
            "",
        ])

        for invariant in workflow.invariants:

            status = (
                "PASS"
                if invariant.passed is True
                else (
                    "FAIL"
                    if invariant.passed is False
                    else "UNKNOWN"
                )
            )

            lines.append(
                (
                    f"- `{invariant.invariant_id}` "
                    f"[{status}] — "
                    f"{invariant.description}"
                )
            )

        return "\n".join(
            lines
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

        if not premises:

            return min(
                0.50,
                self.claim_ceiling,
            )

        return min(
            min(
                self._clamp01(
                    value
                )
                for value
                in premises.values()
            ),
            self.claim_ceiling,
        )

    # ========================================================
    # EPISTEMIC / PROVENANCE
    # ========================================================

    @staticmethod
    def _parse_epistemic(
        value: Any,
    ) -> EpistemicClass:

        try:

            return EpistemicClass(
                str(
                    value
                )
            )

        except ValueError:

            return EpistemicClass.UNKNOWN

    @staticmethod
    def _parse_provenance(
        raw: Any,
    ) -> List[
        ProvenanceRef
    ]:

        if not isinstance(
            raw,
            list,
        ):

            return []

        result = []

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

                    path=(
                        item.get(
                            "path"
                        )
                    ),

                    content_hash=(
                        item.get(
                            "content_hash"
                        )
                    ),

                    claim_id=(
                        item.get(
                            "claim_id"
                        )
                    ),

                    version=(
                        item.get(
                            "version"
                        )
                    ),

                    timestamp=(
                        item.get(
                            "timestamp"
                        )
                    ),
                )
            )

        return result

    def _default_provenance(
        self,
    ) -> List[
        ProvenanceRef
    ]:

        return [
            ProvenanceRef(
                source=(
                    "AMOS Skill Builder"
                ),

                path=(
                    PRIMARY_SKILL_PATH
                ),

                content_hash=(
                    "28e8fb0e13892eec"
                ),

                claim_id=(
                    "derived-workflow-builder"
                ),
            )
        ]

    # ========================================================
    # UTILITIES
    # ========================================================

    @staticmethod
    def _new_id(
        prefix: str,
    ) -> str:

        return (
            f"{prefix}-"
            f"{uuid.uuid4().hex[:12]}"
        )

    @staticmethod
    def _hash_object(
        value: Any,
    ) -> str:

        raw = json.dumps(
            value,
            sort_keys=True,
            default=str,
        ).encode(
            "utf-8"
        )

        return hashlib.sha256(
            raw
        ).hexdigest()

    def _clamp01(
        self,
        value: Any,
    ) -> float:

        return min(
            max(
                float(
                    value
                ),
                0.0,
            ),
            self.claim_ceiling,
        )


# ============================================================
# EXAMPLE
# ============================================================

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO
    )

    agent = (
        AmosWorkflowBuilderAgent(
            repo_root="."
        )
    )

    witness = AuthorityWitness(
        principal=(
            "principal:trang"
        ),

        task=(
            "design-workflow"
        ),

        resource=(
            "workflow:skill-build"
        ),

        allowed_effects=[
            EffectClass.LOCAL_WRITE,
        ],

        issued_at=(
            time.time()
        ),

        expires_at=(
            time.time()
            + 3600
        ),

        provenance=[
            ProvenanceRef(
                source=(
                    "steward_review"
                )
            )
        ],
    )

    ctx = ExecutionContext(
        query=(
            "Create a workflow for building "
            "and validating an AMOS Skill."
        ),

        capability=(
            "workflow.design"
        ),

        authorized_write=True,

        authority_witness=(
            witness
        ),

        inputs={

            "name": (
                "AMOS Skill Build Workflow"
            ),

            "description": (
                "Build, validate, challenge, repair, "
                "and package an AMOS Skill."
            ),

            "version": "1.0.0",

            "scope": (
                "single-skill-build"
            ),

            "regime": (
                "repository"
            ),

            "steps": [

                {
                    "step_id": "orient",

                    "name": (
                        "Orient"
                    ),

                    "step_type": "ANALYZE",

                    "description": (
                        "Lock objective, scope, dependencies, "
                        "gaps, provenance, and recovery state."
                    ),

                    "depends_on": [],

                    "effect_class": (
                        "NONE"
                    ),

                    "input_contract": {
                        "objective": "string",
                    },

                    "output_contract": {
                        "context_map": "object",
                    },

                    "required_capabilities": [],

                    "gates": [
                        {
                            "gate_id": (
                                "objective-present"
                            ),

                            "description": (
                                "Objective must be explicit."
                            ),

                            "status": "PASS",

                            "hard": True,
                        }
                    ],

                    "retry_policy": {
                        "max_attempts": 1,
                    },
                },

                {
                    "step_id": (
                        "read_sources"
                    ),

                    "name": (
                        "Read Sources"
                    ),

                    "step_type": "READ",

                    "description": (
                        "Read source material before modeling."
                    ),

                    "depends_on": [
                        "orient"
                    ],

                    "effect_class": (
                        "READ_ONLY"
                    ),

                    "input_contract": {
                        "sources": "list",
                    },

                    "output_contract": {
                        "source_map": "object",
                    },

                    "required_capabilities": [
                        "source.read"
                    ],

                    "gates": [],

                    "retry_policy": {
                        "max_attempts": 2,
                        "idempotent_required": True,
                    },
                },

                {
                    "step_id": (
                        "create_skill"
                    ),

                    "name": (
                        "Create Skill"
                    ),

                    "step_type": (
                        "TRANSFORM"
                    ),

                    "description": (
                        "Generate the smallest viable Skill "
                        "implementation."
                    ),

                    "depends_on": [
                        "read_sources"
                    ],

                    "effect_class": (
                        "LOCAL_WRITE"
                    ),

                    "input_contract": {
                        "source_map": "object",
                    },

                    "output_contract": {
                        "skill_bundle": "directory",
                    },

                    "required_capabilities": [
                        "skill.create"
                    ],

                    "gates": [
                        {
                            "gate_id": (
                                "contracts-recovered"
                            ),

                            "description": (
                                "Load-bearing contracts recovered."
                            ),

                            "status": "PASS",

                            "hard": True,
                        }
                    ],

                    "retry_policy": {
                        "max_attempts": 2,
                        "idempotent_required": True,
                    },

                    "compensation": {
                        "enabled": True,
                        "action": (
                            "restore prior working tree state"
                        ),
                        "verified": True,
                    },
                },

                {
                    "step_id": (
                        "validate_skill"
                    ),

                    "name": (
                        "Validate Skill"
                    ),

                    "step_type": (
                        "VALIDATE"
                    ),

                    "description": (
                        "Run structural, execution, specification, "
                        "and regression checks."
                    ),

                    "depends_on": [
                        "create_skill"
                    ],

                    "effect_class": (
                        "READ_ONLY"
                    ),

                    "input_contract": {
                        "skill_bundle": "directory",
                    },

                    "output_contract": {
                        "validation": "object",
                    },

                    "required_capabilities": [
                        "skill.validate"
                    ],

                    "gates": [],
                },

                {
                    "step_id": (
                        "package_skill"
                    ),

                    "name": (
                        "Package Skill"
                    ),

                    "step_type": (
                        "PACKAGE"
                    ),

                    "description": (
                        "Package the complete validated Skill."
                    ),

                    "depends_on": [
                        "validate_skill"
                    ],

                    "effect_class": (
                        "LOCAL_WRITE"
                    ),

                    "input_contract": {
                        "validation": "object",
                    },

                    "output_contract": {
                        "skill_zip": "file",
                    },

                    "required_capabilities": [
                        "skill.package"
                    ],

                    "gates": [
                        {
                            "gate_id": (
                                "spec-pass"
                            ),

                            "description": (
                                "Specification validation passed."
                            ),

                            "status": "PASS",

                            "hard": True,
                        },

                        {
                            "gate_id": (
                                "regression-pass"
                            ),

                            "description": (
                                "Regression validation passed."
                            ),

                            "status": "PASS",

                            "hard": True,
                        },
                    ],

                    "retry_policy": {
                        "max_attempts": 1,
                    },

                    "compensation": {
                        "enabled": True,
                        "action": (
                            "delete staged package"
                        ),
                        "verified": True,
                    },
                },
            ],

            "dependencies": [],

            "authority_policy": {
                "durable_effect_requires_fresh_witness":
                    True,

                "delegation_may_only_attenuate":
                    True,
            },

            "resource_budget": {
                "max_steps": 10,
                "max_retries": 5,
            },

            "rollback_policy": {
                "mode": (
                    "nearest-valid-checkpoint"
                ),

                "preserve_unaffected_steps":
                    True,
            },

            "premise_confidences": {
                "workflow-contract": 0.95,
                "step-contracts": 0.92,
                "authority-policy": 0.94,
            },

            "evidence": [
                (
                    "AMOS Skill Builder runtime"
                )
            ],

            "falsifiers": [
                (
                    "workflow admits a durable effect "
                    "without fresh authority"
                ),

                (
                    "workflow retries a non-idempotent "
                    "effect without a guard"
                ),

                (
                    "workflow package proceeds despite "
                    "failed specification or regression gate"
                ),
            ],

            "rollback_path": (
                "restore nearest valid checkpoint"
            ),

            "repair_path": (
                "repair smallest causal workflow edge "
                "and revalidate descendants"
            ),
        },
    )

    try:

        result = agent.run(
            ctx
        )

        print(
            json.dumps(
                asdict(
                    result
                ),
                indent=2,
                ensure_ascii=False,
                default=str,
            )
        )

    except WorkflowBuilderError as exc:

        print(
            json.dumps(
                {
                    "status": (
                        "FAILED_CLOSED"
                    ),

                    "agent": (
                        AGENT_ID
                    ),

                    "error": str(
                        exc
                    ),
                },
                indent=2,
                ensure_ascii=False,
            )
        )
