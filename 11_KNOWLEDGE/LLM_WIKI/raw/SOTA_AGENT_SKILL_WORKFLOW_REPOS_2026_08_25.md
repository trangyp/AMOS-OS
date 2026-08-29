---
title: SOTA Agent Skill / Workflow / Orchestration Repos — Raw Capture
source: web_search
date: '2026-08-25'
epistemic_class: OBSERVATION
provenance: Web search + README snippets; not independently verified
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
