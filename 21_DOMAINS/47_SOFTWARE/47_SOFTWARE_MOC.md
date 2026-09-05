---
title: 01 Software MOC
type: moc
source: 21_DOMAINS/47_SOFTWARE
tags:
  - 01-software
  - canon/domain
  - software-domains-domain-spec
  - software-domains-interfaces
  - software-domains-provenance
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 01 Software — Map of Content

**Path:** `21_DOMAINS/47_SOFTWARE`
**Files:** 5 | **Subdirectories:** 1

## Files

- [[21_DOMAINS/47_SOFTWARE/DOMAINS_SOFTWARE_CONTRACT|DOMAINS_SOFTWARE_CONTRACT]]
- [[21_DOMAINS/47_SOFTWARE/SOFTWARE_DOMAINS_DOMAIN_SPEC|SOFTWARE_DOMAINS_DOMAIN_SPEC]]
- [[21_DOMAINS/47_SOFTWARE/SOFTWARE_DOMAINS_INTERFACES|SOFTWARE_DOMAINS_INTERFACES]]
- [[21_DOMAINS/47_SOFTWARE/SOFTWARE_DOMAINS_PROVENANCE|SOFTWARE_DOMAINS_PROVENANCE]]
- [[21_DOMAINS/47_SOFTWARE/SOFTWARE_DOMAINS_README|SOFTWARE_DOMAINS_README]]

## Subdirectories

- [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] — 00_INDEX

______________________________________________________________________


## Domain Scope

The Software domain covers all aspects of software engineering, development, and architecture within AMOS OS:

### Sub-domains
- **Software architecture**: microservices, monolithic, event-driven, serverless; clean architecture, DDD, hexagonal
- **Software lifecycle**: requirements, design, implementation, testing, deployment, maintenance; SDLC models (waterfall, agile, DevOps)
- **Software quality**: ISO/IEC 25010 (8 quality characteristics); maintainability, reliability, security, performance efficiency
- **Software ecosystems**: package management, dependency resolution, supply chain security (SBOM, Sigstore, SLSA)

### SOTA Methods
- **Languages**: Rust (memory safety), Go (concurrency), TypeScript (type safety), Python (ML), Zig (systems)
- **Frameworks**: React 19 (server components), Next.js 15, Vue 3, Svelte 5; Go (Axum, Actix), Node 22
- **Cloud-native**: Kubernetes 1.30, Istio, ArgoCD, Flux; containers (Docker, Podman); OCI standards
- **AI-assisted**: GitHub Copilot, Cursor, Claude Code, GPT-6 Astra; SWE-bench; automated program repair

### AMOS Integration
- **C10 domain**: [[21_DOMAINS/20_C10_TECH_ENGINEERING/20_C10_TECH_ENGINEERING_MOC|C10 tech-engineering domain]]
- **Coding engine**: [[11_KNOWLEDGE/engine/AMOS_CODING_ENGINE_LAYER|Coding Engine Layer]]
- **Deployment engine**: [[11_KNOWLEDGE/engine/DEPLOYMENT_ENGINE|Deployment Engine]]
- **Engineering standards**: [[11_KNOWLEDGE/engine/ENGINEERING_STANDARDS_LIBRARY|Engineering Standards Library]]

### Invariants
1. `CODE_GENERATED != CODE_CORRECT` — LLM-generated code requires verification
2. `CODE_COMPILES != CODE_WORKS` — compilation does not guarantee correctness
3. All software claims must cite provenance (language, framework, version, test status)
4. `CAPABILITY != AUTHORITY` — ability to generate code does not grant deployment authority


**Parent:** [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]
