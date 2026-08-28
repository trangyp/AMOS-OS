---
title: SSRF BLIND VULNERABILITIES
tags:
- misc
- reference
- general
- canon/knowledge
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# SSRF BLIND VULNERABILITIES

## Blind vulnerabilities
Overview
* When the back-end response is not returned in apps front-end
* Impact often lower than full SSRF vulnerabilities (one way nature)
* Could possibly get RCE

How to find and exploit
* Use OAST techniques
* Trigger HTTP request to external system you control
* Burp Collaborator
* NOTE: Often HTTP blocked by network, but you can do a sneaky with DNS
* Change the referer to your website to check for the response 
* If HTTP request observered coming in from the app, you can do an SSRF

How to attacks
* Leverage to probe for other vulnerabilities on server
* Blindly sweep internal IP address space

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]