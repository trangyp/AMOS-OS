---
title: XSS DOM
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

# XSS DOM

## DOM
DOM-Based XSS
* XSS Triggered through JS changing the HTML
* When app has client-side JS that processes data unsafely (sometimes writing data back to DOM)
* Place data into source so it is propagated to a sink and causes execution of JS
* Common source is a URL
* Work through each available source and test each one individually
* Look at destination, close the tag and add your own tag.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]