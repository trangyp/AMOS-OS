---
title: 2026-08-25 Spectral-Method Governance Layer
type: daily-learning
date: 2026-08-25
epistemic: SOURCE/DERIVED
tags: [math, signal, spectral, diagnostics, dated, dated/2026-08-25]
---

# 2026-08-25 — Spectral-Method Governance (Signal-Kernel Deep)

## Gap found

Spectral methods appear throughout the stack — the Signal Processing kernel, chaos diagnostics' spectra, QCI heart-brain synchrony measurements — and spectral results are exquisitely sensitive to parameters that are **almost never reported**: window function, length/overlap, zero-padding, detrending, normalization, wavelet mother. An unparameterized FFT silently becomes "dominant periodicity detected."

## Closure (4 channels)

| Channel | Artifact |
|---|---|
| Skill | `amos/amos-spectral-method-governance` — mandatory parameter table, five conflation blocks |
| Agent | `.devin/agents/amos-spectral-parameter-auditor-agent.json` — 6 capabilities incl. Gabor-limit block and Nyquist aliasing check |
| Workflow | `spectral-governance-pipeline-workflow.md` — 8-step pipeline |
| Memory + vault note | recorded |

## The five conflation blocks

1. **Peak ≠ periodicity** — significance required against red-noise/AR(1) background; noise produces peaks constantly
2. **1/f discipline** — slope must hold ≥2 decades AND survive detrending choices (mirrors scaling-law decade rule)
3. **Wavelet COI** — edge features inside the cone of influence are artifacts
4. **Gabor limit** — exact simultaneous time+frequency localization is impossible; such claims blocked
5. **Nyquist aliasing** — sampling rate stated; claimed peaks checked against it

## Design note

Zero-padding blocked as super-resolution theater (it interpolates display, adds no information) is the kind of parameter-level lie this layer exists to catch. The audit family now spans data-fits, point-hypotheses, constructions, and transforms — every quantitative evidence class in the corpus.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
