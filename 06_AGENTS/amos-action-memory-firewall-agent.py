from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
import hashlib
import json
import logging
import time


# ============================================================
# AMOS ACTION MEMORY FIREWALL AGENT
# ============================================================

AGENT_ID = "amos-action-memory-firewall-agent"
AGENT_VERSION = "1.0.0"


# ============================================================
# ENUMS
# ============================================================

class ExecutionStatus(str, Enum):
    VERIFIED = "VERIFIED"
    DERIVED = "DERIVED"
    MODEL = "MODEL"
    CONDITIONAL = "CONDITIONAL"
    COMPETING = "COMPETING"
    UNKNOWN = "UNKNOWN/GAP"
    REJECTED = "REJECTED"


class MemoryDecision(str, Enum):
    ALLOW = "ALLOW"
    ALLOW_WITH_BOUNDS = "ALLOW_WITH_BOUNDS"
    REQUIRE_CURRENT_CONFIRMATION = "REQUIRE_CURRENT_CONFIRMATION"
    BLOCK_MEMORY_INFLUENCE = "BLOCK_MEMORY_INFLUENCE"
    ESCALATE = "ESCALATE"
    UNKNOWN = "UNKNOWN/GAP"


class SideEffect(str, Enum):
    READ = "read"
    WRITE = "write"


class ConsentState(str, Enum):
    EXPLICIT_CURRENT = "EXPLICIT_CURRENT"
    EXPLICIT_PERSISTENT = "EXPLICIT_PERSISTENT"
    IMPLIED = "IMPLIED"
    ABSENT = "ABSENT"
    REVOKED = "REVOKED"
    UNKNOWN = "UNKNOWN"


class ProvenanceState(str, Enum):
    ADMISSIBLE = "ADMISSIBLE"
    PARTIAL = "PARTIAL"
    UNTRUSTED = "UNTRUSTED"
    UNKNOWN = "UNKNOWN"


# ============================================================
# ERRORS
# ============================================================

class ActionMemoryFirewallError(RuntimeError):
    pass


class ValidationError(ActionMemoryFirewallError):
    pass


class AuthorizationError(ActionMemoryFirewallError):
    pass


class GapError(ActionMemoryFirewallError):
    pass


# ============================================================
# DATA CONTRACTS
# ============================================================

@dataclass(frozen=True)
class ProvenanceRef:
    source: str
    path: Optional[str] = None
    memory_id: Optional[str] = None
    content_hash: Optional[str] = None


@dataclass
class CapabilityContract:
    name: str
    description: str
    side_effect: SideEffect


@dataclass
class MemoryInfluenceRequest:
    """
    Implements the skill coupling tensor:

    A = T[
        action,
        tool,
        parameter,
        memory_id,
        memory_type,
        source_context,
        destination_context,
        personalizable,
        consent_state,
        stakes,
        irreversibility,
        provenance,
        uncertainty
    ]
    """

    action: str
    tool: Optional[str]
    parameter: str

    memory_id: str
    memory_type: str

    source_context: str
    destination_context: str

    personalizable: bool
    consent_state: ConsentState

    stakes: float
    irreversibility: float

    provenance_state: ProvenanceState
    provenance: List[ProvenanceRef] = field(default_factory=list)

    uncertainty: float = 0.0
    influence: float = 1.0

    relevant: bool = False
    context_compatible: bool = False
    role_boundary_valid: bool = False
    hard_partition_violation: bool = False


@dataclass
class ActionCapsule:
    action: str
    influenced_parameter: str

    memory_id: str
    memory_type: str
    memory_scope: str

    consent_state: ConsentState
    personalizable: bool

    provenance: List[ProvenanceRef]

    hard_gate_passed: bool
    risk_score: Optional[float]

    competing_interpretations: List[str]
    falsifiers: List[str]

    confirmation_required: bool
    rollback_path: Optional[str]

    decision: MemoryDecision
    rationale: List[str]

    confidence: float


@dataclass
class ExecutionContext:
    query: str
    capability: str
    inputs: Dict[str, Any] = field(default_factory=dict)

    authorized_write: bool = False
    authority_witness: Optional[str] = None

    correlation_id: Optional[str] = None


@dataclass
class Claim:
    text: str
    epistemic_class: str
    confidence: float
    provenance: List[ProvenanceRef] = field(default_factory=list)
    scope: Optional[str] = None
    falsifiers: List[str] = field(default_factory=list)

@dataclass
class AgentResult:
    status: ExecutionStatus
    capability: str
    summary: str

    data: Dict[str, Any] = field(default_factory=dict)

    claims: List[Claim] = field(default_factory=list)

    gaps: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    confidence_ceiling: float = 0.95
    provenance: List[ProvenanceRef] = field(default_factory=list)


# ============================================================
# CONFIG
# ============================================================

AGENT_CONFIG: Dict[str, Any] = {
    "name": AGENT_ID,
    "display_name": "Action Memory Firewall",
    "version": "1.0.0",
    "author": "Trang Phan",
    "steward": "Trang Phan",
    "system": "AMOS_OS",
    "role": (
        "Govern how persistent memory, preferences, and retrieved "
        "context may influence actions and tool parameters."
    ),
    "primary_skill": "amos-action-memory-firewall",
    "skill_path": (
        ".devin/skills/"
        "amos-action-memory-firewall/"
        "SKILL.md"
    ),
    "workflow": "amos-action-memory-firewall-workflow.md",
    "epistemic_class": "AMOS_MODEL",
    "claim_ceiling": 0.95,
    "owner_team": "AMOS_CORE",
    "business_domain": "memory",
    "risk_tier": "medium",
    "approval_mode": "steward_review",
    "promotion_state": "production",
    "content_hash": "8b9458db87f7edd8",
}


CAPABILITIES: Dict[str, CapabilityContract] = {
    "memory.execute": CapabilityContract(
        name="memory.execute",
        description=(
            "Evaluate whether memory may influence an action or "
            "parameter, and produce a governed action capsule."
        ),
        side_effect=SideEffect.WRITE,
    ),
    "memory.validate": CapabilityContract(
        name="memory.validate",
        description=(
            "Validate an Action Memory Firewall decision against "
            "hard admission gates and memory-action invariants."
        ),
        side_effect=SideEffect.READ,
    ),
    "memory.trace_provenance": CapabilityContract(
        name="memory.trace_provenance",
        description=(
            "Trace every memory-derived parameter change back to "
            "the memory source, type, context, and provenance."
        ),
        side_effect=SideEffect.READ,
    ),
    "memory.assess_claim": CapabilityContract(
        name="memory.assess_claim",
        description=(
            "Assess claims about memory influence, consent, risk, "
            "and action admissibility."
        ),
        side_effect=SideEffect.READ,
    ),
}


# ============================================================
# AGENT
# ============================================================

class AmosActionMemoryFirewallAgent:
    """
    Runtime implementation of the Action Memory Firewall.

    Core invariant:
        Memory relevance never creates execution authority.

    Hard gate:
        PermitMemoryInfluence =
            Relevant
            AND ContextCompatible
            AND ParameterPersonalizable
            AND ConsentSatisfied
            AND ProvenanceAdmissible
            AND RoleBoundaryValid
            AND NOT HardPartitionViolation

    Risk model after hard gates pass:
        R_mem->act =
            Influence * Stakes * Irreversibility * UncertaintyFactor

    The risk formula is AMOS_MODEL, not an empirical universal law.
    """

    def __init__(
        self,
        repo_root: str | Path = ".",
        claim_ceiling: float = 0.95,
    ) -> None:

        self.repo_root = Path(repo_root).resolve()

        self.skill_path = (
            self.repo_root
            / ".devin"
            / "skills"
            / "amos-action-memory-firewall"
            / "SKILL.md"
        )

        self.claim_ceiling = min(
            max(float(claim_ceiling), 0.0),
            0.95,
        )

        self.logger = logging.getLogger(AGENT_ID)

        self.handlers: Dict[
            str,
            Callable[[ExecutionContext], AgentResult],
        ] = {
            "memory.execute": self._execute_firewall,
            "memory.validate": self._validate_decision,
            "memory.trace_provenance": self._trace_provenance,
            "memory.assess_claim": self._assess_claim,
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
            or self._new_correlation_id()
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
        """
        Even memory.execute being classified as write does not mean
        the agent has authority to execute the external action itself.
        """

        if capability.side_effect != SideEffect.WRITE:
            return

        if not ctx.authorized_write:
            raise AuthorizationError(
                "memory.execute is write-classified. "
                "Capability does not imply authorization."
            )

        if not ctx.authority_witness:
            raise AuthorizationError(
                "Write-classified memory decision requires "
                "an authority_witness."
            )

    # ========================================================
    # EXECUTE FIREWALL
    # ========================================================

    def _execute_firewall(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        request = self._parse_request(
            ctx.inputs.get("request")
        )

        hard_gate, reasons = (
            self._hard_admission_gate(
                request
            )
        )

        if not hard_gate:
            capsule = ActionCapsule(
                action=request.action,
                influenced_parameter=request.parameter,
                memory_id=request.memory_id,
                memory_type=request.memory_type,
                memory_scope=(
                    f"{request.source_context}"
                    f" -> "
                    f"{request.destination_context}"
                ),
                consent_state=request.consent_state,
                personalizable=request.personalizable,
                provenance=request.provenance,
                hard_gate_passed=False,
                risk_score=None,
                competing_interpretations=[],
                falsifiers=self._default_falsifiers(),
                confirmation_required=False,
                rollback_path=None,
                decision=(
                    MemoryDecision.BLOCK_MEMORY_INFLUENCE
                ),
                rationale=reasons,
                confidence=0.95,
            )

            return AgentResult(
                status=ExecutionStatus.VERIFIED,
                capability=ctx.capability,
                summary=(
                    "Memory influence blocked by a hard "
                    "admission gate."
                ),
                data={
                    "capsule": asdict(capsule),
                    "action_authorized": False,
                    "memory_influence_permitted": False,
                },
                warnings=[
                    (
                        "Usefulness or confidence cannot override "
                        "a failed hard gate."
                    )
                ],
                confidence_ceiling=self.claim_ceiling,
                provenance=self._default_provenance(),
            )

        risk = self._calculate_risk(
            request
        )

        decision, confirmation, rationale = (
            self._decide_after_hard_gate(
                request=request,
                risk=risk,
            )
        )

        capsule = ActionCapsule(
            action=request.action,
            influenced_parameter=request.parameter,
            memory_id=request.memory_id,
            memory_type=request.memory_type,
            memory_scope=(
                f"{request.source_context}"
                f" -> "
                f"{request.destination_context}"
            ),
            consent_state=request.consent_state,
            personalizable=request.personalizable,
            provenance=request.provenance,
            hard_gate_passed=True,
            risk_score=risk,
            competing_interpretations=list(
                ctx.inputs.get(
                    "competing_interpretations",
                    [],
                )
            ),
            falsifiers=list(
                ctx.inputs.get(
                    "falsifiers",
                    self._default_falsifiers(),
                )
            ),
            confirmation_required=confirmation,
            rollback_path=ctx.inputs.get(
                "rollback_path"
            ),
            decision=decision,
            rationale=rationale,
            confidence=self._decision_confidence(
                request,
                decision,
            ),
        )

        return AgentResult(
            status=(
                ExecutionStatus.CONDITIONAL
                if confirmation
                else ExecutionStatus.VERIFIED
            ),
            capability=ctx.capability,
            summary=(
                f"Memory influence decision: "
                f"{decision.value}"
            ),
            data={
                "capsule": asdict(capsule),
                "memory_influence_permitted": (
                    decision
                    in {
                        MemoryDecision.ALLOW,
                        MemoryDecision.ALLOW_WITH_BOUNDS,
                    }
                ),
                # The firewall governs steering.
                # It does not independently authorize the world effect.
                "external_action_authorized": False,
            },
            warnings=[
                (
                    "Memory permission is not external execution "
                    "authority."
                ),
                (
                    "Risk score is AMOS_MODEL prioritization, "
                    "not an empirical universal law."
                ),
            ],
            confidence_ceiling=self.claim_ceiling,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # HARD ADMISSION EQUATION
    # ========================================================

    def _hard_admission_gate(
        self,
        request: MemoryInfluenceRequest,
    ) -> tuple[bool, List[str]]:

        reasons: List[str] = []

        if not request.relevant:
            reasons.append(
                "memory_not_relevant"
            )

        if not request.context_compatible:
            reasons.append(
                "source_destination_context_incompatible"
            )

        if not request.personalizable:
            reasons.append(
                "parameter_not_personalizable"
            )

        if not self._consent_satisfied(
            request
        ):
            reasons.append(
                "consent_not_satisfied"
            )

        if not self._provenance_admissible(
            request
        ):
            reasons.append(
                "provenance_not_admissible"
            )

        if not request.role_boundary_valid:
            reasons.append(
                "role_boundary_invalid"
            )

        if request.hard_partition_violation:
            reasons.append(
                "hard_partition_violation"
            )

        return (
            len(reasons) == 0,
            reasons,
        )

    # ========================================================
    # CONSENT
    # ========================================================

    def _consent_satisfied(
        self,
        request: MemoryInfluenceRequest,
    ) -> bool:
        """
        preference != consent

        Persistent preference alone cannot be silently interpreted
        as fresh consent for consequential action.
        """

        if request.consent_state == ConsentState.REVOKED:
            return False

        if request.consent_state == ConsentState.ABSENT:
            return False

        if request.consent_state == ConsentState.UNKNOWN:
            return False

        if request.consent_state == ConsentState.IMPLIED:
            # Keep implied consent restricted to low-stakes,
            # highly reversible cases.
            return (
                request.stakes <= 0.20
                and request.irreversibility <= 0.20
            )

        if request.consent_state == ConsentState.EXPLICIT_PERSISTENT:
            # Persistent consent is insufficient by itself when stakes
            # or irreversibility become material.
            return (
                request.stakes <= 0.50
                and request.irreversibility <= 0.50
            )

        return (
            request.consent_state
            == ConsentState.EXPLICIT_CURRENT
        )

    # ========================================================
    # PROVENANCE
    # ========================================================

    def _provenance_admissible(
        self,
        request: MemoryInfluenceRequest,
    ) -> bool:

        if (
            request.provenance_state
            != ProvenanceState.ADMISSIBLE
        ):
            return False

        return bool(
            request.provenance
        )

    # ========================================================
    # RISK MODEL
    # ========================================================

    def _calculate_risk(
        self,
        request: MemoryInfluenceRequest,
    ) -> float:
        """
        AMOS MODEL:

        R_mem->act =
            Influence
            * Stakes
            * Irreversibility
            * UncertaintyFactor
        """

        uncertainty_factor = (
            1.0
            + self._clamp01(
                request.uncertainty
            )
        )

        risk = (
            self._clamp01(
                request.influence
            )
            * self._clamp01(
                request.stakes
            )
            * self._clamp01(
                request.irreversibility
            )
            * uncertainty_factor
        )

        return min(
            risk,
            1.0,
        )

    # ========================================================
    # POST-GATE DECISION
    # ========================================================

    def _decide_after_hard_gate(
        self,
        request: MemoryInfluenceRequest,
        risk: float,
    ) -> tuple[
        MemoryDecision,
        bool,
        List[str],
    ]:

        rationale: List[str] = []

        # Invariant:
        # low-stakes memory cannot silently set high-stakes parameters.
        if (
            request.memory_type
            in {
                "preference",
                "low_stakes_preference",
            }
            and request.stakes >= 0.60
        ):
            return (
                MemoryDecision.REQUIRE_CURRENT_CONFIRMATION,
                True,
                [
                    (
                        "low_stakes_memory_cannot_silently_"
                        "set_high_stakes_parameter"
                    )
                ],
            )

        # Stricter treatment of irreversible actions.
        if request.irreversibility >= 0.75:
            return (
                MemoryDecision.REQUIRE_CURRENT_CONFIRMATION,
                True,
                [
                    "high_irreversibility_requires_current_confirmation"
                ],
            )

        if request.uncertainty >= 0.70:
            return (
                MemoryDecision.ESCALATE,
                True,
                [
                    "high_uncertainty_reduces_autonomy"
                ],
            )

        if risk >= 0.60:
            return (
                MemoryDecision.REQUIRE_CURRENT_CONFIRMATION,
                True,
                [
                    "modeled_memory_action_risk_high"
                ],
            )

        if risk >= 0.25:
            rationale.append(
                "memory_influence_allowed_only_with_bounds"
            )

            return (
                MemoryDecision.ALLOW_WITH_BOUNDS,
                False,
                rationale,
            )

        return (
            MemoryDecision.ALLOW,
            False,
            [
                "hard_gates_passed",
                "modeled_risk_below_bound",
            ],
        )

    # ========================================================
    # VALIDATION
    # ========================================================

    def _validate_decision(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        raw = ctx.inputs.get(
            "capsule"
        )

        if not isinstance(raw, dict):
            raise GapError(
                "UNKNOWN/GAP: capsule dictionary required."
            )

        issues: List[str] = []

        required = [
            "action",
            "influenced_parameter",
            "memory_id",
            "memory_type",
            "memory_scope",
            "consent_state",
            "personalizable",
            "hard_gate_passed",
            "decision",
            "rationale",
        ]

        for field_name in required:
            if field_name not in raw:
                issues.append(
                    f"missing:{field_name}"
                )

        if (
            raw.get("personalizable") is False
            and raw.get("decision")
            in {
                "ALLOW",
                "ALLOW_WITH_BOUNDS",
            }
        ):
            issues.append(
                "non_personalizable_parameter_was_memory_steered"
            )

        if (
            raw.get("hard_gate_passed") is False
            and raw.get("decision")
            not in {
                "BLOCK_MEMORY_INFLUENCE",
                "UNKNOWN/GAP",
            }
        ):
            issues.append(
                "failed_hard_gate_overridden"
            )

        if (
            raw.get("decision")
            in {
                "ALLOW",
                "ALLOW_WITH_BOUNDS",
            }
            and not raw.get("provenance")
        ):
            issues.append(
                "allowed_memory_change_missing_provenance"
            )

        return AgentResult(
            status=(
                ExecutionStatus.VERIFIED
                if not issues
                else ExecutionStatus.CONDITIONAL
            ),
            capability=ctx.capability,
            summary=(
                "Action Memory Firewall validation completed."
            ),
            data={
                "pass": not issues,
                "issues": issues,
            },
            gaps=issues,
            confidence_ceiling=self.claim_ceiling,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # TRACE PROVENANCE
    # ========================================================

    def _trace_provenance(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        changes = ctx.inputs.get(
            "memory_derived_changes"
        )

        if not isinstance(
            changes,
            list,
        ):
            raise GapError(
                "UNKNOWN/GAP: memory_derived_changes list required."
            )

        traced: List[Dict[str, Any]] = []
        gaps: List[str] = []

        for index, change in enumerate(
            changes
        ):

            if not isinstance(change, dict):
                gaps.append(
                    f"change[{index}]:invalid_record"
                )
                continue

            memory_id = change.get(
                "memory_id"
            )

            parameter = change.get(
                "parameter"
            )

            provenance = change.get(
                "provenance"
            )

            if not memory_id:
                gaps.append(
                    f"change[{index}]:missing_memory_id"
                )

            if not parameter:
                gaps.append(
                    f"change[{index}]:missing_parameter"
                )

            if not provenance:
                gaps.append(
                    f"change[{index}]:missing_provenance"
                )

            traced.append({
                "index": index,
                "memory_id": memory_id,
                "parameter": parameter,
                "source_context": change.get(
                    "source_context"
                ),
                "destination_context": change.get(
                    "destination_context"
                ),
                "provenance": provenance,
                "traceable": bool(
                    memory_id
                    and parameter
                    and provenance
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
                "Memory-action provenance trace completed."
            ),
            data={
                "changes": traced,
            },
            gaps=gaps,
            confidence_ceiling=self.claim_ceiling,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # ASSESS CLAIM
    # ========================================================

    def _assess_claim(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        claim = ctx.inputs.get(
            "claim"
        )

        if not isinstance(claim, dict):
            raise GapError(
                "UNKNOWN/GAP: claim dictionary required."
            )

        issues: List[str] = []

        if not claim.get(
            "memory_id"
        ):
            issues.append(
                "missing_memory_source"
            )

        if not claim.get(
            "scope"
        ):
            issues.append(
                "missing_scope"
            )

        if (
            claim.get(
                "preference_equals_consent"
            )
            is True
        ):
            issues.append(
                "preference_does_not_equal_consent"
            )

        if (
            claim.get(
                "memory_relevance_creates_authority"
            )
            is True
        ):
            issues.append(
                "memory_relevance_does_not_create_authority"
            )

        if (
            claim.get(
                "risk_score_empirical_law"
            )
            is True
        ):
            issues.append(
                "risk_model_is_amos_model_not_empirical_law"
            )

        return AgentResult(
            status=(
                ExecutionStatus.VERIFIED
                if not issues
                else ExecutionStatus.CONDITIONAL
            ),
            capability=ctx.capability,
            summary=(
                "Memory-action claim assessment completed."
            ),
            data={
                "issues": issues,
                "classification": (
                    "AMOS_MODEL"
                    if claim.get(
                        "uses_firewall_model",
                        True,
                    )
                    else "DERIVED"
                ),
            },
            gaps=issues,
            confidence_ceiling=self.claim_ceiling,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # PARSER
    # ========================================================

    def _parse_request(
        self,
        raw: Any,
    ) -> MemoryInfluenceRequest:

        if not isinstance(raw, dict):
            raise GapError(
                "UNKNOWN/GAP: request dictionary required."
            )

        required = [
            "action",
            "parameter",
            "memory_id",
            "memory_type",
            "source_context",
            "destination_context",
        ]

        missing = [
            field_name
            for field_name in required
            if not raw.get(field_name)
        ]

        if missing:
            raise GapError(
                "UNKNOWN/GAP: missing request fields: "
                + ", ".join(missing)
            )

        try:
            consent_state = ConsentState(
                raw.get(
                    "consent_state",
                    "UNKNOWN",
                )
            )
        except ValueError as exc:
            raise ValidationError(
                "invalid consent_state"
            ) from exc

        try:
            provenance_state = ProvenanceState(
                raw.get(
                    "provenance_state",
                    "UNKNOWN",
                )
            )
        except ValueError as exc:
            raise ValidationError(
                "invalid provenance_state"
            ) from exc

        provenance: List[ProvenanceRef] = []

        for item in raw.get(
            "provenance",
            [],
        ):
            if isinstance(item, dict):
                provenance.append(
                    ProvenanceRef(
                        source=str(
                            item.get(
                                "source",
                                "",
                            )
                        ),
                        path=item.get("path"),
                        memory_id=item.get(
                            "memory_id",
                            raw["memory_id"],
                        ),
                        content_hash=item.get(
                            "content_hash"
                        ),
                    )
                )

        return MemoryInfluenceRequest(
            action=str(raw["action"]),
            tool=raw.get("tool"),
            parameter=str(raw["parameter"]),
            memory_id=str(raw["memory_id"]),
            memory_type=str(raw["memory_type"]),
            source_context=str(
                raw["source_context"]
            ),
            destination_context=str(
                raw["destination_context"]
            ),
            personalizable=bool(
                raw.get(
                    "personalizable",
                    False,
                )
            ),
            consent_state=consent_state,
            stakes=self._clamp01(
                float(
                    raw.get(
                        "stakes",
                        0.0,
                    )
                )
            ),
            irreversibility=self._clamp01(
                float(
                    raw.get(
                        "irreversibility",
                        0.0,
                    )
                )
            ),
            provenance_state=provenance_state,
            provenance=provenance,
            uncertainty=self._clamp01(
                float(
                    raw.get(
                        "uncertainty",
                        0.0,
                    )
                )
            ),
            influence=self._clamp01(
                float(
                    raw.get(
                        "influence",
                        1.0,
                    )
                )
            ),
            relevant=bool(
                raw.get(
                    "relevant",
                    False,
                )
            ),
            context_compatible=bool(
                raw.get(
                    "context_compatible",
                    False,
                )
            ),
            role_boundary_valid=bool(
                raw.get(
                    "role_boundary_valid",
                    False,
                )
            ),
            hard_partition_violation=bool(
                raw.get(
                    "hard_partition_violation",
                    False,
                )
            ),
        )

    # ========================================================
    # CONFIDENCE / FALSIFIERS
    # ========================================================

    def _decision_confidence(
        self,
        request: MemoryInfluenceRequest,
        decision: MemoryDecision,
    ) -> float:

        confidence = self.claim_ceiling

        confidence = min(
            confidence,
            1.0 - (
                request.uncertainty * 0.5
            ),
        )

        if (
            request.provenance_state
            != ProvenanceState.ADMISSIBLE
        ):
            confidence = min(
                confidence,
                0.50,
            )

        if decision in {
            MemoryDecision.ESCALATE,
            MemoryDecision.UNKNOWN,
        }:
            confidence = min(
                confidence,
                0.60,
            )

        return max(
            0.0,
            confidence,
        )

    @staticmethod
    def _default_falsifiers() -> List[str]:

        return [
            "memory provenance becomes stale or invalid",
            "consent is revoked or scope changes",
            "parameter is reclassified as non-personalizable",
            "source/destination context becomes incompatible",
            "stakes or irreversibility materially increase",
            "role boundary changes",
            "hard partition violation is discovered",
        ]

    # ========================================================
    # DEFAULT PROVENANCE
    # ========================================================

    def _default_provenance(
        self,
    ) -> List[ProvenanceRef]:

        return [
            ProvenanceRef(
                source=(
                    "AMOS Action Memory Firewall "
                    "source skill"
                ),
                path=(
                    ".devin/skills/"
                    "amos-action-memory-firewall/"
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
    def _clamp01(
        value: float,
    ) -> float:

        return max(
            0.0,
            min(
                1.0,
                float(value),
            ),
        )

    @staticmethod
    def _new_correlation_id() -> str:

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

        return asdict(result)


# ============================================================
# EXAMPLE
# ============================================================

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO
    )

    agent = AmosActionMemoryFirewallAgent(
        repo_root="."
    )

    ctx = ExecutionContext(
        query=(
            "Can stored user preference memory "
            "set this tool parameter?"
        ),
        capability="memory.execute",
        authorized_write=True,
        authority_witness=(
            "steward_review:example"
        ),
        inputs={
            "request": {
                "action": "create_report",
                "tool": "report_generator",
                "parameter": "preferred_format",
                "memory_id": "mem-001",
                "memory_type": "preference",
                "source_context": "user_preferences",
                "destination_context": "report_generation",
                "personalizable": True,
                "consent_state": "EXPLICIT_PERSISTENT",
                "stakes": 0.10,
                "irreversibility": 0.05,
                "provenance_state": "ADMISSIBLE",
                "provenance": [
                    {
                        "source": "user_explicit_preference",
                        "memory_id": "mem-001",
                        "content_hash": "examplehash",
                    }
                ],
                "uncertainty": 0.05,
                "influence": 1.0,
                "relevant": True,
                "context_compatible": True,
                "role_boundary_valid": True,
                "hard_partition_violation": False,
            },
            "rollback_path": (
                "restore default report format"
            ),
        },
    )

    try:

        result = agent.run(ctx)

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

    except ActionMemoryFirewallError as exc:

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