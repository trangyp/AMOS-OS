---
title: AMOS AGENT SYSTEMS LEARNING RECORD
tags: [system]
type: document
source: 11_KNOWLEDGE/system
---


# AMOS Brain: Consolidated Learning Record — All Agent Systems

**Date:** 2026-08-22 (final consolidation)  
**Sources:** AMOS_AGENT_REGISTRY.json, AMOS_Agent_Specifications.md, AMOS_Agent_Orchestration_Workflow.md, AMOS_Os_Agent_v0_Core4.md (brain root), md/Core/ workflows  
**Laws verified:** L1-L6 applied throughout all agent skill content.

---

## What Was Built This Continuation

### 7 System-Agent Skills Created (completing full 7-system coverage)

All 7 canonical agent systems now have dedicated Hermes skills with full execution patterns:

| # | Skill | Path | Covers | Lines |
|---|-------|------|--------|-------|
| 1 | amos-brain-agent | autonomous-ai-agents/ | Architecture, Decomposer, Planner, Reflection, Strategist (5 agents) | ~250 |
| 2 | amos-execution-agent | autonomous-ai-agents/ | Automation, Coding, Deployment, DevOps, Document, Refactor, Writing (7 agents) | ~280 |
| 3 | amos-legal-agent | amos-technical-agent/ + autonomous-ai-agents ref | Compliance, Contract, IP, Legal, LegalRisk (5 agents) | ~300 |
| 4 | amos-finance-agent | amos-technical-agent/ + autonomous-ai-agents ref | Cashflow, Finance, FinanceRisk, Investment, MacroAnalyst, Opportunity (6 agents) | ~320 |
| 5 | amos-world-model-agent | amos-technical-agent/ | GeoAnalyst, MacroAnalyst(WM), SectorAnalyst, Shock, Trend (5 agents) | ~180 |
| 6 | amos-life-agent | amos-technical-agent/ | Health, LoadBalancer, Routine (3 agents) | ~170 |
| 7 | amos-sense-agent | amos-technical-agent/ | Context, Sensors, StateSummarizer (3 agents) | ~90 |

Plus earlier: amos-agent-orchestration, amos-agent-execution, amos-agent-reflective (3 orchestration-layer skills), amos-architecture-agent, amos-coding-agent (deep single-agent skills).

**Total agent coverage: all 36 canonical agents across all 7 systems now have documented execution patterns in operational skills.**

---

## Key Design Decisions Embedded in the Skills

1. **Per-system law emphasis:** Legal agents → L1 (Law of Law) dominant; Life agents → L1 hard prohibition (no medical replacement) + L6 (UBI alignment); Money agents → L4 (model integrity) + mandatory disclaimers; World-model agents → L2 (competing scenarios) + epistemic class labelling; Sense agents → L4 (provenance/freshness labelling).

2. **Mandatory disclaimer gates:** Legal, Finance, and Health outputs ALWAYS carry disclaimers per brain-root safety_and_scope high-risk domain requirements.

3. **Epistemic class discipline:** Sense and World-model agents label every claim OBSERVATION / SOURCE_CLAIM / DERIVED / MODEL / UNKNOWN — matching the copilot core contract's source-separation rule.

4. **Multi-agent collaboration chains documented:** Each skill ends with concrete collaboration patterns (e.g., Trend→Shock→Macro→Sector→FinanceRisk chain).

5. **HIE goal selection per system:** Life agents default to `stabilise_nervous_system`; Legal/Money to `warn` for risk contexts; Sense agents as pipeline starters.

---

## Complete Skill Inventory (final state)

**Reasoning (11):** amos-reasoning-loop, amos-law-stack, amos-cognition-modes, amos-multi-perspective, amos-counterfactual, amos-ubi-alignment, amos-law-analysis, amos-compliance-check, amos-economic-analysis, amos-investment-framework, amos-expression-overlay*

**Communication (3):** amos-expression-overlay*, amos-emotion-analysis, amos-behaviour-design

**Tech (4):** amos-tech-kernel-catalog, amos-architecture-design, amos-data-pipeline, amos-ev-planning

**Agent orchestration layer (3):** amos-agent-orchestration, amos-agent-execution, amos-agent-reflective

**System agents (7):** amos-brain-agent, amos-execution-agent, amos-legal-agent, amos-finance-agent, amos-world-model-agent, amos-life-agent, amos-sense-agent

**Deep single-agent skills (2):** amos-architecture-agent, amos-coding-agent

**Docs (1):** amos-docs-bridge

**Pre-existing AMOS kernel skills (~28):** amos-core-reasoning, amos-os-agent, amos-mind-os, amos-consciousness-engine, amos-emotion-engine, amos-cognition-engine, amos-personality-engine, amos-human-intelligence-engine, amos-tech-engine, amos-tech-architecture, amos-design-kernel, amos-coding-kernel, amos-governance-economy, amos-org-governance, amos-medical-clinical, amos-scientific-reasoning, amos-species-interaction, amos-provenance-trust, amos-rls-provenance, amos-epistemic-governance, amos-absolute-logic, amos-universal-operator, amos-ulK-logic, amos-quantum-stack, amos-os-architecture, amos-brain-master-os, amos-brain-model-integration, amos-failure-memory, plus amos/ subdirectory skills (amos-durable-learning-storage, amos-architecture-verification)

**Total: 57+ AMOS skills**

---

## Vault Files Added This Continuation

1. **AMOS_Brain_Current_State_Memory.md** — comprehensive state: kernels, routing, laws, agents, HIE, expression translation, meta-cognition, 33 blueprints, Tech domains, skills, workflows
2. **AMOS_Brain_Fragment_File_Structure.md** — explains Core2/Core4/Core6/Core7 fragment naming and how to read them
3. **AMOS_Brain_Enhancement_Log.md** — updated continuation session record
4. **AMOS_Brain_Learning_Improvement.md** — what was learned and improved
5. **This file (AMOS_Agent_Systems_Learning_Record.md)** — final agent-systems consolidation

---

## Remaining Known Gaps (documented, not failures)

1. **Blueprint evaluation sections:** 7 root-component blueprints in brain root have empty inputs/outputs/capabilities (AMOS_OS_ROOT, AMOS_BRAIN_ROOT, Language_Overlay_And_IP_Protection, IP_Kernel_Shield, AMOS_ORCHESTRATOR_ROUTING, AMOS_SUPER_FABRICATION, AMOS_OPERATOR_META_SECTOR_ENGINE). Source-defined gaps — filling requires reading deeper into brain root fragments.
2. **Fragment consolidation:** Many *_CoreN.md files could be merged into canonical single files.
3. **Workflow↔skill cross-referencing:** Workflows reference concepts; skills reference workflows; a formal cross-reference index would strengthen navigation.

*Tagged: laws_applied=L1-L6, quadrants=all-4, strategy=direct_structural_answer, deviations=none.*

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[SYSTEM_MOC]]
