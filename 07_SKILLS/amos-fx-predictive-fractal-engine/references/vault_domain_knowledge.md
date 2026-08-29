---
title: Vault Domain Knowledge — Amos Fx Predictive Fractal Engine
type: reference
source: 07_SKILLS/amos-fx-predictive-fractal-engine/references
tags:
- reference
- amos-fx-predictive-fractal-engine
- type/skill
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-fx-predictive-fractal-engine`

## Vault-Sourced Content

### Source 1: AMOS Math Core — Fractal Mathematics & Cognitive Architecture Runtime

> Path: `fractal/AMOS Math Core — Fractal Mathematics & Cognitive Architecture Runtime.md` | Size: 23148 chars | Match score: 13

# AMOS Math Core — Fractal Mathematics & Cognitive Architecture Runtime

## Overview (2)


The module combines established mathematical/statistical methods with AMOS architecture adapters while preserving an important boundary:

> Mathematical estimators measure properties of supplied data. They do not establish that every AMOS system, cognitive process, or real-world phenomenon is intrinsically fractal.

The runtime includes:


---

# 1. Mathematical Runtime Model

The central decomposition is:

[
x_{t+1}=F(x_t)+\varepsilon_t
]

where:


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
4

---

### Source 2: AMOS OMEGA FX STRUCTURAL ENGINE — COMPLETE SYSTEM

> Path: `economy/README_FX_STRUCTURAL_ENGINE.md` | Size: 14238 chars | Match score: 10

# AMOS OMEGA FX STRUCTURAL ENGINE — COMPLETE SYSTEM

## SYSTEM OVERVIEW


This is NOT a signal bot. This is a regime-aware structural operating system that detects macro regimes, computes phase states, maps liquidity loops, calculates fragility, simulates shocks, and makes structural positioning decisions based on invariants and feedback loops.

The engine reasons in: **invariants, feedback loops, tensors, regimes, risk envelopes, phase transitions** ---

## COMPLETE IMPLEMENTATION STATUS

### Core Components (100% Complete)
- **FX Structural Engine** (`fx_structural_engine.py`)
- State vectors, invariants, phase space detection
- **ActionGate System**
- Idempotency + safety for all operations
- **Risk Calculator**
- Shock simulation + fragility modeling
- **Data Connectors**
- Free API integration for macro + market data
- **Self-Evolution Loop** - Controlled learning with drift detection

### Visualization System (100% Complete)
- **Graph Visualization** (`fx_graph_visualization.py`)
- Multi-layer currency coupling + loop graphs
- **Phase Space Plot**
- 3D volatility/liquidity/policy divergence space
- **Regime Timeline**
- Temporal regime segmentation
- **Shock Simulator**
- Interactive shock simulation interface
- **Real-time Updates** - WebSocket streaming + D3.js v7

### Automation System (100% Complete)
- **N8n Integration** (`fx_n8n_integration.py`)
- 5 automated pipelines
 - Pipeline A: Data Ingestion (5-15 min schedule)
 - Pipeline B: Structural Analysis (AMOS computes state vector)
- Pipeline C: Trade Execution (Paper First with ActionGate)
 - Pipeline D: Daily Brief (Structural report to Loveable UI)
- Pipeline E: Risk Monitor (Fragility threshold alerts)

### UI System (100% Complete)
- **Loveable UI Bridge** (`fx_loveable_ui_bridge.py`)
- Live chat + interactive graph UI
- **React 18 + TypeScript**
- Modern frontend with real-time updates
- **5 Main Panels:**
- Live FX Map - Currency coupling graphs
- Structural Trace - Invariants + loops + equations
- Shock Simulator - Interactive controls
- Portfolio Risk - Exposure tensors + fragility
- Reality Panel - WORLD + FX + REPO + BODY views

### Main Integration (100% Complete)
- **Main Integration** (`fx_main_integration.py`)
- Complete system orchestration
- **24/7 Operation**
- Continuous analysis loops + monitoring
- **System Health**
- Component monitoring + alerting
- **Export System**
- Complete data export for analysis

---

## STRUCTURAL FX MODEL (ONLY AMOS CAN DO THIS)

### State Vector Components
For each currency pair:
- **Liquidity Stress (L)**
- Market liquidity compression
- **Policy Divergence (D)**
- Interest rate differentials
- **Volatility Expansion (V)**
- Volatility regime state
- **Capital Flow Pressure (F)**
- Cross-border capital flows
- **Risk Sentiment (R)**
- Market risk appetite
- **Structural Resistance (S)**
- System resilience factors

### Derived Metrics
- **Fragility Index**
- Weighted combination of stress factors
- ** ---

### Source 3: Fractal Cognitive Architecture v2

> Path: `fractal/fractal_cognitive_architecture.md` | Size: 11128 chars | Match score: 10

# Fractal Cognitive Architecture v2

## Overview


The package combines:


The framework is intended for architecture modeling and computational analysis. Fractal, entropy, and cross-scale constructs should be interpreted according to their declared mathematical or model status; structural similarity across scales does not by itself establish an identical real-world mechanism.

---

## Architecture Model

The package operates across three conceptual scales:

### H — Architecture Scale

Represents the complete cognitive system.

Typical concerns include:


### M — Module Scale

Represents interacting cognitive subsystems.

Typical concerns include:


### L — Feature and State Scale

Represents the smallest modeled cognitive units.

Typical concerns include:


Cross-scale projections should preserve identity, scope, assumptions, and relevant invariants.

---

## Core Runtime Objects

### `CognitiveState`

Represents the current state of the cognitive architecture or one of its components.

Use it to hold state information consumed or transformed by architecture modules and analysis engines.

### `FeatureSpec`

Defines an atomic architectural feature.

A feature specification may describe:


### `ModuleSpec`

Defines a cognitive module and its relationship to the wider architecture.

Modules provide the middle layer between individual features and the complete architecture.

### `ArchitectureSpec`

Defines the complete declarative architecture.

It acts as the primary structural input for compilation, analysis, validation, and blueprint generation.

---

## Fractal Runtime

### `FractalEngine`

Provides recursive architecture processing across scale and decomposition depth.

Conceptually:

```text
Architecture
 ↓
Modules
 ↓
Features / States
 ↓
Recursive substructure where defined
```

The engine is responsible for maintaining meaningful relationships between local, subsystem, and architecture-level structure.

Recursive similarity is treated as an architectural property unless independently demonstrated to constitute a mathematical or empirical fractal.

---

## Architecture Compilation

### `ArchitectureCompiler`

Transforms declarative architecture specifications into a normalized representation suitable for analysis.

A typical pipeline is:

```text
ArchitectureSpec
 ↓
Normalize
 ↓
Resolve dependencies
 ↓
Construct graphs
 ↓
Bind rules
 ↓
Validate structure
 ↓
Compiled architecture
```

Compilation should fail or report an explicit gap when required dependencies, definitions, or constraints cannot be resolved.

---

## Deterministic Analysis

### `DeterministicAnalyzer`

Evaluates architecture behavior against deterministic rules and invariants.

Primary responsibilities include:


The associated rule registry is exposed through:

```python
DETERMINISTIC_RULES
```

Deterministic analysis should distinguish between:

1. behavior directly guaranteed by explicit rules;
2. behavior derived from validated architecture struc

---
**MOC:** references_MOC

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-fx-predictive-fractal-engine-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-fx-predictive-fractal-engine/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
