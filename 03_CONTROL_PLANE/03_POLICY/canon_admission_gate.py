"""Fail-closed AMOS canon admission reference gate.

Origin architect / steward: Trang Phan.

This module separates candidate quality from canon authority. Confidence is
metadata only; it can never substitute for provenance, contradiction handling,
required verification, authority, or commit-time freshness.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import FrozenSet, Optional, Tuple

CANON_PROMOTE_SCOPE = "canon:promote"


class AdmissionDecision(Enum):
    HOLD_FOR_EVIDENCE = "HOLD_FOR_EVIDENCE"
    COMPETING = "COMPETING"
    QUARANTINE = "QUARANTINE"
    BLOCK_AUTHORITY = "BLOCK_AUTHORITY"
    PREPARED_FOR_COMMIT = "PREPARED_FOR_COMMIT"
    REVALIDATE_SOURCE = "REVALIDATE_SOURCE"
    REVALIDATE_POLICY = "REVALIDATE_POLICY"
    REVALIDATE_BASELINE = "REVALIDATE_BASELINE"
    REVALIDATE_AUTHORITY = "REVALIDATE_AUTHORITY"
    COMMITTABLE = "COMMITTABLE"


@dataclass(frozen=True)
class CandidateEvidence:
    candidate_id: str
    source_id: str
    source_version: str
    source_hash: str
    source_resolved: bool
    provenance_traceable: bool
    semantics_typed: bool
    assumptions_bound: bool
    contradiction_free: bool
    unresolved_competing: bool = False
    math_claim: bool = False
    equations_checked: bool = False
    counterexamples_checked: bool = False
    implementation_claim: bool = False
    implementation_receipt: Optional[str] = None
    confidence: Optional[float] = None

    def __post_init__(self) -> None:
        for name in ("candidate_id", "source_id", "source_version", "source_hash"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must be non-empty")
        if self.confidence is not None and not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be in [0,1]")


@dataclass(frozen=True)
class AuthorityWitness:
    authority_id: str
    principal: str
    scopes: FrozenSet[str]
    policy_hash: str

    def __post_init__(self) -> None:
        if not self.authority_id.strip() or not self.principal.strip() or not self.policy_hash.strip():
            raise ValueError("authority_id, principal, and policy_hash must be non-empty")

    def permits_canon_promotion(self) -> bool:
        return CANON_PROMOTE_SCOPE in self.scopes


@dataclass(frozen=True)
class AdmissionContext:
    canon_policy_hash: str
    baseline_id: str
    baseline_hash: str

    def __post_init__(self) -> None:
        if not self.canon_policy_hash.strip() or not self.baseline_id.strip() or not self.baseline_hash.strip():
            raise ValueError("policy and baseline identities must be non-empty")


@dataclass(frozen=True)
class PreparedAdmission:
    candidate_id: str
    source_hash: str
    canon_policy_hash: str
    baseline_id: str
    baseline_hash: str
    authority_id: str
    authority_policy_hash: str


@dataclass(frozen=True)
class AdmissionResult:
    decision: AdmissionDecision
    reasons: Tuple[str, ...] = ()
    prepared: Optional[PreparedAdmission] = None


def prepare_admission(
    evidence: CandidateEvidence,
    context: AdmissionContext,
    authority: Optional[AuthorityWitness],
) -> AdmissionResult:
    """Evaluate candidate evidence and authority without committing Canon state."""
    if evidence.unresolved_competing:
        return AdmissionResult(AdmissionDecision.COMPETING, ("unresolved_competing_claim",))

    if not evidence.contradiction_free:
        return AdmissionResult(AdmissionDecision.QUARANTINE, ("unresolved_contradiction",))

    missing = []
    if not evidence.source_resolved:
        missing.append("source_resolved")
    if not evidence.provenance_traceable:
        missing.append("provenance_traceable")
    if not evidence.semantics_typed:
        missing.append("semantics_typed")
    if not evidence.assumptions_bound:
        missing.append("assumptions_bound")
    if evidence.math_claim and not evidence.equations_checked:
        missing.append("equations_checked")
    if evidence.math_claim and not evidence.counterexamples_checked:
        missing.append("counterexamples_checked")
    if evidence.implementation_claim and not (evidence.implementation_receipt or "").strip():
        missing.append("implementation_receipt")

    if missing:
        return AdmissionResult(AdmissionDecision.HOLD_FOR_EVIDENCE, tuple(missing))

    if authority is None:
        return AdmissionResult(AdmissionDecision.BLOCK_AUTHORITY, ("authority_missing",))
    if not authority.permits_canon_promotion():
        return AdmissionResult(AdmissionDecision.BLOCK_AUTHORITY, ("canon_scope_missing",))
    if authority.policy_hash != context.canon_policy_hash:
        return AdmissionResult(AdmissionDecision.BLOCK_AUTHORITY, ("authority_policy_hash_mismatch",))

    prepared = PreparedAdmission(
        candidate_id=evidence.candidate_id,
        source_hash=evidence.source_hash,
        canon_policy_hash=context.canon_policy_hash,
        baseline_id=context.baseline_id,
        baseline_hash=context.baseline_hash,
        authority_id=authority.authority_id,
        authority_policy_hash=authority.policy_hash,
    )
    return AdmissionResult(AdmissionDecision.PREPARED_FOR_COMMIT, prepared=prepared)


def commit_guard(
    prepared: PreparedAdmission,
    *,
    current_source_hash: str,
    current_context: AdmissionContext,
    current_authority: Optional[AuthorityWitness],
) -> AdmissionResult:
    """Commit-time CAS-style revalidation. COMMITTABLE is not itself a write."""
    if current_source_hash != prepared.source_hash:
        return AdmissionResult(AdmissionDecision.REVALIDATE_SOURCE, ("source_hash_changed",))

    if current_context.canon_policy_hash != prepared.canon_policy_hash:
        return AdmissionResult(AdmissionDecision.REVALIDATE_POLICY, ("canon_policy_hash_changed",))

    if (
        current_context.baseline_id != prepared.baseline_id
        or current_context.baseline_hash != prepared.baseline_hash
    ):
        return AdmissionResult(AdmissionDecision.REVALIDATE_BASELINE, ("baseline_identity_changed",))

    if current_authority is None:
        return AdmissionResult(AdmissionDecision.REVALIDATE_AUTHORITY, ("authority_missing_at_commit",))
    if current_authority.authority_id != prepared.authority_id:
        return AdmissionResult(AdmissionDecision.REVALIDATE_AUTHORITY, ("authority_identity_changed",))
    if not current_authority.permits_canon_promotion():
        return AdmissionResult(AdmissionDecision.REVALIDATE_AUTHORITY, ("canon_scope_missing_at_commit",))
    if (
        current_authority.policy_hash != prepared.authority_policy_hash
        or current_authority.policy_hash != current_context.canon_policy_hash
    ):
        return AdmissionResult(AdmissionDecision.REVALIDATE_AUTHORITY, ("authority_policy_binding_changed",))

    return AdmissionResult(AdmissionDecision.COMMITTABLE)
