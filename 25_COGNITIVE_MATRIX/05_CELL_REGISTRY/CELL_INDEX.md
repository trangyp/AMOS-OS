---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cell Index
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# CELL_INDEX — Typed Cognitive Matrix Registry Contract

## Status

`IMPLEMENTED_BOUNDED AT SHARED-CELL CONTRACT / REGISTRY PERSISTENCE STILL OPEN`

The earlier generated definition reduced a cell to `(L-primitive, O-operation, HML-scale)`. That is insufficient for the active typed runtime and can alias states that differ by context, time, observer, or regime.

## Cell coordinate

The shared executable cell contract uses

`CellCoordinate = (primitive, field, context, time_id, scale, observer, regime)`.

Each axis is explicit and non-empty. Axis identity is preserved; one axis cannot silently substitute for another.

A registry entry must preserve at least:
- `cell_id`;
- full typed coordinate;
- semantic owner;
- optional runtime owner;
- optional authority owner;
- cell status;
- provenance;
- source version;
- evidence references;
- dependency IDs.

## Ownership firewall

```text
SEMANTIC_OWNER != RUNTIME_OWNER != AUTHORITY_OWNER
RUNTIME_CAPABILITY != EFFECT_AUTHORITY
CELL_VALID != EFFECT_COMMITTABLE
```

## State firewall

```text
UNBOUND != ZERO
STALE != FALSE
COMPETING != RESOLVED
QUARANTINED != DELETED
VERIFIED_BOUNDED != CANONICAL
```

## Coverage binding

`CELL_INDEX` supplies addressable records to the coverage runtime. Merely registering a cell does not satisfy an implementation/validation/governance requirement. Coverage stage is evaluated separately.

## Remaining gap

A repository-wide persistent cell registry with collision detection, durable version identity, and commit-time authority binding is not yet established by the shared in-memory reference runtime.

[[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/06_CELL_CONTRACTS_MOC|06_CELL_CONTRACTS_MOC]] · [[25_COGNITIVE_MATRIX/07_COVERAGE/COVERAGE_MODEL|COVERAGE_MODEL]]
