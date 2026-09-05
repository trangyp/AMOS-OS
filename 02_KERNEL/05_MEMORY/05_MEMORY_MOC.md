---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 05 Memory Moc
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

# 05 Memory — Map of Content

**Path:** `02_KERNEL/05_MEMORY`
**Files:** 7 | **Subdirectories:** 1

## Files

- [[02_KERNEL/05_MEMORY/KERNEL_MEMORY_CONTRACT|KERNEL_MEMORY_CONTRACT]]
- [[02_KERNEL/05_MEMORY/K_CONTEXT_COMPACTION|K_CONTEXT_COMPACTION]]
- [[02_KERNEL/05_MEMORY/K_MEMORY_ADMISSION|K_MEMORY_ADMISSION]]
- [[02_KERNEL/05_MEMORY/K_MEMORY_CONFLICT|K_MEMORY_CONFLICT]]
- [[02_KERNEL/05_MEMORY/K_MEMORY_IMMUNE|K_MEMORY_IMMUNE]]
- [[02_KERNEL/05_MEMORY/K_MEMORY_RETRIEVAL|K_MEMORY_RETRIEVAL]]
- [[02_KERNEL/05_MEMORY/MEMORY_KERNEL_README|MEMORY_KERNEL_README]]

## Subdirectories

- [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] — 00_INDEX

## Purpose

The Memory Kernel segment governs memory-plane reasoning primitives within the Kernel plane — memory admission, retrieval, conflict resolution, context compaction, and immune memory. Normative load-bearing content lives in the sibling contract; this MOC orients navigation across all memory artifacts.

## Key Artifacts

- [[02_KERNEL/05_MEMORY/MEMORY_KERNEL_README|MEMORY_KERNEL_README]] — package readme and navigation orientation
- [[02_KERNEL/05_MEMORY/KERNEL_MEMORY_CONTRACT|KERNEL_MEMORY_CONTRACT]] — normative contract with invariants and falsifiers
- [[02_KERNEL/05_MEMORY/K_CONTEXT_COMPACTION|K_CONTEXT_COMPACTION]] — context compaction strategy
- [[02_KERNEL/05_MEMORY/K_MEMORY_ADMISSION|K_MEMORY_ADMISSION]] — memory admission control
- [[02_KERNEL/05_MEMORY/K_MEMORY_CONFLICT|K_MEMORY_CONFLICT]] — memory conflict resolution
- [[02_KERNEL/05_MEMORY/K_MEMORY_IMMUNE|K_MEMORY_IMMUNE]] — immune memory protection
- [[02_KERNEL/05_MEMORY/K_MEMORY_RETRIEVAL|K_MEMORY_RETRIEVAL]] — memory retrieval primitive

## Invariants

- Fail closed on UNKNOWN/GAP; gaps stay visible, never promoted to PASS.
- Confidence of any conclusion ≤ confidence of its weakest load-bearing premise (ceiling 0.95).
- Selective invalidation — failure invalidates dependent descendants only; unrelated state is preserved.
- Consequential effects emit receipts; rollback basin exists before mutation.

## Cross-References

- **Parent MOC:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Kernel README:** [[02_KERNEL/KERNEL_README|KERNEL_README]]
- **Canon laws:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Control plane:** [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- **Observability:** [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]]

______________________________________________________________________

**Parent:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
