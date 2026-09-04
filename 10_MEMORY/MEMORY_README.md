---
title: 10_MEMORY — Substrate Architecture & Representation
type: architecture_specification
source: 10_MEMORY
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC
  scope: memory_architecture
tags:
  - amos-os
  - memory
  - episodic
  - semantic
  - working-memory
  - procedural
---

# 10_MEMORY — 4-Tier Memory Substrate

## 1. Architectural Distinction

In AMOS OS, memory is the persisted substrate of past interactions, learned associations, and active contexts. It is governed by strict epistemic boundaries:

```text
MEMORY != KNOWLEDGE
MEMORY != STATE
RETENTION != TRUTH
RECALL != VALIDATION
```

## 2. Four-Tier Memory Architecture

```mermaid
graph TD
    A[AMOS Memory Substrate] --> B[Working Memory<br/>Transient / Scratchpad]
    A --> C[Episodic Memory<br/>Temporal Event Logs]
    A --> D[Semantic Memory<br/>Associative Concept Graph]
    A --> E[Procedural Memory<br/>Compiled Skills & Habits]

    B -->|Consolidation| C
    C -->|Abstraction & Clustering| D
    D -->|Skill Compilation| E
```

### 2.1 Working Memory (`WORKING_MEMORY_REGISTRY.md`)
- **Lifecycle**: Active conversation/task duration.
- **Capacity**: Bounded context window with dynamic scratchpads.
- **Pruning**: Immediate release upon task finalization or transition.

### 2.2 Episodic Memory (`EPISODIC_MEMORY_SUBSTRATE.md`)
- **Lifecycle**: Chronological, immutable append-only logs.
- **Contents**: Past user interactions, tool executions, agent decision trees, and error traces.
- **Indexing**: Timestamp, session ID, task ID, causal epoch.

### 2.3 Semantic Memory (`SEMANTIC_MEMORY_GRAPH.md`)
- **Lifecycle**: Durable, high-retention associative graph.
- **Contents**: Conceptual relationships, ontology vectors, cross-domain mappings.
- **Retrieval**: Hybrid vector embeddings + deterministic wikilink traversal.

### 2.4 Procedural Memory (`PROCEDURAL_MEMORY_CATALOG.md`)
- **Lifecycle**: Permanent, versioned executable patterns.
- **Contents**: Highly optimized skill compositions, standard runbook executions, automated recovery reflexes.

## 3. Retention & Pruning Invariants

1. **Decay with Evidence Invalidation**: If an underlying premise in `01_CANON` or `11_KNOWLEDGE` is invalidated, all dependent semantic memory nodes are flagged for re-evaluation.
2. **No Unchecked Self-Reinforcement**: Hallucinated patterns cannot be consolidated into semantic memory without explicit confirmation gates.
