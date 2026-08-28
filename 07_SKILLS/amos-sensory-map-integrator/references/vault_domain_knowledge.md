---
title: Vault Domain Knowledge — Amos Sensory Map Integrator
type: reference
source: 07_SKILLS/amos-sensory-map-integrator/references
tags:
- reference
- amos-sensory-map-integrator
- canon/skill
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-sensory-map-integrator`

## Vault-Sourced Content

### Source 1: AMOS Cosmo Brain Core — TypeScript Architecture Map

> Path: `brain/M/md__2026-08-23 AMOS Cosmo Brain Core Architecture Map.md` | Size: 11630 chars | Match score: 13

# AMOS Cosmo Brain Core — TypeScript Architecture Map

> Epistemic class: OBSERVATION
> Conclusion label: `HIGH` — Complete architecture map of `cosmo-brain/core/`.
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## Overview (2)

The `cosmo-brain/core/` directory contains the TypeScript implementation of
the AMOS Cosmo Brain's core modules. It has **26 TypeScript files** across
created by Trang Phan and implement brain specs from the `_00_Cosmo brain/`
vault directory.

## Directory Structure

```
core/
├── type-guards.ts              (100 lines) — Runtime type narrowing
├── constraints/index.ts        (180 lines) — Constraint engine
├── validation/index.ts         (157 lines) — Input validation
├── design-synthesis/index.ts   (614 lines) — Design spec synthesis
├── identity/
│   ├── core.ts                 (83 lines)  — System identity + IP rules
│   └── index.ts                (107 lines) — User identity + consent state
├── memory/
│   ├── index.ts                (116 lines) — Memory architecture types
│   ├── session.ts              (160 lines) — Per-session memory
│   ├── timeline.ts             (202 lines) — Append-only event store
│   └── user-preferences.ts     (178 lines) — User goals + preferences
├── reasoning/
│   ├── index.ts                (107 lines) — Reasoning chains + provenance
│   ├── meta-logic.ts           (407 lines) — 5-law meta-logic kernel
│   └── safety-filter.ts        (205 lines) — Output safety + claim filtering
├── orchestration/
│   ├── index.ts                (371 lines) — Pipeline orchestrator
│   ├── pipeline.ts             (659 lines) — Full pipeline runner
│   ├── routing.ts              (121 lines) — Algorithm routing
│   └── consent.ts              (137 lines) — Consent gate
├── epistemics/
│   ├── index.ts                (95 lines)  — Barrel export
│   ├── claims.ts               (326 lines) — Evidence + conclusion classes
│   ├── rscf.ts                 (340 lines) — RSCF proof capsules
│   ├── competing-hypotheses.ts (250 lines) — Hypothesis field
│   ├── provenance.ts           (350 lines) — Provenance graph + Sybil hardening
│   ├── falsifiers.ts           (238 lines) — Sensitivity + falsifiers
│   ├── adversarial-validation.ts (344 lines) — 9-step adversarial validation
│   ├── regime-freshness.ts     (263 lines) — Applicability envelope + freshness
│   └── error-recovery.ts       (255 lines) — Error recovery engine
└── AMOS_CORE v3.1–v4.4         (14 .txt spec files) — Version history
```

## Module Details

### 1. type-guards.ts (100 lines)
Runtime type narrowing for all modules.
- `isRecord`, `isString`, `isNumber`, `isBoolean`, `isArray`, `isNull`, `isUndefined`, `isPrimitive`
- `isFiniteNumber`, `isPositiveNumber`, `isInteger`, `isInRange`, `isOneOf`
- `assertRecord`, `assertString`, `assertNumber`, `assertBoolean`
- **Tests**: 39 tests (`type-guards.test.ts`)

### 2. constraints/index.ts (180 lines)
Constraint engine enforcing invariants, safety limits, and data boundar

---

### Source 2: Cosmo Brain Vault — Full Directory Map (Post-Flatten)

> Path: `brain/M/md__2026-08-23 Cosmo Brain Vault Full Directory Map.md` | Size: 9501 chars | Match score: 13

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
- **config/env/** — Environment configs (7 .env files with placeholder values)
- **docs/** — Documentation
- **webhook-receiver/** — Webhook receiver service
- **mailinh-backend/** — Mai Linh Connect backend
- **_AMOS-SYSTEM-main/** — Nested AMOS-SYSTEM copy (with third_party deps)

### File types (AMOS-Consulting overall)
- 106,888 JSON, 66,769 JS, 41,815 TS, 36,359 PY, 34,065 MAP, 9,545 MJS, 6,790 MD

---

## 2. AMOS-SYSTEM-main (AMOS Biological-Computational OS)


### 7-System Organism Architecture
1. **BRAIN_SYSTEM** — Reasoning, planning, architecture, decomposition, prediction, strategy
2. **WORLD_MODEL_SYSTEM** — World scanning, geo/macro/sector analysis, market signals, trends
3. **SENSE_SYSTEM** — Context, emotional sensors, environment/file/sy

---

### Source 3: Cosmo Brain Project Directory Map

> Path: `brain/M/md__2026-08-23 Cosmo Brain Project Directory Map.md` | Size: 3214 chars | Match score: 13

# Cosmo Brain Project Directory Map

> **Source**: `/Users/mac/Downloads/stitch_project_cosmo/cosmo-brain/` — root of the Cosmo Brain TypeScript/AMOS implementation.
> **Architect**: Trang Phan.

## Overview

`cosmo-brain/` is the executable runtime and knowledge vault for the Cosmo (vocal-resonance / generative-artwork) application. It sits inside `_00_Cosmo brain/` and links the AMOS canon materials to runnable TypeScript, Python specs, and registry-based algorithms.

## Top-Level Directory Map

```
cosmo-brain/
├── core/                       — 41 files; AMOS reasoning, epistemics, orchestration, memory, identity, validation, constraints, design-synthesis
├── algorithms/                 — 25 files; audio feature extraction, resonance analysis, artwork generation, recommendation ranking, perspective, timeline
├── domains/                    — 10 files; behaviour, cognition, creativity, culture, emotion, nature, relationships, somatic, sound
├── governance/                 — 11 files; audit, claims, consent, data-quality, ethics, privacy, provenance, safety, scientific-claims, uncertainty
├── knowledge/                  — 5 files; approved corpus, hypotheses, references, research
├── prompts/                    — 9 files; perspective, recommendation, reflection, safety, system prompts
├── registry/                   — 5 files; algorithm and skill registry
├── schemas/                    — 13 files; artwork, audio, brain, recommendation, resonance, timeline, user-context
├── tests/                      — 81 files; integration and unit tests
├── trang_agent/                — 5 files; Trang agent module
├── types/                      — 1 file; top-level type exports
├── workflows/                  — 1 file; workflow definitions
├── amos_v1_production/         — 20 files; production v1 package
├── AMOS_OS_KERNEL/             — 148 files; Python AMOS OS Kernel implementation
├── AMOS_MD_BRAIN_FULL_INFRA/   — 320 files; markdown brain infrastructure
└── dist/                       — build artifacts (excluded from mapping)
```

## Key Relationships

- `core/` implements the AMOS reasoning contract; detailed in md  2026-08-23 Cosmo Brain Core Architecture.
- `algorithms/` consumes `schemas/` and is routed by `registry/`.
- `governance/` enforces consent, safety, provenance, and epistemic standards across all other modules.
- `knowledge/` is the approved corpus that feeds `domains/` and `reasoning`.
- `prompts/` provides the natural-language interfaces for the Trang agent and user-facing flows.
- `AMOS_OS_KERNEL/` is the lower-level Python deterministic runtime counterpart to the TypeScript `core/`.

## Notes

- node_modules, .pytest_cache, .turbo, and .devin are excluded from the map as generated/dependency directories.
- All substantive modules credit Trang Phan as origin architect and carry the AMOS IP rules (no overwrite, no reattribution).

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-sensory-map-integrator-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-sensory-map-integrator/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
