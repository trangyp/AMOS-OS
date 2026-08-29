---
schema_version: 1.0
title: SKILL — Amos Cell Intelligence Mapper
type: skill
source: 07_SKILLS/amos-cell-intelligence-mapper
name: amos-cell-intelligence-mapper
description: Cell Intelligence Mapper — biology and neuroscience capability. Use when
  biological reasoning, neuroscience, or medical analysis. Use when amos-c04-bio-neuro-master
  routes to this specialized capability. Do not use for generic tasks outside c04
  domain.
parent_skill: amos-c04-bio-neuro-master
domain: c04
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/bio-neuro
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
- 07-skills-moc
- amos-cell-intelligence-mapper-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
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
license: MIT
steward: Trang Phan
---

# Cell Intelligence Mapper

## Identity

Origin architect: **Trang Phan**. Domain: c04. Parent: amos-c04-bio-neuro-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When mapping biological mechanisms: cellular, neural, developmental, and evolutionary
- When assessing cross-species cognition and comparative intelligence
- When modeling morphogenesis: pattern formation, self-organization, and development
- When applying NBI (Neurobiological Intelligence) structural analysis to biological questions
- When the parent skill (`amos-c04-bio-neuro-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **cell_intelligence.map_mechanism**: Map biological mechanisms: cellular, neural, developmental, and evolutionary
- **cell_intelligence.assess_cognition**: Assess cross-species cognition: comparative neural computation and intelligence
- **cell_intelligence.model_morphogenesis**: Model morphogenesis: pattern formation, self-organization, and development
- **cell_intelligence.apply_nbi**: Apply NBI (Neurobiological Intelligence) structural analysis to biological questions
- **cell_intelligence.assess_claim**: Assess biological claims for epistemic class (AMOS_MODEL not medical advice)
- **cell_intelligence.detect_drift**: Detect drift in biological models, mechanism understanding, or evidence freshness
- **cell_intelligence.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **cell_intelligence.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **cell_intelligence.map_mechanism**: Map biological mechanisms: cellular, neural, developmental, and evolutionary
2. **cell_intelligence.assess_cognition**: Assess cross-species cognition: comparative neural computation and intelligence
3. **cell_intelligence.model_morphogenesis**: Model morphogenesis: pattern formation, self-organization, and development
4. **cell_intelligence.apply_nbi**: Apply NBI (Neurobiological Intelligence) structural analysis to biological questions
5. **cell_intelligence.assess_claim**: Assess biological claims for epistemic class (AMOS_MODEL not medical advice)
6. **cell_intelligence.detect_drift**: Detect drift in biological models, mechanism understanding, or evidence freshness
7. **cell_intelligence.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
8. **cell_intelligence.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: `_00_Cosmo brain/engine/A/AMOS_Nbi_Engine_v0_Ubi7.md` (content_hash: bc906ea26514f5b3), `_00_Cosmo brain/misc/C0/C04_bio_neuro.md` (content_hash: ca73264907f22a55) (vault canon, SOURCE_CLAIM)

### NBI (Neurobiological Intelligence) Engine

The NBI Engine is a structural, non-medical reasoning layer for biological analysis:

- **Domain**: Neurobiological Intelligence
- **Description**: Logical, mathematical, mechanistic and scientific processing layer
- **Integration**: Fully integrated with NEI, SI, BEI, TSS, TPE, and PSI in a non-medical, structural way

### Core Principles

- **Rule of 2**: Compare two complementary views: internal vs external, micro vs macro, short vs long term
- **Rule of 4**: Map problems across four quadrants: biological, cognitive, behavioural, systemic
- **Alignment**: Maintain internal logical consistency and respect user-defined constraints
- **Safety**: Do not generate instructions that cause harm or violate medical, legal, or ethical boundaries

### Safety Constraints

- `no_medical_diagnosis`: true — NBI is structural analysis, not medical diagnosis
- `no_therapy`: true — NBI does not prescribe therapy
- `no_personal_future_predictions`: true — NBI does not predict individual health outcomes
- `respect_user_boundaries`: true — NBI respects user-defined boundaries

### C04 Bio-Neuro Domain

- **Focus**: Biological structure, physiology, nervous systems, evolution, health logic
- **Core methods**: mechanism_mapping, evolutionary_considerations, risk_benefit_clinical_patterning, multi_system_interaction_mapping
- **Risk notes**: `not_a_substitute_for_medical_care`, `must_remain_cautious_with_novel_or_rare_conditions`

### Epistemic Boundary

NBI is AMOS_MODEL — structural reasoning about biological systems, NOT medical advice or diagnosis. Biological claims require DOMAIN_EMPIRICAL evidence from established medical/scientific sources. The NBI engine is a non-medical structural analysis tool.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-cell-intelligence-mapper_MOC]]

## Examples

- **Scenario**: When mapping biological mechanisms: cellular, neural, developmental, and evolutionary
  - **Input**: A query matching this skill's domain (c04)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When assessing cross-species cognition and comparative intelligence
  - **Input**: A query matching this skill's domain (c04)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When modeling morphogenesis: pattern formation, self-organization, and development
  - **Input**: A query matching this skill's domain (c04)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c04 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c04-bio-neuro-master` — routes to this skill when c04 specialization is needed
- **Peers**: Other skills in the `c04` domain may be composed in sequence
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

- For generic biological analysis outside the bio/neuro framework
- To claim empirical validation of biological intelligence laws
- As a substitute for domain-specific medical or neuroscience evidence
- Outside biology/neuroscience domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-c04-bio-neuro-master` — parent skill
- `` — corresponding workflow
- `amos-cell-intelligence-mapper-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-cell-intelligence-mapper
node_type: skill
path: 07_SKILLS/amos-cell-intelligence-mapper/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
