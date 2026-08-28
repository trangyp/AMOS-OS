---
title: HTTP HOST HEADER ATTACKS
tags:
- misc
- reference
- general
- canon/knowledge
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# HTTP Host Header Attacks

## Overview
HTTP Host Header attacks exploit applications that implicitly trust the `Host` header to construct URLs, perform redirects, or route requests. When the server fails to validate the Host header, attackers can inject malicious values to achieve cache poisoning, password reset poisoning, or SSRF.

## Attack Vectors

### Web Cache Poisoning
- Inject a malicious Host header that gets cached by a CDN/proxy
- Victims receive the cached poisoned response with attacker-controlled URLs
- Affects all users behind the same cache

### Password Reset Poisoning
- Application constructs password reset links using the Host header
- Attacker sends reset request with `Host: attacker.com`
- Victim receives email with reset link pointing to attacker's domain
- Attacker captures the reset token

### Routing-Based SSRF
- Applications that make backend requests based on Host header
- Attacker redirects internal requests to attacker-controlled server
- Can access internal services or cloud metadata endpoints

### Virtual Host Confusion
- Multiple apps on same server, routing by Host header
- Attacker accesses one app's functionality via another app's domain
- Bypasses access controls that rely on virtual host separation

### Host Header Injection in Business Logic
- Email templates that embed Host-derived URLs
- OAuth redirect URIs constructed from Host header
- Webhook registration URLs that trust Host header

## Detection
- Send requests with arbitrary Host header values and observe behaviour
- Check if password reset emails contain attacker-controlled URLs
- Test for cache poisoning via CDN with mismatched Host headers
- Monitor for Host header values that don't match expected domains

## Mitigation
- **Validate Host header** against an allow-list of expected domains
- **Configure web server** to reject unexpected Host values
- **Use absolute URLs** in emails and redirects instead of Host-derived URLs
- **Separate virtual hosts** at the network level, not just by Host header
- **Disable Host header override** (e.g., `X-Forwarded-Host`) unless explicitly needed
- **Use SNI** for TLS to prevent virtual host confusion

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
