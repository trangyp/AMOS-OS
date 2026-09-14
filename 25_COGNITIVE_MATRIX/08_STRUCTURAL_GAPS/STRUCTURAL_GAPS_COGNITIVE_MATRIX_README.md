---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Structural Gaps Cognitive Matrix Readme
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
canonical_status: CONDITIONAL
---

# 08_STRUCTURAL_GAPS — Executable Gap Registry and Triage

## Purpose

Keep missing, insufficient, stale, competing, falsified, quarantined, cyclic, duplicate, and dependency-incomplete surfaces explicit until resolved by evidence.

## Runtime binding

`cognitive_matrix_coverage_runtime.py` emits typed `Gap` objects and deterministic priority ordering from declared scope and coverage records.

## Current guarantees in the bounded reference implementation

- no missing requirement is converted to PASS;
- no exception state is silently converted into an active promotion stage;
- duplicate records do not become independent confirmation;
- undeclared dependencies and cycles are surfaced;
- dependent requirements fail when a prerequisite fails;
- promotion requires cumulative structural receipts;
- structural priority is explicit and reproducible.

## Non-claims

```text
GAP_PRIORITY != ROOT_CAUSE
STRUCTURAL_FANOUT != CONSEQUENCE_MAGNITUDE
PROMOTABLE_RECORD != AUTHORIZED_EFFECT
LOCAL_TEST_PASS != DEPLOYMENT_VALIDATION
```

## Next use

Use the coverage/gap engine to scan the remaining generated Cognitive Matrix shells and select the highest decision-relevant upstream gaps for implementation, while preserving H/M/L externalities and control-plane authority.

[[25_COGNITIVE_MATRIX/08_STRUCTURAL_GAPS/GAP_REGISTRY|GAP_REGISTRY]] · [[25_COGNITIVE_MATRIX/07_COVERAGE/07_COVERAGE_MOC|07_COVERAGE_MOC]]
