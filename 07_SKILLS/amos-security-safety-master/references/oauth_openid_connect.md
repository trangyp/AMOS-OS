---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: oauth openid connect
type: reference
source: 07_SKILLS/amos-security-safety-master/references
tags:
  - reference
  - amos-security-safety-master
  - type/skill
  - system-scan-agent
  - automation-profiles
  - amos-simulation-kernel-v0-math-foundations
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# OAuth and OpenID Connect

> Source: `_00_Cosmo brain/misc/O/OAuth--OpenID_Connect.md`
> Epistemic class: SOURCE_DERIVED

______________________________________________________________________

## tags: [misc]

## OpenID Connect

What is OpenID Connect?

- extends OAuth protocol to provide dedicated identity/auth layer on top of basic implementation.
- better support for auth case of OAuth
- was not designed for auth -> more for delegation of authority for resources between apps
- Issues: people using it to authenticate users were just doing workarounds and couldn't maintain user authentication
  - no standard way of requesting data for this purpose
- that's what OpenId was created for

How does it work ?

- additional standardized set of scopes that are the same for all providers
- Extra response type: id_token

Roles

- Relying Party - applicaiton requesting authentication of a user (like OAuth client)
- End user - user being authenticated (like resource owner)
- OpenID Provider - OAuth service configured to support OpenID Connect

Claims and Scopes

- claims = key:value pairs representing information on the user on the resource server
- scopes are the same across all OpenID Services
  - Must specify openid and 1 or more other standards:
    \- profile
    \- email
    \- address
    \- phone
  - read access for subset of claims about user

ID Token

- returns JWT with signed JWS
- contains list of cliams based on scope initially requested
- contains info about how/when user was last authenticated by OAuth service.
- Allows client to decide whether the user has been sufficiently authenticated.
- reduces the number of requests that need to be sent between the client and OAuth service (improve performance)
- Integrity of the data is based on JWT signature -> protection against PITM attacks

Identifying OpenID Connect

- obvious through authorization request.
- Look for mandatory openid scope
- check whether the OAuth service supports it
  - Check the providers documentation for any useful info
  - access config file via /.well-known/openid

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

______________________________________________________________________

## **MOC:** references_MOC

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-security-safety-master-oauth-openid-connect
node_type: reference
path: 07_SKILLS/amos-security-safety-master/references/oauth_openid_connect.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
