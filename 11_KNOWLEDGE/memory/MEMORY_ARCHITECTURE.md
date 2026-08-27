---
tags: [memory]
---
# Memory Architecture

## Principle
Memory is coherence carried through transformation.

## Memory state
`M = [origin, state_history, relation_history, mutation_lineage, repair_history, evidence_history, supersession, contradiction_history, provenance]`

## Retention classes
- HOT: decision-active
- WARM: validated reusable capsule
- COLD: recoverable detail
- QUARANTINED: conflict/contamination/staleness
- EXPIRED: invalid in current regime
- RAW_ARCHIVE: exact source, do-not-load by default

## Invariants
Preserve:
objective, hard constraints, load-bearing premises, unresolved contradictions, provenance anchors, falsifiers, rollback points.

Compression may remove repetition but not provenance, contradiction, scope, validity state, or repair history.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
