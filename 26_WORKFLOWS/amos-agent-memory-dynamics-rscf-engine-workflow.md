---
title: amos-agent-memory-dynamics-rscf-engine-workflow
type: workflow-projection
Skill: amos-agent-memory-dynamics-rscf-engine
Agent: amos-agent-memory-dynamics-rscf-engine-agent
version: 2.0.0
origin_architect: Trang Phan
domain: memory
canonical_workflow: 08_WORKFLOWS/amos-agent-memory-dynamics-rscf-engine-workflow.md
---

# Memory Dynamics Workflow Projection

Canonical operational workflow:

`08_WORKFLOWS/amos-agent-memory-dynamics-rscf-engine-workflow.md`

This projection preserves the routing contract without redefining lifecycle semantics.

## Routing

```text
READ -> scope gate -> temporal revision -> OBSERVATION
WRITE -> authority gate -> optimistic revision gate -> append event -> integrity gate
CONFLICT -> bind exact revisions -> quarantine both -> evidence governance
CONTEXT -> retrieve -> budget -> hash-bound snapshot -> replay/staleness gate
```

## Non-negotiable invariants

```text
MEMORY != KNOWLEDGE
RETRIEVAL != VERIFICATION
RELEVANCE != TRUTH
REMEMBERED != AUTHORIZED
REVISION != OVERWRITE
CONFLICT != WINNER
```

Do not duplicate the detailed state machine here. Update the canonical `08_WORKFLOWS` owner first and keep this projection synchronized to its identity/version.
