---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Knowledge Schema
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Knowledge Schema

## 0. Status

`KNOWLEDGE_SCHEMA.md` is a **typed schema specification** for AMOS knowledge claims under `11_KNOWLEDGE`. It is an `AMOS_MODEL` specification: NOT executed, NOT validated, NOT enforced as a validator. Implementation/validation `NOT_ESTABLISHED` / `PARTIAL`.

Governing boundaries preserved:

```text
SOURCE_CLAIM != VERIFIED
TEST_SPECIFIED != TEST_EXECUTED
CAPABILITY != AUTHORITY
KNOWLEDGE != STATE
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

---

## 1. Purpose

A knowledge claim is a typed proposition admitted into the AMOS knowledge layer with explicit epistemic class, provenance, scope, regime, freshness, dependencies, and confidence ceiling. `KNOWLEDGE_SCHEMA.md` types every field so claims can be admitted, promoted, compared, invalidated, and audited without conflating documentation with implementation or memory with knowledge.

---

## 2. Governing rules

- No claim outranks its weakest load-bearing premise (`confidence ceiling ≤ 0.95`).
- Knowledge is validated by evidence, not by repetition; `Repetition != IndependentConfirmation`.
- Scope and regime are declared on every claim; cross-regime transfer requires an explicit bridge.
- Unknown values are `UNKNOWN/GAP`, never invented.
- Falsifiers stay visible; competing claims are preserved until evidence discriminates.

---

## 3. Knowledge claim schema

| name | type | required | description | constraints |
| :--- | :--- | :--- | :--- | :--- |
| `claim_id` | string | true | Stable identifier for the claim | regex `^KN-[0-9]{4}-[0-9]+$` |
| `claim` | string | true | The proposition asserted | non-empty |
| `claim_class` | string | true | Epistemic class of the claim | see §4 |
| `source` | string | true | Origin reference of the claim | non-empty |
| `provenance` | object | true | Source, version, hash, ancestry | see §5 |
| `scope` | string | true | Domain/regime applicability | non-empty |
| `regime` | string | true | Regime under which the claim holds | non-empty |
| `freshness` | object | true | Temporal validity of the claim | see §6 |
| `dependencies` | array | false | Premises the claim depends on | each is a claim_id or law |
| `competing_claims` | array | false | Claims that compete with this one | preserved until discrimination |
| `falsifiers` | array | true | Conditions that would falsify the claim | non-empty |
| `confidence_ceiling` | number | true | Upper bound on confidence | $0 \le c \le 0.95$ |
| `validation_state` | string | true | Current validation state | see §8 |

---

## 4. Claim classes (enum)

| class | meaning |
| :--- | :--- |
| `SOURCE_CLAIM` | Asserted by a source, not yet verified independently |
| `OBSERVATION` | Directly observed / tool-obtained evidence |
| `DERIVED` | Concluded from premises through valid inference |
| `MODEL` | A governing model or abstraction, not empirical truth |
| `DECISION` | A governed choice, not a factual assertion |
| `COMPETING` | A hypothesis held in tension with others |
| `UNKNOWN_GAP` | A recognized absence, not a positive claim |

---

## 5. Provenance

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `source_id` | string | true | Source artifact reference |
| `source_version` | string | true | Version of the source |
| `source_hash` | string | false | Content hash of the source |
| `parent_ids` | array | false | Parent claims this derives from |
| `transformation` | string | false | How this was derived from parents |
| `timestamp` | string | true | Admission timestamp |
| `trust_scope` | string | true | Bounds of trust placed in the source |

---

## 6. Freshness

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `admitted_at` | string | true | When the claim was admitted |
| `valid_until` | string | false | When the claim expires (null = no expiry) |
| `refreshed_at` | string | false | Last successful refresh |
| `stale` | boolean | true | Whether the claim is currently fresh |

A claim is stale when $\Delta t > \theta_{\text{fresh}}$ where $\Delta t$ is elapsed time since admission/refresh and $\theta_{\text{fresh}}$ is the regime-assigned freshness horizon.

---

## 7. Dependencies & confidence ceiling

If a claim $C$ depends on premises $P_1, \dots, P_n$, then:

$$\text{Conf}(C) \le \min_{i} \text{Conf}(P_i)$$

unless $C$ is independently validated. This ceiling is hard and not compensable by combinatorial evidence alone.

---

## 8. Validation state (promotion pipeline)

```
RAW
  ↓ admit
SOURCE_CLAIM
  ↓ verify / observe
OBSERVATION / DERIVED
  ↓ evidence + constraint checks
VALIDATED_KNOWLEDGE
```

| state | meaning |
| :--- | :--- |
| `RAW` | Unprocessed input, not yet admitted |
| `SOURCE_CLAIM` | Admitted source assertion, unverified |
| `OBSERVATION` | Verified by direct/tool observation |
| `DERIVED` | Derived from valid premises |
| `COMPETING` | Held as a live alternative |
| `VALIDATED_KNOWLEDGE` | Passed evidence + constraint checks |
| `QUARANTINED` | Flagged pending re-evaluation |
| `RETRACTED` | Withdrawn / falsified |

Promotion to `VALIDATED_KNOWLEDGE` requires: scope and regime valid, dependencies satisfiable, freshness current, no unsatisfied falsifier, authority for the promotion valid at commit time.

---

## 9. Falsifiers

Every claim carries explicit falsifiers. A satisfied falsifier forces `QUARANTINED` or `RETRACTED` and selective invalidation of dependent descendants only — never of unrelated state.

---

## 10. Status / gaps

- Implementation status: `NOT_ESTABLISHED` — no knowledge-claim validator exists.
- Validation status: `NOT_ESTABLISHED` — no executed receipt for this schema.
- The full promotion pipeline is specified here as `AMOS_MODEL`; executed promotion is `UNKNOWN/GAP` unless separately evidenced.

---

## 11. Cross-plane bindings

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]]
- Knowledge layer — [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[11_KNOWLEDGE/engine/CONSTRAINT_ENGINE|CONSTRAINT_ENGINE]]
- Claims registry — [[11_KNOWLEDGE/02_CLAIMS/02_CLAIMS_MOC|02_CLAIMS_MOC]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]

---

```RSCF-NODE
node_id: amos_16_schemas_knowledge_schema
node_type: schema
path: 16_SCHEMAS/KNOWLEDGE_SCHEMA.md
claim_class: AMOS_MODEL
rscf_state: derived
canonical_status: UNKNOWN/GAP
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
  - GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
  - GROUNDS: [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]]
```
