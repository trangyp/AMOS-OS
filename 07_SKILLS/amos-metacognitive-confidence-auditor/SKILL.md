---
title: SKILL — Amos Metacognitive Confidence Auditor
type: skill
source: 07_SKILLS/amos-metacognitive-confidence-auditor
name: amos-metacognitive-confidence-auditor
description: Metacognitive Confidence Auditor — audit and repair capability. Use when
  auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master
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
- capability/cognition
- capability/repair
- rscf/epistemic
- rscf/M-memory
- rscf/C-constraint
- rscf/P-repair
- rscf/Z-collapse
- rscf/type-process
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-metacognitive-confidence-auditor
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







# Metacognitive Confidence Auditor

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

- **metacognitive_confidence.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **metacognitive_confidence.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **metacognitive_confidence.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **metacognitive_confidence.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **metacognitive_confidence.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
- **metacognitive_confidence.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **metacognitive_confidence.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **metacognitive_confidence.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 308a3432feb5f1b0) for the full vault-sourced domain knowledge (5553 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/cognitive/Metacognitive.md` (content_hash: 156abe467cfa7744) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE.md` (content_hash: e3ca4951a743518b) (vault canon, SOURCE_CLAIM)

### Metacognitive Confidence Auditor

From Cosmo Brain Metacognitive: Metacognitive monitoring and control. From C05 Mind & Behavior: Confidence calibration and metacognitive awareness.

**Metacognitive confidence model**:
- **Confidence calibration**: confidence must be calibrated to evidence strength
- **Confidence ceiling**: confidence cannot exceed evidence support (from RSCF)
- **Confidence tracking**: track confidence changes through reasoning chains
- **Confidence audit**: audit confidence against actual outcomes

**Metacognitive monitoring**:
- **Self-monitoring**: the system monitors its own reasoning process
- **Error detection**: the system detects errors in its own reasoning
- **Uncertainty awareness**: the system is aware of its own uncertainty
- **Confidence awareness**: the system is aware of its own confidence level

**Auditing protocol**:
1. **Sample**: sample reasoning chains for audit
2. **Check confidence**: check confidence against evidence support
3. **Check calibration**: check confidence calibration against outcomes
4. **Check ceiling**: check confidence does not exceed evidence
5. **Report**: report audit findings with provenance

**Auditing laws**:
- `CONFIDENCE != ACCURACY`: high confidence does not imply high accuracy
- `CALIBRATION != CORRECTION**: calibration aligns confidence with accuracy; correction fixes errors
- `METACOGNITION != COGNITION**: metacognition is cognition about cognition; it is not cognition itself

### Epistemic Boundary

Metacognitive confidence auditing is an epistemic construct. It does not prove confidence is always calibrated, that metacognition is always accurate, or that auditing detects all confidence errors.

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: I

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-metacognitive-confidence-auditor_MOC]]

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
- `[[amos-metacognitive-confidence-auditor_MOC]]` — skill Map of Content
- `amos-audit-repair-master` — parent skill
- `[[amos-metacognitive-confidence-auditor-workflow]]` — corresponding workflow
- `amos-metacognitive-confidence-auditor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-metacognitive-confidence-auditor
node_type: skill
path: 07_SKILLS/amos-metacognitive-confidence-auditor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
