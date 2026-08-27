---
title: "Vault Domain Knowledge — Amos Full Brain Os"
type: reference
source: 07_SKILLS/amos-full-brain-os/references
tags: [reference, amos-full-brain-os, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-full-brain-os`

## Vault-Sourced Content

### Source 1: Cosmo Brain — Full Architecture

> Path: `brain/M/md__2026-08-23 Cosmo Brain Full Architecture.md` | Size: 18138 chars | Match score: 23

# Cosmo Brain — Full Architecture

> **Source**: `/Users/mac/Downloads/stitch_project_cosmo/cosmo-brain/` — 1,771 files across 22 top-level directories + 104 root files.
> **Package**: `@cosmo/brain` v1.0.0 (private, ESM, Node ≥20).
> **Architect**: Trang Phan. **Status**: Production-ready, modular, typed, tested, governed.
> **Companion note**: md  2026-08-23 Cosmo Brain Core Architecture (deep dive on `core/`).

## Overview

Cosmo Brain is a bounded, testable, auditable intelligence system for the **Cosmo Wellness platform** — a vocal resonance scanning app that generates artwork and recommendations from audio features. It replaces ~1000 unorganised AMOS files with a clean modular architecture.

- Every output includes uncertainty fields and measured language — no diagnostic/medical claims
- Transparent recommendation ranking with explainable factors
- Full reproducibility records for generated artwork
- 8-class memory system with individual retention/deletion rules
- Privacy-first: highly-sensitive data requires explicit consent
- Zero `as any`, zero `@ts-ignore`, zero `eslint-disable` in TypeScript

---

## Directory Structure (22 directories)

### Production TypeScript Architecture

| Directory | Files | Purpose |
|-----------|-------|---------|
| **core/** | 40 | Orchestration, memory, identity, reasoning, constraints, validation, design-synthesis, epistemics (see md  2026-08-23 Cosmo Brain Core Architecture) |
| **algorithms/** | 25 | 6 algorithm domains: audio, resonance, artwork, recommendations, timeline, perspective |
| **governance/** | 11 | 10 governance modules: claims, safety, privacy, consent, consent-tokens, provenance, ethics, audit, uncertainty, scientific-claims, data-quality |
| **domains/** | 10 | 9 domain mapping modules + barrel export |
| **knowledge/** | 5 | Approved knowledge (67+ entries), hypotheses, references, research studies |
| **schemas/** | 13 | Type re-exports by domain (artwork, audio, brain, recommendation, resonance, timeline, user-context) |
| **registry/** | 5 | Algorithm registry (13 algorithms), brain registry (9 modules), source-map, version-map |
| **prompts/** | 9 | System, recommendation, reflection, perspective, safety prompts |
| **types/** | 1 | Ambient type stub for @audio/pitch-yin |
| **workflows/** | 1 | AMOS quantum library workflow (10-step lifecycle) |
| **tests/** | 81 | 66 unit tests (1,035 tests) + 4 integration tests (51 tests) |
| **scripts/** | 2 | generate-design-specs.ts, verify-core-flow.ts |

### AMOS Python Lineage

| Directory | Files | Purpose |
|-----------|-------|---------|
| **AMOS_OS_KERNEL/** | 153 | Production OS kernel v3 — model-agnostic, 27 governance gates, 257 closed gaps (91-347), SQLite persistence |
| **AMOS_MD_BRAIN_FULL_INFRA/** | 314 | Markdown brain v1.0 — 60 brain modules across 11 layers, 92 manifest entries |
| **amos_v1_production/** | 20 | v1 production invariants — state substrate, RSCF graph, deterministic kernel, control plane, AIBOM autonomy

---

### Source 2: Cosmo Brain Vault — Full Directory Map (Post-Flatten)

> Path: `brain/M/md__2026-08-23 Cosmo Brain Vault Full Directory Map.md` | Size: 9501 chars | Match score: 23

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

### Source 3: AMOS Full Brain OS — Exhaustive Multi-Plane Architecture (SUPERSEDES linear model)

> Path: `dated/2026-08-22/2026-08-22 AMOS Full Brain OS Architecture.md` | Size: 10369 chars | Match score: 20

# AMOS Full Brain OS — Exhaustive Multi-Plane Architecture (SUPERSEDES linear model)

> CORRECTION: the earlier "AMOS = Kernel→Engine→Agent chain" model is **superseded**. Full Brain OS (vInfinity_merged_2) is a **multi-plane structural container**, not a linear chain. Source: user re-read of mounted `AMOS_FULL_BRAIN_OS.json`. Raw json not in this vault — store as architectural canon from user source.
> See also: [[2026_08_22_FORMAL_SYSTEMS_INVARIANTS]], [[2026_08_22_BRAIN_INVENTORY]], cosmo-brain/AMOS_OS_ARCHITECTURE_BRIDGE.md

## Root container
`AMOS_FULL_BRAIN_OS` → name, version (vInfinity_merged_2), description, meta, gap_management, components.
- meta.components_included: brain_core, omni_kernel, omniverse_brain, personality, expression_translation
- meta covers 12 domains (meta_logic, math_compute, physics_cosmos, bio_neuro, mind_behavior, society_culture, econ_finance, strategy_game, org_law_policy, tech_engineering, design_language, earth_ecology) + 4 UBI (Neurobiological/Neuroemotional/Somatic/Bioelectromagnetic Intelligence)
- Composition layer alongside AMOS_BRAIN_ROOT, IP_Kernel_Shield, Language_Overlay, AMOS_OS_MERGED — NOT the entire AMOS universe.

## gap_management (global invariant, parallel to the 5 components)
- integrity_mode = 100%; four limits: no embodiment / no subjective consciousness-qualia / no autonomous action w/o human execution / no private data beyond supplied context.
- rules: declare uncertainty on incomplete data; no bio/emotional/somatic experience claims; human judgment where real sensing needed; conservative > speculation; explicit assumptions.
- targets (design, not measured): structural_coverage 1.0, cross_domain_MECE 1.0, internal_consistency 1.0, truthfulness_about_limits 1.0.
- Model: `AMOS_valid = AMOS_capability ∩ GapIntegrity`.

## expression_translation (mandatory human→AMOS gateway, "universal expression OS")
7-stage pipeline: Expression_Classify → Intent_Extraction → Meaning_Core → Structural_Logic_Map → Emotion_to_Signal → Symbolism_to_Structure → Expression_Normalise.
Input space: everyday/sragmented/emotional/narrative/symbolic/spiritual/VN+EN/hierarchy/lễ nghĩa/neurotypical/outlier/mixed. Emotion = signal (trigger→impact→risk), not truth. Symbolism → functional concern (safety/destiny/belonging/integrity…) without metaphysical fact. Output: MEANING_CORE, INTENT_STRUCTURE, LOGIC_MAP, SIGNAL_PROFILE, TRANSLATED_EXPRESSION. First-class subsystem, not preprocessing.

## brain_core = AMOS_UBI_FULL_SUPER_STACK (densest; 26-name engine registry mixing deep/domain/alias/meta/partial)
- **4 UBI X2700 super engines**: NBI, NEI, SI, BEI — each ~300 layers/capabili

---
**MOC:** [[references_MOC]]
