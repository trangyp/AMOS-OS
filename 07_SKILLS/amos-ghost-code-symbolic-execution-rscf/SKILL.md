---
title: SKILL — Amos Ghost Code Symbolic Execution Rscf
type: skill
source: 07_SKILLS/amos-ghost-code-symbolic-execution-rscf
name: amos-ghost-code-symbolic-execution-rscf
description: Ghost Code Symbolic Execution — formal verification capability. Use when
  formal verification, symbolic execution, proof checking, or mathematical reasoning.
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
- capability/code
- capability/symbolic
- capability/ghost-code
- capability/execution
- capability/reasoning
- rscf/epistemic
- rscf/C-constraint
- rscf/G-relation
- rscf/S-state
- rscf/T-topology
- rscf/type-model
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-ghost-code-symbolic-execution-rscf
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---






# Ghost Code Symbolic Execution Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-formal-engines-master`
- **Domain**: formal
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Formal reasoning engine for Ghost Code Symbolic Execution Rscf

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

- **ghost_code.verify_proof**: Verify formal proofs against axioms, inference rules, and consistency constraints
- **ghost_code.check_soundness**: Check soundness and completeness of formal systems under test
- **ghost_code.propagate_constraints**: Propagate constraints through the formal system and detect unsatisfiable cores
- **ghost_code.validate_invariant**: Validate invariants hold under all specified operating conditions
- **ghost_code.detect_contradiction**: Detect contradictions and derive minimal conflict explanations
- **ghost_code.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **ghost_code.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **ghost_code.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/audit/REAL_CODE_VERIFICATION_COMPLETE.md` (content_hash: 5b9bdbb82bfbbcc5) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE.md` (content_hash: f23d35766fe766bc) (vault canon, SOURCE_CLAIM)

### Ghost Code Symbolic Execution

From Cosmo Brain Real Code Verification System: Code verification with 6 canonical formulas and 8 code levels.

**6 Canonical Formulas** (SOURCE_DERIVED):
1. `RealCode(c) = Compiles(c) ∧ Runs(c) ∧ BindsAllSymbols(c) ∧ ExposesIO(c) ∧ PassesTests(c)`
2. `RealFeature(f) = Spec(f) ∧ Interface(f) ∧ Logic(f) ∧ Output(f) ∧ Verify(f)`
3. `RealSoftware(s) = State(s) ∧ Interfaces(s) ∧ Execution(s) ∧ Persistence(s) ∧ Verification(s) ∧ Recovery(s)`
4. `Understand(c) = Parse(c) + Type(c) + Semantics(c) + Runtime(c) + SpecMatch(c)`
5. `ClaimedCapability <= VerifiedCapability` (no fake claims invariant)
6. `NOT Verified -> NOT Complete` (no completion without proof invariant)

**8 Code Levels**:
- L0 Text: code-shaped text
- L1 Parseable: syntax
- L2 Executable: syntax + runtime
- L3 Functional: syntax + runtime + correct I/O
- L4 Verified: syntax + runtime + correct I/O + tests
- L5 Production: verified + error handling + persistence + observability

**Reality Score**: `RealityScore(f) = (Parse + Bind + Run + IO + State + Test + Error + Observe) / 8`
**Production Ready Threshold**: `RealityScore(f) >= 0.875`

**3 Final Laws**:
1. Code is real only when it becomes verified behavior in a runtime
2. A feature is real only when it transforms input, state, and output under test
3. Software is real only when it executes, persists, verifies, and recovers

**RSCF laws**:
- `SYMBOLIC != CONCRETE`: symbolic execution explores paths; it does not prove runtime behavior
- `GHOST != REAL`: ghost code is for verification; it is not production code
- `VERIFIED != CORRECT`: verification proves properties hold; it does not prove the code is correct

### Epistemic Boundary

Ghost code symbolic execution is a formal verification method. It does not prove all bugs are found, that symbolic execution is complete, or that verified properties guarantee runtime correctness.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-ghost-code-symbolic-execution-rscf_MOC]]

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
- `references/unified_coding_engine_spec.md` — loaded on demand
- `[[amos-ghost-code-symbolic-execution-rscf_MOC]]` — skill Map of Content
- `amos-formal-engines-master` — parent skill
- `[[amos-ghost-code-symbolic-execution-rscf-workflow]]` — corresponding workflow
- `amos-ghost-code-symbolic-execution-rscf-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-ghost-code-symbolic-execution-rscf
node_type: skill
path: 07_SKILLS/amos-ghost-code-symbolic-execution-rscf/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
