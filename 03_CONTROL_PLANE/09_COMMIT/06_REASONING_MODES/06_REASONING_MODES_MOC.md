---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 06 Reasoning Modes Moc
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

# 06 Reasoning Modes — Map of Content

**Path:** `03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES`
**Files:** 3 | **Subdirectories:** 5

## Files

- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/REASONING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY|REASONING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY]]
- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/REASONING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC|REASONING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC]]
- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/REASONING_MODES_COMMIT_CONTROL_PLANE_README|REASONING_MODES_COMMIT_CONTROL_PLANE_README]]

## Subdirectories

- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/01_EXPLORE/01_EXPLORE_MOC|01_EXPLORE_MOC]] — 01_EXPLORE
- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/02_DIAGNOSE/02_DIAGNOSE_MOC|02_DIAGNOSE_MOC]] — 02_DIAGNOSE
- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/03_DESIGN/03_DESIGN_MOC|03_DESIGN_MOC]] — 03_DESIGN
- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/04_AUDIT/04_AUDIT_MOC|04_AUDIT_MOC]] — 04_AUDIT
- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/05_MEASURE/05_MEASURE_MOC|05_MEASURE_MOC]] — 05_MEASURE

## Purpose

Governs the reasoning modes family within the AMOS commit plane — indexing the five canonical reasoning sub-modes (Explore, Diagnose, Design, Audit, Measure) that structure how the system reasons before committing. Each sub-mode has distinct preconditions, exit criteria, and commit semantics.

## Key Artifacts

- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/REASONING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC|REASONING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC]] — Canonical specification for the reasoning modes family
- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/REASONING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY|REASONING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY]] — Registry of admitted reasoning modes with provenance
- [[03_CONTROL_PLANE/09_COMMIT/06_REASONING_MODES/REASONING_MODES_COMMIT_CONTROL_PLANE_README|REASONING_MODES_COMMIT_CONTROL_PLANE_README]] — Overview and navigation for the reasoning modes family

## Invariants

- Each reasoning sub-mode must define explicit exit criteria before activation
- Reasoning mode transitions must be recorded with causal provenance
- No reasoning mode may externalize effects — reasoning is pre-commit
- Sub-mode composition must respect the conflict registry constraints

## Cross-References

- [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]] — Parent commit plane MOC
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/00_MODE_INDEX_MOC|00_MODE_INDEX_MOC]] — Mode index tracks reasoning mode admission and transitions
- [[03_CONTROL_PLANE/05_PROVENANCE/05_PROVENANCE_MOC|05_PROVENANCE_MOC]] — Provenance plane records reasoning mode lineage

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]]
