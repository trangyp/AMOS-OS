---
schema_version: 1.0
title: SKILL — Amos Benchmark Forensics
type: skill
source: 07_SKILLS/amos-benchmark-forensics
name: amos-benchmark-forensics
description: Benchmark Forensics — audit and repair capability. Use when auditing,
  failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master
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
license: MIT
steward: Trang Phan
---

# Benchmark Forensics

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

- **benchmark_forensics.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **benchmark_forensics.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **benchmark_forensics.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **benchmark_forensics.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **benchmark_forensics.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
- **benchmark_forensics.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **benchmark_forensics.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **benchmark_forensics.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **benchmark_forensics.audit_claim**: Audit claims against evidence, provenance, and epistemic class
2. **benchmark_forensics.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
3. **benchmark_forensics.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
4. **benchmark_forensics.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
5. **benchmark_forensics.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
6. **benchmark_forensics.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
7. **benchmark_forensics.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
8. **benchmark_forensics.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE.md` (content_hash: f23d35766fe766bc) (vault canon, SOURCE_CLAIM)

### Benchmark Forensics

From Cognitive Organism OS: Runtime benchmarking with integrity checks. From C10: Engineering QA.

**Benchmark forensics model**:
- **Benchmark integrity**: verify that benchmarks are run correctly and results are not manipulated
- **Result provenance**: trace benchmark results to their execution context
- **Regression detection**: detect when performance regresses from baseline
- **Anomaly detection**: detect anomalous benchmark results that may indicate fraud or error

**Forensic protocol**:
1. **Collect**: collect benchmark results with full provenance (execution context, inputs, outputs, timestamps)
2. **Verify**: verify benchmark execution was correct (no shortcuts, no caching, no special inputs)
3. **Compare**: compare results against baseline and previous runs
4. **Detect**: detect anomalies, regressions, and suspicious patterns
5. **Report**: report findings with confidence and provenance

**Benchmark law**: `BENCHMARK_PASS != PRODUCTION_READY`. A benchmark pass is necessary but not sufficient for production deployment.

**Forensic law**: `RESULT != TRUTH`. A benchmark result is an observation, not a truth claim. Results must be independently verified.

### Epistemic Boundary

Benchmark forensics is an engineering quality construct. It does not prove all fraud is detected, that benchmarks are comprehensive, or that results are always reliable.

## Focus
- transaction IDs
- read/write sets
- transaction-level CAS
- atomic publication
- cross-RSCF invariants
- all-or-nothing rollback

## Markdown brain adaptation
Treat cross-RSCF update sets atomically: all-or-nothing.

## Historical gap
Distributed transaction finality under partition and competing certified transactions.

## Benchmark boundary
```json
{
  "status": "passed_transactional_multi_RSCF_suite",
  "results": {
    "overlapping_transaction_trials": 2000,
    "partial_mixed_states": 0,
    "schedule_dependent_final_states": 0,
    "atomicity_violations": 0,
    "write_skew_violations_accepted": 0,
    "forced_partial_failure_rollback": "passed",
    "transaction_sizes_passed": [
      3,
      10,
      100,
      1000
    ],
    "historical_snapshot_readers": "passed"
  }
}
```

Benchmark results are preserved only within their tested operationalization and are not universal guarantees.

---

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
-

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-benchmark-forensics_MOC]]

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

- `references/asymptotic_ceiling_analysis.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `` — skill Map of Content
- `amos-audit-repair-master` — parent skill
- `` — corresponding workflow
- `amos-benchmark-forensics-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-benchmark-forensics
node_type: skill
path: 07_SKILLS/amos-benchmark-forensics/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]

