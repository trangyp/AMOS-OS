# Durable execution reference

## Purpose

This reference binds the AMOS semantic-workflow Skill to concrete durable-execution mechanisms without granting external frameworks authority over AMOS architecture.

## AMOS runtime owner

Primary executable surface:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/durable_workflow_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/DURABLE_WORKFLOW_CONTRACT.md`
- `19_TESTS/test_durable_workflow_runtime.py`

Use these as the local executable evidence surface. Do not infer distributed or production guarantees from the reference runtime.

## External source: Temporal Python SDK

Repository: `temporalio/sdk-python`

Pinned source commit: `ab25ed693f7ec77589346e66c98db299a8c9c9fe`

Source class: `SOURCE_CLAIM + SOURCE_CODE`.

Mechanisms relevant to AMOS:

- workflow execution is reconstructed from durable history rather than from ordinary in-process memory;
- workflow-code changes can make replay nondeterministic, so compatibility/version markers must preserve old history semantics;
- continue-as-new creates a new run boundary while deliberately carrying selected state;
- external work is modeled separately from deterministic workflow replay;
- a 2026 fix at the pinned commit demonstrates a concrete failure mode: caching/deduplicating repeated identical agent tool/model/backend calls can serve stale results and can break replay compatibility across code changes;
- legacy histories may require old behavior to remain available until their compatibility patch can be retired.

AMOS adaptation:

- do not deduplicate work from `(name, args)` similarity;
- only an explicit caller-owned idempotency/effect key licenses effect receipt reuse;
- bind code-version compatibility to explicit patch markers;
- preserve old execution history rather than rewriting it to fit new behavior.

Not imported:

- Temporal server architecture;
- Temporal-specific APIs or deployment model;
- claims that Temporal semantics automatically make an AMOS effect safe.

## External source: DBOS Transact Python

Repository: `dbos-inc/dbos-transact-py`

Pinned source commit: `83805fd84494c85ea09105443884a2786152d921`

Source class: `SOURCE_CLAIM + SOURCE_CODE`.

Mechanisms relevant to AMOS:

- workflow and step state are persisted in a database;
- interrupted workflows resume from durable completed work rather than restart from the beginning;
- workflow identity can act as an explicit idempotency boundary for event processing;
- durable waits/notifications are persisted state transitions rather than sleeping process memory;
- programmatic workflow state enables targeted recovery and restart from a known step.

AMOS adaptation:

- persist workflow/run identity, explicit state and step receipts;
- distinguish checkpoint recovery from effect atomicity;
- make idempotency explicit rather than inferred from payload equality;
- expose recovery state for audit/reconciliation.

Not imported:

- Postgres dependency as an AMOS requirement;
- DBOS deployment or queue architecture;
- external exactly-once claims as universal guarantees.

## AMOS invariants

```text
WORKFLOW_HISTORY != EXTERNAL_WORLD_STATE
CHECKPOINT != COMMIT_RECEIPT
REPLAY != EFFECT_REEXECUTION
IDENTICAL_INPUT != IDENTICAL_OPERATION
IDEMPOTENCY_KEY_REUSE + DIFFERENT_INPUT -> CONFLICT
STARTED_EFFECT + NO_RECEIPT -> AMBIGUOUS
AMBIGUOUS -> RECONCILE_BEFORE_RETRY
CODE_CHANGE != REPLAY_COMPATIBLE
CONTINUE_AS_NEW != IMPLICIT_CACHE_COPY
TEST_PASS != PRODUCTION_DURABILITY
```

## Resume gate

Resume only when all load-bearing conditions hold:

```text
object_identity_stable
AND checkpoint_valid
AND dependencies_resolvable
AND event_history_integrity_valid
AND code_version_compatible
AND no_unresolved_effect
```

Any unresolved condition remains `UNKNOWN/GAP` or `AMBIGUOUS`; it may not be converted to success by confidence, timeout, or retry count.

## Effect-state rule

For external effects:

```text
NEW -> STARTED -> COMPLETED(receipt)
              \-> AMBIGUOUS -> reconciliation
```

An effect callback exception is not proof that the external effect failed. Network failure, timeout, worker death, and acknowledgement loss can leave the target system changed while the local process lacks a receipt.

Therefore automatic retry from `AMBIGUOUS` is prohibited.

## Epistemic boundary

The local SQLite runtime is an `EXECUTED_MODEL` reference implementation. It establishes only the behavior covered by its tests. Production storage durability, multi-process concurrency, distributed leases, consensus, external transactional semantics, and operational recovery remain separate evidence requirements.
