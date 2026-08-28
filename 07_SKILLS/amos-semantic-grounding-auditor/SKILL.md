---
title: SKILL — Amos Semantic Grounding Auditor
type: skill
source: 07_SKILLS/amos-semantic-grounding-auditor
name: amos-semantic-grounding-auditor
description: Semantic Grounding Auditor — audit and repair capability. Use when auditing,
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
- rscf/epistemic
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-semantic-grounding-auditor
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---



# Semantic Grounding Auditor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Semantic Grounding Auditor

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

- **semantic_grounding.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **semantic_grounding.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **semantic_grounding.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **semantic_grounding.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **semantic_grounding.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
- **semantic_grounding.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **semantic_grounding.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **semantic_grounding.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 85c573728ca44418) for the full vault-sourced domain knowledge (5667 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/O/overlooked.md` (content_hash: eb91d778a79b4c6a) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/misc/N/New.md` (content_hash: 32c4e8fb2fe2d69f) (vault canon, SOURCE_CLAIM)

### Semantic Grounding Auditor

From Cosmo Brain Overlooked: Semantic Grounding Divergence Detector to measure distance between symbolic coherence and structural reality. From New.md: Concrete world model with safe semantics envelope.

**Semantic grounding divergence equations** (SOURCE_DERIVED):
```
Divergence = |Semantic_Coherence - Structural_Grounding|
Grounding_Loss = 1 - exp(-Divergence)
```
- **Semantic coherence**: internal consistency of symbols
- **Structural grounding**: correlation with measurable reality

**Concrete world model** (from New.md):
```
w = (S, T, Predicates, Ctx, Trace)
```
- S = states, T = transitions, Predicates = predicates, Ctx = context, Trace = execution trace
- Claims evaluated via `w ⊨ c` (world satisfies claim)

**Grounding loss examples**: over-academic abstraction, LLM hallucination, legal formalism detached from reality

**Auditing protocol**:
1. **Measure semantic coherence**: measure internal consistency of symbols
2. **Measure structural grounding**: measure correlation with measurable reality
3. **Compute divergence**: compute divergence between the two
4. **Compute grounding loss**: compute grounding loss from divergence
5. **Report**: report with provenance and epistemic class

**Auditing laws**:
- `COHERENCE != GROUNDING`: internal coherence does not imply external grounding
- `SYMBOL != REALITY`: symbols represent reality; they are not reality
- `GROUNDED != TRUE**: grounding connects to measurable reality; it does not prove truth

### Epistemic Boundary

Semantic grounding auditing is an epistemic construct. It does not prove all grounding loss is detected, that the divergence formula is universally applicable, or that grounding implies truth.

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-semantic-grounding-auditor_MOC]]

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
- `[[amos-semantic-grounding-auditor_MOC]]` — skill Map of Content
- `amos-audit-repair-master` — parent skill
- `[[amos-semantic-grounding-auditor-workflow]]` — corresponding workflow
- `amos-semantic-grounding-auditor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-semantic-grounding-auditor
node_type: skill
path: 07_SKILLS/amos-semantic-grounding-auditor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
