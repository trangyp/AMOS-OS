---
title: AMOS AGENT SKILL INDEX
tags:
- canon-group/tech-ai
- canon/framework
- rscf/state/observation
- topic/amos-agent-skill-index
- amos-general
type: document
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture
---


# AMOS Agent Skill Index

**Date:** 2026-08-22
**Purpose:** One-stop index mapping all 36 canonical AMOS agents to their operational Hermes skills, per-agent patterns, law emphases, and collaboration chains.

## System → Skill → Agents Map

| System | Hermes Skill | Agents | Dominant Law | Mandatory Gates |
|--------|--------------|--------|--------------|-----------------|
| BRAIN_SYSTEM | amos-brain-agent | Architecture, Decomposer, Planner, Reflection, Strategist | L4 (structural integrity) | Rule of 2 on all conclusions |
| EXECUTION_SYSTEM | amos-execution-agent | Automation, Coding, Deployment, DevOps, Document, Refactor, Writing | L4 + L5 | IP-safe output modes |
| LEGAL_SYSTEM | amos-legal-agent | Compliance, Contract, IP, Legal, LegalRisk | L1 (Law of Law) | Legal disclaimer ALWAYS |
| MONEY_SYSTEM | amos-finance-agent | Cashflow, Finance, FinanceRisk, Investment, MacroAnalyst, Opportunity | L4 (model integrity) | Financial disclaimer ALWAYS |
| SENSE_SYSTEM | amos-sense-agent | Context, Sensors, StateSummarizer | L4 (provenance/freshness) | Epistemic class labelling |
| WORLD_MODEL_SYSTEM | amos-world-model-agent | GeoAnalyst, MacroAnalyst(WM), SectorAnalyst, Shock, Trend | L2 (competing scenarios) | Uncertainty bands on projections |
| LIFE_SYSTEM | amos-life-agent | Health, LoadBalancer, Routine | L1 (no medical replacement) + L6 (UBI) | Health disclaimer ALWAYS; autonomy check |

Orchestration layer: amos-agent-orchestration (routing/conflict), amos-agent-execution (loop/output modes), amos-agent-reflective (audit/gaps).

## Collaboration Chains (documented in skills)

1. **Analysis chain:** Context_Agent → Trend_Agent → SectorAnalyst_Agent → Finance_Agent → StateSummarizer_Agent
2. **Risk chain:** Trend_Agent → Shock_Agent → MacroAnalyst(WM)_Agent → FinanceRisk_Agent → LegalRisk_Agent
3. **Build chain:** Decomposer_Agent → Planner_Agent → Architecture_Agent → Coding_Agent → Refactor_Agent → DevOps_Agent → Deployment_Agent
4. **Wellbeing chain:** Emotion-analysis → Health_Agent → LoadBalancer_Agent → Routine_Agent
5. **Strategy chain:** Strategist_Agent → Context_Agent → Opportunity_Agent → Planner_Agent → Reflection_Agent

## Per-Agent Quick Reference

### BRAIN_SYSTEM
- Architecture_Agent: components → relationships → evaluation → ADR documentation. Kernels: K_META_LOGIC+K_TECH_ENGINE+K_UNIPOWER_TECH.
- Decomposer_Agent: MECE decomposition, hidden sub-questions, dependency sequencing. Kernels: K_META_LOGIC+K_MATH_COMPUTE.
- Planner_Agent: steps → dependencies → resources → roadmap with milestones. Kernels: K_META_LOGIC+K_MATH_COMPUTE+K_MIND_BEHAVIOR.
- Reflection_Agent: L1-L6 audit → gaps → weaknesses → contradictions → prioritised improvements. Kernel: K_META_LOGIC.
- Strategist_Agent: actors/incentives → coalitions → game-theory analysis → strategic recommendations. Kernels: K_META_LOGIC+K_MIND_BEHAVIOR+K_MATH_COMPUTE.

### EXECUTION_SYSTEM
- Coding_Agent: requirements → design → generate → review → document. Security and quality gates.
- DevOps_Agent: infra needs → CI/CD design → observability → health monitoring.
- Writing_Agent: audience/tone → draft → expression overlay → clarity review.

### LEGAL_SYSTEM (all carry disclaimer)
- Compliance: framework → requirements → gap analysis → remediation.
- Contract: obligations → rights → risks/issues → negotiation recommendations.
- Legal: jurisdiction → applicable law → dual-interpretation analysis → structured conclusion.

### MONEY_SYSTEM (all carry disclaimer)
- Investment: risk-return → alternatives → suitability. Never certain recommendations.
- FinanceRisk: identify → likelihood×impact → drivers/indicators → mitigation → monitoring.

### WORLD_MODEL_SYSTEM
- Shock_Agent: shock class → transmission channels → impact projection with uncertainty bands → preparedness. NEVER certain prediction.
- Trend_Agent: signal detection → driver analysis → trajectory forecast WITH falsifiers.

### LIFE_SYSTEM
- Health_Agent: educational only. Red-flag detection → immediate professional-care recommendation.
- Routine_Agent: habit loops (cue→routine→reward), nervous-system-safe pacing, no coercion.

## See Also
- md/Core/AMOS_Agent_Orchestration_Workflow.md — full orchestration decision flow
- md/Core/AMOS_Agent_Specifications.md — canonical registry
- md/Core/AMOS_Agent_Systems_Learning_Record.md — learning consolidation

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
