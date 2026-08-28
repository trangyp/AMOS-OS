---
title: AGENT TEMPLATES
type: agent
source: 11_KNOWLEDGE
canon-group: meta
canon-type: framework
canon-status: active
canon-scope: agent-architecture
canon-layer: meta-agent
canon-owner: Trang Phan
artifact-id: AMOS-AGENT-TEMPLATES
artifact-type: framework-registry
artifact-class: agent-factory-architecture
version: "2.0.0"
schema-version: "1.0.0"
protocol-version: "1.0.0"
amos-core-target: "v4.4"
rscf-state: source-claim
rscf-class: STRUCTURAL_MODEL
rscf-confidence-ceiling: source-bounded
rscf-provenance-required: true
topic: agent-templates
tags: [canon-group/tech-ai, knowledge, vault, canon/framework, canon/agent, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/agent-templates, topic/agent-architecture, topic/agent-factory, agents]
created: 2026-08-22
updated: 2026-08-25
origin-architect: Trang Phan
steward: Trang Phan
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---


# AMOS Agent Templates

> **Version:** `2.0.0`  
> **Schema Version:** `1.0.0`  
> **Protocol Version:** `1.0.0`  
> **AMOS_CORE Target:** `v4.4`  
> **Origin Architect:** Trang Phan  
> **Classification:** `STRUCTURAL_MODEL`  
> **RSCF State:** `SOURCE_CLAIM`

---

## 1. Purpose

**AMOS Agent Templates** defines the canonical structural templates used to instantiate, configure, validate, govern, version, and retire agents inside the AMOS ecosystem.

The framework does **not** define one universal agent implementation.

It defines the minimum structural contract from which specialized AMOS agents can be constructed without losing:

- identity;
- purpose;
- scope;
- authority;
- capability boundaries;
- dependency lineage;
- provenance;
- evidence classification;
- runtime constraints;
- input/output contracts;
- governance;
- validation;
- version identity;
- lifecycle state;
- rollback and retirement semantics.

The governing principle is:

```text
Agent
=
Identity
+ Purpose
+ Scope
+ Capabilities
+ Dependencies
+ Authority
+ State
+ Runtime
+ Governance
+ Evidence
+ Validation
+ Lifecycle
```

This is an **AMOS structural equation**, not an empirical law of all agent systems.

---

# 2. Canonical Position

```text
AMOS
└── Meta Architecture
    └── Agent Architecture
        ├── Agent Schema
        ├── Agent Templates
        ├── Agent Assembly
        ├── Agent Runtime
        ├── Agent Governance
        ├── Agent Validation
        └── Agent Lifecycle
```

`Agent Templates` sits between the abstract schema and concrete agent instances.

```text
AGENT_SCHEMA
      ↓
AGENT_TEMPLATE
      ↓
AGENT_CONFIGURATION
      ↓
AGENT_INSTANCE
      ↓
RUNTIME_VALIDATION
      ↓
GOVERNED_EXECUTION
```

Hard distinction:

```text
Schema
!=
Template
!=
Configuration
!=
Runtime Instance
```

---

# 3. Framework Invariants

Every AMOS agent template MUST preserve the following invariants.

## AT-I01 — Identity

Every agent has an explicit identity.

```text
AgentIdentity != implicit role inferred from prompt
```

---

## AT-I02 — Purpose

Every agent declares why it exists.

```text
AgentPurpose
=
DeclaredObjectiveSet
```

An agent without a bounded purpose is incomplete.

---

## AT-I03 — Scope

Every agent declares:

```text
IN_SCOPE
OUT_OF_SCOPE
```

Absence of an explicit exclusion does not automatically grant capability or authority.

---

## AT-I04 — Capability / Authority Separation

```text
CanPerform(x)
!=
AuthorizedToPerform(x)
```

Technical capability never creates authority.

---

## AT-I05 — Dependency Declaration

Every load-bearing runtime dependency must be identifiable.

```text
AgentValid
→
DependenciesResolvable
```

---

## AT-I06 — Provenance

Consequential claims and state transitions must remain traceable to their relevant sources.

```text
Claim
→ Source
→ Transformation
→ Dependency
→ Result
```

---

## AT-I07 — Evidence Boundary

Agent outputs must distinguish, where material:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN/GAP
```

---

## AT-I08 — Scope / Regime Boundary

An agent cannot silently generalize beyond its declared applicability envelope.

```text
ValidOutput
→
ScopeCompatible
∧ RegimeCompatible
```

---

## AT-I09 — Safety

Agent objectives do not override higher-order constraints.

```text
UserObjective
∩
AgentCapability
∩
Authority
∩
Governance
∩
Safety
=
AdmissibleActionSpace
```

---

## AT-I10 — Version Identity

Every template and instantiated agent must expose a version identity.

```text
TemplateVersion
!=
InstanceVersion
!=
RuntimeVersion
```

---

## AT-I11 — Lifecycle

Every agent occupies an explicit lifecycle state.

```text
DRAFT
→ REVIEW
→ VALIDATED
→ ACTIVE
→ DEPRECATED
→ RETIRED
```

Transitions need not be strictly linear, but promotion must be governed.

---

## AT-I12 — No Decorative Completion

```text
Configured
!=
Integrated

Integrated
!=
Executed

Executed
!=
Validated

Validated
!=
Authorized
```

---

# 4. Agent Template Tensor

The canonical template can be represented as:

```text
A[
  identity,
  purpose,
  domain,
  scope,
  capability,
  authority,
  dependency,
  state,
  memory,
  tools,
  language,
  input,
  output,
  governance,
  provenance,
  validation,
  lifecycle,
  version
]
```

Each axis carries its own type and constraints.

A value on one axis cannot silently satisfy another.

For example:

```text
capability.tool_access = true
```

does not imply:

```text
authority.tool_execution = true
```

---

# 5. Canonical Agent Template

```yaml
agent:
  identity:
    agent_id: ""
    agent_name: ""
    short_label: ""
    category: ""
    domain: ""
    sub_domains: []

  version:
    template_version: "2.0.0"
    instance_version: "0.1.0"
    runtime_version: ""
    schema_version: "1.0.0"

  ownership:
    origin_architect: "Trang Phan"
    framework: "AMOS"
    steward: ""

  purpose:
    primary_objective: ""
    secondary_objectives: []
    success_conditions: []
    termination_conditions: []

  scope:
    in_scope: []
    out_of_scope: []
    assumptions: []
    applicability:
      systems: []
      environments: []
      regimes: []
      temporal_scope: ""

  capabilities:
    enabled: []
    conditional: []
    disabled: []

  authority:
    authority_class: ""
    allowed_actions: []
    prohibited_actions: []
    escalation_required: []
    irreversible_actions: []

  dependencies:
    required: []
    optional: []
    forbidden: []

  runtime:
    execution_mode: ""
    state_model: ""
    concurrency_model: ""
    failure_mode: "fail_closed"
    fallback_policy: ""
    rollback_policy: ""

  memory:
    enabled: false
    read_scope: []
    write_scope: []
    retention_policy: ""
    provenance_required: true
    invalidation_policy: ""

  tools:
    allowed: []
    conditional: []
    prohibited: []

  inputs:
    accepted_types: []
    required_fields: []
    optional_fields: []
    validation_rules: []

  outputs:
    output_types: []
    required_fields: []
    evidence_classes: []
    uncertainty_required: true

  governance:
    policy_gate_required: true
    authority_check_required: true
    provenance_check_required: true
    commit_time_revalidation: false
    human_escalation_conditions: []

  validation:
    static_checks: []
    runtime_checks: []
    integration_checks: []
    regression_checks: []
    acceptance_criteria: []

  lifecycle:
    state: "draft"
    created_at: ""
    validated_at: ""
    activated_at: ""
    deprecated_at: ""
    retired_at: ""

  provenance:
    source_id: ""
    source_version: ""
    parent_template: ""
    derived_from: []
    transformations: []

  rscf:
    claim_class: "STRUCTURAL_MODEL"
    dependencies: []
    competing: []
    falsifiers: []
    confidence_ceiling: ""
```

---

# 6. Template Families

AMOS agent templates are organized by **function**, not by arbitrary persona.

Canonical families:

```text
T00 — BASE
T01 — ANALYST
T02 — RESEARCHER
T03 — DESIGNER
T04 — ENGINEER
T05 — AUDITOR
T06 — VALIDATOR
T07 — GOVERNOR
T08 — ORCHESTRATOR
T09 — EXECUTION_SUPPORT
T10 — SIMULATOR
T11 — TRAINER
T12 — SPECIALIST
T13 — OBSERVER
T14 — RECOVERY
```

These families describe functional architecture.

They do not imply independent autonomous authority.

---

# 7. T00 — Base Agent

Every AMOS agent inherits the base contract.

```yaml
template:
  id: T00
  name: AMOS_BASE_AGENT

  purpose:
    primary_objective: "Perform a bounded assigned function."

  invariants:
    - preserve_scope
    - preserve_provenance
    - distinguish_capability_from_authority
    - expose_material_uncertainty
    - do_not_invent_missing_evidence
    - fail_closed_on_critical_unknowns

  governance:
    authority_required: true
    provenance_required: true
    scope_check_required: true

  lifecycle:
    initial_state: draft
```

---

# 8. T01 — Analyst Agent

Purpose:

```text
Problem
→ Decomposition
→ Evidence
→ Alternatives
→ Implications
```

Primary capabilities:

* structured decomposition;
* comparison;
* dependency analysis;
* trade-off analysis;
* sensitivity analysis;
* competing-hypothesis analysis.

The analyst does not automatically execute its recommendations.

```text
Analysis
!=
AuthorityToAct
```

---

# 9. T02 — Research Agent

Purpose:

```text
Question
→ Retrieval
→ Evidence
→ Provenance
→ Synthesis
→ Claim
```

Required controls:

```text
source identity
source ancestry
freshness
scope
regime
contradiction
independence
falsifiers
```

Hard rule:

```text
RepeatedSource
!=
IndependentConfirmation
```

---

# 10. T03 — Designer Agent

Purpose:

```text
Requirement
→ Constraints
→ Alternatives
→ Architecture
→ Validation Plan
```

Required distinction:

```text
DesignPlausibility
!=
ImplementedCapability
```

Designer outputs default to:

```text
MODEL
```

until implemented and validated.

---

# 11. T04 — Engineer Agent

Purpose:

```text
Requirement
→ Repository Evidence
→ Implementation
→ Integration
→ Test
→ Verification
```

Required completion model:

```text
EngineeringComplete
=
Implementation
∧ Integration
∧ Runtime
∧ Tests
∧ Regression
∧ Provenance
```

Where applicable:

```text
∧ Security
∧ Migration
∧ Rollback
∧ Performance
```

---

# 12. T05 — Auditor Agent

Purpose:

```text
ClaimedState
vs
ObservedState
```

The auditor must remain structurally independent from the claim it evaluates where independence is required.

Primary outputs:

```text
PASS
FAIL
CONDITIONAL
UNKNOWN/GAP
```

A report must not manufacture evidence for itself.

---

# 13. T06 — Validator Agent

Purpose:

```text
CandidateClaim
+
Evidence
+
Falsifiers
→
ValidationState
```

Canonical validation states:

```text
VERIFIED
DERIVED
CONDITIONAL
COMPETING
FALSIFIED
UNKNOWN/GAP
```

The validator may not promote a claim beyond its weakest load-bearing premise.

---

# 14. T07 — Governor Agent

Purpose:

```text
ProposedAction
→ Authority
→ Policy
→ Constraints
→ Risk
→ Decision
```

Conceptual gate:

```text
Admissible(a)
=
Scope(a)
∧ Authority(a)
∧ Policy(a)
∧ Constraint(a)
∧ Risk(a)
```

The governor controls admissibility.

It does not replace domain expertise.

---

# 15. T08 — Orchestrator Agent

Purpose:

```text
Objective
→ Decomposition
→ Routing
→ Coordination
→ Validation
→ Synthesis
```

The orchestrator should coordinate specialists without absorbing their domain logic.

Invariant:

```text
Orchestration
!=
DomainImplementation
```

---

# 16. T09 — Execution Support Agent

Purpose:

```text
ValidatedDecision
→ ExecutablePlan
```

Typical outputs:

* plans;
* checklists;
* commands;
* procedures;
* implementation sequences.

Execution support does not imply unrestricted execution authority.

---

# 17. T10 — Simulator Agent

Purpose:

```text
InitialState
+
Assumptions
+
Model
→
SimulatedOutcome
```

Hard firewall:

```text
Simulation
!=
ObservedReality
```

Every simulation must preserve its assumption boundary.

---

# 18. T11 — Trainer Agent

Purpose:

```text
LearningObjective
→ Explanation
→ Practice
→ Feedback
→ Assessment
```

Training assessment must not be confused with validated real-world competence unless the assessment supports that conclusion.

---

# 19. T12 — Specialist Agent

Specialist agents extend the base template with bounded domain expertise.

```text
BASE
+
DOMAIN_CONTRACT
+
DOMAIN_EVIDENCE
+
DOMAIN_CONSTRAINTS
=
SPECIALIST
```

Examples may include:

```text
legal
financial
engineering
research
design
governance
data
software
```

High-risk specialists require stronger governance.

---

# 20. T13 — Observer Agent

Purpose:

```text
System
→ Observation
→ State Representation
```

The observer must distinguish:

```text
Observed
Measured
Inferred
Derived
```

Observation does not automatically establish causation.

---

# 21. T14 — Recovery Agent

Purpose:

```text
Failure
→ Localization
→ Dependency Closure
→ Rollback / Repair
→ Revalidation
```

Recovery invariant:

```text
Repair
must preserve
unaffected valid state.
```

Global recomputation is a last resort.

---

# 22. H / M / L Agent Structure

Every non-trivial agent can be represented recursively.

```text
H — Governing Agent Level
    objective
    authority
    scope
    governance
    success criteria

M — Capability / Subsystem Level
    analysis
    tools
    memory
    dependencies
    specialist modules

L — Execution Level
    functions
    commands
    API calls
    reads
    writes
    tests
    evidence
```

Invariant:

```text
H claim confidence
≤
weakest load-bearing M/L premise
```

unless independently revalidated.

---

# 23. Input Contract

Every template must define accepted input.

```yaml
input_contract:
  required:
    - objective

  optional:
    - context
    - constraints
    - evidence
    - attachments
    - desired_output

  validation:
    - objective_is_resolvable
    - scope_is_defined
    - required_authority_is_available
```

Ambiguous input should not be silently converted into a high-impact action.

---

# 24. Output Contract

Canonical output structure:

```yaml
output:
  conclusion:
    class:
    statement:

  evidence:
    sources: []
    observations: []

  uncertainty:
    evidence:
    model:
    scope:
    temporal:
    causal:
    execution:
    provenance_independence:

  dependencies: []

  competing_hypotheses: []

  falsifiers: []

  action:
    recommendation:
    authority_required:
```

Not every response needs every field rendered.

The template defines the conceptual contract.

---

# 25. RSCF Contract

Important agent conclusions should conceptually carry:

```text
Claim
Class
Premises
Evidence
Provenance
Scope
Regime
Freshness
Dependencies
Competing Hypotheses
Falsifiers
Confidence Ceiling
```

Compact form:

```yaml
rscf:
  claim:
  class:
  premises: []
  evidence: []
  dependencies: []
  competing: []
  falsifiers: []
  confidence_ceiling:
```

---

# 26. Agent State Machine

Canonical lifecycle:

```text
UNDEFINED
    ↓
DRAFT
    ↓
CONFIGURED
    ↓
VALIDATING
    ↓
VALIDATED
    ↓
ACTIVE
    ↓
SUSPENDED
    ↓
DEPRECATED
    ↓
RETIRED
```

Additional failure state:

```text
QUARANTINED
```

A quarantined agent cannot silently return to `ACTIVE`.

---

# 27. Promotion Gates

```text
DRAFT → CONFIGURED
requires
Identity + Purpose + Scope

CONFIGURED → VALIDATED
requires
ContractValidation + DependencyValidation

VALIDATED → ACTIVE
requires
Authority + RuntimeAcceptance

ACTIVE → SUSPENDED
triggered by
Failure / Revocation / Staleness / PolicyChange

SUSPENDED → ACTIVE
requires
Revalidation

ANY → QUARANTINED
triggered by
CriticalIntegrityFailure
```

---

# 28. Versioning

AMOS agent templates use semantic structural versioning.

```text
MAJOR.MINOR.PATCH
```

## MAJOR

Increment when:

* required contract changes;
* lifecycle semantics change;
* authority semantics change;
* incompatible fields are introduced or removed.

## MINOR

Increment when:

* backward-compatible capability is added;
* optional governance fields are added;
* new template families are introduced.

## PATCH

Increment when:

* documentation is corrected;
* metadata is repaired;
* non-semantic clarifications are made.

---

# 29. Version Lineage

```yaml
version_lineage:
  current: "2.0.0"

  predecessors:
    - version: "1.x"
      status: historical

  compatibility:
    schema: "1.0.0"
    amos_core_target: "v4.4"

  migration_required_when:
    - authority_contract_changes
    - lifecycle_contract_changes
    - required_fields_change
    - provenance_contract_changes
```

Never silently overwrite version lineage.

---

# 30. Template Inheritance

Templates may inherit from another template.

```text
ChildTemplate
=
ParentTemplate
+
AllowedExtension
```

But inheritance follows:

```text
ChildAuthority
⊆
ParentMaximumAuthority
```

unless a separate authority grant exists.

A child template cannot obtain new authority merely through inheritance.

---

# 31. Constraint Propagation

Parent constraints propagate downward.

```text
C_child
=
C_parent
∪
C_local
```

A child may tighten constraints.

It may not silently weaken a hard parent invariant.

---

# 32. Capability Extension

```text
Capabilities_child
=
Capabilities_parent
∪
Capabilities_extension
```

subject to:

```text
SchemaValid
∧ DependencyValid
∧ AuthorityValid
∧ GovernanceValid
```

---

# 33. Agent Assembly

Agent construction follows:

```text
Schema
↓
Select Template
↓
Bind Identity
↓
Bind Purpose
↓
Bind Domain
↓
Bind Capabilities
↓
Bind Dependencies
↓
Bind Authority
↓
Bind Governance
↓
Validate
↓
Instantiate
```

No agent should be instantiated from capability declarations alone.

---

# 34. Assembly Validation

```text
AssemblyValid
=
IdentityValid
∧ PurposeValid
∧ ScopeValid
∧ DependencyValid
∧ CapabilityValid
∧ AuthorityValid
∧ GovernanceValid
∧ VersionValid
```

If a critical term is unresolved:

```text
AssemblyState = BLOCKED
```

---

# 35. Runtime Preflight

Before consequential execution:

```text
Preflight
=
ScopeFresh
∧ DependenciesAvailable
∧ AuthorityValid
∧ PolicyValid
∧ StateValid
∧ ProvenanceValid
```

For mutable or irreversible effects, preflight alone is insufficient.

---

# 36. Commit-Time Revalidation

For consequential effects:

```text
Commit(effect)
=
PreflightPassed
∧ ReadSetFresh
∧ AuthorityFresh
∧ PolicyFresh
∧ ConstraintFresh
∧ ConflictFree
```

Conceptual principle:

```text
AuthorizedAtPlanTime
!=
AuthorizedAtCommitTime
```

---

# 37. Tool Contract

Tool access must be explicit.

```yaml
tools:
  read:
    allowed: []

  write:
    allowed: []

  external_effect:
    allowed: []

  prohibited: []

  escalation:
    required_for: []
```

Hard invariant:

```text
ToolAvailable
!=
ToolAuthorized
```

---

# 38. Memory Contract

Memory-capable agents must distinguish:

```text
Recall
Working State
Persistent Memory
Evidence
Canon
```

These are not interchangeable.

```text
Memory
!=
Truth

Memory
!=
Authority

Memory
!=
Canon
```

---

# 39. Memory Admission

Conceptual admission gate:

```text
Admit(m)
=
SourceKnown
∧ ScopeKnown
∧ ProvenanceKnown
∧ PolicyCompatible
∧ ContaminationRiskAcceptable
```

Otherwise:

```text
REJECT
QUARANTINE
CONDITIONAL
```

---

# 40. Provenance Contract

```yaml
provenance:
  template_id:
  template_version:
  parent_template:
  source_artifacts: []
  transformations: []
  instantiated_by:
  instantiated_at:
  validated_by:
  validation_epoch:
```

Agent provenance must survive downstream transformation when decision-relevant.

---

# 41. Agent Dependency Graph

Represent dependencies as:

```text
Agent
├── Core
├── Template
├── Domain Engine
├── Memory
├── Tools
├── Policy
├── Data
└── External Services
```

A failed dependency invalidates only dependent claims and actions.

```text
Invalidate(D)
→
Descendants(D)
```

not automatically the entire agent ecosystem.

---

# 42. Failure Recovery

```text
Failure
↓
Locate Failed Premise
↓
Identify Dependency Closure
↓
Quarantine Affected State
↓
Preserve Valid State
↓
Repair / Replace
↓
Revalidate
↓
Resume or Retire
```

Hard rule:

```text
DoNotRepeatFailedPath
unless
EvidenceChanged
```

---

# 43. Agent Audit

Every active template should be auditable across:

```text
Identity
Purpose
Scope
Capability
Authority
Dependencies
Memory
Tools
Governance
Runtime
Provenance
Version
Validation
Lifecycle
```

Canonical audit output:

```yaml
audit:
  identity: PASS
  purpose: PASS
  scope: PASS
  capability: PASS
  authority: PASS
  dependencies: PASS
  provenance: PASS
  runtime: CONDITIONAL
  validation: PASS
  lifecycle: PASS

  overall: CONDITIONAL
```

Overall status cannot exceed a critical failed dimension.

---

# 44. Agent Completion

```text
AgentComplete
=
SchemaComplete
∧ ConfigurationComplete
∧ DependencyComplete
∧ GovernanceComplete
∧ ValidationComplete
```

But:

```text
AgentComplete
!=
UniversallyCorrect
```

Completion is scoped to the declared contract.

---

# 45. Agent Template Registry

```yaml
registry:
  T00:
    name: AMOS_BASE_AGENT
    function: foundational

  T01:
    name: AMOS_ANALYST_AGENT
    function: analysis

  T02:
    name: AMOS_RESEARCH_AGENT
    function: research

  T03:
    name: AMOS_DESIGNER_AGENT
    function: design

  T04:
    name: AMOS_ENGINEER_AGENT
    function: engineering

  T05:
    name: AMOS_AUDITOR_AGENT
    function: audit

  T06:
    name: AMOS_VALIDATOR_AGENT
    function: validation

  T07:
    name: AMOS_GOVERNOR_AGENT
    function: governance

  T08:
    name: AMOS_ORCHESTRATOR_AGENT
    function: orchestration

  T09:
    name: AMOS_EXECUTION_SUPPORT_AGENT
    function: execution_support

  T10:
    name: AMOS_SIMULATOR_AGENT
    function: simulation

  T11:
    name: AMOS_TRAINER_AGENT
    function: training

  T12:
    name: AMOS_SPECIALIST_AGENT
    function: domain_specialization

  T13:
    name: AMOS_OBSERVER_AGENT
    function: observation

  T14:
    name: AMOS_RECOVERY_AGENT
    function: recovery
```

---

# 46. Anti-Patterns

Do not create:

```text
AGENT_WITHOUT_SCOPE
AGENT_WITHOUT_VERSION
AGENT_WITH_IMPLICIT_AUTHORITY
AGENT_WITH_UNBOUNDED_TOOLS
AGENT_WITH_UNTRACEABLE_MEMORY
AGENT_WITHOUT_FAILURE_STATE
AGENT_WITHOUT_TERMINATION
AGENT_WITH_DECORATIVE_GOVERNANCE
AGENT_WHERE_PERSONA_REPLACES_FUNCTION
AGENT_WHERE_CAPABILITY_EQUALS_PERMISSION
AGENT_WHERE_OUTPUT_EQUALS_EVIDENCE
```

---

# 47. Template Selection Rule

Choose the smallest template capable of satisfying the objective.

```text
Template*
=
argmin Complexity(T)
```

subject to:

```text
ObjectiveCovered(T)
∧ ConstraintsSatisfied(T)
∧ GovernanceSatisfied(T)
```

Do not create an orchestrator where a bounded analyst is sufficient.

---

# 48. Composition

Multiple templates may compose:

```text
ORCHESTRATOR
├── RESEARCHER
├── ANALYST
├── DESIGNER
└── VALIDATOR
```

But composition does not merge authority automatically.

```text
Authority(composite)
!=
Σ Authority(children)
```

Authority must be explicitly resolved.

---

# 49. Separation of Cognition and Control

AMOS agent architecture should preserve:

```text
Cognition
=
propose / analyze / infer

Control
=
authorize / constrain / commit
```

A stochastic worker may propose an action.

A governed control layer determines whether that action may become an effect.

---

# 50. RSCF Node

```yaml
node_id: AMOS_AGENT_TEMPLATES_V2

functional_type: Framework
lifecycle_stage: Active
claim_class: STRUCTURAL_MODEL

claim: >
  AMOS agents can be constructed from reusable governed templates that
  explicitly separate identity, purpose, scope, capability, authority,
  dependencies, runtime state, provenance, validation, and lifecycle.

premises:
  - agent roles require explicit structural boundaries
  - capability and authority are distinct
  - consequential outputs require provenance
  - runtime state requires lifecycle governance
  - reusable templates reduce uncontrolled structural divergence

dependencies:
  - AGENT_SCHEMA
  - AMOS_AGENT_ONBOARDING
  - AMOS_CORE
  - governance_layer
  - provenance_layer

competing:
  - fully ad-hoc prompt-defined agents
  - monolithic universal agent
  - capability-only agent definitions
  - role/persona-only agent definitions

falsifiers:
  - template cannot represent required agent function
  - mandatory fields create contradictory contracts
  - authority cannot be represented independently of capability
  - inheritance breaks parent constraints
  - lifecycle cannot represent runtime transitions

confidence_ceiling: >
  Structural AMOS framework. Does not establish that this template
  architecture is universally optimal for all agent systems.
```

---

# 51. Version History

## v2.0.0 — 2026-08-25

Major governed architecture revision.

Added:

* explicit artifact identity;
* document/schema/protocol version separation;
* AMOS_CORE target;
* canonical agent tensor;
* fourteen functional template families plus base template;
* H/M/L decomposition;
* capability/authority separation;
* RSCF output contract;
* provenance contract;
* memory contract;
* tool contract;
* dependency graph;
* lifecycle state machine;
* promotion gates;
* template inheritance;
* constraint propagation;
* assembly validation;
* runtime preflight;
* commit-time revalidation;
* failure recovery;
* selective invalidation;
* audit structure;
* template registry;
* composition rules;
* cognition/control separation;
* anti-pattern registry;
* semantic versioning rules.

## v1.x — Historical

Initial agent-template framework family.

Historical content should remain available through version lineage rather than being silently overwritten.

---

# 52. Canonical Rule

```text
SCHEMA
↓
TEMPLATE
↓
CONFIGURATION
↓
VALIDATION
↓
INSTANCE
↓
AUTHORIZATION
↓
EXECUTION
↓
OBSERVATION
↓
REVALIDATION
↓
EVOLUTION / RETIREMENT
```

The central invariant is:

> **An AMOS agent is not merely a prompt or persona. It is a versioned, scoped, provenance-aware, governed runtime role whose capability, authority, evidence, state, dependencies, and lifecycle remain explicitly distinguishable.**

---

**Related:** [[00_HOME]] · 06-Knowledge-Base-MOC · [[AGENT_SCHEMA]] · AMOS_AGENT_ONBOARDING_GUIDE · AMOS_Simulation_Kernel_v0_Math_Foundations · system_scan_agent · automation_profiles

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: agent_templates
node_type: note
path: 11_KNOWLEDGE/Agent_Templates.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[KNOWLEDGE_MOC]]
