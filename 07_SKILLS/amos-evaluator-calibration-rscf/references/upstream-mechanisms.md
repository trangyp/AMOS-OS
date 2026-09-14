# Pinned Upstream Mechanisms — 2026-09-14

These are `SOURCE_CLAIM` inputs used for mechanism design. They are not vendored dependencies and do not transfer authority.

## Inspect AI

Source: `UKGovernmentBEIS/inspect_ai@1276f419913248bdb4c7c41a8e2274a396e97083`.

Observed mechanisms:
- scorer metrics expose `std`, `stderr`, `bootstrap_stderr`, confidence intervals, Wilson intervals, and Krippendorff alpha;
- evaluation can run multiple epochs, producing multiple scores per sample before reduction;
- model-graded scorers remain scorer outputs rather than ground truth.

AMOS adaptation: keep evaluator observations and uncertainty separate from truth/authority; retain repeated-run identity when applicable.

## EleutherAI lm-evaluation-harness

Source: `EleutherAI/lm-evaluation-harness@d6de81643928d653435c431bae19945d41d32520`.

Observed mechanisms:
- explicit bootstrap iteration count controls standard-error estimation;
- result schemas distinguish metrics from corresponding standard-error fields;
- task aggregation tests exercise uncertainty aggregation.

AMOS adaptation: uncertainty estimator identity/configuration must be explicit and must not erase cohort/sampling assumptions.

## Ragas

Source: `vibrantlabsai/ragas@298b68274234c060deacab3cf5fb52aa3a20e885`.

Observed mechanisms:
- documented LLM-as-judge alignment workflow compares judge outputs with human targets;
- documentation calls for re-evaluation after alignment;
- LLM-based metrics are described as potentially non-deterministic.

AMOS adaptation: split calibration/tuning from held-out validation, preserve reference-source provenance, and never equate human target with infallible truth.

## DeepEval

Source: `confident-ai/deepeval@b1f3f205c30cd3de43e23221b97bdddf92f7aa1c`.

Observed mechanisms:
- metrics carry explicit thresholds and scores;
- evaluation utilities preserve threshold, score, error, and success state;
- some metric surfaces require at least one thresholded non-flaky metric to vote.

AMOS adaptation: threshold is typed configuration evidence; a threshold by itself is not calibration proof and does not create a universal pass standard.

## Opik

Source: `comet-ml/opik@84f1ab7f7b1e038d393346532baef28a9355852d`.

Observed mechanisms:
- experiments connect traces/executions to dataset items;
- evaluation APIs bind tasks, datasets, scoring metrics, project/experiment identity, and sample counts;
- optimizer evaluation surfaces support repeated samples.

AMOS adaptation: bind evaluator reliability evidence to exact dataset/cohort identity and preserve execution/evaluation identity separately from reliability conclusions.

## Source firewalls

- `SOURCE_PROJECT_FEATURE != AMOS_VALIDATED_MECHANISM`
- `HUMAN_TARGET != GROUND_TRUTH`
- `THRESHOLD_CONFIGURED != THRESHOLD_CALIBRATED`
- `STANDARD_ERROR_REPORTED != REPRESENTATIVE_SAMPLE`
- `REPEATED_SAMPLES != INDEPENDENT_SAMPLES`
- `EXPERIMENT_TRACKED != EXPERIMENT_CAUSALLY_IDENTIFIED`
