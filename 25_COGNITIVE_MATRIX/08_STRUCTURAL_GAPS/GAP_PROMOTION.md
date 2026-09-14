---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-claim: bounded-validated
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Gap Promotion
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
---

# GAP_PROMOTION — Executable bounded contract

**Class:** `COGNITIVE_MATRIX_CONTRACT`  
**Status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_contract_runtime.py`

## Promotion contract

Gap closure is a two-gate process:

```text
OPEN
  -- kind-specific repair evidence -->
RESOLUTION_PROPOSED
  -- revalidation receipt + fresh dependencies -->
CLOSED
```

`propose_gap_resolution` requires the evidence identity, gap identity, and state version to match. It then applies a kind-specific evidence predicate.

| Gap kind | Required repair evidence |
|---|---|
| SOURCE | source resolved |
| SEMANTICS | semantics typed |
| IMPLEMENTATION | implementation receipt |
| VALIDATION | executed tests + adversarial tests |
| AUTHORITY | authority witness |
| DEPENDENCY_CYCLE | dependency audit passed |
| STALENESS | dependencies fresh |
| CONTRADICTION | contradiction resolved |

`close_gap` then requires a matching revalidation receipt, `revalidation_passed=true`, and `dependencies_fresh=true`.

## Hard invariants

```text
REPAIR_PROPOSAL != REVALIDATION
REVALIDATION != CANON_PROMOTION
TEST_PASS != AUTHORITY
STALE_DEPENDENCY -> CLOSURE_BLOCKED
STATE_VERSION_MISMATCH -> CLOSURE_BLOCKED
```

A gap cannot be closed by confidence, prose, recency, or a generic completion flag.

Runtime bindings:
- `GapResolutionEvidence`
- `propose_gap_resolution`
- `RevalidationReceipt`
- `close_gap`

Validation: `test_cognitive_matrix_contract_runtime.py`.

______________________________________________________________________

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/08_STRUCTURAL_GAPS_MOC|08_STRUCTURAL_GAPS_MOC]]

RSCF-NODE
node_id: gap_promotion_gaps_definition
node_type: EXECUTABLE_CONTRACT
claim_class: AMOS_MODEL
rscf_state: VALIDATED_BOUNDED
