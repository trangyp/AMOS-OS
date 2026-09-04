---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Os Audit 2026 09 04 Phase46 Skills Workflows Mece Arxiv Builder Repair
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

# AMOS OS Audit — Phase46 Skills / Workflows MECE, Builder and arXiv Expansion

## 1. Objective

Use `_AMOS_OS` as the authoritative extended brain, prioritize `07_SKILLS` and `26_WORKFLOWS`, inspect registry-scale state and governing artifacts, mine richer Drive source material, use recent arXiv research as external evidence, and repair architecture/generators without fabricating payloads or padding every adapter.

## 2. Scan boundary

### Registry-level exhaustive inventory
The pass inspected the current authoritative registry snapshots rather than sampling filenames only.

**Skills reconciliation snapshot**
- Drive registry names: 343
- Drive catalog names: 343
- external `.devin/skills` lock names: 696
- overlap: 339
- Drive-registry-only: 4
- external-lock-only: 357
- Drive corpus census note: 1086 observed `SKILL.md` objects
- reconciliation status: `RECONCILED_NAMESPACES_WITH_MATERIALIZATION_GAP`

These are different logical denominators and are not collapsed into one active-skill count.

**Workflow normalization registry**
- direct normalized adapters: 294
- unique direct workflow names: 294
- retrieval classification observed in this pass:
  - 203 AMOS non-FX/non-arXiv adapters
  - 38 arXiv/research-derived adapters
  - 23 McKinsey-family adapters
  - 18 FX/forex-family adapters
  - 12 other adapters

This classification is an audit convenience, not canonical taxonomy.

### Targeted deep reads
Deep inspection covered:
- Skills MOC / contract / README / map;
- skill registry gateway/catalog/reconciliation evidence;
- AMOS Skill Builder v37 source document;
- Workflows MOC / contract / README / map;
- workflow metadata normalization registry;
- representative generic wrapper (`amos-session-control-plane-workflow`);
- `amos-skill-builder-workflow`;
- `amos-workflow-builder-workflow`;
- Full Brain architecture map;
- Research MOC.

This is **not** a byte-by-byte semantic proof over every skill payload and all 294 workflow bodies.

## 3. Findings and repairs

### F46-01 — Skills plane was registry-centric, not ecosystem-complete
The prior MOC described capability concerns but lacked library-level health, technical debt, transfer/generalization, materialization, supply-chain and maintenance semantics.

**Repair**
`07_SKILLS_MOC.md` now uses nine primary functional concerns:
1. Identity & Discovery
2. Capability Semantics
3. Procedure / Knowledge Package
4. Runtime / Host Binding
5. Composition & Dependency
6. Governance / Security / Exposure
7. Evaluation & Transfer
8. Lifecycle & Maintenance
9. Provenance & Supply Chain

It adds maturity states, library-health/debt classes, transfer matrices and Full Brain boundaries.

### F46-02 — Skills map was too basic
`SKILL_MAP.md` was ~600 bytes and only expressed reading order.

**Repair**
Expanded it into a functional topology, Full Brain interface map, lifecycle map and maintenance map while preserving its role as navigation rather than authority.

### F46-03 — Skills contract lacked library-time maintenance and transfer semantics
The prior contract governed identity and invocation well but mostly treated validation locally.

**Repair**
Expanded `SKILLS_SKILL_CONTRACT.md` with:
- progressive package architecture;
- library-time health/debt;
- explicit local vs transfer vs composition validation;
- supply-chain/provenance;
- transfer axes across task/role/model/host/environment/regime/time;
- governed evolution and quarantine;
- current materialization-gap boundary.

### F46-04 — Workflow architecture mixed purpose with implicit execution patterns
The MOC had strong purpose families but did not explicitly separate purpose from control topology.

**Repair**
`26_WORKFLOWS_MOC.md` now has two orthogonal views:
- six purpose families;
- nine orchestration forms: sequential, DAG, hierarchical/HTN-like, state-machine/event-driven, bounded loop, manager-worker, human checkpoint, transactional effect, hybrid.

It adds typed step contracts, branch/join semantics, loop stopping, procedural-memory placement, resource budgets, version evolution and direct-adapter inventory boundaries.

### F46-05 — Workflow contract remained partly generic
The previous contract had strong metadata normalization but insufficient graph/branch/resource/procedural-memory detail.

**Repair**
`WORKFLOWS_WORKFLOW_CONTRACT.md` now governs objective, control topology, typed steps, branch/join, resources, procedural memory, authority/effects, recovery/replay, evaluation and evolution. It explicitly rejects universal fixed confidence thresholds, chain depth and 1:1:1 bindings.

### F46-06 — Workflow map was too basic
`WORKFLOW_MAP.md` was ~600 bytes.

**Repair**
Expanded it into purpose/topology, Full Brain route, step taxonomy, risk checkpoints and inventory boundaries.

### F46-07 — Skill Builder workflow generated legacy defects
Observed defects in the prior builder:
- conflicting versions and epistemic classes;
- duplicate tags/sections;
- stale trigger;
- hard-coded confidence values (`0.95`, `0.5`, `0.3`);
- “no unresolved contradictions” as an overstrong universal gate;
- fixed maximum chain depth;
- generic single-agent assumption;
- weak alignment with current AMOS Skill Builder source runtime.

**Repair**
Rewrote `amos-skill-builder-workflow.md` as:
`ORIENT → GAP → SOURCE → ARCHITECT → BUILD → INTEGRATE → CHALLENGE → VALIDATE → PACKAGE`, with optional deep source/system phases when load-bearing. Numeric confidence constants and unsupported topology limits were removed.

### F46-08 — Workflow Builder imposed false 1:1:1 architecture
The prior builder required `workflow → agent → skill` 1:1:1 and repeated single-agent assumptions.

**Repair**
Rewrote `amos-workflow-builder-workflow.md` to choose topology from task structure, support zero/many Agents/Skills, gate consequential transitions rather than every harmless step, define budgets/state/recovery, and prohibit unsupported numerical constants.

### F46-09 — External research was not integrated as a bounded evidence layer
Recent research had relevant architecture implications but should not be promoted into canon.

**Repair**
Created:
`22_RESEARCH/AMOS_SKILLS_WORKFLOWS_ARXIV_RESEARCH_2026-09-04.md`
and linked it from `22_RESEARCH_MOC.md`.

Research cells:
- SkillOps — arXiv:2605.13716
- AFTER procedural memory — arXiv:2606.23127
- LEGOMem — arXiv:2510.04851
- Procedural Knowledge / HTN — arXiv:2511.07568

All benchmark claims remain `SOURCE_CLAIM`; architecture implications are `DERIVED`.

### F46-10 — Operations closure chain lagged current authority
Fresh read found `AUTHORITATIVE_STATE.md` already reached Phase45 while `20_OPERATIONS_MOC.md` closure-chain content stopped at Phase41 branches.

**Repair**
Phase46 updates the Operations closure chain with Phase42–46 forward pointers rather than treating the stale MOC chain as current authority.

## 4. Research-derived design implications

External research supports, within its tested scope:
- treating skill libraries as maintainable ecosystems rather than static lists;
- measuring transfer instead of inferring it;
- separating orchestrator procedural memory from fine-grained skill procedure;
- supporting hierarchical/HTN-like workflow decomposition.

It does **not** establish:
- universal performance gains for AMOS;
- universal optimality of HTN;
- universal superiority of multi-agent systems;
- fixed confidence thresholds;
- automatic canon admission.

## 5. Remaining gaps

- no byte-level validation of every skill payload;
- no proof all 343/696/1086 snapshot objects are active/materialized;
- no proof all 294 workflow adapters are semantically unique or implemented;
- no executed benchmark comparing old vs repaired builders yet;
- no complete automated skill technical-debt scanner;
- no cross-host transfer benchmark for AMOS skills;
- no production evidence for every effectful workflow;
- arXiv-derived architecture remains research-backed design input until AMOS-specific validation.

## 6. Next highest-value validation

Use a fixed task set to compare old-generation patterns against repaired builders and measure:
- metadata contradictions;
- duplicate skill creation;
- trigger overlap;
- invalid/missing bindings;
- context footprint;
- negative-path coverage;
- authority/effect containment;
- local vs transfer performance;
- workflow topology fit;
- replay/recovery correctness.

## 7. Conclusion

**CONDITIONAL / COMPLETE FOR THE RECORDED PHASE46 REGISTRY-LEVEL SKILLS/WORKFLOWS AUDIT AND GOVERNING-ARTIFACT REPAIR SCOPE.**

The main improvement is architectural leverage: repair was applied to MOCs, contracts, maps and builders that govern future artifacts rather than mechanically inflating hundreds of documentary wrappers.

---
RSCF-NODE
node_id: amos_os_audit_2026_09_04_phase46_skills_workflows_mece_arxiv_builder_repair
node_type: audit_and_repair_receipt
path: 20_OPERATIONS/AMOS_OS_AUDIT_2026-09-04_PHASE46_SKILLS_WORKFLOWS_MECE_ARXIV_BUILDER_REPAIR.md
claim_class: VALIDATION_RECEIPT
