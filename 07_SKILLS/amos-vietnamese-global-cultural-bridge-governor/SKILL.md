---
title: SKILL — Amos Vietnamese Global Cultural Bridge Governor
type: skill
source: 07_SKILLS/amos-vietnamese-global-cultural-bridge-governor
name: amos-vietnamese-global-cultural-bridge-governor
description: Vietnamese-Global Cultural Bridge Governor — cross-domain capability
  bridging C06 Vietnamese-specific cultural systems (F07 Vietnam Regional, gia hệ
  energy models) with C06 global frameworks (F01-F06, F08-F10). Governs bidirectional
  translation preserving Vietnamese cultural specificity while enabling global comparison.
  Enforces universalization firewall (no VN-specific claim universalized without cross-cultural
  evidence) and cultural specificity preservation (no global model applied to VN context
  without validation). Use when Vietnamese cultural claims need translation to global
  framework terms, when global models need validation for Vietnamese context, or when
  the bidirectional cultural bridge needs governance. Use when amos-c06-society-culture-master
  routes to this specialized capability.
parent_skill: amos-c06-society-culture-master
domain: cross-domain (C06 Vietnamese ↔ Global)
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
claim_ceiling: 0.9
status: production_ready
created: 2026-08-27
tags:
- type/skill
- canon/skill
- domain/society-culture
- canon-group/human-system
- topic/sociology
- capability/governance
- capability/vietnamese
- capability/the_bridge
- capability/enforcement
- topic/vietnamese
- rscf/epistemic
- rscf/B-boundary
- rscf/C-constraint
- rscf/G-relation
- rscf/T-topology
- rscf/type-system
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-vietnamese-global-cultural-bridge-governor
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
---







# Vietnamese-Global Cultural Bridge Governor

## Identity

Origin architect: **Trang Phan**. Domain: cross-domain (C06 Vietnamese ↔ Global). Parent: amos-c06-society-culture-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
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

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-vietnamese-global-cultural-bridge-governor_MOC]]

## Examples

- **Scenario**: When Vietnamese cultural claims need translation to global framework terms
  - **Input**: A query matching this skill's domain (cross-domain (C06 Vietnamese ↔ Global))
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When global models need validation for Vietnamese context
  - **Input**: A query matching this skill's domain (cross-domain (C06 Vietnamese ↔ Global))
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When governing the bidirectional cultural bridge (BRIDGE_PERMITTED / BLOCKED / CONDITIONAL)
  - **Input**: A query matching this skill's domain (cross-domain (C06 Vietnamese ↔ Global))
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the cross-domain (C06 Vietnamese ↔ Global) domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c06-society-culture-master` — routes to this skill when cross-domain (C06 Vietnamese ↔ Global) specialization is needed
- **Peers**: Other skills in the `cross-domain (C06 Vietnamese ↔ Global)` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `references/vn_20_impossible_competitions.md` — loaded on demand
- `references/vn_akashic_thong_thien.md` — loaded on demand
- `references/vn_amos_absolute_architecture.md` — loaded on demand
- `references/vn_amos_absolute_integration.md` — loaded on demand
- `references/vn_cross_time_civilization_journey.md` — loaded on demand
- `references/vn_gia_he_dieu_tiet.md` — loaded on demand
- `references/vn_map_of_everything.md` — loaded on demand
- `references/vn_neural_invariance_silence.md` — loaded on demand
- `references/vn_what_you_discovered.md` — loaded on demand
- `[[amos-vietnamese-global-cultural-bridge-governor_MOC]]` — skill Map of Content
- `amos-c06-society-culture-master` — parent skill
- `[[amos-vietnamese-global-cultural-bridge-governor-workflow]]` — corresponding workflow
- `amos-vietnamese-global-cultural-bridge-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-vietnamese-global-cultural-bridge-governor
node_type: skill
path: 07_SKILLS/amos-vietnamese-global-cultural-bridge-governor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
