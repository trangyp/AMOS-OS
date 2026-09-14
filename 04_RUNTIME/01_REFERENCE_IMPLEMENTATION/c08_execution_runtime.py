"""Bounded executable C08 Execution control-plane staging runtime.

Origin architect / steward: Trang Phan.

AMOS_MODEL reference implementation. C08 validates an executive proposal and
stages a deterministic effect intent for the AMOS infrastructure commit plane.
It does not dispatch, externalize, retry, or commit effects itself.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
import json
import re
from typing import Tuple

from c03_executive_runtime import ExecutiveStatus
from matrix_registry_runtime import AuthorityWitness, Condition


_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class ExecutionStageStatus(Enum):
    STAGE_EFFECT = "STAGE_EFFECT"
    HOLD_UNKNOWN = "HOLD_UNKNOWN"
    HOLD_COMPETING = "HOLD_COMPETING"
    REVALIDATE_STALE = "REVALIDATE_STALE"
    BLOCK_SCHEMA_DRIFT = "BLOCK_SCHEMA_DRIFT"
    BLOCK_EXECUTIVE = "BLOCK_EXECUTIVE"
    BLOCK_KERNEL = "BLOCK_KERNEL"
    BLOCK_AUTHORITY = "BLOCK_AUTHORITY"


@dataclass(frozen=True)
class ExecutionStageRequest:
    request_id: str
    state_version: str
    selected_candidate_id: str
    executive_status: ExecutiveStatus
    kernel_condition: Condition
    effect_digest: str
    idempotency_key: str
    transaction_id: str
    authority: AuthorityWitness
    required_scope: str
    policy_hash: str
    observed_epoch: str
    required_epoch: str
    input_schema_hash: str
    expected_input_schema_hash: str
    output_schema_hash: str
    expected_output_schema_hash: str
    provenance_ids: Tuple[str, ...]
    unknown_gaps: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for value, name in (
            (self.request_id, "request_id"),
            (self.state_version, "state_version"),
            (self.selected_candidate_id, "selected_candidate_id"),
            (self.idempotency_key, "idempotency_key"),
            (self.transaction_id, "transaction_id"),
            (self.required_scope, "required_scope"),
            (self.policy_hash, "policy_hash"),
            (self.observed_epoch, "observed_epoch"),
            (self.required_epoch, "required_epoch"),
            (self.input_schema_hash, "input_schema_hash"),
            (self.expected_input_schema_hash, "expected_input_schema_hash"),
            (self.output_schema_hash, "output_schema_hash"),
            (self.expected_output_schema_hash, "expected_output_schema_hash"),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        if not isinstance(self.executive_status, ExecutiveStatus):
            raise ValueError("executive_status must be ExecutiveStatus")
        if not isinstance(self.kernel_condition, Condition):
            raise ValueError("kernel_condition must be Condition")
        if not isinstance(self.authority, AuthorityWitness):
            raise ValueError("authority must be AuthorityWitness")
        if not _SHA256_RE.fullmatch(self.effect_digest):
            raise ValueError("effect_digest must be lowercase SHA-256 hex")
        if not self.provenance_ids or any(not isinstance(x, str) or not x.strip() for x in self.provenance_ids):
            raise ValueError("provenance_ids must contain non-empty strings")
        if len(set(self.provenance_ids)) != len(self.provenance_ids):
            raise ValueError("provenance_ids must be unique")
        if len(set(self.unknown_gaps)) != len(self.unknown_gaps):
            raise ValueError("unknown_gaps must be unique")
        if any(not isinstance(x, str) or not x.strip() for x in self.unknown_gaps):
            raise ValueError("unknown_gaps must contain non-empty strings")


@dataclass(frozen=True)
class StagedEffectIntent:
    intent_hash: str
    candidate_id: str
    effect_digest: str
    idempotency_key: str
    transaction_id: str
    authority_id: str
    provenance_ids: Tuple[str, ...]
    dispatched: bool = False
    externalized: bool = False

    def __post_init__(self) -> None:
        if not _SHA256_RE.fullmatch(self.intent_hash):
            raise ValueError("intent_hash must be lowercase SHA-256 hex")
        if self.dispatched or self.externalized:
            raise ValueError("C08 reference runtime may stage only; it may not externalize")


@dataclass(frozen=True)
class ExecutionStageResult:
    status: ExecutionStageStatus
    request_id: str
    state_version: str
    staged_intent: StagedEffectIntent | None
    reasons: Tuple[str, ...]
    requires_infrastructure_commit: bool = True

    def __post_init__(self) -> None:
        if not self.request_id.strip() or not self.state_version.strip() or not self.reasons:
            raise ValueError("result identity and reasons are required")
        if not self.requires_infrastructure_commit:
            raise ValueError("C08 cannot bypass the infrastructure commit plane")
        if self.status is ExecutionStageStatus.STAGE_EFFECT and self.staged_intent is None:
            raise ValueError("STAGE_EFFECT requires a staged intent")
        if self.status is not ExecutionStageStatus.STAGE_EFFECT and self.staged_intent is not None:
            raise ValueError("blocked/held C08 result cannot carry staged intent")


def _result(request: ExecutionStageRequest, status: ExecutionStageStatus, *reasons: str,
            intent: StagedEffectIntent | None = None) -> ExecutionStageResult:
    return ExecutionStageResult(
        status=status,
        request_id=request.request_id,
        state_version=request.state_version,
        staged_intent=intent,
        reasons=tuple(reasons),
    )


def _intent_hash(request: ExecutionStageRequest) -> str:
    payload = {
        "authority_id": request.authority.witness_id,
        "candidate_id": request.selected_candidate_id,
        "effect_digest": request.effect_digest,
        "idempotency_key": request.idempotency_key,
        "policy_hash": request.policy_hash,
        "required_scope": request.required_scope,
        "state_version": request.state_version,
        "transaction_id": request.transaction_id,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256(encoded).hexdigest()


def evaluate_execution_stage(request: ExecutionStageRequest) -> ExecutionStageResult:
    """Stage one effect intent after bounded executive/authority/freshness gates."""
    if request.input_schema_hash != request.expected_input_schema_hash or request.output_schema_hash != request.expected_output_schema_hash:
        return _result(request, ExecutionStageStatus.BLOCK_SCHEMA_DRIFT, "SCHEMA_FINGERPRINT_MISMATCH")
    if request.observed_epoch != request.required_epoch or request.kernel_condition is Condition.STALE:
        return _result(request, ExecutionStageStatus.REVALIDATE_STALE, "FRESHNESS_EPOCH_MISMATCH_OR_STALE_KERNEL")
    if request.unknown_gaps:
        return _result(request, ExecutionStageStatus.HOLD_UNKNOWN, "UNKNOWN_GAP_PRESENT", *request.unknown_gaps)
    if request.executive_status is not ExecutiveStatus.SELECT_PROPOSAL:
        return _result(request, ExecutionStageStatus.BLOCK_EXECUTIVE, "C03_DID_NOT_SELECT_UNIQUE_PROPOSAL")
    if request.kernel_condition is Condition.COMPETING:
        return _result(request, ExecutionStageStatus.HOLD_COMPETING, "KERNEL_COMPETING_PRESERVED")
    if request.kernel_condition in (Condition.QUARANTINED, Condition.FALSIFIED):
        return _result(request, ExecutionStageStatus.BLOCK_KERNEL, f"KERNEL_{request.kernel_condition.value}")
    if not request.authority.authorizes(request.required_scope, request.policy_hash, request.state_version):
        return _result(request, ExecutionStageStatus.BLOCK_AUTHORITY, "C01_AUTHORITY_WITNESS_INVALID_OR_STALE")

    intent = StagedEffectIntent(
        intent_hash=_intent_hash(request),
        candidate_id=request.selected_candidate_id,
        effect_digest=request.effect_digest,
        idempotency_key=request.idempotency_key,
        transaction_id=request.transaction_id,
        authority_id=request.authority.witness_id,
        provenance_ids=request.provenance_ids,
    )
    return _result(
        request,
        ExecutionStageStatus.STAGE_EFFECT,
        "C08_EFFECT_INTENT_STAGED",
        "STAGED_IS_NOT_COMMITTED_OR_EXTERNALIZED",
        "INFRASTRUCTURE_COMMIT_REVALIDATION_REQUIRED",
        intent=intent,
    )
