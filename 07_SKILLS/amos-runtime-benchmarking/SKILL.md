---
title: SKILL — Amos Runtime Benchmarking
type: skill
source: 07_SKILLS/amos-runtime-benchmarking
name: amos-runtime-benchmarking
description: Runtime Benchmarking — audit and repair capability. Use when auditing,
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
- capability/benchmarking
- capability/runtime
- capability/audit
- capability/repair
- rscf/epistemic
- rscf/S-state
- rscf/M-memory
- rscf/C-constraint
- rscf/P-repair
- rscf/type-evidence
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-runtime-benchmarking
rscf:
  state: DERIVED
  claim_class: EMPIRICAL
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







# Runtime Benchmarking

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

- **runtime_benchmarking.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **runtime_benchmarking.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **runtime_benchmarking.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **runtime_benchmarking.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **runtime_benchmarking.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 30f0e9656d608195) for the full vault-sourced domain knowledge (9562 chars).
- **runtime_benchmarking.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **runtime_benchmarking.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **runtime_benchmarking.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/B/benchmark-claims.md` (content_hash: 43b8a058f13bebf4) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Runtime Benchmarking

From Cosmo Brain Benchmark Firewall: Any performance, superiority, scaling, latency, throughput, repair, or compression claim requires full provenance.

**Required benchmark fields**: `benchmark_id, version, baseline, workload, harness, environment, raw_outputs, statistic, result, scope, limitations, provenance`

**4 Never rules**:
1. Never generalize beyond the tested scope
2. Never treat structural properties as measured performance
3. Never combine incomparable benchmark statistics
4. Never claim universal superiority from one component-level result

**Benchmarking protocol**:
1. **Declare**: declare benchmark ID, version, baseline, workload, harness, environment
2. **Run**: run the benchmark with declared configuration
3. **Record**: record raw outputs, statistics, results
4. **Scope**: declare scope and limitations
5. **Provenance**: record full provenance chain
6. **Report**: report with all required fields

**Benchmark law**: `BENCHMARK_PASS != PRODUCTION_READY`. A benchmark pass is necessary but not sufficient for production deployment. `RESULT != TRUTH`: a benchmark result is an observation, not a truth claim.

### Epistemic Boundary

Runtime benchmarking is an engineering quality construct. It does not prove all performance issues are detected, that benchmarks cover all cases, or that results generalize beyond tested scope.

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
- **G4 (Anti-overreach)**: No claim b

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-runtime-benchmarking_MOC]]

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
- `[[amos-runtime-benchmarking_MOC]]` — skill Map of Content
- `amos-audit-repair-master` — parent skill
- `[[amos-runtime-benchmarking-workflow]]` — corresponding workflow
- `amos-runtime-benchmarking-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-runtime-benchmarking
node_type: skill
path: 07_SKILLS/amos-runtime-benchmarking/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
