---
title: amos-github-rscf-ingestion-workflow
type: workflow
source: 26_WORKFLOWS
Skill: amos-github-rscf-ingestion
Agent: amos-github-rscf-ingestion-agent
Version: 2.0.0
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
hml_level: M
---

# Workflow: AMOS GitHub RSCF Ingestion

## Objective

Turn a GitHub discovery or repository into a bounded AMOS integration decision while preserving source identity, security boundaries, competing alternatives, and implementation evidence.

## States

`INTAKE -> DISCOVER -> MAP -> EXTRACT -> COMPARE -> SECURITY_REVIEW -> DECIDE -> TEST -> OUTPUT`

Possible terminal states:

- `REJECTED`
- `WATCH`
- `QUARANTINED`
- `ADAPTATION_PROPOSED`
- `TEST_READY`
- `PROMOTION_CANDIDATE`
- `UNKNOWN/GAP`

No workflow state directly means deployed or canonically approved.

## Preconditions

- `amos-github-rscf-ingestion` is available.
- GitHub read capability is available through a governed adapter.
- Research question or AMOS gap is explicit.
- Source identity can be bound to repository + ref/commit before promotion.

## Steps

### 1. INTAKE

Define the AMOS gap, affected owner, desired capability, freshness requirement, and consequence level. If no concrete gap exists, stop at research/watch mode rather than accumulating repositories.

### 2. DISCOVER

Search candidate repositories. Stars and trend position are discovery signals only. Prefer primary/official repositories and current maintained sources.

### 3. MAP

For each serious candidate inspect README/manifests, architecture, entrypoints, dependencies, tests, workflows, security policy, and the smallest relevant implementation files.

### 4. EXTRACT

Produce a knowledge cell:

`mechanism + assumptions + dependencies + invariants + failure modes + provenance + falsifiers`

Do not bulk-copy source code.

### 5. COMPARE

Compare against:
- existing AMOS capability;
- competing repositories/mechanisms;
- integration complexity;
- evidence/test strength;
- security and license constraints;
- expected reduction in search/state/execution/verification cost.

If AMOS already has an adequate owner, improve that owner rather than creating a duplicate.

### 6. SECURITY_REVIEW

For skills, agents, hooks, MCP/tool configs, workflows, and executable assets:
- bind immutable source ref;
- review license/dependencies;
- inspect prompt injection and instruction override risk;
- inspect credential/data-exfiltration paths;
- inspect hidden download/eval/subprocess behavior;
- inspect excessive tool/filesystem/network authority;
- inspect cross-skill composition risk.

HIGH/CRITICAL unresolved risk -> `QUARANTINED` or `REJECTED`.

### 7. DECIDE

Return one of: `REJECT`, `WATCH`, `QUARANTINE`, `ADAPT`, `TEST`, `PROMOTE_CANDIDATE`.

A decision must cite the source commit/ref and the AMOS owner/gap addressed.

### 8. TEST

For adapted mechanisms run, as applicable:
- structural validation;
- correctness tests;
- negative/adversarial tests;
- regression tests;
- replay/idempotency checks;
- recovery/rollback checks;
- benchmark reproduction under comparable conditions.

Do not weaken a failed gate merely to obtain PASS.

### 9. OUTPUT

Emit:

```yaml
status: REJECTED | WATCH | QUARANTINED | ADAPTATION_PROPOSED | TEST_READY | PROMOTION_CANDIDATE | UNKNOWN/GAP
source:
  repository: owner/name
  ref: immutable_commit_or_tag
amos_owner: path_or_capability
gap_addressed: string
mechanisms: []
assumptions: []
dependencies: []
security_findings: []
competing_alternatives: []
tests: []
falsifiers: []
unresolved_gaps: []
confidence_ceiling: number
```

## Failure and recovery

- repository/ref unresolved -> `UNKNOWN/GAP`;
- content truncated -> fetch targeted source before exact claims;
- license unclear -> quarantine code reuse;
- docs contradict implementation -> preserve contradiction and use executable evidence for implementation claims;
- ambiguous external effect -> do not retry blindly; reconcile first;
- upstream drift -> selectively invalidate dependent findings and re-run affected steps.

## Parallelism

Independent repository candidates may be researched in parallel. Integration decisions merge only after candidate evidence is normalized to the same comparison fields. Shared-state repository writes are not part of this read/research workflow and require separate authority.

## Provenance

- Skill: `07_SKILLS/amos-github-rscf-ingestion/SKILL.md`
- Agent: `06_AGENTS/amos-github-rscf-ingestion-agent.json`
- Tool adapter: `14_TOOLS/GITHUB_REPOSITORY_RESEARCH_ADAPTER.md`
- GitHub-native agents: `.github/agents/`

**MOC:** [[26_WORKFLOWS/26_WORKFLOWS_MOC|26_WORKFLOWS_MOC]]
