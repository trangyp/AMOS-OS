---
title: "Vault Domain Knowledge — Amos C02 Math Compute Master"
type: reference
source: 07_SKILLS/amos-c02-math-compute-master/references
tags: [reference, amos-c02-math-compute-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# amos-c02-math-compute-master — Vault-Sourced Domain Knowledge

> Load this reference only when detailed domain knowledge is needed.
> This content was moved from SKILL.md for progressive loading.

---

> **Source**: `11_KNOWLEDGE/AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

# AMOS C02 — Math & Compute Master Knowledge

> **Epistemic boundary**
>
> This file replaces the synthetic `x100k` micro-layer expansion with substantive mathematics
> and computation knowledge. It does not claim encyclopedic completeness. Established theorems,
> standard numerical practice, model-dependent results, method-selection judgment calls,
> AMOS/Trang abstractions, and governance rules are kept separate.
>
> Every equation class is typed explicitly: `SOURCE_CANON` for established mathematical results,
> `AMOS_MODEL` for AMOS/Trang constructs that require validation before being treated as fact.
>
> Mathematical outputs are always precision-, conditioning-, regime-, and assumption-dependent.
> No result may be reported without its error characterization; no optimum claimed without a
> convexity or hardness statement; no statistical estimate without uncertainty quantification.

## 0. C02 Knowledge Contract

### 0.1 Claim classes
- **VERIFIED** — established theorem or strongly supported empirical/numerical result within a stated regime.
- **DERIVED** — mathematical consequence of stated premises/model.
- **MODEL** — representation useful within stated scope.
- **CONDITIONAL** — dependent on explicit assumptions, regime, or scenario.
- **COMPETING** — unresolved alternatives (method choice, interpretation).
- **UNKNOWN/GAP** — insufficient evidence or unresolved question.

### 0.2 Evidence classes
`THEOREM`, `STANDARD_PRACTICE`, `NUMERICAL_EXPERIMENT`, `DERIVED`, `MODEL`, `SCENARIO`,
`SOURCE_CLAIM`, `AMOS_MODEL`, `UNKNOWN`.

Equation typing rule:
- **SOURCE_CANON** — appears in standard references; derivation or proof exists in the literature.
- **AMOS_MODEL** — proposed by AMOS/Trang sources; usable as scaffolding only until validated.

### 0.3 C02 H-level ownership
1. Problem Framing, Dimensional Analysis & Model Selection
2. Numerical Methods: Error, Conditioning, Stability, Convergence
3. Probability & Statistics Kernel
4. Optimization & Decision Formulation
5. Complexity, Scaling & Algorithmic Hardness
6. Control Systems & Feedback Reasoning
7. Signal Processing & Spectral Methods
8. Simulation, Validation & Uncertainty Reporting
9. Meta-Control, Error Budgets & Decision Interface
10. AMOS/Trang Math Research Bridge

A topic has one primary owner. Cross-links are references, not duplicated substantive sections.

### 0.4 Standard knowledge node schema
Where applicable:
**definition → state variables → governing relations → assumptions → mechanisms → observables →
data sources → empirical status → scope/regime → uncertainty → failure modes → competing models →
falsifiers → dependencies → decision relevance → AMOS bridge**.

---

# H1 (F01) — Problem Framing, Dimensional Analysis & Model Selection

## M1. Framing Before Computing

### L1. Question typing
Before any computation, classify:
- what quantity is sought;
- what is optimized, constrained, assumed fixed;
- whether the answer must be exact, approximate, or order-of-magnitude;
- whether the problem is descriptive (characterize data) or inferential (claim beyond data).

Misframing is unrecoverable downstream: a correctly solved wrong formulation produces confident,
wrong answers.

### L2. Dimensional analysis
Unit consistency is the cheapest correctness filter in existence.

Rule (SOURCE_CANON): every physical equation must be homogeneous in dimensions; any dimensionally
inconsistent expression is invalid regardless of how it was derived.

Most fabricated-precision errors die here if allowed to. Run dimensional checks before numerics,
always.

### L3. Back-of-envelope estimation
Order-of-magnitude sanity checks precede detailed computation:
- bound each term roughly;
- identify dominant terms;
- verify the final magnitude is plausible against independent reference points.

An exact-looking result that violates a rough envelope bound signals an input, unit, or model error,
not a discovery.

### L4. Coupled-system decomposition
Decompose along REAL coupling boundaries, not convenient ones.

Two subsystems joined by a strong feedback loop are ONE system for stability purposes.
Decomposing them anyway produces individually verified, jointly wrong answers.

**Class:** STANDARD_PRACTICE (engineering-math kernel discipline). Worked counterexample from
source lineage: thermal + structural solvers run separately on a bracket converged individually,
but thermal-expansion feedback into structural load was the strongest coupling — stress report
wrong by ~40% until co-simulation forced by an honest coupling map.

---

## M2. Model Selection

### L1. Selection discipline
Model choice is a governed step, not a reflex:
1. match model family to the data-generating process;
2. state why this family over alternatives;
3. record assumptions the model makes;
4. plan diagnostics that could falsify the choice.

### L2. Sensitivity analysis
Determine which variables dominate the output before investing in precision elsewhere.
If output variance is dominated by one uncertain input, refining other inputs is wasted effort.

Standard tools: one-at-a-time sweeps, variance-based indices, Monte Carlo sensitivity.

### L3. The x100k tier map as routing structure
The x100k expansion defines 7 tiers of checkpoints:

| Tier | Function |
|------|----------|
| numeric sanity | valid ranges, units, no NaN/inf |
| symbolic structure | equation form, dimensional consistency |
| model selection | right mathematical model for the phenomenon |
| algorithm design | computational approach |
| complexity/scaling | O(n), memory, convergence behavior |
| simulation/validation | known-case tests, Monte Carlo, sensitivity |
| decision interface | translate numbers into decisions with confidence |

**Class:** AMOS_MODEL. Anti-overclaim rule from source: the layers provide STRUCTURE for routing,
not intelligence. Each layer is a checkpoint, not a solver. Actual computation requires external
tools; the framework ensures nothing skips validation.

---

# H2 (F02) — Numerical Methods: Error, Conditioning, Stability, Convergence

## M1. Core Disciplines

Every numerical design must state four disciplines (Numerical Methods Engine):

| Discipline | Question |
|---|---|
| Error control | Truncation vs round-off budget; how accumulated error is bounded |
| Conditioning | Condition number of the problem; ill-conditioned? reformulate |
| Stability | Forward/backward stability of the chosen algorithm; stiff-system handling |
| Convergence | Rate, criteria, termination tests; guaranteed vs empirical |

### L1. Error budget
Total numerical error combines:
- truncation/discretization error (model of the continuum);
- round-off error (finite arithmetic);
- accumulated propagation through composed steps.

Allocate tolerances up front; verify post-run against the allocation. When chaining methods
(discretize → solve → post-process), propagate the budget through the chain rather than resetting it.

### L2. Conditioning
Condition number measures how much output error amplifies input perturbation.

For a linear system `Ax = b`:
`κ(A) = ||A|| · ||A⁻¹||`.

Large `κ` means small input errors become large solution errors — no algorithm fixes an
ill-conditioned *problem*; reformulation (scaling, preconditioning) is required.

Estimate conditioning before solving; flag `κ ≫ 1`.

**Class:** SOURCE_CANON.

---

## M2. Method Families

Conceptual coverage (design layer; not competing with LAPACK/PETSc/FFTW at machine level):
- root-finding & nonlinear systems;
- linear systems (direct/iterative);
- eigenproblems;
- interpolation/approximation;
- quadrature/differentiation;
- ODEs (IVP/BVP; stiff/non-stiff);
- PDE discretizations (FDM/FEM/FVM/spectral);
- continuous optimization;
- FFT/spectral transforms;
- random number generation & Monte Carlo.

### L1. Stiff systems example (from source)
A stiff ODE from kinetics → implicit method selected with stability rationale; explicit Euler
rejected by the stability gate because its stability region cannot accommodate fast modes at
practical step sizes.

**Class:** STANDARD_PRACTICE.

### L2. Iterative solves
Large sparse solve → Krylov methods (CG/GMRES) with preconditioner choice justified;
residual history reported, not just iteration count.

"It stopped" ≠ "it converged." Convergence evidence = residual trends against a stated criterion.

### L3. Numerical-methods gates
1. Any result presented without error characterization? → invalid output.
2. Ill-conditioned system solved without comment? → blocked.
3. Iterative solver terminated without convergence criterion stated? → blocked.
4. Machine-level performance claims made? → out of scope; remove.

---

# H3 (F03) — Probability & Statistics Kernel

## M1. Probability Fundamentals

### L1. Kolmogorov axioms
```
P(A) ≥ 0                                  [non-negativity]
P(Ω) = 1                                  [normalization]
P(∪ Aᵢ) = Σ P(Aᵢ)   for disjoint events    [countable additivity]
```
**Class:** SOURCE_CANON.

### L2. Conditional probability and independence
```
P(A|B) = P(A ∩ B) / P(B)
A ⊥ B  ⟺  P(A ∩ B) = P(A)·P(B)
```

### L3. Law of total probability
```
P(B) = Σᵢ P(B|Aᵢ)·P(Aᵢ)     where {Aᵢ} partitions Ω
```

### L4. Bayes' theorem
```
P(H|E) = P(E|H)·P(H) / P(E)

P(H|E)  posterior given evidence
P(E|H)  likelihood
P(H)    prior
P(E)    marginal likelihood = Σⱼ P(E|Hⱼ)·P(Hⱼ)
```
Failure-mode guard: base-rate neglect. Ignoring `P(H)` and reading `P(E|H)` as `P(H|E)` is the
canonical fallacy — mandatory in screening/diagnosis contexts.

All of M1: **Class:** SOURCE_CANON.

---

## M2. Random Variables & Distribution Selection

### L1. Moments
```
E[X] = Σ x·P(X=x)        (discrete)
E[X] = ∫ x·f(x) dx       (continuous)
Var(X) = E[(X - E[X])²] = E[X²] − (E[X])²
Cov(X,Y) = E[(X−E[X])(Y−E[Y])]
Corr(X,Y) = Cov(X,Y)/(σ_X·σ_Y)
```
**Class:** SOURCE_CANON.

### L2. Distribution selection rules

| Data type / process | Recommended distribution | Key parameters |
|---|---|---|
| Binary outcome, single trial | Bernoulli | p |
| Count of successes in n trials | Binomial | n, p |
| Rare events in fixed interval | Poisson | λ |
| Trials until first success | Geometric | p |
| Continuous waiting times | Exponential | λ |
| Bounded proportions | Beta | α, β |
| Sums of many effects | Normal (approx.) | μ, σ |

Match distribution to the data-generating process; state the mismatch when approximating.

---

## M3. Inference

### L1. Descriptive vs inferential gate
A descriptive statistic (sample mean) is NOT an inferential claim about the population unless
accompanied by uncertainty quantification. Language and methods must follow the classification.

### L2. Confidence intervals
```
CI_{1−α} = x̄ ± z_{α/2}·(σ/√n)
```
Unknown σ / small samples: use t-distribution, `CI = x̄ ± t_{α/2,n−1}·(s/√n)`.

Interpretation: frequentist CI means "if repeated, ~(1−α) of intervals contain true θ" — not a
probability statement about θ itself.

### L3. Hypothesis testing
```
T = (x̄ − μ₀)/(s/√n) ~ t_{n−1} under H₀
p-value = P(|T| ≥ |t_observed| | H₀)
```
Type I error (α): rejecting true H₀. Type II (β): failing to reject false H₀.
Power = 1 − β.

Common tests: t-tests, ANOVA, chi-square, proportion z-tests, nonparametric alternatives
(Mann–Whitney, Kruskal–Wallis, Wilcoxon).

Failure-mode guard — p-hacking: pre-register hypotheses; apply Bonferroni or FDR correction for
multiple comparisons; never selectively report significant results.

### L4. Bayesian updating
```
Posterior ∝ Likelihood × Prior
P(θ|D) = P(D|θ)·P(θ) / P(D)
```

Conjugate example (Beta-Binomial):
```
Prior:      θ ~ Beta(α, β)
Likelihood: D ~ Binomial(n, θ)
Posterior:  θ|D ~ Beta(α+k, β+n−k)
```
Credible interval: direct probability statement about θ — contrast with frequentist CI.

Computation: MCMC (Metropolis-Hastings, HMC, NUTS), variational inference, analytic posteriors
for conjugate models only.

Guard: prior-sensitivity analysis mandatory — disclose priors, test conclusions under weakly
informative and reference alternatives.

### L5. Regression
Linear regression `Y = β₀ + β₁X + ε` with linearity, homoscedasticity, independence, residual
normality assumptions. GLMs extend via link functions. Diagnostics: residuals, Q-Q plots, leverage/
Cook's distance, multicollinearity (VIF). Coefficients reported with confidence intervals, never
bare point estimates.

M3: **Class:** SOURCE_CANON.

---

## M4. Stochastic System State Models

### L1. Generic stochastic evolution (from vault equations)
```
S_{t+1} = C(F(S_t, U_t))

S_t = system state; U_t = stochastic input;
F = forward evolution; C = constraint/correction operator
```
**Class:** AMOS_MODEL (structural scaffold used across UBCAR-style routing; validate F and C per
application before treating outputs as predictions).

### L2. Feedback-ratio stability proxy
```
stability = negative_feedback / (positive_feedback + ε)
positive > negative → collapse risk; negative > positive → stable regime
```
**Class:** AMOS_MODEL. Useful heuristic only; rigorous stability requires the dynamical-systems
analysis in H6/F06.

### L3. Contract-valid statistical output
No output missing `uncertainty_quantification` or `assumption_summary` is contract-valid.
Risk notes from source: false precision if inputs are very uncertain (never report 5 significant
figures for a ±50% input); easy to overfit without domain context.

Statistical safety constraints: no medical diagnosis replacement, no financial advice, no
overconfident claims, correlation ≠ causation, assumption transparency.

---

# H4 (F04) — Optimization & Decision Formulation

## M1. Structural Components

Any optimization formulation must specify:
decision_variables · objective_function · constraints · parameters_and_data ·
solution · sensitivity_and_robustness.

Distinguish what is optimized, what is constrained, what is assumed fixed. A missing component
invalidates the interpretation even if a solver returns numbers.

## M2. Problem Classes

LP (linear) · NLP (nonlinear) · integer/MIP · convex optimization · multi-objective
(Pareto fronts, weighted sums, ε-constraint) · stochastic/robust optimization ·
heuristics/metaheuristics for combinatorial scale.

Method-class matching: convexity present? integrality required? uncertainty modeled?
State why the chosen class fits.

### L1. Convexity and global optima
For convex problems, any local minimum is globally optimal (SOURCE_CANON).

Governance hard rule: **no guaranteed-global-optimum claims for nonconvex, integer, or large-scale
problems.** Heuristic solutions carry bound-gap reporting where bounds exist.

### L2. Worked examples (source lineage)
- Fleet charging schedule → MIP (integer charger assignments, time-window constraints);
  acknowledge NP-hardness; propose heuristic + bound gap reporting.
- "Which portfolio maximizes return?" → governance gate fires: no financial advice; reframe as
  Pareto risk-return surface with explicit non-advice disclaimer.
- Multi-objective → expose the trade-off front rather than collapsing weights silently.


## Vault-Sourced Domain Content

> Source: `11_KNOWLEDGE/AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE.md` (30478 bytes in vault)

### 0.1 Claim Classes

- **VERIFIED** — established theorem or strongly supported empirical/numerical result within a stated regime.
- **DERIVED** — mathematical consequence of stated premises/model.
- **MODEL** — representation useful within stated scope.
- **CONDITIONAL** — dependent on explicit assumptions, regime, or scenario.
- **COMPETING** — unresolved alternatives (method choice, interpretation).
- **UNKNOWN/GAP** — insufficient evidence or unresolved question.

### 0.2 Evidence Classes

`THEOREM`, `STANDARD_PRACTICE`, `NUMERICAL_EXPERIMENT`, `DERIVED`, `MODEL`, `SCENARIO`,
`SOURCE_CLAIM`, `AMOS_MODEL`, `UNKNOWN`.

Equation typing rule:
- **SOURCE_CANON** — appears in standard references; derivation or proof exists in the literature.
- **AMOS_MODEL** — proposed by AMOS/Trang sources; usable as scaffolding only until validated.

### 0.4 Standard Knowledge Node Schema

Where applicable:
**definition → state variables → governing relations → assumptions → mechanisms → observables →
data sources → empirical status → scope/regime → uncertainty → failure modes → competing models →
falsifiers → dependencies → decision relevance → AMOS bridge**.

---

# H1 (F01) — Problem Framing, Dimensional Analysis & Model Selection

### L1. Selection Discipline

Model choice is a governed step, not a reflex:
1. match model family to the data-generating process;
2. state why this family over alternatives;
3. record assumptions the model makes;
4. plan diagnostics that could falsify the choice.

### M1. Core Disciplines

Every numerical design must state four disciplines (Numerical Methods Engine):

| Discipline | Question |
|---|---|
| Error control | Truncation vs round-off budget; how accumulated error is bounded |
| Conditioning | Condition number of the problem; ill-conditioned? reformulate |
| Stability | Forward/backward stability of the chosen algorithm; stiff-system handling |
| Convergence | Rate, criteria, termination tests; guaranteed vs empirical |

### L3. Numerical-Methods Gates

1. Any result presented without error characterization? → invalid output.
2. Ill-conditioned system solved without comment? → blocked.
3. Iterative solver terminated without convergence criterion stated? → blocked.
4. Machine-level performance claims made? → out of scope; remove.

---

# H3 (F03) — Probability & Statistics Kernel

### L1. Kolmogorov Axioms

```
P(A) ≥ 0                                  [non-negativity]
P(Ω) = 1                                  [normalization]
P(∪ Aᵢ) = Σ P(Aᵢ)   for disjoint events    [countable additivity]
```
**Class:** SOURCE_CANON.

### L3. Law Of Total Probability

```
P(B) = Σᵢ P(B|Aᵢ)·P(Aᵢ)     where {Aᵢ} partitions Ω
```

### L1. Descriptive Vs Inferential Gate

A descriptive statistic (sample mean) is NOT an inferential claim about the population unless
accompanied by uncertainty quantification. Language and methods must follow the classification.

### L1. Generic Stochastic Evolution (From Vault Equations)

```
S_{t+1} = C(F(S_t, U_t))

S_t = system state; U_t = stochastic input;
F = forward evolution; C = constraint/correction operator
```
**Class:** AMOS_MODEL (structural scaffold used across UBCAR-style routing; validate F and C per
application before treating outputs as predictions).

### L3. Contract-Valid Statistical Output

No output missing `uncertainty_quantification` or `assumption_summary` is contract-valid.
Risk notes from source: false precision if inputs are very uncertain (never report 5 significant
figures for a ±50% input); easy to overfit without domain context.

Statistical safety constraints: no medical diagnosis replacement, no financial advice, no
overconfident claims, correlation ≠ causation, assumption transparency.

---

# H4 (F04) — Optimization & Decision Formulation

### M3. Optimization Governance Gates

1. Convexity verified before claiming a global optimum?
2. Integrality/combinatorial hardness acknowledged?
3. Objective aligned with real-world purpose, not a proxy?
4. All assumptions stated; data limitations disclosed?
5. Output framed as decision support, never autonomous action?
6. Uncertainty propagated into the recommendation, not averaged away?

Objective-alignment check: flag whenever the mathematical objective diverges from the actual
decision purpose (proxy-objective drift is a top failure mode).

---

# H5 (F05) — Complexity, Scaling & Algorithmic Hardness

### M3. Practical Scaling Discipline

Asymptotic class ≠ runtime. Report:
- measured scaling behavior on representative inputs;
- memory footprint;
- convergence cost for iterative methods;
- where the crossover between competing algorithms lies.

Complexity claims feed the x100k `complexity_and_scaling` tier; every claim there is a checkpoint
to be validated empirically, not asserted.

---

# H6 (F06) — Control Systems & Feedback Reasoning

### M1. Scope

Owned here at summary level (detailed DSP lives in signal-processing skills):
- filtering: FIR/IIR/Kalman;
- transforms: FFT family;
- spectral estimation;
- noise suppression: spectral subtraction with floor;
- feature extraction (MFCC, YIN pitch).

### M3. Execution Discipline

- Seed & replication: fixed-seed reproducibility plus enough replications for stable estimates
  (source example: clinic queue redesign, replications n≥100; waiting-time distribution, not just mean).
- Validation ladder: face validity → extreme-condition test → empirical anchor where available.
- Sensitivity sweep: vary uncertain parameters systematically; report which inputs dominate output
  variance.

### M2. Uncertainty Propagation

Inputs carry uncertainty; outputs inherit it amplified. Report bands, not points — band width IS
part of the answer. Propagation methods: analytic delta method, Monte Carlo sampling, interval
arithmetic; choose and justify per problem.

### M4. Engineering-Math Gate Sequence (Summary)

| Gate | Check |
|---|---|
| G1 | Units verified before numerics |
| G2 | Decomposition respects coupling strength |
| G3 | Output bands present wherever inputs uncertain |
| G4 | Convergence evidenced by residuals |

---

# H10 (F10) — AMOS/Trang Math Research Bridge

### M2. Fractal/Math Canon Gate

Claims about fractals, scaling exponents, golden ratios, entropy, chaos, Hurst long memory,
spectral laws, etc., route through their dedicated canon-grounding gates
(`amos-fractal-math-canon-gate`, `quantum-math-canon-grounding-gates`) before entering C02 outputs.
C02 supplies rigor machinery; it does NOT certify fractal or quantum claims itself.

### M4. Epistemic Firewall For Mathematics

Do not infer from:
- solver success alone (a returned number is not a validated result);
- high R²/model fit alone;
- precision of output beyond input uncertainty;
- convergence of an optimizer to truth (local optima, overfitting);
- simulation plausibility alone.

Valid support comes from: theorem/stated premises, convergence evidence, held-out validation,
sensitivity analysis, and independent replication.

---

# C02 Master Dependency Spine

```text
problem framing + dimensional analysis
            ↓
model selection + decomposition (honest couplings)
            ↓
numerical methods (error / conditioning / stability / convergence)
            ↓
probability & statistics (uncertainty machinery)
            ↓
optimization + complexity (decision formulation, hardness honesty)
            ↓
control + signal processing (dynamic and transformed systems)
            ↓
simulation + validation (scenario discipline)
            ↓
meta-control + error budgets (precision governance)
            ↓
decision interface (confidence-attached answers)
            ↓
AMOS cross-domain math services
```

# C02 Decision Capsule Template

```text
Problem:
Question type (descriptive/inferential/predictive/causal/optimization):
Precision mode (exact/approximate/order-of-magnitude):
Units verified:
Model family + why:
Key assumptions:
Coupling boundaries respected:
Inputs and distributions:
Uncertainty propagation method:
Output bands:
C

... (truncated, see vault source for full content)

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
```

---

**Related:** [[amos-c02-math-compute-master_MOC]]
