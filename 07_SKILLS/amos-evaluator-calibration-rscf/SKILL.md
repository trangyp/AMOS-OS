---
name: amos-evaluator-calibration-rscf
description: Calibrate, validate, audit, and compare evaluator or LLM-as-judge reliability using held-out reference cohorts, abstention-aware confusion evidence, probability calibration metrics, uncertainty intervals, evaluator drift checks, and explicit non-authority boundaries. Use when AMOS must decide whether an evaluator threshold or judge is reliable enough for a declared evaluation policy without promoting agreement, confidence, human labels, calibration scores, or benchmark results into truth or deployment authority.
---

# AMOS Evaluator Calibration RSCF

Origin architect/steward: **Trang Phan**.

Parent capability: `amos-interactive-evaluation-design-rscf`.

This Skill owns evaluator reliability evidence, not evaluation-run orchestration. The parent Skill continues to own run identity, task/process/outcome evidence, reviews, judge disagreement, baseline/candidate comparison, and harness mutation verdicts.

## Epistemic boundary

External repositories provide `SOURCE_CLAIM` mechanisms. The deterministic runtime and its tests provide bounded `EXECUTED_TESTED_SCOPE` evidence only for the implemented local contracts. No score, label source, calibration statistic, or gate establishes ground truth, causal correctness, deployment validity, or authority.

Hard invariants:

- `CALIBRATED != CORRECT`
- `REFERENCE_LABEL != GROUND_TRUTH`
- `HUMAN_LABEL != INFALLIBLE`
- `AGREEMENT != TRUTH`
- `SCORE != PROBABILITY` unless probability semantics are declared and domain-checked.
- `CALIBRATION_COHORT != VALIDATION_COHORT`
- `THRESHOLD_TUNED_ON_COHORT != HELD_OUT_VALIDATION_ON_SAME_COHORT`
- `LOW_BRIER_OR_ECE != SEMANTIC_CORRECTNESS`
- `NARROW_CONFIDENCE_INTERVAL != REPRESENTATIVE_SAMPLE`
- `RELIABILITY_GATE_PASS != DEPLOYMENT_VALIDITY`
- `CALIBRATION_EVIDENCE != AUTHORITY`

## Runtime

Apply:

`BIND EVALUATOR -> BIND REFERENCE -> CALIBRATION COHORT -> FREEZE THRESHOLD/CONFIG -> HELD-OUT VALIDATION -> UNCERTAINTY/CALIBRATION METRICS -> POLICY GATE -> DRIFT CHECK -> RSCF`

1. Bind evaluator identity, version, kind, configuration hash, score semantics, threshold value/source, and expected cohort size.
2. Bind reference-source identity/version/kind and independence status. Never call the reference source ground truth unless separately established.
3. Use `CALIBRATION` only for threshold/config selection evidence.
4. Seal calibration evidence before creating a `VALIDATION` session.
5. Require the validation cohort hash to differ from the calibration cohort hash. Freeze evaluator identity/configuration and threshold lineage from calibration.
6. Record each reference label, evaluator label, optional score, and evidence reference. Preserve `ABSTAIN` separately from wrong answers.
7. Compute confusion evidence and uncertainty only on defined denominators. Do not hide missing observations or abstentions.
8. Compute Brier score/ECE only when `score_semantics=PROBABILITY_PASS` and every probability used lies in `[0,1]`.
9. Evaluate reliability only against an explicit caller policy. Do not invent universal pass thresholds.
10. Compare evaluator versions/configurations for drift only when cohort, reference source, threshold semantics, and observed task set are compatible.
11. Return provenance, scope, missingness, falsifiers, and authority/deployment ceilings.

## Deterministic surfaces

- `scripts/evaluator_calibration.py`: local SQLite calibration/validation runtime.
- `scripts/calibration_contract_check.py`: compact receipt validator.
- Repository regression suite: `19_TESTS/test_evaluator_calibration_runtime.py`.

Run both self-tests and the repository regression suite after changing runtime semantics.

## Mathematical contract

Read `references/equations.md` before changing formulas or interpreting calibration statistics.

The implemented mathematics includes:

- binary confusion counts;
- abstention/classification coverage;
- selective accuracy;
- Wilson score interval for a binomial proportion;
- Brier score for declared binary probabilities;
- fixed-bin expected calibration error (ECE);
- bounded metric deltas for comparable evaluator-drift sessions.

These are established mathematical/statistical constructions where noted in the reference, but their **application** remains assumption- and cohort-bound. A correct formula does not establish representative data or trustworthy labels.

## Reliability gate

A gate accepts only explicit policy terms such as:

- minimum observed coverage;
- minimum classification coverage;
- minimum selective accuracy;
- minimum lower Wilson bound;
- maximum abstention rate;
- maximum Brier score;
- maximum ECE;
- probability completeness requirement;
- independent-reference requirement.

Possible gate states:

`PASS | FAIL | INCONCLUSIVE`

Missing required evidence is `INCONCLUSIVE`, not an inferred PASS.

A `CALIBRATION` session cannot receive a held-out reliability PASS. Reliability gates require a sealed `VALIDATION` session.

## Drift comparison

Allow evaluator version/configuration to be the mutation axis, but freeze:

- evaluator identity;
- validation cohort and expected count;
- reference identity/version/kind/independence;
- score semantics;
- threshold value/source;
- observed task set.

Return `COMPARABLE` or `NOT_COMPARABLE` before computing deltas.

`EVALUATOR_DRIFT_DELTA != CAUSAL_ATTRIBUTION`.

## Source mechanisms

Read `references/upstream-mechanisms.md` for pinned GitHub sources. Key adopted patterns include:

- statistical uncertainty around evaluation metrics;
- multiple-run/epoch awareness;
- explicit metric thresholds;
- dataset/experiment identity;
- judge alignment against human/reference targets followed by re-evaluation.

Do not inherit source-project authority or superiority claims.

## Failure behavior

- Missing evaluator/reference/cohort identity -> reject or `UNKNOWN/GAP`.
- Validation reuses calibration cohort -> reject.
- Validation changes frozen evaluator/threshold identity -> reject.
- Probability score outside `[0,1]` -> reject.
- Score semantics not probabilistic -> do not compute Brier/ECE.
- Incomplete observations -> preserve observed coverage.
- High abstention -> preserve classification coverage and abstention rate separately.
- Non-independent reference -> preserve provenance and allow policy to fail closed.
- Missing policy metric -> `INCONCLUSIVE`.
- Drift axes mismatch -> `NOT_COMPARABLE`.
- Raw prompt/output/credentials in compact evidence -> reject.

## Output contract

Return the smallest sufficient capsule:

- evaluator/config identity;
- calibration or validation phase;
- reference-source identity and independence;
- calibration/validation cohort hashes;
- expected/observed/classification/probability coverage;
- confusion counts and abstention rate;
- applicable uncertainty/probability metrics;
- explicit gate policy and `PASS|FAIL|INCONCLUSIVE` result;
- drift comparability/deltas when requested;
- provenance and falsifiers;
- explicit truth, causal, authority, and deployment ceilings.
