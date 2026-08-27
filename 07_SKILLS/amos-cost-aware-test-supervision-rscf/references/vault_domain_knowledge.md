---
title: vault domain knowledge
type: reference
source: 07_SKILLS/amos-cost-aware-test-supervision-rscf/references
tags: [reference, amos-cost-aware-test-supervision-rscf, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-cost-aware-test-supervision-rscf`

## Vault-Sourced Content

### Source 1: AMOS_Qa_Testing_Kernel_v0_Tech

> Path: `kernel/A/AMOS_Qa_Testing_Kernel_v0_Tech.md` | Size: 2524 chars | Match score: 13

{
  "meta": {
    "name": "QA_Testing_Kernel",
    "version": "1.0.0",
    "description": "Kernel for quality assurance and testing: test strategy, test design, automation, and quality metrics."
  },
  "kernel": {
    "description": "Supports quality assurance activities: test planning, test design, test automation, quality metrics, and defect management.",
    "functions": {
      "test_strategy": {
        "description": "Define testing strategy and scope.",
        "inputs": [
          "product_architecture",
          "risk_assessment",
          "quality_goals",
          "resource_constraints"
        ],
        "outputs": [
          "test_strategy_document",
          "test_scope",
          "risk_based_priorities"
        ]
      },
      "test_design": {
        "description": "Design test cases and test data.",
        "inputs": [
          "requirements",
          "user_stories",
          "system_diagrams",
          "edge_case_catalog"
        ],
        "outputs": [
          "test_case_catalog",
          "test_data_sets",
          "coverage_matrix"
        ]
      },
      "test_automation": {
        "description": "Automate test execution.",
        "inputs": [
          "test_cases",
          "target_stack",
          "ci_pipeline",
          "automation_frameworks"
        ],
        "outputs": [
          "automated_tests",
          "test_scripts",
          "execution_reports"
        ]
      },
      "quality_metrics": {
        "description": "Track and report quality metrics.",
        "inputs": [
          "test_results",
          "defect_data",
          "code_coverage",
          "performance_metrics"
        ],
        "outputs": [
          "quality_dashboard",
          "quality_trends",
          "quality_gate_status"
        ]
      }
    },
    "capabilities": {
      "testing_levels": "Unit, integration, E2E, performance, security, accessibility.",
      "test_design_techniques": "Equivalence partitioning, boundary value, decision tables, state transitions.",
      "defect_management": "Defect tracking, severity classification, root cause analysis.",
      "quality_gates": "Automated quality checks at each stage of development."
    }
  }
}

---

---

### Source 2: AMOS Infrastructure Layer — Test, Fix, Rerun & Architecture Enhancement

> Path: `amos-general/A/Infrastructure/AMOS_INFRASTRUCTURE_TEST_FIX_RERUN_ARCHITECTURE.md` | Size: 13473 chars | Match score: 10

# AMOS Infrastructure Layer — Test, Fix, Rerun & Architecture Enhancement


---

## 1. Executive Conclusion

AMOS is treated as the infrastructure and governance layer above cognition and domain execution.

The validated authority structure is:


Full Brain OS may reason, decompose, route, synthesize, and propose actions. It does **not** own durable-state commit authority, provenance admission, authorization freshness, observability finality, transaction semantics, rollback/finality, or external-effect release.

The executable AMOS_CORE v4.4 artifact was tested, repaired at the smallest causal boundary, and rerun with expanded adversarial coverage.

---

## 2. Baseline Findings

The initial executable baseline exposed four load-bearing infrastructure defects.

### 2.1 Runtime identity drift

The composed v4.4 artifact reported an older internal version identity:

`3.8.0-iterative-provenance-runtime`

This violated runtime identity and lineage consistency.

### 2.2 Durable effects could enter FAST_FINAL

`fast_finalize(..., durable_local=True)` accepted a durability flag but did not enforce it.

A durable effect could therefore incorrectly use proof-based local fast finalization instead of escalating to the infrastructure release boundary.

### 2.3 Commit survived ownership revocation

A fast permit issued during prepare could still commit after ownership/authority conditions changed.

This meant prepare-time validity was being treated as durable commit-time authority.

### 2.4 Commit survived consequence escalation

A permit could also remain valid after consequence risk rose beyond the fast-lane threshold.

This violated freshness and commit-time revalidation.

---

## 3. Root Cause

The defects shared one causal target:

> **Prepare-time proof was being treated as commit-time authority.**

The repair therefore avoided four unrelated patches and instead introduced a single infrastructure invariant:

## PREPARE_PERMIT != COMMIT_AUTHORITY

Any fast-lane decision must be revalidated immediately before publication or durable state transition.

---

## 4. Repair Applied

The repaired v4.4 runtime now enforces:

- Correct composed runtime identity:
- `4.4.0-proof-coordination-avoidance`
- Durable effects are excluded from local proof-based fast finalization.
- Commit-time fast-lane freshness is rechecked.
- Ownership must still be valid.
- Target state/CAS assumptions must still be valid.
- Consequence level must still satisfy fast-lane limits.
- Reversibility assumptions must still hold.
- Conflict probability must still remain below the accepted threshold.
- Transaction identity must remain stable and non-equivocating.

Fast-lane eligibility is now a **fresh commit-time predicate**, not a reusable permit token.

---

## 5. Test → Fix → Rerun Evidence

### Baseline


Failures:

1. Runtime identity mismatch.
2. Durable effect incorrectly entered FAST_FINAL.

Expanded adversarial testing then exposed:

3. Owner revocation not revalidated.
4. Conseque

---

### Source 3: AMOS Infrastructure Layer — Agent Architecture Test / Fix / Rerun Record

> Path: `amos-general/A/Infrastructure/AMOS_Infrastructure_Agent_Architecture_Test_Fix_Rerun_2026-08-25.md` | Size: 11654 chars | Match score: 10

# AMOS Infrastructure Layer — Agent Architecture Test / Fix / Rerun Record


---

## 1. Architecture Boundary

AMOS is treated as the infrastructure/control plane above the cognitive and domain layers:

```text
User / System Authority
        ↓
AMOS Infrastructure / Control Plane
        ↓
AMOS Full Brain OS
        ↓
Specialist Agents / Skills
        ↓
Tools / External Effect Executors
```

Full Brain OS and specialist agents may:

- reason;
- plan;
- retrieve;
- synthesize;
- stage proposals;
- create candidate evidence;
- request effects.

They do **not** independently own:

- durable commit authority;
- canon admission;
- final authorization;
- release/finality;
- authority issuance;
- irreversible effect approval.

Those remain infrastructure responsibilities.

---

## 2. Governing AMOS Contracts

The infrastructure layer should own or validate at minimum:

- `TASK_CONTRACT`
- `AUTHORITY_WITNESS`
- `OBSERVABILITY_ENVELOPE`
- `EVIDENCE_BUNDLE`
- `OBSERVED_READ_SET`
- `EFFECT_INTENT`
- `PROVENANCE_CAPSULE`
- `RSCF_STATE`
- `COMMIT_RESULT`
- rollback / recovery state
- validation epoch / freshness state

Core rule:

```text
Capability != Authority
Proposal != Admission
Execution != Commit
Structural consistency != Empirical validity
```

---

## 3. GitHub Defect Found

Repository:

```text
trangyp/AMOS-SYSTEM
```

A concrete constructor-contract defect was identified in the agent layer.

Several repository-aware agents called:

```python
super().__init__(name, repo_root)
```

while the shared base `Agent` constructor accepted only:

```python
Agent(name)
```

This could cause agent construction and registry initialization to fail before orchestration begins.

---

## 4. First Repair

The base agent contract was changed conceptually to:

```python
Agent(name, repo_root=None)
```

This preserves compatibility with name-only agents while supporting repository-aware agents.

Focused regression coverage was added for:

- `CodeAgent`
- `PlannerAgent`
- `RefactorAgent`
- `RepairAgent`
- `ResearchAgent`
- `DefaultAgent`

A local focused contract rerun previously produced:

```text
1 passed
```

That result is scoped only to the focused constructor contract.

---

## 5. Stale-Branch Detection

The first repair branch was later found to have diverged from `main`:

```text
ahead: 4 commits
behind: 5 commits
```

The repair was therefore **not** promoted from the stale branch.

A fresh branch was created from current `main`:

```text
amos-infra-architecture-20260824-v2
```

This preserved the repair while avoiding stale-state promotion.

---

## 6. ResearchAgent Governance Repair

The original `ResearchAgent` behavior treated external inputs too optimistically.

It could report external material as:

```text
processed
mapped to canon
```

without a separate evidence-admission or control-plane decision.

This violates the intended AMOS infrastructure boundary.

The hardened behavior now treats research outputs as candidate evidence.

Required semantics:

`

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
