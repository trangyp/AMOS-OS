---
title: SKILL — Amos Cognitive Compression Kernel
type: skill
source: 07_SKILLS/amos-cognitive-compression-kernel
name: amos-cognitive-compression-kernel
description: Cognitive Compression Kernel — mind and behavior capability. Use when
  psychological analysis, behavioral reasoning, or cognitive modeling. Use when amos-c05-mind-behavior-master
  routes to this specialized capability.
parent_skill: amos-c05-mind-behavior-master
domain: c05
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/mind-behavior
- canon-group/human-system
- topic/cognition
- capability/kernel
- capability/cognition
- capability/reasoning
- capability/compression
- rscf/epistemic
- rscf/M-memory
- rscf/K-compression
- rscf/S-state
- rscf/G-relation
- rscf/type-model
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-cognitive-compression-kernel
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
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L16
- L17
---







# Cognitive Compression Kernel

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c05-mind-behavior-master`
- **Domain**: c05
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Mind-behavior engine for Cognitive Compression Kernel

## When to Use

- When modeling cognitive processes: attention, awareness, compression
- When allocating attention resources across competing demands
- When assessing awareness levels and meta-cognition
- When governing artistic and emotional expression within bounds
- When the parent skill (`amos-c05-mind-behavior-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **cognitive_compression.model_cognition**: Model cognitive processes: attention, awareness, compression, and inference
- **cognitive_compression.allocate_attention**: Allocate attention resources across competing demands and priorities
- **cognitive_compression.assess_awareness**: Assess awareness levels: meta-cognition, self-monitoring, and calibration
- **cognitive_compression.govern_expression**: Govern artistic and emotional expression within healthy bounds
- **cognitive_compression.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **cognitive_compression.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **cognitive_compression.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 71a6ed8244701a7a) for the full vault-sourced domain knowledge (8109 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/cognitive/AMOS_Cognitive_Compression_Kernel_v0_Meta_Cognition4_2.md` (content_hash: 67524e614c1bae0d) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Cognitive Compression Kernel

From Cosmo Brain Cognitive Compression Kernel v0: Reducing complexity while preserving essential structure, finding the minimum sufficient representation, and avoiding information loss in summarization.

**5 Compression levels**:
- **Raw**: full detail, maximum fidelity, maximum size
- **Detailed**: most detail retained, minor elaboration trimmed, high fidelity, moderate size
- **Structured**: key structure preserved, examples compressed, good fidelity, concise
- **Summary**: core claims and structure only, supporting detail omitted, moderate fidelity, brief
- **Essence**: single core insight, everything else dropped, low fidelity, minimal

**5 Compression principles**:
1. **Minimum sufficient representation**: compress to the smallest representation that preserves all decision-relevant information. Not smaller.
2. **Structure preservation**: preserve structural relationships (entities, relations, hierarchies, dependencies) even when examples are dropped.
3. **Loss audit**: every compression must document what was removed and why it was safe to remove. Loss must be explicit, not hidden.
4. **Context sensitive**: compression level depends on context (decision-making needs structured, quick reference needs summary, exploration needs detailed).
5. **Decompressability**: a good compression should allow reconstruction of the essential structure.

**4 Rules**:
1. `compress_to_need`: don't compress below what the task requires; don't expand above what the task requires
2. `loss_must_be_explicit`: never hide what was lost in compression; state what was dropped and why
3. `structure_over_fluff`: preserve entities, relations, claims, constraints; drop examples, analogies, rhetoric, repetition
4. `truth_preserved_through_compression`: compression must not change truth values, evidence levels, or burden levels

**3 Functions**: `compress_to_level`, `extract_essence`, `audit_compression_loss`

**5 Safety constraints**: never compress away decision-critical information, never hide compression loss, never change claim meaning, always provide loss audit, always match compression to context.

### Epistemic Boundary

Cognitive compression is an operational construct. It does not prove compression is lossless, that the minimum sufficient representation is always found,

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-cognitive-compression-kernel_MOC]]

## Examples

- **Scenario**: When modeling cognitive processes: attention, awareness, compression
  - **Input**: A query matching this skill's domain (c05)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When allocating attention resources across competing demands
  - **Input**: A query matching this skill's domain (c05)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When assessing awareness levels and meta-cognition
  - **Input**: A query matching this skill's domain (c05)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c05 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c05-mind-behavior-master` — routes to this skill when c05 specialization is needed
- **Peers**: Other skills in the `c05` domain may be composed in sequence
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
- `[[amos-cognitive-compression-kernel_MOC]]` — skill Map of Content
- `amos-c05-mind-behavior-master` — parent skill
- `[[amos-cognitive-compression-kernel-workflow]]` — corresponding workflow
- `amos-cognitive-compression-kernel-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-cognitive-compression-kernel
node_type: skill
path: 07_SKILLS/amos-cognitive-compression-kernel/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
