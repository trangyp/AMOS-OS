---
title: SSRF
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


# SSRF
What is it?
* induce server-side application to make HTTP requests to domain of attackers choosing
* maker server make connection back to itself, other web services within organisation or third party stuff.

Impact?
* Result in unauthorised actions/access
* May allow attacker to perform arbitrary command execution (OS COM INJ topic)

Finding Hidden Attack surface for SSRF Vulnerabilities
* Mostly easy to spot (traffic involves request parameters)
* Partial URL's in requests
   	* Sometimes app places hostname or partial URL in request parameters
   	* then incorporated server side.
   	* Hard unless you know the entire URL
* URLs within Data formats
   	* XML, if server processing, could be subject to XXE
* Referer Header
   	* If server side analystics software tracks visitors -> might visit your dody site

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
