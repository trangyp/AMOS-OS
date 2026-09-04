---
title: Memory Map
type: navigation_map
source: 10_MEMORY/00_INDEX
status: ACTIVE_INDEX
conclusion_class: DERIVED
origin_architect: Trang Phan
---
# Memory Map

## Reading order
1. `../10_MEMORY_MOC.md` — plane purpose and routing.
2. `../MEMORY_README.md` — operational orientation and boundaries.
3. `../MEMORY_MEMORY_CONTRACT.md` — normative plane contract.
4. Child artifacts — implementation/domain details where present.

## Map boundary
This map describes topology only.

`MAP EDGE != DEPENDENCY PROOF`
`MAP LOCATION != AUTHORITY`
`MAP COMPLETENESS != SYSTEM COMPLETENESS`

Cross-plane dependencies must be established by the referenced artifact's own typed contract/provenance, not inferred from this map.

## Domain/Plane Overview
The Memory plane (`10_MEMORY`) persists agent-learned memory, session state, and operational history across AMOS sessions. This map describes the topology of that plane: which artifacts exist, how they relate, and in what order a reader should traverse them.

The map covers:
- The plane MOC (`10_MEMORY_MOC`) — purpose, routing, and boundary.
- The operational README (`MEMORY_README`) — orientation and usage boundaries.
- The normative contract (`MEMORY_MEMORY_CONTRACT`) — governing invariants.
- Child artifacts — domain-specific memory implementations where present.

## MECE Classification
| Layer | Artifact | Class | Role |
|-------|----------|-------|------|
| Navigation | `10_MEMORY_MOC` | DERIVED | Plane routing and purpose |
| Orientation | `MEMORY_README` | DERIVED | Operational guidance |
| Normative | `MEMORY_MEMORY_CONTRACT` | AMOS_MODEL | Governing invariants |
| Index | `MEMORY_MEMORY_MAP` | DERIVED | Topology description |
| Index | `INDEX_MEMORY_MEMORY_CONTRACT` | DERIVED | Index-layer contract |

These layers are mutually exclusive in function and collectively exhaustive for the index surface of `10_MEMORY`.

## Key Artifacts
- [[10_MEMORY/10_MEMORY_MOC|10_MEMORY_MOC]] — plane map of content.
- [[10_MEMORY/MEMORY_README|MEMORY_README]] — operational orientation.
- [[10_MEMORY/MEMORY_MEMORY_CONTRACT|MEMORY_MEMORY_CONTRACT]] — normative plane contract.
- [[10_MEMORY/00_INDEX 2/INDEX_MEMORY_MEMORY_CONTRACT|INDEX_MEMORY_MEMORY_CONTRACT]] — index-layer contract.
- [[10_MEMORY/00_INDEX 2/INDEX_MEMORY_README|INDEX_MEMORY_README]] — index README.

## Cross-Plane Relationships
- **Knowledge plane (`11_KNOWLEDGE`)**: memory artifacts may reference knowledge kernels, but dependency is established by the kernel's own provenance, not by this map.
- **Control plane (`03_CONTROL_PLANE`)**: the vault resolver may consult this map for routing; the map does not authorize resolver behavior.
- **Archive (`24_ARCHIVE`)**: retired memory artifacts are moved to archive; this map reflects only active topology.

## Epistemic Boundary
This map is a `DERIVED` topology surface. `MAP EDGE != DEPENDENCY PROOF`, `MAP LOCATION != AUTHORITY`, `MAP COMPLETENESS != SYSTEM COMPLETENESS`. The map does not validate, authorize, or promote any artifact. Cross-plane dependencies require the referenced artifact's own typed contract.

---

**Parent:** [[10_MEMORY/10_MEMORY_MOC|10_MEMORY_MOC]]
