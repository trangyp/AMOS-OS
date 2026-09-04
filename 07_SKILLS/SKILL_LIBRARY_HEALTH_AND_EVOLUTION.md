---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Skill Library Health And Evolution
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Skill Library Health and Evolution

## 0. Purpose

This artifact owns **library-level health, maintenance and evolution** for AMOS Skills.

It does not own task-time orchestration, agent identity, tool authority, or canon admission.

```text
PER-SKILL PASS != LIBRARY HEALTH
MORE SKILLS != MORE CAPABILITY
DUPLICATE NAMES != INDEPENDENT CAPABILITIES
SEMANTIC SIMILARITY != BEHAVIORAL COMPATIBILITY
POPULAR != VALIDATED
REUSED != SAFE
```

## 1. Health dimensions

### Utility
Observed usefulness for declared task classes.

### Compatibility
I/O, dependency, host, tool/model and workflow compatibility.

### Validation
Positive, negative, transfer and regression evidence.

### Risk
Effect class, data exposure, security, authority and irreversible-action risk.

### Retrieval quality
Whether the right skill is selected under task/scope/host constraints.

### Redundancy
Intent-equivalent or behavior-equivalent skills competing for the same route.

### Freshness
Dependency, host, model, tool, protocol and domain validity.

### Context footprint
Prompt/reference size and repeated context cost.

### Evolution debt
Accumulated patches, aliases, superseded variants, unresolved conflicts and missing migrations.

## 2. Library health record

```yaml
skill_library_health:
  epoch:
  registry_snapshot:
  skill_count_observed:
  identity_conflicts: []
  redundancy_clusters: []
  dependency_conflicts: []
  stale_bindings: []
  validation_gaps: []
  high_risk_unvalidated: []
  quarantined: []
  supersession_debt: []
  retrieval_failures: []
  context_hotspots: []
  unresolved_gaps: []
  receipts: []
```

Counts are epoch-bound observations, not permanent truth.

## 3. Technical debt classes

- **Identity debt** — aliases/duplicates with unresolved precedence.
- **Contract debt** — missing/ambiguous triggers, inputs, outputs, effects or failure modes.
- **Dependency debt** — stale/missing/incompatible tool/model/package requirements.
- **Validation debt** — absent negative, transfer or regression evidence.
- **Routing debt** — overbroad triggers, retrieval collisions, superseded skills winning selection.
- **Security debt** — state-changing effects without sufficient authority/exposure constraints.
- **Context debt** — unnecessarily large entrypoints or repeated source payloads.
- **Evolution debt** — patches and forks not reconciled into governed versions.
- **Provenance debt** — missing source identity/ancestry or correlated validators treated as independent.

## 4. Behavioral compatibility gate

Before merging or generalizing two skills:

```text
CANDIDATE_SIMILARITY
→ CROSS-CASE REPLAY
→ FAILURE-MODE COMPARISON
→ MECHANISM COMPATIBILITY
→ SCOPE INTERSECTION
→ REGRESSION CHECK
→ GENERALIZE OR KEEP SEPARATE
```

A merge fails if the generalized skill loses validated behavior of a constituent case or widens effect/authority scope without new governance.

## 5. Redundancy handling

Possible states:

- `ALIAS` — same logical identity, different name.
- `DUPLICATE` — same capability and behavior; consolidate if lineage allows.
- `OVERLAP` — partial shared scope; preserve boundaries.
- `COMPETING` — same target with materially different assumptions/mechanisms.
- `SUPERSEDING` — newer governed version replaces older within declared scope.
- `DISTINCT` — superficially similar but behaviorally or semantically different.

Do not collapse `OVERLAP` or `COMPETING` into `DUPLICATE` just to reduce counts.

## 6. Evolution lifecycle

```text
EXPERIENCE / FAILURE
→ INSTANCE PATCH
→ LOCAL VALIDATION
→ CANDIDATE REUSE
→ CROSS-CASE REPLAY
→ GENERALIZATION CHECK
→ VERSIONED SKILL
→ REGRESSION TEST
→ ADMISSION
→ OBSERVATION
→ PATCH / QUARANTINE / SUPERSEDE / RETIRE
```

## 7. Scope expansion rule

A skill may expand scope only when:
- new scope is explicitly declared;
- prior behavior remains valid;
- new dependencies are resolved;
- new effect risks are governed;
- transfer/regression evidence exists;
- invalidation conditions are updated.

```text
SCOPE EXPANSION != TEXT GENERALIZATION
```

## 8. Context and progressive loading

Entrypoints should carry triggers, runtime, invariants, resource loading and failure behavior.
Large canon/research/reference content belongs in referenced files.

```text
SKILL.md != VAULT DUMP
```

Library maintenance should identify:
- oversized entrypoints;
- duplicated source bodies;
- dead references;
- deeply nested loading paths;
- frequently loaded low-value material.

## 9. Retrieval-health checks

For each routed invocation ask:
1. Was identity resolved?
2. Was the selected skill applicable to scope/regime?
3. Were dependencies available?
4. Was the host compatible?
5. Was the skill fresh?
6. Was validation sufficient for the task stakes?
7. Did a superseded or quarantined skill win retrieval?
8. Was there a more specific skill?
9. Were multiple candidates actually aliases or competing mechanisms?

## 10. Library maintenance loop

```text
SNAPSHOT
→ DIAGNOSE
→ PRIORITIZE BY CONSEQUENCE × FAN-OUT × RECOVERABILITY
→ REPAIR LOCALLY
→ REPLAY AFFECTED CASES
→ CHECK PROTECTED REGRESSIONS
→ UPDATE REGISTRY / LOCK / CATALOG
→ EMIT RECEIPT
```

Priority is conceptual; no universal numeric formula is asserted.

## 11. Research boundary

SkillOps, SkillCommit, SkillCraft and the 2026 Agent Skills ecosystem analysis motivate these library-level concerns. Their reported results remain external source claims. AMOS-specific effectiveness requires AMOS-specific execution evidence.

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- [[07_SKILLS/SKILLS_SKILL_CONTRACT|SKILLS_SKILL_CONTRACT]]
- [[07_SKILLS/amos-skill-registry-gateway|SKILL_REGISTRY_GATEWAY]]
- [[26_WORKFLOWS/26_WORKFLOWS_MOC|WORKFLOWS]]
- [[22_RESEARCH/AGENT_SKILLS_WORKFLOWS_SOTA_2026-09-04|SOTA_RESEARCH]]

---
RSCF-NODE
node_id: skill_library_health_and_evolution
node_type: skill_library_governance
path: 07_SKILLS/SKILL_LIBRARY_HEALTH_AND_EVOLUTION.md
claim_class: AMOS_MODEL
