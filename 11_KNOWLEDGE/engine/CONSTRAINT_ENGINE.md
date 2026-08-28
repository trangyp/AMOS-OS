---
title: CONSTRAINT ENGINE
tags: [engine, processing, runtime, canon/knowledge]
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
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[ENGINE_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
