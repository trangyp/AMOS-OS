---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
name: sota
title: sota
description: Reference document for amos-mdformat-obsidian
type: reference
parent_skill: amos-mdformat-obsidian
source: 07_SKILLS/amos-mdformat-obsidian/references
tags:
  - reference
  - sota
  - mdformat-obsidian
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

## SOTA Regression Prevention (2026)

> **Source**: The Regression Tax (arxiv 2607.22520) — skills can make agents worse via 3 modes. Reliability depends more on grounding and verification than procedural skill choice.

### Mode 1: Description Osmosis Guard

A skill changes agent behavior just by being present in context, even when never invoked.

**Guard**: This skill's description is scoped to its exact trigger conditions. When not triggered, the skill MUST NOT influence agent behavior. Agents MUST NOT apply this skill's procedures to tasks outside its declared scope, even if the skill content is loaded in context.

### Mode 2: Grounding Displacement Guard

A skill's prescribed procedure overrides how the agent interprets its inputs.

**Guard**: This skill's procedure MUST NOT override input interpretation. The agent MUST ground all reasoning in the actual input data, user intent, and observed context — not in the skill's procedural assumptions. If the skill's procedure conflicts with input evidence, input evidence wins. The skill provides HOW to reason, not WHAT to reason about.

### Mode 3: Verification Displacement Guard

A skill's procedure suppresses checks the agent would otherwise perform on its outputs.

**Guard**: This skill MUST NOT suppress post-execution verification. After executing this skill's procedure, the agent MUST independently verify: (1) output matches input intent, (2) output is internally consistent, (3) output does not exceed declared scope, (4) epistemic class labels are accurate. Verification is mandatory, not optional.

## SOTA Grounding Support (2026)

> **Source**: The Regression Tax (arxiv 2607.22520) — grounding displacement is the dominant source of persistent failures. Skills over-support procedure and under-support grounding.

### Input-Grounded Reasoning

All outputs from this skill MUST be grounded in:

1. **Input data**: The actual data provided, not the skill's assumptions about what data should look like
1. **User intent**: What the user actually asked for, not what the skill assumes they want
1. **Observed context**: The real state of the world, not the skill's model of it
1. **Source evidence**: Vault sources, empirical data, or established math — not the skill's internal logic

### Grounding Checks (execute before output)

- [ ] Does the output reference actual input data, not assumed data?
- [ ] Does the output address the actual user request, not a template request?
- [ ] Does the output reflect the current state, not a stale snapshot?
- [ ] Are claims traced to source evidence with provenance?

If any check fails, downgrade confidence and flag as GROUNDING_GAP.

## SOTA Data Trustworthiness (2026)

> **Source**: Atlan/UC Irvine 2026 study — 99% of SKILL.md files have at least one flaw; the 6th practice (data trustworthiness) is named by zero conventional guides.

### Data Trustworthiness Checks

Before applying this skill's outputs, validate:

1. **Freshness**: Is the source data current? Check `content_hash` and vault modification dates. If source is >90 days old and domain is fast-moving, flag as STALE_SOURCE.
1. **Ownership**: Is the source owned by a recognized authority? Vault canon (Trang Phan) = SOURCE_CANON. External papers = SOURCE_CLAIM. User-provided = OBSERVATION. Unattributed = UNKNOWN/GAP.
1. **Certification**: Has the source been validated? Validated sources have `content_hash` matches. Unvalidated sources require independent corroboration (2+ sources) before consolidation.
1. **Integrity**: Has the source been modified since last validation? If `content_hash` mismatches recomputed hash, flag as INTEGRITY_GAP and trigger revalidation.

### Trustworthiness Decision

- SOURCE_CANON + fresh + integrity_verified = TRUSTED (confidence ceiling: 1.0)
- SOURCE_CLAIM + fresh + integrity_verified = RELIABLE (confidence ceiling: 0.95)
- SOURCE_CLAIM + stale or integrity_unverified = CONDITIONAL (confidence ceiling: 0.7)
- UNKNOWN/GAP + any = UNTRUSTED (confidence ceiling: 0.5, require human review)

## SOTA Evaluation Contract (2026)

> **Source**: AEVAL (arxiv 2607.16345) — deterministic, reproducible test pipeline. ACES (arxiv 2608.20614) — paired live trials with and without skill.

### Eval Contract

```yaml
eval_contract:
  skill_name: amos-mdformat-obsidian
  test_tasks:
    - id: basic_trigger
      input: "Query matching this skill's domain"
      expected: "Structured output with epistemic labels and provenance"
    - id: scope_violation
      input: "Query outside this skill's domain"
      expected: "Reject and route to parent skill"
    - id: grounding_check
      input: "Query with insufficient evidence"
      expected: "Flag as GROUNDING_GAP, downgrade confidence"
    - id: regression_osmosis
      input: "Query that should NOT trigger this skill"
      expected: "Skill does not influence output when not triggered"
  grading:
    executor_grader_separation: true
    first_attempt_grading: true
    self_correction_tracking: true
  metrics:
    - skill_lift: "improvement over baseline without skill"
    - regression_rate: "tasks that worsened with skill"
    - grounding_fidelity: "outputs grounded in actual input"
    - verification_completeness: "post-execution checks performed"
```

### Regression Test Protocol

1. Run paired trials: with-skill vs without-skill
1. Measure Skill Lift (improvement) and Regression (worsening)
1. Track 3 regression modes: osmosis, grounding displacement, verification displacement
1. If regression rate > 10%, flag skill for review
1. Executor and grader MUST be structurally separated (no self-grading bias)
