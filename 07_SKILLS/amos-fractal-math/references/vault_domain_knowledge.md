---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Vault Domain Knowledge
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

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-fractal-math`

## Vault-Sourced Content

### Source 1: AMOS Math Core — Fractal Mathematics & Cognitive Architecture Runtime

> Path: `fractal/AMOS Math Core — Fractal Mathematics & Cognitive Architecture Runtime.md` | Size: 23148 chars | Match score: 23 | content_hash: 5212815857bf3528

## AMOS Math Core — Fractal Mathematics & Cognitive Architecture Runtime

## Overview

The module combines established mathematical/statistical methods with AMOS architecture adapters while preserving an important boundary:

> Mathematical estimators measure properties of supplied data. They do not establish that every AMOS system, cognitive process, or real-world phenomenon is intrinsically fractal.

The runtime includes:

______________________________________________________________________

## 1. Mathematical Runtime Model

The central decomposition is:

\[
x\_{t+1}=F(x_t)+\\varepsilon_t
\]

where:

Depending on the dataset, additional estimated quantities may include:

\[
D = \\text{fractal dimension}
\]

\[
H = \\text{Hurst exponent}
\]

\[
\\alpha = \\text{tail or scaling exponent}
\]

These quantities are **estimated from data**. They are not universal constants of the AMOS architecture.

______________________________________________________________________

## 2. Epistemic Boundary

AMOS Math Core separates four different kinds of mathematical use.

### Established Mathematics

Examples include:

### Numerical Estimation

Finite datasets require numerical approximations of theoretical limits.

For example,

\[
D_B =
\\lim\_{\\epsilon\\rightarrow0}
\\frac{\\log N(\\epsilon)}
{\\log(1/\\epsilon)}
\]

cannot normally be evaluated as a literal limit from finite observations.

The implementation therefore estimates the slope over a selected scaling region.

### Implementation Approximation

Some routines use practical numerical approximations rather than exact reference algorithms.

The mathematical object and its software approximation should therefore remain distinguishable.

### AMOS MODEL Integration

When mathematical quantities are mapped onto cognitive architecture, architecture entropy, recursive H/M/L organization, or other AMOS structures, that mapping remains an **AMOS MODEL** unless independently validated for the target domain.

______________________________________________________________________

## 3. Fractal Parameter State

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

______________________________________________________________________

## 4. Fractal Dimension Estimation

## Box-Counting Dimension

```python
box_counting_dimension(...)
```

estimates the Minkowski/box-counting dimension using:

\[
N(\\epsilon)\\sim\\epsilon^{-D}
\]

and therefore:

\[
D \\approx
\\frac{d\\log N(\\epsilon)}
{d\\log(1/\\epsilon)}
\]

The implementation:

1. normalizes the observations;
1. constructs logarithmically spaced scales;
1. counts occupied boxes;
   4

______________________________________________________________________

### Source 3: ancient_math_architecture

> Path: `math/ancient_math_architecture.md` | Size: 1367 chars | Match score: 15 | content_hash: bec25344fc83515f

{
"metadata": {
"title": "Ancient Math Fractal System",
"version": "1.0",
"created_utc": "2026-05-06T08:37:43+00:00",
"purpose": "Fractal architecture for ancient mathematics, symbolic ratios, geometry, astronomy, and cyclical systems."
},
"core_model": {
"system": "Pattern = Structure + Ratio + Cycle + Scale + Meaning + Constraint + Recurrence",
"L_M_H": {
"L": "foundation and material stability",
"M": "balance and transition",
"H": "expansion and transformation"
}
},
"core_equations": \[
{
"id": "AM001",
"name": "cycle_alignment",
"formula": "CA = overlap(cycle_a, cycle_b) / total_cycle"
},
{
"id": "AM002",
"name": "ratio_harmony",
"formula": "RH = min(ratio_a, ratio_b) / max(ratio_a, ratio_b)"
},
{
"id": "AM003",
"name": "fractal_recurrence",
"formula": "FR = similarity(scale_n, scale_n+1)"
},
{
"id": "AM004",
"name": "entropy_shift",
"formula": "ES = disorder_after - disorder_before"
},
{
"id": "AM005",
"name": "symbolic_density",
"formula": "SD = symbolic_units / total_units"
}
\]
}

______________________________________________________________________

______________________________________________________________________

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-fractal-math-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-fractal-math/references/vault_domain_knowledge.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
