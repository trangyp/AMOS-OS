---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Multifractal Hurst Diagnostics
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

# Multifractal-Hurst Diagnostics Layer

> Source: `_00_Cosmo brain/dated/2026-08-25/2026-08-25 Multifractal-Hurst Diagnostics Layer.md`
> Epistemic class: SOURCE_DERIVED

______________________________________________________________________

## title: 2026-08-25 Multifractal-Hurst Diagnostics Layer type: daily-learning date: 2026-08-25 epistemic: SOURCE/DERIVED tags: [math, fractal, multifractal, hurst, diagnostics, dated, dated/2026-08-25]

## 2026-08-25 — Multifractal & Hurst Diagnostics (FR014–FR016 Deep)

## Gap found

FR014 (fBm/Hurst), FR015 (Weierstrass), FR016 (multifractal) are the **subtlest and easiest-to-fake** fractal families. The map names their validation methods (Hurst estimation, nowhere-differentiable check, Legendre transform) but nothing enforced them. The classic error is specific: running multifractal machinery on a monofractal produces a spurious τ(q) spectrum width, and people call it "multifractal". Single-method Hurst estimates biased by short-range dependence are nearly as common.

## Closure (4 channels)

| Channel             | Artifact                                                                                                                     |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Skill               | `amos/amos-multifractal-hurst-diagnostics` — three-track contract with evidence tables, 6-step procedure, guard set          |
| Agent               | `.devin/agents/amos-multifractal-audit-agent.json` — 6 capabilities incl. monofractal null test and finance time-basis check |
| Workflow            | `multifractal-hurst-audit-pipeline-workflow.md` — three-track pipeline                                                       |
| Memory + vault note | recorded                                                                                                                     |

## The classic error now gated

**Linear τ(q) = monofractal.** If the spectrum is a single slope (R²≈1 for one D), the correct claim is monofractal — multifractal machinery applied anyway manufactures spurious f(α) width. The monofractal null test is mandatory before any multifractal claim.

## Other enforced rules

- Multi-method H (R/S + DFA + wavelet variance agreeing within CI); single-method R/S rejected (short-range-dependence bias)
- AR/ARMA baseline before long-memory claims — apparent long memory often vanishes under control
- Δα width must exceed surrogate estimation error
- Weierstrass roughness claims need stated parameters with ab>1
- Financial fBm requires trading-time vs clock-time declaration

## Audit-family status: 11 layers

The fit-gate-label skeleton is now reused across scaling laws, networks, information measures, chaos, and multifractals. Each new layer costs less and shares more infrastructure.

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS Simulation Kernel v0 Math Foundations · system scan agent · automation profiles

______________________________________________________________________

## **MOC:** references_MOC

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-fractal-systems-master-multifractal-hurst-diagnostics
node_type: reference
path: 07_SKILLS/amos-fractal-systems-master/references/multifractal_hurst_diagnostics.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
