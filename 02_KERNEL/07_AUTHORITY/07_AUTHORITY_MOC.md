---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 07 Authority Moc
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

# 07 Authority — Map of Content

**Path:** `02_KERNEL/07_AUTHORITY`
**Files:** 6 | **Subdirectories:** 1

## Files

- [[02_KERNEL/07_AUTHORITY/AUTHORITY_KERNEL_README|AUTHORITY_KERNEL_README]]
- [[02_KERNEL/07_AUTHORITY/KERNEL_AUTHORITY_CONTRACT|KERNEL_AUTHORITY_CONTRACT]]
- [[02_KERNEL/07_AUTHORITY/K_CAPABILITY_AUTHORIZATION|K_CAPABILITY_AUTHORIZATION]]
- [[02_KERNEL/07_AUTHORITY/K_COMMIT_TIME_AUTHORITY|K_COMMIT_TIME_AUTHORITY]]
- [[02_KERNEL/07_AUTHORITY/K_EFFECT_CLASSIFICATION|K_EFFECT_CLASSIFICATION]]
- [[02_KERNEL/07_AUTHORITY/K_INFORMATION_EXPOSURE|K_INFORMATION_EXPOSURE]]

## Subdirectories

- [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] — 00_INDEX

## Purpose

The Authority Kernel segment governs authority reasoning primitives within the Kernel plane — capability authorization, commit-time authority, effect classification, and information exposure control. Normative load-bearing content lives in the sibling contract; this MOC orients navigation across all authority artifacts.

## Key Artifacts

- [[02_KERNEL/07_AUTHORITY/AUTHORITY_KERNEL_README|AUTHORITY_KERNEL_README]] — package readme and navigation orientation
- [[02_KERNEL/07_AUTHORITY/KERNEL_AUTHORITY_CONTRACT|KERNEL_AUTHORITY_CONTRACT]] — normative contract with invariants and falsifiers
- [[02_KERNEL/07_AUTHORITY/K_CAPABILITY_AUTHORIZATION|K_CAPABILITY_AUTHORIZATION]] — capability authorization primitive
- [[02_KERNEL/07_AUTHORITY/K_COMMIT_TIME_AUTHORITY|K_COMMIT_TIME_AUTHORITY]] — commit-time authority enforcement
- [[02_KERNEL/07_AUTHORITY/K_EFFECT_CLASSIFICATION|K_EFFECT_CLASSIFICATION]] — effect classification taxonomy
- [[02_KERNEL/07_AUTHORITY/K_INFORMATION_EXPOSURE|K_INFORMATION_EXPOSURE]] — information exposure control

## Invariants

- Fail closed on UNKNOWN/GAP; gaps stay visible, never promoted to PASS.
- CAPABILITY ≠ AUTHORITY — capability alone never authorizes; authority_ref must be epoch-valid.
- Confidence of any conclusion ≤ confidence of its weakest load-bearing premise (ceiling 0.95).
- Consequential effects emit receipts; rollback basin exists before mutation.

## Cross-References

- **Parent MOC:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Kernel README:** [[02_KERNEL/KERNEL_README|KERNEL_README]]
- **Canon laws:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Control plane:** [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- **Observability:** [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]]

______________________________________________________________________

**Parent:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
