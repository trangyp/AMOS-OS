---
name: amos-observability-driven-harness-evolution-rscf
description: Govern and audit bounded evolution of agent harnesses by inventorying explicit mutable surfaces, freezing evidence-backed mutation manifests before evaluation, enforcing verifier/reward isolation, binding comparable PR19 evaluation receipts and PR22 evaluator-reliability evidence, recommending KEEP/ROLLBACK/INCONCLUSIVE, and reconciling what was actually applied. Use when changing system prompts, tool descriptions/implementations, middleware, Skills, sub-agent configuration, long-term memory, AMOS agent/workflow/policy/tool-registry surfaces, or when auditing self-improving harness loops without granting write, merge, rollback, deployment, or canonical authority.
---

# AMOS Observability-Driven Harness Evolution RSCF

Origin architect and steward: **Trang Phan**.

Operate as a deterministic evidence/control layer around harness mutation. Treat external harness frameworks as `SOURCE_CLAIM`; treat AMOS-specific orchestration and receipt composition as `AMOS_MODEL` unless executable evidence verifies the stated contract.

## Own this capability

Own the transition:

`declared surfaces -> frozen mutation manifest -> isolation gate -> comparable evaluation -> evaluator reliability -> bounded verdict -> reconciliation`

Do not execute edits, evaluations, commits, merges, deployments, rollbacks, or canonical promotion. Those are separate authorities/effectors.

## Hard invariants

- `MUTATION_PROPOSAL != WRITE_AUTHORITY`
- `KEEP_RECOMMENDATION != MERGE_AUTHORITY`
- `ROLLBACK_RECOMMENDATION != ROLLBACK_EXECUTION`
- `NEXT_ROUND_DELTA != CAUSAL_PROOF`
- `PREDICTION != OUTCOME`
- `EDIT_RATIONALE != EVIDENCE`
- `CROSS_COMPONENT_EDIT != SINGLE_COMPONENT_ATTRIBUTION`
- `UNDECLARED_SURFACE != MUTABLE_SURFACE`
- `VERIFIER_ARTIFACT_VISIBLE_TO_NEXT_AGENT != VALID_EVAL`
- `CALIBRATION_PASS != GROUND_TRUTH`
- `COMPARABLE_RUNS != DEPLOYMENT_VALIDITY`
- `RAW_TRACE != DEFAULT_DURABLE_RECEIPT`

## Component contract

Source-derived harness classes:

`SYSTEM_PROMPT | TOOL_DESCRIPTION | TOOL_IMPLEMENTATION | MIDDLEWARE | SKILL | SUB_AGENT_CONFIG | LONG_TERM_MEMORY`

AMOS extension classes:

`AGENT_CONFIG | WORKFLOW | POLICY_CONFIG | TOOL_REGISTRY`

Do not attribute the AMOS extensions to upstream AHE/NexAU sources. See [references/upstream-mechanisms.md](references/upstream-mechanisms.md).

## Runtime

1. **Freeze experiment identity.** Bind target/version, harness baseline/candidate versions, suite/environment, base model/config, evaluator set/version, budget, task cohort, evidence archetype, expected task count, and calibrated evaluator identity/config.
2. **Inventory surfaces.** Register every mutable file path with component class and baseline content hash. Unknown or undeclared paths fail closed.
3. **Create mutation.** Bind root-cause evidence hash, evidence-bundle hash, predicted fix IDs, predicted regression IDs, and attribution mode before candidate evaluation.
4. **Stage changes.** Require before-hash equality with the frozen baseline, a distinct after hash, and an exact rollback hash equal to the prior state.
5. **Freeze manifest.** After freezing, reject additional staged changes. Cross-component mutations require `COUPLED_SET` plus an explicit coupling-reason hash.
6. **Prove isolation.** Record whether prior verifier tests/rewards were hidden and whether agent-owned state was preserved. If shared-verifier residue existed, require sanitization before the next agent phase.
7. **Execute evaluation externally.** This Skill does not run the model/evaluator. Use `amos-interactive-evaluation-design-rscf` for run/comparison evidence.
8. **Bind evaluation evidence.** Require sealed, complete-coverage baseline/candidate run receipts and a hash-valid comparison receipt with all frozen axes matching except the declared harness version mutation.
9. **Bind evaluator reliability.** Require a hash-valid held-out `VALIDATION` report and reliability-gate receipt from `amos-evaluator-calibration-rscf` matching the frozen evaluator identity/config.
10. **Recommend verdict.** Return `KEEP`, `ROLLBACK`, or `INCONCLUSIVE` only. Never emit an authorization or perform the recommended action.
11. **Reconcile observed state.** After another authorized system applies or declines the recommendation, record `KEPT|ROLLED_BACK|NOT_APPLIED`, observed version, exact changed-component hashes, and evidence hash.
12. **Verify ledger.** Treat ledger tamper as a blocking integrity failure.

## Decision rule

Let:

- `F` = observed fixed task IDs;
- `R` = observed regressed task IDs;
- `C` = critical regression task IDs;
- `P_f` = predicted fix IDs;
- `P_r` = predicted regression IDs.

The deterministic diagnostics are:

`fix_precision = |P_f ∩ F| / max(1, |P_f|)`

`regression_recall = 1` when `R` is empty; otherwise

`regression_recall = |P_r ∩ R| / |R|`.

These are descriptive diagnostics, not causal proofs.

Recommend `KEEP` only when all load-bearing evidence is usable, `F` is nonempty, `|F| > |R|`, and `C` is empty.

Recommend `ROLLBACK` only when all load-bearing comparison, reliability, isolation, and attribution evidence is usable and either a critical regression exists or `|R| > |F|`.

Otherwise return `INCONCLUSIVE`.

Read [references/formal-contract.md](references/formal-contract.md) before changing verdict semantics.

## Deterministic surfaces

- Evidence-store/base runtime: `scripts/harness_evolution_runtime.py`
- Active fail-closed decision runtime: `scripts/harness_evolution_guarded_runtime.py`
- Base receipt validator: `scripts/harness_evolution_contract_check.py`
- Active fail-closed receipt validator: `scripts/harness_evolution_guarded_contract_check.py`
- Repository regression suites: `19_TESTS/test_harness_evolution_runtime.py` and `19_TESTS/test_harness_evolution_guarded_runtime.py`

Use the guarded runtime for verdict admission. The base runtime remains part of the evidence-store lineage but must not be used alone to admit KEEP/ROLLBACK. Run both regression suites and both guarded/base self-tests after changing semantics.

## Parent/dependency contract

Use with:

- `amos-interactive-evaluation-design-rscf` for exact run/comparison evidence;
- `amos-evaluator-calibration-rscf` for held-out evaluator reliability;
- `amos-agentops-observability-rscf` when trace/observability evidence is needed.

Accept only explicit receipts/evidence. A sibling Skill's existence does not grant authority or prove its current runtime state.

## Failure behavior

Return `UNKNOWN/GAP` or `INCONCLUSIVE` rather than guessing when:

- a mutable path was not declared;
- baseline/candidate axes are not comparable;
- evaluation coverage is incomplete or unsealed;
- verifier/reward contamination is possible;
- evaluator reliability is not `PASS`;
- attribution is not plausible;
- a receipt hash is invalid;
- rollback state cannot be bound to the pre-change hash;
- reconciliation cannot prove the observed component state.

A critical regression may justify a `ROLLBACK` recommendation only when the bound comparison/reliability/isolation/attribution evidence is usable; otherwise return `INCONCLUSIVE`. A rollback recommendation never executes rollback.

## Output contract

Return the smallest sufficient capsule:

- experiment and mutation identity;
- changed component paths/classes and before/after hashes;
- predicted fixes/regressions;
- isolation status;
- frozen-axis comparison state;
- evaluator-reliability verdict;
- observed fixes/regressions/critical regressions;
- fix precision and regression recall;
- `KEEP|ROLLBACK|INCONCLUSIVE` recommendation;
- reconciliation state if observed;
- evidence/receipt hashes;
- explicit authority ceiling and remaining gaps.

Read [references/upstream-mechanisms.md](references/upstream-mechanisms.md) for source provenance and [references/formal-contract.md](references/formal-contract.md) for state/receipt rules.
