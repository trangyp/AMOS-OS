---
schema_version: 1.0
title: SKILL — Amos Time Series Conformal Uq Rscf Engine
type: skill
source: 07_SKILLS/amos-time-series-conformal-uq-rscf-engine
name: amos-time-series-conformal-uq-rscf-engine
description: Time Series Conformal Uq — formal verification capability. Use when formal verification, symbolic execution, proof checking, or mathematical reasoning. Use when amos-formal-engines-master routes to this specialized capability. Do not use for generic tasks outside formal domain.
parent_skill: amos-formal-engines-master
domain: formal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/formal-engines
- rscf/source_claim
- hml/h
- epistemic/source_claim
- amos_os
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L3_dependency
- L5_scope
- L7_authority
- L22_replayability
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L3
- L4
- L5
- L7
- L16
- L17
- L18
- L19
- L22
license: MIT
steward: Trang Phan
---

# Time Series Conformal Uq Rscf Engine

## Identity

Origin architect: **Trang Phan**. Domain: formal. Parent: amos-formal-engines-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
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

- **time_series_eng.verify_proof**: Verify formal proofs against axioms, inference rules, and consistency constraints
- **time_series_eng.check_soundness**: Check soundness and completeness of formal systems under test
- **time_series_eng.propagate_constraints**: Propagate constraints through the formal system and detect unsatisfiable cores
- **time_series_eng.validate_invariant**: Validate invariants hold under all specified operating conditions
- **time_series_eng.detect_contradiction**: Detect contradictions and derive minimal conflict explanations
- **time_series_eng.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **time_series_eng.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **time_series_eng.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/math/AMOS_Signal_Processing_Kernel_v0_Math_Foundations.md` (content_hash: 3097ca6718b6eb60) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE.md` (content_hash: 7369abada641e374) (vault canon, SOURCE_CLAIM)

### Time Series Conformal UQ

From Signal Processing Kernel: Time series analysis with conformal prediction. From C02 Math & Compute: Uncertainty quantification.

**Conformal prediction model**:
- **Nonconformity score**: measures how nonconforming a new observation is to the calibration set
- **Calibration set**: a held-out set used to calibrate prediction intervals
- **Prediction interval**: an interval that contains the true value with declared probability
- **Exchangeability**: conformal prediction requires exchangeability of data points

**UQ protocol**:
1. **Train model**: train the prediction model on training data
2. **Calibrate**: calibrate prediction intervals on calibration set
3. **Predict**: predict with confidence intervals for new observations
4. **Validate**: validate that intervals achieve declared coverage
5. **Report**: report predictions with intervals and provenance

**RSCF laws**:
- `INTERVAL != CERTAINTY`: a prediction interval is not certainty; it is bounded uncertainty
- `COVERAGE != GUARANTEE`: declared coverage is a target, not a guarantee
- `EXCHANGEABILITY != IID`: exchangeability is weaker than IID; it allows non-IID data

### Epistemic Boundary

Time series conformal UQ is a statistical method. It does not prove intervals always achieve coverage, that exchangeability always holds, or that predictions are always correct.

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
- **G5

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-time-series-conformal-uq-rscf-engine_MOC]]

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


## Do not use

- For generic mathematical analysis outside the formal verification framework
- To claim physical quantum mechanics predictions (AMOS_MODEL only)
- As a substitute for domain-specific numerical or optimization evidence
- Outside formal/math domain reasoning

## References

- `references/biostatistics_kernel.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `` — skill Map of Content
- `amos-formal-engines-master` — parent skill
- `` — corresponding workflow
- `amos-time-series-conformal-uq-rscf-engine-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-time-series-conformal-uq-rscf-engine
node_type: skill
path: 07_SKILLS/amos-time-series-conformal-uq-rscf-engine/[[SKILL]].md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
