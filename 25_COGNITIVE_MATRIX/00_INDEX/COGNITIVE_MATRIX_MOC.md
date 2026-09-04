---
title: Index MOC — Cognitive Matrix / Index
type: moc
source: 25_COGNITIVE_MATRIX/00_INDEX
tags:
  - domain/cognitive-matrix
  - cognitive-matrix-architecture
  - cognitive-matrix-naming-standard
  - status-legend
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: index_navigation
---

# 00 Index — Map of Content

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **MECE Domain:** C — Cognitive Capability & Orchestration
> **Plane:** `25_COGNITIVE_MATRIX/00_INDEX`

**Path:** `25_COGNITIVE_MATRIX/00_INDEX`
**Files:** 10 | **Subdirectories:** 0

## Purpose

The Index sub-plane is the canonical navigation and registry hub for the entire `25_COGNITIVE_MATRIX` plane. It contains the architectural specification, naming standards, registries for all cognitive primitives/lifecycle operations/scales/control planes, and the status legend that governs how cognitive matrix artifacts are classified.

## MECE Scope

Within the MECE partition ([[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]), `00_INDEX` is the navigation hub of `25_COGNITIVE_MATRIX` (Domain C — Cognitive Capability & Orchestration). Its primary ownership is **registry and navigation artifacts for the cognitive matrix**. It does not own primitive definitions, lifecycle operations, or scale configurations — those belong to their respective sub-planes.

## Files

### Architecture & Standards
- [[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_ARCHITECTURE|COGNITIVE_MATRIX_ARCHITECTURE]] — Master architectural specification for the cognitive matrix, defining the overall structure, primitive layers, lifecycle operations, control planes, and scales
- [[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_NAMING_STANDARD|COGNITIVE_MATRIX_NAMING_STANDARD]] — Naming conventions for all cognitive matrix artifacts (primitives, operations, scales, control planes)
- [[25_COGNITIVE_MATRIX/00_INDEX/STATUS_LEGEND|STATUS_LEGEND]] — Status classification system for cognitive matrix artifacts (PROPOSED, ACTIVE, DEPRECATED, etc.)

### Maps & Contracts
- [[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MAP|COGNITIVE_MATRIX_MAP]] — Visual/textual map of the cognitive matrix structure and inter-component relationships
- [[25_COGNITIVE_MATRIX/00_INDEX/INDEX_COGNITIVE_MATRIX_COGNITIVE_MATRIX_CONTRACT|INDEX_COGNITIVE_MATRIX_COGNITIVE_MATRIX_CONTRACT]] — Formal contract governing the cognitive matrix index and its resolution rules
- [[25_COGNITIVE_MATRIX/00_INDEX/INDEX_COGNITIVE_MATRIX_README|INDEX_COGNITIVE_MATRIX_README]] — README explaining the cognitive matrix index and its role in navigation

### Registries
- [[25_COGNITIVE_MATRIX/00_INDEX/PRIMITIVE_REGISTRY|PRIMITIVE_REGISTRY]] — Registry of all 30 cognitive primitives (L00–L29) with their definitions, scales, and status
- [[25_COGNITIVE_MATRIX/00_INDEX/LIFECYCLE_OPERATION_REGISTRY|LIFECYCLE_OPERATION_REGISTRY]] — Registry of all lifecycle operations (O00–O16) with their definitions and bindings
- [[25_COGNITIVE_MATRIX/00_INDEX/SCALE_REGISTRY|SCALE_REGISTRY]] — Registry of the three cognitive scales (L, M, H) with their properties and transition rules
- [[25_COGNITIVE_MATRIX/00_INDEX/CONTROL_PLANE_REGISTRY|CONTROL_PLANE_REGISTRY]] — Registry of the nine cognitive control planes (C01–C09) with their governance scopes

## Cognitive Matrix Structure

The cognitive matrix is organized into four major dimensions:

1. **Primitives (01_PRIMITIVES/)** — 30 cognitive primitives (L00–L29) from reality environment to evolution, forming the complete cognitive cycle
2. **Lifecycle Operations (02_LIFECYCLE_OPERATIONS/)** — 17 operations (O00–O16) that govern how primitives are instantiated, executed, and retired
3. **Control Planes (03_CONTROL_PLANES/)** — 9 control planes (C01–C09) that govern cognitive governance, metacognition, execution, reasoning, representation, memory, perception, execution, and kernel control
4. **Scales (04_SCALES/)** — 3 cognitive scales (L, M, H) representing different processing depths and resource allocations

## Relationships

### Upstream
- [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]] — Parent cognitive matrix MOC
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] — Root navigation
- [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]] — MECE architecture specification

### Downstream
- [[25_COGNITIVE_MATRIX/01_PRIMITIVES/01_PRIMITIVES_MOC|01_PRIMITIVES_MOC]] — Primitives sub-plane
- [[25_COGNITIVE_MATRIX/02_LIFECYCLE_OPERATIONS/02_LIFECYCLE_OPERATIONS_MOC|02_LIFECYCLE_OPERATIONS_MOC]] — Lifecycle operations sub-plane
- [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/03_CONTROL_PLANES_MOC|03_CONTROL_PLANES_MOC]] — Control planes sub-plane
- [[25_COGNITIVE_MATRIX/04_SCALES/04_SCALES_MOC|04_SCALES_MOC]] — Scales sub-plane

### Supporting Sub-planes
- [[25_COGNITIVE_MATRIX/05_CELL_REGISTRY/05_CELL_REGISTRY_MOC|05_CELL_REGISTRY]] — Cell registry
- [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/06_CELL_CONTRACTS_MOC|06_CELL_CONTRACTS]] — Cell contracts
- [[25_COGNITIVE_MATRIX/07_COVERAGE/07_COVERAGE_MOC|07_COVERAGE]] — Coverage analysis
- [[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/08_STRUCTURAL_GAPS_MOC|08_STRUCTURAL_GAPS]] — Structural gap tracking
- [[25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/09_DEPENDENCY_GRAPH_MOC|09_DEPENDENCY_GRAPH]] — Dependency graph
- [[25_COGNITIVE_MATRIX/10_ROUTING/10_ROUTING_MOC|10_ROUTING]] — Cognitive routing
- [[25_COGNITIVE_MATRIX/11_VALIDATION/11_VALIDATION_MOC|11_VALIDATION]] — Validation
- [[25_COGNITIVE_MATRIX/12_GENERATORS/12_GENERATORS_MOC|12_GENERATORS]] — Generators

## Epistemic Boundary

The cognitive matrix is an `AMOS_MODEL` artifact. Its correspondence to actual cognitive architecture is a `SOURCE_CLAIM` from cognitive science and neuroscience literature, not an `EMPIRICAL` observation. The 30-primitive, 17-operation, 9-control-plane, 3-scale structure is a designed architecture, not a discovered one.

`MODEL != OBSERVATION`
`DOCUMENTED != IMPLEMENTED`
`ARCHITECTURE != RUNTIME`

______________________________________________________________________

**Parent:** [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]]
**MECE Architecture:** [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
