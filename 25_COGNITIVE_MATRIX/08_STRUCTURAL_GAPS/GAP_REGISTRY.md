---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Gap Registry
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# GAP_REGISTRY — Executable Structural Gap Schema

## Status

`IMPLEMENTED_BOUNDED / LOCALLY_VALIDATED`

Gap records are emitted by `cognitive_matrix_coverage_runtime.py` from declared scope requirements and observed coverage records.

## Gap object

Each gap preserves:
- requirement ID;
- reason;
- criticality;
- required stage;
- current stage when known;
- downstream dependency fan-out;
- diagnostic detail.

Current reasons:

```text
MISSING
BELOW_REQUIRED_STAGE
DEPENDENCY_GAP
UNDECLARED_DEPENDENCY
INVALID_RECORD
DUPLICATE_RECORD
CYCLE
STALE
COMPETING
FALSIFIED
QUARANTINED
UNBOUND
```

## Semantics

- `MISSING`: no record exists for a declared requirement.
- `BELOW_REQUIRED_STAGE`: record is valid but the active stage is insufficient.
- `DEPENDENCY_GAP`: the requirement's own gate passes but a declared prerequisite does not.
- `UNDECLARED_DEPENDENCY`: the declared scope is not dependency-closed.
- `INVALID_RECORD`: provenance/version/receipt structure is malformed.
- `DUPLICATE_RECORD`: multiple unresolved records bind the same requirement; duplicates are not treated as independent evidence.
- `CYCLE`: dependency closure contains a directed cycle and no explicit fixed-point/bootstrapping semantics are declared.
- exception states retain their literal semantics; they are not collapsed into false/zero.

## Boundary

`GAP_REGISTERED != GAP_CLOSED`.

The registry is structural. It does not prove the causal root of a failure and does not replace the higher-order AMOS Repair Priority Governor for consequential repair allocation.

[[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/GAP_PRIORITY|GAP_PRIORITY]] · [[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/GAP_PROMOTION|GAP_PROMOTION]]
