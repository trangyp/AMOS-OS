---
title: SOTA Agent Skill / Workflow / Orchestration Repos
type: wiki
source: 11_KNOWLEDGE/LLM_WIKI/raw/SOTA_AGENT_SKILL_WORKFLOW_REPOS_2026_08_25.md
date: '2026-08-25'
epistemic_class: DERIVED
provenance: Synthesized from web_search and README snippets
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: SOTA_AGENT_SKILL_WORKFLOW_REPOS_2026_08_25.md
  scope: AMOS_knowledge
tags:
- llm-wiki
- sota
- agent-skills
- agent-workflows
- orchestration
- github
- llm-wiki-synthesis
---

# SOTA Agent Skill / Workflow / Orchestration Repositories

**Epistemic class:** `DERIVED`  
**Raw source:** [[SOTA_AGENT_SKILL_WORKFLOW_REPOS_2026_08_25]]

## Top pick for skill security / registry hardening

`tech-leads-club/agent-skills` (5.1k★)  
- Designed for safe, validated skill distribution.
- Aligns directly with AMOS guardrail and provenance concerns: lockfiles, content hashing, Snyk scanning, path/symlink guards, audit trails.
- Best candidate for importing skill-lifecycle controls.

## Top pick for production multi-agent orchestration

`microsoft/agent-framework` (13.1k★)  
- Multi-language, production-grade agent and workflow framework.
- Supports durable, observable, graph-based multi-agent patterns: sequential, concurrent, handoff, group collaboration.
- Best candidate for hardening AMOS `amos-workflow-runner` and runtime orchestration.

## Top pick for repository-native agentic CI/CD

`github/gh-aw` — GitHub Agentic Workflows  
- Markdown-defined workflows compiled to GitHub Actions.
- Sandboxed, scoped permissions, `safe-outputs`, threat detection, cost controls.
- Best candidate for publishing AMOS workflows into a CI/CD execution layer.

## Specialized candidates

| Repo | Strength | AMOS fit |
|------|----------|----------|
| `yuzhaopeng-up/skill-framework` | 208-skill inventory, L0–L4 classification, YAML templates | Skill taxonomy and governance checklists |
| `agent-skill-harbor` | Org-wide catalog, recommended/discouraged/prohibited governance | Enterprise skill discovery and provenance |
| `gfernandf/agent-skill-registry` | Declarative capabilities/skills, machine-readable catalogs | Standardized capability vocabulary |
| `yiheng8023/agent-skills-curated` | Reviewed, provenance-tracked, release manifests | Curated third-party skill ingestion |
| `microsoft/conductor` | Deterministic YAML workflows, Jinja2 routing, parallel execution | Multi-agent workflow definition language |
| `agentenv/agentflow` | Large-scale agent graphs, optimization rounds, multi-target execution | Scale-out workflow harnesses |

## Synthesis for AMOS

The strongest near-term integration path is:

1. Adopt `tech-leads-club/agent-skills` guardrail patterns for the `skill_guardrail_checker` pipeline.
2. Study `microsoft/agent-framework` orchestration primitives to enhance `amos-workflow-runner` and `amos-agent-orchestrator`.
3. Mirror `github/gh-aw` for execution-boundary controls and cost governance.

**Confidence ceiling:** 0.85 (derived from README claims and star counts, not empirical benchmarks).

---
**MOC:** [[LLM_WIKI_MOC]]

## 2026-08-29 update

Follow-up scan expanded the candidate pool with five additional high-value repositories.

### Best skill marketplaces and runtimes

| Repo | Strength | AMOS fit |
|------|----------|----------|
| `wuyifeishu/nexus-agentos` | Universal agent runtime + 64 built-in skills + MCP + TUI | Harden AMOS runtime and `.devin/skills` discovery/install |
| `zjunlp/SkillNet` | 500K+ skills, 5-dimension scoring, orchestration, MCP | Import skill-evaluation and relationship-graph tooling |
| `songfang/AgentSkillOS` | 90K+ skills, DAG orchestration, skill tree, GUI | Cross-check skill-retrieval and DAG-composition models |

### Best markdown/native orchestration and registry formats

| Repo | Strength | AMOS fit |
|------|----------|----------|
| `nuryslyrt/ORPHEUS` | Natural-language → multi-skill pipeline; typed contracts; filesystem only | Validate AMOS workflow and contract design patterns |
| `gfernandf/agent-skill-registry` | Declarative capabilities/skills, machine-readable catalogs | Standardize AMOS capability vocabulary and registry export |
| `kai98k/agent-skills-registry` | Skill bundles with `SKILL.md`, semver, push/pull CLI | Align skill-bundle packaging with `amos-skill-builder` |
| `yepengfan/agent-registry` | Claude Code native agent/skill/orchestrator registry | Compare install/routing conventions for agents |
| `Rainnystone/skill-orchestration-system` | Local skill packs, vault isolation, workspace routing | Reduce prompt-pollution for large `.devin/skills` trees |
| `tavianm/aidd-framework` | 31 skills, 3 agents, Claude/Cursor/Copilot builds | Reference multi-format skill distribution |

### Updated near-term integration priorities

1. **SkillNet** for the largest evaluatable skill corpus and community scoring.
2. **AgentOS** if AMOS needs a runtime marketplace with MCP integration.
3. **ORPHEUS** to benchmark AMOS workflow contracts and markdown-first orchestration.
4. **agent-skill-registry** / **agent-skills-registry** for vocabulary and bundle standards.

Raw capture: [[SOTA_AGENT_SKILL_WORKFLOW_REPOS_2026_08_29]]

**Confidence ceiling:** 0.80 (derived from README claims; not independently benchmarked).
