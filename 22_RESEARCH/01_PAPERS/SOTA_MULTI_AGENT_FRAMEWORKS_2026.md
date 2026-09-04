---
title: SOTA Multi-Agent Frameworks 2026
type: research_synthesis
source: 22_RESEARCH/01_PAPERS
tags:
  - sota
  - multi-agent
  - agent-framework
  - orchestration
  - coordination
  - research
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: web_search_2026-09-04
  scope: multi_agent_frameworks_2026
  freshness: 2026-09-04
  falsifier: "Multi-agent framework performance validated on benchmarks — production deployment at scale NOT ESTABLISHED"
---

# SOTA Multi-Agent Frameworks 2026

**Date:** 2026-09-04
**Epistemic class:** SOURCE_CLAIM (arXiv + GitHub)
**Confidence ceiling:** 0.85

## 1. ROMA — Recursive Open Meta-Agents (arXiv:2602.01848)

- **Architecture:** Recursive task decomposition with 4 modular roles
  - **Atomizer:** Decides whether to decompose
  - **Planner:** Creates execution plan
  - **Executor:** Runs tasks
  - **Aggregator:** Compresses and validates results
- **Performance:** 9.9% accuracy improvement on SEAL-0 (GLM-4.6 vs Kimi-Researcher)
- **Model-agnostic:** Mix models by cost, latency, capability
- **Prompt optimization:** GEPA+ (Genetic-Pareto prompt proposer)
- **AMOS binding:** `06_AGENTS` · `03_CONTROL_PLANE` — recursive agent decomposition

## 2. MASFactory — Vibe Graphing (arXiv:2603.06007)

- **Innovation:** Natural language → editable workflow spec → executable graph
- **Features:** Reusable components, skill support, multimodal messages, plug-in context
- **Human-in-loop:** Visualizer for topology preview, runtime tracing, interaction
- **AMOS binding:** `08_WORKFLOWS` — NL-to-workflow compilation

## 3. OpenHive — Colony Architecture (GitHub 2026)

- **Pattern:** Queen + worker clones; one loop controlling many loops
- **Coordination:** Shared ledger + persistent plan (no data buffer)
- **Safety:** Crash-safe park/resume, cost enforcement, human-in-loop (Sentinel)
- **Growth:** Colony grows at runtime; no graph to wire
- **AMOS binding:** `06_AGENTS` · `12_STATE` — organic agent colony coordination

## 4. Open Multi-Agent (OMA) (GitHub 2026)

- **Pattern:** Dynamic DAG from goal; coordinator plans at runtime
- **Control:** Preview, approve, suspend plans, dispatches, tool calls
- **Models:** Claude, ChatGPT, Gemini, DeepSeek, local models
- **AMOS binding:** `06_AGENTS` · `03_CONTROL_PLANE` — dynamic goal-to-graph orchestration

## 5. Cornucopia Multi-Agent (GitHub 2026)

- **Modes:** 6 collaboration modes, 8 tools, 4 execution paths
- **Range:** Sequential → LLM-driven deep clustering → dynamic workflows
- **AMOS binding:** `08_WORKFLOWS` — full-spectrum agent collaboration

## AMOS Architecture Mapping

| Framework Component | AMOS Plane | Mapping |
|---------------------|-----------|---------|
| ROMA Atomizer (decompose?) | `03_CONTROL_PLANE` | Mutation classification (M0-M5) |
| ROMA Planner | `03_CONTROL_PLANE` | Commit orchestrator |
| ROMA Executor | `04_RUNTIME` | Runtime execution |
| ROMA Aggregator | `amos-convergence-detection` | Result convergence |
| MASFactory Vibe Graphing | `08_WORKFLOWS` | NL-to-workflow builder |
| OpenHive Queen + workers | `06_AGENTS` | Master skill + specialized agents |
| OpenHive shared ledger | `12_STATE` | Agent state coordination |
| OMA dynamic DAG | `03_CONTROL_PLANE` | Runtime plan generation |
| Crash-safe park/resume | `amos-rollback-recovery` | State recovery |
| Cost enforcement | `amos-token-budget-governance` | Resource budgeting |

## Falsifiers

- `F-MA-1`: ROMA 9.9% improvement on specific benchmarks — AMOS multi-domain generalization NOT ESTABLISHED
- `F-MA-2`: MASFactory Vibe Graphing NL-to-graph — correctness of generated graphs for complex workflows NOT ESTABLISHED
- `F-MA-3`: OpenHive crash-safe claims — formal verification NOT ESTABLISHED
- `F-MA-4`: OMA dynamic DAG — plan quality for long-horizon tasks NOT ESTABLISHED
- `F-MA-5`: All frameworks are open-source — production-scale deployment reliability NOT ESTABLISHED

**Parent:** [[22_RESEARCH/01_PAPERS/SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026|SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026]] · [[22_RESEARCH/22_RESEARCH_README|22_RESEARCH_README]]
