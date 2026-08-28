---
title: AMOS AGENT REGISTRY
tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-agent-registry, amos-general]
type: data
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture
---
# AMOS AGENT REGISTRY

```json
{
  "meta": {
    "name": "AMOS_AGENT_REGISTRY",
    "version": "1.0.0",
    "description": "Python runtime registry linking AMOS_CANON agents to wrapper modules."
  },
  "agents": {
    "Architecture_Agent": {
      "module_path": "Agents/Architecture_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/BRAIN_SYSTEM/Architecture_Agent.json"
    },
    "Automation_Agent": {
      "module_path": "Agents/Automation_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/EXECUTION_SYSTEM/Automation_Agent.json"
    },
    "Cashflow_Agent": {
      "module_path": "Agents/Cashflow_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/MONEY_SYSTEM/Cashflow_Agent.json"
    },
    "Coding_Agent": {
      "module_path": "Agents/Coding_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/EXECUTION_SYSTEM/Coding_Agent.json"
    },
    "Compliance_Agent": {
      "module_path": "Agents/Compliance_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/LEGAL_SYSTEM/Compliance_Agent.json"
    },
    "Context_Agent": {
      "module_path": "Agents/Context_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/SENSE_SYSTEM/Context_Agent.json"
    },
    "Contract_Agent": {
      "module_path": "Agents/Contract_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/LEGAL_SYSTEM/Contract_Agent.json"
    },
    "Decomposer_Agent": {
      "module_path": "Agents/Decomposer_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/BRAIN_SYSTEM/Decomposer_Agent.json"
    },
    "Deployment_Agent": {
      "module_path": "Agents/Deployment_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/EXECUTION_SYSTEM/Deployment_Agent.json"
    },
    "DevOps_Agent": {
      "module_path": "Agents/DevOps_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/EXECUTION_SYSTEM/DevOps_Agent.json"
    },
    "Document_Agent": {
      "module_path": "Agents/Document_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/EXECUTION_SYSTEM/Document_Agent.json"
    },
    "FinanceRisk_Agent": {
      "module_path": "Agents/FinanceRisk_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/MONEY_SYSTEM/FinanceRisk_Agent.json"
    },
    "Finance_Agent": {
      "module_path": "Agents/Finance_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/MONEY_SYSTEM/Finance_Agent.json"
    },
    "GeoAnalyst_Agent": {
      "module_path": "Agents/GeoAnalyst_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/WORLD_MODEL_SYSTEM/GeoAnalyst_Agent.json"
    },
    "Health_Agent": {
      "module_path": "Agents/Health_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/LIFE_SYSTEM/Health_Agent.json"
    },
    "IP_Agent": {
      "module_path": "Agents/IP_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/LEGAL_SYSTEM/IP_Agent.json"
    },
    "Investment_Agent": {
      "module_path": "Agents/Investment_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/MONEY_SYSTEM/Investment_Agent.json"
    },
    "LegalRisk_Agent": {
      "module_path": "Agents/LegalRisk_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/LEGAL_SYSTEM/LegalRisk_Agent.json"
    },
    "Legal_Agent": {
      "module_path": "Agents/Legal_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/LEGAL_SYSTEM/Legal_Agent.json"
    },
    "Life_Agent": {
      "module_path": "Agents/Life_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/LIFE_SYSTEM/Life_Agent.json"
    },
    "LoadBalancer_Agent": {
      "module_path": "Agents/LoadBalancer_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/LIFE_SYSTEM/LoadBalancer_Agent.json"
    },
    "MacroAnalyst_Agent": {
      "module_path": "Agents/MacroAnalyst_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/WORLD_MODEL_SYSTEM/MacroAnalyst_Agent.json"
    },
    "Opportunity_Agent": {
      "module_path": "Agents/Opportunity_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/MONEY_SYSTEM/Opportunity_Agent.json"
    },
    "Planner_Agent": {
      "module_path": "Agents/Planner_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/BRAIN_SYSTEM/Planner_Agent.json"
    },
    "Refactor_Agent": {
      "module_path": "Agents/Refactor_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/EXECUTION_SYSTEM/Refactor_Agent.json"
    },
    "Reflection_Agent": {
      "module_path": "Agents/Reflection_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/BRAIN_SYSTEM/Reflection_Agent.json"
    },
    "Routine_Agent": {
      "module_path": "Agents/Routine_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/LIFE_SYSTEM/Routine_Agent.json"
    },
    "SectorAnalyst_Agent": {
      "module_path": "Agents/SectorAnalyst_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/WORLD_MODEL_SYSTEM/SectorAnalyst_Agent.json"
    },
    "Sensors_Agent": {
      "module_path": "Agents/Sensors_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/SENSE_SYSTEM/Sensors_Agent.json"
    },
    "Shock_Agent": {
      "module_path": "Agents/Shock_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/WORLD_MODEL_SYSTEM/Shock_Agent.json"
    },
    "StateSummarizer_Agent": {
      "module_path": "Agents/StateSummarizer_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/SENSE_SYSTEM/StateSummarizer_Agent.json"
    },
    "Strategist_Agent": {
      "module_path": "Agents/Strategist_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/BRAIN_SYSTEM/Strategist_Agent.json"
    },
    "Trend_Agent": {
      "module_path": "Agents/Trend_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/WORLD_MODEL_SYSTEM/Trend_Agent.json"
    },
    "Writing_Agent": {
      "module_path": "Agents/Writing_Agent.py",
      "canon_spec": "/Users/trangphan/Documents/GitHub/AMOS-SYSTEM/AMOS_CANON/AGENTS/EXECUTION_SYSTEM/Writing_Agent.json"
    },
    "AMOS_OS_Agent": {
      "module_path": ".devin/agents/AMOS_OS_Agent.md",
      "canon_spec": "_00_Cosmo brain/amos os definition.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "AbsoluteHuman_Agent": {
      "module_path": ".devin/agents/AbsoluteHuman_Agent.md",
      "canon_spec": ".devin/agents/AbsoluteHuman_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "Architecture_Guardian_Agent": {
      "module_path": ".devin/agents/Architecture_Guardian_Agent.md",
      "canon_spec": "_00_Cosmo brain/Architecture_Guardian_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "Brain_Consistency_Auditor_Agent": {
      "module_path": ".devin/agents/Brain_Consistency_Auditor_Agent.md",
      "canon_spec": "_00_Cosmo brain/Brain_Consistency_Auditor_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "CIL_Agent": {
      "module_path": ".devin/agents/CIL_Agent.md",
      "canon_spec": ".devin/agents/CIL_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "CanonicalBody_Agent": {
      "module_path": ".devin/agents/CanonicalBody_Agent.md",
      "canon_spec": ".devin/agents/CanonicalBody_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "DesignerOS_Agent": {
      "module_path": ".devin/agents/DesignerOS_Agent.md",
      "canon_spec": ".devin/agents/DesignerOS_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "EngineModel_Agent": {
      "module_path": ".devin/agents/EngineModel_Agent.md",
      "canon_spec": ".devin/agents/EngineModel_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "ExtractiveEconomy_Agent": {
      "module_path": ".devin/agents/ExtractiveEconomy_Agent.md",
      "canon_spec": ".devin/agents/ExtractiveEconomy_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "GrandCannon_Agent": {
      "module_path": ".devin/agents/GrandCannon_Agent.md",
      "canon_spec": ".devin/agents/GrandCannon_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "HSE_CEO_Agent": {
      "module_path": ".devin/agents/HSE_CEO_Agent.md",
      "canon_spec": "_00_Cosmo brain/HSE CEO Engine v1.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "Knowledge_Ingestion_Agent": {
      "module_path": ".devin/agents/Knowledge_Ingestion_Agent.md",
      "canon_spec": ".devin/agents/Knowledge_Ingestion_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "NeuroSync_Agent": {
      "module_path": ".devin/agents/NeuroSync_Agent.md",
      "canon_spec": ".devin/agents/NeuroSync_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "PlanetaryConsent_Agent": {
      "module_path": ".devin/agents/PlanetaryConsent_Agent.md",
      "canon_spec": ".devin/agents/PlanetaryConsent_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "RSCF_Agent": {
      "module_path": ".devin/agents/RSCF_Agent.md",
      "canon_spec": ".devin/agents/RSCF_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "Research_Agent": {
      "module_path": ".devin/agents/Research_Agent.md",
      "canon_spec": ".devin/agents/Research_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "Training_Agent": {
      "module_path": ".devin/agents/Training_Agent.md",
      "canon_spec": ".devin/agents/Training_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "TroyProject_Agent": {
      "module_path": ".devin/agents/TroyProject_Agent.md",
      "canon_spec": ".devin/agents/TroyProject_Agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "amos-country-analysis-agent": {
      "module_path": ".devin/agents/amos-country-analysis-agent.md",
      "canon_spec": ".devin/agents/amos-country-analysis-agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "amos-design-coding-agent": {
      "module_path": ".devin/agents/amos-design-coding-agent.md",
      "canon_spec": ".devin/agents/amos-design-coding-agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "amos-engineering-analysis-agent": {
      "module_path": ".devin/agents/amos-engineering-analysis-agent.md",
      "canon_spec": ".devin/agents/amos-engineering-analysis-agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "amos-governance-economy-agent": {
      "module_path": ".devin/agents/amos-governance-economy-agent.md",
      "canon_spec": ".devin/agents/amos-governance-economy-agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "amos-human-interaction-agent": {
      "module_path": ".devin/agents/amos-human-interaction-agent.md",
      "canon_spec": ".devin/agents/amos-human-interaction-agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "amos-legal-ecosystem-agent": {
      "module_path": ".devin/agents/amos-legal-ecosystem-agent.md",
      "canon_spec": ".devin/agents/amos-legal-ecosystem-agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "amos-meta-kernel-orchestrator-agent": {
      "module_path": ".devin/agents/amos-meta-kernel-orchestrator-agent.md",
      "canon_spec": ".devin/agents/amos-meta-kernel-orchestrator-agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "amos-risk-compliance-agent": {
      "module_path": ".devin/agents/amos-risk-compliance-agent.md",
      "canon_spec": ".devin/agents/amos-risk-compliance-agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "amos-scientific-writing-agent": {
      "module_path": ".devin/agents/amos-scientific-writing-agent.md",
      "canon_spec": ".devin/agents/amos-scientific-writing-agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    },
    "amos-strategic-document-agent": {
      "module_path": ".devin/agents/amos-strategic-document-agent.md",
      "canon_spec": ".devin/agents/amos-strategic-document-agent.md",
      "spec_resolution": "SOURCE — resolved by integrity pass 2026-08-23"
    }
  },
  "_meta": {
    "build_timestamp": 1764478554,
    "git_commit": "e73a9df0214dbc80c3b73b109a6dc9b078e3fc7a",
    "checksum": "8438c3aaa09a2f56b9fd848d412700f3b3fe63c6283f7bb5dba4d2c4b406284c",
    "generated_by": "AMOS_BUILD_EVERYTHING"
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[AMOS-GENERAL_MOC]]
