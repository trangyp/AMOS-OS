---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Dependency Types
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - cognitive-matrix
updated: 2026-09-14
---

# DEPENDENCY_TYPES — Bounded Executable Contract

**Origin architect / steward:** Trang Phan  
**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_runtime.py`

## Directed dependency semantics

A dependency edge is oriented

```text
dependency -> dependent
```

and has exactly one declared type:

- `HARD`: downstream validity/function requires the upstream state.
- `EVIDENCE`: downstream epistemic standing relies on upstream evidence.
- `AUTHORITY`: downstream effect permission relies on upstream authority state.
- `SOFT`: advisory association; does not propagate staleness in this bounded runtime.

Edge type is invariant after insertion; silently retagging an existing edge fails closed.

## Load-bearing propagation

`HARD`, `EVIDENCE`, and `AUTHORITY` edges propagate staleness. `SOFT` edges do not.

If node `p` is invalidated, only descendants reachable through load-bearing edges are marked `STALE`. The invalidated node is quarantined unless already `COMPETING` or `FALSIFIED`.

Hard boundary:

```text
STALE != FALSE
INVALIDATED_PARENT != ALL_GRAPH_INVALID
```

## Cycle semantics

Load-bearing dependency ordering requires a DAG. The runtime therefore separates two algorithms:

1. Tarjan strongly connected components identify directed cycles.
2. Kahn topological ordering executes only after the load-bearing subgraph is acyclic.

A load-bearing SCC with more than one node is an explicit cycle defect and blocks topological ordering. A cycle made only of `SOFT` edges does not block load-bearing ordering.

## Invariants

- Endpoints are non-empty and distinct.
- Dependency direction is never inferred from file order or lexical order.
- Relation/adjacency does not imply causation.
- A cycle is preserved as evidence; it is not broken arbitrarily.
- Invalidation is selective, not global by default.
- Authority dependencies do not mint authority.

## Executed validation

2026-09-14 bounded tests verified:

- dependency-before-dependent ordering;
- deterministic cycle detection;
- fail-closed topological sort on a three-node cycle;
- soft-cycle exclusion from the load-bearing DAG;
- selective descendant invalidation;
- unrelated-node preservation;
- seeded randomized DAGs from 2 through 39 nodes with every generated edge respecting the returned order.

## Boundary

This implementation establishes graph mechanics only. Whether an asserted dependency edge is factually correct remains a separate evidence/provenance question.

[[25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/09_DEPENDENCY_GRAPH_MOC|09_DEPENDENCY_GRAPH_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
