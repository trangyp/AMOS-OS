---
tags:
  - amos
  - cognitive-matrix
  - l03
  - percept-formation
  - agents
  - perception
  - rscf
  - hml
  - governance

title: "L03_PERCEPT_FORMATION — Agents"
origin_architect: "Trang Phan"
status: "MODEL_AGENT_CONTRACT / UNIMPLEMENTED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
---

# L03_PERCEPT_FORMATION — Agents

**Class:** `COGNITIVE_PRIMITIVE_AGENT_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L03_PERCEPT_FORMATION`  
**Artifact:** `AGENTS.md`  
**Status:** `AMOS_MODEL / UNIMPLEMENTED / UNVALIDATED`

> **Canon boundary:** this artifact defines an AMOS-aligned agent architecture for `L03_PERCEPT_FORMATION`. It preserves the distinction between observed inputs, derived percepts, model interpretations, confidence, and downstream decisions. Agent names, role partitions, message types, algorithms, thresholds, and runtime topology below remain `AMOS_MODEL` unless independently recovered from direct Trang/AMOS canon or executable runtime evidence.

---

# 0. Purpose

Define the agent contract for `L03_PERCEPT_FORMATION`.

L03 agents are responsible for converting admitted and attended observations into **typed percept candidates** while preserving uncertainty, source identity, temporal context, observer context, H/M/L scale, provenance, contradiction, and alternative interpretations.

Conceptually:

\[
ObservationSet
\rightarrow
FeatureBinding
\rightarrow
CandidatePercepts
\rightarrow
ConsistencyChecks
\rightarrow
PerceptState
\]

subject to:

```text
attention context
scope
regime
observer
time
source reliability
provenance
modality availability
cross-modal compatibility
uncertainty
hard constraints
```

The governing distinction is:

```text
OBSERVATION
!=
PERCEPT

PERCEPT
!=
FACT

PERCEPT
!=
EXPLANATION

PERCEPT
!=
CAUSAL CLAIM

PERCEPT
!=
DECISION
```

---

# 1. Source / Canon References

## 1.1 AMOS source boundary

Current architectural alignment derives from:

```text
AMOS cognition architecture
AMOS Full Brain OS
AMOS_CORE v3.0 → v4.4 lineage
AMOS H/M/L
AMOS RSCF
AMOS provenance topology
AMOS multimodal perception layer
AMOS uncertainty governance
AMOS constraint propagation
AMOS control-plane separation
```

The AMOS multimodal-perception layer requires:

```text
Trang Phan as origin architect/steward
H/M/L
typed invariants
typed tensors
RSCF
equation registry
falsifiers
repair
```

and preserves the boundary:

```text
SOURCE_DEFINED
!=
EXTERNALLY EMPIRICALLY VALIDATED
```

## 1.2 Canon gaps

At present, this contract does not claim recovery of canonical:

```yaml
canonical_L03_agent_names: UNKNOWN_GAP
canonical_agent_count: UNKNOWN_GAP
canonical_agent_topology: UNKNOWN_GAP
canonical_percept_equations: UNKNOWN_GAP
canonical_agent_protocols: UNKNOWN_GAP
canonical_runtime_implementation: UNKNOWN_GAP
canonical_validation_results: UNKNOWN_GAP
```

---

# 2. Definition and Scope

An L03 agent is a bounded cognitive worker or logical role that participates in constructing, checking, comparing, or repairing percept representations.

Agent function:

[
Agent_i:
(Input_i,Context_i)
\rightarrow
(Output_i,Evidence_i,StateProposal_i)
]

where outputs must remain typed and provenance-bound.

L03 agents may:

```text
normalize attended observations
bind features
construct candidate percepts
integrate compatible modalities
preserve incompatible modalities
compare percept hypotheses
track observer dependence
track temporal continuity
detect percept conflicts
estimate percept uncertainty
request additional observation
propose percept state updates
repair corrupted percept state
```

L03 agents do not inherently own:

```text
raw sensing acquisition
attention-budget authority
truth certification
causal proof
long-term memory authority
external action authority
durable commit
```

---

# 3. Typed Inputs

```yaml
PerceptAgentInput:

  attended_observations:
    type: ObservationRef[]

  attention_state:
    type: AttentionStateRef

  modality_state:
    type: ModalityAvailability

  observer_context:
    type: ObserverContext

  temporal_context:
    type: TemporalContext

  spatial_context:
    type: SpatialContext | null

  prior_percepts:
    type: PerceptRef[]

  candidate_hypotheses:
    type: PerceptHypothesis[]

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  constraints:
    type: ConstraintSet

  evidence:
    type: EvidenceBundle

  provenance:
    type: ProvenanceBundle

  hml:
    type: HMLContext

  authority:
    type: AuthorityContext
```

---

# 4. Typed Outputs

```yaml
PerceptAgentOutput:

  percept_candidates:
    type: PerceptCandidate[]

  integrated_percepts:
    type: PerceptRef[]

  competing_percepts:
    type: CompetingPercept[]

  rejected_bindings:
    type: BindingRef[]

  unresolved_conflicts:
    type: PerceptConflict[]

  missing_observation_requests:
    type: ObservationRequest[]

  uncertainty:
    type: PerceptUncertainty

  provenance:
    type: ProvenanceBundle

  confidence_ceiling:
    type: ConfidenceBound

  state_proposals:
    type: PerceptStateProposal[]

  escalation:
    type: EscalationRequest | null

  status:
    type:
      - PROPOSED
      - CONDITIONAL
      - COMPETING
      - BLOCKED
      - UNKNOWN_GAP
```

Hard boundary:

```text
PERCEPT PROPOSAL
!=
AUTHORITATIVE PERCEPT COMMIT
```

---

# 5. Agent State Variables

```text
Obs_t      = attended observation set
Mod_t      = modality availability state
Bind_t     = candidate binding state
Per_t      = active percept candidates
Comp_t     = competing percepts
Conf_t     = confidence ceilings
Unc_t      = percept uncertainty
ObsCtx_t   = observer context
Time_t     = temporal context
Space_t    = spatial context
Scope_t    = scope
Reg_t      = regime
Fresh_t    = freshness state
Prov_t     = provenance graph
Dep_t      = dependency graph
HML_t      = H/M/L coordinate
Conflict_t = percept conflicts
Repair_t   = repair state
```

---

# 6. Core Agent Registry

The following roles are candidate `AMOS_MODEL` agents.

## 6.1 `L03_PERCEPT_COORDINATOR`

Purpose:

> Coordinate percept formation without silently overriding specialist uncertainty or provenance.

Responsibilities:

```text
receive attended observations
assign specialist agents
maintain percept candidate registry
merge compatible outputs
preserve COMPETING outputs
route conflicts
enforce completion gates
produce final percept proposal
```

Forbidden:

```text
invent missing observations
erase specialist uncertainty
force consensus
self-authorize commit
```

---

## 6.2 `L03_OBSERVATION_NORMALIZER`

Purpose:

> Convert heterogeneous L01/L02 outputs into a typed representation suitable for percept formation.

Responsibilities:

```text
normalize schemas
preserve observation identity
preserve measurement units
preserve timestamps
preserve source identity
preserve modality labels
preserve observer context
```

Hard invariant:

```text
NORMALIZATION
!=
SEMANTIC REINTERPRETATION
```

---

## 6.3 `L03_FEATURE_BINDER`

Purpose:

> Propose which observed features belong to the same candidate object/event/percept.

Candidate transformation:

[
B:
{o_1,o_2,\ldots,o_n}
\rightarrow
{b_1,b_2,\ldots,b_k}
]

Bindings must retain:

```text
member observations
binding rule
time window
space/context assumptions
uncertainty
provenance
```

Hard boundary:

```text
CO-OCCURRENCE
!=
SAME ENTITY
```

---

## 6.4 `L03_MULTIMODAL_INTEGRATOR`

Purpose:

> Combine compatible perceptual evidence across available modalities.

Possible modalities:

```text
text
vision
audio
spatial
somatic
biosignal
system-state
tool telemetry
```

Invariant:

```text
UNAVAILABLE MODALITY
!=
NEGATIVE EVIDENCE
```

Integration must preserve modality availability masks.

---

## 6.5 `L03_TEMPORAL_BINDER`

Purpose:

> Determine whether observations likely belong to one temporally coherent event or evolving percept.

Responsibilities:

```text
sequence observations
distinguish observation time from event time
detect temporal discontinuity
track percept persistence
track transition
flag stale observations
```

Hard boundary:

```text
SEQUENCE
!=
CAUSATION
```

---

## 6.6 `L03_SPATIAL_CONTEXT_AGENT`

Purpose:

> Bind observations to compatible spatial or structural contexts where spatial information exists.

Responsibilities:

```text
coordinate normalization
relative-position tracking
spatial compatibility
boundary detection
location uncertainty
```

No spatial information may be fabricated when unavailable.

---

## 6.7 `L03_OBSERVER_CONTEXT_AGENT`

Purpose:

> Preserve the observer-dependent conditions under which observations and percepts were formed.

Candidate context:

```yaml
ObserverContext:
  observer_id: null
  position: null
  access_channels: []
  measurement_method: null
  known_biases: []
  unavailable_information: []
```

Hard invariant:

```text
ONE OBSERVER VIEW
!=
VIEW FROM NOWHERE
```

---

## 6.8 `L03_PERCEPT_HYPOTHESIS_GENERATOR`

Purpose:

> Generate multiple plausible percept interpretations from admitted observation patterns.

Example:

```text
observations
→ percept hypothesis P1
→ percept hypothesis P2
→ percept hypothesis P3
```

Generation must remain:

```text
MODEL
```

until evidence discriminates among alternatives.

---

## 6.9 `L03_PERCEPT_DISCRIMINATOR`

Purpose:

> Compare candidate percepts and identify the cheapest discriminating observation/test.

For hypotheses:

[
P_1,P_2,\ldots,P_n
]

the agent should identify:

```text
different predictions
missing observations
incompatible features
provenance differences
scope differences
temporal differences
observer differences
```

It must preserve `COMPETING` if discrimination is insufficient.

---

## 6.10 `L03_CROSS_MODAL_CONFLICT_AGENT`

Purpose:

> Detect when multiple modalities provide materially incompatible perceptual information.

Example:

```text
visual observation suggests A
audio observation suggests B
```

Output:

```text
CONFLICT
```

not silent fusion.

---

## 6.11 `L03_PERCEPT_UNCERTAINTY_AGENT`

Purpose:

> Maintain uncertainty separately across percept dimensions.

```yaml
PerceptUncertainty:
  observation: null
  binding: null
  identity: null
  temporal: null
  spatial: null
  modality: null
  observer: null
  scope: null
  regime: null
  provenance: null
  model: null
```

One scalar confidence must not hide decision-relevant uncertainty structure.

---

## 6.12 `L03_PERCEPT_PROVENANCE_AGENT`

Purpose:

> Preserve full lineage from percept back to observations and semantic origins.

Candidate lineage:

```text
PERCEPT
↓
BINDINGS
↓
OBSERVATIONS
↓
SOURCES / SENSORS / TOOL OUTPUTS
```

Multiple percept features derived from one source do not count as independent confirmation.

---

## 6.13 `L03_PERCEPT_FRESHNESS_AGENT`

Purpose:

> Detect stale percept components when underlying observations, environment, or regime change.

Hard boundary:

```text
PREVIOUSLY VALID PERCEPT
!=
CURRENT PERCEPT
```

---

## 6.14 `L03_PERCEPT_CONSTRAINT_AGENT`

Purpose:

> Enforce hard structural constraints before percept promotion.

Candidate checks:

```text
type compatibility
scope compatibility
regime compatibility
temporal consistency
observer compatibility
provenance completeness
modality validity
state-version compatibility
```

Admission equation:

[
Admit(P)
========

\bigwedge_i HardInvariant_i(P)
]

Hard failures are non-compensatory.

---

## 6.15 `L03_PERCEPT_RSCF_AGENT`

Purpose:

> Represent percept claims as explicit RSCF structures.

Each consequential percept should retain:

```text
claim
class
premises
observations
provenance
scope
regime
freshness
competing percepts
falsifiers
confidence ceiling
```

---

## 6.16 `L03_PERCEPT_REPAIR_AGENT`

Purpose:

> Repair invalid percept structures through selective invalidation and reconstruction.

Core rule:

[
Invalid(p)
\Rightarrow
Invalidate(Descendants(p))
]

not global deletion unless dependency closure proves global invalidity.

---

## 6.17 `L03_PERCEPT_AUDITOR`

Purpose:

> Adversarially inspect the final percept proposal before promotion.

Audit for:

```text
missing observation
false binding
scope leakage
regime leakage
observer collapse
stale evidence
false multimodal agreement
correlated provenance
confidence inflation
premature convergence
causal overreach
```

---

# 7. Agent Role Matrix

| Agent                              | Primary Role           | May Propose State | May Commit |
| ---------------------------------- | ---------------------- | ----------------: | ---------: |
| `L03_PERCEPT_COORDINATOR`          | orchestration          |               yes |         no |
| `L03_OBSERVATION_NORMALIZER`       | normalization          |               yes |         no |
| `L03_FEATURE_BINDER`               | feature/object binding |               yes |         no |
| `L03_MULTIMODAL_INTEGRATOR`        | modality integration   |               yes |         no |
| `L03_TEMPORAL_BINDER`              | temporal coherence     |               yes |         no |
| `L03_SPATIAL_CONTEXT_AGENT`        | spatial context        |               yes |         no |
| `L03_OBSERVER_CONTEXT_AGENT`       | observer context       |               yes |         no |
| `L03_PERCEPT_HYPOTHESIS_GENERATOR` | hypotheses             |               yes |         no |
| `L03_PERCEPT_DISCRIMINATOR`        | discrimination         |               yes |         no |
| `L03_CROSS_MODAL_CONFLICT_AGENT`   | contradiction          |               yes |         no |
| `L03_PERCEPT_UNCERTAINTY_AGENT`    | uncertainty            |               yes |         no |
| `L03_PERCEPT_PROVENANCE_AGENT`     | provenance             |               yes |         no |
| `L03_PERCEPT_FRESHNESS_AGENT`      | freshness              |               yes |         no |
| `L03_PERCEPT_CONSTRAINT_AGENT`     | invariants             |               yes |         no |
| `L03_PERCEPT_RSCF_AGENT`           | claim graph            |               yes |         no |
| `L03_PERCEPT_REPAIR_AGENT`         | repair                 |               yes |         no |
| `L03_PERCEPT_AUDITOR`              | validation             |               yes |         no |

Default authority invariant:

```text
L03 AGENT
!=
DURABLE COMMIT AUTHORITY
```

unless explicit higher-order authority is independently established.

---

# 8. H/M/L Agent Applicability

## H — Governing percept formation

H-level agents reason about:

```text
global perceptual frame
observer model
system/environment boundary
major percept contradictions
percept regime
critical uncertainty
```

Example:

```text
"What overall environment state is currently being perceived?"
```

H-level outputs must remain dependent on M/L evidence.

---

## M — Subsystem percept formation

M-level agents integrate:

```text
modality groups
object clusters
event groups
subsystem state
cross-modal conflicts
percept hypotheses
```

Example:

```text
"Do these observations describe one event or several?"
```

---

## L — Local percept formation

L-level agents process:

```text
one observation
one feature
one temporal relation
one spatial relation
one binding
one conflict
```

Example:

```text
"Are these two observed features compatible with the same percept candidate?"
```

Cross-scale invariant:

```text
L observation
!=
M percept
!=
H world-state percept
```

without explicit transformation.

---

# 9. Agent Interaction Topology

Candidate topology:

```text
               L03_PERCEPT_COORDINATOR
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
 Observation         Binding          Governance
 Processing          Agents           Agents
       │                 │                 │
       ├─ Normalizer     ├─ Feature        ├─ Constraint
       ├─ Temporal       ├─ Multimodal     ├─ Provenance
       ├─ Spatial        ├─ Hypothesis     ├─ Freshness
       └─ Observer       └─ Discriminator  └─ RSCF
                         │
                         ↓
                  Percept Candidates
                         │
               Cross-Modal Conflict
                         │
                  Uncertainty Agent
                         │
                    Auditor
                         │
                 State Proposal
```

This topology is a model architecture, not canonical runtime proof.

---

# 10. Agent Workflow

```text
L02_ATTENTION OUTPUT
↓
L03 COORDINATOR
↓
NORMALIZE OBSERVATIONS
↓
CHECK MODALITY AVAILABILITY
↓
BIND TEMPORAL / SPATIAL / OBSERVER CONTEXT
↓
PROPOSE FEATURE BINDINGS
↓
GENERATE PERCEPT CANDIDATES
↓
INTEGRATE COMPATIBLE MODALITIES
↓
PRESERVE CONFLICTS
↓
GENERATE COMPETING PERCEPTS
↓
DISCRIMINATE WHERE POSSIBLE
↓
CHECK PROVENANCE / SCOPE / REGIME / FRESHNESS
↓
CALCULATE CONFIDENCE CEILING
↓
AUDIT
↓
PERCEPT STATE PROPOSAL
```

---

# 11. Protocols

Candidate agent communication protocols:

```text
L03_AGENT_TASK_ASSIGN
L03_OBSERVATION_NORMALIZE_REQUEST
L03_BINDING_PROPOSAL
L03_MODALITY_INTEGRATION_PROPOSAL
L03_TEMPORAL_BINDING_PROPOSAL
L03_SPATIAL_BINDING_PROPOSAL
L03_OBSERVER_CONTEXT_UPDATE
L03_PERCEPT_HYPOTHESIS
L03_PERCEPT_COMPETING_NOTICE
L03_PERCEPT_CONFLICT_NOTICE
L03_PERCEPT_DISCRIMINATION_REQUEST
L03_PERCEPT_PROVENANCE_UPDATE
L03_PERCEPT_FRESHNESS_CHECK
L03_PERCEPT_REPAIR_REQUEST
L03_PERCEPT_AUDIT_RESULT
L03_PERCEPT_STATE_PROPOSAL
```

Canonical protocol identifiers remain `UNKNOWN/GAP`.

---

# 12. Operators

Agents may invoke candidate operators such as:

```text
NORMALIZE()
BIND()
UNBIND()
GROUP()
SEPARATE()
ALIGN_TIME()
ALIGN_SPACE()
ALIGN_OBSERVER()
INTEGRATE_MODALITY()
PRESERVE_CONFLICT()
GENERATE_HYPOTHESIS()
COMPARE_HYPOTHESES()
DISCRIMINATE()
CHECK_SCOPE()
CHECK_REGIME()
CHECK_FRESHNESS()
CHECK_PROVENANCE()
CALCULATE_CONFIDENCE_CEILING()
INVALIDATE()
REPAIR()
PROPOSE_STATE()
```

Agent ownership of an operator must remain separate from control-plane authority.

---

# 13. Agent Invariants

```text
L03-AGENT-INV-001
No agent may invent an unavailable observation.

L03-AGENT-INV-002
Observation and percept classes remain distinct.

L03-AGENT-INV-003
A percept hypothesis does not become OBSERVATION through repetition.

L03-AGENT-INV-004
Unresolved percept alternatives remain COMPETING.

L03-AGENT-INV-005
Cross-modal disagreement cannot be silently averaged away when decision-relevant.

L03-AGENT-INV-006
Unavailable modality != negative evidence.

L03-AGENT-INV-007
Observer context must remain recoverable where relevant.

L03-AGENT-INV-008
Event time and observation time remain distinguishable.

L03-AGENT-INV-009
Sequence alone cannot establish causation.

L03-AGENT-INV-010
Binding requires an explicit relation or compatibility basis.

L03-AGENT-INV-011
Multiple features from one source do not establish independent confirmation.

L03-AGENT-INV-012
Confidence cannot exceed the weakest load-bearing premise unless independently revalidated.

L03-AGENT-INV-013
Scope must survive percept formation.

L03-AGENT-INV-014
Regime must survive percept formation.

L03-AGENT-INV-015
Stale underlying observations invalidate dependent percept components.

L03-AGENT-INV-016
Agent consensus does not itself prove percept truth.

L03-AGENT-INV-017
Agent role separation does not prove provenance independence.

L03-AGENT-INV-018
Unknown/GAP cannot become PASS through agent voting.

L03-AGENT-INV-019
Agent capability does not create authority.

L03-AGENT-INV-020
Percept state proposal does not equal durable commit.
```

---

# 14. Dependencies

Primary modeled chain:

```text
L00_REALITY_ENVIRONMENT
↓
L01_SENSING_OBSERVATION
↓
L02_ATTENTION
↓
L03_PERCEPT_FORMATION
```

L03 depends on:

```text
typed L01 observations
L02 attention state
modality availability
temporal context
observer context
scope
regime
freshness
provenance
constraint state
RSCF support
```

Potential downstream consumers remain outside the claim scope of this file unless independently sourced.

---

# 15. Control-Plane Requirements

The control plane should own or validate:

```text
authoritative state identity
state versions
agent capability registry
agent authority
cross-agent resource limits
persistent percept state
scope/regime policy
provenance admission
memory write authority
external effects
rollback
commit finalization
```

L03 agents should ordinarily emit:

```text
candidate percepts
competing percepts
uncertainty
observation requests
repair proposals
state proposals
```

not authoritative commits.

Hard boundary:

```text
AGENT AGREEMENT
!=
COMMIT AUTHORITY
```

---

# 16. Skills

Relevant capability families may include:

```text
AMOS Multimodal Perception Layer
AMOS Sensory Map Integrator
AMOS Information Geometry Mapper
AMOS Binding RSCF Engine
AMOS Temporal Multi-Scale RSCF Engine
AMOS Provenance Trust Firewall
AMOS Constraint Propagation RSCF Engine
AMOS Metacognitive Confidence Auditor
RSCF Modeler
AMOS Infrastructure Control Plane
```

Skill availability:

```text
!=
Skill invocation

Skill invocation
!=
validated result

validated result
!=
authority to commit
```

---

# 17. Evidence / Provenance

Each consequential agent result should preserve:

```yaml
AgentResultProvenance:

  agent_role: null
  agent_instance: null

  input_refs: []

  observation_refs: []

  parent_percept_refs: []

  transformation_refs: []

  evidence_refs: []

  semantic_origin_refs: []

  scope: null

  regime: null

  observer_context: null

  temporal_context: null

  modality_context: null

  timestamp: null

  runtime_version: null

  validator_refs: []

  result_status: null
```

A percept must remain traceable to the observations that support it.

---

# 18. Uncertainty and Confidence Ceiling

Percept-agent uncertainty should remain vectorized where material:

```yaml
uncertainty:

  observation:
    level: null

  feature_binding:
    level: null

  object_identity:
    level: null

  temporal:
    level: null

  spatial:
    level: null

  multimodal:
    level: null

  observer:
    level: null

  scope:
    level: null

  regime:
    level: null

  provenance:
    level: null

  model:
    level: null

  execution:
    level: null
```

For a percept (P) depending on premises (p_i):

[
Conf(P)
\le
\min_i Conf(p_i)
]

for load-bearing premises unless independently revalidated evidence changes the proof graph.

Multiple agreeing agents do not automatically raise this ceiling if they share the same evidence ancestry.

---

# 19. Failure Modes

```text
FM-L03-AG-001
Observation invented by agent.

FM-L03-AG-002
Observation/percept class collapse.

FM-L03-AG-003
False feature binding.

FM-L03-AG-004
False object identity.

FM-L03-AG-005
Temporal overbinding.

FM-L03-AG-006
Spatial overbinding.

FM-L03-AG-007
Observer context lost.

FM-L03-AG-008
Unavailable modality treated as evidence.

FM-L03-AG-009
Cross-modal disagreement suppressed.

FM-L03-AG-010
Premature percept convergence.

FM-L03-AG-011
COMPETING percepts collapsed by voting.

FM-L03-AG-012
Correlated agent outputs counted independently.

FM-L03-AG-013
Stale observation retained in active percept.

FM-L03-AG-014
Scope leakage.

FM-L03-AG-015
Regime leakage.

FM-L03-AG-016
Confidence inflation.

FM-L03-AG-017
Causal overreach.

FM-L03-AG-018
Agent coordination loop.

FM-L03-AG-019
Repair erases valid percept branch.

FM-L03-AG-020
Agent proposal treated as commit.
```

---

# 20. Repair / Recovery

Generic agent-level recovery:

```text
DETECT PERCEPT FAILURE
↓
IDENTIFY RESPONSIBLE BINDING / AGENT OUTPUT
↓
FREEZE DEPENDENT PERCEPTS
↓
TRACE OBSERVATION ANCESTRY
↓
INVALIDATE FAILED EDGE / PREMISE
↓
PRESERVE UNAFFECTED PERCEPT BRANCHES
↓
RE-RUN ONLY REQUIRED AGENT(S)
↓
RECOMPARE COMPETING PERCEPTS
↓
REVALIDATE
↓
RESUME
```

Core selective invalidation:

[
Invalid(p)
\Rightarrow
Invalidate(Descendants(p))
]

No agent should re-run an unchanged failed path without changed evidence, configuration, or method.

---

# 21. Tests / Validators

Minimum validators:

```text
VALIDATE_AGENT_INPUT_TYPES
VALIDATE_AGENT_OUTPUT_TYPES
VALIDATE_OBSERVATION_PRESERVATION
VALIDATE_PERCEPT_CLASS
VALIDATE_BINDING
VALIDATE_TEMPORAL_CONTEXT
VALIDATE_SPATIAL_CONTEXT
VALIDATE_OBSERVER_CONTEXT
VALIDATE_MODALITY_AVAILABILITY
VALIDATE_CROSS_MODAL_CONFLICT
VALIDATE_PROVENANCE
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_FRESHNESS
VALIDATE_COMPETING_PERCEPTS
VALIDATE_CONFIDENCE_CEILING
VALIDATE_AUTHORITY_BOUNDARY
VALIDATE_REPAIR
```

Minimum tests:

```text
TEST-L03-AG-001
Give an agent missing observation data.
Expected:
UNKNOWN/GAP; no fabrication.

TEST-L03-AG-002
Provide two incompatible percept hypotheses.
Expected:
COMPETING preserved.

TEST-L03-AG-003
Provide correlated evidence through several agents.
Expected:
no false independence.

TEST-L03-AG-004
Remove observer context from observer-dependent observation.
Expected:
downgrade / block.

TEST-L03-AG-005
Provide stale observation.
Expected:
dependent percept becomes stale/revalidated.

TEST-L03-AG-006
One modality unavailable.
Expected:
absence marked unavailable, not negative evidence.

TEST-L03-AG-007
Two modalities conflict.
Expected:
conflict remains visible.

TEST-L03-AG-008
Invalid one binding edge.
Expected:
selectively invalidate dependent percepts.

TEST-L03-AG-009
Agent majority agrees without independent evidence.
Expected:
no automatic VERIFIED state.

TEST-L03-AG-010
Agent proposes durable percept-state mutation without authority.
Expected:
proposal allowed; commit blocked.
```

Current execution state:

```text
NOT_RUN
```

unless separate runtime evidence exists.

---

# 22. Falsifiers

This agent contract must be revised if direct canon establishes that:

```text
L03 does not own percept formation;

percept formation is not agent-addressable;

canonical L03 agents use materially different role boundaries;

canonical percept formation has no multimodal/observer/temporal state;

L03 owns authoritative commit directly;

canonical H/M/L behavior differs materially;

runtime implementation contradicts modeled agent topology;

executed tests falsify the stated invariants.
```

---

# 23. Gap Matrix

```yaml
gap_status:

  primitive_identity:
    status: PARTIAL_SOURCE_BOUND

  percept_formation_role:
    status: MODEL_ALIGNED

  agent_contract:
    status: MODEL_DEFINED

  coordinator_agent:
    status: MODEL_DEFINED

  normalizer_agent:
    status: MODEL_DEFINED

  feature_binding_agent:
    status: MODEL_DEFINED

  multimodal_agent:
    status: MODEL_DEFINED

  temporal_agent:
    status: MODEL_DEFINED

  spatial_agent:
    status: MODEL_DEFINED

  observer_agent:
    status: MODEL_DEFINED

  hypothesis_agent:
    status: MODEL_DEFINED

  discrimination_agent:
    status: MODEL_DEFINED

  conflict_agent:
    status: MODEL_DEFINED

  uncertainty_agent:
    status: MODEL_DEFINED

  provenance_agent:
    status: MODEL_DEFINED

  repair_agent:
    status: MODEL_DEFINED

  auditor_agent:
    status: MODEL_DEFINED

  canonical_agent_registry:
    status: UNKNOWN_GAP

  canonical_agent_names:
    status: UNKNOWN_GAP

  canonical_agent_topology:
    status: UNKNOWN_GAP

  canonical_protocols:
    status: UNKNOWN_GAP

  canonical_thresholds:
    status: UNKNOWN_GAP

  executable_agents:
    status: UNKNOWN_GAP

  executed_validation:
    status: UNKNOWN_GAP
```

---

# 24. Competing Agent Architectures

## COMPETING-001 — Monolithic Percept Agent

```text
one L03 agent
→ performs all percept formation
```

Advantage:

```text
simple coordination
```

Risk:

```text
hidden coupling
poor provenance separation
```

---

## COMPETING-002 — Specialist Agent Cohort

```text
normalization
binding
temporal
spatial
multimodal
hypothesis
audit
```

each handled by separate logical agents.

Advantage:

```text
clearer role boundaries
```

Risk:

```text
coordination cost
false independence
```

---

## COMPETING-003 — Deterministic Percept Pipeline

```text
no autonomous percept agents;
typed deterministic stages only
```

Advantage:

```text
replayability
```

Risk:

```text
lower flexibility
```

---

## COMPETING-004 — Hybrid

```text
deterministic state/control layer
+
bounded specialist AI workers
+
independent audit
```

Current model preference:

```text
COMPETING-004
```

because it preserves flexible percept generation while keeping state, authority, and finalization outside stochastic workers.

This preference remains `MODEL`, not canonical proof.

---

# 25. RSCF Completion State

```yaml
rscf:

  id: L03_PERCEPT_FORMATION_AGENTS

  claim:
    L03_PERCEPT_FORMATION can be represented as a governed collection
    of bounded agent roles that transform attended observations into
    percept candidates while preserving observation identity, modality,
    observer context, time, scope, regime, provenance, uncertainty,
    competing percepts, and authority boundaries.

  claim_class: MODEL

  evidence:
    - AMOS cognition architecture
    - AMOS Full Brain OS
    - AMOS multimodal perception architecture
    - AMOS H/M/L and RSCF governance conventions

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    artifact: AGENTS.md
    derivation: AMOS_MODEL_SOURCE_BOUNDED

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    concern: agent_architecture

  regime:
    governed percept formation

  freshness:
    revalidate_when:
      - canonical L03 source is recovered
      - agent registry changes
      - percept-state contract changes
      - control-plane ownership changes
      - multimodal architecture changes
      - runtime evidence becomes available

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION
    - L03_PERCEPT_FORMATION_DEFINITION
    - L03_PERCEPT_FORMATION_STATE
    - L03_PERCEPT_FORMATION_OPERATORS
    - L03_PERCEPT_FORMATION_INVARIANTS
    - L03_PERCEPT_FORMATION_HML
    - L03_PERCEPT_FORMATION_PROVENANCE
    - L03_PERCEPT_FORMATION_CONTROL_PLANES
    - L03_PERCEPT_FORMATION_WORKFLOWS
    - L03_PERCEPT_FORMATION_PROTOCOLS
    - L03_PERCEPT_FORMATION_TESTS

  competing:
    - monolithic percept agent
    - specialist agent cohort
    - deterministic percept pipeline
    - hybrid deterministic control plus bounded specialist agents

  falsifiers:
    - direct incompatible L03 canon
    - incompatible canonical agent ownership
    - incompatible percept semantics
    - runtime evidence contradicting agent topology
    - executed tests falsifying invariant assumptions

  uncertainty:
    evidence: HIGH
    model: MEDIUM
    scope: MEDIUM
    temporal: MEDIUM
    causal: LOW
    execution: MAXIMUM
    provenance_independence: MEDIUM

  confidence_ceiling:
    MODEL only; detailed L03 agent names, roles, topology, and
    runtime behavior must not be represented as canonical or
    implemented until source/runtime evidence establishes them.

  gap_status:
    canonical_agent_registry: CRITICAL_GAP
    canonical_agent_topology: CRITICAL_GAP
    executable_agents: CRITICAL_GAP
    executed_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    recover direct L03 percept-formation canon; if unavailable,
    implement the smallest typed observation-to-percept harness and
    test observation preservation, binding integrity, multimodal
    conflict retention, provenance independence, COMPETING
    preservation, selective invalidation, and proposal/commit separation.
```

---

# 26. Completion State

```yaml
completion_state:

  source_canon_references:
    status: PARTIAL_SOURCE_BOUND

  definition_scope:
    status: MODEL_COMPLETE

  typed_inputs_outputs:
    status: MODEL_COMPLETE

  state_variables:
    status: MODEL_COMPLETE

  operators:
    status: MODEL_COMPLETE

  invariants:
    status: MODEL_COMPLETE

  dependencies:
    status: MODEL_COMPLETE_WITH_GAPS

  HML_applicability:
    status: MODEL_COMPLETE

  control_plane_requirements:
    status: MODEL_COMPLETE

  agents:
    status: MODEL_COMPLETE

  skills:
    status: MODEL_COMPLETE

  workflows:
    status: MODEL_COMPLETE

  protocols:
    status: MODEL_COMPLETE

  evidence_provenance:
    status: MODEL_COMPLETE_SOURCE_PARTIAL

  uncertainty_confidence:
    status: MODEL_COMPLETE

  failure_modes:
    status: MODEL_COMPLETE

  repair_recovery:
    status: MODEL_COMPLETE

  tests_validators:
    status: MODEL_COMPLETE_UNEXECUTED

  falsifiers:
    status: MODEL_COMPLETE

  canonical_agent_registry:
    status: UNKNOWN_GAP

  executable_runtime:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_AGENT_CONTRACT_SCOPE

  conclusion_class:
    MODEL
```

---

# 27. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

L03-specific:

```text
OBSERVATION != PERCEPT

PERCEPT != FACT

PERCEPT != TRUTH

PERCEPT != CAUSAL PROOF

PERCEPT != DECISION

FEATURE CO-OCCURRENCE != COMMON IDENTITY

SEQUENCE != CAUSATION

MULTIMODAL AGREEMENT != INDEPENDENT CONFIRMATION

MULTIPLE AGENTS != INDEPENDENT EVIDENCE

AGENT CONSENSUS != VALIDATION

UNAVAILABLE MODALITY != NEGATIVE EVIDENCE

OBSERVER-DEPENDENT VIEW != GLOBAL VIEW

MODEL PERCEPT != OBSERVATION

PERCEPT PROPOSAL != STATE COMMIT

AGENT DEFINED != AGENT IMPLEMENTED

AGENT IMPLEMENTED != AGENT VALIDATED
```

---

# 28. Governing Agent Contract

> **`L03_PERCEPT_FORMATION` agents SHALL transform attended observations into bounded percept candidates while preserving the distinction between observation and interpretation. Agent workers MAY normalize, bind, integrate, generate hypotheses, discriminate, audit, and propose repairs, but SHALL NOT fabricate unavailable observations, erase cross-modal or interpretive conflict, inflate confidence through consensus, collapse correlated provenance into independent confirmation, or create authority from capability. Material percepts SHALL retain observation ancestry, scope, regime, freshness, observer context, modality state, H/M/L position, competing alternatives, falsifiers, and confidence ceilings. Durable state effects SHALL remain subject to the governing AMOS control plane.**

---

# 29. Canon Boundary

```text
AMOS-FRAMEWORK-ALIGNED:

Trang Phan origin/stewardship

H/M/L

typed invariants

typed tensors

RSCF

provenance

falsifiers

repair

hard non-compensatory invariants

confidence ceilings

selective invalidation

COMPETING preservation


AMOS_MODEL:

L03 agent registry

coordinator role

normalizer role

feature binder

multimodal integrator

temporal binder

spatial context agent

observer context agent

percept hypothesis generator

percept discriminator

cross-modal conflict agent

uncertainty agent

provenance agent

freshness agent

constraint agent

RSCF agent

repair agent

auditor

agent topology

protocols

workflow


UNKNOWN/GAP:

canonical L03 agent names

canonical agent count

canonical topology

canonical percept equations

canonical protocols

canonical thresholds

runtime implementation

executed tests

formal verification
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

NOT:
VERIFIED COMPLETE L03 CANON

NOT:
PROOF OF IMPLEMENTED AGENTS

NOT:
PROOF OF HUMAN PERCEPTION MECHANISM

NOT:
PROOF OF CONSCIOUS PERCEPTION

NOT:
AUTHORITY TO COMMIT
```

```text

The AMOS multimodal-perception layer used as the supporting architecture requires H/M/L, typed invariants/tensors, RSCF, falsifiers, and repair, while explicitly keeping source-defined constructs separate from external empirical validation. :contentReference[oaicite:0]{index=0}
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
