---
title: XSS STORED
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

# XSS STORED

## Stored
Stored XSS
* AKA Persistant XSS. 
* Receive data from untrusted source and includes that data in HTTP response
* Control a script that is executed whenever another user accesses the site
* Example: posting a comment on a blog. If you post a script, sometimes that script will run whenever another person accesses that blog.
* Difference to Reflected: enables attacks that are self-contained within the application
   	* No external way of inducing another user to participate (reflected must be triggered by an action. The action for stored, is just accessing the webpage)
* Only impacts users accessing site (logged in)
* Test entry and exit points & locate the links
* Entries:
	* Params in URL query string/message body
	* URL file path
	* HTTP Request headers

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]