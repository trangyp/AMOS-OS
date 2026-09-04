---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Neural Symbolic Hybrid
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

# NEURAL_SYMBOLIC_HYBRID — Neural-Symbolic Hybrid Kernel

## 1. Role

The Neural-Symbolic Hybrid kernel defines how AMOS_OS couples **subsymbolic** (neural, statistical, spiking) perception and pattern inference with **symbolic** (logic, RSCF, rule-governed) reasoning into a single coherent decision substrate. It is the architectural point where the 2026 neuromorphic/photonic compute landscape (Loihi 3, Akida, memristor in-memory computing, SNNs) connects to AMOS's governed symbolic kernel.

The kernel preserves the RSCF class boundary enforced across AMOS:
- **Perception / pattern (neural output)** → `OBSERVATION` / `DERIVED` (statistical, non-deductive)
- **Logic / rule application (symbolic step)** → `DECISION` (requires commit-time authority)
- **Proposed but uncommitted conclusion** → `PROPOSAL`

Per AGENTS.md invariant 2, this kernel uses the smallest sufficient dependency closure and never infers authority from capability.

## 2. Architectural Partition

### 2.1 The Subsymbolic Plane

Handles continuous, high-dimensional, noisy signal — sensory streams, embeddings, spike trains, activations. Characterized by:

- Approximate, gradient-learned weights
- Robust to noise and partial occlusion
- No intrinsic causal/authority semantics
- Computed by neuromorphic (spiking), photonic, or traditional ANN accelerators

### 2.2 The Symbolic Plane

Handles discrete, compositional, rule-governed reasoning. Characterized by:

- Exact, deductive, compositional
- Carries provenance and authority
- Governed by K_CORE_LAWS, K_AUTHORITY, K_CANON
- Eq: unification, forward/backward chaining, constraint satisfaction, RSCF class transitions

### 2.3 The Bridge (Neural→Symbolic Interface)

```
neural_activation (subsymbolic, continuous)
        │  MAP (proposition extraction / grounding)
        ▼
grounded_propositions (symbolic, typed)
        │  RSCF_CLASSIFY (OBSERVATION vs PROPOSAL)
        ▼
logic_engine (K_DETERMINISTIC / ULK)
        │  COMMIT_GATE (authority, provenance, freshness)
        ▼
committed_symbolic_conclusion (DECISION)
```

The bridge is the locus of epistemic discipline: no neural output is ever promoted to `DECISION` without passing the grounding, classification, and commit gate.

## 3. Mathematical Foundations

### 3.1 Neural Feature Extraction

Let input $x \in \mathbb{R}^d$ pass through layers to produce a feature/embedding $z = f_\theta(x)$, where $\theta$ are learned weights. In the spiking case, $x$ may be a spike train; $f_\theta$ becomes a temporal dynamics operator (LIF / surrogate-gradient).

### 3.2 Grounding Function

A grounding/proposition-extraction function $\gamma$ maps the subsymbolic feature to a typed logical atom:

$$
\gamma: \mathcal{Z} \to \mathcal{P}
$$

where $\mathcal{P}$ is the set of typed propositions. Each output carries a confidence/entropy metric $c \in [0,1]$ computed from the neural distribution, enabling downstream uncertainty-aware symbolic reasoning.

### 3.3 Posterior-Aware Symbolic Inference

Given grounded atoms with confidence weights, the symbolic engine applies rules $R$ to derive conclusions. Where probabilistic/dempster-shafer extension is enabled, a conclusion's belief mass is the compositional combination of premise masses under rule $R$:

$$
Bel(\phi) = f_R\big(Bel(\psi_1), \dots, Bel(\psi_k)\big), \quad R: \psi_1 \land \dots \land \psi_k \Rightarrow \phi
$$

For the deterministic default, $f_R$ is strict conjunction: $Bel(\phi)=1$ iff all premises carry sufficient confidence and the rule is validly applied.

### 3.4 Spike-Driven Variant

When the neural backend is spiking, $z$ is a spike rate/order code and the confidence $c$ can be derived from temporal statistics (e.g., first-spike latency or rate). This yields energy-proportional grounding: dense, salient inputs fire more, producing higher-confidence atoms.

## 4. AMOS-Specific Constraints

### 4.1 Class Discipline

- Neural outputs are never auto-committed. They enter as `OBSERVATION` (pattern) or `DERIVED` (statistical synthesis).
- Promotion to `DECISION` requires `COMMIT_GATE`: authority, provenance, freshness, and a valid RSCF transition receipt (per K_ATOMIC_MULTI_RSCF).

### 4.2 Fail-Closed Grounding

If the neural→symbolic mapping confidence is below threshold, or the ontology lacks a corresponding type, the kernel **fails closed** (K_FAIL_CLOSED): the observation is tagged `UNKNOWN`/`GAP` rather than coerced into a possibly-wrong symbol.

### 4.3 Authored-Plasticity Boundary

On-chip learning (Loihi 3 STDP, Akida incremental learning) mutates neural weights outside the central commit funnel. This kernel must classify that mutation:
- **Sensor-level adaptation** → `OBSERVATION` (weight drift is evidence, not authority)
- **Reasoning-level change** → `DECISION` (requires authored, committed, provenance-backed evolution — K_GOVERNED_EVOLUTION)

### 4.4 Energy / Latency Budgets

With photonic or neuromorphic backends, grounding cost scales with relevance (spike density). The kernel exposes per-atom grounding cost so SOFT_REALTIME_SCHEDULER can order work by both deadline and energy budget.

## 5. Protocols

### 5.1 Ground-And-Classify

```
GROUND-AND-CLASSIFY(activation z):
    atoms = [] 
    for each candidate region r in z:
        atom_r = GAMMA(z[r])            # proposition extraction
        c_r = confidence(z[r])          # neural confidence
        cls = RSCF-CLASSIFY(atom_r, c_r)  # OBSERVATION | DERIVED | UNKNOWN
        atoms += [(atom_r, c_r, cls)]
    return atoms
```

### 5.2 Commit-Gated Symbolic Step

```
SYMBOLIC-STEP(premises, rule R):
    require all premises passed GROUND-AND-CLASSIFY
    conclusion = APPLY(R, premises)
    # no commitment yet
    return PROPOSAL(conclusion)
    
COMMIT(proposal):
    gated = COMMIT_GATE(proposal)   # authority + provenance + freshness
    if gated passes:
        return COMMITTED_DECISION(proposal)
    else:
        return DEFERRED|REJECTED_BY_AUTHORITY
```

### 5.3 Explanation / Audit

Because the symbolic plane is exact, the kernel can emit a *derivation trace* (rule sequence + provenance pointers) for any committed decision, even when the root evidence was neural. This is a distinguishing capability of the neural-symbolic hybrid vs. a pure subsymbolic system.

## 6. Integration with 2026 Compute Substrates

- **Neuromorphic (Loihi 3 / Akida / BrainScaleS-2)**: fast, energy-frugal grounding for event-driven perception; continuous-time analog output must be epoch-bounded (see MULTI_EPOCH_COORDINATION).
- **Photonic (Envise)**: high-throughput matrix grounding for dense multimodal inputs.
- **Memristor CIM**: in-situ MVM grounding at the sensor edge, reducing data movement into the symbolic plane.

## 7. Invariants

- **NSH-01:** No neural output commits as `DECISION` without passing COMMIT_GATE.
- **NSH-02:** Grounding always emits an explicit confidence and RSCF class.
- **NSH-03:** Fail-closed on low confidence or missing ontology type.
- **NSH-04:** On-chip learning is classified (OBSERVATION vs DECISION) before it influences reasoning.
- **NSH-05:** Every committed decision has a symbolic derivation trace (auditable).
- **NSH-06:** Subsymbolic and symbolic planes observe separate event/latency contracts.

## 8. Inter-Plane Connections

- **Deterministic logic:** [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL|DETERMINISTIC_LOGIC_KERNEL]] — the symbolic engine
- **ULK:** [[02_KERNEL/ULK_LOGIC_KERNEL|ULK_LOGIC_KERNEL]] — universal logic operator set
- **Authority:** [[02_KERNEL/K_AUTHORITY|K_AUTHORITY]] — commit gating
- **Governed evolution:** [[02_KERNEL/K_GOVERNED_EVOLUTION|K_GOVERNED_EVOLUTION]] — authored mutation of weights/rules
- **Reality substrate:** [[02_KERNEL/K_REALITY|K_REALITY]] — grounding to world state
- **Scheduler:** [[02_KERNEL/SOFT_REALTIME_SCHEDULER|SOFT_REALTIME_SCHEDULER]] — energy/latency-aware ordering
- **Runtime epochs:** [[04_RUNTIME/MULTI_EPOCH_COORDINATION|MULTI_EPOCH_COORDINATION]] — bounding continuous-time inputs

______________________________________________________________________

**MOC:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] · [[00_ROOT/00_HOME|00_HOME]]

**Related:** [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL|DETERMINISTIC_LOGIC_KERNEL]] · [[02_KERNEL/K_REALITY|K_REALITY]] · [[22_RESEARCH/SOTA_NEUROMORPHIC_PHOTONIC_COMPUTING_2026|SOTA_NEUROMORPHIC_PHOTONIC_COMPUTING_2026]]
