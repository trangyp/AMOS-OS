---
title: AMOS Domains
type: domains_moc
source: 21_DOMAINS
amos_core_target: v4.4
origin_architect: Trang Phan
status: ACTIVE_DOMAIN_ROUTING_AND_ARCHITECTURE_INDEX
conclusion_class: DERIVED
updated: 2026-09-03
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance:
    - live_11_KNOWLEDGE_domain_masters
    - live_08_WORKFLOWS_domain_workflows
    - 21_DOMAINS/01_DOMAIN_ARCHITECTURE/DOMAIN_ARCHITECTURE_INDEX
  scope: specialist_domain_ownership_and_routing
---

# 21_DOMAINS — Specialist Domain Ownership and Routing

`21_DOMAINS` owns **functional domain identity, routing and capability boundaries**. Physical source
knowledge may remain in `11_KNOWLEDGE`; workflows may remain in `08_WORKFLOWS`; models may remain in
`13_MODELS`. That separation prevents duplication while giving each domain one primary owner.

```text
DOMAIN OWNERSHIP != STORAGE LOCATION
DOMAIN KNOWLEDGE != DOMAIN WORKFLOW
DOMAIN MODEL != EMPIRICAL TRUTH
```

## C01–C12 domain map

| Domain | Primary knowledge surface | Execution bridge |
|---|---|---|
| C01 Meta Logic | [[11_KNOWLEDGE/AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE|C01 Master Knowledge]] | [[08_WORKFLOWS/amos-c01-meta-logic-master-workflow|C01 Workflow]] |
| C02 Math & Compute | [[11_KNOWLEDGE/AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE|C02 Master Knowledge]] | [[08_WORKFLOWS/amos-c02-math-compute-master-workflow|C02 Workflow]] |
| C03 Physics & Cosmos | [[11_KNOWLEDGE/AMOS_C03_PHYSICS_COSMOS_MASTER_KNOWLEDGE|C03 Master Knowledge]] | [[08_WORKFLOWS/amos-c03-physics-cosmos-master-workflow|C03 Workflow]] |
| C04 Biology & Neuro | [[11_KNOWLEDGE/AMOS_C04_BIO_NEURO_MASTER_KNOWLEDGE|C04 Master Knowledge]] | [[08_WORKFLOWS/amos-c04-bio-neuro-master-workflow|C04 Workflow]] |
| C05 Mind & Behavior | [[11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE|C05 Master Knowledge]] | [[08_WORKFLOWS/amos-c05-mind-behavior-master-workflow|C05 Workflow]] |
| C06 Society & Culture | [[11_KNOWLEDGE/AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE|C06 Master Knowledge]] | [[08_WORKFLOWS/amos-c06-society-culture-master-workflow|C06 Workflow]] |
| C07 Economics & Finance | [[11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE|C07 Master Knowledge]] | [[08_WORKFLOWS/amos-c07-econ-finance-master-workflow|C07 Workflow]] |
| C08 Strategy & Games | [[11_KNOWLEDGE/AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE|C08 Master Knowledge]] | [[08_WORKFLOWS/amos-c08-strategy-game-master-workflow|C08 Workflow]] |
| C09 Organization, Law & Policy | [[11_KNOWLEDGE/AMOS_C09_ORG_LAW_POLICY_MASTER_KNOWLEDGE|C09 Master Knowledge]] | [[08_WORKFLOWS/amos-c09-org-law-policy-master-workflow|C09 Workflow]] |
| C10 Technology & Engineering | [[11_KNOWLEDGE/AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE|C10 Master Knowledge]] | [[08_WORKFLOWS/amos-c10-tech-engineering-master-workflow|C10 Workflow]] |
| C11 Design & Language | [[11_KNOWLEDGE/AMOS_C11_DESIGN_LANGUAGE_MASTER_KNOWLEDGE|C11 Master Knowledge]] | [[08_WORKFLOWS/amos-c11-design-language-master-workflow|C11 Workflow]] |
| C12 Earth & Ecology | [[11_KNOWLEDGE/AMOS_C12_EARTH_ECOLOGY_MASTER_KNOWLEDGE|C12 Master Knowledge]] | [[08_WORKFLOWS/amos-c12-earth-ecology-master-workflow|C12 Workflow]] |


## Domain architecture contracts

The substantive functional contract layer now lives at
[[21_DOMAINS/01_DOMAIN_ARCHITECTURE/DOMAIN_ARCHITECTURE_INDEX|DOMAIN_ARCHITECTURE_INDEX]].

Each C-domain has one active architecture contract:

- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C01_META_LOGIC_DOMAIN_ARCHITECTURE|C01 Meta Logic Architecture]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C02_MATH_COMPUTE_DOMAIN_ARCHITECTURE|C02 Math & Compute Architecture]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C03_PHYSICS_COSMOS_DOMAIN_ARCHITECTURE|C03 Physics & Cosmos Architecture]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C04_BIO_NEURO_DOMAIN_ARCHITECTURE|C04 Biology & Neuro Architecture]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C05_MIND_BEHAVIOR_DOMAIN_ARCHITECTURE|C05 Mind & Behavior Architecture]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C06_SOCIETY_CULTURE_DOMAIN_ARCHITECTURE|C06 Society & Culture Architecture]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C07_ECON_FINANCE_DOMAIN_ARCHITECTURE|C07 Economics & Finance Architecture]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C08_STRATEGY_GAME_DOMAIN_ARCHITECTURE|C08 Strategy & Games Architecture]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C09_ORG_LAW_POLICY_DOMAIN_ARCHITECTURE|C09 Organization/Law/Policy Architecture]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C10_TECH_ENGINEERING_DOMAIN_ARCHITECTURE|C10 Technology & Engineering Architecture]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C11_DESIGN_LANGUAGE_DOMAIN_ARCHITECTURE|C11 Design & Language Architecture]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/C12_EARTH_ECOLOGY_DOMAIN_ARCHITECTURE|C12 Earth & Ecology Architecture]]

These files own **functional identity, MECE H-level ownership, composition boundaries and admission
gates**. They deliberately do not duplicate the large knowledge masters.

```text
DOMAIN CONTRACT != KNOWLEDGE MASTER != WORKFLOW != SKILL != MODEL != CONTROL AUTHORITY
```

The domain contract is the first semantic stop after this MOC; deeper retrieval proceeds to the
knowledge/workflow/model/skill layer only when it can change the answer.

## Domain capability contract

Each domain exposes inputs/outputs/units, scope/population, scales/horizons, regime assumptions,
provenance/freshness, models/equations, invariants/falsifiers, competing hypotheses, benchmark
boundaries, risk/authority boundary and degraded behavior.

## Cross-domain composition

Composition routes through
[[11_KNOWLEDGE/AMOS_CROSS_DOMAIN_TENSOR_COMPOSITION_GOVERNOR|CROSS_DOMAIN_TENSOR_COMPOSITION_GOVERNOR]].

Before composition establish variable identity, units, time alignment, scale, scope/regime,
provenance independence and causal type.

## Specialist extensions

FX, banking, scientific, software, research and other specialist Skills/Models can extend a C-domain
or form a scoped specialist subdomain. They must declare parent domain and non-portable assumptions.

## Navigation

- [[21_DOMAINS/00_INDEX/DOMAIN_ALIAS_MAP|DOMAIN_ALIAS_MAP]]
- [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|KNOWLEDGE]]
- [[13_MODELS/13_MODELS_MOC|MODELS]]
- [[07_SKILLS/07_SKILLS_MOC|SKILLS]]
- [[08_WORKFLOWS/08_WORKFLOWS_MOC|WORKFLOWS]]

**Parent:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
