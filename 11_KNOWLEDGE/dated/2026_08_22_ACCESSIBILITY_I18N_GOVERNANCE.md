---
title: 2026 08 22 ACCESSIBILITY I18N GOVERNANCE
tags:
- dated
- dated/2026-08-22
- canon/knowledge
type: document
source: 11_KNOWLEDGE/dated
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# 2026-08-22 Accessibility & i18n Governance

## Overview
Closed gap cluster 270-273: Accessibility & i18n. 4 gaps, 4 subsystems, 4 gates, 48 tests.

## Module
- **File**: `cosmo-brain/AMOS_OS_KERNEL/amos/governance/accessibility_i18n.py`
- **Governor**: `AccessibilityI18nGovernor` — 4 post-execution gates
- **Skill**: `amos-accessibility-i18n`

## Subsystems (4)
| Gap | Subsystem | Gate Name | Status |
|-----|-----------|-----------|--------|
| 270 | AccessibilityConformanceChecker | accessibility-270-non-conformant | FAIL |
| 270 | AccessibilityConformanceChecker | accessibility-270-unassessed | CONDITIONAL |
| 271 | SemanticParityChecker | i18n-271-semantic-divergence | FAIL |
| 271 | SemanticParityChecker | i18n-271-high-semantic-distance | CONDITIONAL |
| 272 | CulturalContextChecker | i18n-272-cultural-inappropriate | FAIL |
| 272 | CulturalContextChecker | i18n-272-needs-adaptation | CONDITIONAL |
| 273 | TranslationLossChecker | i18n-273-severe-translation-loss | FAIL |
| 273 | TranslationLossChecker | i18n-273-high-translation-loss | CONDITIONAL |

## Key Lessons
1. **Each gate produces two possible gate names**: FAIL (takes precedence) and CONDITIONAL. This is a pattern across all 4 gates.
2. **WCAG conformance levels**: A, AA, AAA. Default is AA.
3. **Translation loss categories**: NONE, MINIMAL, MODERATE, SIGNIFICANT, SEVERE. `has_severe_loss()` checks both SEVERE and SIGNIFICANT.
4. **Semantic distance threshold**: 0.3 for high distance. Translation loss score threshold: 0.5.
5. **Aliases needed for __init__.py**: `AccessibilityConformanceAssessor`=`AccessibilityConformanceChecker`, `SemanticParityMeter`=`SemanticParityChecker`, `CulturalContextEvaluator`=`CulturalContextChecker`, `TranslationLossMeter`=`TranslationLossChecker`
6. **Kernel attribute**: `accessibility_governor` (not `accessibility_i18n_governor`)
7. **Store methods**: `list_accessibility_conformance`, `list_semantic_parity`, `list_cultural_context`, `list_translation_loss` (all singular)

## Completion Graph State
- **183 closed gaps** (91-273) across 19 clusters
- **47 open gaps** (274-320) across 4 clusters
- **1310 total tests** in AMOS OS Kernel

## Related
- 2026-08-22 Privacy Compliance Governance
- 2026-08-22 Data Quality Governance
- amos-completion-graph-workflow
- accessibility_i18n

---
- [[KNOWLEDGE_MOC]]
**MOC:** [[DATED_MOC]]
