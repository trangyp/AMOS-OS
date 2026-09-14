---
title: amos-interactive-evaluation-design-rscf-workflow
type: workflow
skill: amos-interactive-evaluation-design-rscf
agent: amos-interactive-evaluation-design-rscf-agent
origin_architect: Trang Phan
version: 3.0.0
epistemic_class: AMOS_MODEL
---

# AMOS Interactive Evaluation Workflow

State machine:

```text
INTAKE
 -> BIND_RUN_IDENTITY
 -> CLASSIFY_ARCHETYPE
 -> DESIGN_ORACLE
 -> EXECUTE_OR_CLASSIFY
 -> RECORD_TASK_RESULTS
 -> RECORD_REVIEWS
 -> RECORD_JUDGMENTS
 -> RECORD_COVERAGE
 -> SEAL_RUN
 -> OPTIONAL_BASELINE_COMPARE
 -> OPTIONAL_MUTATION_VERDICT
 -> REGISTRY_GATE
 -> CLAIM_GATE
 -> TERMINAL
```

## Gates

1. **BIND_RUN_IDENTITY** — bind suite, target/version, environment, harness/version, evaluator set/version, model/config, budget, task cohort, trace identity and evidence archetype.
2. **CLASSIFY_ARCHETYPE** — use `CONTRACT|INTERVENTION|PROCESS|OUTCOME_PROPERTY`; one lane cannot substitute for another.
3. **DESIGN_ORACLE** — define explicit success/failure predicates, falsifiers, and negative cases. Reject circular or same-policy-as-oracle designs.
4. **EXECUTE_OR_CLASSIFY** — no execution means no PASS. Keep reference/model execution separate from deployed-runtime validation.
5. **RECORD_TASK_RESULTS** — preserve outcome/process/safety/recovery/critical-failure state independently.
6. **RECORD_REVIEWS** — bind `CONTINUE|TERMINATE|ESCALATE` to exact subject hash. Review control never supplies runtime authority.
7. **RECORD_JUDGMENTS** — bind evaluator identity/version/evidence reference. Material disagreement remains `COMPETING`.
8. **RECORD_COVERAGE** — store expected and observed counts; `SAMPLED_PASS != COMPLETE_PASS`.
9. **SEAL_RUN** — reject late evidence after sealing; produce hash-bound run receipt.
10. **OPTIONAL_BASELINE_COMPARE** — compare only if suite, target/version, environment, harness identity, evaluator, model/config, budget, cohort and archetype match. Harness version may differ as the declared mutation axis.
11. **OPTIONAL_MUTATION_VERDICT** — return `KEEP|ROLLBACK|INCONCLUSIVE`; critical regressions block KEEP.
12. **REGISTRY_GATE** — historical evidence promotion still passes `eval_registry.py` exact-hash rules.
13. **CLAIM_GATE** — enforce `MODEL_JUDGE_SCORE != GROUND_TRUTH`, `SCORE_DELTA != CAUSAL_ATTRIBUTION`, `EVAL_RESULT != DEPLOYMENT_AUTHORITY`.

## Recovery

- Incomplete task coverage -> preserve gap and downgrade completeness.
- Judge disagreement -> keep competing results and identify next discriminating evidence.
- Frozen-axis mismatch -> `NOT_COMPARABLE`; do not compute performance attribution.
- Ambiguous external effect -> reconcile the effect independently of evaluation score.
- Raw sensitive content discovered in compact evidence -> quarantine/reject and re-run with metadata/hash capture.
- Critical harness regression -> bounded `ROLLBACK` recommendation; rollback execution still requires owning authority.

## Deterministic validation

```bash
python -m unittest -v 19_TESTS/test_agent_evaluation_runtime.py
python 07_SKILLS/amos-interactive-evaluation-design-rscf/scripts/evaluation_contract_check.py --self-test
python 07_SKILLS/amos-interactive-evaluation-design-rscf/scripts/eval_registry.py --self-test
```

GitHub CI is the repository-copy validation authority for this local reference implementation.
