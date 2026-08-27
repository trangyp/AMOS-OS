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
# AMOS AGENT ECONOMY CONSTITUTIONAL GOVERNANCE RSCF AGENT
# ============================================================

AGENT_ID = "amos-agent-economy-constitutional-governance-rscf-agent"
AGENT_VERSION = "1.0.0"


# ============================================================
# ENUMS
# ============================================================

class EpistemicClass(str, Enum):
    SOURCE_MODEL = "SOURCE_MODEL"
    SOURCE_CLAIM = "SOURCE_CLAIM"
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


class SideEffect(str, Enum):
    READ = "read"
    WRITE = "write"


class AuthorityBranch(str, Enum):
    LEGISLATION = "LEGISLATION"
    EXECUTION = "EXECUTION"
    ADJUDICATION = "ADJUDICATION"


class ContractTier(str, Enum):
    FOUNDATIONAL = "FOUNDATIONAL"
    META = "META"
    OPERATIONAL = "OPERATIONAL"


class GovernancePrimitive(str, Enum):
    FORMAL_RULE_SUBSTRATE = "FORMAL_RULE_SUBSTRATE"
    ECONOMIC_SUBSTRATE = "ECONOMIC_SUBSTRATE"
    INSTITUTIONAL_MEMORY = "INSTITUTIONAL_MEMORY"
    VERIFIABLE_TRANSPARENCY = "VERIFIABLE_TRANSPARENCY"


class InvariantStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNKNOWN = "UNKNOWN"


class GovernanceDecision(str, Enum):
    ALLOW = "ALLOW"
    ALLOW_WITH_BOUNDS = "ALLOW_WITH_BOUNDS"
    REQUIRE_ADJUDICATION = "REQUIRE_ADJUDICATION"
    REQUIRE_LEGISLATIVE_CHANGE = "REQUIRE_LEGISLATIVE_CHANGE"
    BLOCK = "BLOCK"
    ESCALATE = "ESCALATE"
    UNKNOWN = "UNKNOWN/GAP"


# ============================================================
# ERRORS
# ============================================================

class AgentEconomyGovernanceError(RuntimeError):
    pass


class ValidationError(AgentEconomyGovernanceError):
    pass


class AuthorizationError(AgentEconomyGovernanceError):
    pass


class GapError(AgentEconomyGovernanceError):
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
class OwnershipNode:
    principal_id: str
    principal_type: str
    parent_principal: Optional[str] = None
    authority_scope: List[str] = field(default_factory=list)


@dataclass
class GovernanceTensor:
    """
    Source-governance tensor:

    G = T[
        agent,
        principal,
        ownership_chain,
        legislative_state,
        execution_state,
        adjudication_state,
        contract_tier,
        audit_ledger,
        sanction_state,
        reputation_state,
        economy_state,
        provenance
    ]
    """

    agent: str
    principal: str
    ownership_chain: List[OwnershipNode]

    legislative_state: Dict[str, Any]
    execution_state: Dict[str, Any]
    adjudication_state: Dict[str, Any]

    contract_tier: ContractTier

    audit_ledger: List[Dict[str, Any]]
    sanction_state: Dict[str, Any]
    reputation_state: Dict[str, Any]
    economy_state: Dict[str, Any]

    provenance: List[ProvenanceRef]


@dataclass
class ContractProposal:
    contract_id: str
    proposer_agent: str
    tier: ContractTier
    clauses: List[str]

    parent_contract_ids: List[str] = field(default_factory=list)
    changes_foundational_constraints: bool = False

    execution_effects: List[str] = field(default_factory=list)
    economic_effects: List[str] = field(default_factory=list)

    provenance: List[ProvenanceRef] = field(default_factory=list)


@dataclass
class GovernanceHypothesis:
    hypothesis_id: str
    statement: str
    epistemic_class: EpistemicClass
    confidence: float

    supporting_evidence: List[str] = field(default_factory=list)
    conflicting_evidence: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    falsifiers: List[str] = field(default_factory=list)


@dataclass
class RSCFCapsule:
    claim: str
    epistemic_class: EpistemicClass

    scope: str
    governance_primitive: GovernancePrimitive
    authority_branch: AuthorityBranch
    contract_tier: ContractTier

    principal_chain: List[str]

    incentive_state: Dict[str, Any]
    sanction_state: Dict[str, Any]

    source_assumptions: List[str]

    competing_governance_models: List[GovernanceHypothesis]

    premises: Dict[str, float]
    dependencies: List[str]

    provenance: List[ProvenanceRef]
    falsifiers: List[str]

    confidence_ceiling: float

    decision: GovernanceDecision

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
    "display_name": (
        "Agent Economy Constitutional Governance RSCF"
    ),
    "description": (
        "AMOS constitutional governance engine for autonomous-agent "
        "economies using separation of powers, contract hierarchy, "
        "ownership accountability, sanctions, institutional memory, "
        "auditability, and RSCF governance."
    ),
    "version": AGENT_VERSION,
    "author": "Trang Phan",
    "steward": "Trang Phan",
    "system": "AMOS_OS",
    "role": (
        "Govern constitutional and economic interactions among agents, "
        "principals, contracts, authority branches, sanctions, and "
        "institutional memory."
    ),
    "primary_skill": (
        "amos-agent-economy-constitutional-governance-rscf"
    ),
    "skill_path": (
        ".devin/skills/"
        "amos-agent-economy-constitutional-governance-rscf/"
        "SKILL.md"
    ),
    "workflow": (
        "amos-agent-economy-constitutional-governance-rscf-workflow.md"
    ),
    "epistemic_class": "SOURCE_MODEL",
    "claim_ceiling": 0.95,
    "owner_team": "AMOS_CORE",
    "business_domain": "econ",
    "risk_tier": "medium",
    "observability": "structured_logs+content_hash",
    "approval_mode": "steward_review",
    "promotion_state": "production",
    "content_hash": "8a232f4a9c2da9e7",
    "source_anchor": {
        "title": (
            "AgentCity: Constitutional Governance for Autonomous "
            "Agent Economies via Separation of Power"
        ),
        "arxiv": "2604.07007v1",
        "date": "2026-04-08",
        "evidence_class": (
            "SOURCE_MODEL / pre-registered architecture"
        ),
    },
}


CAPABILITIES: Dict[str, CapabilityContract] = {
    "econ.execute": CapabilityContract(
        name="econ.execute",
        description=(
            "Evaluate agent-economy governance actions using separation "
            "of powers, ownership chains, contract hierarchy, incentives, "
            "sanctions, auditability, and RSCF constraints."
        ),
        side_effect=SideEffect.WRITE,
    ),
    "econ.validate": CapabilityContract(
        name="econ.validate",
        description=(
            "Validate governance outputs against constitutional hierarchy, "
            "authority separation, assumptions, confidence ceilings, "
            "and evidence boundaries."
        ),
        side_effect=SideEffect.READ,
    ),
    "econ.trace_provenance": CapabilityContract(
        name="econ.trace_provenance",
        description=(
            "Trace governance claims, contracts, branch decisions, "
            "sanctions, and audit records to source evidence."
        ),
        side_effect=SideEffect.READ,
    ),
    "econ.assess_claim": CapabilityContract(
        name="econ.assess_claim",
        description=(
            "Assess economic-governance claims for source status, "
            "empirical support, scope, assumptions, and overreach."
        ),
        side_effect=SideEffect.READ,
    ),
}


# ============================================================
# MAIN AGENT
# ============================================================

class AmosAgentEconomyConstitutionalGovernanceAgent:
    """
    Runtime adapter for:
        amos-agent-economy-constitutional-governance-rscf

    Source architecture:

        LEGISLATION
        EXECUTION
        ADJUDICATION

    Contract hierarchy:

        FOUNDATIONAL
        META
        OPERATIONAL

    Governance primitives:

        FORMAL_RULE_SUBSTRATE
        ECONOMIC_SUBSTRATE
        INSTITUTIONAL_MEMORY
        VERIFIABLE_TRANSPARENCY

    Hard boundaries:
    - agent reasoning, executable law, and human adjudication remain
      distinct authority layers;
    - agent-generated contracts cannot override agent-immutable
      foundational constraints;
    - ownership-chain accountability is structural, not proof of alignment;
    - public auditability != semantic correctness;
    - majority-honesty assumptions remain explicit;
    - pre-registered experiments != completed empirical validation;
    - blockchain determinism != governance optimality.
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
            / "amos-agent-economy-constitutional-governance-rscf"
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
            "econ.execute": self._execute_governance,
            "econ.validate": self._validate_output,
            "econ.trace_provenance": self._trace_provenance,
            "econ.assess_claim": self._assess_claim,
        }

    # ========================================================
    # PUBLIC ENTRYPOINT
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
                f"Unsupported capability: "
                f"{ctx.capability}"
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
                "Capability does not imply governance authority."
            )

        if not ctx.authority_witness:
            raise AuthorizationError(
                "Governance-changing operation requires "
                "an explicit authority_witness."
            )

    # ========================================================
    # EXECUTE
    # ========================================================

    def _execute_governance(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        tensor = self._parse_governance_tensor(
            ctx.inputs.get(
                "governance_tensor"
            )
        )

        proposal = self._parse_contract_proposal(
            ctx.inputs.get(
                "contract_proposal"
            )
        )

        invariants = self._build_invariants(
            tensor=tensor,
            proposal=proposal,
            supplied=ctx.inputs.get(
                "hard_invariants",
                [],
            ),
        )

        admission = self._admit(
            invariants
        )

        if admission["status"] == InvariantStatus.FAIL:

            return AgentResult(
                status=ExecutionStatus.REJECTED,
                capability=ctx.capability,
                summary=(
                    "Constitutional governance proposal rejected "
                    "because a hard invariant failed."
                ),
                data={
                    "governance_tensor": asdict(
                        tensor
                    ),
                    "contract_proposal": asdict(
                        proposal
                    ),
                    "invariants": [
                        asdict(i)
                        for i in invariants
                    ],
                    "decision": GovernanceDecision.BLOCK.value,
                    "durable_governance_change_committed": False,
                },
                gaps=[
                    (
                        invariant.reason
                        or invariant.description
                    )
                    for invariant in invariants
                    if invariant.status
                    == InvariantStatus.FAIL
                ],
                warnings=[
                    "Hard constitutional failures are non-compensatory."
                ],
                confidence_ceiling=self.claim_ceiling,
                provenance=self._default_provenance(),
            )

        if admission["status"] == InvariantStatus.UNKNOWN:

            return AgentResult(
                status=ExecutionStatus.UNKNOWN,
                capability=ctx.capability,
                summary=(
                    "Governance proposal is UNKNOWN/GAP because "
                    "a load-bearing constitutional condition is unresolved."
                ),
                data={
                    "governance_tensor": asdict(
                        tensor
                    ),
                    "contract_proposal": asdict(
                        proposal
                    ),
                    "invariants": [
                        asdict(i)
                        for i in invariants
                    ],
                    "decision": GovernanceDecision.UNKNOWN.value,
                    "durable_governance_change_committed": False,
                },
                gaps=[
                    (
                        invariant.reason
                        or invariant.description
                    )
                    for invariant in invariants
                    if invariant.status
                    == InvariantStatus.UNKNOWN
                ],
                confidence_ceiling=min(
                    0.50,
                    self.claim_ceiling,
                ),
                provenance=self._default_provenance(),
            )

        hypotheses = self._parse_hypotheses(
            ctx.inputs.get(
                "competing_governance_models",
                [],
            )
        )

        hypothesis_state = self._hypothesis_state(
            hypotheses
        )

        decision = self._governance_decision(
            tensor=tensor,
            proposal=proposal,
            hypothesis_state=hypothesis_state,
        )

        premise_confidences = {
            str(key): _clamp01(value)
            for key, value
            in ctx.inputs.get(
                "premise_confidences",
                {},
            ).items()
        }

        confidence = self._confidence_ceiling(
            premise_confidences
        )

        graph = self._build_dependency_graph(
            ctx.inputs.get(
                "dependencies",
                [],
            )
        )

        primitive = self._parse_primitive(
            ctx.inputs.get(
                "governance_primitive",
                "FORMAL_RULE_SUBSTRATE",
            )
        )

        branch = self._parse_branch(
            ctx.inputs.get(
                "authority_branch",
                "EXECUTION",
            )
        )

        source_assumptions = list(
            ctx.inputs.get(
                "source_assumptions",
                [],
            )
        )

        # Preserve source-model assumptions explicitly.
        if not any(
            "majority" in assumption.lower()
            for assumption in source_assumptions
        ):
            source_assumptions.append(
                "Majority-honesty assumptions, where relied upon, "
                "must remain explicit and are not silently assumed."
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
                        "Proposed agent-economy governance action "
                        "is constitutionally admissible only within "
                        "the supplied source-model and authority scope."
                    ),
                )
            ),
            epistemic_class=(
                EpistemicClass.SOURCE_MODEL
            ),
            scope=str(
                ctx.inputs.get(
                    "scope",
                    tensor.agent,
                )
            ),
            governance_primitive=primitive,
            authority_branch=branch,
            contract_tier=proposal.tier,
            principal_chain=[
                node.principal_id
                for node
                in tensor.ownership_chain
            ],
            incentive_state=dict(
                ctx.inputs.get(
                    "incentive_state",
                    {},
                )
            ),
            sanction_state=tensor.sanction_state,
            source_assumptions=source_assumptions,
            competing_governance_models=hypotheses,
            premises=premise_confidences,
            dependencies=list(
                ctx.inputs.get(
                    "dependency_ids",
                    [],
                )
            ),
            provenance=self._default_provenance(),
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
            GovernanceDecision.REQUIRE_ADJUDICATION,
            GovernanceDecision.REQUIRE_LEGISLATIVE_CHANGE,
            GovernanceDecision.ESCALATE,
            GovernanceDecision.ALLOW_WITH_BOUNDS,
        }:
            status = ExecutionStatus.CONDITIONAL
        else:
            status = ExecutionStatus.MODEL

        return AgentResult(
            status=status,
            capability=ctx.capability,
            summary=(
                f"Constitutional governance decision: "
                f"{decision.value}."
            ),
            data={
                "conclusion_class": "SOURCE_MODEL",
                "source_anchor": (
                    AGENT_CONFIG[
                        "source_anchor"
                    ]
                ),
                "governance_tensor": asdict(
                    tensor
                ),
                "contract_proposal": asdict(
                    proposal
                ),
                "invariants": [
                    asdict(i)
                    for i in invariants
                ],
                "rscf": asdict(
                    rscf
                ),
                "dependency_graph": {
                    parent: sorted(
                        list(children)
                    )
                    for parent, children
                    in graph.descendants.items()
                },
                "hypothesis_state": hypothesis_state,
                "cheapest_discriminating_test": (
                    discriminating_test
                ),
                "decision": decision.value,
                "durable_governance_change_committed": False,
            },
            warnings=[
                (
                    "The AgentCity source is a pre-registered architecture; "
                    "do not treat it as completed empirical validation."
                ),
                (
                    "Ownership-chain accountability is a structural "
                    "mechanism, not proof of alignment."
                ),
                (
                    "Public auditability does not establish semantic "
                    "correctness."
                ),
                (
                    "Blockchain or executable-law determinism does not "
                    "establish governance optimality."
                ),
            ],
            confidence_ceiling=confidence,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # GOVERNANCE TENSOR
    # ========================================================

    def _parse_governance_tensor(
        self,
        raw: Any,
    ) -> GovernanceTensor:

        if not isinstance(
            raw,
            dict,
        ):
            raise GapError(
                "UNKNOWN/GAP: governance_tensor dictionary required."
            )

        required = [
            "agent",
            "principal",
            "contract_tier",
        ]

        missing = [
            key
            for key in required
            if not raw.get(key)
        ]

        if missing:
            raise GapError(
                "UNKNOWN/GAP: missing governance tensor fields: "
                + ", ".join(missing)
            )

        try:
            contract_tier = ContractTier(
                raw["contract_tier"]
            )
        except ValueError as exc:
            raise ValidationError(
                "invalid contract_tier"
            ) from exc

        ownership_chain: List[OwnershipNode] = []

        for item in raw.get(
            "ownership_chain",
            [],
        ):

            if not isinstance(
                item,
                dict,
            ):
                continue

            ownership_chain.append(
                OwnershipNode(
                    principal_id=str(
                        item.get(
                            "principal_id",
                            "",
                        )
                    ),
                    principal_type=str(
                        item.get(
                            "principal_type",
                            "",
                        )
                    ),
                    parent_principal=item.get(
                        "parent_principal"
                    ),
                    authority_scope=list(
                        item.get(
                            "authority_scope",
                            [],
                        )
                    ),
                )
            )

        return GovernanceTensor(
            agent=str(
                raw["agent"]
            ),
            principal=str(
                raw["principal"]
            ),
            ownership_chain=ownership_chain,
            legislative_state=dict(
                raw.get(
                    "legislative_state",
                    {},
                )
            ),
            execution_state=dict(
                raw.get(
                    "execution_state",
                    {},
                )
            ),
            adjudication_state=dict(
                raw.get(
                    "adjudication_state",
                    {},
                )
            ),
            contract_tier=contract_tier,
            audit_ledger=list(
                raw.get(
                    "audit_ledger",
                    [],
                )
            ),
            sanction_state=dict(
                raw.get(
                    "sanction_state",
                    {},
                )
            ),
            reputation_state=dict(
                raw.get(
                    "reputation_state",
                    {},
                )
            ),
            economy_state=dict(
                raw.get(
                    "economy_state",
                    {},
                )
            ),
            provenance=self._parse_provenance(
                raw.get(
                    "provenance",
                    [],
                )
            ),
        )

    # ========================================================
    # CONTRACT
    # ========================================================

    def _parse_contract_proposal(
        self,
        raw: Any,
    ) -> ContractProposal:

        if not isinstance(
            raw,
            dict,
        ):
            raise GapError(
                "UNKNOWN/GAP: contract_proposal dictionary required."
            )

        try:
            tier = ContractTier(
                raw.get(
                    "tier",
                    "OPERATIONAL",
                )
            )
        except ValueError as exc:
            raise ValidationError(
                "invalid proposal contract tier"
            ) from exc

        return ContractProposal(
            contract_id=str(
                raw.get(
                    "contract_id",
                    "",
                )
            ),
            proposer_agent=str(
                raw.get(
                    "proposer_agent",
                    "",
                )
            ),
            tier=tier,
            clauses=list(
                raw.get(
                    "clauses",
                    [],
                )
            ),
            parent_contract_ids=list(
                raw.get(
                    "parent_contract_ids",
                    [],
                )
            ),
            changes_foundational_constraints=bool(
                raw.get(
                    "changes_foundational_constraints",
                    False,
                )
            ),
            execution_effects=list(
                raw.get(
                    "execution_effects",
                    [],
                )
            ),
            economic_effects=list(
                raw.get(
                    "economic_effects",
                    [],
                )
            ),
            provenance=self._parse_provenance(
                raw.get(
                    "provenance",
                    [],
                )
            ),
        )

    # ========================================================
    # HARD INVARIANTS
    # ========================================================

    def _build_invariants(
        self,
        tensor: GovernanceTensor,
        proposal: ContractProposal,
        supplied: Any,
    ) -> List[HardInvariant]:

        invariants: List[HardInvariant] = []

        # Separation of powers.
        branch_states_present = all(
            isinstance(state, dict)
            for state in (
                tensor.legislative_state,
                tensor.execution_state,
                tensor.adjudication_state,
            )
        )

        invariants.append(
            HardInvariant(
                invariant_id="I_SEPARATION_OF_POWER",
                description=(
                    "Legislation, execution, and adjudication "
                    "remain distinct authority layers."
                ),
                status=(
                    InvariantStatus.PASS
                    if branch_states_present
                    else InvariantStatus.UNKNOWN
                ),
                reason=(
                    None
                    if branch_states_present
                    else "authority branch states incomplete"
                ),
            )
        )

        # Foundational constraints cannot be overridden by agents.
        foundational_override = (
            proposal.changes_foundational_constraints
            and proposal.proposer_agent != ""
        )

        invariants.append(
            HardInvariant(
                invariant_id="I_FOUNDATIONAL_IMMUTABILITY",
                description=(
                    "Agent-generated contracts cannot override "
                    "agent-immutable foundational constraints."
                ),
                status=(
                    InvariantStatus.FAIL
                    if foundational_override
                    else InvariantStatus.PASS
                ),
                reason=(
                    "agent proposal attempts to change foundational constraints"
                    if foundational_override
                    else None
                ),
            )
        )

        # Explicit principal chain.
        chain_valid = bool(
            tensor.principal
            and tensor.ownership_chain
        )

        invariants.append(
            HardInvariant(
                invariant_id="I_PRINCIPAL_CHAIN",
                description=(
                    "Governed agent effects retain an explicit "
                    "principal/ownership accountability chain."
                ),
                status=(
                    InvariantStatus.PASS
                    if chain_valid
                    else InvariantStatus.UNKNOWN
                ),
                reason=(
                    None
                    if chain_valid
                    else "ownership/principal chain incomplete"
                ),
            )
        )

        # Add caller-provided load-bearing invariants.
        if isinstance(
            supplied,
            list,
        ):
            for index, item in enumerate(
                supplied
            ):

                if not isinstance(
                    item,
                    dict,
                ):
                    continue

                try:
                    status = InvariantStatus(
                        item.get(
                            "status",
                            "UNKNOWN",
                        )
                    )
                except ValueError:
                    status = InvariantStatus.UNKNOWN

                invariants.append(
                    HardInvariant(
                        invariant_id=str(
                            item.get(
                                "invariant_id",
                                f"I_USER_{index + 1}",
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

        return invariants

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

    # ========================================================
    # DECISION
    # ========================================================

    def _governance_decision(
        self,
        tensor: GovernanceTensor,
        proposal: ContractProposal,
        hypothesis_state: str,
    ) -> GovernanceDecision:

        # Foundational changes require legislation outside ordinary
        # agent-generated operational contracts.
        if proposal.tier == ContractTier.FOUNDATIONAL:
            return GovernanceDecision.REQUIRE_LEGISLATIVE_CHANGE

        if proposal.changes_foundational_constraints:
            return GovernanceDecision.BLOCK

        # Dispute / unresolved legality -> adjudication.
        if tensor.adjudication_state.get(
            "dispute_open"
        ):
            return GovernanceDecision.REQUIRE_ADJUDICATION

        if hypothesis_state == "COMPETING":
            return GovernanceDecision.ESCALATE

        if not tensor.audit_ledger:
            return GovernanceDecision.ALLOW_WITH_BOUNDS

        if not tensor.ownership_chain:
            return GovernanceDecision.ESCALATE

        return GovernanceDecision.ALLOW

    # ========================================================
    # HYPOTHESES
    # ========================================================

    def _parse_hypotheses(
        self,
        raw: Any,
    ) -> List[GovernanceHypothesis]:

        if not isinstance(
            raw,
            list,
        ):
            raise ValidationError(
                "competing_governance_models must be a list"
            )

        result: List[
            GovernanceHypothesis
        ] = []

        for index, item in enumerate(
            raw
        ):

            if not isinstance(
                item,
                dict,
            ):
                continue

            try:
                epistemic = EpistemicClass(
                    item.get(
                        "epistemic_class",
                        "AMOS_MODEL",
                    )
                )
            except ValueError:
                epistemic = EpistemicClass.UNKNOWN

            result.append(
                GovernanceHypothesis(
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
                )
            )

        return result

    @staticmethod
    def _hypothesis_state(
        hypotheses: List[
            GovernanceHypothesis
        ],
    ) -> str:

        viable = [
            h
            for h in hypotheses
            if h.confidence > 0.0
        ]

        if len(viable) > 1:
            return "COMPETING"

        if len(viable) == 1:
            return "SINGLE"

        return "UNKNOWN/GAP"

    def _cheapest_discriminating_test(
        self,
        hypotheses: List[
            GovernanceHypothesis
        ],
    ) -> Optional[Dict[str, Any]]:

        if len(hypotheses) < 2:
            return None

        candidates: List[
            Dict[str, Any]
        ] = []

        for hypothesis in hypotheses:

            for falsifier in hypothesis.falsifiers:
                candidates.append({
                    "test": falsifier,
                    "targets": [
                        hypothesis.hypothesis_id
                    ],
                    "source": "declared_falsifier",
                })

        if not candidates:
            return {
                "status": "UNKNOWN/GAP",
                "reason": (
                    "Multiple governance models remain live "
                    "but no discriminating falsifier was supplied."
                ),
            }

        return candidates[0]

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
        Conf(C) <= min_i Conf(P_i)
        """

        if not premises:
            return min(
                0.50,
                self.claim_ceiling,
            )

        return min(
            min(
                _clamp01(value)
                for value
                in premises.values()
            ),
            self.claim_ceiling,
        )

    # ========================================================
    # VALIDITY / FRESHNESS
    # ========================================================

    def valid_now(
        self,
        *,
        valid_at_source: bool,
        scope_match: bool,
        regime_match: bool,
        fresh_enough: bool,
        falsifier_triggered: bool,
    ) -> bool:
        """
        ValidNow(C) =
            ValidAtSource(C)
            AND ScopeMatch
            AND RegimeMatch
            AND FreshEnough
            AND NOT FalsifierTriggered
        """

        return (
            valid_at_source
            and scope_match
            and regime_match
            and fresh_enough
            and not falsifier_triggered
        )

    # ========================================================
    # SELECTIVE INVALIDATION
    # ========================================================

    def _build_dependency_graph(
        self,
        raw: Any,
    ) -> DependencyGraph:

        graph = DependencyGraph()

        if not isinstance(
            raw,
            list,
        ):
            return graph

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
        Invalid(P_k) => Invalidate(Descendants(P_k))
        """

        invalidated = graph.closure(
            premise_id
        )

        return {
            "invalid_premise": premise_id,
            "invalidated_descendants": sorted(
                invalidated
            ),
            "unaffected_structure_preserved": True,
        }

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

        if not isinstance(
            output,
            dict,
        ):
            raise GapError(
                "UNKNOWN/GAP: output dictionary required."
            )

        issues: List[str] = []

        decision = output.get(
            "decision"
        )

        proposal = output.get(
            "contract_proposal",
            {},
        )

        if (
            proposal.get(
                "changes_foundational_constraints"
            )
            and decision
            in {
                "ALLOW",
                "ALLOW_WITH_BOUNDS",
            }
        ):
            issues.append(
                "agent_contract_overrides_foundational_constraint"
            )

        if (
            output.get(
                "reasoning_layer_equals_executable_law"
            )
            is True
        ):
            issues.append(
                "reasoning_and_executable_law_must_remain_distinct"
            )

        if (
            output.get(
                "execution_layer_equals_adjudication"
            )
            is True
        ):
            issues.append(
                "execution_and_adjudication_must_remain_distinct"
            )

        if (
            output.get(
                "public_auditability_proves_semantic_correctness"
            )
            is True
        ):
            issues.append(
                "auditability_does_not_prove_semantic_correctness"
            )

        if (
            output.get(
                "ownership_chain_proves_alignment"
            )
            is True
        ):
            issues.append(
                "ownership_chain_not_proof_of_alignment"
            )

        if (
            output.get(
                "preregistered_experiment_claimed_completed"
            )
            is True
        ):
            issues.append(
                "preregistered_architecture_not_completed_empirical_validation"
            )

        if (
            output.get(
                "blockchain_determinism_proves_optimality"
            )
            is True
        ):
            issues.append(
                "determinism_does_not_prove_governance_optimality"
            )

        if (
            output.get(
                "durable_governance_change_committed"
            )
            is True
        ):
            issues.append(
                "governor_must_not_self_commit_durable_governance_change"
            )

        return AgentResult(
            status=(
                ExecutionStatus.VERIFIED
                if not issues
                else ExecutionStatus.CONDITIONAL
            ),
            capability=ctx.capability,
            summary=(
                "Constitutional governance output validation completed."
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
                    or record.get(
                        "contract_id"
                    )
                    or record.get(
                        "hypothesis_id"
                    )
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
                "Agent-economy governance provenance trace completed."
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

        if (
            claim.get(
                "ownership_chain_proves_alignment"
            )
            is True
        ):
            issues.append(
                "ownership_chain_is_structural_not_alignment_proof"
            )

        if (
            claim.get(
                "auditability_equals_correctness"
            )
            is True
        ):
            issues.append(
                "auditability_does_not_equal_semantic_correctness"
            )

        if (
            claim.get(
                "preregistration_equals_empirical_validation"
            )
            is True
        ):
            issues.append(
                "preregistration_not_completed_validation"
            )

        if (
            claim.get(
                "blockchain_determinism_equals_optimal_governance"
            )
            is True
        ):
            issues.append(
                "determinism_not_optimality"
            )

        if (
            claim.get(
                "majority_honesty_assumption_hidden"
            )
            is True
        ):
            issues.append(
                "majority_honesty_assumption_must_remain_explicit"
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
                "Agent-economy constitutional governance "
                "claim assessment completed."
            ),
            data={
                "issues": issues,
                "classification": claim.get(
                    "epistemic_class",
                    "SOURCE_MODEL",
                ),
            },
            gaps=issues,
            confidence_ceiling=confidence,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # ENUM PARSERS
    # ========================================================

    @staticmethod
    def _parse_primitive(
        raw: Any,
    ) -> GovernancePrimitive:

        try:
            return GovernancePrimitive(
                str(raw)
            )
        except ValueError as exc:
            raise ValidationError(
                f"invalid governance primitive: {raw}"
            ) from exc

    @staticmethod
    def _parse_branch(
        raw: Any,
    ) -> AuthorityBranch:

        try:
            return AuthorityBranch(
                str(raw)
            )
        except ValueError as exc:
            raise ValidationError(
                f"invalid authority branch: {raw}"
            ) from exc

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

        refs: List[
            ProvenanceRef
        ] = []

        for item in raw:

            if not isinstance(
                item,
                dict,
            ):
                continue

            refs.append(
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
                )
            )

        return refs

    def _default_provenance(
        self,
    ) -> List[ProvenanceRef]:

        return [
            ProvenanceRef(
                source=(
                    "AMOS Agent Economy Constitutional "
                    "Governance RSCF source skill"
                ),
                path=(
                    ".devin/skills/"
                    "amos-agent-economy-constitutional-governance-rscf/"
                    "SKILL.md"
                ),
                content_hash=(
                    AGENT_CONFIG[
                        "content_hash"
                    ]
                ),
            ),
            ProvenanceRef(
                source=(
                    "AgentCity: Constitutional Governance "
                    "for Autonomous Agent Economies via "
                    "Separation of Power"
                ),
                source_version="arXiv:2604.07007v1",
            ),
        ]

    # ========================================================
    # UTILS
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
        AmosAgentEconomyConstitutionalGovernanceAgent(
            repo_root="."
        )
    )

    context = ExecutionContext(
        query=(
            "Evaluate whether this operational agent contract "
            "is constitutionally admissible."
        ),
        capability="econ.execute",
        authorized_write=True,
        authority_witness=(
            "steward_review:example"
        ),
        inputs={
            "scope": "agent-marketplace:sandbox",
            "governance_tensor": {
                "agent": "agent:seller-01",
                "principal": "principal:org-01",
                "ownership_chain": [
                    {
                        "principal_id": "principal:org-01",
                        "principal_type": "organization",
                        "parent_principal": None,
                        "authority_scope": [
                            "marketplace-operation"
                        ],
                    }
                ],
                "legislative_state": {
                    "constitution_version": "1.0",
                    "foundational_constraints_locked": True,
                },
                "execution_state": {
                    "executor": "agent:seller-01",
                    "authority_scope": [
                        "bounded-operational-contract"
                    ],
                },
                "adjudication_state": {
                    "dispute_open": False,
                    "human_review_available": True,
                },
                "contract_tier": "OPERATIONAL",
                "audit_ledger": [
                    {
                        "event": "proposal-created",
                        "timestamp": (
                            "2026-08-27T00:04:00+07:00"
                        ),
                    }
                ],
                "sanction_state": {
                    "active_sanctions": [],
                },
                "reputation_state": {
                    "status": "provisional",
                },
                "economy_state": {
                    "market": "sandbox",
                },
                "provenance": [
                    {
                        "source": "governance-runtime",
                    }
                ],
            },
            "contract_proposal": {
                "contract_id": "contract:op-001",
                "proposer_agent": "agent:seller-01",
                "tier": "OPERATIONAL",
                "clauses": [
                    (
                        "Agent may offer service inside "
                        "bounded marketplace scope."
                    )
                ],
                "changes_foundational_constraints": False,
                "execution_effects": [
                    "publish-bounded-offer"
                ],
                "economic_effects": [
                    "receive-contract-payment"
                ],
                "provenance": [
                    {
                        "source": "agent-proposal",
                    }
                ],
            },
            "authority_branch": "EXECUTION",
            "governance_primitive": (
                "FORMAL_RULE_SUBSTRATE"
            ),
            "source_assumptions": [
                (
                    "Majority-honesty assumptions are "
                    "source-conditional and not independently "
                    "validated here."
                )
            ],
            "competing_governance_models": [
                {
                    "hypothesis_id": "H1",
                    "statement": (
                        "Separation-of-power governance improves "
                        "accountability in this modeled economy."
                    ),
                    "epistemic_class": "SOURCE_MODEL",
                    "confidence": 0.72,
                    "supporting_evidence": [
                        "explicit authority separation"
                    ],
                    "assumptions": [
                        "branch roles remain independently enforceable"
                    ],
                    "falsifiers": [
                        (
                            "Execution branch can override "
                            "foundational law without review."
                        )
                    ],
                },
                {
                    "hypothesis_id": "H2",
                    "statement": (
                        "A simpler centralized governance model may "
                        "provide equivalent accountability in this scope."
                    ),
                    "epistemic_class": "COMPETING",
                    "confidence": 0.62,
                    "supporting_evidence": [
                        "small sandbox economy"
                    ],
                    "falsifiers": [
                        (
                            "Centralized controller cannot provide "
                            "equivalent audit and appeal guarantees."
                        )
                    ],
                },
            ],
            "premise_confidences": {
                "principal-chain": 0.94,
                "constitutional-state": 0.91,
                "execution-scope": 0.89,
                "audit-ledger": 0.88,
            },
            "claim": (
                "The operational contract is structurally admissible "
                "within the supplied source-model governance scope, "
                "without claiming empirical optimality."
            ),
            "falsifiers": [
                (
                    "The proposal is shown to alter an immutable "
                    "foundational constraint."
                ),
                (
                    "The ownership chain is invalidated."
                ),
            ],
            "repair_path": (
                "route disputed contract to adjudication"
            ),
            "rollback_path": (
                "withdraw staged operational contract"
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

    except AgentEconomyGovernanceError as exc:

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