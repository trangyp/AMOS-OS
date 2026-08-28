---
title: CSRF XSS VS CSRF
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# CSRF XSS VS CSRF

## XSS vs CSRF
What is the difference?
* XSS = attacker executes arbitrary JS within browser of victim
* CSRF = attacker induce victim user to perform actions that they don't intend to.
* XSS vulnerabilities more serious
* CSRF only applies to subset actions user can perform
   	* Apps often implement CSRF but overlook 1-2 actions
   	* Whereas, successful XSS can perform anything
* CSRF = “one-way” vulnerability
   	* Can induce a HTTP request, but can't retrieve the response

Can CSRF tokens prevent XSS attacks?
* Some attacks can be prevented
* If an XSS attack requires a token, then attack is prevented
* CSRF tokens don't protect against stored XSS, mostly reflected.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]