"""Bounded executable C01 Governance control-plane runtime.

Origin architect / steward: Trang Phan.

AMOS_MODEL reference implementation. C01 does not create authority from model
confidence. It validates an externally attested enforcement root, immutable
precedence identity, freshness, explicit scopes, and a consequential-decision
receipt before emitting a bounded AuthorityWitness.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
import json
from typing import Tuple

from matrix_registry_runtime import AuthorityWitness


class GovernanceStatus(Enum):
    AUTHORIZE_BOUNDED = "AUTHORIZE_BOUNDED"
    REVALIDATE_STALE = "REVALIDATE_STALE"
    BLOCK_ENFORCEMENT_ROOT = "BLOCK_ENFORCEMENT_ROOT"
    BLOCK_PRECEDENCE = "BLOCK_PRECEDENCE"
    BLOCK_RECEIPT = "BLOCK_RECEIPT"
    BLOCK_SCOPE = "BLOCK_SCOPE"
    BLOCK_POLICY = "BLOCK_POLICY"


@dataclass(frozen=True)
class GovernanceRequest:
    request_id: str
    principal: str
    scopes: Tuple[str, ...]
    policy_hash: str
    state_version: str
    enforcement_root_id: str
    enforcement_root_attested: bool
    enforcement_root_agent_write_excluded: bool
    precedence_version: str
    expected_precedence_version: str
    decision_receipt_id: str
    observed_epoch: str
    required_epoch: str

    def __post_init__(self) -> None:
        for value, name in (
            (self.request_id, "request_id"),
            (self.principal, "principal"),
            (self.policy_hash, "policy_hash"),
            (self.state_version, "state_version"),
            (self.enforcement_root_id, "enforcement_root_id"),
            (self.precedence_version, "precedence_version"),
            (self.expected_precedence_version, "expected_precedence_version"),
            (self.decision_receipt_id, "decision_receipt_id"),
            (self.observed_epoch, "observed_epoch"),
            (self.required_epoch, "required_epoch"),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        if type(self.enforcement_root_attested) is not bool or type(self.enforcement_root_agent_write_excluded) is not bool:
            raise ValueError("enforcement-root gates must be bool")
        if not self.scopes or any(not isinstance(scope, str) or not scope.strip() for scope in self.scopes):
            raise ValueError("scopes must contain non-empty strings")
        if len(set(self.scopes)) != len(self.scopes):
            raise ValueError("scopes must be unique")


@dataclass(frozen=True)
class GovernanceResult:
    status: GovernanceStatus
    request_id: str
    authority: AuthorityWitness | None
    governance_receipt_hash: str | None
    reasons: Tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.request_id.strip() or not self.reasons:
            raise ValueError("governance result requires identity and reasons")
        if self.status is GovernanceStatus.AUTHORIZE_BOUNDED:
            if self.authority is None or self.governance_receipt_hash is None:
                raise ValueError("authorized result requires authority and receipt hash")
        elif self.authority is not None or self.governance_receipt_hash is not None:
            raise ValueError("blocked governance result cannot carry authority")


def _blocked(request: GovernanceRequest, status: GovernanceStatus, reason: str) -> GovernanceResult:
    return GovernanceResult(status, request.request_id, None, None, (reason,))


def _receipt_hash(request: GovernanceRequest) -> str:
    payload = {
        "decision_receipt_id": request.decision_receipt_id,
        "enforcement_root_id": request.enforcement_root_id,
        "policy_hash": request.policy_hash,
        "precedence_version": request.precedence_version,
        "principal": request.principal,
        "request_id": request.request_id,
        "scopes": sorted(request.scopes),
        "state_version": request.state_version,
    }
    return sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def evaluate_governance(request: GovernanceRequest) -> GovernanceResult:
    """Validate bounded governance gates and emit an effect-scoped witness."""
    if request.observed_epoch != request.required_epoch:
        return _blocked(request, GovernanceStatus.REVALIDATE_STALE, "GOVERNANCE_EPOCH_STALE")
    if not request.enforcement_root_attested or not request.enforcement_root_agent_write_excluded:
        return _blocked(request, GovernanceStatus.BLOCK_ENFORCEMENT_ROOT, "ENFORCEMENT_ROOT_NOT_ATTESTED_OR_AGENT_WRITE_EXCLUDED")
    if request.precedence_version != request.expected_precedence_version:
        return _blocked(request, GovernanceStatus.BLOCK_PRECEDENCE, "PRECEDENCE_VERSION_MISMATCH")
    if not request.decision_receipt_id.strip():
        return _blocked(request, GovernanceStatus.BLOCK_RECEIPT, "CONSEQUENTIAL_DECISION_RECEIPT_REQUIRED")
    if not request.policy_hash.strip():
        return _blocked(request, GovernanceStatus.BLOCK_POLICY, "POLICY_HASH_REQUIRED")
    if not request.scopes:
        return _blocked(request, GovernanceStatus.BLOCK_SCOPE, "EXPLICIT_SCOPE_REQUIRED")

    receipt_hash = _receipt_hash(request)
    witness = AuthorityWitness(
        witness_id=f"c01:{receipt_hash}",
        principal=request.principal,
        scope=tuple(sorted(request.scopes)),
        policy_hash=request.policy_hash,
        state_version=request.state_version,
        fresh=True,
    )
    return GovernanceResult(
        GovernanceStatus.AUTHORIZE_BOUNDED,
        request.request_id,
        witness,
        receipt_hash,
        (
            "ENFORCEMENT_ROOT_PRECEDENCE_FRESHNESS_SCOPE_AND_RECEIPT_GATES_SATISFIED",
            "BOUNDED_AUTHORITY_IS_NOT_EFFECT_COMMIT",
        ),
    )
