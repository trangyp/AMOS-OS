---
title: SKILL
type: skill
name: docx
description: Docx — technology and engineering capability. Use when software development, engineering design, or technical architecture. Use when amos-c10-tech-engineering-master routes to this specialized capability.
parent_skill: amos-c10-tech-engineering-master
domain: c10
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, docx]
---


# Docx

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c10-tech-engineering-master`
- **Domain**: c10
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Tech-engineering engine for Docx

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

- **docx.parse_document**: Parse .docx files: extract text, tables, styles, headers, footers, and metadata
- **docx.validate_structure**: Validate document structure against OOXML schema and content integrity
- **docx.extract_content**: Extract structured content: paragraphs, runs, tables, images, hyperlinks
- **docx.generate_document**: Generate .docx files from structured content with proper styling and formatting
- **docx.track_provenance**: Track provenance of document content to source sections and transformations
- **docx.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **docx.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **docx.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 869de7474d39fa78) for the full vault-sourced domain knowledge (6462 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE.md` (content_hash: f23d35766fe766bc) (vault canon, SOURCE_CLAIM)

### Utility Tool Integration

This utility skill operates as a file-format handling tool within the AMOS framework. It follows the AMOS tool integration laws:

**Tool laws**:
- `TOOL != CAPABILITY`: a tool is a deployment artifact; a capability is an ontological declaration
- `FORMAT != CONTENT`: file format is not content; content must be extracted and validated
- `PROCESSING != UNDERSTANDING`: processing a file does not mean understanding its content

**Integration protocol**:
1. **Receive**: receive the file with provenance
2. **Parse**: parse the file format
3. **Extract**: extract content with epistemic labels
4. **Validate**: validate extracted content against schema
5. **Output**: output structured content with provenance

### Epistemic Boundary

This utility skill is an operational tool. It does not prove content correctness, that all format variations are supported, or that parsing is always accurate.

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
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **G6 (Failure mode)**: On validation failure, downgrade confidence, flag the gap, escalate — do not force-fit.

## Provenance

- **Skill**: `docx`
- **Parent**: `amos-c10-tech-engineering-master`
- **Domain**: c10
- **Origin architect**: Trang Phan
- **Vault sources**:
- `engine/T/Tech Engine__Archive.md` — Tech Engine__Archive (92349 chars, score: 3), content_hash: 6d78322c6f4a68cf
  - `engine/A/amos_consulting_amos_invest_amos_canon_tech_engine.md` — amos_consulting_amos_invest_am

---
**Links:** [[07_SKILLS_MOC]]
