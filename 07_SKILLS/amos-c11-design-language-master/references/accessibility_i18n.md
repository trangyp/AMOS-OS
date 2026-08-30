---
title: accessibility i18n
type: reference
source: 07_SKILLS/amos-c11-design-language-master/references
tags:
- reference
- amos-c11-design-language-master
- type/skill
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Accessibility & I18n Governance

> Source: `_00_Cosmo brain/dated/2026-08-22/2026-08-22 AMOS Accessibility I18n.md`
> Epistemic class: SOURCE_DERIVED

---
title: AMOS Accessibility I18n
created: "2026-08-22"
type: "note"
tags: [canon-group/human-system, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-accessibility-i18n, dated, dated/2026-08-22]
status: "living"
provenance: "MODEL"
confidence: "VERIFIED"
---

# AMOS Accessibility & i18n (Gaps 270-273)

> Epistemic class: MODEL (code artifact + test verification).
> Related: 2026-08-22 AMOS Privacy Compliance Licensing · 2026-08-22 AMOS Uncertainty Calibration · amos-completion-graph-workflow

## Summary

Closed gaps 270-273 by implementing the **Accessibility & i18n** governance
module (`amos/governance/accessibility_i18n.py`). This is the 20th governance
gate in `AmosKernel.run()`, evaluated post-execution.

## 4 Subsystems

| Gap | Subsystem | Class | Purpose |
|-----|-----------|-------|---------|
| 270 | Accessibility conformance | `AccessibilityConformanceChecker` | WCAG 2.2 A/AA/AAA conformance |
| 271 | Semantic parity | `SemanticParityChecker` | Multilingual semantic parity |
| 272 | Cultural context | `CulturalContextChecker` | Cultural-context robustness |
| 273 | Translation loss | `TranslationLossChecker` | Translation-loss measurement |

## Gate Evaluation

`AccessibilityI18nGovernor.evaluate_post()` returns 4 gate results:
- `accessibility-270-non-conformant` — FAIL if non-conformant, CONDITIONAL if unassessed
- `i18n-271-semantic-divergence` — FAIL if divergence, CONDITIONAL if high distance
- `i18n-272-cultural-inappropriate` — FAIL if inappropriate, CONDITIONAL if needs adaptation
- `i18n-273-severe-translation-loss` — FAIL if severe/significant, CONDITIONAL if high loss

## Key Semantics

1. **WCAG conformance levels**: A, AA, AAA (WCAGConformanceLevel enum)
2. **Conformance status**: CONFORMANT, PARTIAL, NON_CONFORMANT, NOT_ASSESSED
3. **Semantic parity status**: PARITY, PARTIAL_PARITY, DIVERGENCE, NOT_MEASURED
4. **Cultural context status**: APPROPRIATE, NEEDS_ADAPTATION, INAPPROPRIATE, NOT_ASSESSED
5. **Translation loss categories**: NONE, MINIMAL, MODERATE, SIGNIFICANT, SEVERE
6. **API pattern**: All subsystems use `record()` for creation. No `assess()`/`measure()`/`evaluate()` helper methods — status is set explicitly by caller.
7. **Gate naming**: Uses `accessibility-270-*` for gap 270 and `i18n-27X-*` for gaps 271-273.
8. **Governor attributes**: `accessibility`, `semantic_parity`, `cultural_context`, `translation_loss`
9. **Empty state**: All 4 gates return PASS on empty state (no records = no violations).

## Implementation Chain

- **Types**: `amos/core/types.py` — 4 dataclasses + 5 enums
- **Schema**: `amos/state/store.py` — 4 tables + 4 put/list method pairs
- **Module**: `amos/governance/accessibility_i18n.py` — 4 subsystems + governor
- **Kernel**: `amos/kernel.py` — import, instantiation, gate evaluation
- **Exports**: `amos/__init__.py` — all types + `AccessibilityI18nGovernor`
- **Tests**: `tests/test_accessibility_i18n.py` — 30 tests
- **Seeder**: `amos/governance/seed_completion.py` — gaps 270-273 in CLOSED_CLUSTERS

## Completion Graph Impact

- **Closed gaps**: 179 → 183 (gaps 270-273 = 4 gaps closed)
- **Open gaps**: 51 → 47
- **Total tests**: 1262 → 1292 (30 new tests)
- **All 1292 tests pass**

## External References

- **WCAG 2.2**: Web Content Accessibility Guidelines, W3C Recommendation (2023)
- **WCAG conformance levels**: A (minimum), AA (mid), AAA (highest)
- **Semantic distance**: Cosine/euclidean distance between multilingual embeddings
- **Translation loss taxonomy**: Campbell & Hatim translation studies
- **Cultural context**: Hofstede cultural dimensions, Nisbett cultural psychology
- **COSMO accessibility**: Ap-001 (artwork description), Ap-002 (reduced motion), Ap-003 (color contrast), Ap-004 (focus management)

## Lessons Learned

1. **User's class naming**: User uses `*Checker` suffix (not `*Assessor`/`*Meter`/`*Evaluator`).
2. **User's API pattern**: Uses `record()` for creation, no helper methods like `assess()`/`measure()`. Status i

---
**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c11-design-language-master-accessibility-i18n
node_type: reference
path: 07_SKILLS/amos-c11-design-language-master/references/accessibility_i18n.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
