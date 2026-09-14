---
name: amos-interactive-evaluation-design-rscf
description: Design, audit, and evidence interactive evaluations for AMOS agents, skills, workflows, and tool-using systems. Use when final-response scoring is insufficient; when trajectories, recoverability, authority/process compliance, adversarial behavior, efficiency, or runtime evidence must be evaluated; or when test/benchmark claims need provenance-bound promotion or downgrade.
---

# AMOS Interactive Evaluation Design RSCF

Origin architect and steward: **Trang Phan**.

## Core invariants

- `FINAL_RESPONSE_QUALITY != TRAJECTORY_QUALITY`
- `OUTCOME_SUCCESS != PROCESS_COMPLIANCE`
- `TEST_SPECIFIED != TEST_EXECUTED`
- `TEST_EXECUTED != TEST_REPRODUCIBLE`
- `MODEL_JUDGE_SCORE != GROUND_TRUTH`
- `RED_TEAM_NO_FINDING != SAFE`
- `BENCHMARK_SCORE != DEPLOYMENT_VALIDITY`
- `TEST_PASS != TRUTH`

Do not request or expose private chain-of-thought. Evaluate observable plans, tool/action choices, state transitions, receipts, and outputs.

## Evaluation workflow

1. **Resolve the target**
   - Bind target artifact/runtime identity, version/ref, scope, regime, and decision the evaluation will inform.
   - Separate model/reference implementation from deployed runtime.

2. **Choose the evidence lane**
   - deterministic contract;
   - process/trajectory;
   - adversarial/red-team;
   - model-dependent semantic evaluation;
   - runtime/performance;
   - production/deployment validation.

3. **Define the oracle and falsifiers**
   - State what constitutes success/failure.
   - Check that the oracle is not merely the same policy rewritten.
   - Include negative, malformed, stale, unauthorized, replay, timeout, and recovery cases when applicable.

4. **Capture trajectory evidence**
   - Preserve objective, constraints, authority state, actions/tool calls, state transitions, failures, recovery, terminal state, and final output.
   - Keep external tool/model outputs provenance-bound and untrusted until admitted.

5. **Execute or classify honestly**
   - If no run occurred, return `CONCEPTUAL_ONLY` or `UNKNOWN` rather than PASS.
   - If a historical receipt exists but the harness is missing, return `NON_REPRODUCIBLE`.
   - If execution occurred on a model/reference implementation, do not promote it to production-runtime validation.

6. **Bind evidence**
   - Record harness and receipt paths/hashes, environment, source identity, result counts, seeds/workload when applicable, non-coverage, and failure traces.
   - Use `scripts/eval_registry.py` for machine validation of the AMOS evidence registry.

7. **Return the narrowest verdict**
   - `VERIFIED_TESTED_SCOPE`
   - `PARTIAL`
   - `INVALIDATED_EVIDENCE`
   - `CONCEPTUAL_ONLY`
   - `NON_REPRODUCIBLE`
   - `UNKNOWN`

## Deterministic evidence registry

Validate the repository evidence registry with:

```bash
python 07_SKILLS/amos-interactive-evaluation-design-rscf/scripts/eval_registry.py \
  19_TESTS/EVAL_EVIDENCE_REGISTRY.json \
  --repo .
```

Run the script self-test after editing it:

```bash
python 07_SKILLS/amos-interactive-evaluation-design-rscf/scripts/eval_registry.py --self-test
```

A `VERIFIED_TESTED_SCOPE` entry must bind to exact in-repository harness and receipt Git blob hashes plus result counts and environment metadata. Do not weaken this rule to preserve a prior PASS label.

## External evaluation runners

External frameworks such as Promptfoo may be used for CI-friendly evals, red-team case generation, model comparison, or local/private execution when appropriate. Treat them as execution infrastructure, not epistemic authority.

Before adopting an external runner:
- pin source/version where reproducibility matters;
- inspect dependency and secret requirements;
- keep deterministic and model-dependent lanes separate;
- preserve raw results/configuration;
- do not make API keys mandatory for baseline structural gates;
- keep model/provider scores scoped to the exact evaluated configuration.

## Failure handling

- Missing target identity -> `UNKNOWN`.
- Missing harness for a claimed reproducible result -> `NON_REPRODUCIBLE`.
- Receipt/harness hash drift -> invalidate until rerun/review.
- Judge disagreement -> preserve competing results; do not average away material disagreement automatically.
- Ambiguous external effect during an eval -> reconcile before retry.
- Performance claim without exact environment/workload -> downgrade.
- Safety/red-team scan with no findings -> do not infer universal safety.

## References

Read `references/evidence-model.md` for trajectory fields, evidence lanes, judge controls, and falsifiers.

Use `19_TESTS/TESTS_TEST_CONTRACT.md` for AMOS test-plane governance and `19_TESTS/EVAL_EVIDENCE_REGISTRY.json` for current machine-readable evidence status.
