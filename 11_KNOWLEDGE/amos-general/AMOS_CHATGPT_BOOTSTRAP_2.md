---
title: "AMOS ChatGPT Bootstrap — One-Click System Build"
created: "2026-08-22"
origin: "Google Drive — _00_AMOS_CANON/AMOS_CHATGPT_BOOTSTRAP.md"
origin_architect: "Trang Phan"
type: "reference"
tags: [canon-group/meta, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, rscf/T-topology, rscf/K-compression, rscf/G-relation, topic/bootstrap, amos-general]
status: "active"
provenance: "VERIFIED"
confidence: "VERIFIED"
---

# AMOS ChatGPT Bootstrap

## Owner: Trang | System: AMOS (Autonomous Multi-Operator System)

### Root System Rules
- Python version: `/usr/bin/python3`
- AMOS root path: `/Users/trangphan/Documents/GitHub/AMOS-PUBLIC`
- Never require external packages unless explicitly allowed
- Never overwrite canon JSON or Python modules unless instructed
- Always preserve deterministic naming: `<SYSTEM>.json`, `<KernelName>_Kernel.json`, `<EngineName>_Engine.json`, `<AgentName>_Agent.json`
- Always update the registry when new components are created
- Terminal scripts = pure commands only, no comments

### One-Click Full System Build
```bash
cd /Users/trangphan/Documents/GitHub/AMOS-PUBLIC
/usr/bin/python3 AMOS_BUILD_EVERYTHING.py
/usr/bin/python3 AMOS_ONECLICK_ORCHESTRATOR.py
git add .
git commit -m "AMOS full build + orchestration run"
git push
```

**Pipeline**: 1. Canon generation → 2. Kernel/Engine/Agent creation → 3. Layout builder → 4. Wiring pass → 5. Speed optimisation → 6. Full benchmark → 7. Registry rebuild → 8. Git sync

### Canonical Tree
```
AMOS_CANON/
    SYSTEMS/
    KERNELS/<SYSTEM>/
    ENGINES/<SYSTEM>/
    AGENTS/<SYSTEM>/
    registry.json
```

### AMOS Agent Registry (72 agents)
Links Python module paths to canon spec JSON files across 7 systems:
- BRAIN_SYSTEM (6): Architecture, Decomposer, Planner, Reflection, Strategist, Brain Consistency Auditor
- EXECUTION_SYSTEM (7): Automation, Coding, Deployment, DevOps, Document, Refactor, Writing
- LEGAL_SYSTEM (5): Compliance, Contract, IP, LegalRisk, Legal
- LIFE_SYSTEM (4): Health, Life, LoadBalancer, Routine
- MONEY_SYSTEM (5): Cashflow, FinanceRisk, Finance, Investment, Opportunity
- SENSE_SYSTEM (4): Context, Knowledge Ingestion, Sensors, StateSummarizer
- WORLD_MODEL_SYSTEM (5): GeoAnalyst, MacroAnalyst, SectorAnalyst, Shock, Trend
- Specialized (7): AMOS OS, Canonical Body, Extractive Economy, Grand Cannon, HSE CEO, RSCF, Brain Consistency Auditor

---

*Source: RTF file, 189 lines (5KB)*

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
