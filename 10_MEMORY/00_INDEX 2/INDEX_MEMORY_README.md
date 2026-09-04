---
title: Memory Index
type: index
source: 10_MEMORY/00_INDEX
status: ACTIVE_INDEX
conclusion_class: DERIVED
origin_architect: Trang Phan
---
# Memory Index

This directory is a navigation and identity-resolution surface for `10_MEMORY`.

## Entries
- [[MEMORY_MEMORY_MAP|MEMORY_MEMORY_MAP]]
- [[INDEX_MEMORY_MEMORY_CONTRACT|INDEX_MEMORY_MEMORY_CONTRACT]]
- [[../MEMORY_README|MEMORY_README]]
- [[../MEMORY_MEMORY_CONTRACT|MEMORY_MEMORY_CONTRACT]]

## Index invariant
`INDEXED != AUTHORITATIVE`
`LINKED != VALIDATED`
`PRESENT != CURRENT`

An index may locate an artifact. It does not grant authority, upgrade epistemic class, prove implementation, or replace the governing plane contract. Broken or ambiguous resolution remains `UNKNOWN/GAP`.

## Domain/Plane Overview
The `00_INDEX` directory within `10_MEMORY` serves as the navigation and identity-resolution surface for the Memory plane. It aggregates pointers to the plane's MOC, README, contract, and map, enabling readers and agents to locate Memory artifacts without scanning the full directory tree.

This index is not a knowledge store. It holds no semantic content about memory artifacts — only routing metadata sufficient to locate them.

## MECE Classification
| Category | Artifact | Function |
|----------|----------|----------|
| Topology | `MEMORY_MEMORY_MAP` | Describes reading order and map boundaries |
| Contract | `INDEX_MEMORY_MEMORY_CONTRACT` | Bounds index-layer behavior |
| Orientation | `MEMORY_README` | Operational guidance for the plane |
| Normative | `MEMORY_MEMORY_CONTRACT` | Governing plane invariants |

Each entry belongs to exactly one category; together they cover the index surface of `10_MEMORY`.

## Key Artifacts
- [[10_MEMORY/00_INDEX 2/MEMORY_MEMORY_MAP|MEMORY_MEMORY_MAP]] — topology and reading order.
- [[10_MEMORY/00_INDEX 2/INDEX_MEMORY_MEMORY_CONTRACT|INDEX_MEMORY_MEMORY_CONTRACT]] — index contract.
- [[10_MEMORY/MEMORY_README|MEMORY_README]] — operational orientation.
- [[10_MEMORY/MEMORY_MEMORY_CONTRACT|MEMORY_MEMORY_CONTRACT]] — normative contract.
- [[10_MEMORY/10_MEMORY_MOC|10_MEMORY_MOC]] — plane MOC.

## Cross-Plane Relationships
- **Control plane (`03_CONTROL_PLANE`)**: the cognitive vault resolver may consult this index for Memory-plane routing.
- **Knowledge plane (`11_KNOWLEDGE`)**: memory entries may point to knowledge artifacts, but the index does not establish dependency.
- **Archive (`24_ARCHIVE`)**: superseded memory artifacts are archived; this index reflects only active entries.

## Epistemic Boundary
This index is `DERIVED`. `INDEXED != AUTHORITATIVE`, `LINKED != VALIDATED`, `PRESENT != CURRENT`. The index locates artifacts; it does not validate, authorize, or promote them. Missing or ambiguous targets remain `UNKNOWN/GAP` and are never synthesized from filenames.

---

**Parent:** [[10_MEMORY/10_MEMORY_MOC|10_MEMORY_MOC]]
