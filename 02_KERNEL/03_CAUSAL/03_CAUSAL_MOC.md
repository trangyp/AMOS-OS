---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 03 Causal Moc
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# 03 Causal — Map of Content

**Path:** `02_KERNEL/03_CAUSAL`
**Files:** 9 | **Subdirectories:** 1

## Files

- [[02_KERNEL/03_CAUSAL/CAUSAL_KERNEL_README|CAUSAL_KERNEL_README]]
- [[02_KERNEL/03_CAUSAL/KERNEL_CAUSAL_CONTRACT|KERNEL_CAUSAL_CONTRACT]]
- [[02_KERNEL/03_CAUSAL/K_BIOLOGICAL_CAUSALITY|K_BIOLOGICAL_CAUSALITY]]
- [[02_KERNEL/03_CAUSAL/K_CAUSAL_CLOSURE|K_CAUSAL_CLOSURE]]
- [[02_KERNEL/03_CAUSAL/K_CAUSAL_EPOCH|K_CAUSAL_EPOCH]]
- [[02_KERNEL/03_CAUSAL/K_CAUSAL_HIERARCHY|K_CAUSAL_HIERARCHY]]
- [[02_KERNEL/03_CAUSAL/K_CROSS_SCALE_CAUSALITY|K_CROSS_SCALE_CAUSALITY]]
- [[02_KERNEL/03_CAUSAL/K_QUANTUM_CAUSALITY|K_QUANTUM_CAUSALITY]]
- [[02_KERNEL/03_CAUSAL/K_REALITY_CAUSALITY|K_REALITY_CAUSALITY]]

## Subdirectories

- [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] — 00_INDEX

## Purpose

The Causal Kernel segment governs causal reasoning primitives within the Kernel plane — causal closure, causal epochs, causal hierarchy, and cross-scale causality. Normative load-bearing content lives in the sibling contract; this MOC orients navigation across all causal artifacts.

## Key Artifacts

- [[02_KERNEL/03_CAUSAL/CAUSAL_KERNEL_README|CAUSAL_KERNEL_README]] — package readme and navigation orientation
- [[02_KERNEL/03_CAUSAL/KERNEL_CAUSAL_CONTRACT|KERNEL_CAUSAL_CONTRACT]] — normative contract with invariants and falsifiers
- [[02_KERNEL/03_CAUSAL/K_BIOLOGICAL_CAUSALITY|K_BIOLOGICAL_CAUSALITY]] — biological causality reasoning primitive
- [[02_KERNEL/03_CAUSAL/K_CAUSAL_CLOSURE|K_CAUSAL_CLOSURE]] — causal closure boundary definition
- [[02_KERNEL/03_CAUSAL/K_CAUSAL_EPOCH|K_CAUSAL_EPOCH]] — causal epoch ordering and finality
- [[02_KERNEL/03_CAUSAL/K_CAUSAL_HIERARCHY|K_CAUSAL_HIERARCHY]] — hierarchical causal structure
- [[02_KERNEL/03_CAUSAL/K_CROSS_SCALE_CAUSALITY|K_CROSS_SCALE_CAUSALITY]] — cross-scale causal propagation
- [[02_KERNEL/03_CAUSAL/K_QUANTUM_CAUSALITY|K_QUANTUM_CAUSALITY]] — quantum-level causality primitive
- [[02_KERNEL/03_CAUSAL/K_REALITY_CAUSALITY|K_REALITY_CAUSALITY]] — reality-grounded causality binding

## Invariants

- Fail closed on UNKNOWN/GAP; gaps stay visible, never promoted to PASS.
- Confidence of any conclusion ≤ confidence of its weakest load-bearing premise (ceiling 0.95).
- Epochs remain distinct: state_version ≠ causal_epoch ≠ policy_epoch ≠ provenance_epoch unless an explicit mapping licenses equivalence.
- Local finality requires proof — demonstrated dependency closure may avoid coordination; assumed independence may not.

## Cross-References

- **Parent MOC:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Kernel README:** [[02_KERNEL/KERNEL_README|KERNEL_README]]
- **Canon laws:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Control plane:** [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- **Observability:** [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]]

______________________________________________________________________

**Parent:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
