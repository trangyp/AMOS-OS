---
title: SKILL — Amos Memory Conflict Governor
type: skill
source: 07_SKILLS/amos-memory-conflict-governor
name: amos-memory-conflict-governor
description: Memory Conflict Governor — memory systems capability. Use when memory
  management, context continuity, or memory conflict resolution. Use when amos-memory-systems-master
  routes to this specialized capability.
parent_skill: amos-memory-systems-master
domain: memory
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/memory-systems
- canon-group/tech-ai
- topic/memory
- capability/memory
- capability/governance
- capability/conflict-resolution
- capability/context_management
- rscf/epistemic
- rscf/C-constraint
- rscf/G-relation
- rscf/M-memory
- rscf/B-boundary
- rscf/type-system
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-memory-conflict-governor
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







# Memory Conflict Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-memory-systems-master`
- **Domain**: memory
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Memory system engine for Memory Conflict Governor

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

- **memory_conflict.manage_memory**: Manage memory: storage, retrieval, decay, and consolidation
- **memory_conflict.resolve_conflict**: Resolve memory conflicts: contradictions, staleness, and priority
- **memory_conflict.enforce_firewall**: Enforce memory firewall: prevent unauthorized access and tampering
- **memory_conflict.track_dynamics**: Track memory dynamics: formation, consolidation, and forgetting curves

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: ee7032a20ba6061a) for the full vault-sourced domain knowledge (9474 chars).
- **memory_conflict.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **memory_conflict.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **memory_conflict.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/O/overlooked.md` (content_hash: eb91d778a79b4c6a) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/memory/learning_memory_architecture.md` (content_hash: 5eaeecaa5e8cfd3d) (vault canon, SOURCE_CLAIM)

### Memory Conflict Governor

From Cosmo Brain Overlooked: Memory conflict in 3 regimes with Conflict Regime Classifier. From Learning Memory Architecture: Interference score, proactive/retroactive interference, memory entropy.

**3 Memory conflict regimes** (SOURCE_CLAIM):
1. **Dynamic conflict**: later true update supersedes earlier state (legitimate update)
2. **Static conflict**: false contradiction should not overwrite stable fact (protection)
3. **Conditional conflict**: multiple memories valid under different conditions (context split)

**5 Conflict types** (for Conflict Regime Classifier):
- **Update**: legitimate update (dynamic conflict)
- **Poison**: adversarial injection (should be blocked)
- **Context split**: different contexts, both valid (conditional conflict)
- **Ontology fork**: different ontologies, both valid (conditional conflict)
- **Unresolved ambiguity**: cannot classify (requires human escalation)

**Memory interference equations** (SOURCE_DERIVED):
```
IS = similar_memory_conflict / total_related_memory    (interference score)
PI = old_memory_blocks_new_learning                     (proactive interference)
RI = new_memory_blocks_old_recall                       (retroactive interference)
ME = w1*interference + w2*schema_conflict + w3*retrieval_error + w4*attention_leak + w5*context_gap  (memory entropy)
```

**Governor protocol**:
1. **Detect**: detect the memory conflict
2. **Classify**: classify the conflict regime (dynamic, static, conditional)
3. **Classify type**: classify the conflict type (update, poison, context split, ontology fork, unresolved)
4. **Resolve**: resolve based on regime and type
5. **Record**: record with provenance

**Governor laws**:
- `CONFLICT != CONTRADICTION`: conflict is a memory state; contradiction is a logical state
- `UPDATE != OVERWRITE**: update supersedes with reason; overwrite replaces without reason
- `RESOLUTION != DELETION**: resolution resolves the conflict; it does not delete the memory

### Epistemic Boundary

Memory conflict governance is an operational construct. It does not prove all conflicts are detected, that the classification is always correct, or that resolution is always optimal.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skil

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-memory-conflict-governor_MOC]]

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


## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-memory-conflict-governor_MOC]]` — skill Map of Content
- `amos-memory-systems-master` — parent skill
- `[[amos-memory-conflict-governor-workflow]]` — corresponding workflow
- `amos-memory-conflict-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-memory-conflict-governor
node_type: skill
path: 07_SKILLS/amos-memory-conflict-governor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
