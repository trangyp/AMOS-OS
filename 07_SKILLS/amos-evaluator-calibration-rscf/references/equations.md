# Evaluator Calibration Equations

All variables below are dimensionless counts, indicators, proportions, or declared probabilities.

## 1. Confusion counts — ESTABLISHED_MATH

For classified observations only, let the reference label be `y_i in {0,1}` and evaluator class be `h_i in {0,1}`. `1` denotes PASS.

- `TP = sum_i 1[y_i=1 and h_i=1]`
- `TN = sum_i 1[y_i=0 and h_i=0]`
- `FP = sum_i 1[y_i=0 and h_i=1]`
- `FN = sum_i 1[y_i=1 and h_i=0]`

Abstentions are excluded from those four counts and reported separately. This is a definition, not a claim that reference labels are true.

## 2. Coverage and selective accuracy — ESTABLISHED_MATH

Let `N` be observed reference/evaluator pairs and `N_c` the non-abstained subset.

`classification_coverage = N_c / N`, for `N > 0`.

`selective_accuracy = (TP + TN) / N_c`, for `N_c > 0`.

`abstention_rate = 1 - classification_coverage`.

Undefined denominators remain `None/UNKNOWN` rather than being replaced by zero.

## 3. Wilson score interval — ESTABLISHED_MATH

For `k` successes among `n > 0` Bernoulli observations, `p_hat = k/n`, and standard-normal critical value `z` for the requested two-sided confidence level:

`center = (p_hat + z^2/(2n)) / (1 + z^2/n)`

`half = z/(1 + z^2/n) * sqrt(p_hat(1-p_hat)/n + z^2/(4n^2))`

The interval is `[center-half, center+half]`, clipped to `[0,1]` for numerical safety.

Assumptions/limits: the formula is correct for its mathematical construction, but interval interpretation depends on sampling assumptions. It does not prove independence, stationarity, representativeness, or label truth.

## 4. Brier score — ESTABLISHED_MATH

Only when the evaluator output is explicitly declared as probability of PASS, `q_i in [0,1]`, and reference labels are encoded `y_i in {0,1}`:

`Brier = (1/n) * sum_i (q_i - y_i)^2`.

Lower is better for the declared labels. It is a proper scoring rule for probabilistic forecasts, but low Brier score does not establish semantic correctness, trustworthy labels, or deployment validity.

## 5. Fixed-bin ECE — ESTABLISHED_MATH / ESTIMATOR CHOICE

Partition probability outputs into `B >= 2` fixed bins. For each non-empty bin `b`, let `n_b` be bin size, `conf_b` the mean declared probability, and `freq_b` the empirical PASS frequency.

`ECE = sum_b (n_b/n) * |conf_b - freq_b|`.

The binning rule is part of the estimator specification. ECE is descriptive and bin-sensitive; it is not a proper scoring rule and must not be interpreted as truth or causal evidence.

## 6. Drift deltas — DEFINITION

For a metric `m` on comparable baseline `A` and candidate `B`:

`Delta_m = m(B) - m(A)`.

A delta is computed only after comparability gates pass. `Delta_m` alone does not identify the cause of change or statistical significance.

## Hard mathematical invariants

- Denominator zero -> undefined, never silently zero.
- Probability metrics require explicit probability semantics and `q_i in [0,1]`.
- Calibration and validation cohorts must have distinct hashes when a threshold/config was selected using the calibration cohort.
- Confidence intervals describe estimator uncertainty under assumptions; they do not certify data quality.
- Reference labels remain evidence unless independently established as ground truth.
