---
title: OAUTH GRANT TYPES
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# OAUTH GRANT TYPES

## Grant Types
What is a grant type?
* determines the sequence of steps involved in OAuth process.
* Affects how client app communicates with OAuth at each stage (e.g. how access token is sent)
* Also known as “OAuth flows”
* OAuth service configured to support particular grant type before engaging in flow
* Client specifies what grant type it wants to user
* varies in complexity / security.

OAuth Scopes
* Client must specify which data it wants to access / what operations it wants to perform
* Done using the scope parameter in the authorizatoin request to OAuth
* scope is often unique to each OAuth Service
   	* no set parameter values
   	* could be URI, string etc.
* Basic OpenID Connect scope = openid profile
   	* access to predefined set of basic info on a user

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]