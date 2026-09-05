---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 95 Constraint Solving Modes Moc
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

# 95 Constraint Solving Modes — Map of Content

**Path:** `03_CONTROL_PLANE/09_COMMIT/95_CONSTRAINT_SOLVING_MODES`
**Files:** 3 | **Subdirectories:** 0

## Files

- [[03_CONTROL_PLANE/09_COMMIT/95_CONSTRAINT_SOLVING_MODES/CONSTRAINT_SOLVING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY|CONSTRAINT_SOLVING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY]]
- [[03_CONTROL_PLANE/09_COMMIT/95_CONSTRAINT_SOLVING_MODES/CONSTRAINT_SOLVING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC|CONSTRAINT_SOLVING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC]]
- [[03_CONTROL_PLANE/09_COMMIT/95_CONSTRAINT_SOLVING_MODES/CONSTRAINT_SOLVING_MODES_COMMIT_CONTROL_PLANE_README|CONSTRAINT_SOLVING_MODES_COMMIT_CONTROL_PLANE_README]]

## Purpose

Governs the Constraint Solving Modes mode family within the AMOS commit plane — defining how constraint solving modes operations are structured, activated, and committed. This mode family specifies the operational parameters, safety gates, and validation requirements for its domain.

## Key Artifacts

- [[03_CONTROL_PLANE/09_COMMIT/95_CONSTRAINT_SOLVING_MODES/CONSTRAINT_SOLVING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY|CONSTRAINT_SOLVING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY]] — Registry of admitted modes in this family with provenance
- [[03_CONTROL_PLANE/09_COMMIT/95_CONSTRAINT_SOLVING_MODES/CONSTRAINT_SOLVING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC|CONSTRAINT_SOLVING_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC]] — Canonical specification for the mode family
- [[03_CONTROL_PLANE/09_COMMIT/95_CONSTRAINT_SOLVING_MODES/CONSTRAINT_SOLVING_MODES_COMMIT_CONTROL_PLANE_README|CONSTRAINT_SOLVING_MODES_COMMIT_CONTROL_PLANE_README]] — Overview and navigation for this mode family

## Invariants

- Mode family spec must define activation conditions, preconditions, and postconditions
- Mode family registry must track all admitted modes with provenance and signer identity
- Mode transitions must be atomic, auditable, and conflict-registry compliant
- Mode composition must respect the commit-plane safety gate hierarchy

## Cross-References

- [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]] — Parent commit plane MOC
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/00_MODE_INDEX_MOC|00_MODE_INDEX_MOC]] — Mode index tracks admission, conflicts, and coverage
- [[03_CONTROL_PLANE/05_PROVENANCE/05_PROVENANCE_MOC|05_PROVENANCE_MOC]] — Provenance plane records mode lineage and read-set dependencies

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]]
