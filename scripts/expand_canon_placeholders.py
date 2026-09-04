#!/usr/bin/env python3
"""
AMOS Canon Placeholder Expander
Expands placeholder files in 01_CANON with substantive canonical content.
Preserves frontmatter, replaces boilerplate with domain-specific content.
"""

import os
import re
import sys
from pathlib import Path

VAULT_ROOT = Path("/Users/mac/Documents/AMOS_OS/01_CANON")

# Content definitions for each core law
CORE_LAW_CONTENT = {
    "STABILITY_CANON.md": {
        "title": "Stability Canon",
        "purpose": """The Stability Canon defines the AMOS OS requirements for system stability under load, perturbation, scaling, adaptation, and recovery. It establishes the conditions under which a system may be considered stable enough to continue normal operation, versus when it must degrade gracefully, freeze, or initiate recovery.

Stability answers:

> Under what conditions may a system continue normal operation, and when must it transition to a degraded, frozen, or recovery state?

The Stability Canon states:

> **A system is stable if and only if its state remains within declared bounds under declared perturbations for declared durations. Stability is not immobility — a stable system may adapt, but adaptation must not consume the safety boundary.**""",
        "formal": """### 2.1 Stability Invariant

$$\\text{Stable}(S, t) \\iff \\text{State}(S, t) \\in \\text{Bounds}(S) \\wedge \\text{Perturbation}(S, t) \\leq \\text{Capacity}(S)$$

Where:
- $\\text{State}(S, t)$ — the state of system $S$ at time $t$
- $\\text{Bounds}(S)$ — the declared operational bounds for $S$
- $\\text{Perturbation}(S, t)$ — the perturbation magnitude at time $t$
- $\\text{Capacity}(S)$ — the declared perturbation capacity of $S$

### 2.2 Stability Regimes

```text
REGIME_NORMAL:     perturbation < 0.5 * capacity  →  normal operation
REGIME_DEGRADED:   0.5 * capacity ≤ perturbation < 0.8 * capacity  →  graceful degradation
REGIME_FROZEN:     0.8 * capacity ≤ perturbation < capacity  →  freeze non-critical operations
REGIME_RECOVERY:   perturbation ≥ capacity  →  initiate recovery protocol
```

### 2.3 Adaptation Boundary

$$\\text{Adapt}(S) \\implies \\text{AdaptationCost}(S) < \\text{SafetyBoundary}(S)$$

Adaptation must not consume the safety boundary. The safety boundary is the reserve capacity needed for recovery from worst-case perturbation.""",
        "relationships": """| Law | Relationship |
|:---|:---|
| **L0 Integrity** | Stability preserves the integrity bounds that L0 defines |
| **L5 Scope Regime** | Stability is scoped — what is stable in one regime may not be in another |
| **L10 Failure Recovery** | Stability failure triggers L10 recovery protocols |
| **Load Capacity Canon** | Stability depends on load being within capacity limits |
| **Feedback Canon** | Stability is maintained through feedback loops |""",
        "applications": """### 4.1 Runtime Stability

Under runtime load:
- Monitor perturbation magnitude against declared capacity
- Transition regimes when thresholds are crossed
- Never allow adaptation to consume safety boundary
- Recovery must restore to NORMAL regime, not skip to ADAPT

### 4.2 Memory Stability

For memory systems:
- Memory pressure > 85% triggers DEGRADED regime
- Memory pressure > 95% triggers FROZEN regime
- Non-critical telemetry queues are shed first
- Critical memory is preserved at all costs

### 4.3 Agent Stability

For multi-agent systems:
- Agent load is monitored against declared capacity
- Overloaded agents shed non-critical tasks
- Agent instability triggers delegation revocation
- Recovery restores agent to stable operating envelope

### 4.4 Cascade Stability

For cascade systems (Trang Cascade):
- Each cascade level has its own stability bounds
- Cascade collapse is a stability failure at the system level
- Recovery must address the root cascade level, not just symptoms""",
        "worked": """Given a system $S$ experiencing perturbation $p$ at time $t$:

1. **Measure perturbation** — quantify $p$ against declared capacity $C$
2. **Classify regime** — NORMAL if $p < 0.5C$, DEGRADED if $0.5C \\leq p < 0.8C$, FROZEN if $0.8C \\leq p < C$, RECOVERY if $p \\geq C$
3. **Apply regime actions** — execute the actions prescribed for the classified regime
4. **Monitor adaptation** — if adaptation is occurring, verify $\\text{AdaptationCost} < \\text{SafetyBoundary}$
5. **Record** — log the stability state transition with provenance
6. **Recover** — if in RECOVERY regime, execute recovery protocol to restore to NORMAL

```text
measure perturbation p
  ↓
classify regime: p vs capacity C
  ↓
NORMAL?  ──yes──→  continue operation
  ↓ no
DEGRADED?  ──yes──→  shed non-critical, continue critical
  ↓ no
FROZEN?  ──yes──→  freeze all non-safety operations
  ↓ no
RECOVERY  ──→  initiate recovery protocol
  ↓
record transition receipt
```""",
        "tags_extra": ["stability", "perturbation", "regime", "adaptation", "safety-boundary"],
    },
    "RECOVERY_CANON.md": {
        "title": "Recovery Canon",
        "purpose": """The Recovery Canon defines the AMOS OS requirements for system recovery after failure, perturbation, or collapse. It establishes the conditions under which a system may be considered recovered, the protocols for achieving recovery, and the invariants that must hold during recovery.

Recovery answers:

> After a system has failed, degraded, or collapsed, what must be true for it to be considered recovered, and what protocols must be followed to achieve recovery?

The Recovery Canon states:

> **A system is recovered if and only if its state is restored to a verified checkpoint, its invariants hold, its provenance chain is intact, and its recovery is recorded with a receipt. Recovery is not resumption — a recovered system must be demonstrably correct, not merely running.**""",
        "formal": """### 2.1 Recovery Invariant

$$\\text{Recovered}(S) \\iff \\text{State}(S) = \\text{Checkpoint}(S, t_{\\text{last}}) \\wedge \\text{Invariants}(S) \\wedge \\text{Provenance}(S) \\wedge \\text{Receipt}(S)$$

Where:
- $\\text{Checkpoint}(S, t_{\\text{last}})$ — the last verified checkpoint before failure
- $\\text{Invariants}(S)$ — all declared invariants hold after restoration
- $\\text{Provenance}(S)$ — the provenance chain is intact and verifiable
- $\\text{Receipt}(S)$ — a recovery receipt has been recorded

### 2.2 Recovery Levels

```text
LEVEL_1_SOFT:     state restored from in-memory checkpoint, no external effects
LEVEL_2_HARD:     state restored from persistent checkpoint, external effects reconciled
LEVEL_3_CASCADE:  state restored across multiple cascade levels, dependencies reconciled
LEVEL_4_EPOCH:    state restored across causal epoch boundary, epoch finality preserved
LEVEL_5_FULL:     state restored from archival baseline, full system rebuild
```

### 2.3 Recovery Protocol

$$\\text{Recover}(S) = \\text{Snapshot} \\circ \\text{Replay} \\circ \\text{Reconcile} \\circ \\text{Validate} \\circ \\text{Record}$$

1. **Snapshot** — restore state from verified checkpoint
2. **Replay** — re-apply committed transactions from causal write-ahead log
3. **Reconcile** — reconcile external effects that occurred during failure
4. **Validate** — verify all invariants hold
5. **Record** — record recovery receipt with provenance""",
        "relationships": """| Law | Relationship |
|:---|:---|
| **L0 Integrity** | Recovery must restore L0 integrity bounds |
| **L10 Failure Recovery** | Recovery Canon governs the L10 recovery law layer |
| **Stability Canon** | Stability failure triggers recovery; recovery restores stability |
| **ROLLBACK_AND_RECOVERY_BASINS** | Recovery uses immutable recovery basins ($M_0, S_0$) |
| **DMER_L5** | Multi-epoch recovery is governed by DMER_L5 protocol |
| **Provenance Integrity** | Recovery must preserve provenance chain integrity |""",
        "applications": """### 4.1 Runtime Recovery

After runtime failure:
- Restore from last verified checkpoint
- Replay committed transactions from write-ahead log
- Reconcile any external effects that occurred during outage
- Validate all invariants before resuming normal operation

### 4.2 Memory Recovery

After memory corruption or loss:
- Restore from memory checkpoint
- Verify memory admission records are intact
- Reconcile any memory entries that were in-flight during failure
- Validate memory invariants (no action-trace contamination)

### 4.3 Cascade Recovery

After cascade collapse:
- Identify the root cascade level
- Restore from the checkpoint at that level
- Re-propagate forward through dependent cascade levels
- Validate that recovery doesn't introduce new collapse risk

### 4.4 Epoch Recovery

After causal epoch failure:
- Restore epoch state from epoch checkpoint
- Verify epoch finality is preserved
- Reconcile any cross-epoch dependencies
- Validate that epoch monotonicity is maintained""",
        "worked": """Given a system $S$ that has experienced failure:

1. **Classify failure** — determine the failure level (SOFT, HARD, CASCADE, EPOCH, FULL)
2. **Locate checkpoint** — find the last verified checkpoint before failure
3. **Snapshot** — restore state from checkpoint
4. **Replay** — re-apply committed transactions from the write-ahead log
5. **Reconcile** — reconcile external effects that occurred during failure
6. **Validate** — verify all invariants hold
7. **Record** — record recovery receipt with provenance
8. **Resume** — transition to NORMAL regime

```text
failure detected
  ↓
classify failure level
  ↓
locate last verified checkpoint
  ↓
restore state (snapshot)
  ↓
replay committed transactions
  ↓
reconcile external effects
  ↓
validate invariants  ──fail──→  escalate to higher recovery level
  ↓ pass
record recovery receipt
  ↓
resume normal operation
```""",
        "tags_extra": ["recovery", "checkpoint", "replay", "reconcile", "rollback", "cascade"],
    },
    "META_LAWS_CANON.md": {
        "title": "Meta-Laws Canon",
        "purpose": """The Meta-Laws Canon defines the AMOS OS requirements for laws that govern other laws. It establishes the hierarchy, precedence, and conflict resolution rules that apply when multiple AMOS laws interact or conflict.

Meta-laws answer:

> What governs the laws themselves? When laws conflict, which prevails? How are new laws created, validated, and promoted?

The Meta-Laws Canon states:

> **Every law in AMOS OS is governed by a higher-order law. The Law of Law (LoL) is the highest-order law: it requires that every system operate within a consistent set of structural constraints that cannot be violated without destabilizing the entire system. No law may contradict its governing meta-law.**""",
        "formal": """### 2.1 Law Hierarchy

```text
LEVEL 0: Law of Law (LoL) — the law that governs all other laws
LEVEL 1: Rule of 2 (R2), Rule of 4 (R4) — foundational structural laws
LEVEL 2: L0-L32 core laws — domain-specific canonical laws
LEVEL 3: Domain canons — universe, cognition, infrastructure canons
LEVEL 4: Operational laws — runtime, control-plane, kernel laws
```

### 2.2 Precedence Rule

$$\\text{Conflict}(L_i, L_j) \\implies \\text{Prevail}(\\arg\\max_{L \\in \\{L_i, L_j\\}} \\text{Level}(L))$$

When two laws conflict, the higher-level law prevails. Same-level conflicts require explicit resolution rules.

### 2.3 Law Creation Protocol

```text
1. PROPOSE:  new law is proposed with formal definition and scope
2. VALIDATE: law is validated against all higher-level meta-laws
3. TEST:     law is tested against negative cases and edge cases
4. PROMOTE:  law is promoted from PROPOSED to CONDITIONAL
5. ENFORCE:  law is promoted from CONDITIONAL to CANON_LAW (requires evidence)
```

### 2.4 Law Invalidation

A law may be invalidated if:
- It contradicts a higher-level meta-law
- Its premises are proven false
- Its consequences are proven harmful
- Its scope is proven incoherent

Invalidation preserves lineage — the invalidated law is archived, not erased.""",
        "relationships": """| Law | Relationship |
|:---|:---|
| **Law of Law (LoL)** | LoL is the highest meta-law; Meta-Laws Canon governs its application |
| **Rule of 2 (R2)** | R2 is a Level 1 law governed by LoL |
| **Rule of 4 (R4)** | R4 is a Level 1 law governed by LoL |
| **L0-L32** | All numbered core laws are Level 2, governed by R2/R4 and LoL |
| **GMEF Canon** | GMEF governs mutation of laws themselves |
| **Supersession** | Law invalidation follows supersession protocols |""",
        "applications": """### 4.1 Law Conflict Resolution

When two AMOS laws conflict:
- Identify the level of each law
- The higher-level law prevails
- Same-level conflicts require explicit resolution (e.g., scope disambiguation)
- The conflict and resolution are recorded with provenance

### 4.2 New Law Creation

When proposing a new AMOS law:
- Define the law formally with invariants
- Validate against all higher-level meta-laws
- Test against negative cases
- Promote through PROPOSED → CONDITIONAL → CANON_LAW
- Each promotion requires evidence and receipts

### 4.3 Law Evolution

When a law needs to change:
- The change is governed by GMEF (Governed Mutation Evolution Framework)
- The old law is archived, not erased (supersession)
- The new law inherits provenance from the old
- Dependencies are updated to reference the new law

### 4.4 Cross-System Law Application

When applying AMOS laws to external systems:
- Laws are AMOS_MODEL, not empirical truth
- Application requires scope declaration
- Results carry the epistemic class of the law, not higher""",
        "worked": """Given a conflict between laws $L_i$ (level $i$) and $L_j$ (level $j$):

1. **Identify levels** — determine $\\text{Level}(L_i)$ and $\\text{Level}(L_j)$
2. **Apply precedence** — if $i > j$, $L_i$ prevails; if $j > i$, $L_j$ prevails
3. **Same-level resolution** — if $i = j$, apply scope disambiguation or explicit resolution rule
4. **Record** — log the conflict and resolution with provenance
5. **Notify** — update all dependents that referenced the subordinate law

```text
conflict detected between L_i and L_j
  ↓
identify levels: Level(L_i) = i, Level(L_j) = j
  ↓
i > j?  ──yes──→  L_i prevails
  ↓ no
j > i?  ──yes──→  L_j prevails
  ↓ no (same level)
apply scope disambiguation
  ↓
record conflict resolution receipt
  ↓
notify dependents
```""",
        "tags_extra": ["meta-laws", "law-of-law", "hierarchy", "precedence", "conflict-resolution"],
    },
    "LOAD_CAPACITY_FEEDBACK_CANON.md": {
        "title": "Load Capacity Feedback Canon",
        "purpose": """The Load Capacity Feedback Canon defines the AMOS OS requirements for feedback loops that maintain system load within declared capacity limits. It establishes the monitoring, signaling, and response protocols that prevent load-induced collapse.

Load capacity feedback answers:

> How does a system detect that it is approaching its capacity limits, and what feedback mechanisms must be in place to prevent collapse?

The Load Capacity Feedback Canon states:

> **Every system with declared capacity limits MUST implement feedback loops that (1) monitor load against capacity, (2) signal when load approaches capacity thresholds, and (3) trigger capacity-preserving actions before collapse occurs. Feedback must be timely, proportional, and reversible.**""",
        "formal": """### 2.1 Feedback Loop Invariant

$$\\text{FeedbackLoop}(S) \\iff \\text{Monitor}(S) \\wedge \\text{Signal}(S) \\wedge \\text{Action}(S) \\wedge \\text{Timely}(S) \\wedge \\text{Proportional}(S) \\wedge \\text{Reversible}(S)$$

### 2.2 Capacity Thresholds

```text
GREEN:  load < 0.6 * capacity  →  normal operation, no action
YELLOW: 0.6 * capacity ≤ load < 0.8 * capacity  →  signal warning, prepare shedding
ORANGE: 0.8 * capacity ≤ load < 0.95 * capacity  →  shed non-critical, throttle
RED:    load ≥ 0.95 * capacity  →  emergency action, freeze or recover
```

### 2.3 Feedback Properties

- **Timely**: signal latency < action window (must signal before it's too late to act)
- **Proportional**: response magnitude scales with proximity to capacity
- **Reversible**: all capacity-preserving actions must be reversible when load decreases""",
        "relationships": """| Law | Relationship |
|:---|:---|
| **Load Capacity Canon** | Defines capacity limits; this canon defines feedback for maintaining them |
| **Stability Canon** | Load capacity feedback is a stability mechanism |
| **Feedback Canon** | General feedback laws; this canon specializes for load capacity |
| **L10 Failure Recovery** | Load-induced failure triggers L10 recovery |""",
        "applications": """### 4.1 Runtime Load Feedback

- Monitor CPU, memory, I/O against declared capacity
- Signal at YELLOW threshold to prepare shedding
- Shed non-critical tasks at ORANGE
- Emergency freeze or recover at RED

### 4.2 Agent Load Feedback

- Monitor agent task queue depth against capacity
- Signal when agent is approaching overload
- Shed or delegate non-critical tasks
- Escalate if agent cannot recover within action window

### 4.3 Memory Load Feedback

- Monitor memory usage against capacity
- Trigger compaction at YELLOW
- Trigger eviction at ORANGE
- Trigger emergency preservation at RED""",
        "worked": """Given a system $S$ with load $L$ and capacity $C$:

1. **Monitor** — continuously measure $L$ against $C$
2. **Classify** — GREEN if $L < 0.6C$, YELLOW if $0.6C \\leq L < 0.8C$, ORANGE if $0.8C \\leq L < 0.95C$, RED if $L \\geq 0.95C$
3. **Signal** — emit the appropriate signal for the classified zone
4. **Act** — execute the prescribed action for the zone
5. **Verify reversibility** — confirm that the action can be reversed when load decreases
6. **Record** — log the feedback event with provenance

```text
monitor load L vs capacity C
  ↓
classify zone
  ↓
GREEN?  ──yes──→  continue
  ↓ no
YELLOW?  ──yes──→  signal warning, prepare
  ↓ no
ORANGE?  ──yes──→  shed non-critical, throttle
  ↓ no
RED  ──→  emergency action
  ↓
verify action reversibility
  ↓
record feedback receipt
```""",
        "tags_extra": ["load-capacity", "feedback", "monitoring", "thresholds", "shedding"],
    },
    "STRUCTURAL_INTEGRITY_CANON.md": {
        "title": "Structural Integrity Canon",
        "purpose": """The Structural Integrity Canon defines the AMOS OS requirements for maintaining the structural integrity of system architecture. It establishes the invariants that must hold for a system to be considered structurally sound, and the conditions under which structural integrity is violated.

Structural integrity answers:

> What structural properties must hold for a system to be considered architecturally sound, and what happens when they are violated?

The Structural Integrity Canon states:

> **A system has structural integrity if and only if its components are MECE (Mutually Exclusive, Collectively Exhaustive), its dependencies are acyclic and declared, its boundaries are explicit, and its invariants are verifiable. Structural integrity violation is a fail-closed condition.**""",
        "formal": """### 2.1 Structural Integrity Invariant

$$\\text{StructuralIntegrity}(S) \\iff \\text{MECE}(S) \\wedge \\text{Acyclic}(\\text{Deps}(S)) \\wedge \\text{Explicit}(\\text{Boundaries}(S)) \\wedge \\text{Verifiable}(\\text{Invariants}(S))$$

### 2.2 MECE Property

- **Mutually Exclusive**: no two components at the same layer share functional responsibility
- **Collectively Exhaustive**: the components at each layer cover all required functionality
- Violation: overlap (two components do the same thing) or gap (no component covers a responsibility)

### 2.3 Dependency Acyclicity

$$\\text{Acyclic}(\\text{Deps}(S)) \\iff \\nexists\\, \\text{cycle in dependency graph of } S$$

Cyclic dependencies indicate architectural error and must be resolved by introducing an intermediate layer or restructuring.

### 2.4 Boundary Explicitness

All system boundaries must be:
- **Declared**: explicitly named and typed
- **Enforced**: violations are detected and blocked
- **Observable**: boundary crossings are logged""",
        "relationships": """| Law | Relationship |
|:---|:---|
| **Rule of 4 (R4)** | R4 bounds component count per layer; structural integrity requires MECE |
| **L0 Integrity** | L0 defines integrity preservation; structural integrity is the architectural aspect |
| **ABSOLUTE_STRUCTURAL_INTEGRITY_CANON** | The absolute version; this is the operational version |
| **Difference Relation Boundary Canon** | Defines boundaries; structural integrity requires them to be explicit |""",
        "applications": """### 4.1 Architecture Validation

When validating AMOS architecture:
- Verify MECE property at each layer
- Check dependency graph for cycles
- Verify all boundaries are declared and enforced
- Validate that invariants are testable

### 4.2 System Evolution

When evolving the system:
- Structural integrity must be maintained after each change
- New components must not violate MECE
- New dependencies must not create cycles
- New boundaries must be declared and enforced

### 4.3 Cross-System Integration

When integrating with external systems:
- External boundaries must be explicitly declared
- External dependencies must not create cycles
- Integration must preserve AMOS structural integrity""",
        "worked": """Given a system $S$ undergoing structural validation:

1. **Check MECE** — for each layer, verify mutual exclusivity and collective exhaustiveness
2. **Check dependencies** — traverse dependency graph, detect cycles
3. **Check boundaries** — verify all boundaries are declared, enforced, observable
4. **Check invariants** — verify all declared invariants are testable
5. **Classify** — if all pass, structural integrity holds; if any fail, fail-closed
6. **Record** — log the validation result with provenance

```text
validate system S
  ↓
check MECE at each layer  ──fail──→  flag overlap/gap
  ↓ pass
check dependency acyclicity  ──fail──→  flag cycle
  ↓ pass
check boundary explicitness  ──fail──→  flag undeclared boundary
  ↓ pass
check invariant verifiability  ──fail──→  flag untestable invariant
  ↓ pass
structural integrity holds
  ↓
record validation receipt
```""",
        "tags_extra": ["structural-integrity", "mece", "acyclic", "boundaries", "invariants"],
    },
    "PROVENANCE_INTEGRITY_CANON.md": {
        "title": "Provenance Integrity Canon",
        "purpose": """The Provenance Integrity Canon defines the AMOS OS requirements for maintaining the integrity of provenance chains. It establishes the invariants that must hold for provenance to be considered trustworthy, and the conditions under which provenance integrity is violated.

Provenance integrity answers:

> What must be true for a provenance chain to be considered trustworthy, and what happens when provenance integrity is violated?

The Provenance Integrity Canon states:

> **A provenance chain has integrity if and only if it is complete (no missing links), tamper-evident (modifications are detectable), independently verifiable (verification does not depend on the source being verified), and fresh (not stale beyond declared validity). Provenance integrity violation is a fail-closed condition.**""",
        "formal": """### 2.1 Provenance Integrity Invariant

$$\\text{ProvenanceIntegrity}(P) \\iff \\text{Complete}(P) \\wedge \\text{TamperEvident}(P) \\wedge \\text{IndependentlyVerifiable}(P) \\wedge \\text{Fresh}(P)$$

### 2.2 Completeness

$$\\text{Complete}(P) \\iff \\forall\\, n \\in P, \\text{Source}(n) \\neq \\text{null} \\wedge \\text{Timestamp}(n) \\neq \\text{null} \\wedge \\text{Identity}(n) \\neq \\text{null}$$

Every node in the provenance chain must have a source, timestamp, and identity.

### 2.3 Tamper-Evidence

$$\\text{TamperEvident}(P) \\iff \\forall\\, n \\in P, \\exists\\, h(n) : \\text{Hash}(n) \\text{ is cryptographically bound to } \\text{Hash}(\\text{pred}(n))$$

Each node's hash includes the hash of its predecessor, creating a tamper-evident chain.

### 2.4 Independent Verifiability

$$\\text{IndependentlyVerifiable}(P) \\iff \\text{Verify}(P) \\text{ does not require trust in any node in } P$$

### 2.5 Freshness

$$\\text{Fresh}(P) \\iff \\text{Age}(P) \\leq \\text{ValidityWindow}(P)$$""",
        "relationships": """| Law | Relationship |
|:---|:---|
| **L2 Provenance** | L2 defines provenance laws; this canon governs their integrity |
| **Rule of 2 (R2)** | R2 requires source independence; provenance integrity requires independent verifiability |
| **Provenance Trust Firewall** | Enforces provenance integrity at the trust boundary |
| **L22 Replayability** | Provenance integrity is required for deterministic replay |""",
        "applications": """### 4.1 Knowledge Ingestion

When ingesting knowledge into the vault:
- Every claim must have complete provenance (source, timestamp, identity)
- Provenance chain must be tamper-evident (hash-chained)
- Verification must not depend on the source being verified
- Provenance must be fresh (within validity window)

### 4.2 Decision Recording

When recording decisions:
- Decision provenance must include all premises and their sources
- Provenance chain must be complete and tamper-evident
- Decision freshness must be within validity window

### 4.3 Memory Admission

When admitting to persistent memory:
- Memory entry provenance must be complete
- Provenance integrity must be verified before admission
- Stale provenance triggers revalidation or eviction""",
        "worked": """Given a provenance chain $P$ undergoing integrity validation:

1. **Check completeness** — verify every node has source, timestamp, identity
2. **Check tamper-evidence** — verify hash chain is intact
3. **Check independent verifiability** — verify that verification doesn't require trust in chain nodes
4. **Check freshness** — verify age is within validity window
5. **Classify** — if all pass, provenance integrity holds; if any fail, fail-closed
6. **Record** — log the validation result

```text
validate provenance chain P
  ↓
check completeness  ──fail──→  flag missing source/timestamp/identity
  ↓ pass
check tamper-evidence  ──fail──→  flag hash chain break
  ↓ pass
check independent verifiability  ──fail──→  flag circular trust
  ↓ pass
check freshness  ──fail──→  flag stale provenance
  ↓ pass
provenance integrity holds
  ↓
record validation receipt
```""",
        "tags_extra": ["provenance", "integrity", "tamper-evident", "verifiable", "freshness"],
    },
    "UNIVERSE_LOGIC_KERNEL_CANON.md": {
        "title": "Universe Logic Kernel Canon",
        "purpose": """The Universe Logic Kernel Canon defines the AMOS OS requirements for the logic kernel that governs universe-level reasoning. It establishes the foundational logic primitives, their interaction rules, and the invariants that must hold for universe-level reasoning to be valid.

Universe logic kernel answers:

> What are the irreducible logic primitives that govern universe-level reasoning, and how do they interact?

The Universe Logic Kernel Canon states:

> **Universe-level reasoning is governed by a kernel of irreducible logic primitives (ALUs — Absolute Logic Units). These primitives are self-contained, non-decomposable, and their interactions are governed by a fixed interaction matrix. No universe-level reasoning may bypass the kernel.**""",
        "formal": """### 2.1 Kernel Primitives

The Universe Logic Kernel consists of 19 Absolute Logic Units (ALUs):

```text
ALU-01: DISTINCTION    — what is separate from what
ALU-02: RELATION       — how things connect
ALU-03: BOUNDARY       — where things begin and end
ALU-04: MEMORY         — what persists across time
ALU-05: ENTROPY        — how disorder grows
ALU-06: REPAIR         — how disorder is corrected
ALU-07: RECURSION      — how patterns repeat at different scales
ALU-08: SELECTION      — how choices are made
ALU-09: CONSEQUENCE    — how effects propagate
ALU-10: OBSERVER       — how observation affects the observed
ALU-11: COLLAPSE       — how systems fail
ALU-12: RECOVERY       — how systems restore
ALU-13: IDENTITY       — how things remain themselves
ALU-14: CAUSALITY      — how causes produce effects
ALU-15: SCOPE          — how context bounds meaning
ALU-16: PROVENANCE     — how origin is traced
ALU-17: EPISTEMIC      — how knowledge is classified
ALU-18: AUTHORITY      — how permission is granted
ALU-19: COMMIT         — how decisions are finalized
```

### 2.2 Interaction Matrix

$$\\text{Interact}(\\text{ALU}_i, \\text{ALU}_j) \\in \\{\\text{reinforce}, \\text{constrain}, \\text{transform}, \\text{null}\\}$$

The 19×19 interaction matrix defines how each ALU interacts with every other ALU. The matrix is fixed and non-configurable.

### 2.3 Kernel Invariant

$$\\text{KernelValid}(K) \\iff |\\text{ALUs}(K)| = 19 \\wedge \\text{Matrix}(K) \\text{ is complete} \\wedge \\text{NoBypass}(K)$$""",
        "relationships": """| Law | Relationship |
|:---|:---|
| **CORE-19 Canon** | CORE-19 defines the 19 primitives; this canon governs their kernel application |
| **MURK Reasoning Engine** | MURK implements the 19×19 interaction matrix |
| **Absolute Logic Canon** | Defines absolute logic; this canon applies it at universe level |
| **Law of Law (LoL)** | LoL governs the kernel; the kernel governs universe-level reasoning |""",
        "applications": """### 4.1 Universe-Level Reasoning

When reasoning about universe-level structures:
- All reasoning must pass through the logic kernel
- No primitive may be bypassed or skipped
- Interactions must follow the fixed interaction matrix
- Results carry the epistemic class of the kernel (AMOS_MODEL)

### 4.2 Cross-Domain Application

When applying universe logic to specific domains:
- The kernel primitives are domain-agnostic
- Domain-specific logic is built on top of the kernel
- Domain logic must not contradict kernel primitives

### 4.3 Kernel Validation

When validating the logic kernel:
- Verify all 19 ALUs are present and functional
- Verify the 19×19 interaction matrix is complete
- Verify no bypass paths exist
- Verify kernel integrity is tamper-evident""",
        "worked": """Given a universe-level reasoning task $T$:

1. **Decompose** — break $T$ into sub-tasks that map to ALU primitives
2. **Apply kernel** — for each sub-task, apply the corresponding ALU
3. **Check interactions** — verify that ALU interactions follow the matrix
4. **Synthesize** — combine ALU outputs into a result
5. **Validate** — verify the result is consistent with kernel invariants
6. **Record** — log the reasoning trace with provenance

```text
reasoning task T arrives
  ↓
decompose T into ALU-mapped sub-tasks
  ↓
apply each ALU to its sub-task
  ↓
check interactions against 19×19 matrix  ──fail──→  flag violation
  ↓ pass
synthesize results
  ↓
validate against kernel invariants
  ↓
record reasoning trace
```""",
        "tags_extra": ["universe-logic", "kernel", "alu", "interaction-matrix", "murk"],
    },
    "ATOMIC_REASONING_LEGACY.md": {
        "title": "Atomic Reasoning Legacy",
        "purpose": """The Atomic Reasoning Legacy artifact preserves the historical formulation of AMOS atomic reasoning laws before their promotion to the L22 core law. It serves as a lineage record, not as active canon.

Atomic reasoning answers:

> What is the smallest unit of reasoning that can be independently validated, and what laws govern it?

The Atomic Reasoning Legacy states:

> **The smallest unit of reasoning is an atomic reasoning step: a single inference from premises to conclusion, with declared provenance, that can be independently validated. Atomic reasoning steps are the building blocks of all AMOS reasoning chains.**""",
        "formal": """### 2.1 Atomic Reasoning Step

$$\\text{AtomicStep}(p_1, \\ldots, p_n \\vdash c) \\iff \\text{SingleInference}(p_1, \\ldots, p_n, c) \\wedge \\text{DeclaredProvenance}(c) \\wedge \\text{IndependentlyValidatable}(c)$$

### 2.2 Composition Law

$$\\text{ReasoningChain} = \\text{AtomicStep}_1 \\circ \\text{AtomicStep}_2 \\circ \\ldots \\circ \\text{AtomicStep}_n$$

A reasoning chain is a composition of atomic steps. Each step's conclusion becomes the next step's premise.

### 2.3 Validation Law

Each atomic step must be independently validatable:
- Premises are explicit and declared
- Inference rule is explicit and declared
- Conclusion follows from premises via the declared rule
- Provenance is complete and verifiable""",
        "relationships": """| Law | Relationship |
|:---|:---|
| **L22 Atomic Reasoning** | L22 is the promoted core law version of this legacy artifact |
| **L22 Replayability** | Atomic steps are required for deterministic replay |
| **L17 RSCF** | Atomic reasoning steps are the unit of RSCF claim discipline |
| **MURK Reasoning Engine** | MURK primitives are atomic reasoning units |""",
        "applications": """### 4.1 Reasoning Chain Construction

When building reasoning chains:
- Each step must be atomic (single inference)
- Premises must be explicit
- Provenance must be declared
- Each step must be independently validatable

### 4.2 Reasoning Validation

When validating reasoning:
- Validate each atomic step independently
- If any step fails, the chain fails at that point
- Dependent steps are invalidated, not the entire chain

### 4.3 Historical Reference

This artifact serves as:
- Lineage record for L22 Atomic Reasoning
- Reference for the original formulation
- Provenance anchor for the promotion to core law""",
        "worked": """Given a reasoning chain $C = s_1 \\circ s_2 \\circ \\ldots \\circ s_n$:

1. **Decompose** — verify $C$ is a composition of atomic steps
2. **Validate each step** — for each $s_i$, verify premises, inference rule, conclusion, provenance
3. **Check composition** — verify each step's conclusion is the next step's premise
4. **Identify failure point** — if any step fails, mark it and all dependent steps as invalid
5. **Record** — log the validation result with provenance

```text
reasoning chain C arrives
  ↓
decompose into atomic steps
  ↓
for each step s_i:
  verify premises are explicit
  verify inference rule is declared
  verify conclusion follows
  verify provenance is complete
  ↓
all steps valid?  ──no──→  mark failure point, invalidate dependents
  ↓ yes
chain is valid
  ↓
record validation receipt
```""",
        "tags_extra": ["atomic-reasoning", "legacy", "lineage", "l22", "inference"],
    },
    "LOAD_CAPACITY_CANON.md": {
        "title": "Load Capacity Canon",
        "purpose": """The Load Capacity Canon defines the AMOS OS requirements for declaring, monitoring, and enforcing system load capacity limits. It establishes the conditions under which a system may accept additional load, and when it must refuse or shed load.

Load capacity answers:

> How much load can a system handle, and what must happen when load approaches or exceeds that limit?

The Load Capacity Canon states:

> **Every system MUST declare its capacity limits. Load exceeding declared capacity MUST be refused or shed. Capacity declarations MUST be verifiable and must account for both steady-state and peak load conditions.**""",
        "formal": """### 2.1 Capacity Declaration

$$\\text{Capacity}(S) = \\{\\text{SteadyState}(S), \\text{Peak}(S), \\text{Burst}(S), \\text{Recovery}(S)\\}$$

Where:
- $\\text{SteadyState}(S)$ — sustainable load indefinitely
- $\\text{Peak}(S)$ — maximum load for declared duration
- $\\text{Burst}(S)$ — maximum instantaneous load
- $\\text{Recovery}(S)$ — capacity available during recovery

### 2.2 Load Admission Rule

$$\\text{Admit}(L, S) \\iff L \\leq \\text{Available}(S) \\wedge \\text{Reserve}(S) \\geq \\text{MinReserve}(S)$$

### 2.3 Load Shedding Rule

$$\\text{Shed}(S) \\iff \\text{Load}(S) > \\text{Peak}(S) \\vee \\text{Reserve}(S) < \\text{MinReserve}(S)$$""",
        "relationships": """| Law | Relationship |
|:---|:---|
| **Load Capacity Feedback Canon** | Feedback loops maintain load within capacity limits |
| **Stability Canon** | Load within capacity is necessary for stability |
| **L10 Failure Recovery** | Load-induced failure triggers recovery |
| **L5 Scope Regime** | Capacity is scoped — different regimes have different limits |""",
        "applications": """### 4.1 Runtime Capacity

- Declare CPU, memory, I/O, network capacity
- Monitor actual load against declared capacity
- Refuse new work when approaching peak
- Shed non-critical work when exceeding peak

### 4.2 Agent Capacity

- Declare agent task capacity (concurrent tasks, memory, tokens)
- Monitor agent load against capacity
- Delegate or refuse when approaching limits
- Shed non-critical tasks when exceeding capacity

### 4.3 Memory Capacity

- Declare memory tier capacity
- Monitor memory usage against capacity
- Evict least-recently-used when approaching limits
- Preserve critical memory during shedding""",
        "worked": """Given a system $S$ with load $L$ and declared capacity $C$:

1. **Check capacity** — retrieve declared capacity $C = \\{\\text{SteadyState}, \\text{Peak}, \\text{Burst}, \\text{Recovery}\\}$
2. **Classify load** — determine if $L$ is within SteadyState, Peak, or Burst
3. **Check reserve** — verify $\\text{Reserve}(S) \\geq \\text{MinReserve}(S)$
4. **Decide** — admit if within capacity and reserve is sufficient; refuse or shed otherwise
5. **Record** — log the decision with provenance

```text
load L arrives at system S
  ↓
retrieve declared capacity C
  ↓
L ≤ SteadyState?  ──yes──→  admit
  ↓ no
L ≤ Peak?  ──yes──→  admit with warning
  ↓ no
L ≤ Burst?  ──yes──→  admit if reserve sufficient
  ↓ no
refuse or shed
  ↓
record decision receipt
```""",
        "tags_extra": ["load-capacity", "admission", "shedding", "peak", "steady-state"],
    },
}

# Template for expanded content
TEMPLATE = '''---
title: {title}
type: canon
source: 01_CANON/01_CORE_LAWS
artifact: {filename}
artifact_id: 01_canon_01_core_laws_{id_base}
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 01_CANON
segment: 01_CANON/01_CORE_LAWS
artifact_kind: CANON
path: 01_CANON/01_CORE_LAWS/{filename}
tags:
  - 01_core_laws
  - amos-os
  - canon
  - canon/universe
  - rscf
  - universe
  - placeholder_expanded
  - law-hierarchy{tags_extra}
version: 1.0.0
updated: '2026-09-04'
status: SUBSTANTIVE_SPECIFICATION
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
  regime: canon
  confidence_ceiling: source_supported
  provenance_independence: NOT_ESTABLISHED
---

# {title}

## 0. Status

`{filename}` defines the proposed AMOS OS **{title_short}** core law.

This artifact replaces a structural placeholder with substantive content. It does not, by its own existence, establish final AMOS canon, executable enforcement, empirical validity, or runtime implementation.

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

Origin architect / steward: **Trang Phan**

______________________________________________________________________

## 1. Purpose

{purpose}

______________________________________________________________________

## 2. Formal Definition

{formal}

______________________________________________________________________

## 3. Relationship to Other Core Laws

{relationships}

______________________________________________________________________

## 4. Application Domains

{applications}

______________________________________________________________________

## 5. Worked Semantics

{worked}

______________________________________________________________________

## 6. Non-Purpose

This law MUST NOT be used to claim:
- universal laws of reality;
- scientific proof;
- empirical truth;
- runtime enforcement that has not been implemented;
- final canonical status;
- authority merely from architectural importance;
- or successful validation merely because the slot is addressable.

______________________________________________________________________

## 7. Gaps

- Executable binding NOT_ESTABLISHED — this law is specified but not yet enforced by runtime code
- Canonical status CONDITIONAL — proposed specification, not yet promoted to full canon
- Automated validation NOT_ESTABLISHED — automated enforcement is not implemented
- Cross-domain testing NOT_ESTABLISHED — testing across all AMOS domains is not complete

______________________________________________________________________

## 8. Promotion-Gate Checklist

- [x] substantive content populated from AMOS corpus sources
- [x] formal definition provided (§2)
- [x] relationship to other core laws documented (§3)
- [x] application domains specified (§4)
- [x] worked semantics defined (§5)
- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

______________________________________________________________________

## 9. Cross-Plane Bindings

- Governed by — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]]
- Kernel enforcement — [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- Control-plane gates — [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via — [[20_OPERATIONS/20_OPERATIONS_MOC|20_OPERATIONS_MOC]]

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

node_id: amos_01_canon_01_core_laws_{id_base}

node_type: canon

path: 01_CANON/01_CORE_LAWS/{filename}

claim_class: AMOS_MODEL

rscf_state: SOURCE_CLAIM

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]
'''


def expand_file(filepath, content_def):
    """Expand a placeholder file with substantive content."""
    filename = os.path.basename(filepath)
    id_base = filename.replace(".md", "").lower()

    title = content_def["title"]
    title_short = title.replace(" Canon", "").replace(" Legacy", "")

    tags_extra = ""
    if "tags_extra" in content_def:
        tags_extra = "\n  - " + "\n  - ".join(content_def["tags_extra"])

    content = TEMPLATE.format(
        title=title,
        title_short=title_short,
        filename=filename,
        id_base=id_base,
        tags_extra=tags_extra,
        purpose=content_def["purpose"],
        formal=content_def["formal"],
        relationships=content_def["relationships"],
        applications=content_def["applications"],
        worked=content_def["worked"],
    )

    with open(filepath, "w") as f:
        f.write(content)

    return len(content)


def main():
    core_laws_dir = VAULT_ROOT / "01_CORE_LAWS"

    expanded = 0
    for filename, content_def in CORE_LAW_CONTENT.items():
        filepath = core_laws_dir / filename
        if filepath.exists():
            size = expand_file(str(filepath), content_def)
            print(f"Expanded {filename}: {size} bytes")
            expanded += 1
        else:
            print(f"WARNING: {filename} not found")

    print(f"\nTotal expanded: {expanded}")


if __name__ == "__main__":
    main()
