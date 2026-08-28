---
title: web cache poisoning
type: reference
source: 07_SKILLS/amos-security-safety-master/references
tags: [reference, amos-security-safety-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Web Cache Poisoning

> Source: `_00_Cosmo brain/misc/W/Web_Cache_Posioning--Web_Cache.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [misc]
---
## Web Cache
How does it work?
* If server had to send new response to every HTTP request seperately, would overload server
   	* cause latency
* Cache sits between user and server
* Save responses to particular requests for amount of time.

What are Cache Keys?
* When recieving a request, determine if there is a cached response or not.
* cache key = predefined subset of request's components
   	* usually includes request line and host header
* EXPLOITABLE FEATURE: all other components (unkeyed) are ignored by the cache
   	* We can add some naughty things in there maybeee?

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[references_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-security-safety-master-web-cache-poisoning
node_type: reference
path: 07_SKILLS/amos-security-safety-master/references/web_cache_poisoning.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
