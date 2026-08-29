---
schema_version: 1.0
title: SKILL — Amos Causal Reasoning Master
type: skill
source: 07_SKILLS/amos-causal-reasoning-master
name: amos-causal-reasoning-master
description: AMOS Causal Reasoning — causal closure, causal hierarchy, counterfactual
  reasoning, intervention analysis. 4 causal modes (Direct, Distributed, Delayed,
  Cascading), 6 causal gates. Use when causal a. Do not use for generic tasks outside
  causal domain.
parent_skill: none
domain: causal
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- canon/skill
- domain/causal-reasoning
- rscf/source_claim
- hml/h
- epistemic/source_canon
- amos_os
- agent-template
- amos-causal-reasoning-master-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- 07-skills-moc
- references-moc
- trang-framework-recursive-ontology-dynamics
- skill
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L24_causal_epoch
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
- L24
license: MIT
steward: Trang Phan
---

# K CAUSAL HIERARCHY

## Identity

Origin architect: **Trang Phan**. Domain: causal. Parent: none. Epistemic class: SOURCE_CANON. H/M/L: H.
## When to Use

- When determining whether a relationship is causal vs correlational vs associational
- When performing counterfactual reasoning or intervention analysis
- When classifying causal modes: Direct, Distributed, Delayed, Cascading
- When evaluating causal evidence strength against the causal hierarchy
- When applying the causal firewall to prevent causal overreach
- When a child skill routes a causal analysis or counterfactual task to this master

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **causal_reason.analyze_causal**: Analyze AMOS Causal Reasoning causal hierarchy: observation, intervention, counterfactual, and causal closure.
- **causal_reason.validate_causal**: Validate AMOS Causal Reasoning causal claims for identification, confounder control, and causal gate compliance.
- **causal_reason.apply_intervention**: Apply AMOS Causal Reasoning causal intervention analysis: do-calculus, effect estimation, and counterfactual mapping.
- **causal_reason.trace_causal_provenance**: Trace AMOS Causal Reasoning causal findings to observational data, intervention records, and counterfactual models.
- **causal_reason.assess_causal_claim**: Assess AMOS Causal Reasoning causal claims for identification type, evidence strength, and mechanism vs correlation.
- **causal_reason.manage_causal_lifecycle**: Manage AMOS Causal Reasoning causal lifecycle: observe, hypothesize, test, intervene, validate, and finalize.
- **causal_reason.detect_causal_drift**: Detect causal drift: confounder emergence, regime change, causal chain break, and effect decay.
- **causal_reason.escalate_causal_gaps**: Escalate AMOS Causal Reasoning causal gaps: flag unconfirmed causality, require discriminating test, trigger analysis.
- **causal_reason.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **causal_reason.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **causal_reason.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **causal_reason.analyze_causal**: Analyze AMOS Causal Reasoning causal hierarchy: observation, intervention, counterfactual, and causal closure.
2. **causal_reason.validate_causal**: Validate AMOS Causal Reasoning causal claims for identification, confounder control, and causal gate compliance.
3. **causal_reason.apply_intervention**: Apply AMOS Causal Reasoning causal intervention analysis: do-calculus, effect estimation, and counterfactual mapping.
4. **causal_reason.trace_causal_provenance**: Trace AMOS Causal Reasoning causal findings to observational data, intervention records, and counterfactual models.
5. **causal_reason.assess_causal_claim**: Assess AMOS Causal Reasoning causal claims for identification type, evidence strength, and mechanism vs correlation.
6. **causal_reason.manage_causal_lifecycle**: Manage AMOS Causal Reasoning causal lifecycle: observe, hypothesize, test, intervene, validate, and finalize.
7. **causal_reason.detect_causal_drift**: Detect causal drift: confounder emergence, regime change, causal chain break, and effect decay.
8. **causal_reason.escalate_causal_gaps**: Escalate AMOS Causal Reasoning causal gaps: flag unconfirmed causality, require discriminating test, trigger analysis.
9. **causal_reason.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
10. **causal_reason.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
11. **causal_reason.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: `_00_Cosmo brain/misc/CA/causal.md` (content_hash: 6035054c7197da54), `_00_Cosmo brain/misc/CA/CAUSAL_FIREWALL.md` (content_hash: f71dae4c4d3e7ba6) (vault canon, SOURCE_CLAIM)

### Causal Evidence Hierarchy

| Level | Class | Evidence Required |
|-------|-------|-------------------|
| 0 | descriptive | observation only |
| 1 | association | co-occurrence |
| 2 | correlation | statistical correlation |
| 3 | enabling condition | enabling factor identified |
| 4 | mediator/confounder | mediation or confounding analysis |
| 5 | mechanism | mechanistic understanding |
| 6 | intervention effect | controlled intervention |

### Causal Firewall Rules

1. A stronger causal class requires stronger evidence.
2. Sequence, co-occurrence, analogy, structural resemblance, and predictive success do not by themselves establish mechanism or intervention effect.
3. For causal counterfactuals: identify intervention variable, hold background conditions explicit, separate observed from hypothetical states, mark unidentifiable counterfactuals UNKNOWN.

### Causal Relation Types

- `association` — co-occurrence without direction
- `correlation` — statistical correlation without causation
- `enabling_condition` — necessary but not sufficient
- `mediator` — intermediate variable in causal chain
- `confounder` — common cause of both variables
- `feedback` — bidirectional causal loop
- `necessary_condition` — must be present for effect
- `sufficient_condition` — alone can produce effect
- `mechanism` — explains how cause produces effect
- `intervention_effect` — confirmed by controlled intervention

### 4 Causal Modes

- **Direct**: A → B (immediate, single-step)
- **Distributed**: A → {B1, B2, ...} (fan-out, parallel)
- **Delayed**: A →[Δt]→ B (time-lagged)
- **Cascading**: A → B → C → ... (chain reactio
- AGENT_TEMPLATE

---
**MOC:** [[amos-causal-reasoning-master_MOC]]

## Examples

- **Scenario**: When determining whether a relationship is causal vs correlational vs associational
  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When performing counterfactual reasoning or intervention analysis
  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When classifying causal modes: Direct, Distributed, Delayed, Cascading
  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the causal domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `none` — routes to this skill when causal specialization is needed
- **Peers**: Other skills in the `causal` domain may be composed in sequence
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


## Do not use

- For generic causal analysis outside the AMOS causal framework
- To claim empirical validation of causal closure or hierarchy theories
- As a substitute for domain-specific causal or counterfactual evidence
- Outside causal reasoning domain reasoning

## References

- `references/counterfactual_reasoning_kernel.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/sensitivity_falsifiers.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `none` — parent skill
- `` — corresponding workflow
- `amos-causal-reasoning-master-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-causal-reasoning-master
node_type: skill
path: 07_SKILLS/amos-causal-reasoning-master/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
