---
schema_version: 1.0
title: SKILL — H/M/L Canon
type: skill
source: 07_SKILLS/amos-hml-canon
name: amos-hml-canon
description: Fractal knowledge resolution and retrieval architecture using High/Medium/Low (H/M/L) decomposition. See canonical HML Canon. Use when the parent skill (amos-canon-universe-master) routes to this specialized capability. Do not use for generic tasks outside canon domain.
parent_skill: amos-canon-universe-master
domain: canon
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
  - type/skill
  - domain/canon
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

# H/M/L Canon

## Identity

Origin architect: **Trang Phan**. Domain: canon. Parent: amos-canon-universe-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- Fractal knowledge resolution and retrieval architecture using High/Medium/Low (H/M/L) decomposition. See canonical HML Canon.
- When the parent skill (`amos-canon-universe-master`) routes to this specialized capability.
- Do not use for generic tasks outside the canon domain.

## Capabilities

- Provide governed canon reasoning for the H/M/L Canon capability.
- Maintain RSCF epistemic boundaries (`SOURCE_CLAIM`, `DERIVED`, `AMOS_MODEL`, `UNKNOWN/GAP`).
- Coordinate with parent skill and related AMOS OS planes.

## Canonical Reference

- [[01_CANON/02_UNIVERSE_CANON/HML_CANON|H/M/L Canon Canonical Spec]]

## Implementation Status

`AMOS_MODEL` / `DERIVED` — structural specification present. Executable closure must be independently established for the exact scope and version.

______________________________________________________________________

**MOC:** [[07_SKILLS/amos-hml-canon/amos-hml-canon_MOC|H/M/L Canon MOC]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
