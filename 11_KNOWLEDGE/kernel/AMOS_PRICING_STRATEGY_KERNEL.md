---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Pricing Strategy Kernel
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

# AMOS Pricing Strategy Kernel

> [!abstract] Kernel Specification
> Defines the pricing strategy framework for AMOS: pricing models, willingness-to-pay measurement, price discrimination mechanisms, price elasticity, and value-based pricing. This is the AMOS reasoning/spec pattern for pricing — **not** a claim that AMOS OS executes live pricing operations (per AGENTS.md invariant 4).

> [!warning] Source Reconstitution
> This kernel was originally a GAP (auto-parse failed). Content has been reconstructed from cross-references in AMOS_UNIVERSE_OS_vInfinity P7_domain_engines, the Marketing GTM Kernel (pricing_strategy cluster), Sales Kernel (pricing cluster), and Product Strategy Kernel (value_proposition_design). All claims are `SOURCE_CLAIM`/`DERIVED` until validated against original source material.

---

## 1. Purpose

The Pricing Strategy Kernel provides:

- A structured framework for pricing model selection and optimization
- Willingness-to-pay (WTP) measurement and application
- Price discrimination and segmentation-based pricing
- Price elasticity modeling and demand forecasting
- Value-based pricing methodology
- Integration with [[11_KNOWLEDGE/kernel/AMOS_BUSINESS_MODEL_KERNEL|AMOS_BUSINESS_MODEL_KERNEL]], [[11_KNOWLEDGE/kernel/AMOS_REVENUE_ARCHITECTURE_KERNEL|AMOS_REVENUE_ARCHITECTURE_KERNEL]], and [[11_KNOWLEDGE/kernel/AMOS_CUSTOMER_INSIGHT_KERNEL|AMOS_CUSTOMER_INSIGHT_KERNEL]]

---

## 2. Pricing Models

### 2.1 Model Taxonomy

| Model | Mechanism | When to Use | Risk |
| :--- | :--- | :--- | :--- |
| **Cost-plus** | Price = Cost + Markup | Commodity; regulated markets | Ignores value; leaves money on table |
| **Competitive** | Price at market parity | Undifferentiated offerings | Race to bottom; margin pressure |
| **Value-based** | Price = Share of customer value | Differentiated; measurable ROI | Requires value quantification |
| **Dynamic** | Price adjusts to demand/time | High-demand variability | Customer fairness perception |
| **Freemium** | Free tier + paid upgrade | Large TAM; low marginal cost | Conversion rate risk |
| **Tiered** | Multiple price-feature bundles | Diverse segments with different WTP | Complexity; cannibalization risk |
| **Usage-based** | Pay per unit consumed | Variable consumption; scales with value | Revenue volatility |
| **Subscription** | Recurring flat fee | Predictable value delivery | Retention dependency |

### 2.2 Pricing Model Selection

The optimal model is selected by evaluating:

$$\text{Model Score}(m) = \sum_{k=1}^{5} w_k \cdot \text{Fit}_{m,k}$$

| Dimension | Weight | Description |
| :--- | :--- | :--- |
| Value capture efficiency | 0.30 | How well the model captures willingness-to-pay |
| Customer fairness perception | 0.20 | How fair customers perceive the pricing |
| Revenue predictability | 0.20 | How stable and forecastable revenue is |
| Operational simplicity | 0.15 | How easy the model is to implement and explain |
| Competitive positioning | 0.15 | How the price compares to alternatives |

---

## 3. Willingness-to-Pay (WTP)

### 3.1 WTP Definition

Willingness-to-pay $WTP(q) = V(q) - \text{Surplus}_{\text{threshold}}$, where $V$ is perceived value and surplus threshold is the minimum consumer surplus required to transact.

### 3.2 WTP Measurement Methods

| Method | Description | Accuracy | Cost |
| :--- | :--- | :--- | :--- |
| **Van Westendorp** | Four-price-point survey (too cheap, cheap, expensive, too expensive) | Medium | Low |
| **Gabor-Granger** | Direct price-response survey | Medium | Low |
| **Conjoint Analysis** | Feature-price tradeoff modeling | High | High |
| **A/B Price Testing** | Real-market price experiments | High | Medium |
| **Economic Value Estimation** | Reference-price + differentiation-value calculation | Medium | Low |
| **Competitive Benchmarking** | Market price mapping | Low | Low |

### 3.3 WTP Distribution

WTP across a segment follows a distribution $WTP \sim \mathcal{F}(\mu_{wtp}, \sigma_{wtp})$ — typically Normal, Log-normal (right-skewed), or Uniform (maximum-entropy). The revenue-maximizing price depends on distribution shape (see §4).

---

## 4. Price Optimization

### 4.1 Revenue Maximization

Given a WTP distribution $f(w)$ and cost $c$ per unit:

$$\text{Revenue}(p) = p \times \text{Demand}(p) = p \times \int_p^{\infty} f(w) \, dw$$

The optimal price $p^*$ maximizes revenue:

$$p^* = \arg\max_p \, p \int_p^{\infty} f(w) \, dw$$

For a normal distribution, $p^* \approx \mu + \sigma \cdot \Phi^{-1}\left(\frac{c}{\mu}\right)$ (with appropriate adjustments).

### 4.2 Profit Maximization

$$\text{Profit}(p) = (p - c) \times \text{Demand}(p) = (p - c) \times \int_p^{\infty} f(w) \, dw$$

$$p^*_{\text{profit}} = \arg\max_p \, (p - c) \int_p^{\infty} f(w) \, dw$$

The profit-maximizing price is always $\geq$ the revenue-maximizing price (when $c > 0$).

### 4.3 Price Elasticity of Demand

Price elasticity $\epsilon$ measures demand sensitivity:

$$\epsilon = \frac{\partial Q / Q}{\partial P / P} = \frac{\partial Q}{\partial P} \times \frac{P}{Q}$$

| Elasticity | Interpretation | Pricing Implication |
| :--- | :--- | :--- |
| $|\epsilon| > 1$ | Elastic (price-sensitive) | Lower price → higher revenue |
| $|\epsilon| = 1$ | Unit elastic | Revenue-maximizing point |
| $|\epsilon| < 1$ | Inelastic (price-insensitive) | Higher price → higher revenue |
| $\epsilon = 0$ | Perfectly inelastic | Price can increase without demand loss |

---

## 5. Price Discrimination and Versioning

| Degree | Mechanism | AMOS Application |
| :--- | :--- | :--- |
| **First-degree** | Charge each customer their exact WTP | Personalized pricing (where feasible and ethical) |
| **Second-degree** | Self-selection through versioning/tiers | Tiered pricing; volume discounts |
| **Third-degree** | Segment-based pricing | Different prices for different segments |

Product tiers maximize surplus extraction:

$$\text{Tier Value} = \text{Feature Bundle} \times \text{Segment WTP}$$

| Tier | Target Segment | Pricing Relation |
| :--- | :--- | :--- |
| **Basic** | Price-sensitive; low WTP | $p_{basic} = WTP_{low}$ |
| **Professional** | Moderate WTP; needs core features | $p_{pro} = WTP_{mid}$ |
| **Enterprise** | High WTP; needs advanced features | $p_{enterprise} = WTP_{high}$ |

Self-selection is encouraged by feature differentiation (not just restriction) so each segment prefers its intended tier. Price discrimination is bounded by fairness, transparency, non-discrimination, and AMOS M01 compliance (`INTEGRITY > COMPLETENESS > FLUENCY > SPEED`).

---

## 6. Value-Based Pricing

### 6.1 Value quantification

$$\text{Price} = \alpha \times \text{Economic Value to Customer (EVC)}$$

where $\alpha \in [0, 1]$ is the value share (typically 0.2–0.5 for B2B, 0.1–0.3 for B2C):

$$\text{EVC} = \text{Reference Value} + \text{Differentiation Value}$$

- **Reference Value**: Price of the best alternative
- **Differentiation Value**: Additional value from your product's unique features

### 6.2 Value Proposition Pricing Alignment

The pricing must align with the value proposition hierarchy (see [[11_KNOWLEDGE/kernel/AMOS_BUSINESS_MODEL_KERNEL|AMOS_BUSINESS_MODEL_KERNEL]] §3.3):

- Functional value → measurable ROI pricing
- Emotional value → premium positioning
- Social value → status-based pricing
- Ecosystem value → platform/network pricing

---

## 7. Price Testing and Optimization

### 7.1 A/B Price Testing

A/B price testing follows: (1) random assignment into control/variant groups, (2) expose different prices, (3) measure conversion rate and revenue per visitor, (4) apply statistical test (see [[11_KNOWLEDGE/kernel/AMOS_PROBABILITY_STATISTICS_KERNEL|AMOS_PROBABILITY_STATISTICS_KERNEL]]), (5) deploy winning price. Ongoing monitoring tracks: price realization (actual/list), discount depth, win rate by price band, and competitive price index.

---

## 8. Failure Modes

| Failure | Detection | Recovery |
| :--- | :--- | :--- |
| WTP miscalibration | Low conversion despite high perceived value | Re-measure WTP; adjust pricing |
| Price elasticity misread | Revenue declines after price increase | Roll back; conduct elasticity study |
| Tier cannibalization | Customers self-select to lower tier | Redesign feature differentiation |
| Competitive undercutting | Win rate drops below benchmark | Evaluate value differentiation; consider strategic pricing |
| Price perception gap | Customer surveys show "too expensive" vs "good value" | Improve value communication; adjust pricing |

---

## 9. Integration Points

| Interface | Direction | Contract |
| :--- | :--- | :--- |
| [[11_KNOWLEDGE/kernel/AMOS_BUSINESS_MODEL_KERNEL\|AMOS_BUSINESS_MODEL_KERNEL]] | Read/Write | Pricing feeds value proposition; cost structure constrains pricing floor |
| [[11_KNOWLEDGE/kernel/AMOS_REVENUE_ARCHITECTURE_KERNEL\|AMOS_REVENUE_ARCHITECTURE_KERNEL]] | Write | Pricing defines revenue per unit for revenue modeling |
| [[11_KNOWLEDGE/kernel/AMOS_CUSTOMER_INSIGHT_KERNEL\|AMOS_CUSTOMER_INSIGHT_KERNEL]] | Read | Segment WTP data; persona-based pricing needs |
| [[11_KNOWLEDGE/kernel/AMOS_PARTNERSHIPS_CHANNELS_KERNEL\|AMOS_PARTNERSHIPS_CHANNELS_KERNEL]] | Read | Channel margin requirements constrain pricing ceiling |
| [[11_KNOWLEDGE/kernel/AMOS_PROBABILITY_STATISTICS_KERNEL\|AMOS_PROBABILITY_STATISTICS_KERNEL]] | Read | Statistical testing for price experiments |

---

```RSCF-NODE
node_id: pricing_strategy_kernel_knowledge_spec
node_type: kernel_specification
domain: 11_KNOWLEDGE/kernel
claim_class: AMOS_MODEL
confidence_ceiling:
  pricing_model_selection: medium
  willingness_to_pay_measurement: medium
  price_optimization: high
  price_discrimination: medium
falsifiers:
  - Pricing set without measuring WTP
  - Price elasticity not tracked after deployment
  - Tier cannibalization not detected or addressed
```

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/kernel/AMOS_BUSINESS_MODEL_KERNEL|AMOS_BUSINESS_MODEL_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_REVENUE_ARCHITECTURE_KERNEL|AMOS_REVENUE_ARCHITECTURE_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_CUSTOMER_INSIGHT_KERNEL|AMOS_CUSTOMER_INSIGHT_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_PARTNERSHIPS_CHANNELS_KERNEL|AMOS_PARTNERSHIPS_CHANNELS_KERNEL]]

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/kernel/KERNEL_MOC|KERNEL_MOC]]
