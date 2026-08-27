---
title: SKILL
type: skill
name: amos-growth-graph
description: Growth Graph — society and culture capability. Use when social analysis, cultural reasoning, or anthropological study. Use when amos-c06-society-culture-master routes to this specialized capability.
parent_skill: amos-c06-society-culture-master
domain: c06
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-growth-graph]
---


# Growth Graph

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c06-society-culture-master`
- **Domain**: c06
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Society-culture engine for Growth Graph

## When to Use

- When modeling cognitive substrate memory graphs: field-level lineage, consolidation
- When analyzing memory operation graphs: vertices, edges, operations, queries
- When managing dependency-safe forgetting and reconsolidation
- When tracking growth patterns across knowledge and social networks
- When the parent skill (`amos-c06-society-culture-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **growth_graph.analyze_social**: Analyze emergent social intelligence: norms, networks, and cultural dynamics
- **growth_graph.model_memory_graph**: Model cognitive substrate memory graphs: field-level lineage and consolidation
- **growth_graph.manage_forgetting**: Manage dependency-safe forgetting and reconsolidation governance
- **growth_graph.track_growth**: Track growth patterns across knowledge and social networks
- **growth_graph.detect_drift**: Detect drift in memory graphs, lineage chains, or growth patterns
- **growth_graph.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **growth_graph.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: `_00_Cosmo brain/dated/2026-08-22/2026-08-22 Cognitive Substrate Memory Graph.md` (content_hash: 89323199f0a3b075), `_00_Cosmo brain/cognitive/AMOS_Cognitive_Substrate_v2_Implementation_Notes.md` (content_hash: 39237d966cc491cf) (vault canon, SOURCE_CLAIM)

### Memory Operation Graph Formalization

`M_t = (V_t, E_t, O_t, I_t, Q_t, L_t)`

- `V_t`: vertices (memory items at time t)
- `E_t`: edges (relationships between memories)
- `O_t`: operations (create, update, merge, delete)
- `I_t`: indices (retrieval structures)
- `Q_t`: queries (retrieval requests)
- `L_t`: lineage (provenance chains)

### Field-Level Lineage

Partial-memory validity is tracked at the field level, not just the record level. Each field has its own lineage chain, enabling:
- Partial validity: some fields can be valid while others are stale
- Targeted reconsolidation: only invalid fields need refreshing
- Contradiction retention: conflicting values preserved with provenance

### Epistemic-Class Preservation Rules (8)

1. Class preservation: memory class must be preserved through operations
2. Modality: modal claims (possible, necessary) preserved
3. Negation: negative facts preserved as explicitly negated
4. Quantifier: universal vs existential quantifiers preserved
5. Correlation ≠ cause: correlations never promoted to causation
6. Future ≠ present: future predictions never stored as present facts
7. Perspective: observer perspective preserved
8. Provenance: source chain preserved for every field

### Retrieval Failure Attribution (6 types)

1. Missing index — no retrieval path exists
2. Stale entry — entry exists but is outdated
3. Scope violation — entry exists but outside query scope
4. Contradiction — multiple conflicting entries
5. Provenance gap — entry exists but provenance is broken
6. Epistemic class mismatch — entry class doesn't match query class

### 4-Slice Cognitive Architecture

- **Reality Gate**: filters inputs against reality constraints
- **Reasoning Graph**: 11 typed reasoning operators
- **Memory Graph**: 9 memory/structural operators
- **Interface Coupling**: external system integration

### Epistemic Boundary

Memory graph formalization is AMOS_MODEL. The cognitive substrate is a structural model of memory operations, NOT a neuroscience claim or cognitive architecture proof.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evide

---
**Links:** [[07_SKILLS_MOC]]
