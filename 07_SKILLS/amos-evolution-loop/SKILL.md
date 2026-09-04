---
schema_version: 1.0
title: SKILL — Evolution Loop
type: skill
source: 07_SKILLS/amos-evolution-loop
name: amos-evolution-loop
description: Continuous observe→integrate cycle with rollback. Monitors system state, ingests observations, integrates validated updates, and rolls back on failure. Use when the parent skill (amos-os-runtime-master) routes to this specialized capability. Do not use for generic tasks outside runtime domain.
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

# Evolution Loop

## Identity

Origin architect: **Trang Phan**. Domain: runtime. Parent: amos-os-runtime-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- Continuous observe→integrate cycle with rollback. Monitors system state, ingests observations, integrates validated updates, and rolls back on failure.
- When the parent skill (`amos-os-runtime-master`) routes to this specialized capability.
- Do not use for generic tasks outside the runtime domain.

## Capabilities

- Provide governed runtime reasoning for the Evolution Loop capability.
- Maintain RSCF epistemic boundaries (`SOURCE_CLAIM`, `DERIVED`, `AMOS_MODEL`, `UNKNOWN/GAP`).
- Coordinate with parent skill and related AMOS OS planes.

## Implementation Status

`AMOS_MODEL` / `DERIVED` — structural specification present. Executable closure must be independently established for the exact scope and version.

______________________________________________________________________

**MOC:** [[07_SKILLS/amos-evolution-loop/amos-evolution-loop_MOC|Evolution Loop MOC]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
