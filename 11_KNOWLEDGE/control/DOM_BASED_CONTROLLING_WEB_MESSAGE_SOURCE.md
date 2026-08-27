---
tags: [control]
---
## Controlling web-message source
What is it
* web messages can be used as a source
* unsafe = not verifying the origin of incoming messages correctly in event listener, properties and functions called by listener

Impact
* Dependent on destination doc's handling of incoming message.
* Compromise accounts.

How to construct an attack
* Identify a target page that uses `postMessage` without origin verification in its `message` event listener
* Craft a malicious page that calls `targetWindow.postMessage(payload, '*')` with `*` as targetOrigin, bypassing origin restrictions
* If the listener does not check `event.origin` before acting on the message, the payload is processed as if it came from a trusted source
* Exploit the listener's DOM manipulation: the message may trigger `eval()`, `innerHTML` assignment, redirect, or data exfiltration
* For embedded frames: if the parent page listens for messages from a child frame without origin validation, an attacker can inject a malicious child frame that sends crafted messages
* For cross-origin messaging: exploit `event.source` to send a reply to a different window, creating a confused-deputy scenario where the trusted page acts on behalf of the attacker

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
