---
title: SKILL — Frontend Engineering Qa
type: skill
source: 07_SKILLS/frontend-engineering-qa
name: frontend-engineering-qa
description: Frontend Engineering Qa — technology and engineering capability. Use
  when software development, engineering design, or technical architecture. Use when
  amos-c10-tech-engineering-master routes to this specialized capability.
parent_skill: amos-c10-tech-engineering-master
domain: c10
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/tech-engineering
- canon-group/tech-ai
- topic/engineering
- capability/frontend
- capability/provenance
- rscf/epistemic
- rscf/T-topology
- rscf/M-memory
- rscf/C-constraint
- rscf/B-boundary
- rscf/type-system
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- frontend-engineering-qa
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---






# Frontend Engineering Qa

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c10-tech-engineering-master`
- **Domain**: c10
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Tech-engineering engine for Frontend Engineering Qa

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

- **frontendering_qa.analyze_architecture**: Analyze software architecture: patterns, dependencies, coupling, cohesion
- **frontendering_qa.discover_program**: Discover program behavior: black-box analysis, symbolic execution, fuzzing
- **frontendering_qa.verify_code_facts**: Verify code facts: type safety, memory safety, termination, complexity
- **frontendering_qa.optimize_performance**: Optimize performance: profiling, bottleneck analysis, and resource tuning
- **frontendering_qa.enforce_bounds**: Enforce bounded code: resource limits, time limits, and capability limits
- **frontendering_qa.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **frontendering_qa.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **frontendering_qa.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 9d19043fdc5ef7a6) for the full vault-sourced domain knowledge (6462 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE.md` (content_hash: f23d35766fe766bc) (vault canon, SOURCE_CLAIM)

### Frontend Engineering QA

From C10 Tech & Engineering: Frontend quality assurance.

**Frontend QA dimensions**:
- **Accessibility**: WCAG compliance, screen reader compatibility, keyboard navigation
- **Cross-browser**: compatibility across browsers and versions
- **Responsive**: layout correctness across viewport sizes
- **Performance**: render time, bundle size, runtime performance
- **Visual regression**: visual consistency across changes
- **User experience**: interaction correctness, error states, loading states

**Frontend QA protocol**:
1. **Unit test**: test individual components in isolation
2. **Integration test**: test component composition
3. **Visual regression**: compare visual output against baseline
4. **Accessibility audit**: audit against WCAG criteria
5. **Performance audit**: audit render time and bundle size
6. **Cross-browser test**: test across target browsers

### Epistemic Boundary

Frontend engineering QA is an engineering process. It does not prove the UI is perfect, that all browsers are covered, or that accessibility is complete.

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

- **Skill**: `fronte

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[frontend-engineering-qa_MOC]]

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
- `[[frontend-engineering-qa_MOC]]` — skill Map of Content
- `amos-c10-tech-engineering-master` — parent skill
- `[[frontend-engineering-qa-workflow]]` — corresponding workflow
- `frontend-engineering-qa-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: frontend-engineering-qa
node_type: skill
path: 07_SKILLS/frontend-engineering-qa/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
