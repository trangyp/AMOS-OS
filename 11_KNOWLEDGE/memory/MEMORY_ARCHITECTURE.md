---
title: MEMORY ARCHITECTURE
tags:
- memory
- state
- persistence
- canon/knowledge
type: document
source: 11_KNOWLEDGE/memory
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: memory_system
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
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[memory_MOC]]
