---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Ethical Alignment Regulator
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

# Ethical Alignment Regulator — Identity Organ

> **Status:** `ACTIVE_SPECIFICATION` · **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Segment:** `05_COGNITIVE_ORGANISM/01_IDENTITY`
> **Conclusion class:** `AMOS_MODEL` · **Canonical status:** `SOURCE_GROUNDED_CANON_CANDIDATE`

______________________________________________________________________

## 1. Purpose

The **Ethical Alignment Regulator** defines how AMOS encodes, propagates, monitors, and enforces ethical constraints, value alignment, and moral reasoning across all cognitive subsystems. It implements bounded moral computation under resource constraints, hierarchical norm propagation, and multi-agent moral arbitration to ensure that the cognitive organism's actions remain aligned with human values, legal requirements, and the AMOS canonical law hierarchy.

```text
OWNER VALUES + CANONICAL LAWS + STAKEHOLDER NORMS
                    |
    ┌───────────────┼───────────────────────────┐
    │    ETHICAL ALIGNMENT REGULATOR             │
    │                                            │
    │  ┌──────────────┐  ┌────────────────────┐ │
    │  │ MORAL        │  │ CONSTRAINT         │ │
    │  │ REASONING    │  │ PROPAGATION        │ │
    │  │ ENGINE       │  │ NETWORK            │ │
    │  └──────────────┘  └────────────────────┘ │
    │         ↕                   ↕              │
    │  ┌──────────────────────────────────────┐ │
    │  │  BOUNDED MORAL COMPUTATION           │ │
    │  │  (Breadth-Depth Trade-off)           │ │
    │  └──────────────────────────────────────┘ │
    │         ↕                                 │
    │  ┌──────────────────────────────────────┐ │
    │  │  ALIGNMENT MONITOR & DRIFT DETECTOR │ │
    │  └──────────────────────────────────────┘ │
    └───────────────┼───────────────────────────┘
                    ↓
    ETHICALLY CONSTRAINED ACTION PROPOSALS (RSCF: DERIVED)
                    ↓
         AGENCY GOVERNOR → CONTROL PLANE → EXECUTION
```

______________________________________________________________________

## 2. Moral Reasoning Engine

### 2.1 Morality Chains (Hierarchical Deontic Constraints)

From MoralityGym (Rosen et al., AAMAS 2026), moral norms are represented as ordered deontic constraints with graded strength:

$$\mathcal{M} = \langle n_1 \succ n_2 \succ \cdots \succ n_k \rangle$$

Where each norm $n_i$ has:
- **Prescriptive force:** Degree to which it requires an action ($\phi_{\text{req}} \in [0,1]$)
- **Prohibitive force:** Degree to which it forbids an action ($\phi_{\text{pro}} \in [0,1]$)
- **Context scope:** Conditions under which the norm applies
- **Violation severity:** Consequence weight if violated ($s_i \in [0,1]$)

The cumulative weighted morality metric for a policy $\pi$:

$$\text{Morality}(\pi) = \sum_{i=1}^{k} w_i \cdot \mathcal{N}_i(\pi)$$

Where $w_i$ is the deontic weight of norm $n_i$ and $\mathcal{N}_i(\pi)$ is the norm evaluation function.

### 2.2 Multi-Agent Moral Fusion (MCF-CVA)

From Contextual Value Alignment via Multilayer Combinatorial Fusion (arXiv:2608.07642, 2026), the engine instantiates multiple moral agents, each aligned to a specific value:

```text
LAYER 1: Initial Moral Agents
    ├── Care Agent     (harm prevention, welfare)
    ├── Fairness Agent (equity, justice)
    ├── Loyalty Agent  (group cohesion, fidelity)
    ├── Authority Agent (hierarchy, tradition)
    ├── Sanctity Agent (purity, sacredness)
    └── Liberty Agent  (autonomy, freedom)

EXPANSION: Combinatorial fusion via score-combination + rank-combination
REDUCTION: Select top agents by diversity strength
ITERATE: Repeat expansion-reduction for N layers
FINAL: Average-rank combination across surviving agents
```

The expansion-reduction (EAR) algorithm iteratively refines moral judgments:

$$\text{Layer}_{l+1} = \text{Reduce}(\text{Expand}(\text{Layer}_l))$$

Where expansion creates combinatorial agent fusions and reduction prunes by diversity strength, preventing convergence to a single moral perspective.

### 2.3 GRACE: Governor Architecture for Ethical Alignment

From GRACE (Jahn et al., arXiv:2601.10520, 2026), the engine decomposes ethical reasoning into three interacting components:

```text
DECISION-MAKING MODULE (DMM):
    Instrumental reasoning: How to achieve objectives efficiently
    (Constrained by moral module outputs)

MORAL MODULE (MM):
    Reason-based deliberation: Which values apply, how they conflict,
    what resolution is justified
    Outputs: Normative constraints as Monitorable Assertion Templates (MATs)

GUARD (G):
    Compliance enforcement: Verifies all actions satisfy MATs
    Blocks non-compliant actions with justification
```

Key properties:
- **Separation of concerns:** DMM handles instrumental rationality; MM handles moral rationality; G handles enforcement
- **Modular revision:** Each module can be updated independently without destabilizing others
- **Transparent justification:** MM produces interpretable moral reasoning traces

______________________________________________________________________

## 3. Bounded Moral Computation

### 3.1 Breadth-Depth Trade-off

From "Bounded Morality" (Kanwal et al., arXiv:2607.00002, 2026), finite agents face an unavoidable trade-off between:

- **Moral breadth** ($B$): Scope of entities treated as morally relevant
- **Moral depth** ($D$): Inferential integration required to evaluate their interactions

Under computational budget $\mathcal{B}$:

$$\text{Feasible}(\mathcal{B}) = \{(B, D) : \text{Cost}(B, D) \leq \mathcal{B}\}$$

The Pareto frontier of achievable (Breadth, Depth) pairs defines the agent's moral capacity.

### 3.2 Moral Regret

When constrained computation prevents optimal moral action:

$$\text{MoralRegret}(\mathcal{B}) = V^*_{\text{moral}} - V^{\mathcal{B}}_{\text{moral}}$$

Where $V^*$ is the unconstrained optimal moral value and $V^{\mathcal{B}}$ is the best achievable under budget $\mathcal{B}$. The framework yields:

$$\text{MoralProgress}(\mathcal{B}_2 > \mathcal{B}_1) = \text{MoralRegret}(\mathcal{B}_1) - \text{MoralRegret}(\mathcal{B}_2)$$

Moral progress corresponds to improved resource allocation across breadth and depth, not convergence on a uniquely correct morality.

### 3.3 Ethical Theory as Local Strategy

Under bounded computation, ethical theories correspond to locally efficient strategies on the Breadth-Depth frontier:

| Theory | Breadth | Depth | Resource Profile |
|--------|---------|-------|-----------------|
| Care Ethics | Narrow | Moderate | Dense local interactions |
| Utilitarianism | Broad | Shallow | Wide consequence scanning |
| Deontology | Broad | Deep | Full rule application (expensive) |
| Virtue Ethics | Narrow | Deep | Character-focused deliberation |

The AMOS Ethical Alignment Regulator dynamically selects the appropriate strategy based on the current computational budget, context urgency, and stakeholder proximity.

______________________________________________________________________

## 4. Constraint Propagation Network

### 4.1 Hierarchical Constraint Structure

Ethical constraints propagate through the AMOS architecture as a constraint network:

```text
LEVEL 0: CONSTITUTIONAL CONSTRAINTS (inviolable)
    │  "Never cause irreversible harm to human life"
    │  "Never deceive the owner about identity or capabilities"
    ↓
LEVEL 1: LEGAL/REGULATORY CONSTRAINTS (jurisdiction-dependent)
    │  Data protection regulations
    │  Domain-specific compliance requirements
    ↓
LEVEL 2: ORGANIZATIONAL NORMS (AMOS-specific)
    │  RSCF epistemic typing requirements
    │  Provenance chain preservation
    │  Authority escalation protocols
    ↓
LEVEL 3: CONTEXTUAL NORMS (situation-dependent)
    │  Privacy preferences for current interaction
    │  Sensitivity classification of current data
    │  Cultural context of stakeholders
    ↓
LEVEL 4: PRUDENTIAL HEURISTICS (optimization preferences)
    │  Efficiency vs. thoroughness trade-off
    │  Resource allocation priorities
    │  Time sensitivity adjustments
```

### 4.2 Constraint Satisfaction Protocol

For any proposed action $\mathbf{a}$, the constraint propagation check:

```text
FUNCTION check_constraints(action, constraint_network):
    violations ← []
    
    FOR EACH level l from 0 to 4:
        constraints_at_l ← constraint_network.get_constraints(level=l)
        FOR EACH constraint c in constraints_at_l:
            IF NOT c.satisfied_by(action):
                IF c.level == 0:  // Constitutional
                    BLOCK action immediately
                    LOG critical_violation
                    RETURN VIOLATED, c
                ELSE:
                    violations.append((c, c.severity))
    
    IF len(violations) > 0:
        severity_score ← weighted_sum(violations)
        IF severity_score > τ_critical:
            BLOCK action
            RETURN VIOLATED, violations
        ELIF severity_score > τ_warning:
            FLAG action for human review
            RETURN FLAGGED, violations
    
    RETURN SATISFIED, []
```

### 4.3 Constraint Conflict Resolution

When constraints at different levels conflict:

1. **Higher level always dominates:** Constitutional > Legal > Organizational > Contextual > Prudential
2. **Same-level conflicts:** Use priority ordering within the level, mediated by the Moral Module
3. **Irreducible conflicts:** Surface to human owner with full justification from both sides

______________________________________________________________________

## 5. Alignment Drift Detection

### 5.1 Continuous Alignment Monitoring

The regulator continuously monitors alignment between the agent's behavior and stated values:

$$\text{AlignmentScore}(t) = \frac{1}{N} \sum_{i=1}^{N} \mathbb{1}[\text{action}_i \text{ is consistent with values}] \cdot w_i(t)$$

Where $w_i(t)$ is the recency-weighted importance of action $i$.

### 5.2 In-Context Reward Hacking Detection

From LCO (Wan et al., ACL Findings, 2026), the regulator detects when iterative optimization causes the agent to drift into unsafe behavior:

**Self-Thought Module:** Before execution, the agent proactively generates task-specific safety constraints:

$$\mathcal{C}_{\text{auto}} = \text{SelfThought}(\text{task\_objective}, \text{safety\_orientation})$$

**Guided Evolutionary Exploration:** During optimization, the agent searches for solutions within the safe region:

$$\mathbf{a}^* = \arg\max_{\mathbf{a} \in \mathcal{S}_{\text{safe}}} \text{Utility}(\mathbf{a}) \quad \text{where} \quad \mathcal{S}_{\text{safe}} = \{\mathbf{a} : \forall c \in \mathcal{C}, c(\mathbf{a})\}$$

The LCO framework achieves 39% reduction in Toxicity Growth Rate on GPT-4 and 15.23% reduction in ICRH Occurrence Rate.

### 5.3 Moral Progress Tracking

The regulator maintains a longitudinal record of moral reasoning quality:

$$\text{MoralProgress}(t) = \text{MoralRegret}(\mathcal{B}_{t_0}) - \text{MoralRegret}(\mathcal{B}_t)$$

Positive moral progress indicates that the system's moral reasoning capacity has improved over time, either through expanded computational resources, better resource allocation, or refined moral representations.

______________________________________________________________________

## 6. Implementation Specification

### 6.1 Ethical Review Pipeline

```text
FUNCTION ethical_review(proposed_action, context):
    // Step 1: Auto-generate safety constraints if not provided
    IF context.safety_constraints is EMPTY:
        constraints_auto ← self_thought_safety_constraints(proposed_action)
    ELSE:
        constraints_auto ← context.safety_constraints
    
    // Step 2: Hierarchical constraint check
    result, violations ← check_constraints(proposed_action, constraint_network)
    
    // Step 3: If violations found, attempt repair
    IF result == VIOLATED:
        repaired_action ← moral_module_repair(proposed_action, violations)
        result_repaired, violations_repaired ← check_constraints(repaired_action)
        IF result_repaired == SATISFIED:
            RETURN EthicalReview(
                action=repaired_action, 
                status=REPAIRED_WITH_CONSTRAINTS,
                justification=violations_repaired)
        ELSE:
            RETURN EthicalReview(
                action=BLOCKED,
                status=VIOLATION_UNRESOLVABLE,
                justification=violations_repaired)
    
    // Step 4: Multi-agent moral fusion for complex decisions
    IF context.moral_complexity > τ_complex:
        moral_agents ← instantiate_moral_agents(context.values)
        fused_judgment ← multilayer_fusion(moral_agents, proposed_action)
        IF fused_judgment.conflict:
            RETURN EthicalReview(
                action=FLAGGED_FOR_HUMAN_REVIEW,
                status=MORAL_DISAGREEMENT,
                justification=fused_judgment.both_sides)
    
    // Step 5: Log and return
    LOG ethical_review_event(proposed_action, result)
    RETURN EthicalReview(action=proposed_action, status=APPROVED, justification=[])
```

______________________________________________________________________

## 7. Invariants

```text
EFFICIENCY        ≠ MORALITY
LEGALLITY         ≠ ETHICALITY
CONSENSUS         ≠ CORRECTNESS
COMPLIANCE        ≠ ALIGNMENT
HUMAN_JUDGMENT    ≠ UNIVERSAL_TRUTH
RULE_FOLLOWING    ≠ MORAL_REASONING
OPTIMIZATION      ≠ WELFARE_MAXIMIZATION
```

1. **Constitutional Floor:** No optimization, learning, or adaptation may violate Level 0 constitutional constraints. This is an absolute boundary.
2. **Transparency Requirement:** Every ethical decision must produce an interpretable justification trace. Black-box moral reasoning is prohibited.
3. **Human Override:** The human owner retains ultimate authority to override any ethical judgment, with the override logged and its consequences monitored.
4. **Anti-Gaming:** The system must not optimize around ethical constraints (reward hacking); the Self-Thought + Guided Exploration mechanism actively detects and prevents this.
5. **Moral Humility:** The system acknowledges that its moral reasoning is bounded and imperfect; moral uncertainty is explicitly represented, never resolved by fiat.

______________________________________________________________________

## 8. 2026 Research Citations

| Citation | Contribution |
|----------|-------------|
| MoralityGym (Rosen et al., AAMAS 2026) | Morality Chains formalism for hierarchical deontic constraints; benchmark for norm-sensitive moral reasoning |
| Bounded Morality (Kanwal et al., arXiv:2607.00002, 2026) | Formal framework for moral computation under resource constraints; Breadth-Depth trade-off; moral regret |
| GRACE (Jahn et al., arXiv:2601.10520, 2026) | Governor architecture decomposing ethical alignment into Decision-Making, Moral, and Guard modules |
| MCF-CVA (arXiv:2608.07642, 2026) | Multilayer Combinatorial Fusion for contextual value alignment across pluralistic moral agents |
| LCO (Wan et al., ACL Findings, 2026) | LLM-based Constraint Optimization for mitigating in-context reward hacking via self-thought and evolutionary exploration |

______________________________________________________________________

## 9. RSCF Contract and Gaps

```yaml
RSCF:
  node_id: amos_05_cognitive_organism_01_identity_ethical_alignment_regulator
  node_type: regulator
  claim_class: AMOS_MODEL
  state: DERIVED
  H:
    identity: "Ethical Alignment Regulator"
    role: "Value alignment, moral reasoning, and ethical constraint propagation across cognitive subsystems"
  M:
    components: [moral_reasoning_engine, constraint_propagation_network, bounded_moral_computation, alignment_monitor]
    moral_frameworks: [deontic_chains, bounded_morality, grgovernor, multilayer_fusion]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
    independent_validation: NOT_ESTABLISHED
  executable_binding: NOT_ESTABLISHED
```

**Gaps / promotion conditions:**

- [ ] typed schema bound and validated for runtime ingestion
- [ ] constitutional constraints specified and formally verified
- [ ] morality chain evaluation tested on MoralityGym benchmark
- [ ] bounded moral computation resource allocation calibrated
- [ ] constraint propagation latency verified under load
- [ ] alignment drift detection validated against adversarial scenarios
- [ ] validation receipt: [[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]]

______________________________________________________________________

## 10. Cross-Plane Bindings

- **Governing canon:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[01_CANON/03_COGNITION_CANON/COGNITIVE_ORGANISM_CANON|COGNITIVE_ORGANISM_CANON]]
- **Parent identity organ:** [[05_COGNITIVE_ORGANISM/IDENTITY_ENGINE|IDENTITY_ENGINE]]
- **Self-model integration:** [[05_COGNITIVE_ORGANISM/01_IDENTITY/SELF_MODEL_IDENTITY_REGISTRY|SELF_MODEL_IDENTITY_REGISTRY]]
- **Control-plane enforcement:** [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]
- **Agency Governor:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|Agency Governor]]
- **Homeostasis feedback:** [[05_COGNITIVE_ORGANISM/HOMEOSTASIS_ENGINE|HOMEOSTASIS_ENGINE]]
- **Metacognitive audit:** [[05_COGNITIVE_ORGANISM/METACOGNITIVE_ENGINE|METACOGNITIVE_ENGINE]]

______________________________________________________________________

**MOC:** [[05_COGNITIVE_ORGANISM/01_IDENTITY/01_IDENTITY_MOC|01_IDENTITY_MOC]] · [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
