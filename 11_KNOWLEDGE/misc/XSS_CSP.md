---
tags: [misc]
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
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
