---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Cognitive Matrix Structural Gaps Contract
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# COGNITIVE MATRIX STRUCTURAL GAPS CONTRACT

## 0. Status

`AMOS_MODEL / IMPLEMENTED_BOUNDED / LOCALLY_VALIDATED`

Structural gaps are now generated from an executable scoped-coverage model instead of being only generator-filled documentation shells.

## 1. Gap production

The coverage runtime emits typed gaps for:

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

Each gap carries requirement identity, criticality, required/current stage, downstream dependency fan-out, and diagnostic detail.

## 2. Completion interaction

- `FALSIFIED` can drive `CONTRADICTORY`.
- unresolved high-criticality cycle/duplicate/undeclared/stale/competing/quarantined state drives `UNKNOWN/GAP`.
- known high-criticality missing or insufficient stage drives `INCOMPLETE`.
- only explanatory/cosmetic gaps drive `CONDITIONAL`.
- zero gaps after dependency closure yields `COMPLETE_FOR_SCOPE`.

## 3. Priority

Structural triage is lexicographic by criticality, downstream dependency fan-out, blocker class, and stable ID. It deliberately avoids a pseudo-precise weighted scalar.

This local ordering is **not** causal root-cause proof and does not replace the AMOS Repair Priority Governor for consequential allocation.

## 4. Promotion

Gap closure claims are stage/receipt gated. `STALE`, `COMPETING`, `FALSIFIED`, and `QUARANTINED` cannot be erased by ordinary promotion; they require re-evidencing/reconciliation through the relevant governed path.

## 5. Firewalls

```text
GAP_REGISTERED != GAP_CLOSED
HIGH_FANOUT != ROOT_CAUSE
HIGH_PRIORITY != AUTHORITY_TO_REPAIR
LOCAL_PASS != SYSTEM_COMPLETE
COVERAGE_COMPLETE_FOR_SCOPE != CANONICAL
```

## 6. Executed evidence

Bounded local evidence is shared with the coverage runtime: 19 tests, 5,000 random topology differential checks, and 128 promotion-state checks with no observed failures in the tested domain.

## 7. Remaining gaps

Repository-scale automatic extraction of requirements from every Cognitive Matrix/OS surface is still open. Until that inventory is explicitly declared, completion claims remain scoped to supplied requirements only.

[[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/GAP_REGISTRY|GAP_REGISTRY]] · [[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/GAP_PRIORITY|GAP_PRIORITY]] · [[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/GAP_PROMOTION|GAP_PROMOTION]]
