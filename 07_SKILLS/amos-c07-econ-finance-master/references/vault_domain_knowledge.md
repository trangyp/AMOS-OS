---
title: Vault Domain Knowledge — Amos C07 Econ Finance Master
type: reference
source: 07_SKILLS/amos-c07-econ-finance-master/references
tags:
- reference
- amos-c07-econ-finance-master
- type/skill
- skill
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# amos-c07-econ-finance-master — Vault-Sourced Domain Knowledge

> Load this reference only when detailed domain knowledge is needed.
> This content was moved from SKILL.md for progressive loading.

---

> **Source**: `11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

# AMOS C07 — Economics & Finance Master Knowledge

> **Epistemic boundary**
>
> This file replaces synthetic `x100k` micro-module expansion with substantive economics and
> finance knowledge. It does not claim encyclopedic completeness. Established results,
> tested models, regime-dependent projections, competing hypotheses, normative choices, and
> AMOS/Trang abstractions are kept separate.
>
> **Hard boundary (non-negotiable):** every output in this domain is analytical decision
> support labeled MODEL or CONDITIONAL. There is no personalized financial advice, no trading
> recommendation, no autonomous execution of trades/purchases/deployments, and no performance
> guarantee anywhere in C07. All forecasts are CONDITIONAL/MODEL and carry assumption registers
> and uncertainty bands.

## 0. C07 Knowledge Contract

### 0.1 Claim classes
- **VERIFIED** — strongly supported empirical regularity within a stated market/regime.
- **DERIVED** — mathematical or logical consequence of stated premises/model.
- **MODEL** — representation useful within stated scope; default class for all C07 outputs.
- **CONDITIONAL** — dependent on explicit assumptions, scenario, or regime.
- **COMPETING** — unresolved alternatives (e.g., efficient vs behavioral pricing).
- **UNKNOWN/GAP** — insufficient evidence or unresolved mechanism.

### 0.2 Evidence classes
`OBSERVATION`, `MARKET_DATA`, `STATEMENT_RECORD`, `BACKTEST`, `MONITORING`, `DERIVED`,
`MODEL`, `SCENARIO`, `SOURCE_CLAIM`, `UNKNOWN`.

Sample-size honesty is part of the evidence policy: any statistic computed from N observations
must carry N, its regime window, and a statement of whether N supports the claimed precision.
Backtests on short windows are anecdotes with arithmetic attached.

### 0.3 C07 H-level ownership
1. Economic Structure, Stocks & Flows
2. Market Dynamics, Regimes & Statistics Discipline
3. Business & Corporate Finance Structure
4. Market Sizing & Economic Forecasting
5. FX Structural Analysis
6. Risk, Scenarios & Coupled-Position Systems
7. Data, Measurement & Financial Indicators
8. Investment Reasoning & Governance Stack
9. AMOS/Trang Finance Research Bridge (wealth-equations spine)

A topic has one primary owner. Cross-links are references, not duplicated substantive sections.

### 0.4 Standard knowledge node schema
Where applicable:
**definition → state variables → governing relations → assumptions → mechanisms → observables →
data sources → empirical status → scope/regime → uncertainty → failure modes → competing models →
falsifiers → dependencies → decision relevance → AMOS bridge**.

---

# H1 — Economic Structure, Stocks & Flows

## M1. The Economy as a Coupled System

### L1. Major interacting subsystems
C07 models economies as coupled systems containing:
- households (consumption, labor supply, saving);
- firms (production, investment, hiring);
- financial intermediaries (credit creation, maturity transformation);
- government (taxing, spending, regulation, monetary authority);
- external sector (trade, capital flows, exchange rates);
- real assets and infrastructure;
- information and expectation systems.

These are analytical partitions, not independent worlds. Money, goods, labor, capital,
information, and expectations cross boundaries continuously.

### L2. Stocks and flows
A stock `X` changes according to:
`dX/dt = Σ inflows - Σ outflows + internal production - internal depreciation`.

Examples:
- household net worth; corporate debt stock;
- money aggregates; inventory stocks;
- public debt-to-GDP ratio; capital stock.

A flow statement (income statement) without its balance-sheet counterpart hides solvency.
C07 requires both levels before structural conclusions.

### L3. Accounting identities
National accounting identities are definitional, not behavioral claims:
`Y = C + I + G + NX` (expenditure identity);
`S - I = CA` (saving-investment / current-account link).

They constrain any story told about an economy. A narrative violating them is wrong by
construction, regardless of plausibility.

### L4. Feedback
Feedback exists when a state change alters processes that subsequently affect that state.

Positive (amplifying) examples:
- collateral values ↔ credit availability;
- bank deleveraging ↔ asset fire sales;
- currency depreciation ↔ imported inflation.

Negative (dampening) examples:
- price adjustment rationing demand;
- automatic fiscal stabilizers;
- central-bank reaction functions.

Amplifying feedback does not mean beneficial; it means instability-prone under stress.

---

## M2. Money, Credit & Interest Rates

### L1. Money and credit creation
Modern banking systems create deposits through lending subject to capital, liquidity,
and regulatory constraints. Central banks set or influence short rates and reserves;
the transmission to broad credit runs through bank balance sheets, borrower demand,
and collateral conditions.

### L2. Interest-rate structure
Key distinctions that must never be collapsed into one number:
- nominal vs real rate (`r_real ≈ r_nominal - expected inflation`);
- risk-free benchmark vs credit spread;
- spot curve vs forward-implied curve;
- policy rate vs market-clearing rate.

### L3. Discounting
Present value: `PV = Σ CF_t / (1+r)^t`.
The discount rate encodes time preference, risk premia, and liquidity premia simultaneously.
Choice of rate dominates long-horizon valuations; it is partly normative and must be explicit.

### L4. Debt service reality
Debt capacity depends on cash-flow coverage, refinancing schedule, rate structure
(fixed/floating), and collateral haircuts — not on headline leverage alone.

---

## M3. Inflation & Macro Adjustment

### L1. Inflation measurement
Headline CPI, core measures, deflators, and asset-price indices answer different questions.
Measurement choice (basket, owner-occupancy treatment, quality adjustment) materially changes
the series; declare it before interpreting.

### L2. Drivers
Inflation dynamics involve demand pressure, supply shocks, wage setting, exchange-rate
pass-through, expectations formation, and monetary/fiscal stance. Competing models weight
these differently; no single-cause account survives contact with most episodes.

### L3. Expectations
Expectation regimes matter: anchored vs de-anchored inflation expectations change the
persistence of shocks. Expectation data are measured imperfectly (surveys, breakevens,
model estimates) and each measure carries its own bias.

---

# H2 — Market Dynamics, Regimes & Statistics Discipline

## M1. Prices, Returns & Risk Measures

### L1. Return conventions
Simple vs log returns differ materially over multi-period horizons:
log returns add across periods; simple returns compound.
Volatility scaling assumes stationarity that markets frequently violate.

### L2. Distributional facts
Empirical return distributions exhibit fat tails, volatility clustering, and asymmetric
downside more often than Gaussian models imply. Tail-risk statements require explicit
distribution assumptions and should report tail estimates' estimation error.

### L3. Correlation nonstationarity
Pairwise correlations rise toward 1 in crises precisely when diversification is needed.
C07 rule: stressed-regime math uses stressed correlation matrices, not calm-regime averages.

---

## M2. Market Regime Statistics (sample-size honesty)

### L1. Regime definition
A regime is a stated window + stated classification rule
(trend/range/crisis; bull/bear; expansion/recession). Different rules produce different
regime histories on identical data. Declare the rule before reporting regime statistics.

### L2. Sample-size honesty gate
For any regime statistic:
- report N (observations in regime), window dates, and selection rule;
- if N < ~30 for parametric inference, label the result ANECDOTAL/CONDITIONAL, not VERIFIED;
- distinguish in-sample fit from out-of-sample skill;
- multiple-testing discipline: searching many rules until one backtests well inflates
  apparent skill; report the number of trials.

### L3. Backtest failure modes
Survivorship bias, look-ahead leakage, regime overfitting, cost/slippage omission, and
selection after the fact are the standard killers. A backtest without these disclosures
carries no evidential weight in C07.

### L4. Correct claim form
`Under regime definition R and window W (N observations), statistic S held; out-of-sample
status UNKNOWN.` — not `the market always does X`.

---

# H3 — Business & Corporate Finance Structure (BizFin Engine)

Source lineage: `amos-bizfin-engine` (unit economics, statement reading, valuation framing,
stress points). Analysis lens MODEL; not advice.

## M1. Unit Economics First

### L1. Per-transaction view
Before aggregate questions ("will this scale?"), answer the unit question
("does one transaction work?"):
contribution margin per unit, customer acquisition cost, payback period, retention/churn,
repeat behavior. Gate G1: unit level answered before aggregate level.

### L2. Contribution margin
`CM = price - variable cost per unit`. Fixed-cost recovery and operating leverage direction
follow from CM against fixed base. Negative-CM growth destroys value at scale rather than
creating it.

### L3. CAC and payback
CAC payback must be read against churn-adjusted customer lifetime value and funding horizon.
Assumptions about retention dominate the result and must be stated.

## M2. Statement Structural Reading

### L1. Cash flow as truth serum
Gate G2: cash flow privileged over earnings narratives.
Accrual earnings embed estimates (revenue recognition timing, provisions, capitalization
choices); operating cash flow and free cash flow reveal whether reported profit converts
to cash.

### L2. Working-capital behavior
Receivables/inventory growth outpacing revenue signals deteriorating collection, channel
stuffing risk, or demand weakness. Working-capital trajectory is a leading behavioral record.

### L3. Debt service reality
Interest coverage, amortization schedule, refinancing wall timing, covenant headroom,
fixed/floating mix. Headline leverage ratios alone mislead when maturities cluster.

## M3. Valuation Framing

### L1. Multiple methods with assumption sets
DCF, comparables, precedent transactions each carry distinct assumption sets.
Gate G3: valuation ranges carry their assumption sets; single-number false precision is
blocked. Sensitivity of value to discount rate/growth/margin assumptions must be visible.

### L2. Stress points ranking
Where does the model break?
customer concentration, fixed-cost leverage direction, refinancing walls, key-person
dependence, regulatory exposure, supplier concentration.
Output: ranked break-risks, each tagged with severity and detectability.

Gates G1–G4 enforced together; G4 requires MODEL labels and the not-advice disclaimer on
every output.

---

# H4 — Market Sizing & Economic Forecasting (BizFin Kernel v0)

Source lineage: `amos-bizfin-kernel-v0`. Bilingual en/vi. Base reasoning layer for BizFin
SUPER engines.

## M1. The Typed Axis System (declare before computing)

No number is meaningful until all five axes are declared:

| Axis | Values |
|---|---|
| AX01 analysis_scope | macro · sector · industry · company · project |
| AX02 geo_level | global · region · country · subnational · city_cluster |
| AX03 time_horizon | nowcast · short_term · medium_term · long_term · structural |
| AX04 sector_classification | GICS · NAICS · ISIC · custom |
| AX05 market_boundary | defined per engagement |

### L1. Axis declaration operation
Fix all five axes with the requester before any sizing work. Example: "EV charging market
in Vietnam" → sector-level / country / medium_term / custom classification /
boundary = public-charging-infrastructure — then and only then size.

### L2. Classification consistency
One sector system per analysis. Cross-system conversions (GICS↔NAICS etc.) must be logged;
silent merging of classification systems is blocked.

### L3. Boundary honesty
What is inside/outside the market boundary (value chain segments, channels included,
double-counting risks between layers) stated explicitly.

## M2. Horizon-Appropriate Method

### L1. Method tiering
nowcast ≠ long_term: methods and uncertainty differ by tier.
Nowcasting leans on high-frequency indicators; structural analysis on demographics,
productivity, institutions. Applying forecast language to nowcast-grade evidence triggers
re-tier.

### L2. Sizing decomposition
TAM/SAM/SOM style decompositions multiply assumption chains; each multiplication compounds
uncertainty. Report ranges with driver-level sensitivities, not point sizes.

### L3. Decision gates (kernel)
1. Sizing output without declared axes → invalid.
2. Mixed classification silently merged → blocked.
3. Forecast language on nowcast-grade evidence → re-tier.
4. Hard boundary: analytical decision support only — never financial advice, never
   autonomous execution (inherits math-compute-kernels governance).

---

# H5 — FX Structural Analysis (Omega FX Structural Engine)

Source lineage: FRACTAL FOREX ENTERPRISE + AMOS FX Validation Updates. All outputs MODEL;
never trading advice.

## M1. Structural Levels via Fractal Recurrence

### L1. Level detection
Structural levels identified through multi-timeframe recurrence match — a level counts only
when confirmed across timeframes. Gate: multi-timeframe confirmation required for any level
claim. Single-timeframe "levels" are observations, not structure.

### L2. Epistemic status
Fractal recurrence is a pattern-description device (MODEL), not a proven physical law of
markets. Levels are conditional reference points whose validity decays with regime change.

## M2. Regime Superposition & Position Tagging

### L1. Regime posteriors
Regime classes (trend/range/crisis) hold posterior weights updated on macro evidence.
No single regime is asserted while alternatives retain material probability.

### L2. Entanglement check
Correlated pairs audited before sizing decisions: shared factor exposures mean changing one
position re-runs its entangled partners. In crisis-regime math the stressed matrix replaces
the historical correlation matrix.

### L3. Risk tags
Every position carries LOW/MEDIUM/HIGH/UNKNOWN; UNKNOWN forces size caps.
Gates: confirmation required; stressed matrix in crisis math; tags mandatory;
MODEL labeling present; no performance guarantees.

---

# H6 — Risk, Scenarios & Coupled-Position Systems (QFS)

Source lineage: `amos-quantum-financial-system` (quantum-style reasoning applied to finance).
Orchestration framework canon (AMOS MODEL); all financial outputs analysis, never advice.

## M1. Hard Boundary (non-negotiable)

Analytical decision support only:
- no personalised financial advice, trading strategies, or investment recommendations;
- no autonomous execution of trades, purchases, or deployments;
- every output carries explicit uncertainty bands and assumption registers.

## M2. Superposition Scenario Fan-Out (MODEL-tagged)

The QFS stage model:

```text
1. DECOMPOSE     request into hori


## Vault-Sourced Domain Content

> Source: `11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE.md` (26747 bytes in vault)

### 0.1 Claim Classes

- **VERIFIED** — strongly supported empirical regularity within a stated market/regime.
- **DERIVED** — mathematical or logical consequence of stated premises/model.
- **MODEL** — representation useful within stated scope; default class for all C07 outputs.
- **CONDITIONAL** — dependent on explicit assumptions, scenario, or regime.
- **COMPETING** — unresolved alternatives (e.g., efficient vs behavioral pricing).
- **UNKNOWN/GAP** — insufficient evidence or unresolved mechanism.

### 0.2 Evidence Classes

`OBSERVATION`, `MARKET_DATA`, `STATEMENT_RECORD`, `BACKTEST`, `MONITORING`, `DERIVED`,
`MODEL`, `SCENARIO`, `SOURCE_CLAIM`, `UNKNOWN`.

Sample-size honesty is part of the evidence policy: any statistic computed from N observations
must carry N, its regime window, and a statement of whether N supports the claimed precision.
Backtests on short windows are anecdotes with arithmetic attached.

### 0.4 Standard Knowledge Node Schema

Where applicable:
**definition → state variables → governing relations → assumptions → mechanisms → observables →
data sources → empirical status → scope/regime → uncertainty → failure modes → competing models →
falsifiers → dependencies → decision relevance → AMOS bridge**.

---

# H1 — Economic Structure, Stocks & Flows

### L2. Sample-Size Honesty Gate

For any regime statistic:
- report N (observations in regime), window dates, and selection rule;
- if N < ~30 for parametric inference, label the result ANECDOTAL/CONDITIONAL, not VERIFIED;
- distinguish in-sample fit from out-of-sample skill;
- multiple-testing discipline: searching many rules until one backtests well inflates
  apparent skill; report the number of trials.

### L3. Backtest Failure Modes

Survivorship bias, look-ahead leakage, regime overfitting, cost/slippage omission, and
selection after the fact are the standard killers. A backtest without these disclosures
carries no evidential weight in C07.

### M1. The Typed Axis System (Declare Before Computing)

No number is meaningful until all five axes are declared:

| Axis | Values |
|---|---|
| AX01 analysis_scope | macro · sector · industry · company · project |
| AX02 geo_level | global · region · country · subnational · city_cluster |
| AX03 time_horizon | nowcast · short_term · medium_term · long_term · structural |
| AX04 sector_classification | GICS · NAICS · ISIC · custom |
| AX05 market_boundary | defined per engagement |

### L3. Boundary Honesty

What is inside/outside the market boundary (value chain segments, channels included,
double-counting risks between layers) stated explicitly.

### L3. Decision Gates (Kernel)

1. Sizing output without declared axes → invalid.
2. Mixed classification silently merged → blocked.
3. Forecast language on nowcast-grade evidence → re-tier.
4. Hard boundary: analytical decision support only — never financial advice, never
   autonomous execution (inherits math-compute-kernels governance).

---

# H5 — FX Structural Analysis (Omega FX Structural Engine)

Source lineage: FRACTAL FOREX ENTERPRISE + AMOS FX Validation Updates. All outputs MODEL;
never trading advice.

### L2. Epistemic Status

Fractal recurrence is a pattern-description device (MODEL), not a proven physical law of
markets. Levels are conditional reference points whose validity decays with regime change.

### M1. Hard Boundary (Non-Negotiable)

Analytical decision support only:
- no personalised financial advice, trading strategies, or investment recommendations;
- no autonomous execution of trades, purchases, or deployments;
- every output carries explicit uncertainty bands and assumption registers.

### M2. Superposition Scenario Fan-Out (Model-Tagged)

The QFS stage model:

```text
1. DECOMPOSE     request into horizons × systems × constraints
2. FAN-OUT       enumerate what-if branches (rate paths, regime shifts, liquidity states)
                 — evaluate ALL branches before any collapse
3. ENTANGLE      map co-varying positions/assets; shared-factor clusters flagged
4. COLLAPSE      select branch by declared criteria; tag assumptions,
                 confidence ceiling ≤ 0.95, risk level
5. GOVERN        Rule-of-2 dual frame (bull/bear), Rule-of-4 quadrant impact,
                 no-advice disclaimer attached
```

**Class:** MODEL — an orchestration metaphor, not a claim that markets are quantum-mechanical.

### M1. Law-Stack Application To Finance

- **L1 Law of Law:** investment analysis internally consistent; governed by highest applicable
  constraint including financial regulations.
- **L2 Rule of 2:** at least two interpretations held simultaneously — bullish/bearish,
  base/alternative scenario.
- **L3 Rule of 4:** map analysis across biological (investor wellbeing/security),
  experiential (lived experience of investing), logical (soundness of reasoning),
  systemic (fit within broader financial system) quadrants.
- **L4 Absolute Structural Integrity:** return assumptions, risk assumptions, horizon, data
  limitations stated explicitly. No hidden leaps from analysis to recommendation.
- **L5 Post-Theory Communication:** precise language over jargon obfuscation.
- **L6 UBI Biological Alignment:** arrangements threatening investor wellbeing/security flagged.

### M2. Hie Pipeline (Finance Instance)

Parse investor context (risk tolerance, horizon, objectives, liquidity needs, constraints)
→ update state → goal → strategy (direct_structural_answer | step_by_step_tutorial) →
structure (entities: investment/investor/asset-class/market/alternatives/benchmark;
relations: OWNS, OWES, BENEFITS_FROM, IS_SUBJECT_TO, RISK_FROM, COMPETES_WITH,
CORRELATES_WITH; risk-return, temporal, uncertainty structures) → safety → channel →
realise → evaluate (disclaimer present? both sides analyzed? Rule-of-2 applied?
uncertainty labelled?).

Safety step is critical: analysis ≠ advice; disclaimer always attached; hard prohibitions on
harmful specific recommendations and market manipulation.

### M2. Wealth-Equations Spine

From `wealth-equation-systems`: 7 core spine equations describe structural wealth mechanics —

WealthAcceleration · DebtPower · Extraction · Rent · Collapse · CreditAmplification ·
PowerCompounding — across 7 accumulation modes (accumulation, extraction, control, deferral,
arbitrage, capture, exit).

### M4. Financial Causal Firewall

Do not infer causation from correlation, sequence alone, model fit alone, or narrative
plausibility alone. Identification requires explicit assumptions (instrument validity,
exogeneity), natural experiments where available, and convergent independent evidence.
Event studies must disclose the identification assumption, not just the abnormal-return
arithmetic.

### M5. Scenario Firewall

Scenario pathways are not probabilities unless explicitly probabilized.

Correct: `Under rate-path X and margin-assumption Y, model Z produces outcome range R.`

Incorrect: `Rates will do X` / `Buy Y`.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

---
**MOC:**

## Related

-

---

**Related:** [[amos-c07-econ-finance-master_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c07-econ-finance-master-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-c07-econ-finance-master/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
