---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Coverage Thresholds
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# COVERAGE_THRESHOLDS — Requirement-Level Gates

## Status

`IMPLEMENTED_BOUNDED / LOCALLY_VALIDATED`

AMOS does not use a global file-count percentage as a completion threshold. Every declared requirement carries its own minimum active stage.

## Active stage ordering

For the active chain only:

`CONTRACT_ONLY < IMPLEMENTED_BOUNDED < VALIDATED_BOUNDED < GOVERNED_BOUNDED`.

Equivalent rank function:

`rho : S_active -> {1,2,3,4}`

with the order above.

A record can satisfy requirement `r` only when

`rho(current(r)) >= rho(required(r))`

and its receipt/provenance gates pass.

## Exception states

`UNBOUND`, `STALE`, `COMPETING`, `FALSIFIED`, and `QUARANTINED` are not assigned promotion ranks. Treating any of them as numeric zero or as an automatically lower active stage is forbidden.

## Completion threshold

`COMPLETE_FOR_SCOPE` requires every declared requirement and its transitive dependency closure to satisfy its own threshold. No average may compensate for one failed critical requirement.

```text
99% FILE PRESENCE + 1 MISSING CRITICAL AUTHORITY GATE
!= COMPLETE_FOR_SCOPE
```

## Promotion receipts

- implementation threshold -> implementation receipt;
- validation threshold -> implementation + validation receipts;
- governance threshold -> implementation + validation + governance receipts.

The receipt booleans in the reference runtime are bounded structural witnesses only. Production authority must bind stronger receipt identity, freshness, provenance, and control-plane semantics.

[[25_COGNITIVE_MATRIX/07_COVERAGE/COVERAGE_MODEL|COVERAGE_MODEL]]
