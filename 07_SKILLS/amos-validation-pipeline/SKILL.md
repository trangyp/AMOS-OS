---
schema_version: 1.0
title: SKILL — Validation Pipeline
type: skill
source: 07_SKILLS/amos-validation-pipeline
name: amos-validation-pipeline
description: Ten-stage fail-fast validation plus GMEF authorization. Validates candidate changes before they are committed or executed. Use when the parent skill (amos-os-runtime-master) routes to this specialized capability. Do not use for generic tasks outside runtime domain.
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

# Validation Pipeline

## Identity

Origin architect: **Trang Phan**. Domain: runtime. Parent: amos-os-runtime-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- Ten-stage fail-fast validation plus GMEF authorization. Validates candidate changes before they are committed or executed.
- When the parent skill (`amos-os-runtime-master`) routes to this specialized capability.
- Do not use for generic tasks outside the runtime domain.

## Capabilities

- Provide governed runtime reasoning for the Validation Pipeline capability.
- Maintain RSCF epistemic boundaries (`SOURCE_CLAIM`, `DERIVED`, `AMOS_MODEL`, `UNKNOWN/GAP`).
- Coordinate with parent skill and related AMOS OS planes.

## Implementation Status

`AMOS_MODEL` / `DERIVED` — structural specification present. Executable closure must be independently established for the exact scope and version.

______________________________________________________________________

**MOC:** [[07_SKILLS/amos-validation-pipeline/amos-validation-pipeline_MOC|Validation Pipeline MOC]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
