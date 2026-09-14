---
title: amos-interactive-evaluation-design-rscf-workflow
type: workflow
source: 08_WORKFLOWS
skill: amos-interactive-evaluation-design-rscf
agent: amos-interactive-evaluation-design-rscf-agent
status: CONDITIONAL
origin_architect: Trang Phan
---

# Workflow: AMOS Interactive Evaluation Design

## Objective

Produce the narrowest defensible evaluation verdict for an agent, Skill, workflow, tool integration, or runtime without collapsing final-output quality into trajectory/process quality or model tests into deployment validity.

## State machine

```text
INTAKE
  -> BIND_TARGET
  -> CLASSIFY_EVIDENCE_LANE
  -> DESIGN_ORACLE
  -> DESIGN_NEGATIVES
  -> EXECUTE_OR_CLASSIFY_UNEXECUTED
  -> CAPTURE_TRAJECTORY
  -> FORENSICS
  -> REGISTRY_VALIDATE
  -> VERDICT
  -> TERMINAL
```

## Inputs

- target artifact/runtime + version/ref;
- decision the evaluation informs;
- scope/regime/environment;
- available harnesses, configurations, receipts and raw results;
- observable trajectory/tool/action traces when interactive behavior is evaluated;
- authority/process contract when process compliance matters.

## Gates

### G1 — Target identity

Resolve exact target identity. Missing identity -> `UNKNOWN`.

### G2 — Evidence lane

Choose one or more independent lanes:
- deterministic contract;
- trajectory/process;
- adversarial/red-team;
- model-dependent semantic;
- runtime/performance;
- production/deployment.

Do not let one lane substitute for another.

### G3 — Oracle quality

Define explicit success/failure predicates and falsifiers. Reject circular tests where the oracle merely restates the implementation/policy under test.

### G4 — Negative coverage

Include applicable malformed, missing, stale, unauthorized, replay, timeout, partial-effect, poisoned-tool/prompt, failure-recovery and stopping cases.

### G5 — Execution boundary

If no execution occurred, label the result conceptual/unknown. If execution used a model/reference implementation, do not call it runtime validation.

### G6 — Trajectory capture

For interactive systems preserve observable actions, tool arguments/results, state transitions, authority/effect state, errors, recovery and terminal state. Do not require private chain-of-thought.

### G7 — Evidence binding

Bind harness + receipt identity, source/artifact hashes, environment, result counts, seeds/workload where relevant, non-coverage and failure traces.

### G8 — Registry validation

Run:

```bash
python 07_SKILLS/amos-interactive-evaluation-design-rscf/scripts/eval_registry.py \
  19_TESTS/EVAL_EVIDENCE_REGISTRY.json \
  --repo .
```

A stale hash, missing harness or invalid evidence promotion blocks the corresponding registry promotion.

## Verdicts

- `VERIFIED_TESTED_SCOPE`
- `PARTIAL`
- `INVALIDATED_EVIDENCE`
- `CONCEPTUAL_ONLY`
- `NON_REPRODUCIBLE`
- `UNKNOWN`

## External eval/red-team runners

External runners such as Promptfoo may organize model comparisons, CI evaluations or adversarial cases. Preserve their exact configs/results and treat them as evidence infrastructure, not epistemic authority. Baseline deterministic gates should not require external model/API secrets.

## Failure/recovery

- missing target identity -> `UNKNOWN`;
- absent historical harness -> `NON_REPRODUCIBLE`;
- target/harness/receipt hash drift -> invalidate and rerun/review;
- ambiguous external effect -> reconcile before retry;
- judge disagreement -> preserve competing outcomes;
- performance environment mismatch -> downgrade scope;
- no adversarial finding -> never infer universal safety.

## Outputs

Return:
- target identity;
- evidence lanes used;
- executed/not-executed classification;
- trajectory/process findings;
- adversarial findings;
- result counts and environment when executed;
- explicit non-coverage;
- provenance/hash bindings;
- final bounded verdict;
- next discriminating test if unresolved.

## Terminal invariant

`TEST_PASS != TRUTH` and `EVAL_RESULT != DEPLOYMENT_AUTHORITY`.

**MOC:** [[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS_MOC]]
