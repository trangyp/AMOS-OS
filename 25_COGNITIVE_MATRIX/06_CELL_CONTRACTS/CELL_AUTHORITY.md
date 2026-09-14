---
canon-group: cognition
canon-type: authority_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_infrastructure_control_plane
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cell Authority
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
implementation_status: BOUNDED_BINDING_ONLY
---

# CELL_AUTHORITY — Cognitive Matrix Authority Boundary

**Origin architect / steward:** **Trang Phan**

## Purpose

A Cognitive Matrix cell may name an authority owner, but the cell layer does not mint, refresh, or finalize authority.

The authoritative ordering remains:

```text
user/system authority
-> AMOS infrastructure/control plane
-> cognitive/runtime capability
-> matrix cell proposal/state
-> staged effect
-> commit-time authorization
-> effect release
```

## Cell-level authority binding

The bounded cell object carries only:

```text
authority_owner_or_none
```

This field answers: **which control-plane authority domain governs an effect involving this cell?**

It does not answer whether a particular effect is currently authorized.

## Hard separation

```text
CELL_VALUE != AUTHORIZATION
SEMANTIC_OWNER != AUTHORITY_OWNER
RUNTIME_OWNER != AUTHORITY_OWNER
AUTHORITY_OWNER != AUTHORITY_WITNESS
AUTHORITY_WITNESS != EFFECT_RELEASE_RECEIPT
CAPABILITY != AUTHORITY
```

A runtime can be capable of computing or transforming a cell while `effect_authority_bound = false`.

## Durable-effect handoff

If a cell-derived proposal can create a durable or external effect, hand off to the AMOS infrastructure/control plane.

The control plane, not the cell, owns current checks such as:

- task/intent binding;
- policy and constraint freshness;
- exact observed read set;
- semantic-transaction lineage;
- authority witness identity/scope/freshness;
- staged-effect digest;
- idempotency and release-ledger state;
- receiver receipt/reconciliation where applicable;
- rollback/finality policy.

The cell must carry enough provenance and dependency identity for those checks, but may not self-authorize them.

## Canon boundary

A cell may contain a canon candidate or a value derived from canon material. That does not authorize the cell to promote itself or mutate the canon boundary used to judge it.

Canon admission remains a separate governed process.

## Executable binding

`cognitive_matrix_cell_runtime.py` verifies only the structural distinction between runtime capability and an explicit authority-owner binding.

Current shared-cell suite: **12 passed / 0 failed**.

No claim is made that the cell runtime itself implements the infrastructure commit guard.

## Hard boundaries

```text
BOUND_AUTHORITY_OWNER != CURRENT_AUTHORIZATION
COMPUTATION_SUCCESS != COMMIT_PERMISSION
LOCAL_CELL_VALIDITY != SYSTEM_EFFECT_VALIDITY
COMMITTABLE != COMMITTED
```

RSCF-NODE

```text
node_id: cell_authority_contracts_definition
node_type: authority_contract
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
```

**MOC:** [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/06_CELL_CONTRACTS_MOC|06_CELL_CONTRACTS_MOC]]
