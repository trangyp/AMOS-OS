---
title: GENERATORS COGNITIVE MATRIX README
tags: ['cognitive_matrix', 'generators', 'readme']
---


Below is a **full replacement README** for `12_GENERATORS`. It treats the branch as an AMOS infrastructure layer for governed generation rather than a collection of arbitrary content-producing scripts. The structure is **DERIVED / CONDITIONAL** from the Full Brain OS, v4.4 runtime, RSCF, authority/control-plane, deployment, and provenance rules; it does not claim that every proposed generator type already exists in source canon. The Full Brain architecture explicitly separates cognition, runtime, control/authority, and deployment, so generators must preserve those boundaries.  

---
id: AMOS-12-GENERATORS
title: "12_GENERATORS — Governed Generation Infrastructure"
origin_architect: "Trang Phan"
artifact_type: "architecture_readme"

class: "MATRIX_INFRASTRUCTURE"
conclusion_class: "DERIVED"
canon_status: "CONDITIONAL"
validation_status: "ARCHITECTURE_DEFINED_IMPLEMENTATION_PARTIAL_OR_UNKNOWN"
gap_status: "OPEN"

scope:
  - generator_contracts
  - generator_registry
  - generation_planning
  - generation_execution
  - artifact_generation
  - knowledge_generation
  - hypothesis_generation
  - simulation_generation
  - code_and_fabrication_generation
  - provenance
  - validation
  - authority
  - commit_control

runtime_dependencies:
  - "AMOS_FULL_BRAIN_OS"
  - "OMNI_KERNEL"
  - "BRAIN_CORE"
  - "OMNIVERSE_BRAIN"
  - "AMOS_OS_KERNEL_v4.4"
  - "RSCF"
  - "HML"
  - "INFRASTRUCTURE_CONTROL_PLANE"

hard_rule: "GENERATION != TRUTH != AUTHORITY != COMMIT"
---

# 12_GENERATORS

**Class:** `MATRIX_INFRASTRUCTURE`

**Origin architect / steward:** Trang Phan

**Status:** `CONDITIONAL / ARCHITECTURE_DEFINED / IMPLEMENTATION_MUST_BE_PROVEN_PER GENERATOR`

---

# 1. Purpose

`12_GENERATORS` defines the AMOS architecture for producing new candidate artifacts from validated inputs under explicit constraints.

A **generator** is an addressable transformation capability that accepts typed inputs and produces one or more typed candidate outputs.

A generator may produce:

- text;
- structured knowledge;
- models;
- hypotheses;
- proof capsules;
- plans;
- workflows;
- schemas;
- simulations;
- code;
- designs;
- configurations;
- reports;
- datasets;
- tests;
- agents;
- tool specifications;
- fabrication specifications;
- other governed artifacts.

Generation itself does **not** establish:

```text
correctness
truth
validation
authority
permission
canonical status
commit eligibility
```

The central contract is:

```text
INPUT
  ↓
ADMISSION
  ↓
GENERATION PLAN
  ↓
CONSTRAINED GENERATION
  ↓
CANDIDATE OUTPUT
  ↓
VALIDATION
  ↓
AUTHORITY / POLICY CHECK
  ↓
PROPOSAL
  ↓
OPTIONAL COMMIT
```

Never collapse this into:

```text
PROMPT
→ GENERATE
→ ACCEPT
```

---

# 2. Architectural Position

`12_GENERATORS` is **not the Full Brain OS**.

It is downstream of cognitive routing and upstream of effectful deployment.

```text
HUMAN / ENVIRONMENT
        ↓
EXPRESSION TRANSLATION
        ↓
OMNI KERNEL
        ↓
BRAIN CORE + OMNIVERSE BRAIN
        ↓
COGNITIVE SYNTHESIS
        ↓
AMOS OS KERNEL v4.4
        ↓
GENERATION REQUEST
        ↓
12_GENERATORS
        ↓
CANDIDATE ARTIFACT
        ↓
VALIDATION
        ↓
INFRASTRUCTURE CONTROL PLANE
        ↓
COMMIT / REJECT / HOLD / REPAIR
        ↓
DEPLOYMENT / WORLD EFFECT
```

The Full Brain OS preserves cognition, runtime, control-plane authority, and deployment as separate architectural dimensions. A generator therefore cannot grant itself authority merely because it knows how to produce an artifact.

---

# 3. Core Definition

```text
Generator
=
TypedTransformation
+
ExplicitScope
+
ConstraintSet
+
Provenance
+
ValidationContract
+
FailureContract
```

More formally:

```text
G:
(InputState, Context, Constraints, AuthorityView)
→
CandidateOutput
```

where:

```text
CandidateOutput != ValidatedOutput
```

and:

```text
ValidatedOutput != CommittedOutput
```

A generator is only an **artifact-producing capability**.

It does not own final truth classification, authorization, or commit.

---

# 4. Non-Equivalences

These boundaries are mandatory.

```text
GENERATOR != AGENT

GENERATOR != TOOL

GENERATOR != WORKFLOW

GENERATOR != ENGINE

GENERATOR != KERNEL

GENERATOR != VALIDATOR

GENERATOR != AUTHORITY

GENERATOR != COMMITTER

GENERATED != VERIFIED

ADDRESSABLE != IMPLEMENTED

IMPLEMENTED != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

SIMULATION != OBSERVATION

MODEL OUTPUT != EMPIRICAL FACT

SOURCE_CLAIM != VERIFIED

UNKNOWN/GAP != PASS
```

A generator may be **used by** an agent or workflow.

A generator may be **implemented through** a tool, skill, code module, model, or external executor.

Those bindings do not redefine the generator's semantic role.

---

# 5. Generator Lifecycle

Every governed generator should follow:

```text
01 REQUEST
    ↓
02 CLASSIFY
    ↓
03 RESOLVE GENERATOR
    ↓
04 LOAD MINIMUM DEPENDENCIES
    ↓
05 BUILD READ SET
    ↓
06 CHECK SCOPE / REGIME / FRESHNESS
    ↓
07 CHECK AUTHORITY
    ↓
08 BUILD GENERATION PLAN
    ↓
09 GENERATE CANDIDATE
    ↓
10 TYPE OUTPUT
    ↓
11 ATTACH PROVENANCE
    ↓
12 VALIDATE
    ↓
13 CHALLENGE
    ↓
14 REPAIR OR REGENERATE IF REQUIRED
    ↓
15 CLASSIFY RESULT
    ↓
16 PROPOSE
    ↓
17 COMMIT ONLY IF SEPARATELY AUTHORIZED
    ↓
18 PERSIST LINEAGE
```

---

# 6. Generator Registry

Every generator must be registered using a typed record.

Minimum schema:

```yaml
generator_id: null
name: null
version: null

class: GENERATOR
subclass: null

status:
  implementation: UNKNOWN
  validation: UNKNOWN
  deployment: UNKNOWN

owner_domain: null

purpose: null

accepted_inputs: []
produced_outputs: []

scope:
  systems: []
  domains: []
  scales: []
  environments: []
  regimes: []
  temporal_validity: null

dependencies: []

required_authority: []

read_set_contract: []
write_set_contract: []

operators: []

invariants: []

validators: []

falsifiers: []

failure_modes: []

repair_paths: []

provenance_requirements: []

confidence_ceiling: 0

deployment_bindings:
  skills: []
  tools: []
  workflows: []
  agents: []
  code: []

supersedes: []
superseded_by: null
```

Unknown values remain `UNKNOWN`.

Do not fill them with plausible-looking defaults.

---

# 7. Proposed Generator Families

The following taxonomy is a **DERIVED architecture proposal**, not automatically source-defined canon.

It creates addressable families without claiming that all are implemented.

## 7.1 Knowledge Generators

Produce candidate knowledge artifacts such as:

* domain nodes;
* definitions;
* structured summaries;
* knowledge graphs;
* taxonomies;
* dependency maps;
* claim registries;
* ontology extensions.

Contract:

```text
sources
+
scope
+
epistemic typing
+
provenance
→
candidate knowledge artifact
```

Hard rule:

```text
knowledge generation
!=
knowledge validation
```

---

## 7.2 RSCF / Proof Capsule Generators

Produce structured reasoning capsules containing:

```text
claim
class
premises
evidence
provenance
scope
regime
freshness
dependencies
competing hypotheses
falsifiers
confidence ceiling
```

They may assemble a proof structure.

They may not fabricate missing evidence.

---

## 7.3 Hypothesis Generators

Produce candidate explanations.

```text
Observations
+
Constraints
+
ExistingModels
→
{H1, H2, H3, ...}
```

Requirements:

* hypotheses must be distinguishable;
* assumptions must be explicit;
* shared provenance must remain visible;
* alternatives must not be suppressed simply because one is fluent;
* each hypothesis should expose potential discriminating evidence.

Output class defaults to:

```text
MODEL
or
COMPETING
```

not `VERIFIED`.

---

## 7.4 Counter-Hypothesis Generators

Generate genuinely different challenge paths.

Purpose:

```text
seek contradiction
seek provenance correlation
seek stale premises
seek scope leakage
seek causal overreach
seek hidden dependencies
seek stronger alternatives
```

They must not merely paraphrase the primary hypothesis negatively.

---

## 7.5 Plan Generators

Produce candidate plans:

```text
objective
+
constraints
+
resources
+
risks
+
dependencies
→
candidate plan
```

Plan generation does not authorize execution.

Output:

```text
PROPOSAL
```

until approved.

---

## 7.6 Workflow Generators

Produce workflow definitions.

Possible outputs:

```text
steps
dependency graph
state transitions
branch rules
error handlers
rollback paths
authority gates
```

Generated workflows require validation before deployment.

---

## 7.7 Protocol Generators

Produce governed interaction protocols.

Examples:

* message protocols;
* tool protocols;
* agent handoff protocols;
* transaction protocols;
* experiment protocols;
* evaluation protocols;
* data exchange contracts.

A protocol generator must define:

```text
participants
messages
state transitions
timeouts
failure handling
authority
termination
```

---

## 7.8 Schema Generators

Produce:

* JSON schemas;
* YAML contracts;
* database schemas;
* event schemas;
* API structures;
* registry formats;
* state structures.

Schema generation must preserve:

```text
semantic type
cardinality
nullability
versioning
compatibility
validation
```

---

## 7.9 Code Generators

Produce candidate code.

Code generation must additionally record:

```text
language
runtime
dependencies
permissions
side effects
tests
security constraints
environment assumptions
```

Generated code must not be treated as executed or validated until actually tested.

---

## 7.10 Test Generators

Produce candidate validation tests.

Families may include:

* unit tests;
* integration tests;
* property tests;
* regression tests;
* adversarial tests;
* invariant tests;
* failure-injection tests;
* epistemic validators.

Generated tests require review because a flawed test can validate a flawed implementation.

---

## 7.11 Simulation Generators

Produce simulation definitions or runnable simulation artifacts.

Inputs must include:

```text
model
state variables
initial conditions
boundary conditions
parameters
numerical method
uncertainty
random seed policy
termination criteria
```

Hard boundary:

```text
simulation output
!=
observation of reality
```

---

## 7.12 Scenario Generators

Produce internally coherent conditional futures.

Output class:

```text
MODEL / CONDITIONAL
```

A scenario is not automatically a forecast.

---

## 7.13 Design Generators

Produce candidate system/design structures:

* software architecture;
* hardware design;
* infrastructure design;
* UI;
* schemas;
* organizational design;
* processes;
* fabrication specifications.

Every design must expose assumptions and failure modes.

---

## 7.14 Artifact Generators

Generic family for bounded document or file production.

Examples:

* Markdown;
* JSON;
* YAML;
* CSV;
* diagrams;
* documentation;
* reports;
* manifests;
* registry files.

Artifact-generation success means:

```text
artifact produced
```

not:

```text
artifact semantically correct
```

---

## 7.15 Agent Generators

Produce candidate bounded-agent specifications.

Generated agent definition should include:

```text
goal
scope
authority
memory
tools
planning permissions
termination conditions
escalation
audit
```

Generated agent:

```text
!= active agent
```

Activation belongs to deployment/control architecture.

---

## 7.16 Skill Generators

Produce host deployment skill definitions.

AMOS rule:

```text
Skill
=
deployment artifact
```

not:

```text
Skill
=
AMOS ontology object
```

A skill generator must preserve that distinction.

---

## 7.17 Fabrication Generators

Produce candidate fabrication specifications or execution plans.

These carry elevated governance because outputs may lead to physical effects.

Required:

```text
safety validation
material constraints
authority
reversibility analysis
execution boundary
```

before effectful use.

---

# 8. Typed Inputs

Generator inputs must be typed.

Canonical input categories may include:

```text
OBSERVATION
SOURCE_CLAIM
DERIVED
MODEL
DECISION
UNKNOWN
```

Additional operational types:

```text
USER_REQUEST
DOMAIN_STATE
RSCF_OBJECT
EVIDENCE_SET
CONSTRAINT_SET
POLICY
AUTHORITY_TOKEN
SCENARIO
SIMULATION_STATE
ARTIFACT
CODE
SCHEMA
PLAN
```

A generator must declare which it accepts.

Example:

```yaml
accepted_inputs:
  - USER_REQUEST
  - SOURCE_CLAIM
  - RSCF_OBJECT
  - CONSTRAINT_SET
```

Unsupported types must be rejected or routed through an explicit translator.

---

# 9. Typed Outputs

Every generator output must have both an artifact type and epistemic status.

Example:

```yaml
output:
  artifact_type: KNOWLEDGE_NODE
  epistemic_state: MODEL
  validation_state: UNVALIDATED
  commit_state: PROPOSED
```

Possible artifact types include:

```text
KNOWLEDGE_NODE
RSCF_CAPSULE
MODEL
HYPOTHESIS
PLAN
WORKFLOW
PROTOCOL
SCHEMA
CODE
TEST
SIMULATION
SCENARIO
DESIGN
AGENT_SPEC
SKILL_SPEC
REPORT
MANIFEST
CONFIG
DATASET
```

---

# 10. Generator State Machine

Recommended generator state machine:

```text
UNREGISTERED
    ↓
REGISTERED
    ↓
ADDRESSABLE
    ↓
IMPLEMENTED
    ↓
TESTED
    ↓
VALIDATED
    ↓
DEPLOYABLE
    ↓
ACTIVE
```

These are **not equivalent states**.

A generator can be:

```text
REGISTERED
+
UNIMPLEMENTED
```

or:

```text
IMPLEMENTED
+
UNVALIDATED
```

or:

```text
VALIDATED
+
UNAUTHORIZED_FOR_CURRENT_EFFECT
```

---

# 11. Request State

A specific generation request may move through:

```text
RECEIVED
↓
CLASSIFIED
↓
ADMITTED
↓
PLANNED
↓
GENERATING
↓
CANDIDATE_READY
↓
VALIDATING
↓
CHALLENGED
↓
REPAIRED
↓
APPROVED_AS_PROPOSAL
↓
COMMIT_PENDING
↓
COMMITTED
```

Alternative terminal states:

```text
REJECTED
BLOCKED
FAILED
CANCELLED
UNKNOWN/GAP
SUPERSEDED
```

---

# 12. Core Operators

The generator infrastructure may expose operators such as:

```text
RESOLVE_GENERATOR(request)

ADMIT(request, generator)

BUILD_CONTEXT(read_set)

GENERATE(plan, context)

TYPE_OUTPUT(candidate)

ATTACH_PROVENANCE(candidate)

VALIDATE(candidate)

CHALLENGE(candidate)

REPAIR(candidate, failures)

COMPARE(candidates)

SELECT(candidate_set)

PROPOSE(candidate)

COMMIT(candidate, authority)

ROLLBACK(commit_id)

SUPERSEDE(old, new)
```

These are architecture-level operator names.

They do not imply that corresponding source-code functions already exist.

---

# 13. Generation Function

Abstractly:

```text
Candidate
=
G(
    Objective,
    Inputs,
    Context,
    Constraints,
    DomainKnowledge,
    State,
    Regime,
    GenerationPolicy
)
```

but:

```text
Confidence(Candidate)
≤
Confidence(weakest load-bearing input)
```

unless independent revalidation increases support.

---

# 14. Invariants

The generator layer must preserve the following invariants.

## 14.1 Epistemic invariant

```text
generated claim
cannot silently become
verified claim
```

## 14.2 Provenance invariant

```text
every material generated conclusion
must remain traceable
to its load-bearing inputs
```

## 14.3 Scope invariant

```text
output scope
must not exceed
supported input/model scope
without explicit qualification
```

## 14.4 Regime invariant

```text
cross-regime transfer
requires explicit bridge
```

## 14.5 Authority invariant

```text
generation capability
does not imply
execution authority
```

## 14.6 Commit invariant

```text
candidate
!=
committed state
```

## 14.7 Contradiction invariant

Unresolved contradictions remain visible.

## 14.8 Gap invariant

```text
missing evidence
must remain missing
```

Fluent completion cannot replace it.

## 14.9 Independence invariant

Multiple outputs generated from the same evidence ancestry do not create independent support.

## 14.10 Reversibility invariant

When uncertainty and downstream cost are high, prefer reversible candidate actions.

---

# 15. H / M / L Applicability

Generators may operate at all H/M/L scales.

## H — high-level generation

Examples:

* architecture;
* strategy;
* research program;
* cross-domain model;
* policy framework.

## M — subsystem generation

Examples:

* workflow;
* module;
* domain subsystem;
* causal graph;
* test strategy.

## L — detailed generation

Examples:

* function;
* equation;
* configuration;
* file;
* local procedure;
* test case.

Generation should default to the **lowest sufficient scope**.

Do not generate H-level restructuring when an L-level repair is enough.

---

# 16. Fractal Generation

Any generated object may itself contain subordinate generation contexts.

```text
H Generator
  ↓
generates architecture
  ↓
M Generators
  ↓
generate subsystems
  ↓
L Generators
  ↓
generate implementation detail
```

But dependency inheritance must remain explicit.

A low-level artifact must not lose the provenance and constraints inherited from its parent generation.

---

# 17. Dependencies

`12_GENERATORS` depends on the following architectural services.

## 17.1 Omni Kernel

Provides:

```text
routing
generator selection
priority
integration policy
```

## 17.2 Brain Core

Provides domain/capability reasoning.

## 17.3 Omniverse Brain

Provides world/system/context representation.

## 17.4 AMOS OS Kernel v4.4

Provides:

```text
typed state
admission
planning
scheduling
RSCF
provenance
repair
audit
finalization
```

## 17.5 Memory

Provides relevant persisted state and prior artifacts.

## 17.6 Control Plane

Provides:

```text
authority
read/write permissions
freshness checks
transaction eligibility
commit
rollback
```

## 17.7 Observability

Provides:

```text
generation traces
validation events
failure events
repair events
commit lineage
```

---

# 18. Control-Plane Requirements

A generator may read only authorized state.

A generator may propose write effects only within declared effect bounds.

Commit eligibility requires the separate control-plane gate.

Conceptual condition:

```text
EffectAllowed
=
FreshAuthority
AND CausallyPrior
AND EffectBound
AND EligibleAtCommit
```

Therefore:

```text
GeneratorCanProduce(X)
```

does not imply:

```text
GeneratorMayCommit(X)
```

---

# 19. Read Sets

Every consequential generation should declare a read set.

Example:

```yaml
read_set:
  - artifact://domain/C03/master
  - state://runtime/current
  - policy://generator/code
  - evidence://experiment/E102
```

The generator should be invalidated or rerun when a load-bearing read changes beyond permitted freshness/version rules.

---

# 20. Write Sets

Generators do not own unrestricted writes.

Candidate write set:

```yaml
proposed_write_set:
  - path: "22_RESEARCH/..."
    operation: CREATE
```

Actual write set becomes valid only after authorization.

---

# 21. MVCC / CAS Compatibility

When persistent state is mutable, generation may use snapshot/version concepts.

Conceptually:

```text
read version V1
generate candidate
validate candidate
compare current version
```

If:

```text
current_version != V1
```

then:

```text
revalidate
or
abort
```

rather than blindly committing stale output.

---

# 22. Agents

Agents may orchestrate generators but generators are not automatically agents.

A bounded generator agent may own:

```text
generation objective
generator selection
candidate iteration
validation loop
escalation
```

It must still respect external authority.

Agent requirements:

```yaml
goal_scope: required
authority_scope: required
termination: required
memory_scope: required
tool_scope: required
escalation: required
audit: required
```

---

# 23. Skills

Skills are deployment bindings.

A generator can be exposed through a skill:

```text
AMOS GENERATOR CONTRACT
        ↓
deployment binding
        ↓
HOST SKILL
```

But:

```text
Generator ontology
!=
Skill implementation
```

Skill failure should not silently redefine generator semantics.

---

# 24. Tools

Tools perform operational functions such as:

* file writing;
* code execution;
* API calls;
* simulation;
* database writes;
* external effects.

Generator output may be passed to tools.

Tools must not be treated as epistemic validators by default.

---

# 25. Workflows

A workflow can compose multiple generators.

Example:

```text
SOURCE ANALYSIS
    ↓
KNOWLEDGE GENERATOR
    ↓
CLAIM GENERATOR
    ↓
COUNTER-HYPOTHESIS GENERATOR
    ↓
VALIDATOR
    ↓
REPORT GENERATOR
```

Workflow order must preserve dependency and provenance.

---

# 26. Generator Composition

Generators may be composed:

```text
G3(G2(G1(x)))
```

but composition creates dependency chains.

If:

```text
G1 invalid
```

then descendants that materially depend on `G1` must be invalidated.

Do not preserve downstream confidence after upstream failure.

---

# 27. Parallel Generation

Multiple generators may create competing candidates.

```text
Input
 ├── G1 → Candidate A
 ├── G2 → Candidate B
 └── G3 → Candidate C
```

This is useful when:

* uncertainty is high;
* multiple models are plausible;
* irreversible decisions are involved;
* provenance paths differ;
* architecture alternatives matter.

Parallel generation should not be used merely to generate stylistic duplicates.

---

# 28. Independence

Two outputs are not independent merely because they were generated separately.

If both rely on the same:

```text
source
model
prompt
dataset
assumption
generator ancestry
```

their evidence may be correlated.

Independence must be demonstrated.

---

# 29. Protocols

Every generator should conform to at least these protocols.

## 29.1 Admission Protocol

```text
request
→ generator resolution
→ scope check
→ dependency check
→ authority read check
→ admit / reject
```

## 29.2 Generation Protocol

```text
build context
→ construct plan
→ generate
→ type
→ attach provenance
```

## 29.3 Validation Protocol

```text
schema validation
→ invariant validation
→ evidence check
→ scope/regime check
→ contradiction challenge
→ confidence ceiling
```

## 29.4 Repair Protocol

```text
identify failed premise/operator
→ invalidate dependent portion
→ regenerate smallest required region
→ revalidate
```

## 29.5 Commit Protocol

```text
candidate
→ approval
→ authority gate
→ compare read versions
→ commit
→ persist provenance
```

---

# 30. Evidence and Provenance

Every consequential generated artifact should record:

```yaml
generated_by:
  generator_id: null
  generator_version: null

inputs: []

source_provenance: []

generation_time: null

runtime_context: null

scope: null

regime: null

read_set: []

dependency_hashes: []

validators_run: []

validation_results: []

competing_candidates: []

confidence_ceiling: null

commit_state: PROPOSED
```

---

# 31. Persistent Lineage

Artifact lineage should support:

```text
SOURCE
  ↓
GENERATION V1
  ↓
VALIDATION
  ↓
REPAIR
  ↓
GENERATION V2
  ↓
COMMIT
  ↓
SUPERSESSION
```

Previous states should remain recoverable when provenance matters.

---

# 32. Uncertainty Vector

Generator uncertainty should not be collapsed into one score when consequential.

Track separately where material:

```yaml
uncertainty:
  evidence: null
  model: null
  scope: null
  temporal: null
  causal: null
  execution: null
  provenance_independence: null
```

The generator may only spend additional computation where reducing uncertainty can change the result.

---

# 33. Confidence Ceiling

Generated confidence is bounded by the weakest load-bearing dependency.

```text
C_output
≤
min(
    C_premise1,
    C_premise2,
    ...
)
```

unless a premise is independently revalidated.

Fluency, length, formal notation, or repeated generation must not raise this ceiling.

---

# 34. Failure Modes

## F01 — Fabrication

Generator fills absent evidence with plausible content.

Response:

```text
FAIL
→ UNKNOWN/GAP
```

---

## F02 — Scope Leakage

Output applies beyond source/model scope.

Response:

```text
restrict scope
or
downgrade
```

---

## F03 — Regime Leakage

Output crosses operating regimes without a validated bridge.

---

## F04 — Provenance Loss

Generated artifact cannot be traced back to load-bearing sources.

---

## F05 — Correlated Evidence Inflation

Multiple generated descendants are counted as independent evidence.

---

## F06 — Causal Overreach

Association or analogy becomes a causal claim.

---

## F07 — Authority Escalation

Generator writes or acts beyond granted authority.

---

## F08 — Proposal/Commit Collapse

Candidate artifact is treated as committed state without control-plane admission.

---

## F09 — Stale Read Set

Generator uses outdated mutable state.

---

## F10 — Invalid Composition

Downstream generator depends on failed upstream output.

---

## F11 — Generator Drift

Implementation changes while generator identifier/version remains unchanged.

---

## F12 — Validator Collusion

Generator and validator share hidden assumptions that make validation circular.

---

## F13 — Infinite Generation

System repeatedly regenerates without reducing decision-relevant uncertainty.

---

## F14 — Over-Generation

The generator produces architecture or detail beyond what can materially change the outcome.

---

## F15 — False Completeness

Generator fills every field despite unresolved gaps.

---

# 35. Repair / Recovery

Repair is local.

```text
detect failure
↓
identify failed node / premise / operator
↓
mark invalid
↓
find dependent descendants
↓
invalidate only affected outputs
↓
preserve unaffected artifacts
↓
retrieve changed evidence
↓
regenerate smallest sufficient region
↓
revalidate
```

Global regeneration is last resort.

---

# 36. Retry Rule

Do not retry the same generation path after failure unless something material changes:

```text
input
constraint
model
generator
evidence
parameter
authority
environment
```

Otherwise repeated generation only repeats the same failure class.

---

# 37. Tests and Validators

Generator infrastructure should support:

## Structural tests

* schema completeness;
* required-field tests;
* type checks;
* version checks.

## Invariant tests

* provenance preserved;
* no authority escalation;
* no automatic commit;
* no unknown-to-pass conversion.

## Epistemic tests

* claim typing;
* premise traceability;
* confidence ceiling;
* competing hypothesis retention;
* falsifier presence.

## Scope tests

* domain;
* H/M/L level;
* environment;
* regime;
* timescale.

## Causal tests

* association vs causal claim;
* mechanism presence;
* confounding declared;
* causal boundary respected.

## State tests

* freshness;
* read-set validity;
* CAS/version assumptions;
* stale state detection.

## Failure tests

* malformed input;
* missing evidence;
* contradiction;
* partial dependency outage;
* validator failure;
* unauthorized write;
* rollback.

---

# 38. Generator Acceptance Criteria

A generator is not `VALIDATED` merely because it can generate output.

Minimum acceptance:

```text
registered
+
implemented
+
typed input/output
+
repeatable behavior where expected
+
failure handling
+
provenance
+
scope enforcement
+
validator coverage
+
authority separation
+
known limitations
```

Domain-specific generators may require much more.

---

# 39. Falsifiers

The architecture itself should be rejected or revised if implementation shows that:

1. generator identity cannot be separated from deployment binding;
2. provenance cannot be retained through generation;
3. candidate state cannot be separated from committed state;
4. scope cannot be enforced;
5. downstream invalidation cannot identify dependency closure;
6. authority cannot be independently controlled;
7. validators cannot detect intentional generator failure cases;
8. version changes cannot be tracked;
9. generator outputs cannot be reproducibly attributed to inputs and context;
10. the proposed abstraction adds no useful separation beyond ordinary tool/workflow contracts.

These are genuine architecture falsifiers, not merely missing features.

---

# 40. Security / Governance Boundary

Consequential generators require elevated validation when producing artifacts that may affect:

```text
legal outcomes
financial outcomes
health
safety
infrastructure
security
institutional governance
irreversible physical systems
large downstream dependency graphs
```

The preferred pattern is:

```text
generate
→ sandbox
→ validate
→ review
→ stage
→ observe
→ expand authority only if justified
```

---

# 41. Irreversibility

Define generation risk partly through:

```text
Impact
×
Irreversibility
×
DependencyReach
×
Uncertainty
```

High-risk generated actions should not proceed directly to effect.

---

# 42. Stopping Conditions

Generation should stop when:

### Claim Sufficiency

Enough evidence and reasoning exist to state the warranted conclusion.

### Decision Sufficiency

Additional generation is unlikely to change the chosen decision.

### Action Sufficiency

The next reversible safe action is known.

Do not generate merely because more generation is possible.

---

# 43. Generator Selection

Generator selection belongs primarily to routing.

Conceptually:

```text
SelectGenerator
=
f(
    objective,
    artifact_type,
    domain,
    mode,
    HML_scale,
    evidence_state,
    risk,
    authority,
    deployment_availability
)
```

The smallest sufficient generator should be preferred.

---

# 44. Mode Compatibility

Generator mode can include:

```text
EXPLORE
DIAGNOSE
DESIGN
AUDIT
MEASURE
```

Examples:

```text
HypothesisGenerator + EXPLORE

RepairPlanGenerator + DIAGNOSE

ArchitectureGenerator + DESIGN

CounterexampleGenerator + AUDIT

ExperimentGenerator + MEASURE
```

Mode is independent of generator identity.

---

# 45. Domain Binding

Generators may be domain-neutral or domain-bound.

Example:

```yaml
generator_id: C03_PHYSICS_MODEL_GENERATOR
domain: C03
```

versus:

```yaml
generator_id: GENERIC_MARKDOWN_ARTIFACT_GENERATOR
domain: null
```

A domain-neutral generator cannot supply domain expertise that is absent from its inputs.

---

# 46. Cross-Domain Generation

Cross-domain generation should declare every contributing domain.

Example:

```text
C12 Earth Ecology
+
C07 Economics
+
C09 Policy
+
C10 Engineering
→
Climate Adaptation Infrastructure Candidate
```

Confidence must respect the weakest materially load-bearing cross-domain bridge.

---

# 47. Generator Matrix

A generator may be indexed across several independent axes.

| Axis             | Example         |
| ---------------- | --------------- |
| Family           | PLAN_GENERATOR  |
| Domain           | C12             |
| Mode             | DESIGN          |
| Scale            | M               |
| Epistemic output | MODEL           |
| Execution        | NON_EFFECTFUL   |
| Governance       | REVIEW_REQUIRED |
| Deployment       | SKILL + TOOL    |

This is why `12_GENERATORS` is appropriately a **matrix infrastructure** branch.

---

# 48. Suggested Internal Folder Architecture

The exact file/folder inventory remains an architectural proposal unless separately defined in canon.

```text
12_GENERATORS/
│
├── README.md
│
├── 00_REGISTRY/
│   ├── GENERATOR_REGISTRY.yaml
│   ├── GENERATOR_TYPES.md
│   ├── GENERATOR_STATUS.md
│   └── GENERATOR_VERSION_MAP.md
│
├── 01_CORE/
│   ├── GENERATOR_CONTRACT.md
│   ├── INPUT_OUTPUT_TYPES.md
│   ├── GENERATION_STATE_MACHINE.md
│   ├── OPERATOR_REGISTRY.md
│   └── INVARIANTS.md
│
├── 02_KNOWLEDGE/
├── 03_RSCF_PROOF/
├── 04_HYPOTHESES/
├── 05_PLANS/
├── 06_WORKFLOWS/
├── 07_PROTOCOLS/
├── 08_SCHEMAS/
├── 09_CODE/
├── 10_TESTS/
├── 11_SIMULATIONS/
├── 12_SCENARIOS/
├── 13_DESIGNS/
├── 14_ARTIFACTS/
├── 15_AGENTS/
├── 16_SKILLS/
├── 17_FABRICATION/
│
├── 20_VALIDATION/
│   ├── VALIDATOR_REGISTRY.md
│   ├── ACCEPTANCE_CRITERIA.md
│   ├── ADVERSARIAL_TESTS.md
│   └── FALSIFIER_REGISTRY.md
│
├── 21_PROVENANCE/
│   ├── GENERATION_LINEAGE.md
│   ├── SOURCE_ANCESTRY.md
│   └── SUPERSESSION_LOG.md
│
├── 22_GOVERNANCE/
│   ├── AUTHORITY_REQUIREMENTS.md
│   ├── READ_WRITE_SETS.md
│   ├── COMMIT_POLICY.md
│   └── ROLLBACK_POLICY.md
│
├── 23_OBSERVABILITY/
│   ├── GENERATION_EVENTS.md
│   ├── FAILURE_EVENTS.md
│   └── METRICS.md
│
└── 99_GAPS/
    ├── OPEN_GAPS.md
    ├── UNIMPLEMENTED_GENERATORS.md
    └── UNRESOLVED_CANON.md
```

Do not create a generator folder merely to make the tree look complete.

Unimplemented families should remain explicit placeholders until real content exists.

---

# 49. Generator README Template

Every generator folder should include a README with at least:

# Generator Name

## Identity

## Purpose

## Status

## Scope

## Inputs

## Outputs

## State Variables

## Operators

## Invariants

## Dependencies

## H/M/L Applicability

## Modes

## Authority Requirements

## Read Set

## Proposed Write Set

## Agents

## Skills

## Tools

## Workflows

## Protocols

## Provenance Requirements

## Uncertainty

## Confidence Ceiling

## Failure Modes

## Repair / Recovery

## Validators

## Tests

## Falsifiers

## Deployment Bindings

## Supersession

## Open Gaps

---

# 50. RSCF State for This README

This README is no longer accurately represented as:

```yaml
claim_class: UNKNOWN/GAP
confidence_ceiling: 0
```

because a substantial architecture can now be derived from known AMOS boundaries.

However, implementation-specific claims remain unresolved.

Correct state:

```yaml
claim_class: DERIVED

evidence:
  - AMOS Full Brain OS architecture
  - AMOS OS v4.4 runtime principles
  - RSCF epistemic architecture
  - Infrastructure Control Plane boundaries

provenance:
  origin_architect: Trang Phan
  transformation: generator-infrastructure architecture completion
  status: derived_from_corpus

scope:
  branch: 12_GENERATORS
  role: governed_candidate_generation

regime:
  architecture: AMOS Full Brain OS
  runtime: AMOS OS v4.4

freshness:
  revalidate_on:
    - canon_change
    - generator_contract_change
    - control_plane_change
    - runtime_change

dependencies:
  - OMNI_KERNEL
  - BRAIN_CORE
  - OMNIVERSE_BRAIN
  - AMOS_OS_KERNEL_v4.4
  - RSCF
  - HML
  - CONTROL_PLANE
  - PROVENANCE

competing:
  - generator-as-tool-only architecture
  - generator-as-agent architecture
  - workflow-only generation architecture

falsifiers:
  - provenance cannot survive generation
  - proposal cannot be separated from commit
  - generator semantics cannot be separated from deployment
  - authority cannot be externally enforced

confidence_ceiling:
  architecture: CONDITIONAL
  implementation: UNKNOWN
```

---

# 51. Known Gaps

The following remain `UNKNOWN/GAP` unless specific source artifacts close them:

```text
exact canonical generator registry

exact number of generator families

which generator implementations currently exist

canonical generator naming convention

canonical generator IDs

exact generator-to-skill bindings

exact generator-to-agent bindings

exact generator-to-tool bindings

generator persistence mechanism

generator scheduler implementation

generator transaction implementation

generator-specific authority schemas

generator-specific runtime state schemas

canonical location of every generator family

version precedence among historical generator artifacts
```

Do not invent these merely to complete the matrix.

---

# 52. Promotion Rules

A generator moves from:

```text
PLACEHOLDER
```

to:

```text
DEFINED
```

when its semantic contract is complete.

From:

```text
DEFINED
```

to:

```text
IMPLEMENTED
```

when a concrete executable binding exists.

From:

```text
IMPLEMENTED
```

to:

```text
TESTED
```

when relevant tests have actually run.

From:

```text
TESTED
```

to:

```text
VALIDATED
```

only when evidence supports its intended behavior and scope.

From:

```text
VALIDATED
```

to:

```text
DEPLOYABLE
```

only when authority, safety, and environment requirements are satisfied.

None of those states are automatic.

---

# 53. Anti-Regression Contract

Any future modification to `12_GENERATORS` must preserve or improve:

```text
factual support
epistemic typing
provenance recoverability
scope correctness
regime correctness
contradiction visibility
causal discipline
authority separation
proposal/commit separation
rollback capability
user fit
```

An optimization that weakens one of these must be rejected or rolled back.

---

# 54. Core Laws

```text
INTEGRITY
>
COMPLETENESS
>
FLUENCY
>
SPEED
>
TOKEN SAVINGS
```

and:

```text
GENERATION
!=
VALIDATION
```

```text
VALIDATION
!=
AUTHORIZATION
```

```text
AUTHORIZATION
!=
EXECUTION
```

```text
EXECUTION
!=
SUCCESS
```

```text
SUCCESS
!=
TRUTH
```

```text
REPETITION
!=
INDEPENDENT CONFIRMATION
```

```text
STRUCTURAL SIMILARITY
!=
CAUSATION
```

```text
PLACEHOLDER
!=
IMPLEMENTED
```

```text
ADDRESSABLE
!=
VALIDATED
```

```text
CAPABILITY
!=
AUTHORITY
```

```text
PROPOSAL
!=
COMMIT
```

```text
UNKNOWN/GAP
!=
PASS
```

---

# 55. Final Contract

`12_GENERATORS` exists to make generation **governed, typed, provenance-aware, repairable, auditable, and separable from authority**.

Its job is not:

```text
make AMOS generate more
```

Its job is:

```text
make every generation
addressable
typed
bounded
traceable
challengeable
repairable
and safe to either reject,
retain as a proposal,
or commit under independent authority
```

The branch is complete only when each registered generator can answer:

```text
WHAT does it generate?

FROM WHAT inputs?

UNDER WHAT scope?

USING WHICH dependencies?

WITH WHICH operators?

PRESERVING WHICH invariants?

AT WHICH H/M/L scale?

UNDER WHICH regime?

WITH WHAT provenance?

WITH WHAT uncertainty?

WHAT can falsify it?

HOW can it fail?

HOW is it repaired?

WHO may invoke it?

WHO may authorize effects?

HOW is its output validated?

WHEN may it be committed?

HOW is it rolled back?

WHAT remains unknown?
```

Until those questions are answered for an individual generator:

```text
generator_status
=
UNKNOWN / PARTIAL
```

not:

```text
READY
```

```

This is the appropriate replacement for the current placeholder README: the **branch-level architecture is now substantially defined**, while the actual registry of implemented generators remains an explicit gap rather than being fabricated. The key AMOS Full Brain boundary underneath it is that capability, runtime reasoning, authority, and deployment are distinct layers; a generator can produce a candidate without acquiring execution or commit authority. :contentReference[oaicite:2]{index=2}

**Conclusion class:** `DERIVED / CONDITIONAL`. The contract is AMOS-consistent; exact generator implementations and the canonical generator inventory remain `UNKNOWN/GAP`.
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[GENERATORS_MAP]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: generators_cognitive_matrix_readme
node_type: note
path: 25_COGNITIVE_MATRIX/12_GENERATORS/GENERATORS_COGNITIVE_MATRIX_README.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[12_GENERATORS_MOC]]
