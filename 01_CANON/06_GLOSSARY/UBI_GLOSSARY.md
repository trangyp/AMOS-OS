---
title: UBI Glossary
type: glossary
source: 01_CANON/06_GLOSSARY
artifact: UBI_GLOSSARY.md
artifact_id: 01_canon_06_glossary_ubi_glossary
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 01_CANON
segment: 01_CANON/06_GLOSSARY
artifact_kind: GLOSSARY
path: 01_CANON/06_GLOSSARY/UBI_GLOSSARY.md
tags:
  - 06_glossary
  - amos-os
  - canon
  - canon/universe
  - canon_placeholder
  - glossary
  - rscf
  - universe
  - placeholder_expanded
  - routing-policy-validation-receipt
  - authz-engine-validation-receipt
  - law-hierarchy
version: 0.2.0
updated: '2026-08-27'
status: CANON_REFERENCE
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
implementation_status: NOT_ESTABLISHED
validation_status: NOT_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: ADD_ONLY
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: 01_CANON
  regime: canon_placeholder
  confidence_ceiling: source_supported
  provenance_independence: NOT_ESTABLISHED
---

## 0. Canonical Status

`UBI_GLOSSARY.md` is an **ADD-ONLY placeholder-expanded artifact** for the **01_CANON** plane segment.

It reserves the canonical slot for the AMOS framework family named **UBI Glossary**.

The artifact is presently:

```text
status: CANON_REFERENCE
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
implementation_status: NOT_ESTABLISHED
validation_status: NOT_ESTABLISHED
executable_binding: NOT_ESTABLISHED
```

This artifact MUST NOT be interpreted as establishing completed, validated, or enforced canon.

## 1. Governing Integrity Boundary

The following distinctions are mandatory:

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

No downstream layer may silently collapse these distinctions.

Origin architect / steward: **Trang Phan**

System: **AMOS OS**

______________________________________________________________________

# UBI Glossary

## 0. Status

`UBI_GLOSSARY.md` is an **ADD-ONLY placeholder** for the **Canon** plane segment at `01_CANON/06_GLOSSARY`.

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

This artifact reserves the **UBI Glossary** slot within the Canon plane. The Canon plane governs canonical laws, universe/cognition/infrastructure canons, variable registry, glossary, provenance lineage, and supersession.

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

## UBI Glossary — Source-Grounded Terms

> **Provenance:** Terms below are extracted from verified Knowledge Plane artifacts: [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_FRAMEWORK|UBI_FRAMEWORK]], [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE|UBI_SCORE]], [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE_FRAMEWORK|UBI_SCORE_FRAMEWORK]], [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_MASTER|UBI_MASTER]], [[11_KNOWLEDGE/05_FRAMEWORKS/UNIFIED_BIOLOGICAL_INTELLIGENCE|UNIFIED_BIOLOGICAL_INTELLIGENCE]], and the domain docs `11_KNOWLEDGE/06_DOMAIN_KNOWLEDGE/UBI_{NEUROBIOLOGICAL,NEUROEMOTIONAL,SOMATIC,BIOELECTROMAGNETIC}_INTELLIGENCE.md`.
> **Claim class:** `AMOS_MODEL` — these are AMOS model terms, not empirical/biological claims.

## Core terms

| Term | Definition (source-grounded) |
| :--- | :--- |
| **UBI — Unified Biological Intelligence** | AMOS framework establishing intelligence as a physical and biological living system governed by four irreducible, non-compensatory domains: NBI, NEI, SI, BEI. |
| **NBI — Neurobiological Intelligence** | Domain grounded in cortical processing / CNS; governs thought, perception, pattern recognition; influences reasoning, decision loops, memory. |
| **NEI — Neuroemotional Intelligence** | Domain grounded in limbic pathways and vagal tone; governs autonomic & emotional regulation; influences stress resistance, empathy, interpersonal accuracy. |
| **SI — Somatic Intelligence** | Domain grounded in fascial tensegrity and biomechanics; governs proprioception and embodied stability; influences physical action, coordination, resilience. |
| **BEI — Bioelectromagnetic Intelligence** | Domain grounded in cardiac rhythms and neural fields; governs oscillatory synchrony and EM timing; influences systemic coherence, phase locking, timing. |
| **Non-compensatory domains** | The four UBI domains are irreducible: no domain may substitute for another's deficit. |
| **UBI Score ($i$)** | $i_{\text{UBI}} = (\text{NBI} \cdot \text{NEI} \cdot \text{SI} \cdot \text{BEI})^{1/4} \in [0,1]$ — geometric-mean alignment metric. |
| **Strict geometric multiplicity** | If any single domain drops to zero, total UBI Score collapses to zero ($\min = 0 \implies i = 0$). |
| **Emergence factor ($e$)** | $e = i^2$ — systemic creative throughput and stress resilience grow non-linearly with balanced alignment (quadratic emergence). |
| **Proof of biological aliveness** | Multi-domain synchrony (e.g. ECG-EEG coherence + natural micro-tremor) used in `UBI_ID_EXCHANGE_BINDING` to evidence living human presence. |
| **ConsentX binding** | `UBI_CONSENTX_BINDING` binds continuous autonomic, somatic, and bioelectromagnetic signals into consent arbitration rooted in autonomic alignment. |
| **Entropy correction / homeostatic recovery** | `UBI_ENTROPY_CORRECTION` / `UBI_FRACTAL_ARCHITECTURE` mechanisms preserving $e = i^2$ via entropy dissipation and homeostatic recovery. |
| **Cross-species functional modes** | `UBI_CROSS_SPECIES_FUNCTIONAL_MODES` specializations (cetacean acoustic coherence, avian geomagnetic synchrony, cephalopod distributed edge, insect swarm stigmergy). |
| **NeuroSyncAI binding** | `UBI_NEUROSYNCAI_BINDING` — dynamic pacing & token throttling preserving $e = i^2$ at the AI interface. |
| **Wearable telemetry** | `UBI_WEARABLE_FRAMEWORK` — continuous physiological telemetry interface feeding the UBI scoring protocols. |

## Related

- [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_FRAMEWORK|UBI_FRAMEWORK]] · [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_MASTER|UBI_MASTER]] · [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_SCORE_FRAMEWORK|UBI_SCORE_FRAMEWORK]] · [[11_KNOWLEDGE/05_FRAMEWORKS/AMOS_UBI_SUPER_ENGINE|AMOS_UBI_SUPER_ENGINE]] · [[25_COGNITIVE_MATRIX/AMOS_X_UBI|AMOS_X_UBI]]

RSCF-NODE

node_id: amos_01_canon_06_glossary_ubi_glossary

node_type: glossary

path: 01_CANON/06_GLOSSARY/UBI_GLOSSARY.md

claim_class: AMOS_MODEL

rscf_state: canon_reference

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/06_GLOSSARY/06_GLOSSARY_MOC|06_GLOSSARY_MOC]]
