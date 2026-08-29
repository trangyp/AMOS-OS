---
title: AMOS INFRASTRUCTURE FULL BRAIN AGENT ARCHITECTURE ROUND11
tags:
- knowledge
- note
- canon/knowledge
type: document
source: 11_KNOWLEDGE/root
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# AMOS Infrastructure, Full Brain OS, Agents & Skills Architecture
## Round 11 — Governed Architecture Summary

**Origin architect / steward:** Trang Phan
**Document type:** Architecture synthesis and implementation-status report
**Conclusion class:** **DERIVED**
**Governed AMOS_CORE baseline:** **v4.4** unless a later candidate is explicitly admitted
**Package basis:** `final_skill_package_amos_infrastructure_round11/skill.zip`

> This document summarizes the current AMOS infrastructure model encoded in the validated Skill package.
> AMOS/Trang corpus statements are preserved as **SOURCE_CLAIM / MODEL** unless separately supported by executable or external evidence.
> Open-source systems are implementation analogues, not AMOS canon.

---

## 1. Executive Architecture Statement

**AMOS is the infrastructure envelope and control architecture above the host model, Full Brain OS, specialist agents, Skills, memory, policy, tools, deployment adapters, and world-effect executors.**

Full Brain OS is the principal cognitive / supervisory subsystem inside that larger architecture.

The most useful distinction is:

```text
SYSTEM SCOPE / AUTHORITY ENVELOPE

AMOS Infrastructure
├── Governance / Policy / Authority
├── Trust Roots / Identity / Capability Grants
├── Lineage / Canon / Configuration Admission
├── Provenance / Evidence / Memory Admission
├── Runtime / Transaction / Freshness / Finality
├── Agent Lifecycle / Task Orchestration
├── Full Brain OS
│   ├── Supervisory cognition
│   ├── decomposition
│   ├── routing
│   ├── synthesis
│   └── competing-hypothesis management
├── Specialist Agents
├── Skills / Kernels / Engines
├── Host Runtime / Tools / APIs
└── Effect Adapters
```

while an individual execution path may look like:

```text
Human / Environment
        ↓
Full Brain OS
        ↓
Reasoning Runtime / RSCF
        ↓
AMOS Infrastructure Control Plane
        ↓
Host Deployment / Tool / Effect Adapter
        ↓
World Effect
```

These are different dimensions.

**Authority precedence does not imply literal structural containment at every runtime step.**

---

## 2. Core Separation of Responsibilities

### 2.1 Full Brain OS

Full Brain OS may:

- interpret objectives;
- decompose complex work;
- select reasoning modes;
- perform H/M/L routing;
- route to specialist agents and Skills;
- compare hypotheses;
- identify contradictions;
- synthesize evidence;
- propose decisions and actions;
- request authorization;
- escalate unresolved uncertainty.

Full Brain OS may **not automatically**:

- issue itself durable-effect authority;
- create new root trust;
- admit its own source claims as trusted canon;
- approve its own external actions;
- override revocation or freshness;
- silently widen tool permissions;
- finalize infrastructure transactions;
- relabel MODEL / SOURCE_CLAIM as VERIFIED;
- mutate canonical memory without admission.

### 2.2 AMOS Infrastructure Control Plane

The infrastructure layer owns, or must govern:

- authority validation;
- capability grants;
- workload identity;
- provenance admission;
- freshness;
- scope/regime compatibility;
- state legality;
- transaction / CAS / fencing semantics;
- commit-time revalidation;
- finality;
- rollback / repair;
- recovery authority;
- lineage admission;
- canon/config activation;
- agent lifecycle legality;
- task leasing;
- cancellation;
- spawn budgets;
- durable checkpoint admission;
- observability binding;
- final effect eligibility.

---

## 3. AMOS_CORE v3.0 → v4.4 Infrastructure Spine

The currently governed lineage is:

| Version | Architectural contribution |
|---|---|
| v3.0 | deterministic logic |
| v3.1 | logic repair |
| v3.2.1 | recursive RSCF + H/M/L |
| v3.3 | governed evolution |
| v3.4.1 | causal lineage |
| v3.5 | epistemic / environment regimes |
| v3.6 | competing hypotheses |
| v3.7 | provenance topology |
| v3.7.1 | Sybil / correlated-source hardening |
| v3.8 | deeper provenance traversal |
| v3.9 | persistent provenance |
| v4.0 | MVCC / CAS concepts |
| v4.1 | atomic multi-RSCF reasoning / transaction concepts |
| v4.2 | causal epoch finality |
| v4.3 | hardened shard-local finalization |
| v4.4 | proof-based coordination avoidance |

These are **AMOS design/runtime patterns**.

They are not automatic claims that ChatGPT itself implements a distributed database, consensus system, or production MVCC engine.

---

## 4. Agent Architecture

AMOS should not be implemented as one giant autonomous agent.

### Full Brain Supervisor

Purpose:

- high-level cognitive orchestration;
- task decomposition;
- agent selection;
- evidence synthesis;
- uncertainty management;
- escalation.

Default authority:

```text
COGNITIVE / PROPOSAL
```

not:

```text
ROOT / GOVERNOR / EFFECT
```

### Planner Agent

Produces:

- execution plans;
- task DAGs;
- dependencies;
- assumptions;
- rollback points;
- decision-changing uncertainty.

It cannot certify its own authorization.

### Research / Evidence Agent

Produces typed evidence with:

- source identity;
- source ancestry;
- revision;
- freshness;
- scope;
- regime;
- evidence class;
- contradictions;
- falsifiers.

It cannot promote its own extraction to VERIFIED automatically.

### Engineering Agent

Produces:

- code;
- architecture;
- patches;
- configuration;
- migrations.

Its write / deployment scope must be capability-bound.

### Verification Agent

Runs:

- deterministic tests;
- adversarial checks;
- mutation testing;
- conformance testing;
- replay;
- regression validation.

Independence must be demonstrated if its result is load-bearing.

### Memory / Knowledge Agent

Proposes:

- additions;
- revisions;
- contradiction links;
- retirement;
- revalidation.

Canonical writes go through knowledge admission.

### Policy / Governance Agent

May help interpret or construct policy.

For consequential decisions, policy should preferably be externalized into deterministic / independently testable enforcement.

### Effect Adapter

Performs actual:

- API calls;
- DB writes;
- GitHub mutations;
- deployments;
- messages;
- financial/business system changes;
- other external effects.

It cannot widen the authorized action.

---

## 5. Capability-Based Authorization

Capability is separate from identity, trust, reasoning confidence, and evidence confidence.

```text
identity ≠ capability
capability ≠ trust score
capability ≠ reasoning confidence
capability ≠ evidence confidence
```

A consequential capability grant should bind:

- grant ID / hash;
- principal;
- agent;
- task;
- resource;
- effect;
- risk ceiling;
- environment;
- trust domain;
- policy version;
- manifest version;
- issuance epoch;
- expiry;
- provenance;
- parent grant if delegated.

### Delegation Law

Delegation may only reduce authority.

A child grant must not:

- add effects;
- add resources;
- increase risk;
- extend expiration;
- cross trust domain;
- outlive a parent;
- survive parent revocation.

### Commit-Time Revalidation

A planning-time allow decision is insufficient.

Before a durable effect:

```text
revalidate(grant)
revalidate(identity)
revalidate(policy)
revalidate(state)
revalidate(resource)
revalidate(effect)
revalidate(risk)
revalidate(freshness)
revalidate(parent-chain)
```

A capability revoked after ticket issuance must block commit.

---

## 6. Agent Lifecycle & Long-Running Orchestration

Round 11 introduces a stronger lifecycle model.

### Task Lifecycle

```text
SUBMITTED
   ↓
WORKING
   ├── INPUT_REQUIRED
   ├── AUTH_REQUIRED
   └── WAITING_DEPENDENCY
   ↓
COMPLETED / CANCELED / REJECTED / FAILED
```

Terminal tasks do not restart in place.

A retry should create a new attempt or explicit epoch while preserving ancestry.

### Task Contract

Every consequential task should include:

- task ID;
- context ID;
- owner agent;
- root objective;
- parent task;
- lifecycle state;
- state epoch;
- capability hash;
- input schema;
- output / artifact schema;
- dependencies;
- budget;
- deadline;
- freshness;
- retry / idempotency policy;
- cancellation state;
- provenance;
- checkpoint;
- final artifact / receipt.

---

## 7. Leases, Fencing & Zombie Workers

Stateful work requires a bounded lease.

A lease should bind:

- agent identity;
- task;
- fencing epoch;
- acquisition time;
- expiry;
- heartbeat policy.

If ownership changes:

```text
epoch N → epoch N+1
```

Any worker still operating under epoch N becomes stale.

A stale agent may not commit results.

This prevents:

- two active owners;
- duplicate effects;
- old workers publishing after reassignment;
- stale checkpoint restoration overwriting newer state.

---

## 8. Spawn Governance & Backpressure

Full Brain may request sub-agents.

AMOS infrastructure controls whether they are admitted.

Bound:

- maximum recursion depth;
- maximum fan-out;
- maximum concurrently active agents;
- tool-call budget;
- time budget;
- cost/token budget;
- model class;
- agent role;
- authority ceiling.

Child authority is:

```text
parent capability
∩ task capability
∩ infrastructure policy
```

not:

```text
parent authority + new child authority
```

### Overload Handling

Prefer:

- bounded queues;
- admission control;
- concurrency limits;
- circuit breakers;
- backoff;
- deadlines;
- load shedding.

Never respond to overload with unlimited agent spawning.

---

## 9. Retry, Idempotency & IN_DOUBT

Retry rules depend on effect type.

### Pure / Read-Only

Normally safe to retry within budget/freshness policy.

### Idempotent Effect

Retry only with explicit idempotency semantics.

### Non-Idempotent Effect

Require:

- idempotency key; or
- outcome discrimination.

### Unknown Effect Outcome

State becomes:

```text
IN_DOUBT
```

Do not assume:

- success;
- failure;
- rollback.

Do not blindly retry.

---

## 10. Cancellation

Cancellation is a governed transition.

When canceled:

- stop new child admission;
- propagate cancellation to active children;
- block new external effects;
- preserve completed evidence;
- preserve partial artifacts;
- fence stale workers;
- record partial completion.

Compensation is a separate authorized action.

---

## 11. Fan-In / Join Semantics

A supervisor may synthesize agent results only when dependency policy is satisfied.

Each dependency should record:

- required / optional;
- lifecycle state;
- artifact identity;
- provenance;
- freshness;
- evidence class;
- contradiction state.

A required child that is:

- FAILED;
- CANCELED;
- missing;
- stale;

cannot silently count as success.

Partial synthesis requires an explicit partial-results policy.

---

## 12. Messages vs Artifacts

A critical infrastructure distinction:

```text
MESSAGE ≠ ARTIFACT
```

A message is communication.

An artifact is an output object.

Examples:

> “Tests passed.”

is not equivalent to:

```text
test receipt
+ test command
+ version/hash
+ environment
+ result
+ timestamp
+ provenance
```

Critical agent outputs should be durable artifacts or evidence records.

---

## 13. Skills as Versioned Capability Modules

A Skill should be treated as a bounded, versioned capability module—not hidden prompt authority.

A consequential Skill invocation should declare:

- Skill ID;
- Skill version;
- task ID;
- input contract;
- output contract;
- required scripts;
- required references;
- capability requirements;
- deterministic validation;
- artifacts;
- failure modes;
- compatibility.

A Skill can constrain or organize authority.

A Skill may not create new infrastructure authority.

---

## 14. Memory Architecture

Avoid one universal untyped agent memory.

Separate:

### Working Memory

Temporary task-local state.

### Agent Scratch State

Private implementation/reasoning support.

### Shared Operational State

Cross-agent workflow state.

### Evidence / Provenance Graph

Source and derivation topology.

### Canonical Knowledge

Governed persistent knowledge.

Canonical writes require:

- source identity;
- provenance;
- revision;
- freshness;
- scope/regime;
- evidence class;
- contradiction checks;
- CAS/version preconditions where concurrency exists.

---

## 15. Living Knowledge Infrastructure

The research/knowledge pipeline remains:

```text
raw source
→ evidence atom
→ typed relationship
→ contradiction / gap map
→ governed synthesis
→ decision / product
```

Knowledge-state operations include:

- reinforce;
- contradict;
- split;
- merge;
- mutate;
- retire;
- promote.

These transitions are governed.

They do not create truth automatically.

---

## 16. Trust Root & Runtime Identity

Behavioral trust scores are not cryptographic authority.

```text
trust score ≠ workload identity
trust score ≠ root key
trust score ≠ capability
trust score ≠ threshold signature
```

Root bootstrap requires an explicitly trusted basis.

Root rotation should preserve:

- monotonic versions;
- old-root authorization;
- new-root threshold;
- revocation;
- trust domain;
- expiry;
- transition provenance.

---

## 17. Canon & Configuration Admission

A file is not trusted because it is named:

- `canon`;
- `manifest`;
- `policy`;
- `config`;
- `README`.

The activation path should be:

```text
candidate input
→ immutable identity
→ provenance
→ schema validation
→ semantic validation
→ freshness
→ environment validation
→ authority
→ ACTIVE
```

Tests alone cannot authorize activation.

Signatures alone do not establish truth.

---

## 18. Recovery & Break-Glass

Normal authority is distinct from recovery authority.

```text
normal authority ≠ recovery authority ≠ break-glass authority
```

For an ambiguous effect:

```text
effect
→ uncertainty
→ IN_DOUBT
→ collect discriminating evidence
→ independently authorized resolution
→ finalized / repaired state
```

Break-glass must be:

- scoped;
- temporary;
- audited;
- explicitly justified;
- independently approved for high-impact use.

It cannot rewrite provenance or mark UNKNOWN as VERIFIED.

---

## 19. Host Portability

AMOS semantic identity must survive changes in:

- model provider;
- agent framework;
- workflow runtime;
- policy engine;
- memory store;
- tool protocol.

Host migration may not silently:

- widen authority;
- remove provenance;
- remove rollback;
- downgrade persistent memory to chat context;
- change decision boundaries;
- upgrade evidence class.

The host implements AMOS semantics.

The host does not redefine them.

---

## 20. Open-Source Interoperability Map

The following are **implementation analogues**, not AMOS canon.

| Open-source system / standard | Useful AMOS mapping |
|---|---|
| Open Policy Agent | policy decision vs enforcement |
| OpenFGA | contextual / relationship authorization |
| SPIFFE / SPIRE | workload identity and trust domains |
| TUF | trust-root roles, thresholds, expiry, rollback defense |
| Sigstore / Rekor | transparency / artifact history |
| SLSA | software/artifact provenance |
| OpenTelemetry | traces, events, metrics, execution context |
| Temporal | durable orchestration and resumability |
| A2A | agent-to-agent tasks, messages, artifacts, capabilities |
| MCP | model/agent-to-tool interface and typed requests |
| Hypothesis | property-based testing |
| mutation testing | tests for whether controls actually detect defects |

### Important Firewall

```text
Open-source pattern
→ implementation candidate
→ AMOS invariant validation
→ admit / reject
```

Never:

```text
popular framework
→ AMOS canon
```

---

## 21. A2A / MCP / Durable Runtime Integration

### A2A

Useful concepts:

- task IDs;
- context IDs;
- stateful tasks;
- messages;
- artifacts;
- agent cards;
- version negotiation;
- streaming updates.

AMOS adds:

- provenance;
- RSCF dependency structure;
- authority;
- evidence class;
- commit semantics;
- regime/freshness controls.

### MCP

Useful for:

- typed tool calls;
- tool discovery;
- tool schemas;
- progress;
- cancellation;
- routing.

MCP tool availability does not equal permission.

### Durable Workflow Runtime

Useful for:

- process recovery;
- retry;
- timers;
- durable state;
- signals;
- task queues.

Workflow history is not canonical truth.

---

## 22. Business Interpretation

For a non-technical executive:

> **The AI model is the reasoning engine. Full Brain is the cognitive management system. AMOS is the infrastructure, governance, memory, security, orchestration, and control layer around them.**

AMOS decides and records:

- who may act;
- what they may act on;
- which evidence is trusted;
- what is remembered;
- how agents coordinate;
- when retries are safe;
- what happens after failure;
- what reaches external systems;
- how every consequential action is audited.

This is much closer to an **enterprise AI operating/control plane** than to a chatbot.

---

## 23. Production Architecture

A practical deployment target:

```text
                    ┌───────────────────────────────┐
                    │      USER / SYSTEM / EVENT    │
                    └───────────────┬───────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │      AMOS INGRESS GATE        │
                    │ identity / task / scope/risk  │
                    └───────────────┬───────────────┘
                                    │
                                    ▼
┌───────────────────────────────────────────────────────────────┐
│                    AMOS INFRASTRUCTURE                         │
│                                                               │
│ trust • lineage • capability • policy • provenance • memory  │
│ lifecycle • leases • fencing • budgets • transactions        │
└───────────────┬───────────────────────────────┬───────────────┘
                │                               │
                ▼                               ▼
┌───────────────────────────┐       ┌───────────────────────────┐
│      FULL BRAIN OS        │       │ EVIDENCE / MEMORY GRAPH   │
│ supervisory cognition     │       │ provenance / freshness    │
└───────────────┬───────────┘       └───────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────────────────┐
│                     SPECIALIST AGENTS                         │
│ Planner • Research • Engineer • Verify • Memory • Policy     │
└───────────────┬───────────────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────────────────┐
│                 SKILLS / KERNELS / ENGINES                    │
└───────────────┬───────────────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────────────────┐
│             AUTHORIZED EFFECT / TOOL GATE                     │
└───────────────┬───────────────────────────────────────────────┘
                │
                ▼
        GitHub / APIs / DB / CI / Cloud / Human
```

---

## 24. What Is Actually Verified in Round 11

The packaged Skill itself was measured as:

- **632 tests passed**
- **100% statement coverage** across governed validators
- **100% branch coverage** across governed validators
- **91 / 91 critical mutation attacks killed**
- package structure validation: **PASS**
- ZIP integrity: **PASS**
- clean-room pytest from final archive: **632 passed**
- clean-room mutation suite: **91 / 91 killed**
- `SKILL.md`: **474 lines**
- package: **114 entries**
- archive: **226,493 bytes**

These measurements validate the Skill package and its deterministic controls.

They do **not** prove that every conceptual AMOS subsystem described in the broader corpus is deployed as a production service.

---

## 25. Remaining Production Gaps

### CRITICAL

**Persistent runtime implementation**

The Skill specifies:

- task leases;
- fencing;
- transactions;
- recovery;
- capability admission;
- provenance;
- canonical memory.

A production deployment still needs durable infrastructure providing these controls.

### CRITICAL

**Independent effect authorization**

Consequential effects should eventually use an independently enforceable authorization service or gateway, not LLM prose alone.

### CRITICAL

**Workload identity**

Production agents need real workload/process identity rather than agent names alone.

### DECISION-RELEVANT

**Task queue / workflow runtime**

Long-running workflows need real durable scheduling and checkpointing.

### DECISION-RELEVANT

**Provenance database**

The evidence topology must be persistently stored and queryable.

### DECISION-RELEVANT

**Memory isolation**

Working, operational, evidence, and canonical memories require typed persistence and admission policies.

### DECISION-RELEVANT

**Agent protocol runtime**

The A2A/MCP-style contracts need actual network/runtime enforcement to become deployment guarantees.

---

## 26. Recommended Next Engineering Sequence

1. **Runtime schema package**
   Define machine-readable schemas for Task, Agent, Grant, Evidence, Artifact, Checkpoint, PolicyDecision, and EffectReceipt.

2. **Persistent task service**
   Implement task state, leases, fencing epochs, cancellation, joins, retry policies, and budget accounting.

3. **Capability service**
   Implement grant issuance, attenuation, delegation, revocation, expiry, and commit-time checks.

4. **Agent registry**
   Register agent roles, versions, schemas, capabilities, dependencies, and failure modes.

5. **Skill registry**
   Treat Skills as versioned deployable capability modules with compatibility and authority metadata.

6. **Provenance/evidence graph**
   Store evidence identity, ancestry, contradictions, freshness, regimes, falsifiers, and derivations.

7. **Typed memory fabric**
   Separate operational, working, evidence, and canonical memory.

8. **Policy decision service**
   Move consequential governance into deterministic policy evaluation where practical.

9. **Effect gateway**
   Bind actual API/DB/GitHub/cloud effects to fresh capability and policy decisions.

10. **Durable orchestration**
    Add resumable, crash-safe long-running workflows.

11. **Observability**
    Trace request → Full Brain → agent → Skill → policy → effect → receipt.

12. **Adversarial evaluation**
    Continue property, mutation, concurrency, replay, stale-state, authorization, and protocol compatibility testing.

---

## 27. Final Architecture Rule

The round-11 architecture can be compressed into one line:

> **Full Brain coordinates intelligence; specialist agents perform bounded work; Skills package repeatable capability; AMOS infrastructure owns identity, authority, provenance, memory admission, lifecycle, transaction safety, recovery, and the final boundary to real-world effects.**

That distinction should remain invariant even as host models, agent frameworks, memory systems, protocols, and deployment technology change.

---

## Conclusion Class

**DERIVED**

The architecture is grounded in the supplied AMOS corpus, the validated round-11 Skill implementation, and bounded comparison with mature open-source infrastructure patterns.

The Skill's tests are **VERIFIED for that package and test environment**.

Claims about the complete conceptual AMOS architecture operating as a deployed production infrastructure remain **MODEL / CONDITIONAL** until corresponding runtime services and deployment evidence exist.

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: amos_infrastructure_full_brain_agent_architecture_round11
node_type: note
path: 11_KNOWLEDGE/AMOS_INFRASTRUCTURE_FULL_BRAIN_AGENT_ARCHITECTURE_ROUND11.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[KNOWLEDGE_MOC]]
