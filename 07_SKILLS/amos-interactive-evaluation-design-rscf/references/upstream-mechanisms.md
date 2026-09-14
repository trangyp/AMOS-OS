# Upstream mechanism provenance

External mechanisms are `SOURCE_CLAIM` until independently executed inside AMOS. No upstream code is vendored by this Skill.

## Inspect AI

Pinned source: `UKGovernmentBEIS/inspect_ai@1276f419913248bdb4c7c41a8e2274a396e97083`.

Adapted mechanism:
- post-tool result review occurs after a tool executes and before the model consumes the result;
- review decisions are `continue | terminate | escalate`;
- review identity/explanation can be persisted as a separate event.

AMOS boundary:
- review-flow decision is not tool authorization, runtime privilege, or external-effect finality.

## OpenAI monitorability-evals

Pinned source: `openai/monitorability-evals@d14f181a0623f7949fdb2d8c3f15874115fa44ba`.

Adapted mechanisms:
- keep intervention, process, and outcome-property evaluations distinct;
- paired perturbation designs require identity linkage across perturbed/unperturbed rows;
- monitor/grader mismatch can invalidate an evaluation rather than being averaged away;
- tool/resource monitorability requires explicit provenance and limitation handling.

AMOS boundary:
- monitor labels are evaluator evidence, not ground truth or deployment validity.

## Promptfoo

Pinned source: `promptfoo/promptfoo@ad3bee3299e3a9864ef6d47482298b2e7f1ceb37`.

Adapted mechanisms:
- bind assertions/thresholds to explicit configs;
- keep execution metadata and provider/runtime identity with results;
- choose an execution provider according to the runtime boundary under evaluation;
- treat red-team/generated cases as configured evidence inputs.

AMOS boundary:
- runner pass/fail does not replace AMOS evidence/authority gates.

## OpenHands Benchmarks

Pinned source: `OpenHands/benchmarks@405bae7140d7e961a75f4910a0b2e7069731db96`.

Adapted mechanisms:
- benchmark environment identity must be content/version bound;
- duplicated/forked environment setup can silently drift and break comparability;
- use one shared build path where possible and bound retry behavior.

AMOS boundary:
- comparable environment identity is necessary for attribution but not sufficient for causal proof.

## AMOS harness evolution

Internal companion Skill: `amos-observability-driven-harness-evolution-rscf`.

Use its rules to freeze base model/evaluator/budget, record predicted fixes/regressions before mutation, test the next round, and preserve rollback. This evaluation Skill supplies deterministic review/comparison evidence; it does not self-authorize harness mutation or promotion.
