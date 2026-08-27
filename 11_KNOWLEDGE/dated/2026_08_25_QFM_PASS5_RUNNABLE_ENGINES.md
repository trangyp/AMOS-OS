---
title: 2026 08 25 QFM PASS5 RUNNABLE ENGINES
type: engine
tags: [daily/integrity-pass, topic/qfm-runnable-engines, dated, dated/2026-08-25]
created: 2026-08-25
conclusion_class: AMOS MODEL / DERIVED
---



# 2026-08-25 Pass 5 — QFM Runnable Engines + Skill Enhancement

## The shift this pass: prose → executable

Previous passes produced rich skill/agent/workflow documents. This pass made the priority stack **runnable**: three Python engines in `cosmo-brain/` now back the agents with deterministic computation, each with a self-contained selftest that passed green on first run.

## New runnable engines (all first-run green)

| Engine | Selftest | Implements |
|--------|----------|-----------|
| `cosmo-brain/lacunarity_auditor.py` | **13/13** | gliding-box Λ = Var/Mean², multi-scale scan, band classification (crystal/Goldilocks/pathological/crisis), H/M/L layer audits vs healthy-body & healthy-society reference tables, PV persistence scoring, survival-law verdict, hallucination-risk gate |
| `cosmo-brain/nine_hoshi_compass.py` | **9/9** | compass walkthrough (D16→…→Q4 walk order), D4-framing rule (empty competing-hypotheses corner blocks K10), liberty counting, ko governor cooling-off, territory-vs-influence gating |
| `cosmo-brain/ancient_math_equations.py` | **9/9** | AM001 cycle_alignment (Maya LCM 18,980 days verified computationally), AM002 ratio_harmony vs {φ,√2,3/2,4/3}, AM003 recurrence guard (≥3 scales before "fractal" label), AM004 entropy_shift on normalized proxy, AM005 symbolic density |

## Skill enhancements
- `amos-ancient-math-fractal-architecture` v1.0 → v2.0: from 1.8KB skeleton to full operational definitions — compute recipes, worked Maya example (RH≈0.993 vs √2 honestly labeled near-harmony not identity), decision gates
- `amos-fractal-lacunarity-metrics`: engine link added to Related section (skill had grown to 251 lines via sibling generator; respected its structure)
- `amos-cognitive-field-19x19`: compass engine link added

## Agent wiring
- `amos-lacunarity-auditor-agent` → 6 caps (+engine execution), dep on lacunarity_auditor.py
- `amos-cognitive-field-navigator-agent` → 6 caps, dep on nine_hoshi_compass.py

## Verification
- All 3 engines selftest green; 0 broken agent deps; 0 empty skills (233 dirs)
- Audit RESULT OK: registry 315↔277, 0 unregistered; vault health pass
- cosmo app unaffected and green (tsc clean, 28/28)

## Pattern to institutionalize
Every QFM agent should have a runnable engine + passing selftest behind its capabilities — prose-only agents are MODEL claims; engines make them executable. Candidates for next pass: tensor gate checker, wealth-game equation evaluator, DMER trajectory classifier already exists (dmer_kernel.py).

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · 2026-08-25-qfm-pass15-corpus-depth · 2026-08-25-qfm-pass5-zero-empty · 2026-08-25-qfm-pass4-runtime-sync

---
**MOC:** [[DATED_MOC]]
