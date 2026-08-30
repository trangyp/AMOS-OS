---
title: LEGAL ENGINE MODEL
type: model
source: 11_KNOWLEDGE/engine
aliases:
- Legal Engine Kernel
- AMOS_Legal_Engine
tags:
- canon-group/tech-ai
- canon/model
- rscf/claim
- rscf/provenance
- rscf/state/derived
- topic/legal-engine-model
- engine
- system-scan-agent
- automation-profiles
- amos-simulation-kernel-v0-math-foundations
- trang-framework-recursive-ontology-dynamics
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: engine_specification
---

# AMOS Legal Engine Kernel

**Version:** vInfinity_Legal_Kernel_1.0.0
**Source:** `AMOS_Legal_Kernel_v0.json`

The **Legal Engine Kernel** provides a clean, MECE structure for legal reasoning, without replacing qualified human counsel.

## Safety and Governance
- **No Jurisdiction Advice:** Do not simulate a law firm or claim to be a lawyer. Always require local counsel for high-risk topics.
- **No Hallucination:** Do not invent statutes, case law, or regulatory texts.

## Architecture
The kernel models matters as a tensor across 7 layers (doctrine, facts, risk, governance, docs, negotiation, enforcement).

### The 24 Dimensions
Key variables that shape the legal strategy:
- `D01`: Matter Type (transactional, contentious, regulatory)
- `D02`: Jurisdiction Scope (local to global)
- `D06`: Financial Materiality
- `D11`: Evidence State (incomplete to forensic)
- `D12`: Counterparty Profile (cooperative to aggressive)
- `D19`: Evidence Risk Tolerance

### Routing
The engine routes based on matter type to focus on specific clusters (e.g., contentious matters focus on Disputes & Litigation, International Arbitration, and prioritize the fact pattern and enforcement layers).

---
**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

---
**MOC:** [[11_KNOWLEDGE/engine/ENGINE_MOC|ENGINE_MOC]]

---
**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
