---
title: SKILL
type: skill
name: amos-benchmark-forensics
description: Benchmark Forensics — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-benchmark-forensics]
---


# Benchmark Forensics

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Benchmark Forensics

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