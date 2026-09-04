---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: access control
type: reference
source: 07_SKILLS/amos-security-safety-master/references
tags:
  - reference
  - amos-security-safety-master
  - type/skill
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Access Control & Privilege Escalation

> Source: `_00_Cosmo brain/control/Access_Control-Priv_Esc.md`
> Epistemic class: SOURCE_CANON

______________________________________________________________________

## tags: [control]

## Access Control/Priv Esc

What is it?

- Application of constraints on who/what actions can be performed
- Access control is dependent on authentication and session management.
- Authentication: identifies and confirms user
- Session Management: identifies which HTTP requests are made by same user
- Access Control: determines whether a user can carry out an action

Prevention

- Don't rely on obfuscation for access control
- All non-publically accessible resources should be denied by default
- Use signle application-wide mechanisms for enforcing access controls
- Mandate developers to declare the allowed access for each resource and deny access by default
- Audit and test to ensure they are working as designed.

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS Simulation Kernel v0 Math Foundations · system scan agent · automation profiles

______________________________________________________________________

## **MOC:** references_MOC

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-security-safety-master-access-control
node_type: reference
path: 07_SKILLS/amos-security-safety-master/references/access_control.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
