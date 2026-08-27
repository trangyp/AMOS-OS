---
tags: [fractal]
---
# AMOS Math Core — Fractal Mathematics & Cognitive Architecture Runtime

## Overview

**AMOS Math Core** provides the mathematical and computational foundation for fractal, persistence, heavy-tail, multifractal, signal-processing, and information-analysis components used by the wider AMOS architecture.

The module combines established mathematical/statistical methods with AMOS architecture adapters while preserving an important boundary:

> Mathematical estimators measure properties of supplied data. They do not establish that every AMOS system, cognitive process, or real-world phenomenon is intrinsically fractal.

The runtime includes:

* fractal-dimension estimation;
* Hurst and persistence analysis;
* detrended fluctuation analysis;
* fractional and heavy-tail noise generation;
* continuous wavelet analysis;
* spectral cycle detection;
* multifractal-spectrum estimation;
* tail-index estimation;
* entropy-rate approximation;
* mutual information;
* comprehensive fractal-analysis pipelines;
* AMOS data/configuration loaders;
* hierarchical architecture generation;
* Fractal Cognitive Architecture v2 integration; and
* Fractal Cognitive Programming integration.

---

# 1. Mathematical Runtime Model

The central decomposition is:

[
x_{t+1}=F(x_t)+\varepsilon_t
]

where:

* (x_t) is the observed or modeled state at time (t);
* (F) is the deterministic or estimated structural component;
* (\varepsilon_t) is the residual/noise component.

Depending on the dataset, additional estimated quantities may include:

[
D = \text{fractal dimension}
]

[
H = \text{Hurst exponent}
]

[
\alpha = \text{tail or scaling exponent}
]

These quantities are **estimated from data**. They are not universal constants of the AMOS architecture.

---

# 2. Epistemic Boundary

AMOS Math Core separates four different kinds of mathematical use.

### Established Mathematics

Examples include:

* box-counting dimension;
* Grassberger–Procaccia correlation dimension;
* information dimension;
* R/S analysis;
* detrended fluctuation analysis;
* Pareto distributions;
* Fourier/spectral analysis;
* wavelet analysis;
* mutual information; and
* multifractal partition functions.

### Numerical Estimation

Finite datasets require numerical approximations of theoretical limits.

For example,

[
D_B =
\lim_{\epsilon\rightarrow0}
\frac{\log N(\epsilon)}
{\log(1/\epsilon)}
]

cannot normally be evaluated as a literal limit from finite observations.

The implementation therefore estimates the slope over a selected scaling region.

### Implementation Approximation

Some routines use practical numerical approximations rather than exact reference algorithms.

The mathematical object and its software approximation should therefore remain distinguishable.

### AMOS MODEL Integration

When mathematical quantities are mapped onto cognitive architecture, architecture entropy, recursive H/M/L organization, or other AMOS structures, that mapping remains an **AMOS MODEL** unless independently validated for the target domain.

---

# 3. Fractal Parameter State

```python
@dataclass
class FractalParameters:
    D_box: Optional[float] = None
    D_corr: Optional[float] = None
    D_info: Optional[float] = None
    H: Optional[float] = None
    alpha: Optional[float] = None
    tau: Optional[Dict] = None
    f_alpha: Optional[Dict] = None
    scales: Optional[np.ndarray] = None
```

`FractalParameters` provides a common state container for the primary fractal and scaling quantities produced by the runtime.

Conceptually:

```text
Observed Data
     │
     ├── D_box
     ├── D_corr
     ├── D_info
     ├── H
     ├── α
     ├── τ(q)
     └── f(α)
```

Each value should retain the dataset, estimator, scale range, preprocessing assumptions, and numerical conditions under which it was obtained.

---

# 4. Fractal Dimension Estimation

## Box-Counting Dimension

```python
box_counting_dimension(...)
```

estimates the Minkowski/box-counting dimension using:

[
N(\epsilon)\sim\epsilon^{-D}
]

and therefore:

[
D \approx
\frac{d\log N(\epsilon)}
{d\log(1/\epsilon)}
]

The implementation:

1. normalizes the observations;
2. constructs logarithmically spaced scales;
3. counts occupied boxes;
4. identifies usable scales; and
5. performs log-log linear regression.

The returned value is a **finite-sample estimate**, not the theoretical limit itself.

---

## Correlation Dimension

```python
correlation_dimension(...)
```

implements a Grassberger–Procaccia-style estimator.

The correlation sum is modeled as:

[
C(r)\sim r^{D_2}
]

with:

[
C(r)=
\frac{2}{N(N-1)}
\sum_{i<j}
\Theta(r-|x_i-x_j|)
]

The slope of

[
\log C(r)
]

against

[
\log r
]

provides an estimate of the correlation dimension.

Large datasets may be subsampled for computational tractability.

Subsampling introduces an additional uncertainty source and should therefore be recorded when results are used downstream.

---

## Information Dimension

```python
information_dimension(...)
```

estimates:

[
D_1=
\lim_{\epsilon\rightarrow0}
\frac{H(\epsilon)}
{\log(1/\epsilon)}
]

where:

[
H(\epsilon)=
-\sum_i p_i(\epsilon)\log p_i(\epsilon)
]

The implementation coarse-grains observations at multiple resolutions and estimates the scaling relationship numerically.

---

# 5. Persistence and Long-Range Dependence

## Hurst Exponent

```python
hurst_exponent_rs(...)
```

uses rescaled-range analysis:

[
E[R/S]\sim c,n^H
]

The implementation estimates (H) from the log-log relationship between window size and average rescaled range.

Typical interpretation:

```text
H < 0.5     anti-persistent / mean-reverting tendency
H ≈ 0.5     approximately uncorrelated scaling
H > 0.5     persistent tendency
```

These interpretations depend on the process assumptions and estimator behavior.

A measured (H>0.5) does not by itself establish a causal mechanism or guarantee future persistence.

---

## Detrended Fluctuation Analysis

```python
detrended_fluctuation_analysis(...)
```

estimates the DFA scaling exponent from:

[
F(n)\sim n^\alpha
]

The runtime:

```text
Input Series
     ↓
Mean Removal
     ↓
Cumulative Integration
     ↓
Window Segmentation
     ↓
Polynomial Detrending
     ↓
RMS Fluctuation
     ↓
Log-Log Scaling Fit
     ↓
α
```

The `order` parameter determines the polynomial detrending order.

---

# 6. Stochastic and Heavy-Tail Generators

AMOS Math Core includes three principal synthetic signal generators.

## Fractional Brownian Motion

```python
generate_fbm(...)
```

generates an approximate fractional-Brownian-motion-style signal parameterized by the Hurst exponent (H).

The theoretical covariance associated with fBm is:

[
\operatorname{Cov}(B_H(t),B_H(s))
=================================

\frac12
\left(
t^{2H}+s^{2H}-|t-s|^{2H}
\right)
]

The current implementation uses frequency-domain spectral scaling.

Therefore the implementation should be described as an **approximate spectral generator**, rather than claiming exact Davies–Harte execution unless the algorithm is actually implemented as such.

---

## Pareto Noise

```python
generate_pareto_noise(...)
```

generates power-law/Pareto samples using:

[
f(x)=
\frac{\alpha x_{\min}^{\alpha}}
{x^{\alpha+1}},
\qquad x\geq x_{\min}
]

with inverse-CDF sampling:

[
x=x_{\min}U^{-1/\alpha}
]

where:

[
U\sim\operatorname{Uniform}(0,1)
]

Important theoretical regimes include:

```text
α ≤ 1     theoretical mean diverges
α ≤ 2     theoretical variance diverges
```

for the ideal Pareto model.

---

## Multifractal Noise

```python
generate_multifractal_noise(...)
```

constructs a synthetic cascade using recursively applied random multiplicative weights.

Conceptually:

```text
Initial Measure
      ↓
Scale 1 Split
    ↙     ↘
Scale 2   Scale 2
  ↙ ↘       ↙ ↘
...
      ↓
Multiplicative Cascade
      ↓
Integrated Signal
```

The resulting signal is a synthetic model useful for experimentation.

It should not be interpreted as evidence that an observed system follows the same generative mechanism.

---

# 7. Signal Processing

## Continuous Wavelet Transform

```python
wavelet_transform(...)
```

provides multiscale signal decomposition.

Supported wavelet behavior includes:

* Morlet;
* Mexican-hat; and
* fallback behavior.

The output is:

```text
coefficients[scale, time]
scales
```

allowing local structure to be inspected simultaneously across time and scale.

---

## Spectral Cycle Detection

```python
detect_cycles_spectral(...)
```

performs:

```text
Signal
  ↓
Detrend
  ↓
Periodogram
  ↓
Peak Detection
  ↓
Frequency Ranking
  ↓
Cycle Periods
```

The strongest spectral peak becomes the reported dominant frequency/period.

A spectral peak demonstrates periodic energy in the analyzed sample; it does not by itself establish a stable causal cycle.

---

# 8. Multifractal Spectrum

```python
compute_multifractal_spectrum(...)
```

implements a partition-function-based multifractal analysis.

The central relation is:

[
Z_q(\epsilon)
=============

\sum_i\mu_i(\epsilon)^q
\sim
\epsilon^{\tau(q)}
]

From the mass exponent:

[
\alpha(q)
=========

\frac{d\tau(q)}{dq}
]

and:

[
f(\alpha)
=========

q\alpha-\tau(q)
]

The generalized dimensions are:

[
D_q=
\frac{\tau(q)}
{q-1}
]

for (q\neq1).

The spectrum width:

[
\Delta\alpha=
\alpha_{\max}-\alpha_{\min}
]

is returned as a descriptive complexity measure.

The implementation numerically approximates derivatives and scaling relationships, so interpretation should include sensitivity to:

* sample length;
* scale selection;
* (q)-range;
* preprocessing;
* zero handling; and
* regression stability.

---

# 9. Tail Analysis

```python
estimate_tail_index(...)
```

provides Hill-estimator-based tail analysis.

For the upper-order statistics:

[
\hat{\alpha}
============

\frac{k}
{
\sum_{i=1}^{k}
\log(X_i/X_k)
}
]

The parameter (k), represented indirectly through `tail_fraction`, is load-bearing.

Different tail thresholds can materially change the estimate.

Accordingly, serious downstream use should include threshold-sensitivity analysis rather than relying on a single value.

---

# 10. Entropy Analysis

```python
compute_entropy_rate(...)
```

approximates sequence entropy after symbolizing the input series.

The conceptual target is:

[
h
=

-\sum
p(x_{n+1}\mid x_n,\ldots)
\log
p(x_{n+1}\mid x_n,\ldots)
]

The implementation uses finite symbol sequences and returns an entropy-per-order approximation.

This quantity should not automatically be identified with the exact Kolmogorov–Sinai entropy of the underlying dynamical system.

---

# 11. Mutual Information

```python
mutual_information(...)
```

estimates:

[
I(X;Y)
======

\sum_{x,y}
p(x,y)
\log
\frac{p(x,y)}
{p(x)p(y)}
]

using discretized joint and marginal distributions.

Optional normalization rescales the estimate using the entropy of (X).

Mutual information establishes statistical dependence under the estimator.

It does **not** establish:

[
X\rightarrow Y
]

or any other causal direction.

---

# 12. Comprehensive Analysis Pipeline

```python
comprehensive_fractal_analysis(data)
```

provides a unified entry point returning:

```python
{
    "D_box": ...,
    "D_corr": ...,
    "D_info": ...,
    "H": ...,
    "alpha_dfa": ...,
    "tail_index": ...,
    "entropy_rate": ...,
}
```

Conceptually:

```text
                     Input Data
                         │
          ┌──────────────┼──────────────┐
          │              │              │
      Geometry       Persistence    Distribution
          │              │              │
       D_box             H           Tail Index
       D_corr          DFA α
       D_info
          │              │              │
          └──────────────┼──────────────┘
                         │
                    Entropy Rate
                         │
                         ▼
              Fractal Analysis Report
```

No individual estimator should dominate the interpretation without consistency checks against the others.

---

# 13. AMOS Architecture Integration

The mathematical runtime connects to several higher-order AMOS components.

## Hierarchical AI Architecture Generator

When available:

```python
HierarchicalGenerator
ArchitectureFactory
UnifiedGenerator
AMOSArchitectureBridge
GoalDrivenGenerator
AIArchitectureEngine
GeneratedArchitecture
generate_from_goal
load_ontology
```

Availability is represented by:

```python
HIERARCHICAL_AI_AVAILABLE
```

---

## Fractal Cognitive Architecture v2

When available:

```python
CognitiveState
FeatureSpec
ModuleSpec
ArchitectureSpec
FractalEngine
ArchitectureCompiler
EntropyAnalyzer
DeterministicAnalyzer
ArchitectureValidator
BlueprintGenerator
ArchitectureReport
```

with architecture registries:

```python
EQUATIONS
DETERMINISTIC_RULES
ENTROPY_RULES
COGNITIVE_LAYER_GRAPH
SCALE_GRAPH
ENTROPY_SOURCES
```

Availability is represented by:

```python
FRACTAL_COGNITIVE_V2_AVAILABLE
```

The relationship is conceptually:

```text
Mathematical Measurements
          ↓
Typed Analysis Results
          ↓
Fractal Cognitive Architecture
          ↓
H / M / L Interpretation
          ↓
Validation
          ↓
Architecture Report
```

Cross-scale mappings remain valid only within their declared assumptions.

---

## Fractal Cognitive Programming Architecture

The runtime can additionally expose:

```python
FractalCognitiveEngine
RELATIONSHIPS
REQUIRED_FEATURE_FIELDS
validate_feature
detect_fake_features
validate_architecture
clean_text_core
clean_text_validator
```

through the optional programming-architecture integration.

Availability is represented by:

```python
FRACTAL_PROGRAMMING_AVAILABLE
```

---

# 14. H/M/L Fractal Interpretation

AMOS can organize the mathematical runtime through three analytical scales.

## H — System Scale

Questions include:

* Does the complete dataset exhibit stable scaling?
* Are multiple estimators mutually compatible?
* Is the apparent structure robust across regimes?
* Does the overall architecture remain internally coherent?

## M — Subsystem Scale

Questions include:

* Which intervals or modules carry the observed structure?
* Does persistence vary by subsystem?
* Are entropy and tail behavior localized?
* Are different regimes being incorrectly combined?

## L — Local Scale

Questions include:

* Which observations generate the measured effect?
* Which scales determine the regression?
* Which tail observations determine (\hat\alpha)?
* Which spectral peaks dominate cycle detection?

The system should not infer H-level universality merely because an L-level pattern exists.

---

# 15. Deterministic + Stochastic Decomposition

The architecture distinguishes:

[
\text{Observed State}
=====================

\text{Structure}
+
\text{Residual}
]

or dynamically:

[
x_{t+1}=F(x_t)+\varepsilon_t
]

This distinction creates two different analytical responsibilities.

### Deterministic Channel

Estimate or define:

[
F(x_t)
]

and test whether the deterministic structure is stable and reproducible.

### Residual Channel

Analyze:

[
\varepsilon_t
=============

x_{t+1}-F(x_t)
]

for:

* autocorrelation;
* long-range dependence;
* heavy tails;
* scaling;
* multifractality;
* entropy; and
* regime dependence.

A fractal property should ideally be measured on the appropriate residual or state representation rather than assumed in advance.

---

# 16. Validation Contract

A robust analysis should preserve the following sequence:

```text
DATA
 ↓
Input Validation
 ↓
Preprocessing
 ↓
Estimator Selection
 ↓
Scale / Threshold Selection
 ↓
Numerical Estimation
 ↓
Goodness-of-Fit / Stability Checks
 ↓
Cross-Estimator Comparison
 ↓
Regime / Sensitivity Analysis
 ↓
Interpretation
```

A numerical result is not sufficient by itself for a strong architecture claim.

---

# 17. Provenance Contract

Every consequential mathematical result should ideally retain:

```text
dataset
dataset version/hash
observation interval
preprocessing
estimator
estimator parameters
scale range
random seed
software version
dependency versions
result
diagnostics
assumptions
scope
regime
```

This allows an analysis to be reproduced, challenged, invalidated, or recomputed when its dependencies change.

---

# 18. Reproducibility

Stochastic functions expose optional random seeds:

```python
seed: Optional[int]
```

For reproducible experiments, seeds should be explicitly supplied and recorded.

A reproducible stochastic realization is still only one realization of the process.

Therefore:

```text
same seed → reproducible realization
```

does not imply:

```text
one realization → complete characterization
```

---

# 19. Important Implementation Boundaries

Several distinctions should remain explicit.

### Theoretical Formula ≠ Numerical Estimator

A finite regression approximating a mathematical limit does not prove that the limit exists for the observed process.

### Spectral Scaling ≠ Exact fBm Algorithm

The current `generate_fbm` implementation uses spectral shaping. Its documentation should not claim exact Davies–Harte execution unless that algorithm is actually implemented.

### Entropy Approximation ≠ Exact KS Entropy

`compute_entropy_rate` is a symbolized finite-sequence approximation.

### Mutual Information ≠ Causality

[
I(X;Y)>0
]

supports dependence, not causal direction.

### Fractal Fit ≠ Universal Fractality

A measured scaling region must survive robustness and alternative-model checks before stronger conclusions are warranted.

### Architecture Mapping ≠ Empirical Validation

Connecting mathematical measurements to AMOS cognitive modules creates an analytical architecture. It does not independently prove a biological or physical interpretation.

---

# 20. Public API

The module exposes mathematical, loader, architecture, validation, and convenience interfaces through `__all__`.

Principal mathematical functions include:

```python
box_counting_dimension
correlation_dimension
information_dimension

hurst_exponent_rs
detrended_fluctuation_analysis

generate_fbm
generate_pareto_noise
generate_multifractal_noise

wavelet_transform
detect_cycles_spectral

compute_multifractal_spectrum

estimate_tail_index
compute_entropy_rate
mutual_information

comprehensive_fractal_analysis
```

Primary architecture interfaces include:

```python
HierarchicalGenerator
ArchitectureFactory
UnifiedGenerator
AMOSArchitectureBridge
GoalDrivenGenerator
AIArchitectureEngine

CognitiveState
FeatureSpec
ModuleSpec
ArchitectureSpec
FractalEngine
ArchitectureCompiler
EntropyAnalyzer
DeterministicAnalyzer
ArchitectureValidator
BlueprintGenerator
ArchitectureReport

FractalCognitiveEngine
```

---

# 21. Runtime Availability

The module exposes:

```python
MATH_IMPL_AVAILABLE = True
```

and optional subsystem flags:

```python
HIERARCHICAL_AI_AVAILABLE
FRACTAL_COGNITIVE_V2_AVAILABLE
FRACTAL_PROGRAMMING_AVAILABLE
```

These flags report whether the corresponding Python components were successfully imported.

They indicate **software availability**, not scientific validation.

---

# 22. AMOS Analysis Status Model

For downstream reasoning, results should use the weakest accurate conclusion class:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN / GAP
```

Examples:

```text
VERIFIED
Function executed successfully on the specified dataset
and its output was independently checked.

DERIVED
A quantity follows deterministically from validated inputs.

MODEL
An AMOS architecture interpretation maps measured quantities
onto a larger cognitive/system model.

CONDITIONAL
The conclusion depends materially on scale, threshold,
preprocessing, stationarity, or another unresolved assumption.

COMPETING
Multiple explanations remain consistent with the observations.

UNKNOWN / GAP
Available evidence is insufficient to discriminate the claim.
```

---

# 23. Recommended AMOS Fractal Analysis Loop

```text
1. Observe
      ↓
2. Validate data
      ↓
3. Separate deterministic structure and residual
      ↓
4. Analyze L-scale behavior
      ↓
5. Aggregate to M-scale structure
      ↓
6. Test H-scale consistency
      ↓
7. Compare competing explanations
      ↓
8. Run sensitivity tests
      ↓
9. Validate architecture constraints
      ↓
10. Report bounded conclusion
```

If a local assumption fails, invalidate only conclusions dependent upon that assumption.

---

# 24. Core Design Principles

**Measure before declaring fractality.**

**Estimate parameters from the relevant dataset rather than assigning universal values.**

**Keep deterministic structure separate from residual stochastic behavior.**

**Preserve scale and regime information.**

**Do not infer causation from dependence or structural similarity.**

**Treat finite-sample estimators as approximations of theoretical quantities.**

**Record stochastic seeds and numerical parameters for reproducibility.**

**Test sensitivity to scale ranges, thresholds, preprocessing, and sample length.**

**Keep established mathematics separate from AMOS MODEL mappings.**

**Preserve unresolved competing explanations rather than forcing convergence.**

---

# 25. References

The mathematical foundation represented by this module includes methods associated with:

* Falconer — *Fractal Geometry*;
* Grassberger & Procaccia — correlation-dimension estimation;
* Mandelbrot — fractal geometry and scaling processes;
* Hurst — rescaled-range analysis; and
* Kantelhardt et al. — detrended fluctuation and multifractal analysis.

References identify mathematical lineage; they do not independently validate every numerical implementation or every AMOS-specific application.

---

# 26. Architecture Position

```text
                    AMOS Architecture
                           │
                  Cognitive / AI Layer
                           │
              Fractal Cognitive Architecture
                           │
                  ┌────────┴────────┐
                  │                 │
          Deterministic Core   Entropy Core
                  │                 │
                  └────────┬────────┘
                           │
                     AMOS Math Core
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
 Fractal Geometry     Time-Series         Information
        │              Dynamics              Theory
        │                  │                  │
   D_box/D_corr       H / DFA / FFT       Entropy / MI
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                      Observed Data
```

AMOS Math Core therefore serves as a **measurement and numerical-analysis substrate** beneath the higher-level fractal cognitive architecture.

Its role is not to assume that the universe, cognition, or an arbitrary dataset is fractal.

Its role is to provide explicit mathematical procedures capable of testing, estimating, simulating, and challenging those hypotheses.

---

**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · Fractal_Cognitive_Architecture_v2 · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
