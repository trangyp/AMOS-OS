---
title: SKILL
type: skill
name: amos-time-series-conformal-uq-rscf-engine
description: Time Series Conformal Uq — formal verification capability. Use when formal verification, symbolic execution, proof checking, or mathematical reasoning. Use when amos-formal-engines-master routes to this specialized capability.
parent_skill: amos-formal-engines-master
domain: formal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-time-series-conformal-uq-rscf-engine]
---


# Time Series Conformal Uq Rscf Engine

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-formal-engines-master`
- **Domain**: formal
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Formal reasoning engine for Time Series Conformal Uq Rscf Engine

## When to Use

- When verifying formal proofs against axioms and inference rules
- When checking soundness and completeness of formal systems
- When propagating constraints and detecting unsatisfiable cores
- When validating invariants under all operating conditions
- When the parent skill (`amos-formal-engines-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **time_series_eng.verify_proof**: Verify formal proofs against axioms, inference rules, and consistency constraints
- **time_series_eng.check_soundness**: Check soundness and completeness of formal systems under test
- **time_series_eng.propagate_constraints**: Propagate constraints through the formal system and detect unsatisfiable cores
- **time_series_eng.validate_invariant**: Validate invariants hold under all specified operating conditions
- **time_series_eng.detect_contradiction**: Detect contradictions and derive minimal conflict explanations
- **time_series_eng.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **time_series_eng.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **time_series_eng.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/math/AMOS_Signal_Processing_Kernel_v0_Math_Foundations.md` (content_hash: 3097ca6718b6eb60) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE.md` (content_hash: 7369abada641e374) (vault canon, SOURCE_CLAIM)

### Time Series Conformal UQ

From Signal Processing Kernel: Time series analysis with conformal prediction. From C02 Math & Compute: Uncertainty quantification.

**Conformal prediction model**:
- **Nonconformity score**: measures how nonconforming a new observation is to the calibration set
- **Calibration set**: a held-out set used to calibrate prediction intervals
- **Prediction interval**: an interval that contains the true value with declared probability
- **Exchangeability**: conformal prediction requires exchangeability of data points

**UQ protocol**:
1. **Train model**: train the prediction model on training data
2. **Calibrate**: calibrate prediction intervals on calibration set
3. **Predict**: predict with confidence intervals for new observations
4. **Validate**: validate that intervals achieve declared coverage
5. **Report**: report predictions with intervals and provenance

**RSCF laws**:
- `INTERVAL != CERTAINTY`: a prediction interval is not certainty; it is bounded uncertainty
- `COVERAGE != GUARANTEE`: declared coverage is a target, not a guarantee
- `EXCHANGEABILITY != IID`: exchangeability is weaker than IID; it allows non-IID data

### Epistemic Boundary

Time series conformal UQ is a statistical method. It does not prove intervals always achieve coverage, that exchangeability always holds, or that predictions are always correct.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for every derived claim.
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and epistemic class.
- **G5