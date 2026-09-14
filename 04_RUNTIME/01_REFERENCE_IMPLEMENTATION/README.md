---
title: AMOS Runtime Reference Implementation
artifact_id: AMOS-RUNTIME-REFERENCE
type: runtime_reference
status: PARTIAL_EXECUTABLE
conclusion_class: AMOS_MODEL
origin_architect: Trang Phan
steward: Trang Phan
---

# AMOS Runtime Reference Implementation

## Status

The AMOS runtime remains a partially executable reference architecture.

```text
PLACEHOLDER != IMPLEMENTED
DOCUMENTED != ENFORCED
REFERENCE_EXECUTOR != PRODUCTION_RUNTIME
TEST_PASS != TRUTH
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

## Runtime pipeline

```text
Perceive -> Route -> Admit -> Plan -> Schedule -> Execute -> Observe -> Repair -> Audit -> Finalize
```

## Executable reference surfaces

### Durable workflow persistence

The first bounded durable-execution reference is implemented in:

- `durable_workflow_runtime.py`
- `DURABLE_WORKFLOW_CONTRACT.md`
- `19_TESTS/test_durable_workflow_runtime.py`

It provides tested local SQLite semantics for:

- stable workflow/run identity;
- explicit checkpoints and state hashes;
- hash-chained history integrity;
- completed-step receipts;
- pure-step retry after interruption;
- explicit external-effect idempotency keys;
- ambiguous-effect quarantine and reconciliation;
- code-version compatibility markers;
- continue-as-new with explicit state carry only.

This closes the previous `Executable binding NOT_ESTABLISHED` gap only for this declared local reference surface.

## Governing boundaries

The executable reference preserves:

```text
HISTORY_REPLAY != EFFECT_REEXECUTION
CHECKPOINT_PRESENT != EFFECT_COMMITTED
CODE_CHANGE != REPLAY_COMPATIBLE
IDENTICAL_ARGUMENTS != SAME_OPERATION
REFERENCE_IMPLEMENTATION != DEPLOYMENT_AUTHORITY
```

An external effect that was started but lacks a durable completion receipt remains `AMBIGUOUS`; it must be reconciled before retry or continuation.

## Cross-plane bindings

- `02_KERNEL` — deterministic primitives and invariant checks.
- `03_CONTROL_PLANE` — authority remains external to runtime capability.
- `04_RUNTIME` — execution/replay owner.
- `08_WORKFLOWS` / `26_WORKFLOWS` — workflow transition contracts.
- `12_STATE` — durable state semantics.
- `17_OBSERVABILITY` — observation/trace only; no authority inheritance.
- `19_TESTS` — executed evidence and falsification surface.

## Remaining gaps

- Distributed durable execution: `UNKNOWN/GAP`.
- Multi-worker leasing/heartbeats: `UNKNOWN/GAP`.
- Distributed consensus/finality implementation: `UNKNOWN/GAP`.
- Production database migration/backup behavior: `UNKNOWN/GAP`.
- External-effect atomicity across third-party systems: `UNKNOWN/GAP`.
- End-to-end production recovery drills: `UNKNOWN/GAP`.
- Canonical runtime promotion: `NONE`.
- Deployment authority: `NONE`.

## Evidence rule

A local reference test may upgrade only the claims exercised by that test.

```text
LOCAL_EXECUTED_TEST
  -> EXECUTED_TESTED_SCOPE
  -/> PRODUCTION_VALIDITY
  -/> DISTRIBUTED_VALIDITY
  -/> CANONICAL_AUTHORITY
```

External durable-runtime designs may inform mechanisms, but AMOS imports no external authority from them.
