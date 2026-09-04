---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: canon
type: reference
source: 07_SKILLS/amos-skill-builder/references
tags:
  - reference
  - amos-skill-builder
  - type/skill
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Skill Builder — Canon Reference

## AMOS Canon Structure

The AMOS canon is the authoritative knowledge base sourced from the Obsidian vault.

### Canon Domains (C01–C12)

| Code | Domain          | Master Skill                  |
| ---- | --------------- | ----------------------------- |
| C01  | Meta Logic      | amos-c01-meta-logic-master    |
| C02  | Physics         | amos-c02-physics-master       |
| C03  | Biology         | amos-c03-biology-master       |
| C04  | Chemistry       | amos-c04-chemistry-master     |
| C05  | Mind & Behavior | amos-c05-mind-behavior-master |
| C06  | Society         | amos-c06-society-master       |
| C07  | Economy         | amos-c07-economy-master       |
| C08  | Technology      | amos-c08-technology-master    |
| C09  | Mathematics     | amos-c09-mathematics-master   |
| C10  | Information     | amos-c10-information-master   |
| C11  | Governance      | amos-c11-governance-master    |
| C12  | Evolution       | amos-c12-evolution-master     |

### Vault Source Paths

- Master knowledge files: `11_KNOWLEDGE/AMOS_C<NN>_<DOMAIN>_MASTER_KNOWLEDGE.md`
- Framework files: `11_KNOWLEDGE/AMOS_<FRAMEWORK>.md`
- Equation registries: `11_KNOWLEDGE/AMOS_<REGISTRY>_EQUATIONS.md`

### Canon Integration Rules

1. All skill content must trace to a vault source file
1. Epistemic class must be labeled per claim
1. No claim beyond the vault source's scope
1. Confidence ceiling enforced per H/M/L level
1. Provenance path recorded for every derived claim

______________________________________________________________________

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-skill-builder-canon
node_type: reference
path: 07_SKILLS/amos-skill-builder/references/canon.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
