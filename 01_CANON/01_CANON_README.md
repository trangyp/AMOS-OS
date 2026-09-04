---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 01 Canon Readme
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

# 01 Canon — README

## Role

The Canon layer owns high-governance semantics — definitions, invariants, constraints, identity, and semantic boundaries for all of AMOS OS. Canon establishes what things mean, what the rules are, and what cannot be violated.

## Scope

### In Scope

- Core laws (AMOS_CORE_LAWS) — the 20+ fundamental invariants (M01–M20)
- Universe Canon — ontological foundations, Trang Framework, HML canon
- Cognition Canon — cognitive architecture definitions
- Infrastructure Canon — system infrastructure definitions
- Glossary — controlled vocabulary and definitions
- Provenance — source tracking, lineage, heritage
- Supersession — version history and deprecation records
- Variable Registry — formal symbol and variable definitions

### Out of Scope

- Runtime state (04_RUNTIME)
- Agent definitions (06_AGENTS)
- Knowledge claims (11_KNOWLEDGE) — Canon defines what knowledge is; Knowledge layer contains the knowledge itself

## Structure

```
01_CANON/
├── 00_INDEX/                  ← Navigation indices and registries
├── 01_CORE_LAWS/              ← Fundamental invariants and laws
├── 02_UNIVERSE_CANON/         ← Ontological foundations
├── 03_COGNITION_CANON/        ← Cognitive architecture definitions
├── 04_INFRASTRUCTURE_CANON/   ← Infrastructure definitions
├── 05_VARIABLE_REGISTRY/      ← Formal symbol definitions
├── 06_GLOSSARY/               ← Controlled vocabulary
├── 07_PROVENANCE/             ← Source tracking and lineage
└── 08_SUPERSESSION/           ← Version history
```

## Key Invariants

- Canon defines what things mean, not what exists
- Canon ≠ Implementation (M07)
- Canon changes require governance approval
- All Canon definitions carry full provenance

## Inter-Plane Connections

- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] — Kernel validates Canon compliance
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — Control plane enforces Canon
- **Knowledge:** [[11_KNOWLEDGE/KNOWLEDGE_CONTRACT|KNOWLEDGE_CONTRACT]] — Knowledge promotes to Canon with governance

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
