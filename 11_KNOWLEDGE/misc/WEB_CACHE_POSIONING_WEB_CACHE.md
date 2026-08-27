---
title: WEB CACHE POSIONING WEB CACHE
tags: [misc, reference, general]
type: document
source: 11_KNOWLEDGE/misc
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
**MOC:** [[MISC_MOC]]
