---
schema_version: 1.0
title: SKILL — Amos System Completion Auditor
type: skill
source: 07_SKILLS/amos-system-completion-auditor
name: amos-system-completion-auditor
description: System Completion Auditor — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability. Do not use for generic tasks outside audit domain.
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

# System Completion Auditor

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

- **system_completion.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **system_completion.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **system_completion.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **system_completion.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **system_completion.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 9faeebb0102d09c3) for the full vault-sourced domain knowledge (9570 chars).

- **system_completion.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **system_completion.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **system_completion.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **system_completion.audit_claim**: Audit claims against evidence, provenance, and epistemic class
1. **system_completion.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
1. **system_completion.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
1. **system_completion.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
1. **system_completion.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
1. **system_completion.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **system_completion.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
1. **system_completion.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### System Completion Audit

The Cognitive Organism OS defines system completion auditing for verifying that all declared capabilities are implemented, tested, and validated.

**Audit dimensions**:

1. **Capability coverage**: all declared capabilities have implementations
1. **Test coverage**: all implementations have tests
1. **Validation coverage**: all tests pass validation gates
1. **Provenance coverage**: all implementations have traceable provenance
1. **Documentation coverage**: all capabilities are documented
1. **Binding coverage**: all capabilities have 1:1:1 binding (skill-agent-workflow)

**Completion law**: `IMPLEMENTED != COMPLETE`. A capability being implemented does not mean it is complete. Completion requires implementation + tests + validation + provenance + documentation + binding.

**Audit protocol**:

1. List all declared capabilities
1. Check each capability for implementation
1. Check each implementation for tests
1. Check each test for validation gate passage
1. Flag gaps as COMPLETION_GAP
1. Report completion percentage with provenance

### Epistemic Boundary

System completion audit is a quality construct. It does not prove the system is perfect, bug-free, or that all capabilities are correctly implemented. It verifies declared completeness, not absolute correctness.

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

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-system-completion-auditor/amos-system-completion-auditor_MOC|amos-system-completion-auditor_MOC]]

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
- \`\` — skill Map of Content
- `amos-audit-repair-master` — parent skill
- \`\` — corresponding workflow
- `amos-system-completion-auditor-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-system-completion-auditor
node_type: skill
path: 07_SKILLS/amos-system-completion-auditor/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
