---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Horizontal Access Control
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

# Horizontal Access Control

> Source: `_00_Cosmo brain/control/Access_Control-Priv_Esc--Horizontal_Access.md`
> Epistemic class: SOURCE_DERIVED

______________________________________________________________________

## tags: [control]

## Horizontal Access

Overview

- Access control for specific users, rather than groups
- e.g. banking applications let you view your account + make transactions, but not other people's accounts
- Gaining access to resources that belong to another user.

Basic Tactics

- If there is an ID in the URL params or storage, change it.
  - Can find ID by guessing. Or exploring other places it could be exposes (messages, reviews)
  - Poke around web page and find places the user has interacted in the past (maybe a blog post?)
- If you are getting redirected:
  - Look at response containing redirect (could contain sensitive data)

Horizontal to Vertical privledge escalation

- Try and force the page to react to an admins account to get some info, then log in as admin.

Insecure Direct Object References (IDOR)

- Subcategory of access control vulnerabilities.
- When app uses user-supplied input to access objects directly.
- Explore other files on the system if there is a download link.
- More on another page
  Direct reference to DB objects
- If you have access to DB, you can upgrade your own privledges
  Direct reference to static files
- sensitive resources sometimes located in static files on server-side filesystem.
- Sometimes files are saved with incrementing values -> if you have been asked to save file4, try and access file3

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

______________________________________________________________________

## **MOC:** references_MOC

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-security-safety-master-horizontal-access-control
node_type: reference
path: 07_SKILLS/amos-security-safety-master/references/horizontal_access_control.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
