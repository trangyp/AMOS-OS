---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 02 Diagnose Moc
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

# 02 Diagnose — Map of Content

**Path:** `03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/02_DIAGNOSE`
**Files:** 3 | **Subdirectories:** 0

## Files

- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/02_DIAGNOSE/COMMIT_CONTROL_PLANE_MODE_SPEC|COMMIT_CONTROL_PLANE_MODE_SPEC]]
- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/02_DIAGNOSE/COMMIT_CONTROL_PLANE_PROVENANCE|COMMIT_CONTROL_PLANE_PROVENANCE]]
- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/02_DIAGNOSE/DIAGNOSE_REASONING_MODES_COMMIT_CONTROL_PLANE_README|DIAGNOSE_REASONING_MODES_COMMIT_CONTROL_PLANE_README]]

## Purpose

Governs the Diagnose reasoning sub-mode within the AMOS commit plane — defining how diagnostic reasoning and root-cause analysis are structured, validated, and committed. This sub-mode operates under the reasoning modes family with its own preconditions, exit criteria, and provenance requirements.

## Key Artifacts

- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/02_DIAGNOSE/COMMIT_CONTROL_PLANE_MODE_SPEC|COMMIT_CONTROL_PLANE_MODE_SPEC]] — Detailed mode specification with preconditions and exit criteria
- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/02_DIAGNOSE/COMMIT_CONTROL_PLANE_PROVENANCE|COMMIT_CONTROL_PLANE_PROVENANCE]] — Provenance record for sub-mode admission and lineage
- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/02_DIAGNOSE/DIAGNOSE_REASONING_MODES_COMMIT_CONTROL_PLANE_README|DIAGNOSE_REASONING_MODES_COMMIT_CONTROL_PLANE_README]] — Overview and navigation for this reasoning sub-mode

## Invariants

- Diagnose sub-mode must define explicit preconditions and exit criteria
- Sub-mode transitions must be recorded with causal provenance
- No sub-mode may externalize effects — reasoning is pre-commit
- Sub-mode activation must satisfy parent reasoning mode family constraints

## Cross-References

- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/06_REASONING_MODES_MOC|06_REASONING_MODES_MOC]] — Parent reasoning modes family MOC
- [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]] — Parent commit plane MOC
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/00_MODE_INDEX_MOC|00_MODE_INDEX_MOC]] — Mode index tracks admission, conflicts, and coverage

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/06_REASONING_MODES_MOC|06_REASONING_MODES_MOC]]
