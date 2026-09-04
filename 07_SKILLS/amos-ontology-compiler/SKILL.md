---
schema_version: 1.0
title: SKILL — Amos Ontology Compiler
type: skill
source: 07_SKILLS/amos-ontology-compiler
name: amos-ontology-compiler
description: Ontology Compiler — canon and universe capability. Use when canon reasoning, universe-level analysis, or invariant verification. Use when amos-canon-universe-master routes to this specialized capability. Do not use for generic tasks outside canon domain.
parent_skill: amos-canon-universe-master
domain: canon
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
  - type/skill
  - type/skill
  - domain/canon-universe
  - epistemic/source_claim
  - hml/h
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
hml_level: H
gmef_gates:
  - L0_integrity
  - L1_epistemic
  - L2_provenance
  - L3_dependency
  - L5_scope
  - L7_authority
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
license: MIT
steward: Trang Phan
---

# Ontology Compiler

## Identity

Origin architect: **Trang Phan**. Domain: canon. Parent: amos-canon-universe-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.

## When to Use

- When compiling canonical structure from vault sources
- When checking canon consistency for contradictions and gaps
- When enforcing canon invariants across all parts
- When navigating canon to locate parts for any topic
- When the parent skill (`amos-canon-universe-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **ontology_compiler.compile_canon**: Compile canonical structure from sources into a consistent, navigable canon
- **ontology_compiler.check_consistency**: Check canon consistency: no contradictions, no gaps, no orphan references
- **ontology_compiler.enforce_invariant**: Enforce canon invariants: structural laws that must hold across all parts
- **ontology_compiler.navigate_canon**: Navigate canon: locate the canonical part for any topic or query
- **ontology_compiler.validate_substrate**: Validate canonical software substrate against canon requirements

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 5344bb5fa149725a) for the full vault-sourced domain knowledge (9514 chars).

- **ontology_compiler.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **ontology_compiler.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **ontology_compiler.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **ontology_compiler.compile_canon**: Compile canonical structure from sources into a consistent, navigable canon
1. **ontology_compiler.check_consistency**: Check canon consistency: no contradictions, no gaps, no orphan references
1. **ontology_compiler.enforce_invariant**: Enforce canon invariants: structural laws that must hold across all parts
1. **ontology_compiler.navigate_canon**: Navigate canon: locate the canonical part for any topic or query
1. **ontology_compiler.validate_substrate**: Validate canonical software substrate against canon requirements
1. **ontology_compiler.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **ontology_compiler.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
1. **ontology_compiler.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/ARCHITECTURE/AMOS ARCHITECTURE.md` (content_hash: 66150ef7c392872f) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Ontology Compiler

From Cosmo Brain AMOS Architecture: Ontology Compiler as execution layer E3. Compiles concepts, relations, and distinctions into executable coherence architectures.

**Ontology Compiler equation** (AMOS_MODEL):

```
O = (D × C × T) / (X + A)
```

- O = ontology integrity, D = definitional precision, C = cross-domain consistency, T = type coherence
- X = contradiction, A = ambiguity

**Governs**: entities, types, operators, hierarchy, inheritance, state grammar

**Input**: Concepts, Relations, Distinctions, Scientific Structures, Civilization Memory
**Output**: Executable Coherence Architectures

**Compiler functions**:

- **Stabilize meaning**: stabilize the meaning of concepts across the ontology
- **Resolve contradictions**: resolve contradictions in the ontology
- **Map cross-domain topology**: map the cross-domain topology of the ontology
- **Compile**: compile the ontology into executable form

**Compiler laws**:

- `ONTOLOGY != TAXONOMY`: ontology includes relations and constraints; taxonomy is hierarchical classification only
- `COMPILED != EXECUTABLE`: compilation produces executable form; executability requires runtime validation
- `MEANING != DEFINITION`: meaning is contextual; definition is declarative

### Epistemic Boundary

Ontology compiler is an AMOS_MODEL. It does not prove all ontologies are compilable, that the equation is empirically validated, or that compiled ontologies are always correct.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for every derived cl

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-ontology-compiler/amos-ontology-compiler_MOC|amos-ontology-compiler_MOC]]

## Examples

- **Scenario**: When compiling canonical structure from vault sources

  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When checking canon consistency for contradictions and gaps

  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When enforcing canon invariants across all parts

  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance

## Anti-Patterns

- **Do not use** for tasks outside the canon domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval

## Composition

- **Parent**: `amos-canon-universe-master` — routes to this skill when canon specialization is needed
- **Peers**: Other skills in the `canon` domain may be composed in sequence
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

- For generic structural analysis outside the canon framework
- To claim empirical validation of consciousness or civilization theories
- As a substitute for domain-specific historical or scientific evidence
- Outside canon/universe domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- \`\` — skill Map of Content
- `amos-canon-universe-master` — parent skill
- \`\` — corresponding workflow
- `amos-ontology-compiler-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-ontology-compiler
node_type: skill
path: 07_SKILLS/amos-ontology-compiler/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
