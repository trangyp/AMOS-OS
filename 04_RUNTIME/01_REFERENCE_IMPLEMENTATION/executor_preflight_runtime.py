"""Bounded AMOS Executor preflight runtime.

Origin architect / steward: Trang Phan.

This module closes the agent-to-control-plane preparation gap only. It consumes
an action proposal plus explicit authority/policy bindings, validates structural
freshness and effect identity, and emits a prepared execution capsule. It does
not dispatch effects, validate cryptographic authority, own the authoritative
read set, or return COMMITTABLE/COMMITTED.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import hashlib
import json
from typing import FrozenSet, Optional, Sequence, Tuple


class PreflightStatus(Enum):
    PREPARED_FOR_CONTROL_PLANE = "PREPARED_FOR_CONTROL_PLANE"
    REJECT_SCHEMA = "REJECT_SCHEMA"
    HOLD_STALE = "HOLD_STALE"
    HOLD_AUTHORITY = "HOLD_AUTHORITY"
    HOLD_POLICY = "HOLD_POLICY"
    BLOCK_EFFECT_BINDING = "BLOCK_EFFECT_BINDING"
    BLOCK_READ_SET = "BLOCK_READ_SET"
    BLOCK_WRITE_SET = "BLOCK_WRITE_SET"
    BLOCK_IDEMPOTENCY = "BLOCK_IDEMPOTENCY"


class Reversibility(Enum):
    REVERSIBLE = "REVERSIBLE"
    COMPENSATABLE = "COMPENSATABLE"
    IRREVERSIBLE = "IRREVERSIBLE"


def _text(name: str, value: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError(f"{name} must be non-empty")
    return value


def _hex_digest(name: str, value: str) -> str:
    value = _text(name, value).lower()
    if len(value) != 64 or any(ch not in "0123456789abcdef" for ch in value):
        raise ValueError(f"{name} must be a 64-character lowercase-or-uppercase hex SHA-256 digest")
    return value


@dataclass(frozen=True)
class ActionProposal:
    proposal_id: str
    principal: str
    objective: str
    action_type: str
    target: str
    payload_hash: str
    expected_effect: str
    risk_class: str
    reversibility: Reversibility
    authority_reference: str
    created_at: int
    expires_at: int
    evidence_ids: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for name in ("proposal_id", "principal", "objective", "action_type", "target", "expected_effect", "risk_class", "authority_reference"):
            _text(name, getattr(self, name))
        _hex_digest("payload_hash", self.payload_hash)
        if self.created_at < 0 or self.expires_at <= self.created_at:
            raise ValueError("proposal timestamps must satisfy 0 <= created_at < expires_at")
        if any(not item.strip() for item in self.evidence_ids):
            raise ValueError("evidence_ids must be non-empty strings")


@dataclass(frozen=True)
class AuthorityBinding:
    witness_id: str
    principal: str
    policy_id: str
    policy_epoch: str
    effect_digest: str
    transaction_id: Optional[str]
    idempotency_key: Optional[str]
    allowed_action_types: FrozenSet[str]
    allowed_targets: FrozenSet[str]
    valid_from: int
    expires_at: int
    revoked: bool = False

    def __post_init__(self) -> None:
        for name in ("witness_id", "principal", "policy_id", "policy_epoch"):
            _text(name, getattr(self, name))
        _hex_digest("effect_digest", self.effect_digest)
        if self.transaction_id is not None:
            _text("transaction_id", self.transaction_id)
        if self.idempotency_key is not None:
            _text("idempotency_key", self.idempotency_key)
        if not self.allowed_action_types or not self.allowed_targets:
            raise ValueError("authority action/target scopes must be non-empty")
        if any(not item.strip() for item in (*self.allowed_action_types, *self.allowed_targets)):
            raise ValueError("authority scopes must contain non-empty strings")
        if self.valid_from < 0 or self.expires_at <= self.valid_from:
            raise ValueError("authority timestamps must satisfy 0 <= valid_from < expires_at")


@dataclass(frozen=True)
class PolicyBinding:
    policy_id: str
    policy_epoch: str
    allowed_action_types: FrozenSet[str]
    allowed_targets: FrozenSet[str]
    policy_hash: str

    def __post_init__(self) -> None:
        _text("policy_id", self.policy_id)
        _text("policy_epoch", self.policy_epoch)
        _hex_digest("policy_hash", self.policy_hash)
        if not self.allowed_action_types or not self.allowed_targets:
            raise ValueError("policy action/target scopes must be non-empty")
        if any(not item.strip() for item in (*self.allowed_action_types, *self.allowed_targets)):
            raise ValueError("policy scopes must contain non-empty strings")


@dataclass(frozen=True, order=True)
class ObservedRead:
    resource: str
    field: str
    version: str
    content_hash: str

    def __post_init__(self) -> None:
        for name in ("resource", "field", "version"):
            _text(name, getattr(self, name))
        _hex_digest("content_hash", self.content_hash)


@dataclass(frozen=True, order=True)
class IntendedWrite:
    resource: str
    field: str
    operation: str
    value_hash: str
    expected_precondition_hash: Optional[str] = None

    def __post_init__(self) -> None:
        for name in ("resource", "field", "operation"):
            _text(name, getattr(self, name))
        _hex_digest("value_hash", self.value_hash)
        if self.expected_precondition_hash is not None:
            _hex_digest("expected_precondition_hash", self.expected_precondition_hash)


@dataclass(frozen=True)
class ExecutionRequest:
    request_id: str
    tx_id: str
    principal: str
    proposal: ActionProposal
    authority: Optional[AuthorityBinding]
    policy: PolicyBinding
    expected_state_epoch: str
    observed_read_set: Tuple[ObservedRead, ...]
    intended_write_set: Tuple[IntendedWrite, ...]
    idempotency_key: Optional[str]
    rollback_policy: str
    durable_effect: bool
    created_at: int
    expires_at: int

    def __post_init__(self) -> None:
        for name in ("request_id", "tx_id", "principal", "expected_state_epoch", "rollback_policy"):
            _text(name, getattr(self, name))
        if self.idempotency_key is not None:
            _text("idempotency_key", self.idempotency_key)
        if self.created_at < 0 or self.expires_at <= self.created_at:
            raise ValueError("request timestamps must satisfy 0 <= created_at < expires_at")


@dataclass(frozen=True)
class PreparedExecution:
    request_id: str
    proposal_id: str
    tx_id: str
    principal: str
    effect_digest: str
    authority_witness_id: str
    policy_id: str
    policy_epoch: str
    policy_hash: str
    idempotency_key: Optional[str]
    declared_read_set_hash: str
    write_set_hash: str
    expected_state_epoch: str
    expires_at: int
    commit_authorized: bool = False


@dataclass(frozen=True)
class PreflightResult:
    status: PreflightStatus
    reasons: Tuple[str, ...] = ()
    prepared: Optional[PreparedExecution] = None


def _canonical_hash(records: Sequence[dict]) -> str:
    encoded = json.dumps(list(records), sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def read_set_hash(reads: Sequence[ObservedRead]) -> str:
    rows = [
        {"resource": r.resource, "field": r.field, "version": r.version, "content_hash": r.content_hash.lower()}
        for r in sorted(reads)
    ]
    return _canonical_hash(rows)


def write_set_hash(writes: Sequence[IntendedWrite]) -> str:
    rows = [
        {
            "resource": w.resource,
            "field": w.field,
            "operation": w.operation,
            "value_hash": w.value_hash.lower(),
            "expected_precondition_hash": None if w.expected_precondition_hash is None else w.expected_precondition_hash.lower(),
        }
        for w in sorted(writes)
    ]
    return _canonical_hash(rows)


def effect_digest(proposal: ActionProposal, writes: Sequence[IntendedWrite]) -> str:
    payload = [{
        "proposal_id": proposal.proposal_id,
        "principal": proposal.principal,
        "objective": proposal.objective,
        "action_type": proposal.action_type,
        "target": proposal.target,
        "payload_hash": proposal.payload_hash.lower(),
        "expected_effect": proposal.expected_effect,
        "risk_class": proposal.risk_class,
        "reversibility": proposal.reversibility.value,
        "write_set_hash": write_set_hash(writes),
    }]
    return _canonical_hash(payload)


def _duplicate_coordinates(items: Sequence[object]) -> bool:
    coords = [(getattr(item, "resource"), getattr(item, "field")) for item in items]
    return len(coords) != len(set(coords))


def prepare_execution(request: ExecutionRequest, *, now: int) -> PreflightResult:
    """Prepare an execution capsule; never returns COMMITTABLE or performs an effect."""
    if now < 0:
        raise ValueError("now must be non-negative")

    proposal = request.proposal
    authority = request.authority
    policy = request.policy

    if not (proposal.created_at <= now < proposal.expires_at) or not (request.created_at <= now < request.expires_at):
        return PreflightResult(PreflightStatus.HOLD_STALE, ("proposal_or_request_expired_or_not_yet_valid",))

    if request.principal != proposal.principal:
        return PreflightResult(PreflightStatus.BLOCK_EFFECT_BINDING, ("request_principal_differs_from_proposal",))

    if _duplicate_coordinates(request.observed_read_set):
        return PreflightResult(PreflightStatus.BLOCK_READ_SET, ("duplicate_read_coordinate",))
    if _duplicate_coordinates(request.intended_write_set):
        return PreflightResult(PreflightStatus.BLOCK_WRITE_SET, ("duplicate_write_coordinate",))

    if request.durable_effect and not (request.idempotency_key or "").strip():
        return PreflightResult(PreflightStatus.BLOCK_IDEMPOTENCY, ("durable_effect_requires_stable_idempotency_key",))

    digest = effect_digest(proposal, request.intended_write_set)
    if authority is None:
        return PreflightResult(PreflightStatus.HOLD_AUTHORITY, ("authority_missing",))
    if not (authority.valid_from <= now < authority.expires_at) or authority.revoked:
        return PreflightResult(PreflightStatus.HOLD_AUTHORITY, ("authority_stale_or_revoked",))
    if proposal.authority_reference != authority.witness_id:
        return PreflightResult(PreflightStatus.HOLD_AUTHORITY, ("proposal_authority_reference_mismatch",))
    if request.principal != authority.principal:
        return PreflightResult(PreflightStatus.HOLD_AUTHORITY, ("authority_principal_mismatch",))
    if digest != authority.effect_digest.lower():
        return PreflightResult(PreflightStatus.BLOCK_EFFECT_BINDING, ("authority_effect_digest_mismatch",))
    if request.durable_effect:
        if authority.transaction_id != request.tx_id:
            return PreflightResult(PreflightStatus.HOLD_AUTHORITY, ("authority_transaction_binding_mismatch",))
        if authority.idempotency_key != request.idempotency_key:
            return PreflightResult(PreflightStatus.HOLD_AUTHORITY, ("authority_idempotency_binding_mismatch",))
    elif authority.transaction_id is not None and authority.transaction_id != request.tx_id:
        return PreflightResult(PreflightStatus.HOLD_AUTHORITY, ("authority_transaction_binding_mismatch",))
    if proposal.action_type not in authority.allowed_action_types or proposal.target not in authority.allowed_targets:
        return PreflightResult(PreflightStatus.HOLD_AUTHORITY, ("effect_outside_authority_scope",))

    if authority.policy_id != policy.policy_id or authority.policy_epoch != policy.policy_epoch:
        return PreflightResult(PreflightStatus.HOLD_POLICY, ("authority_policy_binding_mismatch",))
    if proposal.action_type not in policy.allowed_action_types or proposal.target not in policy.allowed_targets:
        return PreflightResult(PreflightStatus.HOLD_POLICY, ("effect_outside_policy_scope",))

    prepared = PreparedExecution(
        request_id=request.request_id,
        proposal_id=proposal.proposal_id,
        tx_id=request.tx_id,
        principal=request.principal,
        effect_digest=digest,
        authority_witness_id=authority.witness_id,
        policy_id=policy.policy_id,
        policy_epoch=policy.policy_epoch,
        policy_hash=policy.policy_hash.lower(),
        idempotency_key=request.idempotency_key,
        declared_read_set_hash=read_set_hash(request.observed_read_set),
        write_set_hash=write_set_hash(request.intended_write_set),
        expected_state_epoch=request.expected_state_epoch,
        expires_at=min(proposal.expires_at, request.expires_at, authority.expires_at),
        commit_authorized=False,
    )
    return PreflightResult(PreflightStatus.PREPARED_FOR_CONTROL_PLANE, prepared=prepared)
