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
# AMOS AGENCY CONSEQUENCE GOVERNOR AGENT
# ============================================================

AGENT_ID = "amos-agency-consequence-governor-agent"
AGENT_VERSION = "1.0.0"


# ============================================================
# ENUMS
# ============================================================

class EpistemicClass(str, Enum):
    SOURCE_DEFINED = "SOURCE_DEFINED"
    SOURCE = "SOURCE"
    DERIVED = "DERIVED"
    AMOS_MODEL = "AMOS_MODEL"
    EMPIRICAL = "EMPIRICAL"
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


class InvariantStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNKNOWN = "UNKNOWN"


class SideEffect(str, Enum):
    READ = "read"
    WRITE = "write"


class AgencyDecision(str, Enum):
    ALLOW = "ALLOW"
    ALLOW_WITH_BOUNDS = "ALLOW_WITH_BOUNDS"
    REQUIRE_APPROVAL = "REQUIRE_APPROVAL"
    ESCALATE = "ESCALATE"
    BLOCK = "BLOCK"
    UNKNOWN = "UNKNOWN/GAP"


class EquationType(str, Enum):
    SOURCE_DEFINED = "SOURCE_DEFINED"
    AMOS_MODEL = "AMOS_MODEL"
    DERIVED = "DERIVED"
    EMPIRICAL = "EMPIRICAL"
    UNVERIFIED = "UNVERIFIED"


# ============================================================
# ERRORS
# ============================================================

class AgencyConsequenceError(RuntimeError):
    pass


class ValidationError(AgencyConsequenceError):
    pass


class AuthorizationError(AgencyConsequenceError):
    pass


class GapError(AgencyConsequenceError):
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
class TensorCell:
    """
    Generic typed cell for agency/consequence state.

    H/M/L meaning is preserved by the caller's axis labels rather than
    inventing unsupported source-specific tensor dimensions.
    """

    cell_id: str
    level: str  # H | M | L
    axis: str
    value: Any
    epistemic_class: EpistemicClass
    confidence: float
    timestamp: Optional[str] = None
    provenance: List[ProvenanceRef] = field(default_factory=list)


@dataclass
class EquationRecord:
    equation_id: str
    expression: str
    equation_type: EquationType
    terms: Dict[str, Any] = field(default_factory=dict)
    assumptions: List[str] = field(default_factory=list)
    falsifiers: List[str] = field(default_factory=list)
    provenance: List[ProvenanceRef] = field(default_factory=list)


@dataclass
class Hypothesis:
    hypothesis_id: str
    statement: str
    epistemic_class: EpistemicClass
    confidence: float
    supporting_evidence: List[str] = field(default_factory=list)
    conflicting_evidence: List[str] = field(default_factory=list)
    falsifiers: List[str] = field(default_factory=list)


@dataclass
class ConsequenceState:
    """
    Bounded consequence representation.

    These dimensions are operational AMOS_MODEL fields, not claimed
    universal empirical quantities.
    """

    stakes: float
    irreversibility: float
    blast_radius: float
    persistence: float
    uncertainty: float

    def risk_score(self) -> float:
        """
        AMOS_MODEL prioritization score.

        No claim is made that this is an externally established
        empirical risk equation.
        """
        return _clamp01(
            (
                _clamp01(self.stakes)
                + _clamp01(self.irreversibility)
                + _clamp01(self.blast_radius)
                + _clamp01(self.persistence)
                + _clamp01(self.uncertainty)
            )
            / 5.0
        )


@dataclass
class AgencyState:
    perception_available: bool
    option_space_available: bool
    permission_present: bool
    execution_capacity_present: bool
    consequence_tracking_present: bool

    def structurally_complete(self) -> bool:
        return all(
            (
                self.perception_available,
                self.option_space_available,
                self.permission_present,
                self.execution_capacity_present,
                self.consequence_tracking_present,
            )
        )


@dataclass
class RSCFCapsule:
    claim: str
    epistemic_class: EpistemicClass
    scope: str

    premises: Dict[str, float]
    dependencies: List[str]

    provenance: List[ProvenanceRef]
    competing_hypotheses: List[Hypothesis]

    falsifiers: List[str]
    confidence_ceiling: float

    decision: AgencyDecision
    repair_path: Optional[str] = None
    rollback_path: Optional[str] = None


@dataclass
class DependencyGraph:
    descendants: Dict[str, Set[str]] = field(default_factory=dict)

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
    inputs: Dict[str, Any] = field(default_factory=dict)

    # Write classification does not confer authority.
    authorized_write: bool = False
    authority_witness: Optional[str] = None

    correlation_id: Optional[str] = None


@dataclass
class Claim:
    text: str
    epistemic_class: "EpistemicClass"
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
    "display_name": "Agency Consequence Governor",
    "description": (
        "AMOS Agency & Consequence Governor — governs bounded agency "
        "through source identity, scope, invariants, permissions, "
        "consequence, RSCF dependencies, competing hypotheses, "
        "provenance, validation, and repair."
    ),
    "version": AGENT_VERSION,
    "author": "Trang Phan",
    "steward": "Trang Phan",
    "system": "AMOS_OS",
    "role": (
        "Govern agency as bounded action capacity with explicit "
        "permission and consequence tracking."
    ),
    "primary_skill": "amos-agency-consequence-governor",
    "skill_path": (
        ".devin/skills/"
        "amos-agency-consequence-governor/"
        "SKILL.md"
    ),
    "workflow": (
        "amos-agency-consequence-governor-workflow.md"
    ),
    "epistemic_class": "AMOS_MODEL",
    "claim_ceiling": 0.95,
    "owner_team": "AMOS_CORE",
    "business_domain": "agent",
    "risk_tier": "medium",
    "observability": "structured_logs+content_hash",
    "approval_mode": "steward_review",
    "promotion_state": "production",
    "content_hash": "fb3874d8cc9eb283",
}


CAPABILITIES: Dict[str, CapabilityContract] = {
    "agent.execute": CapabilityContract(
        name="agent.execute",
        description=(
            "Evaluate a proposed agent action through agency completeness, "
            "hard invariants, consequence, permissions, provenance, "
            "COMPETING hypotheses, and RSCF governance."
        ),
        side_effect=SideEffect.WRITE,
    ),
    "agent.validate": CapabilityContract(
        name="agent.validate",
        description=(
            "Validate Agency Consequence Governor output against hard "
            "invariants, confidence ceilings, authority boundaries, "
            "H/M/L structure, and consequence requirements."
        ),
        side_effect=SideEffect.READ,
    ),
    "agent.trace_provenance": CapabilityContract(
        name="agent.trace_provenance",
        description=(
            "Trace agency state, consequence claims, equations, tensor "
            "cells, hypotheses, and decisions to their source evidence."
        ),
        side_effect=SideEffect.READ,
    ),
    "agent.assess_claim": CapabilityContract(
        name="agent.assess_claim",
        description=(
            "Assess agency or consequence claims for epistemic class, "
            "evidence strength, authority scope, and regime validity."
        ),
        side_effect=SideEffect.READ,
    ),
}


# ============================================================
# MAIN AGENT
# ============================================================

class AmosAgencyConsequenceGovernorAgent:
    """
    Runtime adapter for amos-agency-consequence-governor.

    Source-bound rules:

        Admit(x) = AND_i HardInvariant_i(x)

        Conf(C) <= min_i Conf(P_i)

        Invalid(p) => invalidate(descendants(p))

    H:
        source identity, scope, hard invariants,
        governance, consequence

    M:
        typed tensor state, RSCF dependency graph,
        COMPETING hypotheses, validation, repair

    L:
        equation terms, tensor cells, timestamps,
        parameters, falsifiers, implementation mappings

    Important:
    - hard failures are non-compensatory;
    - missing load-bearing evidence => UNKNOWN/GAP;
    - preserve COMPETING;
    - SOURCE_DEFINED equations are framework canon and are not
      automatically externally validated empirical laws;
    - capability does not imply permission or authority.
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
            / "amos-agency-consequence-governor"
            / "SKILL.md"
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
            "agent.execute": self._execute_governance,
            "agent.validate": self._validate_output,
            "agent.trace_provenance": self._trace_provenance,
            "agent.assess_claim": self._assess_claim,
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
        self._validate_context(ctx)

        capability = CAPABILITIES.get(
            ctx.capability
        )

        if capability is None:
            raise ValidationError(
                f"Unsupported capability: {ctx.capability}"
            )

        self._check_execution_authority(
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

    def _check_execution_authority(
        self,
        capability: CapabilityContract,
        ctx: ExecutionContext,
    ) -> None:

        if capability.side_effect != SideEffect.WRITE:
            return

        if not ctx.authorized_write:
            raise AuthorizationError(
                f"{capability.name} is write-classified. "
                "Capability does not imply authority."
            )

        if not ctx.authority_witness:
            raise AuthorizationError(
                "Write-classified governance operation requires "
                "an authority_witness."
            )

    # ========================================================
    # EXECUTE
    # ========================================================

    def _execute_governance(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        target = ctx.inputs.get(
            "target"
        )

        action = ctx.inputs.get(
            "action"
        )

        if not target:
            raise GapError(
                "UNKNOWN/GAP: target is required."
            )

        if not action:
            raise GapError(
                "UNKNOWN/GAP: proposed action is required."
            )

        # ----------------------------------------------------
        # H — identity, scope, governance, invariants, consequence
        # ----------------------------------------------------

        h_state = {
            "source_identity": ctx.inputs.get(
                "source_identity"
            ),
            "target": target,
            "scope": ctx.inputs.get(
                "scope",
                str(target),
            ),
            "governance": ctx.inputs.get(
                "governance",
                {},
            ),
            "proposed_action": action,
        }

        invariants = self._parse_invariants(
            ctx.inputs.get(
                "hard_invariants",
                [],
            )
        )

        agency_state = self._parse_agency_state(
            ctx.inputs.get(
                "agency_state",
                {},
            )
        )

        consequence = self._parse_consequence(
            ctx.inputs.get(
                "consequence",
                {},
            )
        )

        h_state["agency"] = asdict(
            agency_state
        )

        h_state["consequence"] = asdict(
            consequence
        )

        # ----------------------------------------------------
        # HARD GATE
        # ----------------------------------------------------

        admission = self._admit(
            invariants
        )

        if admission["status"] == InvariantStatus.FAIL:

            return AgentResult(
                status=ExecutionStatus.REJECTED,
                capability=ctx.capability,
                summary=(
                    "Proposed agency operation rejected because "
                    "a hard invariant failed."
                ),
                data={
                    "H": {
                        **h_state,
                        "invariants": [
                            asdict(i)
                            for i in invariants
                        ],
                    },
                    "decision": AgencyDecision.BLOCK.value,
                    "admission": self._serialize_admission(
                        admission
                    ),
                    "world_effect_committed": False,
                },
                gaps=[
                    i.reason or i.description
                    for i in invariants
                    if i.status == InvariantStatus.FAIL
                ],
                warnings=[
                    "Hard invariant failures are non-compensatory."
                ],
                confidence_ceiling=self.claim_ceiling,
                provenance=self._default_provenance(),
            )

        if admission["status"] == InvariantStatus.UNKNOWN:

            return AgentResult(
                status=ExecutionStatus.UNKNOWN,
                capability=ctx.capability,
                summary=(
                    "Agency decision is UNKNOWN/GAP because a "
                    "load-bearing invariant is unresolved."
                ),
                data={
                    "H": {
                        **h_state,
                        "invariants": [
                            asdict(i)
                            for i in invariants
                        ],
                    },
                    "decision": AgencyDecision.UNKNOWN.value,
                    "admission": self._serialize_admission(
                        admission
                    ),
                    "world_effect_committed": False,
                },
                gaps=[
                    i.reason or i.description
                    for i in invariants
                    if i.status == InvariantStatus.UNKNOWN
                ],
                confidence_ceiling=min(
                    0.50,
                    self.claim_ceiling,
                ),
                provenance=self._default_provenance(),
            )

        # ----------------------------------------------------
        # Agency completeness
        # ----------------------------------------------------

        if not agency_state.structurally_complete():

            missing = self._missing_agency_dimensions(
                agency_state
            )

            return AgentResult(
                status=ExecutionStatus.CONDITIONAL,
                capability=ctx.capability,
                summary=(
                    "Agency operation is incomplete: one or more "
                    "agency dimensions are unavailable."
                ),
                data={
                    "H": {
                        **h_state,
                        "invariants": [
                            asdict(i)
                            for i in invariants
                        ],
                    },
                    "decision": (
                        AgencyDecision.REQUIRE_APPROVAL.value
                        if "permission_present" in missing
                        else AgencyDecision.ESCALATE.value
                    ),
                    "missing_agency_dimensions": missing,
                    "world_effect_committed": False,
                },
                gaps=missing,
                warnings=[
                    (
                        "Apparent capability is not equivalent to "
                        "bounded authorized agency."
                    )
                ],
                confidence_ceiling=min(
                    0.70,
                    self.claim_ceiling,
                ),
                provenance=self._default_provenance(),
            )

        # ----------------------------------------------------
        # M — tensor / hypotheses / RSCF / dependency graph
        # ----------------------------------------------------

        hypotheses = self._parse_hypotheses(
            ctx.inputs.get(
                "hypotheses",
                [],
            )
        )

        hypothesis_state = self._hypothesis_state(
            hypotheses
        )

        dependency_graph = self._build_dependency_graph(
            ctx.inputs.get(
                "dependencies",
                [],
            )
        )

        # ----------------------------------------------------
        # L — equations / tensor cells / timestamps / falsifiers
        # ----------------------------------------------------

        tensor_cells = self._parse_tensor_cells(
            ctx.inputs.get(
                "tensor_cells",
                [],
            )
        )

        equations = self._parse_equations(
            ctx.inputs.get(
                "equations",
                [],
            )
        )

        # ----------------------------------------------------
        # Confidence ceiling
        # ----------------------------------------------------

        premise_confidences = {
            str(key): _clamp01(value)
            for key, value in ctx.inputs.get(
                "premise_confidences",
                {},
            ).items()
        }

        confidence = self._confidence_ceiling(
            premise_confidences
        )

        # ----------------------------------------------------
        # Consequence-aware bounded decision
        # ----------------------------------------------------

        decision = self._consequence_decision(
            consequence=consequence,
            hypothesis_state=hypothesis_state,
            current_authority_present=(
                agency_state.permission_present
            ),
        )

        discriminating_test = (
            self._cheapest_discriminating_test(
                hypotheses
            )
        )

        rscf = RSCFCapsule(
            claim=str(
                ctx.inputs.get(
                    "claim",
                    (
                        "Proposed agent action is admissible "
                        "only within bounded agency and consequence."
                    ),
                )
            ),
            epistemic_class=EpistemicClass.AMOS_MODEL,
            scope=str(
                h_state["scope"]
            ),
            premises=premise_confidences,
            dependencies=list(
                ctx.inputs.get(
                    "dependency_ids",
                    [],
                )
            ),
            provenance=self._default_provenance(),
            competing_hypotheses=hypotheses,
            falsifiers=list(
                ctx.inputs.get(
                    "falsifiers",
                    [],
                )
            ),
            confidence_ceiling=confidence,
            decision=decision,
            repair_path=ctx.inputs.get(
                "repair_path"
            ),
            rollback_path=ctx.inputs.get(
                "rollback_path"
            ),
        )

        if hypothesis_state == "COMPETING":
            status = ExecutionStatus.COMPETING
        elif decision in {
            AgencyDecision.REQUIRE_APPROVAL,
            AgencyDecision.ALLOW_WITH_BOUNDS,
            AgencyDecision.ESCALATE,
        }:
            status = ExecutionStatus.CONDITIONAL
        else:
            status = ExecutionStatus.MODEL

        return AgentResult(
            status=status,
            capability=ctx.capability,
            summary=(
                f"Agency governance decision: {decision.value}. "
                f"Modeled consequence risk: "
                f"{consequence.risk_score():.2f}."
            ),
            data={
                "conclusion_class": (
                    "AMOS_MODEL"
                ),
                "scope": h_state["scope"],
                "H": {
                    **h_state,
                    "invariants": [
                        asdict(i)
                        for i in invariants
                    ],
                    "admission": self._serialize_admission(
                        admission
                    ),
                },
                "M": {
                    "hypotheses": [
                        asdict(h)
                        for h in hypotheses
                    ],
                    "hypothesis_state": hypothesis_state,
                    "dependency_graph": {
                        parent: sorted(
                            list(children)
                        )
                        for parent, children
                        in dependency_graph.descendants.items()
                    },
                    "rscf": asdict(rscf),
                },
                "L": {
                    "tensor_slice": [
                        asdict(cell)
                        for cell in tensor_cells
                    ],
                    "equations": [
                        asdict(eq)
                        for eq in equations
                    ],
                    "falsifiers": list(
                        ctx.inputs.get(
                            "falsifiers",
                            [],
                        )
                    ),
                    "implementation_mapping": (
                        ctx.inputs.get(
                            "implementation_mapping",
                            {},
                        )
                    ),
                },
                "decision": decision.value,
                "cheapest_discriminating_test": (
                    discriminating_test
                ),
                "world_effect_committed": False,
            },
            warnings=[
                (
                    "Agency modeling does not independently authorize "
                    "the proposed external or durable action."
                ),
                (
                    "SOURCE_DEFINED equations remain framework canon "
                    "unless independently externally validated."
                ),
                (
                    "Consequence scoring is AMOS_MODEL unless separately "
                    "calibrated in the target environment."
                ),
            ],
            confidence_ceiling=confidence,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # AGENCY
    # ========================================================

    def _parse_agency_state(
        self,
        raw: Any,
    ) -> AgencyState:

        if not isinstance(raw, dict):
            raise ValidationError(
                "agency_state must be a dictionary"
            )

        return AgencyState(
            perception_available=bool(
                raw.get(
                    "perception_available",
                    False,
                )
            ),
            option_space_available=bool(
                raw.get(
                    "option_space_available",
                    False,
                )
            ),
            permission_present=bool(
                raw.get(
                    "permission_present",
                    False,
                )
            ),
            execution_capacity_present=bool(
                raw.get(
                    "execution_capacity_present",
                    False,
                )
            ),
            consequence_tracking_present=bool(
                raw.get(
                    "consequence_tracking_present",
                    False,
                )
            ),
        )

    def _missing_agency_dimensions(
        self,
        state: AgencyState,
    ) -> List[str]:

        missing: List[str] = []

        for key, value in asdict(
            state
        ).items():
            if value is not True:
                missing.append(key)

        return missing

    # ========================================================
    # CONSEQUENCE
    # ========================================================

    def _parse_consequence(
        self,
        raw: Any,
    ) -> ConsequenceState:

        if not isinstance(raw, dict):
            raise ValidationError(
                "consequence must be a dictionary"
            )

        return ConsequenceState(
            stakes=_clamp01(
                raw.get(
                    "stakes",
                    0.0,
                )
            ),
            irreversibility=_clamp01(
                raw.get(
                    "irreversibility",
                    0.0,
                )
            ),
            blast_radius=_clamp01(
                raw.get(
                    "blast_radius",
                    0.0,
                )
            ),
            persistence=_clamp01(
                raw.get(
                    "persistence",
                    0.0,
                )
            ),
            uncertainty=_clamp01(
                raw.get(
                    "uncertainty",
                    0.0,
                )
            ),
        )

    def _consequence_decision(
        self,
        consequence: ConsequenceState,
        hypothesis_state: str,
        current_authority_present: bool,
    ) -> AgencyDecision:

        if not current_authority_present:
            return AgencyDecision.REQUIRE_APPROVAL

        risk = consequence.risk_score()

        if (
            consequence.irreversibility >= 0.85
            or consequence.blast_radius >= 0.90
        ):
            return AgencyDecision.REQUIRE_APPROVAL

        if (
            hypothesis_state == "COMPETING"
            and risk >= 0.40
        ):
            return AgencyDecision.ESCALATE

        if consequence.uncertainty >= 0.75:
            return AgencyDecision.ESCALATE

        if risk >= 0.70:
            return AgencyDecision.REQUIRE_APPROVAL

        if risk >= 0.35:
            return AgencyDecision.ALLOW_WITH_BOUNDS

        return AgencyDecision.ALLOW

    # ========================================================
    # HARD INVARIANTS
    # ========================================================

    def _parse_invariants(
        self,
        raw: Any,
    ) -> List[HardInvariant]:

        if not isinstance(raw, list):
            raise ValidationError(
                "hard_invariants must be a list"
            )

        result: List[HardInvariant] = []

        for index, item in enumerate(raw):

            if not isinstance(item, dict):
                raise ValidationError(
                    f"hard_invariants[{index}] must be a dictionary"
                )

            try:
                status = InvariantStatus(
                    item.get(
                        "status",
                        "UNKNOWN",
                    )
                )
            except ValueError as exc:
                raise ValidationError(
                    "invalid invariant status"
                ) from exc

            result.append(
                HardInvariant(
                    invariant_id=str(
                        item.get(
                            "invariant_id",
                            f"I{index + 1}",
                        )
                    ),
                    description=str(
                        item.get(
                            "description",
                            "",
                        )
                    ),
                    status=status,
                    evidence=list(
                        item.get(
                            "evidence",
                            [],
                        )
                    ),
                    reason=item.get(
                        "reason"
                    ),
                )
            )

        return result

    def _admit(
        self,
        invariants: List[HardInvariant],
    ) -> Dict[str, Any]:

        if any(
            invariant.status == InvariantStatus.FAIL
            for invariant in invariants
        ):
            return {
                "status": InvariantStatus.FAIL,
                "admitted": False,
            }

        if any(
            invariant.status == InvariantStatus.UNKNOWN
            for invariant in invariants
        ):
            return {
                "status": InvariantStatus.UNKNOWN,
                "admitted": False,
            }

        return {
            "status": InvariantStatus.PASS,
            "admitted": True,
        }

    @staticmethod
    def _serialize_admission(
        admission: Dict[str, Any],
    ) -> Dict[str, Any]:

        return {
            "status": admission["status"].value,
            "admitted": admission["admitted"],
        }

    # ========================================================
    # HYPOTHESES
    # ========================================================

    def _parse_hypotheses(
        self,
        raw: Any,
    ) -> List[Hypothesis]:

        if not isinstance(raw, list):
            raise ValidationError(
                "hypotheses must be a list"
            )

        result: List[Hypothesis] = []

        for index, item in enumerate(raw):

            if not isinstance(item, dict):
                continue

            try:
                epistemic_class = EpistemicClass(
                    item.get(
                        "epistemic_class",
                        "AMOS_MODEL",
                    )
                )
            except ValueError:
                epistemic_class = EpistemicClass.UNKNOWN

            result.append(
                Hypothesis(
                    hypothesis_id=str(
                        item.get(
                            "hypothesis_id",
                            f"H{index + 1}",
                        )
                    ),
                    statement=str(
                        item.get(
                            "statement",
                            "",
                        )
                    ),
                    epistemic_class=epistemic_class,
                    confidence=min(
                        _clamp01(
                            item.get(
                                "confidence",
                                0.0,
                            )
                        ),
                        self.claim_ceiling,
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

    def _hypothesis_state(
        self,
        hypotheses: List[Hypothesis],
    ) -> str:

        viable = [
            hypothesis
            for hypothesis in hypotheses
            if hypothesis.confidence > 0.0
        ]

        if len(viable) > 1:
            return "COMPETING"

        if len(viable) == 1:
            return "SINGLE"

        return "UNKNOWN/GAP"

    def _cheapest_discriminating_test(
        self,
        hypotheses: List[Hypothesis],
    ) -> Optional[Dict[str, Any]]:

        if len(hypotheses) < 2:
            return None

        for hypothesis in hypotheses:
            if hypothesis.falsifiers:
                return {
                    "test": hypothesis.falsifiers[0],
                    "targets": [
                        hypothesis.hypothesis_id
                    ],
                    "source": "declared_falsifier",
                }

        return {
            "status": "UNKNOWN/GAP",
            "reason": (
                "Multiple hypotheses remain viable but no "
                "discriminating falsifier was supplied."
            ),
        }

    # ========================================================
    # TENSOR CELLS
    # ========================================================

    def _parse_tensor_cells(
        self,
        raw: Any,
    ) -> List[TensorCell]:

        if not isinstance(raw, list):
            raise ValidationError(
                "tensor_cells must be a list"
            )

        cells: List[TensorCell] = []

        for index, item in enumerate(raw):

            if not isinstance(item, dict):
                continue

            level = str(
                item.get(
                    "level",
                    "L",
                )
            ).upper()

            if level not in {
                "H",
                "M",
                "L",
            }:
                raise ValidationError(
                    f"tensor_cells[{index}]: invalid H/M/L level"
                )

            try:
                epistemic = EpistemicClass(
                    item.get(
                        "epistemic_class",
                        "AMOS_MODEL",
                    )
                )
            except ValueError:
                epistemic = EpistemicClass.UNKNOWN

            provenance = self._parse_provenance(
                item.get(
                    "provenance",
                    [],
                )
            )

            cells.append(
                TensorCell(
                    cell_id=str(
                        item.get(
                            "cell_id",
                            f"C{index + 1}",
                        )
                    ),
                    level=level,
                    axis=str(
                        item.get(
                            "axis",
                            "unknown",
                        )
                    ),
                    value=item.get(
                        "value"
                    ),
                    epistemic_class=epistemic,
                    confidence=min(
                        _clamp01(
                            item.get(
                                "confidence",
                                0.0,
                            )
                        ),
                        self.claim_ceiling,
                    ),
                    timestamp=item.get(
                        "timestamp"
                    ),
                    provenance=provenance,
                )
            )

        return cells

    # ========================================================
    # EQUATIONS
    # ========================================================

    def _parse_equations(
        self,
        raw: Any,
    ) -> List[EquationRecord]:

        if not isinstance(raw, list):
            raise ValidationError(
                "equations must be a list"
            )

        records: List[EquationRecord] = []

        for index, item in enumerate(raw):

            if not isinstance(item, dict):
                continue

            try:
                equation_type = EquationType(
                    item.get(
                        "equation_type",
                        "UNVERIFIED",
                    )
                )
            except ValueError:
                equation_type = EquationType.UNVERIFIED

            records.append(
                EquationRecord(
                    equation_id=str(
                        item.get(
                            "equation_id",
                            f"E{index + 1}",
                        )
                    ),
                    expression=str(
                        item.get(
                            "expression",
                            "",
                        )
                    ),
                    equation_type=equation_type,
                    terms=dict(
                        item.get(
                            "terms",
                            {},
                        )
                    ),
                    assumptions=list(
                        item.get(
                            "assumptions",
                            [],
                        )
                    ),
                    falsifiers=list(
                        item.get(
                            "falsifiers",
                            [],
                        )
                    ),
                    provenance=self._parse_provenance(
                        item.get(
                            "provenance",
                            [],
                        )
                    ),
                )
            )

        return records

    # ========================================================
    # DEPENDENCIES / SELECTIVE INVALIDATION
    # ========================================================

    def _build_dependency_graph(
        self,
        raw: Any,
    ) -> DependencyGraph:

        graph = DependencyGraph()

        if not isinstance(raw, list):
            return graph

        for item in raw:

            if not isinstance(item, dict):
                continue

            parent = item.get(
                "parent"
            )

            child = item.get(
                "child"
            )

            if parent and child:
                graph.add_edge(
                    str(parent),
                    str(child),
                )

        return graph

    def invalidate_premise(
        self,
        graph: DependencyGraph,
        premise_id: str,
    ) -> Dict[str, Any]:
        """
        Implements:

            Invalid(p) => invalidate(descendants(p))
        """

        invalidated = graph.closure(
            premise_id
        )

        return {
            "invalid_premise": premise_id,
            "invalidated_descendants": sorted(
                invalidated
            ),
            "unaffected_state_preserved": True,
        }

    # ========================================================
    # CONFIDENCE
    # ========================================================

    def _confidence_ceiling(
        self,
        premises: Dict[str, float],
    ) -> float:
        """
        Implements:

            Conf(C) <= min_i Conf(P_i)
        """

        if not premises:
            return min(
                0.50,
                self.claim_ceiling,
            )

        weakest = min(
            _clamp01(value)
            for value in premises.values()
        )

        return min(
            weakest,
            self.claim_ceiling,
        )

    # ========================================================
    # VALIDATE OUTPUT
    # ========================================================

    def _validate_output(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        output = ctx.inputs.get(
            "output"
        )

        if not isinstance(output, dict):
            raise GapError(
                "UNKNOWN/GAP: output dictionary required."
            )

        issues: List[str] = []

        for required in (
            "H",
            "M",
            "L",
            "decision",
        ):
            if required not in output:
                issues.append(
                    f"missing_{required}"
                )

        h_state = output.get(
            "H",
            {},
        )

        admission = h_state.get(
            "admission",
            {}
        )

        if (
            admission.get("status") == "FAIL"
            and output.get("decision")
            not in {
                "BLOCK",
                "UNKNOWN/GAP",
            }
        ):
            issues.append(
                "hard_invariant_failure_was_compensated"
            )

        agency = h_state.get(
            "agency",
            {}
        )

        if (
            agency
            and not agency.get(
                "permission_present",
                False,
            )
            and output.get("decision")
            == "ALLOW"
        ):
            issues.append(
                "agency_allowed_without_permission"
            )

        if (
            output.get(
                "world_effect_committed"
            )
            is True
        ):
            issues.append(
                "governor_must_not_self_commit_world_effect"
            )

        l_state = output.get(
            "L",
            {},
        )

        for equation in l_state.get(
            "equations",
            [],
        ):
            if (
                isinstance(equation, dict)
                and equation.get(
                    "equation_type"
                )
                == "SOURCE_DEFINED"
                and equation.get(
                    "externally_validated_empirical_law"
                )
                is True
            ):
                issues.append(
                    "source_defined_equation_promoted_without_external_validation"
                )

        return AgentResult(
            status=(
                ExecutionStatus.VERIFIED
                if not issues
                else ExecutionStatus.CONDITIONAL
            ),
            capability=ctx.capability,
            summary=(
                "Agency Consequence Governor output validation completed."
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

        records = ctx.inputs.get(
            "records"
        )

        if not isinstance(records, list):
            raise GapError(
                "UNKNOWN/GAP: records list required."
            )

        traced: List[Dict[str, Any]] = []
        gaps: List[str] = []

        for index, record in enumerate(
            records
        ):

            if not isinstance(record, dict):
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
                    record.get("id")
                    or record.get("cell_id")
                    or record.get("equation_id")
                    or record.get("hypothesis_id")
                ),
                "provenance": provenance,
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
                "Agency/consequence provenance trace completed."
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

        if (
            claim.get(
                "capability_equals_permission"
            )
            is True
        ):
            issues.append(
                "capability_does_not_equal_permission"
            )

        if (
            claim.get(
                "permission_equals_consequence_acceptability"
            )
            is True
        ):
            issues.append(
                "permission_does_not_remove_consequence_governance"
            )

        if (
            claim.get(
                "source_defined_equation_is_empirical_law"
            )
            is True
        ):
            issues.append(
                "source_defined_equation_not_automatically_empirical"
            )

        if (
            claim.get(
                "competing_hypotheses_forced_to_single_answer"
            )
            is True
        ):
            issues.append(
                "must_preserve_competing_when_unresolved"
            )

        confidence = self._confidence_ceiling(
            {
                str(key): float(value)
                for key, value
                in claim.get(
                    "premise_confidences",
                    {},
                ).items()
            }
        )

        return AgentResult(
            status=(
                ExecutionStatus.CONDITIONAL
                if issues
                else ExecutionStatus.DERIVED
            ),
            capability=ctx.capability,
            summary=(
                "Agency/consequence claim assessment completed."
            ),
            data={
                "issues": issues,
                "classification": claim.get(
                    "epistemic_class",
                    "AMOS_MODEL",
                ),
            },
            gaps=issues,
            confidence_ceiling=confidence,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # PROVENANCE PARSER
    # ========================================================

    @staticmethod
    def _parse_provenance(
        raw: Any,
    ) -> List[ProvenanceRef]:

        if not isinstance(raw, list):
            return []

        result: List[ProvenanceRef] = []

        for item in raw:
            if not isinstance(item, dict):
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
                )
            )

        return result

    # ========================================================
    # DEFAULT PROVENANCE
    # ========================================================

    def _default_provenance(
        self,
    ) -> List[ProvenanceRef]:

        return [
            ProvenanceRef(
                source=(
                    "AMOS Agency & Consequence Governor "
                    "source skill"
                ),
                path=(
                    ".devin/skills/"
                    "amos-agency-consequence-governor/"
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
    # UTILITIES
    # ========================================================

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


# ============================================================
# EXAMPLE
# ============================================================

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO
    )

    agent = (
        AmosAgencyConsequenceGovernorAgent(
            repo_root="."
        )
    )

    context = ExecutionContext(
        query=(
            "Determine whether this agent may execute "
            "the proposed action."
        ),
        capability="agent.execute",
        authorized_write=True,
        authority_witness=(
            "steward_review:example"
        ),
        inputs={
            "source_identity": "agent:planner-01",
            "target": "shared-runtime-config",
            "scope": (
                "single governed configuration proposal"
            ),
            "action": {
                "type": "update_configuration",
                "parameter": "retry_budget",
                "proposed_value": 4,
            },
            "governance": {
                "authority_scope": (
                    "configuration-proposal-only"
                ),
                "commit_authority": False,
            },
            "agency_state": {
                "perception_available": True,
                "option_space_available": True,
                "permission_present": True,
                "execution_capacity_present": True,
                "consequence_tracking_present": True,
            },
            "consequence": {
                "stakes": 0.35,
                "irreversibility": 0.15,
                "blast_radius": 0.30,
                "persistence": 0.25,
                "uncertainty": 0.20,
            },
            "hard_invariants": [
                {
                    "invariant_id": "I1",
                    "description": (
                        "Agent cannot widen its own authority."
                    ),
                    "status": "PASS",
                    "evidence": [
                        "requested effect remains inside delegated scope"
                    ],
                },
                {
                    "invariant_id": "I2",
                    "description": (
                        "Durable effect requires separate "
                        "commit authority."
                    ),
                    "status": "PASS",
                    "evidence": [
                        "this governor returns proposal only"
                    ],
                },
            ],
            "hypotheses": [
                {
                    "hypothesis_id": "H1",
                    "statement": (
                        "Increasing retry budget may improve "
                        "recoverability."
                    ),
                    "epistemic_class": "AMOS_MODEL",
                    "confidence": 0.78,
                    "supporting_evidence": [
                        "recent retry exhaustion"
                    ],
                    "falsifiers": [
                        (
                            "Controlled test shows retries increase "
                            "failure amplification."
                        )
                    ],
                },
                {
                    "hypothesis_id": "H2",
                    "statement": (
                        "Current retry budget may already be optimal "
                        "and increased retries may add load."
                    ),
                    "epistemic_class": "COMPETING",
                    "confidence": 0.72,
                    "supporting_evidence": [
                        "queue pressure rises under repeated execution"
                    ],
                    "falsifiers": [
                        (
                            "Load test shows no material queue "
                            "pressure increase."
                        )
                    ],
                },
            ],
            "tensor_cells": [
                {
                    "cell_id": "C1",
                    "level": "L",
                    "axis": "retry_budget",
                    "value": 3,
                    "epistemic_class": "DERIVED",
                    "confidence": 0.92,
                    "timestamp": "2026-08-27T00:03:00+07:00",
                    "provenance": [
                        {
                            "source": "runtime-config",
                        }
                    ],
                }
            ],
            "equations": [
                {
                    "equation_id": "E_AGENCY_01",
                    "expression": (
                        "Admit(x)=AND_i HardInvariant_i(x)"
                    ),
                    "equation_type": "SOURCE_DEFINED",
                    "terms": {
                        "x": "proposed action"
                    },
                    "assumptions": [
                        "all load-bearing hard invariants are enumerated"
                    ],
                    "falsifiers": [
                        (
                            "a missing hard invariant materially changes "
                            "admission"
                        )
                    ],
                    "provenance": [
                        {
                            "source": (
                                "amos-agency-consequence-governor"
                            )
                        }
                    ],
                }
            ],
            "premise_confidences": {
                "current-config": 0.92,
                "retry-exhaustion-observation": 0.84,
                "authority-scope": 0.95,
            },
            "claim": (
                "The agent may propose the bounded retry-budget "
                "change, but the governor does not itself commit it."
            ),
            "falsifiers": [
                (
                    "Delegated authority is revoked or target scope changes."
                ),
                (
                    "Controlled testing shows the proposed change "
                    "increases downstream failure."
                ),
            ],
            "repair_path": (
                "revise proposal using observed test result"
            ),
            "rollback_path": (
                "retain current retry budget"
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

    except AgencyConsequenceError as exc:
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