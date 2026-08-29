---
schema_version: 1.0
title: SKILL — Amos Repair Allocation Optimizer
type: skill
source: 07_SKILLS/amos-repair-allocation-optimizer
name: amos-repair-allocation-optimizer
description: Repair Allocation Optimizer — audit and repair capability. Use when auditing,
  failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master
  routes to this specialized capability. Do not use for generic tasks outside audit
  domain.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/audit-repair
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
- 07-skills-moc
- amos-repair-allocation-optimizer-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- references-moc
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

# Repair Allocation Optimizer

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

- **repair_allocation.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **repair_allocation.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **repair_allocation.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **repair_allocation.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **repair_allocation.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
- **repair_allocation.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **repair_allocation.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **repair_allocation.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: e2f9936cfad21b78) for the full vault-sourced domain knowledge (7564 chars).

## Operations

1. **repair_allocation.audit_claim**: Audit claims against evidence, provenance, and epistemic class
2. **repair_allocation.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
3. **repair_allocation.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
4. **repair_allocation.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
5. **repair_allocation.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
6. **repair_allocation.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
7. **repair_allocation.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
8. **repair_allocation.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/O/overlooked.md` (content_hash: eb91d778a79b4c6a) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/misc/D/Distinction–Mutation–Entropy–Repair.md` (content_hash: 551b49315372ac2d) (vault canon, SOURCE_CLAIM)

### Repair Allocation Optimizer

From Cosmo Brain Overlooked: Repair allocation optimizer as module #37 in R (Repair) category. From Distinction-Mutation-Entropy-Repair: Repair priority formula.

**Repair allocation equation** (AMOS_MODEL):
```
R = (repair_capacity × recovery_window) / (damage_rate + latency)
```
- R = repair feasibility, repair_capacity = available repair resources, recovery_window = time available for repair
- damage_rate = rate of ongoing damage, latency = repair latency

**Allocation optimization model**:
- **Repair capacity**: available resources for repair (people, compute, time)
- **Recovery window**: time available before damage becomes irreversible
- **Damage rate**: rate at which the system is degrading
- **Latency**: time from repair initiation to repair effect

**Optimization protocol**:
1. **Assess damage**: assess the damage rate and severity
2. **Estimate capacity**: estimate available repair capacity
3. **Calculate window**: calculate the recovery window
4. **Compute feasibility**: compute repair feasibility using the equation
5. **Allocate**: allocate repair resources to maximize feasibility
6. **Monitor**: monitor repair progress and adjust allocation

**Optimization laws**:
- `FEASIBILITY > 1` required for repair to succeed (capacity × window > damage × latency)
- `ALLOCATION != REPAIR`: allocation assigns resources; repair executes the work
- `OPTIMAL != PERFECT**: optimal allocation maximizes feasibility; it does not guarantee success

### Epistemic Boundary

Repair allocation optimization is an operational construct. It does not prove optimal allocation, that the equation is empirically validated, or that repair always succeeds.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and rela

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-repair-allocation-optimizer_MOC]]

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
- `amos-repair-allocation-optimizer-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-repair-allocation-optimizer
node_type: skill
path: 07_SKILLS/amos-repair-allocation-optimizer/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
