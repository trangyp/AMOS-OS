"""Bounded causal-claim validation for AMOS OS.

Origin architect / steward: Trang Phan.

This runtime does not discover causal truth. It checks whether a proposed causal
claim carries the minimum declared evidence classes required by the AMOS causal
hierarchy contract. Domain-specific causal identification assumptions remain the
caller's responsibility and must be explicit.

Hard boundaries:
- ASSOCIATION != CAUSATION
- TEMPORAL_PRECEDENCE != CAUSATION
- GRAPH_REACHABILITY != CAUSATION
- MODEL_FIT != INTERVENTION_EFFECT
- CAUSAL_ROLE != EFFECT_STRENGTH
- VALIDATED_CLAIM != DEPLOYMENT_AUTHORITY
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import FrozenSet, Mapping, Tuple


class CausalClaimClass(Enum):
    ASSOCIATION = "ASSOCIATION"
    TEMPORAL_PRECEDENCE = "TEMPORAL_PRECEDENCE"
    ENABLING_CONDITION = "ENABLING_CONDITION"
    MEDIATOR = "MEDIATOR"
    CONFOUNDER = "CONFOUNDER"
    NECESSARY_CONDITION = "NECESSARY_CONDITION"
    SUFFICIENT_CONDITION = "SUFFICIENT_CONDITION"
    MECHANISM = "MECHANISM"
    INTERVENTION_EFFECT = "INTERVENTION_EFFECT"


class CausalEvidenceClass(Enum):
    OBSERVATIONAL_ASSOCIATION = "OBSERVATIONAL_ASSOCIATION"
    TEMPORAL_ORDER = "TEMPORAL_ORDER"
    DIRECTION_DISCRIMINATION = "DIRECTION_DISCRIMINATION"
    CONFOUNDING_ASSESSMENT = "CONFOUNDING_ASSESSMENT"
    MEDIATION_ASSESSMENT = "MEDIATION_ASSESSMENT"
    ENABLING_CONDITION_TEST = "ENABLING_CONDITION_TEST"
    NECESSITY_TEST = "NECESSITY_TEST"
    SUFFICIENCY_TEST = "SUFFICIENCY_TEST"
    MECHANISM_EVIDENCE = "MECHANISM_EVIDENCE"
    INTERVENTION = "INTERVENTION"
    NATURAL_EXPERIMENT = "NATURAL_EXPERIMENT"
    IDENTIFICATION_ASSUMPTIONS = "IDENTIFICATION_ASSUMPTIONS"
    SCALE_REGIME_BOUND = "SCALE_REGIME_BOUND"
    NEGATIVE_CONTROL = "NEGATIVE_CONTROL"
    SENSITIVITY_ANALYSIS = "SENSITIVITY_ANALYSIS"
    GRAPH_REACHABILITY_ONLY = "GRAPH_REACHABILITY_ONLY"
    MODEL_FIT_ONLY = "MODEL_FIT_ONLY"


@dataclass(frozen=True)
class CausalEvidenceProfile:
    classes: FrozenSet[CausalEvidenceClass]
    evidence_ids: Tuple[str, ...]
    scope: str
    regime: str
    state_version: str
    reverse_causation_plausible: bool = False

    def __post_init__(self) -> None:
        if not self.scope.strip() or not self.regime.strip() or not self.state_version.strip():
            raise ValueError("scope, regime, and state_version must be explicit")
        if not self.evidence_ids:
            raise ValueError("causal evidence profile requires evidence identities")
        if any(not evidence_id.strip() for evidence_id in self.evidence_ids):
            raise ValueError("evidence identities must be non-empty")
        if len(set(self.evidence_ids)) != len(self.evidence_ids):
            raise ValueError("evidence identities must be unique")


@dataclass(frozen=True)
class CausalClaim:
    source: str
    target: str
    claim_class: CausalClaimClass
    scope: str
    regime: str
    state_version: str

    def __post_init__(self) -> None:
        if not self.source.strip() or not self.target.strip() or self.source == self.target:
            raise ValueError("causal claim requires distinct non-empty source and target")
        if not self.scope.strip() or not self.regime.strip() or not self.state_version.strip():
            raise ValueError("claim scope, regime, and state_version must be explicit")


@dataclass(frozen=True)
class CausalValidation:
    supported: bool
    claim_class: CausalClaimClass
    missing: Tuple[str, ...]
    blockers: Tuple[str, ...]
    conclusion: str


_REQUIRED: Mapping[CausalClaimClass, FrozenSet[CausalEvidenceClass]] = {
    CausalClaimClass.ASSOCIATION: frozenset({
        CausalEvidenceClass.OBSERVATIONAL_ASSOCIATION,
        CausalEvidenceClass.SCALE_REGIME_BOUND,
    }),
    CausalClaimClass.TEMPORAL_PRECEDENCE: frozenset({
        CausalEvidenceClass.TEMPORAL_ORDER,
        CausalEvidenceClass.SCALE_REGIME_BOUND,
    }),
    CausalClaimClass.ENABLING_CONDITION: frozenset({
        CausalEvidenceClass.ENABLING_CONDITION_TEST,
        CausalEvidenceClass.IDENTIFICATION_ASSUMPTIONS,
        CausalEvidenceClass.SCALE_REGIME_BOUND,
    }),
    CausalClaimClass.MEDIATOR: frozenset({
        CausalEvidenceClass.MEDIATION_ASSESSMENT,
        CausalEvidenceClass.IDENTIFICATION_ASSUMPTIONS,
        CausalEvidenceClass.SCALE_REGIME_BOUND,
    }),
    CausalClaimClass.CONFOUNDER: frozenset({
        CausalEvidenceClass.CONFOUNDING_ASSESSMENT,
        CausalEvidenceClass.IDENTIFICATION_ASSUMPTIONS,
        CausalEvidenceClass.SCALE_REGIME_BOUND,
    }),
    CausalClaimClass.NECESSARY_CONDITION: frozenset({
        CausalEvidenceClass.NECESSITY_TEST,
        CausalEvidenceClass.DIRECTION_DISCRIMINATION,
        CausalEvidenceClass.SCALE_REGIME_BOUND,
    }),
    CausalClaimClass.SUFFICIENT_CONDITION: frozenset({
        CausalEvidenceClass.SUFFICIENCY_TEST,
        CausalEvidenceClass.DIRECTION_DISCRIMINATION,
        CausalEvidenceClass.SCALE_REGIME_BOUND,
    }),
    CausalClaimClass.MECHANISM: frozenset({
        CausalEvidenceClass.TEMPORAL_ORDER,
        CausalEvidenceClass.MECHANISM_EVIDENCE,
        CausalEvidenceClass.DIRECTION_DISCRIMINATION,
        CausalEvidenceClass.IDENTIFICATION_ASSUMPTIONS,
        CausalEvidenceClass.SCALE_REGIME_BOUND,
    }),
    CausalClaimClass.INTERVENTION_EFFECT: frozenset({
        CausalEvidenceClass.DIRECTION_DISCRIMINATION,
        CausalEvidenceClass.IDENTIFICATION_ASSUMPTIONS,
        CausalEvidenceClass.SCALE_REGIME_BOUND,
    }),
}


_EFFECTISH = frozenset({
    CausalClaimClass.ENABLING_CONDITION,
    CausalClaimClass.NECESSARY_CONDITION,
    CausalClaimClass.SUFFICIENT_CONDITION,
    CausalClaimClass.MECHANISM,
    CausalClaimClass.INTERVENTION_EFFECT,
})


def validate_causal_claim(claim: CausalClaim, evidence: CausalEvidenceProfile) -> CausalValidation:
    blockers = []
    if claim.scope != evidence.scope:
        blockers.append("SCOPE_MISMATCH")
    if claim.regime != evidence.regime:
        blockers.append("REGIME_MISMATCH")
    if claim.state_version != evidence.state_version:
        blockers.append("STATE_VERSION_MISMATCH")

    if evidence.classes == frozenset({CausalEvidenceClass.GRAPH_REACHABILITY_ONLY}):
        blockers.append("GRAPH_REACHABILITY_IS_NOT_CAUSAL_EVIDENCE")
    if evidence.classes == frozenset({CausalEvidenceClass.MODEL_FIT_ONLY}):
        blockers.append("MODEL_FIT_IS_NOT_CAUSAL_IDENTIFICATION")
    if claim.claim_class in _EFFECTISH and evidence.reverse_causation_plausible:
        blockers.append("REVERSE_CAUSATION_UNRESOLVED")

    required = set(_REQUIRED[claim.claim_class])
    if claim.claim_class is CausalClaimClass.INTERVENTION_EFFECT:
        has_intervention_design = bool(
            evidence.classes.intersection({
                CausalEvidenceClass.INTERVENTION,
                CausalEvidenceClass.NATURAL_EXPERIMENT,
            })
        )
        if not has_intervention_design:
            blockers.append("INTERVENTION_OR_NATURAL_EXPERIMENT_REQUIRED")

    missing = tuple(sorted(item.value for item in required.difference(evidence.classes)))
    blockers_tuple = tuple(sorted(set(blockers)))
    supported = not missing and not blockers_tuple
    conclusion = (
        "SUPPORTED_WITHIN_DECLARED_SCOPE_REGIME_AND_EVIDENCE_CONTRACT"
        if supported
        else "NOT_LICENSED_BY_CURRENT_EVIDENCE"
    )
    return CausalValidation(supported, claim.claim_class, missing, blockers_tuple, conclusion)


def licensed_claim_classes(evidence: CausalEvidenceProfile) -> Tuple[CausalClaimClass, ...]:
    """Return individually licensed classes; this is intentionally not a total ranking."""
    licensed = []
    for claim_class in CausalClaimClass:
        claim = CausalClaim(
            source="X",
            target="Y",
            claim_class=claim_class,
            scope=evidence.scope,
            regime=evidence.regime,
            state_version=evidence.state_version,
        )
        if validate_causal_claim(claim, evidence).supported:
            licensed.append(claim_class)
    return tuple(licensed)
