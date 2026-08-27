---
title: SKILL
type: skill
name: amos-provenance-trust-firewall
description: Provenance Trust Firewall — security and safety capability. Use when security analysis, safety verification, or adversarial defense. Use when amos-security-safety-master routes to this specialized capability.
parent_skill: amos-security-safety-master
domain: security
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-provenance-trust-firewall]
---


# Provenance Trust Firewall

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-security-safety-master`
- **Domain**: security
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Security and trust engine for Provenance Trust Firewall

## When to Use

- When detecting adversarial activity: attacks, probes, manipulation
- When quantifying adversarial entropy and attack surface
- When governing principal-trust relationships: delegation, revocation
- When monitoring distributed attack composition: multi-stage threats
- When the parent skill (`amos-security-safety-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **provenance_trust.detect_adversary**: Detect adversarial activity: attacks, probes, and manipulation attempts
- **provenance_trust.quantify_entropy**: Quantify adversarial entropy: uncertainty, information leakage, and attack surface
- **provenance_trust.govern_trust**: Govern principal-trust relationships: delegation, revocation, and audit
- **provenance_trust.monitor_attack**: Monitor distributed attack composition: multi-stage, multi-vector threats
- **provenance_trust.replay_provenance**: Replay execution provenance: trace and verify every action for integrity
- **provenance_trust.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **provenance_trust.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **provenance_trust.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 737938b28246ae22) for the full vault-sourced domain knowledge (7602 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/dated/2026-08-22/2026-08-22 Cognitive Substrate Reality Gate.md` (content_hash: 2c93bdf31c3481c7) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Provenance Trust Firewall

From Cosmo Brain Cognitive Substrate Reality Gate: Prevents epistemic autopoisoning by requiring reality contact before any LLM-generated claim is promoted to durable memory.

**The problem**: Epistemic autopoisoning -- LLM generates X -> X stored -> X retrieved -> X treated as evidence -> X strengthened -> X stored again. Confidence rises with no new reality contact. The system becomes internally coherent and externally wrong.

**The gate**:
```
Promote(X) => RC(X) >= theta_RC AND IR(X) <= theta_IR
```
- `RC(X)` -- number/quality of independent external observations supporting X
- `IR(X)` -- fraction of support ultimately descending from AMOS-generated state
- Default thresholds: `theta_RC = 1.0`, `theta_IR = 0.5` (raise both for high-stakes claims)

**Memory I/O pipelines**:
- Write path: `Propose -> Type -> CheckEvidence -> CheckScope -> CheckProvenance -> Admit`
- Read path: `Retrieve -> Validate -> Contextualize -> Use`
- Failure at any stage quarantines the object; provenance is retained, nothing is silently deleted

**4 Key invariants**:
1. Claim strength must not exceed evidence strength (high confidence does not bypass the gate)
2. Repetition does not establish source independence (non-independent contacts are not double-counted)
3. Short internal-recursion paths raise IR and tighten the gate
4. Counterfactual repair: a quarantined object is rescued only by adding an independent external contact and re-running `promote()`

**Cognitive integrity formula**: `CognitiveIntegrity = ReasoningIntegrity ∧ MemoryIntegrity ∧ InterfaceIntegrity ∧ RealityContact`

### Epistemic Boundary

Provenance trust firewall is a security construct. It does not prove all autopoisoning is prevented, that thresholds are always correct, or that the gate cannot be bypassed.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation 