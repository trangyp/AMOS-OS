---
title: 2026 08 25 QUANTUM V090 HONESTY CYCLE
tags: [dated, dated/2026-08-25]
type: document
source: 11_KNOWLEDGE/dated
---


# Quantum Library v0.9.0 Cycle — Honesty Infrastructure (2026-08-25)

## Cycle summary

Focus: **honesty infrastructure** — the entries that keep AMOS claims honest about QML advantages and fault-tolerance thresholds.

### New canonical entries
| ID | Content | Source |
|---|---|---|
| **AM-QML-001** | QML generalization bounds: ε=O(sqrt((d_eff·ln(n/d_eff)+ln(1/δ))/n)); classical surrogacy under bounded measurements; dequantization discipline | Huang/Kueng/Preskill Nature Physics 17:1191 (2021) |
| **AM-QEC-009** | BP+OSD decoder: degeneracy breaks BP exactness, OSD post-processing at O(n²)/round — the real-time FT bottleneck | Roffe arXiv:2004.14440; Panteleev & Kalachev |
| **AM-QEC-010** | Circuit-level noise tiers: capacity→circuit ≈10× threshold reduction; Google 2023 below-threshold proof; correlated decoding mandatory | Bravyi et al. PRX/Nature; Google Nature 614:676 |

Plus bounds 060–062, invariants 037–038 (baseline honesty + noise-model tier), FM59–60 (dequantization miss, model-tier conflation), sources S69–S74.

## New ID family
**AM-QML** opened — quantum machine learning now a first-class canon family.

## De-duplication rulings
- BP+OSD inside AM-QEC-009 (single decoder entry)
- Correlated decoding folded into AM-QEC-010

## Verification (live runs)
- Loader parse: 78/78 unique, version 0.9.0 ✓
- Injection: axioms 68 / bounds 70 / invariants 42 / FMs 45 ✓ Integration OK
- Approved index regenerated: 78 quantum + 22 foundational = 100 total ✓
- Gate 10/10 · TS suite 1142/1142 ✓

## Downstream syncs in same pass
- UBCAR SSOT O1/O7 → v0.9.0 counts
- max-power skill description + integration refs → v0.9.0
- quantum-knowledge-pipeline skill → v2.2.0

## Commit chain
v0.9.0 library commit · skill v2.2.0 commit · SSOT/max-power sync commit

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[2026-08-25-qfm-pass15-corpus-depth]] · [[2026-08-25-qfm-pass5-zero-empty]] · [[2026-08-25-qfm-pass4-runtime-sync]]

---
**MOC:** [[DATED_MOC]]
