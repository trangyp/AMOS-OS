---
title: MD 2026 08 23 COSMO BRAIN PROJECT DIRECTORY MAP
origin_architect: Trang Phan
provenance: direct file inspection of cosmo-brain/ on 2026-08-23
confidence: 0.95
epistemic_class: OBSERVATION
conclusion_class: VERIFIED
tags: [cosmo-brain, project-map, typescript, amos, architecture, algorithms, governance, domains, schemas, registry, knowledge, prompts, brain]
---


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

- `core/` implements the AMOS reasoning contract; detailed in md__2026-08-23 Cosmo Brain Core Architecture.
- `algorithms/` consumes `schemas/` and is routed by `registry/`.
- `governance/` enforces consent, safety, provenance, and epistemic standards across all other modules.
- `knowledge/` is the approved corpus that feeds `domains/` and `reasoning`.
- `prompts/` provides the natural-language interfaces for the Trang agent and user-facing flows.
- `AMOS_OS_KERNEL/` is the lower-level Python deterministic runtime counterpart to the TypeScript `core/`.

## Notes

- node_modules, .pytest_cache, .turbo, and .devin are excluded from the map as generated/dependency directories.
- All substantive modules credit Trang Phan as origin architect and carry the AMOS IP rules (no overwrite, no reattribution).

---
**Links:** [[BRAIN_MOC]] | [[KNOWLEDGE_MOC]]
