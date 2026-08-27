---
title: SKILL
type: skill
name: amos-agent-storage-footprint-rscf
description: Agent Storage Footprint — knowledge research capability. Use when knowledge management, research, or Obsidian vault integration. Use when amos-knowledge-research-master routes to this specialized capability.
parent_skill: amos-knowledge-research-master
domain: knowledge
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-agent-storage-footprint-rscf]
---


# Agent Storage Footprint Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-knowledge-research-master`
- **Domain**: knowledge
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Knowledge-research engine for Agent Storage Footprint Rscf

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
