---
title: amos-evaluator-calibration-rscf-workflow
type: workflow
source: 08_WORKFLOWS
origin_architect: Trang Phan
version: 1.0.0
epistemic_class: AMOS_MODEL
---

# Workflow: AMOS Evaluator Calibration RSCF

Parent: `amos-interactive-evaluation-design-rscf`.

State machine:

`INTAKE -> BIND_EVALUATOR -> BIND_REFERENCE -> CALIBRATION_COHORT -> FREEZE_CONFIG_THRESHOLD -> HELD_OUT_VALIDATION -> METRIC_GATE -> RELIABILITY_POLICY -> OPTIONAL_DRIFT_COMPARE -> RECEIPT_GATE -> TERMINAL`

## Preconditions

- Evaluator identity/version/configuration hash is exact.
- Reference source identity/version/kind/independence is declared.
- Cohort hash and expected count are bound.
- Score semantics are declared before probability metrics are allowed.
- Calibration and validation evidence remain separate.

## Gates

1. **Calibration gate** — threshold/config selection may use only the calibration cohort.
2. **Held-out gate** — validation cohort hash must differ from calibration cohort hash and evaluator/threshold identity must be frozen.
3. **Metric gate** — undefined denominators remain UNKNOWN; abstentions remain separate; Brier/ECE require `PROBABILITY_PASS`.
4. **Reliability-policy gate** — use only explicit policy thresholds. No universal threshold is invented.
5. **Drift gate** — compute deltas only after cohort/reference/task-set comparability succeeds.
6. **Receipt gate** — raw prompt/output/credentials are rejected from compact durable receipts.

## Terminal states

- `PASS`: explicit validation policy satisfied on held-out evidence.
- `FAIL`: one or more explicit policy conditions failed.
- `INCONCLUSIVE`: required evidence or applicable metric is missing.
- `NOT_COMPARABLE`: drift axes are incompatible.

None of these states grants runtime, deployment, merge, or canonical-promotion authority.

## Recovery

- Same calibration/validation cohort -> reject and create a truly held-out cohort.
- Evaluator/config/threshold changed after calibration -> invalidate validation identity and restart calibration lineage.
- Reference independence `UNKNOWN` or `RELATED` -> preserve state; fail any policy requiring independent reference.
- Missing probabilities -> preserve probability coverage; probability-required policy becomes FAIL/INCONCLUSIVE according to its explicit check.
- Judge/reference disagreement -> evidence, not truth resolution.
