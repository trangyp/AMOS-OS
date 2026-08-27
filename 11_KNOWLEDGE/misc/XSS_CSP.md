---
title: XSS CSP
tags: [misc]
type: document
source: 11_KNOWLEDGE/misc
---


## CSP
What is it?
* Browser Security Mechanism that mitigates XSS and other attacks
* restricts resources (scripts, images etc.) that a page loads
* Stops pages being framed by others
* Enabled through HTTP Response header: Content-Security-Policy
* Generates a nonce (random value) unguessable by an attacker - noonce must match for a script to execute.
* Or they can take a hash.

Bypassing with policy injection
* inject a ; to add your own CSP directives.
* You will need to overwrite existing directives in order to exploit this vulnerability and bypass the policy.

Protecting against clickjacking
* Framing:
   	* ‘self’ allows page to be framed by other pages of same origin
   	* ‘none’ prevents framing
   	* You can also specify specific and multiple domains

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
