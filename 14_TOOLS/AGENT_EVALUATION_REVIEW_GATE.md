---
title: AMOS Agent Evaluation Review Gate
type: tool-contract
origin_architect: Trang Phan
status: IMPLEMENTED_LOCAL_REFERENCE
epistemic_class: AMOS_MODEL
---

# AMOS Agent Evaluation Review Gate

Tool ID: `amos-agent-evaluation-review`

## Purpose

Validate trajectory-aware evaluation evidence, post-tool review decisions, sampling coverage, judge disagreement, frozen-axis run comparability, and harness-mutation verdicts without granting runtime, merge, deployment, or canonical-promotion authority.

## Local capability envelope

Tier: `T1` local deterministic validation.

Capabilities:

- `EVAL_RUN_VALIDATE`
- `REVIEW_RECORD_VALIDATE`
- `JUDGE_DISAGREEMENT_AUDIT`
- `SAMPLING_COVERAGE_AUDIT`
- `BASELINE_CANDIDATE_COMPARE`
- `HARNESS_MUTATION_VERDICT`
- `EVAL_RECEIPT_VALIDATE`

External model judges, hosted eval runners, or benchmark services are separate T3 operations and require separately available credentials/authority.

## Firewalls

- `REVIEW_DECISION != RUNTIME_AUTHORITY`
- `EVALUATION != INTERVENTION_AUTHORITY`
- `MODEL_JUDGE_SCORE != GROUND_TRUTH`
- `SAMPLED_PASS != COMPLETE_PASS`
- `SCORE_DELTA != CAUSAL_ATTRIBUTION`
- `KEEP_VERDICT != MERGE_AUTHORITY`
- `ROLLBACK_VERDICT != ROLLBACK_EXECUTION_AUTHORITY`
- `EVAL_RECEIPT != DEPLOYMENT_VALIDITY`
- `HASH_MATCH != TRUST`

## Executable evidence

Canonical deterministic surfaces:

- `07_SKILLS/amos-interactive-evaluation-design-rscf/scripts/evaluation_runtime.py`
- `07_SKILLS/amos-interactive-evaluation-design-rscf/scripts/evaluation_contract_check.py`
- `19_TESTS/test_agent_evaluation_runtime.py`

Validated scope is local SQLite/reference evaluation semantics only. External judge correctness, production benchmark validity, and deployment decisions remain independently governed.
