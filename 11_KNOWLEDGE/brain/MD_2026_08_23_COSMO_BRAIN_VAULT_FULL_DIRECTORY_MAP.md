---
title: MD 2026 08 23 COSMO BRAIN VAULT FULL DIRECTORY MAP
type: map
source: 11_KNOWLEDGE/brain
origin_architect: Trang Phan
provenance: direct file inspection + subagent exploration of _00_Cosmo brain subdirectories on 2026-08-23. All source files have been flattened to root level.
confidence: 0.9
epistemic_class: OBSERVATION
conclusion_class: VERIFIED
tags:
- cosmo-brain
- flatten
- amos-consulting
- amos-system-main
- amos-forex
- openclaw
- main
- amos-copilot
- architecture
- directory-map
- brain
- canon/knowledge
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: cognitive_architecture
---


# Cosmo Brain Vault — Full Directory Map (Post-Flatten)

> **Path**: `/Users/mac/Downloads/stitch_project_cosmo/_00_Cosmo brain/`
> **Date**: 2026-08-23
> **Status**: All subdirectories flattened to root. Only `md/` remains as a subdirectory.
> **Root files**: ~153,788 (after flatten, before dedup)

## Flatten Summary

All source files from 7 subdirectories were moved to the vault root with flattened names (path separators replaced with `__`). Dependency directories (node_modules, .git, .venv, .next, .idea, third_party, etc.) were deleted. Exact duplicates were removed by content hash.

### Original Subdirectories (now flattened)

| Directory | Total Files | Non-Dep Files | Description |
|-----------|-------------|---------------|-------------|
| **AMOS-Consulting/** | 354,927 | ~100K | Massive repo with AMOS-Invest, AMOS-Mai Linh Connect, AMOS-SYSTEM-main |
| **AMOS-SYSTEM-main/** | 5,623 | ~4,600 | AMOS biological-computational OS (40+ AMOS_* modules) |
| **AMOS forex/** | 7,255 | ~50 | Forex trading system (mostly node_modules) |
| **openclaw-main/** | 80,115 | ~8K | OpenClaw AI platform (mostly node_modules/dist) |
| **MAIN/** | 7,628 | 7,628 | Main brain/systems/data directory (no deps) |
| **amos-copilot-fullpack/** | 8 | 8 | 8 AMOS skill zip files |
| **amos-copilot-fullpack 2/** | 8 | 8 | Exact duplicate — deleted |

---

## 1. AMOS-Consulting (largest repo)

**Structure**: AMOS-Invest/ + AMOS-Mai Linh Connect/ + AMOS-SYSTEM-main/ (nested)

### AMOS-Invest/
- **AMOS-Claws/** — OpenClaw fork with copilot proxy, GitHub copilot integration
- **AMOS-Code/** — Code generation/analysis tools
- **_AMOS_CANON/** — Canon specifications (already flattened in previous session)
- **amos/** — Core AMOS Python package
- **amos-stack/** — Full-stack deployment
- **amos-ui/** — UI components
- **amos-vscode-extension/** — VS Code extension
- **amos_financial_platform/** — Financial platform
- **bolt.diy/** — Bolt.diy fork
- **deploy_package/** — Deployment packaging
- **monetary_signal_system/** — Monetary signal analysis
- **openclaw/** — Another OpenClaw fork
- **tradingview_complete/, tradingview_clone/, tradingview-app/** — TradingView implementations
- **repo_doctor/** — Repository health tool
- **redis/** — Redis configuration
- **tests/** — Test suite

### AMOS-Mai Linh Connect/
- **config/env/** — Environment configs (7 .env files with stub values)
- **docs/** — Documentation
- **webhook-receiver/** — Webhook receiver service
- **mailinh-backend/** — Mai Linh Connect backend
- **_AMOS-SYSTEM-main/** — Nested AMOS-SYSTEM copy (with third_party deps)

### File types (AMOS-Consulting overall)
- 106,888 JSON, 66,769 JS, 41,815 TS, 36,359 PY, 34,065 MAP, 9,545 MJS, 6,790 MD

---

## 2. AMOS-SYSTEM-main (AMOS Biological-Computational OS)

**What**: Autonomous Mind Operating System — a biological-computational OS that treats AI reasoning as a self-organizing organism.

**Owner**: Trang Phan ("AMOS by Trang")
**Scale**: 5,623 files (4,601 Python), ~40 AMOS_* directories

### 7-System Organism Architecture
1. **BRAIN_SYSTEM** — Reasoning, planning, architecture, decomposition, prediction, strategy
2. **WORLD_MODEL_SYSTEM** — World scanning, geo/macro/sector analysis, market signals, trends
3. **SENSE_SYSTEM** — Context, emotional sensors, environment/file/system scanning
4. **MONEY_SYSTEM** — Finance, cashflow, investment, opportunity analysis
5. **LEGAL_SYSTEM** — Compliance, contracts, IP protection, legal risk
6. **EXECUTION_SYSTEM** — Automation, coding, deployment, DevOps, documentation
7. **LIFE_SYSTEM** — Energy, health, mood, routine, load balancing

### Key Modules (40+ AMOS_* directories)
- **AMOS_ASSURANCE/** — Assurance, compliance, security, benchmarking
- **AMOS_AUTOGEN/** — Auto-generation kernels and blueprint stores
- **AMOS_CANON/** — Canonical specifications (agents, engines, identity, routing)
- **AMOS_CONSCIOUSNESS/** — Consciousness and awareness layers
- **AMOS_GOVERNANCE/** — Governance, policies, identity, access control
- **AMOS_INTEGRITY/** — Law integrity preservation
- **AMOS_KERNEL/** — OS-kernel-level services
- **AMOS_LAWS/** — Meta-laws and legal frameworks
- **AMOS_MEMORY/** — Episodic and semantic memory engines
- **AMOS_MODE/** — Profile and mode management
- **AMOS_ORGANISM_OS/** — 14 subsystems (00_ROOT through 14_INTERFACES)
- **AMOS_OS/** — Core OS (world_model, system_state)
- **AMOS_PERCEPTION/** — Multiscale perception kernel
- **AMOS_PLATFORM/** — Platform services (API, deployment, tenant)
- **AMOS_RESEARCH/** — Research modules
- **AMOS_SECURITY/** — Zero trust, key management
- **AMOS_TRUST/** — Recursive trust engine
- **AMOS_UNIVERSE/** — Universe/civilization canon loaders
- **AMOS_WORLD/** — Internal world model

### CANON_* Directories
- **CANON_BIOLOGY/** — Biological axioms, constraints, operators
- **CANON_COGNITION/** — Cognitive axioms, constraints, operators
- **CANON_ORG/** — Organizational canon
- **CANON_PHYSICS/** — Physical laws and constraints
- **CANON_RISK/** — Risk assessment canon
- **CANON_SYSTEMS/** — Systems canon

### GRAND_CANON/
- Unified law corpus: biological_computation_laws, collapse_recovery_laws, governance_laws, identity_ethics_laws, unified_law

### src/amos_system/
- **kernels/** — identity, integrity, governance, emotion, omega_brain, consciousness, ubi
- **runtime/** — Organism + OS runtime, biological layer state machines
- **engines/** — Domain-specific engines (specs/ and adapters/)
- **io/** — Entry points and integration surfaces
- **universe/** — Higher-order universe/civilization canon loaders
- **workflows/** — High-level orchestrations
- **web/** — FastAPI HTTP API and web interface

### Omega Brain Kernel
- `omega_context.py` — State container for reasoning passes
- `omega_registry.py` — Index of invariants, equations, operators, rules
- `omega_reasoner.py` — Deterministic reasoning pipeline
- `max_omega_brain.py` — High-level façade for MAX brain

### Modes of Operation
CALM, FOCUS, REPAIR, EXPLORE, EMERGENCY, SHUTDOWN

### Data Flow
```
User Input → AmosRuntime.run_max() → MaxOmegaBrain.run_comprehensive_reasoning()
→ OmegaContext → Cognition Kernels → Result + Validation → Response
```

### Biological Metaphors
- Brain → OMEGA Brain Kernel
- Nervous System → Event Bus
- Immune System → Identity Kernel
- Memory → World Model
- Homeostasis → System State
- Consciousness → Global Workspace
- Reflexes → Reflex Engine

---

## 3. AMOS Forex

**What**: Forex trading system with research, infrastructure, execution, risk management, signal generation, and validation modules.

**Structure**:
- research/, infra/, execution/, risk/, signal/, validation/, monitoring/
- orchestrator.js, event_bus.js
- Dockerfile, package.json, run_tests.py
- node_modules/ (deleted)

**File types**: 4,219 JS, 653 TS, 583 MAP, 579 MD, 577 JSON, 69 YML, 61 PY

---

## 4. openclaw-main

**What**: OpenClaw — an AI platform with UI, plugin SDK, GitHub Copilot integration, and extensive TypeScript/JavaScript codebase.

**Structure**:
- ui/ — UI components (with node_modules)
- dist/ — Build output (deleted)
- Plugin SDK, extensions (copilot-proxy, github-copilot)
- Multiple validation/evolution reports (MOTHER_CYCLE*, PHASE*_VALIDATION_REPORT*)

**File types**: 31,236 TS, 17,187 JS, 15,328 MAP, 3,539 MJS, 2,481 MD, 2,314 JSON

---

## 5. MAIN

**What**: Main brain/systems/data directory — the core AMOS brain implementation.

**Structure**:
- BRAIN/ — Brain modules
- SYSTEMS/ — System implementations (PROD, CORE, DEV)
- DATA/ — Data files (ACHIEVEMENTS)

**File types**: 2,990 PY, 1,589 JSON, 781 JS, 751 TS, 616 MD, 94 MJS, 77 TSX, 58 PDF, 49 SVG

---

## 6. amos-copilot-fullpack (8 files)

8 AMOS skill zip files:
- amos-competing-hypotheses
- amos-core-reasoning
- amos-fractal-routing
- amos-governed-evolution
- amos-provenance-trust
- amos-repository-reasoning
- amos-rscf-claims
- amos-speed-token-governor

---

## Flattened File Naming Convention

All flattened files use the pattern:
```
<ParentDir>__<SubDir>__<SubDir>__<filename>
```
Path separators (`/`) are replaced with `__`. Spaces in directory names are replaced with `_`.

Examples:
- `AMOS-Consulting__AMOS-Invest__amos__core__engine.py`
- `AMOS-SYSTEM-main__AMOS_CANON__agent_base.py`
- `MAIN__BRAIN__cognition.py`

---

## Memory Notes in md/

- `00_Cosmo_Brain_MOC.md` — Master Map of Content
- `2026-08-23 Cosmo Brain Full Architecture.md` — Production cosmo-brain/ architecture
- `2026-08-23 Cosmo Brain Core Architecture.md` — Core module deep dive
- `2026-08-23 AMOS Canon LEGACY BRAIN2 Core.md` — Legacy brain2 core specs
- `2026-08-23 AMOS Cosmo Brain Core Architecture Map.md`
- `2026-08-23 AMOS-Consulting LEGACY BRAIN2 Core Empty State.md`
- `2026-08-23 Cosmo Brain Project Directory Map.md`
- `AMOS_Cognitive_Substrate_v2_Implementation_Notes.md`

---

## Cross-References

- [[00_COSMO_BRAIN_MOC]]
- md__2026-08-23 Cosmo Brain Full Architecture
- md__2026-08-23 Cosmo Brain Core Architecture
- 2026-08-23 AMOS Canon LEGACY BRAIN2 Core
- AMOS Core Version Lineage
- AMOS Brain Engine Specs

---
**MOC:** [[BRAIN_MOC]]
