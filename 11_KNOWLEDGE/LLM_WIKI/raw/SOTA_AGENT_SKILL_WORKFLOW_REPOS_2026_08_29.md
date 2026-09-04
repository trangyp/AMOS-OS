---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
date: 2026-08-29
epistemic_class: OBSERVATION
provenance: Web search + README snippets; not independently verified
source: web_search
title: SOTA Agent Skill / Workflow / Orchestration Repos — Raw Capture
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: active__AMOS_OS
---

# SOTA Agent, Skill and Workflow Repositories — Raw Capture

Search context: identify public GitHub repositories useful for continuously enhancing AMOS skill/agent/workflow governance.

## Search 1: best skill marketplace multi agent framework github 2026

- `wuyifeishu/nexus-agentos` — AgentOS

  - Universal agent runtime with Skill Marketplace, MCP integration, and TUI.
  - 64 built-in skills across 11 categories, 8 built-in MCP servers, 34 tools out of the box.
  - Sub-agent dispatch; JWT auth for developers; admin review for skill publishing.

- `zjunlp/SkillNet` — Open infrastructure for discovering, evaluating, composing, and orchestrating reusable AI agent skills.

  - 500K+ GitHub skills indexed, improved deduplication, scientific-research and data-analysis skill coverage.
  - Search, install, create, evaluate, organize skills; MCP server support.
  - 2026-03 integration with JiuwenClaw; CycleChain maintains MCP server.

- `songfang/AgentSkillOS` — Build your agent from 90,000+ skills via retrieval & orchestration.

  - Skill search & discovery with skill tree hierarchy.
  - Skill orchestration as DAG with dependency and data-flow management.
  - Built-in GUI for human-in-the-loop control.

- `fpganewbie/SkillNet` — Fork of zjunlp/SkillNet with same search/evaluate/orchestrate scope.

- `tavianm/aidd-framework` — Marketplace of skills, agents, rules for AI-Driven Development.

  - 6 plugins, 31 skills, 3 agents, MIT.
  - Claude Code native; also ships builds for Cursor, GitHub Copilot, Codex, OpenCode.

## Search 2: agentic skills registry orchestration github AgentSkillOS ORPHEUS alternatives

- `nuryslyrt/ORPHEUS` — Orchestrated Runtime Protocol for Hierarchical Execution Unified Skills.

  - Build multi-skill AI systems in seconds from natural language.
  - Orchestrator → Experts → Workers; typed contracts; decision logs; no new infrastructure.

- `gfernandf/agent-skill-registry` — Open registry of reusable AI agent skills and capability definitions.

  - 159 capabilities, 37 skills, validation tooling, machine-readable catalogs.

- `kai98k/agent-skills-registry` — Centralized registry platform for AI Agent Skills (npm/Docker Hub-like).

  - Standardized skill bundles (SKILL.md + scripts/ + references/ + assets/), `agentskills push/pull` CLI.
  - Semver, discoverability, version pinning.

- `yepengfan/agent-registry` — Unified registry for Claude Code agents, orchestrators, skills.

  - Agent/skill/slash-command packages, behaviors, criteria, profiles, installer, discovery.

- `Rainnystone/skill-orchestration-system` — Skill-first CLI for turning agent skills into reviewable, routing-friendly packs.

  - Local skill manager for Codex / Claude Code; vault isolation, workspace packs, local adaptive learning.
  - Reduces active-layer skills by 90% to prevent prompt pollution and context dilution.

## Search 3: self-evolving / trainable skills and deterministic workflow execution

- `zzatpku/AgentFactory` — ACL 2026 System Demonstrations

  - Self-evolving framework that preserves successful task solutions as executable subagent code.
  - Meta-agent decomposes tasks, allocates tool subsets, refines subagents from execution feedback.
  - Skills shipped as Python scripts plus `SKILL.md` documentation; portable to LangChain, AutoGen, Claude Code.

- `microsoft/SkillOpt` — 16.3k stars, MIT

  - Text-space optimizer that trains reusable natural-language skills for frozen LLM agents.
  - Trajectory-driven edits, validation-gated updates, `best_skill.md` artifacts.
  - PyPI package; skill training as epochs/mini-batches/learning rates without touching model weights.

- `linxuhao/SkillFlow` — 3 stars, MIT

  - Deterministic agentic workflow framework; YAML DAG executor with human-in-the-loop checkpoints.
  - Framework Mode (engine drives agents) and Runner Mode (external agent over MCP/CLI).
  - Immutable SQLite audit trace, loops, retries, recovery, event streaming, provider-agnostic.

- `XSkill-Agent/XSkill` — ICML 2026

  - Continual learning from trajectories: task-level Skills + action-level Experiences, no parametric training.
  - Visually-grounded trajectory summarization, cross-rollout critique, hierarchical consolidation.
  - Evaluated on VisualToolBench, TIR-Bench, MMSearch-Plus, AgentVista, MMBrowseComp.

## Search 4: production skill marketplaces and hardened registries

- `tech-leads-club/agent-skills` — 5,087 stars, production skill catalog.

  - Hardened, human-curated skill library with Snyk Agent Scan, lockfiles, content hashing.
  - Multi-agent installer for Claude Code, Cursor, Cline, GitHub Copilot, Windsurf, Aider, etc.
  - Skills grouped in categories (`(development)`, `(cloud)`, `(security)`, etc.); `SKILL.md` + `references/` + `scripts/` + templates.
  - CLI `npx @tech-leads-club/agent-skills` with install/update/list, copy or symlink scope.
  - Strong governance: Verifier pattern (author != verifier), deterministic `scripts/*.py` gates, `STATE.md` decision log.

- `ivanzwb/agent-skills` — TypeScript skill lifecycle framework.

  - Open [Agent Skills Specification](https://agentskills.io/specification) implementation.
  - Progressive loading L0/L1/L2, `manifest.json` tool declarations, dependency installers (npm/pip/extensible).
  - CLI `skill` with install/uninstall/preview/search; GitHub + ClawHub network install.
  - Security: zip-slip detection, path traversal prevention, atomic lockfile, JSON persistent registry.

- `ComeOnOliver/skillshub` — Token-efficient skill resolver API.

  - `skillshub.wtf` search/resolve endpoints: 1 API call returns the best-fit skill for a task.
  - 5,000+ skills indexed from 230+ repos; no auth required for search/fetch; raw `SKILL.md` via `?format=md`.
