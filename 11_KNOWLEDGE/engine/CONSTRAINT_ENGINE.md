---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Constraint Engine
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

# Constraint Propagation Engine

> [!ABSTRACT] Engine Specification
> Defines the constraint satisfaction and propagation system that enforces hard, soft, temporal, epistemic, resource, causal, governance, authority, and safety constraints across all AMOS operations. Ensures that no operation proceeds unless its constraint closure is satisfiable.

---

## 1. Constraint Taxonomy

| Type | Semantics | Violation Consequence | Enforcement Level |
| :--- | :--- | :--- | :--- |
| **Hard** | Must be satisfied; no compensation possible | Immediate rejection | Kernel-level |
| **Soft** | Preferred; violations trigger trade-off analysis | Degraded scoring | Control-plane |
| **Temporal** | Time-bounded validity; deadlines, TTLs | Staleness quarantine | Runtime |
| **Epistemic** | Knowledge quality bounds; confidence, freshness | Knowledge demotion | Knowledge layer |
| **Resource** | Capacity limits; token budget, memory, compute | Throttling / rejection | Runtime |
| **Causal** | Dependency ordering; happens-before constraints | Dependency violation | Kernel |
| **Governance** | Policy compliance; regulatory, legal, ethical | Policy escalation | Control-plane |
| **Authority** | Permission bounds; who may do what | Authorization rejection | Control-plane |
| **Safety** | Harm prevention; physical, informational, systemic | Immediate halt + quarantine | Kernel |

---

## 2. Constraint Tensor

Every constraint is represented as a structured tensor:

```yaml
constraint_tensor:
  id: "C-2026-09-04-001"
  type: "hard"  # hard | soft | temporal | epistemic | resource | causal | governance | authority | safety
  target: "02_KERNEL/DETERMINISTIC_LOGIC_KERNEL"
  predicate: "M04: SOURCE_CLAIM != VERIFIED"
  scope: "inference_pipeline"
  regime: "always_on"
  priority: 0  # 0 = highest (hard constraints always priority 0)
  authority: "01_CANON/01_CORE_LAWS"
  valid_from: "2026-08-25T00:00:00Z"
  valid_until: null  # null = permanent
  provenance:
    source: "01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS"
    version: "v4.4"
    hash: "sha256:abc123..."
  violation_response: "REJECT_AND_LOG"
  propagation_scope: "full_graph"
```

---

## 3. Admissibility Function

An operation $x$ is admissible if and only if all hard constraints are satisfied and soft constraints are handled through governed trade-off:

$$\text{Admissible}(x) = \bigwedge_{c \in \text{Hard}(C)} c.\text{predicate}(x) \;\wedge\; \text{GovernedSoftTradeoff}(x, \text{Soft}(C))$$

### 3.1 Hard Constraint Evaluation

```text
FOR EACH hard_constraint c IN constraint_set:
    IF NOT c.predicate(operation):
        EMIT constraint_violation:
            constraint_id: c.id
            operation_id: operation.id
            violation_type: HARD
            response: REJECT
        HALT operation
        RETURN False
RETURN True
```

**Critical invariant**: A hard-constraint failure cannot be compensated by a higher optimization score elsewhere. This is absolute and non-negotiable.

### 3.2 Governed Soft Trade-Off

For soft constraints, the engine computes a trade-off score:

$$\text{SoftScore}(x) = \sum_{c \in \text{Soft}(C)} w_c \cdot \text{satisfaction}(c, x)$$

Where $w_c$ are governance-assigned weights. The trade-off is admissible only if:

1. No hard constraint is violated
2. The soft score exceeds the minimum threshold $\theta_{\text{soft}}$
3. The trade-off is approved by the appropriate authority level

---

## 4. Propagation Protocol

When a constraint changes (added, modified, or retracted), propagation follows:

```text
CONSTRAINT CHANGED
        │
        ▼
┌─────────────────────────┐
│ 1. IDENTIFY DEPENDENTS  │  ← Find all operations/statements depending on this constraint
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 2. CHECK PROPAGATION    │  ← Only propagate through dependent edges (M18)
│    SCOPE                │     Do NOT recompute the entire graph
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 3. RE-EVALUATE          │  ← Re-check admissibility for each dependent
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 4. HANDLE VIOLATIONS    │  ← Reject, quarantine, or escalate as appropriate
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 5. LOG PROPAGATION      │  ← Record propagation trace for observability
└─────────────────────────┘
```

### 4.1 Propagation Optimization

- **Incremental propagation**: Only affected dependents are re-evaluated
- **Batched propagation**: Multiple constraint changes within a single epoch are batched
- **Lazy propagation**: Non-critical constraint changes may be deferred to the next epoch boundary
- **Eager propagation**: Hard and safety constraint changes propagate immediately

---

## 5. Constraint Interaction Rules

| Scenario | Rule |
| :--- | :--- |
| **Hard vs Hard conflict** | Escalate to control plane; no automatic resolution |
| **Hard vs Soft conflict** | Hard wins; soft constraint overridden |
| **Soft vs Soft conflict** | Higher-priority soft wins; trade-off logged |
| **Temporal expiry** | Constraint transitions to EXPIRED; dependents re-evaluated |
| **Authority revocation** | All constraints tied to revoked authority are immediately retracted |
| **Scope expansion** | New constraints added; propagation triggered |

---

## 6. Constraint Categories in AMOS

### 6.1 Kernel Constraints (Hard)

- M01–M20 invariants (from `01_CANON/01_CORE_LAWS`)
- Proof trail validity requirements
- Non-monotonic retraction rules

### 6.2 Control-Plane Constraints (Governance)

- Authority grant/revocation bounds
- Policy compliance requirements
- Commit gate conditions

### 6.3 Runtime Constraints (Resource/Temporal)

- Token budget limits
- Execution timeout bounds
- Memory capacity limits
- Causal epoch ordering

### 6.4 Knowledge Constraints (Epistemic)

- Freshness requirements ($\Delta t < \theta_{\text{fresh}}$)
- Confidence ceiling enforcement
- Provenance completeness requirements
- Scope/regime compatibility

### 6.5 Safety Constraints (Safety)

- Irreversibility governance (M20)
- Harm prevention bounds
- Data privacy constraints
- External system interaction limits

---

## 7. Integration Points

| Interface | Direction | Contract |
| :--- | :--- | :--- |
| **01_CANON** | Read | Hard constraint definitions; axioms |
| **02_KERNEL** | Read/Write | Constraint evaluation; proof trail checks |
| **03_CONTROL_PLANE** | Read/Write | Governance constraints; authority constraints |
| **04_RUNTIME** | Read/Write | Resource constraints; temporal constraints |
| **11_KNOWLEDGE** | Read/Write | Epistemic constraints; knowledge quality bounds |
| **17_OBSERVABILITY** | Write | Constraint violation logs; propagation traces |

---

## 8. Failure Modes

| Failure | Detection | Recovery |
| :--- | :--- | :--- |
| **Hard constraint violation not caught** | Post-hoc audit / invariant check | Quarantine affected operation; force full re-evaluation |
| **Propagation incomplete** | Dependency graph integrity check | Re-trigger propagation from changed constraint |
| **Constraint conflict unresolvable** | Timeout on conflict resolution | Escalate to human steward; freeze affected operations |
| **Stale constraint applied** | Temporal validity check | Refresh constraint; re-evaluate dependents |

---

## 9. Cross-Vault References

- [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]]
- [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL|DETERMINISTIC_LOGIC_KERNEL]]
- [[03_CONTROL_PLANE/03_POLICY/03_POLICY_MOC|03_POLICY_MOC]]
- [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]]

---

```RSCF-NODE
node_id: constraint_engine
node_type: engine_specification
domain: 11_KNOWLEDGE/engine
claim_class: AMOS_MODEL
confidence_ceiling:
  hard_constraint_enforcement: high
  soft_constraint_tradeoff: high
  propagation_completeness: high
falsifiers:
  - A hard-constraint violation passes without rejection
  - Propagation fails to reach a dependent that is affected by the change
  - Soft constraint trade-off bypasses authority requirements
```
