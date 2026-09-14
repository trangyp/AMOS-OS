---
canon-group: cognition
canon-type: binding_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_cell_runtime
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cell Bindings
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
implementation_status: BOUNDED_EXECUTABLE_BINDING
---

# CELL_BINDINGS — Cognitive Matrix Binding Contract

**Origin architect / steward:** **Trang Phan**

## Purpose

A cell binding declares who or what owns the cell's semantics, executable capability, and effect authority. These are separate bindings.

```text
CellBinding
  cell_id
  semantic_owner
  runtime_owner_or_none
  authority_owner_or_none
```

## Owner separation

### Semantic owner

Defines the meaning/schema of the cell within its declared scope. Semantic ownership does not imply executable implementation.

### Runtime owner

Names the runtime component capable of evaluating or transforming the cell. Runtime capability does not imply authority to create external or durable effects.

### Authority owner

Names the control-plane authority domain that may participate in authorizing an effect involving the cell. Presence of this field is still not a commit token or authority witness.

## Hard binding rules

1. Every cell has exactly one explicit `cell_id` and semantic owner in this bounded contract.
2. Runtime ownership is optional; unimplemented cells may remain semantic-only.
3. Authority ownership is optional for non-effect-bearing cells.
4. `runtime_owner != authority_owner` unless an independently governed architecture explicitly binds both roles.
5. A runtime owner cannot infer effect authority from its ability to compute a value.
6. A semantic owner cannot promote itself to Canon solely by owning a schema.
7. A cell binding may not erase coordinate axes, provenance, source version, or status.
8. Rebinding any owner is a versioned state change and may stale dependent cached decisions.

## Durable-effect boundary

The cell layer validates state/binding structure only.

Any durable or external effect must route to the AMOS infrastructure/control plane for current authority, constraint, observed-read-set, transaction, idempotency, and release-state checks.

```text
CELL_AUTHORITY_OWNER
!= AUTHORITY_WITNESS
!= COMMIT_AUTHORIZATION
!= EFFECT_RELEASE
```

## Executable binding

`cognitive_matrix_cell_runtime.py` tests that runtime capability and effect-authority binding remain separate.

Current bounded suite: **12 passed / 0 failed** across shared cell-state/binding/evidence/transform behavior.

## Hard boundaries

```text
SEMANTIC_OWNER != IMPLEMENTATION_PROOF
RUNTIME_OWNER != EFFECT_AUTHORITY
AUTHORITY_OWNER_FIELD != FRESH_AUTHORITY_WITNESS
CAPABILITY != AUTHORITY
CELL_BINDING != CANON_PROMOTION
```

RSCF-NODE

```text
node_id: cell_bindings_contracts_definition
node_type: binding_contract
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
```

**MOC:** [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/06_CELL_CONTRACTS_MOC|06_CELL_CONTRACTS_MOC]]
