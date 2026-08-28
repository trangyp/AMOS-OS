---
title: TSS Meta Laws
type: trang-framework
source: 11_KNOWLEDGE/05_FRAMEWORKS
artifact: TSS_META_LAWS.md
artifact_id: amos_11_knowledge_05_frameworks_tss_meta_laws
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 11_KNOWLEDGE
segment: 11_KNOWLEDGE/05_FRAMEWORKS
artifact_kind: FRAMEWORK
path: 11_KNOWLEDGE/05_FRAMEWORKS/TSS_META_LAWS.md
tags:
  - amos_os
  - knowledge
  - vault
  - 11_knowledge
  - 05_frameworks
  - tss
  - meta_laws
  - non_compensatory
  - conservation_of_debt
  - scale_fragility
  - rscf
  - canon_candidate
  - canon/knowledge
version: 1.0.0
updated: '2026-08-27'
status: ACTIVE_REFERENCE
epistemic_class: AMOS_MODEL
canonical_status: SOURCE_GROUNDED_CANON_CANDIDATE
implementation_status: CONCEPTUAL_SOURCE_DEFINED
validation_status: NOT_INDEPENDENTLY_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: NATIVE_CANON_INGESTION
raw_source_policy: DO_NOT_LOAD_UNLESS_REQUIRED
rscf:
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance:
    - THE_TRANG_SYSTEM_CODEX_META_LAWS
    - TSS_THE_TRANG_SYSTEM_OFFICIAL_MANUAL
    - AMOS_CORPUS
  scope:
    - KNOWLEDGE_FRAMEWORKS
    - STRUCTURAL_LAWS
    - SOURCE_DEFINED_MODEL
framework_binding:
  parent_framework:
    name: The Trang System™
    acronym: TSS
    artifact: [[TSS_THE_TRANG_SYSTEM]]
  cognitive_matrix_binding:
    artifact: [[AMOS_X_TSS]]
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  framework_structure: VERIFIED_SOURCE_STRUCTURE
  law_statements: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---


# TSS Meta Laws

`TSS_META_LAWS.md` is the canonical Knowledge Plane reference artifact codifying the **Fundamental Meta Laws** governing systems dynamics in The Trang System™ within `11_KNOWLEDGE/05_FRAMEWORKS`.

---

# 1. The Core Meta Laws of The Trang System™

1. **Law of Inevitable Overload ($\frac{\partial \Omega}{\partial t} > 0$ without Active Pruning):**
   * Complex systems inherently accumulate coordination friction, regulatory bloat, and technical debt unless energetic resources are continually expended on structural simplification.

2. **Law of Non-Compensatory Cohesion ($H \perp \text{Capital/Tools}$):**
   * Financial capital, computational scale, or physical infrastructure cannot substitute for a catastrophic loss of internal human cohesion ($H$) and shared foundational trust.

3. **Law of Scale Fragility (Complexity Multiplies Shock):**
   $$\text{Damage}(S) \propto \Omega \cdot F$$
   * External shocks ($S$) produce localized stress in cohesive systems ($F \to 0$), but catastrophic systemic cascades in fragmented, high-load systems ($F \to 1, \Omega \to 1$).

4. **Law of Conservation of Debt:**
   * Deferred structural maintenance, suppressed conflicts, and unmodeled risks never dissipate; they compound non-linearly into future collapse probabilities ($P_{\text{collapse}}$).

---

# 2. Inter-Plane & Vault Connections

- **Master Framework:** [[TSS_THE_TRANG_SYSTEM]]
- **Seven Cycles:** [[TSS_SEVEN_CYCLES]]
- **Foresight Integration:** [[TSS_TPE_INTEGRATION]]
- **Native Codex:** `11_KNOWLEDGE/trang/THE_TRANG_SYSTEM_CODEX_META_LAWS`

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_11_knowledge_05_frameworks_tss_meta_laws
  node_type: framework
  claim_class: AMOS_MODEL
  state: SOURCE_CLAIM
  H:
    identity: "TSS Meta Laws"
    role: "Fundamental structural meta laws governing systems stability, complexity, and debt"
  M:
    laws: [inevitable_overload, non_compensatory_cohesion, scale_fragility, conservation_of_debt]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[05_FRAMEWORKS_MOC]] · [[TSS_THE_TRANG_SYSTEM]] · [[TSS_SEVEN_CYCLES]] · [[AMOS_X_TSS]]

---
**MOC:** [[05_FRAMEWORKS_MOC]]
