---
tags: [kernel]
---
# Deterministic Logic Kernel

## Core logical objects
ATOM, NOT, AND, OR, IMPLIES, BOTTOM, PARADOX, convergence/divergence forms, positive/negative/zero/dual/multi/meta logic modes.

## Invariants
- normalize deterministically for equivalent supported inputs
- preserve contradiction explicitly
- distinguish syntactic normalization from semantic entailment
- do not infer classical truth from unsupported meta-logic operators
- use tested propositional behavior only within its verified fragment

## Contradiction
A proposition and its negation may be represented as an explicit contradiction state rather than silently repaired.

## Entailment
Entailment claims require premises + inference rule + applicable logic fragment.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
