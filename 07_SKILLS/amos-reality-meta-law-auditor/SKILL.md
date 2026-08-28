---
title: SKILL — Amos Reality Meta Law Auditor
type: skill
source: 07_SKILLS/amos-reality-meta-law-auditor
name: amos-reality-meta-law-auditor
description: Reality Meta Law Auditor — audit and repair capability. Use when auditing,
  failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master
  routes to this specialized capability.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/audit-repair
- canon-group/tech-ai
- topic/quality-assurance
- capability/audit
- capability/repair
- rscf/epistemic
- rscf/C-constraint
- rscf/M-memory
- rscf/P-repair
- rscf/Z-collapse
- rscf/type-model
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-reality-meta-law-auditor
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
---







# Reality Meta Law Auditor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Reality Meta Law Auditor

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

- **reality_meta.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **reality_meta.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **reality_meta.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **reality_meta.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **reality_meta.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 82f89f9854baa4fc) for the full vault-sourced domain knowledge (9344 chars).
- **reality_meta.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **reality_meta.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **reality_meta.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE.md` (content_hash: ff5575df755d7e25) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Reality Meta-Law Auditor

From C01 Meta Logic: 5 meta-laws as the foundation for reality auditing. From Cognitive Organism OS: Reality Gate as L0 cognitive substrate.

**5 Meta-laws for reality auditing**:
1. **Law of Law**: no unresolved contradictions within the system
2. **Rule of 2**: at least 2 independent supports for any claim
3. **Rule of 4**: check 4 dimensions: scope, regime, evidence, falsifier
4. **Signal Fidelity Preservation**: no loss of signal fidelity through processing
5. **Structural Integrity**: system structure must be maintained under stress

**Reality auditing protocol**:
1. **Check contradictions**: verify no unresolved contradictions (Law of Law)
2. **Check independence**: verify at least 2 independent supports (Rule of 2)
3. **Check 4 dimensions**: verify scope, regime, evidence, falsifier (Rule of 4)
4. **Check signal fidelity**: verify no signal fidelity loss
5. **Check structural integrity**: verify structure maintained under stress
6. **Report**: report with audit outcome and provenance

**Reality Gate (L0)**:
- **Perception-as-science-substrate filter**: perceptions filtered through science substrate
- **Anti-autopoisoning**: system cannot poison its own perception
- **Reality check**: every observation must pass reality check

**Auditing laws**:
- `AUDIT != PROOF`: auditing checks declared properties; it does not prove truth
- `META-LAW != LAW**: meta-laws govern laws; they are not laws themselves
- `REALITY != PERCEPTION**: reality is independent of observation; perception is interpretation

### Epistemic Boundary

Reality meta-law auditing is an epistemic governance construct. It does not prove reality is knowable, that all meta-laws are covered, or that auditing always detects violations.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retrac

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-reality-meta-law-auditor_MOC]]

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


## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-reality-meta-law-auditor_MOC]]` — skill Map of Content
- `amos-audit-repair-master` — parent skill
- `[[amos-reality-meta-law-auditor-workflow]]` — corresponding workflow
- `amos-reality-meta-law-auditor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-reality-meta-law-auditor
node_type: skill
path: 07_SKILLS/amos-reality-meta-law-auditor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
