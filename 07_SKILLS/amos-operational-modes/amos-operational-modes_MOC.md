---
title: Operational Modes — MOC
type: moc
source: 07_SKILLS/amos-operational-modes
moc: true
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---
# Operational Modes — Map of Content

**Path:** `07_SKILLS/amos-operational-modes`

## Role

Three safety envelopes that constrain what an AMOS runtime is allowed to do based on risk, authority, capability, and environmental conditions:
- **SAFE_INTROSPECTION_ONLY** — read-only self-analysis, no external effects.
- **EXTERNAL_WRITE_LOW_RISK** — bounded, low-consequence external writes with receipts.
- **EXPERIMENTAL_BUILD** — higher-risk construction, requires explicit authority and rollback plan.

## When to Use

- Select the runtime safety envelope based on risk, authority, and capability envelope.
- A mutation or action requires a mode transition.
- A failure or anomaly forces a mode downgrade.
- An autonomous evolution step must be classified by allowed mode.

## Files

- [[07_SKILLS/amos-operational-modes/SKILL|Operational Modes SKILL]] — canonical skill definition
- [[07_SKILLS/amos-operational-modes/amos-operational-modes_MOC|Operational Modes MOC]] — this index

## Mode Hierarchy

| Mode | Allowed Effects | Authority Required | Failure Default |
|------|-----------------|--------------------|-----------------|
| `SAFE_INTROSPECTION_ONLY` | Self-read, audit, introspection | none beyond identity | remain in mode |
| `EXTERNAL_WRITE_LOW_RISK` | Bounded external writes with receipts | delegation witness | downgrade to safe |
| `EXPERIMENTAL_BUILD` | Construction, mutation, high-consequence writes | governance commit + rollback basin | fail-closed |

## Mode Transition Rules

- Upgrades require positive evidence: authority, verification, and valid delegation.
- Downgrades can be triggered by risk thresholds, violations, or user revocation.
- Mode transitions are logged and form part of the causal epoch.
- No `EXPERIMENTAL_BUILD` without a valid `DELEGATION_WITNESS` and `ENFORCEMENT_TRUST_CONTRACT`.

## Cross-Plane Bindings

- **Governance:** [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C01_GOVERNANCE/C01_GOVERNANCE_MOC|C01_GOVERNANCE_MOC]]
- **Kernel control:** [[25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C09_KERNEL_CONTROL/C09_KERNEL_CONTROL_MOC|C09_KERNEL_CONTROL_MOC]]
- **Runtime:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] · [[07_SKILLS/amos-os-runtime-master/amos-os-runtime-master_MOC|amos-os-runtime-master_MOC]]
- **Capability-bound governance:** [[07_SKILLS/amos-capability-bound-governance/SKILL|amos-capability-bound-governance]]
- **Delegation witness:** [[03_CONTROL_PLANE/04_AUTHORITY/DELEGATION_WITNESS|DELEGATION_WITNESS]]
- **Parent skill:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Governance Notes

- This skill is `AMOS_MODEL` / `DERIVED`.
- Executable closure is not established by this specification.
- All routed tasks must preserve RSCF epistemic boundaries.
- `MODE_CAPABILITY != MODE_AUTHORITY`.

## Parent

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
