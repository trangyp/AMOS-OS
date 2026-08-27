---
title: WEB SOCKETS WHAT IS IT
tags: [misc]
type: document
source: 11_KNOWLEDGE/misc
---


## What is it?
* Bi-directional communications protocol over HTTP
* used for streaming data and async traffic

Difference to HTTP
* Most communication on web uses HTTP
* HTTP is Request and response
* WS initiated over HTTP, long-lived.
   	* Not transactional
* WS useful when low-latency / server-initiated messages required
   	* real-time feeds.

How are connections established?
* Normally created with Client-side JS
* var ws = new WebSocket("wss://normal-website.com/chat");
* WSS protocol: establish WS over encrypted TLS connection
   	* WS is unencrupted
* Browser and server WS handshake over HTTP
   	* Connection / Upgrade headers indicate handshake
   	* Sec-WebSocket-Key header Base64-encoded random value each request
   	* Sec-WebSocket-Accept header is hash of value submitted in key. Prevents misleading responsing from misconfigured servers

What do they look like?
* send message:
   	* ws.send("Peter Wiener");
* Can be sent in any data format, JSON is common
   	* {"user":"Hal Pline","content":"I wanted to be a Playstation growing up, not a device to answer your inane questions"}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
