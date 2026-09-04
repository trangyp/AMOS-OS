---
title: "Operating Model Decision Rights Contract — Epistemic Authority Lattices & Quorum Specifications"
type: subplane_contract
plane: 23_OPERATING_MODEL
subplane: 02_DECISION_RIGHTS
domain: A_NORMATIVE_GOVERNANCE
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_SPECIFICATION
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 23_OPERATING_MODEL/OPERATING_MODEL_OPERATING_MODEL_CONTRACT
    - 23_OPERATING_MODEL/01_ROLES/OPERATING_MODEL_ROLES_CONTRACT
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
  scope: decision_rights_and_quorum_lattices
tags:
  - amos-os
  - 23-operating-model
  - decision-rights
  - authority-lattice
  - quorum-thresholds
  - consensus-mechanisms
---

# Operating Model Decision Rights Contract — Epistemic Authority Lattices & Quorum Specifications

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Domain Alignment:** Domain A (Normative & Governance Definition)  
> **Conclusion Class:** `DERIVED` (RSCF Validated)  
> **Status:** `ACTIVE_SPECIFICATION`

---

## 1. Architectural Scope & Subsystem Role

`23_OPERATING_MODEL/02_DECISION_RIGHTS` formalizes the epistemic authority levels, multi-agent quorum thresholds, and automated decision-gate criteria governing state mutations, architectural promotions, and risk approvals in AMOS OS.

```text
AUTHORITY != CAPABILITY
CONSENSUS != UNANIMITY
REVERSIBLE_DECISION != IRREVERSIBLE_COMMIT
LOCAL_OPTIMIZATION != GLOBAL_SYSTEM_STABILITY
```

---

## 2. Decision Impact Tiers & Required Quorum Matrix

Decisions within AMOS OS are strictly categorized into 4 impact tiers:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      DECISION AUTHORITY LATTICE                        │
├──────┬──────────────────────┬─────────────────────────┬────────────────┤
│ Tier │ Blast Radius         │ Required Quorum Gate    │ Time Horizon   │
├──────┼──────────────────────┼─────────────────────────┼────────────────┤
│ D0   │ Local Ephemeral Task │ 1 Execution Agent       │ < 10 ms        │
│ D1   │ Workspace State Edit │ 2-of-3 Analyst Quorum   │ < 1.0 s        │
│ D2   │ Subplane Spec Change │ Plane Lead + Coordinator│ < 60 s         │
│ D3   │ Canonical Law / Core │ Trang Phan (Steward)    │ Explicit Comm. │
└──────┴──────────────────────┴─────────────────────────┴────────────────┘
```

---

## 3. Mathematical Quorum Formulation

For Tier D1 and D2 multi-agent decisions, approval is given by the weighted consensus indicator $\Phi_{\text{decision}}$:

$$\Phi_{\text{decision}}(\mathcal{D}) = \mathbb{I}\left( \sum_{i \in \text{VotingAgents}} \omega_i \cdot \text{Vote}_i \ge \Theta_{\text{quorum}} \right) \wedge \left( \prod_{j \in \text{VetoAgents}} (1 - \text{Veto}_j) == 1 \right)$$

Where:
- $\omega_i \in [0, 1]$: Sybil-hardened epistemic weight of agent $i$.
- $\Theta_{\text{quorum}} = 0.67$ (Supermajority requirement).
- $\text{VetoAgents}$: Dedicated adversarial red-team agents endowed with hard fail-closed veto power.

---

## 4. Invariants & Guardrails

1. **Reversibility Principle (Two-Way Doors):** All Tier D0 and D1 decisions must support automated one-click rollback via MVCC state journals.
2. **One-Way Door Containment:** Tier D3 decisions (cryptographic key rotation, canonical law mutations, permanent archive deletion) are irreversibly bounded and require explicit human-in-the-loop authorization by **Trang Phan**.

---

## 5. Lineage & Cross-Plane References

- **Parent Contract:** [[23_OPERATING_MODEL/OPERATING_MODEL_OPERATING_MODEL_CONTRACT|OPERATING_MODEL_OPERATING_MODEL_CONTRACT]]
- **Roles Matrix:** [[23_OPERATING_MODEL/01_ROLES/OPERATING_MODEL_ROLES_CONTRACT|OPERATING_MODEL_ROLES_CONTRACT]]
- **Governance Forums:** [[23_OPERATING_MODEL/03_GOVERNANCE_FORUMS/OPERATING_MODEL_GOVERNANCE_FORUMS_CONTRACT|OPERATING_MODEL_GOVERNANCE_FORUMS_CONTRACT]]
- **Escalation Engine:** [[23_OPERATING_MODEL/04_ESCALATION/OPERATING_MODEL_ESCALATION_CONTRACT|OPERATING_MODEL_ESCALATION_CONTRACT]]

