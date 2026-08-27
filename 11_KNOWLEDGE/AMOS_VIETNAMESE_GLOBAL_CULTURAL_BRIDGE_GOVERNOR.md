---
title: AMOS VIETNAMESE GLOBAL CULTURAL BRIDGE GOVERNOR
type: bridge
claim_ceiling: 0.9
created: 2026-08-27
domain: cross-domain
epistemic_class: SOURCE_CLAIM
origin_architect: Trang Phan
parent_skill: amos-c06-society-culture-master
rscf_node_type: skill
status: production_ready
tags: [rscf/node, knowledge, vault]
- canon-group/cross-domain
- topic/vietnamese-global
- topic/cultural-bridge
---



# AMOS Vietnamese-Global Cultural Bridge Governor

> **RSCF-NODE** · skill · cross-domain (C06 Vietnamese to Global)

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c06-society-culture-master`
- **Domain**: cross-domain (C06 Vietnamese-Specific to Global Models)
- **Epistemic class**: SOURCE_CLAIM
- **Claim ceiling**: 0.90
- **Status**: PRODUCTION_READY (all 10 QA gates pass)

## The Problem This Skill Solves

The `_00_Cosmo brain` exploration identified: *"Vietnamese-Specific and Global Models: Vietnamese-specific cultural, legal, and business models lack bridges to global frameworks."*

## The Bridge

```text
Vietnamese-Specific (C06 F07, C09 F06) <-> translate <-> Global Frameworks (C06 F01-F06, F08-F10)
```

Bidirectional translation preserving Vietnamese cultural specificity while enabling global comparison.

## Capabilities (10)

1. `vgc_bridge.translate_vietnamese_to_global` — Translate VN claims to global framework terms
2. `vgc_bridge.validate_global_for_vietnamese` — Validate global model applies to VN context
3. `vgc_bridge.govern_bridge` — Govern bidirectional bridge (BRIDGE_PERMITTED/BLOCKED/CONDITIONAL)
4. `vgc_bridge.detect_cultural_drift` — Detect cultural drift between VN and global models
5. `vgc_bridge.compare_cultural_systems` — Compare VN and global cultural systems
6. `vgc_bridge.trace_cultural_provenance` — Trace provenance in both directions
7. `vgc_bridge.assess_cultural_claim` — Assess claim for epistemic class and universalization risk
8. `vgc_bridge.manage_lifecycle` — Manage lifecycle: classify, validate, trace, assess, detect
9. `vgc_bridge.detect_drift` — Detect drift in evidence chains and provenance freshness
10. `vgc_bridge.validate_outputs` — Validate outputs against domain constraints and epistemic class

## Validation Gates (10)

- G1: No contradictions across VN-global bridge
- G2: VN claims CONDITIONAL on context; global claims MODEL unless validated
- G3: Provenance recorded for every cultural claim
- G4: No VN claim universalized without evidence; no global claim applied without validation
- G5: Cultural ritual energy equations (gia hệ) tagged as MODEL
- G6: Failure mode handled
- G7: Cultural specificity preserved during translation
- G8: Universalization firewall (no VN-specific universalized without cross-cultural evidence)
- G9: Global models validated for VN context
- G10: Bidirectional provenance traceable

## Artifacts (1:1:1 binding)

- **Skill**: `.devin/skills/amos-vietnamese-global-cultural-bridge-governor/SKILL.md`
- **Agent**: `.devin/agents/amos-vietnamese-global-cultural-bridge-governor-agent.json`
- **Workflow**: `.devin/workflows/amos-vietnamese-global-cultural-bridge-governor-workflow.md`
- **Vault reference**: `.devin/skills/.../references/vault_domain_knowledge.md`

## RSCF-RELATIONS

- PARENT_OF: `amos-c06-society-culture-master`
- COMPOSES_WITH: `amos-cross-domain-tensor-composition-governor`
- BRIDGES: C06 Vietnamese-Specific, C06 Global Frameworks, C09 F06 VN/CN Legal
- INDEXED_BY: `11_KNOWLEDGE_MOC`

---

**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_CROSS_DOMAIN_TENSOR_COMPOSITION_GOVERNOR]]

## Vault Sources Enriched (2026-08-27)

### Vietnamese Heritage Frameworks (Cosmo brain: vietnamese/, 96 files)

- `TRANG ∅ FRAMEWORK – HERITAGE ∅` — Comprehensive heritage mapping
- `HERITAGE INTELLIGENCE V7 0` — Full heritage intelligence architecture
- `HERITAGE ∅ – GIẢI MÃ HOA VĂN TRỐNG ĐỒNG` — Dong Son drum pattern decoding
- `Ứng dụng Khung Độ Phức Tạp` — Complexity framework for 3 symbolic systems: Dong Son, Co Loa, Trong Dong
- `ẢNH HƯỞNG GIA HỆ` — Gia hệ as cross-10 regulatory mechanism

### Vietnamese Business/Legal Models

- `11 Tiêu chí mô hình kinh doanh` — 11 business model criteria
- `BÁO CÁO THẨM ĐỊNH PHÁP LÝ` — Legal audit report
- `BẢN ĐỀ XUẤT ĐẦU TƯ` — Investment proposal

### Cognitive Engine for Vietnamese

- AMOS_Society_Culture_Engine — Institutions, norms, demographics, cultural evolution
- AMOS_Vn_Legal_Engine — Vietnam-specialised legal reasoning, defaults to Vietnamese language and Vietnam law while preserving global legal safety constraints

---
**MOC:** [[KNOWLEDGE_MOC]]
