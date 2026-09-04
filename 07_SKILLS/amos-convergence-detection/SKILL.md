---
schema_version: 1.0
title: SKILL — Convergence Detection
type: skill
source: 07_SKILLS/amos-convergence-detection
name: amos-convergence-detection
description: Tracks productive versus stuck evolution steps. Detects when iterative processes are converging, oscillating, or diverging. Use when the parent skill (amos-os-runtime-master) routes to this specialized capability. Do not use for generic tasks outside runtime domain.
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
  - type/skill
  - domain/runtime
  - epistemic/source_claim
  - hml/m
  - amos-os
  - skill
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.0.0
rscf_state: SOURCE_CLAIM
hml_level: M
collapse_class: reversible
license: MIT
steward: Trang Phan
---

# Convergence Detection

## Identity

Origin architect: **Trang Phan**. Domain: runtime. Parent: amos-os-runtime-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- Tracks productive versus stuck evolution steps. Detects when iterative processes are converging, oscillating, or diverging.
- When the parent skill (`amos-os-runtime-master`) routes to this specialized capability.
- Do not use for generic tasks outside the runtime domain.

## Capabilities

- Provide governed runtime reasoning for the Convergence Detection capability.
- Maintain RSCF epistemic boundaries (`SOURCE_CLAIM`, `DERIVED`, `AMOS_MODEL`, `UNKNOWN/GAP`).
- Coordinate with parent skill and related AMOS OS planes.

## Implementation Status

`AMOS_MODEL` / `DERIVED` — structural specification present. Executable closure must be independently established for the exact scope and version.

______________________________________________________________________

**MOC:** [[07_SKILLS/amos-convergence-detection/amos-convergence-detection_MOC|Convergence Detection MOC]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
