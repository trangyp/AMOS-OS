---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-claim: bounded-validated
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Gap Registry
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
---

# GAP_REGISTRY — Executable bounded contract

**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_contract_runtime.py`

## Gap identity

Each registered structural gap contains:

```text
GapRecord = (
  GapSignal,
  state_version,
  lifecycle_state,
  resolution_evidence_id?,
  revalidation_receipt_id?
)
```

Lifecycle is deliberately monotonic:

```text
OPEN
  -> RESOLUTION_PROPOSED
  -> CLOSED
```

A gap cannot be silently overwritten, skipped directly from `OPEN` to `CLOSED`, reopened by mutating the same record, or closed against a different state version.

## Gap classes

The runtime preserves the existing typed gap classes:

- `SOURCE`
- `SEMANTICS`
- `IMPLEMENTATION`
- `VALIDATION`
- `AUTHORITY`
- `DEPENDENCY_CYCLE`
- `STALENESS`
- `CONTRADICTION`

Different gap classes require different evidence. A generic `fixed=true` flag has no closure semantics.

## Hard boundaries

```text
GAP_RECORDED != GAP_RESOLVED
RESOLUTION_PROPOSED != CLOSED
CLOSED != CANON_PROMOTED
MISSING_EVIDENCE != PASS
UNKNOWN/GAP != FALSE
```

Runtime bindings:
- `GapRecord`
- `GapRegistry`
- `GapState`

Validation: `test_cognitive_matrix_contract_runtime.py`.

______________________________________________________________________

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/08_STRUCTURAL_GAPS_MOC|08_STRUCTURAL_GAPS_MOC]]

RSCF-NODE
node_id: gap_registry_gaps_definition
node_type: EXECUTABLE_CONTRACT
claim_class: AMOS_MODEL
rscf_state: VALIDATED_BOUNDED
