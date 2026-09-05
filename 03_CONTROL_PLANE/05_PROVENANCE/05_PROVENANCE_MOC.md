---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 05 Provenance Moc
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

# 05 Provenance — Map of Content

**Path:** `03_CONTROL_PLANE/05_PROVENANCE`
**Files:** 5 | **Subdirectories:** 1

## Files

- [[03_CONTROL_PLANE/05_PROVENANCE/CONTROL_PLANE_PROVENANCE_CONTRACT|CONTROL_PLANE_PROVENANCE_CONTRACT]]
- [[03_CONTROL_PLANE/05_PROVENANCE/OBSERVED_READ_SET|OBSERVED_READ_SET]]
- [[03_CONTROL_PLANE/05_PROVENANCE/PROVENANCE_CONTROL_PLANE_README|PROVENANCE_CONTROL_PLANE_README]]
- [[03_CONTROL_PLANE/05_PROVENANCE/PROVENANCE_LEDGER|PROVENANCE_LEDGER]]
- [[03_CONTROL_PLANE/05_PROVENANCE/READ_SET_VALIDATOR|READ_SET_VALIDATOR]]

## Subdirectories

- [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] — 00_INDEX

## Purpose

Governs the provenance tracking surface of the AMOS control plane — recording the read-set dependencies, lineage, and causal history that underpin commit-time validation. Provenance is the evidentiary substrate that makes replay, rollback, and audit possible.

## Key Artifacts

- [[03_CONTROL_PLANE/05_PROVENANCE/PROVENANCE_LEDGER|PROVENANCE_LEDGER]] — Append-only ledger of provenance records with causal ordering
- [[03_CONTROL_PLANE/05_PROVENANCE/OBSERVED_READ_SET|OBSERVED_READ_SET]] — Captured read-set at observation time for validation
- [[03_CONTROL_PLANE/05_PROVENANCE/READ_SET_VALIDATOR|READ_SET_VALIDATOR]] — Validates observed read-sets against current state at commit time
- [[03_CONTROL_PLANE/05_PROVENANCE/CONTROL_PLANE_PROVENANCE_CONTRACT|CONTROL_PLANE_PROVENANCE_CONTRACT]] — Binding contract for provenance record format and semantics

## Invariants

- Provenance records are append-only; no mutation or deletion is permitted
- Read-set must be captured at observation time, not retroactively reconstructed
- Causal ordering must be preserved: effect provenance must precede effect commit
- Provenance gaps invalidate downstream commits until reconciled

## Cross-References

- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/06_SEMANTIC_TRANSACTION_MOC|06_SEMANTIC_TRANSACTION_MOC]] — Semantic transaction plane uses provenance for multi-RSCF atomicity
- [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]] — Commit plane validates provenance before finalization
- [[03_CONTROL_PLANE/11_REPLAY/11_REPLAY_MOC|11_REPLAY_MOC]] — Replay plane depends on provenance for deterministic re-execution

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
