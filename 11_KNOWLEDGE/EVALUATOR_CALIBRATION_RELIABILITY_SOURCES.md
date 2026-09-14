# Evaluator Calibration / Reliability Source Registry — 2026-09-14

Epistemic class: `SOURCE_CLAIM` unless separately executed inside AMOS.

Pinned primary repositories:

- `UKGovernmentBEIS/inspect_ai@1276f419913248bdb4c7c41a8e2274a396e97083`
  - bootstrap stderr, confidence intervals, Wilson intervals, Krippendorff alpha, multi-epoch score reduction.
- `EleutherAI/lm-evaluation-harness@d6de81643928d653435c431bae19945d41d32520`
  - bootstrap iteration controls and metric/stderr result separation.
- `vibrantlabsai/ragas@298b68274234c060deacab3cf5fb52aa3a20e885`
  - judge-to-human-target alignment workflow followed by re-evaluation; LLM metrics described as potentially nondeterministic.
- `confident-ai/deepeval@b1f3f205c30cd3de43e23221b97bdddf92f7aa1c`
  - threshold/score/success as explicit metric state.
- `comet-ml/opik@84f1ab7f7b1e038d393346532baef28a9355852d`
  - experiment/dataset/trace/scoring identity and repeated-sample evaluation surfaces.

AMOS adopts mechanisms, not source-project truth or authority.

Research boundary:

`UNCERTAINTY_ESTIMATE != DATA_REPRESENTATIVENESS`

`HUMAN_TARGET != GROUND_TRUTH`

`THRESHOLD_CONFIGURED != THRESHOLD_CALIBRATED`

`CALIBRATION_FIT != HELD_OUT_GENERALIZATION`

`EXPERIMENT_TRACKED != CAUSAL_IDENTIFICATION`
