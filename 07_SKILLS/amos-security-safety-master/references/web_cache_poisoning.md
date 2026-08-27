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
