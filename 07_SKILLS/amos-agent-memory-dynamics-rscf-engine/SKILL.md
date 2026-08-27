---
title: SKILL
type: skill
name: amos-agent-memory-dynamics-rscf-engine
description: Agent Memory Dynamics — memory systems capability. Use when memory management, context continuity, or memory conflict resolution. Use when amos-memory-systems-master routes to this specialized capability.
parent_skill: amos-memory-systems-master
domain: memory
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-agent-memory-dynamics-rscf-engine]
---


# Agent Memory Dynamics Rscf Engine

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-memory-systems-master`
- **Domain**: memory
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Memory system engine for Agent Memory Dynamics Rscf Engine

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
**Links:** [[07_SKILLS_MOC]]
