---
title: DOM BASED SINKS LEADING TO DOM BASED VULNS
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general

---

# DOM BASED SINKS LEADING TO DOM BASED VULNS

## Sinks leading to DOM-based vulns

### Open Redirection
- `window.location` / `window.location.href` — assignment to location object with user input
- `location.assign()` / `location.replace()` — programmatic redirect with user input
- `element.src` — setting iframe/script/img src to user-controlled URL
- `form.action` — setting form action to user-controlled URL

### DOM-based XSS
- `innerHTML` / `outerHTML` — writing user input to DOM without sanitisation
- `document.write()` — writing user input directly to document
- `eval()` / `setTimeout(string)` / `setInterval(string)` — executing user input as code
- `element.insertAdjacentHTML()` — inserting unsanitised HTML
- `document.createElement()` + `innerHTML` — creating elements with unsanitised content

### Cookie Manipulation
- `document.cookie` — writing user input to cookie store
- Cookie injection via `Set-Cookie` header reflection

### DOM Clobbering
- `element.id` / `element.name` — naming elements to clobber global variables
- `<form><input name="attributes">` — clobbering DOM properties

### WebSocket Hijacking
- `new WebSocket(userUrl)` — connecting to attacker-controlled WebSocket server
- Cross-site WebSocket hijacking (CSWSH)

### Local Storage / Session Storage
- `localStorage.setItem()` / `sessionStorage.setItem()` — storing unsanitised user input
- Reading and injecting stored data into DOM without sanitisation

### PostMessage
- `window.postMessage()` — sending data to arbitrary frames without origin check
- `window.addEventListener('message', ...)` — receiving messages without origin validation

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]