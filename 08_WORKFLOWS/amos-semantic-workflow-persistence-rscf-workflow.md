---
title: amos-semantic-workflow-persistence-rscf-workflow
type: workflow
Skill: amos-semantic-workflow-persistence-rscf
Agent: amos-semantic-workflow-persistence-rscf-agent
Version: 2.0.0
origin_architect: Trang Phan
steward: Trang Phan
epistemic_class: AMOS_MODEL
status: PARTIAL_EXECUTABLE
---

# Workflow: AMOS Semantic Workflow Persistence

## Objective

Persist and recover long-running AMOS workflows without confusing replay with external-effect execution, checkpoints with commits, or local reference tests with production durability.

## Hard invariants

```text
CAPABILITY != AUTHORITY
CHECKPOINT_PRESENT != EFFECT_COMMITTED
HISTORY_REPLAY != EFFECT_REEXECUTION
IDENTICAL_ARGUMENTS != IDENTICAL_OPERATION
CODE_CHANGE != REPLAY_COMPATIBLE
AMBIGUOUS != FAILED
UNKNOWN/GAP != PASS
TEST_PASS != PRODUCTION_VALIDITY
```

A failed hard invariant is non-compensatory.

## Typed state

```yaml
workflow_state:
  workflow_id: string
  run_id: integer
  code_version: string
  objective: string
  scope: string
  status: RUNNING | COMPLETED | CONTINUED_AS_NEW | BLOCKED | UNKNOWN/GAP
  explicit_state_hash: string
  event_head: string
  dependencies: []
  unresolved_effects: []
  authority_ref: optional
  provenance: []
  gaps: []
```

## State machine

```text
INTAKE
  -> BIND_IDENTITY
  -> LOAD_CHECKPOINT
  -> VERIFY_HISTORY
  -> CHECK_CODE_VERSION
  -> CLASSIFY_NEXT_STEP
       -> PURE
       -> EFFECT -> AUTHORITY_GATE
  -> RECORD_STARTED
  -> EXECUTE
       -> COMPLETED_RECEIPT
       -> RETRYABLE_PURE
       -> AMBIGUOUS_EFFECT
  -> CHECKPOINT
  -> CONTINUE_AS_NEW | FINALIZE | HOLD
```

## Execution stages

### 1. INTAKE

Bind the governing objective, scope, termination condition, and material constraints. Do not infer authority from the existence of a workflow or Skill.

### 2. BIND_IDENTITY

Require stable:

- `workflow_id`;
- `run_id`;
- `code_version`;
- dependency identity;
- provenance root.

Missing identity is `UNKNOWN/GAP`.

### 3. LOAD_CHECKPOINT

Load only persisted explicit state and receipts needed for the next decision. Do not reconstruct undeclared state from conversational similarity or model memory.

### 4. VERIFY_HISTORY

Validate:

- explicit-state hash;
- append-only event sequence;
- previous-event hash chain;
- completed-step output receipts;
- unresolved effect set.

Any integrity mismatch -> `QUARANTINE`.

### 5. CHECK_CODE_VERSION

If stored `code_version` differs from current code:

- require an explicit compatibility patch marker;
- preserve the old history semantics;
- block resume when compatibility is unknown.

A patch marker declares a compatibility path; it is not proof of universal semantic equivalence.

### 6. CLASSIFY_NEXT_STEP

Every step is classified before execution.

`PURE`:
- local/deterministic;
- no consequential external effect;
- retryable after interrupted `STARTED` state if step identity/input remain stable.

`EFFECT`:
- may mutate an external system;
- requires explicit effect/idempotency key;
- requires an applicable authority witness outside this workflow;
- may not be retried blindly after ambiguous completion.

### 7. AUTHORITY_GATE

For `EFFECT`, ask the AMOS control plane to validate authority, freshness, scope, recipient/resource constraints, and effect binding.

This workflow never self-authorizes.

### 8. RECORD_STARTED

Persist `STARTED` before invoking the operation, including:

- stable step ID;
- step kind;
- input hash;
- effect key if applicable.

### 9. EXECUTE

Execute through the declared adapter/runtime.

Outcomes:

```text
PURE success -> COMPLETED_RECEIPT
PURE interruption/error -> RETRYABLE
EFFECT success + durable receipt -> COMPLETED_RECEIPT
EFFECT started + missing/uncertain receipt -> AMBIGUOUS
```

An effect exception, timeout, worker crash, or missing acknowledgement does not prove the external system was unchanged.

### 10. RECONCILE EFFECT

`AMBIGUOUS` external effects require an independent target-state check or provider receipt.

Allowed reconciliation:

```text
AMBIGUOUS -> COMPLETED
AMBIGUOUS -> NOT_APPLIED -> RETRYABLE
```

No blind retry.

### 11. CHECKPOINT

Persist explicit workflow state, receipts, event head, dependencies, gaps, and provenance. Keep transient caches outside authoritative state unless deliberately admitted.

### 12. CONTINUE_AS_NEW

Create a new `run_id` with explicit selected carry state only.

Do not implicitly carry:

- pure-step result caches;
- undeclared model context;
- stale authority;
- unresolved effects.

An external completed effect may be reused across runs only when the caller deliberately supplies the same effect key and the input identity matches.

### 13. FINALIZE

Finalization requires:

- valid history;
- resolvable dependencies;
- compatible code version;
- no unresolved effect;
- applicable final authority for consequential commit state.

Otherwise `HOLD` / `UNKNOWN/GAP`.

## Failure and recovery table

| Condition | State | Recovery |
| --- | --- | --- |
| Pure step interrupted | RETRYABLE | replay same step identity/input |
| Effect started, no receipt | AMBIGUOUS | reconcile external target before retry |
| Effect key reused with different input | CONFLICT | reject; require new key or corrected identity |
| History/state hash mismatch | QUARANTINE | restore from independently validated checkpoint/evidence |
| Code version changed without patch | BLOCKED | add/test explicit compatibility path |
| Dependency unresolved | UNKNOWN/GAP | resolve dependency; do not guess |
| Timeout before any effect dispatch evidence | FAILED/TIMEOUT | retry only under declared policy |
| Timeout after possible effect dispatch | AMBIGUOUS | reconcile |
| Cancellation | CANCELLED | preserve checkpoint and effect state |

`TIMEOUT`, `CANCELLED`, `FAILED`, `AMBIGUOUS`, and `UNKNOWN/GAP` are distinct states.

## Parallelism

Parallel steps are allowed only when:

- step identities are distinct;
- dependency sets are independent or merge semantics are explicit;
- external effect keys are distinct unless deliberate idempotent reuse is intended;
- completion order cannot change a hard invariant.

Otherwise serialize or escalate coordination.

## Executable reference

Local reference implementation:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/durable_workflow_runtime.py`
- `19_TESTS/test_durable_workflow_runtime.py`
- `07_SKILLS/amos-semantic-workflow-persistence-rscf/scripts/durable_contract_check.py`

These provide `EXECUTED_TESTED_SCOPE` evidence for local SQLite semantics only.

## Output

```yaml
result:
  workflow_id: string
  run_id: integer
  code_version: string
  status: string
  next_transition: string | null
  unresolved_effects: []
  checkpoint_valid: true | false | unknown
  history_integrity: valid | invalid | unknown
  replay_compatibility: compatible | incompatible | unknown
  authority_state: valid | invalid | required | unknown
  provenance: []
  gaps: []
  verdict: VERIFIED_TESTED_SCOPE | PARTIAL | CONDITIONAL | UNKNOWN/GAP | QUARANTINE
```

## Evidence boundary

A successful local replay or test run does not establish distributed durability, production database guarantees, external transactional atomicity, or deployment validity.
