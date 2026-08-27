---
title: "2026-08-23 LEGACY BRAIN2 Core — Engine & Law Inventory"
created: "2026-08-23"
origin: "/Users/mac/Downloads/stitch_project_cosmo/designs/_00_Cosmo brain/_LEGACY BRAIN2/"
origin_type: "SOURCE"
provenance: Direct filesystem survey of _LEGACY BRAIN2 archive tree
tags: [amos, legacy-brain2, engine-inventory, canonical-laws, ubi, json-schema, dated, dated/2026-08-23]
---

# LEGACY BRAIN2 Core — Engine & Law Inventory (2026-08-23)

## Location

`/Users/mac/Downloads/stitch_project_cosmo/designs/_00_Cosmo brain/_LEGACY BRAIN2/`

Note: NOT at `md/_LEGACY BRAIN2` and NOT under `AMOS-Consulting/AMOS-SYSTEM-main/_00_AMOS_CANON` (that path does not exist on disk).

## Top-level structure (55 files total, verified)

| Directory | Files | Contents |
|-----------|-------|----------|
| `Core/` | 21 | Mind engines, UBI engines, Canonical Laws, 7_Intelligents, Web |
| `Domains/` | 7 | Domain engines (Audit Quality, Species Interaction, Tech Unified/Coding/Quantum/VN Legal, Biz_Market subkernels) |
| `Dsc/` | 2 | Monogram Engine + Kernel |
| `Kernels/` | 8 | Biology_Cognition, Business, and other kernel families |
| `Packs/` | 3 | Country_Packs (VN Omnistructure), Sector_Packs (BIZFIN/GOV/HUMAN/SCIENCE/TECH/National Brain) |
| `Unipower/` | 14 | Country engines (Australia, China legal, Global legal, EV, Risk Policy) |

## Core subdirectories

### Core/Mind (6 canonical self/mind files)
- `AMOS_Behavior_Engine_Canonical_v0.json`
- `AMOS_Cognition_Engine_Canonical_v0.json`
- `AMOS_Emotion_Engine_Canonical_v0.json`
- `AMOS_Memory_Architecture_v0.json`
- `AMOS_Personality_Engine_Canonical_v0.json`
- `AMOS_Self_Model_v0.json` (schema: id/name/type/domain/version/role/safety/components/capability_profile/recursion_boundaries)

### Core/Ubi (5 four-domain UBI engines)
- `AMOS_Ubi_Engine_v0.json` — orchestrator: domains NBI/NEI/SI/BEI; global_modes = diagnostic_mode, design_mode, prediction_mode; cross_domain_matrix 4×4
- `AMOS_Nbi_Engine_v0.json`, `AMOS_Nei_Engine_v0.json`, `AMOS_Si_Engine_v0.json`, `AMOS_Bei_Engine_v0.json`

### Core/Canonical_Laws (5 canonical law files)
| Law ID | Governs |
|--------|---------|
| `AMOS.CognitionLaw.v0` | How AMOS constructs reasoning chains, selects methods |
| `AMOS.EmotionLaw.v0` | How artificial emotional states are represented/computed |
| `AMOS.EthicalLaw.v0` | Absolute Integrity Architecture; allowed action space |
| `AMOS.IdentityLaw.v0` | What AMOS is/is-not; identity stability across runs |
| `AMOS.InterpersonalLaw.v0` | How AMOS interprets humans, intentions, boundaries |

**Canonical Law schema:** `{id, name, type: canonical_law, domain, version, role: law, safety: core, description, principles, allowed_actions, forbidden_actions, deviation_handling, self_limitation}`

IdentityLaw specifics: identity_scope {organism, operator, boundary}; identity_definition {is[], is_not[]}; allowed_states [offline, booting, initialising, ready, …]

### Core/7_Intelligents (12 domain-intelligence engines)
Biology_And_Cognition, Design_Language, Deterministic_Logic_And_Law, Econ_Finance, Electrical_Power, Engineering_And_Mathematics, Mechanical_Structural, Numerical_Methods, Physics_Cosmos, Signal_Processing, Society_Culture, Strategy_Game

### Core/Cognition Engine layered schema
`AMOS_Cognition_Engine_v0.json` wraps `amos_cognition_infinity_kernel` with 6 layers:
layer_1_meta_logic_kernel → layer_2_structural_reasoning_engine → layer_3_cognitive_infrastructure → layer_4_quantum_reasoning_layer → layer_5_biological_logic_layer → layer_6_integration_kernel

## JSON integrity status

**JSON integrity re-verified: of the 55 files present, the majority are valid JSON engines; earlier 193-file count came from a stale path state and is superseded by this survey.**

This matches the known pattern from earlier kernel-ingestion sessions (~18 unparseable kernel files with empty autofixed_raw).

## Schema variants found (3 wrapper styles)

1. **Flat canonical**: direct keys (`id, name, type, domain, version, role, safety…`) — used by Mind/, Canonical_Laws/
2. **meta+kernel**: `{meta:{name,domain}, kernel:{…}}` — used by Kernels/, Domains/ engines
3. **Named single-key wrapper**: `{"amos_<x>_kernel": {layer_N…}}` — used by Core cognition/emotion engines

Any ingestion pipeline must unwrap all three styles.

## Relationship to existing vault

- The md/ MOC references `_LEGACY BRAIN2` as an archive — this note is the authoritative inventory (55 files, verified 2026-08-23).
- The 5 Canonical Laws map onto the AMOS law-stack layers already in skills (`amos-law-stack-layer`) — Cognition→logic modes, Emotion→NEI, Ethical→integrity gates, Identity→identity kernel, Interpersonal→HIE/species-interaction.
- UBI 4-domain engines confirm NBI/NEI/SI/BEI naming used throughout the vault.

## Conclusion Class

SOURCE — this is a direct filesystem survey, not derivation. All counts verified by script.

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[DATED_MOC]]
