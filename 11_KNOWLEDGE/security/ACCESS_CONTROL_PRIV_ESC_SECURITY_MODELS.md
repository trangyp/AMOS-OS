---
title: ACCESS CONTROL PRIV ESC SECURITY MODELS
tags:
- security
- safety
- adversarial
- canon/knowledge
type: document
source: 11_KNOWLEDGE/security
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: security_model
---

# ACCESS CONTROL PRIV ESC SECURITY MODELS

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
**MOC:** [[security_MOC]]