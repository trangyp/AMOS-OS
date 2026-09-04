---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Graph Family Specification
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

# GRAPH FAMILY SPECIFICATION

> [!ABSTRACT] Purpose
> `GRAPH_FAMILY_SPECIFICATION` defines the twelve typed graph families identified in the
> AMOS OS Architecture Audit (2026-09-04 § "Graph substrate correction"). It establishes
> node semantics, edge semantics, algebraic structure, invariants, cross-graph morphisms,
> and AMOS-specific constraints for each family. This replaces the audit's implicit
> `graph` monolith with governed typed graph families whose composition is regulated.
>
> **Status:** AMOS_MODEL · CONDITIONAL · implementation PARTIAL.
>
> **Key invariant:** `GRAPH_TYPE_1 ≠ GRAPH_TYPE_2` unless an explicit morphism proves
> structural and semantic adequacy. Graph families are typed and non-interchangeable,
> mirroring the tensor axis typing law.

---

## 0. Architectural Context

The architecture audit (2026-09-04) identified that AMOS uses "graph" as one generic
architecture object and directed:

> "Do not use `graph` as one generic architecture object. Define typed graph families."

This document implements that correction. The 12 families partition the graph substrate
along semantic axes that align with the seven MECE representation axes:

```
Authority        → Authority Graph (G_AUTH)
Cognitive        → Knowledge Graph (G_KN), Epistemic Graph (G_EPI),
                   Intent Graph (G_INT), Causal Graph (G_CAU)
Execution        → Communication Graph (G_COM), Resource Graph (G_RES)
Information      → Provenance Graph (G_PROV), Temporal Graph (G_TMP)
Assurance        → Identity Graph (G_ID)
Scale            → Spatial Graph (G_SPA)
Lifecycle        → Evolution Graph (G_EVO)
```

---

## 1. Graph Type Lattice

The following diagram shows the partial order of graph families by informational
dependency. An arrow `A → B` means B may depend on A but not vice versa.

```
                    ┌──────────────┐
                    │  G_PROV      │
                    │  Provenance  │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
       ┌──────▼──────┐ ┌──▼───────┐ ┌──▼──────────┐
       │  G_KN       │ │  G_CAU   │ │  G_EVO      │
       │  Knowledge  │ │  Causal  │ │  Evolution  │
       └──────┬──────┘ └──┬───────┘ └──┬──────────┘
              │            │            │
       ┌──────▼──────┐    │            │
       │  G_EPI      │    │            │
       │  Epistemic  │    │            │
       └──────┬──────┘    │            │
              │            │            │
       ┌──────▼──────┐    │            │
       │  G_INT      │    │            │
       │  Intent     │    │            │
       └──────┬──────┘    │            │
              │            │            │
              └────────────┼────────────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
       ┌──────▼──────┐ ┌──▼───────┐ ┌──▼──────────┐
       │  G_TMP      │ │  G_SPA   │ │  G_ID       │
       │  Temporal   │ │  Spatial │ │  Identity   │
       └──────┬──────┘ └──┬───────┘ └──┬──────────┘
              │            │            │
              └────────────┼────────────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
       ┌──────▼──────┐ ┌──▼───────┐ ┌──▼──────────┐
       │  G_COM      │ │  G_AUTH  │ │  G_RES      │
       │  Communic.  │ │  Auth.   │ │  Resource   │
       └─────────────┘ └──────────┘ └─────────────┘
```

Key reading: Provenance sits at the top (everything may depend on lineage tracking).
Communication, Authority, and Resource graphs sit at the base (they are constitutive
infrastructure that other graphs may reference but do not internally contain).

---

## 2. Cross-Graph Morphism Structure

Morphisms are typed, partial, structure-preserving maps between graph families. Not all
morphisms exist. The registry below is the authoritative allowed-set.

```
Source → Target        Morphism Class       Guard
─────────────────────  ───────────────────  ──────────────────────────────
G_KN  →  G_EPI        projection           evidence_class axis retained
G_KN  →  G_CAU        extraction           only causal-level edges survive
G_KN  →  G_PROV       embedding            provenance axis promoted
G_CAU →  G_TMP        temporal_slice       time axis extracted
G_CAU →  G_EPI        confidence_lift      confidence propagated
G_PROV→  G_EVO        version_fold         version axis becomes primary
G_PROV→  G_ID         signer_project       provenance→identity extraction
G_INT →  G_COM        channel_bind         goals mapped to channels
G_INT →  G_RES        resource_bind        plans mapped to resource needs
G_TMP →  G_SPA        spatial_project      epoch vector→spatial state
G_ID  →  G_AUTH       credential_lift      identity→authority grant
G_COM →  G_TMP        round_index          consensus rounds→time
G_RES →  G_SPA        allocation_map       resources→spatial shards
G_EVO →  G_PROV       ancestry_embed       version history→provenance
G_EPI →  G_INT        uncertainty_goal     confidence→goal prioritization
```

### Morphism contract

Every morphism `φ: G_A → G_B` must satisfy:

1. **Typed signature** — node types in G_A map to a declared subset of G_B node types.
2. **Edge preservation** — if `(u,v) ∈ E_A` with edge type `t`, then
   `φ(u), φ(v) ∈ V_B` with edge type `ψ(t)` where `ψ` is the declared edge map.
3. **Provenance union** — `Prov(φ(G_A)) ⊇ Prov(G_A)`.
4. **Epistemic ceiling** — confidence in G_B ≤ confidence in G_A.
5. **Finiteness** — φ terminates for finite input.
6. **Reversibility marker** — if φ is not invertible, the morphism must declare `LOSSY`
   with the specific information not recoverable.

---

## 3. Graph Family Definitions

### 3.1 Knowledge Graph (G_KN)

**Purpose:** Semantic knowledge — entities, relations, entailment, ontology.

| Aspect | Definition |
|--------|-----------|
| **Node types** | `Entity`, `Class`, `Property`, `Relation`, `Axiom`, `OntologyNode` |
| **Edge types** | `IS_A`, `INSTANCE_OF`, `HAS_PROPERTY`, `ENTAILS`, `CONTRADICTS`, `PART_OF`, `DEFINED_BY` |
| **Algebraic structure** | Semilattice (join = least common subsumer); composition via path-concatenation; quotient by equivalence classes |
| **Invariants** | (1) No orphan relation edges; every edge references valid typed nodes. (2) `ENTAILS` is transitive and acyclic. (3) `CONTRADICTS` is symmetric and must not transitively close to self-contradiction in a consistent ontology. (4) Class hierarchy is a DAG. |
| **AMOS constraints** | Preserve SOURCE_CLAIM / OBSERVATION / DERIVED / MODEL distinctions on every entity. Schema version must be declared. Unknown entity types recorded as `UNKNOWN/GAP`. |

### 3.2 Causal Graph (G_CAU)

**Purpose:** Causal relations, counterfactuals, interventions, mechanism hypotheses.

| Aspect | Definition |
|--------|-----------|
| **Node types** | `CauseNode`, `MediatorNode`, `EffectNode`, `ConfoundNode`, `InterventionNode`, `CounterfactualNode` |
| **Edge types** | `CAUSES`, `MEDIATES`, `CONFOUNDS`, `PREVENTS`, `ENABLES`, `INTERVENES_ON`, `COUNTERFACTUAL_OF` |
| **Algebraic structure** | Directed acyclic graph (DAG) for causal hypotheses; do-calculus composition; intervention transforms the graph via node deletion/fixing |
| **Invariants** | (1) No cycles in the `CAUSES` subgraph. (2) Every causal claim carries evidence_class and confidence ceiling. (3) Counterfactuals are explicitly typed, never silently promoted to actuals. (4) Confound edges must be present or explicitly marked UNKNOWN. |
| **AMOS constraints** | Maps from tensor axis `cause`, `mediator`, `target` of the seed tensor M. Causal bridges require evidence appropriate to causal inference. `CANDIDATE_CAUSE ≠ VERIFIED_CAUSE`. Preserves the causal firewall from TENSORS §10. |

### 3.3 Provenance Graph (G_PROV)

**Purpose:** Source tracking, derivation chains, epistemic lineage, ancestry.

| Aspect | Definition |
|--------|-----------|
| **Node types** | `SourceNode`, `DerivationNode`, `TransformationNode`, `ObservationNode`, `InferenceNode`, `MergeNode` |
| **Edge types** | `DERIVED_FROM`, `TRANSFORMED_BY`, `OBSERVED_AT`, `INFERRED_VIA`, `MERGED_FROM`, `SUPERSEDES`, `RETRACTED` |
| **Algebraic structure** | Free category on derivation morphisms; path composition yields ancestry chains; joins at merge nodes; idempotent retraction |
| **Invariants** | (1) Every derived node has at least one `DERIVED_FROM` edge. (2) Retraction nodes do not delete ancestors — `RETRACTED ≠ ERASED`. (3) Provenance union: `Prov(composed) ⊇ ∪ Prov(inputs)`. (4) Independence annotation on parallel branches. |
| **AMOS constraints** | Provenance-sybil firewall: repeated derivation from the same source ≠ independent confirmation. Preservation under all tensor transformations (TENSORS §7). Implements the audit's "Provenance — ancestry, transformation and correlation topology." |

### 3.4 Authority Graph (G_AUTH)

**Purpose:** Delegation chains, credentials, trust anchors, capability grants, revocations.

| Aspect | Definition |
|--------|-----------|
| **Node types** | `IdentityNode`, `CapabilityNode`, `GrantNode`, `RevocationNode`, `TrustAnchor`, `DelegationNode`, `ScopeNode` |
| **Edge types** | `DELEGATES_TO`, `GRANTS_CAPABILITY`, `REVOKES`, `TRUSTS`, `SCOPE_CONSTRAINS`, `REQUIRES`, `AUTHORIZED_BY` |
| **Algebraic structure** | Partially ordered set (poset) under delegation depth; transitive closure for trust chains; difference for revocation; meet/join for scope intersection/union |
| **Invariants** | (1) No capability may be granted without an authorization source traced to a trust anchor. (2) Revocation is non-monotonic — once revoked, re-grant requires fresh authorization. (3) Delegation depth must be bounded. (4) `CAPABILITY ≠ AUTHORITY` enforced structurally: capability nodes and authority nodes are disjoint types. |
| **AMOS constraints** | Maps to tensor axis `authority` in T_G. Implements the audit's authority axis (Canon → Policy → Control → Effect). Epoch validity on every grant. Capability alone never authorizes — authority_ref must be epoch-valid. |

### 3.5 Temporal Graph (G_TMP)

**Purpose:** Time-indexed states, epoch vectors, causality ordering, event sequencing.

| Aspect | Definition |
|--------|-----------|
| **Node types** | `EventNode`, `StateNode`, `EpochNode`, `IntervalNode`, `SnapshotNode` |
| **Edge types** | `OCCURS_BEFORE`, `OCCURS_AFTER`, `DURING`, `AT_EPOCH`, `TRANSITIONS_TO`, `PRECEDES_CAUALLY`, `SNAPSHOT_OF` |
| **Algebraic structure** | Poset under temporal ordering; interval algebra (Allen's relations); epoch-lattice for parallel time dimensions; product with causal graph |
| **Invariants** | (1) `OCCURS_BEFORE` is transitive and acyclic. (2) Every event is assigned to at least one epoch or interval. (3) State nodes carry a version indicator. (4) Causal ordering is consistent with temporal ordering but not identical: `PRECEDES_CAUALLY ⊆ OCCURS_BEFORE` is not required. |
| **AMOS constraints** | Maps to tensor axis `time`. Preserves distinct time semantics (observation time, event time, validity interval, simulation step) — see TENSORS §14. Cross-graph morphism from G_CAU temporal slice extracts time-indexed causal subgraph. |

### 3.6 Spatial Graph (G_SPA)

**Purpose:** Topological relationships, boundary definitions, shard maps, locality.

| Aspect | Definition |
|--------|-----------|
| **Node types** | `RegionNode`, `ShardNode`, `BoundaryNode`, `LocalityNode`, `AdjacencyNode` |
| **Edge types** | `ADJACENT_TO`, `CONTAINS`, `BOUNDARY_OF`, `SHARD_OF`, `LOCAL_TO`, `CROSS_SHARD`, `TOPOLOGICAL_EQUIV` |
| **Algebraic structure** | Topological space (open sets); lattice of regions under containment; quotient by topological equivalence; product with temporal graph for space-time |
| **Invariants** | (1) Containment is antisymmetric and transitive. (2) Every shard belongs to exactly one shard map. (3) Boundary nodes separate disjoint regions. (4) Cross-shard edges carry a locality annotation. |
| **AMOS constraints** | Maps to tensor axis `scale` and `regime`. Shard-local finalization: no cross-shard commit without explicit cross-shard edge. Supports the audit's H/M/L recursive decomposition. |

### 3.7 Epistemic Graph (G_EPI)

**Purpose:** Knowledge states, confidence levels, uncertainty propagation, belief revision.

| Aspect | Definition |
|--------|-----------|
| **Node types** | `BeliefNode`, `ConfidenceNode`, `UncertaintyNode`, `EvidenceStateNode`, `FalsifierNode` |
| **Edge types** | `SUPPORTS`, `UNDERMINES`, `REQUIRES_CONFIDENCE`, `FALSIFIES`, `UPDATES`, `PROPAGATES_UNCERTAINTY`, `COMPETING_WITH` |
| **Algebraic structure** | Bayesian network structure (DAG with conditional distributions); belief revision operators (AGM-style: contraction, expansion, revision); interval-valued confidence semilattice |
| **Invariants** | (1) Confidence propagation is monotonic only under composition of independent evidence. (2) `COMPETING_WITH` edges must not transitively collapse to a single belief without discriminating evidence. (3) Falsifier edges are non-monotonic: once triggered, downstream beliefs require re-evaluation. (4) UNKNOWN confidence is preserved, never defaulted. |
| **AMOS constraints** | Implements "confidence ≤ weakest load-bearing premise" (TENSORS §38, §62). Maps from G_KN projection retaining evidence_class axis. Preserves SOURCE_CLAIM / OBSERVATION / DERIVED / MODEL / COMPETING / UNKNOWN epistemic classes. |

### 3.8 Intent Graph (G_INT)

**Purpose:** Goals, plans, commitments, task decomposition, rollback points.

| Aspect | Definition |
|--------|-----------|
| **Node types** | `GoalNode`, `PlanNode`, `CommitmentNode`, `TaskNode`, `RollbackPointNode`, `ConstraintNode`, `PreferenceNode` |
| **Edge types** | `SUBGOAL_OF`, `PLAN_FOR`, `DEPENDS_ON`, `CONSTRAINS`, `PREFERRED_OVER`, `ROLLBACK_TO`, `COMMITS_TO`, `SATISFIES`, `BLOCKED_BY` |
| **Algebraic structure** | AND/OR tree for decomposition; priority lattice for preference ordering; product with authority graph for authorized plans; temporal ordering for plan sequencing |
| **Invariants** | (1) Every commitment has a designated rollback point. (2) Plan nodes reference at least one resource node or are marked ABSTRACT. (3) Goal nodes carry a confidence/uncertainty annotation. (4) `PROPOSAL ≠ COMMIT` — plan state must be explicit. |
| **AMOS constraints** | Maps to the cognitive-function axis (Value/Goal → Planning/Decision). Implements the audit's "Goal/Plan Graph — objectives, subgoals, constraints, plans and rollback points." Cross-graph morphism to G_COM binds goals to communication channels; to G_RES binds plans to resource allocations. |

### 3.9 Communication Graph (G_COM)

**Purpose:** Message passing, channel topology, consensus rounds, protocol state.

| Aspect | Definition |
|--------|-----------|
| **Node types** | `AgentNode`, `ChannelNode`, `MessageNode`, `RoundNode`, `ProtocolNode`, `ReceiptNode` |
| **Edge types** | `SENDS_THROUGH`, `RECEIVES_FROM`, `IN_ROUND`, `FOLLOWS_PROTOCOL`, `ACKNOWLEDGES`, `REJECTS`, `BROADCASTS_TO`, `CONSENSUS_WITH` |
| **Algebraic structure** | Bipartite graph (agents ↔ channels); round-indexed snapshots; product with temporal graph for protocol evolution; monoid of message concatenation per channel |
| **Invariants** | (1) Every message has exactly one sender and at least one receiver. (2) Receipt nodes are non-repudiable once committed. (3) Consensus rounds have defined termination or explicit timeout. (4) Channel topology changes are versioned. |
| **AMOS constraints** | Implements the execution axis (Agents → Workflows). Consequential effects require receipts appropriate to the active control-plane contract (AGENTS invariant §9). |

### 3.10 Resource Graph (G_RES)

**Purpose:** Resource allocation, dependency tracking, contention resolution, capacity.

| Aspect | Definition |
|--------|-----------|
| **Node types** | `ResourceNode`, `AllocationNode`, `CapacityNode`, `ContentionNode`, `DependencyNode`, `ConsumptionNode` |
| **Edge types** | `ALLOCATED_TO`, `REQUIRES`, `CONTENDS_WITH`, `DEPENDS_ON`, `CONSUMES`, `RELEASES`, `CAPACITY_OF`, `SHARED_BY` |
| **Algebraic structure** | Resource-algebra (monoid of allocations under composition); contention lattice (join = union of claims, meet = available capacity); dependency DAG |
| **Invariants** | (1) Total allocation ≤ capacity for each resource. (2) Contention nodes must have a resolution strategy or be marked UNRESOLVED. (3) Release edges must reference prior allocation edges. (4) Shared resources carry an exclusivity annotation. |
| **AMOS constraints** | Maps to the execution axis (Kernel primitives → Tools). Cross-graph morphism from G_INT binds plan requirements to resource allocations. Supports H/M/L decomposition for resource hierarchies. |

### 3.11 Identity Graph (G_ID)

**Purpose:** Agent identity, capability registration, role assignments, lifecycle.

| Aspect | Definition |
|--------|-----------|
| **Node types** | `AgentIdentityNode`, `RoleNode`, `CapabilityRegistrationNode`, `LifecycleStateNode`, `CredentialNode` |
| **Edge types** | `HAS_ROLE`, `REGISTERED_CAPABILITY`, `IN_STATE`, `CREDENTIAL_OF`, `SUPERSEDES_IDENTITY`, `DELEGATED_IDENTITY`, `REVOKED_IDENTITY` |
| **Algebraic structure** | Identity poset under supersession; role lattice under inclusion; lifecycle state machine (create → active → suspended → retired); product with authority graph |
| **Invariants** | (1) Every agent identity has exactly one current lifecycle state. (2) Capability registration requires authority graph binding. (3) Revoked identities cannot re-activate without fresh registration. (4) Identity supersession preserves historical lineage. |
| **AMOS constraints** | Implements the audit's "Identity/continuity" P0 gap. Cross-graph morphism to G_AUTH lifts identity→authority. Implements Trang Phan as origin architect and steward; agents must not claim independent authorship (AGENTS invariant §10). |

### 3.12 Evolution Graph (G_EVO)

**Purpose:** Version history, mutation tracking, lineage, supersession, consolidation.

| Aspect | Definition |
|--------|-----------|
| **Node types** | `VersionNode`, `MutationNode`, `SupersessionNode`, `ConsolidationNode`, `RetirementNode`, `RepairNode` |
| **Edge types** | `VERSION_OF`, `MUTATED_FROM`, `SUPERSEDES`, `CONSOLIDATED_INTO`, `RETIRED_BY`, `REPAIRED_BY`, `BRANCHES_FROM`, `MERGES_INTO` |
| **Algebraic structure** | Git-like DAG of versions; partial order under supersession; merge lattice; liveness monoid (retirement is terminal per branch) |
| **Invariants** | (1) Every version node has exactly one `VERSION_OF` edge. (2) Supersession is transitive and acyclic. (3) Retirement is terminal — no outgoing mutation edges from retired nodes. (4) Repair nodes reference the specific defect and the repair provenance. |
| **AMOS constraints** | Implements the lifecycle axis (create → use → revalidate → commit → learn → consolidate → retire → repair). `LATEST ≠ AUTHORITATIVE` (AGENTS invariant). `DOCUMENTED ≠ IMPLEMENTED`. Maps to G_PROV via ancestry embed. Preserves the canonical lineage boundary: v3.0 → v4.4. |

---

## 4. Universal Graph Invariants

These invariants hold across all 12 graph families:

```
INV-1: TYPED NODES
  ∀v ∈ V_G : type(v) ∈ NodeTypes(G)
  "Every node is typed. Untyped nodes are rejected."

INV-2: TYPED EDGES
  ∀e ∈ E_G : type(e) ∈ EdgeTypes(G)
  "Every edge is typed. Untyped edges are rejected."

INV-3: PROVENANCE CARRYING
  ∀G_family : ∃ prov : G_family → P (provenance monoid)
  "Every graph family carries provenance. Transformations preserve it."

INV-4: EPISTEMIC CEILING
  confidence(G_output) ≤ min(confidence(G_inputs))
  "Composition cannot manufacture confidence."

INV-5: UNKNOWN PRESERVATION
  UNKNOWN ≠ FALSE ≠ 0 ≠ ABSENT
  "Missing information is explicitly recorded."

INV-6: SCOPE RESTRICTION
  scope(G_composed) ⊆ ∩ scope(G_inputs)
  "Composition does not silently expand applicability."

INV-7: REGIME RESTRICTION
  regime(G_composed) ⊆ ∩ regime(G_inputs)
  "Composition does not silently cross regimes."

INV-8: MORPHISM TYPEDNESS
  ∀φ : G_A → G_B, φ is typed and annotated LOSSY where non-invertible.

INV-9: NO AUTORORITY ESCALATION
  No node may gain authority by graph position alone.

INV-10: COMPETING PRESERVATION
  Competing hypotheses preserved until discriminating evidence exists.
```

---

## 5. Graph Algebra Summary

Each graph family supports a standard set of algebraic operations, specialized by type:

| Operation | Semantics | Applies To |
|-----------|-----------|-----------|
| **Union** (G₁ ∪ G₂) | Node/edge set union, provenance merged | All families |
| **Intersection** (G₁ ∩ G₂) | Common nodes, edge intersection where both endpoints present | All families |
| **Composition** (G₁ ◦ G₂) | Path-concatenation through shared node types | G_KN, G_CAU, G_PROV, G_TMP |
| **Join** (G₁ ⊔ G₂) | Disjoint union (parallel composition) | All families |
| **Projection** (π_S(G)) | Retain nodes/edges matching type set S | All families; LOSSY annotation required |
| **Selection** (σ_R(G)) | Retain nodes matching predicate R | All families |
| **Quotient** (G/~) | Collapse equivalence classes | G_KN, G_SPA, G_ID |
| **Transpose** (G^T) | Reverse all edge directions | G_CAU, G_PROV, G_TMP |
| **Transitive closure** (G*) | Reflexive-transitive closure | G_KN (ENTAILS), G_TMP (BEFORE) |
| **Difference** (G₁ \ G₂) | Remove G₂'s nodes/edges from G₁ | All families; revocation in G_AUTH |
| **Fixpoint** (μx.G(x)) | Smallest fixed point of graph equation | G_INT (plan expansion), G_EPI (belief revision) |

### Composition guard (universal)

```
Compose(G_A, G_B) is PERMITTED iff:
  1. Shared node types are semantically compatible
  2. Epistemic classes are preserved or explicitly downgraded
  3. Provenance union holds
  4. Scope intersection holds
  5. Regime intersection holds
  6. Bridge type is classified (ANALOGY | ISOMORPHISM | CAUSAL | INFORMATIONAL | STRUCTURAL)
  7. Confidence ceiling is respected
Otherwise: BLOCKED or CONDITIONAL with explicit annotation.
```

---

## 6. Cross-Graph Interaction Matrix

```
         G_KN  G_CAU  G_PROV  G_AUTH  G_TMP  G_SPA  G_EPI  G_INT  G_COM  G_RES  G_ID  G_EVO
G_KN       ·    extr    emb     —      —      —     proj    —      —      —      —      —
G_CAU     —      ·      —      —    slic     —     lift    —      —      —      —      —
G_PROV    —      —       ·     proj    —      —      —      —      —      —    proj   fold
G_AUTH    —      —       —       ·     —      —      —      —      —      —    lift    —
G_TMP     —      —       —      —       ·    prod    —      —    indx    —      —      —
G_SPA     —      —       —      —     prod     ·      —      —      —    map     —      —
G_EPI     —      —       —      —      —      —       ·    goal     —      —      —      —
G_INT     —      —       —      —      —      —       ·      ·    bind    bind   —      —
G_COM     —      —       —      —    indx      —      —      —       ·      —      —      —
G_RES     —      —       —      —      —     map      —    bind     —       ·     —      —
G_ID      —      —       —    lift     —      —      —      —      —      —       ·     —
G_EVO     —      —     emb      —      —      —      —      —      —      —      —       ·
```

Legend: `extr`=extract, `emb`=embed, `proj`=project, `slic`=temporal_slice, `lift`=lift,
`prod`=product, `indx`=round_index, `map`=allocation_map, `goal`=uncertainty_goal,
`bind`=channel/resource_bind, `fold`=version_fold. `—` = no direct morphism defined.

---

## 7. Relationship to Tensor Framework

The 12 graph families interoperate with the 6 tensor contracts (T_R, T_F, T_E, T_C, T_G, T_M):

```
Tensor Contract   Primary Graph Families         Secondary
────────────────  ───────────────────────────    ──────────────────
T_R (Reasoning)   G_KN, G_EPI, G_CAU            G_TMP, G_PROV
T_F (Fractal)     G_SPA, G_EVO                  G_TMP
T_E (Evidence)    G_PROV, G_EPI                 G_KN
T_C (Claim)       G_KN, G_EPI, G_CAU            G_INT, G_AUTH
T_G (Governance)  G_AUTH, G_INT, G_COM          G_ID, G_RES
T_M (Memory)      G_EVO, G_PROV, G_EPI          G_TMP
```

Key invariant from TENSORS §53:
> "Tensor composition is prohibited until shared axes are semantically compatible."

This translates to the graph algebra composition guard (§5): graph composition is
prohibited until shared node/edge types are semantically compatible. Same-name node types
across different graph families do not automatically establish compatibility.

---

## 8. Failure Modes

| Failure Mode | Graph Family | Guard |
|-------------|-------------|-------|
| ORPHAN_NODE | All | Every node must have at least one edge or be a declared root |
| CYCLE_IN_DAG | G_CAU, G_TMP, G_EVO | Acyclicity check on causal/temporal/evolution subgraphs |
| PROVENANCE_LOSS | All | Provenance union invariant (INV-3) |
| CONFIDENCE_INFLATION | G_EPI | Epistemic ceiling invariant (INV-4) |
| AUTHORITY_ESCALATION | G_AUTH | No authority from position (INV-9) |
| SCOPE_LEAK | All via composition | Scope restriction (INV-6) |
| REGIME_DRIFT | All via composition | Regime restriction (INV-7) |
| SILENT_MORPHISM_LOSS | Cross-graph | Mandatory LOSSY annotation on non-invertible morphisms |
| UNKNOWN_PROMOTION | All | UNKNOWN preservation (INV-5) |
| COMPETING_COLLAPSE | G_EPI, G_KN | Competing preservation (INV-10) |
| RETIRED_MUTATION | G_EVO | Retirement terminal invariant |
| CROSS_SHARD_COMMIT | G_SPA | Shard-local finalization without cross-shard edge |
| REVISION_LOOP | G_EPI | Belief revision convergence check |

---

## 9. Promotion-Gate Checklist

Before any graph family is promoted from SPECIFICATION to IMPLEMENTED:

- [ ] Typed node/edge schemas bound and validated
- [ ] Identity and versioning implemented
- [ ] Negative cases covered (missing, malformed, stale, unauthorized)
- [ ] Provenance edges persisted and validated
- [ ] Rollback basin demonstrated for consequential effects
- [ ] At least one cross-graph morphism implemented and tested
- [ ] Composition guard enforced in code
- [ ] Executed validation receipt specific to this graph family
- [ ] Unresolved critical gaps registered as UNKNOWN/GAP (visible)

---

## 10. Epistemic Status

| Layer | Status |
|-------|--------|
| 12 graph families identified | SOURCE_GROUNDED (audit §34–48) |
| Node/edge type enumerations | AMOS_MODEL (derived normalization) |
| Algebraic structures | AMOS_MODEL (derived from standard algebra applied to graph types) |
| Cross-graph morphism registry | AMOS_MODEL (derived; no runtime implementation) |
| Universal invariants | AMOS_MODEL (derived from tensor axioms and audit invariants) |
| Composition guard | AMOS_MODEL (derived from TENSORS §53–68) |
| Implementation binding | UNKNOWN/GAP |
| Executable validation | UNKNOWN/GAP |
| Empirical testing | UNKNOWN/GAP |

---

## 11. Related

- [[11_KNOWLEDGE/TENSORS|TENSORS]] — Typed tensor framework (seed definition)
- [[11_KNOWLEDGE/TENSOR_CONTRACTS|TENSOR_CONTRACTS]] — Six tensor contracts
- [[11_KNOWLEDGE/AMOS_CROSS_DOMAIN_TENSOR_COMPOSITION_GOVERNOR|AMOS_CROSS_DOMAIN_TENSOR_COMPOSITION_GOVERNOR]] — Cross-domain composition rules
- [[00_ROOT/AMOS_OS_ARCHITECTURE_AUDIT_2026-09-04|AMOS_OS_ARCHITECTURE_AUDIT_2026-09-04]] — Source audit identifying 12 graph types
- [[03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION/LINEAGE_GRAPH|LINEAGE_GRAPH]] — Existing lineage graph (control plane)
- [[03_CONTROL_PLANE/09_COMMIT/87_KNOWLEDGE_GRAPH_MODES/KNOWLEDGE_GRAPH_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC|KNOWLEDGE_GRAPH_MODES_COMMIT_CONTROL_PLANE_MODE_FAMILY_SPEC]] — Knowledge graph modes commit spec
- [[11_KNOWLEDGE/KNOWLEDGE_CONTRACT|KNOWLEDGE_CONTRACT]] — Knowledge plane governance
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] — Root navigation

__________________________________________________________________________

RSCF-NODE
node_id: graph_family_specification
node_type: note
path: 11_KNOWLEDGE/GRAPH_FAMILY_SPECIFICATION.md
claim_class: AMOS_MODEL

__________________________________________________________________________

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
