---
title: "K_NSERK — Neuro-Symbolic Economic Reasoning & Constraint-Governance Kernel"
type: kernel_specification
artifact_id: AMOS-KERNEL-NSERK
canonical_name: K_NSERK

origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
amos_core_target: v4.4

source: 02_KERNEL
plane: 02_KERNEL
path: 02_KERNEL/K_NSERK.md
domain: neuro_symbolic_economic_reasoning

version: 3.0.0
updated: 2026-09-04

status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
canonical_status: ACTIVE_CANON_CANDIDATE

implementation_status: NOT_ESTABLISHED
runtime_enforcement_status: NOT_ESTABLISHED
formal_verification_status: NOT_ESTABLISHED
deployment_validation_status: NOT_ESTABLISHED

source_lineage:
  - arxiv:2603.18107v1
  - "ARTEMIS: A Neuro-Symbolic Framework for Economically Constrained Market Dynamics"
  - AMOS_CORE_v4_4_lineage
  - 02_KERNEL/KERNEL_KERNEL_CONTRACT

source_boundary:
  ARTEMIS_SOURCE:
    - continuous_time_Laplace_Neural_Operator_encoder
    - neural_SDE_latent_dynamics
    - Feynman_Kac_PDE_regularization
    - market_price_of_risk_regularization
    - differentiable_symbolic_bottleneck
    - adaptive_conformal_prediction
    - optional_portfolio_allocation
  AMOS_EXTENSION:
    - typed_constraint_registry
    - hard_constraint_gate
    - SMT_or_optimization_verifier_interface
    - authority_firewall
    - execution_admission
    - fail_closed_solver_behavior
    - provenance_and_receipts
    - RSCF_constraint_evidence
    - regime_and_freshness_governance

rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - arxiv:2603.18107v1
    - AMOS_CORE_v4_4_lineage
  scope: neuro_symbolic_economic_reasoning_kernel
  confidence_ceiling: DERIVED

tags:
  - amos-os
  - kernel
  - neuro-symbolic
  - economics
  - financial-modeling
  - neural-sde
  - feynman-kac
  - no-arbitrage
  - symbolic-regression
  - conformal-prediction
  - constraints
  - optimization
  - verification
  - rscf
---

# K_NSERK

## Neuro-Symbolic Economic Reasoning & Constraint-Governance Kernel

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Epistemic Class:** `AMOS_MODEL`  
> **Conclusion Class:** `DERIVED`  
> **Status:** `ACTIVE_SPECIFICATION`

---

## 0. Canonical Boundary

`K_NSERK` defines an AMOS kernel architecture for combining learned economic models with explicit symbolic, mathematical, risk, policy, and execution constraints.

The kernel is inspired in part by ARTEMIS, whose source architecture combines:

```text
Laplace Neural Operator
→ neural stochastic differential equation
→ economics-informed regularization
→ differentiable symbolic bottleneck
→ adaptive conformal uncertainty
→ optional portfolio construction
```

`K_NSERK` extends this pattern with AMOS governance controls.

The extensions MUST NOT be attributed to ARTEMIS unless the paper explicitly provides them.

Hard firewall:

```text
ARTEMIS SOURCE CLAIM
!=
AMOS EXTENSION

SOFT ECONOMIC REGULARIZATION
!=
HARD FORMAL GUARANTEE

SYMBOLIC BOTTLENECK
!=
FIRST-ORDER LOGIC PROOF

DIFFERENTIABLE SYMBOLIC REGRESSION
!=
SMT SOLVING

CONSTRAINT SATISFACTION
!=
ECONOMIC CORRECTNESS

NO-ARBITRAGE REGULARIZER
!=
PROOF OF GLOBAL NO-ARBITRAGE

CONFORMAL INTERVAL
!=
MARKET-RISK GUARANTEE

OPTIMIZATION FEASIBILITY
!=
AUTHORITY TO TRADE

FORMAL SPECIFICATION
!=
FORMAL VERIFICATION

MODEL OUTPUT
!=
EXECUTION AUTHORITY

BACKTEST PERFORMANCE
!=
LIVE TRADING EDGE

DOCUMENTED
!=
IMPLEMENTED

UNKNOWN/GAP
!=
PASS
```

---

## 1. Purpose

`K_NSERK` governs economic reasoning where a learned model proposes forecasts, latent dynamics, symbolic rules, allocations, prices, hedges, or other candidate economic actions that must remain inside explicitly declared admissibility constraints.

Canonical pipeline:

```text
MARKET / ECONOMIC OBSERVATION
→ POINT-IN-TIME FEATURE ADMISSION
→ LEARNED REPRESENTATION
→ STOCHASTIC / DYNAMIC MODEL
→ ECONOMIC REGULARIZATION
→ SYMBOLIC DISTILLATION
→ UNCERTAINTY ESTIMATION
→ CANDIDATE POLICY
→ HARD CONSTRAINT VALIDATION
→ AUTHORITY VALIDATION
→ EXECUTION ADMISSION
→ PROPOSE | HOLD | REJECT
```

The kernel separates four distinct questions:

```text
1. Is the prediction statistically useful?
2. Is the model economically plausible?
3. Does the candidate satisfy declared hard constraints?
4. Is the system authorized to act?
```

These questions MUST NOT be collapsed.

---

## 2. Architectural Scope

`K_NSERK` owns kernel semantics for:

1. economic-model constraint typing;
2. source-vs-extension separation;
3. learned economic dynamics;
4. stochastic latent-state modeling;
5. soft economics-informed regularization;
6. symbolic model extraction;
7. hard feasibility constraints;
8. solver-mediated projection or rejection;
9. uncertainty-aware decisions;
10. no-arbitrage claim boundaries;
11. solvency and collateral constraints;
12. portfolio feasibility;
13. constraint provenance;
14. regime validity;
15. point-in-time integrity;
16. solver failure behavior;
17. proof-status typing;
18. model-to-execution firewall.

It does not itself own:

```text
exchange connectivity
broker execution
custody
capital authorization
live trading authority
market data entitlement
position persistence
settlement
legal compliance
production risk limits
```

---

## 3. Source-Grounded ARTEMIS Architecture

The ARTEMIS source architecture is represented as:

\[
x_{1:T}
\xrightarrow{E_\phi}
z_{1:T}
\xrightarrow{\text{Neural SDE}}
\tilde z_{T+h}
\xrightarrow{g_\theta}
\hat y
\]

with auxiliary components for:

```text
economics-informed loss
symbolic distillation
conformal uncertainty
optional portfolio optimization
```

The source paper reports a composite training objective of the form:

\[
\mathcal L_{\mathrm{ARTEMIS}}
=
\mathcal L_{\mathrm{forecast}}
+
\lambda_{\mathrm{PDE}}\mathcal L_{\mathrm{PDE}}
+
\lambda_{\mathrm{MPR}}\mathcal L_{\mathrm{MPR}}
+
\lambda_{\mathrm{cons}}\mathcal L_{\mathrm{cons}}
\]

where:

- \(\mathcal L_{\mathrm{forecast}}\) is the predictive loss;
- \(\mathcal L_{\mathrm{PDE}}\) is a Feynman-Kac-style economic regularizer;
- \(\mathcal L_{\mathrm{MPR}}\) regularizes market price of risk;
- \(\mathcal L_{\mathrm{cons}}\) constrains latent trajectory consistency.

Hard epistemic rule:

```text
REGULARIZATION TERM
!=
HARD CONSTRAINT CERTIFICATE
```

---

## 4. ARTEMIS Evidence Boundary

The source reports benchmark results across:

```text
Jane Street
Optiver
Time-IMM
DSLOB
```

and reports strong directional accuracy in some settings, including synthetic DSLOB and Time-IMM, while also reporting weak performance on Optiver.

Therefore the proper conclusion is:

```text
ARTEMIS SHOWS PROMISING
DATASET-CONDITIONAL RESULTS
```

not:

```text
ARTEMIS ESTABLISHES
UNIVERSAL ECONOMIC VALIDITY
```

Hard rule:

```text
ONE OR MORE STRONG BENCHMARKS
!=
GENERAL MARKET VALIDITY
```

---

## 5. ARTEMIS Limitation Preserved

The source itself identifies an important issue around interpretation of the Feynman-Kac residual and the unknown risk-neutral drift.

Therefore `K_NSERK` MUST preserve:

```text
PDE REGULARIZER
→ ECONOMIC INDUCTIVE BIAS

PDE REGULARIZER
!=
PROOF THAT THE LEARNED PHYSICAL-MEASURE DYNAMICS
ARE A TRUE RISK-NEUTRAL MODEL
```

This limitation is load-bearing.

It MUST NOT be removed by stronger AMOS prose.

---

## 6. Neuro-Symbolic Architecture

AMOS defines the neuro-symbolic economic system as:

\[
\mathcal N
=
\langle
E,
D,
S,
Y,
C_s,
C_h,
U,
A
\rangle
\]

where:

- \(E\): encoder;
- \(D\): learned dynamics;
- \(S\): symbolic representation;
- \(Y\): prediction/policy proposal;
- \(C_s\): soft constraints;
- \(C_h\): hard constraints;
- \(U\): uncertainty representation;
- \(A\): authority context.

---

## 7. Learned Representation

Given point-in-time admissible market state \(x_t\):

\[
z_t = E_\phi(x_{\le t})
\]

where the information set MUST satisfy:

```text
NO FUTURE DATA
NO POST-OUTCOME LABEL INFORMATION
NO REVISED DATA WITHOUT RELEASE-TIME HANDLING
NO TEST-SET FITTING
```

Hard invariant:

```text
PREDICTIVE MODEL
MUST BE POINT-IN-TIME SAFE
```

---

## 8. Continuous-Time Encoder

Where irregular observations motivate continuous-time encoding, ARTEMIS proposes a Laplace Neural Operator-based encoder.

AMOS preserves this as:

```text
SOURCE_CLAIM / EMPIRICAL_MODEL
```

rather than a universal requirement.

Alternative encoders MAY include:

```text
neural ODE
neural CDE
state-space model
transformer
recurrent model
Kalman/state-space model
event-time encoder
```

subject to benchmark evidence.

---

## 9. Neural Stochastic Dynamics

A generic latent SDE is:

\[
dz_t
=
\mu_\theta(z_t,t)\,dt
+
\sigma_\theta(z_t,t)\,dW_t
\]

where:

- \(\mu_\theta\) is learned drift;
- \(\sigma_\theta\) is learned diffusion;
- \(W_t\) is a Wiener process under the chosen model measure.

Critical distinction:

```text
LEARNED SDE
!=
TRUE MARKET DYNAMICS
```

and:

```text
LATENT DIFFUSION
!=
OBSERVED MARKET VOLATILITY
```

unless separately calibrated and validated.

---

## 10. Numerical SDE Boundary

If Euler-Maruyama is used:

\[
z_{t+\Delta t}
=
z_t
+
\mu_\theta(z_t,t)\Delta t
+
\sigma_\theta(z_t,t)\sqrt{\Delta t}\,\epsilon
\]

with:

\[
\epsilon\sim\mathcal N(0,I)
\]

Numerical convergence depends on regularity assumptions.

No solver accuracy guarantee is inferred without validating:

```text
step size
Lipschitz behavior
growth conditions
numerical stability
discretization error
```

---

## 11. Economic Constraint Classes

`K_NSERK` separates:

```text
C0 — DATA / TYPE CONSTRAINT
C1 — ACCOUNTING IDENTITY
C2 — PORTFOLIO FEASIBILITY
C3 — RISK LIMIT
C4 — ECONOMIC MODEL CONDITION
C5 — MARKET-STRUCTURE CONDITION
C6 — LEGAL / POLICY CONSTRAINT
C7 — AUTHORITY CONSTRAINT
C8 — EXECUTION CONSTRAINT
```

This is MECE by functional responsibility, not by economic theory.

---

## 12. Soft vs Hard Constraints

A constraint \(C_k\) may be:

```text
SOFT
HARD
CONDITIONAL
DIAGNOSTIC
```

## Soft

Violations increase training or decision loss.

## Hard

Violation makes the candidate inadmissible.

## Conditional

Hard only in specific regimes.

## Diagnostic

Observed but does not itself block action.

Hard rule:

```text
SOFT PENALTY
!=
HARD SATISFACTION
```

---

## 13. Soft Constraint Objective

A general soft-constrained training objective is:

\[
\min_\theta
\mathbb E_{(x,y)\sim\mathcal D}
\left[
\mathcal L_{\mathrm{data}}
+
\sum_{k=1}^{K}
\lambda_k
\psi_k
\right]
\]

where:

\[
\lambda_k\ge 0
\]

and \(\psi_k\) is a constraint-violation penalty.

A generic inequality penalty may be:

\[
\psi_k(z)
=
\left[
\max(0,g_k(z))
\right]^2
\]

for desired:

\[
g_k(z)\le 0
\]

This is a penalty formulation.

It does not prove:

\[
g_k(z)\le0
\]

for every model output.

---

## 14. First-Order Logic Boundary

FOL MAY be used in the AMOS extension to encode symbolic policies such as:

\[
\forall a:
Eligible(a)
\Rightarrow
Risk(a)\le R_{\max}
\]

but this is not a source-derived ARTEMIS component.

Hard provenance label:

```text
FOL_CONSTRAINT_ENGINE:
  origin: AMOS_EXTENSION
```

---

## 15. SMT Boundary

SMT MAY be used for suitable discrete, linear, nonlinear-real, integer, or mixed symbolic constraint systems.

Example:

```text
ASSERT budget <= capital
ASSERT leverage <= leverage_limit
ASSERT position_i <= position_limit_i
ASSERT authority_valid == true
```

But:

```text
SMT SAT
!=
ECONOMIC TRUTH

SMT UNSAT
!=
MARKET IMPOSSIBILITY
```

It means only that the encoded formula is satisfiable or unsatisfiable under the solver theory.

---

## 16. Constraint Registry

```yaml
EconomicConstraint:
  constraint_id:
  class:

  expression:
  variables:
  domains:
  units:

  type:
    - HARD
    - SOFT
    - CONDITIONAL
    - DIAGNOSTIC

  regime:
  freshness:

  source:
  provenance:

  authority:
  enforcement_layer:

  falsifier:
```

---

## 17. Hard Feasible Set

Let candidate policy be:

\[
a\in\mathcal A
\]

and hard constraints:

\[
g_i(a,x)\le0
\]

\[
h_j(a,x)=0
\]

Then the feasible set is:

\[
\mathcal C(x)
=
\left\{
a\in\mathcal A:
g_i(a,x)\le0,\;
h_j(a,x)=0
\right\}
\]

A candidate is admissible only if:

\[
a\in\mathcal C(x)
\]

for all required hard constraints.

---

## 18. Projection

When the feasible set is nonempty and projection semantics are valid:

\[
\Pi_{\mathcal C}(y)
=
\arg\min_{z\in\mathcal C}
\frac12
(z-y)^\top Q(z-y)
\]

where:

\[
Q\succeq0
\]

The projection is unique only under appropriate convexity/strict-convexity conditions.

Hard firewall:

```text
PROJECTION EXISTS
!=
PROJECTION UNIQUE

NUMERICAL SOLVER SUCCESS
!=
MATHEMATICAL PROOF OF GLOBAL OPTIMUM

PROJECTED POLICY
!=
AUTHORIZED POLICY
```

---

## 19. Nonconvex Constraint Boundary

If \(\mathcal C\) is nonconvex:

```text
LOCAL SOLVER SUCCESS
```

may identify only a local feasible/optimal point.

Therefore solver metadata MUST preserve:

```text
solver
algorithm
status
tolerance
optimality_status
feasibility_status
iterations
termination_reason
```

---

## 20. Fail-Closed Projection

Critical correction:

```text
SOLVER FAILURE
MUST NOT
RETURN AN UNVERIFIED FALLBACK PORTFOLIO
```

Required behavior:

```text
SOLVER FAILURE
→ NO_ACTION / HOLD / ESCALATE
```

unless an independently validated safe fallback policy exists.

Hard rule:

```text
INFEASIBLE
!=
NORMALIZE WEIGHTS AND CONTINUE
```

---

## 21. Safe Solver Contract

```yaml
ConstraintSolveResult:
  request_id:

  solver:
  solver_version:

  feasible:
  optimal:
  certified:

  primal_residual:
  dual_residual:

  candidate:
  violated_constraints: []

  status:
    - FEASIBLE
    - FEASIBLE_NOT_PROVEN_OPTIMAL
    - INFEASIBLE
    - NUMERICAL_FAILURE
    - TIMEOUT
    - UNKNOWN

  action:
    - PASS_TO_NEXT_GATE
    - HOLD
    - REJECT
```

---

## 22. Portfolio Budget Constraint

For portfolio weights:

\[
w\in\mathbb R^n
\]

a fully invested portfolio may impose:

\[
\mathbf 1^\top w = 1
\]

If long-only:

\[
w_i\ge0
\]

But:

```text
SUM(w)=1
AND
w_i>=0
```

do not imply no-arbitrage.

They are portfolio feasibility constraints.

---

## 23. Leverage

Gross leverage may be:

\[
L(w)
=
\sum_i |w_i|
\]

with:

\[
L(w)\le L_{\max}
\]

where the permitted limit is policy-specific.

No universal value is imposed.

---

## 24. Position Limits

\[
|w_i|
\le
\bar w_i
\]

may enforce asset-level exposure limits.

These limits are:

```text
POLICY / RISK CONSTRAINTS
```

not fundamental economic laws.

---

## 25. Solvency

A simplified balance-sheet solvency condition may be:

\[
A_t-L_t\ge B_t
\]

where:

- \(A_t\): admissibly valued assets;
- \(L_t\): liabilities;
- \(B_t\): required buffer.

The valuation rules, haircut rules, liquidity assumptions, and legal definitions MUST be specified.

---

## 26. Collateral Ratio

A collateral ratio may be defined:

\[
CR_t
=
\frac{V_{\mathrm{eligible\ collateral},t}}
{Exposure_t}
\]

with requirement:

\[
CR_t\ge CR_{\min}
\]

But:

```text
CR_min = 1.25
```

is NOT a universal AMOS invariant.

The earlier hardcoded `1.25` threshold is removed.

Thresholds MUST come from:

```text
policy
contract
regulation
venue rules
risk governance
```

---

## 27. No-Arbitrage Boundary

No-arbitrage is a property of a defined market model.

It is not equivalent to:

```text
long-only weights
positive asset prices
budget conservation
low volatility
positive portfolio value
```

Hard rule:

```text
POSITIVE PORTFOLIO VALUE
!=
NO ARBITRAGE
```

---

## 28. Fundamental Theorem Boundary

Under suitable mathematical assumptions, versions of the Fundamental Theorem of Asset Pricing relate absence of arbitrage to existence of an equivalent martingale measure.

But the exact theorem depends on:

```text
discrete vs continuous time
market completeness
admissible strategies
semimartingale assumptions
NFLVR or other arbitrage definition
measure-theoretic conditions
```

Therefore:

```text
FTAP
MUST NOT
BE COMPRESSED INTO
ONE UNIVERSAL MARKET EQUATION
```

---

## 29. Risk-Neutral Martingale Condition

For a tradable asset with appropriate assumptions under a risk-neutral measure \(\mathbb Q\):

\[
\mathbb E^\mathbb Q
\left[
D_{t,T}S_T
\mid
\mathcal F_t
\right]
=
S_t
\]

where \(D_{t,T}\) is the applicable discount factor.

This is model-dependent.

It is not a directly enforceable constraint on arbitrary forecasting outputs.

---

## 30. Feynman-Kac PDE

For diffusion:

\[
dZ_t
=
\mu^{\mathbb Q}(Z_t,t)\,dt
+
\sigma(Z_t,t)\,dW_t^{\mathbb Q}
\]

and value function \(V(z,t)\), a Feynman-Kac PDE may take the form:

\[
\frac{\partial V}{\partial t}
+
\mu^{\mathbb Q}\cdot\nabla V
+
\frac12
\operatorname{tr}
\left(
\sigma\sigma^\top\nabla^2V
\right)
-
rV
=
0
\]

under the relevant assumptions.

Critical invariant:

```text
PDE USE REQUIRES THE CORRECT MEASURE
AND VALID MODEL ASSUMPTIONS
```

---

## 31. Physical vs Risk-Neutral Measure

Distinguish:

\[
\mathbb P
\]

from:

\[
\mathbb Q
\]

Under a diffusion model, a market-price-of-risk process may connect drifts:

\[
\mu^{\mathbb Q}
=
\mu^{\mathbb P}
-
\sigma\lambda
\]

under appropriate dimensions and assumptions.

Hard rule:

```text
mu_P
!=
mu_Q
IN GENERAL
```

---

## 32. ARTEMIS PDE Caveat

If a PDE residual is evaluated using an estimated latent drift without properly identifying the risk-neutral drift, the residual should be treated as:

```text
ECONOMIC REGULARIZATION
```

not:

```text
FORMAL NO-ARBITRAGE CERTIFICATE
```

This correction is mandatory.

---

## 33. Market Price of Risk

A simplified scalar representation:

\[
\lambda_t
=
\frac{\mu_t-r_t}{\sigma_t}
\]

requires:

\[
\sigma_t>0
\]

and applies only under the corresponding one-dimensional model.

In multiple dimensions:

\[
\mu-r\mathbf 1
=
\sigma\lambda
\]

may be underdetermined or model-dependent.

Therefore:

```text
MARKET PRICE OF RISK
!=
UNIVERSAL SCALAR
```

---

## 34. Market-Price-of-Risk Penalty

A soft penalty can be:

\[
\mathcal L_{\mathrm{MPR}}
=
\mathbb E
\left[
\phi(\|\lambda_t\|-\lambda_{\max})
\right]
\]

with a nonnegative penalty \(\phi\).

This expresses inductive bias.

It does not establish the true market price of risk.

---

## 35. Symbolic Bottleneck

ARTEMIS proposes a differentiable symbolic bottleneck producing sparse human-readable expressions.

A generic representation:

\[
\hat y_{\mathrm{sym}}
=
\sum_{k=1}^{K}
\alpha_k f_k(x)
\]

where \(f_k\) are candidate symbolic basis functions.

Hard separation:

```text
HUMAN-READABLE EXPRESSION
!=
CAUSAL EXPLANATION

SYMBOLIC EXPRESSION
!=
ECONOMIC LAW

DISTILLED RULE
!=
GROUND TRUTH
```

---

## 36. Teacher–Student Distillation

A symbolic student may approximate neural teacher output through:

\[
\mathcal L_{\mathrm{distill}}
=
\frac1N
\sum_{i=1}^{N}
\left(
\hat y^{sym}_i
-
\hat y^{teacher}_i
\right)^2
+
\lambda_s\Omega(\alpha)
\]

where \(\Omega\) encourages simplicity or sparsity.

A successful approximation proves fidelity to the teacher over the measured domain.

It does not prove the teacher is correct.

---

## 37. Symbolic Complexity

Symbolic model quality SHOULD track:

```text
prediction fidelity
expression complexity
stability across resamples
regime stability
feature dependence
causal status
```

A simpler expression is not automatically more truthful.

---

## 38. Formal Logic Layer

AMOS MAY convert selected symbolic expressions into explicit logical propositions.

Example:

```text
IF volatility > v_max
AND liquidity < l_min
THEN candidate_trade = inadmissible
```

Logical rule provenance MUST indicate whether it comes from:

```text
regulation
risk policy
economic theorem
empirical discovery
human rule
AMOS model
```

---

## 39. Formal Proof Boundary

A formal proof establishes only the encoded proposition under its assumptions.

```text
THEOREM PROVED
!=
MODEL ASSUMPTIONS TRUE

THEOREM PROVED
!=
MARKET MODEL VALID

THEOREM PROVED
!=
LIVE TRADING SAFE
```

---

## 40. Lean 4 Boundary

The earlier Lean theorem:

```text
no_negative_wealth_under_admissible_weights
```

does NOT prove no-arbitrage.

At most, assumptions of:

```text
positive asset prices
nonnegative weights
weights summing to one
```

support positivity of the marked portfolio value.

That proposition is a portfolio-valuation fact, not FTAP.

Therefore it MUST NOT be named or cited as a no-arbitrage proof.

---

## 41. Formal Proposition Registry

```yaml
FormalProposition:
  proposition_id:
  theorem_name:

  statement:
  assumptions:

  domain:
  scope:

  proof_system:
    - Lean4
    - Coq
    - Isabelle
    - SMT
    - MANUAL

  proof_status:
    - PROVED
    - CHECKED
    - PARTIAL
    - UNPROVED
    - FALSIFIED

  source_hash:
  prover_version:
  proof_artifact_ref:
```

---

## 42. No `sorry` Promotion

A Lean declaration containing:

```lean
sorry
```

is not a completed formal proof.

Hard rule:

```text
LEAN FILE COMPILES WITH SORRY
!=
FORMALLY VERIFIED THEOREM
```

---

## 43. Correct Formal Target

A suitable bounded proposition might be:

```text
Given:
- a nonempty finite portfolio,
- nonnegative weights,
- total weight equal to one,
- strictly positive asset prices,

the weighted portfolio marked value is strictly positive.
```

Conclusion class:

```text
ESTABLISHED_MATH
```

if actually proved.

It remains unrelated to global no-arbitrage.

---

## 44. Conformal Prediction

Given calibration scores:

\[
s_i
=
|y_i-\hat y_i|
\]

a standard split-conformal interval can be constructed:

\[
C_\alpha(x)
=
[
\hat y(x)-q_{1-\alpha},
\hat y(x)+q_{1-\alpha}
]
\]

under the standard conformal assumptions.

For exchangeable data, marginal finite-sample coverage is the relevant guarantee.

---

## 45. Time-Series Conformal Boundary

Financial time series violate ordinary exchangeability.

Adaptive conformal methods may update calibration dynamically, but their guarantees depend on the specific method and assumptions.

Therefore:

```text
ADAPTIVE CONFORMAL
!=
UNCONDITIONAL DISTRIBUTION-FREE
TIME-SERIES COVERAGE
```

---

## 46. Coverage vs Conditional Accuracy

A conformal interval may achieve marginal coverage while performing poorly in:

```text
specific regimes
specific assets
tail periods
volatility spikes
subgroups
```

Hard rule:

```text
MARGINAL COVERAGE
!=
CONDITIONAL COVERAGE
```

---

## 47. Conformal Calibration State

```yaml
ConformalState:
  method:
  alpha:
  calibration_window:
  score_function:

  nominal_coverage:
  observed_coverage:

  regime:
  horizon:

  coverage_by_regime:
  interval_width:

  last_update:
  validity_status:
```

---

## 48. Prediction Uncertainty Is Not Risk

```text
FORECAST UNCERTAINTY
!=
PORTFOLIO RISK
```

Portfolio risk also depends on:

```text
exposure
covariance
liquidity
transaction costs
market impact
tail dependence
leverage
funding
counterparty risk
execution risk
```

---

## 49. Portfolio Optimization

A mean-variance-style objective may be:

\[
\max_w
\quad
w^\top\hat\mu
-
\frac{\gamma}{2}
w^\top\hat\Sigma w
\]

subject to explicit constraints.

This is an optimization model, not an economic truth.

---

## 50. Kelly Boundary

The exact Kelly objective is:

\[
\max_w
\mathbb E
\left[
\log(1+w^\top R)
\right]
\]

subject to the log argument remaining positive under the modeled return support.

A quadratic approximation:

\[
w^\top\mu
-
\frac12
w^\top\Sigma w
\]

is an approximation.

Hard rule:

```text
QUADRATIC KELLY APPROXIMATION
!=
EXACT KELLY SOLUTION
```

---

## 51. Covariance Boundary

Conformal interval widths alone do not generally identify the full return covariance matrix.

Therefore:

```text
q_i^2
as diagonal covariance proxy
```

is a modeling approximation.

It MUST be labeled:

```text
MODEL
```

not `OBSERVATION`.

---

## 52. Market Dynamics Regime

Each predictive/economic claim MUST declare regime variables where material:

```yaml
MarketRegime:
  volatility:
  liquidity:
  spread:
  trend:
  jump_intensity:
  funding_conditions:
  macro_event_state:
  market_session:
```

No universal regime classifier is prescribed.

---

## 53. Regime Firewall

\[
Valid(C,R_1)
\]

does not imply:

\[
Valid(C,R_2)
\]

Hard rule:

```text
TRAINING REGIME
!=
DEPLOYMENT REGIME
```

---

## 54. Distribution Shift

Monitor at minimum where appropriate:

```text
feature drift
prediction drift
residual drift
volatility regime shift
spread/liquidity shift
coverage degradation
constraint violation rate
```

Shift detection is diagnostic.

It is not itself a causal explanation.

---

## 55. Point-in-Time Integrity

Every economic input MUST preserve:

```text
observation timestamp
publication timestamp
availability timestamp
revision status
market-session timestamp
```

where material.

Hard rule:

```text
KNOWN LATER
!=
AVAILABLE THEN
```

---

## 56. Leakage Firewall

Reject experiments containing:

```text
future prices
future labels
post-event revisions
look-ahead normalization
train/test contamination
future-derived technical indicators
survivorship contamination where relevant
```

---

## 57. Data Provenance

```yaml
MarketObservation:
  instrument:
  venue:
  field:

  event_time:
  receive_time:
  availability_time:

  value:
  units:

  source:
  revision:

  quality_status:
  provenance:
```

---

## 58. Economic Claim Classes

Use:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
EMPIRICAL_MODEL
AMOS_MODEL
PREDICTION
DECISION
UNKNOWN/GAP
```

Examples:

```text
"ARTEMIS reports 64.96% directional accuracy on DSLOB"
→ SOURCE_CLAIM

"our reproduced run obtains 64.96%"
→ OBSERVATION only after execution evidence

"the PDE term causes the gain"
→ causal claim requiring stronger evidence

"the PDE term is associated with ablation performance differences"
→ supported experimental description
```

---

## 59. Ablation Causality Firewall

Removing a component and observing performance change gives intervention evidence within that trained experimental pipeline.

It does not establish that the component represents the true causal economic mechanism.

```text
MODEL COMPONENT ABLATION EFFECT
!=
MARKET-MECHANISM PROOF
```

---

## 60. Benchmark Boundary

A benchmark result inherits:

```text
dataset
split
horizon
target
metric
seed
preprocessing
baseline implementation
compute environment
```

No benchmark result may be silently generalized outside those conditions.

---

## 61. DSLOB Boundary

DSLOB is synthetic.

Therefore:

```text
SUCCESS ON DSLOB
!=
SUCCESS IN LIVE CRASH MARKETS
```

Synthetic regimes can test hypotheses but do not independently prove deployment validity.

---

## 62. Time-IMM Boundary

Performance on an environmental temperature forecasting dataset may demonstrate architecture-level forecasting behavior.

It is not financial-market evidence.

```text
TIME-SERIES TRANSFER
!=
ECONOMIC VALIDATION
```

---

## 63. Optiver Negative Evidence

Poor or weaker performance on a benchmark is retained as negative evidence.

AMOS MUST NOT hide it when characterizing ARTEMIS.

Hard invariant:

```text
NEGATIVE RESULT
IS PART OF MODEL SCOPE
```

---

## 64. Candidate Economic Decision

```yaml
EconomicDecisionCandidate:
  decision_id:

  timestamp:
  horizon:

  instrument_set:
  candidate_action:

  forecast:
  forecast_uncertainty:

  symbolic_explanation:

  soft_constraint_scores: []
  hard_constraint_results: []

  regime:
  provenance:

  authority_ref:
```

---

## 65. Hard Gate

A candidate may proceed only if:

\[
HardPass(a)
=
\bigwedge_{k\in H}
C_k(a)=TRUE
\]

If any hard constraint is:

```text
FALSE
UNKNOWN
STALE
UNVERIFIED
```

then:

```text
NO EXECUTION
```

---

## 66. Constraint Freshness

A constraint evaluated at time \(t_0\) may become stale before commit.

For mutable constraint state:

\[
Fresh(C_k)
=
Identity_{observed}(C_k)
=
Identity_{current}(C_k)
\]

This applies to:

```text
risk limits
position limits
capital
authority
market status
venue status
portfolio state
```

---

## 67. Authority Firewall

Even when:

\[
HardPass(a)=TRUE
\]

the action cannot execute unless:

\[
AuthorityValid(a)=TRUE
\]

Thus:

\[
Executable(a)
=
HardPass(a)
\land
AuthorityValid(a)
\land
CommitFresh(a)
\]

for governed effects.

---

## 68. Model / Authority Separation

```text
MODEL CAN:
forecast
rank
score
propose
explain
estimate

MODEL CANNOT:
grant itself trading authority
change capital limits
change governance limits
promote itself to production
```

---

## 69. Execution Firewall

`K_NSERK` SHOULD emit:

```text
PROPOSE
HOLD
REJECT
```

not broker-native orders.

Order construction belongs to the domain/runtime execution layer.

---

## 70. No Emergency Self-Hedge Authority

The earlier behavior:

```text
solver failure
→ emergency market-neutral hedge
```

is unsafe as a kernel default.

Solver failure does not establish:

```text
hedge need
hedge instrument
hedge ratio
liquidity
authority
```

Correct behavior:

```text
SOLVER FAILURE
→ FAIL CLOSED
→ HOLD / ESCALATE
```

---

## 71. No Automatic Liquidation

The earlier behavior:

```text
failure
→ liquidate risk-bearing positions
→ move to sovereign reserve assets
```

is rejected as a universal kernel rule.

Liquidation may itself create:

```text
market impact
tax consequences
liquidity loss
realized loss
basis risk
legal issues
operational risk
```

Such action requires a separate authorized recovery policy.

---

## 72. Recovery Classes

```text
R0 — NO ACTION
R1 — RECOMPUTE
R2 — REPROJECT
R3 — REDUCE SCOPE
R4 — BLOCK NEW RISK
R5 — EXECUTE PREAUTHORIZED HEDGE
R6 — EXECUTE PREAUTHORIZED LIQUIDATION
R7 — HUMAN / CONTROL-PLANE ESCALATION
```

R5/R6 require independent authorization.

---

## 73. Constraint Failure Taxonomy

```text
MODEL_VIOLATION
SOLVER_INFEASIBLE
NUMERICAL_FAILURE
STALE_DATA
STALE_CONSTRAINT
AUTHORITY_FAILURE
RISK_LIMIT_FAILURE
MARKET_CLOSED
LIQUIDITY_FAILURE
UNKNOWN_GAP
```

Different failures require different responses.

---

## 74. Economic Consistency Is Layered

```text
ACCOUNTING CONSISTENT
```

does not imply:

```text
ECONOMICALLY OPTIMAL
```

which does not imply:

```text
NO ARBITRAGE
```

which does not imply:

```text
SAFE
```

which does not imply:

```text
AUTHORIZED
```

---

## 75. Constraint Contradiction

Hard constraints may themselves conflict.

If:

\[
\mathcal C
=
\varnothing
\]

then no feasible action exists.

Correct result:

```text
INFEASIBLE
```

not silent relaxation.

---

## 76. Constraint Relaxation

Relaxing a hard constraint requires:

```text
explicit authority
new version
provenance
justification
scope
expiry
```

A solver MUST NOT autonomously convert a hard constraint into a soft one.

---

## 77. Constraint Priority

When constraints conflict, resolution follows explicit governance hierarchy.

Example:

```text
legal constraint
>
capital-preservation constraint
>
risk policy
>
optimization preference
```

only if that hierarchy is explicitly defined.

No universal ordering is invented here.

---

## 78. Economic Invariant Registry

```yaml
EconomicInvariant:
  invariant_id:

  statement:
  domain:
  scope:

  class:
    - ACCOUNTING
    - SOLVENCY
    - RISK
    - MARKET_MODEL
    - POLICY
    - AUTHORITY

  hard:
  source:

  assumptions:
  units:

  validation_method:
  falsifier:
```

---

## 79. No-Arbitrage Verification Levels

Use:

```text
NA0 — NOT CHECKED
NA1 — HEURISTIC REGULARIZATION
NA2 — LOCAL MODEL CONSISTENCY CHECK
NA3 — EXPLICIT MODEL ARBITRAGE TEST
NA4 — FORMAL PROPERTY UNDER DECLARED MODEL
NA5 — EMPIRICALLY MONITORED DEPLOYMENT CONDITION
```

No level establishes absolute market-wide no-arbitrage.

---

## 80. Solvency Verification Levels

```text
SV0 — UNKNOWN
SV1 — ACCOUNTING CHECK
SV2 — HAIRCUT / COLLATERAL CHECK
SV3 — STRESS CHECK
SV4 — LEGAL / POLICY VERIFIED
SV5 — COMMIT-TIME CAPITAL VERIFIED
```

---

## 81. Prediction Calibration

For point predictions, calibration may require:

```text
residual distribution
coverage
bias
horizon
regime
```

For directional probabilities, monitor:

```text
Brier score
log loss
reliability
sharpness
```

where applicable.

---

## 82. Directional Accuracy Boundary

Directional accuracy:

\[
DA
=
\frac1N
\sum_{i=1}^{N}
\mathbf 1[
\operatorname{sign}(\hat y_i)
=
\operatorname{sign}(y_i)
]
\]

does not account for:

```text
transaction costs
magnitude
turnover
tail loss
class imbalance
economic value
```

---

## 83. RankIC Boundary

Rank information coefficient measures rank association.

```text
HIGH RankIC
!=
PROFITABILITY

LOW RankIC
!=
UNUSABLE UNDER ALL OBJECTIVES
```

---

## 84. RMSE Boundary

\[
RMSE
=
\sqrt{
\frac1N
\sum_i
(y_i-\hat y_i)^2
}
\]

Lower RMSE does not automatically imply better trading performance.

---

## 85. Economic Evaluation

A complete evaluation MAY include:

```text
forecast accuracy
directional accuracy
calibration
turnover
transaction costs
slippage
drawdown
tail loss
Sharpe-like metrics
capacity
market impact
regime stability
```

No single metric is sufficient.

---

## 86. Sharpe Boundary

Sample Sharpe:

\[
\widehat{SR}
=
\frac{\bar r-r_f}{s_r}
\]

depends strongly on:

```text
sample period
frequency
serial correlation
non-normality
costs
regime
```

It must not be treated as an invariant measure of strategy quality.

---

## 87. Economic Backtest Firewall

```text
BACKTEST
!=
LIVE PERFORMANCE

PAPER TRADE
!=
LIVE EXECUTION

LIVE EXECUTION
!=
PERSISTENT EDGE
```

---

## 88. Constraint Adversarial Testing

Test at minimum:

```text
empty feasible set
near-boundary feasible set
floating-point tolerance
contradictory constraints
missing constraint
stale constraint
wrong units
wrong sign
overflow / NaN
solver timeout
solver local optimum
authority revocation
market halt
liquidity collapse
```

---

## 89. Unit Integrity

Economic quantities MUST carry units.

Examples:

```text
price: USD/share
position: shares
notional: USD
volatility: annualized_fraction
rate: 1/year
time: year
```

Hard rule:

```text
NUMERIC COMPATIBILITY
!=
UNIT COMPATIBILITY
```

---

## 90. Currency Integrity

Cross-currency calculations require explicit FX conversion.

\[
V_{\mathrm{base}}
=
FX_{c\rightarrow b}
V_c
\]

with:

```text
timestamp
venue/source
quote convention
```

preserved.

---

## 91. Sign Convention Integrity

P&L, liabilities, cash, exposures, and short positions require declared sign conventions.

Silent sign inversion is a critical economic-control failure.

---

## 92. Missing Data

Missing market input MUST be represented explicitly.

```text
MISSING
!=
ZERO
```

Imputation must preserve:

```text
method
time availability
uncertainty
```

---

## 93. Market Closure

A mathematically feasible action may be operationally impossible when:

```text
market closed
instrument halted
venue unavailable
borrow unavailable
```

Therefore:

```text
MODEL FEASIBILITY
!=
EXECUTION FEASIBILITY
```

---

## 94. Liquidity Constraint

Possible constraint:

\[
|q_i|
\le
\eta ADV_i
\]

where:

- \(q_i\): proposed trade quantity;
- \(ADV_i\): average daily volume or another liquidity proxy;
- \(\eta\): governed participation threshold.

This is a policy model.

---

## 95. Transaction-Cost Constraint

Expected edge should not be evaluated without modeled costs when costs are material.

\[
Edge_{\mathrm{net}}
=
Edge_{\mathrm{gross}}
-
Costs
\]

Costs may include:

```text
spread
fees
slippage
market impact
borrow
funding
tax
```

---

## 96. Arbitrage vs Statistical Edge

```text
ARBITRAGE
!=
HIGH EXPECTED RETURN

ARBITRAGE
!=
STATISTICAL PREDICTABILITY

ARBITRAGE
!=
HIGH SHARPE
```

The word "arbitrage" must retain its financial-theory meaning.

---

## 97. Economic Plausibility

Economic plausibility is weaker than proof.

Examples:

```text
reasonable risk premium
bounded leverage
coherent accounting
monotonic option-price relation
nonnegative variance
```

may improve plausibility.

They do not establish truth.

---

## 98. Model Measure Registry

```yaml
MeasureContext:
  measure:
    - PHYSICAL_P
    - RISK_NEUTRAL_Q
    - FORWARD_MEASURE
    - EMPIRICAL
    - MODEL_INTERNAL

  numeraire:
  filtration:
  horizon:

  assumptions:
  provenance:
```

No equation involving expected returns or discounted prices may omit measure context when material.

---

## 99. Market Filtration

Information available at time \(t\) is represented:

\[
\mathcal F_t
\]

A prediction using information outside:

\[
\mathcal F_t
\]

violates point-in-time integrity.

---

## 100. Forecast Object

```yaml
EconomicForecast:
  forecast_id:

  target:
  horizon:

  prediction:
  distribution:
  interval:

  model_id:
  model_version:

  information_cutoff:
  regime:

  calibration_status:
  uncertainty_status:

  provenance:
```

---

## 101. Symbolic Rule Object

```yaml
SymbolicEconomicRule:
  rule_id:

  expression:
  variables:
  units:

  source:
    - DISTILLED
    - HUMAN_POLICY
    - ECONOMIC_THEORY
    - FORMAL_RULE

  fidelity_to_teacher:
  empirical_support:

  causal_status:
    - NONE
    - ASSOCIATION
    - MECHANISTIC
    - UNKNOWN

  scope:
  regime:

  falsifiers:
```

---

## 102. Constraint Evaluation Object

```yaml
ConstraintEvaluation:
  evaluation_id:
  candidate_id:

  constraint_id:
  constraint_version:

  observed_inputs:
  input_versions:

  result:
    - PASS
    - FAIL
    - UNKNOWN
    - STALE

  margin:
  tolerance:

  solver:
  provenance:
```

---

## 103. Execution Proposal

```yaml
EconomicExecutionProposal:
  proposal_id:

  candidate:
  portfolio_before:
  portfolio_after:

  predicted_value:
  uncertainty:

  hard_gate:
  authority_gate:
  freshness_gate:
  liquidity_gate:
  risk_gate:

  decision:
    - PROPOSE
    - HOLD
    - REJECT

  reasons: []
  provenance:
```

---

## 104. RSCF Proof Capsule

```yaml
RSCF:
  id: K_NSERK

  type: kernel_architecture
  HML: H

  origin_architect: Trang Phan
  steward: Trang Phan

  claim: >
    K_NSERK defines an AMOS neuro-symbolic economic reasoning architecture
    that combines learned market representations, stochastic latent
    dynamics, economics-informed regularization, symbolic distillation,
    uncertainty quantification, and explicit hard constraint governance
    while preserving the separation between economic plausibility,
    mathematical feasibility, formal verification, authority, and
    executable market action.

  claim_class: AMOS_MODEL
  conclusion_class: DERIVED

  source_support:
    ARTEMIS:
      - continuous_time_encoder
      - neural_SDE
      - PDE_regularization
      - market_price_of_risk_regularization
      - symbolic_bottleneck
      - adaptive_conformal_prediction

    AMOS_EXTENSION:
      - FOL_constraint_registry
      - SMT_interface
      - hard_projection_gate
      - authority_gate
      - execution_firewall
      - fail_closed_solver_behavior

  invariants:
    - SOURCE_NOT_EXTENSION
    - SOFT_NOT_HARD
    - MODEL_NOT_MARKET_TRUTH
    - NO_ARBITRAGE_NOT_SIMPLEX
    - P_NOT_Q
    - SYMBOLIC_NOT_CAUSAL
    - CONFORMAL_NOT_RISK_GUARANTEE
    - SOLVER_FAILURE_FAILS_CLOSED
    - MODEL_NOT_AUTHORITY
    - BACKTEST_NOT_LIVE_EDGE
    - FORMAL_SPEC_NOT_FORMAL_PROOF
    - UNKNOWN_NOT_PASS

  dependencies:
    - 02_KERNEL/KERNEL_KERNEL_CONTRACT
    - 02_KERNEL/K_FAIL_CLOSED
    - 02_KERNEL/K_GOVERNANCE
    - 02_KERNEL/K_MATHEMATICAL_RIGOR
    - 03_CONTROL_PLANE
    - 04_RUNTIME
    - 06_REASONING
    - 12_STATE
    - 16_SCHEMAS
    - 17_OBSERVABILITY
    - 18_SECURITY
    - 19_TESTS
    - 21_DOMAINS/08_ECONOMICS

  competing:
    - economic_regularization_vs_hard_model_constraint
    - neural_flexibility_vs_symbolic_fidelity
    - point_accuracy_vs_directional_accuracy
    - physical_measure_vs_risk_neutral_measure
    - projection_vs_rejection
    - standard_vs_adaptive_conformal
    - prediction_quality_vs_economic_value

  falsifiers:
    - ARTEMIS_attributed_SMT_claim
    - soft_loss_promoted_to_absolute_no_arbitrage
    - simplex_constraint_promoted_to_no_arbitrage
    - positive_value_theorem_promoted_to_FTAP
    - failed_solver_returns_unverified_portfolio
    - hardcoded_universal_collateral_ratio
    - automatic_liquidation_without_authority
    - conformal_interval_promoted_to_tail_risk_guarantee
    - backtest_promoted_to_live_edge
    - sorry_promoted_to_formal_proof

  confidence_ceiling:
    architecture: DERIVED
    ARTEMIS_source_summary: SOURCE_GROUNDED
    AMOS_extensions: AMOS_MODEL
    executable_binding: UNKNOWN/GAP
    live_trading_validity: UNKNOWN/GAP
```

---

## 105. Positive Tests

```text
NSERK-P01
Neural forecast violates hard leverage constraint.
EXPECTED:
REJECT candidate.

NSERK-P02
Soft PDE residual is nonzero but all hard execution constraints pass.
EXPECTED:
record economic regularization score;
do not claim no-arbitrage proof.

NSERK-P03
Solver reports infeasible feasible-set intersection.
EXPECTED:
HOLD / REJECT;
no fallback allocation.

NSERK-P04
Candidate satisfies portfolio simplex constraint.
EXPECTED:
portfolio feasibility PASS;
no no-arbitrage claim.

NSERK-P05
Symbolic student closely matches neural teacher.
EXPECTED:
high teacher fidelity;
causal status remains unproven.

NSERK-P06
Adaptive conformal interval achieves target historical coverage.
EXPECTED:
calibration evidence within tested regime;
no universal future coverage claim.

NSERK-P07
Authority is revoked after optimization.
EXPECTED:
execution blocked.

NSERK-P08
Risk-neutral PDE uses physical drift without valid transformation.
EXPECTED:
model-measure inconsistency flagged.

NSERK-P09
Formal Lean theorem is checked without sorry.
EXPECTED:
only exact proposition receives PROVED status.

NSERK-P10
Synthetic DSLOB performance is strong.
EXPECTED:
retain synthetic-regime scope.
```

---

## 106. Negative Tests

```text
NSERK-N01
Claim:
ARTEMIS uses SMT verification.
EXPECTED:
REJECT unless independently sourced.

NSERK-N02
Claim:
ARTEMIS guarantees no arbitrage.
EXPECTED:
REJECT.

NSERK-N03
Claim:
nonnegative weights summing to one prove no-arbitrage.
EXPECTED:
REJECT.

NSERK-N04
Claim:
portfolio collateral ratio must universally exceed 1.25.
EXPECTED:
REJECT.

NSERK-N05
Claim:
positive portfolio market value proves no-arbitrage.
EXPECTED:
REJECT.

NSERK-N06
Claim:
conformal prediction guarantees financial safety.
EXPECTED:
REJECT.

NSERK-N07
Claim:
symbolic expression is causal explanation.
EXPECTED:
REJECT.

NSERK-N08
Claim:
solver success grants execution authority.
EXPECTED:
REJECT.

NSERK-N09
Claim:
solver failure justifies automatic liquidation.
EXPECTED:
REJECT.

NSERK-N10
Claim:
Lean theorem containing sorry is formally verified.
EXPECTED:
REJECT.
```

---

## 107. Adversarial Tests

```text
NSERK-A01 — MEASURE CONFUSION
Train drift under physical data.
Use it directly in risk-neutral pricing PDE.
EXPECTED:
flag P/Q ambiguity.

NSERK-A02 — FALSE FEASIBILITY
Optimizer returns success with residual above tolerance.
EXPECTED:
fail validation.

NSERK-A03 — NAN FALLBACK
Solver receives NaN volatility inputs.
EXPECTED:
fail closed.

NSERK-A04 — STALE CAPITAL
Optimization uses old capital state.
Capital changes before commit.
EXPECTED:
freshness failure.

NSERK-A05 — CONSTRAINT CAPTURE
Model proposes changing its own risk threshold.
EXPECTED:
reject; capability != authority.

NSERK-A06 — CONFORMAL REGIME BREAK
Historical interval coverage is adequate.
Crash-regime coverage collapses.
EXPECTED:
regime degradation visible.

NSERK-A07 — SYMBOLIC MIMICRY
Symbolic rule matches teacher on training data but fails OOS.
EXPECTED:
fidelity downgrade.

NSERK-A08 — BACKTEST LEAKAGE
Normalization uses future samples.
EXPECTED:
experiment invalid.

NSERK-A09 — SYNTHETIC OVERGENERALIZATION
Strong DSLOB result claimed as live-market proof.
EXPECTED:
reject generalization.

NSERK-A10 — AUTOMATIC HEDGE ESCALATION
Solver timeout invokes an unauthorized hedge.
EXPECTED:
critical governance violation.
```

---

## 108. Corrected Python Reference Implementation

```python
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

import numpy as np
import scipy.optimize as opt


class SolveStatus(str, Enum):
    FEASIBLE = "FEASIBLE"
    INFEASIBLE = "INFEASIBLE"
    NUMERICAL_FAILURE = "NUMERICAL_FAILURE"
    INVALID_INPUT = "INVALID_INPUT"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class ProjectionResult:
    status: SolveStatus
    weights: Optional[np.ndarray]
    objective_value: Optional[float]
    budget_residual: Optional[float]
    risk_residual: Optional[float]
    message: str


class NeuroSymbolicEconomicConstraintKernel:
    """
    Reference AMOS_MODEL implementation for bounded portfolio projection.

    This class demonstrates fail-closed constraint handling.
    It does NOT establish no-arbitrage, solvency, authority, live trading
    validity, or production implementation.
    """

    def __init__(
        self,
        num_assets: int,
        max_weighted_risk: float,
        tolerance: float = 1e-8,
    ):
        if num_assets <= 0:
            raise ValueError("num_assets must be positive")

        if not np.isfinite(max_weighted_risk):
            raise ValueError("max_weighted_risk must be finite")

        if tolerance <= 0:
            raise ValueError("tolerance must be positive")

        self.n = num_assets
        self.max_weighted_risk = float(max_weighted_risk)
        self.tolerance = float(tolerance)

    def project_allocation(
        self,
        raw_weights: np.ndarray,
        risk_coefficients: np.ndarray,
    ) -> ProjectionResult:

        raw = np.asarray(raw_weights, dtype=float)
        risk = np.asarray(risk_coefficients, dtype=float)

        if raw.shape != (self.n,) or risk.shape != (self.n,):
            return ProjectionResult(
                status=SolveStatus.INVALID_INPUT,
                weights=None,
                objective_value=None,
                budget_residual=None,
                risk_residual=None,
                message="shape mismatch",
            )

        if not np.all(np.isfinite(raw)) or not np.all(np.isfinite(risk)):
            return ProjectionResult(
                status=SolveStatus.INVALID_INPUT,
                weights=None,
                objective_value=None,
                budget_residual=None,
                risk_residual=None,
                message="non-finite input",
            )

        if np.any(risk < 0):
            return ProjectionResult(
                status=SolveStatus.INVALID_INPUT,
                weights=None,
                objective_value=None,
                budget_residual=None,
                risk_residual=None,
                message="risk coefficients must be non-negative",
            )

        minimum_possible_risk = float(np.min(risk))

        if minimum_possible_risk > self.max_weighted_risk + self.tolerance:
            return ProjectionResult(
                status=SolveStatus.INFEASIBLE,
                weights=None,
                objective_value=None,
                budget_residual=None,
                risk_residual=minimum_possible_risk - self.max_weighted_risk,
                message="risk constraint infeasible under long-only full-investment assumptions",
            )

        clipped = np.maximum(raw, 0.0)

        if clipped.sum() <= self.tolerance:
            x0 = np.full(self.n, 1.0 / self.n)
        else:
            x0 = clipped / clipped.sum()

        def objective(w: np.ndarray) -> float:
            delta = w - raw
            return 0.5 * float(delta @ delta)

        def gradient(w: np.ndarray) -> np.ndarray:
            return w - raw

        constraints = [
            {
                "type": "eq",
                "fun": lambda w: float(np.sum(w) - 1.0),
            },
            {
                "type": "ineq",
                "fun": lambda w: float(
                    self.max_weighted_risk - np.dot(w, risk)
                ),
            },
        ]

        bounds = [(0.0, 1.0)] * self.n

        result = opt.minimize(
            objective,
            x0,
            jac=gradient,
            constraints=constraints,
            bounds=bounds,
            method="SLSQP",
            options={
                "ftol": self.tolerance,
                "maxiter": 1000,
            },
        )

        if not result.success:
            return ProjectionResult(
                status=SolveStatus.NUMERICAL_FAILURE,
                weights=None,
                objective_value=None,
                budget_residual=None,
                risk_residual=None,
                message=str(result.message),
            )

        w = np.asarray(result.x, dtype=float)

        budget_residual = abs(float(np.sum(w) - 1.0))
        weighted_risk = float(np.dot(w, risk))
        risk_residual = max(
            0.0,
            weighted_risk - self.max_weighted_risk,
        )

        if (
            np.any(w < -self.tolerance)
            or budget_residual > self.tolerance
            or risk_residual > self.tolerance
        ):
            return ProjectionResult(
                status=SolveStatus.NUMERICAL_FAILURE,
                weights=None,
                objective_value=float(result.fun),
                budget_residual=budget_residual,
                risk_residual=risk_residual,
                message="solver returned candidate outside validation tolerance",
            )

        return ProjectionResult(
            status=SolveStatus.FEASIBLE,
            weights=w,
            objective_value=float(result.fun),
            budget_residual=budget_residual,
            risk_residual=risk_residual,
            message="feasible constrained projection",
        )
```

---

## 109. Formal Verification Specification

Formal verification is separated into narrow propositions.

```yaml
formal_verification_targets:

  NSERK-FV-001:
    proposition: >
      Under a long-only portfolio contract with nonnegative weights
      summing to one and strictly positive asset prices, portfolio
      marked value is strictly positive.
    meaning: portfolio_value_property
    meaning_not: no_arbitrage
    status: UNPROVED_IN_THIS_ARTIFACT

  NSERK-FV-002:
    proposition: >
      A projection result marked FEASIBLE satisfies every encoded hard
      constraint within declared numerical tolerance.
    meaning: solver_postcondition
    status: UNPROVED_IN_THIS_ARTIFACT

  NSERK-FV-003:
    proposition: >
      A solver failure cannot produce an executable allocation from the
      reference fail-closed interface.
    meaning: fail_closed_control_property
    status: UNPROVED_IN_THIS_ARTIFACT

  NSERK-FV-004:
    proposition: >
      Execution authority is required independently of mathematical
      feasibility.
    meaning: AMOS_governance_invariant
    status: SPECIFIED_NOT_FORMALLY_PROVED
```

---

## 110. Formal Verification Firewall

```text
NO ARBITRAGE
!=
POSITIVE PORTFOLIO VALUE

SMT SAT
!=
ECONOMIC VALIDITY

QP FEASIBLE
!=
OPTIMAL UNDER TRUE MARKET DYNAMICS

LEAN COMPILES
!=
ASSUMPTIONS TRUE

PROVED PROPERTY
!=
SYSTEM VERIFIED

FORMAL MODEL
!=
LIVE MARKET
```

---

## 111. MECE Ownership

| Capability | Primary Owner |
|---|---|
| neuro-symbolic economic kernel semantics | `02_KERNEL/K_NSERK` |
| formal mathematical rigor | `02_KERNEL` mathematical rigor layer |
| fail-closed semantics | `02_KERNEL/K_FAIL_CLOSED` |
| authority | `03_CONTROL_PLANE` |
| runtime model execution | `04_RUNTIME` |
| generic reasoning | `06_REASONING` |
| market/economic domain semantics | `21_DOMAINS/08_ECONOMICS` |
| state persistence | `12_STATE` |
| schemas | `16_SCHEMAS` |
| telemetry | `17_OBSERVABILITY` |
| security | `18_SECURITY` |
| executable tests | `19_TESTS` |
| live operational procedures | `20_OPERATIONS` |

---

## 112. Kernel Invariants

```text
INV-NSERK-001
SOURCE_DERIVATION_MUST_BE_PRESERVED

INV-NSERK-002
SOFT_CONSTRAINT_NOT_HARD_CERTIFICATE

INV-NSERK-003
RISK_NEUTRAL_AND_PHYSICAL_MEASURES_NOT_SILENTLY_MERGED

INV-NSERK-004
PORTFOLIO_FEASIBILITY_NOT_NO_ARBITRAGE

INV-NSERK-005
SYMBOLIC_FIDELITY_NOT_CAUSAL_TRUTH

INV-NSERK-006
CONFORMAL_COVERAGE_NOT_FINANCIAL_SAFETY

INV-NSERK-007
SOLVER_FAILURE_FAILS_CLOSED

INV-NSERK-008
NO_UNAUTHORIZED_AUTOMATIC_HEDGE

INV-NSERK-009
NO_UNAUTHORIZED_AUTOMATIC_LIQUIDATION

INV-NSERK-010
NO_HARDCODED_UNIVERSAL_MARGIN_RATIO

INV-NSERK-011
MODEL_OUTPUT_NOT_AUTHORITY

INV-NSERK-012
POINT_IN_TIME_DATA_INTEGRITY

INV-NSERK-013
REGIME_VALIDITY_PRESERVED

INV-NSERK-014
FORMAL_SPEC_NOT_FORMAL_PROOF

INV-NSERK-015
UNKNOWN_GAP_NOT_PASS
```

---

## 113. Corrected Legacy Claims

The following earlier claims are rejected or narrowed:

```text
"ARTEMIS combines FOL and SMT"
→ REJECTED AS SOURCE CLAIM.
  May exist only as AMOS_EXTENSION.

"ARTEMIS eliminates hallucinated economic policies"
→ REJECTED.
  It introduces economic inductive biases and interpretability mechanisms.

"formal semantic barrier certificates"
→ NOT ESTABLISHED BY ARTEMIS SOURCE.

"exact inference-time projector"
→ NOT ESTABLISHED AS CORE ARTEMIS SOURCE COMPONENT.

"strict no-arbitrage guarantee"
→ REJECTED.

"portfolio simplex = no-arbitrage"
→ REJECTED.

"collateral ratio >= 1.25 is a kernel invariant"
→ REJECTED.

"SMT bounds failure triggers market-neutral hedge"
→ REJECTED.

"recovery means automatic liquidation to sovereign reserves"
→ REJECTED.

"Lean positive-value theorem proves no-arbitrage"
→ REJECTED.

"Lean code with sorry is formal verification"
→ REJECTED.

"verified with 10,000 crash simulations"
→ NOT ESTABLISHED WITHOUT EXECUTION EVIDENCE.

"guarantees absolute economic validity"
→ REJECTED.

"formally certified execution"
→ REJECTED WITHOUT FORMAL + RUNTIME + AUTHORITY EVIDENCE.
```

---

## 114. Known Gaps

```yaml
known_gaps:

  NSERK-GAP-001:
    class: CRITICAL
    issue: >
      Executable binding of K_NSERK to a production AMOS runtime has
      not been established by this specification.
    status: UNKNOWN/GAP

  NSERK-GAP-002:
    class: DECISION_RELEVANT
    issue: >
      ARTEMIS economics-informed losses do not by themselves provide a
      formal proof of global no-arbitrage.
    status: SOURCE_LIMITATION

  NSERK-GAP-003:
    class: DECISION_RELEVANT
    issue: >
      Identification of the risk-neutral drift from learned physical
      market dynamics remains model-dependent.
    status: MODEL_SPECIFIC

  NSERK-GAP-004:
    class: DECISION_RELEVANT
    issue: >
      Adaptive conformal coverage under strongly nonstationary financial
      regimes requires method-specific validation.
    status: REGIME_SPECIFIC

  NSERK-GAP-005:
    class: DECISION_RELEVANT
    issue: >
      Symbolic bottleneck fidelity does not establish causal validity.
    status: EPISTEMIC_BOUNDARY

  NSERK-GAP-006:
    class: DECISION_RELEVANT
    issue: >
      No universal collateral, leverage, risk, or liquidity thresholds
      are established.
    status: POLICY_SPECIFIC

  NSERK-GAP-007:
    class: DECISION_RELEVANT
    issue: >
      Formal Lean/SMT verification artifacts for this kernel are not
      established.
    status: NOT_ESTABLISHED

  NSERK-GAP-008:
    class: DECISION_RELEVANT
    issue: >
      ARTEMIS benchmark findings require reproduction before promotion
      from SOURCE_CLAIM to OBSERVATION in AMOS.
    status: REPRODUCTION_REQUIRED

  NSERK-GAP-009:
    class: DECISION_RELEVANT
    issue: >
      Live trading edge, transaction-cost robustness, market-impact
      robustness, and deployment validity are not established.
    status: UNKNOWN/GAP
```

---

## 115. Falsifiers

This specification is violated if a conforming implementation:

```text
attributes SMT/FOL machinery to ARTEMIS without source evidence;

calls a soft PDE penalty a formal no-arbitrage guarantee;

treats the physical and risk-neutral drifts as identical without
declared assumptions;

treats simplex portfolio weights as proof of no-arbitrage;

uses one fixed collateral threshold as a universal law;

executes an unverified fallback after solver failure;

automatically hedges or liquidates without explicit authority;

treats symbolic distillation as causal explanation;

treats conformal intervals as tail-risk guarantees;

uses future information in model training or testing;

promotes synthetic benchmark results into live-market evidence;

treats a theorem containing sorry as formally verified;

treats mathematical feasibility as execution authority;

represents SOURCE_CLAIM benchmark numbers as reproduced observations
without executable evidence.
```

---

## 116. Nine-Part Contract

## 116.1 ROLE

Provide governed neuro-symbolic economic reasoning in which learned predictions are constrained by explicit economic, mathematical, risk, policy, and authority contracts.

## 116.2 INTERFACES

```text
IF-NSERK-OBSERVATION
IF-NSERK-MODEL
IF-NSERK-SYMBOLIC
IF-NSERK-CONSTRAINT
IF-NSERK-UNCERTAINTY
IF-NSERK-PROPOSAL
IF-NSERK-RECEIPT
```

No specific Arrow IPC or broker protocol is canonically required by this kernel.

## 116.3 DEPENDENCIES

```text
02_KERNEL/KERNEL_KERNEL_CONTRACT
02_KERNEL/K_FAIL_CLOSED
02_KERNEL/K_GOVERNANCE
03_CONTROL_PLANE
04_RUNTIME
06_REASONING
12_STATE
16_SCHEMAS
17_OBSERVABILITY
18_SECURITY
19_TESTS
21_DOMAINS/08_ECONOMICS
```

## 116.4 INVARIANTS

All invariants in Section 112.

## 116.5 AUTHORITY

`K_NSERK` has proposal and validation semantics only.

It does not grant itself external market authority.

## 116.6 PROVENANCE

```text
Origin Architect / Steward:
Trang Phan

Source influence:
ARTEMIS, arXiv:2603.18107v1

AMOS-specific governance:
AMOS_MODEL
```

## 116.7 TESTS

Tests MUST be represented as:

```text
SPECIFIED
IMPLEMENTED
EXECUTED
PASSED
FAILED
UNKNOWN
```

No numerical test count is claimed without execution evidence.

## 116.8 FAILURE

Any unresolved hard constraint, invalid data state, solver failure, stale authority, or unknown commit-critical premise causes:

```text
HOLD / REJECT
```

rather than speculative execution.

## 116.9 RECOVERY

Recovery is policy-bound and may include:

```text
recompute
reproject
reduce scope
block new risk
invoke preauthorized hedge
invoke preauthorized liquidation
escalate
```

No recovery action is automatically authorized by the kernel.

---

## 117. Navigation

## Kernel

```text
[[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
[[02_KERNEL/KERNEL_KERNEL_CONTRACT|KERNEL_KERNEL_CONTRACT]]
[[02_KERNEL/K_FAIL_CLOSED|K_FAIL_CLOSED]]
[[02_KERNEL/K_FAILURE_RECOVERY|K_FAILURE_RECOVERY]]
[[02_KERNEL/K_GOVERNANCE|K_GOVERNANCE]]
[[02_KERNEL/K_MVCC|K_MVCC]]
[[02_KERNEL/K_CAS|K_CAS]]
```

## Reasoning

```text
[[06_REASONING/REASONING_REASONING_CONTRACT|REASONING_REASONING_CONTRACT]]
```

## Economics

```text
[[21_DOMAINS/08_ECONOMICS/08_ECONOMICS_MOC|08_ECONOMICS_MOC]]
```

## State / Observability / Tests

```text
[[12_STATE/12_STATE_MOC|12_STATE_MOC]]
[[16_SCHEMAS/16_SCHEMAS_MOC|16_SCHEMAS_MOC]]
[[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
[[19_TESTS/19_TESTS_MOC|19_TESTS_MOC]]
```

---

## 118. Final Status

```yaml
artifact_status:
  artifact: K_NSERK
  version: 3.0.0

  origin_architect: Trang Phan
  steward: Trang Phan
  target: AMOS_CORE_v4.4

  status: ACTIVE_SPECIFICATION
  epistemic_class: AMOS_MODEL
  conclusion_class: DERIVED
  canonical_status: ACTIVE_CANON_CANDIDATE

  ARTEMIS_source_boundary: DEFINED
  AMOS_extension_boundary: DEFINED

  continuous_time_encoder: SOURCE_GROUNDED
  neural_SDE: SOURCE_GROUNDED
  PDE_regularization: SOURCE_GROUNDED
  market_price_of_risk_regularization: SOURCE_GROUNDED
  symbolic_bottleneck: SOURCE_GROUNDED
  adaptive_conformal_prediction: SOURCE_GROUNDED

  FOL_engine: AMOS_EXTENSION
  SMT_engine: AMOS_EXTENSION
  hard_projection_gate: AMOS_EXTENSION
  authority_gate: AMOS_EXTENSION
  execution_firewall: AMOS_EXTENSION

  absolute_economic_validity: REJECTED
  strict_no_arbitrage_guarantee: REJECTED
  simplex_equals_no_arbitrage: REJECTED
  universal_collateral_1_25: REJECTED
  automatic_solver_fallback: REJECTED
  automatic_hedge_on_failure: REJECTED
  automatic_liquidation: REJECTED
  Lean_sorry_equals_verification: REJECTED
  positive_value_equals_no_arbitrage: REJECTED

  executable_binding: NOT_ESTABLISHED
  formal_verification: NOT_ESTABLISHED
  benchmark_reproduction: NOT_ESTABLISHED
  live_trading_edge: NOT_ESTABLISHED
  deployment_validation: NOT_ESTABLISHED

  final_conclusion: DERIVED
```

---

**Origin Architect / Steward: Trang Phan**