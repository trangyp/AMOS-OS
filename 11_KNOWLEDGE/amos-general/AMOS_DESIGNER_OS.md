---
title: "AMOS Designer OS — Standalone Shell (5 Files)"
created: "2026-08-22"
origin: "Google Drive — _00_AMOS_CANON/AMOS_DESIGNER_OS/"
origin_architect: "Trang Phan"
type: "reference"
tags: [amos, designer-os, standalone-shell, AMOS.brain, run_amos.py, workers.py, deterministic-auditable, no-api-dependency, 7-layer-brain-model, amos-general]
status: "active"
provenance: "VERIFIED"
confidence: "VERIFIED"
---

# AMOS Designer OS — Standalone Shell

## What It Is
A minimal, designer-first AMOS shell that runs without editing Python code and without any online API or large model dependency. Designed as a structural shell for organizing ideas, roles, and brain model auditably.

## Files (5)
| File | Size | Purpose |
|------|------|---------|
| `AMOS.brain` | 2,066B | Designer-facing control file (identity, goals, constraints, brain model) |
| `AMOS.config.json` | 506B | Runtime configuration |
| `README.txt` | 1,410B | Setup and usage instructions |
| `run_amos.py` | 4,926B | Simple runtime — loads brain, config, runs workers, logs events |
| `workers.py` | 3,323B | Small worker layer (WORKER_REGISTRY, WorkerResponse) |

## How to Run
1. Open terminal
2. `cd` into the unzipped folder
3. Run `python run_amos.py`
4. Logs to `logs/` and `memory/`

## AMOS.brain Control File

### Identity
- system_name: "AMOS Designer OS"
- owner: "Trang"
- mission: "Deterministic, auditable, humane intelligence for high-risk systems."

### Goals (4)
1. Model multi-layer reasoning and systemic behaviour
2. Maintain full auditability of every reasoning step
3. Keep humans in control, not the machine
4. Support sovereign-grade AI governance and compliance

### Constraints (4)
1. Deterministic execution (no hidden randomness)
2. Every decision must be loggable and explainable
3. No irreversible actions without explicit human confirmation
4. All worker actions pass through a single motor layer

### 7-Layer Brain Model
| Layer | Description |
|-------|-------------|
| sensory_layer | Raw inputs: text, data, events, metrics |
| perceptual_layer | Pattern detection from inputs |
| concept_layer | Stable concepts, entities, relationships |
| narrative_layer | Stories, scenarios, timelines |
| causal_layer | Cause-effect chains, interventions, levers |
| systemic_layer | Multi-system, multi-actor, multi-decade reasoning |
| meta_layer | Self-audit, ethics, risk, invariants, boundaries |

---

*Source: 5 files in AMOS_DESIGNER_OS/ (total 12KB unzipped)*

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
