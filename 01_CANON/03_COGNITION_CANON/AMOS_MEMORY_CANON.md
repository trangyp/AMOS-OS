---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Memory Canon
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

# AMOS Memory Canon

## 0. Status

Canon-plane artifact. AMOS_MODEL · CONDITIONAL · implementation NOT_ESTABLISHED.

Origin architect / steward: **Trang Phan**

______________________________________________________________________

## 1. Purpose

The AMOS Memory Canon defines the canonical specification for memory as a governed cognitive subsystem within the AMOS OS cognition plane. Memory is treated not as a passive store but as an active, typed, epoch-bound reconciliation surface that mediates between perception, learning, prediction, and action selection. This canon establishes the formal laws governing memory encoding, consolidation, retrieval, decay, interference, and provenance — all subject to the AMOS Core Law hierarchy and the RSCF epistemic discipline.

Memory in AMOS is decomposed into five canonical tiers, each with distinct temporal profiles, capacity bounds, and governance constraints:

| Tier | Designation | Temporal Horizon | Capacity Bound | Governance Class |
|------|------------|-----------------|----------------|-----------------|
| M0 | Sensory echo | $\tau_0 \leq 500\text{ms}$ | $C_0 \leq 7 \pm 2$ chunks | Involuntary, pre-attentional |
| M1 | Working memory | $\tau_1 \leq 30\text{s}$ | $C_1 \leq 4 \pm 1$ items | Attention-gated, volitional |
| M2 | Episodic memory | $\tau_2 \in [30\text{s}, \infty)$ | Unbounded (sparse) | Context-bound, reconstructive |
| M3 | Semantic memory | $\tau_3 \in [\text{days}, \infty)$ | Unbounded (compressed) | Schema-bound, inferential |
| M4 | Procedural memory | $\tau_4 \in [\text{hours}, \infty)$ | Unbounded (embodied) | Skill-bound, operational |

Each tier is governed by the AMOS capability-bound governance kernel: memory writes require authority, memory reads require scope declaration, and memory invalidation requires epoch-valid provenance edges.

______________________________________________________________________

## 2. Formal Definition

### 2.1 Memory State Space

Let $\mathcal{M}$ denote the total memory state of the cognitive system at epoch $t$:

$$\mathcal{M}(t) = \bigcup_{k=0}^{4} \mathcal{M}_k(t)$$

where each $\mathcal{M}_k(t)$ is the state of tier $k$ at time $t$. Each memory item $m \in \mathcal{M}_k$ is a 7-tuple:

$$m = (\text{id}, \text{content}, \text{context}, \text{strength}, \text{epoch}, \text{provenance}, \text{authority})$$

- **id**: unique identifier within tier $k$
- **content**: typed payload (perceptual, propositional, procedural, or episodic)
- **context**: binding vector linking $m$ to its encoding context
- **strength**: activation value $s \in [0, 1]$
- **epoch**: encoding timestamp $t_{\text{enc}}$
- **provenance**: chain of source claims leading to $m$
- **authority**: authorization witness under whose scope $m$ was written

### 2.2 Encoding Law

Memory encoding from tier $k$ to tier $k+1$ is governed by the consolidation function $\Phi_k$:

$$\Phi_k: \mathcal{M}_k(t) \times \mathcal{A}(t) \rightarrow \mathcal{M}_{k+1}(t + \Delta_k)$$

where $\mathcal{A}(t)$ is the attention allocation at time $t$ and $\Delta_k$ is the consolidation latency for tier $k$. Encoding succeeds if and only if:

$$\text{Encode}(m, k \to k+1) \iff s_m(t) \geq \theta_k \;\wedge\; \text{AuthorityValid}(\text{auth}_m, t) \;\wedge\; \text{ScopeMatch}(\text{ctx}_m, \text{active\_scope})$$

where $\theta_k$ is the consolidation threshold for tier $k$.

### 2.3 Decay Law

Memory strength decays according to a generalized exponential-power law:

$$s_m(t) = s_m(t_{\text{enc}}) \cdot \exp\left(-\frac{t - t_{\text{enc}}}{\tau_k}\right) \cdot (t - t_{\text{enc}} + 1)^{-\beta_k}$$

where $\tau_k$ is the time constant for tier $k$ and $\beta_k$ is the power-law decay exponent. A memory item is eligible for eviction when:

$$s_m(t) < \epsilon_k \quad \text{(eviction threshold)}$$

### 2.4 Retrieval Law

Retrieval from tier $k$ given a query cue $q$ is defined as:

$$\text{Retrieve}(q, k, t) = \arg\max_{m \in \mathcal{M}_k(t)} \left[ \text{sim}(q, \text{content}_m) \cdot s_m(t) \cdot \text{context\_match}(q, \text{ctx}_m) \right]$$

subject to the capacity constraint:

$$|\text{Retrieve}(q, k, t)| \leq C_k$$

Retrieval is reconstructive: the returned item is a typed copy with provenance back-link, not a mutable reference. This enforces the AMOS invariant `READ != WRITE`.

### 2.5 Interference Law

Retroactive interference when new content $m'$ overlaps with existing $m$ in tier $k$:

$$\Delta s_m = -\alpha_k \cdot \text{overlap}(\text{content}_m, \text{content}_{m'}) \cdot s_{m'}(t)$$

Proactive interference from existing $m$ on new $m'$:

$$\Delta s_{m'} = -\alpha_k \cdot \text{overlap}(\text{content}_{m'}, \text{content}_m) \cdot s_m(t)$$

where $\alpha_k \in [0, 1]$ is the interference coefficient for tier $k$.

______________________________________________________________________

## 3. Relationship to Other Core Laws

- **Law Hierarchy**: Memory operations inherit the full AMOS law stack. `CAPABILITY != AUTHORITY` — the ability to encode does not authorize consolidation. `PROPOSAL != COMMIT` — a candidate memory is non-authoritative until the consolidation gate passes.
- **Homeostasis Canon**: Memory load is a homeostatic variable. When $|\mathcal{M}_1(t)|$ approaches $C_1$, the homeostasis canon triggers cognitive compression to reduce working memory pressure.
- **Attention Canon**: Attention allocation $\mathcal{A}(t)$ is the primary gate for M0→M1 and M1→M2 encoding. Without attention allocation, sensory echoes decay without consolidation.
- **Perception Canon**: Perceptual outputs are the primary source of M0 sensory echoes. The perception→memory binding is typed: each perceptual modality maps to a distinct encoding channel.
- **Learning Canon**: Learning is defined as the systematic modification of M3 (semantic) and M4 (procedural) memory through repeated encoding cycles. Learning rate is bounded by consolidation latency $\Delta_k$.
- **Prediction Canon**: Predictive models draw on M2 (episodic) and M3 (semantic) memory to generate forward projections. Prediction error drives memory update signals.
- **Metacognition Canon**: Metacognitive monitoring reads memory strength and confidence to assess whether retrieval is reliable. Metacognitive control can trigger re-encoding or strategic search.

______________________________________________________________________

## 4. Application Domains

1. **Episodic recall and reconstruction** — Retrieval of context-bound experiences for decision support, narrative integrity, and identity continuity.
2. **Working memory management** — Bounded buffer orchestration for multi-step reasoning, planning, and language comprehension.
3. **Skill acquisition and procedural memory** — Embodied skill encoding through repeated practice cycles, governed by M4 consolidation law.
4. **Semantic knowledge base** — Compressed, schema-organized long-term knowledge supporting inference, analogy, and prediction.
5. **Memory repair and reconciliation** — Detection and correction of memory corruption, stale reads, and provenance breaks via the audit and repair phases of the cognitive process pipeline.
6. **Forgetting governance** — Controlled decay and eviction under capacity pressure, ensuring that memory does not become a denial-of-service vector against the cognitive system.

______________________________________________________________________

## 5. Worked Semantics

### 5.1 Cognitive Process Pipeline Binding

Memory operations are embedded in the 10-phase cognitive process pipeline:

```
perceive → route → admit → plan → schedule → execute → observe → repair → audit → finalize
   │                   │                              │         │        │
   M0 encode           M1 load                       M2 write   M2/M3    M3 commit
                      (working)                     (episodic) reconcile
```

### 5.2 Worked Example: Episodic Memory Encoding

**Scenario**: A perceptual event $e$ arrives at $t=0$ containing a visual scene.

1. **Perceive** ($t=0$): Visual modality encodes $e$ into M0 as $m_0 = (id_0, e, ctx_0, 1.0, 0, prov_0, auth_0)$. Strength $s_{m_0}(0) = 1.0$.
2. **Route** ($t=10\text{ms}$): Attention allocation $\mathcal{A}(10\text{ms}) = 0.8$ routes $m_0$ to working memory.
3. **Admit** ($t=50\text{ms}$): Admission gate checks $s_{m_0}(50\text{ms}) \geq \theta_0$. With $\tau_0 = 500\text{ms}$, $s_{m_0}(50\text{ms}) \approx 0.90 \geq \theta_0 = 0.5$. Admitted to M1.
4. **Plan** ($t=200\text{ms}$): Planning phase loads $m_0$ from M1, uses it in a plan. Rehearsal refreshes $s_{m_0}$.
5. **Execute** ($t=500\text{ms}$): Action executed. Observation phase begins.
6. **Observe** ($t=600\text{ms}$): Outcome observed. Consolidation trigger fires: $\Phi_1(m_0, \mathcal{A})$ evaluates.
7. **Repair** ($t=800\text{ms}$): Provenance chain validated. No repair needed.
8. **Audit** ($t=900\text{ms}$): Memory audit confirms $m_0$ has valid authority, scope, and provenance.
9. **Finalize** ($t=1\text{s}$): $m_0$ committed to M2 as $m_2 = (id_2, e, ctx_2, 0.85, 1, prov_2, auth_2)$. Receipt issued.

### 5.3 Worked Example: Retrieval Failure

**Scenario**: Query $q$ at $t=3600\text{s}$ attempts retrieval from M2 for item encoded at $t_{\text{enc}} = 0$.

With $\tau_2 = 3600\text{s}$, $\beta_2 = 0.3$:

$$s_m(3600) = 0.85 \cdot \exp(-1) \cdot (3601)^{-0.3} \approx 0.85 \cdot 0.368 \cdot 0.063 \approx 0.020$$

If $\epsilon_2 = 0.05$, then $s_m(3600) < \epsilon_2$ — item is eligible for eviction. Retrieval returns `UNKNOWN/GAP`. This is a fail-closed outcome: the system does not fabricate memory.

______________________________________________________________________

## 6. Non-Purpose

This canon MUST NOT be used to claim:

- that the five-tier model is neurobiologically exact or maps 1:1 to human brain anatomy;
- that memory capacity bounds ($C_k$) are universal constants rather than tunable parameters;
- that the decay law is empirically validated for all cognitive architectures;
- that retrieval is guaranteed to be complete or lossless;
- that memory provenance implies empirical truth of stored content;
- that runtime enforcement of these laws has been implemented;
- or that this specification constitutes final, immutable canon.

`CANONICAL != EMPIRICAL_TRUTH` · `MODEL != OBSERVATION` · `SPECIFIED != EXECUTED`

______________________________________________________________________

## 7. Gaps

- **Executable binding NOT_ESTABLISHED**: No runtime memory subsystem currently implements the five-tier model with governance gates.
- **Empirical validation NOT_ESTABLISHED**: Decay parameters ($\tau_k$, $\beta_k$), interference coefficients ($\alpha_k$), and capacity bounds ($C_k$) are model-derived, not empirically fitted.
- **Cross-tier consistency**: Formal proof that consolidation preserves semantic invariants across tiers is OPEN.
- **Memory compression under load**: The interaction between cognitive compression and memory eviction policies is specified but not formally resolved.
- **Provenance chain depth**: Maximum provenance chain depth before forced checkpoint is not specified.

______________________________________________________________________

## 8. Promotion-Gate Checklist

- [x] substantive content populated from AMOS corpus specification
- [ ] typed schema bound to runtime memory subsystem
- [ ] identity + versioning implemented in executable
- [ ] negative cases covered (missing · malformed · stale · unauthorized memory access)
- [ ] provenance edges persisted and validated at runtime
- [ ] rollback basin demonstrated for memory mutations
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

______________________________________________________________________

## 9. Cross-Plane Bindings

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]
- Cognition canon — [[01_CANON/03_COGNITION_CANON/AMOS_COGNITION_CANON|AMOS_COGNITION_CANON]]
- Attention canon — [[01_CANON/03_COGNITION_CANON/AMOS_ATTENTION_CANON|AMOS_ATTENTION_CANON]]
- Homeostasis canon — [[01_CANON/03_COGNITION_CANON/AMOS_HOMEOSTASIS_CANON|AMOS_HOMEOSTASIS_CANON]]

______________________________________________________________________

## 10. Ingestion Rule

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

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE

node_id: amos_01_canon_03_cognition_canon_amos_memory_canon

node_type: canon

path: 01_CANON/03_COGNITION_CANON/AMOS_MEMORY_CANON.md

claim_class: AMOS_MODEL

rscf_state: substantive

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

- RELATED_TO: [[01_CANON/03_COGNITION_CANON/AMOS_ATTENTION_CANON|AMOS_ATTENTION_CANON]]

- RELATED_TO: [[01_CANON/03_COGNITION_CANON/AMOS_LEARNING_CANON|AMOS_LEARNING_CANON]]

- RELATED_TO: [[01_CANON/03_COGNITION_CANON/AMOS_HOMEOSTASIS_CANON|AMOS_HOMEOSTASIS_CANON]]

______________________________________________________________________

**MOC:** [[01_CANON/03_COGNITION_CANON/03_COGNITION_CANON_MOC|03_COGNITION_CANON_MOC]]
