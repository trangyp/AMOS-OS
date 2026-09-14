---
name: amos-semantic-workflow-persistence-rscf
description: Persist, resume, audit, replay, and recover long-running AMOS workflows as typed semantic state. Use for durable checkpoints, workflow/run identity, code-version replay compatibility, pure-versus-effect separation, explicit idempotency, ambiguous external effects, continue-as-new boundaries, persistent inference/approval records, provenance, and recovery after interruption. Preserve UNKNOWN/GAP and never treat checkpoint presence, replay success, or test pass as proof that an external effect committed or that a production runtime is valid.
---

# AMOS Semantic Workflow Persistence RSCF

Apply:

`integrity > completeness > fluency > speed > token savings`

## Core object

Treat a workflow as persistent typed knowledge, not an ephemeral chat trace:

```text
WorkflowExecution =
  objective
  + scope
  + workflow_id
  + run_id
  + code_version
  + explicit_state
  + dependency_set
  + event_history
  + step_receipts
  + effect_receipts
  + provenance
  + authority_state
  + unresolved_gaps
```

Use H/M/L:

- **H** — objective, scope, authority, hard invariants, termination condition.
- **M** — workflow/run state, dependencies, checkpoints, provenance, competing hypotheses, recovery state.
- **L** — exact step identity, input/output hashes, effect keys, receipts, failures, patch markers, commands.

## Hard firewalls

```text
WORKFLOW_STATE != CONVERSATION_TEXT
CHECKPOINT_PRESENT != EFFECT_COMMITTED
HISTORY_REPLAY != EFFECT_REEXECUTION
IDENTICAL_ARGUMENTS != IDENTICAL_OPERATION
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
CODE_CHANGE != REPLAY_COMPATIBLE
TEST_PASS != PRODUCTION_VALIDITY
UNKNOWN/GAP != PASS
AMBIGUOUS != FAILED
```

Do not compensate for a failed hard invariant with confidence, retries, popularity, or another passing metric.

## Step classes

Classify every executable step before running it.

### PURE

A local/deterministic computation with no consequential external effect.

A `PURE` step may be retried after an interruption if its identity and input hash are unchanged.

### EFFECT

A step that may change external state: tool write, API mutation, message send, deployment, payment, file mutation, database write, etc.

An `EFFECT` step requires:

- stable `step_id`;
- explicit caller-owned `effect_key` / idempotency key;
- input hash;
- authority witness outside the Skill when the action is consequential;
- durable completion receipt or explicit reconciliation result.

Never infer idempotency from tool name, arguments, prompt text, or semantic similarity.

## Effect state machine

```text
NEW -> STARTED -> COMPLETED(receipt)
              \-> AMBIGUOUS -> RECONCILE
                                -> COMPLETED
                                -> RETRYABLE -> STARTED
```

`STARTED + no durable completion receipt` is `AMBIGUOUS` for an external effect.

Do not automatically retry an ambiguous effect. A timeout, worker crash, network error, or missing acknowledgement does not prove the target system was unchanged.

## Resume gate

Resume only when all load-bearing predicates hold:

```text
object_identity_stable
AND checkpoint_valid
AND dependencies_resolvable
AND event_history_integrity_valid
AND code_version_compatible
AND no_unresolved_effect
```

If any predicate is unresolved, return `UNKNOWN/GAP` or `AMBIGUOUS` and stop the unsafe transition.

## Code evolution

Stored execution history is version-bound.

When workflow code changes:

1. identify the prior `code_version`;
2. determine whether replay semantics changed;
3. require an explicit compatibility/patch marker for an in-flight run;
4. preserve old history semantics during the compatibility window;
5. re-run replay/regression tests before retiring legacy compatibility behavior.

A patch marker is a deliberate compatibility declaration, not universal proof of semantic equivalence.

## Continue-as-new

Use a new run boundary for long-lived workflows when history/state should be compacted or a new execution epoch should begin.

Carry only explicitly selected state.

Do **not** silently carry:

- transient caches;
- model outputs that are not declared state;
- completed pure-step results merely because they have identical arguments;
- unresolved effects.

External effects may be reused across runs only through the same explicit effect key and matching input identity.

## Operational workflow

1. **Bind identity** — objective, scope, workflow ID, run ID, code version.
2. **Load minimal state** — checkpoint, dependencies, event head, unresolved effect set.
3. **Classify step** — `PURE` or `EFFECT` before execution.
4. **Gate authority** — consequential effect permission stays in the AMOS control plane.
5. **Execute** — record `STARTED` before invoking work.
6. **Persist receipt** — output hash and effect receipt on completion.
7. **Recover** — pure steps may retry; ambiguous effects require reconciliation.
8. **Replay/audit** — verify history/state hashes and version compatibility.
9. **Continue or finalize** — no unresolved effect may cross finalization or continue-as-new.
10. **Emit RSCF** — evidence class, scope, gaps, provenance, falsifier, bounded conclusion.

## Deterministic checks

Use the repository executable surfaces when available:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/durable_workflow_runtime.py` — local executable durable reference.
- `19_TESTS/test_durable_workflow_runtime.py` — restart/replay/effect adversarial tests.
- `scripts/durable_contract_check.py` — validate a serialized workflow snapshot; unresolved effects quarantine the snapshot.

For generic semantic checks, preserve the installed AMOS rules:

- deterministic operation -> `DERIVE`;
- mediated LLM judgment -> `INFER`;
- otherwise -> `UNKNOWN/GAP`;
- direct state transitions require an executor-mediated declared slot.

## Output contract

Return the smallest sufficient structure:

```yaml
workflow_id: string
run_id: integer
status: RUNNING | COMPLETED | CONTINUED_AS_NEW | BLOCKED | UNKNOWN/GAP
code_version: string
step_state: optional
unresolved_effects: []
checkpoint_valid: true | false | unknown
history_integrity: valid | invalid | unknown
replay_compatibility: compatible | incompatible | unknown
provenance: []
gaps: []
verdict: VERIFIED_TESTED_SCOPE | PARTIAL | CONDITIONAL | UNKNOWN/GAP | QUARANTINE
```

`VERIFIED_TESTED_SCOPE` refers only to the exact executed reference/test boundary. Never promote it to distributed or production validity without new evidence.

## Failure handling

- missing workflow/run identity -> `UNKNOWN/GAP`;
- stale or mismatched input for the same step -> replay divergence;
- reused effect key with different input -> hard conflict;
- effect started without receipt -> `AMBIGUOUS`;
- changed code without compatibility marker -> block resume;
- history/state hash mismatch -> quarantine;
- missing dependency -> `UNKNOWN/GAP`;
- unresolved effect -> block finalization and continue-as-new;
- production/distributed claim from local test -> reject overreach.

## Progressive references

Read only when needed:

- `references/durable-execution.md` — source lineage, Temporal/DBOS mechanisms, effect/replay failure modes.
- `references/vault_domain_knowledge.md` — broader AMOS/RSCF knowledge.
- `references/references_MOC.md` — package navigation.

External framework behavior is evidence input, never AMOS authority.
