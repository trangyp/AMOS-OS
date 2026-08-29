---
title: qfm architecture refinement
type: reference
source: 07_SKILLS/amos-formal-engines-master/references
tags:
- reference
- amos-formal-engines-master
- type/skill
- system-scan-agent
- automation-profiles
- amos-simulation-kernel-v0-math-foundations
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# QFM Architecture Refinement Pass

> Source: `_00_Cosmo brain/dated/2026-08-25/2026-08-25 QFM Architecture Refinement Pass.md`
> Epistemic class: SOURCE_DERIVED

---
title: 2026-08-25 QFM Architecture Refinement Pass
type: daily-learning
date: 2026-08-25
epistemic: DERIVED
tags: [architecture, refinement, qfm, routing, dated, dated/2026-08-25]
---

# 2026-08-25 — QFM Refinement Pass (using what was created)

## Method shift

Previous passes added components. This pass **refined the created components against each other**: audited all 8 session-created agents for dependency completeness, re-wired the master router with everything built since its creation, and upgraded the orchestration gate block.

## Findings & fixes

1. **Router drift**: `amos-qfm-master-router` (created mid-session) predated 5 later artifacts — RG-fractal bridge, QCI governance, law-stack enforcement, tensor composition gate. Its layer table and gate composition were stale.
   - Fixed: layer table updated (L2 + RG bridge deepening; L4 + QCI coherence; new Cross-cutting tensor row); routing question 6 added (joins); gates extended to 8+2+1 (G11 = tensor composition).
2. **G3 was a name without a procedure** in the orchestration workflow — now explicitly bound to `amos-law-stack-enforcement` + gate agent with ordered LoL→R2→R4.
3. **Dependency audit**: 8/8 session agents parse valid JSON; one (bridge-auditor) uses a different dependency schema shape than siblings (`dependencies.{skills,workflows,agents}` vs flat keys) — functional but noted for future normalization.

## Final architecture (all verified on disk)

```
Entry: amos-qfm-master-router (v1.1)
  L1 Knowledge      quantum library discipline
  L2 Bridges        B1–B5 (+ RG-scaling audit for B1)
  L3 Dynamics       A-matrix coupling
  L4 Collapse       QLS/UCP verdicts + QCI coherence classes
  L5 Enforcement    ERA + adversarial fuzz
  Cross-cutting     tensor composition G11
Gates: G1–G8 base · G9 bridge · G10 adversarial · G11 composition
Agents owned per layer: 8 dedicated + orchestration + router
```

## Meta-lesson recorded

**Refinement passes are not optional after building passes.** Components created at different times drift from each other; the router itself became stale within one session. Schedule: build pass → refine pass → build pass → refine pass, never N builds in a row.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

---
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-formal-engines-master-qfm-architecture-refinement
node_type: reference
path: 07_SKILLS/amos-formal-engines-master/references/qfm_architecture_refinement.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
