# Formal contract

## State objects

Let an experiment be

`E = (T, H0, H1, S, V, M, Q, B, C, A)`

where:

- `T` is target identity/version;
- `H0,H1` are baseline/candidate harness versions;
- `S` is suite/environment identity;
- `V` is evaluator set/version;
- `M` is base model/config identity;
- `Q` is task-cohort/evidence-archetype identity;
- `B` is evaluation budget;
- `C` is expected task count;
- `A` is calibrated evaluator identity/config.

A mutation manifest is

`U = (e, r, P_f, P_r, a, D)`

where:

- `e` is the evidence-bundle hash;
- `r` is the root-cause-evidence hash;
- `P_f` is the predicted-fix set;
- `P_r` is the predicted-regression set;
- `a` is attribution mode;
- `D` is the finite set of staged file changes.

For every staged change `d in D`:

`d = (path, class, h_before, h_after, h_rollback)`

with invariants:

`h_before = registered_baseline_hash(path)`

`h_after != h_before`

`h_rollback = h_before`.

These are identity constraints, not evidence that the content is semantically correct.

## Attribution boundary

`SINGLE_COMPONENT` is admissible only when all changed files map to one component class.

If more than one component class changes, require `COUPLED_SET` and a nonempty coupling-reason hash. A coupled edit may be evaluated as a set, but the observed delta does not identify the causal contribution of each component.

## Isolation predicate

Let:

- `T_h` = prior verifier tests hidden from the next agent;
- `R_h` = prior reward/verifier outputs hidden;
- `A_p` = legitimate agent-owned state preserved;
- `S_a` = shared-verifier residue sanitized before the next agent;
- `P_s` = prior shared-verifier state existed.

Base isolation requires:

`I_base = T_h AND R_h AND A_p`.

For a shared-verifier transition:

`I = I_base AND (NOT P_s OR S_a)`.

For single-step/separate-verifier modes, `P_s` must be false in the local reference contract.

`I=true` is evidence of the declared isolation checks only; it is not proof that no other contamination channel exists.

## Frozen-axis comparison

Baseline/candidate evaluation receipts must agree on:

`suite, target/version, environment, harness_id, evaluator_set/version, model/config, budget, task_cohort, evidence_archetype, expected_task_count`.

Only the harness version is the declared mutation axis. Both receipts must be sealed and complete coverage. The comparison receipt must bind their exact run IDs.

## Evaluator reliability dependency

A reliability gate is usable only when its companion report is a held-out `VALIDATION` report and matches the frozen calibrated evaluator ID/version/config.

`reliability=PASS` is a prerequisite for a KEEP recommendation, not truth.

## Verdict

Let `F,R,C,P_f,P_r` be observed fixes, regressions, critical regressions, predicted fixes, predicted regressions.

Diagnostics:

`precision_fix = |P_f intersection F| / max(1, |P_f|)`

`recall_reg = 1` if `R` is empty, otherwise

`recall_reg = |P_r intersection R| / |R|`.

Define the evidence-ready predicate:

`G = comparable AND reliability_pass AND isolation_valid AND attribution_plausible`.

Then the local reference recommendation is:

- `ROLLBACK` if `C` is nonempty;
- otherwise `ROLLBACK` if `G` and `|R| > |F|`;
- otherwise `KEEP` if `G`, `|F| > |R|`, and `|F| > 0`;
- otherwise `INCONCLUSIVE`.

This is an AMOS local policy, not an established universal optimization theorem.

## Receipt schemas

- `amos.harness-evolution.mutation.v1`
- `amos.harness-evolution.isolation.v1`
- `amos.harness-evolution.decision.v1`
- `amos.harness-evolution.reconciliation.v1`

Each receipt carries a SHA-256 hash over canonical JSON excluding the `receipt_hash` field itself.

## Authority ceiling

A decision receipt is evidence/recommendation only:

`KEEP != APPLY`

`KEEP != MERGE`

`ROLLBACK != REVERT_EXECUTION`

`RECONCILED != AUTHORIZED`

The durable action must be performed by a separately authorized effect path.
