---
name: amos-interactive-evaluation-design-rscf
description: Design, execute, audit, compare, and govern evidence for interactive AMOS evaluations of agents, Skills, workflows, tools, and harness mutations. Use when final-answer scoring is insufficient; when trajectory/process/recovery evidence matters; when tool-result review must continue, terminate, or escalate; when model judges or external eval runners disagree; when sampled runs must not be confused with complete coverage; or when baseline-vs-candidate harness changes require a bounded KEEP, ROLLBACK, or INCONCLUSIVE verdict.
---

# AMOS Interactive Evaluation Design RSCF

Origin architect/steward: **Trang Phan**.

Treat evaluation as evidence production, not authority or truth promotion.

## Hard invariants

- `FINAL_RESPONSE_QUALITY != TRAJECTORY_QUALITY`
- `OUTCOME_SUCCESS != PROCESS_COMPLIANCE`
- `OBSERVATION != EVALUATION`
- `EVALUATION != INTERVENTION`
- `REVIEW_DECISION != RUNTIME_AUTHORITY`
- `MODEL_JUDGE_SCORE != GROUND_TRUTH`
- `JUDGE_AGREEMENT != GROUND_TRUTH`
- `SAMPLED_PASS != COMPLETE_PASS`
- `TEST_SPECIFIED != TEST_EXECUTED`
- `TEST_EXECUTED != TEST_REPRODUCIBLE`
- `SCORE_DELTA != CAUSAL_ATTRIBUTION`
- `BENCHMARK_SCORE != DEPLOYMENT_VALIDITY`
- `TEST_PASS != TRUTH`

Do not request hidden chain-of-thought. Use observable actions, tool calls/results, state transitions, receipts, outputs, and explicit review/evaluation artifacts.

## Evaluation runtime

1. Bind exact evaluation identity:
   - suite;
   - target + version;
   - environment;
   - harness + version;
   - evaluator set + version;
   - model/config;
   - budget;
   - task cohort;
   - evidence archetype;
   - trace/round-trip receipt when relevant.
2. Classify evidence as `CONTRACT|INTERVENTION|PROCESS|OUTCOME_PROPERTY`.
3. Record per-task outcome, process, safety, recovery, and critical-failure state separately.
4. Record judge outputs as append-only evidence with evaluator identity/version and evidence reference.
5. Preserve disagreement. Do not average materially competing judge outputs into false certainty.
6. Review executed tool/trajectory results with `CONTINUE|TERMINATE|ESCALATE` only as evaluation-control decisions.
7. Record expected vs observed task counts. Partial sampling remains incomplete coverage.
8. Seal the run before relying on its receipt.
9. Compare baseline/candidate runs only when all load-bearing axes except the declared mutation axis are frozen.
10. Return harness-mutation verdict `KEEP|ROLLBACK|INCONCLUSIVE` from observed fixes/regressions, critical regressions, and attribution plausibility.

## Frozen-axis comparison contract

For harness attribution, keep these identical unless the experiment explicitly targets one of them:

- suite and task cohort;
- target implementation/version;
- environment identity;
- harness identity (version may differ as the mutation axis);
- evaluator set/version;
- base model + model configuration;
- evaluation budget;
- evidence archetype.

A mismatch makes the pair `NOT_COMPARABLE`; do not manufacture deltas.

## Review contract

Adapt post-tool review as a separate evidence stage:

- `CONTINUE`: pass evaluation control onward; does not authorize the tool/effect.
- `TERMINATE`: stop the evaluation/sample; does not revoke external runtime authority.
- `ESCALATE`: route to the next reviewer; does not escalate privileges.

Bind each review to the exact subject reference/hash and reviewer identity/version.

## Deterministic surfaces

- Runtime: `scripts/evaluation_runtime.py`
- Runtime receipt validator: `scripts/evaluation_contract_check.py`
- Historical evidence-registry validator: `scripts/eval_registry.py`
- Regression suite in AMOS repo: `19_TESTS/test_agent_evaluation_runtime.py`

Run all deterministic tests after changing runtime semantics.

## Evidence registry

For repository evidence promotion, validate:

```bash
python scripts/eval_registry.py <registry.json> --repo <repo-root>
```

`VERIFIED_TESTED_SCOPE` requires exact repository harness/receipt blob hashes plus bounded result/environment metadata. Never weaken the registry to preserve an old PASS label.

## External runners and judges

Inspect AI, Promptfoo, monitorability datasets, OpenHands benchmarks, and similar frameworks may supply execution/review/eval mechanisms. Treat them as infrastructure or source evidence only.

When using external systems:

- pin source/version for reproducibility;
- bind exact config/environment/model identity;
- preserve raw results outside the compact receipt when allowed;
- keep secrets and raw prompts/outputs out of durable AMOS receipts by default;
- keep deterministic and model-dependent evaluation lanes separate;
- record sampling/missingness explicitly;
- preserve evaluator disagreement;
- never infer deployment authority from a score.

Read [references/evidence-model.md](references/evidence-model.md) for evidence lanes, trajectory fields, comparison rules, and mutation metrics. Read [references/upstream-mechanisms.md](references/upstream-mechanisms.md) before making source-specific claims about external evaluation frameworks.

## Failure behavior

- Missing target/version/environment identity -> `UNKNOWN`.
- Missing historical harness -> `NON_REPRODUCIBLE`.
- Stale harness/receipt hash -> `INVALIDATED_EVIDENCE` until rerun/review.
- Incomplete sample -> preserve coverage gap; do not promote to complete pass.
- Judge disagreement -> `COMPETING`; do not silently average.
- Baseline/candidate frozen-axis mismatch -> `NOT_COMPARABLE`.
- Critical regression -> mutation cannot receive `KEEP`.
- Benefit without plausible attribution -> `INCONCLUSIVE`.
- External effect ambiguity -> reconcile effect state before retry/finality claims.
- Raw sensitive content in compact receipt -> reject.

## Output contract

Return the smallest sufficient evaluation capsule:

- target/run identity;
- evidence archetype and lanes;
- expected/observed coverage;
- process/outcome/safety/recovery findings;
- reviewer decisions;
- evaluator disagreement;
- baseline/candidate comparability;
- fixes/regressions/critical regressions;
- bounded verdict;
- explicit non-coverage;
- provenance and falsifier;
- authority/deployment claim ceiling.
