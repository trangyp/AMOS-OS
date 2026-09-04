---
title: O02 Relation MOC
type: moc
source: 25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION
tags:
  - o02-relation
  - domain/cognitive-matrix
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# O02 Relation — Map of Content

**Path:** `25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION`
**Files:** 20 | **Subdirectories:** 1

## Files

- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/COGNITIVE_MATRIX_O02_RELATION_CONTRACT|COGNITIVE_MATRIX_O02_RELATION_CONTRACT]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_AGENTS|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_AGENTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_CONTROL_PLANES|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_CONTROL_PLANES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEFINITION|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEFINITION]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEPENDENCIES|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_DEPENDENCIES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_FAILURE_MODES|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_FAILURE_MODES]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_GAP_MATRIX|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_GAP_MATRIX]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_HML|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_HML]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INPUT_OUTPUT|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INPUT_OUTPUT]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INVARIANTS|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_INVARIANTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_POSTCONDITIONS|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_POSTCONDITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PRECONDITIONS|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PRECONDITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PROTOCOLS|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_PROTOCOLS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_RSCF|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_RSCF]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SEMANTICS|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SEMANTICS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SKILLS|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_SKILLS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_STATE_TRANSITIONS|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_STATE_TRANSITIONS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_TESTS|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_TESTS]]
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_WORKFLOWS|O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_WORKFLOWS]]

## Purpose & Definition

O02 Relation is the **third lifecycle operation** — it discovers, establishes, and maintains relationships between objects constituted by O01. Relations are the connective tissue of the cognitive matrix: they transform a collection of isolated objects into a structured graph where meaning emerges from connections. A relation in AMOS is a typed, directional (or bidirectional) link between two or more objects, carrying metadata about the nature, strength, and provenance of the connection.

Relations enable downstream operations to reason about structure: [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O03_BINDING/O03_BINDING_MOC|O03 Binding]] groups related objects into coherent schemas, and [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O06_MODEL/O06_MODEL_MOC|O06 Model]] uses relation graphs to construct internal models of the world.

## Key Sub-artifacts and Their Roles
See the **Files** section above for the complete list of 20 sub-artifacts. Key artifacts:
| `DEFINITION` | Formal specification of relation types, semantics, and inference rules |
| `CONTRACT` | Input/output contract binding relation formation to the lifecycle |
| `PRECONDITIONS` | Requires at least two constituted objects from O01 |
| `POSTCONDITIONS` | All output relations are typed, validated, and registered in the relation graph |
| `INVARIANTS` | Relation integrity: no dangling relations; all endpoints must be live objects |

*...and remaining artifacts (PROTOCOLS, FAILURE_MODES, HML, GAP_MATRIX, DEPENDENCIES, AGENTS, CONTROL_PLANES, SKILLS, WORKFLOWS, TESTS, RSCF, README) — see Files section.*

## Input/Output Contracts

- **Input:** Constituted objects from [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O01_OBJECT/O01_OBJECT_MOC|O01 Object]] — at least two objects with stable identities and attribute sets.
- **Output:** A relation graph — typed edges between objects, each carrying relation type, strength, provenance, and temporal metadata. Registered for consumption by O03 Binding.
- **Contract:** `COGNITIVE_MATRIX_O02_RELATION_CONTRACT` — binds relation formation to lifecycle invariants.

## Cross-references to Lifecycle Operations

- **Predecessor:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O01_OBJECT/O01_OBJECT_MOC|O01 Object]] — provides constituted objects as endpoints for relations.
- **Successor:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O03_BINDING/O03_BINDING_MOC|O03 Binding]] — groups related objects into coherent bound structures.
- **Chain position:** O00→O01→**O02**→O03→O04→O05→O06→O07→O08→O09→O10→O11→O12→O13→O14→O15

## Canonical Laws

- **L3 (Relation Law):** Every relation has a type, a direction, and a strength; untyped or undirected relations are treated as unknown until classified.
- **L4 (Graph Integrity Law):** The relation graph must remain consistent — no dangling edges, no orphaned endpoints.
- **L7 (Observability Law):** Relation discovery and modification are observable and auditable.
- **L10 (Transitivity Law):** Transitive relation types propagate through the graph according to their defined closure rules.
- Applicable: L0–L16 operational, L17–L32 governance constraints on relation authority.

## AMOS Architectural Alignment

O02 Relation sits in `02_LIFECYCLE_OPERATIONS` within the 25-plane MECE architecture. It is governed by [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C05_REPRESENTATION/C05_REPRESENTATION_MOC|C05 Representation]] (relation encoding) and [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C01_GOVERNANCE/C01_GOVERNANCE_MOC|C01 Governance]] (authority to create/modify relations). The relation graph interfaces with [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O05_MEMORY/O05_MEMORY_MOC|O05 Memory]] for persistence and [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O06_MODEL/O06_MODEL_MOC|O06 Model]] for model construction.

## Implementation Status and Open Questions

- **Status:** `DERIVED` — relation formation is specified but executable closure is not verified. `SPECIFIED != EXECUTED`.
- **Open questions:** How are relation types discovered vs predefined? What is the relation strength decay function? How are conflicting relations between the same object pair resolved?
- **Gaps:** See `GAP_MATRIX` sub-artifact for the full inventory.

## Related Skills, Agents & Workflows

- **Skills:** `amos-relation-extraction`, `amos-graph-reasoning`, `amos-link-prediction`
- **Agents:** `amos-relation-agent.json`, `amos-graph-agent.json`
- **Workflows:** `amos-relation-discovery.json`, `amos-graph-maintenance.json`

## Subdirectories

- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/O02_RELATION/00_INDEX/INDEX_O02_RELATION_LIFECYCLE_OPERATIONS_COGNITIVE_MATRIX_README|O02 Relation Index README]] — 00_INDEX

______________________________________________________________________

**Parent:** [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/02_LIFECYCLE_OPERATIONS_MOC|02_LIFECYCLE_OPERATIONS_MOC]]
