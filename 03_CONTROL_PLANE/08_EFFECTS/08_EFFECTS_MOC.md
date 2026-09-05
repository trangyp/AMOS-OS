---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 08 Effects Moc
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

# 08 Effects — Map of Content

**Path:** `03_CONTROL_PLANE/08_EFFECTS`
**Files:** 5 | **Subdirectories:** 1

## Files

- [[03_CONTROL_PLANE/08_EFFECTS/CONTROL_PLANE_EFFECTS_CONTRACT|CONTROL_PLANE_EFFECTS_CONTRACT]]
- [[03_CONTROL_PLANE/08_EFFECTS/EFFECTS_CONTROL_PLANE_README|EFFECTS_CONTROL_PLANE_README]]
- [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_INTENT|EFFECT_INTENT]]
- [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_MANIFEST|EFFECT_MANIFEST]]
- [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_RELEASE_STATE|EFFECT_RELEASE_STATE]]

## Subdirectories

- [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] — 00_INDEX

## Purpose

Governs the effects surface of the AMOS control plane — modeling the lifecycle of effects from intent through release state, ensuring that externalized effects are authorized, witnessed, and committed before they become observable. Effects are the boundary where internal decisions become external consequences.

## Key Artifacts

- [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_INTENT|EFFECT_INTENT]] — Declared intent for an effect before authorization or execution
- [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_RELEASE_STATE|EFFECT_RELEASE_STATE]] — State machine governing effect release: pending → authorized → committed → externalized
- [[03_CONTROL_PLANE/08_EFFECTS/EFFECT_MANIFEST|EFFECT_MANIFEST]] — Manifest of all declared effects with scope and target
- [[03_CONTROL_PLANE/08_EFFECTS/CONTROL_PLANE_EFFECTS_CONTRACT|CONTROL_PLANE_EFFECTS_CONTRACT]] — Binding contract for effect declaration, authorization, and release

## Invariants

- Effect ≠ Authorization — declaring an effect does not authorize it
- Effects must not externalize before commit-time freshness validation
- Effect release state transitions must be atomic and auditable
- Effect sink attestations must bound trusted intermediary behavior

## Cross-References

- [[03_CONTROL_PLANE/04_AUTHORITY/04_AUTHORITY_MOC|04_AUTHORITY_MOC]] — Authority plane authorizes effects before release
- [[03_CONTROL_PLANE/07_OBSERVABILITY/07_OBSERVABILITY_MOC|07_OBSERVABILITY_MOC]] — Observability plane monitors effect lifecycle events
- [[03_CONTROL_PLANE/10_EXPOSURE/10_EXPOSURE_MOC|10_EXPOSURE_MOC]] — Exposure plane governs the externalization boundary for effects

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
