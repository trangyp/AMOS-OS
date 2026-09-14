---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-claim: bounded-validated
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cell Status Registry
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
---

# CELL_STATUS_REGISTRY — Executable bounded contract

**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_contract_runtime.py`

## Status state

Cell status preserves two orthogonal coordinates:

```text
maturity ∈ {
  PLACEHOLDER,
  SOURCE_BOUND,
  CONTRACT_COMPLETE,
  IMPLEMENTED,
  VALIDATED_BOUNDED,
  AUTHORIZED_BOUNDED
}

condition ∈ {
  ACTIVE,
  STALE,
  COMPETING,
  QUARANTINED,
  FALSIFIED
}
```

A cell can therefore remain `IMPLEMENTED` while becoming `STALE`; staleness does not retroactively erase implementation evidence and does not imply falsity.

## Executable invariants

```text
STALE != FALSIFIED
QUARANTINED != DELETED
IMPLEMENTED != VALIDATED_BOUNDED
VALIDATED_BOUNDED != AUTHORIZED_BOUNDED
MATURITY != CONDITION
```

`project_cell_status` preserves cell identity and state version while projecting the two status axes without collapsing them into one scalar label.

Validation: `test_cognitive_matrix_contract_runtime.py`.

______________________________________________________________________

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[25_COGNITIVE_MATRIX/05_CELL_REGISTRY/05_CELL_REGISTRY_MOC|05_CELL_REGISTRY_MOC]]

RSCF-NODE
node_id: cell_status_registry_registry_definition
node_type: EXECUTABLE_CONTRACT
claim_class: AMOS_MODEL
rscf_state: VALIDATED_BOUNDED
