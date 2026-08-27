---
tags: [brain]
---
# AMOS Provenance and Trust

## Trust is local
Trust is typed, scoped, provenance-aware, regime-aware, and freshness-bounded.

## Evidence identity
Track when material:
- source identity
- source type
- parent/ancestor source
- timestamp/version
- environment/regime
- transformation history
- independence status

## Sybil hardening
Multiple documents, posts, agents, or summaries descending from the same origin count as correlated support, not independent confirmation.

Authority, popularity, repetition, or paraphrase do not prove independence.

## Independence test
Before aggregating support ask:
1. Do sources share a parent?
2. Do they share a dataset, benchmark, fixture, model output, or press release?
3. Is one merely summarizing another?
4. Were they independently measured?
5. Do they fail independently?

If unknown, mark provenance independence as uncertain.

## Freshness
A stale source can remain historically accurate but lose applicability in a changed regime.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
