"""Bounded executable C09 Kernel Control runtime.

Origin architect / steward: Trang Phan.

AMOS_MODEL reference implementation for the Cognitive Matrix C09 kernel-control
contract. C09 validates control-plane preconditions and may forward a proposal to
C01 Governance. It never mints authority and never commits an external effect.

Bounded contract implemented here:
- every emitted result remains provenance-bound;
- UNKNOWN/GAP never becomes a passing state;
- stale upstream state routes to revalidation;
- schema drift fails closed;
- COMPETING remains held, not collapsed;
- effect proposals require a fresh, scope/policy/state-bound C01 authority witness;
- successful effect validation means FORWARD_TO_C01, not COMMITTED.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple

from matrix_registry_runtime import AuthorityWitness, Condition


class KernelControlStatus(Enum):
    VALIDATED_BOUNDED = "VALIDATED_BOUNDED"
    HOLD_UNKNOWN = "HOLD_UNKNOWN"
    HOLD_COMPETING = "HOLD_COMPETING"
    REVALIDATE_STALE = "REVALIDATE_STALE"
    BLOCK_SCHEMA_DRIFT = "BLOCK_SCHEMA_DRIFT"
    BLOCK_UPSTREAM = "BLOCK_UPSTREAM"
    BLOCK_AUTHORITY = "BLOCK_AUTHORITY"
    FORWARD_TO_C01 = "FORWARD_TO_C01"


@dataclass(frozen=True)
class KernelControlRequest:
    request_id: str
    operation: str
    state_version: str
    provenance_ids: Tuple[str, ...]
    input_schema_hash: str
    expected_input_schema_hash: str
    output_schema_hash: str
    expected_output_schema_hash: str
    observed_epoch: str
    required_epoch: str
    upstream_condition: Condition = Condition.ACTIVE
    unknown_gaps: Tuple[str, ...] = ()
    effect_requested: bool = False
    effect_scope: Optional[str] = None
    policy_hash: Optional[str] = None

    def __post_init__(self) -> None:
        for value, name in (
            (self.request_id, "request_id"),
            (self.operation, "operation"),
            (self.state_version, "state_version"),
            (self.input_schema_hash, "input_schema_hash"),
            (self.expected_input_schema_hash, "expected_input_schema_hash"),
            (self.output_schema_hash, "output_schema_hash"),
            (self.expected_output_schema_hash, "expected_output_schema_hash"),
            (self.observed_epoch, "observed_epoch"),
            (self.required_epoch, "required_epoch"),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")

        if not self.provenance_ids:
            raise ValueError("C09 cannot emit output for an unprovenanced request")
        if len(set(self.provenance_ids)) != len(self.provenance_ids):
            raise ValueError("provenance_ids must be unique")
        if any(not isinstance(item, str) or not item.strip() for item in self.provenance_ids):
            raise ValueError("provenance_ids must contain non-empty strings")

        if len(set(self.unknown_gaps)) != len(self.unknown_gaps):
            raise ValueError("unknown_gaps must be unique")
        if any(not isinstance(item, str) or not item.strip() for item in self.unknown_gaps):
            raise ValueError("unknown_gaps must contain non-empty strings")

        if not isinstance(self.upstream_condition, Condition):
            raise ValueError("upstream_condition must be a Condition")

        if self.effect_requested:
            if not self.effect_scope or not self.effect_scope.strip():
                raise ValueError("effect_scope is required for an effect proposal")
            if not self.policy_hash or not self.policy_hash.strip():
                raise ValueError("policy_hash is required for an effect proposal")
        elif self.effect_scope is not None or self.policy_hash is not None:
            raise ValueError("effect metadata is invalid when effect_requested is false")


@dataclass(frozen=True)
class KernelControlResult:
    status: KernelControlStatus
    request_id: str
    state_version: str
    provenance_ids: Tuple[str, ...]
    reasons: Tuple[str, ...]
    authority_witness_id: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.request_id.strip() or not self.state_version.strip():
            raise ValueError("result identity and state_version must be explicit")
        if not self.provenance_ids:
            raise ValueError("C09 result cannot lose provenance")
        if not self.reasons:
            raise ValueError("C09 result must state at least one reason")
        if self.status is KernelControlStatus.FORWARD_TO_C01 and not self.authority_witness_id:
            raise ValueError("FORWARD_TO_C01 requires an authority witness identity")

    @property
    def commits_effect(self) -> bool:
        """C09 never owns final effect authority or commit."""
        return False


def _result(
    request: KernelControlRequest,
    status: KernelControlStatus,
    *reasons: str,
    authority_witness_id: Optional[str] = None,
) -> KernelControlResult:
    return KernelControlResult(
        status=status,
        request_id=request.request_id,
        state_version=request.state_version,
        provenance_ids=request.provenance_ids,
        reasons=tuple(reasons),
        authority_witness_id=authority_witness_id,
    )


def evaluate_kernel_control(
    request: KernelControlRequest,
    authority: Optional[AuthorityWitness] = None,
) -> KernelControlResult:
    """Evaluate C09 in deterministic fail-closed precedence order.

    Precedence is structural identity -> freshness -> epistemic condition -> gaps
    -> effect authority. A result may validate or forward a proposal, but cannot
    authorize or commit an effect.
    """

    if (
        request.input_schema_hash != request.expected_input_schema_hash
        or request.output_schema_hash != request.expected_output_schema_hash
    ):
        return _result(
            request,
            KernelControlStatus.BLOCK_SCHEMA_DRIFT,
            "SCHEMA_FINGERPRINT_MISMATCH",
        )

    if request.observed_epoch != request.required_epoch or request.upstream_condition is Condition.STALE:
        return _result(
            request,
            KernelControlStatus.REVALIDATE_STALE,
            "FRESHNESS_EPOCH_MISMATCH_OR_STALE_UPSTREAM",
        )

    if request.upstream_condition is Condition.COMPETING:
        return _result(
            request,
            KernelControlStatus.HOLD_COMPETING,
            "UPSTREAM_COMPETING_STATE_PRESERVED",
        )

    if request.upstream_condition in (Condition.QUARANTINED, Condition.FALSIFIED):
        return _result(
            request,
            KernelControlStatus.BLOCK_UPSTREAM,
            f"UPSTREAM_{request.upstream_condition.value}",
        )

    if request.unknown_gaps:
        return _result(
            request,
            KernelControlStatus.HOLD_UNKNOWN,
            "UNKNOWN_GAP_PRESENT",
            *request.unknown_gaps,
        )

    if request.effect_requested:
        assert request.effect_scope is not None
        assert request.policy_hash is not None
        if authority is None or not authority.authorizes(
            request.effect_scope,
            request.policy_hash,
            request.state_version,
        ):
            return _result(
                request,
                KernelControlStatus.BLOCK_AUTHORITY,
                "C01_AUTHORITY_MISSING_STALE_OR_MISMATCHED",
            )
        return _result(
            request,
            KernelControlStatus.FORWARD_TO_C01,
            "C09_PRECONDITIONS_SATISFIED",
            "C01_REMAINS_FINAL_AUTHORITY_OWNER",
            authority_witness_id=authority.witness_id,
        )

    return _result(
        request,
        KernelControlStatus.VALIDATED_BOUNDED,
        "C09_BOUNDED_NON_EFFECT_CONTRACTS_SATISFIED",
    )
