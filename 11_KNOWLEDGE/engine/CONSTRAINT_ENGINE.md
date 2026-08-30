---
title: CONSTRAINT ENGINE
tags:
- engine
- processing
- runtime
- canon/knowledge
- system-scan-agent
- automation-profiles
- amos-simulation-kernel-v0-math-foundations
- trang-framework-recursive-ontology-dynamics
type: document
source: 11_KNOWLEDGE/engine
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: engine_specification
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
**MOC:** [[11_KNOWLEDGE/engine/ENGINE_MOC|ENGINE_MOC]]

---
**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
