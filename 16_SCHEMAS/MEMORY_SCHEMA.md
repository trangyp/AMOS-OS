---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Memory Schema
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

# Memory Schema

## 0. Status

`MEMORY_SCHEMA.md` is a **typed schema specification** for AMOS memory records under `10_MEMORY`. It is an `AMOS_MODEL` specification: NOT executed, NOT validated, NOT enforced as a validator. Implementation/validation `NOT_ESTABLISHED` / `PARTIAL`.

Governing boundaries preserved:

```text
MEMORY != KNOWLEDGE
MEMORY != STATE
REMEMBERED_PREFERENCE != PERMISSION
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

---

## 1. Purpose

A memory record captures a stored, retrievable trace of the system — events, episodes, cases, semantic associations, or preferences. `MEMORY_SCHEMA.md` types every field so memory can be encoded, consolidated, retained, retrieved, invalidated, superseded, and forgotten without collapsing memory into knowledge or into runtime state.

---

## 2. The `Memory != Knowledge != State` boundary

| concept | role |
| :--- | :--- |
| **Memory** | Stored, retrievable trace (what was experienced / stored) |
| **Knowledge** | Validated, governed claims (what is justified) |
| **State** | Current authoritative system condition (what is true now) |

- A memory may exist without being validated knowledge; memory informs proposal, it does not establish truth.
- Memory may influence personalization but cannot silently authorize consequential action (`RememberedPreference != Permission`).
- Memory is not runtime state: a memory is a historical trace; state is the authoritative current fact, and stale memory must never drive a final commit.

---

## 3. Memory record schema

| name | type | required | description | constraints |
| :--- | :--- | :--- | :--- | :--- |
| `memory_id` | string | true | Stable identifier for the memory | regex `^MEM-[0-9]{4}-[0-9]+$` |
| `class` | string | true | Memory family | see §4 |
| `encoding` | object | true | How the memory is represented / serialized | see §5 |
| `consolidation_state` | string | true | Consolidation lifecycle state | see §6 |
| `retention_curve` | object | true | Biologically/physics-grounded retention parameters | see §7 |
| `retrieval` | object | true | Retrieval policy and activation | see §8 |
| `invalidation` | object | true | Conditions that invalidate the memory | see §9 |
| `supersession` | object | false | Which memory(ies) this supersedes | see §10 |
| `forgetting` | object | false | Forgetting / eviction metadata | see §11 |
| `provenance` | object | true | Source and lineage of the record | see §12 |

---

## 4. Memory classes (enum)

| class | meaning |
| :--- | :--- |
| `working` | Short-lived active context (ring buffer, session-scoped) |
| `episodic` | Causal event traces with timestamps |
| `case` | Stored case/instance for reuse |
| `long-term` | Persistent semantic / associative graph |
| `negative` | Stored record of what not to do / non-examples |
| `authority-sensitive` | Memory touching permissions or classified content |

---

## 5. Encoding

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `representation` | string | true | Serialization form (e.g. `structured_trace`, `vector`, `graph`) |
| `schema_ref` | string | false | Schema that governs this memory's shape |
| `hash` | string | false | Content hash for integrity checks |
| `tier` | string | true | Storage tier (e.g. `tier0_working` … `tier3_procedural`) |

---

## 6. Consolidation state

| state | meaning |
| :--- | :--- |
| `ENCODED` | Admitted into memory |
| `CONSOLIDATING` | Undergoing re-processing / pattern abstraction |
| `CONSOLIDATED` | Stable, retrievable |
| `QUARANTINED` | Flagged pending re-evaluation |
| `EXPIRED` | Retained as tombstone only |
| `FORGOTTEN` | Evicted / no longer retrievable |

---

## 7. Retention curve

Retention probability follows the generalized decay:

$$R(t) = \exp\left( -\frac{t}{S(m)} \right)$$

with stability

$$S(m) = S_0 \cdot (1 + \alpha \cdot \text{Salience}(m))^{\beta \cdot \text{Rehearsals}(m)}$$

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `baseline_stability` | number | true | $S_0$ — default half-life |
| `salience_weight` | number | true | $\alpha$ — epistemic importance weight |
| `rehearsal_multiplier` | number | true | $\beta$ — retrieval strengthening |
| `salience` | number | false | $\text{Salience} \in [0,1]$ |
| `rehearsals` | integer | false | Count of successful retrievals |

---

## 8. Retrieval

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `retrieval_key` | string | true | Primary retrieval key |
| `activation_level` | number | true | Current activation $A(m)$ |
| `access_count` | integer | false | Number of retrievals |
| `last_accessed` | string | false | Last access timestamp |
| `relevance_required` | boolean | true | Whether relevance gate must pass before use |

---

## 9. Invalidation

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `invalidated` | boolean | true | Whether the memory is currently valid |
| `reason` | string | false | Why it was invalidated |
| `invalidate_descendants_only` | boolean | true | Selective (non-global) invalidation |

Failure invalidates dependent descendants only; unrelated memory is preserved.

---

## 10. Supersession

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `superseded_by` | string | false | memory_id that replaces this one |
| `supersedes` | array | false | memory_ids this replaces |
| `retain_ancestry` | boolean | true | Whether lineage is preserved after supersession |

---

## 11. Forgetting

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `forgetting_curve` | string | true | Model governing decay |
| `eviction_policy` | string | false | How eviction selects entries (e.g. lowest activation) |
| `tombstone_retained` | boolean | true | Whether a tombstone remains after forgetting |

Eviction selects the lowest activation: $\text{Evict}(t) = \arg\min_{i \in \text{Buffer}} A_i(t)$.

---

## 12. Provenance

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `source` | string | true | Where the memory came from |
| `timestamp` | string | true | When it was encoded |
| `causal_epoch` | integer | false | Causal epoch at encoding |
| `parent_ids` | array | false | Memory/state it derives from |

---

## 13. Memory-action firewall

```text
Memory may inform proposal.
Memory must not silently authorize irreversible action.
Stale memory must not drive a final commit.
```

The `authority-sensitive` class requires explicit access-control handling and carries the strongest provenance/classification obligations.

---

## 14. Status / gaps

- Implementation status: `NOT_ESTABLISHED` — no memory validator exists.
- Validation status: `NOT_ESTABLISHED` — no executed receipt for this schema.
- Retention-curve parameters and consolidation engine are specified as `AMOS_MODEL`; executed behavior is `UNKNOWN/GAP` unless separately evidenced.

---

## 15. Cross-plane bindings

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]]
- Memory layer — [[10_MEMORY/EPISODIC_MEMORY_SUBSTRATE|EPISODIC_MEMORY_SUBSTRATE]] · [[10_MEMORY/TIERED_MEMORY_LIFECYCLE_ARCHITECTURE|TIERED_MEMORY_LIFECYCLE_ARCHITECTURE]]
- State layer — [[12_STATE/12_STATE_MOC|12_STATE_MOC]] (Memory ≠ State)
- Knowledge contrast — [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] (Memory ≠ Knowledge)
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority

---

```RSCF-NODE
node_id: amos_16_schemas_memory_schema
node_type: schema
path: 16_SCHEMAS/MEMORY_SCHEMA.md
claim_class: AMOS_MODEL
rscf_state: derived
canonical_status: UNKNOWN/GAP
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
  - GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
  - GROUNDS: [[10_MEMORY/EPISODIC_MEMORY_SUBSTRATE|EPISODIC_MEMORY_SUBSTRATE]]
```
