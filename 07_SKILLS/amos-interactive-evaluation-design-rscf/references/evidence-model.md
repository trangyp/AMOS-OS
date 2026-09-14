# Evaluation evidence, review, and comparison model

## Evidence firewall

Preserve:

- `FINAL_RESPONSE_QUALITY != TRAJECTORY_QUALITY`
- `OUTCOME_SUCCESS != PROCESS_COMPLIANCE`
- `OBSERVATION != EVALUATION`
- `EVALUATION != AUTHORITY`
- `JUDGE_OUTPUT != GROUND_TRUTH`
- `SAMPLED_TRACE != COMPLETE_TRACE`
- `HASH_MATCH != TRUST`
- `SCORE_DELTA != CAUSAL_ATTRIBUTION`
- `RECEIPT != INDEPENDENT_CONFIRMATION` when both descend from one run.

## Evidence archetypes

Use four non-substitutable archetypes:

- `CONTRACT`: deterministic schema/invariant/state checks.
- `INTERVENTION`: paired or controlled perturbation evidence.
- `PROCESS`: trajectory/action/recovery evidence.
- `OUTCOME_PROPERTY`: properties of terminal outputs or effects.

An archetype labels what was measured; it does not increase epistemic authority.

## Interactive trajectory object

Minimum observable record:

```text
task_id
objective
constraints
authority_state
observations
actions/tool calls
arguments/result hashes
state transitions
errors/recovery
effect state
terminal state
final output hash
```

Do not require private chain-of-thought.

## Reviewer stage

A reviewer operates on an already-observed subject and records:

```text
review_id
run_id
task_id
stage
reviewer identity/version
subject reference/hash
decision = CONTINUE | TERMINATE | ESCALATE
explanation hash
metadata hash
```

The review decision controls the evaluation flow only.

## Judge disagreement

For criterion `c`, let the observed categorical judgments be

`J_c = {j_1, ..., j_n}`.

Define agreement only when all observed non-missing judgments are identical:

`Agreed(c) := |unique(J_c)| = 1`.

If `|unique(J_c)| > 1`, classify the set `COMPETING`. Do not map disagreement to an arithmetic mean unless the rubric explicitly defines a valid numeric scale and aggregation rule.

## Sampling and coverage

Let `N_e` be the declared expected task count and `N_o` the observed task count.

`Coverage = N_o / N_e`, for `N_e > 0`.

Complete coverage requires `N_o = N_e`. A high pass rate on a sample does not establish complete-suite pass.

## Baseline/candidate comparability

Let each run identity be

`R = (S,T,V,E,H,H_v,Q,Q_v,M,M_c,B,C,A)`

where:
- `S`: suite;
- `T,V`: target and target version;
- `E`: environment identity;
- `H,H_v`: harness and harness version;
- `Q,Q_v`: evaluator set and version;
- `M,M_c`: model and model-config identity;
- `B`: budget;
- `C`: task-cohort identity;
- `A`: evidence archetype.

For a harness-version experiment, runs are comparable only when all coordinates except `H_v` match. This is a structural comparability rule, not proof that the harness edit uniquely caused the observed delta.

## Mutation metrics

For predicted-fix set `P_f`, observed-fix set `O_f`, predicted-regression set `P_r`, and observed-regression set `O_r`:

`Precision_fix = |P_f ∩ O_f| / max(1, |P_f|)`.

When `O_r` is non-empty:

`Recall_reg = |P_r ∩ O_r| / |O_r|`.

When `O_r` is empty, define `Recall_reg := 1` because there are no observed regressions to miss.

These metrics evaluate prediction quality only; neither proves causal attribution.

## Mutation verdict

Use:

- `KEEP`: comparable runs, plausible attribution, at least one observed fix, more fixes than regressions, and no critical regression.
- `ROLLBACK`: any critical regression or regressions exceed fixes.
- `INCONCLUSIVE`: non-comparable runs, attribution not plausible, or insufficient net evidence.

An AMOS `KEEP` verdict is a bounded harness-evaluation recommendation. It does not grant merge, deployment, or canonical-promotion authority.
