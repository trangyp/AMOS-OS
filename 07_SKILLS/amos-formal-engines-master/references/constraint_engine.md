---
title: constraint engine
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

# Constraint Engine

> Source: `_00_Cosmo brain/engine/C/CONSTRAINT_ENGINE.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [engine]
---
# Constraint Propagation Engine

## Constraint types
`hard | soft | temporal | epistemic | resource | causal | governance | authority | safety`

## Constraint tensor
`C = T[id, type, target, predicate, scope, regime, priority, authority, valid_from, valid_until, provenance]`

## Admissibility
`Admissible(x) = ∧ hard_constraints(x) ∧ GovernedSoftTradeoff(x)`

A hard-constraint failure cannot be compensated by a higher optimization score elsewhere.

Propagate a changed constraint only through dependent edges.

---
**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

---
**MOC:** references_MOC
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-formal-engines-master-constraint-engine
node_type: reference
path: 07_SKILLS/amos-formal-engines-master/references/constraint_engine.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
