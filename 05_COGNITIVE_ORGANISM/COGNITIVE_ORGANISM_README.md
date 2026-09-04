---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: Cognitive Organism Readme
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# COGNITIVE ORGANISM README

## 1. Purpose

`05_COGNITIVE_ORGANISM` is the Full Brain field for **persistent governed cognition**. It composes
perception, attention, reasoning, memory access, affect/drive models, world modeling, simulation,
planning, decision support, learning, reflection, regulation and repair into typed cognitive
proposals.

It is neither the entire Full Brain OS nor the effect-authority layer.

```text
COGNITIVE_ORGANISM != FULL_BRAIN_OS
COGNITION != CONTROL
PROPOSAL != COMMIT
```

## 2. Position inside Full Brain OS

```text
FULL BRAIN OS
├── representation / expression
├── cognitive coordination / omni-kernel
├── capability / brain-core ecosystem
├── world-system representation / omniverse brain
├── COGNITIVE ORGANISM
├── runtime continuity
├── control / effect governance
└── deployment adapters
```

The organism coordinates cognitive state and proposals. Control Plane owns durable-effect admission.

## 3. Five foundational substrates

The source model decomposes the organism into:

```text
CORE = {
  Identity,
  State,
  Flow,
  Memory,
  Governance
}
```

These are substrates, not five exhaustive organs.

- **Identity** — continuity, lineage, role and invariant envelope.
- **State** — current cognitive/regulatory/lifecycle condition.
- **Flow** — typed evidence, events, proposals and feedback.
- **Memory** — temporal continuity with epistemic state preserved.
- **Governance** — admissibility, authority boundary and fail-closed constraints.

## 4. MECE organ responsibility groups

### A. Input / representation

```text
Perception
Attention
Context
WorldModel access
```

Responsibility: turn available signals and context into typed representations without silently
promoting interpretation to observation.

### B. Interpretation / reasoning

```text
Cognition
Structural reasoning
Hypothesis competition
Causal analysis
Simulation
Decision support
```

Responsibility: transform representations into candidate explanations, predictions and proposals.

### C. Affect / drive

```text
EmotionModel
Instinct
Motivation
Goal
```

Responsibility: represent preference/drive/priority state. These are AMOS models, not claims of felt
emotion or biological truth.

### D. Prospective / action formation

```text
Planning
AgencyProposal
ActionInterface
```

Responsibility: construct prospective action structures and requests for authorization.

### E. Adaptation / continuity

```text
Memory access
Learning
Reflection
Identity continuity
Lifecycle
```

Responsibility: preserve continuity, update candidates and maintain ancestry across episodes.

### F. Social / expression

```text
Social
Expression
```

Responsibility: model social context and transform internal proposals into communicable forms.

### G. Regulation / assurance

```text
Homeostasis
Risk
Safety
Repair
Observability
```

Responsibility: maintain bounded operation, detect degradation, expose failure and trigger repair.

## 5. Active cognitive loop

```text
SENSE
→ REPRESENT
→ ATTEND
→ CONTEXTUALIZE
→ RETRIEVE MEMORY / KNOWLEDGE
→ REASON
→ PRESERVE COMPETING HYPOTHESES
→ SIMULATE
→ PLAN
→ DECIDE / PROPOSE
→ METACOGNITIVE CHECK
→ AUTHORITY GATE
→ ACT IF AUTHORIZED
→ OBSERVE OUTCOME
→ LEARN
→ REFLECT
→ REGULATE / REPAIR
```

The loop may short-circuit when claim, decision and action sufficiency are reached.

It escalates when decision-changing uncertainty remains around:
- critical gaps;
- contradictory evidence;
- correlated provenance;
- stale premises;
- scope/regime mismatch;
- causal ambiguity;
- irreversible stakes;
- authority/finality.

## 6. Typed event flow

Organs should not mutate each other implicitly.

```yaml
event:
  event_id:
  source_organ:
  target_organ:
  event_type:
  payload:
  timestamp:
  state_version:
  provenance:
  transaction:
  authority_context:
```

```text
EVENT_DELIVERED != STATE_MUTATED
MESSAGE != ARTIFACT
```

State mutation requires schema, version/precondition, applicable constraints and authority where
consequential.

## 7. Perception firewall

Separate:

```text
RAW_OBSERVATION
FEATURE_EXTRACTION
INTERPRETATION
INFERENCE
MODEL
```

Hard rules:

```text
OBSERVATION != INFERENCE
UNAVAILABLE_SENSOR != INFERRED_SENSOR
INTERPRETATION != VERIFIED FACT
MODEL OUTPUT != OBSERVATION
```

## 8. Attention / context budget

Attention allocation should prioritize:
- decision relevance;
- consequence;
- uncertainty;
- contradiction;
- irreversibility;
- freshness;
- dependency criticality;
- discriminating information value.

Retention priority:

```text
hard constraints
> critical evidence
> unresolved contradictions
> current decisions
> provenance
> recovery state
> narrative detail
```

`SALIENCE != TRUTH` and `ATTENTION != VALIDATION`.

## 9. Reasoning architecture

The cognition source describes six layers:

```text
C1 Meta Logic
C2 Structural Reasoning
C3 Cognitive Infrastructure
C4 Multi-Possibility Reasoning
C5 Biological Logic Lens
C6 Integration Kernel
```

v4.4 discipline adds:
- recursive RSCF / H-M-L;
- scope and regime firewall;
- causal firewall;
- provenance topology and Sybil/correlation hardening;
- competing hypotheses;
- confidence ceiling;
- selective invalidation;
- commit-time freshness;
- falsifier-first sensitivity checks.

## 10. RSCF proof capsule requirements

A consequential cognitive conclusion should preserve:

```text
claim / conclusion class
load-bearing premises
evidence
provenance + source ancestry
scope
regime
freshness
dependencies
competing explanations
falsifiers
invalidation conditions
confidence ceiling
```

Derived confidence cannot exceed the weakest load-bearing premise unless independently revalidated.

## 11. Multi-hypothesis discipline

Maintain genuine alternatives:

```text
H1 strongest supported explanation
H2 strongest materially different alternative
H3... additional decision-relevant alternatives
```

Do not force convergence when support is equal, incomparable, correlated or insufficient.

Prefer the cheapest high-information discriminating test.

## 12. Causal firewall

Allowed relation types include:

```text
ASSOCIATION
CORRELATION
CONFOUNDER
MEDIATOR
ENABLING_CONDITION
NECESSARY_CONDITION
SUFFICIENT_CONDITION
MECHANISM
FEEDBACK
INTERVENTION_EFFECT
UNKNOWN
```

Sequence, resemblance and co-occurrence do not by themselves establish causation.

## 13. Homeostasis and degradation

Conceptual lifecycle:

```text
BOOT
→ WARMUP
→ ACTIVE
→ LOADED
→ DEGRADED
→ REPAIR
→ RECOVERED
→ ACTIVE
```

Controlled exits may include:

```text
ACTIVE → GRACEFUL_SHUTDOWN
DEGRADED → SUSPEND
CRITICAL → QUARANTINE
UNRECOVERABLE → TERMINATE
```

A critical integrity/authority gap fails closed for consequential paths.

## 14. Action and authority boundary

The organism may:
- perceive;
- infer;
- remember/retrieve;
- simulate;
- plan;
- compare alternatives;
- recommend;
- request authorization;
- learn from admitted outcomes.

It may not by itself:
- grant new root authority;
- widen capabilities;
- override revocation;
- mark its own source claims as verified;
- commit durable external effects;
- rewrite provenance;
- silently convert `UNKNOWN/GAP` into pass.

## 15. Cross-plane contracts

Inputs may come from:

```text
10_MEMORY
11_KNOWLEDGE
12_STATE
13_MODELS
21_DOMAINS
15_INTERFACES
```

Primitive/runtime/governance dependencies:

```text
02_KERNEL
03_CONTROL_PLANE
04_RUNTIME
16_SCHEMAS
18_SECURITY
```

Delegated/deployment surfaces:

```text
06_AGENTS
07_SKILLS
26_WORKFLOWS
14_TOOLS
```

Feedback/assurance:

```text
17_OBSERVABILITY
19_TESTS
20_OPERATIONS
22_RESEARCH
```

## 16. Required input envelope

```yaml
cognitive_input:
  objective:
  scope:
  regime:
  consequence_class:
  observations: []
  evidence: []
  provenance:
  state_version:
  memory_refs: []
  knowledge_refs: []
  active_constraints: []
  authority_context:
  freshness:
```

## 17. Required output envelope

```yaml
cognitive_output:
  conclusion_class:
  claims: []
  proposals: []
  competing_hypotheses: []
  dependencies: []
  evidence_refs: []
  provenance:
  scope:
  regime:
  freshness:
  uncertainty_vector:
  falsifiers: []
  confidence_ceiling:
  authority_required:
  unresolved_gaps: []
```

## 18. Failure and repair semantics

On a failed premise/edge:
1. invalidate only dependent conclusions;
2. preserve unaffected state;
3. roll back to the nearest valid reasoning state;
4. reroute using changed evidence or assumptions;
5. avoid repeating the same failed path without changed evidence;
6. escalate globally only when dependency closure requires it.

## 19. Navigation

- [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
- [[05_COGNITIVE_ORGANISM/00_INDEX/COGNITIVE_ORGANISM_MAP|COGNITIVE_ORGANISM_MAP]]
- [[05_COGNITIVE_ORGANISM/COGNITIVE_ORGANISM_COGNITIVE_ORGANISM_CONTRACT|COGNITIVE_ORGANISM_CONTRACT]]
- [[01_CANON/03_COGNITION_CANON/COGNITIVE_ORGANISM_CANON|COGNITIVE_ORGANISM_CANON]]
- [[01_CANON/03_COGNITION_CANON/FULL_BRAIN_OS_CANON|FULL_BRAIN_OS_CANON]]
- [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
- [[11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL|AMOS_COGNITIVE_ORGANISM_OS_DETAIL]]

## 20. Integrity boundary

```text
ORGANISM_MODEL != BIOLOGICAL_ORGANISM
BRAIN_ARCHITECTURE != HUMAN BRAIN
EMOTION_MODEL != FELT EMOTION
SELF_MODEL != SUBJECTIVE SELF
AGENCY_MODEL != UNBOUNDED AUTONOMY
COGNITIVE INTEGRATION != EFFECT AUTHORITY
DOCUMENTED != IMPLEMENTED
UNKNOWN/GAP != PASS
```
