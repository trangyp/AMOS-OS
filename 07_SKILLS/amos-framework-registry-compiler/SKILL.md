---
title: SKILL — Amos Framework Registry Compiler
type: skill
source: 07_SKILLS/amos-framework-registry-compiler
name: amos-framework-registry-compiler
description: Framework Registry Compiler — technology and engineering capability. Use when software development,
  engineering design, or technical architecture. Use when amos-c10-tech-engineering-master routes to this
  specialized capability.
parent_skill: amos-c10-tech-engineering-master
domain: c10
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/tech-engineering
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
---








# Framework Registry Compiler

## Identity

Origin architect: **Trang Phan**. Domain: c10. Parent: amos-c10-tech-engineering-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When analyzing software architecture: patterns, dependencies, coupling
- When discovering program behavior via black-box analysis or symbolic execution
- When verifying code facts: type safety, memory safety, termination
- When enforcing bounded code: resource, time, and capability limits
- When the parent skill (`amos-c10-tech-engineering-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **framework_registry.analyze_architecture**: Analyze software architecture: patterns, dependencies, coupling, cohesion
- **framework_registry.discover_program**: Discover program behavior: black-box analysis, symbolic execution, fuzzing
- **framework_registry.verify_code_facts**: Verify code facts: type safety, memory safety, termination, complexity
- **framework_registry.optimize_performance**: Optimize performance: profiling, bottleneck analysis, and resource tuning
- **framework_registry.enforce_bounds**: Enforce bounded code: resource limits, time limits, and capability limits
- **framework_registry.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **framework_registry.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **framework_registry.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: c16fd76631fdb5c1) for the full vault-sourced domain knowledge (6462 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/logic/Biological Programming.md` (content_hash: 0547f70391d7cbf5) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Framework Registry Compiler

From Cosmo Brain Biological Programming: Framework Registry JSON schema to log every new concept with metadata fields. Describes canonical naming and hierarchy map for organizing frameworks.

**Framework Registry JSON schema**:
Every new framework concept is logged with:
- **name**: canonical name of the framework
- **family**: family/group the framework belongs to
- **scope**: declared scope of applicability
- **status**: current status (active, deprecated, experimental)
- **IP status**: intellectual property status
- **location**: location in AMOS architecture

**Compiler operations**:
1. **Register**: register a new framework with full metadata
2. **Validate**: validate the framework against registry schema
3. **Compile**: compile the framework into executable form
4. **Index**: index the framework for retrieval
5. **Cross-reference**: cross-reference with existing frameworks
6. **Hierarchy**: place the framework in the hierarchy map

**Compiler laws**:
- `REGISTERED != VALIDATED`: registration logs the framework; validation checks it
- `COMPILED != EXECUTABLE`: compilation produces executable form; executability requires runtime validation
- `FRAMEWORK != SKILL`: a framework is a structural specification; a skill is a capability declaration

**Canonical naming**: Every framework has a canonical name. Non-canonical names are aliases that resolve to the canonical name.

### Epistemic Boundary

Framework registry compiler is an operational construct. It does not prove all frameworks are registered, that the schema is complete, or that compilation is always correct.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evid

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-framework-registry-compiler_MOC]]

## Examples

- **Scenario**: When analyzing software architecture: patterns, dependencies, coupling
  - **Input**: A query matching this skill's domain (c10)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When discovering program behavior via black-box analysis or symbolic execution
  - **Input**: A query matching this skill's domain (c10)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When verifying code facts: type safety, memory safety, termination
  - **Input**: A query matching this skill's domain (c10)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c10 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c10-tech-engineering-master` — routes to this skill when c10 specialization is needed
- **Peers**: Other skills in the `c10` domain may be composed in sequence
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
- `[[amos-framework-registry-compiler_MOC]]` — skill Map of Content
- `amos-c10-tech-engineering-master` — parent skill
- `[[amos-framework-registry-compiler-workflow]]` — corresponding workflow
- `amos-framework-registry-compiler-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-framework-registry-compiler
node_type: skill
path: 07_SKILLS/amos-framework-registry-compiler/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
