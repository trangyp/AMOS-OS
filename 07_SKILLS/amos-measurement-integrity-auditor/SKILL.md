---
schema_version: 1.0
title: SKILL — Amos Measurement Integrity Auditor
type: skill
source: 07_SKILLS/amos-measurement-integrity-auditor
name: amos-measurement-integrity-auditor
description: Measurement Integrity Auditor — audit and repair capability. Use when
  auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master
  routes to this specialized capability. Do not use for generic tasks outside audit
  domain.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- type/skill
- domain/audit-repair
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
- L22_replayability
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
- L22
license: MIT
steward: Trang Phan
---

# Measurement Integrity Auditor

## Identity

Origin architect: **Trang Phan**. Domain: audit. Parent: amos-audit-repair-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When auditing claims against evidence and provenance
- When detecting gaps in capabilities, evidence, tests, or monitors
- When allocating repair resources to highest-leverage gaps
- When verifying gap closure across the full lifecycle chain
- When the parent skill (`amos-audit-repair-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **measurement_integrity.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **measurement_integrity.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **measurement_integrity.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **measurement_integrity.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **measurement_integrity.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: d0d25eb4d17058d9) for the full vault-sourced domain knowledge (9047 chars).
- **measurement_integrity.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **measurement_integrity.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **measurement_integrity.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **measurement_integrity.audit_claim**: Audit claims against evidence, provenance, and epistemic class
2. **measurement_integrity.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
3. **measurement_integrity.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
4. **measurement_integrity.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
5. **measurement_integrity.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
6. **measurement_integrity.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
7. **measurement_integrity.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
8. **measurement_integrity.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/Collapse/AMOS Collapse-Space Coverage Audit.md` (content_hash: 8a6e8edc4d87f23a) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/dated/2026-08-23/2026-08-23 Vault Integrity Pass.md` (content_hash: ce31f8fdd0467e1e) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE.md` (content_hash: ff5575df755d7e25) (vault canon, SOURCE_CLAIM)

### Measurement Integrity Auditor

From Cosmo Brain Collapse-Space Coverage Audit: Measurement integrity in collapse-space auditing. From Vault Integrity Pass: 7-part canon lens applied to vault integrity.

**Measurement integrity model**:
- **Measurement validity**: measurements must be valid (measure what they claim to measure)
- **Measurement reliability**: measurements must be reliable (reproducible under same conditions)
- **Measurement accuracy**: measurements must be accurate (close to true value)
- **Measurement precision**: measurements must be precise (low variance)

**7-part canon lens for integrity auditing** (from Vault Integrity Pass):
1. **Constraint**: what bounded this audit (scope, limitations)
2. **Flow**: what was done (steps, actions)
3. **Structure**: what holds it (canon notes, validators, mappings)
4. **Enforcement**: what corrects errors (deterministic gates, re-runnable audits)
5. **Time**: lifecycle considerations (drift, new gaps)
6. **Adaptation**: how to handle new gaps (add pointer/anchor, never fabricate)
7. **Termination**: completion state (GREEN/RED, known-state)

**Integrity audit protocol**:
1. **Baseline**: file health (0 empty, 0 broken symlinks)
2. **Scan**: scan for broken targets, gaps, orphans
3. **Classify**: classify issues (drift, genuine gap, known-state)
4. **Repair**: repair drift links, create anchor notes for gaps
5. **Validate**: run deterministic validator
6. **Report**: report with honest status (don't claim zero broken if data-dump orphans exist)

**Integrity law**: `AUDIT_PASS != PERFECT`. An audit pass means declared checks pass; it does not prove perfection. Known-state issues are documented, not hidden.

### Epistemic Boundary

Measurement integrity auditing is an operational governance construct. It does not prove all issues are detected, that measurements are always correct, or that the audit is complete.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the q

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-measurement-integrity-auditor_MOC]]

## Examples

- **Scenario**: When auditing claims against evidence and provenance
  - **Input**: A query matching this skill's domain (audit)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When detecting gaps in capabilities, evidence, tests, or monitors
  - **Input**: A query matching this skill's domain (audit)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When allocating repair resources to highest-leverage gaps
  - **Input**: A query matching this skill's domain (audit)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the audit domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-audit-repair-master` — routes to this skill when audit specialization is needed
- **Peers**: Other skills in the `audit` domain may be composed in sequence
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

- For generic audit analysis outside the AMOS audit/repair framework
- To claim empirical validation of repair or recovery theories
- As a substitute for domain-specific audit or quality evidence
- Outside audit/repair domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-audit-repair-master` — parent skill
- `` — corresponding workflow
- `amos-measurement-integrity-auditor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-measurement-integrity-auditor
node_type: skill
path: 07_SKILLS/amos-measurement-integrity-auditor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
