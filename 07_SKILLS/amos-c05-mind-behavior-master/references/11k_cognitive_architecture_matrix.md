---
title: 11k cognitive architecture matrix
type: reference
source: 07_SKILLS/amos-c05-mind-behavior-master/references
tags:
- reference
- amos-c05-mind-behavior-master
- canon/skill
- references-moc
- 07-skills-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# 11K Cognitive Architecture Matrix

> Source: `/Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/Cosmo_Brain/AMOS_COGNITIVE_ARCHITECTURE_MATRIX.md`
> Epistemic class: SOURCE_DERIVED

# AMOS Cognitive Architecture Matrix

> **Status:** v1.0 — formal 4-axis matrix exposing every cognitive-primitive × lifecycle-operation × control-plane × scale interaction in AMOS, with rule-based coverage status.
> **Companion artifact:** `AMOS_Cognitive_Architecture_Matrix.json` (machine-readable, 13,770 cells).
> **Generator:** `build_amos_cognitive_matrix.py` (auditable, reproducible).

## 1. Purpose

The prior gap analysis (gaps 901–1500) enumerated **capabilities** as a flat list. That abstraction is wrong: it exposes missing *modules* but hides missing **interactions**. A complete AMOS cognitive architecture is not `LLM → Skills → Agents`, nor even `Kernel → Engine → Agent → Memory`. It is a 30-layer cognitive stack (L0–L29) wrapped by 9 cross-cutting control planes, where every primitive must pass through every lifecycle operation at every scale under every plane.

The matrix's job is therefore not to count features. It is to make the **interaction space** addressable so that the gaps that live *between* modules become visible. The headline finding confirms the gap document's conclusion:

> **The completion denominator is not yet closed.** Of 13,770 addressable interaction cells, only **1.98%** are existing, **22.96%** partial, **7.04%** explicitly missing, and **68.02%** are *structural gaps* — interactions AMOS has not yet recognized or named.

A flat "1501–2000" list would have continued to miss the 9,367 structural-gap cells. The matrix is the correct abstraction to expose them.

The architectural invariant this matrix enforces:

```
LLM ⊂ CognitiveExecution
AMOS = Kernel + CognitiveRuntime + MemorySystem + WorldModel
      + ReasoningSystem + SimulationSystem + DecisionSystem
      + LearningSystem + AgentSystem + GovernanceSystem
AMOS ≠ LLM
```

## 2. The Four Axes

### Axis P — Cognitive Primitives (30, L0–L29)

The vertical cognitive stack. Each primitive carries a **maturity** score versus current AMOS, derived from the gap document's explicit claims (not guessed).

| ID | Primitive | Subsystem / Gap ref | Maturity | Basis |
|----|-----------|---------------------|----------|-------|
| L0 | Reality / Environment | Environment substrate | missing | Not a typed subsystem |
| L1 | Sensing / Observation | 931–960 | missing | Perception needs epistemic machinery |
| L2 | Attention | 901–930 | missing | Attention missing as real subsystem |
| L3 | Percept Formation | 931–960 | missing | Observation ≠ Interpretation firewall absent |
| L4 | Object / Entity Formation | 961–990 | missing | Persistent entity identity absent |
| L5 | Binding | 991–1020 | missing | Explicit relational cognition absent |
| L6 | Working State | 1021–1050 | missing | No cognitive workspace beyond context window |
| L7 | Memory | 1051–1140 | partial | HOT/WARM lifecycle exists; activation/interference/forgetting missing |
| L8 | Representation | 1141–1170 | partial | Partial representation; world-model engine largely missing |
| L9 | Inference | Reasoning kernel | partial | CORE-19 reasoning kernel exists |
| L10 | World Modeling | 1141–1170 | missing | Enormous gap; LLM must not be the world model |
| L11 | Causal Modeling | Causal mediation | partial | Counterfactual/causal kernels exist |
| L12 | Counterfactual Simulation | 1201–1230 | partial | Counterfactual kernel exists; simulation worlds missing |
| L13 | Prediction | 1171–1200 | missing | Prediction governance missing |
| L14 | Valuation | 1231–1260 | missing | No explicit value-function architecture |
| L15 | Goal Formation | Kernel goals | partial | Goals exist in kernel typed state |
| L16 | Planning | Planning | partial | Planning exists; limited machinery |
| L17 | Decision | 1261–1290 | partial | Decision filter exists; much missing |
| L18 | Action | Execution plane | existing | Agents/Skills/Tools execution exists |
| L19 | Outcome Observation | 931–960 | missing | Observation-to-outcome loop absent |
| L20 | Credit Assignment | 1291–1320 | missing | No explicit credit/blame

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c05-mind-behavior-master-11k-cognitive-architecture-matrix
node_type: reference
path: 07_SKILLS/amos-c05-mind-behavior-master/references/11k_cognitive_architecture_matrix.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
