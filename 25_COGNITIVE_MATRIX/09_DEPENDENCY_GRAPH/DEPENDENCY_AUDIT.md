---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Dependency Audit
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# DEPENDENCY_AUDIT — Executable Dependency Graph Audit

## Status

`IMPLEMENTED_BOUNDED / LOCALLY_VALIDATED`

Executor: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_dependency_runtime.py`.

## Audit procedure

1. require unique node IDs;
2. require unique edge IDs;
3. require every active edge endpoint to resolve to a declared node;
4. preserve the typed relation instead of flattening edges;
5. build load-bearing adjacency only from `NECESSARY`, `DERIVED_FROM`, and `CONDITIONED_ON`;
6. compute Boolean transitive closure;
7. surface load-bearing cycles as `UNKNOWN/GAP` unless fixed-point semantics are separately declared;
8. extract contradiction pairs without selecting a winner;
9. extract `INVALIDATES` and `SUPERSEDES` relations as proposals, not committed effects;
10. export direct load-bearing dependency maps for the coverage engine;
11. on invalidation, stale only transitive dependents and preserve unrelated state.

## Graph status

```text
VALID_BOUNDED
INVALID
UNKNOWN/GAP
```

`INVALID` is used for malformed graph identity/endpoints. `UNKNOWN/GAP` is used for a structurally known graph whose cyclic load-bearing semantics are unresolved.

## Executed evidence — 2026-09-14

Local bounded runs:
- dependency unit suite: 19 pass / 0 fail;
- dependency-to-coverage integration: 3 pass / 0 fail;
- combined dependency repair suite: 22 pass / 0 fail;
- seeded DAG stress: 5,000 graphs;
- closure checks: 29,949 node-level comparisons against independent DFS reachability;
- selective invalidation checks: 5,000 comparisons against independently constructed reverse reachability;
- observed stress mismatches: 0.

No GitHub Actions receipt is attached to this repair.

## Non-claims

```text
22 LOCAL PASS != SYSTEM-WIDE CORRECTNESS
DEPENDENCY_GRAPH != CAUSAL_GRAPH
INVALIDATION_PROPOSAL != AUTHORIZED_EFFECT
ACYCLIC_GRAPH != EMPIRICAL_TRUTH
```

[[25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/COGNITIVE_MATRIX_DEPENDENCY_GRAPH_CONTRACT|COGNITIVE_MATRIX_DEPENDENCY_GRAPH_CONTRACT]]
