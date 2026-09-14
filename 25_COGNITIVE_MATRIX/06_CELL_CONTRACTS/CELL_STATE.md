---
canon-group: cognition
canon-type: state_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_cell_runtime
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cell State
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
implementation_status: BOUNDED_EXECUTABLE_BINDING
---

# CELL_STATE — Typed Cognitive Matrix State Contract

**Origin architect / steward:** **Trang Phan**

## Purpose

A Cognitive Matrix cell is a typed state object, not a free-form note and not a scalar value detached from context.

Each cell binds:

```text
cell_id
primitive
field
context
time
scale
observer
regime
status
value_or_unknown
unit_or_none
provenance
source_version
evidence[]
dependencies[]
```

The coordinate axes are explicit before a value is populated.

## Cell statuses

```text
UNBOUND
SOURCE_CLAIM
AMOS_MODEL
DERIVED
VERIFIED_BOUNDED
COMPETING
FALSIFIED
STALE
QUARANTINED
```

These statuses are not a single confidence scale. They encode different epistemic/runtime states.

## Hard state rules

1. `UNBOUND` carries no fabricated value, provenance, or source version.
2. `UNBOUND != 0` and `UNKNOWN/GAP != false`.
3. Every bound cell carries recoverable provenance and a source/runtime version.
4. `VERIFIED_BOUNDED` requires a fresh execution or formal-proof receipt in the bounded reference runtime.
5. Active cells may not silently carry stale evidence.
6. A `STALE` cell preserves its previous value/evidence for lineage but loses active decision authority until revalidated.
7. `QUARANTINED` preserves evidence; it is not deletion.
8. Dependency failure invalidates/stales only dependent cells unless broader coupling is demonstrated.

## Tensor-coordinate rule

A cell coordinate currently uses:

```text
primitive x field x context x time x scale x observer x regime
```

Adding an axis requires a versioned schema change. Removing an axis may not erase a load-bearing distinction.

Axis position and meaning are non-interchangeable.

## Transform rule

A cell transform must declare at least:

```text
source_regime
target_regime
provenance_preservation
explicit_regime_mapping_if_changed
unknown_handling
```

The bounded validator rejects:

- provenance erasure;
- cross-regime transforms without an explicit mapping;
- unknown-to-zero conversion.

## Executable binding

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_cell_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_cognitive_matrix_cell_runtime.py`

Local reconstructed evidence on 2026-09-14: **12 passed / 0 failed** for the shared cell runtime suite.

## Hard boundaries

```text
CELL_ADDRESS != SEMANTIC_COMPLETENESS
UNBOUND != ZERO
VALUE != EVIDENCE
STATUS != AUTHORITY
TENSOR_REPRESENTATION != REPRESENTED_SYSTEM
STALE != FALSE
QUARANTINE != DELETE
TEST_PASS != CANON_PROMOTION
```

RSCF-NODE

```text
node_id: cell_state_contracts_definition
node_type: state_contract
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
```

**MOC:** [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/06_CELL_CONTRACTS_MOC|06_CELL_CONTRACTS_MOC]]
