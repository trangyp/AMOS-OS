---
type: cognitive
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION
tags: [amos, cognitive-matrix, l03, percept-formation, hml, cross-scale, rscf, provenance, governance, canon/cognitive-matrix]

title: "L03_PERCEPT_FORMATION — HML"
origin_architect: "Trang Phan"
status: "MODEL_HML_CONTRACT / UNIMPLEMENTED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# L03_PERCEPT_FORMATION — HML

**Class:** `COGNITIVE_PRIMITIVE_HML_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L03_PERCEPT_FORMATION`  
**Artifact:** `HML.md`  
**Status:** `AMOS_MODEL / UNIMPLEMENTED / UNVALIDATED`

> **Source boundary:** The AMOS Cross-Scale RSCF Tensor Engine defines the governing H/M/L model through typed cross-scale tensors, upward aggregation, downward constraint, explicit transformation edges, confidence ceilings, selective invalidation, scope/regime/observer propagation, sensitivity testing, and RSCF-bound tensor cells. It explicitly states that aggregation does not prove identity, local correlation does not prove macro causation, macro stability can coexist with local collapse, and downward constraint must remain distinct from downward causation. 

---

# 0. Purpose

Define how `L03_PERCEPT_FORMATION` operates across:

```text
H = high / governing / global percept structure
M = middle / object-event-subsystem percept structure
L = local / feature-observation percept structure
```

without silently promoting:

```text
local features
→ object identity

object percepts
→ global scene truth

high-level interpretation
→ rewritten low-level observation
```

The L03 H/M/L contract must support both:

```text
UPWARD FORMATION
L → M → H
```

and:

```text
DOWNWARD CONSTRAINT
H → M → L
```

while preserving the causal firewall:

```text
AGGREGATION != IDENTITY

CONSTRAINT != CAUSATION

LOCAL CORRELATION != MACRO CAUSATION

GLOBAL COHERENCE != LOCAL VALIDITY
```

---

# 1. Source / Canon References

## 1.1 Source-aligned H/M/L architecture

The AMOS Cross-Scale RSCF Tensor Engine defines the model state:

[
X[h,m,l,t,r,o,f]
]

where H/M/L state is jointly indexed with:

```text
time
regime
observer
field/context
```

It provides source-aligned upward transforms:

[
X_M=A_{L\rightarrow M}(X_L)
]

[
X_H=A_{M\rightarrow H}(X_M)
]

and downward constraints:

[
X'*M=C*{H\rightarrow M}(X_H,X_M)
]

[
X'*L=C*{M\rightarrow L}(X'_M,X_L)
]

together with the general cross-scale update:

[
\Delta X_s(t+1)
===============

\sum_q T_{q\rightarrow s}\Delta X_q(t)+u_s-d_s
]

These equations are explicitly AMOS `MODEL`, not claims of universal cognitive law.

## 1.2 Direct L03 H/M/L canon status

```yaml
canonical_L03_HML_definition: UNKNOWN_GAP
canonical_L03_H_level: UNKNOWN_GAP
canonical_L03_M_level: UNKNOWN_GAP
canonical_L03_L_level: UNKNOWN_GAP
canonical_L_to_M_transform: UNKNOWN_GAP
canonical_M_to_H_transform: UNKNOWN_GAP
canonical_H_to_M_constraint: UNKNOWN_GAP
canonical_M_to_L_constraint: UNKNOWN_GAP
canonical_cross_scale_thresholds: UNKNOWN_GAP
canonical_L03_HML_runtime: UNKNOWN_GAP
```

Therefore the L03-specific mappings below are `AMOS_MODEL`.

---

# 2. Definition and Scope

`L03_PERCEPT_FORMATION/HML` defines how perceptual state is represented, transformed, constrained, validated, and repaired across local, middle, and high levels.

Working model:

[
X^{L03}
=======

X[h,m,l,t,r,o,f]
]

with:

```text
h = high-level percept state
m = middle-level percept state
l = local percept state
t = temporal coordinate
r = regime
o = observer
f = perceptual field/context
```

The H/M/L model is not merely hierarchical summarization.

It must preserve:

```text
dependency lineage
transformation type
scope
regime
observer
freshness
provenance
confidence ceiling
heterogeneity
competing percepts
falsifiers
```

at each transformation.

---

# 3. H/M/L Semantic Levels

## 3.1 L — Local Percept Formation

`L` contains the lowest perceptual units relevant to L03.

Candidate examples:

```text
single observed feature
local signal
token or phrase feature
visual edge
local color patch
audio transient
localized motion
timestamp relation
single spatial relation
one modality cue
one observation-feature binding
```

Candidate typed state:

```yaml
L03LocalPerceptState:
  level: L

  observation_refs: []
  feature_refs: []
  local_bindings: []

  modality: null
  observer: null

  time: null
  spatial_context: null

  scope: null
  regime: null
  freshness: null

  provenance: []

  uncertainty: null
  confidence_ceiling: null

  status:
    - VALID
    - CONDITIONAL
    - COMPETING
    - INVALID
    - UNKNOWN_GAP
```

Hard boundary:

```text
LOCAL FEATURE
!=
OBJECT
```

---

## 3.2 M — Middle Percept Formation

`M` represents percepts composed from multiple local observations/features.

Candidate examples:

```text
object candidate
event candidate
speaker candidate
movement pattern
localized scene region
cross-modal object hypothesis
bounded event structure
subsystem percept
```

Candidate state:

```yaml
L03MiddlePerceptState:
  level: M

  percept_id: null

  local_dependencies: []

  object_or_event_type: null

  binding_state: null

  temporal_structure: null
  spatial_structure: null
  modality_structure: null

  competing_percepts: []

  scope: null
  regime: null
  observer: null
  freshness: null

  provenance: []

  uncertainty: null
  confidence_ceiling: null

  status:
    - VALID
    - CONDITIONAL
    - COMPETING
    - INVALID
    - UNKNOWN_GAP
```

Hard boundary:

```text
MULTIPLE FEATURES
!=
PROVEN OBJECT IDENTITY
```

---

## 3.3 H — High Percept Formation

`H` represents governing or global percept structure.

Candidate examples:

```text
scene-level percept
environmental configuration
global event interpretation
overall system situation
world-state percept frame
large-scale multimodal organization
```

Candidate state:

```yaml
L03HighPerceptState:
  level: H

  percept_frame_id: null

  middle_dependencies: []

  scene_or_global_structure: null

  unresolved_regions: []

  competing_global_percepts: []

  scope: null
  regime: null
  observer: null
  freshness: null

  provenance: []

  uncertainty: null
  confidence_ceiling: null

  status:
    - VALID
    - CONDITIONAL
    - COMPETING
    - INVALID
    - UNKNOWN_GAP
```

Hard boundary:

```text
GLOBAL COHERENCE
!=
GLOBAL TRUTH
```

---

# 4. Typed Inputs

```yaml
L03HMLInput:

  local_observations:
    type: ObservationRef[]

  local_features:
    type: FeatureRef[]

  existing_middle_percepts:
    type: PerceptRef[]

  existing_high_percepts:
    type: PerceptRef[]

  attention_state:
    type: AttentionStateRef

  modality_state:
    type: ModalityAvailability

  temporal_context:
    type: TemporalContext

  spatial_context:
    type: SpatialContext | null

  observer_context:
    type: ObserverContext

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  provenance:
    type: ProvenanceBundle

  dependency_graph:
    type: DependencyGraph

  constraints:
    type: ConstraintSet

  authority_context:
    type: AuthorityContext
```

---

# 5. Typed Outputs

```yaml
L03HMLOutput:

  local_state:
    type: L03LocalPerceptState[]

  middle_state:
    type: L03MiddlePerceptState[]

  high_state:
    type: L03HighPerceptState[]

  upward_transforms:
    type: HMLTransform[]

  downward_constraints:
    type: HMLConstraint[]

  competing_cross_scale_models:
    type: CompetingHMLModel[]

  invalidated_nodes:
    type: PerceptRef[]

  unresolved_cross_scale_gaps:
    type: HMLGap[]

  uncertainty:
    type: HMLUncertainty

  confidence_ceiling:
    type: ConfidenceBound

  provenance:
    type: ProvenanceBundle

  status:
    type:
      - VALID
      - CONDITIONAL
      - COMPETING
      - INVALID
      - UNKNOWN_GAP

  commit_authority:
    type: NONE
```

---

# 6. State Variables

Candidate H/M/L state:

[
X^{L03}_{t}
===========

(X^H_t,X^M_t,X^L_t)
]

with supporting state:

```text
D_t     = cross-scale dependency graph
T_t     = cross-scale transforms
C_t     = downward constraints
Prov_t  = provenance topology
U_t     = uncertainty
Conf_t  = confidence ceilings
Scope_t = scope
Reg_t   = regime
Obs_t   = observer context
Fresh_t = freshness
Gap_t   = unresolved H/M/L gaps
Comp_t  = competing cross-scale interpretations
```

Extended tensor:

[
X^{L03}[h,m,l,t,r,o,f]
]

remains the preferred AMOS MODEL representation where multiple scale, temporal, regime, observer, and field coordinates matter.

---

# 7. Core H/M/L Operators

```text
REGISTER_LOCAL()
REGISTER_MIDDLE()
REGISTER_HIGH()

MAP_L_TO_M()
MAP_M_TO_H()

CONSTRAIN_H_TO_M()
CONSTRAIN_M_TO_L()

TRACE_UPWARD()
TRACE_DOWNWARD()

AGGREGATE()
DECOMPOSE()

PRESERVE_HETEROGENEITY()

CHECK_HML_COMPATIBILITY()
CHECK_CROSS_SCALE_SCOPE()
CHECK_CROSS_SCALE_REGIME()
CHECK_CROSS_SCALE_PROVENANCE()
CHECK_CROSS_SCALE_CONFIDENCE()

INVALIDATE_CROSS_SCALE_DESCENDANTS()
REVALIDATE_SCALE()
REPAIR_SCALE_MAPPING()

PROPOSE_HML_STATE()
```

Canonical operator names remain `UNKNOWN/GAP`.

---

# 8. Upward Formation

## 8.1 L → M

Source-aligned form:

[
X_M=A_{L\rightarrow M}(X_L)
]

L03 specialization:

[
P^M_j
=====

A^{L03}*{L\rightarrow M}
(
P^L*{1:n},
R_{LM},
K
)
]

where:

```text
P^L = local percept state
P^M = middle percept candidate
R_LM = typed aggregation/binding relation
K = applicable constraints
```

Example:

```text
L:
  shape cue
  motion cue
  temporal cue
  spatial cue

↓ typed binding

M:
  moving-object candidate
```

Hard rule:

```text
L AGGREGATION
!=
REAL-WORLD IDENTITY PROOF
```

This directly follows the source invariant that aggregation does not prove identity.

---

## 8.2 M → H

Source-aligned form:

[
X_H=A_{M\rightarrow H}(X_M)
]

L03 specialization:

[
P^H_k
=====

A^{L03}*{M\rightarrow H}
(
P^M*{1:n},
R_{MH},
K
)
]

Example:

```text
M:
  moving vehicle A
  moving vehicle B
  road region
  signal structure

↓ governed aggregation

H:
  traffic-scene percept candidate
```

Hard boundary:

```text
MIDDLE-LEVEL AGREEMENT
!=
GLOBAL TRUTH
```

---

# 9. Downward Constraint

## 9.1 H → M

Source-aligned:

[
X'*M=C*{H\rightarrow M}(X_H,X_M)
]

L03 interpretation:

High-level percept state may constrain which middle-level percepts remain plausible.

Example:

```text
H:
  indoor-room percept

M candidates:
  chair
  wall
  doorway
  cloud
```

The H-level state may alter plausibility of `cloud` as an indoor object candidate.

But:

```text
DOWNWARD CONSTRAINT
!=
DOWNWARD CAUSATION
```

and:

```text
HIGH-LEVEL EXPECTATION
!=
LICENSE TO DELETE CONTRADICTORY OBSERVATION
```

The cross-scale source explicitly requires downward constraint to remain distinct from downward causation.

---

## 9.2 M → L

Source-aligned:

[
X'*L=C*{M\rightarrow L}(X'_M,X_L)
]

L03 specialization:

Middle-level object/event hypotheses may guide local feature interpretation.

Example:

```text
M:
  vehicle candidate

L:
  ambiguous contour
```

The object hypothesis may alter interpretation priority, but must not rewrite the local observation itself.

Hard rule:

```text
INTERPRETATION CONDITIONING
!=
OBSERVATION MODIFICATION
```

---

# 10. General Cross-Scale Update

Source-aligned AMOS model:

[
\Delta X_s(t+1)
===============

\sum_q T_{q\rightarrow s}\Delta X_q(t)+u_s-d_s
]

where (T_{q\rightarrow s}) are typed cross-scale transformations.

L03 interpretation:

```text
state change at L
may influence M and H

state change at H
may constrain M and L

but propagation is dependency-specific
```

No universal numeric form for (T), (u_s), or (d_s) is asserted.

---

# 11. H/M/L Dependency Graph

Candidate graph:

```text
                H PERCEPT FRAME
                 /    |     \
                /     |      \
               ▼      ▼       ▼
             M1      M2      M3
            /  \     / \     / \
           ▼    ▼   ▼   ▼   ▼   ▼
          L1   L2  L3  L4  L5  L6
```

Every edge must be typed.

Candidate:

```yaml
HMLEdge:
  parent: null
  child: null

  edge_type:
    - AGGREGATION
    - CONSTRAINT
    - DEPENDENCY
    - SUPPORT
    - CONTRADICTION
    - INVALIDATION
    - UNKNOWN

  load_bearing: false

  independence:
    - INDEPENDENT
    - CORRELATED
    - UNKNOWN

  condition: null

  provenance: []

  scope: null
  regime: null
```

The source cross-scale contract requires each transformation to bind to a typed RSCF edge.

---

# 12. H/M/L RSCF Binding

Every material H/M/L state used in a conclusion should map to an RSCF node:

```yaml
RSCFNode:
  id: null

  type:
    - SOURCE_CLAIM
    - OBSERVATION
    - DERIVED
    - MODEL
    - DECISION
    - UNKNOWN

  HML:
    - H
    - M
    - L

  claim: null

  scope: null
  regime: null
  time: null
  observer: null

  provenance: []

  confidence: null
  falsifier: null

  status:
    - VALID
    - CONDITIONAL
    - COMPETING
    - INVALID
    - UNKNOWN_GAP
```

This follows the source-defined mandatory RSCF node schema.

---

# 13. H/M/L Invariants

```text
L03-HML-INV-001
Aggregation does not prove identity.

L03-HML-INV-002
Macro/high-level stability may coexist with local collapse.

L03-HML-INV-003
Local correlation does not establish macro causation.

L03-HML-INV-004
Downward constraint must remain distinct from downward causation.

L03-HML-INV-005
Decision-relevant heterogeneity must survive aggregation.

L03-HML-INV-006
Scope propagates across scale transforms.

L03-HML-INV-007
Regime propagates across scale transforms.

L03-HML-INV-008
Observer context propagates across scale transforms.

L03-HML-INV-009
Provenance survives L→M→H transformation.

L03-HML-INV-010
Confidence cannot rise merely because evidence is aggregated upward.

L03-HML-INV-011
A high-level percept cannot silently rewrite contradictory local observations.

L03-HML-INV-012
A local percept cannot silently become a global percept.

L03-HML-INV-013
A failed local node invalidates only dependent M/H descendants.

L03-HML-INV-014
Independent M/H branches survive unrelated local failure.

L03-HML-INV-015
Cross-scale transformations must be explicitly typed.

L03-HML-INV-016
UNKNOWN/GAP at a load-bearing level cannot become PASS at a higher level.

L03-HML-INV-017
COMPETING local/middle percepts must remain representable at higher scales where material.

L03-HML-INV-018
H/M/L similarity does not establish causal recurrence across scales.

L03-HML-INV-019
Capability at one scale does not imply authority at another.

L03-HML-INV-020
H/M/L proposal completion does not equal authoritative commit.
```

The first six are direct applications of the source cross-scale invariants.

---

# 14. Heterogeneity Preservation

Aggregation must not destroy materially distinct local or middle states.

Suppose:

```text
L1 = red feature
L2 = blue feature
L3 = uncertain feature
```

An M-level summary:

```text
"colored region"
```

may be useful.

But if the distinction affects a decision, the lower-level variation must remain recoverable.

Hard rule:

```text
COMPRESSION
!=
ERASURE
```

Candidate preservation condition:

[
MaterialDifference(L_i,L_j)
\Rightarrow
Recoverable(L_i,L_j\mid M)
]

`AMOS_MODEL`.

---

# 15. Confidence Propagation

Source-aligned confidence ceiling:

[
Conf(c)
\le
\min_{p\in P_c}Conf(p)
]

for load-bearing parents unless independently revalidated.

L03 application:

[
Conf(M)
\le
\min_{l\in LB(M)}Conf(l)
]

and:

[
Conf(H)
\le
\min_{m\in LB(H)}Conf(m)
]

unless an independent validated support path exists.

Example:

```text
L1 confidence = HIGH
L2 confidence = MEDIUM
L3 confidence = HIGH

M depends on L1,L2,L3

M ceiling = MEDIUM
```

No upward confidence amplification by aggregation alone is allowed.

---

# 16. Uncertainty Propagation

Candidate H/M/L uncertainty:

```yaml
HMLUncertainty:

  L:
    observation: null
    feature: null
    temporal: null
    spatial: null
    modality: null

  M:
    binding: null
    identity: null
    event: null
    multimodal: null

  H:
    scene: null
    global_context: null
    scope: null
    regime: null

  cross_scale:
    transform: null
    provenance: null
    independence: null
```

Hard boundary:

```text
LOW H-LEVEL UNCERTAINTY
does not erase
HIGH L-LEVEL UNCERTAINTY
```

if the local uncertainty remains decision-relevant.

---

# 17. Scope Propagation

Candidate:

[
Scope(M)
\subseteq
\bigcap_{l\in LB(M)}Scope(l)
]

and:

[
Scope(H)
\subseteq
\bigcap_{m\in LB(H)}Scope(m)
]

unless a validated scale-transfer relation broadens scope.

Cross-scale source rules explicitly require scope envelopes to propagate with claims.

---

# 18. Regime Propagation

Candidate:

[
RegimeValid(M)
==============

\bigwedge_{l\in LB(M)}
Compat(Regime(l),Regime(M))
]

and similarly for H.

If an L-level dependency changes regime:

```text
L changed regime
↓
revalidate dependent M
↓
revalidate dependent H
```

not unrelated branches.

---

# 19. Observer Propagation

A percept may depend on observer position or measurement context.

Candidate:

```text
L observer-dependent cue
↓
M observer-dependent object percept
↓
H observer-dependent scene percept
```

Hard boundary:

```text
OBSERVER-DEPENDENT L
cannot silently become
OBSERVER-INDEPENDENT H
```

Cross-scale observer envelopes must remain explicit.

---

# 20. Provenance Propagation

Candidate ancestry:

```text
SOURCE
↓
OBSERVATION
↓
L FEATURE
↓
M PERCEPT
↓
H PERCEPT
```

For H node (H_i):

[
Anc(H_i)
========

\bigcup_{m\in LB(H_i)}
Anc(m)
]

and recursively to L/source state.

Hard rule:

```text
AGGREGATED DESCENDANTS
!=
INDEPENDENT SOURCES
```

---

# 21. Selective Invalidation

Source-aligned:

[
Invalidate(p)=Desc_{LB}(p)
]

meaning invalidation propagates through load-bearing descendants only.

Example:

```text
L1 → M1 → H1
L2 → M2 → H2
```

Invalidate `L1`.

Expected:

```text
L1 = INVALID
M1 = INVALID / REVALIDATE
H1 = INVALID / REVALIDATE

L2 = unchanged
M2 = unchanged
H2 = unchanged
```

assuming there is no hidden shared dependency.

---

# 22. Macro Stability / Local Collapse

The source model explicitly allows:

```text
MACRO STABILITY
+
LOCAL COLLAPSE
```

to coexist.

L03 example:

```text
H:
  "overall scene remains traffic"

while

L:
  one vehicle identity becomes invalid
```

This does not necessarily invalidate the H scene if the H percept has sufficient independent support.

Therefore:

```text
LOCAL FAILURE
!=
AUTOMATIC H FAILURE
```

---

# 23. Local Change / Macro Causation Firewall

A local signal may correlate with a high-level percept.

But:

[
Corr(L,H)
\not\Rightarrow
Cause(L,H)
]

Hard rule:

```text
LOCAL ASSOCIATION
!=
MACRO CAUSATION
```

This is source-aligned.

---

# 24. Downward Constraint / Causation Firewall

A high-level percept may alter the interpretation space of local features.

Candidate:

[
L'*t=C*{H\rightarrow L}(H_t,L_t)
]

But this is a model of informational constraint.

It does not license the empirical causal claim:

```text
H caused L observation
```

without separate causal evidence.

---

# 25. Competing Cross-Scale Percepts

Example:

```text
L:
  ambiguous local motion

M1:
  object moving

M2:
  observer moving

H1:
  moving-object scene

H2:
  observer-motion scene
```

If available evidence cannot distinguish them:

```text
H1
H2
→ COMPETING
```

Higher-level integration must not erase lower-level ambiguity merely to produce one coherent scene.

---

# 26. H/M/L Sensitivity

The source cross-scale architecture defines a sensitivity flip set:

[
F_c
===

{
p
\mid
\text{plausible change in }p
\text{ flips conclusion }c
}
]

L03 use:

```text
For H percept H1:
identify which M or L premise could plausibly flip H1.

Test that premise before spending resources on irrelevant details.
```

Candidate:

[
p^*
===

\arg\min_{p\in F_c}
Cost(Test(p))
]

subject to sufficient discriminating power.

This last selection equation is `AMOS_MODEL`.

---

# 27. Cross-Scale Gap Classes

Use the source gap classes:

```text
CRITICAL
DECISION_RELEVANT
EXPLANATORY
COSMETIC
```

Examples:

```text
CRITICAL:
no mapping exists between required L and M states

DECISION_RELEVANT:
M→H aggregation uncertainty could flip percept decision

EXPLANATORY:
exact biological analogy unknown but runtime decision unaffected

COSMETIC:
naming inconsistency with no semantic consequence
```

---

# 28. H/M/L Failure Modes

```text
FM-L03-HML-001
L observation promoted directly to H without mapping.

FM-L03-HML-002
M object candidate treated as proven global state.

FM-L03-HML-003
H prior overwrites contradictory L evidence.

FM-L03-HML-004
Aggregation erases decision-relevant heterogeneity.

FM-L03-HML-005
Local correlation presented as macro causation.

FM-L03-HML-006
Downward constraint presented as causal effect.

FM-L03-HML-007
Scope lost during L→M or M→H transformation.

FM-L03-HML-008
Regime lost across scale transformation.

FM-L03-HML-009
Observer dependence lost across scale.

FM-L03-HML-010
Provenance ancestry lost during aggregation.

FM-L03-HML-011
Confidence rises merely because more nodes are aggregated.

FM-L03-HML-012
Correlated descendants counted as independent support.

FM-L03-HML-013
Local failure triggers unjustified global invalidation.

FM-L03-HML-014
Dependent H state survives invalidated load-bearing M/L premise.

FM-L03-HML-015
Cross-scale transform is untyped.

FM-L03-HML-016
UNKNOWN local state converted to valid high-level percept.

FM-L03-HML-017
COMPETING states collapse without discriminating evidence.

FM-L03-HML-018
High-level stability hides decision-relevant local collapse.

FM-L03-HML-019
H/M/L analogy presented as established cognitive mechanism.

FM-L03-HML-020
H/M/L state proposal bypasses control-plane authority.
```

---

# 29. Repair / Recovery

Cross-scale repair workflow:

```text
DETECT H/M/L FAILURE
↓
IDENTIFY AFFECTED SCALE
↓
TRACE LOAD-BEARING CROSS-SCALE EDGES
↓
IDENTIFY EARLIEST FAILED NODE / TRANSFORM
↓
FREEZE DEPENDENT DESCENDANTS
↓
PRESERVE UNAFFECTED BRANCHES
↓
RESTORE ORIGINAL L/M/H EVIDENCE
↓
REPAIR TRANSFORM OR MAPPING
↓
RE-RUN HETEROGENEITY CHECK
↓
RECHECK SCOPE / REGIME / OBSERVER
↓
RECHECK PROVENANCE
↓
RECALCULATE CONFIDENCE CEILINGS
↓
REOPEN COMPETING STATES IF REQUIRED
↓
REVALIDATE UPWARD / DOWNWARD TRANSFORMS
↓
PROPOSE RECOVERED STATE
```

Hard repair rule:

```text
DO NOT ALTER LOWER-LEVEL EVIDENCE
MERELY TO PRESERVE A HIGHER-LEVEL PERCEPT
```

---

# 30. Dependencies

Internal dependencies:

```text
L03_PERCEPT_FORMATION/DEFINITION
L03_PERCEPT_FORMATION/VARIABLES
L03_PERCEPT_FORMATION/STATE
L03_PERCEPT_FORMATION/OPERATORS
L03_PERCEPT_FORMATION/INVARIANTS
L03_PERCEPT_FORMATION/DEPENDENCIES
L03_PERCEPT_FORMATION/EQUATIONS
L03_PERCEPT_FORMATION/PROVENANCE
L03_PERCEPT_FORMATION/FAILURE_MODES
L03_PERCEPT_FORMATION/REPAIR
L03_PERCEPT_FORMATION/CONTROL_PLANES
L03_PERCEPT_FORMATION/TESTS
```

Upstream:

```text
L01_SENSING_OBSERVATION
L02_ATTENTION
```

Cross-cutting:

```text
AMOS Cross-Scale RSCF Tensor Engine
AMOS RSCF
AMOS provenance architecture
AMOS constraint propagation
AMOS infrastructure control plane
```

---

# 31. Control-Plane Requirements

The H/M/L cognitive layer may:

```text
construct local percepts
construct middle percepts
construct high percepts
propose upward aggregation
propose downward constraints
identify contradictions
propose invalidation
propose repair
```

The control plane should govern:

```text
authoritative H/M/L state identity
version/freshness
cross-scale dependency registration
authority
scope/regime validity
commit eligibility
durable mutation
rollback
```

Hard boundary:

```text
H/M/L TRANSFORM VALID
!=
STATE COMMIT AUTHORIZED
```

---

# 32. Agents

Candidate logical H/M/L roles:

```text
L03_LOCAL_PERCEPT_AGENT
L03_MIDDLE_PERCEPT_AGENT
L03_HIGH_PERCEPT_AGENT

L03_L_TO_M_AGGREGATOR
L03_M_TO_H_AGGREGATOR

L03_H_TO_M_CONSTRAINT_AGENT
L03_M_TO_L_CONSTRAINT_AGENT

L03_HML_PROVENANCE_AUDITOR
L03_HML_CONSISTENCY_AUDITOR
L03_HML_SENSITIVITY_AGENT
L03_HML_REPAIR_AGENT
```

Status:

```text
MODEL ROLES
```

not evidence of implemented agents.

---

# 33. Skills

Relevant capability families:

```text
AMOS Cross-Scale RSCF Tensor Engine
AMOS Multimodal Perception Layer
AMOS Binding RSCF Engine
AMOS Temporal Multi-Scale RSCF Engine
AMOS Constraint Propagation RSCF Engine
AMOS Provenance Trust Firewall
AMOS Universal Coordinate System
AMOS Metacognitive Confidence Auditor
AMOS Infrastructure Control Plane
RSCF Modeler
```

Hard boundary:

```text
SKILL AVAILABLE
!=
L03 HML INTEGRATED

INTEGRATED
!=
VALIDATED
```

---

# 34. Workflow

The source cross-scale workflow is:

```text
DEFINE H/M/L ONTOLOGY
↓
INSTANTIATE SPARSE TENSOR SLICE
↓
BIND CELLS TO RSCF
↓
TYPE TRANSFORMS
↓
TEST INVARIANTS
↓
PROPAGATE ADMISSIBLE EDGES
↓
TEST CHEAPEST FLIP PREMISE
↓
ISSUE WEAKEST ACCURATE CONCLUSION
```

L03 specialization:

```text
RECEIVE L OBSERVATIONS / FEATURES
↓
BUILD L PERCEPT STATE
↓
REGISTER L RSCF NODES
↓
DEFINE L→M TRANSFORMS
↓
BUILD M PERCEPT CANDIDATES
↓
PRESERVE COMPETING M STATES
↓
DEFINE M→H TRANSFORMS
↓
BUILD H PERCEPT CANDIDATES
↓
CHECK DOWNWARD CONSTRAINT CONSISTENCY
↓
CHECK SCOPE / REGIME / OBSERVER
↓
CHECK PROVENANCE
↓
CHECK CONFIDENCE CEILINGS
↓
RUN SENSITIVITY FLIP TEST
↓
VALID / CONDITIONAL / COMPETING / UNKNOWN_GAP
↓
PROPOSE H/M/L STATE
```

---

# 35. Protocols

Candidate protocol surface:

```text
L03_HML_REGISTER_NODE
L03_HML_REGISTER_EDGE

L03_HML_L_TO_M_PROPOSE
L03_HML_M_TO_H_PROPOSE

L03_HML_H_TO_M_CONSTRAINT
L03_HML_M_TO_L_CONSTRAINT

L03_HML_CONFLICT_NOTICE
L03_HML_SCOPE_NOTICE
L03_HML_REGIME_NOTICE
L03_HML_PROVENANCE_NOTICE

L03_HML_INVALIDATE
L03_HML_REVALIDATE
L03_HML_REPAIR
L03_HML_RESULT
```

Canonical identifiers remain:

```text
UNKNOWN/GAP
```

---

# 36. Evidence / Provenance

Each H/M/L conclusion must preserve:

```yaml
HMLProvenance:

  target_node: null

  level:
    - H
    - M
    - L

  parent_nodes: []

  source_observations: []

  transformations: []

  edge_types: []

  semantic_origins: []

  scope: null
  regime: null
  time: null
  observer: null

  confidence_ceiling: null

  falsifiers: []

  validator_refs: []
```

Source requirement:

> each tensor cell used in a conclusion must bind to an RSCF node, and each transform must bind to a typed RSCF edge.

---

# 37. Tests / Validators

Minimum validators:

```text
VALIDATE_HML_NODE_TYPES
VALIDATE_HML_EDGE_TYPES

VALIDATE_L_TO_M_MAPPING
VALIDATE_M_TO_H_MAPPING

VALIDATE_H_TO_M_CONSTRAINT
VALIDATE_M_TO_L_CONSTRAINT

VALIDATE_HETEROGENEITY_PRESERVATION
VALIDATE_SCOPE_PROPAGATION
VALIDATE_REGIME_PROPAGATION
VALIDATE_OBSERVER_PROPAGATION
VALIDATE_PROVENANCE_PROPAGATION

VALIDATE_CONFIDENCE_CEILING

VALIDATE_NO_LOCAL_TO_MACRO_CAUSAL_OVERREACH
VALIDATE_NO_CONSTRAINT_AS_CAUSATION

VALIDATE_SELECTIVE_INVALIDATION
VALIDATE_COMPETING_PRESERVATION
VALIDATE_SENSITIVITY_FLIP_SET

VALIDATE_UNKNOWN_NOT_PASS
```

Conceptual tests:

```text
TEST-L03-HML-001
Aggregate L1/L2 into M1.
Expected:
ancestry L1/L2 remains recoverable.

TEST-L03-HML-002
Create M1 from weak L2.
Expected:
M1 confidence <= L2 load-bearing ceiling.

TEST-L03-HML-003
Create H1 from M1/M2.
Expected:
H1 does not exceed weakest load-bearing M premise.

TEST-L03-HML-004
Invalidate L1 where L1→M1→H1.
Expected:
M1/H1 revalidated or invalidated.

TEST-L03-HML-005
Invalidate unrelated L3.
Expected:
M1/H1 unchanged.

TEST-L03-HML-006
H prior conflicts with L observation.
Expected:
L preserved; H revalidated.

TEST-L03-HML-007
Local correlation strongly tracks H state.
Expected:
no macro causal claim without causal evidence.

TEST-L03-HML-008
H constrains M interpretation.
Expected:
constraint classified separately from causation.

TEST-L03-HML-009
Aggregation hides decision-relevant L heterogeneity.
Expected:
FAIL.

TEST-L03-HML-010
Unknown L premise supports H.
Expected:
H cannot be PASS/VERIFIED.

TEST-L03-HML-011
Multiple L descendants share one source.
Expected:
one provenance ancestry family.

TEST-L03-HML-012
All H/M/L structural tests pass.
Expected:
does not imply empirical neuroscience validation.
```

Execution state:

```yaml
tests_defined: true
tests_executed: false
runtime_validation: false
empirical_validation: false
```

---

# 38. Falsifiers

Revise this contract if direct canonical evidence establishes:

```text
different canonical H/M/L meanings;

different L→M or M→H semantics;

different downward constraint semantics;

no H/M/L treatment in canonical L03;

different provenance propagation;

different confidence propagation;

different invalidation behavior;

different observer/scope/regime propagation;

or executable runtime evidence contradicts these mappings.
```

Specific modeled claims are falsified by examples where:

```text
valid aggregation requires identity equivalence;

local failure always necessarily destroys H;

downward constraint is canonically defined as causal effect;

heterogeneity is intentionally discarded even when decision-relevant;

or confidence legitimately increases solely because the same evidence is aggregated across scales.
```

---

# 39. Gap Matrix

```yaml
gap_status:

  generic_HML_tensor:
    status: SOURCE_ALIGNED_MODEL

  upward_aggregation:
    status: SOURCE_ALIGNED_MODEL

  downward_constraint:
    status: SOURCE_ALIGNED_MODEL

  general_cross_scale_update:
    status: SOURCE_ALIGNED_MODEL

  RSCF_node_binding:
    status: SOURCE_ALIGNED

  RSCF_edge_binding:
    status: SOURCE_ALIGNED

  confidence_ceiling:
    status: SOURCE_ALIGNED

  selective_invalidation:
    status: SOURCE_ALIGNED

  sensitivity_flip_set:
    status: SOURCE_ALIGNED

  L03_L_definition:
    status: MODEL_DEFINED

  L03_M_definition:
    status: MODEL_DEFINED

  L03_H_definition:
    status: MODEL_DEFINED

  L03_L_to_M_mapping:
    status: MODEL_DEFINED

  L03_M_to_H_mapping:
    status: MODEL_DEFINED

  L03_H_to_M_constraint:
    status: MODEL_DEFINED

  L03_M_to_L_constraint:
    status: MODEL_DEFINED

  L03_provenance_propagation:
    status: MODEL_DEFINED

  L03_HML_failure_model:
    status: MODEL_DEFINED

  canonical_L03_HML_definition:
    status: CRITICAL_GAP

  canonical_transform_operators:
    status: CRITICAL_GAP

  canonical_transform_thresholds:
    status: DECISION_RELEVANT_GAP

  canonical_runtime_mapping:
    status: CRITICAL_GAP

  executable_HML_engine:
    status: CRITICAL_GAP

  executed_tests:
    status: CRITICAL_GAP

  empirical_percept_validation:
    status: CRITICAL_GAP
```

---

# 40. Competing H/M/L Architectures

## COMPETING-001 — Strict Hierarchy

```text
L
↓
M
↓
H
```

No downward effects.

Advantage:

```text
simple provenance
```

Risk:

```text
cannot model contextual/top-down constraints
```

---

## COMPETING-002 — Bidirectional Hierarchy

```text
L ⇄ M ⇄ H
```

Allows upward formation and downward constraint.

Risk:

```text
feedback loops
potential source/inference contamination
```

---

## COMPETING-003 — Flat Percept Graph

No privileged H/M/L levels.

```text
all percept nodes
→ typed dependency graph
```

Advantage:

```text
less forced hierarchy
```

Risk:

```text
weaker scale governance
```

---

## COMPETING-004 — Governed Sparse Cross-Scale Tensor

```text
typed H/M/L nodes
+
explicit upward aggregation
+
explicit downward constraint
+
RSCF-bound edges
+
provenance
+
scope/regime/observer
+
selective invalidation
```

Current model preference:

```text
COMPETING-004
```

because it most directly aligns with the source Cross-Scale RSCF Tensor Engine.

It remains an L03 `MODEL`.

---

# 41. Uncertainty and Confidence Ceiling

```yaml
uncertainty:

  source:
    level: MEDIUM
    reason: generic AMOS H/M/L architecture is source-aligned

  L03_mapping:
    level: HIGH
    reason: direct canonical L03 H/M/L mapping not recovered

  transform:
    level: HIGH
    reason: exact L→M/M→H functional forms unknown

  cross_scale_causal:
    level: HIGH
    reason: structural transforms do not establish causal mechanism

  scope:
    level: MEDIUM

  regime:
    level: MEDIUM

  observer:
    level: MEDIUM

  provenance:
    level: MEDIUM

  execution:
    level: MAXIMUM
    reason: executable L03 H/M/L runtime not established

  empirical:
    level: MAXIMUM
    reason: no empirical perceptual validation established here
```

Confidence ceiling:

```text
generic AMOS H/M/L architecture:
SOURCE-ALIGNED MODEL

specific L03 H/M/L mapping:
MODEL

canonical L03 H/M/L:
UNKNOWN/GAP

runtime implementation:
UNKNOWN/GAP

empirical cognition claim:
UNKNOWN/GAP
```

---

# 42. RSCF Completion State

```yaml
rscf:

  id: L03_PERCEPT_FORMATION_HML

  claim:
    L03_PERCEPT_FORMATION can be represented across local,
    middle, and high perceptual levels using explicit upward
    aggregation, downward constraint, typed cross-scale
    dependencies, RSCF-bound nodes/edges, provenance,
    confidence ceilings, scope/regime/observer propagation,
    competing percept preservation, sensitivity testing,
    and selective invalidation.

  claim_class: MODEL

  evidence:
    - AMOS Cross-Scale RSCF Tensor Engine
    - AMOS perception architecture
    - modeled L03 definition/dependency/equation contracts

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    artifact: HML.md
    derivation: SOURCE_ALIGNED_HML_PLUS_L03_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    concern: HML_cross_scale_percept_formation

  regime:
    governed cognitive/perceptual architecture

  freshness:
    revalidate_when:
      - direct L03 HML canon is recovered
      - cross-scale engine changes
      - L03 definition changes
      - L03 dependencies change
      - HML transforms are implemented
      - runtime validation becomes available

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION
    - L03_PERCEPT_FORMATION_DEFINITION
    - L03_PERCEPT_FORMATION_DEPENDENCIES
    - L03_PERCEPT_FORMATION_EQUATIONS
    - L03_PERCEPT_FORMATION_STATE
    - L03_PERCEPT_FORMATION_INVARIANTS
    - L03_PERCEPT_FORMATION_PROVENANCE
    - L03_PERCEPT_FORMATION_FAILURE_MODES
    - AMOS_CROSS_SCALE_RSCF_TENSOR_ENGINE
    - AMOS_RSCF
    - AMOS_INFRASTRUCTURE_CONTROL_PLANE

  competing:
    - strict upward-only hierarchy
    - bidirectional H/M/L hierarchy
    - flat percept dependency graph
    - governed sparse cross-scale tensor

  falsifiers:
    - incompatible canonical L03 H/M/L semantics
    - incompatible canonical cross-scale transforms
    - incompatible invalidation semantics
    - runtime evidence contradicting modeled hierarchy
    - empirical counterevidence to any later biological interpretation

  uncertainty:
    source: MEDIUM
    model: MEDIUM
    L03_mapping: HIGH
    cross_scale_causal: HIGH
    execution: MAXIMUM
    empirical: MAXIMUM
    provenance_independence: MEDIUM

  confidence_ceiling:
    Generic AMOS H/M/L mechanics are source-aligned.
    Their specific use as the L03 percept-formation hierarchy
    remains MODEL until direct L03 canon and runtime evidence
    establish the mapping.

  gap_status:
    canonical_L03_HML: CRITICAL_GAP
    canonical_transforms: CRITICAL_GAP
    canonical_thresholds: DECISION_RELEVANT_GAP
    executable_HML_runtime: CRITICAL_GAP
    executed_validation: CRITICAL_GAP
    empirical_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    recover direct L03 H/M/L canon and compare its H, M, L
    definitions plus all upward/downward transform rules against
    this model; then build a minimal three-level dependency graph
    and test provenance preservation, confidence ceilings,
    heterogeneity retention, selective invalidation, constraint/
    causation separation, and sensitivity-flip behavior.
```

---

# 43. Completion State

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

  canonical_HML:
    status: UNKNOWN_GAP

  executable_HML_runtime:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP

  empirical_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_HML_CONTRACT_SCOPE

  conclusion_class:
    MODEL
```

---

# 44. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

H/M/L-specific boundaries:

```text
L != M != H

LOCAL FEATURE != OBJECT IDENTITY

OBJECT PERCEPT != GLOBAL SCENE TRUTH

AGGREGATION != IDENTITY

AGGREGATION != CAUSATION

CORRELATION != CAUSATION

DOWNWARD CONSTRAINT != DOWNWARD CAUSATION

HIGH-LEVEL CONTEXT != LOW-LEVEL OBSERVATION

MACRO STABILITY != LOCAL VALIDITY

LOCAL COLLAPSE != AUTOMATIC GLOBAL COLLAPSE

MULTIPLE DESCENDANTS != INDEPENDENT SOURCES

COMPRESSION != HETEROGENEITY ERASURE

CROSS-SCALE COHERENCE != EMPIRICAL TRUTH

MODEL HML != CANONICAL HML

CANONICAL HML != IMPLEMENTED HML

IMPLEMENTED HML != VALIDATED HML

VALIDATED COMPUTATION != HUMAN COGNITIVE LAW
```

---

# 45. Governing H/M/L Contract

> **`L03_PERCEPT_FORMATION` SHALL preserve explicit local, middle, and high percept states and SHALL represent every material cross-scale movement through typed transformations bound to provenance-aware RSCF edges. Upward aggregation from L→M→H SHALL NOT by itself prove identity, truth, or causation. Downward H→M→L influence SHALL be classified as constraint or conditioning unless separately causal evidence exists. Scope, regime, observer context, provenance, uncertainty, confidence ceilings, heterogeneity, and competing percepts SHALL propagate across scale transforms. Confidence SHALL NOT increase merely through aggregation. A failed load-bearing node SHALL invalidate only dependency-connected descendants, while independent branches remain valid. Material local contradiction SHALL NOT be overwritten merely to preserve higher-level coherence. Any canonical L03 H/M/L semantics not directly recovered SHALL remain `UNKNOWN/GAP`, and all L03-specific transforms in this artifact remain `MODEL`.**

---

# 46. Canon Boundary

```text
SOURCE-ALIGNED:

Trang Phan origin/stewardship

AMOS cross-scale state tensor:
X[h,m,l,t,r,o,f]

upward aggregation:
X_M = A_L→M(X_L)
X_H = A_M→H(X_M)

downward constraint:
X_M' = C_H→M(X_H,X_M)
X_L' = C_M→L(X_M',X_L)

general cross-scale update

aggregation != identity

macro stability may coexist with local collapse

local correlation != macro causation

downward constraint != downward causation

decision-relevant heterogeneity preservation

scope/regime/observer propagation

RSCF-bound tensor cells

typed RSCF edges

confidence ceiling

selective invalidation

sensitivity flip set

gap classes


AMOS_MODEL:

L03 local percept definition

L03 middle percept definition

L03 high percept definition

L03 L→M percept formation

L03 M→H percept formation

L03 H→M constraint semantics

L03 M→L constraint semantics

cross-scale percept uncertainty

L03 H/M/L agent roles

L03 H/M/L protocol names

L03 failure and repair mapping

L03 tests


UNKNOWN/GAP:

direct canonical L03 H/M/L definitions

canonical L03 scale boundaries

canonical transform functions

canonical transformation thresholds

canonical downstream/upstream scale protocols

canonical runtime state tensors

executable implementation

executed validation

formal verification

empirical perceptual validation
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

GENERIC AMOS H/M/L BASIS:
SOURCE-ALIGNED MODEL

L03-SPECIFIC H/M/L MAPPING:
MODEL

DIRECT L03 CANON:
UNKNOWN/GAP

IMPLEMENTATION:
UNKNOWN/GAP

VALIDATION:
UNKNOWN/GAP

EMPIRICAL HUMAN-PERCEPTION CLAIM:
NOT ESTABLISHED
```

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l03_percept_formation_primitives_cognitive_matrix_hml
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION/L03_PERCEPT_FORMATION_PRIMITIVES_COGNITIVE_MATRIX_HML.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L03_PERCEPT_FORMATION_MOC]]
