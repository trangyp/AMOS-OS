---
title: RUNTIME LINEAGE
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general

---


# AMOS_CORE Runtime Lineage

These files adapt the *reasoning pattern* of each runtime version into Markdown. They do not claim the host LLM literally provides the underlying concurrency/distributed guarantees.

| Version | Title | Focus | Known gap at version |
| --- | --- | --- | --- |
| v3.0 | Deterministic Reasoning Kernel | Core-19 logic; rewrite system; knowledge base; entailment; contradiction detection; TSS-style state; task/engine API | Original contradiction rewrite cycle and insufficient propositional entailment semantics. |
| v3.1 | Logic Fixed | canonical contradiction handling; deterministic SAT-backed classical fragment; meta-logic fallback | Higher structural runtime layers not yet executable. |
| v3.2.1 | RSCF HML Recursive Runtime | recursive RSCF state; H/M/L alignment; scale translation; entropy; future debt; repair; collapse/regeneration; lineage | Meta-evolution/governance depth not yet first-class. |
| v3.3 | Governed Meta-Evolution Runtime | recursive depth; consequence radius; irreversibility; external governance hash; self-modification gates | Distributed stale-state, target-binding, and concurrent merge semantics. |
| v3.4.1 | Distributed Causal Evolution Runtime | runtime-parent lineage binding; exact transition binding; causal clocks; deterministic distributed reconciliation; duplicate/equivocation handling | Authorization validity not bound to changing environment/evidence regime. |
| v3.5 | Epistemic Regime Lineage Runtime | environment hash; regime epoch; evidence hash/epoch; validity windows; falsifiers; revalidation states | Equal high-quality incompatible hypotheses prematurely collapsed by deterministic ranking. |
| v3.6 | Competing Hypothesis Field Runtime | separation of truth state and governance action state; partial-order hypothesis dominance; COMPETING/GAP preservation | Evidence independence supplied as scalar rather than verified from provenance topology. |
| v3.7 | Provenance Topology Runtime | evidence lineage topology; derived independence; source/root/method/dataset relations; provenance-aware hypothesis resolution | Sybil fake-origin aliases sharing identical root payload could regain artificial independence. |
| v3.7.1 | Provenance Topology Hardened Runtime | root-content fingerprints; Sybil alias collapse; cycle/missing-parent/equivocation rejection | Recursive Python traversal failed around depth ~3000. |
| v3.8 | Iterative Provenance Runtime | iterative stack/topological traversal; memoized ancestry; deep provenance without Python recursion | Million-node local changes still triggered whole-graph reconstruction. |
| v3.9 | Persistent Incremental Provenance Runtime | persistent live graph; localized cycle checks; dependency-aware invalidation; versioned hashes; copy-on-write updates | Concurrent overlapping writes remained execution-order dependent; no MVCC/CAS snapshot semantics. |
| v4.0 | MVCC Causal Concurrency Runtime | immutable snapshots; exact CAS; deterministic same-target conflict reconciliation; versioned rollback | Multi-RSCF transactions reconciled per target, allowing partial mixed transaction state. |
| v4.1 | Transactional Multi-RSCF Runtime | transaction IDs; read/write sets; transaction-level CAS; atomic publication; cross-RSCF invariants; all-or-nothing rollback | Distributed transaction finality under partition and competing certified transactions. |
| v4.2 | Deterministic Causal Epoch Runtime | quorum certification; causal epochs; closed membership; deterministic conflict ordering; compact epoch encoding | Caller-supplied shard subset could omit touched shard; transaction-ID equivocation across disjoint payloads. |
| v4.3 | Hardened Adaptive Epoch Runtime | derived required shard set; transaction-ID immutable payload binding; shard-local copy-on-write finalization; epoch-bundle compression | Independent transactions still paid epoch coordination overhead. |
| v4.4 | Coordination Avoidance Runtime | proof-of-independence fast lane; local finalization for disjoint causal cones; automatic escalation for overlap/uncertainty/high consequence; handoff to coordinated epoch path | No later hard-test result is available in the current conversation after promotion; future limits remain untested here. |

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
