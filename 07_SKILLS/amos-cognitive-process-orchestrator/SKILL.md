---
schema_version: 1.0
title: SKILL — Amos Cognitive Process Orchestrator
type: skill
source: 07_SKILLS/amos-cognitive-process-orchestrator
name: amos-cognitive-process-orchestrator
description: Cognitive Process Orchestrator — mind and behavior capability. Use when psychological analysis, behavioral reasoning, or cognitive modeling. Use when amos-c05-mind-behavior-master routes to this specialized capability. Do not use for generic tasks outside c05 domain.
parent_skill: amos-c05-mind-behavior-master
domain: c05
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/mind-behavior
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
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

# Cognitive Process Orchestrator

## Identity

Origin architect: **Trang Phan**. Domain: c05. Parent: amos-c05-mind-behavior-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
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

- **cognitive_process.model_cognition**: Model cognitive processes: attention, awareness, compression, and inference
- **cognitive_process.allocate_attention**: Allocate attention resources across competing demands and priorities
- **cognitive_process.assess_awareness**: Assess awareness levels: meta-cognition, self-monitoring, and calibration
- **cognitive_process.govern_expression**: Govern artistic and emotional expression within healthy bounds
- **cognitive_process.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **cognitive_process.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **cognitive_process.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 17b6beae69565d78) for the full vault-sourced domain knowledge (7950 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE.md` (content_hash: e3ca4951a743518b) (vault canon, SOURCE_CLAIM)

### Cognitive Process Orchestrator

From Cognitive Organism OS: 10-step runtime pipeline for cognitive process orchestration.

**10-step runtime pipeline**:
```
Perceive -> Route -> Admit -> Plan -> Schedule -> Execute -> Observe -> Repair -> Audit -> Finalize
```

**Orchestration principles**:
- Each step has declared inputs, outputs, and validation gates
- Steps are ordered; skipping steps requires explicit justification
- Repair can insert re-execution of earlier steps
- Audit checks all steps before finalization
- Finalization commits the result with provenance

**8 independent axes** for orchestration:
1. Cognitive organization
2. Capability granularity
3. Cognitive mode (EXPLORE/DIAGNOSE/DESIGN/AUDIT/MEASURE)
4. Scale (H/M/L)
5. Epistemic state (OBSERVATION/SOURCE_CLAIM/DERIVED/MODEL/DECISION/UNKNOWN)
6. Execution
7. Governance
8. Deployment

**5 Cognitive modes**:
- **EXPLORE**: discover and map the problem space
- **DIAGNOSE**: identify the root cause of a problem
- **DESIGN**: create a solution for a diagnosed problem
- **AUDIT**: verify that a solution meets its declared properties
- **MEASURE**: quantify the properties of a system or solution

**Orchestration laws**:
- `ORCHESTRATION != EXECUTION**: orchestration coordinates; execution does the work
- `STEP != CAPABILITY**: a step invokes a capability; it is not the capability
- `PIPELINE != WATERFALL**: the pipeline has feedback (repair -> re-execute); it is not a strict waterfall

### Epistemic Boundary

Cognitive process orchestration is a runtime architecture. It does not prove cognitive completeness, optimality, or that all cognitive processes can be decomposed into this pipeline.

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the ski

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-cognitive-process-orchestrator_MOC]]

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


## Do not use

- For generic psychological analysis outside the mind/behavior framework
- To claim empirical validation of consciousness or cognitive theories
- As a substitute for domain-specific psychological or psychiatric evidence
- Outside mind/behavior domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-cognitive-process-orchestrator_MOC]]` — skill Map of Content
- `amos-c05-mind-behavior-master` — parent skill
- `[[amos-cognitive-process-orchestrator-workflow]]` — corresponding workflow
- `amos-cognitive-process-orchestrator-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-cognitive-process-orchestrator
node_type: skill
path: 07_SKILLS/amos-cognitive-process-orchestrator/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
