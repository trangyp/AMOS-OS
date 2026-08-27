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
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
