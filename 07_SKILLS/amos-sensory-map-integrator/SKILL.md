---
schema_version: 1.0
title: SKILL — Amos Sensory Map Integrator
type: skill
source: 07_SKILLS/amos-sensory-map-integrator
name: amos-sensory-map-integrator
description: Sensory Map Integrator — biology and neuroscience capability. Use when biological reasoning, neuroscience, or medical analysis. Use when amos-c04-bio-neuro-master routes to this specialized capability. Do not use for generic tasks outside c04 domain.
parent_skill: amos-c04-bio-neuro-master
domain: c04
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
  - type/skill
  - type/skill
  - domain/bio-neuro
  - epistemic/source_claim
  - hml/m
  - epistemic/source_claim
  - amos-os
  - law-hierarchy
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

# Sensory Map Integrator

## Identity

Origin architect: **Trang Phan**. Domain: c04. Parent: amos-c04-bio-neuro-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- When mapping neurotransmitter systems: synthesis, release, reuptake, receptor activation
- When integrating sensory maps across biological cognition layers
- When modeling 7-layer biological scaffolding from molecular to social cognition
- When assessing cross-species cognition and comparative intelligence
- When the parent skill (`amos-c04-bio-neuro-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **sensory_map.map_mechanism**: Map biological mechanisms: cellular, neural, developmental, and evolutionary
- **sensory_map.assess_cognition**: Assess cross-species cognition: comparative neural computation and intelligence
- **sensory_map.model_morphogenesis**: Model morphogenesis: pattern formation, self-organization, and development
- **sensory_map.map_neurotransmitters**: Map neurotransmitter systems: synthesis sites, release sites, receptor subtypes
- **sensory_map.integrate_layers**: Integrate biological cognition layers: molecular → neural → cognitive → social
- **sensory_map.detect_drift**: Detect drift in neurotransmitter maps, cognition models, or evidence freshness
- **sensory_map.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **sensory_map.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **sensory_map.map_mechanism**: Map biological mechanisms: cellular, neural, developmental, and evolutionary
1. **sensory_map.assess_cognition**: Assess cross-species cognition: comparative neural computation and intelligence
1. **sensory_map.model_morphogenesis**: Model morphogenesis: pattern formation, self-organization, and development
1. **sensory_map.map_neurotransmitters**: Map neurotransmitter systems: synthesis sites, release sites, receptor subtypes
1. **sensory_map.integrate_layers**: Integrate biological cognition layers: molecular → neural → cognitive → social
1. **sensory_map.detect_drift**: Detect drift in neurotransmitter maps, cognition models, or evidence freshness
1. **sensory_map.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **sensory_map.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: `_00_Cosmo brain/system/Neurotransmitter Map — Complete Human System.md` (content_hash: 65ce68025b96d942), `_00_Cosmo brain/biology-ubi/Biology_Cognition_Model.md` (content_hash: ba8c82870d94b577) (vault canon, SOURCE_CLAIM)

### Neurotransmitter System Map

11 neurotransmitters with complete mapping (synthesis → release → reuptake → receptor activation):

- **Dopamine**: mesolimbic, mesocortical, nigrostriatal pathways
- **Serotonin**: mood, sleep, appetite regulation
- **Norepinephrine**: attention, arousal, stress response
- **GABA**: inhibitory balance
- **Glutamate**: excitatory signaling, learning
- **Acetylcholine**: memory, muscle activation
- **Histamine**: wakefulness, inflammatory response
- **Oxytocin**: social bonding, trust
- **Vasopressin**: social behavior, water balance
- **Cortisol**: stress response (GR/MR receptors)
- **Melatonin**: circadian regulation (MT1/MT2 receptors)

**Receptor types**: ionotropic (fast, ligand-gated) vs metabotropic (slow, G-protein coupled)

### 7-Layer Biological Cognition Model

| Layer | Name      | Focus                                        |
| ----- | --------- | -------------------------------------------- |
| L1    | Molecular | DNA/RNA, neurotransmitters, receptor binding |
| L2    | Cellular  | Neurons, glia, signal transduction           |
| L3    | Circuit   | Rate coding, oscillations, synchrony         |
| L4    | System    | Perception, attention, learning, memory      |
| L5    | Emotion   | Motivation, affect, behavioral drives        |
| L6    | Social    | Social cognition, theory of mind, interfaces |
| L7    | Interface | External coupling, environment, culture      |

### Epistemic Boundary

Neurotransmitter mapping is SOURCE_CLAIM (vault-sourced structural model). Biological cognition layers are AMOS_MODEL. Neither constitutes medical advice or neuroscience proof. Always recommend professional medical review for clinical questions.

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
- -

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-sensory-map-integrator/amos-sensory-map-integrator_MOC|amos-sensory-map-integrator_MOC]]

## Examples

- **Scenario**: When mapping neurotransmitter systems: synthesis, release, reuptake, receptor activation

  - **Input**: A query matching this skill's domain (c04)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When integrating sensory maps across biological cognition layers

  - **Input**: A query matching this skill's domain (c04)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When modeling 7-layer biological scaffolding from molecular to social cognition

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
- \`\` — skill Map of Content
- `amos-c04-bio-neuro-master` — parent skill
- \`\` — corresponding workflow
- `amos-sensory-map-integrator-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-sensory-map-integrator
node_type: skill
path: 07_SKILLS/amos-sensory-map-integrator/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
