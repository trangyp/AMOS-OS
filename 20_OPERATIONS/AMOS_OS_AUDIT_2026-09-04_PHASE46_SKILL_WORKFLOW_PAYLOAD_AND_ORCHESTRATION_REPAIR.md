---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Os Audit 2026 09 04 Phase46 Skill Workflow Payload And Orchestration Repair
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

# AMOS OS Audit — Phase46 Skill / Workflow Payload and Orchestration Repair

## Objective

Continue beneath prior plane-level MECE repair and fix high-value active Skill/Workflow payload defects:
placeholder content, missing materialization, stale orchestration assumptions, syntax corruption, and missing state/effect/applicability semantics.

## Inventory boundary

The current Skill evidence contains different denominators:
- legacy Drive registry snapshot: **343 names**;
- external `.devin/skills` lock snapshot: **696 names**;
- Drive corpus census: **1,086 observed `SKILL.md` objects**.

These are different scopes.

```text
OBJECT_COUNT != ACTIVE_SKILL_COUNT
REGISTERED != MATERIALIZED
MATERIALIZED != APPLICABLE
APPLICABLE != EFFECTIVE
MIRROR != INDEPENDENT CAPABILITY
```

The workflow metadata normalization registry contains **294 normalized workflow entries**, all classified as `workflow_specification / AMOS_MODEL` in that registry scope.

This pass therefore used inventory breadth for coverage but exact Drive identity for mutation.

## F46-01 — `amos-skill-builder` was still a placeholder

Observed exact Drive object:
`1IojH2znqct0xPWC3AWoE10mnFU5KYYQF`

Before repair:
- 349 bytes;
- explicit placeholder description;
- no operational builder runtime.

### Repair

Replaced the same object in place with a source-bound Skill Builder implementing:
- ORIENT/READ/PARSE/TYPE/UNDERSTAND/MODEL/PLAN/CREATE/VALIDATE/EXECUTE/CHALLENGE/REPAIR/PACKAGE;
- H/M/L;
- capability manifests;
- applicability lifecycle;
- effect classes;
- Skill composition relations;
- validation ladder;
- negative-test/retest behavior;
- cross-layer alignment;
- update attribution;
- package/install boundary.

## F46-02 — `amos-workflow-builder` folder had no materialized Skill

Observed folder:
`1QUA5OT_jtzhN5Ezk2pMQmCJ2hDfGRfvD`

Fresh folder listing returned no child payload.

### Repair

Created `SKILL.md` in that existing folder, preserving the preexisting logical namespace.

The new Skill owns workflow graph construction and audit, not Skill semantics or effect authority.

## F46-03 — Builder workflows were stale and architecturally over-constrained

### Skill Builder workflow

Old metadata included contradictory workflow epistemic classes and a generic runtime trigger.

Replaced in place with v2:
`RESOLVE_AUTHORITY -> INVENTORY -> GAP_CLASSIFY -> SOURCE -> CONTRACT -> BUILD_OR_REPAIR -> STATIC_VALIDATE -> NEGATIVE_TEST -> EXECUTE_IF_APPLICABLE -> CROSS_LAYER_AUDIT -> RETEST -> PACKAGE -> REGISTRY_PROPOSAL -> RECEIPT`.

### Workflow Builder workflow

The previous workflow imposed a universal `workflow -> agent -> skill` 1:1:1 binding.

That is incompatible with Full Brain orchestration where one workflow may compose several typed capabilities.

Replaced in place with v2 and this rule:

```text
ONE PRIMARY ORCHESTRATION OWNER
+ 0..N AGENTS
+ 0..N SKILLS
+ TYPED EDGES
```

Canonical node classes:
`READ | DERIVE | VALIDATE | PROPOSE | AUTHORIZE | COMMIT | OBSERVE | COMPENSATE | ESCALATE`.

## F46-04 — Skill applicability was under-modeled

Added to `07_SKILLS_MOC`:

```text
DISCOVERED
-> REGISTERED
-> MATERIALIZED
-> LOADABLE
-> APPLICABLE
-> EXECUTABLE
-> VALIDATED
-> ACTIVE
```

Hard distinctions:
`SKILL_RETRIEVED != SKILL_APPLICABLE != SKILL_EFFECTIVE`
and
`SIMILAR_TO != DEPEND_ON != COMPOSE_WITH`.

Added payload-quality criteria so file length alone is not treated as a defect.

## F46-05 — Workflow graph/effect semantics required deeper MECE structure

Added to `26_WORKFLOWS_MOC`:
- typed node and edge classes;
- 0..n capability bindings;
- read/write sets;
- effect class;
- commit-time freshness;
- idempotency/retry/compensation;
- `IN_DOUBT`;
- execution-feedback refinement;
- quality metrics beyond final task success.

## F46-06 — Obsidian Markdown corruption in Sensory Map Skill

`amos-sensory-map-integrator/SKILL.md` had escaped YAML/headings/Markdown (`\---`, `\#`, escaped emphasis), making normal Obsidian rendering unreliable.

Replaced same Drive object in place with normalized Markdown while preserving the substantive sensory-map contract.

## F46-07 — Current research was not yet represented in the vault's Skill/Workflow architecture

Created:
`22_RESEARCH/SKILL_WORKFLOW_SOTA_2026-09-04.md`

Research sources include:
- arXiv:2608.14036 — procedural compatibility and Skill failure modes;
- arXiv:2608.10039 — execution-feedback workflow graph generation;
- arXiv:2608.09248 — experimental model-internal routing signals;
- arXiv:2605.18747 — code as agent harness;
- existing AMOS Skill Builder Drive lineage.

### Research firewall

- benchmark gains remain source-bound;
- historical trajectory success does not create workflow authority;
- model-internal affect/confidence does not establish truth or user intent;
- code execution evidence does not establish semantic correctness;
- biological/control analogies remain MODEL unless independently validated.

## Validation performed

Fresh Drive writes succeeded for:
- same-ID `amos-skill-builder/SKILL.md`;
- new `amos-workflow-builder/SKILL.md` in existing namespace;
- same-ID `amos-skill-builder-workflow.md`;
- same-ID `amos-workflow-builder-workflow.md`;
- same-ID `amos-sensory-map-integrator/SKILL.md`;
- same-ID `07_SKILLS_MOC.md`;
- same-ID `26_WORKFLOWS_MOC.md`;
- new Research capsule.

No installation claim is made.

## Remaining gaps

1. A 1,086-object Drive census contains mirrors/historical copies and cannot be equated to active capability inventory.
2. A full payload-by-payload semantic review of every duplicate/mirror was not performed; this would waste effort and can corrupt provenance.
3. Additional true placeholders should be resolved by exact identity + active registry state + source availability, not search-hit text alone.
4. Workflow normalization currently covers 294 entries in its recorded registry; absent/non-normalized workflow objects require identity resolution before mutation.
5. Builder Skills were not packaged/installed by this vault-repair pass.
6. Execution-feedback research has not been benchmarked on AMOS workflows in the current target runtime.

## Next governed repair queue

Priority:
1. exact-identity scan of active registered Skills for placeholder/TODO payloads;
2. cross-layer registry ↔ Skill ↔ Workflow ↔ Agent conformance audit;
3. workflow graph linter for node/edge/effect semantics;
4. deterministic validator coverage for consequential Skills;
5. matched tests of Skill applicability/effectiveness;
6. trajectory-based workflow refinement experiments with held-out tasks;
7. stale/mirror retirement proposals after provenance reconciliation.

## Conclusion

**CONDITIONAL / COMPLETE FOR THE RECORDED PHASE46 ACTIVE BUILDER, MOC, SYNTAX, AND RESEARCH-INTEGRATION SCOPE.**

This pass materially improves the recursive repair machinery of `_AMOS_OS`: the system now has source-backed Skill and Workflow builders capable of auditing subsequent payloads under the same MECE, provenance, applicability, effect, and validation rules.

It does **not** claim that every historical/mirrored `SKILL.md` object is current, unique, installed, executable, or validated.

---
RSCF-NODE
node_id: amos_os_audit_2026_09_04_phase46_skill_workflow_payload_orchestration_repair
node_type: audit_and_repair_receipt
claim_class: VALIDATION_RECEIPT
