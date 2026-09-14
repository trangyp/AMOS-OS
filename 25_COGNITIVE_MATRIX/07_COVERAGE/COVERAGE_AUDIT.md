---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Coverage Audit
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# COVERAGE_AUDIT — Executable Audit Contract

## Status

`IMPLEMENTED_BOUNDED / LOCALLY_VALIDATED`

Executor: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/cognitive_matrix_coverage_runtime.py`

## Audit procedure

For a declared `CoverageScope`:
1. require unique requirement IDs;
2. require every dependency to be declared inside the scope;
3. construct directed adjacency and Boolean transitive-closure matrices;
4. surface cycle nodes instead of assuming recursive closure;
5. resolve exactly one coverage record per requirement;
6. validate provenance/source version and stage-specific receipts;
7. reject exception states as active-stage evidence;
8. compare active stage against the requirement-specific threshold;
9. propagate dependency failure to dependent requirements;
10. classify the scope as `COMPLETE_FOR_SCOPE`, `CONDITIONAL`, `INCOMPLETE`, `CONTRADICTORY`, or `UNKNOWN/GAP`;
11. return explicit gaps ordered deterministically for triage.

## Receipt rules

```text
IMPLEMENTED_BOUNDED -> implementation_receipt
VALIDATED_BOUNDED   -> implementation_receipt + validation_receipt
GOVERNED_BOUNDED    -> implementation_receipt + validation_receipt + governance_receipt
```

`UNBOUND` may not carry fabricated provenance or promotion receipts.

## Audit firewalls

```text
DUPLICATE_RECORD != INDEPENDENT_EVIDENCE
STALE != FALSE
QUARANTINED != DELETED
COMPETING != RESOLVED
LOCAL_TEST_PASS != CI_PASS
DEPENDENCY_EDGE != CAUSAL_EDGE
```

## Current executable evidence

2026-09-14 local run:
- pytest: 19 passed / 0 failed;
- random topology differential check: 5,000 graphs / 0 observed mismatches;
- promotion-state enumeration: 128 combinations / 0 observed invalid admissions.

The audit implementation does not authorize durable effects and does not promote Canon.

[[25_COGNITIVE_MATRIX/07_COVERAGE/COVERAGE_MODEL|COVERAGE_MODEL]] · [[25_COGNITIVE_MATRIX/07_COVERAGE/COVERAGE_THRESHOLDS|COVERAGE_THRESHOLDS]]
