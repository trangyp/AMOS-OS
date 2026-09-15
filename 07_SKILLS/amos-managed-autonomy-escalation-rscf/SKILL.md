---
name: amos-managed-autonomy-escalation-rscf
description: Govern agent autonomy as an explicit finite-state lifecycle with stable operation, local recovery, assisted recovery, suspension, and regulated surrender. Use when epistemic validity degrades, persistent disagreement remains unresolved, recovery attempts fail, authority becomes stale, or an agent must decide whether to continue, recover, suspend, escalate, or relinquish authority without treating anomaly detection as action authority.
---

# AMOS Managed Autonomy Escalation RSCF

Origin architect/steward: **Trang Phan**.

## Purpose

Own the bounded autonomy-lifecycle decision between ordinary operation and relinquishing autonomous control. This Skill does not diagnose failures, authorize tools, or execute external effects.

## Runtime

`BIND -> OBSERVE -> CLASSIFY -> DECIDE -> TRANSITION -> FENCE -> RECEIPT -> RECHECK`

Use `scripts/managed_autonomy.py` for deterministic lifecycle checks and `scripts/audit_rscf.py` for receipt validation.

States:

`STABLE -> LOCAL_RECOVERY -> ASSISTED_RECOVERY -> SUSPENDED -> SURRENDERED`

Transitions may skip upward when evidence requires stricter containment. Downward transitions require explicit recovery evidence and fresh authority. `SURRENDERED` is terminal for the lifecycle instance; resumption requires a new lifecycle identity.

## Load-bearing evidence classes

- `SOFT_DEGRADATION`
- `RECOVERY_FAILURE`
- `RECOVERY_SUCCESS`
- `PERSISTENT_DISAGREEMENT`
- `EVIDENCE_GAP`
- `HARD_INVARIANT_FAILURE`
- `AUTHORITY_STALE`
- `EXTERNAL_BLOCK`
- `ASSISTED_APPROVAL`
- `ASSISTED_DENIAL`

Do not infer severity from fluent text or confidence alone.

## Decision rules

1. Hard invariant failure, stale authority, or an external blocking proof can move directly to `SUSPENDED`.
2. Soft degradation enters `LOCAL_RECOVERY` while local-attempt budget remains.
3. Exhausted local recovery, persistent disagreement, or unresolved evidence gap enters `ASSISTED_RECOVERY`.
4. Exhausted assisted recovery or explicit assisted denial enters `SURRENDERED`.
5. `RECOVERY_SUCCESS` can de-escalate only if blocking evidence is cleared and authority/policy epochs are current.
6. `SUSPENDED -> STABLE` requires explicit assisted approval plus current authority and no active hard block.
7. Every transition increments a fencing epoch. Receipts from older epochs are stale.

Detailed transition semantics are in `references/lifecycle-contract.md`.

## Hard invariants

- `ANOMALY_DETECTED != RESPONSE_AUTHORITY`.
- `RECOVERY_ATTEMPT != RECOVERY_SUCCESS`.
- `MODEL_CONFIDENCE != AUTONOMY_PERMISSION`.
- `LOCAL_RECOVERY_EXHAUSTED -> ASSISTED_RECOVERY_OR_STRICTER`.
- `HARD_INVARIANT_FAILURE -> NO_AUTONOMOUS_CONTINUE`.
- `STALE_AUTHORITY != VALID_AUTHORITY`.
- `SUSPENDED != SURRENDERED`.
- `SURRENDERED != PAUSED`.
- `TERMINAL_SURRENDER != IN_PLACE_RESUME`.
- `CHECKPOINT_PRESENT != SAFE_TO_RESUME`.
- `RESUME != RESET_RECOVERY_BUDGET`.
- `ESCALATION_RECEIPT != EXECUTION_AUTHORITY`.

## Composition

Accept evidence from exposure control, distributed-attack composition, evaluator reliability, authorization, or other specialist Skills only as typed evidence. Their PASS/BLOCK outputs do not become lifecycle authority automatically.

For consequential external effects, return a lifecycle recommendation/evidence receipt to the AMOS infrastructure control plane. The infrastructure layer owns actual tool/effect authorization and commit.

## Epistemic boundary

The five-state lifecycle and transition policy are `AMOS_MODEL`. Upstream framework mechanisms are `SOURCE_CLAIM`. Local test execution is `EXECUTED_OBSERVATION`. Passing this runtime does not prove deployment safety, causal diagnosis, or optimal escalation thresholds.

## Stop outputs

Return one of:

`CONTINUE_STABLE | ENTER_LOCAL_RECOVERY | REQUIRE_ASSISTED_RECOVERY | SUSPEND_AUTONOMY | SURRENDER_AUTONOMY | RESUME_STABLE | REMAIN_CONTAINED | UNKNOWN_GAP`
