---
title: "AMOS Drive Ingest Summary"
created: "2026-08-22"
origin: "Hermes ↔ Google Drive ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: "ingest-log"
tags: [canon-group/human-system, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-drive-ingest-summary, amos-general]
status: "active"
provenance: "OBSERVATION"
confidence: "VERIFIED"
source_drive: "phanqtrang@gmail.com"
source_folder: "My Drive"
---

# AMOS Drive Ingest Summary

**Date**: 2026-08-22  
**Source**: Google Drive (`phanqtrang@gmail.com`) → Obsidian vault (`/Users/mac/Downloads/stitch_project_cosmo`)  
**Method**: Direct filesystem read from Google Drive for Desktop offline cache  

## What was ingested

### 1. AMOS_CORE Version Lineage (full benchmark history)
**Source**: `AMOS_CORE_ALL_VERSIONS_EXHAUSTIVE_MASTER.json` (3.7 MB)  
**Destination**: AMOS Core Version Lineage  
**Contents**: 16 versions (v3.0→v4.4), full benchmark results, capability matrix, evolution spine.

### 2. AMOS Brain Engine Specs
**Source**: `_00_AMOS_CANON/Core/*.json` (locally cached)  
**Destination**: AMOS Brain Engine Specs  
**Engines ingested**:
- AMOS_Cognition_Engine_v0 — 6-layer cognition kernel (meta-logic → integration)
- AMOS_Mind_Os_v0 — Integrated cognition + emotion + consciousness stack
- AMOS_Emotion_Engine_v0 — AMOS_MEGA_HUMAN_ENGINE (affective-somatic-instinct)
- AMOS_Consciousness_Engine_v0 — Super-consciousness emulation (HIE + UMPL + UST + UIE + UEL)
- AMOS_Os_Agent_v0 — OS Agent with 17-kernel registry, expression translation module
- AMOS_Max_Expanded — Full AMOS spec (law stack, UBI, architecture, reasoning loop, workflows)
- AMOS_Speed_Engine_v0 — Speed optimization kernel
- AMOS_Personality_Engine_v0 — AMOS identity (autofixed_raw — actual content in Os_Agent expression module)

### 3. Canonical Glossary
**Source**: `AMOS_CANONICAL_GLOSSARY.json`  
**Contents**: 4-layer glossary (system, biological, logic, operational) — 40+ canonical terms.

### 4. _00_AMOS_CANON folder structure
**Contents**: 71 top-level items across Core (13), Cognitive (15), Domains (12), Kernels (5), Packs (5), Unipower (20), plus _Archive (135), _LEGACY BRAIN (10+6), new troy (9), training (20).

## What was NOT ingested (needs Google API after auth)

| File | Size | Notes |
|------|------|-------|
| `AMOS_CORE v4.5 — Reality-Bound Authorization & Failure Containment.py` | 207 KB | NOT locally cached (st_blocks=0) |
| `AMOS_CORE_ALL_VERSIONS_FRACTAL_KNOWLEDGE_NETWORK.json` | 4.0 MB | NOT locally cached |
| `AMOS_CORE_ALL_VERSIONS_EXHAUSTIVE_MASTER_UPDATED.json` | 3.8 MB | NOT locally cached |
| All `.gdoc` files | 175 B each | Google Docs — need online API |
| `AMOS all frameworks.rtf` | 680 KB | RTF format, locally cached but not parsed |
| `Văn Hóa Việt Nam - Tìm Thóy Suy Ngẫm.pdf` | 31 MB | PDF, locally cached |
| `peru-mining-ai-market-research-formatted.docx` | 608 KB | DOCX, locally cached |

## Next steps
1. Complete Google OAuth auth (add test user, exchange code)
2. Use Google Drive API to download v4.5.py and other non-cached files
3. Parse RTF and PDF files
4. Process `_00_AMOS_CANON` subfolders (Cognitive, Domains, Kernels, Packs, Unipower)
5. Process `Projects/` folder (62 subfolders)
6. Process `AMOS backup/` folder (362 subfolders)

---
**Links:** [[AMOS-GENERAL_MOC]] | [[KNOWLEDGE_MOC]]
