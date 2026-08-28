---
title: SKILL — Amos Tensor Network Contraction Sketch Rscf Engine
type: skill
source: 07_SKILLS/amos-tensor-network-contraction-sketch-rscf-engine
name: amos-tensor-network-contraction-sketch-rscf-engine
description: Tensor Network Contraction Sketch — formal verification capability. Use
  when formal verification, symbolic execution, proof checking, or mathematical reasoning.
  Use when amos-formal-engines-master routes to this specialized capability.
parent_skill: amos-formal-engines-master
domain: formal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/formal-engines
- canon-group/tech-ai
- topic/formal-verification
- capability/tensor
- capability/sketching
- capability/network
- rscf/epistemic
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-tensor-network-contraction-sketch-rscf-engine
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---



# Tensor Network Contraction Sketch Rscf Engine

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-formal-engines-master`
- **Domain**: formal
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Formal reasoning engine for Tensor Network Contraction Sketch Rscf Engine

## When to Use

- When verifying formal proofs against axioms and inference rules
- When checking soundness and completeness of formal systems
- When propagating constraints and detecting unsatisfiable cores
- When validating invariants under all operating conditions
- When the parent skill (`amos-formal-engines-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **tensor_network.verify_proof**: Verify formal proofs against axioms, inference rules, and consistency constraints
- **tensor_network.check_soundness**: Check soundness and completeness of formal systems under test
- **tensor_network.propagate_constraints**: Propagate constraints through the formal system and detect unsatisfiable cores
- **tensor_network.validate_invariant**: Validate invariants hold under all specified operating conditions
- **tensor_network.detect_contradiction**: Detect contradictions and derive minimal conflict explanations
- **tensor_network.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **tensor_network.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **tensor_network.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 75bbbc19b4efd122) for the full vault-sourced domain knowledge (7541 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### RSCF Epistemic Substrate

This RSCF engine operates on the AMOS RSCF (Reasoning, Scope, Claim, Falsifier) epistemic substrate.

**RSCF objects**: claim / class / premises / evidence / provenance / scope / regime / freshness / dependencies / competing hypotheses / falsifiers / confidence ceiling.

**RSCF state kinds**: OBSERVATION, SOURCE_CLAIM, DERIVED, MODEL, DECISION, UNKNOWN.

**RSCF laws**:
- `CLAIM != FACT`: a claim is not a fact; it must be labeled with epistemic class
- `CONFIDENCE <= EVIDENCE`: confidence cannot exceed evidence support
- `FALSIFIER_REQUIRED`: every claim must declare its falsifier
- `SCOPE_BOUND`: every claim is valid only within its declared scope and regime
- `PROVENANCE_REQUIRED`: every claim must have traceable provenance

**RSCF validation gates**:
- G1 (Law of Law): no unresolved contradictions
- G2 (Epistemic class): all claims labeled, no class promotion without evidence
- G3 (Provenance): source path recorded for every derived claim
- G4 (Anti-overreach): no claim beyond declared scope
- G5 (Equation firewall): equations carry status tags
- G6 (Failure mode): on failure, downgrade, flag, escalate

### Epistemic Boundary

This RSCF engine is an epistemic governance tool. It does not prove claims are true, that all falsifiers are known, or that the RSCF framework is complete.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for every derived claim.
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and epistemic class.
- **G5 (Equation firewal

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-tensor-network-contraction-sketch-rscf-engine_MOC]]

## Examples

- **Scenario**: When verifying formal proofs against axioms and inference rules
  - **Input**: A query matching this skill's domain (formal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When checking soundness and completeness of formal systems
  - **Input**: A query matching this skill's domain (formal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When propagating constraints and detecting unsatisfiable cores
  - **Input**: A query matching this skill's domain (formal)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the formal domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-formal-engines-master` — routes to this skill when formal specialization is needed
- **Peers**: Other skills in the `formal` domain may be composed in sequence
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
- `[[amos-tensor-network-contraction-sketch-rscf-engine_MOC]]` — skill Map of Content
- `amos-formal-engines-master` — parent skill
- `[[amos-tensor-network-contraction-sketch-rscf-engine-workflow]]` — corresponding workflow
- `amos-tensor-network-contraction-sketch-rscf-engine-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-tensor-network-contraction-sketch-rscf-engine
node_type: skill
path: 07_SKILLS/amos-tensor-network-contraction-sketch-rscf-engine/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
