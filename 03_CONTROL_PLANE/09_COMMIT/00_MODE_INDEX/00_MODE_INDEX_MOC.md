---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 00 Mode Index Moc
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

# 00 Mode Index — Map of Content

**Path:** `03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX`
**Files:** 15 | **Subdirectories:** 0

## Files

- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_ADMISSION_QUEUE|MODE_ADMISSION_QUEUE]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_COMPOSITION_REGISTRY|MODE_COMPOSITION_REGISTRY]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_CONFLICT_REGISTRY|MODE_CONFLICT_REGISTRY]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_COVERAGE_MATRIX|MODE_COVERAGE_MATRIX]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_DEPENDENCY_GRAPH|MODE_DEPENDENCY_GRAPH]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_DISCOVERY_QUEUE|MODE_DISCOVERY_QUEUE]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_EXTENSION_PROTOCOL|MODE_EXTENSION_PROTOCOL]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_FALSIFIER_REGISTRY|MODE_FALSIFIER_REGISTRY]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_GAP_REGISTRY|MODE_GAP_REGISTRY]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_INDEX_COMMIT_CONTROL_PLANE_README|MODE_INDEX_COMMIT_CONTROL_PLANE_README]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_ONTOLOGY|MODE_ONTOLOGY]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_PLACEHOLDER_AUDIT_2026-08-25|MODE_PLACEHOLDER_AUDIT_2026-08-25]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_REGISTRY|MODE_REGISTRY]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_REVALIDATION_SCHEDULE|MODE_REVALIDATION_SCHEDULE]]
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_TRANSITION_MATRIX|MODE_TRANSITION_MATRIX]]

## Purpose

Governs the mode index registry within the AMOS commit plane — providing the authoritative index of all commit modes, their admission status, conflicts, coverage, and lifecycle. The mode index is the central registry that makes the commit mode system navigable and auditable.

## Key Artifacts

- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_REGISTRY|MODE_REGISTRY]] — Authoritative registry of all admitted commit modes
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_ADMISSION_QUEUE|MODE_ADMISSION_QUEUE]] — Queue of modes awaiting admission review
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_CONFLICT_REGISTRY|MODE_CONFLICT_REGISTRY]] — Registry of known mode conflicts and resolution strategies
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_COVERAGE_MATRIX|MODE_COVERAGE_MATRIX]] — Coverage matrix mapping modes to operational domains
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_ONTOLOGY|MODE_ONTOLOGY]] — Ontological classification of commit modes
- [[03_CONTROL_PLANE/09_COMMIT/00_MODE_INDEX/MODE_TRANSITION_MATRIX|MODE_TRANSITION_MATRIX]] — State transition matrix for mode lifecycle

## Invariants

- Every admitted mode must have a registry entry with provenance and signer identity
- Mode conflicts must be resolved before commit; unresolved conflicts block finalization
- Mode coverage gaps must be registered in the gap registry with remediation status
- Mode admission requires falsifier registry clearance and extension protocol compliance

## Cross-References

- [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]] — Parent commit plane MOC
- [[03_CONTROL_PLANE/06_AUDIT/06_AUDIT_MOC|06_AUDIT_MOC]] — Audit plane verifies mode admission provenance
- [[03_CONTROL_PLANE/03_POLICY/03_POLICY_MOC|03_POLICY_MOC]] — Policy plane evaluates mode admission criteria

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]]
