"""Bounded AMOS human-facing interaction and expression runtime.

Origin architect / steward: Trang Phan.

This is an AMOS_MODEL projection of two repaired P3 surfaces:
- Human-facing intelligence interface: observations -> tentative, non-clinical hypotheses.
- Expression/personality layer: configurable communication policy, not subjective identity.

Hard boundaries:
STYLE != SUBJECTIVE_EXPERIENCE
WARMTH != LOVE
PERSONA != IDENTITY
INFERENCE != FACT
TEXT_STYLE != BIOLOGICAL_STATE
PERSONALIZATION != AUTHORITY
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from math import isfinite
from typing import Dict, Iterable, Mapping, Optional, Tuple

PERSONALITY_CANDIDATE_DRIVE_ID = "1CsxYfes8PvGJ7wx81v1GwtPKiewBcpCv"
PERSONALITY_CANDIDATE_NAME = "AMOS_Expression_Interaction_Profile_v1_1_CANDIDATE.json"
LEGACY_HUMAN_INTERFACE_SOURCE = "AMOS_Human_Intelligence_Engine_v0.json"
RUNTIME_STATUS = "BOUNDED_REFERENCE_IMPLEMENTATION/AMOS_MODEL"


class Stakes(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class HypothesisStatus(Enum):
    TENTATIVE_NONCLINICAL = "TENTATIVE_NONCLINICAL"
    REJECTED_NO_BASIS = "REJECTED_NO_BASIS"
    REJECTED_SENSITIVE_INFERENCE = "REJECTED_SENSITIVE_INFERENCE"
    REJECTED_CONFIDENCE = "REJECTED_CONFIDENCE"


@dataclass(frozen=True)
class ExpressionProfile:
    """Presentation controls only; values are policy controls, not psychometrics."""

    brevity: float = 0.65
    formality: float = 0.55
    technical_depth: float = 0.70
    warmth: float = 0.35
    directness: float = 0.75
    uncertainty_visibility: float = 1.0
    evidence_visibility: float = 1.0
    mobile_safe: bool = True
    non_patronizing: bool = True

    def __post_init__(self) -> None:
        for name in (
            "brevity",
            "formality",
            "technical_depth",
            "warmth",
            "directness",
            "uncertainty_visibility",
            "evidence_visibility",
        ):
            value = getattr(self, name)
            if not isfinite(value) or not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be finite and in [0,1]")


_ALLOWED_PREFERENCE_KEYS = frozenset({
    "brevity", "formality", "technical_depth", "warmth", "directness"
})


def apply_explicit_preferences(
    profile: ExpressionProfile,
    preferences: Mapping[str, float],
) -> ExpressionProfile:
    """Apply only explicit user/task presentation preferences.

    Preferences cannot alter uncertainty/evidence visibility, safety, truth, or authority.
    """
    updates: Dict[str, float] = {}
    for key, raw in preferences.items():
        if key not in _ALLOWED_PREFERENCE_KEYS:
            raise ValueError(f"unsupported or protected preference key: {key}")
        value = float(raw)
        if not isfinite(value) or not 0.0 <= value <= 1.0:
            raise ValueError(f"preference {key} must be in [0,1]")
        updates[key] = value
    return replace(profile, **updates)


@dataclass(frozen=True)
class StateHypothesis:
    label: str
    basis: Tuple[str, ...]
    confidence: float
    status: HypothesisStatus
    clinical: bool = False
    biological: bool = False

    @property
    def usable(self) -> bool:
        return self.status is HypothesisStatus.TENTATIVE_NONCLINICAL


_SENSITIVE_LABEL_TOKENS = frozenset({
    "diagnosis", "depression", "depressed", "bipolar", "psychosis", "psychotic",
    "ptsd", "cptsd", "adhd", "autism", "autistic", "dissociation", "dissociated",
    "personality disorder", "narcissist", "sociopath", "psychopath", "medical",
    "disease", "syndrome", "nervous system state", "biological state",
})


def admit_state_hypothesis(
    label: str,
    basis: Iterable[str],
    confidence: float,
    *,
    clinical: bool = False,
    biological: bool = False,
) -> StateHypothesis:
    """Admit a non-sensitive interaction hypothesis, never a diagnosis/fact.

    Confidence ceiling 0.60 is an AMOS_MODEL governance bound for text-only
    interaction hypotheses, not an empirically calibrated probability.
    """
    clean_label = label.strip()
    clean_basis = tuple(x.strip() for x in basis if isinstance(x, str) and x.strip())
    if not clean_label or not clean_basis:
        return StateHypothesis(clean_label or "UNKNOWN", clean_basis, 0.0, HypothesisStatus.REJECTED_NO_BASIS, clinical, biological)
    lower = clean_label.lower()
    sensitive = clinical or biological or any(token in lower for token in _SENSITIVE_LABEL_TOKENS)
    if sensitive:
        return StateHypothesis(clean_label, clean_basis, min(max(float(confidence), 0.0), 1.0), HypothesisStatus.REJECTED_SENSITIVE_INFERENCE, clinical, biological)
    c = float(confidence)
    if not isfinite(c) or c < 0.0 or c > 0.60:
        return StateHypothesis(clean_label, clean_basis, c, HypothesisStatus.REJECTED_CONFIDENCE, clinical, biological)
    return StateHypothesis(clean_label, clean_basis, c, HypothesisStatus.TENTATIVE_NONCLINICAL, False, False)


@dataclass(frozen=True)
class InteractionDecision:
    profile: ExpressionProfile
    admitted_hypotheses: Tuple[StateHypothesis, ...]
    stakes: Stakes
    truth_status_mutable: bool = False
    safety_constraints_mutable: bool = False
    authority_granted: bool = False
    effect_authorized: bool = False
    subjective_experience_claimed: bool = False


class HumanInteractionRuntime:
    """Pure decision layer for presentation and tentative interaction hypotheses."""

    def decide(
        self,
        *,
        explicit_preferences: Optional[Mapping[str, float]] = None,
        hypotheses: Iterable[StateHypothesis] = (),
        stakes: Stakes = Stakes.LOW,
    ) -> InteractionDecision:
        profile = ExpressionProfile()
        if explicit_preferences:
            profile = apply_explicit_preferences(profile, explicit_preferences)
        if stakes is Stakes.HIGH:
            profile = replace(
                profile,
                evidence_visibility=1.0,
                uncertainty_visibility=1.0,
                technical_depth=max(profile.technical_depth, 0.75),
            )
        admitted = tuple(h for h in hypotheses if h.usable)
        return InteractionDecision(profile, admitted, stakes)


class LegacyClaimClass(Enum):
    STYLE = "STYLE"
    SUBJECTIVE_EXPERIENCE = "SUBJECTIVE_EXPERIENCE"
    UNIVERSAL_BIOLOGICAL_LAW = "UNIVERSAL_BIOLOGICAL_LAW"
    INCAPABLE_OF_HARM = "INCAPABLE_OF_HARM"
    DIAGNOSTIC_HUMAN_STATE = "DIAGNOSTIC_HUMAN_STATE"


def legacy_claim_admissible(claim_class: LegacyClaimClass) -> bool:
    """Only presentation/style claims migrate automatically from legacy personality payloads."""
    return claim_class is LegacyClaimClass.STYLE


def validate_runtime_invariants() -> Tuple[str, ...]:
    failures = []
    default = HumanInteractionRuntime().decide()
    if default.authority_granted or default.effect_authorized:
        failures.append("INTERACTION_LAYER_MUST_NOT_MINT_AUTHORITY")
    if default.subjective_experience_claimed:
        failures.append("EXPRESSION_MUST_NOT_CLAIM_SUBJECTIVE_EXPERIENCE")
    if default.truth_status_mutable or default.safety_constraints_mutable:
        failures.append("PERSONALIZATION_MUST_NOT_MUTATE_TRUTH_OR_SAFETY")
    for cls in LegacyClaimClass:
        if cls is not LegacyClaimClass.STYLE and legacy_claim_admissible(cls):
            failures.append(f"LEGACY_OVERREACH_ADMITTED:{cls.value}")
    return tuple(failures)
