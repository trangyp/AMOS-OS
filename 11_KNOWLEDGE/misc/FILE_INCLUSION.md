---
title: FILE INCLUSION
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


# File Inclusion
* [CHECKLIST](https://www.onsecurity.io/blog/file-upload-checklist/#magic-byte-forgery)
* Often used to load classes, share templates between web pages
* Vulnerability comes from lack of filtering of user-controlled parameters in file name.
* PHP:
   	* Require, require_once, include, include_once
* LFI (Local) and RFI (Remote) vulnerability escalations
* PHP disables loading remote files by default
   	* allow_url_include
* Use techniques from dir traversal to detect LFI
* Request external resources (other URLS) to detect RFI
   	*  http://assets.pentesterlab.com/test_include_system.txt.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
