---
title: SKILL
type: skill
name: amos-knowledge-harvest-runtime
description: Knowledge Harvest Runtime — knowledge research capability. Use when knowledge management, research, or Obsidian vault integration. Use when amos-knowledge-research-master routes to this specialized capability.
parent_skill: amos-knowledge-research-master
domain: knowledge
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-knowledge-harvest-runtime]
---


# Knowledge Harvest Runtime

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-knowledge-research-master`
- **Domain**: knowledge
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Knowledge-research engine for Knowledge Harvest Runtime

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

- **knowledge_harvest.search_corpus**: Search the corpus directly: retrieve relevant passages with provenance
- **knowledge_harvest.manage_artifact**: Manage research artifacts: create, version, and link to vault sources
- **knowledge_harvest.trace_footprint**: Trace agent storage footprint and optimize knowledge retention
- **knowledge_harvest.validate_epistemology**: Validate knowledge epistemology: source quality, freshness, and scope
- **knowledge_harvest.index_knowledge**: Index knowledge for rapid retrieval and cross-reference navigation
- **knowledge_harvest.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **knowledge_harvest.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **knowledge_harvest.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: d13ba2328adc6f64) for the full vault-sourced domain knowledge (7366 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/K/KNOWLEDGE_HARVEST.md` (content_hash: ebf6cf9c8fcd5127) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Knowledge Harvest Runtime

From Cosmo Brain Knowledge Harvest: Ephemeral Code -> Persistent Evidence -> Validated Knowledge. Reject: Ephemeral Code -> LLM Summary -> Delete Evidence.

**Principle**: `Ephemeral Code -> Persistent Evidence -> Validated Knowledge`
**Rejected pattern**: `Ephemeral Code -> LLM Summary -> Delete Evidence`

**Structural equation**: `PermanentKnowledge = Claim + Scope + Evidence + Provenance + Constraint + FailureMode + Validity + Lineage`

**7-step pipeline**:
1. **Acquire/fingerprint**: acquire the knowledge and fingerprint it
2. **Deterministic structure extraction**: extract structure deterministically
3. **Small falsifiable semantic claims**: break into small falsifiable claims
4. **Provenance/evidence/regime/governance validation**: validate with full governance
5. **Structured storage**: store in structured form
6. **Retention-class-controlled cleanup**: cleanup with retention class control
7. **Compact retrieval compilation**: compile for compact retrieval

**Retrieval compiler**: `user_problem -> AMOS_structural_decomposition -> knowledge_registry_query -> candidate_RSCF_retrieval -> scope_filter -> evidence_filter -> freshness_filter -> governance_filter -> conflict_field_resolution -> compact_context_compile -> LLM_or_agent`

**Anti-pattern**: `vector_search -> dump_many_raw_repository_chunks -> LLM` (rejected -- no scope/evidence/freshness/governance filtering)

**Harvest laws**:
- `EPHEMERAL != PERMANENT`: ephemeral code is not permanent knowledge; it must be harvested
- `SUMMARY != EVIDENCE**: LLM summary is not evidence; evidence must be independently validated
- `CLAIM != KNOWLEDGE**: a claim is not knowledge; knowledge requires claim + scope + evidence + provenance + constraint + failure mode + validity + lineage

### Epistemic Boundary

Knowledge harvest runtime is an operational construct. It does not prove all knowledge is harvested, that the pipeline is optimal, or that harvested knowledge is always correct.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding 