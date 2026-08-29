---
title: conjecture discipline
type: reference
source: 07_SKILLS/amos-rscf-epistemic-master/references
tags:
- reference
- amos-rscf-epistemic-master
- canon/skill
- 00-home
- knowledge-moc
- references-moc
- amos-rscf-nodes
- law-hierarchy
- 07-skills-moc
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: skill_reference
---

# Conjecture Discipline Layer

> Source: `_00_Cosmo brain/dated/2026-08-25/2026-08-25 Conjecture Discipline Layer.md`
> Epistemic class: SOURCE_DERIVED

---
title: 2026-08-25 Conjecture Discipline Layer
type: daily-learning
date: 2026-08-25
epistemic: SOURCE/DERIVED
tags: [math, conjectures, epistemic-discipline, dated, dated/2026-08-25]
---

# 2026-08-25 — Conjecture Discipline Layer

## Gap found

The corpus leans on unproven conjectures in at least three places: BSD in the arithmetic-geometry mapping (which has good BSD-specific decision gates), Yang–Mills existence/mass gap in the QFT mapping (MODEL boundary), and Riemann Hypothesis implicitly wherever L-functions appear. But the BSD gate pattern was **never generalized** — no contract classifies *how* a conjecture is being used, and fact-slippage ("the rank is given by the L-function", stated unconditionally) had no detector.

## Closure (4 channels)

| Channel | Artifact |
|---|---|
| Skill | `amos/amos-conjecture-discipline` — U1/U2/U3/U4 usage classes, gate procedure, corpus conjecture inventory with status |
| Agent | `.devin/agents/amos-conjecture-gate-agent.json` — 5 capabilities incl. conditional-trace checking and exponent-gate cooperation |
| Workflow | `conjecture-discipline-pipeline-workflow.md` — 5-step pipeline wired into G3 + scaling auditor |
| Memory + vault note | recorded |

## The four usage classes

U1 Conditional derivation (`CONDITIONAL-ON: C` carried through all dependents + failure note) · U2 Evidence citation (proven fragments only — Coates–Wiles, Wiles/Taylor–Wiles modularity) · U3 Heuristic analogy (MODEL + bridge routing) · **U4 Fact-slippage = hard block**, logged as Signal Fidelity violation into law-stack G3.

## Key design decisions

1. **CONDITIONAL-ON becomes a first-class epistemic class** alongside SOURCE/DERIVED/MODEL — the labeler can now express "true if BSD" natively.
2. **Conjecture-based exponents blocked from universality matching even conditionally** — assuming BSD doesn't make an exponent established.
3. **Poincaré corrected**: it's a theorem (Perelman); the inventory explicitly prevents it appearing on conjecture lists.
4. **Proven fragments enumerated** so U2 citations are precise: partial results are real evidence; the full conjecture is not.

## Meta-pattern completion
This pass completes the epistemic-gate family: bridges (analogy discipline), collapse verdicts (claim discipline), coherence (class discipline), scaling laws (fit discipline), and now conjectures (conditional discipline). Each domain's characteristic failure mode now has a named gate.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · AMOS Simulation Kernel v0 Math Foundations · system scan agent · automation profiles

---
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-rscf-epistemic-master-conjecture-discipline
node_type: reference
path: 07_SKILLS/amos-rscf-epistemic-master/references/conjecture_discipline.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
