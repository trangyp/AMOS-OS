---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Urta Risk Tension Architecture
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

# URTA Risk Tension Architecture

Formal risk lattice evaluating dynamic tension and collapse probabilities ($P_{\text{collapse}}$). Classifies risks, resolves tensions between competing goals, and arbitrates when goals conflict.

________________________________________________________________________

## 1. Definition

URTA (Unified Risk-Tension Architecture) is the AMOS framework for:

- **Risk classification**: categorizing threats by type, severity, and reversibility
- **Tension identification**: detecting competing goals that create structural tension
- **Tension resolution**: arbitrating between competing goals using governance rules
- **Collapse probability**: estimating the likelihood of system-level failure from accumulated tension

$$P_{\text{collapse}} = f(\text{risk\_accumulation}, \text{tension\_density}, \text{mitigation\_coverage})$$

________________________________________________________________________

## 2. Purpose

Complex systems accumulate tensions from:
- Competing optimization objectives (speed vs. safety vs. completeness)
- Resource constraints (token budget, time, computational capacity)
- Irreversible commitments (deployments, promotions, authority grants)
- Uncertainty propagation (unresolved hypotheses compounding)

Without a structured risk-tension architecture, these tensions accumulate silently until system-level failure occurs. URTA makes tensions visible and governs their resolution.

________________________________________________________________________

## 3. Risk Classification

Risks are classified along three axes:

| Axis | Values | Description |
|------|--------|-------------|
| Reversibility | REVERSIBLE, IRREVERSIBLE | Can the consequence be undone? |
| Severity | NEGLIGIBLE, LOW, MEDIUM, HIGH, CRITICAL | What is the magnitude of impact? |
| Velocity | SLOW, MODERATE, FAST, INSTANTANEOUS | How quickly does the risk materialize? |

Risk priority matrix (simplified):

| Severity \ Reversibility | REVERSIBLE | IRREVERSIBLE |
|---|---|---|
| CRITICAL | HIGH priority | IMMEDIATE ESCALATION |
| HIGH | MEDIUM priority | HIGH priority |
| MEDIUM | LOW priority | MEDIUM priority |
| LOW | MONITOR | LOW priority |
| NEGLIGIBLE | ACCEPT | MONITOR |

IRREVERSIBLE + CRITICAL = mandatory control-plane escalation (M20: stronger governance for irreversible actions).

________________________________________________________________________

## 4. Tension Lattice

Tensions form a lattice $\mathcal{T} = (\text{Tensions}, \preceq_T)$ where:

$$T_1 \preceq_T T_2 \iff \text{resolution}(T_1) \text{ is a prerequisite for } \text{resolution}(T_2)$$

Common tension types:

| Tension Type | Example |
|---|---|
| Speed ↔ Safety | Fast deployment vs. thorough validation |
| Completeness ↔ Timeliness | Full analysis vs. deadline |
| Autonomy ↔ Control | Agent independence vs. governance |
| Local ↔ Global | Local optimization vs. system-wide coherence |
| Innovation ↔ Stability | New approaches vs. proven patterns |
| Confidence ↔ Caution | Strong claims vs. epistemic humility |

________________________________________________________________________

## 5. Tension Resolution Protocol

$$\text{Resolve}(T) = \text{Arbitrate}(\text{Classify}(T), \text{GovernanceRules}(T), \text{Stakes}(T))$$

Resolution steps:

1. **Classify** the tension type and severity
2. **Identify** affected goals and stakeholders
3. **Evaluate** governance rules applicable to this tension type
4. **Assess** stakes: irreversibility, severity, velocity
5. **Arbitrate**: apply the governing priority ordering:
   - INTEGRITY > COMPLETENESS > FLUENCY > SPEED > TOKEN SAVINGS
   - REVERSIBLE > IRREVERSIBLE (under uncertainty)
   - SAFETY > CONVENIENCE
6. **Document** the resolution and its provenance
7. **Monitor** for tension recurrence

________________________________________________________________________

## 6. Collapse Probability

$$P_{\text{collapse}} = 1 - \prod_{i=1}^{n} (1 - p_i \cdot m_i)$$

Where:
- $p_i$ = probability of risk event $i$ materializing
- $m_i$ = mitigation coverage for risk $i$ ($m_i = 1$ if fully mitigated, $m_i = 0$ if unmitigated)

High collapse probability triggers:
- $P_{\text{collapse}} > 0.3$: increased monitoring and targeted mitigation
- $P_{\text{collapse}} > 0.6$: active tension resolution and governance escalation
- $P_{\text{collapse}} > 0.8$: mandatory system-level review and possible rollback

________________________________________________________________________

## 7. Invariants

| Invariant | Statement |
|-----------|-----------|
| Tension visibility | $\forall T \in \text{active tensions} : T \text{ is documented}$ |
| Irreversible escalation | $\text{IRREVERSIBLE}(T) \wedge \text{SEVERITY}(T) \geq \text{HIGH} \Rightarrow \text{control-plane escalation}$ |
| Priority ordering | Resolution preserves $\text{INTEGRITY} > \text{COMPLETENESS} > \text{FLUENCY} > \text{SPEED}$ |
| No silent accumulation | Tensions must not accumulate without governance review |
| Resolution provenance | $\text{Resolve}(T) \Rightarrow \text{provenance recorded}$ |

________________________________________________________________________

## 8. Falsifiers

| Falsifier | Description |
|-----------|-------------|
| Unresolved critical tension | A CRITICAL tension exists without governance review |
| Silent accumulation | Tensions accumulate without monitoring or documentation |
| Priority violation | Resolution violates the INTEGRITY > COMPLETENESS > FLUENCY ordering |
| Irreversible without escalation | IRREVERSIBLE + CRITICAL tension resolved without control-plane |
| False mitigation | Mitigation claimed but $m_i$ is effectively 0 |

________________________________________________________________________

## 9. Integration

- **Master equations**: Emergence and entropy dynamics from [[01_CANON/02_UNIVERSE_CANON/KHUNG_TRANG_MASTER_EQUATIONS|KHUNG_TRANG_MASTER_EQUATIONS]] feed risk assessment.
- **Entropy repair**: High entropy states from [[01_CANON/02_UNIVERSE_CANON/KHUNG_TRANG_ENTROPY_REPAIR|entropy repair]] increase tension density.
- **Control-plane**: IRREVERSIBLE + CRITICAL tensions require control-plane authorization.
- **TPE**: [[01_CANON/02_UNIVERSE_CANON/TPE_PREDICTION_LAYER|TPE predictions]] inform collapse probability estimation.
- **Observer gap**: [[01_CANON/02_UNIVERSE_CANON/KHUNG_TRANG_OBSERVER_EXPERIENCE_GAP|Observer frame limitations]] contribute to risk uncertainty.
- **Rollback**: High collapse probability may trigger [[01_CANON/01_CORE_LAWS/ROLLBACK_AND_RECOVERY_BASINS|rollback]] to a valid basin.

________________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[01_CANON/02_UNIVERSE_CANON/02_UNIVERSE_CANON_MOC|02_UNIVERSE_CANON_MOC]] · [[01_CANON/02_UNIVERSE_CANON/URTA_RISK_TENSION_ARCHITECTURE|URTA_RISK_TENSION_ARCHITECTURE]] · [[01_CANON/02_UNIVERSE_CANON/TSS_7_CYCLE|TSS_7_CYCLE]]

**MOC:** [[01_CANON/02_UNIVERSE_CANON/02_UNIVERSE_CANON_MOC|02_UNIVERSE_CANON_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

________________________________________________________________________

RSCF-NODE
node_id: urta_risk_tension_architecture
node_type: universe_canon
path: 01_CANON/02_UNIVERSE_CANON/URTA_RISK_TENSION_ARCHITECTURE.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[01_CANON/02_UNIVERSE_CANON/02_UNIVERSE_CANON_MOC|02_UNIVERSE_CANON_MOC]]
- FEEDS_INTO: [[01_CANON/01_CORE_LAWS/ROLLBACK_AND_RECOVERY_BASINS|ROLLBACK_AND_RECOVERY_BASINS]]
- RELATED_TO: [[01_CANON/02_UNIVERSE_CANON/TPE_PREDICTION_LAYER|TPE_PREDICTION_LAYER]]
- RELATED_TO: [[01_CANON/02_UNIVERSE_CANON/KHUNG_TRANG_MASTER_EQUATIONS|KHUNG_TRANG_MASTER_EQUATIONS]]
