---
canon-group: cognition
canon-type: evidence_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_cell_runtime
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cell Evidence
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
implementation_status: BOUNDED_EXECUTABLE_BINDING
---

# CELL_EVIDENCE — Cognitive Matrix Evidence Contract

**Origin architect / steward:** **Trang Phan**

## Evidence object

Every evidence item bound to a matrix cell carries:

```text
evidence_id
evidence_class
provenance
provenance_root
source_version
freshness_state
execution_receipt_flag
formal_proof_receipt_flag
```

Supported evidence classes in the bounded runtime:

```text
SOURCE
OBSERVATION
EXECUTION
FORMAL_PROOF
MODEL
DERIVED
```

Evidence class and cell status are different coordinates. A `SOURCE` item may support a `SOURCE_CLAIM`; it does not automatically create `VERIFIED_BOUNDED` state.

## Receipt rule

The bounded reference validator permits `VERIFIED_BOUNDED` only when at least one **fresh** bound evidence item carries an execution receipt or formal-proof receipt.

This is a minimum executable gate, not a complete proof policy. A receipt must still be scoped to the claim it supports.

## Provenance-root rule

Repeated files, summaries, agent outputs, mirrors, or generated descendants with the same provenance root count as one ancestry root for this cell-level check.

```text
DISTINCT_ARTIFACT_IDS != INDEPENDENT_EVIDENCE
DISTINCT_PROVENANCE_ROOTS != PROOF_OF_PHYSICAL_INDEPENDENCE
```

The bounded `COMPETING` state requires at least two provenance roots so a single source cannot manufacture a conflict with its own descendants. This does not prove the roots are fully independent; stronger provenance/Sybil controls remain upstream.

## Freshness rule

Active states other than `STALE`, `QUARANTINED`, and `UNBOUND` may not silently carry stale evidence in the bounded validator.

When a load-bearing evidence item becomes stale:

```text
stale parent -> stale dependent cell
```

unless a separate valid dependency path preserves the conclusion.

`STALE != FALSE`.

## Evidence promotion boundary

```text
SOURCE_PRESENCE != MATHEMATICAL_VERIFICATION
MODEL_OUTPUT != OBSERVATION
EXECUTION_RECEIPT != UNIVERSAL_PROOF
FORMAL_PROOF != EMPIRICAL_TRUTH
PROVENANCE_COUNT != CONFIDENCE_SUM
```

## Executable binding

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_cell_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_cognitive_matrix_cell_runtime.py`

Current local reconstructed shared-cell suite: **12 passed / 0 failed**.

## RSCF node

```text
node_id: cell_evidence_contracts_definition
node_type: evidence_contract
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
```

**MOC:** [[25_COGNITIVE_MATRIX/06_CELL_CONTRACTS/06_CELL_CONTRACTS_MOC|06_CELL_CONTRACTS_MOC]]
