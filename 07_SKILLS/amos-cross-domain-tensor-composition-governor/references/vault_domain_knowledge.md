---
title: vault domain knowledge
type: reference
source: 07_SKILLS/amos-cross-domain-tensor-composition-governor/references
tags: [reference, amos-cross-domain-tensor-composition-governor, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault Domain Knowledge — Cross-Domain Tensor Composition Governor

> **Source**: AMOS_OS Obsidian vault and Cosmo Brain vault (`_00_Cosmo brain/`)

## 1. Tensor Compatibility Invariant (TENSOR_CONTRACTS.md)

The canonical tensor contracts define 6 typed tensors:

- **T_R** (Universal reasoning): `T[claim, evidence_class, domain, HML_scale, time, regime, observer, provenance, confidence, consequence, governance]`
- **T_F** (Fractal): `T[object, HML_scale, recursion_depth, pattern_class, boundary, entropy_proxy, lacunarity_proxy, mutation_state, selection_state, time, regime, provenance]`
- **T_E** (Evidence): `T[evidence_id, source_id, source_type, ancestry, timestamp, version, scope, regime, measurement, quality, independence, revocation_state]`
- **T_C** (Claim): `T[claim_id, text, class, premises, evidence_refs, scope, regime, freshness, causal_level, competing_set, falsifiers, confidence_ceiling]`
- **T_G** (Governance): `T[action, capability, authority, consequence_radius, reversibility, approval, rollback, evidence_threshold, mutation_class]`
- **T_M** (Memory): `T[item_id, content_class, state, provenance, dependencies, freshness, contradiction_state, retention_class, revalidation_epoch]`

**Critical invariant**: "Tensor composition is prohibited until shared axes are semantically compatible. Same-name axes do not prove same meaning."

## 2. Fractal Tensor Architecture (Cosmo brain: fractal/FRACTAL.md)

The fractal tensor `T_F` is the primary cross-scale composition mechanism:

`F = T[object, HML_scale, recursion_depth, pattern_class, boundary, entropy_proxy, lacunarity_proxy, mutation_state, selection_state, time, regime, provenance]`

### H/M/L Decomposition

- **H** = governing objective, law, macro field, long horizon
- **M** = subsystem, mediator, architecture, translation layer
- **L** = local evidence, code line, event, operation, token-level detail

Default retrieval: `bootstrap capsule -> H -> M -> L -> raw evidence only if required`

### Cross-Scale Rule

A projection from L→M or M→H is admissible only if identity, provenance, scope, regime, and declared invariants survive.

### Recursion Rule

`X_(k+1) = G(X_k, constraints, feedback, mutation)`

This remains AMOS_MODEL unless independently grounded in established mathematics for the domain.

### Anti-Overreach (from FRACTAL.md)

- repeated pattern != proven fractal dimension
- H/M/L similarity != identical mechanism
- entropy proxy != thermodynamic entropy
- lacunarity proxy != mathematical lacunarity unless defined as such
- cross-scale analogy != causation

### Compression

At each scale retain only information capable of changing:

- the conclusion
- the action
- the confidence ceiling
- the falsifier set
- the dependency graph

## 3. Domain Axis Semantic Differences

Each AMOS domain (C01-C12) interprets shared axes differently:

| Axis | C01 Meta-Logic | C02 Math | C03 Physics | C04 Bio-Neuro | C05 Mind | C06 Society | C07 Econ | C08 Strategy | C09 Org-Law | C10 Tech | C11 Design | C12 Earth-Eco |
|------|----------------|----------|-------------|---------------|----------|-------------|----------|--------------|-------------|----------|------------|---------------|
| scope | logical argument | problem domain | physical system | biological system | psychological context | social system | market/economy | game/strategic | organization/jurisdiction | technical system | design artifact | earth-system |
| regime | reasoning mode | numerical regime | physical regime | physiological state | emotional/cognitive state | social/political regime | market regime | game/information regime | regulatory regime | operational regime | aesthetic register | climate/ecological regime |
| time | logical time | computational time | physical time | biological timescale | psychological time | historical/social time | economic time | strategic time | legal/policy time | system uptime | design lifecycle | geological time |
| causal_level | inference depth | mathematical proof | physical mechanism | biological mechanism | psychological mechanism | social mechanism | economic mechanism | strategic mechanism | legal mechanism | technical mechanism | design rationale | earth-system mechanism |

## 4. Fractal Architecture Sources (Cosmo brain: fractal/)

The Cosmo brain `fractal/` directory contains 42 files including:

- `FRACTAL.md` — Core fractal reasoning with H/M/L decomposition and tensor definition
- `FRACTAL_RUNTIME.md` — Runtime execution of fractal decomposition
- `AMOS Math Core — Fractal Mathematics & Cognitive Architecture Runtime.md` — Math core
- `AMOS_FRACTAL_CONSCIOUSNESS_WHITEPAPER_FULL_FIXED.md` — Consciousness fractal model
- `Fractal Semantic Intelligence Architecture (FSIA).md` — Semantic intelligence
- `HERITAGE ∅ – 12 LOẠI FRACTAL.md` — 12 fractal types (Vietnamese heritage)
- `HERITAGE ∅ – ANCIENT FRACTAL MATHEMATICS.md` — Ancient fractal math
- `FRACTAL ECONOMY.md` — Fractal economics application
- `FRACTAL FOREX ENTERPRISE.md` — Fractal forex application

These sources confirm that fractal tensors are the primary cross-domain composition mechanism, but all mappings remain AMOS_MODEL unless independently grounded.

## 5. Claim Classes Per Domain

All 12 domains share the same claim class taxonomy but apply it domain-specifically:

- VERIFIED, DERIVED, MODEL, CONDITIONAL, COMPETING, UNKNOWN/GAP

Evidence classes differ per domain (e.g., C03 has OBSERVATION/EXPERIMENT, C04 has CLINICAL/PHYSIOLOGICAL_MEASURE, C06 has SURVEY/ETHNOGRAPHY/HISTORICAL_RECORD).

## 6. Weakest Load-Bearing Edge Rule

Cited in C06, C07, C12 master knowledge:

- C06: "Trust ↔ institutions causal direction runs both ways and remains unresolved at macro level"
- C07: "final outcome confidence cannot exceed the weakest load-bearing edge"
- C12: "each edge can be modified by technology, trade, policy, inequality... final outcome confidence cannot exceed the weakest load-bearing edge"

Canonical ceiling: `CONFIDENCE(C) <= MIN(CONFIDENCE(LOAD-BEARING PREMISES))` subject to independent revalidation.

## 7. Cross-Domain Gaps Identified

From skill survey (714+ skills): only 3 explicit cross-domain skills in formal domain:

- amos-cross-architecture-tensor-engine
- amos-cross-scale-rscf-tensor-engine
- amos-cross-species-cognition-mapper (C04 bio domain)

From _00_Cosmo brain exploration: 8 cross-domain integration gaps (all now covered by governor skills).

## 8. Anti-Overclaim Boundaries Per Domain

Each domain has explicit anti-overclaim firewalls that must be preserved across boundaries:

- C03: "AMOS/Trang boundary-locking proposal is MODEL, not established quantum mechanics"
- C04: "quantum effects in brain, quantum consciousness are CONTESTED or MODEL"
- C05: "All substantive psychological claims are MODEL unless explicitly sourced"
- C06: "Vietnamese cultural ritual energy equations are MODEL/structural metaphor, NOT physically measurable"
- C08: "Analogy ≠ isomorphism: board mappings organize hypotheses; domain evidence decides them"
- C11: "Aesthetic judgments are VALUES, not FACTS"
- C12: "A project is not ecologically beneficial merely because it contains vegetation (greenwashing firewall)"

## 9. Relation Tensor (RELATION_TENSOR.md)

The relation tensor R_ij represents typed relations between AMOS objects:

`R_ij = T[type, direction, strength, dependency, confidence, causal_pressure, trust, conflict, lag, entropy, repair_coupling, mutation_transfer, observer_variance, provenance]`

This is the structural basis for cross-domain bridge classification.

## 10. Full Brain OS Architecture (AMOS_Full_Brain_OS_Architecture.md)

The UBCAR architecture requires cross-domain integration:

- O2 Routing: 3-tier routing across C01-C12 domain engines (ExpressionGateway → KernelRouter → Domain Engines)
- 36 epistemic boundaries (anti-overclaim, consolidated)
- Core equation: `S_{t+1} = C(F(S_t, U_t))` where F includes domain engine routing
- "Dynamic routing → activate MINIMUM relevant region, then integrate"
- 102 distinct decision gates (deduplicated, each with one home layer)

The Cross-Domain Tensor Composition Governor provides the governance layer for this integration.

## 11. Cognitive Domain Engines (Cosmo brain: cognitive/AMOS Cognitive Domain Engines.md)

13 Cognitive Stack Engines provide the domain-specific reasoning:

- AMOS_Deterministic_Logic_And_Law_Engine — Unified kernel for deterministic reasoning
- AMOS_Signal_Processing_Engine — Signal processing for noise filtering
- AMOS_Strategy_Game_Engine — Game-theoretic planning
- AMOS_Econ_Finance_Engine — Micro, macro, trade, public finance
- AMOS_Physics_Cosmos_Engine — Classical, quantum, statistical, cosmological
- AMOS_Society_Culture_Engine — Institutions, norms, demographics
- AMOS_Biology_And_Cognition_Engine — Biological cognition
- AMOS_Design_Language_Engine — Cross-modal design + linguistic

15 Domain Engines provide specialized reasoning across Tech_Systems, Science_Health, Org_Risk_Policy, and Quantum subsystems.

Each engine produces typed tensors that must pass compatibility validation before cross-domain composition.

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
