---
title: 2026 08 22 UNCERTAINTY CALIBRATION GOVERNANCE
tags: [dated, dated/2026-08-22]
type: document
source: 11_KNOWLEDGE/dated
---



# Uncertainty & Calibration Governance (Gaps 217-221)

**Date**: 2026-08-22
**Cluster**: `uncertainty_calibration`
**Status**: CLOSED (11-layer chains complete)
**Tests**: 30 new tests (777 total)

## Overview

Implemented the Uncertainty & Calibration governance module for the AMOS OS Kernel, covering 5 gaps (217-221) across uncertainty decomposition, confidence propagation, correlated uncertainty detection, unknown-probability handling, and calibration drift monitoring.

## 5 Subsystems

| Gap | Subsystem | Class | Description |
|-----|-----------|-------|-------------|
| 217 | UncertaintyDecomposer | `UncertaintyDecomposer` | Aleatoric/epistemic/ontological/distributional decomposition |
| 218 | ConfidencePropagator | `ConfidencePropagator` | Confidence propagation (softmax, MC dropout, ensemble, Bayesian, conformal) |
| 219 | CorrelationHandler | `CorrelationHandler` | Correlated uncertainty detection and modeling |
| 220 | UnknownProbabilityHandler | `UnknownProbabilityHandler` | Unknown-probability handling (max entropy, imprecise, evidence, robust Bayes) |
| 221 | CalibrationDriftMonitor | `CalibrationDriftMonitor` | Calibration drift monitoring and recalibration triggering |

## Key Algorithms

- **Independence violated**: `|correlation_coefficient| > 0.3` or `|covariance| > 0.1`
- **Calibration drift detected**: `|observed_ece - expected_ece| > 0.05`
- **Recalibration needed**: `|drift| > 0.1`
- **High ontological uncertainty**: `ontological_uncertainty > 0.5`
- **Low confidence**: `confidence < 0.3`
- **Epistemic fraction**: `sum(epistemic) / sum(total)` across all decompositions

## Governor Gates

5 advisory post-execution gates (CONDITIONAL, not FAIL):

| Gate Name | Condition for CONDITIONAL |
|-----------|--------------------------|
| uncertainty-high-ontological | Ontological uncertainty > 0.5 |
| uncertainty-low-confidence | Confidence < 0.3 |
| uncertainty-independence-violated | Independence assumption violated |
| uncertainty-unknown-probability | Truly unknown queries exist |
| uncertainty-calibration-drift | Calibration drift detected |

## Files Modified

- `amos/governance/uncertainty_calibration.py` — 5 subsystems + governor (new, ~351 lines)
- `amos/state/store.py` — 5 store method pairs (fixed column count mismatches)
- `amos/kernel.py` — import + instantiation + evaluate_post wiring
- `amos/__init__.py` — exports for all 5 subsystems + governor
- `amos/governance/seed_completion.py` — moved uncertainty_calibration to CLOSED_CLUSTERS
- `tests/test_uncertainty_calibration.py` — 30 tests (new)
- `tests/test_completion.py` — updated counts (131 closed, 99 open)
- `AGENTS.md` — updated gate list, gap counts, test count

## Completion Graph State

- **131 closed gaps** (91-221) across 13 clusters
- **99 open gaps** (222-320) across 10 clusters
- **19 matrix gaps** (321-339)
- **777 total tests**

## Related

- 2026-08-22 Adversarial Robustness Governance
- 2026-08-22 Distributed Consensus Governance
- [[00_COSMO_BRAIN_MOC]]

#uncertainty-calibration #governance #gaps-217-221 #closed #amos-os-kernel

---
**MOC:** [[DATED_MOC]]
