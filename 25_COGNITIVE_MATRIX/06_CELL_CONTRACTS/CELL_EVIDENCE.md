---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cell Evidence
created: 2026-08-22
updated: 2026-09-14
---

# CELL_EVIDENCE — Executable Evidence Contract

**Origin architect / steward:** Trang Phan  
**Status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/matrix_registry_runtime.py`

## Typed evidence classes

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
AMOS_MODEL
EXECUTED_TEST
FORMAL_PROOF
```

Every evidence reference binds:

```text
evidence_id
evidence_class
source_id
state_version
fresh
```

## Validation rule

For every evidence ID attached to a cell, the executable validator requires that the evidence exists, is fresh, and binds the cell's exact `state_version`.

Failure states are explicit:

```text
MISSING:<evidence_id>
STATE_VERSION_MISMATCH:<evidence_id>
STALE:<evidence_id>
```

## Invariants

```text
SOURCE_CLAIM != VERIFIED
EXECUTED_TEST != FORMAL_PROOF
EVIDENCE_FOR_VERSION_v1 != EVIDENCE_FOR_VERSION_v2
STALE_EVIDENCE != CURRENT_EVIDENCE
MISSING_EVIDENCE != PASS
```

The runtime preserves evidence type rather than collapsing all supporting material into a single confidence score.

## Validation evidence

The bounded test suite executes both positive and stale-evidence cases. Passing tests validate this evidence-binding mechanism only, not the truth of arbitrary domain claims carried by a cell.

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]]
