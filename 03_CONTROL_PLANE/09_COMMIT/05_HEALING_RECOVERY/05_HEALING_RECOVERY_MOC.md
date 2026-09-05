---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 05 Healing Recovery Moc
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

# 05 Healing Recovery — Map of Content

**Path:** `03_CONTROL_PLANE/09_COMMIT/05_HEALING_RECOVERY`
**Files:** 6 | **Subdirectories:** 0

## Files

- [[03_CONTROL_PLANE/09_COMMIT/05_HEALING_RECOVERY/COMMIT_CONTROL_PLANE_ACTIVATION_RULES|COMMIT_CONTROL_PLANE_ACTIVATION_RULES]]
- [[03_CONTROL_PLANE/09_COMMIT/05_HEALING_RECOVERY/HEALING_RECOVERY_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY|HEALING_RECOVERY_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY]]
- [[03_CONTROL_PLANE/09_COMMIT/05_HEALING_RECOVERY/HEALING_RECOVERY_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC|HEALING_RECOVERY_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC]]
- [[03_CONTROL_PLANE/09_COMMIT/05_HEALING_RECOVERY/HEALING_RECOVERY_COMMIT_CONTROL_PLANE_MODE_SPEC|HEALING_RECOVERY_COMMIT_CONTROL_PLANE_MODE_SPEC]]
- [[03_CONTROL_PLANE/09_COMMIT/05_HEALING_RECOVERY/HEALING_RECOVERY_COMMIT_CONTROL_PLANE_PROVENANCE|HEALING_RECOVERY_COMMIT_CONTROL_PLANE_PROVENANCE]]
- [[03_CONTROL_PLANE/09_COMMIT/05_HEALING_RECOVERY/HEALING_RECOVERY_COMMIT_CONTROL_PLANE_README|HEALING_RECOVERY_COMMIT_CONTROL_PLANE_README]]

## Purpose

Governs the healing and recovery commit mode family within the AMOS commit plane — defining how the system detects degraded states, activates recovery procedures, and commits healed state transitions. Healing modes ensure that the system can self-repair without violating commit invariants.

## Key Artifacts

- [[03_CONTROL_PLANE/09_COMMIT/05_HEALING_RECOVERY/HEALING_RECOVERY_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC|HEALING_RECOVERY_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC]] — Canonical specification for healing-recovery mode family
- [[03_CONTROL_PLANE/09_COMMIT/05_HEALING_RECOVERY/HEALING_RECOVERY_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY|HEALING_RECOVERY_COMMIT_CONTROL_PLANE_MODE_FAMILY_REGISTRY]] — Registry of admitted healing-recovery modes
- [[03_CONTROL_PLANE/09_COMMIT/05_HEALING_RECOVERY/COMMIT_CONTROL_PLANE_ACTIVATION_RULES|COMMIT_CONTROL_PLANE_ACTIVATION_RULES]] — Activation rules for healing-recovery mode triggering
- [[03_CONTROL_PLANE/09_COMMIT/05_HEALING_RECOVERY/HEALING_RECOVERY_COMMIT_CONTROL_PLANE_MODE_SPEC|HEALING_RECOVERY_COMMIT_CONTROL_PLANE_MODE_SPEC]] — Detailed mode specification for healing-recovery operations

## Invariants

- Healing modes must not externalize effects during recovery — recovery is internal
- Recovery state transitions must be atomic and rollback-safe
- Healing mode activation must be triggered by observed degradation, not speculation
- Recovered state must pass full commit-time validation before finalization

## Cross-References

- [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]] — Parent commit plane MOC
- [[03_CONTROL_PLANE/12_ROLLBACK/12_ROLLBACK_MOC|12_ROLLBACK_MOC]] — Rollback plane provides state restoration for failed healing
- [[03_CONTROL_PLANE/07_OBSERVABILITY/07_OBSERVABILITY_MOC|07_OBSERVABILITY_MOC]] — Observability plane detects degradation triggering healing

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/09_COMMIT/09_COMMIT_MOC|09_COMMIT_MOC]]
