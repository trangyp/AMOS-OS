---
title: cors security
type: reference
source: 07_SKILLS/amos-security-safety-master/references
tags:
- reference
- amos-security-safety-master
- type/skill
- system-scan-agent
- automation-profiles
- amos-simulation-kernel-v0-math-foundations
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# CORS Access Control

> Source: `_00_Cosmo brain/control/CORS--Access-Control-Allow-Origin_Header.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [control]
---
## Access-Control-Allow-Origin Header
Overview
* CORS specs provides controlled relaxation on the same-origin policy for HTTP requests
* The header is included to enable this if the other website has the same header

Implementing Simple Cross-Origin resource Sharing
* The header can contain multiple origins or NULL.
* Request Origin needs to be in Response ACAO.

Handling cross-origin resource requests with credentials
* If you want to send across credentials (like cookies) you set Access-Control-All-Credentials to true

Relaxation of CORS specs w/ Wildcards
* ACAO supports wildcard * (when used in isolation)
* wildcard is restricted in specs
   	* Can't combine * with cross-origin transfers of credentials (authentication, cookies, client-side certs)
   	* Security feature.

Pre-flight checks
* added to CORS specs to protect legacy resources
* Adds extra HTTP request round-trip to request, so increase browsing overhead.
* Sometimes, cross domain request includes non-standard HTTP methods or headers
   	* pre-flight checks, checks if the methods/headers in a request are permitted before performing them
EXAMPLE
OPTIONS /data HTTP/1.1
   Host: <some website>
   ...
   Origin: https://normal-website.com
   Access-Control-Request-Method: PUT
   Access-Control-Request-Headers: Special-Request-Header

 ---- RESPONDS WITH ----

 HTTP/1.1 204 No Content
   ...
   Access-Control-Allow-Origin: https://normal-website.com
   Access-Control-Allow-Methods: PUT, POST, OPTIONS
   Access-Control-Allow-Headers: Special-Request-Header
   Access-Control-Allow-Credentials: true
   Access-Control-Max-Age: 240

Does CORS protect against CSRF?
* Doesn't!!!
* Common misconception
* CORS = controlled relaxation of same-origin policy
* If poorly configured, might increase possibility of CSRF

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
node_id: amos-security-safety-master-cors-security
node_type: reference
path: 07_SKILLS/amos-security-safety-master/references/cors_security.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
