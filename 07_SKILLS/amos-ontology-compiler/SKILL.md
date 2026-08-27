---
title: SKILL
type: skill
name: amos-ontology-compiler
description: Ontology Compiler — canon and universe capability. Use when canon reasoning, universe-level analysis, or invariant verification. Use when amos-canon-universe-master routes to this specialized capability.
parent_skill: amos-canon-universe-master
domain: canon
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-ontology-compiler]
---


# Ontology Compiler

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-canon-universe-master`
- **Domain**: canon
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Canon and universe engine for Ontology Compiler

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