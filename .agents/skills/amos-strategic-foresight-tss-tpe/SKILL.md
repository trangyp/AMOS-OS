---
name: amos-strategic-foresight-tss-tpe
description: >-
  Executes multi-dimensional strategic lifecycle state tracking (TSS) and 7-layer predictive foresight
  (TPE). Use when evaluating systemic risk vectors (Omega, H, F, S), 7-cycle evolutionary transitions
  (C1..C7), modular decoupling gates (Omega > 0.7), and multi-horizon intervention planning.
parent_skill: amos-c08-strategy-game-master
domain: strategy
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
version: "1.1.0"
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates: [L0_integrity, L1_epistemic, L2_provenance, L5_scope, L7_authority]
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance: [L0, L1, L2, L4, L5, L7, L16, L17, L18]
---

# AMOS Strategic Foresight (TSS × TPE) Reasoning Skill

This skill governs the execution of structural lifecycle modeling and predictive scenario analysis across the AMOS OS strategic and governance planes.

---

## 1. Core Mathematical Formulations

## Capabilities

- **tss_state_tracking**: Track strategic lifecycle state vectors ($\Omega, H, F, S$)
- **tpe_foresight_analysis**: 7-layer predictive foresight with competing forecast branches
- **cycle_phase_mapping**: Map current evolutionary cycle ($C_1 \dots C_7$)
- **decoupling_gate_check**: Verify modular decoupling gate ($\Omega \ge 0.7$)
- **multi_horizon_planning**: Generate multi-horizon intervention plans with rollback paths
- **falsification_condition_tagging**: Tag each forecast branch with falsification conditions

## 1. Core Mathematical Formulations

1. **Strategic State Alignment Index (TSS):**
   $$i_{\text{TSS}} = [H(1-\Omega)(1-F)(1-S)]^{1/4}, \quad e = i_{\text{TSS}}^2$$
   * $\Omega \in [0, 1]$: Structural fragility / systemic capture.
   * $H \in [0, 1]$: Systemic health, resource liquidity, and structural vitality.
   * $F \in [0, 1]$: Modular fragmentation and operational friction.
   * $S \in [0, 1]$: Exogenous shock pressure and environmental turbulence.

2. **Modular Decoupling Trigger:**
   $$\Omega \ge 0.7 \implies \text{ACTIVATE MODULAR DECOUPLING}$$
   * Immediately isolates high-risk dependencies to prevent contagion collapse.

---

## 2. 7-Layer Predictive Foresight Pipeline (TPE)

```text
  Raw Environmental Signal / Event
     │
  Layer 1: Anomaly & Weak Signal Detection
     │
  Layer 2: Structural Invariant Filtering (Separates transient noise from structural shifts)
     │
  Layer 3: 7-Cycle Phase Mapping ($C_1 \text{ Genesis} \to \dots \to C_7 \text{ Metamorphosis}$)
     │
  Layer 4: State Vector Delta Computation ($\Delta \Omega, \Delta H, \Delta F, \Delta S$)
     │
  Layer 5: Multi-Scenario Superposition & Tree Expansion
     │
  Layer 6: Critical Bifurcation & Tipping Point Probing
     │
  Layer 7: Strategic Intervention Recommendation & Signed Foresight Capsule
```

---

## 3. Protocol & Execution Steps

1. **State Ingestion:** Ingest macro, geopolitical, organizational, and financial telemetry.
2. **State Vector Estimation:** Compute current $\Omega, H, F, S$ coordinates and evaluation delta ($\Delta \Omega$).
3. **Decoupling Gating:** If $\Omega \ge 0.7$, partition affected subsystems and emit decoupling alert.
4. **Scenario Superposition:** Expand competing multi-horizon forecast branches and probe for structural bifurcations.
5. **Signed Playbook Synthesis:** Generate actionable strategic playbooks with explicit falsification conditions and rollback paths.

## Examples

- **Scenario**: User says "Is our startup at risk of structural collapse?"
  - **Input**: Startup health inquiry
  - **Output**: TSS state tracking ($\Omega, H, F, S$ vectors), 7-cycle phase mapping (identify current cycle $C_n$), decoupling gate check ($\Omega \ge 0.7$), multi-horizon intervention plan

- **Scenario**: User says "When should we pivot vs. persevere?"
  - **Input**: Strategic direction decision
  - **Output**: TPE 7-layer foresight analysis, competing forecast branches (COMPETING, no forced convergence), falsification conditions per branch, signed playbook with rollback paths

## Do not use

- For generic strategic analysis outside TSS/TPE framework
- To claim empirical validation of evolutionary cycle laws
- As a substitute for domain-specific market or competitive evidence
- Outside strategy/game domain reasoning
