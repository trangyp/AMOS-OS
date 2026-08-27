---
title: SKILL
type: skill
name: amos-os-kernel
description: Os Kernel — runtime and OS capability. Use when runtime reasoning, OS kernel operations, or adaptive stability. Use when amos-os-runtime-master routes to this specialized capability.
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-os-kernel]
---


# Os Kernel

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-os-runtime-master`
- **Domain**: runtime
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Runtime and OS engine for Os Kernel

## When to Use

- When monitoring runtime stability: drift, oscillation, divergence
- When calibrating feedback control loops for stable operation
- When decomposing complex operations into primitive steps
- When enforcing closed-loop learning and drift alignment
- When the parent skill (`amos-os-runtime-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **os.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
- **os.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
- **os.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
- **os.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
- **os.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration
- **os.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **os.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **os.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: fdd6514d733facae) for the full vault-sourced domain knowledge (7991 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/0/00_AMOS_Full_Brain_OS_Architecture.md` (content_hash: b7acbb430dff829e) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### OS Kernel

From Cosmo Brain Full Brain OS Architecture: AMOS OS Kernel v4.4 with typed state, RSCF, provenance, repair, audit.

**OS Kernel v4.4 position in architecture**:
```
COGNITIVE SYNTHESIS -> OS KERNEL v4.4 -> INFRASTRUCTURE CONTROL PLANE -> HOST/LLM
```

**OS Kernel v4.4 responsibilities**:
- **Typed state**: all state is typed with epistemic class
- **RSCF**: claim/class/premises/evidence/provenance/scope/regime/freshness/falsifiers
- **Provenance**: full provenance chain for every state transition
- **Repair**: repair failed state transitions with rollback
- **Audit**: audit all state transitions before finalization

**10-step runtime pipeline**: Perceive -> Route -> Admit -> Plan -> Schedule -> Execute -> Observe -> Repair -> Audit -> Finalize

**AMOS RUNTIME system**: OS Kernel, RSCF, H/M/L, provenance, memory, competing hypotheses, firewalls, repair/replay/audit

**Kernel laws**:
- `KERNEL != ENGINE`: the kernel coordinates; engines execute
- `STATE != FACT`: typed state is a claim with epistemic class; it is not a fact
- `REPAIR != IMPROVEMENT`: repair fixes a specific issue; it does not improve the system

### Epistemic Boundary

OS Kernel is a runtime architecture. It does not prove all state is typed, that the pipeline is optimal, or that repair always succeeds.

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
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and epistemic class.
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **G6 (Failure mode)**: On v

---
**Links:** [[07_SKILLS_MOC]]
