---
title: SKILL
type: skill
name: amos-portable-agent-authorization-rscf
description: Portable Agent Authorization — agent systems capability. Use when agent design, delegation reasoning, or multi-agent governance. Use when amos-agent-systems-master routes to this specialized capability.
parent_skill: amos-agent-systems-master
domain: agent
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-portable-agent-authorization-rscf]
---


# Portable Agent Authorization Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-agent-systems-master`
- **Domain**: agent
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Agent systems engine for Portable Agent Authorization Rscf

## When to Use

- When governing agency: who acts, under what authority, consequences
- When designing agent externalization: delegation and controls
- When attributing agent ownership and responsibility
- When verifying delegation witness validity: temporal, revocable, attenuation-bound
- When checking enforcement trust contracts for agent authorization chains
- When the parent skill (`amos-agent-systems-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **portable_agent.govern_agency**: Govern agency: who acts, under what authority, with what consequences
- **portable_agent.design_externalization**: Design agent externalization: what is delegated, to whom, with what controls
- **portable_agent.attribute_ownership**: Attribute agent ownership: who is responsible for each agent action
- **portable_agent.verify_agentic**: Verify agentic skill-lie algebroid: structural consistency of agent capabilities
- **portable_agent.validate_delegation**: Validate delegation witness: temporal, revocable, attenuation-bound
- **portable_agent.detect_drift**: Detect drift in authorization chains, delegation validity, or trust contracts
- **portable_agent.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **portable_agent.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: Enforcement Trust Contract (v43) and Enforcement Root Attestation (v42) from AMOS brain production code (vault canon, SOURCE_CLAIM)

### Delegation Witness (v43)

Temporal, revocable, attenuation-bound delegation closing the zombie-agent problem:

- `ChildScope(t) ⊆ ParentScope(t)` — child scope must be subset of parent at all times
- `ChildLifetime ≤ ParentLifetime` — child cannot outlive parent
- `¬ParentEligible(t) ⇒ ChildEligible(t+Δ) = FALSE` — parent ineligibility propagates to child

### Enforcement Trust Contract (v43)

16-field contract binding authority to the entire enforcement chain:
- Control plane, policy artifact + signer + compiler, refmon, runtime/kernel
- Workload, egress guard, epochs, delegation parent + attenuation
- Independence root, agent-write exclusion, release ledger

**Hard rule**: An effect cannot become authoritative merely because AMOS approved it; AMOS must also establish the currently executing enforcement chain is the same trusted chain to which approval was issued.

### Separability Law (expanded v43)

`Capability ≠ Reachability ≠ Identity ≠ Authorization ≠ Delegation ≠ Observability ≠ Enforcement ≠ Finality ≠ Consequence`

Enforcement identity itself must be proven — not just the decision, but the mechanism enforcing it.

### MayExternalize_v43

`MayExternalize_v43 = v42 18-term ∧ EnforcementTrustContractValid ∧ DelegationWitnessValid` (20 terms total)

### Epistemic Boundary

Enforcement trust contracts are AMOS_MODEL validated through synthetic fuzz testing (300k deterministic fuzz, seed 202608232231). Synthetic fuzz proves logic correctness vs self-defined adversary, NOT universal security. "AMOS universally guarantees AI containment" = NOT ESTABLISHED. Hardware/root-of-trust compromise NOT ESTABLISHED.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond

---
**Links:** [[07_SKILLS_MOC]]
