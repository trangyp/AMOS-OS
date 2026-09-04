---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Business Model Kernel
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

# AMOS Business Model Kernel

> [!abstract] Kernel Specification
> Defines the business model analysis framework for AMOS: value proposition design, cost/revenue structure, unit economics, and business model canvas integration. This is the AMOS reasoning/spec pattern for business model evaluation — **not** a claim that AMOS OS executes business operations (per AGENTS.md invariant 4).

> [!warning] Source Reconstitution
> This kernel was originally a GAP (auto-parse failed). Content has been reconstructed from cross-references in AMOS_UNIVERSE_OS_vInfinity P7_domain_engines, related kernel clusters, and AMOS Business4 domain patterns. All claims are `SOURCE_CLAIM`/`DERIVED` until validated against original source material.

---

## 1. Purpose

The Business Model Kernel provides:

- A structured framework for analyzing and designing business models
- Value proposition design and validation
- Cost structure and revenue stream mapping
- Unit economics calculation and viability assessment
- Integration with pricing, customer insight, and revenue architecture kernels

This kernel is the central business-analysis substrate consumed by downstream kernels: [[11_KNOWLEDGE/kernel/AMOS_REVENUE_ARCHITECTURE_KERNEL|AMOS_REVENUE_ARCHITECTURE_KERNEL]], [[11_KNOWLEDGE/kernel/AMOS_PRICING_STRATEGY_KERNEL|AMOS_PRICING_STRATEGY_KERNEL]], [[11_KNOWLEDGE/kernel/AMOS_CUSTOMER_INSIGHT_KERNEL|AMOS_CUSTOMER_INSIGHT_KERNEL]], and [[11_KNOWLEDGE/kernel/AMOS_PARTNERSHIPS_CHANNELS_KERNEL|AMOS_PARTNERSHIPS_CHANNELS_KERNEL]].

---

## 2. Business Model Canvas

### 2.1 Nine-Block Framework

| Block | Description | AMOS Mapping |
| :--- | :--- | :--- |
| **Customer Segments** | Target groups of customers | [[11_KNOWLEDGE/kernel/AMOS_CUSTOMER_INSIGHT_KERNEL\|AMOS_CUSTOMER_INSIGHT_KERNEL]] |
| **Value Propositions** | Products/services that solve customer problems | This kernel (§3) |
| **Channels** | How value is delivered to customers | [[11_KNOWLEDGE/kernel/AMOS_PARTNERSHIPS_CHANNELS_KERNEL\|AMOS_PARTNERSHIPS_CHANNELS_KERNEL]] |
| **Customer Relationships** | Types of relationships with each segment | [[11_KNOWLEDGE/kernel/AMOS_CUSTOMER_INSIGHT_KERNEL\|AMOS_CUSTOMER_INSIGHT_KERNEL]] |
| **Revenue Streams** | How the model captures value as revenue | [[11_KNOWLEDGE/kernel/AMOS_REVENUE_ARCHITECTURE_KERNEL\|AMOS_REVENUE_ARCHITECTURE_KERNEL]] |
| **Key Resources** | Critical assets for the model | Resource inventory (internal) |
| **Key Activities** | Critical operations the model performs | Process architecture |
| **Key Partnerships** | External entities that enable the model | [[11_KNOWLEDGE/kernel/AMOS_PARTNERSHIPS_CHANNELS_KERNEL\|AMOS_PARTNERSHIPS_CHANNELS_KERNEL]] |
| **Cost Structure** | All costs incurred to operate the model | This kernel (§5) |

### 2.2 Canvas Evaluation Function

A business model $M$ is evaluated on five dimensions:

$$\text{Score}(M) = (V, C, R, S, P)$$

where:

- $V$ = value proposition strength (customer problem-solution fit)
- $C$ = cost structure efficiency (unit economics viability)
- $R$ = revenue stream quality (predictability, scalability)
- $S$ = strategic alignment (fit with organizational capabilities)
- $P$ = practical feasibility (execution risk assessment)

---

## 3. Value Proposition Design

### 3.1 Value Proposition Canvas

The value proposition is validated against two components:

**Customer Profile:**

- **Customer jobs**: Functional, social, and emotional tasks the customer tries to perform
- **Pains**: Obstacles, risks, and negative outcomes associated with customer jobs
- **Gains**: Desired outcomes, benefits, and aspirations

**Value Map:**

- **Products and services**: The offering portfolio
- **Pain relievers**: How the offering eliminates or reduces customer pains
- **Gain creators**: How the offering produces customer gains

### 3.2 Fit Assessment

Product-market fit is achieved when:

$$\text{Fit}(M) = \frac{|\text{Pain Relievers} \cap \text{Customer Pains}| + |\text{Gain Creators} \cap \text{Customer Gains}|}{|\text{Customer Pains}| + |\text{Customer Gains}|} \geq \tau_{fit}$$

where $\tau_{fit}$ is the minimum acceptable coverage threshold (typically $\geq 0.7$).

### 3.3 Value Proposition Hierarchy

| Level | Description | Validation Method |
| :--- | :--- | :--- |
| **Functional** | Solves a practical problem | Feature-benefit testing |
| **Emotional** | Makes customers feel something | Qualitative feedback |
| **Social** | Improves customers' social standing | Market research |
| **Ecosystem** | Creates platform/network value | Network-effect modeling |

---

## 4. Revenue Stream Analysis

### 4.1 Revenue Stream Types

| Type | Description | Predictability | Scalability |
| :--- | :--- | :--- | :--- |
| **Asset sale** | One-time product purchase | Low | Medium |
| **Usage fee** | Pay-per-use pricing | Medium | High |
| **Subscription** | Recurring access fee | High | High |
| **Licensing** | Permission to use IP | Medium | Very High |
| **Brokerage** | Intermediary fee | Medium | High |
| **Advertising** | Attention-based revenue | Low | Very High |

### 4.2 Revenue Diversity Index

Revenue diversity reduces concentration risk:

$$H_{rev} = -\sum_{i=1}^{n} p_i \ln(p_i)$$

where $p_i$ is the proportion of revenue from stream $i$. Higher Shannon entropy $H_{rev}$ indicates greater diversification.

---

## 5. Cost Structure

### 5.1 Cost Categories

| Category | Description | Behavior |
| :--- | :--- | :--- |
| **Fixed costs** | Costs that do not vary with output (rent, salaries) | Constant |
| **Variable costs** | Costs that scale with output (materials, compute) | Proportional to volume |
| **Semi-variable** | Costs with a fixed base and variable component (cloud compute) | Step function |

### 5.2 Cost Structure Classification

- **Cost-driven**: Minimize costs wherever possible (lean operations)
- **Value-driven**: Focus on maximum value creation (premium positioning)

---

## 6. Unit Economics

### 6.1 Key Metrics

| Metric | Formula | Viability Threshold |
| :--- | :--- | :--- |
| **Customer Acquisition Cost (CAC)** | $\text{Total Sales \& Marketing Spend} / \text{New Customers}$ | Must be recovered within payback period |
| **Lifetime Value (LTV)** | $\text{Avg Revenue/Customer} \times \text{Gross Margin} \times \text{Avg Lifespan}$ | $> 3 \times \text{CAC}$ |
| **LTV:CAC Ratio** | $\text{LTV} / \text{CAC}$ | $\geq 3$ for viability |
| **Payback Period** | $\text{CAC} / \text{Gross Margin per Customer}$ | $\leq 12$ months |
| **Gross Margin** | $(\text{Revenue} - \text{COGS}) / \text{Revenue}$ | $\geq 0.6$ for SaaS; varies by domain |
| **Break-even Volume** | $\text{Fixed Costs} / (\text{Price} - \text{Variable Cost per Unit})$ | Must be achievable within timeline |

### 6.2 Unit Economics Viability Check

A business model is economically viable when:

$$\text{LTV} > 3 \times \text{CAC} \quad \land \quad \text{Payback Period} \leq 12\text{ months} \quad \land \quad \text{Gross Margin} \geq \tau_{gm}$$

Failure on any condition flags the model as requiring redesign.

---

## 7. Business Model Patterns

| Pattern | Description | When to Apply |
| :--- | :--- | :--- |
| **Unbundling** | Separate products into focused offerings | When one product serves multiple distinct segments |
| **Long tail** | Aggregate niche offerings | When distribution costs are low |
| **Multi-sided platforms** | Serve multiple customer groups simultaneously | When network effects create value |
| **Free/freemium** | Offer basic free, charge for premium | When marginal cost is near zero |
| **Razor/blade** | Sell base cheap, profit on consumables | When recurring consumption is high |
| **Lock-in** | Create switching costs | When ecosystem value compounds |

---

## 8. Integration Points

| Interface | Direction | Contract |
| :--- | :--- | :--- |
| [[11_KNOWLEDGE/kernel/AMOS_REVENUE_ARCHITECTURE_KERNEL\|AMOS_REVENUE_ARCHITECTURE_KERNEL]] | Write | Revenue stream design and monetization models |
| [[11_KNOWLEDGE/kernel/AMOS_PRICING_STRATEGY_KERNEL\|AMOS_PRICING_STRATEGY_KERNEL]] | Read/Write | Pricing models and willingness-to-pay data |
| [[11_KNOWLEDGE/kernel/AMOS_CUSTOMER_INSIGHT_KERNEL\|AMOS_CUSTOMER_INSIGHT_KERNEL]] | Read | Customer segments and needs mapping |
| [[11_KNOWLEDGE/kernel/AMOS_PARTNERSHIPS_CHANNELS_KERNEL\|AMOS_PARTNERSHIPS_CHANNELS_KERNEL]] | Read | Channel and partnership economics |
| [[11_KNOWLEDGE/kernel/AMOS_SIMULATION_KERNEL\|AMOS_SIMULATION_KERNEL]] | Write | Business model scenarios for simulation |

---

```RSCF-NODE
node_id: business_model_kernel_knowledge_spec
node_type: kernel_specification
domain: 11_KNOWLEDGE/kernel
claim_class: AMOS_MODEL
confidence_ceiling:
  value_proposition_design: medium
  unit_economics: high
  cost_structure_analysis: medium
falsifiers:
  - Unit economics viability check passes when LTV:CAC < 3
  - Value proposition fit score accepted below threshold
  - Revenue diversity index not computed for multi-stream models
```

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/kernel/AMOS_REVENUE_ARCHITECTURE_KERNEL|AMOS_REVENUE_ARCHITECTURE_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_PRICING_STRATEGY_KERNEL|AMOS_PRICING_STRATEGY_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_CUSTOMER_INSIGHT_KERNEL|AMOS_CUSTOMER_INSIGHT_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_PARTNERSHIPS_CHANNELS_KERNEL|AMOS_PARTNERSHIPS_CHANNELS_KERNEL]]

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/kernel/KERNEL_MOC|KERNEL_MOC]]
