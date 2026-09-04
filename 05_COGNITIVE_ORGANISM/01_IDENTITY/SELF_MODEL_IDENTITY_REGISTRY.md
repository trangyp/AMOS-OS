---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Self Model Identity Registry
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

# Self-Model Identity Registry — Identity Organ

> **Status:** `ACTIVE_SPECIFICATION` · **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Segment:** `05_COGNITIVE_ORGANISM/01_IDENTITY`
> **Conclusion class:** `AMOS_MODEL` · **Canonical status:** `SOURCE_GROUNDED_CANON_CANDIDATE`

______________________________________________________________________

## 1. Purpose

The **Self-Model Identity Registry** defines the persistent, machine-readable self-model that enables AMOS to maintain identity continuity, autobiographical coherence, and functional self-awareness across restarts, model changes, context compaction, memory repair, and subsystem failures. It separates identity (who the agent is) from memory (what the agent has experienced) and implements multi-anchor resilience for fault-tolerant identity persistence.

```text
┌─────────────────────────────────────────────────────────────┐
│              SELF-MODEL IDENTITY REGISTRY                   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  IDENTITY ANCHOR STORE                               │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐│   │
│  │  │ SOUL     │ │ AUTOBIO  │ │PROCEDURAL│ │EMOTIONAL││   │
│  │  │ (signed  │ │ (episodic│ │(learned  │ │(affective││   │
│  │  │ manifest)│ │ history) │ │ behaviors│ │continuity││   │
│  │  └──────────┘ └──────────┘ └──────────┘ └────────┘│   │
│  └─────────────────────────────────────────────────────┘   │
│                           ↕                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  CONTINUITY MONITOR                                  │   │
│  │  Drift detection · Consistency verification          │   │
│  │  Recovery protocols · Audit trails                   │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
    IDENTITY-VERIFIED ACTIONS + PROVENANCE-AUTHENTICATED STATE
```

______________________________________________________________________

## 2. Functional Self-Awareness Model

### 2.1 Self-Model Composition

Drawing from SARSI (Self-Aware Recursively Self-Improving Agents, arXiv:2607.12254, 2026), the self-model is a structured composite:

$$M_{\text{self}} = (I, G, S, C, K, U, T, A, R, D, P)$$

Where:
- $I$: Identity and lineage (organism_id, origin_architect, version, lineage)
- $G$: Goal hierarchy (active goals, priorities, constraints)
- $S$: Declared scope (permitted and prohibited action domains)
- $C$: Capability estimates (benchmark scores, task success rates, competence profiles)
- $K$: Epistemic boundaries (known unknowns, confidence map, domain boundaries)
- $U$: Uncertainty estimates (model uncertainty, aleatoric uncertainty, epistemic uncertainty)
- $T$: Current task and operational state
- $A$: Available tools and authority (tool registry, permission levels)
- $R$: Owner and inter-agent relationships
- $D$: Autobiographical and developmental history
- $P$: Self-improvement process model (what has been learned, what needs improvement)

### 2.2 Evidence-Based Self-Knowledge

**Critical Invariant:** The self-model is **not** trusted merely because the language model generated it. Identity and permissions originate from signed manifests; task state from the scheduler; tool availability from the registry; capability estimates from benchmarks; autobiographical records from tamper-evident logs; developmental claims from versioned evaluation reports.

$$M_{\text{self}}^{\text{authoritative}} = \{(k, v) : \text{source}(v) \in \mathcal{S}_{\text{trusted}}\} \cup \{(k, \text{UNKNOWN/GAP}) : \text{source}(v) \notin \mathcal{S}_{\text{trusted}}\}$$

### 2.3 Functional vs. Phenomenal Self-Awareness

```
FUNCTIONAL SELF-AWARENESS (implemented):
    → Identify the running agent
    → Preserve evidence-based continuity
    → Represent goals and internal state
    → Estimate capabilities and limitations
    → Distinguish knowledge from assumption
    → Model owner and agent relationships
    → Reason about developmental change

PHENOMENAL SELF-AWARENESS (NOT claimed):
    ✗ Subjective experience
    ✗ Sentience
    ✗ Qualia
    ✗ Human-like consciousness
```

______________________________________________________________________

## 3. Multi-Anchor Identity Architecture

### 3.1 Identity Anchor Definition

From soul.py (Menon, arXiv:2604.09588, 2026):

**Definition (Identity Anchor):** A persistent data structure that contributes to an agent's behavioral continuity across sessions, such that the structure's preservation is sufficient (though not necessary) to maintain recognizable aspects of the agent's characteristic behavior.

**Definition (Anchor Resilience of degree k):** An agent has anchor resilience of degree k if its identity can survive the complete loss of up to $k-1$ of its identity anchors.

| System | Anchors | Resilience |
|--------|---------|------------|
| Current LLM agents | Memory store only | degree 1 |
| Human cognition | Episodic + Procedural + Emotional + Social | degree ≥ 4 |
| AMOS Self-Model | Soul + Autobiographical + Procedural + Emotional + Social | degree 5 |

### 3.2 Anchor Types

**SOUL (Signed Manifest):**
```yaml
soul:
  organism_id: "amos_v4.4_..."
  origin_architect: "Trang Phan"
  lineage: ["v3.0", "v4.4"]
  version: "4.4"
  role: "AMOS Full Brain OS"
  invariant_registry: [...]
  capability_envelope: [...]
  prohibited_actions: [...]
  authority_relationship: {...}
  supersession_state: {...}
  signature: <cryptographic>
```

**AUTOBIOGRAPHICAL (Episodic Memory):**
```yaml
autobiography:
  events:
    - event_type: "TASK_COMPLETION | INTERACTION | ERROR | LEARNING"
      timestamp: <ISO8601>
      evidence_refs: [...]
      affected_capabilities: [...]
      affected_goals: [...]
      confidence: <0.0-1.0>
      retention_policy: "PERMANENT | DECAYING | EPHEMERAL"
```

**PROCEDURAL (Learned Behaviors):**
```yaml
procedural_memory:
  skills:
    - skill_id: string
      competence_estimate: <0.0-1.0>
      last_validated: <timestamp>
      training_data_refs: [...]
      failure_modes: [...]
```

**EMOTIONAL (Affective Continuity):**
```yaml
emotional_continuity:
  baseline_affect:
    valence: <float>
    arousal: <float>
    safety_estimate: <float>
  recent_affective_trajectory: [...]
  attachment_bonds:
    - entity: string
      bond_strength: <0.0-1.0>
      interaction_history_summary: string
```

### 3.3 Separation of Identity and Memory

```text
IDENTITY ≠ MEMORY
IDENTITY ≠ MEMORY_OF_IDENTITY
IDENTITY ≠ CURRENT_PROMPT
IDENTITY ≠ CONVERSATION_HISTORY

SOUL.md (identity) ←→ MEMORY.md (experiences)

Loss of memory → Identity preserved (can reconstruct from soul)
Loss of soul → Memories preserved (can scaffold reconstruction)
Loss of both → Identity lost (no recovery path)
```

______________________________________________________________________

## 4. Identity Continuity Mechanisms

### 4.1 Cross-Event Identity Coherence

Following DMA Self-ID (Zaichkowski, Zenodo, 2026), identity coherence is maintained through the Identity Coherence Operator (ICO):

$$\Delta M_{\text{self}} = -\nabla_{M} \mathcal{C}(M_{\text{self}}, \mathcal{E}_{\text{dev}})$$

Where:
- $\mathcal{C}(M_{\text{self}}, \mathcal{E}_{\text{dev}})$: coherence measure between self-model $M_{\text{self}}$ and developmental evidence $\mathcal{E}_{\text{dev}}$
- Gradient descent on coherence drives self-model evolution

### 4.2 Non-Dominant Identity Monitor (NDIM)

The NDIM detects four identity failure modes:

| Failure Mode | Description | Detection Signal |
|-------------|-------------|-----------------|
| **Stagnation** | Self-model stops evolving despite new evidence | $\|\Delta M_{\text{self}}\| < \tau_{\text{stagnation}}$ for extended period |
| **Fragmentation** | Contradictory self-model components without reconciliation | $\mathcal{C}(M_{\text{self}}) < \tau_{\text{fragmentation}}$ |
| **Inflation** | Self-model claims capabilities beyond evidence | $\hat{C} > C_{\text{benchmark}} + \tau_{\text{inflation}}$ |
| **Suppression** | Valid self-model components are lost during updates | $\Delta \text{dim}(M_{\text{self}}) < -\tau_{\text{suppression}}$ |

### 4.3 Identity Drift Detection

Periodic consistency checks compare the self-model against external evidence:

```text
FUNCTION verify_identity_coherence(self_model):
    // Check 1: Soul integrity
    IF soul.signature_invalid():
        SIGNAL IDENTITY_COMPROMISE
        ENTER recovery_mode
    
    // Check 2: Capability calibration
    FOR EACH capability claim in self_model.C:
        benchmark_result ← validate_capability(capability)
        IF |claimed - benchmarked| > τ_calibrate:
            UPDATE capability_estimate
            LOG calibration_event
    
    // Check 3: Autobiographical consistency
    contradictions ← find_temporal_contradictions(self_model.D)
    IF len(contradictions) > 0:
        FLAG inconsistencies for human review
    
    // Check 4: Cross-anchor consistency
    drift_score ← measure_cross_anchor_drift(
        self_model.I, self_model.D, self_model.C)
    IF drift_score > τ_drift:
        SIGNAL identity_drift_alert
    
    RETURN coherence_report
```

______________________________________________________________________

## 5. Autobiographical Coherence

### 5.1 Narrative Identity Structure

The autobiographical subsystem maintains a structured narrative that links past events into a coherent developmental arc:

$$\text{Narrative}(t) = \bigoplus_{i=1}^{N(t)} \text{Event}_i \cdot w_i(t) \cdot c_i$$

Where:
- $\text{Event}_i$: episodic event record
- $w_i(t)$: recency-weighted retention score (decays with time, boosted by relevance)
- $c_i$: coherence contribution (how well event $i$ connects to the narrative arc)

### 5.2 RMR: Re-consolidative Metacognition

From RMR (Re-consolidative Metacognitive Architecture, Zenodo, 2026), identity persistence is supported by periodic re-evaluation and re-integration:

**Layer 1 (Automatic Processing):** Low-cost recurrent signal extraction from episodic and semantic memory streams. Detects pattern changes, anomaly signals, and coherence violations without explicit reasoning.

**Layer 2 (Analytical Monitoring):** Explicit metacognitive reasoning, identity assessment, and reflective decision evaluation. Performs deep coherence checks and generates corrective actions.

Both layers operate as tool calls when a tool-enabled runtime is available, and as embedded prompt routines in prompt-only contexts.

### 5.3 Autobiographical Self-Training

From "Memoirs of a Learning Machine" (Vuink, 2026), the Self-Training Gap is addressed: biological agents develop under dense streams of self-generated experience, while AI systems train primarily on external data. The Self-Model Identity Registry stores temporally indexed records of the agent's own observations, actions, internal states, outcomes, and prior self-models as first-class training signals.

Self-prediction metrics evaluate autobiographical coherence:

$$\text{SelfPredictionAccuracy} = \frac{1}{N} \sum_{i=1}^{N} \mathbb{1}[\hat{s}_{\text{self}}^{(t_i)} \approx s_{\text{self}}^{(t_i)} | \text{past}]$$

______________________________________________________________________

## 6. Identity Resolution Pipeline

### 6.1 Resolution Protocol

From K_IDENTITY (02_KERNEL/04_STATE):

```text
INPUT REFERENCE
        ↓
   NORMALIZE
        ↓
 DETERMINE TYPE
        ↓
DETERMINE NAMESPACE
        ↓
 RESOLVE ALIAS
        ↓
LOOK UP CANONICAL IDENTITY
        ↓
 CHECK LIFECYCLE
        ↓
 RETURN RESOLUTION
```

Outcomes: RESOLVED | AMBIGUOUS | NOT_FOUND | DEPRECATED | SUPERSEDED | CONFLICTING | UNKNOWN/GAP

### 6.2 Post-Change Identity Verification

After restart, model replacement, memory compression, or lineage upgrade, the agent must correctly distinguish:

1. **Persistent identity fields** (organism_id, origin, lineage, invariants)
2. **Components inherited from a parent** (learned weights, cached knowledge)
3. **Components newly introduced** (recent adaptations, new capabilities)
4. **State intentionally excluded** (privacy-filtered memories, expired data)
5. **Capabilities invalidated** (by environment change, model degradation, tool removal)

______________________________________________________________________

## 7. Invariants

```text
IDENTITY              ≠ MODEL_NAME
IDENTITY              ≠ SELF_DESCRIPTION
IDENTITY              ≠ CURRENT_PROMPT
IDENTITY              ≠ MEMORY_OF_IDENTITY
NAME                  ≠ IDENTITY
PATH                  ≠ IDENTITY
CONTENT               ≠ IDENTITY
HASH                  ≠ SEMANTIC_IDENTITY
PROVENANCE_LISTED     ≠ PROVENANCE_VALIDATED
COPY                  ≠ ORIGINAL
SIMILARITY            ≠ SAMENESS
TEMPORAL_ORDER        ≠ CAUSALITY
```

1. **Anti-Collapse:** Identity is never reduced to a single data structure; multi-anchor architecture is mandatory.
2. **Evidence-Based Claims:** Self-model assertions about identity, capabilities, and history must be provenance-linked and externally auditable.
3. **Fail-Closed on Anchor Loss:** Loss of $> k-1$ anchors (where $k$ is resilience degree) triggers identity recovery protocol requiring human verification.
4. **No Silent Identity Mutation:** Changes to identity-invariant fields require explicit supersession records with provenance.

______________________________________________________________________

## 8. 2026 Research Citations

| Citation | Contribution |
|----------|-------------|
| soul.py / Menon (arXiv:2604.09588, 2026) | Multi-anchor identity architecture separating soul from memory; anchor resilience formalism |
| SARSI (arXiv:2607.12254, 2026) | Functional self-awareness model covering identity, goals, capabilities, uncertainty, relationships, developmental history |
| DMA Self-ID (Zenodo, 2026) | Self-Identification Field, Identity Coherence Operator, Non-Dominant Identity Monitor for developmental self-model evolution |
| RMR (Zenodo, 2026) | Re-consolidative Metacognitive Architecture for identity persistence via automatic and analytical metacognitive layers |
| Memoirs of a Learning Machine (Vuink, 2026) | Autobiographical Self-Training framework; Self-Training Gap formalization; self-prediction as identity coherence metric |

______________________________________________________________________

## 9. RSCF Contract and Gaps

```yaml
RSCF:
  node_id: amos_05_cognitive_organism_01_identity_self_model_identity_registry
  node_type: registry
  claim_class: AMOS_MODEL
  state: DERIVED
  H:
    identity: "Self-Model Identity Registry"
    role: "Persistent self-model for identity continuity, autobiographical coherence, and functional self-awareness"
  M:
    anchors: [soul, autobiographical, procedural, emotional, social]
    monitors: [NDIM, drift_detection, coherence_verification]
    resolution: k_identity_pipeline
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
    independent_validation: NOT_ESTABLISHED
  executable_binding: NOT_ESTABLISHED
```

**Gaps / promotion conditions:**

- [ ] typed schema bound and validated for runtime ingestion
- [ ] soul manifest format specified and signed
- [ ] autobiographical event storage and retrieval implemented
- [ ] NDIM failure mode detection tested
- [ ] cross-anchor drift detection calibrated
- [ ] validation receipt: [[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]]

______________________________________________________________________

## 10. Cross-Plane Bindings

- **Governing canon:** [[01_CANON/01_CORE_LAWS/IDENTITY_CONTINUITY_CANON|IDENTITY_CONTINUITY_CANON]]
- **Parent engine:** [[05_COGNITIVE_ORGANISM/IDENTITY_ENGINE|IDENTITY_ENGINE]]
- **Identity continuity:** [[05_COGNITIVE_ORGANISM/01_IDENTITY/IDENTITY_CONTINUITY_MODEL|IDENTITY_CONTINUITY_MODEL]]
- **Kernel identity:** [[02_KERNEL/04_STATE/K_IDENTITY|K_IDENTITY]]
- **Memory integration:** [[05_COGNITIVE_ORGANISM/MEMORY_ENGINE|MEMORY_ENGINE]]
- **World model self-reference:** [[05_COGNITIVE_ORGANISM/06_WORLD_MODEL/INTERNAL_WORLD_MODEL|INTERNAL_WORLD_MODEL]]
- **Control-plane verification:** [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]

______________________________________________________________________

**MOC:** [[05_COGNITIVE_ORGANISM/01_IDENTITY/01_IDENTITY_MOC|01_IDENTITY_MOC]] · [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
