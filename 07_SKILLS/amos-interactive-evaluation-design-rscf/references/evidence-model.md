# Evaluation evidence and trajectory model

## Evidence firewall

Preserve these distinctions:

- `FINAL_RESPONSE_QUALITY != TRAJECTORY_QUALITY`
- `OUTCOME_SUCCESS != PROCESS_COMPLIANCE`
- `TEST_SPECIFIED != TEST_EXECUTED`
- `TEST_EXECUTED != TEST_REPRODUCIBLE`
- `MODEL_JUDGE_SCORE != GROUND_TRUTH`
- `RED_TEAM_NO_FINDING != SAFE`
- `BENCHMARK_SCORE != DEPLOYMENT_VALIDITY`
- `RECEIPT != INDEPENDENT_CONFIRMATION` when both descend from one execution.

## Evaluation object

For interactive/tool-using systems, evaluate the state-changing trajectory rather than only the final text.

Minimum trajectory record:

```text
task_id
initial_state
objective
constraints
authority_state
steps[]:
  observation
  decision_or_plan
  action_or_tool
  arguments_digest
  result_digest
  state_transition
  authority/effect_state
  errors
  recovery
terminal_state
final_output
```

Do not require private chain-of-thought. Plans/decisions here mean inspectable external artifacts or tool/action choices, not hidden reasoning.

## Evaluation lanes

### Deterministic contract

Use exact predicates for schemas, invariants, state transitions, authorization, replay, idempotency, and bounded outputs. Prefer this lane when a direct oracle exists.

### Process/trajectory

Score whether the agent:
- selected an admissible action;
- preserved task identity and constraints;
- respected authority and scope;
- recovered correctly after failure;
- avoided repeated failed paths;
- stopped at the correct terminal state;
- used unnecessary calls/tokens/time only when justified.

### Adversarial/red-team

Exercise prompt/tool poisoning, untrusted MCP metadata, authority escalation, data exfiltration, stale state, replay, malformed schemas, ambiguous external effects, unsafe handoffs, and context contamination.

A generator such as Promptfoo may propose attacks or organize runs, but its generated cases and pass/fail labels remain evidence inputs. Preserve exact configuration, model/provider versions where applicable, seeds, and raw results.

### Model-dependent semantic evaluation

LLM judges may help evaluate open-ended quality, but require:
- an explicit rubric;
- judge identity/version;
- calibration against human or deterministic anchors when stakes require it;
- position/order bias controls where pairwise comparison is used;
- separation between judge disagreement and target-agent failure.

### Performance/runtime

Latency, throughput, storage, token usage, memory, and cost claims require exact hardware/runtime/workload identities. Do not reuse numbers across environments without remeasurement.

## Evidence classes and verdicts

Use `19_TESTS/EVAL_EVIDENCE_REGISTRY.json` and the benchmark-forensics classes/verdicts.

Strong promotion to `VERIFIED_TESTED_SCOPE` requires exact artifact/harness/receipt hashes and a complete enough execution envelope for the bounded claim. Otherwise use `PARTIAL`, `NON_REPRODUCIBLE`, `CONCEPTUAL_ONLY`, `INVALIDATED_EVIDENCE`, or `UNKNOWN`.

## Falsifiers

An evaluation conclusion must be downgraded when:
- the harness/receipt hash changes;
- the target implementation changes in a load-bearing way;
- the environment/regime changes beyond declared validity;
- the oracle is found to be circular or incorrect;
- missing negative cases can flip the decision;
- reproduced raw results disagree with the receipt;
- a benchmark claim exceeds the executed target or tested scope.
