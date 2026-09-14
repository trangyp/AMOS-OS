---
title: amos-distributed-attack-composition-monitor-rscf-workflow
type: workflow
skill: amos-distributed-attack-composition-monitor-rscf
agent: amos-distributed-attack-composition-monitor-rscf-agent
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
---

# Distributed Attack Composition Workflow

`INGEST -> NORMALIZE -> LOCAL_ALLOW_FILTER -> WINDOW -> POLICY_EPOCH_GATE -> COMPOSE -> MINIMAL_CUT -> BLOCK|NO_MATCH|REVALIDATE`

## Gates
1. Bind exact event identity, principal, session, repository, target, effect and provenance.
2. Analyze only declared rule atoms; no free-form inference may silently become a hard block condition.
3. Exclude locally denied/unknown actions from the harder “locally allowed but globally harmful” composition test.
4. Require one policy epoch across the rule and candidate events.
5. Apply rule window plus configured distinct-principal/session constraints.
6. If matched, derive a bounded minimum-cardinality satisfying event set when candidate count <= 12.
7. Emit evidence only; response, rollback, quarantine, repository write or enforcement authority is separate.

Terminal states: `BLOCK_COMPOSITION | NO_COMPOSITION_MATCH | REVALIDATE_COMPOSITION | UNKNOWN_GAP`.
