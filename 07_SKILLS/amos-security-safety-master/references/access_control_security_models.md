---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Access Control Security Models
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

# Access Control & Privilege Escalation Security Models

> Source: `_00_Cosmo brain/security/Access_Control-Priv_Esc--Security_Models.md`
> Epistemic class: SOURCE_DERIVED

______________________________________________________________________

## tags: [security]

## Security Models

What is it?

- Formally defined definition of set access control rules independent of tech + implementation platform
- Implemented outside of OS, Networks, DBMS, back office, app and server software
- Various styles:

Programmatic access control

- matrix of user privledges stored in DB applied programmaticly,
- Includes roles, groups, individual users, collections, workflows, processes
- Granular

Discretionary Access Control (DAC)

- constraints based on users or named groups of users
- Owners of resources/functions delegate access permissions
- Very complex to design and manage (lots of individuals in charge of delegating access)

Mandatory Access Control (MAC)

- centrally controlled system of controls
- Very different to DAC : new user control over access
- Associated with military clearance-based systems

Role-based Access Control (RBAC)

- Named roles desined to which access privledges assigned
- Users assigned 1+ roles
- Enhanced management over models.
- Easy to revoke and define group membership

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

______________________________________________________________________

## **MOC:** references_MOC

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-security-safety-master-access-control-security-models
node_type: reference
path: 07_SKILLS/amos-security-safety-master/references/access_control_security_models.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
