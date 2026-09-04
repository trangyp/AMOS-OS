---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: Knowledge Provenance Binding Protocol
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# Knowledge-Provenance Binding Protocol Specification

> [!ABSTRACT] Protocol Specification
> Formalizes the binding between knowledge claims and their provenance chains in AMOS. Ensures that every consequential knowledge item carries a complete provenance record and that knowledge promotion follows a governed pipeline.

---

## 1. Purpose

Knowledge without provenance is indistinguishable from opinion. This protocol ensures that:

- Every consequential knowledge claim is bound to its source chain
- Knowledge promotion follows a governed pipeline (RAW → SOURCE_CLAIM → EVIDENCE → VALIDATED)
- Provenance completeness is enforced at every promotion boundary
- Falsification conditions are explicitly declared

---

## 2. Knowledge Promotion Pipeline

```text
RAW SIGNAL
    │
    │  Salience filter: ΔH_epistemic > θ_admit
    ▼
SOURCE_CLAIM
    │  Source bound: parent source identified
    │  No independent verification yet
    ▼
EVIDENCE
    │  Cross-reference: ≥2 independent sources OR
    │  Single source with high authority
    │  Provenance check: source ancestry valid
    ▼
CONTRADICTION_CHECK
    │  No active contradiction in knowledge graph
    │  Competing claims identified and documented
    ▼
SCOPE_REGIME_CHECK
    │  Claim scope and regime explicitly declared
    │  Falsifiers explicitly documented
    ▼
VALIDATED KNOWLEDGE
    │  Promotion receipt generated
    │  RSCF node created
    │  Dependent inference enabled
    ▼
ACTIVE KNOWLEDGE
    │  Freshness monitoring active
    │  Revalidation schedule set
    ▼
EXPIRED / SUPERSEDED
    │  TTL expired OR newer version promoted
    │  Tombstone preserved for lineage
```

---

## 3. Provenance Record Structure

Every knowledge item at `EVIDENCE` level or above must carry:

```yaml
provenance_record:
  knowledge_id: "KN-2026-09-04-001"
  claim: "DeeperBrain achieves +18.4% F1 improvement over EEGNet"
  claim_class: "EMPIRICAL"
  
  source_chain:
    - source_id: "arxiv:2601.06134"
      type: "peer_reviewed_preprint"
      authors: ["Wang J", "Zhao S", "et al."]
      institution: "Zhejiang University"
      date: "2026-01-10"
      access: "open"
      hash: "sha256:def456..."
    
    - source_id: "ICLR_2026_benchmark"
      type: "conference_paper"
      venue: "ICLR 2026"
      date: "2026-01-26"
      hash: "sha256:ghi789..."
  
  source_ancestry:
    independent_sources: 2
    shared_ancestry: false
    descendant_copies: 0
  
  scope:
    domain: "EEG_neural_decoding"
    recording_modality: "scalp_EEG"
    task_types: ["motor_imagery", "speech", "emotion"]
    population: "healthy_adults"
  
  regime:
    environment: "laboratory"
    signal_quality: "research_grade"
    generalization: "cross_subject"
  
  freshness:
    published: "2026-01-10"
    last_validated: "2026-09-04"
    ttl_days: 365
    revalidation_schedule: "quarterly"
  
  falsifiers:
    - "Replication study shows no significant improvement over EEGNet"
    - "Foundation model fails to generalize to clinical populations"
    - "Classical decoder with matched compute achieves comparable results"
  
  competing_claims:
    - claim: "ST-EEGFormer achieves comparable performance"
      source: "ICLR_2026"
      relationship: "replication"
  
  confidence_ceiling:
    empirical_evidence: HIGH
    cross_subject_generalization: MEDIUM
    clinical_applicability: LOW
```

---

## 4. Provenance Invariants

| ID | Invariant | Enforcement |
| :--- | :--- | :--- |
| `INV-KP-01` | `10 descendants of 1 source != 10 independent sources` (M15) | Source ancestry checked; copies don't increase weight |
| `INV-KP-02` | Every `EVIDENCE`+ claim has ≥1 source in chain | Promotion blocked without source |
| `INV-KP-03` | Source hashes are immutable | Any hash change creates new source version |
| `INV-KP-04` | Falsifiers must be declared at promotion | Promotion blocked without falsifier documentation |
| `INV-KP-05` | Scope and regime must be explicit | Implicit scope defaults to `UNKNOWN/GAP` |
| `INV-KP-06` | Competing claims must be documented | Active contradictions trigger QUARANTINED status |
| `INV-KP-07` | Freshness TTL is enforced | Expired knowledge is demoted until revalidated |

---

## 5. Promotion Gate Functions

### 5.1 Source Independence Check

$$\text{Independent}(s_1, s_2) \iff \text{Ancestry}(s_1) \cap \text{Ancestry}(s_2) = \emptyset$$

Two sources are independent only if they share no common ancestor in the source graph.

### 5.2 Contradiction Detection

$$\text{Contradicts}(k_1, k_2) \iff \exists\, p \in \text{Predicates}(k_1): p \in \text{Negations}(\text{Predicates}(k_2))$$

When contradiction is detected:
1. Both claims enter `QUARANTINED` status
2. Human steward or SMT solver must resolve
3. Resolution record added to both provenance chains

### 5.3 Confidence Ceiling Propagation

$$\text{Confidence}(k) = \min_{s \in \text{Sources}(k)} \text{Authority}(s) \cdot \text{IndependenceFactor}(k)$$

Where:
- $\text{Authority}(s)$: Source quality rating (peer-reviewed > preprint > blog > social)
- $\text{IndependenceFactor}(k)$: $\sqrt{n_{\text{independent}} / n_{\text{total}}}$ (penalizes redundant sources)

---

## 6. Failure Modes

| Failure | Detection | Recovery |
| :--- | :--- | :--- |
| **Missing provenance** | Promotion gate check | Block promotion; require source identification |
| **Circular provenance** | Source ancestry graph cycle detection | Break cycle; quarantine affected claims |
| **Stale provenance** | TTL expiry check | Demote to `EXPIRED`; require revalidation |
| **False independence** | Source ancestry analysis | Adjust confidence; document shared ancestry |
| **Undeclared falsifiers** | Promotion gate check | Block promotion until falsifiers declared |

---

## 7. Binding Lifecycle

### 7.1 Initial Binding

When a new knowledge claim is first admitted to the system, it enters as `SOURCE_CLAIM` with minimal provenance:

```yaml
initial_binding:
  trigger: "New claim enters via observation or agent inference"
  epistemic_class: "SOURCE_CLAIM"
  provenance_required:
    - "claim_text: string"
    - "claim_source: string (origin identifier)"
    - "timestamp: causal_epoch"
  provenance_optional:
    - "confidence_estimate: float"
    - "supporting_evidence: list[string]"
  binding_action:
    - "Generate unique knowledge_id"
    - "Create RSCF node with SOURCE_CLAIM class"
    - "Record binding in provenance registry"
    - "Set freshness TTL based on source type"
```

### 7.2 Evidence Accumulation

As supporting evidence is gathered, the binding is enriched:

```yaml
evidence_accumulation:
  trigger: "Additional sources or cross-references identified"
  actions:
    - "Append new sources to source_chain"
    - "Recalculate source_ancestry.independent_sources"
    - "Update confidence_ceiling based on new evidence"
    - "Check for contradictions with existing claims"
  promotion_check:
    gate: "≥2 independent sources OR single source with high authority"
    if_met: "Proceed to CONTRADICTION_CHECK"
    if_not_met: "Remain at SOURCE_CLAIM; continue accumulating"
```

### 7.3 Validation Binding

When a claim reaches `VALIDATED` status, full provenance binding is enforced:

```yaml
validation_binding:
  trigger: "Claim passes all promotion gates"
  binding_requirements:
    - "source_chain is non-empty"
    - "source_ancestry is computed and verified"
    - "scope is explicitly declared"
    - "regime is explicitly declared"
    - "falsifiers are documented (≥1)"
    - "competing_claims are identified"
    - "confidence_ceiling is computed"
  binding_action:
    - "Generate promotion receipt"
    - "Create RSCF node with VALIDATED class"
    - "Set revalidation schedule"
    - "Enable dependent inference"
```

### 7.4 Ongoing Maintenance

Validated knowledge requires ongoing provenance maintenance:

| Activity | Frequency | Trigger | Action |
| :--- | :--- | :--- | :--- |
| Freshness check | Daily | TTL approaching expiry | Revalidation required |
| Source verification | Quarterly | Scheduled | Verify sources still accessible |
| Contradiction scan | On admission | New claim admitted | Check against existing claims |
| Confidence recalculation | On new evidence | New source added | Recompute confidence ceiling |
| Tombstone maintenance | On expiry | TTL expired | Preserve lineage, mark EXPIRED |

---

## 8. Provenance Graph Structure

### 8.1 Graph Nodes

```yaml
provenance_graph:
  node_types:
    knowledge_claim:
      fields: ["knowledge_id", "claim_text", "claim_class", "epistemic_class"]
      example: "KN-2026-09-04-001"
    
    source:
      fields: ["source_id", "type", "authors", "date", "hash"]
      example: "arxiv:2601.06134"
    
    agent:
      fields: ["agent_id", "capability_set", "authority_scope"]
      example: "amos-literature-agent-01"
    
    observation:
      fields: ["observation_id", "tool_id", "timestamp", "output_class"]
      example: "OBS-2026-09-04-00129"
    
    decision:
      fields: ["decision_id", "authority_token", "rationale"]
      example: "DEC-2026-09-04-001"
```

### 8.2 Graph Edges

```yaml
provenance_edges:
  source_of:
    from: "source"
    to: "knowledge_claim"
    meaning: "Source supports this claim"
    properties: ["confidence_contribution", "relevance_score"]
  
  derived_from:
    from: "knowledge_claim"
    to: "knowledge_claim"
    meaning: "Claim B is inferred from claim A"
    properties: ["inference_method", "confidence_propagation"]
  
  observed_by:
    from: "observation"
    to: "knowledge_claim"
    meaning: "Observation supports this claim"
    properties: ["observation_tool", "observation_epoch"]
  
  decided_by:
    from: "decision"
    to: "knowledge_claim"
    meaning: "Authority decision affects this claim"
    properties: ["decision_type", "authority_scope"]
  
  contradicts:
    from: "knowledge_claim"
    to: "knowledge_claim"
    meaning: "Claim A contradicts claim B"
    properties: ["contradiction_type", "resolution_status"]
```

### 8.3 Graph Invariants

| ID | Invariant | Enforcement |
| :--- | :--- | :--- |
| `INV-PG-01` | Every knowledge claim has at least one inbound edge | Promotion blocked without source |
| `INV-PG-02` | No cycles in the `derived_from` edge type | Cycle detection on every new edge |
| `INV-PG-03` | `contradicts` edges are bidirectional | Automatic mirror on creation |
| `INV-PG-04` | Source nodes are immutable | Any change creates new source version |
| `INV-PG-05` | Agent nodes carry authority scope | Authority validated on edge creation |

---

## 9. Promotion Gate Functions (Extended)

### 9.1 Source Quality Rating

$$\text{Authority}(s) = \begin{cases} 1.0 & \text{if } s \text{ is peer-reviewed journal} \\ 0.9 & \text{if } s \text{ is peer-reviewed conference} \\ 0.8 & \text{if } s \text{ is preprint (arXiv, bioRxiv)} \\ 0.6 & \text{if } s \text{ is technical blog (authoritative)} \\ 0.4 & \text{if } s \text{ is blog post} \\ 0.2 & \text{if } s \text{ is social media} \\ 0.1 & \text{if } s \text{ is unknown origin} \end{cases}$$

### 9.2 Independence Factor

$$\text{IndependenceFactor}(k) = \sqrt{\frac{n_{\text{independent}}}{n_{\text{total}}}}$$

Where:
- $n_{\text{independent}}$ = number of sources with disjoint ancestry
- $n_{\text{total}}$ = total number of sources

This penalizes redundant sources (e.g., 10 copies of the same paper do not increase confidence).

### 9.3 Confidence Ceiling Computation

$$\text{Confidence}(k) = \min_{s \in \text{Sources}(k)} \text{Authority}(s) \cdot \text{IndependenceFactor}(k)$$

The confidence ceiling is the **minimum** source authority multiplied by the independence factor. This ensures that:
- A claim supported only by social media has low confidence regardless of how many social media sources agree
- A claim supported by 10 copies of the same paper is not treated as 10 independent confirmations

### 9.4 Freshness Decay

$$\text{Freshness}(k, t) = \text{Confidence}(k) \cdot e^{-\lambda \cdot (t - t_{\text{last\_validated}})}$$

Where:
- $\lambda$ = decay rate (configured per domain)
- $t$ = current time
- $t_{\text{last\_validated}}$ = time of last validation

When $\text{Freshness}(k, t) < \theta_{\text{min}}$, the claim is demoted to `EXPIRED` until revalidated.

---

## 10. Failure Modes (Extended)

| Failure | Detection | Recovery | Severity |
| :--- | :--- | :--- | :--- |
| **Missing provenance** | Promotion gate check | Block promotion; require source identification | HIGH |
| **Circular provenance** | Source ancestry graph cycle detection | Break cycle; quarantine affected claims | CRITICAL |
| **Stale provenance** | TTL expiry check | Demote to `EXPIRED`; require revalidation | MEDIUM |
| **False independence** | Source ancestry analysis | Adjust confidence; document shared ancestry | HIGH |
| **Undeclared falsifiers** | Promotion gate check | Block promotion until falsifiers declared | HIGH |
| **Source hash tampering** | Hash verification on source access | Quarantine claim; escalate to security | CRITICAL |
| **Contradiction cascade** | Contradiction detection on new admission | Quarantine all affected claims; human resolution | CRITICAL |
| **Confidence inflation** | Confidence ceiling computation | Recompute; demote if ceiling below threshold | HIGH |

---

## 11. Cross-Vault References

- [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE_MOC]]
- [[01_CANON/07_PROVENANCE/07_PROVENANCE_MOC|07_PROVENANCE_MOC]]
- [[01_CANON/07_PROVENANCE/CANON_PROVENANCE_CONTRACT|CANON_PROVENANCE_CONTRACT]]
- [[11_KNOWLEDGE/02_CLAIMS/02_CLAIMS_MOC|02_CLAIMS_MOC]]
- [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL|DETERMINISTIC_LOGIC_KERNEL]]
- [[10_MEMORY/TIERED_MEMORY_LIFECYCLE_ARCHITECTURE|TIERED_MEMORY_LIFECYCLE_ARCHITECTURE]] — Provenance ties to memory tier lifecycle
- [[09_PROTOCOLS/AGENT_TOOL_INTERACTION_PROTOCOL|AGENT_TOOL_INTERACTION_PROTOCOL]] — Tool outputs bind to provenance

---

```RSCF-NODE
node_id: knowledge_provenance_binding_protocol
node_type: protocol_specification
domain: 09_PROTOCOLS
claim_class: AMOS_MODEL
confidence_ceiling:
  promotion_pipeline: high
  provenance_enforcement: high
  contradiction_detection: high
  source_independence: high
  confidence_computation: high
  freshness_decay: high
falsifiers:
  - A knowledge claim reaches VALIDATED without complete provenance
  - Source independence check fails to detect dependent sources
  - Contradiction detection misses a direct logical negation
  - Confidence ceiling computation produces inflated values
  - Freshness decay fails to demote expired knowledge
```
