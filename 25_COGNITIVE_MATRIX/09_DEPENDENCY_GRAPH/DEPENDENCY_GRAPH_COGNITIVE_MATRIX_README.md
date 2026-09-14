---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Dependency Graph Cognitive Matrix Readme
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# 09_DEPENDENCY_GRAPH — Typed Relations and Selective Invalidation

## Purpose

Represent which AMOS objects depend on, support, contradict, supersede, observe, invalidate, condition, correlate with, or provide alternatives to other objects without collapsing these relations into one generic edge.

## Current executable surface

`cognitive_matrix_dependency_runtime.py` implements:
- typed node and edge identity;
- eleven relation classes;
- load-bearing dependency filtering;
- directed adjacency and transitive closure;
- cycle detection;
- contradiction/supersession/invalidation-proposal extraction;
- direct dependency export to the coverage runtime;
- selective stale propagation;
- review-only handling for support/sufficiency loss;
- unrelated-state preservation.

## Hard boundaries

```text
RELATION != CAUSATION
DEPENDENCY != SUPPORT
SUPPORT != PROOF
CONTRADICTION != TRUTH_SELECTION
INVALIDATION_PROPOSAL != COMMIT
STALE != FALSE
```

## Verification

Local 2026-09-14 evidence:
- 22/22 dependency + integration tests;
- 5,000 stress DAGs;
- 29,949 closure-node checks;
- 5,000 selective-invalidation checks;
- 0 observed stress mismatches.

No CI receipt is attached.

## Dependency position

- Cell registry supplies addressable nodes/state.
- Dependency graph supplies typed load-bearing and non-load-bearing relations.
- Coverage consumes only exported load-bearing prerequisites.
- Structural gaps use dependency fan-out for local triage.
- Control plane remains the authority owner for durable invalidation/supersession effects.

[[25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/09_DEPENDENCY_GRAPH_MOC|09_DEPENDENCY_GRAPH_MOC]] · [[25_COGNITIVE_MATRIX/07_COVERAGE/07_COVERAGE_MOC|07_COVERAGE_MOC]]
