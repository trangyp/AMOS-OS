---
title: access control security models
type: reference
source: 07_SKILLS/amos-security-safety-master/references
tags:
- reference
- amos-security-safety-master
- canon/skill
- 00-home
- knowledge-moc
- system-scan-agent
- automation-profiles
- references-moc
- amos-simulation-kernel-v0-math-foundations
- amos-rscf-nodes
- law-hierarchy
- 07-skills-moc
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Access Control & Privilege Escalation Security Models

> Source: `_00_Cosmo brain/security/Access_Control-Priv_Esc--Security_Models.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [security]
---
## Security Models
What is it?
* Formally defined definition of set access control rules independent of tech + implementation platform
* Implemented outside of OS, Networks, DBMS, back office, app and server software
* Various styles:

Programmatic access control
* matrix of user privledges stored in DB applied programmaticly,
* Includes roles, groups, individual users, collections, workflows, processes
* Granular

Discretionary Access Control (DAC)
* constraints based on users or named groups of users
* Owners of resources/functions delegate access permissions
* Very complex to design and manage (lots of individuals in charge of delegating access)

Mandatory Access Control (MAC)
* centrally controlled system of controls
* Very different to DAC : new user control over access
* Associated with military clearance-based systems

Role-based Access Control (RBAC)
* Named roles desined to which access privledges assigned
* Users assigned 1+ roles
* Enhanced management over models.
* Easy to revoke and define group membership

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[references_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-security-safety-master-access-control-security-models
node_type: reference
path: 07_SKILLS/amos-security-safety-master/references/access_control_security_models.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
