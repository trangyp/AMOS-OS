---
schema_version: 1.0
title: SKILL — Amos Closed Loop Learning Governor
type: skill
source: 07_SKILLS/amos-closed-loop-learning-governor
name: amos-closed-loop-learning-governor
description: Closed Loop Learning Governor — runtime and OS capability. Use when runtime reasoning, OS kernel operations, or adaptive stability. Use when amos-os-runtime-master routes to this specialized capability. Do not use for generic tasks outside runtime domain.
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
  - type/skill
  - type/skill
  - domain/os-runtime
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
  - L7_authority
  - L8_execution
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
  - L0
  - L1
  - L2
  - L4
  - L5
  - L7
  - L8
  - L16
  - L17
  - L18
license: MIT
steward: Trang Phan
---

# Closed Loop Learning Governor

## Identity

Origin architect: **Trang Phan**. Domain: runtime. Parent: amos-os-runtime-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- When monitoring runtime stability: drift, oscillation, divergence
- When calibrating feedback control loops for stable operation
- When decomposing complex operations into primitive steps
- When enforcing closed-loop learning and drift alignment
- When the parent skill (`amos-os-runtime-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **closed_loop.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
- **closed_loop.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
- **closed_loop.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
- **closed_loop.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
- **closed_loop.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 43d76b1897997c62) for the full vault-sourced domain knowledge (9437 chars).

- **closed_loop.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **closed_loop.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **closed_loop.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **closed_loop.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
1. **closed_loop.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
1. **closed_loop.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
1. **closed_loop.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
1. **closed_loop.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration
1. **closed_loop.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **closed_loop.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
1. **closed_loop.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE.md` (content_hash: e3ca4951a743518b) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Closed-Loop Learning Governor

From C05 Mind & Behavior: Closed-loop learning with feedback. From Cognitive Organism OS: Self-audit gate and repair cycle.

**Closed-loop learning model**:

- **Observe**: observe the outcome of an action
- **Evaluate**: evaluate the outcome against expectations
- **Learn**: learn from the discrepancy (if any)
- **Adjust**: adjust the model based on learning
- **Re-execute**: re-execute with the adjusted model
- **Audit**: audit the learning loop for correctness

**Closed-loop laws**:

- `LEARNING != IMPROVEMENT`: learning changes the model; improvement requires validation that the change is better
- \`FEEDBACK != TRUTH\*\*: feedback is an observation; it is not truth
- \`CLOSED_LOOP != CONVERGENCE\*\*: a closed loop ensures feedback; it does not guarantee convergence

**Governor responsibilities**:

- **Loop integrity**: ensure the learning loop is closed (no missing feedback)
- **Loop speed**: ensure the loop runs fast enough to be useful
- **Loop safety**: ensure the loop does not cause runaway adaptation
- **Loop audit**: ensure the loop is auditable (every iteration recorded)

**Self-audit gate**: every runtime cycle passes through self-audit before finalization. The self-audit checks that the learning loop is functioning correctly.

**Repair cycle**: if the learning loop is broken (missing feedback, runaway adaptation), the repair cycle activates to fix the loop.

### Epistemic Boundary

Closed-loop learning governance is an operational construct. It does not prove learning always converges, that the loop is always closed, or that adaptation is always beneficial.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions with

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-closed-loop-learning-governor/amos-closed-loop-learning-governor_MOC|amos-closed-loop-learning-governor_MOC]]

## Examples

- **Scenario**: When monitoring runtime stability: drift, oscillation, divergence

  - **Input**: A query matching this skill's domain (runtime)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When calibrating feedback control loops for stable operation

  - **Input**: A query matching this skill's domain (runtime)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When decomposing complex operations into primitive steps

  - **Input**: A query matching this skill's domain (runtime)
  - **Output**: Structured result with epistemic labels and provenance

## Anti-Patterns

- **Do not use** for tasks outside the runtime domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval

## Composition

- **Parent**: `amos-os-runtime-master` — routes to this skill when runtime specialization is needed
- **Peers**: Other skills in the `runtime` domain may be composed in sequence
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

- For generic runtime analysis outside the AMOS OS/runtime framework
- To claim empirical validation of OS or runtime theories
- As a substitute for domain-specific runtime or infrastructure evidence
- Outside runtime/OS domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- \`\` — skill Map of Content
- `amos-os-runtime-master` — parent skill
- \`\` — corresponding workflow
- `amos-closed-loop-learning-governor-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-closed-loop-learning-governor
node_type: skill
path: 07_SKILLS/amos-closed-loop-learning-governor/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
