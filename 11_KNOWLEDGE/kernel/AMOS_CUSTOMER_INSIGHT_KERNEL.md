---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Customer Insight Kernel
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

# AMOS Customer Insight Kernel

> [!abstract] Kernel Specification
> Defines the customer insight framework for AMOS: segmentation methodology, persona modeling, needs-mapping, Ideal Customer Profile (ICP) definition, and buying-center analysis. This is the AMOS reasoning/spec pattern for customer understanding — **not** a claim that AMOS OS executes live customer analytics (per AGENTS.md invariant 4).

> [!warning] Source Reconstitution
> This kernel was originally a GAP (auto-parse failed). Content has been reconstructed from cross-references in AMOS_UNIVERSE_OS_vInfinity P7_domain_engines, the Marketing GTM Kernel (customer_segmentation, ICP, persona/buying_center clusters), Product Strategy Kernel (customer_segments, persona_system), and Sales Kernel (discovery, stakeholder_mapping). All claims are `SOURCE_CLAIM`/`DERIVED` until validated against original source material.

---

## 1. Purpose

The Customer Insight Kernel provides:

- A structured methodology for customer segmentation
- Persona modeling for target customer archetypes
- Needs-mapping to align value propositions with customer pains/gains
- Ideal Customer Profile (ICP) definition for acquisition targeting
- Buying-center analysis for complex B2B sales

This kernel feeds data to [[11_KNOWLEDGE/kernel/AMOS_BUSINESS_MODEL_KERNEL|AMOS_BUSINESS_MODEL_KERNEL]] (customer segments block), [[11_KNOWLEDGE/kernel/AMOS_REVENUE_ARCHITECTURE_KERNEL|AMOS_REVENUE_ARCHITECTURE_KERNEL]] (segment-specific revenue modeling), and [[11_KNOWLEDGE/kernel/AMOS_PRICING_STRATEGY_KERNEL|AMOS_PRICING_STRATEGY_KERNEL]] (willingness-to-pay by segment).

---

## 2. Segmentation Framework

### 2.1 Segmentation Dimensions

| Dimension | Description | Data Source |
| :--- | :--- | :--- |
| **Firmographic** | Company size, industry, geography, revenue | CRM, public data |
| **Behavioral** | Usage patterns, feature adoption, engagement | Product analytics |
| **Psychographic** | Values, attitudes, risk tolerance | Surveys, interviews |
| **Needs-based** | Problems to solve, jobs to be done | Customer discovery |
| **Technographic** | Technology stack, maturity, adoption stage | Sales intelligence |

### 2.2 Segment Evaluation

Each segment $S_j$ is evaluated on:

$$\text{Score}(S_j) = w_1 \cdot \text{Market Size}(S_j) + w_2 \cdot \text{Accessibility}(S_j) + w_3 \cdot \text{Profitability}(S_j) + w_4 \cdot \text{Strategic Fit}(S_j)$$

where weights $w_1 + w_2 + w_3 + w_4 = 1$ reflect organizational priorities.

### 2.3 Segment Viability Criteria

A segment is viable when:

$$\text{Market Size}(S_j) \geq \text{Minimum Threshold} \quad \land \quad \text{Profitability}(S_j) \geq \tau_{profit} \quad \land \quad \text{Competitive Position}(S_j) > 0$$

Segments failing viability criteria are deprioritized or eliminated from the target portfolio.

---

## 3. Persona Modeling

### 3.1 Persona Structure

A persona $P$ is defined as:

$$P = (\text{Role}, \text{Context}, \text{Goals}, \text{Pains}, \text{InfoSources}, \text{DecisionProcess})$$

| Field | Description |
| :--- | :--- |
| **Role** | Job title, responsibilities, authority level |
| **Context** | Organizational environment, constraints, culture |
| **Goals** | What the persona is trying to achieve (functional, emotional, social) |
| **Pains** | Obstacles, frustrations, risks faced |
| **InfoSources** | Where they learn, research, seek validation |
| **DecisionProcess** | How they evaluate, decide, and implement |

### 3.2 Persona Prioritization

Personas are prioritized by:

1. **Revenue potential**: Expected LTV from persona's segment
2. **Acquisition feasibility**: CAC to reach and convert persona
3. **Strategic alignment**: Fit with product roadmap and capabilities
4. **Accessibility**: Availability of channels to reach persona

### 3.3 Buying Center Analysis

For B2B personas, the buying center includes:

| Role | Function | Engagement Strategy |
| :--- | :--- | :--- |
| **Champion** | Internal advocate; drives the process | Empower with ROI tools and business case |
| **Decision Maker** | Final authority to approve | Executive-level value proposition |
| **Influencer** | Technical or domain expert; shapes opinion | Technical proof, demos, POCs |
| **Gatekeeper** | Controls information flow and access | Compliance documentation, security reviews |
| **End User** | Actually uses the product | UX-driven demos, training |
| **Blocker** | Has veto power or active resistance | Address concerns directly; find workarounds |

---

## 4. Ideal Customer Profile (ICP)

### 4.1 ICP Definition

An ICP $I$ is a composite of attributes that predict high-value engagement:

$$I = (\text{Firmographic Range}, \text{Behavioral Threshold}, \text{Need Alignment}, \text{Budget Range})$$

| Attribute | Specification |
| :--- | :--- |
| **Firmographic Range** | Company size $[n_{min}, n_{max}]$, industries, geographies |
| **Behavioral Threshold** | Minimum usage frequency, feature adoption rate |
| **Need Alignment** | Score of problem-solution fit (see AMOS_BUSINESS_MODEL_KERNEL §3.2) |
| **Budget Range** | Expected budget $[B_{min}, B_{max}]$ for the problem category |

### 4.2 ICP Scoring

Each prospect is scored against the ICP:

$$\text{ICP Score}(q) = \frac{\sum_{k=1}^{m} w_k \cdot \text{Match}_k(q, I)}{\sum_{k=1}^{m} w_k}$$

where $\text{Match}_k(q, I) \in [0, 1]$ measures how well prospect $q$ matches attribute $k$ of ICP $I$.

Prospects with $\text{ICP Score} \geq \tau_{icp}$ are prioritized for acquisition.

---

## 5. Needs Mapping

### 5.1 Jobs-to-Be-Done Framework

| Job Type | Description | Example |
| :--- | :--- | :--- |
| **Functional** | Practical task to accomplish | "Reduce report generation time" |
| **Emotional** | How they want to feel | "Feel confident in data accuracy" |
| **Social** | How they want to be perceived | "Be seen as a data-driven leader" |

### 5.2 Pain-Gain Mapping

Each customer job $J_k$ is mapped to:

- **Pains** $\{p_{k1}, \ldots, p_{ka}\}$: Obstacles or negative outcomes when $J_k$ is performed poorly
- **Gains** $\{g_{k1}, \ldots, g_{kb}\}$: Desired outcomes when $J_k$ is performed well

The value proposition is validated when pain relievers and gain creators覆盖 the mapped pains and gains (see [[11_KNOWLEDGE/kernel/AMOS_BUSINESS_MODEL_KERNEL|AMOS_BUSINESS_MODEL_KERNEL]] §3.2).

### 5.3 Needs Prioritization

Needs are prioritized by:

$$\text{Priority}(n) = \text{Frequency}(n) \times \text{Severity}(n) \times \text{Willingness-to-Pay}(n)$$

High-priority needs receive focused product development and marketing attention.

---

## 6. Data Collection Methods

| Method | What It Captures | When to Use |
| :--- | :--- | :--- |
| **Customer Interviews** | Deep qualitative insights | Early discovery; persona validation |
| **Surveys** | Quantitative validation at scale | Segment sizing; needs ranking |
| **Product Analytics** | Behavioral patterns | Usage-based segmentation; activation |
| **Win/Loss Analysis** | Decision factors | ICP refinement; competitive positioning |
| **Social Listening** | Unfiltered sentiment | Pain discovery; trend identification |
| **Support Tickets** | Pain points and friction | Product improvement; churn prevention |

---

## 7. Failure Modes

| Failure | Detection | Recovery |
| :--- | :--- | :--- |
| Stale persona | Persona doesn't match recent customer data | Refresh with new interviews and data |
| Over-segmentation | Segments too small to be actionable | Consolidate similar segments |
| ICP drift | ICP score doesn't predict high-value customers | Recalibrate ICP attributes and weights |
| Buying-center gap | Key stakeholder role not addressed in sales process | Map complete buying center before engagement |
| Needs misalignment | Value proposition doesn't address top-priority needs | Revisit needs mapping; adjust value proposition |

---

## 8. Integration Points

| Interface | Direction | Contract |
| :--- | :--- | :--- |
| [[11_KNOWLEDGE/kernel/AMOS_BUSINESS_MODEL_KERNEL\|AMOS_BUSINESS_MODEL_KERNEL]] | Write | Customer segments populate canvas; needs map validates value proposition |
| [[11_KNOWLEDGE/kernel/AMOS_REVENUE_ARCHITECTURE_KERNEL\|AMOS_REVENUE_ARCHITECTURE_KERNEL]] | Write | Segment data feeds cohort-based revenue modeling |
| [[11_KNOWLEDGE/kernel/AMOS_PRICING_STRATEGY_KERNEL\|AMOS_PRICING_STRATEGY_KERNEL]] | Read/Write | Willingness-to-pay data informs pricing; pricing affects segment viability |
| [[11_KNOWLEDGE/kernel/AMOS_PARTNERSHIPS_CHANNELS_KERNEL\|AMOS_PARTNERSHIPS_CHANNELS_KERNEL]] | Read | Channel preferences inform distribution strategy |
| [[11_KNOWLEDGE/kernel/AMOS_SIMULATION_KERNEL\|AMOS_SIMULATION_KERNEL]] | Write | Customer models used in market simulation |

---

```RSCF-NODE
node_id: customer_insight_kernel_knowledge_spec
node_type: kernel_specification
domain: 11_KNOWLEDGE/kernel
claim_class: AMOS_MODEL
confidence_ceiling:
  segmentation_methodology: medium
  persona_modeling: medium
  icp_definition: medium
  needs_mapping: high
falsifiers:
  - Persona not validated with real customer data
  - ICP score does not predict actual high-value customers
  - Buying center analysis missing key stakeholder role
```

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/kernel/AMOS_BUSINESS_MODEL_KERNEL|AMOS_BUSINESS_MODEL_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_REVENUE_ARCHITECTURE_KERNEL|AMOS_REVENUE_ARCHITECTURE_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_PRICING_STRATEGY_KERNEL|AMOS_PRICING_STRATEGY_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_PARTNERSHIPS_CHANNELS_KERNEL|AMOS_PARTNERSHIPS_CHANNELS_KERNEL]]

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/kernel/KERNEL_MOC|KERNEL_MOC]]
