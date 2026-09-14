---
title: AMOS Evaluator Calibration Verifier
type: tool
origin_architect: Trang Phan
tool_id: amos-evaluator-calibration
execution_tier: T1
status: IMPLEMENTED_LOCAL_REFERENCE
epistemic_class: AMOS_MODEL
---

# AMOS Evaluator Calibration Verifier

Local deterministic verifier for evaluator calibration and held-out reliability evidence.

## Capability mask

- `EVALUATOR_CALIBRATION_RECORD_VALIDATE`
- `HELD_OUT_VALIDATION_LINEAGE_AUDIT`
- `ABSTENTION_COVERAGE_AUDIT`
- `WILSON_INTERVAL_CALCULATE`
- `BRIER_SCORE_CALCULATE`
- `ECE_CALCULATE`
- `EVALUATOR_RELIABILITY_GATE`
- `EVALUATOR_DRIFT_COMPARE`
- `CALIBRATION_RECEIPT_VALIDATE`

## Tier boundary

T1 includes local parsing, SQLite evidence state, deterministic metric calculation, receipt validation, and drift comparison.

External model-judge execution, human-label collection platforms, hosted experiment backends, or networked evaluation services are separate T3 operations. This tool does not inherit their credentials or authority.

## Hard firewalls

- `CALIBRATED != CORRECT`
- `REFERENCE_LABEL != GROUND_TRUTH`
- `AGREEMENT != TRUTH`
- `SCORE != PROBABILITY`
- `CALIBRATION_COHORT != VALIDATION_COHORT`
- `LOW_ECE != DEPLOYMENT_VALIDITY`
- `RELIABILITY_GATE_PASS != DEPLOYMENT_AUTHORITY`
- `DRIFT_DELTA != CAUSAL_ATTRIBUTION`

## Evidence

Local executable evidence: `19_TESTS/test_evaluator_calibration_runtime.py` plus runtime/receipt self-tests and explicit mathematical recalculation fixtures.

External generalization, evaluator semantic validity, reference-label correctness, and deployment validity remain `UNKNOWN/GAP` unless independently established.
