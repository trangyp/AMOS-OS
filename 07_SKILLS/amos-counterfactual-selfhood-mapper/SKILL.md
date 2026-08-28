---
schema_version: 1.0
title: SKILL — Amos Counterfactual Selfhood Mapper
type: skill
source: 07_SKILLS/amos-counterfactual-selfhood-mapper
name: amos-counterfactual-selfhood-mapper
description: Counterfactual Selfhood Mapper — causal reasoning capability. Use when causal analysis, counterfactual reasoning, or intervention design. Use when amos-causal-reasoning-master routes to this specialized capability. Do not use for generic tasks outside causal domain.
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
license: MIT
steward: Trang Phan
---

# Counterfactual Selfhood Mapper

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

- **counterfactual_selfhood.validate_abstraction**: Validate causal abstraction: does the higher-level model preserve causal structure?
- **counterfactual_selfhood.enforce_closure**: Enforce causal closure: every effect must have a sufficient cause within the system
- **counterfactual_selfhood.govern_hierarchy**: Govern causal hierarchy: direct, distributed, delayed, and cascading causes
- **counterfactual_selfhood.reason_counterfactual**: Reason counterfactually: what would happen under alternative interventions

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: df869b1e6ab5a677) for the full vault-sourced domain knowledge (9620 chars).
- **counterfactual_selfhood.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **counterfactual_selfhood.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **counterfactual_selfhood.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Counterfactual Selfhood Mapping

The Cognitive Organism OS defines counterfactual selfhood as the exploration of "what would the self be like under different conditions."

**Counterfactual selfhood model**: `SelfModel(conditions) = f(Identity, Continuity, Boundary, Self-awareness)`

**Counterfactual dimensions**:
- **Identity counterfactual**: what if the system had different identity parameters?
- **Continuity counterfactual**: what if the system's continuity was interrupted?
- **Boundary counterfactual**: what if the system's boundaries were different?
- **Self-awareness counterfactual**: what if the system's self-awareness level changed?

**Mapping protocol**:
1. **Declare current self-model**: identity, continuity, boundary, self-awareness
2. **Construct counterfactual**: vary one dimension while holding others constant
3. **Map the counterfactual self**: what would the self-model look like?
4. **Compare**: how does the counterfactual self differ from the actual self?
5. **Classify**: STRUCTURAL (same structure, different parameters), FUNCTIONAL (different structure, same function), INCOMMENSURABLE (no comparison possible)

**Law**: `SELF_MODEL != SUBJECTIVE_SELF`. The counterfactual self is a model exploration, not a phenomenological claim.

### Epistemic Boundary

Counterfactual selfhood mapping is an analytical model. It does not prove the system has a self, that counterfactual selves are real, or that selfhood is mappable in all dimensions.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for every derived claim.
- **G4 (Anti-overreach)**: No claim be

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-counterfactual-selfhood-mapper_MOC]]

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
- `[[amos-counterfactual-selfhood-mapper_MOC]]` — skill Map of Content
- `amos-causal-reasoning-master` — parent skill
- `[[amos-counterfactual-selfhood-mapper-workflow]]` — corresponding workflow
- `amos-counterfactual-selfhood-mapper-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-counterfactual-selfhood-mapper
node_type: skill
path: 07_SKILLS/amos-counterfactual-selfhood-mapper/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
