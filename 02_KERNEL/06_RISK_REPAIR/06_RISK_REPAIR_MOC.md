---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 06 Risk Repair Moc
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

# 06 Risk Repair — Map of Content

**Path:** `02_KERNEL/06_RISK_REPAIR`
**Files:** 11 | **Subdirectories:** 1

## Files

- [[02_KERNEL/06_RISK_REPAIR/KERNEL_RISK_REPAIR_CONTRACT|KERNEL_RISK_REPAIR_CONTRACT]]
- [[02_KERNEL/06_RISK_REPAIR/K_ABSOLUTE_BIOLOGICAL_INTEGRITY|K_ABSOLUTE_BIOLOGICAL_INTEGRITY]]
- [[02_KERNEL/06_RISK_REPAIR/K_COLLAPSE_RECOVERY|K_COLLAPSE_RECOVERY]]
- [[02_KERNEL/06_RISK_REPAIR/K_HOMEOSTASIS|K_HOMEOSTASIS]]
- [[02_KERNEL/06_RISK_REPAIR/K_NEUROSYNCAI_RECOVERY|K_NEUROSYNCAI_RECOVERY]]
- [[02_KERNEL/06_RISK_REPAIR/K_REPAIR_HARM|K_REPAIR_HARM]]
- [[02_KERNEL/06_RISK_REPAIR/K_REPAIR_PRIORITY|K_REPAIR_PRIORITY]]
- [[02_KERNEL/06_RISK_REPAIR/K_RISK_CONSTRAINT|K_RISK_CONSTRAINT]]
- [[02_KERNEL/06_RISK_REPAIR/K_UBI_ENTROPY_CORRECTION|K_UBI_ENTROPY_CORRECTION]]
- [[02_KERNEL/06_RISK_REPAIR/K_UBI_HOMEOSTASIS|K_UBI_HOMEOSTASIS]]
- [[02_KERNEL/06_RISK_REPAIR/RISK_REPAIR_KERNEL_README|RISK_REPAIR_KERNEL_README]]

## Subdirectories

- [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] — 00_INDEX

## Purpose

The Risk Repair Kernel segment governs risk constraint and repair reasoning primitives within the Kernel plane — homeostasis, collapse recovery, repair priority, repair harm prevention, and biological integrity. Normative load-bearing content lives in the sibling contract; this MOC orients navigation across all risk-repair artifacts.

## Key Artifacts

- [[02_KERNEL/06_RISK_REPAIR/RISK_REPAIR_KERNEL_README|RISK_REPAIR_KERNEL_README]] — package readme and navigation orientation
- [[02_KERNEL/06_RISK_REPAIR/KERNEL_RISK_REPAIR_CONTRACT|KERNEL_RISK_REPAIR_CONTRACT]] — normative contract with invariants and falsifiers
- [[02_KERNEL/06_RISK_REPAIR/K_ABSOLUTE_BIOLOGICAL_INTEGRITY|K_ABSOLUTE_BIOLOGICAL_INTEGRITY]] — absolute biological integrity boundary
- [[02_KERNEL/06_RISK_REPAIR/K_COLLAPSE_RECOVERY|K_COLLAPSE_RECOVERY]] — collapse recovery protocol
- [[02_KERNEL/06_RISK_REPAIR/K_HOMEOSTASIS|K_HOMEOSTASIS]] — homeostasis maintenance primitive
- [[02_KERNEL/06_RISK_REPAIR/K_NEUROSYNCAI_RECOVERY|K_NEUROSYNCAI_RECOVERY]] — NeuroSyncAI recovery binding
- [[02_KERNEL/06_RISK_REPAIR/K_REPAIR_HARM|K_REPAIR_HARM]] — repair harm prevention
- [[02_KERNEL/06_RISK_REPAIR/K_REPAIR_PRIORITY|K_REPAIR_PRIORITY]] — repair priority ordering
- [[02_KERNEL/06_RISK_REPAIR/K_RISK_CONSTRAINT|K_RISK_CONSTRAINT]] — risk constraint enforcement
- [[02_KERNEL/06_RISK_REPAIR/K_UBI_ENTROPY_CORRECTION|K_UBI_ENTROPY_CORRECTION]] — UBI entropy correction
- [[02_KERNEL/06_RISK_REPAIR/K_UBI_HOMEOSTASIS|K_UBI_HOMEOSTASIS]] — UBI homeostasis binding

## Invariants

- Fail closed on UNKNOWN/GAP; gaps stay visible, never promoted to PASS.
- Confidence of any conclusion ≤ confidence of its weakest load-bearing premise (ceiling 0.95).
- Consequential effects emit receipts; rollback basin exists before mutation.
- Competing hypotheses remain visible when evidence does not discriminate.

## Cross-References

- **Parent MOC:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Kernel README:** [[02_KERNEL/KERNEL_README|KERNEL_README]]
- **Canon laws:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Control plane:** [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- **Observability:** [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]]

______________________________________________________________________

**Parent:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
