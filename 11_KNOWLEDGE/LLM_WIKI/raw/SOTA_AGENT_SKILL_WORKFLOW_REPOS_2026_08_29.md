---
date: 2026-08-29
epistemic_class: OBSERVATION
provenance: Web search + README snippets; not independently verified
source: web_search
title: SOTA Agent Skill / Workflow / Orchestration Repos — Raw Capture
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
