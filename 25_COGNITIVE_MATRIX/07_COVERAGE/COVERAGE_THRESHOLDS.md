---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Coverage Thresholds
created: 2026-08-22
updated: 2026-09-14
---

# COVERAGE_THRESHOLDS — Executable Threshold Contract

**Origin architect / steward:** Trang Phan  
**Status:** `IMPLEMENTED_BOUNDED / VALIDATED_BOUNDED`  
**Runtime:** `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/matrix_registry_runtime.py`

## Dimensions

Coverage thresholds are defined independently for:

```text
source
contract
implementation
validation
authority
```

Each threshold is a finite real value in `[0,1]`. Address coverage is measured but is not used as a substitute for the other dimensions.

Default strict thresholds are `1.0` for all five decision dimensions. A caller may explicitly use lower thresholds for a bounded task, but the selected thresholds must travel with the resulting audit claim.

## Invariants

```text
0 <= threshold_d <= 1
ADDRESS_COVERAGE != IMPLEMENTATION_COVERAGE
IMPLEMENTATION_COVERAGE != VALIDATION_COVERAGE
VALIDATION_COVERAGE != AUTHORITY_COVERAGE
CUSTOM_THRESHOLD != UNIVERSAL_COMPLETENESS_STANDARD
```

A threshold outside `[0,1]` is rejected by the runtime.

## Boundary

Threshold selection is an AMOS decision model, not an empirical law. Passing a bounded threshold does not imply that the full AMOS OS is complete.

[[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]]
