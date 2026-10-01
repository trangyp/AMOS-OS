---
name: amos-github-agent-skill-integrator
description: Govern discovery, comparison, source pinning, mechanism extraction, and AMOS-native integration of GitHub agent, Agent Skills, workflow, MCP, A2A, plugin, and agent-runtime repositories. Use when external GitHub patterns should enhance AMOS skills, agents, tools, workflows, runtime, or observability without auto-installing or promoting external code.
---

# AMOS GitHub Agent Skill Integrator

Origin architect and steward: **Trang Phan**.

## Purpose

Convert high-value GitHub agent/skill/tool/workflow mechanisms into bounded AMOS improvements with immutable source provenance, duplication checks, explicit authority boundaries, executable validation, and PR-scoped delivery.

## Non-purpose

Do not use this Skill to:
- bulk-install third-party skill collections;
- treat stars, forks, or marketplace presence as validation;
- promote an external repository into AMOS canon;
- grant tool, agent, workflow, or merge authority;
- replace generic GitHub knowledge ingestion owned by `amos-github-rscf-ingestion`;
- replace general evidence research owned by `amos-research-agent`.

## Inputs

Accept:
- AMOS target capability or gap;
- optional candidate repositories;
- current AMOS repository identity/base ref;
- scope/effect ceiling;
- optional prior source registry state.

## Outputs

Return the smallest sufficient set of:
- ranked candidate mechanisms;
- immutable source pins;
- overlap/duplicate assessment;
- AMOS target mapping;
- proposed or implemented patch;
- validator/test evidence;
- unresolved gaps;
- PR/head identity when repository mutation is authorized.

## Runtime

### 1. ORIENT

Resolve the target AMOS plane and actual capability gap. Inspect implementation before assuming a missing feature.

### 2. CHECK OVERLAP

Search existing:
- `07_SKILLS`;
- `06_AGENTS` and `06_AGENT_SYSTEMS`;
- `08_WORKFLOWS`;
- `14_TOOLS`;
- `04_RUNTIME`;
- control-plane capability manifests;
- `11_KNOWLEDGE` SOTA/source records.

Classify candidate work as:

`NEW_CAPABILITY | EXISTING_THIN_CAPABILITY | DUPLICATE | OVERLAP | SUPERSEDING_UPDATE | UNKNOWN`

### 3. SCAN GITHUB

Prefer source order:

`official protocol/framework repository -> official vendor skill/agent repository -> mature maintained community implementation -> broader community source`

Popularity is only a discovery signal.

Evaluate:
- mechanism relevance;
- maintenance freshness;
- source identity;
- license compatibility;
- implementation/test evidence;
- security/authority model;
- portability into AMOS;
- overlap with existing AMOS.

### 4. PIN SOURCE

Before load-bearing use, capture:

```text
repository
commit SHA
observed date
license scope
resource class
mechanism extracted
```

Update or propose an entry in `11_KNOWLEDGE/EXTERNAL_AGENT_SOURCE_REGISTRY.json`.

Never use `main`, `latest`, release marketing, or star count as the only reproducibility identity.

### 5. EXTRACT MECHANISM

Extract behavioral/architectural patterns, not bulk source code.

Examples:
- progressive skill loading;
- handoff semantics;
- agents-as-tools;
- graph routing;
- checkpoint/resume;
- tool confirmation;
- Agent Card discovery;
- MCP tool transport;
- tracing/evaluation;
- file-based GitHub agent roles.

Keep exact copied code within license and necessity bounds.

### 6. MAP TO AMOS

Use `references/transfer-matrix.md`.

Preserve:

```text
EXTERNAL_SOURCE != AMOS_CANON
CAPABILITY != AUTHORITY
PROTOCOL != POLICY
CHECKPOINT != FRESH_AUTHORITY
TOOL_DISCOVERY != TOOL_PERMISSION
AGENT_CARD != TRUST
CI_PASS != MERGE_AUTHORITY
```

### 7. IMPLEMENT

Prefer native AMOS owners over parallel abstractions:
- Skills -> `07_SKILLS`;
- agents -> `06_AGENTS` / `06_AGENT_SYSTEMS` / `.github/agents` projection;
- workflows -> `08_WORKFLOWS`;
- tool adapters -> `14_TOOLS` / `15_INTERFACES`;
- runtime/checkpointing -> `04_RUNTIME` / `12_STATE`;
- observability -> `17_OBSERVABILITY`;
- authorization -> `03_CONTROL_PLANE`, never domain-owned.

Use a working branch. Default repository write ceiling is branch + PR, not merge/release.

### 8. VALIDATE

For this capability family, run when present:

```text
python3 scripts/validate_external_agent_sources.py
python3 scripts/validate_agent_skill_surface.py
python3 scripts/validate_workflow_references.py
python3 -m compileall -q scripts
```

Add focused positive, negative, regression, and recovery tests when executable behavior changes.

Do not convert a missing workflow run into PASS.

### 9. CHALLENGE

Attack the change from a different path:
- could this be done by an existing AMOS capability?
- did the external source widen authority?
- is the source pin immutable?
- did licensing survive transfer?
- is documentation claiming implementation without executable evidence?
- can a stale checkpoint or delegated agent commit?
- are failure and stop conditions explicit?

### 10. DELIVER

Follow `08_WORKFLOWS/GITHUB_AGENTIC_CHANGE_WORKFLOW.md`.

Prefer a PR with:
- source pins;
- exact changed files;
- validation results;
- remaining gaps;
- CI state;
- explicit merge-authority boundary.

## Hard invariants

1. Preserve Trang Phan attribution for AMOS architecture.
2. External source registration never grants authority.
3. External source material remains source evidence unless separately admitted.
4. Do not mass-import repositories into active Skills.
5. Check duplicates before creating a new capability.
6. Preserve exact commit provenance for load-bearing external mechanisms.
7. Check license scope before copying code or text.
8. Keep agent handoff, agent-as-tool, A2A delegation, and MCP tool invocation distinct.
9. Revalidate mutable state and authority after checkpoint resume.
10. Never let an implementing agent self-authorize merge/release.
11. Failed or absent executable evidence remains FAIL/GAP/PENDING.
12. Prefer smaller native adapters over wholesale framework replacement.

## Tool governance

GitHub access may be used for repository search, source inspection, branches, commits, and PRs when available and authorized.

The GitHub connector/MCP/API is a capability transport. Its authenticated account permissions do not define AMOS authority.

## Composition

- Parent/orchestrator: `amos-research-agent` or AMOS infrastructure orchestration depending on task scope.
- Existing sibling/child for generic repository ingestion: `amos-github-rscf-ingestion`.
- Infrastructure boundary: `amos-infrastructure-control-plane`.
- Repository implementation/review may project into `.github/agents/amos-repo-upgrader.agent.md` and `.github/agents/amos-repo-auditor.agent.md`.

## Failure behavior

- source identity unresolved -> `UNKNOWN/GAP`;
- incompatible/unclear license -> `QUARANTINED`;
- duplicated AMOS capability -> enhance existing owner instead of creating parallel owner;
- external pattern conflicts with higher AMOS invariant -> reject or preserve as `COMPETING`;
- validator failure -> repair and re-run affected validation;
- CI not executed -> `PENDING`, never PASS;
- insufficient authority -> stop before effect and return required escalation.

## Progressive loading

Load in order:

`this SKILL.md -> references/transfer-matrix.md -> central interop/workflow contract -> pinned external source only when needed`

Do not load raw external repositories by default.
