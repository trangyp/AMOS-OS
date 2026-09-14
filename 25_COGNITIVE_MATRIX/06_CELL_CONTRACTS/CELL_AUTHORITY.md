---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cell Authority
created: 2026-08-22
updated: 2026-09-14
---

# CELL_AUTHORITY — Executable Authority Binding

**Origin architect / steward:** Trang Phan  
**Status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/matrix_registry_runtime.py`

## Authority witness

A bounded authority witness binds:

```text
witness_id
principal
scope[]
policy_hash
state_version
fresh
```

A cell may pass the bounded authority check only when:

1. its maturity is `AUTHORIZED_BOUNDED`;
2. it names an existing authority witness;
3. the witness is fresh;
4. required scope is explicitly granted;
5. policy hash matches exactly;
6. witness state version matches the cell state version.

## Invariants

```text
CAPABILITY != AUTHORITY
VALIDATED_BOUNDED != AUTHORIZED_BOUNDED
AUTHORITY_SCOPE_A != AUTHORITY_SCOPE_B
STALE_AUTHORITY != CURRENT_AUTHORITY
POLICY_HASH_MISMATCH -> REJECT
STATE_VERSION_MISMATCH -> REJECT
```

Evidence quality cannot manufacture authority. A routing or skill capability also cannot self-promote a cell into an authorized state.

## Boundary

`AUTHORIZED_BOUNDED` is an internal bounded runtime state. It is not by itself permission for an external durable/world effect; infrastructure commit-time authorization remains authoritative.

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]]
