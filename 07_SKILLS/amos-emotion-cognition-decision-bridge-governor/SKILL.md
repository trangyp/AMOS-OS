---
title: SKILL — Amos Emotion Cognition Decision Bridge Governor
type: skill
source: 07_SKILLS/amos-emotion-cognition-decision-bridge-governor
name: amos-emotion-cognition-decision-bridge-governor
description: Emotion-Cognition-Decision Bridge Governor — mind and behavior capability. Bridges C05 emotion/personality/behavior engines with C01 meta-logic decision gates and C10 technical decision-making. Enforces the emotion influence gating invariant (emotion may bias prioritization and tone, NEVER facts or logic), connects C05's 5-axis emotion state to C01's reasoning mode selection, and unifies C05's decision style ordering with C10's diagnose-before-edit principle. Use when a decision requires both emotional state awareness and cognitive/technical rigor. Use when amos-c05-mind-behavior-master routes to this specialized capability. Do not use for pure emotional analysis without cognitive/technical decision context, or tasks outside the bridge governance scope.
parent_skill: amos-c05-mind-behavior-master
domain: cross-domain (C05→C01→C10)
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/cross-domain
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
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

# Emotion-Cognition-Decision Bridge Governor

## Identity

Origin architect: **Trang Phan**. Domain: cross-domain (C05→C01→C10). Parent: amos-c05-mind-behavior-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## The Problem This Skill Solves

C05 defines a rich emotion-personality-behavior system with a critical invariant: *"Emotional axes may bias prioritization and tone, never facts or logic."* C01 defines meta-logic decision gates and reasoning mode governance. C10 defines technical decision-making with diagnose-before-edit. However, these three systems operate independently:

1. **C05's emotion state has no bridge to C01's reasoning mode selection** — high `risk_alert` should force conservative routing in C01, but no mechanism connects them
2. **C05's decision style ordering (integrity > correctness > completeness > fluency > speed) has no bridge to C10's technical decisions** — the ordering should govern technical trade-off resolution, but no pipeline carries it
3. **C01's uncertainty/risk assessment has no input from C05's emotional state** — `confidence_level` and `risk_alert` from C05 should inform C01's uncertainty budgeting
4. **No unified decision pipeline** combines emotional state + cognitive mode + technical constraints into a single auditable decision trace

The `_00_Cosmo brain` exploration explicitly identified this gap: *"Emotion ↔ Cognition ↔ Decision: Emotion rules exist but lack direct integration with cognitive engines and decision-making pipelines."*

## When to Use

- When a decision requires both emotional state awareness (C05) and cognitive/technical rigor (C01/C10)
- When routing a query based on emotional state (e.g., high risk_alert → conservative mode)
- When resolving a technical trade-off using C05's decision style ordering
- When validating that emotion influence gating is preserved across domain boundaries
- When producing a unified decision trace that includes emotion state, cognitive mode, and technical constraints
- When C05's behavior engine goal ordering needs to be applied in a C10 technical context
- When the parent skill (`amos-c05-mind-behavior-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **ecd_bridge.route_by_emotion**: Route a reasoning task to the appropriate C01 cognitive mode based on C05's 5-axis emotion state. High `risk_alert` → conservative/defensive mode; high `curiosity_focus` → exploratory mode; high `confidence_level` → execution mode. Returns mode + routing rationale.
- **ecd_bridge.gate_emotion_influence**: Gate emotion influence when crossing from C05 into C01/C10. Enforces the invariant: emotion may bias prioritization and tone, NEVER facts or logic. Returns PERMITTED_INFLUENCE list (pacing, verbosity, caution flags, routing) and BLOCKED_INFLUENCE list (factual content, logical structure, claims of felt experience).
- **ecd_bridge.unify_decision_style**: Unify C05's decision style ordering (integrity > correctness > completeness > fluency > speed) with C10's technical trade-off resolution and C01's meta-logic decision gates. Produces a single ordered preference list applicable across all three domains.
- **ecd_bridge.assess_risk_combined**: Combine C

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-emotion-cognition-decision-bridge-governor_MOC]]

## Examples

- **Scenario**: When a decision requires both emotional state awareness (C05) and cognitive/technical rigor (C01/C10)
  - **Input**: A query matching this skill's domain (cross-domain (C05→C01→C10))
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When routing a query based on emotional state (e.g., high risk_alert → conservative mode)
  - **Input**: A query matching this skill's domain (cross-domain (C05→C01→C10))
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When resolving a technical trade-off using C05's decision style ordering
  - **Input**: A query matching this skill's domain (cross-domain (C05→C01→C10))
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the cross-domain (C05→C01→C10) domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c05-mind-behavior-master` — routes to this skill when cross-domain (C05→C01→C10) specialization is needed
- **Peers**: Other skills in the `cross-domain (C05→C01→C10)` domain may be composed in sequence
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
- `[[amos-emotion-cognition-decision-bridge-governor_MOC]]` — skill Map of Content
- `amos-c05-mind-behavior-master` — parent skill
- `[[amos-emotion-cognition-decision-bridge-governor-workflow]]` — corresponding workflow
- `amos-emotion-cognition-decision-bridge-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-emotion-cognition-decision-bridge-governor
node_type: skill
path: 07_SKILLS/amos-emotion-cognition-decision-bridge-governor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
