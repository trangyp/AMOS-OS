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
# AMOS SKILL BUILDER AGENT
# ============================================================

AGENT_ID = "amos-skill-builder-agent"
AGENT_VERSION = "1.0.0"

PRIMARY_SKILL = "amos-skill-builder"
PRIMARY_SKILL_PATH = ".devin/skills/amos-skill-builder/SKILL.md"

CLAIM_CEILING = 0.95


# ============================================================
# ENUMS
# ============================================================

class EpistemicClass(str, Enum):
    SOURCE_CANON = "SOURCE_CANON"
    SOURCE_CLAIM = "SOURCE_CLAIM"
    SOURCE_THEOREM = "SOURCE_THEOREM"
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


class BuilderStage(str, Enum):
    ORIENT = "ORIENT"
    READ = "READ"
    PARSE = "PARSE"
    TYPE = "TYPE"
    UNDERSTAND = "UNDERSTAND"
    MODEL = "MODEL"
    PLAN = "PLAN"
    CREATE = "CREATE"
    EXECUTE = "EXECUTE"
    OBSERVE = "OBSERVE"
    VERIFY = "VERIFY"
    CHALLENGE = "CHALLENGE"
    REPAIR = "REPAIR"
    COMPRESS = "COMPRESS"
    PACKAGE = "PACKAGE"


class StageStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    ACTIVE = "ACTIVE"
    PASS = "PASS"
    FAIL = "FAIL"
    GAP = "GAP"
    SKIPPED = "SKIPPED"


class TestState(str, Enum):
    NOT_RUN = "NOT_RUN"
    SYNTAX_PASS = "SYNTAX_PASS"
    STATIC_PASS = "STATIC_PASS"
    EXECUTION_PASS = "EXECUTION_PASS"
    TEST_PASS = "TEST_PASS"
    SPEC_PASS = "SPEC_PASS"
    SYSTEM_PASS = "SYSTEM_PASS"
    REGRESSION_PASS = "REGRESSION_PASS"

    SYNTAX_FAIL = "SYNTAX_FAIL"
    STATIC_FAIL = "STATIC_FAIL"
    EXECUTION_FAIL = "EXECUTION_FAIL"
    TEST_FAIL = "TEST_FAIL"
    SPEC_FAIL = "SPEC_FAIL"
    SYSTEM_FAIL = "SYSTEM_FAIL"
    REGRESSION_FAIL = "REGRESSION_FAIL"

    EXECUTION_GAP = "EXECUTION_GAP"


class GapClass(str, Enum):
    CRITICAL = "CRITICAL"
    DECISION_RELEVANT = "DECISION_RELEVANT"
    EXPLANATORY = "EXPLANATORY"
    COSMETIC = "COSMETIC"


class DriftType(str, Enum):
    MODEL = "MODEL_DRIFT"
    DATA = "DATA_DRIFT"
    SCOPE = "SCOPE_DRIFT"
    ARCHITECTURE = "ARCHITECTURE_DRIFT"
    CONTRACT = "CONTRACT_DRIFT"
    PROVENANCE = "PROVENANCE_DRIFT"
    CONFIDENCE = "CONFIDENCE_DECAY"
    CONTEXT = "CONTEXT_DRIFT"
    NONE = "NONE"


class LifecycleState(str, Enum):
    INIT = "INIT"
    RUNNING = "RUNNING"
    CHECKPOINTED = "CHECKPOINTED"
    RECOVERING = "RECOVERING"
    FINALIZING = "FINALIZING"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    QUARANTINED = "QUARANTINED"


class ValidationGate(str, Enum):
    ARCHITECTURE_COMPATIBLE = "ARCHITECTURE_COMPATIBLE"
    CONTRACT_COMPATIBLE = "CONTRACT_COMPATIBLE"
    HARD_INVARIANTS_PASS = "HARD_INVARIANTS_PASS"
    SPEC_PASS = "SPEC_PASS"
    REGRESSION_PASS = "REGRESSION_PASS"


# ============================================================
# ERRORS
# ============================================================

class SkillBuilderError(RuntimeError):
    pass


class ValidationError(SkillBuilderError):
    pass


class AuthorizationError(SkillBuilderError):
    pass


class GapError(SkillBuilderError):
    pass


class ParseGapError(SkillBuilderError):
    pass


class ExecutionGapError(SkillBuilderError):
    pass


# ============================================================
# CORE DATACLASSES
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
class ContextMapItem:
    objective: str
    artifact: Optional[str] = None
    dependency: Optional[str] = None
    open_question: Optional[str] = None
    assumption: Optional[str] = None
    source_location: Optional[str] = None
    execution_state: Optional[str] = None
    conflict: Optional[str] = None
    freshness: Optional[float] = None
    recovery_cost: float = 0.0
    replay_need: bool = False
    drop_priority: float = 0.0
    load_bearing: bool = False
    active_falsifier: bool = False
    failure_trace_required: bool = False

    def compressible(self) -> bool:
        """
        Compressible(x) =
            Redundant(x)
            AND NonLoadBearing(x)
            AND Recoverable(x)

        This object uses caller-provided state for the three terms.
        """
        redundant = self.drop_priority >= 0.70
        non_load_bearing = not self.load_bearing
        recoverable = self.recovery_cost <= 0.30 and not self.replay_need

        if self.active_falsifier:
            return False

        if self.conflict:
            return False

        if self.failure_trace_required:
            return False

        return redundant and non_load_bearing and recoverable


@dataclass
class SourceRecord:
    source_id: str
    section: Optional[str]
    claim: Optional[str]
    equation: Optional[str]
    assumption: Optional[str]
    method: Optional[str]
    result: Optional[str]
    limitation: Optional[str]
    contradiction: Optional[str]
    provenance_anchor: Optional[str]


@dataclass
class CodeState:
    file: str
    language: Optional[str] = None
    ast_node: Optional[str] = None
    symbol: Optional[str] = None
    imports: List[str] = field(default_factory=list)
    call_edges: List[str] = field(default_factory=list)
    cfg_edges: List[str] = field(default_factory=list)
    data_edges: List[str] = field(default_factory=list)
    schema: Optional[str] = None
    config: Optional[str] = None
    tests: List[str] = field(default_factory=list)
    runtime_trace: Optional[str] = None
    provenance: List[ProvenanceRef] = field(default_factory=list)


@dataclass
class SystemState:
    component: str
    interface: Optional[str] = None
    dependency: Optional[str] = None
    data_contract: Optional[str] = None
    config: Optional[str] = None
    resource: Optional[str] = None
    runtime: Optional[str] = None
    policy: Optional[str] = None
    owner: Optional[str] = None
    risk: Optional[str] = None
    provenance: List[ProvenanceRef] = field(default_factory=list)


@dataclass
class ClaimState:
    claim_id: str
    epistemic_class: EpistemicClass
    premises: List[str]
    dependencies: List[str]
    scope: str
    regime: str
    falsifiers: List[str]
    status: str
    confidence: float
    provenance: List[ProvenanceRef] = field(default_factory=list)


@dataclass
class CanonicalTensor:
    """
    X = T[
        object,
        primitive,
        scale,
        time,
        regime,
        observer,
        provenance,
        epistemic_class,
        confidence,
        consequence
    ]
    """
    object: str
    primitive: str
    scale: str
    time: str
    regime: str
    observer: str
    provenance: List[ProvenanceRef]
    epistemic_class: EpistemicClass
    confidence: float
    consequence: Dict[str, Any]


@dataclass
class HarnessTensor:
    """
    H = T[
        artifact,
        representation,
        parser_state,
        context_state,
        execution_state,
        test_state,
        invariant_state,
        evidence_state,
        repair_state,
        version,
        provenance
    ]
    """
    artifact: str
    representation: str
    parser_state: str
    context_state: str
    execution_state: str
    test_state: str
    invariant_state: str
    evidence_state: str
    repair_state: str
    version: str
    provenance: List[ProvenanceRef]


@dataclass
class HardInvariant:
    invariant_id: str
    description: str
    passed: Optional[bool]
    evidence: List[str] = field(default_factory=list)
    reason: Optional[str] = None


@dataclass
class PlanAction:
    action_id: str
    description: str

    impact: float
    uncertainty_reduction: float
    dependency_fanout: float
    cost: float

    required: bool = False
    executed: bool = False

    def priority(self) -> float:
        """
        AMOS MODEL:
        Priority(i) =
            Impact
            * UncertaintyReduction
            * DependencyFanout
            / Cost
        """
        denominator = max(self.cost, 0.000001)

        return (
            self.impact
            * self.uncertainty_reduction
            * self.dependency_fanout
            / denominator
        )


@dataclass
class CreateCandidate:
    intent: str
    architecture: Dict[str, Any]
    interfaces: List[Dict[str, Any]]
    constraints: List[str]
    evidence: List[str]
    tests: List[str]
    change_boundary: List[str]


@dataclass
class ExecutionRecord:
    """
    E = T[
        command,
        cwd,
        environment,
        input_hash,
        exit_code,
        stdout_hash,
        stderr_hash,
        duration,
        timeout,
        artifact_hash,
        parent_run,
        state_hash,
        test_state
    ]
    """
    command: str
    cwd: str
    environment: Dict[str, Any]
    input_hash: str
    exit_code: Optional[int]
    stdout_hash: Optional[str]
    stderr_hash: Optional[str]
    duration: Optional[float]
    timeout: Optional[float]
    artifact_hash: Optional[str]
    parent_run: Optional[str]
    state_hash: str
    test_state: TestState
    executed: bool
    observation: Optional[str] = None


@dataclass
class ObservationState:
    syntax: TestState = TestState.NOT_RUN
    static: TestState = TestState.NOT_RUN
    execution: TestState = TestState.NOT_RUN
    tests: TestState = TestState.NOT_RUN
    spec: TestState = TestState.NOT_RUN
    system: TestState = TestState.NOT_RUN
    regression: TestState = TestState.NOT_RUN

    def failures(self) -> List[TestState]:
        return [
            state
            for state in (
                self.syntax,
                self.static,
                self.execution,
                self.tests,
                self.spec,
                self.system,
                self.regression,
            )
            if state.value.endswith("_FAIL")
            or state == TestState.EXECUTION_GAP
        ]


@dataclass
class CompetingHypothesis:
    hypothesis_id: str
    statement: str
    confidence: float
    evidence: List[str] = field(default_factory=list)
    counterevidence: List[str] = field(default_factory=list)
    falsifiers: List[str] = field(default_factory=list)


@dataclass
class RSCFCapsule:
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
    competing_hypotheses: List[CompetingHypothesis]

    confidence_ceiling: float
    consequence: Dict[str, Any]

    repair_path: Optional[str] = None


@dataclass
class ChallengeResult:
    parser_information_loss: bool
    stale_context: bool
    correlated_provenance: bool
    hidden_dependency: bool
    tensor_axis_mismatch: bool
    undefined_equation_variables: bool
    architecture_drift: bool
    local_pass_global_fail: bool
    benchmark_mismatch: bool
    causal_overreach: bool
    authority_mismatch: bool
    storage_context_blowup: bool
    repair_regression: bool

    issues: List[str] = field(default_factory=list)

    def succeeded(self) -> bool:
        return any(
            (
                self.parser_information_loss,
                self.stale_context,
                self.correlated_provenance,
                self.hidden_dependency,
                self.tensor_axis_mismatch,
                self.undefined_equation_variables,
                self.architecture_drift,
                self.local_pass_global_fail,
                self.benchmark_mismatch,
                self.causal_overreach,
                self.authority_mismatch,
                self.storage_context_blowup,
                self.repair_regression,
            )
        )


@dataclass
class GapRecord:
    gap_id: str
    gap_class: GapClass
    description: str
    blocking: bool
    repair_action: Optional[str] = None
    confidence_impact: float = 0.0


@dataclass
class DriftRecord:
    drift_type: DriftType
    description: str
    severity: float
    evidence: List[str]
    invalidates: List[str]
    repair_required: bool


@dataclass
class StageRecord:
    stage: BuilderStage
    status: StageStatus
    started_at: Optional[float] = None
    finished_at: Optional[float] = None
    output: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)


@dataclass
class BuilderCheckpoint:
    checkpoint_id: str
    lifecycle_state: LifecycleState
    current_stage: Optional[BuilderStage]

    objective: str
    target_skill: Optional[str]

    stages: Dict[str, StageRecord]

    context_map: List[ContextMapItem]
    claims: List[ClaimState]
    gaps: List[GapRecord]
    drifts: List[DriftRecord]

    artifacts: Dict[str, Any]
    provenance: List[ProvenanceRef]

    created_at: float
    state_hash: str


@dataclass
class BuilderState:
    run_id: str
    lifecycle_state: LifecycleState

    objective: str
    target_skill: Optional[str]

    current_stage: Optional[BuilderStage]

    stages: Dict[str, StageRecord]

    context_map: List[ContextMapItem]
    sources: List[SourceRecord]

    code_state: List[CodeState]
    system_state: List[SystemState]
    claims: List[ClaimState]

    tensors_x: List[CanonicalTensor]
    tensors_h: List[HarnessTensor]

    invariants: List[HardInvariant]

    plan: List[PlanAction]

    create_candidate: Optional[CreateCandidate]

    executions: List[ExecutionRecord]
    observations: ObservationState

    rscf: Optional[RSCFCapsule]

    challenge: Optional[ChallengeResult]

    gaps: List[GapRecord]
    drifts: List[DriftRecord]

    checkpoints: List[BuilderCheckpoint]

    artifacts: Dict[str, Any]

    provenance: List[ProvenanceRef]

    created_at: float
    updated_at: float


@dataclass
class ExecutionContext:
    query: str
    capability: str
    inputs: Dict[str, Any] = field(default_factory=dict)

    authorized_write: bool = False
    authority_witness: Optional[str] = None

    correlation_id: Optional[str] = None


@dataclass
class AgentResult:
    status: ExecutionStatus
    capability: str
    summary: str

    data: Dict[str, Any] = field(default_factory=dict)

    gaps: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    confidence_ceiling: float = CLAIM_CEILING
    provenance: List[ProvenanceRef] = field(default_factory=list)


# ============================================================
# CONFIG
# ============================================================

AGENT_CONFIG = {
    "name": AGENT_ID,
    "display_name": "Skill Builder",
    "description": (
        "AMOS Skill Builder — builds Skills as governed executable "
        "reasoning systems rather than instruction dumps."
    ),
    "version": AGENT_VERSION,
    "author": "Trang Phan",
    "steward": "Trang Phan",
    "system": "AMOS_OS",
    "role": (
        "System-aware Skill construction, validation, repair, lifecycle, "
        "provenance, packaging, and system-completion specialist."
    ),
    "skill_binding": {
        "primary_skill": PRIMARY_SKILL,
        "skill_path": PRIMARY_SKILL_PATH,
    },
    "epistemic_class": "AMOS_MODEL",
    "claim_ceiling": CLAIM_CEILING,
    "content_hash": "28e8fb0e13892eec",
    "governance": {
        "owner_team": "AMOS_CORE",
        "business_domain": "runtime",
        "risk_tier": "medium",
        "observability": "structured_logs+content_hash",
        "approval_mode": "steward_review",
        "promotion_state": "production",
    },
}


CAPABILITIES: Dict[str, CapabilityContract] = {
    "runtime.design_builder": CapabilityContract(
        name="runtime.design_builder",
        description=(
            "Design and run the full AMOS Skill Builder lifecycle."
        ),
        side_effect=SideEffect.WRITE,
    ),
    "runtime.validate_builder": CapabilityContract(
        name="runtime.validate_builder",
        description=(
            "Validate Skill Builder artifacts, state, promotion gates, "
            "RSCF, tests, architecture, and regression safety."
        ),
        side_effect=SideEffect.READ,
    ),
    "runtime.analyze_builder": CapabilityContract(
        name="runtime.analyze_builder",
        description=(
            "Analyze builder structure, dependencies, architecture, "
            "state, claims, gaps, and system-completion sufficiency."
        ),
        side_effect=SideEffect.READ,
    ),
    "runtime.trace_builder_provenance": CapabilityContract(
        name="runtime.trace_builder_provenance",
        description=(
            "Trace Skill Builder outputs to source, execution, dependency, "
            "and RSCF provenance."
        ),
        side_effect=SideEffect.READ,
    ),
    "runtime.assess_builder_claim": CapabilityContract(
        name="runtime.assess_builder_claim",
        description=(
            "Assess Skill Builder claims for class, evidence, scope, "
            "regime, freshness, dependencies, falsifiers, and confidence."
        ),
        side_effect=SideEffect.READ,
    ),
    "runtime.manage_builder_lifecycle": CapabilityContract(
        name="runtime.manage_builder_lifecycle",
        description=(
            "Manage Skill Builder lifecycle: init, run, checkpoint, "
            "recover, finalize."
        ),
        side_effect=SideEffect.WRITE,
    ),
    "runtime.detect_builder_drift": CapabilityContract(
        name="runtime.detect_builder_drift",
        description=(
            "Detect model, data, scope, architecture, provenance, "
            "context, and confidence drift."
        ),
        side_effect=SideEffect.READ,
    ),
    "runtime.escalate_builder_gaps": CapabilityContract(
        name="runtime.escalate_builder_gaps",
        description=(
            "Escalate Skill Builder UNKNOWN/GAP states, downgrade "
            "confidence, classify gaps, and trigger bounded repair."
        ),
        side_effect=SideEffect.WRITE,
    ),
}


# ============================================================
# AGENT
# ============================================================

class AmosSkillBuilderAgent:
    """
    Full runtime implementation of the AMOS Skill Builder.

    Runtime:
        ORIENT
        -> READ
        -> PARSE
        -> TYPE
        -> UNDERSTAND
        -> MODEL
        -> PLAN
        -> CREATE
        -> EXECUTE
        -> OBSERVE
        -> VERIFY
        -> CHALLENGE
        -> REPAIR
        -> COMPRESS
        -> PACKAGE
    """

    def __init__(
        self,
        repo_root: str | Path = ".",
        claim_ceiling: float = CLAIM_CEILING,
    ) -> None:
        self.repo_root = Path(repo_root).resolve()

        self.skill_path = (
            self.repo_root
            / ".devin"
            / "skills"
            / "amos-skill-builder"
            / "SKILL.md"
        )

        self.claim_ceiling = min(
            max(float(claim_ceiling), 0.0),
            CLAIM_CEILING,
        )

        self.logger = logging.getLogger(
            AGENT_ID
        )

        self.handlers: Dict[
            str,
            Callable[[ExecutionContext], AgentResult],
        ] = {
            "runtime.design_builder":
                self._design_builder,

            "runtime.validate_builder":
                self._validate_builder,

            "runtime.analyze_builder":
                self._analyze_builder,

            "runtime.trace_builder_provenance":
                self._trace_builder_provenance,

            "runtime.assess_builder_claim":
                self._assess_builder_claim,

            "runtime.manage_builder_lifecycle":
                self._manage_builder_lifecycle,

            "runtime.detect_builder_drift":
                self._detect_builder_drift,

            "runtime.escalate_builder_gaps":
                self._escalate_builder_gaps,
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
            or self._new_id("corr")
        )

        self._load_skill()
        self._validate_context(ctx)

        capability = CAPABILITIES.get(
            ctx.capability
        )

        if capability is None:
            raise ValidationError(
                f"Unsupported capability: {ctx.capability}"
            )

        self._check_authority(
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
    # SKILL / AUTHORITY
    # ========================================================

    def _load_skill(self) -> str:

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

        if capability.side_effect != SideEffect.WRITE:
            return

        if not ctx.authorized_write:
            raise AuthorizationError(
                f"{capability.name} is write-classified. "
                "Capability does not confer authority."
            )

        if not ctx.authority_witness:
            raise AuthorizationError(
                "Write-classified builder capability requires "
                "authority_witness."
            )

    # ========================================================
    # STATE CREATION
    # ========================================================

    def _new_builder_state(
        self,
        objective: str,
        target_skill: Optional[str],
        provenance: Optional[List[ProvenanceRef]] = None,
    ) -> BuilderState:

        now = time.time()

        stages = {
            stage.value: StageRecord(
                stage=stage,
                status=StageStatus.NOT_STARTED,
            )
            for stage in BuilderStage
        }

        return BuilderState(
            run_id=self._new_id("run"),
            lifecycle_state=LifecycleState.INIT,
            objective=objective,
            target_skill=target_skill,
            current_stage=None,
            stages=stages,
            context_map=[],
            sources=[],
            code_state=[],
            system_state=[],
            claims=[],
            tensors_x=[],
            tensors_h=[],
            invariants=[],
            plan=[],
            create_candidate=None,
            executions=[],
            observations=ObservationState(),
            rscf=None,
            challenge=None,
            gaps=[],
            drifts=[],
            checkpoints=[],
            artifacts={},
            provenance=provenance or self._default_provenance(),
            created_at=now,
            updated_at=now,
        )

    # ========================================================
    # DESIGN BUILDER
    # ========================================================

    def _design_builder(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        objective = str(
            ctx.inputs.get(
                "objective",
                ctx.query,
            )
        )

        target_skill = ctx.inputs.get(
            "target_skill"
        )

        state = self._new_builder_state(
            objective=objective,
            target_skill=target_skill,
            provenance=self._parse_provenance(
                ctx.inputs.get(
                    "provenance",
                    [],
                )
            ) or self._default_provenance(),
        )

        state.lifecycle_state = (
            LifecycleState.RUNNING
        )

        pipeline = [
            self._stage_orient,
            self._stage_read,
            self._stage_parse,
            self._stage_type,
            self._stage_understand,
            self._stage_model,
            self._stage_plan,
            self._stage_create,
            self._stage_execute,
            self._stage_observe,
            self._stage_verify,
            self._stage_challenge,
            self._stage_repair,
            self._stage_compress,
            self._stage_package,
        ]

        for stage_fn in pipeline:

            stage = self._stage_for_fn(
                stage_fn
            )

            state.current_stage = stage

            record = state.stages[
                stage.value
            ]

            record.status = (
                StageStatus.ACTIVE
            )

            record.started_at = (
                time.time()
            )

            try:

                stage_output = stage_fn(
                    state,
                    ctx.inputs,
                )

                record.output = (
                    stage_output
                    if isinstance(
                        stage_output,
                        dict,
                    )
                    else {}
                )

                if record.status == StageStatus.ACTIVE:
                    record.status = (
                        StageStatus.PASS
                    )

            except (
                GapError,
                ParseGapError,
                ExecutionGapError,
            ) as exc:

                record.status = (
                    StageStatus.GAP
                )

                record.errors.append(
                    str(exc)
                )

                state.gaps.append(
                    GapRecord(
                        gap_id=self._new_id(
                            "gap"
                        ),
                        gap_class=(
                            GapClass.CRITICAL
                            if stage in {
                                BuilderStage.PARSE,
                                BuilderStage.EXECUTE,
                                BuilderStage.VERIFY,
                                BuilderStage.PACKAGE,
                            }
                            else GapClass.DECISION_RELEVANT
                        ),
                        description=str(
                            exc
                        ),
                        blocking=True,
                        repair_action=(
                            "supply missing evidence/runtime "
                            "or repair stage"
                        ),
                        confidence_impact=0.30,
                    )
                )

                break

            except Exception as exc:

                record.status = (
                    StageStatus.FAIL
                )

                record.errors.append(
                    str(exc)
                )

                state.gaps.append(
                    GapRecord(
                        gap_id=self._new_id(
                            "gap"
                        ),
                        gap_class=(
                            GapClass.CRITICAL
                        ),
                        description=(
                            f"{stage.value} failed: {exc}"
                        ),
                        blocking=True,
                        repair_action=(
                            "locate causal target and "
                            "rerun changed path"
                        ),
                        confidence_impact=0.40,
                    )
                )

                break

            finally:

                record.finished_at = (
                    time.time()
                )

                state.updated_at = (
                    time.time()
                )

        blocking = [
            gap
            for gap in state.gaps
            if gap.blocking
        ]

        if blocking:
            state.lifecycle_state = (
                LifecycleState.FAILED
            )

            status = (
                ExecutionStatus.UNKNOWN
            )

        elif state.stages[
            BuilderStage.PACKAGE.value
        ].status == StageStatus.PASS:

            state.lifecycle_state = (
                LifecycleState.COMPLETE
            )

            status = (
                ExecutionStatus.VERIFIED
                if self._promotion_passes(
                    state
                )
                else ExecutionStatus.CONDITIONAL
            )

        else:
            state.lifecycle_state = (
                LifecycleState.FAILED
            )

            status = (
                ExecutionStatus.CONDITIONAL
            )

        state.current_stage = None

        confidence = (
            self._state_confidence(
                state
            )
        )

        return AgentResult(
            status=status,
            capability=ctx.capability,
            summary=(
                "Skill Builder lifecycle "
                f"{state.lifecycle_state.value}."
            ),
            data={
                "builder_state": self._serialize_state(
                    state
                ),
                "promotion_pass": (
                    self._promotion_passes(
                        state
                    )
                ),
                "stop_rule": (
                    self._stop_rule(
                        state
                    )
                ),
                "installation_claimed": False,
            },
            gaps=[
                gap.description
                for gap in state.gaps
            ],
            warnings=[
                (
                    "A generated Skill is not complete merely "
                    "because SKILL.md exists."
                ),
                (
                    "Failed execution remains a failed execution "
                    "until the runtime evidence changes."
                ),
                (
                    "Packaging must return the complete Skill artifact, "
                    "not only a patch."
                ),
            ],
            confidence_ceiling=confidence,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # ORIENT
    # ========================================================

    def _stage_orient(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        items_raw = inputs.get(
            "context_map",
            [],
        )

        if not isinstance(
            items_raw,
            list,
        ):
            raise ValidationError(
                "context_map must be a list"
            )

        if not items_raw:
            items_raw = [
                {
                    "objective": state.objective,
                    "artifact": state.target_skill,
                    "load_bearing": True,
                    "recovery_cost": 0.8,
                    "replay_need": True,
                }
            ]

        state.context_map = [
            ContextMapItem(
                objective=str(
                    item.get(
                        "objective",
                        state.objective,
                    )
                ),
                artifact=item.get(
                    "artifact"
                ),
                dependency=item.get(
                    "dependency"
                ),
                open_question=item.get(
                    "open_question"
                ),
                assumption=item.get(
                    "assumption"
                ),
                source_location=item.get(
                    "source_location"
                ),
                execution_state=item.get(
                    "execution_state"
                ),
                conflict=item.get(
                    "conflict"
                ),
                freshness=item.get(
                    "freshness"
                ),
                recovery_cost=float(
                    item.get(
                        "recovery_cost",
                        0.0,
                    )
                ),
                replay_need=bool(
                    item.get(
                        "replay_need",
                        False,
                    )
                ),
                drop_priority=float(
                    item.get(
                        "drop_priority",
                        0.0,
                    )
                ),
                load_bearing=bool(
                    item.get(
                        "load_bearing",
                        False,
                    )
                ),
                active_falsifier=bool(
                    item.get(
                        "active_falsifier",
                        False,
                    )
                ),
                failure_trace_required=bool(
                    item.get(
                        "failure_trace_required",
                        False,
                    )
                ),
            )
            for item in items_raw
            if isinstance(
                item,
                dict,
            )
        ]

        return {
            "retained_items": len(
                state.context_map
            ),
            "compressible_items": sum(
                1
                for item in state.context_map
                if item.compressible()
            ),
        }

    # ========================================================
    # READ
    # ========================================================

    def _stage_read(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        raw_sources = inputs.get(
            "sources",
            [],
        )

        if not isinstance(
            raw_sources,
            list,
        ):
            raise ValidationError(
                "sources must be a list"
            )

        for index, raw in enumerate(
            raw_sources
        ):

            if not isinstance(
                raw,
                dict,
            ):
                continue

            state.sources.append(
                SourceRecord(
                    source_id=str(
                        raw.get(
                            "source_id",
                            f"SRC-{index + 1}",
                        )
                    ),
                    section=raw.get(
                        "section"
                    ),
                    claim=raw.get(
                        "claim"
                    ),
                    equation=raw.get(
                        "equation"
                    ),
                    assumption=raw.get(
                        "assumption"
                    ),
                    method=raw.get(
                        "method"
                    ),
                    result=raw.get(
                        "result"
                    ),
                    limitation=raw.get(
                        "limitation"
                    ),
                    contradiction=raw.get(
                        "contradiction"
                    ),
                    provenance_anchor=raw.get(
                        "provenance_anchor"
                    ),
                )
            )

        # Source-free creation is allowed only when caller explicitly
        # marks the task as architecture/model design.
        if (
            not state.sources
            and not inputs.get(
                "allow_source_free_model_design",
                False,
            )
        ):
            state.gaps.append(
                GapRecord(
                    gap_id=self._new_id(
                        "gap"
                    ),
                    gap_class=(
                        GapClass.DECISION_RELEVANT
                    ),
                    description=(
                        "No source records supplied."
                    ),
                    blocking=False,
                    repair_action=(
                        "load authoritative sources if "
                        "source-derived claims are required"
                    ),
                    confidence_impact=0.20,
                )
            )

        contradictions = [
            source
            for source in state.sources
            if source.contradiction
        ]

        return {
            "source_records": len(
                state.sources
            ),
            "contradictions": len(
                contradictions
            ),
        }

    # ========================================================
    # PARSE
    # ========================================================

    def _stage_parse(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        deterministic_parse_required = bool(
            inputs.get(
                "deterministic_parse_required",
                False,
            )
        )

        raw_code = inputs.get(
            "code_state",
            [],
        )

        raw_system = inputs.get(
            "system_state",
            [],
        )

        raw_claims = inputs.get(
            "claims",
            [],
        )

        if not isinstance(
            raw_code,
            list,
        ):
            raise ValidationError(
                "code_state must be a list"
            )

        if not isinstance(
            raw_system,
            list,
        ):
            raise ValidationError(
                "system_state must be a list"
            )

        if not isinstance(
            raw_claims,
            list,
        ):
            raise ValidationError(
                "claims must be a list"
            )

        state.code_state = [
            CodeState(
                file=str(
                    item.get(
                        "file",
                        "",
                    )
                ),
                language=item.get(
                    "language"
                ),
                ast_node=item.get(
                    "AST_node"
                ),
                symbol=item.get(
                    "symbol"
                ),
                imports=list(
                    item.get(
                        "imports",
                        [],
                    )
                ),
                call_edges=list(
                    item.get(
                        "call_edges",
                        [],
                    )
                ),
                cfg_edges=list(
                    item.get(
                        "CFG_edges",
                        [],
                    )
                ),
                data_edges=list(
                    item.get(
                        "data_edges",
                        [],
                    )
                ),
                schema=item.get(
                    "schema"
                ),
                config=item.get(
                    "config"
                ),
                tests=list(
                    item.get(
                        "tests",
                        [],
                    )
                ),
                runtime_trace=item.get(
                    "runtime_trace"
                ),
                provenance=self._parse_provenance(
                    item.get(
                        "provenance",
                        [],
                    )
                ),
            )
            for item in raw_code
            if isinstance(
                item,
                dict,
            )
        ]

        state.system_state = [
            SystemState(
                component=str(
                    item.get(
                        "component",
                        "",
                    )
                ),
                interface=item.get(
                    "interface"
                ),
                dependency=item.get(
                    "dependency"
                ),
                data_contract=item.get(
                    "data_contract"
                ),
                config=item.get(
                    "config"
                ),
                resource=item.get(
                    "resource"
                ),
                runtime=item.get(
                    "runtime"
                ),
                policy=item.get(
                    "policy"
                ),
                owner=item.get(
                    "owner"
                ),
                risk=item.get(
                    "risk"
                ),
                provenance=self._parse_provenance(
                    item.get(
                        "provenance",
                        [],
                    )
                ),
            )
            for item in raw_system
            if isinstance(
                item,
                dict,
            )
        ]

        state.claims = [
            ClaimState(
                claim_id=str(
                    item.get(
                        "id",
                        self._new_id(
                            "claim"
                        ),
                    )
                ),
                epistemic_class=self._parse_epistemic(
                    item.get(
                        "class",
                        "UNKNOWN/GAP",
                    )
                ),
                premises=list(
                    item.get(
                        "premises",
                        [],
                    )
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
                        state.target_skill or state.objective,
                    )
                ),
                regime=str(
                    item.get(
                        "regime",
                        "default",
                    )
                ),
                falsifiers=list(
                    item.get(
                        "falsifiers",
                        [],
                    )
                ),
                status=str(
                    item.get(
                        "status",
                        "OPEN",
                    )
                ),
                confidence=self._clamp_confidence(
                    item.get(
                        "confidence",
                        0.5,
                    )
                ),
                provenance=self._parse_provenance(
                    item.get(
                        "provenance",
                        [],
                    )
                ),
            )
            for item in raw_claims
            if isinstance(
                item,
                dict,
            )
        ]

        if (
            deterministic_parse_required
            and not (
                state.code_state
                or state.system_state
                or state.claims
            )
        ):
            raise ParseGapError(
                "PARSE_GAP: deterministic structure "
                "could not be recovered."
            )

        return {
            "code_records": len(
                state.code_state
            ),
            "system_records": len(
                state.system_state
            ),
            "claims": len(
                state.claims
            ),
        }

    # ========================================================
    # TYPE
    # ========================================================

    def _stage_type(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        raw_x = inputs.get(
            "tensor_x",
            [],
        )

        raw_h = inputs.get(
            "tensor_h",
            [],
        )

        if not isinstance(
            raw_x,
            list,
        ):
            raise ValidationError(
                "tensor_x must be a list"
            )

        if not isinstance(
            raw_h,
            list,
        ):
            raise ValidationError(
                "tensor_h must be a list"
            )

        for raw in raw_x:

            if not isinstance(
                raw,
                dict,
            ):
                continue

            state.tensors_x.append(
                CanonicalTensor(
                    object=str(
                        raw.get(
                            "object",
                            state.target_skill
                            or state.objective,
                        )
                    ),
                    primitive=str(
                        raw.get(
                            "primitive",
                            "skill",
                        )
                    ),
                    scale=str(
                        raw.get(
                            "scale",
                            "M",
                        )
                    ),
                    time=str(
                        raw.get(
                            "time",
                            "current",
                        )
                    ),
                    regime=str(
                        raw.get(
                            "regime",
                            "default",
                        )
                    ),
                    observer=str(
                        raw.get(
                            "observer",
                            AGENT_ID,
                        )
                    ),
                    provenance=self._parse_provenance(
                        raw.get(
                            "provenance",
                            [],
                        )
                    ),
                    epistemic_class=self._parse_epistemic(
                        raw.get(
                            "epistemic_class",
                            "AMOS_MODEL",
                        )
                    ),
                    confidence=self._clamp_confidence(
                        raw.get(
                            "confidence",
                            0.5,
                        )
                    ),
                    consequence=dict(
                        raw.get(
                            "consequence",
                            {},
                        )
                    ),
                )
            )

        for raw in raw_h:

            if not isinstance(
                raw,
                dict,
            ):
                continue

            state.tensors_h.append(
                HarnessTensor(
                    artifact=str(
                        raw.get(
                            "artifact",
                            state.target_skill
                            or "skill",
                        )
                    ),
                    representation=str(
                        raw.get(
                            "representation",
                            "skill",
                        )
                    ),
                    parser_state=str(
                        raw.get(
                            "parser_state",
                            "UNKNOWN",
                        )
                    ),
                    context_state=str(
                        raw.get(
                            "context_state",
                            "UNKNOWN",
                        )
                    ),
                    execution_state=str(
                        raw.get(
                            "execution_state",
                            "NOT_RUN",
                        )
                    ),
                    test_state=str(
                        raw.get(
                            "test_state",
                            "NOT_RUN",
                        )
                    ),
                    invariant_state=str(
                        raw.get(
                            "invariant_state",
                            "UNKNOWN",
                        )
                    ),
                    evidence_state=str(
                        raw.get(
                            "evidence_state",
                            "UNKNOWN",
                        )
                    ),
                    repair_state=str(
                        raw.get(
                            "repair_state",
                            "NONE",
                        )
                    ),
                    version=str(
                        raw.get(
                            "version",
                            "0.0.0",
                        )
                    ),
                    provenance=self._parse_provenance(
                        raw.get(
                            "provenance",
                            [],
                        )
                    ),
                )
            )

        return {
            "X_count": len(
                state.tensors_x
            ),
            "H_count": len(
                state.tensors_h
            ),
        }

    # ========================================================
    # UNDERSTAND
    # ========================================================

    def _stage_understand(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        dependency_closure_covered = bool(
            inputs.get(
                "dependency_closure_covered",
                bool(
                    state.code_state
                    or state.system_state
                    or inputs.get(
                        "architecture"
                    )
                ),
            )
        )

        contracts_recovered = bool(
            inputs.get(
                "load_bearing_contracts_recovered",
                bool(
                    inputs.get(
                        "interfaces"
                    )
                    or inputs.get(
                        "contracts"
                    )
                ),
            )
        )

        gaps_classified = bool(
            inputs.get(
                "critical_gaps_classified",
                True,
            )
        )

        sufficient = (
            dependency_closure_covered
            and contracts_recovered
            and gaps_classified
        )

        if not sufficient:

            state.gaps.append(
                GapRecord(
                    gap_id=self._new_id(
                        "gap"
                    ),
                    gap_class=(
                        GapClass.DECISION_RELEVANT
                    ),
                    description=(
                        "UnderstandingSufficient(q) is false."
                    ),
                    blocking=bool(
                        inputs.get(
                            "understanding_required_for_create",
                            True,
                        )
                    ),
                    repair_action=(
                        "recover smallest sufficient dependency closure"
                    ),
                    confidence_impact=0.25,
                )
            )

        if any(
            gap.blocking
            for gap in state.gaps
            if (
                gap.description
                == "UnderstandingSufficient(q) is false."
            )
        ):
            raise GapError(
                "UNKNOWN/GAP: system understanding insufficient."
            )

        return {
            "dependency_closure_covered":
                dependency_closure_covered,
            "load_bearing_contracts_recovered":
                contracts_recovered,
            "critical_gaps_classified":
                gaps_classified,
            "understanding_sufficient":
                sufficient,
        }

    # ========================================================
    # MODEL
    # ========================================================

    def _stage_model(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        raw_invariants = inputs.get(
            "hard_invariants",
            [],
        )

        if not isinstance(
            raw_invariants,
            list,
        ):
            raise ValidationError(
                "hard_invariants must be a list"
            )

        state.invariants = [
            HardInvariant(
                invariant_id=str(
                    raw.get(
                        "invariant_id",
                        self._new_id(
                            "inv"
                        ),
                    )
                ),
                description=str(
                    raw.get(
                        "description",
                        "",
                    )
                ),
                passed=raw.get(
                    "passed"
                ),
                evidence=list(
                    raw.get(
                        "evidence",
                        [],
                    )
                ),
                reason=raw.get(
                    "reason"
                ),
            )
            for raw in raw_invariants
            if isinstance(
                raw,
                dict,
            )
        ]

        # Default integrity invariant.
        if not state.invariants:

            state.invariants.append(
                HardInvariant(
                    invariant_id=(
                        "I_NO_FABRICATION"
                    ),
                    description=(
                        "No invented evidence, equations, "
                        "execution results, provenance, dependencies, "
                        "or tool capabilities."
                    ),
                    passed=True,
                    evidence=[
                        "builder runtime policy"
                    ],
                )
            )

        gate = self._admit(
            state.invariants
        )

        if gate is False:
            raise ValidationError(
                "Hard admission failed."
            )

        if gate is None:
            raise GapError(
                "UNKNOWN/GAP: hard invariant unresolved."
            )

        return {
            "H": {
                "mission": state.objective,
                "scope": state.target_skill,
                "invariants": len(
                    state.invariants
                ),
            },
            "M": {
                "workflow": [
                    stage.value
                    for stage in BuilderStage
                ],
            },
            "L": {
                "claims": len(
                    state.claims
                ),
                "tensor_X": len(
                    state.tensors_x
                ),
                "tensor_H": len(
                    state.tensors_h
                ),
            },
        }

    # ========================================================
    # PLAN
    # ========================================================

    def _stage_plan(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        raw_plan = inputs.get(
            "plan_actions",
            [],
        )

        if not isinstance(
            raw_plan,
            list,
        ):
            raise ValidationError(
                "plan_actions must be a list"
            )

        state.plan = [
            PlanAction(
                action_id=str(
                    raw.get(
                        "action_id",
                        self._new_id(
                            "action"
                        ),
                    )
                ),
                description=str(
                    raw.get(
                        "description",
                        "",
                    )
                ),
                impact=self._clamp_confidence(
                    raw.get(
                        "impact",
                        0.5,
                    )
                ),
                uncertainty_reduction=(
                    self._clamp_confidence(
                        raw.get(
                            "uncertainty_reduction",
                            0.5,
                        )
                    )
                ),
                dependency_fanout=(
                    max(
                        float(
                            raw.get(
                                "dependency_fanout",
                                1.0,
                            )
                        ),
                        0.0,
                    )
                ),
                cost=max(
                    float(
                        raw.get(
                            "cost",
                            1.0,
                        )
                    ),
                    0.000001,
                ),
                required=bool(
                    raw.get(
                        "required",
                        False,
                    )
                ),
            )
            for raw in raw_plan
            if isinstance(
                raw,
                dict,
            )
        ]

        state.plan.sort(
            key=lambda action:
                action.priority(),
            reverse=True,
        )

        return {
            "actions": [
                {
                    "action_id": action.action_id,
                    "priority": action.priority(),
                    "description": action.description,
                }
                for action in state.plan
            ],
        }

    # ========================================================
    # CREATE
    # ========================================================

    def _stage_create(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        raw_candidate = inputs.get(
            "create_candidate",
            {},
        )

        if not isinstance(
            raw_candidate,
            dict,
        ):
            raise ValidationError(
                "create_candidate must be a dictionary"
            )

        architecture = dict(
            raw_candidate.get(
                "architecture",
                inputs.get(
                    "architecture",
                    {},
                ),
            )
        )

        interfaces = list(
            raw_candidate.get(
                "interfaces",
                inputs.get(
                    "interfaces",
                    [],
                ),
            )
        )

        constraints = list(
            raw_candidate.get(
                "constraints",
                inputs.get(
                    "constraints",
                    [],
                ),
            )
        )

        evidence = list(
            raw_candidate.get(
                "evidence",
                inputs.get(
                    "creation_evidence",
                    [],
                ),
            )
        )

        tests = list(
            raw_candidate.get(
                "tests",
                inputs.get(
                    "test_oracles",
                    [],
                ),
            )
        )

        change_boundary = list(
            raw_candidate.get(
                "change_boundary",
                inputs.get(
                    "change_boundary",
                    [],
                ),
            )
        )

        state.create_candidate = (
            CreateCandidate(
                intent=str(
                    raw_candidate.get(
                        "intent",
                        state.objective,
                    )
                ),
                architecture=architecture,
                interfaces=interfaces,
                constraints=constraints,
                evidence=evidence,
                tests=tests,
                change_boundary=change_boundary,
            )
        )

        if not change_boundary:
            raise GapError(
                "UNKNOWN/GAP: change boundary is undefined."
            )

        return {
            "candidate": asdict(
                state.create_candidate
            ),
        }

    # ========================================================
    # EXECUTE
    # ========================================================

    def _stage_execute(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        raw_runs = inputs.get(
            "execution_records",
            [],
        )

        if not isinstance(
            raw_runs,
            list,
        ):
            raise ValidationError(
                "execution_records must be a list"
            )

        execution_required = bool(
            inputs.get(
                "execution_required",
                False,
            )
        )

        for raw in raw_runs:

            if not isinstance(
                raw,
                dict,
            ):
                continue

            executed = bool(
                raw.get(
                    "executed",
                    False,
                )
            )

            test_state = self._parse_test_state(
                raw.get(
                    "test_state",
                    (
                        "EXECUTION_GAP"
                        if not executed
                        else "NOT_RUN"
                    ),
                )
            )

            record = ExecutionRecord(
                command=str(
                    raw.get(
                        "command",
                        "",
                    )
                ),
                cwd=str(
                    raw.get(
                        "cwd",
                        ".",
                    )
                ),
                environment=dict(
                    raw.get(
                        "environment",
                        {},
                    )
                ),
                input_hash=str(
                    raw.get(
                        "input_hash",
                        "",
                    )
                ),
                exit_code=raw.get(
                    "exit_code"
                ),
                stdout_hash=raw.get(
                    "stdout_hash"
                ),
                stderr_hash=raw.get(
                    "stderr_hash"
                ),
                duration=raw.get(
                    "duration"
                ),
                timeout=raw.get(
                    "timeout"
                ),
                artifact_hash=raw.get(
                    "artifact_hash"
                ),
                parent_run=raw.get(
                    "parent_run"
                ),
                state_hash=str(
                    raw.get(
                        "state_hash",
                        self._hash_json(
                            raw
                        ),
                    )
                ),
                test_state=test_state,
                executed=executed,
                observation=raw.get(
                    "observation"
                ),
            )

            state.executions.append(
                record
            )

        if (
            execution_required
            and not any(
                record.executed
                for record in state.executions
            )
        ):
            state.observations.execution = (
                TestState.EXECUTION_GAP
            )

            raise ExecutionGapError(
                "EXECUTION_GAP: required execution "
                "could not be performed."
            )

        return {
            "execution_records": len(
                state.executions
            ),
            "executed_records": sum(
                1
                for record in state.executions
                if record.executed
            ),
        }

    # ========================================================
    # OBSERVE
    # ========================================================

    def _stage_observe(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        raw = inputs.get(
            "observation_state",
            {},
        )

        if not isinstance(
            raw,
            dict,
        ):
            raise ValidationError(
                "observation_state must be a dictionary"
            )

        state.observations = (
            ObservationState(
                syntax=self._parse_test_state(
                    raw.get(
                        "syntax",
                        "NOT_RUN",
                    )
                ),
                static=self._parse_test_state(
                    raw.get(
                        "static",
                        "NOT_RUN",
                    )
                ),
                execution=self._parse_test_state(
                    raw.get(
                        "execution",
                        "NOT_RUN",
                    )
                ),
                tests=self._parse_test_state(
                    raw.get(
                        "tests",
                        "NOT_RUN",
                    )
                ),
                spec=self._parse_test_state(
                    raw.get(
                        "spec",
                        "NOT_RUN",
                    )
                ),
                system=self._parse_test_state(
                    raw.get(
                        "system",
                        "NOT_RUN",
                    )
                ),
                regression=self._parse_test_state(
                    raw.get(
                        "regression",
                        "NOT_RUN",
                    )
                ),
            )
        )

        # Later passes never erase earlier failures.
        return {
            "states": asdict(
                state.observations
            ),
            "failures": [
                failure.value
                for failure
                in state.observations.failures()
            ],
        }

    # ========================================================
    # VERIFY
    # ========================================================

    def _stage_verify(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        premises = {
            str(key):
                self._clamp_confidence(
                    value
                )
            for key, value
            in inputs.get(
                "premise_confidences",
                {},
            ).items()
        }

        confidence = (
            self._confidence_ceiling(
                premises
            )
        )

        hypotheses = [
            CompetingHypothesis(
                hypothesis_id=str(
                    raw.get(
                        "hypothesis_id",
                        self._new_id(
                            "hyp"
                        ),
                    )
                ),
                statement=str(
                    raw.get(
                        "statement",
                        "",
                    )
                ),
                confidence=self._clamp_confidence(
                    raw.get(
                        "confidence",
                        0.0,
                    )
                ),
                evidence=list(
                    raw.get(
                        "evidence",
                        [],
                    )
                ),
                counterevidence=list(
                    raw.get(
                        "counterevidence",
                        [],
                    )
                ),
                falsifiers=list(
                    raw.get(
                        "falsifiers",
                        [],
                    )
                ),
            )
            for raw in inputs.get(
                "competing_hypotheses",
                [],
            )
            if isinstance(
                raw,
                dict,
            )
        ]

        state.rscf = (
            RSCFCapsule(
                claim=str(
                    inputs.get(
                        "verification_claim",
                        (
                            "The generated Skill satisfies "
                            "the supplied architecture, contracts, "
                            "invariants, specification, and regression "
                            "requirements."
                        ),
                    )
                ),
                epistemic_class=(
                    EpistemicClass.DERIVED
                ),
                premises=premises,
                evidence=list(
                    inputs.get(
                        "verification_evidence",
                        [],
                    )
                ),
                provenance=(
                    self._parse_provenance(
                        inputs.get(
                            "verification_provenance",
                            [],
                        )
                    )
                    or self._default_provenance()
                ),
                dependencies=list(
                    inputs.get(
                        "verification_dependencies",
                        [],
                    )
                ),
                scope=str(
                    inputs.get(
                        "verification_scope",
                        state.target_skill
                        or state.objective,
                    )
                ),
                regime=str(
                    inputs.get(
                        "verification_regime",
                        "default",
                    )
                ),
                freshness=self._clamp_confidence(
                    inputs.get(
                        "verification_freshness",
                        0.5,
                    )
                ),
                falsifiers=list(
                    inputs.get(
                        "falsifiers",
                        [],
                    )
                ),
                competing_hypotheses=hypotheses,
                confidence_ceiling=confidence,
                consequence=dict(
                    inputs.get(
                        "consequence",
                        {},
                    )
                ),
                repair_path=inputs.get(
                    "repair_path"
                ),
            )
        )

        return {
            "rscf": asdict(
                state.rscf
            ),
        }

    # ========================================================
    # CHALLENGE
    # ========================================================

    def _stage_challenge(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        raw = inputs.get(
            "challenge",
            {},
        )

        if not isinstance(
            raw,
            dict,
        ):
            raise ValidationError(
                "challenge must be a dictionary"
            )

        state.challenge = ChallengeResult(
            parser_information_loss=bool(
                raw.get(
                    "parser_information_loss",
                    False,
                )
            ),
            stale_context=bool(
                raw.get(
                    "stale_context",
                    False,
                )
            ),
            correlated_provenance=bool(
                raw.get(
                    "correlated_provenance",
                    False,
                )
            ),
            hidden_dependency=bool(
                raw.get(
                    "hidden_dependency",
                    False,
                )
            ),
            tensor_axis_mismatch=bool(
                raw.get(
                    "tensor_axis_mismatch",
                    False,
                )
            ),
            undefined_equation_variables=bool(
                raw.get(
                    "undefined_equation_variables",
                    False,
                )
            ),
            architecture_drift=bool(
                raw.get(
                    "architecture_drift",
                    False,
                )
            ),
            local_pass_global_fail=bool(
                raw.get(
                    "local_pass_global_fail",
                    False,
                )
            ),
            benchmark_mismatch=bool(
                raw.get(
                    "benchmark_mismatch",
                    False,
                )
            ),
            causal_overreach=bool(
                raw.get(
                    "causal_overreach",
                    False,
                )
            ),
            authority_mismatch=bool(
                raw.get(
                    "authority_mismatch",
                    False,
                )
            ),
            storage_context_blowup=bool(
                raw.get(
                    "storage_context_blowup",
                    False,
                )
            ),
            repair_regression=bool(
                raw.get(
                    "repair_regression",
                    False,
                )
            ),
            issues=list(
                raw.get(
                    "issues",
                    [],
                )
            ),
        )

        if state.challenge.succeeded():

            state.gaps.append(
                GapRecord(
                    gap_id=self._new_id(
                        "gap"
                    ),
                    gap_class=(
                        GapClass.DECISION_RELEVANT
                    ),
                    description=(
                        "Independent challenge found a "
                        "decision-relevant issue."
                    ),
                    blocking=bool(
                        inputs.get(
                            "challenge_issue_blocking",
                            True,
                        )
                    ),
                    repair_action=(
                        "repair challenged dependency and revalidate"
                    ),
                    confidence_impact=0.20,
                )
            )

        return {
            "challenge_succeeded":
                state.challenge.succeeded(),
            "challenge": asdict(
                state.challenge
            ),
        }

    # ========================================================
    # REPAIR
    # ========================================================

    def _stage_repair(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        if not state.challenge:
            return {
                "repair_required": False,
            }

        if not state.challenge.succeeded():
            return {
                "repair_required": False,
            }

        repair = inputs.get(
            "repair",
            {},
        )

        if not isinstance(
            repair,
            dict,
        ):
            raise ValidationError(
                "repair must be a dictionary"
            )

        changed_evidence = bool(
            repair.get(
                "changed_evidence",
                False,
            )
        )

        changed_code = bool(
            repair.get(
                "changed_code",
                False,
            )
        )

        changed_assumptions = bool(
            repair.get(
                "changed_assumptions",
                False,
            )
        )

        changed_environment = bool(
            repair.get(
                "changed_environment",
                False,
            )
        )

        changed_test_design = bool(
            repair.get(
                "changed_test_design",
                False,
            )
        )

        changed = any(
            (
                changed_evidence,
                changed_code,
                changed_assumptions,
                changed_environment,
                changed_test_design,
            )
        )

        if not changed:
            raise GapError(
                "UNKNOWN/GAP: failed path cannot be repeated "
                "without changed evidence/code/assumptions/"
                "environment/test design."
            )

        reexecuted = bool(
            repair.get(
                "reexecuted",
                False,
            )
        )

        regression_checked = bool(
            repair.get(
                "regression_checked",
                False,
            )
        )

        rscf_revalidated = bool(
            repair.get(
                "rscf_revalidated",
                False,
            )
        )

        if not all(
            (
                reexecuted,
                regression_checked,
                rscf_revalidated,
            )
        ):
            raise GapError(
                "UNKNOWN/GAP: repair incomplete. "
                "Required: ReExecute -> RegressionCheck -> RevalidateRSCF."
            )

        # Clear only repairable challenge-dependent gaps.
        for gap in state.gaps:
            if (
                "challenge"
                in gap.description.lower()
            ):
                gap.blocking = False

        return {
            "repair_required": True,
            "causal_target": repair.get(
                "causal_target"
            ),
            "minimal_state_modified": (
                repair.get(
                    "minimal_state_modified",
                    True,
                )
            ),
            "reexecuted": reexecuted,
            "regression_checked":
                regression_checked,
            "rscf_revalidated":
                rscf_revalidated,
        }

    # ========================================================
    # COMPRESS
    # ========================================================

    def _stage_compress(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        retained = []
        compressed = []

        for item in state.context_map:

            if item.compressible():
                compressed.append(
                    asdict(
                        item
                    )
                )
            else:
                retained.append(
                    asdict(
                        item
                    )
                )

        state.artifacts[
            "retention"
        ] = {
            "decisions": list(
                inputs.get(
                    "retained_decisions",
                    [],
                )
            ),
            "observations": [
                asdict(
                    record
                )
                for record
                in state.executions
            ],
            "derivations": (
                asdict(
                    state.rscf
                )
                if state.rscf
                else None
            ),
            "duplicates": list(
                inputs.get(
                    "duplicates",
                    [],
                )
            ),
        }

        return {
            "retained": retained,
            "compressed": compressed,
            "recoverability_preserved": True,
        }

    # ========================================================
    # PACKAGE
    # ========================================================

    def _stage_package(
        self,
        state: BuilderState,
        inputs: Dict[str, Any],
    ) -> Dict[str, Any]:

        package = inputs.get(
            "package",
            {},
        )

        if not isinstance(
            package,
            dict,
        ):
            raise ValidationError(
                "package must be a dictionary"
            )

        skill_md_present = bool(
            package.get(
                "skill_md_present",
                False,
            )
        )

        references_present = bool(
            package.get(
                "references_present",
                False,
            )
        )

        scripts_present = bool(
            package.get(
                "scripts_present",
                False,
            )
        )

        validate_script_run = bool(
            package.get(
                "validate_amos_skill_run",
                False,
            )
        )

        domain_tests_run = bool(
            package.get(
                "domain_tests_run",
                False,
            )
        )

        official_packaging_run = bool(
            package.get(
                "official_skill_creator_packaging_run",
                False,
            )
        )

        complete_zip_present = bool(
            package.get(
                "complete_skill_zip_present",
                False,
            )
        )

        required = [
            skill_md_present,
            validate_script_run,
            domain_tests_run,
            official_packaging_run,
            complete_zip_present,
        ]

        if not all(
            required
        ):
            raise GapError(
                "UNKNOWN/GAP: package incomplete. "
                "Complete Skill packaging evidence missing."
            )

        state.artifacts[
            "package"
        ] = {
            "skill_md_present":
                skill_md_present,
            "references_present":
                references_present,
            "scripts_present":
                scripts_present,
            "validate_amos_skill_run":
                validate_script_run,
            "domain_tests_run":
                domain_tests_run,
            "official_skill_creator_packaging_run":
                official_packaging_run,
            "complete_skill_zip_present":
                complete_zip_present,
            "skill_zip_path":
                package.get(
                    "skill_zip_path"
                ),
            "installation_occurred":
                bool(
                    package.get(
                        "installation_occurred",
                        False,
                    )
                ),
        }

        return state.artifacts[
            "package"
        ]

    # ========================================================
    # VALIDATE BUILDER
    # ========================================================

    def _validate_builder(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        raw = ctx.inputs.get(
            "builder_state"
        )

        if not isinstance(
            raw,
            dict,
        ):
            raise GapError(
                "UNKNOWN/GAP: builder_state dictionary required."
            )

        issues: List[str] = []

        observation = raw.get(
            "observations",
            {}
        )

        promotion = {
            ValidationGate.ARCHITECTURE_COMPATIBLE:
                bool(
                    ctx.inputs.get(
                        "architecture_compatible",
                        False,
                    )
                ),

            ValidationGate.CONTRACT_COMPATIBLE:
                bool(
                    ctx.inputs.get(
                        "contract_compatible",
                        False,
                    )
                ),

            ValidationGate.HARD_INVARIANTS_PASS:
                bool(
                    ctx.inputs.get(
                        "hard_invariants_pass",
                        False,
                    )
                ),

            ValidationGate.SPEC_PASS:
                (
                    observation.get(
                        "spec"
                    )
                    == "SPEC_PASS"
                ),

            ValidationGate.REGRESSION_PASS:
                (
                    observation.get(
                        "regression"
                    )
                    == "REGRESSION_PASS"
                ),
        }

        for gate, passed in promotion.items():

            if not passed:
                issues.append(
                    f"promotion_gate_failed:{gate.value}"
                )

        # Keep pass classes distinct.
        if (
            observation.get(
                "system"
            )
            == "SYSTEM_PASS"
            and observation.get(
                "spec"
            )
            != "SPEC_PASS"
        ):
            issues.append(
                "system_pass_does_not_erase_spec_failure"
            )

        if (
            observation.get(
                "regression"
            )
            == "REGRESSION_PASS"
            and observation.get(
                "execution"
            )
            == "EXECUTION_FAIL"
        ):
            issues.append(
                "later_pass_does_not_erase_execution_failure"
            )

        package = raw.get(
            "artifacts",
            {}
        ).get(
            "package",
            {}
        )

        if not package.get(
            "complete_skill_zip_present",
            False,
        ):
            issues.append(
                "complete_skill_zip_missing"
            )

        return AgentResult(
            status=(
                ExecutionStatus.VERIFIED
                if not issues
                else ExecutionStatus.CONDITIONAL
            ),
            capability=ctx.capability,
            summary=(
                "Skill Builder validation completed."
            ),
            data={
                "promotion": {
                    gate.value: passed
                    for gate, passed
                    in promotion.items()
                },
                "issues": issues,
            },
            gaps=issues,
            confidence_ceiling=self.claim_ceiling,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # ANALYZE BUILDER
    # ========================================================

    def _analyze_builder(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        raw = ctx.inputs.get(
            "builder_state",
            {}
        )

        if not isinstance(
            raw,
            dict,
        ):
            raise GapError(
                "UNKNOWN/GAP: builder_state required."
            )

        stages = raw.get(
            "stages",
            {}
        )

        failed = [
            name
            for name, stage
            in stages.items()
            if isinstance(
                stage,
                dict,
            )
            and stage.get(
                "status"
            )
            in {
                "FAIL",
                "GAP",
            }
        ]

        common_modules = {
            "context_orientation":
                ctx.inputs.get(
                    "has_context_orientation",
                    False,
                ),

            "context_budget":
                ctx.inputs.get(
                    "has_context_budget",
                    False,
                ),

            "storage_footprint":
                ctx.inputs.get(
                    "has_storage_footprint",
                    False,
                ),

            "deep_source_parsing":
                ctx.inputs.get(
                    "has_deep_source_parsing",
                    False,
                ),

            "repository_graphing":
                ctx.inputs.get(
                    "has_repository_graphing",
                    False,
                ),

            "architecture_reconstruction":
                ctx.inputs.get(
                    "has_architecture_reconstruction",
                    False,
                ),

            "operational_spec_recovery":
                ctx.inputs.get(
                    "has_operational_spec_recovery",
                    False,
                ),

            "execution_provenance":
                ctx.inputs.get(
                    "has_execution_provenance",
                    False,
                ),

            "replay":
                ctx.inputs.get(
                    "has_replay",
                    False,
                ),

            "rollback":
                ctx.inputs.get(
                    "has_rollback",
                    False,
                ),

            "benchmark_forensics":
                ctx.inputs.get(
                    "has_benchmark_forensics",
                    False,
                ),

            "system_completion_audit":
                ctx.inputs.get(
                    "has_system_completion_audit",
                    False,
                ),
        }

        missing = [
            name
            for name, present
            in common_modules.items()
            if not present
        ]

        return AgentResult(
            status=(
                ExecutionStatus.CONDITIONAL
                if failed or missing
                else ExecutionStatus.DERIVED
            ),
            capability=ctx.capability,
            summary=(
                "Skill Builder structural analysis completed."
            ),
            data={
                "failed_or_gap_stages": failed,
                "missing_system_modules": missing,
                "local_repository_runtime_requirement_distinctions": {
                    "LOCAL_CORRECTNESS": True,
                    "REPOSITORY_COHERENCE": True,
                    "RUNTIME_CORRECTNESS": True,
                    "REQUIREMENT_CORRECTNESS": True,
                },
            },
            gaps=(
                failed
                + [
                    f"missing_module:{item}"
                    for item in missing
                ]
            ),
            confidence_ceiling=self.claim_ceiling,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # TRACE PROVENANCE
    # ========================================================

    def _trace_builder_provenance(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        records = ctx.inputs.get(
            "records",
            [],
        )

        if not isinstance(
            records,
            list,
        ):
            raise GapError(
                "UNKNOWN/GAP: records must be a list."
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

            dependencies = record.get(
                "dependencies",
                []
            )

            if not provenance:
                gaps.append(
                    f"record[{index}]:missing_provenance"
                )

            traced.append({
                "index": index,
                "record_id": (
                    record.get(
                        "claim_id"
                    )
                    or record.get(
                        "artifact_id"
                    )
                    or record.get(
                        "run_id"
                    )
                    or record.get(
                        "id"
                    )
                ),
                "provenance": provenance,
                "dependencies": dependencies,
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
                "Skill Builder provenance trace completed."
            ),
            data={
                "records": traced,
            },
            gaps=gaps,
            confidence_ceiling=self.claim_ceiling,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # CLAIM ASSESSMENT
    # ========================================================

    def _assess_builder_claim(
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
            "failed_execution_as_success"
        ) is True:
            issues.append(
                "failed_execution_cannot_be_conceptual_success"
            )

        if claim.get(
            "later_pass_erases_earlier_failure"
        ) is True:
            issues.append(
                "later_pass_does_not_erase_earlier_failure"
            )

        if claim.get(
            "complexity_equals_speedup"
        ) is True:
            issues.append(
                "complexity_class_not_measured_speedup"
            )

        if claim.get(
            "installation_claim_without_installation"
        ) is True:
            issues.append(
                "do_not_claim_installation_without_installation"
            )

        premises = {
            str(key):
                self._clamp_confidence(
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
                "Skill Builder claim assessment completed."
            ),
            data={
                "issues": issues,
                "confidence_ceiling":
                    confidence,
                "epistemic_class":
                    claim.get(
                        "epistemic_class",
                        "DERIVED",
                    ),
            },
            gaps=issues,
            confidence_ceiling=confidence,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # LIFECYCLE
    # ========================================================

    def _manage_builder_lifecycle(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        operation = str(
            ctx.inputs.get(
                "operation",
                "",
            )
        ).lower()

        if operation not in {
            "init",
            "run",
            "checkpoint",
            "recover",
            "finalize",
        }:
            raise ValidationError(
                "operation must be one of: "
                "init, run, checkpoint, recover, finalize"
            )

        if operation == "init":

            state = self._new_builder_state(
                objective=str(
                    ctx.inputs.get(
                        "objective",
                        ctx.query,
                    )
                ),
                target_skill=ctx.inputs.get(
                    "target_skill"
                ),
            )

            return AgentResult(
                status=ExecutionStatus.MODEL,
                capability=ctx.capability,
                summary=(
                    "Builder lifecycle initialized."
                ),
                data={
                    "builder_state":
                        self._serialize_state(
                            state
                        ),
                },
                provenance=self._default_provenance(),
            )

        if operation == "checkpoint":

            state_raw = ctx.inputs.get(
                "builder_state"
            )

            if not isinstance(
                state_raw,
                dict,
            ):
                raise GapError(
                    "UNKNOWN/GAP: builder_state required "
                    "for checkpoint."
                )

            checkpoint = self._checkpoint_from_dict(
                state_raw
            )

            return AgentResult(
                status=ExecutionStatus.VERIFIED,
                capability=ctx.capability,
                summary=(
                    "Builder checkpoint created."
                ),
                data={
                    "checkpoint":
                        asdict(
                            checkpoint
                        ),
                },
                provenance=self._default_provenance(),
            )

        if operation == "recover":

            checkpoint_raw = ctx.inputs.get(
                "checkpoint"
            )

            if not isinstance(
                checkpoint_raw,
                dict,
            ):
                raise GapError(
                    "UNKNOWN/GAP: checkpoint required."
                )

            recovered = dict(
                checkpoint_raw
            )

            recovered[
                "lifecycle_state"
            ] = LifecycleState.RECOVERING.value

            return AgentResult(
                status=ExecutionStatus.DERIVED,
                capability=ctx.capability,
                summary=(
                    "Builder state recovered from checkpoint."
                ),
                data={
                    "recovered_state":
                        recovered,
                    "recovery_rule": (
                        "resume from nearest valid state; "
                        "do not recompute unaffected work"
                    ),
                },
                provenance=self._default_provenance(),
            )

        if operation == "finalize":

            complete = bool(
                ctx.inputs.get(
                    "claim_sufficient",
                    False,
                )
                and ctx.inputs.get(
                    "decision_sufficient",
                    False,
                )
                and ctx.inputs.get(
                    "action_sufficient",
                    False,
                )
            )

            return AgentResult(
                status=(
                    ExecutionStatus.VERIFIED
                    if complete
                    else ExecutionStatus.CONDITIONAL
                ),
                capability=ctx.capability,
                summary=(
                    "Builder finalized."
                    if complete
                    else (
                        "Builder cannot finalize: "
                        "stop rule not satisfied."
                    )
                ),
                data={
                    "ClaimSufficient":
                        bool(
                            ctx.inputs.get(
                                "claim_sufficient",
                                False,
                            )
                        ),
                    "DecisionSufficient":
                        bool(
                            ctx.inputs.get(
                                "decision_sufficient",
                                False,
                            )
                        ),
                    "ActionSufficient":
                        bool(
                            ctx.inputs.get(
                                "action_sufficient",
                                False,
                            )
                        ),
                },
                provenance=self._default_provenance(),
            )

        # operation == "run"
        return self._design_builder(
            ExecutionContext(
                query=ctx.query,
                capability=(
                    "runtime.design_builder"
                ),
                inputs=ctx.inputs,
                authorized_write=True,
                authority_witness=(
                    ctx.authority_witness
                ),
                correlation_id=(
                    ctx.correlation_id
                ),
            )
        )

    # ========================================================
    # DRIFT
    # ========================================================

    def _detect_builder_drift(
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

        drifts: List[DriftRecord] = []

        checks = [
            (
                DriftType.MODEL,
                "model_version",
            ),
            (
                DriftType.DATA,
                "source_hash",
            ),
            (
                DriftType.SCOPE,
                "scope",
            ),
            (
                DriftType.ARCHITECTURE,
                "architecture_hash",
            ),
            (
                DriftType.CONTRACT,
                "contract_hash",
            ),
            (
                DriftType.PROVENANCE,
                "provenance_hash",
            ),
            (
                DriftType.CONTEXT,
                "context_hash",
            ),
        ]

        for drift_type, key in checks:

            if (
                baseline.get(
                    key
                )
                != current.get(
                    key
                )
            ):
                drifts.append(
                    DriftRecord(
                        drift_type=drift_type,
                        description=(
                            f"{key} changed"
                        ),
                        severity=float(
                            ctx.inputs.get(
                                f"{key}_severity",
                                0.5,
                            )
                        ),
                        evidence=[
                            f"baseline={baseline.get(key)}",
                            f"current={current.get(key)}",
                        ],
                        invalidates=list(
                            ctx.inputs.get(
                                f"{key}_invalidates",
                                [],
                            )
                        ),
                        repair_required=True,
                    )
                )

        baseline_conf = float(
            baseline.get(
                "confidence",
                1.0,
            )
        )

        current_conf = float(
            current.get(
                "confidence",
                baseline_conf,
            )
        )

        if current_conf < baseline_conf:

            drifts.append(
                DriftRecord(
                    drift_type=(
                        DriftType.CONFIDENCE
                    ),
                    description=(
                        "confidence decayed"
                    ),
                    severity=min(
                        max(
                            baseline_conf
                            - current_conf,
                            0.0,
                        ),
                        1.0,
                    ),
                    evidence=[
                        (
                            f"{baseline_conf}"
                            f"->{current_conf}"
                        )
                    ],
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
                f"{len(drifts)} builder drift condition(s) detected."
            ),
            data={
                "drifts": [
                    asdict(
                        drift
                    )
                    for drift in drifts
                ],
            },
            gaps=[
                drift.description
                for drift in drifts
            ],
            provenance=self._default_provenance(),
        )

    # ========================================================
    # GAP ESCALATION
    # ========================================================

    def _escalate_builder_gaps(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        raw_gaps = ctx.inputs.get(
            "gaps",
            [],
        )

        if not isinstance(
            raw_gaps,
            list,
        ):
            raise ValidationError(
                "gaps must be a list"
            )

        gaps = [
            GapRecord(
                gap_id=str(
                    raw.get(
                        "gap_id",
                        self._new_id(
                            "gap"
                        ),
                    )
                ),
                gap_class=GapClass(
                    raw.get(
                        "gap_class",
                        "DECISION_RELEVANT",
                    )
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
                        (
                            raw.get(
                                "gap_class"
                            )
                            == "CRITICAL"
                        ),
                    )
                ),
                repair_action=raw.get(
                    "repair_action"
                ),
                confidence_impact=float(
                    raw.get(
                        "confidence_impact",
                        0.1,
                    )
                ),
            )
            for raw in raw_gaps
            if isinstance(
                raw,
                dict,
            )
        ]

        gaps.sort(
            key=lambda gap:
                self._gap_priority(
                    gap.gap_class
                )
        )

        base_confidence = (
            self._clamp_confidence(
                ctx.inputs.get(
                    "base_confidence",
                    self.claim_ceiling,
                )
            )
        )

        downgrade = sum(
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
            min(
                self.claim_ceiling,
                base_confidence - downgrade,
            ),
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
                "Builder gaps escalated and confidence downgraded."
            ),
            data={
                "ordered_gaps": [
                    asdict(
                        gap
                    )
                    for gap in gaps
                ],
                "blocking_gap_count":
                    len(
                        blocking
                    ),
                "repair_triggered":
                    bool(
                        gaps
                    ),
                "confidence_after_downgrade":
                    confidence,
            },
            gaps=[
                gap.description
                for gap in gaps
            ],
            confidence_ceiling=confidence,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # PROMOTION / STOP RULE
    # ========================================================

    def _promotion_passes(
        self,
        state: BuilderState,
    ) -> bool:

        architecture_compatible = bool(
            state.create_candidate
            and state.create_candidate.architecture
        )

        contract_compatible = bool(
            state.create_candidate
            and (
                state.create_candidate.interfaces
                or state.create_candidate.constraints
            )
        )

        hard_invariants_pass = (
            self._admit(
                state.invariants
            )
            is True
        )

        spec_pass = (
            state.observations.spec
            == TestState.SPEC_PASS
        )

        regression_pass = (
            state.observations.regression
            == TestState.REGRESSION_PASS
        )

        return all(
            (
                architecture_compatible,
                contract_compatible,
                hard_invariants_pass,
                spec_pass,
                regression_pass,
            )
        )

    def _stop_rule(
        self,
        state: BuilderState,
    ) -> Dict[str, bool]:

        claim_sufficient = bool(
            state.rscf
            and state.rscf.confidence_ceiling
            > 0
        )

        decision_sufficient = bool(
            not any(
                gap.blocking
                for gap in state.gaps
            )
        )

        action_sufficient = bool(
            state.artifacts.get(
                "package",
                {}
            ).get(
                "complete_skill_zip_present",
                False,
            )
        )

        return {
            "ClaimSufficient":
                claim_sufficient,
            "DecisionSufficient":
                decision_sufficient,
            "ActionSufficient":
                action_sufficient,
            "Stop": (
                claim_sufficient
                and decision_sufficient
                and action_sufficient
            ),
        }

    # ========================================================
    # SELECTIVE INVALIDATION
    # ========================================================

    def invalidate_claim_descendants(
        self,
        claims: Iterable[ClaimState],
        invalid_claim_id: str,
    ) -> List[str]:

        graph: Dict[
            str,
            Set[str],
        ] = {}

        for claim in claims:

            for parent in claim.dependencies:

                graph.setdefault(
                    parent,
                    set(),
                ).add(
                    claim.claim_id
                )

        visited: Set[str] = set()
        stack = [
            invalid_claim_id
        ]

        while stack:

            parent = stack.pop()

            for child in graph.get(
                parent,
                set(),
            ):

                if child in visited:
                    continue

                visited.add(
                    child
                )

                stack.append(
                    child
                )

        return sorted(
            visited
        )

    # ========================================================
    # QUANTITATIVE DISCIPLINE
    # ========================================================

    @staticmethod
    def speedup_latency(
        baseline_latency: float,
        test_latency: float,
    ) -> float:

        if test_latency <= 0:
            raise ValidationError(
                "test_latency must be > 0"
            )

        return (
            baseline_latency
            / test_latency
        )

    @staticmethod
    def throughput_gain(
        baseline_throughput: float,
        test_throughput: float,
    ) -> float:

        if baseline_throughput <= 0:
            raise ValidationError(
                "baseline_throughput must be > 0"
            )

        return (
            test_throughput
            / baseline_throughput
        )

    @staticmethod
    def compression_ratio(
        baseline_tokens: float,
        test_tokens: float,
    ) -> float:

        if test_tokens <= 0:
            raise ValidationError(
                "test_tokens must be > 0"
            )

        return (
            baseline_tokens
            / test_tokens
        )

    @staticmethod
    def repair_gain(
        global_cost: float,
        local_cost: float,
    ) -> float:

        if local_cost <= 0:
            raise ValidationError(
                "local_cost must be > 0"
            )

        return (
            global_cost
            / local_cost
        )

    # ========================================================
    # INTERNAL HELPERS
    # ========================================================

    def _admit(
        self,
        invariants: List[HardInvariant],
    ) -> Optional[bool]:
        """
        Admit(x) = AND_i I_i(x)

        Returns:
            True  => all hard invariants pass
            False => at least one fails
            None  => unresolved hard invariant
        """

        if any(
            invariant.passed is False
            for invariant in invariants
        ):
            return False

        if any(
            invariant.passed is None
            for invariant in invariants
        ):
            return None

        return True

    def _confidence_ceiling(
        self,
        premises: Dict[str, float],
    ) -> float:
        """
        Conf(C) <= min_i Conf(P_i)
        """

        if not premises:
            return min(
                0.50,
                self.claim_ceiling,
            )

        return min(
            min(
                self._clamp_confidence(
                    value
                )
                for value
                in premises.values()
            ),
            self.claim_ceiling,
        )

    def _state_confidence(
        self,
        state: BuilderState,
    ) -> float:

        if state.rscf:
            confidence = (
                state.rscf
                .confidence_ceiling
            )
        else:
            confidence = min(
                0.50,
                self.claim_ceiling,
            )

        penalty = sum(
            gap.confidence_impact
            for gap in state.gaps
            if gap.blocking
        )

        return max(
            0.0,
            min(
                self.claim_ceiling,
                confidence - penalty,
            ),
        )

    @staticmethod
    def _gap_priority(
        gap_class: GapClass,
    ) -> int:

        order = {
            GapClass.CRITICAL: 0,
            GapClass.DECISION_RELEVANT: 1,
            GapClass.EXPLANATORY: 2,
            GapClass.COSMETIC: 3,
        }

        return order[
            gap_class
        ]

    def _checkpoint_from_dict(
        self,
        raw: Dict[str, Any],
    ) -> BuilderCheckpoint:

        payload = json.dumps(
            raw,
            sort_keys=True,
            default=str,
        ).encode()

        state_hash = hashlib.sha256(
            payload
        ).hexdigest()

        return BuilderCheckpoint(
            checkpoint_id=self._new_id(
                "checkpoint"
            ),
            lifecycle_state=(
                LifecycleState.CHECKPOINTED
            ),
            current_stage=(
                BuilderStage(
                    raw["current_stage"]
                )
                if raw.get(
                    "current_stage"
                )
                else None
            ),
            objective=str(
                raw.get(
                    "objective",
                    "",
                )
            ),
            target_skill=raw.get(
                "target_skill"
            ),
            stages={},
            context_map=[],
            claims=[],
            gaps=[],
            drifts=[],
            artifacts=dict(
                raw.get(
                    "artifacts",
                    {},
                )
            ),
            provenance=self._parse_provenance(
                raw.get(
                    "provenance",
                    [],
                )
            ),
            created_at=time.time(),
            state_hash=state_hash,
        )

    def _serialize_state(
        self,
        state: BuilderState,
    ) -> Dict[str, Any]:

        return asdict(
            state
        )

    def _stage_for_fn(
        self,
        fn: Callable,
    ) -> BuilderStage:

        mapping = {
            self._stage_orient:
                BuilderStage.ORIENT,

            self._stage_read:
                BuilderStage.READ,

            self._stage_parse:
                BuilderStage.PARSE,

            self._stage_type:
                BuilderStage.TYPE,

            self._stage_understand:
                BuilderStage.UNDERSTAND,

            self._stage_model:
                BuilderStage.MODEL,

            self._stage_plan:
                BuilderStage.PLAN,

            self._stage_create:
                BuilderStage.CREATE,

            self._stage_execute:
                BuilderStage.EXECUTE,

            self._stage_observe:
                BuilderStage.OBSERVE,

            self._stage_verify:
                BuilderStage.VERIFY,

            self._stage_challenge:
                BuilderStage.CHALLENGE,

            self._stage_repair:
                BuilderStage.REPAIR,

            self._stage_compress:
                BuilderStage.COMPRESS,

            self._stage_package:
                BuilderStage.PACKAGE,
        }

        return mapping[
            fn
        ]

    def _parse_test_state(
        self,
        raw: Any,
    ) -> TestState:

        try:
            return TestState(
                str(
                    raw
                )
            )
        except ValueError as exc:
            raise ValidationError(
                f"invalid test state: {raw}"
            ) from exc

    def _parse_epistemic(
        self,
        raw: Any,
    ) -> EpistemicClass:

        try:
            return EpistemicClass(
                str(
                    raw
                )
            )
        except ValueError:
            return EpistemicClass.UNKNOWN

    def _clamp_confidence(
        self,
        value: Any,
    ) -> float:

        return min(
            max(
                float(value),
                0.0,
            ),
            self.claim_ceiling,
        )

    @staticmethod
    def _hash_json(
        value: Any,
    ) -> str:

        raw = json.dumps(
            value,
            sort_keys=True,
            default=str,
        ).encode()

        return hashlib.sha256(
            raw
        ).hexdigest()

    @staticmethod
    def _new_id(
        prefix: str,
    ) -> str:

        return (
            f"{prefix}-"
            f"{uuid.uuid4().hex[:12]}"
        )

    @staticmethod
    def _parse_provenance(
        raw: Any,
    ) -> List[ProvenanceRef]:

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
                    path=item.get(
                        "path"
                    ),
                    content_hash=item.get(
                        "content_hash"
                    ),
                    claim_id=item.get(
                        "claim_id"
                    ),
                    version=item.get(
                        "version"
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
                    "AMOS Skill Builder"
                ),
                path=(
                    PRIMARY_SKILL_PATH
                ),
                content_hash=(
                    AGENT_CONFIG[
                        "content_hash"
                    ]
                ),
            )
        ]


# ============================================================
# EXAMPLE
# ============================================================

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO
    )

    agent = AmosSkillBuilderAgent(
        repo_root="."
    )

    ctx = ExecutionContext(
        query=(
            "Build a governed example AMOS Skill."
        ),
        capability="runtime.design_builder",
        authorized_write=True,
        authority_witness=(
            "steward_review:example"
        ),
        inputs={
            "objective": (
                "Build example-skill as a governed "
                "executable reasoning Skill."
            ),
            "target_skill": (
                "example-skill"
            ),

            # -----------------------------------------------
            # ORIENT
            # -----------------------------------------------

            "context_map": [
                {
                    "objective": (
                        "Build example-skill"
                    ),
                    "artifact": (
                        "example-skill"
                    ),
                    "source_location": (
                        "design-spec.md"
                    ),
                    "recovery_cost": 0.9,
                    "replay_need": True,
                    "load_bearing": True,
                }
            ],

            # -----------------------------------------------
            # READ
            # -----------------------------------------------

            "sources": [
                {
                    "source_id": "SRC-1",
                    "section": "Requirements",
                    "claim": (
                        "The Skill must validate inputs "
                        "before execution."
                    ),
                    "assumption": (
                        "Inputs follow the declared schema."
                    ),
                    "limitation": (
                        "External APIs are not available "
                        "in offline execution."
                    ),
                    "provenance_anchor": (
                        "design-spec.md#requirements"
                    ),
                }
            ],

            # -----------------------------------------------
            # PARSE
            # -----------------------------------------------

            "deterministic_parse_required": True,

            "system_state": [
                {
                    "component": (
                        "example-skill-runtime"
                    ),
                    "interface": (
                        "run(input)->result"
                    ),
                    "data_contract": (
                        "ExampleInput"
                    ),
                    "policy": (
                        "fail closed on invalid input"
                    ),
                }
            ],

            "claims": [
                {
                    "id": "C1",
                    "class": "SOURCE_CLAIM",
                    "premises": [
                        "SRC-1"
                    ],
                    "dependencies": [],
                    "scope": (
                        "example-skill"
                    ),
                    "regime": (
                        "offline"
                    ),
                    "falsifiers": [
                        (
                            "runtime accepts malformed input"
                        )
                    ],
                    "status": "OPEN",
                    "confidence": 0.92,
                }
            ],

            # -----------------------------------------------
            # TYPE
            # -----------------------------------------------

            "tensor_x": [
                {
                    "object": (
                        "example-skill"
                    ),
                    "primitive": "skill",
                    "scale": "M",
                    "time": "current",
                    "regime": "offline",
                    "observer": AGENT_ID,
                    "epistemic_class": (
                        "AMOS_MODEL"
                    ),
                    "confidence": 0.90,
                    "consequence": {
                        "risk": "low",
                    },
                }
            ],

            "tensor_h": [
                {
                    "artifact": (
                        "example-skill"
                    ),
                    "representation": (
                        "SKILL.md+references+scripts"
                    ),
                    "parser_state": "PASS",
                    "context_state": "ORIENTED",
                    "execution_state": "NOT_RUN",
                    "test_state": "NOT_RUN",
                    "invariant_state": "PASS",
                    "evidence_state": "SOURCE_BOUND",
                    "repair_state": "NONE",
                    "version": "1.0.0",
                }
            ],

            # -----------------------------------------------
            # UNDERSTAND
            # -----------------------------------------------

            "dependency_closure_covered": True,
            "load_bearing_contracts_recovered": True,
            "critical_gaps_classified": True,
            "interfaces": [
                {
                    "name": (
                        "run"
                    ),
                    "input": (
                        "ExampleInput"
                    ),
                    "output": (
                        "ExampleResult"
                    ),
                }
            ],

            # -----------------------------------------------
            # MODEL
            # -----------------------------------------------

            "hard_invariants": [
                {
                    "invariant_id": (
                        "I_INPUT_VALIDATION"
                    ),
                    "description": (
                        "Malformed input must fail closed."
                    ),
                    "passed": True,
                    "evidence": [
                        "schema test"
                    ],
                },
                {
                    "invariant_id": (
                        "I_NO_FABRICATION"
                    ),
                    "description": (
                        "No invented evidence or execution."
                    ),
                    "passed": True,
                    "evidence": [
                        "runtime policy"
                    ],
                },
            ],

            # -----------------------------------------------
            # PLAN
            # -----------------------------------------------

            "plan_actions": [
                {
                    "action_id": "P1",
                    "description": (
                        "Implement deterministic validator."
                    ),
                    "impact": 1.0,
                    "uncertainty_reduction": 0.9,
                    "dependency_fanout": 3,
                    "cost": 1.0,
                    "required": True,
                },
                {
                    "action_id": "P2",
                    "description": (
                        "Write documentation."
                    ),
                    "impact": 0.5,
                    "uncertainty_reduction": 0.3,
                    "dependency_fanout": 1,
                    "cost": 1.0,
                },
            ],

            # -----------------------------------------------
            # CREATE
            # -----------------------------------------------

            "create_candidate": {
                "intent": (
                    "Build example-skill"
                ),
                "architecture": {
                    "runtime": (
                        "SKILL.md"
                    ),
                    "validator": (
                        "scripts/validate.py"
                    ),
                },
                "interfaces": [
                    {
                        "name": (
                            "run"
                        ),
                    }
                ],
                "constraints": [
                    (
                        "fail closed on invalid input"
                    )
                ],
                "evidence": [
                    "SRC-1"
                ],
                "tests": [
                    (
                        "invalid input rejected"
                    )
                ],
                "change_boundary": [
                    (
                        ".devin/skills/example-skill/"
                    )
                ],
            },

            # -----------------------------------------------
            # EXECUTE
            # -----------------------------------------------

            "execution_required": True,

            "execution_records": [
                {
                    "command": (
                        "python scripts/validate.py"
                    ),
                    "cwd": (
                        ".devin/skills/example-skill"
                    ),
                    "environment": {
                        "python": "3.x"
                    },
                    "input_hash": (
                        "input-hash-example"
                    ),
                    "exit_code": 0,
                    "stdout_hash": (
                        "stdout-hash"
                    ),
                    "stderr_hash": (
                        "stderr-hash"
                    ),
                    "duration": 0.4,
                    "timeout": 30,
                    "artifact_hash": (
                        "artifact-hash"
                    ),
                    "parent_run": None,
                    "test_state": (
                        "EXECUTION_PASS"
                    ),
                    "executed": True,
                    "observation": (
                        "validator completed successfully"
                    ),
                }
            ],

            # -----------------------------------------------
            # OBSERVE
            # -----------------------------------------------

            "observation_state": {
                "syntax": (
                    "SYNTAX_PASS"
                ),
                "static": (
                    "STATIC_PASS"
                ),
                "execution": (
                    "EXECUTION_PASS"
                ),
                "tests": (
                    "TEST_PASS"
                ),
                "spec": (
                    "SPEC_PASS"
                ),
                "system": (
                    "SYSTEM_PASS"
                ),
                "regression": (
                    "REGRESSION_PASS"
                ),
            },

            # -----------------------------------------------
            # VERIFY
            # -----------------------------------------------

            "premise_confidences": {
                "source-requirement": 0.92,
                "execution-evidence": 0.95,
                "spec-test": 0.94,
                "regression-test": 0.93,
            },

            "verification_claim": (
                "example-skill satisfies the "
                "declared requirements."
            ),

            "verification_evidence": [
                "execution-record-1",
                "spec-pass",
                "regression-pass",
            ],

            "verification_scope": (
                "example-skill"
            ),

            "verification_regime": (
                "offline"
            ),

            "verification_freshness": 0.95,

            "falsifiers": [
                (
                    "malformed input is accepted"
                ),
                (
                    "regression test fails"
                ),
            ],

            "competing_hypotheses": [
                {
                    "hypothesis_id": "H1",
                    "statement": (
                        "Current validator is sufficient."
                    ),
                    "confidence": 0.90,
                    "evidence": [
                        "spec pass"
                    ],
                    "falsifiers": [
                        (
                            "new invalid input bypasses validator"
                        )
                    ],
                }
            ],

            # -----------------------------------------------
            # CHALLENGE
            # -----------------------------------------------

            "challenge": {
                "parser_information_loss": False,
                "stale_context": False,
                "correlated_provenance": False,
                "hidden_dependency": False,
                "tensor_axis_mismatch": False,
                "undefined_equation_variables": False,
                "architecture_drift": False,
                "local_pass_global_fail": False,
                "benchmark_mismatch": False,
                "causal_overreach": False,
                "authority_mismatch": False,
                "storage_context_blowup": False,
                "repair_regression": False,
                "issues": [],
            },

            # -----------------------------------------------
            # COMPRESS
            # -----------------------------------------------

            "retained_decisions": [
                (
                    "validator remains deterministic"
                )
            ],

            # -----------------------------------------------
            # PACKAGE
            # -----------------------------------------------

            "package": {
                "skill_md_present": True,
                "references_present": True,
                "scripts_present": True,
                "validate_amos_skill_run": True,
                "domain_tests_run": True,
                "official_skill_creator_packaging_run": True,
                "complete_skill_zip_present": True,
                "skill_zip_path": (
                    "/tmp/example-skill.zip"
                ),
                "installation_occurred": False,
            },
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

    except SkillBuilderError as exc:

        print(
            json.dumps(
                {
                    "status": "FAILED_CLOSED",
                    "agent": AGENT_ID,
                    "error": str(exc),
                },
                indent=2,
                ensure_ascii=False,
            )
        )