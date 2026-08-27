---
title: 2026 08 25 QUANTUM V080 THERMODYNAMICS CYCLE
tags: [dated, dated/2026-08-25]
type: document
source: 11_KNOWLEDGE/dated
---


# Quantum Library v0.8.0 Cycle — Quantum Thermodynamics (2026-08-25)

## Cycle summary

Focus domain: **Quantum Thermodynamics** — was the thinnest family (3 entries), now 6.

### New canonical entries
| ID | Content | Source |
|---|---|---|
| AM-QT-004 | Jarzynski equality + Crooks fluctuation theorem; second-law recovery via Jensen | Jarzynski PRL 78:2690 (1997); Crooks PRE 60:2721 |
| AM-QT-005 | Maxwell demon resolved: Sagawa–Ueda feedback bound + Landauer erasure closes the cycle; information-to-work cap k_BT·ln2 per bit | Sagawa & Ueda PRL 100:080403 (2008); Koski PRL 113:030601 (2014) |
| AM-QT-006 | Ergotropy (extractable work ≠ stored energy) + collective QB charging exponent α∈[1,2] | Binder et al. NJP 17:075015 (2015) |

Plus bounds 057–059, invariants 035–036, failure modes FM56–58, sources S61–S68 (all Tier 1).

## De-duplication rulings this cycle
- Crooks kept INSIDE AM-QT-004 (strictly implies Jarzynski)
- Landauer NOT re-entered (already AM-QT-001); referenced

## Verification (all live runs)
- Loader parse: 75/75 unique entries, version 0.8.0 ✓
- Injection: axioms 66 / bounds 70 / invariants 42 / FMs 45, Integration OK ✓
- Approved index regenerated: 75 quantum + 22 foundational, 0 empty sources ✓
- Canon gate self-test: 10/10 ✓
- TS suite: 1142/1142 ✓

## Incident during cycle
External writer modified `tests/unit/knowledge.test.ts` to import a never-existing
`getApprovedKnowledgeByCategory`. Resolved by ADDING that function to the generator
(runtime-safe string-typed getter) rather than reverting the test — both API and
test contract now satisfied. Same actor as prior redirect-clobbering events;
watch for further uncommitted test edits.

## Commits
`6994bc6` v0.8.0 library + index · skill update commit

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[2026-08-25-qfm-pass15-corpus-depth]] · [[2026-08-25-qfm-pass5-zero-empty]] · [[2026-08-25-qfm-pass4-runtime-sync]]

---
**MOC:** [[DATED_MOC]]
