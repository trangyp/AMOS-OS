---
title: WEB SOCKETS
tags: [misc]
type: document
source: 11_KNOWLEDGE/misc
---


# Web Sockets
* Any HTTP basesd attacks (mostly) can be performed

Security Vulns
* If User-supplied input transmitted: SQLI, XXE
* Blind Vuns (used OAST)
* If data transmitted sent to other users: XSS, Client-side vulns

How to secure a WS connection (prevention)
* use WSS:// protocol (TLS, encrypted)
* Hard code URL of WS endpoint, don't incorporate user-controllable data in URL
* Protect against CSRF
* Treat data as untrusted in both directions

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
