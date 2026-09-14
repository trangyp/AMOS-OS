---
title: AMOS Durable Workflow Runtime Contract
type: runtime_contract
status: REFERENCE_IMPLEMENTATION
conclusion_class: AMOS_MODEL
origin_architect: Trang Phan
steward: Trang Phan
---

# AMOS Durable Workflow Runtime Contract

## Scope

This contract governs the local executable reference implementation in:

`04_RUNTIME/01_REFERENCE_IMPLEMENTATION/durable_workflow_runtime.py`

It establishes tested SQLite-backed workflow persistence semantics only. It does **not** establish distributed consensus, production durability, exactly-once delivery, external-system atomicity, deployment authority, or canonical runtime promotion.

## Runtime object

A durable workflow run consists of:

- stable `workflow_id`;
- monotonic `run_id`;
- explicit `code_version`;
- explicit persisted state;
- append-only hash-chained event history;
- step identity and input hash;
- output receipts for completed steps;
- explicit idempotency keys for external effects;
- parent-run lineage across continue-as-new.

The reference runtime separates two step classes:

- `PURE` — deterministic/local computation that may be retried after interruption;
- `EFFECT` — an operation that may change external state and therefore requires a durable effect key and receipt boundary.

## Hard invariants

1. `HISTORY_REPLAY != EFFECT_REEXECUTION`.
2. `STEP_IDENTITY = workflow_id + run_id + step_id`; identical arguments do not collapse distinct steps.
3. Repeated identical effect calls are distinct work unless the caller deliberately supplies the same explicit `effect_key`.
4. Reusing an `effect_key` with different input is a hard conflict.
5. An effect recorded `STARTED` without a durable completion receipt is `AMBIGUOUS`; it may not be retried automatically.
6. An ambiguous effect must be reconciled as `COMPLETED` or `NOT_APPLIED` before progress.
7. A pure step interrupted after `STARTED` may be retried because replay cannot duplicate an external effect by contract.
8. `CODE_CHANGE != REPLAY_COMPATIBLE`; a version change requires an explicit compatibility patch marker.
9. Event-history integrity is checked before resume or execution.
10. Completed-step output hashes are checked before replay reuse.
11. Continue-as-new carries only explicitly supplied workflow state. Prior per-run pure-step cache is not implicitly inherited.
12. Continue-as-new is blocked while any external effect is unresolved.
13. `CHECKPOINT_PRESENT != EFFECT_COMMITTED`.
14. `RECEIPT_PRESENT != EXTERNAL_TRUTH`; external truth may still require reconciliation against the actual target system.
15. `DURABLE_REFERENCE_TEST_PASS != PRODUCTION_DURABILITY`.

## State transitions

```text
RUNNING
  -> COMPLETED
  -> CONTINUED_AS_NEW

PURE step:
  NEW -> STARTED -> COMPLETED
                 -> RETRYABLE -> STARTED

EFFECT step:
  NEW -> STARTED -> COMPLETED
                 -> AMBIGUOUS -> RECONCILE
                                -> COMPLETED
                                -> RETRYABLE -> STARTED
```

`AMBIGUOUS` is intentionally non-compensatory. A retry policy, confidence score, or timeout cannot convert it into success.

## Upgrade/replay boundary

The stored workflow code version is part of the replay contract. Resuming under a different version fails closed unless an explicit `(workflow_id, from_version, to_version, patch_id)` compatibility marker exists.

A patch marker is evidence that compatibility was deliberately declared; it is not proof that every semantic change is replay-safe. Production promotion would require stronger migration tests and source-version binding.

## Continue-as-new boundary

A new run receives:

- new `run_id`;
- explicit carried state;
- parent-run reference;
- parent event-head hash;
- its own new event history and per-run step table.

Completed external effects remain deduplicable across runs only through explicit effect keys. Pure-step results are not silently carried across the boundary.

## Executed validation

`19_TESTS/test_durable_workflow_runtime.py` covers:

- restart and pure-step retry;
- completed-step receipt reuse;
- mandatory effect keys;
- repeated identical effects with distinct keys;
- explicit effect-key deduplication;
- effect-key/input conflicts;
- interrupted effect quarantine;
- effect-exception ambiguity;
- explicit reconciliation;
- code-version patch gating;
- event-chain tamper detection;
- continue-as-new state isolation;
- continue-as-new blocking on unresolved effects.

## External mechanism provenance

The implementation adapts mechanisms rather than vendoring runtimes:

- Temporal Python SDK, commit `ab25ed693f7ec77589346e66c98db299a8c9c9fe`: replay compatibility, explicit version/patch discipline, continue-as-new boundaries, and the failure mode where result caching/deduplication can make legitimate repeated calls stale or replay-incompatible.
- DBOS Transact Python, commit `83805fd84494c85ea09105443884a2786152d921`: durable step checkpoints, resume from completed work, explicit workflow identity/idempotency, and database-backed workflow state.

External project claims remain `SOURCE_CLAIM`. AMOS validation applies only to the local reference implementation and its executed test surface.

## Promotion boundary

Current status:

```text
REFERENCE_IMPLEMENTATION = EXECUTED_TESTED_SCOPE
DISTRIBUTED_RUNTIME = UNKNOWN/GAP
PRODUCTION_DURABILITY = UNKNOWN/GAP
EXTERNAL_EFFECT_ATOMICITY = UNKNOWN/GAP
DEPLOYMENT_AUTHORITY = NONE
CANONICAL_PROMOTION = NONE
```
