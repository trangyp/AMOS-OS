---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 02 Capability Moc
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

# 02 Capability — Map of Content

**Path:** `03_CONTROL_PLANE/02_CAPABILITY`
**Files:** 4 | **Subdirectories:** 1

## Files

- [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_CONTROL_PLANE_README|CAPABILITY_CONTROL_PLANE_README]]
- [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_MANIFEST|CAPABILITY_MANIFEST]]
- [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_RESOLVER|CAPABILITY_RESOLVER]]
- [[03_CONTROL_PLANE/02_CAPABILITY/CONTROL_PLANE_CAPABILITY_CONTRACT|CONTROL_PLANE_CAPABILITY_CONTRACT]]

## Subdirectories

- [[03_CONTROL_PLANE/02_CAPABILITY/00_INDEX/CAPABILITY_MAP|CAPABILITY_MAP]] — 00_INDEX

## Purpose

Governs the capability surface of the AMOS control plane — defining, resolving, and manifesting the bounded authority capabilities that agents may exercise. Capabilities are the atomic unit of bounded authority: they encode what an agent *can* do, not what it *may* do (that is the domain of policy).

## Key Artifacts

- [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_MANIFEST|CAPABILITY_MANIFEST]] — Canonical manifest of all admitted capabilities with scope and attenuation
- [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_RESOLVER|CAPABILITY_RESOLVER]] — Resolves capability requests against the manifest at commit time
- [[03_CONTROL_PLANE/02_CAPABILITY/CONTROL_PLANE_CAPABILITY_CONTRACT|CONTROL_PLANE_CAPABILITY_CONTRACT]] — Binding contract between capability grants and enforcement

## Invariants

- Capability ≠ Authority — a capability grant does not authorize exercise
- Capability ≠ Reachability — holding a capability does not guarantee a path to the target
- Capabilities are attenuable: child scope ⊆ parent scope at all times
- Capability manifests must be content-addressed and version-pinned at commit time

## Cross-References

- [[03_CONTROL_PLANE/03_POLICY/03_POLICY_MOC|03_POLICY_MOC]] — Policy plane decides whether a capability may be exercised
- [[03_CONTROL_PLANE/04_AUTHORITY/04_AUTHORITY_MOC|04_AUTHORITY_MOC]] — Authority plane binds capabilities to authorization decisions
- [[03_CONTROL_PLANE/05_PROVENANCE/05_PROVENANCE_MOC|05_PROVENANCE_MOC]] — Provenance plane tracks capability lineage and read-set dependencies

______________________________________________________________________

**Parent:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
