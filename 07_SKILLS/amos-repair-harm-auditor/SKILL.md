---
title: SKILL — Amos Repair Harm Auditor
type: skill
source: 07_SKILLS/amos-repair-harm-auditor
name: amos-repair-harm-auditor
description: Repair Harm Auditor — audit and repair capability. Use when auditing,
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
- capability/repair
- capability/audit
- rscf/epistemic
- rscf/M-memory
- rscf/C-constraint
- rscf/P-repair
- rscf/Z-collapse
- rscf/type-process
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-repair-harm-auditor
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---




# Repair Harm Auditor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Repair Harm Auditor

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

- **repair_harm.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **repair_harm.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **repair_harm.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **repair_harm.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **repair_harm.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
- **repair_harm.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **repair_harm.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **repair_harm.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 2397f64f36ba675e) for the full vault-sourced domain knowledge (7564 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/O/overlooked.md` (content_hash: eb91d778a79b4c6a) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/system/AMOS_Evolutionary_Adaptive_Systems_Cancer_to_AI_v2.md` (content_hash: 5843a9c7931441ea) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/amos-general/A/PART/AMOS_7_PART_UNIVERSE_CANON_FULL_ARCHITECTURE_V2.md` (content_hash: f1acd357d7c51047) (vault canon, SOURCE_CLAIM)

### Repair Harm Auditor

From Cosmo Brain Overlooked: Repair Harm Auditor measures whether repair increases long-term coherence or only suppresses visible failure. From Evolutionary Adaptive Systems: Repair harm as defense externality. From 7-Part Universe Canon: Repair harm firewall.

**Repair harm definition**: A repair is invalid if it restores one part while causing larger structural damage elsewhere.

**Defense externality equation** (SOURCE_DERIVED):
```
NetDefenseValue = PreventedHarm - DefenseExternality
```
- Repair harm is a defense externality alongside: over-refusal, capability destruction, false quarantine, excessive friction, loss of useful diversity

**Repair Harm Auditor module** (from Overlooked):
- Measures whether repair increases long-term coherence
- Or only suppresses visible failure
- Key question: does the repair make the system genuinely better, or just quieter?

**Repair harm firewall** (from 7-Part Universe Canon):
- A repair is invalid if it restores one part while causing larger structural damage elsewhere
- Repair must be evaluated for system-wide impact, not just local fix

**Auditing protocol**:
1. **Measure local benefit**: measure the benefit of the repair at the repair site
2. **Measure systemic harm**: measure the harm caused elsewhere in the system
3. **Compute net value**: compute net defense value
4. **Decide**: if net value < 0, the repair is harmful; block it
5. **Record**: record with provenance

**Auditing laws**:
- `REPAIR != IMPROVEMENT`: repair fixes a specific issue; it does not always improve the system
- `LOCAL_FIX != SYSTEMIC_HEALTH**: a local fix may cause systemic harm
- `SUPPRESSION != RESOLUTION**: suppressing a visible failure is not resolving the underlying issue

### Epistemic Boundary

Repair harm auditing is an operational construct. It does not prove all repair harm is detected, that the net value calculation is always correct, or that harmful repairs can always be blocked.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-repair-harm-auditor_MOC]]

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
- `[[amos-repair-harm-auditor_MOC]]` — skill Map of Content
- `amos-audit-repair-master` — parent skill
- `[[amos-repair-harm-auditor-workflow]]` — corresponding workflow
- `amos-repair-harm-auditor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-repair-harm-auditor
node_type: skill
path: 07_SKILLS/amos-repair-harm-auditor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
