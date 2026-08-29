---
title: access control priv esc
type: reference
source: 07_SKILLS/amos-security-safety-master/references
tags:
- reference
- amos-security-safety-master
- type/skill
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

# Access Control Privilege Escalation Vertical

> Source: `_00_Cosmo brain/control/Access_Control-Priv_Esc--Vertical_Access.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [control]
---
## Vertical Access
Overview
* restricts access to functionality based on TYPE of user
* e.g. Admin vs Basic User
* Gaining access to functionality not in their type is vertical privlege escalation.

Unprotected Functionality
* Accessing an admin only function. If the functionality isn't protected, anyone can access it
* View robots.txt to have a look at file structure.
* Security by Obscurity: concealing a less predictable URL
* View the HTML and scripts to see if “protected” URL's are referenced in the code

Parameter-based access control methods
* Some apps determine roles at login then store info in user controllable location
   	* hidden field
   	* cookie
   	* preset query string param
   	* https://insecure-website.com/login/home.jsp?admin=true
   	* https://insecure-website.com/login/home.jsp?role=1

Broken Access control resulting from platform misconfig
* Platform layer controls.
* Restrict access to specific URLs and HTTP methods based on role.
   	* DENY: POST, /admin/deleteUser, managers
* Non-Standard HTTP headers that can override URL of original request
   	* X-Original-URL & X-Rewrite-URL /admin
   	* Order is: http://URL/X-Original-URL/REQUEST-URL
* /admin-roles
* If you have access to admin account, perform desired action and trace requests in Burp
   	* Then attempt to perform that same activity with a non-admin's cookie.
   	* Change POST request to POSTX or GET?

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

---
**MOC:** references_MOC
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-security-safety-master-access-control-priv-esc
node_type: reference
path: 07_SKILLS/amos-security-safety-master/references/access_control_priv_esc.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
