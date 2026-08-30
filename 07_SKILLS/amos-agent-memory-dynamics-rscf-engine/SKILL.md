---
schema_version: 1.0
title: SKILL — Amos Agent Memory Dynamics Rscf Engine
type: skill
source: 07_SKILLS/amos-agent-memory-dynamics-rscf-engine
name: amos-agent-memory-dynamics-rscf-engine
description: Agent Memory Dynamics — memory systems capability. Use when memory management,
  context continuity, or memory conflict resolution. Use when amos-memory-systems-master
  routes to this specialized capability. Do not use for generic tasks outside memory
  domain.
parent_skill: amos-memory-systems-master
domain: memory
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- type/skill
- domain/memory-systems
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

# Agent Memory Dynamics Rscf Engine

## Identity

Origin architect: **Trang Phan**. Domain: memory. Parent: amos-memory-systems-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When managing memory: storage, retrieval, decay, consolidation
- When resolving memory conflicts: contradictions, staleness, priority
- When enforcing memory firewall: preventing unauthorized access
- When tracking memory dynamics: formation, consolidation, forgetting
- When the parent skill (`amos-memory-systems-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **agent_memory.manage_memory**: Manage memory: storage, retrieval, decay, and consolidation
- **agent_memory.resolve_conflict**: Resolve memory conflicts: contradictions, staleness, and priority
- **agent_memory.enforce_firewall**: Enforce memory firewall: prevent unauthorized access and tampering
- **agent_memory.track_dynamics**: Track memory dynamics: formation, consolidation, and forgetting curves
- **agent_memory.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **agent_memory.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **agent_memory.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **agent_memory.manage_memory**: Manage memory: storage, retrieval, decay, and consolidation
2. **agent_memory.resolve_conflict**: Resolve memory conflicts: contradictions, staleness, and priority
3. **agent_memory.enforce_firewall**: Enforce memory firewall: prevent unauthorized access and tampering
4. **agent_memory.track_dynamics**: Track memory dynamics: formation, consolidation, and forgetting curves
5. **agent_memory.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
6. **agent_memory.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
7. **agent_memory.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Agent Memory Dynamics

From Cognitive Organism OS: Memory modules (Context, Immune, Manager, Orientation) and agent memory interactions.

**Agent memory model**:
- **Context budget**: ContextBudgetGovernor manages token/context budget for agents
- **Memory immune**: MemoryImmuneSystem detects and quarantines corrupted memory entries
- **Memory manager**: MemoryManager handles memory encoding, consolidation, retrieval
- **Orientation cache**: OrientationCache caches agent orientation for fast retrieval

**Memory dynamics**:
- **Encoding**: agent experiences are encoded into memory with provenance
- **Consolidation**: memory entries are consolidated across episodes
- **Retrieval**: relevant memory is retrieved for current context
- **Forgetting**: stale or irrelevant memory is pruned
- **Conflict**: memory conflicts are detected and resolved

**RSCF laws for agent memory**:
- `AGENT_MEMORY != CANONICAL_MEMORY`: agent memory is local; canonical memory requires admission
- `MEMORY != TRUTH`: memory entries are claims, not facts
- `CONSOLIDATION <= CORROBORATION`: consolidation requires corroboration

### Epistemic Boundary

Agent memory dynamics is an operational model. It does not prove memory completeness, that all conflicts are resolved, or that memory is always accurate.

## Defect found

Integrity sweep of all 607 agent JSONs found **26 invalid entries**:
- 25 used a divergent schema (`purpose` instead of `description`; `capabilities` as free-text string or list-of-dicts) from the vault_consolidation generator
- 1 had literal name `"0"` (amos-quantum-enhanced-tensor-field-agent) — collision-prone and unsearchable

## Repair

- 22 files: `description` derived from `purpose`/display_name+capabilities; written back valid
- 1 file renamed `0.json` → `amos-fractal-systems-master` (content preserved, name fixed)
- 4 files already had descriptions after purpose-merge
- Re-verified: **607/607 agents parse with name + description present** ## Lesson

Generators drift in schema even within one session's outputs. The registry-level invariant "every agent has name + description" should be a standing check in the brain-consistency audit.

---

---

### Source 2: AMOS Agent Orchestration Workflow

> Path: `amos-general/A/Agent/AMOS_Agent_Orchestration_Workflow.md` | Size: 35578 chars | Match score: 7 | content_hash: 22c44e5890a68473

# AMOS Agent Orchestration Workflow

Comprehensive workflow for orchestrating all 36 AMOS agents across 7 canonical systems. Covers agent selection, coordination patterns, execution loops, conflict resolution, output modes, and integration with existing brain workflows.

## Overview

AMOS has 36 agents organized into 7 canonical systems. This

---
**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-agent-memory-dynamics-rscf-engine/amos-agent-memory-dynamics-rscf-engine_MOC|amos-agent-memory-dynamics-rscf-engine_MOC]]

## Examples

- **Scenario**: When managing memory: storage, retrieval, decay, consolidation
  - **Input**: A query matching this skill's domain (memory)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When resolving memory conflicts: contradictions, staleness, priority
  - **Input**: A query matching this skill's domain (memory)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When enforcing memory firewall: preventing unauthorized access
  - **Input**: A query matching this skill's domain (memory)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the memory domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-memory-systems-master` — routes to this skill when memory specialization is needed
- **Peers**: Other skills in the `memory` domain may be composed in sequence
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

- For generic memory analysis outside the AMOS memory framework
- To claim empirical validation of memory consolidation theories
- As a substitute for domain-specific memory or context evidence
- Outside memory systems domain reasoning

## References

- `references/amos-agent-memory-dynamics-rscf-engine_code.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `` — skill Map of Content
- `amos-memory-systems-master` — parent skill
- `` — corresponding workflow
- `amos-agent-memory-dynamics-rscf-engine-agent` — corresponding agent
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-agent-memory-dynamics-rscf-engine
node_type: skill
path: 07_SKILLS/amos-agent-memory-dynamics-rscf-engine/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
