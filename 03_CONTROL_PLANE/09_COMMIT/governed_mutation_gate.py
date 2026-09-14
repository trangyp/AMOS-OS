"""Bounded governed-mutation permit gate for AMOS OS.

Origin architect / steward: Trang Phan.

Implements a control-plane subset of GMEF: capability to change is not authority
to change; a candidate cannot rewrite the rules used to approve itself; and a
permitted transition still requires commit-time freshness and effect binding.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import FrozenSet, Optional, Tuple

MUTATION_APPROVE_SCOPE = "mutation:approve"


class MutationClass(Enum):
    M0 = "M0"
    M1 = "M1"
    M2 = "M2"
    M3 = "M3"
    M4 = "M4"
    M5 = "M5"


class EvidenceLevel(IntEnum):
    ET0 = 0
    ET1 = 1
    ET2 = 2
    ET3 = 3
    ET4 = 4
    ET5 = 5


class AuthorityLevel(IntEnum):
    HA0 = 0
    HA1 = 1
    HA2 = 2
    HA3 = 3
    HA4 = 4
    HA5 = 5


class Lifecycle(Enum):
    PROPOSED = "PROPOSED"
    ELIGIBILITY_CHECK = "ELIGIBILITY_CHECK"
    SANDBOXED = "SANDBOXED"
    EXPERIMENTING = "EXPERIMENTING"
    EVIDENCE_PENDING = "EVIDENCE_PENDING"
    CHALLENGED = "CHALLENGED"
    GOVERNANCE_REVIEW = "GOVERNANCE_REVIEW"
    APPROVED_LIMITED = "APPROVED_LIMITED"
    CANARY = "CANARY"
    PRODUCTION_LIMITED = "PRODUCTION_LIMITED"
    PRODUCTION_GENERAL = "PRODUCTION_GENERAL"
    QUARANTINED = "QUARANTINED"
    ROLLED_BACK = "ROLLED_BACK"


class MutationDecision(Enum):
    HOLD = "HOLD"
    BLOCK = "BLOCK"
    ESCALATE_CONSTITUTIONAL = "ESCALATE_CONSTITUTIONAL"
    PREPARED = "PREPARED"
    REVALIDATE = "REVALIDATE"
    COMMITTABLE = "COMMITTABLE"


_ALLOWED_TRANSITIONS = {
    (Lifecycle.PROPOSED, Lifecycle.ELIGIBILITY_CHECK),
    (Lifecycle.ELIGIBILITY_CHECK, Lifecycle.SANDBOXED),
    (Lifecycle.SANDBOXED, Lifecycle.EXPERIMENTING),
    (Lifecycle.EXPERIMENTING, Lifecycle.EVIDENCE_PENDING),
    (Lifecycle.EVIDENCE_PENDING, Lifecycle.CHALLENGED),
    (Lifecycle.CHALLENGED, Lifecycle.GOVERNANCE_REVIEW),
    (Lifecycle.GOVERNANCE_REVIEW, Lifecycle.APPROVED_LIMITED),
    (Lifecycle.APPROVED_LIMITED, Lifecycle.CANARY),
    (Lifecycle.CANARY, Lifecycle.PRODUCTION_LIMITED),
    (Lifecycle.PRODUCTION_LIMITED, Lifecycle.PRODUCTION_GENERAL),
}


def _require_text(name: str, value: str) -> None:
    if not value.strip():
        raise ValueError(f"{name} must be non-empty")


@dataclass(frozen=True)
class MutationPermissionProfile:
    mutation_class: MutationClass
    allowed_targets: FrozenSet[str]
    evidence_threshold: EvidenceLevel
    approval_authority: AuthorityLevel
    propagation_limit: FrozenSet[str]
    rollback_required: bool
    monitoring_window: str
    policy_hash: str

    def __post_init__(self) -> None:
        _require_text("monitoring_window", self.monitoring_window)
        _require_text("policy_hash", self.policy_hash)
        if not self.allowed_targets:
            raise ValueError("allowed_targets must be non-empty")


@dataclass(frozen=True)
class MutationCandidate:
    change_id: str
    change_hash: str
    parent_hash: str
    mutation_class: MutationClass
    target: str
    current_state: Lifecycle
    proposed_state: Lifecycle
    evidence_level: EvidenceLevel
    invariants_passed: bool
    safety_passed: bool
    audit_complete: bool
    rollback_parent_hash: Optional[str]
    requested_propagation: FrozenSet[str]
    modifies_governance_boundary: bool = False

    def __post_init__(self) -> None:
        for name in ("change_id", "change_hash", "parent_hash", "target"):
            _require_text(name, getattr(self, name))


@dataclass(frozen=True)
class MutationAuthority:
    authority_id: str
    level: AuthorityLevel
    scopes: FrozenSet[str]
    policy_hash: str

    def __post_init__(self) -> None:
        _require_text("authority_id", self.authority_id)
        _require_text("policy_hash", self.policy_hash)


@dataclass(frozen=True)
class PreparedMutation:
    change_id: str
    change_hash: str
    parent_hash: str
    policy_hash: str
    authority_id: str
    required_authority_level: AuthorityLevel
    target: str
    proposed_state: Lifecycle


@dataclass(frozen=True)
class MutationResult:
    decision: MutationDecision
    reasons: Tuple[str, ...] = ()
    prepared: Optional[PreparedMutation] = None


def prepare_mutation(
    candidate: MutationCandidate,
    profile: MutationPermissionProfile,
    authority: Optional[MutationAuthority],
) -> MutationResult:
    if candidate.mutation_class is MutationClass.M0 or candidate.modifies_governance_boundary:
        return MutationResult(
            MutationDecision.ESCALATE_CONSTITUTIONAL,
            ("constitutional_or_governance_boundary_change",),
        )

    reasons = []
    if candidate.mutation_class is not profile.mutation_class:
        reasons.append("mutation_class_mismatch")
    if candidate.target not in profile.allowed_targets:
        reasons.append("target_outside_allowed_range")
    if (candidate.current_state, candidate.proposed_state) not in _ALLOWED_TRANSITIONS:
        reasons.append("illegal_lifecycle_transition")
    if candidate.evidence_level < profile.evidence_threshold:
        reasons.append("evidence_below_threshold")
    if not candidate.invariants_passed:
        reasons.append("invariant_gate_failed")
    if not candidate.safety_passed:
        reasons.append("safety_gate_failed")
    if not candidate.audit_complete:
        reasons.append("audit_incomplete")
    if not candidate.requested_propagation.issubset(profile.propagation_limit):
        reasons.append("propagation_outside_envelope")
    if profile.rollback_required and not (candidate.rollback_parent_hash or "").strip():
        reasons.append("rollback_target_missing")

    if reasons:
        return MutationResult(MutationDecision.BLOCK, tuple(reasons))

    if authority is None:
        return MutationResult(MutationDecision.HOLD, ("authority_missing",))
    if MUTATION_APPROVE_SCOPE not in authority.scopes:
        return MutationResult(MutationDecision.HOLD, ("mutation_scope_missing",))
    if authority.level < profile.approval_authority:
        return MutationResult(MutationDecision.HOLD, ("authority_level_insufficient",))
    if authority.policy_hash != profile.policy_hash:
        return MutationResult(MutationDecision.HOLD, ("authority_policy_hash_mismatch",))

    return MutationResult(
        MutationDecision.PREPARED,
        prepared=PreparedMutation(
            change_id=candidate.change_id,
            change_hash=candidate.change_hash,
            parent_hash=candidate.parent_hash,
            policy_hash=profile.policy_hash,
            authority_id=authority.authority_id,
            required_authority_level=profile.approval_authority,
            target=candidate.target,
            proposed_state=candidate.proposed_state,
        ),
    )


def commit_guard(
    prepared: PreparedMutation,
    *,
    current_change_hash: str,
    current_parent_hash: str,
    current_policy_hash: str,
    current_authority: Optional[MutationAuthority],
) -> MutationResult:
    """Commit-time check: fresh, causally prior, effect-bound, eligible now."""
    if current_change_hash != prepared.change_hash:
        return MutationResult(MutationDecision.REVALIDATE, ("change_hash_changed",))
    if current_parent_hash != prepared.parent_hash:
        return MutationResult(MutationDecision.REVALIDATE, ("parent_hash_changed",))
    if current_policy_hash != prepared.policy_hash:
        return MutationResult(MutationDecision.REVALIDATE, ("policy_hash_changed",))
    if current_authority is None:
        return MutationResult(MutationDecision.REVALIDATE, ("authority_missing_at_commit",))
    if current_authority.authority_id != prepared.authority_id:
        return MutationResult(MutationDecision.REVALIDATE, ("authority_identity_changed",))
    if MUTATION_APPROVE_SCOPE not in current_authority.scopes:
        return MutationResult(MutationDecision.REVALIDATE, ("mutation_scope_missing_at_commit",))
    if current_authority.level < prepared.required_authority_level:
        return MutationResult(MutationDecision.REVALIDATE, ("authority_level_downgraded",))
    if current_authority.policy_hash != current_policy_hash:
        return MutationResult(MutationDecision.REVALIDATE, ("authority_policy_binding_changed",))
    return MutationResult(MutationDecision.COMMITTABLE)
