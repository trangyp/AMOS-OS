---
name: amos-ubi-bio-reasoning
description: Executes Unified Biological Intelligence (UBI) reasoning across the 4
  non-compensatory domains (NBI, NEI, SI, BEI). Use when evaluating physiological
  telemetry, cognitive load, autonomic vagal coherence, 40Hz multi-agent clock pacing,
  quadratic emergence (e = i^2), and substrate distress veto (tau < 0.2).
parent_skill: amos-c04-bio-neuro-master
domain: bio
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
tags:
- type/skill
- canon/skill
- domain/bio-neuro
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
---


# AMOS Unified Biological Intelligence (UBI) Reasoning Skill

## Identity

Origin architect: **Trang Phan**. Domain: bio. Parent: amos-c04-bio-neuro-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- When evaluating physiological telemetry, cognitive load, and autonomic vagal coherence
- When assessing 40Hz multi-agent clock pacing and quadratic emergence (e = i^2)
- When applying substrate distress veto (tau < 0.2) across NBI/NEI/SI/BEI domains
- When reasoning about non-compensatory biological intelligence constraints

This skill governs the execution of biological intelligence constraints, living-substrate primacy, and bio-adaptive runtime pacing across the AMOS OS cognitive architecture.

---

## Capabilities

- **nbi_assessment**: Neurobiological Intelligence — cognitive load assessment
- **nei_assessment**: Neuro-Emotional Intelligence — autonomic vagal coherence analysis
- **si_assessment**: Social Intelligence — team interaction telemetry analysis
- **bei_assessment**: Body-Element Intelligence — substrate distress evaluation
- **quadratic_emergence_check**: Verify emergence condition ($e = i^2$)
- **substrate_distress_veto**: Activate veto if $\tau_{\text{bio}} < 0.2$
- **clock_pacing_recommendation**: 40Hz multi-agent clock pacing

## 1. Core Mathematical Primitives

1. **Non-Compensatory Alignment Formulation:**
   $$i_{\text{UBI}} = (\text{NBI} \cdot \text{NEI} \cdot \text{SI} \cdot \text{BEI})^{1/4}$$
   * If any single domain drops to zero ($x_k \to 0$), total alignment collapses ($i_{\text{UBI}} \to 0$).

2. **Quadratic Emergence Scaling:**
   $$e = i_{\text{UBI}}^2$$
   * Direct governor for System 2 tree search depth in [`04_RUNTIME/06_EXECUTION/ADAPTIVE_COMPLEXITY_RUNTIME`](file:///Users/mac/Documents/AMOS_OS/04_RUNTIME/06_EXECUTION/ADAPTIVE_COMPLEXITY_RUNTIME.md).

3. **Thermodynamic Entropy Export:**
   $$\frac{dS}{dt} = \frac{d_i S}{dt} + \frac{d_e S}{dt}, \quad \text{where } \frac{d_e S}{dt} < 0$$
   * Actively purges cognitive drift and computational entropy to maintain non-positive system entropy ($\frac{dS}{dt} \le 0$).

4. **Absolute Substrate Distress Veto:**
   $$\tau_{\text{bio}} < \tau_{\text{crit}} = 0.2 \implies \text{HALT / PRE-EMPTIVE INTERRUPT}$$
   * Forces immediate system fallback to restorative ground state rest ($S_0$).

---

## 2. The 4 Biological Intelligence Domains

- **NBI (Neurobiological Intelligence):** Cortical load management, theta/gamma oscillatory phase locking, and working memory saturation prevention.
- **NEI (Neuroemotional Intelligence):** Autonomic vagal tone tracking (HRV RMSSD), sympathetic de-escalation, and Phép Trang semantic reframing.
- **SI (Somatic Intelligence):** Biotensegrity proprioception, fascial shear dynamics, and somatic ground anchoring.
- **BEI (Bioelectromagnetic Intelligence):** Cardiac-neural field coherence and 40Hz unified oscillatory system clock pacing.

---

## 3. Protocol & Execution Steps

1. **Telemetry Ingestion:** Sample real-time NBI, NEI, SI, and BEI vector inputs.
2. **Substrate Veto Check:** If $\tau_{\text{bio}} < 0.2$ or any domain $< 0.1$, halt execution, emit distress warning, and lock in rest mode ($S_0$).
3. **Emergence Throttling:** Calculate $i_{\text{UBI}}$ and scale permissible token budget and search tree depth according to $e = i^2$.
4. **Bio-Synchrony Cadence:** Adjust UI contrast and LLM generation latency via NeurosyncAI bi-directional pacing loops.
5. **RSCF Proof Emission:** Assemble signed proof capsule linking bio-telemetry to the causal state commit.

## Examples

- **Scenario**: User says "Am I cognitively overloaded right now?"
  - **Input**: Physiological telemetry (heart rate variability, pupil dilation)
  - **Output**: NBI cognitive load assessment, NEI autonomic vagal coherence, 40Hz clock pacing recommendation, substrate distress veto check ($\tau < 0.2$), tagged AMOS_MODEL

- **Scenario**: User says "Is this team's collective intelligence emerging?"
  - **Input**: Team interaction telemetry
  - **Output**: UBI 4-domain analysis (NBI/NEI/SI/BEI), quadratic emergence check ($e = i^2$), emergence throttling recommendation, RSCF proof capsule

## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Do not use

- For generic biological analysis outside UBI 4-domain framework
- To claim empirical validation of biological intelligence laws
- As a substitute for domain-specific medical or neuroscience evidence
- Outside biology/neuroscience domain reasoning
