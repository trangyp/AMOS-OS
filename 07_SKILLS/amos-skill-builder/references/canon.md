---
title: canon
type: reference
source: 07_SKILLS/amos-skill-builder/references
tags: [reference, amos-skill-builder, canon/skill]
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
| Code | Domain | Master Skill |
|------|--------|-------------|
| C01 | Meta Logic | amos-c01-meta-logic-master |
| C02 | Physics | amos-c02-physics-master |
| C03 | Biology | amos-c03-biology-master |
| C04 | Chemistry | amos-c04-chemistry-master |
| C05 | Mind & Behavior | amos-c05-mind-behavior-master |
| C06 | Society | amos-c06-society-master |
| C07 | Economy | amos-c07-economy-master |
| C08 | Technology | amos-c08-technology-master |
| C09 | Mathematics | amos-c09-mathematics-master |
| C10 | Information | amos-c10-information-master |
| C11 | Governance | amos-c11-governance-master |
| C12 | Evolution | amos-c12-evolution-master |

### Vault Source Paths
- Master knowledge files: `11_KNOWLEDGE/AMOS_C<NN>_<DOMAIN>_MASTER_KNOWLEDGE.md`
- Framework files: `11_KNOWLEDGE/AMOS_<FRAMEWORK>.md`
- Equation registries: `11_KNOWLEDGE/AMOS_<REGISTRY>_EQUATIONS.md`

### Canon Integration Rules
1. All skill content must trace to a vault source file
2. Epistemic class must be labeled per claim
3. No claim beyond the vault source's scope
4. Confidence ceiling enforced per H/M/L level
5. Provenance path recorded for every derived claim

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
