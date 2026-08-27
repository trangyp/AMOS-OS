---
title: SKILL
type: skill
name: amos-runtime-benchmarking
description: Runtime Benchmarking — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-runtime-benchmarking]
---


# Runtime Benchmarking

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Runtime Benchmarking

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
