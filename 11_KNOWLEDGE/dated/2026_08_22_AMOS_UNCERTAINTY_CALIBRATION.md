---
title: "AMOS Uncertainty & Calibration"
created: "2026-08-22"
type: note
source: 11_KNOWLEDGE/dated
tags: [canon-group/human-system, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-uncertainty-calibration, dated, dated/2026-08-22]
status: "living"
provenance: "MODEL"
confidence: "VERIFIED"
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS Uncertainty & Calibration (Gaps 217-221)

> Epistemic class: MODEL (code artifact + test verification).
> Related: 2026-08-22 AMOS Adversarial Robustness · 2026-08-22 Distributed Consensus Governance · amos-completion-graph-workflow

## Summary

Closed gaps 217-221 by implementing the **Uncertainty & Calibration**
governance module (`amos/governance/uncertainty_calibration.py`). This is the 14th
governance gate in `AmosKernel.run()`, evaluated post-execution as an advisory gate.

## 5 Subsystems

| Gap | Subsystem | Class | Purpose |
|-----|-----------|-------|---------|
| 217 | Uncertainty decomposition | `UncertaintyDecomposer` | Aleatoric/epistemic/ontological decomposition |
| 218 | Confidence propagation | `ConfidencePropagator` | Confidence propagation math (softmax, MC dropout, ensemble, Bayesian, conformal) |
| 219 | Correlated uncertainty | `CorrelationHandler` | Correlated uncertainty detection + independence checking |
| 220 | Unknown probability | `UnknownProbabilityHandler` | Unknown-probability handling (max entropy, imprecise, evidence, robust Bayes, ignorance) |
| 221 | Calibration drift | `CalibrationDriftMonitor` | Calibration drift monitoring + recalibration triggers |

## Gate Evaluation

`UncertaintyCalibrationGovernor.evaluate_post()` returns 5 gate results:
- `uncertainty-high-ontological` — CONDITIONAL if ontological uncertainty > 0.5
- `uncertainty-low-confidence` — CONDITIONAL if confidence < 0.3
- `uncertainty-independence-violated` — CONDITIONAL if independence assumption violated
- `uncertainty-unknown-probability` — CONDITIONAL if queries flagged as truly unknown
- `uncertainty-calibration-drift` — CONDITIONAL if calibration drift detected

## Key Semantics

1. **Uncertainty decomposition**: total = aleatoric + epistemic + ontological (not enforced, just tracked)
2. **Independence violation**: `abs(correlation_coefficient) > 0.3 OR abs(covariance) > 0.1`
3. **Calibration drift detected**: `abs(observed_ece - expected_ece) > 0.05`
4. **Recalibration needed**: `abs(observed_ece - expected_ece) > 0.1`
5. **Epistemic fraction**: `sum(epistemic) / sum(total)` across all decompositions for a model
6. **Average confidence**: `sum(confidence) / count` across all propagations for a model

## Implementation Chain

- **Types**: `amos/core/types.py` — 5 dataclasses + 5 enums
- **Schema**: `amos/state/store.py` — 5 tables + 5 put/list method pairs
- **Module**: `amos/governance/uncertainty_calibration.py` — 5 subsystems + governor
- **Kernel**: `amos/kernel.py` — import, instantiation, gate evaluation
- **Exports**: `amos/__init__.py` — all types + `UncertaintyCalibrationGovernor`
- **Tests**: `tests/test_uncertainty.py` — 30 tests
- **Seeder**: `amos/governance/seed_completion.py` — gaps 217-221 in CLOSED_CLUSTERS

## Completion Graph Impact

- **Closed gaps**: 126 → 131 (gaps 217-221 = 5 gaps closed)
- **Open gaps**: 104 → 99
- **Total tests**: 717 → 777 (60 new tests)
- **All 777 tests pass**

## Files Modified

- `amos/core/types.py` — 5 new dataclasses + 5 new enums
- `amos/state/store.py` — 5 new tables + 5 store method pairs
- `amos/governance/uncertainty_calibration.py` — full governance module (user created)
- `amos/kernel.py` — kernel wiring (user added)
- `amos/__init__.py` — exports (user added)
- `amos/governance/seed_completion.py` — moved to CLOSED_CLUSTERS
- `tests/test_uncertainty.py` — 30 new tests
- `tests/test_completion.py` — updated counts (126→131, 104→99)

## Lessons Learned

1. **Redundant file pattern**: The user consistently pre-creates governance modules.
   Always check for existing files before creating new ones. Remove redundant files immediately.
2. **Independence violation threshold**: Uses OR logic — either correlation OR covariance
   can trigger violation, not just correlation alone.
3. **Calibration drift thresholds**: Two-tier — 0.05 for drift_detected, 0.1 for
   recalibration_needed. Tests must distinguish between these.
4. **Governor attribute names**: The user uses descriptive names like
   `uncertainty_decomposer`, `confidence_propagator`, `correlation_handler`,
   `unknown_probability`, `calibration_drust` (not abbreviated).

---
**Links:** [[DATED_MOC]] | [[KNOWLEDGE_MOC]]
