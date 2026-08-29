---
schema_version: 1.0
title: SKILL — Amos Agent Storage Footprint Rscf
type: skill
source: 07_SKILLS/amos-agent-storage-footprint-rscf
name: amos-agent-storage-footprint-rscf
description: Agent Storage Footprint — knowledge research capability. Use when knowledge
  management, research, or Obsidian vault integration. Use when amos-knowledge-research-master
  routes to this specialized capability. Do not use for generic tasks outside knowledge
  domain.
parent_skill: amos-knowledge-research-master
domain: knowledge
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- type/skill
- domain/knowledge-research
- epistemic/source_claim
- hml/m
- epistemic/source_claim
- amos-os
- 07-skills-moc
- amos-agent-storage-footprint-rscf-moc
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
license: MIT
steward: Trang Phan
---

# Agent Storage Footprint Rscf

## Identity

Origin architect: **Trang Phan**. Domain: knowledge. Parent: amos-knowledge-research-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When searching the corpus for relevant passages with provenance
- When managing research artifacts and linking to vault sources
- When tracing agent storage footprint and optimizing retention
- When validating knowledge epistemology and source quality
- When the parent skill (`amos-knowledge-research-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **agent_storage.search_corpus**: Search the corpus directly: retrieve relevant passages with provenance
- **agent_storage.manage_artifact**: Manage research artifacts: create, version, and link to vault sources
- **agent_storage.trace_footprint**: Trace agent storage footprint and optimize knowledge retention
- **agent_storage.validate_epistemology**: Validate knowledge epistemology: source quality, freshness, and scope
- **agent_storage.index_knowledge**: Index knowledge for rapid retrieval and cross-reference navigation
- **agent_storage.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **agent_storage.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **agent_storage.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **agent_storage.search_corpus**: Search the corpus directly: retrieve relevant passages with provenance
2. **agent_storage.manage_artifact**: Manage research artifacts: create, version, and link to vault sources
3. **agent_storage.trace_footprint**: Trace agent storage footprint and optimize knowledge retention
4. **agent_storage.validate_epistemology**: Validate knowledge epistemology: source quality, freshness, and scope
5. **agent_storage.index_knowledge**: Index knowledge for rapid retrieval and cross-reference navigation
6. **agent_storage.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
7. **agent_storage.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
8. **agent_storage.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE.md` (content_hash: f23d35766fe766bc) (vault canon, SOURCE_CLAIM)

### Agent Storage Footprint RSCF

From Cognitive Organism OS: Agent storage with RSCF provenance. From C10 Tech & Engineering: Storage footprint optimization for agent systems.

**Agent storage footprint model**:
- **Agent state storage**: each agent has a state that must be stored
- **Agent history storage**: each agent has a history that must be stored
- **Agent capability storage**: each agent has capabilities that must be stored
- **Agent provenance storage**: each agent has provenance that must be stored

**RSCF for storage**:
- **Claim**: the storage claim (what is stored, why, for how long)
- **Scope**: the storage scope (what agents, what time range)
- **Regime**: the storage regime (hot, warm, cold, archive)
- **Freshness**: the storage freshness (how current is the stored data)
- **Falsifier**: what would falsify the storage claim

**Storage footprint optimization**:
- **Minimal sufficient storage**: store only what is needed for decision-making
- **Retention-class-controlled cleanup**: cleanup with retention class control
- **Compression**: compress stored data while preserving structure
- **Provenance-preserving eviction**: evict data while preserving provenance

**Footprint laws**:
- `STORED != NEEDED`: stored data may not be needed; needed data may not be stored
- `FOOTPRINT != COST**: footprint is the storage size; cost includes access and maintenance
- `RETENTION != HOARDING**: retention keeps what's needed; hoarding keeps everything

### Epistemic Boundary

Agent storage footprint RSCF is an operational construct. It does not prove all storage is optimized, that the footprint is always minimal, or that retention is always correct.

## Defect found

Integrity sweep of all 607 agent JSONs found **26 invalid entries**:
- 25 used a divergent schema (`purpose` instead of `description`; `capabilities` as free-text string or list-of-dicts) from the vault_consolidation generator
- 1 had literal name `"0"` (amos-quantum-enhanced-tensor-field-agent) — collision-prone and unsearchable

## Repair

- 22 files: `description` derived from `purpose`/display_name+capabilities; written back valid
- 1 file renamed `0.json` → `amos-fractal-systems-master` (content preserved, name fixed)
- 4 files already had descriptions after purpose-merge
- Re-verified: **607/607 agents parse with name + description present** ## Lesson

Generators drift in schema even within one session's outputs. The registry-level invarian

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-agent-storage-footprint-rscf_MOC]]

## Examples

- **Scenario**: When searching the corpus for relevant passages with provenance
  - **Input**: A query matching this skill's domain (knowledge)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When managing research artifacts and linking to vault sources
  - **Input**: A query matching this skill's domain (knowledge)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When tracing agent storage footprint and optimizing retention
  - **Input**: A query matching this skill's domain (knowledge)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the knowledge domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-knowledge-research-master` — routes to this skill when knowledge specialization is needed
- **Peers**: Other skills in the `knowledge` domain may be composed in sequence
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

- For generic knowledge management outside the AMOS knowledge framework
- To claim empirical validation of knowledge representation theories
- As a substitute for domain-specific research or curatorial evidence
- Outside knowledge research domain reasoning

## References

- `references/amos-agent-storage-footprint-rscf_code.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `` — skill Map of Content
- `amos-knowledge-research-master` — parent skill
- `` — corresponding workflow
- `amos-agent-storage-footprint-rscf-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-agent-storage-footprint-rscf
node_type: skill
path: 07_SKILLS/amos-agent-storage-footprint-rscf/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
