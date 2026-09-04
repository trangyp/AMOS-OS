---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Epistemic Regime Canon
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Epistemic Regime Infrastructure Canon

> **Authoritative Canon Boundary**
>
> This document defines the canonical laws governing **Epistemic Regimes** and cross-regime translation boundaries within AMOS Core v4.4.
>
> ```text
> MATHEMATICAL PROOF != PHYSICAL ACTUALITY
> POLICY AUTHORIZATION != PHYSICAL POSSIBILITY
> EMPIRICAL MEASUREMENT != FORMAL AXIOM
> SIMULATION != PHYSICAL REALITY
> CROSS-REGIME TRANSLATION REQUIRES EXPLICIT LOSS ACCOUNTING
> ```

---

## 1. Architectural Purpose & Problem Statement

A frequent mode of catastrophic failure in AI and autonomous systems is **regime confusion**—treating a mathematical theorem as a guarantee of hardware performance, or treating policy compliance as proof of physical feasibility.

The **Epistemic Regime Canon** establishes that all truth claims, validations, and inferences in AMOS operate within bounded epistemic regimes. No claim validated under one regime may be imported into another regime without explicit translation rules and loss accounting.

---

## 2. The Five Canonical Epistemic Regimes

1. **Empirical / Physical Regime ($\mathcal{E}_{\text{physical}}$)**:
   - *Substrate*: Hardware telemetry, sensory observation, physical constants, clinical trials.
   - *Verification Criteria*: Sensor calibration, measurement uncertainty ($\pm \sigma$), statistical replication.
   - *Firewall*: $\text{Simulated Trace} \ne \text{Physical Measurement}$.
2. **Formal / Mathematical Regime ($\mathcal{E}_{\text{formal}}$)**:
   - *Substrate*: Axiomatic systems, type systems, proof checkers, discrete logic.
   - *Verification Criteria*: Deterministic deductive derivation, proof obligations discharged.
   - *Firewall*: $\text{Formal Consistency} \ne \text{Empirical Truth}$.
3. **Architectural / Model Regime ($\mathcal{E}_{\text{model}}$)**:
   - *Substrate*: System specifications, component designs, simulated state transitions.
   - *Verification Criteria*: Structural schema conformance, interface contracts.
   - *Firewall*: $\text{Documented Specification} \ne \text{Deployed Runtime}$.
4. **Normative / Governance Regime ($\mathcal{E}_{\text{normative}}$)**:
   - *Substrate*: Legal policies, ethical constraints, authority grants, access tokens.
   - *Verification Criteria*: Cryptographic lease validity, steward signatures, compliance audits.
   - *Firewall*: $\text{Authority Grant} \ne \text{Technical Feasibility}$.
5. **Experiential / Subjective Regime ($\mathcal{E}_{\text{subjective}}$)**:
   - *Substrate*: User intent, human verbal feedback, modeled emotional valence.
   - *Verification Criteria*: Self-consistency, explicit user ratification.
   - *Firewall*: $\text{User Preference} \ne \text{Objective Physical Law}$.

---

## 3. Canonical Laws of Epistemic Regimes

### Law ERC-01: Mandatory Regime Tagging
Every claim in an RSCF record must declare its operational regime (`regime: physical|formal|model|normative|subjective`).

### Law ERC-02: Cross-Regime Boundary Barrier
Direct unmediated inference across regime boundaries is strictly prohibited:
$$\mathcal{E}_A \cap \mathcal{E}_B = \emptyset \implies \text{DirectPromotion}(\text{Claim}_A \rightarrow \text{Claim}_B) == \text{ILLEGAL}$$

### Law ERC-03: Governed Cross-Regime Mapping
Cross-regime translation requires an explicit `RegimeMapping` object declaring:
1. Translation assumptions;
2. Information loss;
3. Falsification conditions;
4. Experimental or observational grounding.

---

## 4. Cross-Plane Bindings

- **`02_KERNEL`**: Enforces regime separation during proof evaluation.
- **`03_CONTROL_PLANE`**: Restricts normative authority grants from asserting empirical truth.
- **`16_SCHEMAS`**: Binds regime enums to all tensor and contract schemas.
- **`17_OBSERVABILITY`**: Tags all telemetry with origin regime.

---

```RSCF-NODE
node_id: amos_01_canon_04_infrastructure_canon_epistemic_regime_canon
node_type: infrastructure_canon
plane: 01_CANON
domain: INFRASTRUCTURE
claim_class: CANONICAL_LAW
status: ACTIVE_CANON
confidence_ceiling: ABSOLUTE_FOR_CANONICAL_LAW
falsifiers:
  - Importation of a formal mathematical proof as an empirical physical fact without measurement grounding.
  - State mutation committed across regime boundaries without declared translation loss.
```
