---
title: "21 Domains — README"
type: readme
source: 21_DOMAINS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: domains_readme
---

# 21 Domains — README

## Role

Domain-specific specialization — logic, math, physics, biology, cognition, society, economics, law, strategy, engineering, design, ecology. Domains are the "what" of AMOS knowledge: they define the subject-matter expertise that informs reasoning and decision-making.

## Core Principle

```
Domain knowledge is contextual, not universal.
All domain claims require domain-specific evidence and validation.
```

## Directory Structure

```
21_DOMAINS/
├── 00_INDEX/              ← Domain indices and navigation registries
├── 01_DOMAIN_ARCHITECTURE/ ← Domain architecture definitions
├── 11_C01_META_LOGIC/     ← C01 Meta-Logic domain
├── 12_C02_MATH_COMPUTE/   ← C02 Math-Compute domain
├── 13_C03_PHYSICS_COSMOS/ ← C03 Physics-Cosmos domain
├── 14_C04_BIO_NEURO/      ← C04 Bio-Neuro domain
├── 15_C05_MIND_BEHAVIOR/  ← C05 Mind-Behavior domain
├── 16_C06_SOCIETY_CULTURE/ ← C06 Society-Culture domain
├── 17_C07_ECON_FINANCE/   ← C07 Econ-Finance domain
├── 18_C08_STRATEGY_GAME/  ← C08 Strategy-Game domain
├── 19_C09_ORG_LAW_POLICY/ ← C09 Org-Law-Policy domain
├── 20_C10_TECH_ENGINEERING/ ← C10 Tech-Engineering domain
├── 21_C11_DESIGN_LANGUAGE/ ← C11 Design-Language domain
├── 22_C12_EARTH_ECOLOGY/  ← C12 Earth-Ecology domain
├── 23_UBI_BEI_BIOELECTROMAGNETIC/ ← UBI-BEI domain
├── 24_UBI_NBI_NEUROBIOLOGICAL/ ← UBI-NBI domain
├── 25_UBI_NEI_NEUROEMOTIONAL/ ← UBI-NEI domain
├── 26_UBI_SI_SOMATIC/     ← UBI-SI domain
├── 27_UBI_SUPER/          ← UBI Super domain
├── 28_ENGINEERING_MATH/   ← Engineering-Math domain
├── 29_MEDICAL_CLINICAL/   ← Medical-Clinical domain
├── ... (45+ domain directories total)
├── 21_DOMAINS_MOC.md      ← Master map of content for the Domains plane
└── DOMAINS_DOMAIN_ALIAS_CONTRACT.md ← Domain alias governance contract
```

## Domain Categories

- **Formal Sciences:** [[11_C01_META_LOGIC|C01 Meta-Logic]], [[12_C02_MATH_COMPUTE|C02 Math-Compute]], [[13_C03_PHYSICS_COSMOS|C03 Physics-Cosmos]]
- **Natural Sciences:** [[22_C12_EARTH_ECOLOGY|C12 Earth-Ecology]], [[24_UBI_NBI_NEUROBIOLOGICAL|UBI-NBI Neurobiological]], [[25_UBI_NEI_NEUROEMOTIONAL|UBI-NEI Neuroemotional]]
- **Social Sciences:** [[15_C05_MIND_BEHAVIOR|C05 Mind-Behavior]], [[16_C06_SOCIETY_CULTURE|C06 Society-Culture]], [[17_C07_ECON_FINANCE|C07 Econ-Finance]]
- **Applied Sciences:** [[18_C08_STRATEGY_GAME|C08 Strategy-Game]], [[19_C09_ORG_LAW_POLICY|C09 Org-Law-Policy]], [[20_C10_TECH_ENGINEERING|C10 Tech-Engineering]], [[21_C11_DESIGN_LANGUAGE|C11 Design-Language]]
- **Professional Domains:** [[28_ENGINEERING_MATH|Engineering-Math]], [[29_MEDICAL_CLINICAL|Medical-Clinical]], [[30_CLINICAL_RESEARCH|Clinical-Research]], [[31_CONTROL_SYSTEMS|Control-Systems]]
- **Business Domains:** [[33_ORGANIZATIONAL_BEHAVIOR|Org-Behavior]], [[34_HEALTH_POLICY|Health-Policy]], [[35_BUSINESS_ANALYSIS|Business-Analysis]], [[36_MARKET_INTELLIGENCE|Market-Intelligence]]
- **Technology Domains:** [[37_TECH_ARCHITECTURE|Tech-Architecture]], [[41_QUANTUM_SYSTEMS|Quantum-Systems]], [[44_EV_INFRASTRUCTURE|EV-Infrastructure]]
- **Geopolitical Domains:** [[39_POLITICS_POWER|Politics-Power]], [[40_HSE_SAFETY|HSE-Safety]], [[42_SECTOR_VALUE_CHAIN|Sector-Value-Chain]], [[43_GEO_GEOPOLITICS|Geo-Geopolitics]]
- **Meta-Domains:** [[45_MODES|Modes]], [[03_FOREX|Forex]]

## Hard Boundaries

- **Domain != Authority** — domain knowledge is contextual; it does not override governance
- **Domain Expertise != Universal Truth** — domain claims require domain-specific evidence
- **Domain Overlap != Conflict** — multiple domains can legitimately address the same topic from different perspectives
- **Domain Specificity != Domain Isolation** — domains interact through governed interfaces

## Routing Rules

- **LoadDomain only if DomainCanMateriallyChangeOutcome** — don't load domain knowledge for trivial decisions
- **Domain Evidence Overrides General Knowledge** — when domain-specific evidence exists, it takes precedence
- **Domain Conflicts Require Resolution** — when domains disagree, escalate to governance

## Key Artifacts

- **Domain Alias Contract:** [[21_DOMAINS/DOMAINS_DOMAIN_ALIAS_CONTRACT|Domain Alias Contract]] — governance for domain aliases
- **Domain Architecture:** `01_DOMAIN_ARCHITECTURE/` — domain structure and routing definitions
- **C01–C12 Canonical:** 12 domain directories mapping to AMOS knowledge master files; **UBI Domains:** 5 sub-domains (BEI, NBI, NEI, SI, Super)

## Canonical Laws Governing

- **M07 (Canon ≠ Implementation):** Domain specifications are not runtime implementations
- **CAPABILITY ≠ AUTHORITY:** Domain expertise does not grant execution authority
- **Domain knowledge is contextual:** All domain claims require domain-specific evidence and validation

## Cross-Plane Relationships

- **Knowledge:** [[11_KNOWLEDGE/KNOWLEDGE_CONTRACT|KNOWLEDGE_CONTRACT]] — Domains structure knowledge; knowledge is organized by domain
- **Skills:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] — Skills are domain-specific; domains define skill applicability
- **Research:** [[22_RESEARCH/22_RESEARCH_README|22_RESEARCH_README]] — Research produces domain-specific evidence
- **Cognitive Matrix:** [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_README|25_COGNITIVE_MATRIX_README]] — Domains feed cognitive matrix reasoning

## Entry Points

- **Master MOC:** [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]] · **Alias Contract:** [[21_DOMAINS/DOMAINS_DOMAIN_ALIAS_CONTRACT|Alias Contract]]

## Implementation Status

- **Structural completeness:** 45+ domain directories covering formal, natural, social, applied, professional, business, technology, and geopolitical domains
- **C01–C12 canonical:** 12 canonical domain directories aligned with AMOS knowledge master files
- **UBI domains:** 5 biological intelligence sub-domains (BEI, NBI, NEI, SI, Super) structurally present
- **Executable closure:** UNKNOWN/GAP — domain directories are structural organization unless tied to executed domain routing evidence

## AMOS MECE Alignment

The Domains Plane is Plane 21 of 26. It is mutually exclusive from Knowledge (11_KNOWLEDGE, which owns epistemic infrastructure) and Research (22_RESEARCH, which produces evidence). It is collectively exhaustive with all other planes in covering the subject-matter-routing dimension. MECE boundary: it owns domain-specific specialization and routing, not epistemic claims, evidence production, or skill definitions.

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
