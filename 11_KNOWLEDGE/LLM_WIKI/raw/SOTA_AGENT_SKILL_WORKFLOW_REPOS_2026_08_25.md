---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: SOTA Agent Skill / Workflow / Orchestration Repos — Raw Capture
source: web_search
date: '2026-08-25'
epistemic_class: OBSERVATION
provenance: Web search + README snippets; not independently verified
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: active__AMOS_OS
---

# SOTA Agent, Skill and Workflow Repositories — Raw Capture

Search context: identify public GitHub repositories useful for continuously enhancing AMOS skill/agent/workflow governance.

## Search 1: agent workflow governance skill registry 2026

- `tech-leads-club/agent-skills` — 5.1k stars

  - Hardened skill registry for AI coding agents.
  - Claims 100% open source, static analysis in CI, immutable integrity via lockfiles and content hashing, human-curated prompts.
  - CLI with path isolation, symlink guards, atomic lockfile, audit trail.
  - Scanned with Snyk Agent Scan before publishing.

- `yuzhaopeng-up/skill-framework` — 1 star, MIT

  - L0–L4 skill classification; 208-skill inventory; YAML templates.
  - Quality gates, Python lint/scan/backfill tools.

- `agent-skill-harbor` (npm registry / org-wide catalog)

  - Skill governance for companies; discovery for teams.
  - Marks skills as recommended/discouraged/prohibited; provenance tracking.
  - Git-native, backend-less, workflow-friendly.

- `gfernandf/agent-skill-registry` — 2 stars, Apache-2.0

  - Open registry of reusable AI agent skills and capability definitions.
  - Declarative capabilities, composable skills/workflows, shared vocabulary.

- `yiheng8023/agent-skills-curated`

  - Reviewed cross-agent skills, provenance, capability topology, adaptive harness governance.

## Search 2: agent workflow orchestration framework 2026

- `microsoft/agent-framework` — 13.1k stars, MIT

  - Multi-language (Python, .NET, Go) framework for building, orchestrating and deploying production-grade AI agents and multi-agent workflows.
  - Graph-based patterns: sequential, concurrent, handoff, group collaboration.
  - Checkpointing, streaming, human-in-the-loop, time-travel, durability, observability.

- `github/gh-aw` — GitHub Agentic Workflows

  - Define AI-powered repository automation in Markdown with YAML frontmatter.
  - Run agents securely through GitHub Actions.
  - Sandboxed by default; `safe-outputs` jobs; scoped permissions; threat detection.
  - Supports GitHub Copilot, Claude Code, OpenAI Codex, Google Gemini, Pi.

- `microsoft/conductor`

  - CLI tool for defining and running multi-agent workflows with GitHub Copilot SDK and Anthropic Claude.
  - Deterministic, repeatable, source-controlled YAML-based workflows.
  - Jinja2 routing, parallel execution, sub-workflow composition, script/set/terminate steps.

- `agentenv/agentflow` — 1.4k stars, MIT

  - Orchestrate thousands of agents/harnesses as dependency graphs.
  - Codex, Claude, Kimi, Pi support; parallel fanout, iterative cycles.
  - Local Docker, SSH, EC2, ECS targets; graph optimization rounds.

## Search 3: self-evolving / trainable skills and deterministic workflow execution 2026-08-29

- `zzatpku/AgentFactory` — ACL 2026 System Demonstrations

  - Self-evolving framework that preserves successful task solutions as executable subagent code.
  - Meta-agent decomposes tasks, allocates tool subsets, refines subagents from execution feedback.
  - Skills shipped as Python scripts plus `SKILL.md` documentation; portable to LangChain, AutoGen, Claude Code.
  - AMOS fit: skill evolution loop, execution feedback, canonical `SKILL.md` packaging.

- `microsoft/SkillOpt` — 16.3k stars, MIT

  - Text-space optimizer that trains reusable natural-language skills for frozen LLM agents.
  - Trajectory-driven edits, validation-gated updates, `best_skill.md` artifacts.
  - PyPI package; skill training as epochs/mini-batches/learning rates without touching model weights.
  - AMOS fit: skill quality gates, versioned best-skill artifacts, validation-before-promotion.

- `linxuhao/SkillFlow` — 3 stars, MIT

  - Deterministic agentic workflow framework; YAML DAG executor with human-in-the-loop checkpoints.
  - Framework Mode (engine drives agents) and Runner Mode (external agent over MCP/CLI).
  - Immutable SQLite audit trace, loops, retries, recovery, event streaming, provider-agnostic.
  - AMOS fit: deterministic workflow runtime, durable audit trace, MCP gateway.

- `XSkill-Agent/XSkill` — ICML 2026

  - Continual learning from trajectories: task-level Skills + action-level Experiences, no parametric training.
  - Visually-grounded trajectory summarization, cross-rollout critique, hierarchical consolidation.
  - Evaluated on VisualToolBench, TIR-Bench, MMSearch-Plus, AgentVista, MMBrowseComp.
  - AMOS fit: trajectory-to-skill distillation, experience memory, multimodal skill extraction.
