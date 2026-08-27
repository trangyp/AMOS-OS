---
title: SKILL
type: skill
name: amos-adversarial-entropy-accountant
description: Adversarial Entropy Accountant — security and safety capability. Use when security analysis, safety verification, or adversarial defense. Use when amos-security-safety-master routes to this specialized capability.
parent_skill: amos-security-safety-master
domain: security
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-adversarial-entropy-accountant]
---


# Adversarial Entropy Accountant

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-security-safety-master`
- **Domain**: security
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Security and trust engine for Adversarial Entropy Accountant

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

- **adversarial_entropy.detect_adversary**: Detect adversarial activity: attacks, probes, and manipulation attempts
- **adversarial_entropy.quantify_entropy**: Quantify adversarial entropy: uncertainty, information leakage, and attack surface
- **adversarial_entropy.govern_trust**: Govern principal-trust relationships: delegation, revocation, and audit
- **adversarial_entropy.monitor_attack**: Monitor distributed attack composition: multi-stage, multi-vector threats
- **adversarial_entropy.replay_provenance**: Replay execution provenance: trace and verify every action for integrity

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 62451434613b51d8) for the full vault-sourced domain knowledge (8755 chars).
- **adversarial_entropy.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **adversarial_entropy.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **adversarial_entropy.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/O/overlooked.md` (content_hash: eb91d778a79b4c6a) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE.md` (content_hash: ff5575df755d7e25) (vault canon, SOURCE_CLAIM)

### Adversarial Entropy Accountant

From Cosmo Brain Overlooked: Adversarial Entropy Accounting as a new AMOS module. Repair cannot assume the system is honestly broken. Some failures are injected, hidden, delayed, or strategically shaped.

**Adversarial Entropy Accounting tracks**:
- **Accidental entropy**: entropy from normal system operation
- **Adversarial entropy**: entropy intentionally injected by an adversary
- **Latent poison**: delayed-activation corruption planted for future trigger
- **Coordinated distortion**: multiple distortions coordinated to appear independent
- **Delayed activation**: corruption that activates after a delay or trigger condition

**Key principle**: Repair cannot assume the system is honestly broken. Some failures are injected, hidden, delayed, or strategically shaped. This is deeper than normal repair.

**Accounting protocol**:
1. **Detect**: detect entropy type (accidental vs adversarial)
2. **Classify**: classify the adversarial entropy type (latent, coordinated, delayed)
3. **Trace**: trace the entropy to its source (accidental source vs adversarial source)
4. **Quantify**: quantify the entropy impact
5. **Repair**: repair with adversarial awareness (don't just fix the symptom; find the adversary)
6. **Record**: log with provenance and adversarial classification

**Accounting laws**:
- `ACCIDENTAL != ADVERSARIAL`: accidental entropy is from normal operation; adversarial entropy is injected
- `REPAIR != ADVERSARIAL_REPAIR`: normal repair fixes accidental entropy; adversarial repair also finds the adversary
- `LATENT != ACTIVE`: latent poison is not yet active; it must be detected before activation

### Epistemic Boundary

Adversarial entropy accounting is a security construct. It does not prove all adversarial entropy is detected, that the classification is always correct, or that the adversary is always found.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing

---
**Links:** [[07_SKILLS_MOC]]
