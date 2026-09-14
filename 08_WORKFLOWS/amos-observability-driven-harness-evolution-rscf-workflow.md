---
title: amos-observability-driven-harness-evolution-rscf-workflow
type: workflow
skill: amos-observability-driven-harness-evolution-rscf
agent: amos-observability-driven-harness-evolution-rscf-agent
version: 3.0.0
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
status: implemented_local_reference
---

# Workflow: AMOS Observability-Driven Harness Evolution

This workflow governs mutation evidence. It does not execute harness writes, evaluation jobs, rollback, merge, deployment, or canonical promotion.

## State machine

`INTAKE -> FREEZE_EXPERIMENT -> INVENTORY_SURFACES -> CREATE_MUTATION -> STAGE_CHANGES -> FREEZE_MANIFEST -> ISOLATION_GATE -> EXECUTE_EVAL_EXTERNALLY -> BIND_EVALUATION -> BIND_EVALUATOR_RELIABILITY -> MUTATION_VERDICT -> OPTIONAL_RECONCILIATION -> TERMINAL`

## Preconditions

- `amos-observability-driven-harness-evolution-rscf` is available.
- Baseline harness identity is exact and immutable for this experiment.
- Candidate harness version is distinct from baseline.
- PR19-compatible evaluation receipts and PR22-compatible calibration receipts can be produced or the workflow will terminate `INCONCLUSIVE`.
- Mutation authority is separate from this workflow.

## Steps

1. **INTAKE** — bind objective, repository/ref, declared mutation scope, and authority ceiling.
2. **FREEZE_EXPERIMENT** — freeze target/version, baseline/candidate harness versions, suite/environment, model/config, evaluator set/version, budget, task cohort, evidence archetype, expected task count, and calibrated evaluator identity/config.
3. **INVENTORY_SURFACES** — register every mutable file path, component class, baseline hash, and mutability flag.
4. **CREATE_MUTATION** — bind root-cause evidence hash, evidence-bundle hash, predicted fix set, predicted regression set, and attribution mode before evaluation.
5. **STAGE_CHANGES** — for each changed path require declared surface, exact baseline hash, distinct candidate hash, and rollback hash equal to baseline.
6. **FREEZE_MANIFEST** — reject later staging; require `COUPLED_SET` when multiple component classes change.
7. **ISOLATION_GATE** — verify prior tests/rewards are hidden, legitimate agent-owned state is preserved, and shared-verifier residue was sanitized before the next agent phase.
8. **EXECUTE_EVAL_EXTERNALLY** — evaluation is performed by an authorized external runner; this workflow only consumes bounded receipts.
9. **BIND_EVALUATION** — validate sealed complete-coverage baseline/candidate run receipts and exact comparison receipt; reject frozen-axis drift.
10. **BIND_EVALUATOR_RELIABILITY** — validate held-out `VALIDATION` calibration report and reliability-gate receipt matching frozen evaluator identity/config.
11. **MUTATION_VERDICT** — use `harness_evolution_guarded_runtime.py` and the guarded receipt validator; emit `KEEP|ROLLBACK|INCONCLUSIVE` recommendation only. Both KEEP and ROLLBACK require comparable, reliable, isolated, plausibly attributable evidence; otherwise emit `INCONCLUSIVE`.
12. **OPTIONAL_RECONCILIATION** — observe `KEPT|ROLLED_BACK|NOT_APPLIED`, exact observed harness version, changed-component hashes, and reconciliation evidence.
13. **TERMINAL** — return bounded receipt hashes, gaps, authority ceiling, and falsifiers.

## Recovery

- Undeclared or immutable surface -> reject mutation; re-inventory rather than widening scope silently.
- Baseline hash mismatch -> invalidate staged change and re-read current baseline.
- Cross-component mutation under `SINGLE_COMPONENT` -> reject; either split the experiment or explicitly declare coupled attribution.
- Verifier/reward contamination -> invalidate comparative evidence and rerun from a clean state.
- Incomplete/unsealed evaluation -> `INCONCLUSIVE`; do not extrapolate.
- Frozen-axis mismatch -> `NOT_COMPARABLE`; do not compute a causal claim.
- Evaluator reliability not `PASS` -> `INCONCLUSIVE`; do not use the untrusted evaluation to justify KEEP or ROLLBACK.
- Critical regression under comparable, reliable, isolated, plausibly attributable evidence -> recommend `ROLLBACK`; otherwise `INCONCLUSIVE`. Never execute rollback here.
- Reconciliation mismatch -> preserve recommendation but mark actual effect `UNKNOWN/GAP`.

## Hard firewalls

`MUTATION_PROPOSAL != WRITE_AUTHORITY`

`KEEP_RECOMMENDATION != MERGE_AUTHORITY`

`ROLLBACK_RECOMMENDATION != ROLLBACK_EXECUTION`

`NEXT_ROUND_DELTA != CAUSAL_PROOF`

`VERIFIER_OR_REWARD_LEAKAGE != VALID_COMPARATIVE_EVIDENCE`

`CALIBRATION_PASS != GROUND_TRUTH`
