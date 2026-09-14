---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-claim: bounded-validated
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Invalidation Rules
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
---

# INVALIDATION_RULES — Executable bounded contract

**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_runtime.py` and `cognitive_matrix_contract_runtime.py`

## Selective invalidation

For a directed dependency graph, invalidating a node changes only the state that depends on it through load-bearing edges.

Runtime rule:

```text
invalidated root:
  ACTIVE -> QUARANTINED

load-bearing descendants through
HARD | EVIDENCE | AUTHORITY:
  ACTIVE -> STALE

SOFT-only descendants:
  unchanged

unrelated nodes:
  unchanged
```

If the invalidated root is already `FALSIFIED` or `COMPETING`, that stronger epistemic condition is preserved rather than overwritten by quarantine.

## Hard invariants

```text
STALE != FALSE
INVALIDATED_ANCESTOR != ALL_DESCENDANTS_FALSE
SOFT_DEPENDENCY != LOAD_BEARING_DEPENDENCY
QUARANTINE != DELETE
UNRELATED_STATE -> PRESERVE
```

Invalidation is dependency-sensitive, not global. A source change therefore creates a bounded revalidation requirement over its dependent closure rather than erasing the entire matrix.

Runtime bindings:
- `DependencyKind.propagates_staleness`
- `DependencyGraph.descendants`
- `DependencyGraph.selective_invalidate`
- `audit_selective_invalidation`

Validation: `test_cognitive_matrix_runtime.py` and `test_cognitive_matrix_contract_runtime.py`.

______________________________________________________________________

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/09_DEPENDENCY_GRAPH_MOC|09_DEPENDENCY_GRAPH_MOC]]

RSCF-NODE
node_id: invalidation_rules_graph_definition
node_type: EXECUTABLE_CONTRACT
claim_class: AMOS_MODEL
rscf_state: VALIDATED_BOUNDED
