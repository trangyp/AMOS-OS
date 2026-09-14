---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Dependency Types
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# DEPENDENCY_TYPES — Typed Relation Algebra for the Cognitive Matrix

## Status

`AMOS_MODEL / IMPLEMENTED_BOUNDED / LOCALLY_VALIDATED`

Executable owner: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_dependency_runtime.py`.

## Relation syntax

Every active edge is a typed tuple

`e = (edge_id, src, relation, dst, provenance, source_version)`.

The surface syntax is read as

`src RELATION dst`.

The direction is relation-specific; a relation label may not be replaced by an untyped generic edge.

## Relation registry

```text
NECESSARY
SUFFICIENT
SUPPORTING
ALTERNATIVE
CONTRADICTING
DERIVED_FROM
OBSERVED_BY
SUPERSEDES
INVALIDATES
CONDITIONED_ON
CORRELATED_WITH
```

### Load-bearing dependency relations

For structural dependency closure, only

`D_load = {NECESSARY, DERIVED_FROM, CONDITIONED_ON}`

are load-bearing in this bounded runtime.

If `x NECESSARY y`, `x DERIVED_FROM y`, or `x CONDITIONED_ON y`, the direction means `x` depends on `y` for current validity/applicability.

### Review-only evidence relations

`SUPPORTING` and `SUFFICIENT` can trigger re-evaluation when a source is lost, but source loss alone does not justify automatic staleness or falsity of the target.

### Non-dependency relations

`ALTERNATIVE`, `CONTRADICTING`, `OBSERVED_BY`, `SUPERSEDES`, `INVALIDATES`, and `CORRELATED_WITH` do not enter load-bearing dependency closure by default.

`INVALIDATES` is represented as an invalidation proposal relation; it is not self-executing authority.

## Hard firewalls

```text
RELATION != CAUSATION
CORRELATED_WITH != CAUSES
SUPPORTING != NECESSARY
SUFFICIENT_SOURCE_LOST != TARGET_FALSE
CONTRADICTING(A,B) != TRUE(A) OR TRUE(B)
INVALIDATES_EDGE != AUTHORIZED_COMMIT
SUPERSEDES_EDGE != DELETION
```

## Scope boundary

These relation classes are AMOS structural semantics. Domain-specific logic may refine them, but may not silently collapse them into one edge type.

[[25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/INVALIDATION_RULES|INVALIDATION_RULES]] · [[25_COGNITIVE_MATRIX/07_COVERAGE/COVERAGE_MODEL|COVERAGE_MODEL]]
