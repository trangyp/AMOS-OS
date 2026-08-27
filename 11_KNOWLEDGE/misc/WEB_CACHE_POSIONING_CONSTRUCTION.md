---
title: WEB CACHE POSIONING CONSTRUCTION
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general

---

# WEB CACHE POSIONING CONSTRUCTION

## Construction
Identify and evaluate unkeyed inputs
* inject your payload in an unkeyed element
* add random inputs to request and observe impact on the response
   	* sometimes hard to notice, there are other techniques listed bellow.
Param Miner
* Extension in Burp
* Right click on request and select “Guess Headers”
* Logged in 2 places:
   	* BurpPRO: Issues pane
   	* BurpCOM: Extender>Extensions>Param Miner>Output


Elicit harmful response from back-end server
* Evaluate how website processes it
* It is a potential entry for poisoning if:
   	* input reflected in response without sanitisation
   	* response used to dynamically generate other data

Get response cached
* success depends on file extensions, content type, route, status code, response headers

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]