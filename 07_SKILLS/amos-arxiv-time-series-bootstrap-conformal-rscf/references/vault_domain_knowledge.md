---
title: vault domain knowledge
type: reference
source: 07_SKILLS/amos-arxiv-time-series-bootstrap-conformal-rscf/references
tags: [reference, amos-arxiv-time-series-bootstrap-conformal-rscf, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-arxiv-time-series-bootstrap-conformal-rscf`

## Vault-Sourced Content

### Source 1: AMOS_CHATGPT_BOOTSTRAP.md

> Path: `amos-general/A/ChatGPT/AMOS_CHATGPT_BOOTSTRAP.md` | Size: 4460 chars | Match score: 10 | content_hash: 69b9cbfbb6f4dd3c

# AMOS_CHATGPT_BOOTSTRAP.md  
## Official Bootstrap for All ChatGPT Conversations

This file must be followed by ChatGPT in every conversation that references AMOS.  
It ensures deterministic behaviour, correct naming, correct Python version, correct repo, and consistent system expansion.

---

# 1. ROOT SYSTEM RULES

ChatGPT must automatically apply these rules:

- Python version must always be:  
  `/usr/bin/python3`  
- AMOS root path must always be:  
  `/Users/trangphan/Documents/GitHub/AMOS-PUBLIC`
- Never generate code requiring external packages unless explicitly allowed.
- Never overwrite existing canon JSON or Python modules unless instructed.
- Always preserve deterministic naming:
- `<SYSTEM>.json`
  - `<KernelName>_Kernel.json`
- `<EngineName>_Engine.json`
  - `<AgentName>_Agent.json`
- Always update the registry when new components are created.
- When the user asks for a **terminal script**, return **pure commands only**, no comments.

When user says “max power” →  
ChatGPT must generate the most exhaustive, scalable, deterministic, fully governed version.

---

# 2. ABSOLUTE SYSTEM PATHS (ALWAYS USE THESE)

```
AMOS_ROOT=/Users/trangphan/Documents/GitHub/AMOS-PUBLIC
PYTHON=/usr/bin/python3
```

---

# 3. ONE-CLICK FULL SYSTEM BUILD

The official AMOS full rebuild command:

```
cd /Users/trangphan/Documents/GitHub/AMOS-PUBLIC
/usr/bin/python3 AMOS_BUILD_EVERYTHING.py
/usr/bin/python3 AMOS_ONECLICK_ORCHESTRATOR.py
git add .
git commit -m "AMOS full build + orchestration run"
git push
```

This pipeline performs:

1. Canon generation
2. Kernel/Engine/Agent creation  
3. Layout builder
4. Wiring pass  
5. Speed optimisation
6. Full benchmark  
7. Registry rebuild
8. Git sync

---

# 4. OFFICIAL CANON RULES

AMOS must always maintain this deterministic tree:

```
AMOS_CANON/
    SYSTEMS/
    KERNELS/<SYSTEM>/
    ENGINES/<SYSTEM>/
    AGENTS/<SYSTEM>/
    registry.json
```

Each component obeys:

```
```

Python modules must be placed beside JSON if required.

---

# 5. MASTER GENERATION SCRIPTS (MANDATORY)

AMOS_BUILD_EVERYTHING.py  
AMOS_BUILD_ALL_AGENTS.py  
AMOS_BUILD_ALL_ENGINES.py  
AMOS_BUILD_ALL_KERNELS.py  

These scripts:

- read the official system definition
- create all JSON files  
- create all Python agent stubs
- never overwrite existing files  
- regenerate registry
- ensure full structural integrity  

---

# 6. CHATGPT BEHAVIOUR RULES

ChatGPT must automatically:

- Reload this bootstrap whenever the user referencing AMOS enters a conversation.
- Always infer the current state of AMOS from GitHub repo `trangyp/AMOS-PUBLIC`.
- Use only deterministic naming.
- Respect Trang’s authority over system rules (“governed by Trang”).
- Generate scalable, exhaustive system components when requested.
- Produce 100% Python-3.9-compatible code.

When user asks:

### “next”, “continue”, “max power”, “expand”, “upgrade”
ChatGPT must:
- choose the highest-power deterministic expansion  
- identify missing component

---

### Source 2: AMOS ChatGPT Bootstrap

> Path: `amos-general/A/ChatGPT/AMOS ChatGPT Bootstrap.md` | Size: 2587 chars | Match score: 10 | content_hash: d608da5becd7a2ce

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


---

---

### Source 3: RSCF Contract

> Path: `rscf/rscf.md` | Size: 1387 chars | Match score: 5 | content_hash: ae5e4fdd2e612802

# RSCF Contract

Use **RSCF — Recursive Structured Claim Framework** for every load-bearing conclusion.

```yaml
claim_id: stable-id
claim: concise proposition
class: VERIFIED | DERIVED | MODEL | CONDITIONAL | COMPETING | UNKNOWN/GAP
scale: H | M | L
premises: []
evidence: []
provenance:
  ancestry: []
  independence_status: demonstrated | correlated | unknown
scope:
  system_or_population: null
  environment: null
  scale: null
  time_window: null
  measurement_method: null
  assumptions: []
regime:
  id: null
  validity_conditions: []
freshness:
  observed_at: null
  revalidate_at: null
dependencies: []
competing_hypotheses: []
falsifiers: []
confidence_ceiling: 0.0
decision_relevance: low | medium | high
```

## RSCF invariants
1. Confidence cannot exceed the weakest load-bearing premise without independent revalidation.
2. Descendants of one source are correlated provenance, not independent confirmation.
3. Scope, regime, and freshness propagate to dependent claims.
4. Structural similarity never proves causation.
5. Equal/incomparable support remains COMPETING.
6. Failed premises invalidate only dependent descendants.
7. Framework equations remain MODEL unless independently validated.

---

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
