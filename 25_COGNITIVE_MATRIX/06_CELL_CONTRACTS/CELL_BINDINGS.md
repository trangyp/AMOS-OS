---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-claim: bounded-validated
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cell Bindings
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
---

# CELL_BINDINGS — Executable bounded contract

**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_contract_runtime.py`

## Scope

A cell binding joins one cell identity and state version to the source, evidence, authority, and dependency identities that are allowed to support that exact state.

```text
CellBinding = (
  cell_id,
  state_version,
  source_ids,
  evidence_ids,
  authority_witness_id?,
  dependency_ids
)
```

The binding is an AMOS_MODEL runtime contract. It is not Canon promotion and does not itself authorize an effect.

## Executable invariants

1. `cell_id` and `state_version` are non-empty.
2. Source, evidence, and dependency identifiers are unique within a binding.
3. A cell cannot depend on itself.
4. Re-registering the same cell ID with a different binding fails closed.
5. A binding validates against a `MatrixCellRecord` only when the cell identity, state version, source IDs, evidence IDs, and authority-witness identity match exactly.
6. A capability/evidence binding never mints authority.

```text
BINDING_MATCH != AUTHORIZATION
SOURCE_BOUND != VERIFIED
EVIDENCE_PRESENT != EVIDENCE_FRESH
CAPABILITY != AUTHORITY
```

## Runtime binding

- `CellBinding`
- `CellBindingRegistry.register`
- `CellBindingRegistry.validate_against_cell`

Validation: `test_cognitive_matrix_contract_runtime.py`.

______________________________________________________________________

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/06_CELL_CONTRACTS_MOC|06_CELL_CONTRACTS_MOC]]

RSCF-NODE
node_id: cell_bindings_contracts_definition
node_type: EXECUTABLE_CONTRACT
claim_class: AMOS_MODEL
rscf_state: VALIDATED_BOUNDED
