---
schema_version: 1.0
title: SKILL — Amos Repair Priority Governor
type: skill
source: 07_SKILLS/amos-repair-priority-governor
name: amos-repair-priority-governor
description: Repair Priority Governor — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability. Do not use for generic tasks outside audit domain.
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

# Repair Priority Governor

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

- **repair_priority.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **repair_priority.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **repair_priority.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **repair_priority.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **repair_priority.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
- **repair_priority.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **repair_priority.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **repair_priority.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: a7b67e0c7ee84164) for the full vault-sourced domain knowledge (7564 chars).

## Operations

1. **repair_priority.audit_claim**: Audit claims against evidence, provenance, and epistemic class
1. **repair_priority.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
1. **repair_priority.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
1. **repair_priority.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
1. **repair_priority.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
1. **repair_priority.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **repair_priority.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
1. **repair_priority.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/D/Distinction–Mutation–Entropy–Repair.md` (content_hash: 551b49315372ac2d) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Repair Priority Governor

From Cosmo Brain Distinction-Mutation-Entropy-Repair: Repair priority formula and selective repair. Global recomputation is last resort.

**Repair priority formula** (SOURCE_DERIVED):

```
Priority_i = Impact_i × DependencyFanout_i × Irreversibility_i × UncertaintyReduction_i
```

subject to hard safety constraints.

**Priority factors**:

- **Impact**: how much does the issue affect the system?
- **Dependency fanout**: how many other components depend on this one?
- **Irreversibility**: how hard is it to undo the repair if it's wrong?
- **Uncertainty reduction**: how much does the repair reduce uncertainty?

**Selective repair principle**: `Invalid(p) => Repair(p)` not `Invalid(p) => ResetEverything`. Global recomputation is last resort.

**5 Priority levels** (P0-P4):

- **P0 CRITICAL**: system cannot function; repair immediately, block all other work
- **P1 HIGH**: core capability degraded; repair before any non-repair work
- **P2 MEDIUM**: secondary capability degraded; repair within current cycle
- **P3 LOW**: minor issue; repair when capacity allows
- **P4 DEFERRED**: known issue, no current impact; log and monitor

**Repair laws**:

- `RepairCapacity > RepairDemand` required for autonomous repair
- `REPAIR != IMPROVEMENT`: repair fixes a specific issue; it does not improve the system
- \`SYMPTOM != CAUSE\*\*: repairing the symptom does not repair the cause
- \`SELECTIVE != GLOBAL\*\*: selective repair targets the specific issue; global recomputation is last resort

### Epistemic Boundary

Repair priority governance is an operational construct. It does not prove optimal repair ordering, that all issues are prioritized, or that repair always succeeds.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## V

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-repair-priority-governor/amos-repair-priority-governor_MOC|amos-repair-priority-governor_MOC]]

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
- \`\` — skill Map of Content
- `amos-audit-repair-master` — parent skill
- \`\` — corresponding workflow
- `amos-repair-priority-governor-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-repair-priority-governor
node_type: skill
path: 07_SKILLS/amos-repair-priority-governor/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
