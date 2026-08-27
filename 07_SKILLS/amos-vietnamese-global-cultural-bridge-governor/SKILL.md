---
title: SKILL
type: skill
name: amos-vietnamese-global-cultural-bridge-governor
description: Vietnamese-Global Cultural Bridge Governor — cross-domain capability bridging C06 Vietnamese-specific cultural systems (F07 Vietnam Regional, gia hệ energy models) with C06 global frameworks (F01-F06, F08-F10). Governs bidirectional translation preserving Vietnamese cultural specificity while enabling global comparison. Enforces universalization firewall (no VN-specific claim universalized without cross-cultural evidence) and cultural specificity preservation (no global model applied to VN context without validation). Use when Vietnamese cultural claims need translation to global framework terms, when global models need validation for Vietnamese context, or when the bidirectional cultural bridge needs governance. Use when amos-c06-society-culture-master routes to this specialized capability.
parent_skill: amos-c06-society-culture-master
domain: cross-domain (C06 Vietnamese ↔ Global)
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
claim_ceiling: 0.9
status: production_ready
created: 2026-08-27
tags: [note, amos-vietnamese-global-cultural-bridge-governor]
---


# Vietnamese-Global Cultural Bridge Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c06-society-culture-master`
- **Domain**: cross-domain (C06 Vietnamese-Specific ↔ Global Frameworks)
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from C06 master knowledge and Vietnamese-specific vault content)

Bridges Vietnamese-specific cultural systems with global frameworks. C06 F07 provides Vietnam Regional Society Systems (gia hệ energy models, Vietnamese language systems, regional analysis). C06 F01-F06, F08-F10 provide global frameworks (political dynamics, institutions, social networks, culture, conflict, ethics). C09 F06 provides VN/CN legal ecosystems. This governor ensures bidirectional translation preserves cultural specificity while enabling global comparison — with a universalization firewall preventing VN-specific claims from being universalized without cross-cultural evidence.

## The Problem This Skill Solves

The `_00_Cosmo brain` exploration identified: *"Vietnamese-Specific and Global Models: Vietnamese-specific cultural, legal, and business models lack bridges to global frameworks."*

Specifically:

1. **Vietnamese cultural claims (F07) have no bridge to global frameworks** — VN-specific insights remain local, never contributing to global understanding
2. **Global frameworks have no bridge to Vietnamese context** — global models are applied to VN without validation of cultural fit
3. **No universalization firewall** — VN-specific claims risk being universalized without cross-cultural evidence
4. **No cultural specificity preservation** — global models risk erasing VN cultural specificity during application

## The Bridge

```text
Vietnamese-Specific (C06 F07, C09 F06)
    ↔ TRANSLATE ↔ Global Frameworks (C06 F01-F06, F08-F10)
```

Bidirectional translation with two firewall rules:

- **Universalization firewall**: No VN-specific claim universalized to global without cross-cultural evidence
- **Cultural specificity preservation**: No global model applied to VN without context validation

## When to Use

- When Vietnamese cultural claims need translation to global framework terms
- When global models need validation for Vietnamese context
- When governing the bidirectional cultural bridge (BRIDGE_PERMITTED / BLOCKED / CONDITIONAL)
- When detecting cultural drift between VN and global models
- When comparing VN and global cultural systems
- When assessing claims for universalization risk
- When the parent skill (`amos-c06-society-culture-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **vgc_bridge.translate_vietnamese_to_global**: Translate VN claims to global framework terms. Maps F07 VN-specific concepts to F01-F06/F08-F10 global equivalents. Tags translated claims as CONDITIONAL (context-dependent). Returns translated claim + mapping rationale + universality assessment.
- **vgc_bridge.validate_global_for_vietnamese**: Validate global model applies to VN context. Checks cultural fit, contextual validity, and specificity preservation. Returns validation result + context adaptation requirements.
- **vgc_bridge.govern_bridge**: Govern bidirectional bridge (BRIDGE_PERMITTED / BLOCKED / CONDITIONAL). Block if: universalization without evidence, global model without VN validation, cultural specificity loss. Returns bridge state + blocking reason.
- **vgc_bridge.detect_cultural_drift**: Detect cultural drift between VN and global models. Checks: VN model updated without global sync, global model updated without VN validation, cultural specif