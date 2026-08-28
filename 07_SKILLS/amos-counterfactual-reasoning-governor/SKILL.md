---
title: SKILL — Amos Counterfactual Reasoning Governor
type: skill
source: 07_SKILLS/amos-counterfactual-reasoning-governor
name: amos-counterfactual-reasoning-governor
description: Counterfactual Reasoning Governor — causal reasoning capability. Use when causal analysis, counterfactual reasoning, or intervention design. Use when amos-causal-reasoning-master routes to this specialized capability. Do not use for generic tasks outside causal domain.
parent_skill: amos-causal-reasoning-master
domain: causal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/causal-reasoning
- rscf/source_claim
- hml/h
- epistemic/source_claim
- amos_os
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
---

# Counterfactual Reasoning Governor

## Identity

Origin architect: **Trang Phan**. Domain: causal. Parent: amos-causal-reasoning-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
## When to Use

- When validating causal abstraction across model levels
- When enforcing causal closure: every effect has a sufficient cause
- When governing causal hierarchy: direct, distributed, delayed, cascading
- When reasoning counterfactually about alternative interventions
- When the parent skill (`amos-causal-reasoning-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **counterfactual_reasoning.validate_abstraction**: Validate causal abstraction: does the higher-level model preserve causal structure?
- **counterfactual_reasoning.enforce_closure**: Enforce causal closure: every effect must have a sufficient cause within the system
- **counterfactual_reasoning.govern_hierarchy**: Govern causal hierarchy: direct, distributed, delayed, and cascading causes
- **counterfactual_reasoning.reason_counterfactual**: Reason counterfactually: what would happen under alternative interventions

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: ef41fd5a1688a1f8) for the full vault-sourced domain knowledge (9239 chars).
- **counterfactual_reasoning.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **counterfactual_reasoning.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **counterfactual_reasoning.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/kernel/A/AMOS_Counterfactual_Reasoning_Kernel_v0_Meta_Cognition4_2.md` (content_hash: 8809484d7b9a31de) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Counterfactual Reasoning

From Cosmo Brain Counterfactual Reasoning Kernel v0: What-if analysis, alternative scenario reasoning, and causal inference through comparison of actual vs hypothetical states.

**4 Counterfactual types**:
- **Past counterfactual**: What would have happened if something in the past had been different? (e.g., "If we had launched earlier...")
- **Future counterfactual**: What would happen if something changes in the future? (e.g., "If we increase price by 10%...")
- **Structural counterfactual**: What does the structure imply would happen under different conditions? (e.g., "Given this system design, if load doubles...")
- **Causal counterfactual**: What can we infer about causation by comparing what happened with what would have happened without the cause?

**5 Valid counterfactual criteria**:
1. **Plausible initial state**: the counterfactual starting point must be plausible or clearly flagged as implausible
2. **Minimal change principle**: change only what's necessary; don't silently change other things
3. **Causal chain conservation**: respect the causal structure (A->B->C, changing A propagates through B to C)
4. **Uncertainty proportionate**: the further from actuality, the larger the uncertainty
5. **Assumption transparency**: all assumptions about how the world would differ must be explicit

**4 Rules**:
1. `counterfactual_needs_causal_model`: valid counterfactual reasoning requires a causal model; without it, you're guessing
2. `uncertainty_grows_with_distance`: the more different the counterfactual world is from actuality, the larger the uncertainty
3. `minimal_intervention`: change only what's specified; don't silently assume other things stay the same
4. `counterfactual_is_not_prediction`: a counterfactual is a reasoned exploration of alternatives, not a prediction

**5 Safety constraints**:
- Never present counterfactual as fact
- Never ignore uncertainty in far counterfactuals
- Always state assumptions explicitly
- Always label counterfactual as counterfactual
- Never use counterfactual to over-determine outcomes

**3 Functions**: `construct_counterfactual`, `compare_actual_vs_counterfactual`, `scenario_analysis`

### Epistemic Boundary

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-counterfactual-reasoning-governor_MOC]]

## Examples

- **Scenario**: When validating causal abstraction across model levels
  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When enforcing causal closure: every effect has a sufficient cause
  - **Input**: A query matching this skill's domain (causal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When governing causal hierarchy: direct, distributed, delayed, cascading
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

- **Parent**: `amos-causal-reasoning-master` — routes to this skill when causal specialization is needed
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

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-counterfactual-reasoning-governor_MOC]]` — skill Map of Content
- `amos-causal-reasoning-master` — parent skill
- `[[amos-counterfactual-reasoning-governor-workflow]]` — corresponding workflow
- `amos-counterfactual-reasoning-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-counterfactual-reasoning-governor
node_type: skill
path: 07_SKILLS/amos-counterfactual-reasoning-governor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
