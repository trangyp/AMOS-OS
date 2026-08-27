---
title: CLICK JACKING
tags: [misc]
type: document
source: 11_KNOWLEDGE/misc
---


# Click Jacking
What is it?
* interface-based attack
* user tricked to clicking on actionable content
* On hidden website
* Dependent on incorporation of invisible iframe containing a button
* iframe hidden behind (dodgy one)
* Different from CSRF attack
   	* user is required to perform an action.
   	* CSRF depends on forging entire request without knowledge of user.
* attack not mitigated by CSRF token

Prevention
* Server driven protocols
* define / communicate constraints
* X-Frame-Options and CSP

X-Frame-Options
* Website owner has control of use of iframes/objects in their page
* X-Frame-Options:
   	* deny
   	* sameorigin
   	* allow-from https://normal-website.com
* Use in conjunction with CSP for multi-layer defense

CSP
* detection and prevention mechanism
* provides client browser with info about permitting web resources
* incorporate frame-ancestors directive
   	* ‘none' ‘self’ ‘normal-website.com’
   	* similar to X-Frame-Options

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
