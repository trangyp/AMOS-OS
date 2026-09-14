---
canon-group: cognition
canon-type: map_of_content
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_cell_runtime
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cognitive Matrix Cell Contracts MOC
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
implementation_status: PARTIAL_EXECUTABLE_BINDING
---

# 06 Cell Contracts — Map of Content

**Path:** `25_COGNITIVE_MATRIX/06_CELL_CONTRACTS`  
**Origin architect / steward:** **Trang Phan**

## Active cell contract

The shared Cognitive Matrix cell layer now has bounded executable validation for typed state, evidence ancestry, owner bindings, and safe tensor transforms.

```text
CellCoordinate
  primitive
  field
  context
  time
  scale
  observer
  regime

CellRecord
  cell_id
  coordinate
  status
  value_or_unknown
  unit
  provenance
  source_version
  evidence[]
  dependencies[]

CellBinding
  semantic_owner
  runtime_owner_or_none
  authority_owner_or_none
```

## Executable evidence

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_cell_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_cognitive_matrix_cell_runtime.py`
- Local reconstructed suite: **12 PASS / 0 FAIL**.
- GitHub CI receipt: `NOT_ATTACHED`.

## Files

- [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/CELL_STATE|CELL_STATE]] — typed coordinate/state/status contract.
- [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/CELL_EVIDENCE|CELL_EVIDENCE]] — evidence class, provenance-root, freshness, receipt boundary.
- [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/CELL_BINDINGS|CELL_BINDINGS]] — semantic/runtime/authority owner separation.
- [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/CELL_AUTHORITY|CELL_AUTHORITY]] — control-plane handoff; cell authority field is not commit authorization.
- [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/CELL_CONTRACTS_COGNITIVE_MATRIX_README|CELL_CONTRACTS_COGNITIVE_MATRIX_README]]
- [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/COGNITIVE_MATRIX_CELL_CONTRACTS_CONTRACT|COGNITIVE_MATRIX_CELL_CONTRACTS_CONTRACT]]

## Hard invariants

```text
UNBOUND != ZERO
VALUE != EVIDENCE
STATUS != AUTHORITY
RUNTIME_CAPABILITY != EFFECT_AUTHORITY
DISTINCT_FILES != INDEPENDENT_EVIDENCE
STALE != FALSE
QUARANTINE != DELETE
TENSOR_REPRESENTATION != REPRESENTED_SYSTEM
```

## Effect boundary

The cell layer may validate structure and name an authority owner. Durable/external effects remain subordinate to the AMOS infrastructure/control plane and its fresh authority, transaction, read-set, idempotency, release-ledger, and receipt checks.

```text
CELL_VALID != EFFECT_COMMITTABLE
EFFECT_COMMITTABLE != COMMITTED
```

**Parent:** [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]]
