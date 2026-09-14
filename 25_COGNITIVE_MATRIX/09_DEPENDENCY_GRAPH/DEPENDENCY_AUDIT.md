---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-claim: bounded-validated
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Dependency Audit
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
---

# DEPENDENCY_AUDIT — Executable bounded contract

**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_runtime.py` and `cognitive_matrix_contract_runtime.py`

## Graph contract

Edges are directed:

```text
dependency -> dependent
```

Load-bearing edge kinds are:

```text
HARD | EVIDENCE | AUTHORITY
```

`SOFT` edges do not propagate staleness and do not participate in the load-bearing DAG requirement.

The audit executes:

1. Tarjan strongly-connected-component decomposition over load-bearing edges.
2. Detection of any SCC with more than one node as a load-bearing dependency cycle.
3. Kahn topological ordering only when no load-bearing cycle exists.

Therefore:

```text
load_bearing_cycle_present -> no valid dependency topological order
```

This is a finite directed-graph result, not a causal or logical-entailment claim.

## Hard boundaries

```text
DEPENDENCY != CAUSATION
DEPENDENCY != LOGICAL_NECESSITY
SOFT_EDGE != STALENESS_PROPAGATION
CYCLE_DETECTED != COMPONENT_FALSE
TOPOLOGICAL_ORDER != PROOF_ORDER
```

Runtime bindings:
- `DependencyGraph.strongly_connected_components`
- `DependencyGraph.load_bearing_cycles`
- `DependencyGraph.topological_order`
- `audit_dependencies`

Validation: `test_cognitive_matrix_runtime.py` and `test_cognitive_matrix_contract_runtime.py`.

______________________________________________________________________

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[25_COGNITIVE_MATRIX/09_DEPENDENCY_GRAPH/09_DEPENDENCY_GRAPH_MOC|09_DEPENDENCY_GRAPH_MOC]]

RSCF-NODE
node_id: dependency_audit_graph_definition
node_type: EXECUTABLE_CONTRACT
claim_class: AMOS_MODEL
rscf_state: VALIDATED_BOUNDED
