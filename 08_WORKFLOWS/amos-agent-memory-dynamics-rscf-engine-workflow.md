---
title: amos-agent-memory-dynamics-rscf-engine-workflow
type: workflow
Skill: amos-agent-memory-dynamics-rscf-engine
Agent: amos-agent-memory-dynamics-rscf-engine-agent
version: 2.0.0
origin_architect: Trang Phan
domain: memory
---

# Workflow: Agent Memory Dynamics RSCF Engine

A memory workflow is a governed state transition, not a retrieval shortcut.

## Preconditions

- resolve namespace and requested operation;
- resolve caller scopes and external write authority when mutation is requested;
- bind memory identity and provenance for writes;
- bind `as_of` for historical reads when relevant;
- preserve `MEMORY != KNOWLEDGE`.

## Read path

1. Validate namespace and scope.
2. Resolve the revision valid at `as_of`.
3. Exclude quarantined, tombstoned, and expired memory by default.
4. Return retrieval result as `OBSERVATION` regardless of source class.
5. If building context, enforce the explicit context budget and persist a snapshot identity/hash.
6. Mark snapshot replay stale when selected revisions are no longer latest.
7. Fail closed if a selected memory is now quarantined or tombstoned.

## Write path

1. Require a valid external control-plane write decision; Skill invocation is not authority.
2. `ADMIT`: require stable ID, namespace, provenance, scope, source class, content, and temporal coordinates.
3. `REVISE`: require `expected_revision`; reject stale writers.
4. Preserve the prior revision and close its validity window.
5. `QUARANTINE` or `TOMBSTONE`: require expected revision and explicit reason.
6. Append the lifecycle event to the hash chain.
7. Verify local integrity after consequential mutation.
8. Never promote a successful memory write to knowledge or canon automatically.

## Conflict path

1. Accept a conflict only when an upstream evidence process identifies incompatible memories.
2. Bind both exact memory revisions.
3. Record the conflict and quarantine both memories.
4. Preserve both provenance chains.
5. Route resolution to evidence/knowledge governance.
6. Do not choose a winner using retrieval score, recency alone, or repetition.

## Terminal states

- `READ_OBSERVATION`
- `CONTEXT_SNAPSHOT_CREATED`
- `MEMORY_MUTATION_RECORDED`
- `QUARANTINED`
- `TOMBSTONED`
- `STALE_WRITE_REJECTED`
- `AUTHORITY_GAP`
- `INTEGRITY_QUARANTINE`
- `UNKNOWN/GAP`

## Validation

Execute:

```bash
python 07_SKILLS/amos-agent-memory-dynamics-rscf-engine/scripts/memory_lifecycle.py --self-test
python -m unittest -v 19_TESTS/test_memory_lifecycle.py
```

A local pass proves only the tested SQLite semantics.
