---
title: SKILL — Amos Knowledge Research Master
type: skill
source: 07_SKILLS/amos-knowledge-research-master
name: amos-knowledge-research-master
description: AMOS Knowledge & Research — Obsidian vault integration, arxiv research,
  knowledge indexing, curation, RAG best practices. 68,979-note vault as reasoning
  brain. Use for knowledge management, researc...
parent_skill: none
domain: knowledge
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- canon/skill
- domain/knowledge-research
- canon-group/tech-ai
- topic/knowledge-management
- capability/knowledge
- capability/research
- capability/ast
- rscf/epistemic
- rscf/D-distinction
- rscf/M-memory
- rscf/G-relation
- rscf/K-compression
- rscf/type-system
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-knowledge-research-master
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---




# 11_KNOWLEDGE MOC

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 143 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 143 separate shallow skills. **Epistemic class**: SOURCE_CLAIM (vault-sourced from `11_KNOWLEDGE/11_KNOWLEDGE_MOC.md` (content_hash: 665f1b63068333a0)).

## When to Use

AMOS Knowledge & Research — Obsidian vault integration, arxiv research, knowledge indexing, curation, RAG best practices. 68,979-note vault as reasoning brain. Use for knowledge management, researc...

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **knowle_research.integrate_vault**: Integrate AMOS Knowledge & Research vault knowledge: read, parse, index Markdown files with provenance and epistemic class.
- **knowle_research.validate_knowledge**: Validate AMOS Knowledge & Research knowledge entries for provenance, epistemic class, freshness, and dependency chain.
- **knowle_research.analyze_knowledge**: Analyze AMOS Knowledge & Research knowledge graph: MOC structure, orphan notes, wikilink health, and knowledge frontier.
- **knowle_research.trace_knowledge_provenance**: Trace AMOS Knowledge & Research knowledge to vault source paths, arxiv papers, and derivation chain.
- **knowle_research.assess_knowledge_claim**: Assess AMOS Knowledge & Research knowledge claims for source quality, citation completeness, and scope validity.
- **knowle_research.manage_knowledge_lifecycle**: Manage AMOS Knowledge & Research knowledge lifecycle: ingest, index, curate, validate, update, and archive.
- **knowle_research.detect_knowledge_drift**: Detect knowledge drift: stale entries, broken wikilinks, orphan notes, and provenance decay.
- **knowle_research.escalate_knowledge_gaps**: Escalate AMOS Knowledge & Research knowledge gaps: flag missing sources, broken links, trigger vault repair.
- **knowle_research.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **knowle_research.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **knowle_research.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Consolidated Sub-Skills (143)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

*...and 123 more sub-skills.*

## Vault-Sourced Domain Knowledge

> **Source**: `11_KNOWLEDGE/11_KNOWLEDGE_MOC.md` (content_hash: 665f1b63068333a0) from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

# 11_KNOWLEDGE MOC

> Index of 40 top-level knowledge notes.

## C1
- [[AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE]] — AMOS C01 META LOGIC MASTER KNOWLEDGE

## C10
- [[AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE]] — AMOS C10 TECH ENGINEERING MASTER KNOWLEDGE

## C11
- [[AMOS_C11_DESIGN_LANGUAGE_MASTER_KNOWLEDGE]] — AMOS C11 DESIGN LANGUAGE MASTER KNOWLEDGE

## C12
- [[AMOS_C12_EARTH_ECOLOGY_MASTER_KNOWLEDGE]] — AMOS C12 — Earth & Ecology Master Knowledge

## C2
- [[AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE]] — AMOS C02 MATH COMPUTE MASTER KNOWLEDGE

## C3
- [[AMOS_C03_PHYSICS_COSMOS_MASTER_KNOWLEDGE]] — AMOS C03 — Physics & Cosmos Master Knowledge

## C4
- [[AMOS_C04_BIO_NEURO_MASTER_KNOWLEDGE]] — AMOS C04 BIO NEURO MASTER KNOWLEDGE

## C5
- [[AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE]] — AMOS C05 MIND BEHAVIOR MASTER KNOWLEDGE

## C6
- [[AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE]] — AMOS C06 SOCIETY CULTURE MASTER KNOWLEDGE

## C7
- [[AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE]] — AMOS C07 ECON FINANCE MASTER KNOWLEDGE

## C8
- [[AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE]] — AMOS C08 STRATEGY GAME MASTER KNOWLEDGE

## C9
- [[AMOS_C09_ORG_LAW_POLICY_MASTER_KNOWLEDGE]] — AMOS C09 ORG LAW POLICY MASTER KNOWLEDGE

## agent
- [[AGENT_ONBOARDING_GUIDE]] — AMOS AGENT ONBOARDING GUIDE
- [[AGENT_SCHEMA]] — AMOS Agent Schema — Full Governed Specification
- [[AGENT_TEMPLATES]] — AMOS Agent Templates
- [[AMOS_CONTENT_AGENT_MATRIX_SYSTEM]] — AMOS Content Agent Matrix
- [[AMOS_INFRASTRUCTURE_FULL_BRAIN_AGENT_ARCHITECTURE_ROUND11]] — AMOS Infrastructure, Full Brain OS, Agents & Skills Architecture
- [[ENVIRONMENT_SCAN_AGENT]] — AMOS EnvironmentScan Agent
- EXECUTOR
- [[AGENT_TEMPLATE]]

---
**MOC:** [[amos-knowledge-research-master_MOC]]

## Examples

- **Scenario**: When managing lifecycle operations across classify, validate, trace, assess, and detect
  - **Input**: A query matching this skill's domain (knowledge)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When detecting drift in evidence chains, provenance freshness, or confidence calibration
  - **Input**: A query matching this skill's domain (knowledge)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When validating outputs against domain constraints and epistemic class
  - **Input**: A query matching this skill's domain (knowledge)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the knowledge domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `none` — routes to this skill when knowledge specialization is needed
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


## References

- `references/11k_cosmo_brain_bridge_index.md` — loaded on demand
- `references/11k_cosmo_brain_moc.md` — loaded on demand
- `references/auto_extracted_archive_index.md` — loaded on demand
- `references/brain_router_detailed.md` — loaded on demand
- `references/index_arxiv.md` — loaded on demand
- `references/index_daily.md` — loaded on demand
- `references/index_hash_prefixed.md` — loaded on demand
- `references/index_main.md` — loaded on demand
- `references/index_openclaw.md` — loaded on demand
- `references/index_root_misc.md` — loaded on demand
- `references/master_non_overlap_index.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/rscf_brain_router.md` — loaded on demand
- `references/science_engine_sector_packs.md` — loaded on demand
- `references/scientific_engine_layer.md` — loaded on demand
- `references/scientific_engine_vinfinity.md` — loaded on demand
- `[[amos-knowledge-research-master_MOC]]` — skill Map of Content
- `none` — parent skill
- `[[amos-knowledge-research-master-workflow]]` — corresponding workflow
- `amos-knowledge-research-master-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-knowledge-research-master
node_type: skill
path: 07_SKILLS/amos-knowledge-research-master/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
