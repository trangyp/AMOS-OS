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

Persist and recover long-running AMOS workflows as typed state while preserving the distinction between deterministic replay and external effects.

## Invariants

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

## Runtime state

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

## Transition graph

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

## Gates

### Identity gate

Require stable workflow ID, run ID, code version, dependency identity, and provenance root. Missing identity -> `UNKNOWN/GAP`.

### Checkpoint gate

Load only explicit persisted state and receipts. Conversational similarity, model memory, or a cached response is not authoritative workflow state.

### Integrity gate

Validate state hash, event sequence/hash chain, completed-step receipts, and unresolved-effect set. Mismatch -> `QUARANTINE`.

### Version gate

A changed workflow implementation requires an explicit compatibility patch marker before an in-flight history may resume. Preserve old-history behavior until the compatibility window is deliberately retired.

### Step classification gate

`PURE` steps are local/deterministic and may retry after interruption if step identity/input remain stable.

`EFFECT` steps can alter external state and require an explicit effect key, applicable authority, and a durable receipt/reconciliation boundary.

### Authority gate

The AMOS control plane validates consequential effect authority. Workflow capability never self-grants permission.

### Execution gate

Record `STARTED` before work.

```text
PURE success -> COMPLETED
PURE interruption -> RETRYABLE
EFFECT success + receipt -> COMPLETED
EFFECT possible dispatch + uncertain receipt -> AMBIGUOUS
```

### Reconciliation gate

An ambiguous effect must be checked against the actual target/provider before any retry.

```text
AMBIGUOUS -> COMPLETED
AMBIGUOUS -> NOT_APPLIED -> RETRYABLE
```

No blind retry.

### Continue-as-new gate

New run boundaries carry only explicitly selected state. They may not silently carry result caches, undeclared model context, stale authority, or unresolved effects.

### Finalization gate

Finalize only with valid history, resolvable dependencies, compatible code, no unresolved effects, and required final authority.

## Failure semantics

```text
TIMEOUT != CANCELLED
CANCELLED != FAILED
FAILED != AMBIGUOUS
AMBIGUOUS != UNKNOWN/GAP
UNKNOWN/GAP != SUCCESS
```

A timeout after possible external dispatch is `AMBIGUOUS`, not a safe retry signal.

## Parallelism

Parallel transitions require distinct step identities, dependency independence or explicit merge semantics, and compatible effect-key semantics. Otherwise serialize.

## Executable evidence

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/durable_workflow_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/DURABLE_WORKFLOW_CONTRACT.md`
- `19_TESTS/test_durable_workflow_runtime.py`
- `07_SKILLS/amos-semantic-workflow-persistence-rscf/scripts/durable_contract_check.py`

The executable evidence supports only the declared local reference boundary.

## Output schema

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

## Boundary

Local reference validation does not establish production durability, distributed consensus, multi-worker leasing, external transaction atomicity, or deployment authority.
