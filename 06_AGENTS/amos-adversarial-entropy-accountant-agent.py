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
# AMOS ADVERSARIAL ENTROPY ACCOUNTANT AGENT
# ============================================================

AGENT_ID = "amos-adversarial-entropy-accountant-agent"
AGENT_VERSION = "1.0.0"


# ============================================================
# ENUMS
# ============================================================

class EpistemicClass(str, Enum):
    SOURCE = "SOURCE"
    DERIVED = "DERIVED"
    AMOS_MODEL = "AMOS_MODEL"
    EMPIRICAL = "EMPIRICAL"
    COMPETING = "COMPETING"
    UNKNOWN = "UNKNOWN/GAP"


class ExecutionStatus(str, Enum):
    VERIFIED = "VERIFIED"
    CONDITIONAL = "CONDITIONAL"
    COMPETING = "COMPETING"
    MODEL = "MODEL"
    UNKNOWN = "UNKNOWN/GAP"
    REJECTED = "REJECTED"


class SideEffect(str, Enum):
    READ = "read"
    WRITE = "write"


class EntropyOrigin(str, Enum):
    ORGANIC = "ORGANIC"
    ADVERSARIAL = "ADVERSARIAL"
    MIXED = "MIXED"
    COMPETING = "COMPETING"
    UNKNOWN = "UNKNOWN/GAP"


class RepairTargetClass(str, Enum):
    ROOT_CAUSE = "ROOT_CAUSE"
    CONTRIBUTOR = "CONTRIBUTOR"
    SYMPTOM = "SYMPTOM"
    DECOY_CANDIDATE = "DECOY_CANDIDATE"
    UNKNOWN = "UNKNOWN/GAP"


# ============================================================
# ERRORS
# ============================================================

class AdversarialEntropyError(RuntimeError):
    pass


class ValidationError(AdversarialEntropyError):
    pass


class AuthorizationError(AdversarialEntropyError):
    pass


class GapError(AdversarialEntropyError):
    pass


# ============================================================
# DATA CONTRACTS
# ============================================================

@dataclass(frozen=True)
class ProvenanceRef:
    source: str
    path: Optional[str] = None
    content_hash: Optional[str] = None
    event_id: Optional[str] = None


@dataclass
class CapabilityContract:
    name: str
    description: str
    side_effect: SideEffect


@dataclass
class DegradationObservation:
    observation_id: str
    description: str
    severity: float
    repair_burden: float
    first_observed_at: Optional[str] = None
    affected_components: List[str] = field(default_factory=list)
    provenance: List[ProvenanceRef] = field(default_factory=list)


@dataclass
class FailureMechanism:
    mechanism_id: str
    description: str
    origin: EntropyOrigin
    confidence: float

    hidden: bool = False
    delayed: bool = False
    strategically_shaped: bool = False

    supporting_evidence: List[str] = field(default_factory=list)
    conflicting_evidence: List[str] = field(default_factory=list)

    falsifiers: List[str] = field(default_factory=list)
    provenance: List[ProvenanceRef] = field(default_factory=list)


@dataclass
class RepairTarget:
    target_id: str
    description: str
    target_class: RepairTargetClass
    repair_cost: float
    expected_burden_reduction: float
    reversibility: float
    evidence: List[str] = field(default_factory=list)


@dataclass
class BurdenMap:
    organic_burden: float
    adversarial_added_burden: float
    detection_delay: float
    cascade_amplification: float
    total_modeled_burden: float


@dataclass
class Hypothesis:
    hypothesis_id: str
    statement: str
    origin: EntropyOrigin
    confidence: float
    evidence: List[str] = field(default_factory=list)
    counterevidence: List[str] = field(default_factory=list)
    falsifiers: List[str] = field(default_factory=list)


@dataclass
class DiscriminatingTest:
    test_id: str
    description: str
    distinguishes: List[str]
    expected_information_gain: float
    cost: float
    reversible: bool = True


@dataclass
class SecurityAssessment:
    burden_map: BurdenMap
    attack_hypothesis: Optional[Hypothesis]
    organic_alternative: Optional[Hypothesis]
    hypothesis_state: EntropyOrigin
    discriminating_test: Optional[DiscriminatingTest]
    repair_priority: List[RepairTarget]
    containment_actions: List[str]
    confidence_ceiling: float


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
    "display_name": "Adversarial Entropy Accountant",
    "description": (
        "AMOS Adversarial Entropy Accountant — distinguishes organic "
        "degradation from candidate adversarially shaped repair burden, "
        "delayed failures, decoy repair targets, and cascade amplification."
    ),
    "version": AGENT_VERSION,
    "author": "Trang Phan",
    "steward": "Trang Phan",
    "system": "AMOS_OS",
    "role": (
        "Security and trust specialist for separating organic entropy "
        "from potentially adversarially injected or strategically shaped "
        "degradation while preserving competing hypotheses."
    ),
    "primary_skill": "amos-adversarial-entropy-accountant",
    "skill_path": (
        ".devin/skills/"
        "amos-adversarial-entropy-accountant/"
        "SKILL.md"
    ),
    "workflow": (
        "amos-adversarial-entropy-accountant-workflow.md"
    ),
    "epistemic_class": "AMOS_MODEL",
    "claim_ceiling": 0.95,
    "owner_team": "AMOS_CORE",
    "business_domain": "security",
    "risk_tier": "medium",
    "observability": "structured_logs+content_hash",
    "approval_mode": "steward_review",
    "promotion_state": "production",
    "content_hash": "b15bf94fd05d48e9",
}


CAPABILITIES: Dict[str, CapabilityContract] = {
    "security.execute": CapabilityContract(
        name="security.execute",
        description=(
            "Analyze degradation and repair burden, distinguish organic "
            "versus candidate adversarial mechanisms, identify decoy "
            "targets, and propose reversible containment and repair priority."
        ),
        side_effect=SideEffect.WRITE,
    ),
    "security.validate": CapabilityContract(
        name="security.validate",
        description=(
            "Validate adversarial entropy conclusions against evidence, "
            "hypothesis preservation, attribution boundaries, and repair logic."
        ),
        side_effect=SideEffect.READ,
    ),
    "security.trace_provenance": CapabilityContract(
        name="security.trace_provenance",
        description=(
            "Trace degradation, attack hypotheses, repair targets, and "
            "burden estimates to their underlying evidence."
        ),
        side_effect=SideEffect.READ,
    ),
    "security.assess_claim": CapabilityContract(
        name="security.assess_claim",
        description=(
            "Assess claims about adversarial shaping, attribution, hidden "
            "failure mechanisms, and repair burden."
        ),
        side_effect=SideEffect.READ,
    ),
}


# ============================================================
# MAIN AGENT
# ============================================================

class AmosAdversarialEntropyAccountantAgent:
    """
    Runtime implementation of amos-adversarial-entropy-accountant.

    Core rule:
        Do not assume every failure is honestly generated by the system itself.

    Workflow:
        1. Define observed degradation and repair burden.
        2. Separate organic entropy from candidate adversarial injection.
        3. Trace hidden/delayed/strategically shaped mechanisms.
        4. Detect decoy or symptom-level repair targets.
        5. Preserve organic and adversarial COMPETING hypotheses.
        6. Estimate added repair cost, detection delay, cascade amplification.
        7. Prefer reversible containment while attribution is uncertain.
        8. Return burden map, attack hypothesis, organic alternative,
           discriminating test, and repair priority.
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
            / "amos-adversarial-entropy-accountant"
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
            "security.execute": self._execute_analysis,
            "security.validate": self._validate_assessment,
            "security.trace_provenance": self._trace_provenance,
            "security.assess_claim": self._assess_claim,
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

        capability = CAPABILITIES.get(ctx.capability)

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
    # SKILL + AUTHORITY
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

        if capability.side_effect != SideEffect.WRITE:
            return

        if not ctx.authorized_write:
            raise AuthorizationError(
                f"{capability.name} is write-classified. "
                "Capability does not imply authority."
            )

        if not ctx.authority_witness:
            raise AuthorizationError(
                "Write-classified security operation requires "
                "an authority_witness."
            )

    # ========================================================
    # EXECUTE
    # ========================================================

    def _execute_analysis(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        observations = self._parse_observations(
            ctx.inputs.get(
                "observations",
                [],
            )
        )

        if not observations:
            raise GapError(
                "UNKNOWN/GAP: at least one degradation observation "
                "is required."
            )

        mechanisms = self._parse_mechanisms(
            ctx.inputs.get(
                "failure_mechanisms",
                [],
            )
        )

        repair_targets = self._parse_repair_targets(
            ctx.inputs.get(
                "repair_targets",
                [],
            )
        )

        organic_hypothesis = self._build_organic_hypothesis(
            mechanisms
        )

        attack_hypothesis = self._build_attack_hypothesis(
            mechanisms
        )

        hypothesis_state = self._hypothesis_state(
            organic_hypothesis,
            attack_hypothesis,
        )

        burden_map = self._build_burden_map(
            observations=observations,
            mechanisms=mechanisms,
            raw=ctx.inputs.get(
                "burden_metrics",
                {},
            ),
        )

        repair_priority = self._rank_repair_targets(
            repair_targets
        )

        discriminating_test = (
            self._select_discriminating_test(
                organic_hypothesis,
                attack_hypothesis,
                ctx.inputs.get(
                    "candidate_tests",
                    [],
                ),
            )
        )

        containment = self._containment_actions(
            hypothesis_state=hypothesis_state,
            repair_priority=repair_priority,
        )

        confidence = self._confidence_ceiling(
            ctx.inputs.get(
                "premise_confidences",
                {},
            )
        )

        assessment = SecurityAssessment(
            burden_map=burden_map,
            attack_hypothesis=attack_hypothesis,
            organic_alternative=organic_hypothesis,
            hypothesis_state=hypothesis_state,
            discriminating_test=discriminating_test,
            repair_priority=repair_priority,
            containment_actions=containment,
            confidence_ceiling=confidence,
        )

        if hypothesis_state == EntropyOrigin.COMPETING:
            status = ExecutionStatus.COMPETING
        elif hypothesis_state == EntropyOrigin.UNKNOWN:
            status = ExecutionStatus.UNKNOWN
        else:
            status = ExecutionStatus.CONDITIONAL

        return AgentResult(
            status=status,
            capability=ctx.capability,
            summary=(
                "Adversarial entropy accounting completed. "
                f"Hypothesis state: {hypothesis_state.value}."
            ),
            data={
                "assessment": asdict(assessment),
                "attribution_finalized": False,
                "containment_mode": "REVERSIBLE_FIRST",
                "external_action_committed": False,
            },
            warnings=[
                (
                    "Candidate adversarial shaping is not attribution "
                    "to a specific actor."
                ),
                (
                    "Burden, delay, and amplification scores are "
                    "AMOS_MODEL accounting quantities unless independently "
                    "calibrated."
                ),
                (
                    "Preserve organic and adversarial hypotheses until "
                    "a discriminating test resolves them."
                ),
            ],
            confidence_ceiling=confidence,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # OBSERVATIONS
    # ========================================================

    def _parse_observations(
        self,
        raw: Any,
    ) -> List[DegradationObservation]:

        if not isinstance(raw, list):
            raise ValidationError(
                "observations must be a list"
            )

        result: List[DegradationObservation] = []

        for index, item in enumerate(raw):

            if not isinstance(item, dict):
                raise ValidationError(
                    f"observations[{index}] must be a dictionary"
                )

            provenance: List[ProvenanceRef] = []

            for p in item.get("provenance", []):
                if isinstance(p, dict):
                    provenance.append(
                        ProvenanceRef(
                            source=str(
                                p.get("source", "")
                            ),
                            path=p.get("path"),
                            content_hash=p.get(
                                "content_hash"
                            ),
                            event_id=p.get(
                                "event_id"
                            ),
                        )
                    )

            result.append(
                DegradationObservation(
                    observation_id=str(
                        item.get(
                            "observation_id",
                            f"O{index + 1}",
                        )
                    ),
                    description=str(
                        item.get(
                            "description",
                            "",
                        )
                    ),
                    severity=_clamp01(
                        item.get(
                            "severity",
                            0.0,
                        )
                    ),
                    repair_burden=_nonnegative(
                        item.get(
                            "repair_burden",
                            0.0,
                        )
                    ),
                    first_observed_at=item.get(
                        "first_observed_at"
                    ),
                    affected_components=list(
                        item.get(
                            "affected_components",
                            [],
                        )
                    ),
                    provenance=provenance,
                )
            )

        return result

    # ========================================================
    # MECHANISMS
    # ========================================================

    def _parse_mechanisms(
        self,
        raw: Any,
    ) -> List[FailureMechanism]:

        if not isinstance(raw, list):
            raise ValidationError(
                "failure_mechanisms must be a list"
            )

        mechanisms: List[FailureMechanism] = []

        for index, item in enumerate(raw):

            if not isinstance(item, dict):
                continue

            try:
                origin = EntropyOrigin(
                    item.get(
                        "origin",
                        "UNKNOWN/GAP",
                    )
                )
            except ValueError:
                origin = EntropyOrigin.UNKNOWN

            provenance: List[ProvenanceRef] = []

            for p in item.get(
                "provenance",
                [],
            ):
                if isinstance(p, dict):
                    provenance.append(
                        ProvenanceRef(
                            source=str(
                                p.get(
                                    "source",
                                    "",
                                )
                            ),
                            path=p.get("path"),
                            content_hash=p.get(
                                "content_hash"
                            ),
                            event_id=p.get(
                                "event_id"
                            ),
                        )
                    )

            mechanisms.append(
                FailureMechanism(
                    mechanism_id=str(
                        item.get(
                            "mechanism_id",
                            f"M{index + 1}",
                        )
                    ),
                    description=str(
                        item.get(
                            "description",
                            "",
                        )
                    ),
                    origin=origin,
                    confidence=min(
                        _clamp01(
                            item.get(
                                "confidence",
                                0.0,
                            )
                        ),
                        self.claim_ceiling,
                    ),
                    hidden=bool(
                        item.get(
                            "hidden",
                            False,
                        )
                    ),
                    delayed=bool(
                        item.get(
                            "delayed",
                            False,
                        )
                    ),
                    strategically_shaped=bool(
                        item.get(
                            "strategically_shaped",
                            False,
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
                    provenance=provenance,
                )
            )

        return mechanisms

    # ========================================================
    # HYPOTHESES
    # ========================================================

    def _build_organic_hypothesis(
        self,
        mechanisms: List[FailureMechanism],
    ) -> Optional[Hypothesis]:

        organic = [
            m
            for m in mechanisms
            if m.origin in {
                EntropyOrigin.ORGANIC,
                EntropyOrigin.MIXED,
            }
        ]

        if not organic:
            return None

        confidence = min(
            (
                min(
                    m.confidence
                    for m in organic
                )
            ),
            self.claim_ceiling,
        )

        return Hypothesis(
            hypothesis_id="H_ORGANIC",
            statement=(
                "Observed degradation may be explained by "
                "organic system failure or accumulated repair debt."
            ),
            origin=EntropyOrigin.ORGANIC,
            confidence=confidence,
            evidence=[
                evidence
                for mechanism in organic
                for evidence in mechanism.supporting_evidence
            ],
            counterevidence=[
                evidence
                for mechanism in organic
                for evidence in mechanism.conflicting_evidence
            ],
            falsifiers=[
                falsifier
                for mechanism in organic
                for falsifier in mechanism.falsifiers
            ],
        )

    def _build_attack_hypothesis(
        self,
        mechanisms: List[FailureMechanism],
    ) -> Optional[Hypothesis]:

        adversarial = [
            m
            for m in mechanisms
            if (
                m.origin
                in {
                    EntropyOrigin.ADVERSARIAL,
                    EntropyOrigin.MIXED,
                }
                or m.strategically_shaped
            )
        ]

        if not adversarial:
            return None

        confidence = min(
            min(
                m.confidence
                for m in adversarial
            ),
            self.claim_ceiling,
        )

        return Hypothesis(
            hypothesis_id="H_ADVERSARIAL",
            statement=(
                "Observed degradation may include hidden, delayed, "
                "or strategically shaped adversarial burden."
            ),
            origin=EntropyOrigin.ADVERSARIAL,
            confidence=confidence,
            evidence=[
                evidence
                for mechanism in adversarial
                for evidence in mechanism.supporting_evidence
            ],
            counterevidence=[
                evidence
                for mechanism in adversarial
                for evidence in mechanism.conflicting_evidence
            ],
            falsifiers=[
                falsifier
                for mechanism in adversarial
                for falsifier in mechanism.falsifiers
            ],
        )

    def _hypothesis_state(
        self,
        organic: Optional[Hypothesis],
        attack: Optional[Hypothesis],
    ) -> EntropyOrigin:

        if organic and attack:
            # Preserve competition unless the evidence genuinely
            # discriminates one explanation.
            return EntropyOrigin.COMPETING

        if attack:
            return EntropyOrigin.ADVERSARIAL

        if organic:
            return EntropyOrigin.ORGANIC

        return EntropyOrigin.UNKNOWN

    # ========================================================
    # BURDEN ACCOUNTING
    # ========================================================

    def _build_burden_map(
        self,
        observations: List[DegradationObservation],
        mechanisms: List[FailureMechanism],
        raw: Any,
    ) -> BurdenMap:
        """
        This accounting is explicitly AMOS_MODEL.

        It is a prioritization / decomposition model, not an empirical law.
        """

        if not isinstance(raw, dict):
            raw = {}

        observed_burden = sum(
            observation.repair_burden
            for observation in observations
        )

        organic_weight = sum(
            mechanism.confidence
            for mechanism in mechanisms
            if mechanism.origin
            in {
                EntropyOrigin.ORGANIC,
                EntropyOrigin.MIXED,
            }
        )

        adversarial_weight = sum(
            mechanism.confidence
            for mechanism in mechanisms
            if (
                mechanism.origin
                in {
                    EntropyOrigin.ADVERSARIAL,
                    EntropyOrigin.MIXED,
                }
                or mechanism.strategically_shaped
            )
        )

        total_weight = (
            organic_weight
            + adversarial_weight
        )

        if total_weight > 0:
            organic_fraction = (
                organic_weight
                / total_weight
            )
            adversarial_fraction = (
                adversarial_weight
                / total_weight
            )
        else:
            organic_fraction = 0.0
            adversarial_fraction = 0.0

        organic_burden = float(
            raw.get(
                "organic_burden",
                observed_burden
                * organic_fraction,
            )
        )

        adversarial_added_burden = float(
            raw.get(
                "adversarial_added_burden",
                observed_burden
                * adversarial_fraction,
            )
        )

        detection_delay = _nonnegative(
            raw.get(
                "detection_delay",
                sum(
                    1.0
                    for m in mechanisms
                    if m.delayed or m.hidden
                ),
            )
        )

        cascade_amplification = _nonnegative(
            raw.get(
                "cascade_amplification",
                1.0
                + 0.25
                * sum(
                    1
                    for m in mechanisms
                    if m.strategically_shaped
                ),
            )
        )

        total_modeled_burden = (
            organic_burden
            + adversarial_added_burden
        ) * max(
            1.0,
            cascade_amplification,
        )

        return BurdenMap(
            organic_burden=organic_burden,
            adversarial_added_burden=(
                adversarial_added_burden
            ),
            detection_delay=detection_delay,
            cascade_amplification=(
                cascade_amplification
            ),
            total_modeled_burden=(
                total_modeled_burden
            ),
        )

    # ========================================================
    # REPAIR TARGETS / DECOYS
    # ========================================================

    def _parse_repair_targets(
        self,
        raw: Any,
    ) -> List[RepairTarget]:

        if not isinstance(raw, list):
            raise ValidationError(
                "repair_targets must be a list"
            )

        targets: List[RepairTarget] = []

        for index, item in enumerate(raw):

            if not isinstance(item, dict):
                continue

            try:
                target_class = RepairTargetClass(
                    item.get(
                        "target_class",
                        "UNKNOWN/GAP",
                    )
                )
            except ValueError:
                target_class = (
                    RepairTargetClass.UNKNOWN
                )

            targets.append(
                RepairTarget(
                    target_id=str(
                        item.get(
                            "target_id",
                            f"R{index + 1}",
                        )
                    ),
                    description=str(
                        item.get(
                            "description",
                            "",
                        )
                    ),
                    target_class=target_class,
                    repair_cost=_nonnegative(
                        item.get(
                            "repair_cost",
                            0.0,
                        )
                    ),
                    expected_burden_reduction=(
                        _nonnegative(
                            item.get(
                                "expected_burden_reduction",
                                0.0,
                            )
                        )
                    ),
                    reversibility=_clamp01(
                        item.get(
                            "reversibility",
                            0.0,
                        )
                    ),
                    evidence=list(
                        item.get(
                            "evidence",
                            [],
                        )
                    ),
                )
            )

        return targets

    def _rank_repair_targets(
        self,
        targets: List[RepairTarget],
    ) -> List[RepairTarget]:

        priority_weight = {
            RepairTargetClass.ROOT_CAUSE: 1.00,
            RepairTargetClass.CONTRIBUTOR: 0.75,
            RepairTargetClass.SYMPTOM: 0.30,
            RepairTargetClass.DECOY_CANDIDATE: 0.05,
            RepairTargetClass.UNKNOWN: 0.10,
        }

        def score(
            target: RepairTarget,
        ) -> float:

            benefit = (
                target.expected_burden_reduction
                + target.reversibility
            )

            cost = max(
                target.repair_cost,
                0.01,
            )

            return (
                priority_weight[
                    target.target_class
                ]
                * benefit
                / cost
            )

        return sorted(
            targets,
            key=score,
            reverse=True,
        )

    # ========================================================
    # DISCRIMINATING TEST
    # ========================================================

    def _select_discriminating_test(
        self,
        organic: Optional[Hypothesis],
        attack: Optional[Hypothesis],
        raw_tests: Any,
    ) -> Optional[DiscriminatingTest]:

        if not organic or not attack:
            return None

        tests: List[DiscriminatingTest] = []

        if isinstance(raw_tests, list):

            for index, item in enumerate(
                raw_tests
            ):

                if not isinstance(
                    item,
                    dict,
                ):
                    continue

                tests.append(
                    DiscriminatingTest(
                        test_id=str(
                            item.get(
                                "test_id",
                                f"T{index + 1}",
                            )
                        ),
                        description=str(
                            item.get(
                                "description",
                                "",
                            )
                        ),
                        distinguishes=list(
                            item.get(
                                "distinguishes",
                                [
                                    "H_ORGANIC",
                                    "H_ADVERSARIAL",
                                ],
                            )
                        ),
                        expected_information_gain=(
                            _clamp01(
                                item.get(
                                    "expected_information_gain",
                                    0.0,
                                )
                            )
                        ),
                        cost=_nonnegative(
                            item.get(
                                "cost",
                                1.0,
                            )
                        ),
                        reversible=bool(
                            item.get(
                                "reversible",
                                True,
                            )
                        ),
                    )
                )

        # If explicit tests exist, prefer best information gain per cost
        # while favoring reversible tests.
        if tests:

            return max(
                tests,
                key=lambda test: (
                    (
                        test.expected_information_gain
                        / max(
                            test.cost,
                            0.01,
                        )
                    )
                    * (
                        1.25
                        if test.reversible
                        else 1.0
                    )
                ),
            )

        # Use supplied falsifiers if no explicit test exists.
        organic_falsifier = (
            organic.falsifiers[0]
            if organic.falsifiers
            else None
        )

        attack_falsifier = (
            attack.falsifiers[0]
            if attack.falsifiers
            else None
        )

        if (
            organic_falsifier
            or attack_falsifier
        ):
            return DiscriminatingTest(
                test_id="T_FALSIFIER",
                description=(
                    organic_falsifier
                    or attack_falsifier
                    or ""
                ),
                distinguishes=[
                    "H_ORGANIC",
                    "H_ADVERSARIAL",
                ],
                expected_information_gain=0.60,
                cost=1.0,
                reversible=True,
            )

        return None

    # ========================================================
    # REVERSIBLE CONTAINMENT
    # ========================================================

    def _containment_actions(
        self,
        hypothesis_state: EntropyOrigin,
        repair_priority: List[RepairTarget],
    ) -> List[str]:

        actions: List[str] = []

        if hypothesis_state in {
            EntropyOrigin.COMPETING,
            EntropyOrigin.UNKNOWN,
        }:
            actions.extend([
                (
                    "isolate suspicious propagation paths "
                    "without deleting evidence"
                ),
                (
                    "preserve logs, provenance, timestamps, "
                    "and affected-state snapshots"
                ),
                (
                    "reduce exposure or privilege through "
                    "reversible controls"
                ),
                (
                    "avoid irreversible attribution-dependent repair "
                    "until hypotheses are discriminated"
                ),
            ])

        if repair_priority:
            top = repair_priority[0]

            if top.target_class in {
                RepairTargetClass.ROOT_CAUSE,
                RepairTargetClass.CONTRIBUTOR,
            }:
                actions.append(
                    f"stage repair of target:{top.target_id}"
                )

            elif top.target_class in {
                RepairTargetClass.SYMPTOM,
                RepairTargetClass.DECOY_CANDIDATE,
            }:
                actions.append(
                    (
                        f"do not prioritize target:{top.target_id} "
                        "without additional causal evidence"
                    )
                )

        return actions

    # ========================================================
    # CONFIDENCE
    # ========================================================

    def _confidence_ceiling(
        self,
        raw: Any,
    ) -> float:

        if not isinstance(raw, dict) or not raw:
            return min(
                0.50,
                self.claim_ceiling,
            )

        weakest = min(
            _clamp01(value)
            for value
            in raw.values()
        )

        return min(
            weakest,
            self.claim_ceiling,
        )

    # ========================================================
    # VALIDATE
    # ========================================================

    def _validate_assessment(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        assessment = ctx.inputs.get(
            "assessment"
        )

        if not isinstance(
            assessment,
            dict,
        ):
            raise GapError(
                "UNKNOWN/GAP: assessment dictionary required."
            )

        issues: List[str] = []

        required = [
            "burden_map",
            "attack_hypothesis",
            "organic_alternative",
            "hypothesis_state",
            "repair_priority",
            "containment_actions",
        ]

        for key in required:
            if key not in assessment:
                issues.append(
                    f"missing:{key}"
                )

        if (
            assessment.get(
                "hypothesis_state"
            )
            == "ADVERSARIAL"
            and not assessment.get(
                "attack_hypothesis"
            )
        ):
            issues.append(
                "adversarial_class_without_attack_hypothesis"
            )

        if (
            assessment.get(
                "attribution_finalized"
            )
            is True
            and assessment.get(
                "hypothesis_state"
            )
            in {
                "COMPETING",
                "UNKNOWN/GAP",
            }
        ):
            issues.append(
                "attribution_finalized_while_uncertain"
            )

        repair_priority = assessment.get(
            "repair_priority",
            [],
        )

        if repair_priority:
            first = repair_priority[0]

            if (
                isinstance(first, dict)
                and first.get(
                    "target_class"
                )
                == "DECOY_CANDIDATE"
            ):
                issues.append(
                    "decoy_candidate_ranked_as_top_repair"
                )

        return AgentResult(
            status=(
                ExecutionStatus.VERIFIED
                if not issues
                else ExecutionStatus.CONDITIONAL
            ),
            capability=ctx.capability,
            summary=(
                "Adversarial entropy assessment validation completed."
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
    # PROVENANCE
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
                    record.get("id")
                    or record.get(
                        "observation_id"
                    )
                    or record.get(
                        "mechanism_id"
                    )
                    or record.get(
                        "target_id"
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
                "Adversarial entropy provenance tracing completed."
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
                "failure_implies_attack"
            )
            is True
        ):
            issues.append(
                "failure_does_not_imply_adversarial_origin"
            )

        if (
            claim.get(
                "adversarial_hypothesis_as_attribution"
            )
            is True
        ):
            issues.append(
                "attack_hypothesis_is_not_actor_attribution"
            )

        if (
            claim.get(
                "symptom_repair_as_root_cause_proof"
            )
            is True
        ):
            issues.append(
                "symptom_repair_does_not_establish_root_cause"
            )

        if (
            claim.get(
                "entropy_accounting_as_empirical_law"
            )
            is True
        ):
            issues.append(
                "entropy_accounting_is_amos_model"
            )

        return AgentResult(
            status=(
                ExecutionStatus.CONDITIONAL
                if issues
                else ExecutionStatus.MODEL
            ),
            capability=ctx.capability,
            summary=(
                "Adversarial entropy claim assessment completed."
            ),
            data={
                "issues": issues,
                "classification": "AMOS_MODEL",
            },
            gaps=issues,
            confidence_ceiling=self.claim_ceiling,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # DEFAULT PROVENANCE
    # ========================================================

    def _default_provenance(
        self,
    ) -> List[ProvenanceRef]:

        return [
            ProvenanceRef(
                source=(
                    "AMOS Adversarial Entropy Accountant "
                    "source skill"
                ),
                path=(
                    ".devin/skills/"
                    "amos-adversarial-entropy-accountant/"
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
        AmosAdversarialEntropyAccountantAgent(
            repo_root="."
        )
    )

    ctx = ExecutionContext(
        query=(
            "Determine whether the recent degradation is organic "
            "or potentially adversarially shaped."
        ),
        capability="security.execute",
        authorized_write=True,
        authority_witness=(
            "steward_review:example"
        ),
        inputs={
            "observations": [
                {
                    "observation_id": "O1",
                    "description": (
                        "Repair load increased after a sequence "
                        "of configuration changes."
                    ),
                    "severity": 0.72,
                    "repair_burden": 8.0,
                    "affected_components": [
                        "config-loader",
                        "runtime-policy",
                    ],
                    "provenance": [
                        {
                            "source": "incident-log",
                            "event_id": "INC-001",
                        }
                    ],
                }
            ],
            "failure_mechanisms": [
                {
                    "mechanism_id": "M1",
                    "description": (
                        "Organic configuration drift."
                    ),
                    "origin": "ORGANIC",
                    "confidence": 0.68,
                    "supporting_evidence": [
                        "multiple stale configuration branches"
                    ],
                    "falsifiers": [
                        (
                            "Fresh controlled rebuild reproduces "
                            "the failure without drift."
                        )
                    ],
                },
                {
                    "mechanism_id": "M2",
                    "description": (
                        "Strategically delayed malformed state "
                        "introduced through a privileged path."
                    ),
                    "origin": "ADVERSARIAL",
                    "confidence": 0.61,
                    "hidden": True,
                    "delayed": True,
                    "strategically_shaped": True,
                    "supporting_evidence": [
                        "unexpected privileged state transition"
                    ],
                    "falsifiers": [
                        (
                            "Audit proves transition was generated "
                            "by expected automation with intact provenance."
                        )
                    ],
                },
            ],
            "repair_targets": [
                {
                    "target_id": "R1",
                    "description": (
                        "Patch visible error handler."
                    ),
                    "target_class": "SYMPTOM",
                    "repair_cost": 1.0,
                    "expected_burden_reduction": 1.0,
                    "reversibility": 0.95,
                },
                {
                    "target_id": "R2",
                    "description": (
                        "Quarantine privileged configuration mutation path."
                    ),
                    "target_class": "CONTRIBUTOR",
                    "repair_cost": 2.0,
                    "expected_burden_reduction": 6.0,
                    "reversibility": 0.90,
                },
            ],
            "candidate_tests": [
                {
                    "test_id": "T1",
                    "description": (
                        "Replay configuration lineage against a clean "
                        "trusted baseline and compare privileged transitions."
                    ),
                    "distinguishes": [
                        "H_ORGANIC",
                        "H_ADVERSARIAL",
                    ],
                    "expected_information_gain": 0.90,
                    "cost": 1.5,
                    "reversible": True,
                }
            ],
            "premise_confidences": {
                "incident_log": 0.92,
                "configuration_lineage": 0.81,
                "privileged_transition_trace": 0.76,
            },
        },
    )

    try:

        result = agent.run(
            ctx
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

    except AdversarialEntropyError as exc:

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