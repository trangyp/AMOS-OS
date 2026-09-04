---
title: TSS/TPE Glossary
type: glossary
source: 01_CANON/06_GLOSSARY
artifact: TSS_TPE_GLOSSARY.md
artifact_id: amos_01_canon_06_glossary_tss_tpe_glossary
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 01_CANON
segment: 01_CANON/06_GLOSSARY
artifact_kind: GLOSSARY
path: 01_CANON/06_GLOSSARY/TSS_TPE_GLOSSARY.md
tags:
  - amos-os
  - canon
  - universe
  - glossary
  - canon_placeholder
  - rscf
  - canon/universe
  - routing-policy-validation-receipt
  - authz-engine-validation-receipt
  - law-hierarchy
version: 0.1.0
updated: '2026-08-27'
status: PLACEHOLDER
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
implementation_status: NOT_ESTABLISHED
validation_status: NOT_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: ADD_ONLY
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# TSS/TPE Glossary

## 0. Status

`TSS_TPE_GLOSSARY.md` is an **ADD-ONLY placeholder** for the **Canon** plane segment at `01_CANON/06_GLOSSARY`.

It marks a canonical slot reserved by the AMOS canon-ingestion manifest for the framework family named above. It is NOT populated canon, NOT validated, and NOT enforced.

The governing boundaries are:

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

DOCUMENTED != ENFORCED

MODEL != OBSERVATION

SOURCE_CLAIM != VERIFIED

CANON_CANDIDATE != CANONICAL

CANONICAL != EMPIRICAL_TRUTH

CAPABILITY != AUTHORITY

AUTHORIZATION != COMMIT

PROPOSAL != COMMIT

IMPLEMENTED != VALIDATED

LOGGED != APPROVED

UNKNOWN/GAP != PASS
```

Origin architect / steward:

**Trang Phan**

______________________________________________________________________

## 1. Purpose

This artifact reserves the **TSS/TPE Glossary** slot within the Canon plane. The Canon plane governs canonical laws, universe/cognition/infrastructure canons, variable registry, glossary, provenance lineage, and supersession.

Substantive content (canonical definitions, laws, registries, schemas, models, or bindings) is to be populated from verified native-canon sources under the AMOS_CANON_INGESTION_RULE. This placeholder does not, by its existence, establish canon, empirical validity, or runtime enforcement.

______________________________________________________________________

## 2. Non-Purpose

This placeholder MUST NOT be used to claim:

- universal laws of reality;
- scientific proof;
- biological truth;
- mathematical theoremhood;
- philosophical certainty;
- runtime enforcement that has not been implemented;
- final canonical status;
- authority merely from architectural importance;
- or successful validation merely because the slot is addressable.

______________________________________________________________________

## 3. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:
  existing_folder:
    preserve: true
  existing_file:
    preserve: true
    overwrite: false
  new_framework:
    action: ADD_FILE_TO_EXISTING_FOLDER
  master_source:
    action: NORMALIZE_TO_RSCF_FILE
  framework_existing_in_multiple_sources:
    action:
      - CREATE_ONE_CANONICAL_NODE
      - LINK_ALL_SOURCE_PROVENANCE
      - DO_NOT_CREATE_DUPLICATE_CANON
  historical_source:
    action:
      - LINK_TO_CANON
      - RECORD_LINEAGE
      - PRESERVE_HERITAGE
  external_research:
    action:
      - KEEP_OUT_OF_NATIVE_CANON
      - LINK_AS_EVIDENCE
  duplicate_filename:
    action:
      - COMPARE_CONTENT_AND_LINEAGE
      - DO_NOT_OVERWRITE
  uncertainty:
    action:
      - MARK_GAP_OR_COMPETING
      - NEVER_INVENT_CANON
```

______________________________________________________________________

## 4. Contract discipline

Typed artifacts · provenance stamped · epistemic class declared · confidence ceiling · fail-closed on UNKNOWN/GAP · receipts for consequential effects · rollback basin before mutation.

______________________________________________________________________

## 5. Gaps

Executable binding NOT_ESTABLISHED. Canonical status UNKNOWN/GAP. Substantive content pending native-canon source ingestion. Validation receipt required before promotion: [[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]] · [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]].

______________________________________________________________________

## 6. Worked semantics (target)

Given an operation touching `01_CANON · GLOSSARY` within the Canon plane:

1. **Admit** — resolve the artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
1. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.
1. **Check authority** — authority_ref must be epoch-valid; capability alone never authorizes.
1. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.
1. **Propose** — candidate state is non-authoritative until gates pass (`PROPOSAL ≠ COMMIT`).
1. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.

______________________________________________________________________

## 7. Promotion-gate checklist

- [ ] substantive content populated from verified native-canon source
- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

______________________________________________________________________

## 8. Cross-plane bindings (target)

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]|AMOS Core Laws · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________


---

# TSS / TPE Glossary — Source-Grounded Terms

> **Provenance:** [[11_KNOWLEDGE/05_FRAMEWORKS/TSS_META_LAWS|TSS_META_LAWS]], [[11_KNOWLEDGE/05_FRAMEWORKS/TSS_SEVEN_CYCLES|TSS_SEVEN_CYCLES]], [[11_KNOWLEDGE/05_FRAMEWORKS/TSS_TPE_INTEGRATION|TSS_TPE_INTEGRATION]], [[11_KNOWLEDGE/05_FRAMEWORKS/TSS_THE_TRANG_SYSTEM|TSS_THE_TRANG_SYSTEM]].
> **Claim class:** `AMOS_MODEL` — systems-dynamics model terms, not empirical law.

## TSS state variables

| Symbol | Term | Meaning |
| :--- | :--- | :--- |
| $\Omega$ | **Overload** | Accumulated coordination friction, regulatory bloat, and technical debt in a system. |
| $H$ | **Cohesion** | Internal human cohesion and shared foundational trust. |
| $F$ | **Fragmentation** | Degree of siloing, factional division, and trust decay ($F \to 1$ = fragmented). |
| $S$ | **Shock / Stress** | External shock magnitude; damage $\propto \Omega \cdot F$. |

## TSS Meta Laws

| Term | Statement |
| :--- | :--- |
| **Law of Inevitable Overload** | $\partial\Omega/\partial t > 0$ without active pruning — systems accumulate friction/debt unless energy is spent on structural simplification. |
| **Law of Non-Compensatory Cohesion** | $H \perp \text{Capital/Tools}$ — capital, compute, or infrastructure cannot substitute for catastrophic loss of cohesion/trust. |
| **Law of Scale Fragility** | $\text{Damage}(S) \propto \Omega \cdot F$ — shocks produce localized stress in cohesive systems, catastrophic cascades in fragmented high-load systems. |
| **Law of Conservation of Debt** | Deferred maintenance, suppressed conflict, and unmodeled risk compound non-linearly into future $P_{\text{collapse}}$. |

## Seven Evolutionary Cycles ($C_1 \dots C_7$)

| Cycle | Phase | Indicator |
| :--- | :--- | :--- |
| $C_1$ | Emergence | Birth; high $H$, low $\Omega$ |
| $C_2$ | Expansion | Growth, functional scaling, reserve accumulation |
| $C_3$ | Peak & Overreach | Maximum scale, hidden debt, efficiency obsession |
| $C_4$ | Fragmentation | Siloing, $F \uparrow$, trust decay $H \downarrow$ |
| $C_5$ | Crisis & Destabilization | Acute $S \uparrow$, rapid fragility unmasking |
| $C_6$ | Collapse & Dissolution | Structural disintegration, asset dispersal |
| $C_7$ | Reset & Reconstruction | Genesis re-anchoring, new charter |

## TPE — Trang Prediction Engine

TPE is the multi-horizon predictive foresight layer coupled to TSS (see [[11_KNOWLEDGE/05_FRAMEWORKS/TSS_TPE_INTEGRATION|TSS_TPE_INTEGRATION]] and [[11_KNOWLEDGE/trang/TPE_TRANG_PREDICTION_ENGINE|TPE_TRANG_PREDICTION_ENGINE]]): it projects cycle transitions and collapse-risk trajectories from the TSS state variables. Predictions remain `AMOS_MODEL` — foresight models, not verified forecasts.

## Related

- [[11_KNOWLEDGE/05_FRAMEWORKS/TSS_THE_TRANG_SYSTEM|TSS_THE_TRANG_SYSTEM]] · [[11_KNOWLEDGE/05_FRAMEWORKS/TSS_META_LAWS|TSS_META_LAWS]] · [[11_KNOWLEDGE/05_FRAMEWORKS/TSS_SEVEN_CYCLES|TSS_SEVEN_CYCLES]] · [[11_KNOWLEDGE/05_FRAMEWORKS/TSS_TPE_INTEGRATION|TSS_TPE_INTEGRATION]] · [[25_COGNITIVE_MATRIX/AMOS_X_TSS|AMOS_X_TSS]]

RSCF-NODE

node_id: amos_01_canon_06_glossary_tss_tpe_glossary

node_type: glossary

path: 01_CANON/06_GLOSSARY/TSS_TPE_GLOSSARY.md

claim_class: AMOS_MODEL

rscf_state: canon_reference

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/06_GLOSSARY/06_GLOSSARY_MOC|06_GLOSSARY_MOC]]
