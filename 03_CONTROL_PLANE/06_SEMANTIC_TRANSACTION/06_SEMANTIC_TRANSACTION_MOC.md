---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 06 Semantic Transaction Moc
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

# 06 Semantic Transaction — Map of Content

**Path:** `03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION`
**Files:** 8 | **Subdirectories:** 1

## Files

- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/CANON_SEMANTIC_TRANSACTION|CANON_SEMANTIC_TRANSACTION]]
- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/CONTROL_PLANE_SEMANTIC_TRANSACTION_CONTRACT|CONTROL_PLANE_SEMANTIC_TRANSACTION_CONTRACT]]
- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/CROSS_FRAMEWORK_TRANSACTION|CROSS_FRAMEWORK_TRANSACTION]]
- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/LINEAGE_GRAPH|LINEAGE_GRAPH]]
- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/MULTI_RSCF_TRANSACTION|MULTI_RSCF_TRANSACTION]]
- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/PARAMETER_PROVENANCE|PARAMETER_PROVENANCE]]
- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/SEMANTIC_TRANSACTION|SEMANTIC_TRANSACTION]]
- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/SEMANTIC_TRANSACTION_CONTROL_PLANE_README|SEMANTIC_TRANSACTION_CONTROL_PLANE_README]]

## Subdirectories

- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/00_INDEX/SEMANTIC_TRANSACTION_MAP|SEMANTIC_TRANSACTION_MAP]] — 00_INDEX

## Purpose

Governs the semantic transaction surface of the AMOS control plane — managing cross-framework, multi-RSCF transactions that span multiple reasoning and structural contexts. Semantic transactions ensure that multi-step operations either commit atomically or roll back cleanly.

## Key Artifacts

- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/CANON_SEMANTIC_TRANSACTION|CANON_SEMANTIC_TRANSACTION]] — Canonical semantic transaction model with ACID-like guarantees
- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/MULTI_RSCF_TRANSACTION|MULTI_RSCF_TRANSACTION]] — Multi-RSCF transaction coordinator for cross-context atomicity
- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/CROSS_FRAMEWORK_TRANSACTION|CROSS_FRAMEWORK_TRANSACTION]] — Cross-framework transaction protocol for inter-system operations
- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/LINEAGE_GRAPH|LINEAGE_GRAPH]] — Lineage graph tracking transaction dependency chains

## Invariants

- Multi-RSCF transactions must be atomic: all participants commit or none commit
- Transaction lineage must be acyclic; cycles indicate dependency corruption
- Parameter provenance must be captured for every transaction participant
- Cross-framework transactions must respect the weakest-framework safety floor

## Cross-References

- [[03_CONTROL_PLANE/05_PROVENANCE/05_PROVENANCE_MOC|05_PROVENANCE_MOC]] — Provenance plane provides the read-set validation substrate
- [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]] — Commit plane finalizes semantic transactions
- [[03_CONTROL_PLANE/12_ROLLBACK/12_ROLLBACK_MOC|12_ROLLBACK_MOC]] — Rollback plane handles transaction abort and state restoration

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
