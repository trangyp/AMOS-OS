---
title: DOMAINS_MOC
type: map_of_content
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_INDEX
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__AMOS_OS
tags:
  - domains
  - index
  - moc
---

# Master Domains MOC (21_DOMAINS)

## 1. Architectural Scope
Plane 21 houses all 45+ specialized scientific, technological, socioeconomic, and physiological domain specifications.

## 2. Domain Taxonomy
- **Foundational Sciences**: Philosophy, Mathematics, Physics, Biology, Mind & Behavior.
- **Engineering & Systems**: Tech & Engineering, Robotics, AI Compute Systems, Quantum Systems.
- **Physiology & Neurotech**: UBI/NBI Neurobiological, Somatic, Bioelectromagnetic, Clinical Medicine.
- **Socio-Legal & Strategy**: Economics, Strategy & Game Theory, Organizational Law, HSE Safety.

## 3. Navigation
- [[00_ROOT/00_ROOT_MOC|Root Navigation MOC]]
- [[21_DOMAINS/21_DOMAINS_MOC|Domains Plane MOC]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/DOMAIN_ARCHITECTURE_INDEX|Domain Architecture Index]]

## Domain/Plane Overview
The Domains plane (`21_DOMAINS`) houses all 45+ specialized domain specifications within AMOS OS. These span foundational sciences (Philosophy, Mathematics, Physics, Biology, Mind & Behavior), engineering and systems (Tech & Engineering, Robotics, AI Compute, Quantum), physiology and neurotech (UBI/NBI, Somatic, Bioelectromagnetic, Clinical Medicine), and socio-legal and strategy (Economics, Strategy, Organizational Law, HSE Safety).

The `00_INDEX` subdirectory provides the master navigation surface for this plane, routing readers to domain architecture specifications, individual domain MOCs, and cross-references to the Research and Knowledge planes.

## MECE Classification
| Cluster | Domains | Count |
|---------|---------|-------|
| Foundational Sciences | Philosophy, Mathematics, Physics, Biology, Mind & Behavior | 5 |
| Engineering & Systems | Tech & Engineering, Robotics, AI Compute, Quantum Systems | 4 |
| Physiology & Neurotech | UBI/NBI Neurobiological, Somatic, Bioelectromagnetic, Clinical Medicine | 4 |
| Socio-Legal & Strategy | Economics, Strategy & Game Theory, Organizational Law, HSE Safety | 4 |
| Cross-Cutting | Domain Architecture, Domain Index | 2 |

Clusters are mutually exclusive; together they cover the domain specification surface of `21_DOMAINS`.

## Key Artifacts
- [[21_DOMAINS/21_DOMAINS_MOC|Domains Plane MOC]] — primary plane navigation.
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/DOMAIN_ARCHITECTURE_INDEX|Domain Architecture Index]] — architecture specifications.
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C10_AI_COMPUTE_SYSTEMS_SPECIALIST_ARCHITECTURE|C10 AI Compute Architecture]] — AI compute domain spec.
- [[21_DOMAINS/20_C10_TECH_ENGINEERING/20_C10_TECH_ENGINEERING_MOC|C10 Tech Engineering MOC]] — engineering domain MOC.
- [[00_ROOT/00_ROOT_MOC|Root Navigation MOC]] — vault-wide navigation.

## Cross-Plane Relationships
- **Knowledge (`11_KNOWLEDGE`)**: domain specifications reference knowledge kernels for semantic grounding.
- **Research (`22_RESEARCH`)**: research artifacts feed into domain specifications as evidence.
- **Memory (`10_MEMORY`)**: agent-learned memory may reference domain specs for provenance.
- **Root (`00_ROOT`)**: the root MOC includes this plane in vault-wide navigation.

## Epistemic Boundary
This MOC is `DERIVED` from the authoritative AMOS OS structure. It describes topology and routing only. `INDEXED != AUTHORITATIVE`, `SPECIFIED != IMPLEMENTED`. The presence of a domain specification in this index does not prove its implementation, deployment, or operational validation. Cross-plane dependencies require each referenced artifact's own typed contract and provenance.

---

**Parent:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
