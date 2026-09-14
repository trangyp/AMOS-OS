---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Gap Priority
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# GAP_PRIORITY — Deterministic Structural Triage

## Status

`IMPLEMENTED_BOUNDED / LOCALLY_VALIDATED`

The coverage runtime intentionally avoids an opaque weighted scalar score. Gaps are ordered lexicographically by:
1. criticality;
2. downstream dependency fan-out;
3. blocker class;
4. stable requirement ID tie-break.

Criticality order:

`CRITICAL > DECISION_RELEVANT > EXPLANATORY > COSMETIC`.

For dependency-closure matrix `C`, downstream fan-out of requirement `r_j` is

`fanout(r_j) = sum_{i != j} C[i,j]`.

This counts how many declared requirements transitively depend on `r_j`. It is a topology measure only; it is **not** causal impact, business value, harm magnitude, urgency, or empirical repair benefit.

## Repair-governor boundary

Structural triage selects high-leverage candidates for investigation. A consequential repair decision still requires H/M/L target analysis, causal uncertainty, reversibility, repair externalities, authority, and rollback checks.

```text
HIGH_FANOUT != ROOT_CAUSE
HIGH_PRIORITY != AUTHORITY_TO_REPAIR
STRUCTURAL_ORDER != EMPIRICAL_UTILITY_SCORE
```

[[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/GAP_REGISTRY|GAP_REGISTRY]]
