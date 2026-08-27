---
title: SKILLS README
type: note
tags: [note, 07-skills]
---

# AMOS OS Skills — Complete Inventory

## Overview
This directory contains all AMOS OS skills, indexed by the 7-Part Universe Canon scaffold (Constraint→Flow→Structure→Enforcement→Time→Adaptation→Termination). Every skill maps to one or more of the 7 canonical parts, and the inventory is MECE across the 7 parts — no skill duplicates another's responsibility, and every part has at least one skill owning it.

## Skill Directory Structure
Skills live at `.hermes/skills/amos-<name>/` and are synced to `07_SKILLS/amos-<name>/` via `hermes curator adopt`. The vault directory `07_SKILLS/` is the **canonical on-disk index**; `.hermes/skills/` is the **working copy** where skills are created and edited.

## Canonical Entry Format (SKILL.md)
Each skill has a `SKILL.md` with YAML frontmatter and markdown body:

```yaml
name: amos-<skill-name>
description: <one sentence — exactly 57 characters or fewer, no truncation>
version: 1.0.0
origin_architect: <your name or "user-supplied">
source: <path to vault source>
type: skill
tags: [topic/<part>, ...]
provenance: SOURCE_CLAIM | DERIVED | MODEL | UNKNOWN
confidence: HIGH | MEDIUM | FRONTIER
```

## 7-Part Mapping (Required)
Every SKILL.md MUST include a "## 7-Part Mapping" section:

| Part | Owned By | Gap Status |
|------|----------|-----------|
| I — Constraint | <skill names> | <FILLED/EMPTY> |
| II — Flow | <skill names> | <FILLED/EMPTY> |
| III — Structure | <skill names> | <FILLED/EMPTY> |
| IV — Enforcement | <skill names> | <FILLED/EMPTY> |
| V — Time | <skill names> | <FILLED/EMPTY> |
| VI — Adaptation | <skill names> | <FILLED/EMPTY> |
| VII — Termination | <skill names> | <FILLED/EMPTY> |

## Known Skills (11 currently with SKILL.md in hermes)
- amos-7-part-universe-canon — the 7-part canon itself (owned by Part I–VII)
- amos-a-matrix-system-dynamics — A-Matrix dynamics (Part III: Structure)
- amos-law-stack-enforcement — Law of Law/Rule of 2/Rule of 4 (Part IV: Enforcement)
- amos-qfm-agent — QFM agent with Trinity Model (Parts I, II, IV)
- amos-qfm-orchestration — 7-phase QFM pipeline (Part II: Flow)
- amos-fractal-equation-families — FR001–FR025 (Part III: Structure)
- amos-quantum-fractal-math — quantum-fractal-math master (Parts I, III, V)
- amos-optimization-claim-governance — claim hierarchy (Part IV: Enforcement)
- amos-conjecture-discipline — BSD gates (Part VII: Termination)
- amos-entropy-lacunarity-viability — entropy/lacunarity (Part V: Time)

## Gap Inventory
| Part | Skills | Gap Status |
|------|--------|-----------|
| I — Constraint | 2 | ✅ Filled |
| II — Flow | 3 | ✅ Filled |
| III — Structure | 5 | ✅ Filled |
| IV — Enforcement | 4 | ✅ Filled |
| V — Time | 2 | ✅ Filled |
| VI — Adaptation | 1 | ⚠️ EMPTY — needs skill |
| VII — Termination | 2 | ✅ Filled |

## Sync Protocol
1. Create/edit `.hermes/skills/amos-<name>/SKILL.md`
2. Run `hermes curator adopt amos-<name>` to sync to `07_SKILLS/amos-<name>/SKILL.md`
3. Run `brain-consistency-audit.py` to verify no empty parts
4. Commit both vault and hermes sides

## Gap Resolution Priority
1. Part VI — Adaptation (currently 1 skill; needs 2+ for MECE)
2. Part V — Time (currently 2 skills; verify MECE split)
3. Any new skill must map to an EMPTY part before filling a PARTIALLY-FILLED part

---
**MOC:** [[07_SKILLS_MOC]]
