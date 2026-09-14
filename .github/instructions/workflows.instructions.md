---
description: AMOS workflow state, authority, replay, recovery, observability, and agent handoff rules.
applyTo: '08_WORKFLOWS/**'
---

# AMOS Workflow Instructions

A workflow is an executable state-transition contract, not a prose checklist.

## Minimum workflow model

For every material workflow declare:
- objective and terminal states;
- typed inputs/outputs;
- participating agents/skills/tools;
- preconditions and postconditions;
- transition guards;
- authority required per effectful step;
- retry policy and retry ceiling;
- idempotency key strategy for durable effects;
- timeout/cancellation behavior;
- failure and recovery transitions;
- observability/provenance outputs;
- rollback or reconciliation path.

## Handoff invariant

Each handoff must preserve task identity, authoritative constraints, provenance, unresolved gaps, and effect state. A receiving agent must not infer missing authority from the fact that a prior agent requested a handoff.

## Parallelism

Parallelize only branches with explicit independence or safe merge semantics. Preserve deterministic merge rules for shared state. If two branches can mutate the same authoritative object, route through concurrency/commit control.

## Failure semantics

Do not collapse TIMEOUT, CANCELLED, FAILED, UNKNOWN, EXTERNALIZED_UNKNOWN, and SUCCEEDED into one boolean. Blind retry after an ambiguous external effect is prohibited; reconcile first.

## Validation

Test the happy path plus malformed input, unauthorized effect, stale state, dependency failure, timeout, duplicate/replay, partial completion, and recovery when applicable.
