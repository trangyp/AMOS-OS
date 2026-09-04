---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Skills Skill Contract
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

# Skills Plane Contract

## 0. Contract boundary

This contract governs **skill identity, capability semantics, package structure, composition, runtime binding, governance, validation, transfer and lifecycle maintenance**.

```text
REGISTRY ENTRY != PAYLOAD
PAYLOAD != EXECUTABLE
EXECUTABLE != VALIDATED
LOCAL PASS != GENERALIZATION
SKILL OUTPUT != AUTHORITY
SKILL PACKAGE != WORKFLOW
```

Documentary compliance does not prove runtime enforcement.

## 1. Hard invariants

1. One stable skill identity resolves before invocation.
2. Aliases never silently merge distinct payload/version identities.
3. Capability semantics are separate from host availability and authority.
4. Parent/child delegation may narrow but not silently widen scope or effects.
5. Skill composition preserves provenance, epistemic class, scope/regime and authority constraints.
6. A privileged/effectful skill cannot self-authorize external effects.
7. Validation claims bind the exact skill version/payload, environment and test envelope.
8. Local benchmark success does not establish cross-task/role/model/host transfer.
9. Multiple packages descending from one source/model do not provide independent evidence.
10. Missing payload/dependency/authority/freshness produces an explicit state, never fabricated capability.
11. Entry-point growth must not defeat progressive loading.
12. Library maintenance may quarantine or supersede a skill but must preserve lineage.

## 2. Skill contract envelope

```yaml
skill_contract:
  identity:
    skill_id:
    version:
    canonical_name:
    aliases: []
    semantic_origin:
  trigger:
    use_when: []
    do_not_use_when: []
  capability:
    purpose:
    inputs: []
    outputs: []
    effect_class:
    side_effects: []
  package:
    entrypoint:
    references: []
    scripts: []
    assets: []
    payload_ref:
    payload_hash:
  runtime:
    host_binding:
    connector_requirements: []
    tool_bindings: []
    model_bindings: []
    environment_assumptions: []
  composition:
    parent:
    children: []
    sibling_boundaries: []
    dependencies: []
    workflow_interfaces: []
  governance:
    scope:
    regime:
    authority_requirements: []
    data_exposure:
    security_constraints: []
    freshness_requirements: []
  validation:
    positive: []
    negative: []
    transfer: []
    composition: []
    falsifiers: []
    invalidation_conditions: []
  provenance:
    source_refs: []
    dependency_ancestry: []
    license_ip:
  lifecycle:
    state:
    debt_state:
    quarantine:
    supersession:
    retirement:
    rollback:
```

## 3. Resolution and admission

```text
DISCOVER
→ RESOLVE STABLE ID + VERSION
→ RECONCILE REGISTRY / LOCK / CATALOG
→ RESOLVE PAYLOAD
→ VERIFY DEPENDENCIES
→ VERIFY HOST COMPATIBILITY
→ BIND TASK SCOPE / REGIME
→ BIND SECURITY / EXPOSURE / AUTHORITY
→ CHECK VALIDATION STATE
→ ADMIT / HOLD / DENY / UNKNOWN-GAP
```

Filename similarity and folder presence are only discovery signals.

## 4. Progressive package architecture

A high-quality skill is a compact control plane, not a vault dump.

```text
metadata
→ SKILL.md
→ targeted reference
→ raw source only when decision-relevant
```

Use `scripts/` only when deterministic repeatability is stronger than prose. Use `assets/` only for output-consumed artifacts. References remain source- and version-bound.

## 5. Composition contract

A parent or workflow may call a skill only with a typed input envelope and must receive a typed result envelope.

**Accept**
- target/task;
- scope/regime;
- evidence/source bundle;
- authority context when effectful;
- optional prior state.

**Return**
- result and conclusion class;
- gaps/contradictions;
- provenance/dependencies;
- effect proposal if any;
- invalidation conditions;
- escalation requirement.

A child may not inherit undeclared authority from its caller.

## 6. Library-time maintenance

Skill quality is partly an ecosystem property.

Maintain a `SkillHealth` vector:

```text
SkillHealth =
[utility, compatibility, risk, validation, freshness,
 provenance, duplication, materialization, retrievability, maintainability]
```

This vector is an AMOS governance model; it is not an established universal metric and need not be collapsed to one score.

Debt detection should flag:
- trigger overlap;
- orphaned dependencies;
- missing payload;
- stale environment binding;
- obsolete source revision;
- undocumented privileged effect;
- untested fallback;
- duplicate semantic origin;
- incompatible composition;
- unbounded context/reference expansion.

## 7. Transfer and generalization

When reusability matters, test beyond the task that produced the skill.

```text
TransferEvidence =
task × role × model × host × environment × regime × time
```

Record `TESTED`, `FAILED`, or `UNKNOWN`; absence of evidence is not transfer success.

Research such as AFTER (arXiv:2606.23127) motivates this evaluation dimension. Its reported benchmark results remain external `SOURCE_CLAIM`.

## 8. Security and supply-chain boundary

Before admitting an effectful or externally sourced skill:
- bind semantic origin and payload identity;
- inspect dependency and tool privileges;
- identify data/exposure channels;
- validate least-required capability;
- preserve revocation/freshness;
- test negative permissions;
- quarantine ambiguous or tampered provenance.

A signed or popular skill is not necessarily safe.

## 9. Evolution

```text
DRAFT
→ DISCOVERED
→ RESOLVED
→ MATERIALIZED
→ EXECUTABLE
→ LOCALLY_VALIDATED
→ [TRANSFER_VALIDATED]
→ [COMPOSITION_VALIDATED]
→ GOVERNANCE_ADMITTED
→ ACTIVE
→ QUARANTINED / SUPERSEDED / RETIRED
```

Brackets indicate optional evidence states, not mandatory claims.

Skill evolution must preserve predecessor identity, changed semantics, migration effects, validation evidence and rollback path.

## 10. Workflow boundary

Workflows own sequencing and graph control. Skills own reusable capability semantics.

A workflow-specific adaptation should be represented as parameters/adapters or a distinct versioned skill only when capability semantics materially change.

## 11. Falsifiers / repair

Revise or quarantine a skill if:
- registry and payload identities diverge;
- its trigger routes materially outside declared capability;
- required dependencies cannot be resolved;
- negative-path testing exposes undeclared effects;
- transfer/composition evidence contradicts generalized claims;
- source provenance is revoked or invalidated;
- a newer canonical contract supersedes load-bearing semantics.

Repair the smallest affected edge and revalidate descendants.

## 12. Current known gap

The 2026-09-03 registry reconciliation records substantial namespace/materialization mismatch across Drive registry, corpus and external lock views. Therefore, plane-wide installed/executable completeness remains `UNKNOWN/GAP`.

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- [[07_SKILLS/SKILLS_README|SKILLS_README]]
- [[07_SKILLS/00_INDEX/SKILL_MAP|SKILL_MAP]]
- [[26_WORKFLOWS/26_WORKFLOWS_MOC|WORKFLOWS]]
- [[06_AGENTS/06_AGENTS_MOC|AGENTS]]
- [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|CONTROL_PLANE]]
- [[18_SECURITY/18_SECURITY_MOC|SECURITY]]
- [[19_TESTS/19_TESTS_MOC|TESTS]]
- [[22_RESEARCH/22_RESEARCH_MOC|RESEARCH]]

---
RSCF-NODE
node_id: skills_skill_contract
node_type: contract
path: 07_SKILLS/SKILLS_SKILL_CONTRACT.md
claim_class: AMOS_MODEL
