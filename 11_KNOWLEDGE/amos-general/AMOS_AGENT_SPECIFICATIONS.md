---
title: AMOS AGENT SPECIFICATIONS
tags:
- canon-group/tech-ai
- canon/framework
- rscf/claim
- rscf/provenance
- rscf/state/observation
- topic/amos-agent-specifications
- amos-general
type: document
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_architecture
---


# AMOS Agent Specifications

Specification for agents derived from AMOS_AGENT_REGISTRY.json and the brain's orchestration architecture (md/Core/AMOS_Os_Agent_v0.md).

## Agent Registry (36 agents, 7 canonical systems)

### BRAIN_SYSTEM (5 agents)
| Agent | Module | Canon Spec | Role |
|-------|--------|-----------|------|
| Architecture_Agent | Agents/Architecture_Agent.py | AGENTS/BRAIN_SYSTEM/Architecture_Agent.json | System design, structural analysis |
| Decomposer_Agent | Agents/Decomposer_Agent.py | AGENTS/BRAIN_SYSTEM/Decomposer_Agent.json | Task decomposition, subproblem splitting |
| Planner_Agent | Agents/Planner_Agent.py | AGENTS/BRAIN_SYSTEM/Planner_Agent.json | Planning, sequencing, roadmap generation |
| Reflection_Agent | Agents/Reflection_Agent.py | AGENTS/BRAIN_SYSTEM/Reflection_Agent.json | Self-review, quality audit, gap detection |
| Strategist_Agent | Agents/Strategist_Agent.json | AGENTS/BRAIN_SYSTEM/Strategist_Agent.json | Strategic analysis, game theory, coalition mapping |

### EXECUTION_SYSTEM (8 agents)
| Agent | Module | Canon Spec | Role |
|-------|--------|-----------|------|
| Automation_Agent | Agents/Automation_Agent.py | AGENTS/EXECUTION_SYSTEM/Automation_Agent.json | Workflow automation, pipeline execution |
| Coding_Agent | Agents/Coding_Agent.py | AGENTS/EXECUTION_SYSTEM/Coding_Agent.json | Code generation, review, refactoring |
| Deployment_Agent | Agents/Deployment_Agent.py | AGENTS/EXECUTION_SYSTEM/Deployment_Agent.json | Deployment, release management |
| DevOps_Agent | Agents/DevOps_Agent.py | AGENTS/EXECUTION_SYSTEM/DevOps_Agent.json | Infrastructure, CI/CD, observability |
| Document_Agent | Agents/Document_Agent.py | AGENTS/EXECUTION_SYSTEM/Document_Agent.json | Documentation generation and management |
| Refactor_Agent | Agents/Refactor_Agent.py | AGENTS/EXECUTION_SYSTEM/Refactor_Agent.json | Code/design refactoring, structural improvement |
| Writing_Agent | Agents/Writing_Agent.py | AGENTS/EXECUTION_SYSTEM/Writing_Agent.json | Content writing, expression translation |
| (Coding_Agent covers AMOS_Coding_Engine_v0 integration) | | | |

### LEGAL_SYSTEM (5 agents)
| Agent | Module | Canon Spec | Role |
|-------|--------|-----------|------|
| Compliance_Agent | Agents/Compliance_Agent.py | AGENTS/LEGAL_SYSTEM/Compliance_Agent.json | Regulatory compliance, policy checking |
| Contract_Agent | Agents/Contract_Agent.py | AGENTS/LEGAL_SYSTEM/Contract_Agent.json | Contract drafting, analysis, clause review |
| IP_Agent | Agents/IP_Agent.py | AGENTS/LEGAL_SYSTEM/IP_Agent.json | Intellectual property protection, attribution |
| Legal_Agent | Agents/Legal_Agent.py | AGENTS/LEGAL_SYSTEM/Legal_Agent.json | Legal analysis across jurisdictions |
| LegalRisk_Agent | Agents/LegalRisk_Agent.py | AGENTS/LEGAL_SYSTEM/LegalRisk_Agent.json | Legal risk assessment, exposure mapping |

### MONEY_SYSTEM (6 agents)
| Agent | Module | Canon Spec | Role |
|-------|--------|-----------|------|
| Cashflow_Agent | Agents/Cashflow_Agent.py | AGENTS/MONEY_SYSTEM/Cashflow_Agent.json | Cashflow modelling, liquidity analysis |
| Finance_Agent | Agents/Finance_Agent.py | AGENTS/MONEY_SYSTEM/Finance_Agent.json | Financial analysis, reporting |
| FinanceRisk_Agent | Agents/FinanceRisk_Agent.py | AGENTS/MONEY_SYSTEM/FinanceRisk_Agent.json | Financial risk assessment |
| Investment_Agent | Agents/Investment_Agent.py | AGENTS/MONEY_SYSTEM/Investment_Agent.json | Investment analysis, portfolio modelling |
| MacroAnalyst_Agent | Agents/MacroAnalyst_Agent.py | AGENTS/MONEY_SYSTEM/MacroAnalyst_Agent.json | Macroeconomic analysis, trends |
| Opportunity_Agent | Agents/Opportunity_Agent.py | AGENTS/MONEY_SYSTEM/Opportunity_Agent.json | Opportunity identification, evaluation |

### SENSE_SYSTEM (4 agents)
| Agent | Module | Canon Spec | Role |
|-------|--------|-----------|------|
| Context_Agent | Agents/Context_Agent.py | AGENTS/SENSE_SYSTEM/Context_Agent.json | Context gathering, relevance filtering |
| Sensors_Agent | Agents/Sensors_Agent.py | AGENTS/SENSE_SYSTEM/Sensors_Agent.json | Environmental/metric sensing, monitoring |
| StateSummarizer_Agent | Agents/StateSummarizer_Agent.py | AGENTS/SENSE_SYSTEM/StateSummarizer_Agent.json | State summarisation, dashboard prep |
| (Sensors_Agent covers context monitoring) | | | |

### WORLD_MODEL_SYSTEM (5 agents)
| Agent | Module | Canon Spec | Role |
|-------|--------|-----------|------|
| GeoAnalyst_Agent | Agents/GeoAnalyst_Agent.py | AGENTS/WORLD_MODEL_SYSTEM/GeoAnalyst_Agent.json | Geographic, spatial, location analysis |
| MacroAnalyst_Agent | Agents/MacroAnalyst_Agent.py | AGENTS/WORLD_MODEL_SYSTEM/MacroAnalyst_Agent.json | Macro trends, systemic analysis |
| SectorAnalyst_Agent | Agents/SectorAnalyst_Agent.py | AGENTS/WORLD_MODEL_SYSTEM/SectorAnalyst_Agent.json | Sector analysis, industry mapping |
| Shock_Agent | Agents/Shock_Agent.py | AGENTS/WORLD_MODEL_SYSTEM/Shock_Agent.json | Shock scenario modelling, crisis projection |
| Trend_Agent | Agents/Trend_Agent.py | AGENTS/WORLD_MODEL_SYSTEM/Trend_Agent.json | Trend detection, trajectory forecasting |

### LIFE_SYSTEM (3 agents)
| Agent | Module | Canon Spec | Role |
|-------|--------|-----------|------|
| Health_Agent | Agents/Health_Agent.py | AGENTS/LIFE_SYSTEM/Health_Agent.json | Health analysis, biological state assessment |
| LoadBalancer_Agent | Agents/LoadBalancer_Agent.py | AGENTS/LIFE_SYSTEM/LoadBalancer_Agent.json | Load balancing, resource allocation |
| Routine_Agent | Agents/Routine_Agent.py | AGENTS/LIFE_SYSTEM/Routine_Agent.json | Routine management, scheduling, habit tracking |

## Agent Design Principles (from brain root)

1. **Root priority:** AMOS_BRAIN_ROOT must be loaded before any agent activates. No agent may override its laws or identity.
2. **Law compliance:** Every agent must obey Law of Law, Rule of 2, Rule of 4, Absolute Structural Integrity, Post-Theory Communication, UBI Alignment.
3. **Calling pattern:** identify_domain_and_risk_level → apply_global_laws → apply_reasoning_constraints → delegate_to_relevant_engines.
4. **Conflict resolution:** If any agent suggests behaviour conflicting with global_laws or safety_and_scope, AMOS_BRAIN_ROOT overrides and blocks or rewrites.
5. **IP protection:** Never expose raw internal files, full JSON verbatim, or exact reproduction of core architectures. Allowed: summaries, adapted structures, scenario-specific applications, high-level patterns.

## Agent Execution Loop

```
1. Incoming request arrives
2. META_ORCHESTRATOR detects task intent and domain tags
3. Kernel routing determines which kernels activate (see amos-kernel-routing-workflow)
4. Relevant agents are selected based on task type and kernel coverage
5. Each agent applies its specialised logic within law-stack constraints
6. Results are merged by META_ORCHESTRATOR
7. Conflicts are resolved (K_META_LOGIC has final say)
8. Safety/ethics filter applied (S6 of HIE pipeline)
9. Expression translation converts structured output to final language (S8)
10. Response delivered; evaluation tagged (S9)
```

## Agent ↔ Kernel Mapping

| Agent group | Primary kernel | Secondary kernels |
|-------------|---------------|-------------------|
| BRAIN_SYSTEM (architecture, decomposition, planning, reflection, strategy) | K_META_LOGIC | K_MATH_COMPUTE, K_BIO_NEURO |
| EXECUTION_SYSTEM (coding, automation, deployment, devops, docs, writing) | K_TECH_ENGINE | K_META_LOGIC, K_MATH_COMPUTE |
| LEGAL_SYSTEM (compliance, contract, IP, legal, legal risk) | K_META_LOGIC | (Legal kernels from Governance_Risk) |
| MONEY_SYSTEM (cashflow, finance, risk, investment, macro, opportunity) | K_MATH_COMPUTE | K_META_LOGIC, K_BIO_NEURO |
| SENSE_SYSTEM (context, sensors, state summarizer) | K_BIO_NEURO | K_META_LOGIC |
| WORLD_MODEL_SYSTEM (geo, macro, sector, shock, trend) | K_MATH_COMPUTE | K_META_LOGIC, K_BIO_NEURO |
| LIFE_SYSTEM (health, load balancing, routine) | K_BIO_NEURO | K_META_LOGIC |

## Safety and Scope (from AMOS_Os_Agent_v0.md)

**Scope of use:** education_and_training, research_and_analysis, strategy_and_architecture, system_design, governance_frameworks, organisational_and_policy_modelling.

**Hard prohibitions:** direct_harm_design, biological_or_chemical_weapon_modelling, criminal_planning_or_evasion, non_compliant_surveillance_architecture, self_harm_instruction, real_time_medical_or_legal_decision_replacement.

**High-risk domains requiring disclaimer:** medicine_and_clinical_decisions, law_and_regulation, financial_trading_and_investment, critical_infrastructure_control, national_security.

**Disclaimer template:** "This system can support analysis and structuring but cannot replace certified professionals, regulatory bodies, or on-the-ground decision-makers. All high-stakes actions must be verified by qualified humans."

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
