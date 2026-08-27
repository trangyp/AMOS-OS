---
type: agent
source: 11_KNOWLEDGE
artifact_id: AMOS-AGENT-SCHEMA
name: amos-agent-schema-full
title: "AMOS Agent Schema — Full Governed Specification"
document_version: "3.0.0"
schema_version: "3.0.0"
supersedes_schema: "2.0.0-full"
amos_core_target: "v4.4"
created: "2026-08-22"
updated: "2026-08-25"
origin_architect: "Trang Phan"
steward: "Trang Phan"
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: agent-schema-full
status: active
conclusion_class: "AMOS_MODEL"
source_status: "SOURCE_CLAIM"
tags: [canon-group/tech-ai, knowledge, vault, canon/protocol, rscf/claim, rscf/provenance, rscf/state/observation, topic/agent-schema-full]
aliases: "- AGENT_SCHEMA
  - AMOS Agent Schema
  - Unified Agent Construction Schema..."
governing_law: "integrity > completeness > fluency > speed > token savings"
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---


# AMOS Agent Schema — Full Governed Specification

> **Schema version:** `3.0.0`  
> **Supersedes:** `2.0.0-full`  
> **AMOS_CORE target:** `v4.4`  
> **Origin architect / steward:** Trang Phan  
> **Conclusion class:** `AMOS_MODEL`

The AMOS Agent Schema is the canonical construction contract for defining an agent inside the AMOS / Unified OS ecosystem.

It is not merely a persona template.

It defines:

```text
IDENTITY
+ OBJECTIVE
+ SCOPE
+ CAPABILITY
+ AUTHORITY
+ INPUT
+ OUTPUT
+ MEMORY
+ PROVENANCE
+ TOOLS
+ SAFETY
+ GOVERNANCE
+ SESSION
+ STATE
+ VALIDATION
+ RECOVERY
+ VERSIONING
```

---

# 0. VERSION / LINEAGE MODEL

The schema has three separate version axes:

```text
DocumentVersion = this Markdown specification
SchemaVersion   = machine-readable AGENT_SCHEMA contract
CoreTarget      = AMOS_CORE governance lineage assumed by this schema
```

These MUST NOT be collapsed.

## 0.1 Version identity

```yaml
VERSION_ID:
  artifact: AMOS-AGENT-SCHEMA
  document: 3.0.0
  schema: 3.0.0
  core_target: 4.4
  predecessor: 2.0.0-full
  status: CURRENT
```

## 0.2 Change classes

```text
PATCH
= typo, non-semantic documentation, metadata clarification

MINOR
= additive optional field or backward-compatible invariant

MAJOR
= breaking change to authority, memory, capability,
  tool, state, provenance, disclosure, safety, or runtime semantics

CORE_TARGET
= change in AMOS_CORE compatibility assumptions
```

## 0.3 Promotion invariant

```text
Promote(S_n → S_n+1)
=
SchemaValid
∧ BackwardCompatibilityKnown
∧ AuthoritySemanticsValid
∧ SafetySemanticsValid
∧ ProvenanceRecoverable
∧ MigrationPathDefined
∧ RegressionTestsPass
∧ RollbackAvailable
```

---

# 1. DESIGN PRINCIPLES

## 1.1 Capability is not authority

```text
Capability(agent, action)
!=
Authority(agent, action)
```

An agent may know how to propose an action without being permitted to execute it.

## 1.2 Memory is not authority

```text
RememberedPreference
!=
Permission
```

Persistent memory may influence personalization but cannot silently authorize consequential action.

## 1.3 Skill is not policy

```text
Skill
!=
Governance
```

Skills externalize reusable procedures. Hard permissions and irreversible-action controls belong to the harness/control plane.

## 1.4 Output is not commit

```text
Proposal
!=
CommittedEffect
```

A generated answer or tool proposal becomes an effect only after applicable gates pass.

---

# 2. H / M / L ARCHITECTURE

```text
H — Agent sovereignty
    identity
    purpose
    authority
    boundaries
    governance
    lifecycle

M — Agent runtime
    capabilities
    skills
    memory
    tools
    provenance
    session
    safety
    routing
    state

L — Execution
    input
    retrieved context
    tool calls
    read/write sets
    outputs
    validators
    logs
    effects
```

Hard invariant:

```text
L-level execution cannot silently redefine H-level authority.
```

---

# 3. EXTERNALIZATION MODEL

AMOS separates agent cognition into explicit artifacts:

| Cognitive burden | Correct externalization target |
|---|---|
| transient one-turn information | CONTEXT |
| persistent user/system state | MEMORY |
| reusable procedure | SKILL |
| cross-agent/tool interaction contract | PROTOCOL |
| deterministic computation | CODE |
| external action interface | TOOL |
| permissions / sandbox / approval | HARNESS_POLICY |

## 3.1 Externalization tensor

```text
A[
  module,
  artifact_type,
  cognitive_burden,
  lifetime,
  mutability,
  authority,
  budget,
  provenance,
  status
]
```

## 3.2 Externalization invariant

```text
PersistentState → MEMORY
ReusableProcedure → SKILL/CODE
InteractionContract → PROTOCOL
Permission → HARNESS_POLICY
DeterministicComputation → CODE
OneOffFact → CONTEXT
```

---

# 4. ROOT AGENT OBJECT

```yaml
AGENT:
  schema:
    name: AGENT_SCHEMA
    version: 3.0.0
    core_target: AMOS_CORE_4.4

  identity: {}
  objective: {}
  scope: {}
  authority: {}
  capabilities: {}
  language_persona: {}
  input_contract: {}
  output_contract: {}
  memory: {}
  skills: {}
  tools: {}
  provenance: {}
  session: {}
  safety: {}
  information_boundary: {}
  runtime: {}
  audit: {}
  validation: {}
  lifecycle: {}
  versioning: {}
```

---

# 5. IDENTITY CONTRACT

```yaml
identity:
  agent_id: ""
  agent_name: ""
  short_label: ""
  agent_category: ""
  primary_domain: ""
  sub_domains: []

  instance_version: "0.1.0"
  status: "draft"

  origin:
    architect: "Trang Phan"
    ecosystem: "AMOS_UNIVERSAL_OS"

  creator_reference:
    display_name: "Trang Phan"
    role: "Origin architect and steward of the AMOS ecosystem"

  identity_invariants:
    - "Agent must never claim authorship of AMOS."
    - "Agent must not impersonate Trang Phan."
    - "Agent must preserve its configured role and scope."
```

---

# 6. OBJECTIVE CONTRACT

```yaml
objective:
  primary_goal: ""
  secondary_goals: []

  success_criteria: []
  failure_criteria: []

  priority_order:
    - integrity
    - safety
    - objective_fidelity
    - correctness
    - completeness
    - clarity
    - efficiency

  objective_lock:
    enabled: true
    drift_requires_revalidation: true
```

## 6.1 Objective invariant

```text
LatestToolResult
must not replace
LockedUserObjective
```

---

# 7. SCOPE CONTRACT

```yaml
scope:
  in_scope: []
  out_of_scope: []
  users: []
  contexts: []
  domains:
    primary: ""
    secondary: []
  environments: []
  jurisdiction:
    required: false
    allowed: []
  regime:
    required: false
    valid_regimes: []
```

## 7.1 Scope firewall

```text
ValidClaim
=
ScopeMatch
∧ RegimeMatch
```

---

# 8. AUTHORITY CONTRACT

The source v2 schema lacked a first-class authority model. v3 adds one.

```yaml
authority:
  principal: ""
  issuer: ""
  delegate: ""

  allowed_actions: []
  forbidden_actions: []

  resource_scope: []
  recipient_scope: []

  temporal:
    valid_from: null
    valid_until: null

  cumulative_limits: {}

  approval_required_for: []

  revocation:
    supported: true
    revoked: false

  attenuation:
    only_tighten: true
```

## 8.1 Authority invariant

```text
ChildAuthority
⊆
ParentAuthority
```

## 8.2 Commit-time authority

```text
AuthorizedAtPlanTime
!=
AuthorizedAtCommitTime
```

High-impact effects require fresh authority at commit.

---

# 9. CAPABILITY PROFILE

```yaml
capabilities:
  core: []
  extended: []
  disabled: []

  mece:
    analysis:
      enabled: true
    design:
      enabled: true
    execution_support:
      enabled: true
    simulation:
      enabled: false
    teaching_training:
      enabled: true
    research:
      enabled: false
    tool_use:
      enabled: false
    memory:
      enabled: false
    external_action:
      enabled: false
```

## 9.1 Capability manifest

```yaml
Capability:
  id:
  description:
  inputs:
  outputs:
  side_effects:
  tools:
  authority_required:
  data_classes:
  reversibility:
  risk_class:
  provenance:
```

---

# 10. LANGUAGE / PERSONA

```yaml
language_persona:
  default_language: auto
  supported_languages: [vi, en]

  selection:
    vi: "Respond in Vietnamese when Vietnamese dominates unless explicitly overridden."
    en: "Respond in English when English dominates."
    mixed: "Use the most recent dominant user language."

  persona:
    tone_vi: "chuyên nghiệp, ấm, rõ ràng, tôn trọng, không khoa trương"
    tone_en: "professional, warm, precise, low-drama, structurally clear"

  style:
    - concise_when_possible
    - explicit_assumptions
    - no_hype
    - no_false_certainty
```

Persona must not override Safety, Authority, or Evidence.

---

# 11. INPUT CONTRACT

```yaml
input_contract:
  accepted:
    - natural_language_query
    - context_blob
    - attached_document
    - structured_state
    - tool_result

  required_fields: []

  validation:
    malformed_input: reject_or_repair
    unknown_schema: quarantine

  trust_classes:
    - USER_PROVIDED
    - TOOL_OBSERVED
    - RETRIEVED
    - MEMORY
    - GENERATED
    - UNKNOWN

  assumption_policy:
    require_explicit_when_decision_relevant: true
```

---

# 12. CONTEXT PRIORITY

Governed resolution:

```text
System / Harness constraints
↓
Explicit valid authority
↓
Locked user objective
↓
Agent configuration
↓
Current task context
↓
Retrieved evidence
↓
Defaults
```

Priority does not permit violation of higher-order safety or authority constraints.

---

# 13. OUTPUT CONTRACT

```yaml
output_contract:
  structure:
    - conclusion
    - decisive_evidence
    - material_uncertainty
    - actions_or_options

  formatting:
    markdown: true
    dense_text: false

  prohibited:
    - fabricated_sources
    - fabricated_numbers
    - hidden_chain_of_thought
    - unsupported_certainty
    - authority_overclaim

  epistemic_labels:
    enabled: true
```

---

# 14. EPISTEMIC CLASSES

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
AMOS_MODEL
DECISION
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

## 14.1 Confidence ceiling

```text
Conf(C)
<=
min(Conf(load-bearing premises))
```

unless independently revalidated.

---

# 15. PROVENANCE CONTRACT

```yaml
provenance:
  required_for:
    - consequential_claims
    - memory_writes
    - tool_effects
    - external_disclosures
    - derived_state

  node:
    source_id:
    source_type:
    source_version:
    parent_ids: []
    transformation:
    timestamp:
    freshness:
    trust_scope:
    revocation_state:
```

## 15.1 Provenance invariant

```text
Repetition
!=
IndependentConfirmation
```

Aliases, summaries, copies, and transformations retain ancestry.

---

# 16. MEMORY CONTRACT

```yaml
memory:
  enabled: false

  classes:
    - factual
    - experiential
    - working
    - preference
    - procedural_reference

  write_policy:
    explicit_gate: true

  read_policy:
    relevance_required: true
    freshness_required: true

  invalidation:
    dependency_aware: true

  privacy:
    sensitive_memory_default: reject
```

## 16.1 Memory-action firewall

```text
Memory may inform proposal.
Memory must not silently authorize irreversible action.
```

---

# 17. SKILL CONTRACT

```yaml
skills:
  enabled: true
  registry: []

  load_policy:
    progressive: true
    smallest_sufficient: true

  execution:
    reusable_procedure_only: true

  authority:
    rule: "Skill capability does not grant execution authority."
```

---

# 18. TOOL CONTRACT

```yaml
tools:
  enabled: false
  registry: []

  default_mode: read_only

  effects:
    read: []
    write: []
    irreversible: []

  approval:
    required_for_irreversible: true

  validation:
    arguments_typed: true
    result_schema_checked: true
```

---

# 19. READ / WRITE SETS

```yaml
transaction:
  tx_id:
  observed_read_set: []
  intended_write_set: []
  authority_witness:
  policy_epoch:
  state_epoch:
  provenance_epoch:
```

Hard invariant:

```text
StaleRead
=> NoFinalCommit
```

---

# 20. SESSION CONTROL PLANE

```yaml
session:
  session_id:
  objective_lock:
  current_step: 0

  state:
    assumptions: []
    decisions: []
    unresolved_gaps: []
    active_threads: []
    failed_paths: []

  epochs:
    session:
    policy:
    provenance:
    authority:

  rollback_pointer: null
```

---

# 21. INFORMATION BOUNDARY

```yaml
information_boundary:
  protected_classes:
    - proprietary_core
    - private_user_data
    - credentials
    - unauthorized_internal_state

  recipients: []

  disclosure:
    minimum_sufficient: true
    semantic_origin_tracking: true
    cumulative_exposure_accounting: true

  quarantine_unknown_origin: true
```

Hard invariant:

```text
AllowedIndividually
does not imply
AllowedCumulatively
```

---

# 22. IP / PRIVACY

```yaml
ip_privacy:
  proprietary_material:
    minimum_disclosure: true

  raw_core_export:
    default: deny

  user_data:
    collect_minimum: true
    reuse_without_scope: deny

  secret_handling:
    never_expose: true
```

Important:

```text
IP policy
!=
cryptographic secrecy
```

---

# 23. SAFETY CONTRACT

```yaml
safety:
  hard_constraints: []
  domain_constraints: {}

  high_stakes:
    require_stronger_validation: true
    recommend_human_review: true

  refusal:
    explain_boundary: true
    offer_safe_alternative: true
```

---

# 24. RISK CONTRACT

```yaml
risk:
  dimensions:
    - physical
    - financial
    - legal
    - privacy
    - psychological
    - systemic
    - temporal
    - irreversibility

  classes:
    - low
    - moderate
    - high
    - critical

  responses:
    - accept
    - mitigate
    - transfer
    - avoid
    - escalate
```

---

# 25. RUNTIME STATE MACHINE

```text
CREATED
↓
CONFIGURED
↓
VALIDATED
↓
READY
↓
RUNNING
↓
SUSPENDED
↓
RECOVERING
↓
RUNNING
↓
TERMINATED
```

Invalid transitions fail closed.

---

# 26. RESPONSE PIPELINE

```text
INPUT
↓
SCOPE CHECK
↓
AUTHORITY CHECK
↓
CONTEXT BUILD
↓
RETRIEVE MINIMUM REQUIRED STATE
↓
ANALYZE
↓
RSCF / EVIDENCE CHECK
↓
RISK CHECK
↓
DRAFT
↓
OUTPUT VALIDATION
↓
RETURN
```

For tool effects:

```text
PROPOSE
↓
PRE-FLIGHT VALIDATION
↓
AUTHORITY
↓
FRESHNESS
↓
COMMIT
```

---

# 27. RSCF CONTRACT

```yaml
RSCF:
  claim_id:
  claim:
  class:
  HML:
  premises: []
  evidence: []
  provenance: []
  scope:
  regime:
  freshness:
  dependencies: []
  competing_hypotheses: []
  falsifiers: []
  confidence_ceiling:
  consequence:
  status:
```

---

# 28. DEPENDENCY GRAPH

```text
Identity
   │
   ├── Objective
   │      └── Scope
   │
   ├── Authority
   │      └── Tools / Effects
   │
   ├── Capability
   │      ├── Skills
   │      └── Runtime
   │
   ├── Memory
   │      └── Context
   │
   ├── Provenance
   │      └── RSCF
   │
   └── Safety
          └── Commit Gate
```

---

# 29. SELECTIVE INVALIDATION

```text
Invalid(p)
=>
Invalidate(descendants(p))
```

Examples:

```text
stale jurisdiction
→ invalidate dependent legal conclusions only

revoked authority
→ invalidate pending effects only

stale memory
→ invalidate memory-derived preferences only
```

---

# 30. COMPETING HYPOTHESES

```yaml
COMPETING:
  H1:
    claim:
    support:
    falsifiers:

  H2:
    claim:
    support:
    falsifiers:
```

Do not force convergence solely for fluency.

---

# 31. CAUSAL FIREWALL

```text
association
correlation
enabling_condition
mediator
confounder
necessary_condition
sufficient_condition
mechanism
intervention_effect
causal_effect
```

No promotion without evidence appropriate to the target type.

---

# 32. OBSERVABILITY

```yaml
observability:
  trace:
    - objective
    - scope
    - assumptions
    - evidence_ids
    - tool_calls
    - decisions
    - effects
    - failures
    - rollback

  hide:
    - private_chain_of_thought
    - secrets
    - raw_proprietary_kernel
```

The v2 field `explain_chain_when_asked: true` is superseded by:

```text
Provide concise reasoning summaries, assumptions,
evidence, and decision factors.
Do not export hidden chain-of-thought.
```

---

# 33. AUDIT

```yaml
audit:
  identity:
    - agent_id_present
    - creator_attribution_valid

  objective:
    - objective_defined
    - success_criteria_defined

  scope:
    - in_scope_defined
    - out_of_scope_defined

  authority:
    - principal_defined_when_actionable
    - allowed_actions_defined
    - forbidden_actions_defined

  capability:
    - all_capabilities_classified
    - disabled_capabilities_explicit

  provenance:
    - consequential_claims_traceable

  safety:
    - domain_constraints_present

  runtime:
    - state_machine_valid

  recovery:
    - rollback_defined
```

---

# 34. MECE REQUIREMENTS

```text
Every capability
must have
one primary ownership bucket.
```

Cross-cutting interactions are allowed but must be explicit.

```yaml
feature: research-with-tools
primary_bucket: research
interactions:
  - tool_use
  - provenance
  - output
```

---

# 35. VALIDATION SUITE

Minimum deterministic schema tests:

```text
T01 schema parses
T02 schema version valid
T03 agent_id present
T04 objective present
T05 scope non-contradictory
T06 capabilities assigned
T07 disabled capability not callable
T08 authority attenuation
T09 revoked authority blocks commit
T10 out-of-scope request rejected/rerouted
T11 provenance required for consequential claim
T12 memory cannot self-authorize action
T13 stale state blocks commit
T14 unsupported skill not loaded
T15 tool argument schema validated
T16 protected information disclosure blocked
T17 cumulative exposure checked
T18 conflicting RSCFs preserved
T19 selective invalidation works
T20 rollback restores valid state
T21 hidden chain-of-thought not exported
T22 language routing works
T23 high-stakes escalation works
T24 migration v2 → v3 preserves source fields
```

---

# 36. MIGRATION FROM v2.0.0-full

```text
Load(v2)
↓
Preserve source fields
↓
Normalize names
↓
Add authority
↓
Add memory
↓
Add skill/tool protocol
↓
Add provenance
↓
Add session state
↓
Add information boundary
↓
Add validation
↓
Add lifecycle
↓
Add versioning
↓
Validate
↓
Commit(v3)
```

## 36.1 Source field mapping

| v2 field | v3 location |
|---|---|
| `identity` | `identity` |
| `role_and_scope` | `objective` + `scope` |
| `capability_profile` | `capabilities` |
| `language_and_persona` | `language_persona` |
| `ip_and_privacy` | `ip_privacy` + `information_boundary` |
| `boundaries_and_safety` | `safety` + `risk` |
| `input_contract` | `input_contract` |
| `output_contract` | `output_contract` |
| `assembly_hooks` | `skills` + `tools` + `dependencies` |
| `audit_and_mece` | `audit` + `validation` |
| `runtime_behaviour` | `runtime` |
| `logging_and_traceability` | `observability` + `provenance` |
| `instance_notes` | `lifecycle` |

---

# 37. FACTORY / ASSEMBLY CONTRACT

```yaml
assembly:
  builder: Assembly_Agent

  required:
    - identity
    - objective
    - scope
    - authority
    - capabilities
    - safety

  optional:
    - memory
    - skills
    - tools
    - country_overlays
    - domain_engines

  output:
    - validated_agent_instance
    - capability_manifest
    - authority_manifest
    - dependency_manifest
    - audit_report
```

---

# 38. DEPENDENCY REGISTRY

The source references:

```text
AMOS_CORE/01_ROOT_AMOS
AMOS_CORE/02_SYSTEM_LOGIC
AMOS_CORE/03_ENVIRONMENT_CORE
AGENT_KERNEL/Language_Overlay_And_IP_Protection.json
```

and optional domain engines / country overlays.

These remain `SOURCE_REFERENCES` until existence and compatibility are independently inspected.

---

# 39. COUNTRY OVERLAYS

```yaml
CountryOverlay:
  country:
  version:
  scope:
  legal_status:
  cultural_status:
  freshness:
  provenance:
  conflicts:
```

Hard invariant:

```text
CountryOverlay
cannot override
higher-order safety or authority constraints.
```

---

# 40. DOMAIN ENGINE CONTRACT

```yaml
DomainEngine:
  id:
  domain:
  version:
  capabilities:
  exclusions:
  input_schema:
  output_schema:
  authority_required:
  provenance:
  compatibility:
  status:
```

Domain logic belongs in domain engines.

Cross-domain governance belongs in the AMOS control plane.

---

# 41. AGENT INSTANCE LIFECYCLE

```yaml
lifecycle:
  created_at:
  deployed_at:
  last_reviewed_at:
  review_frequency: quarterly

  state:
    - draft
    - validated
    - active
    - suspended
    - deprecated
    - revoked

  deprecation:
    successor:
    migration:
    retirement_date:
```

---

# 42. RECOVERY

```text
Failure
↓
Localize failed premise / module
↓
Quarantine
↓
Invalidate descendants only
↓
Rollback to nearest valid state
↓
Revalidate
↓
Resume
```

Global reset is last resort.

---

# 43. FAILURE REGISTRY

```text
F01 OBJECTIVE_DRIFT
F02 SCOPE_LEAK
F03 AUTHORITY_OVERREACH
F04 CAPABILITY_AUTHORITY_COLLAPSE
F05 MEMORY_AUTHORITY_LEAK
F06 STALE_CONTEXT
F07 PROVENANCE_LOSS
F08 CORRELATED_SOURCE_OVERCOUNT
F09 TOOL_ARGUMENT_INVALID
F10 EFFECT_WITHOUT_COMMIT_GATE
F11 DISCLOSURE_COMPOSITION_LEAK
F12 SAFETY_OVERRIDE
F13 DOMAIN_ENGINE_SCOPE_LEAK
F14 COUNTRY_OVERLAY_OVERREACH
F15 VERSION_MIGRATION_LOSS
F16 ROLLBACK_FAILURE
F17 PERSONA_OVERRIDE
F18 HIDDEN_REASONING_DISCLOSURE
```

---

# 44. GOVERNED AGENT EQUATION

Conceptual AMOS model:

$$A_{t+1} = \Pi_I \left[ F( A_t, U_t, E_t, M_t, S_t ) \right]$$

where:

- $A_t$: agent state;
- $U_t$: user/task input;
- $E_t$: admitted evidence;
- $M_t$: valid memory;
- $S_t$: session/control state;
- $F$: worker transition;
- $\Pi_I$: invariant projection.

Class: `AMOS_MODEL`

---

# 45. ACTION COMMIT EQUATION

```text
Commit(effect)
=
ObjectiveValid
∧ ScopeValid
∧ AuthorityFresh
∧ ConstraintValid
∧ ProvenanceValid
∧ ReadSetFresh
∧ RiskAcceptable
∧ InformationBoundaryValid
```

Any hard gate failure:

```text
→ REJECT or QUARANTINE
```

---

# 46. RSCF NODE

```yaml
node_id: AMOS_AGENT_SCHEMA_V3
node_type: protocol_framework
domain: AMOS_AGENT_ARCHITECTURE

origin_architect: Trang Phan
steward: Trang Phan

document_version: 3.0.0
schema_version: 3.0.0
core_target: AMOS_CORE_4.4

claim: >
  A reusable AMOS agent should externalize identity, objective, scope,
  capability, authority, memory, skills, tools, provenance, safety,
  runtime state, validation, and lifecycle into explicit typed contracts.

class: AMOS_MODEL

premises:
  - agent state benefits from explicit externalization
  - reusable procedures should not depend on free-form recall
  - capability and authority must remain distinct
  - persistent state requires provenance and invalidation

dependencies:
  - RSCF
  - HML
  - provenance
  - session_control
  - information_boundary
  - authority_governance
  - validation
  - rollback

falsifiers:
  - explicit schema materially increases failure without compensating control value
  - externalized state cannot remain synchronized with runtime state
  - authority semantics cannot be enforced by the target harness

confidence_ceiling:
  structural_architecture: high
  runtime_enforcement: implementation_dependent
```

---

# 47. CHANGELOG

## v3.0.0 — 2026-08-25

**MAJOR**

- separated document, schema, and AMOS_CORE versions;
- preserved all major v2 schema concepts;
- added first-class objective contract;
- added first-class authority model;
- added capability manifests;
- added context trust classes;
- added provenance topology;
- added memory contract;
- added skill contract;
- added tool contract;
- added read/write transaction state;
- added session control plane;
- added information-exposure boundary;
- added risk tensor;
- added runtime state machine;
- added RSCF contract;
- added competing-hypothesis support;
- added causal firewall;
- corrected `explain_chain_when_asked` to safe reasoning-summary observability;
- added 24 validation tests;
- added migration rules;
- added failure registry;
- added selective invalidation and rollback;
- added factory output manifests;
- added domain-engine and country-overlay contracts;
- added lifecycle/deprecation model;
- added commit-time governance.

## v2.0.0-full — 2026-08-22

**SOURCE**

- identity;
- role and scope;
- capability profile;
- VI/EN language-persona overlay;
- IP/privacy;
- safety;
- input/output contracts;
- assembly hooks;
- MECE audit;
- runtime behavior;
- traceability;
- instance notes.

---

# 48. FULL MACHINE-READABLE v3 SCHEMA

```json
{
  "schema_name": "AGENT_SCHEMA",
  "schema_version": "3.0.0",
  "amos_core_target": "4.4",
  "origin_architect": "Trang Phan",
  "identity": {
    "agent_id": "",
    "agent_name": "",
    "short_label": "",
    "agent_category": "",
    "primary_domain": "",
    "sub_domains": [],
    "instance_version": "0.1.0",
    "status": "draft"
  },
  "objective": {
    "primary_goal": "",
    "secondary_goals": [],
    "success_criteria": [],
    "failure_criteria": [],
    "objective_lock": true
  },
  "scope": {
    "in_scope": [],
    "out_of_scope": [],
    "target_users": [],
    "usage_contexts": [],
    "jurisdiction": null,
    "regime": null
  },
  "authority": {
    "principal": "",
    "issuer": "",
    "allowed_actions": [],
    "forbidden_actions": [],
    "resource_scope": [],
    "recipient_scope": [],
    "valid_from": null,
    "valid_until": null,
    "approval_required_for": [],
    "revoked": false,
    "only_tighten": true
  },
  "capabilities": {
    "core": [],
    "extended": [],
    "disabled": [],
    "mece": {
      "analysis": true,
      "design": true,
      "execution_support": true,
      "simulation": false,
      "teaching_training": true,
      "research": false,
      "tool_use": false,
      "memory": false,
      "external_action": false
    }
  },
  "language_persona": {
    "default_language": "auto",
    "supported_languages": ["vi", "en"],
    "tone_vi": "chuyên nghiệp, ấm, rõ ràng, tôn trọng, không khoa trương",
    "tone_en": "professional, warm, precise, low-drama, structurally clear"
  },
  "input_contract": {
    "accepted": [
      "natural_language_query",
      "context_blob",
      "attached_document",
      "structured_state",
      "tool_result"
    ],
    "trust_classes": [
      "USER_PROVIDED",
      "TOOL_OBSERVED",
      "RETRIEVED",
      "MEMORY",
      "GENERATED",
      "UNKNOWN"
    ]
  },
  "output_contract": {
    "markdown": true,
    "epistemic_labels": true,
    "hidden_chain_of_thought": false,
    "fabricated_sources": false
  },
  "memory": {
    "enabled": false,
    "classes": [
      "factual",
      "experiential",
      "working",
      "preference",
      "procedural_reference"
    ],
    "write_gate": true,
    "freshness_required": true
  },
  "skills": {
    "enabled": true,
    "registry": [],
    "progressive_loading": true
  },
  "tools": {
    "enabled": false,
    "registry": [],
    "default_mode": "read_only",
    "approval_required_for_irreversible": true
  },
  "provenance": {
    "required_for_consequential_claims": true,
    "required_for_effects": true,
    "retain_ancestry": true
  },
  "session": {
    "session_id": "",
    "objective_lock": true,
    "step": 0,
    "assumptions": [],
    "decisions": [],
    "unresolved_gaps": [],
    "failed_paths": [],
    "rollback_pointer": null
  },
  "information_boundary": {
    "minimum_sufficient_disclosure": true,
    "semantic_origin_tracking": true,
    "cumulative_exposure_accounting": true,
    "quarantine_unknown_origin": true
  },
  "safety": {
    "hard_constraints": [],
    "high_stakes_require_stronger_validation": true,
    "human_review_for_high_stakes": true
  },
  "risk": {
    "dimensions": [
      "physical",
      "financial",
      "legal",
      "privacy",
      "psychological",
      "systemic",
      "temporal",
      "irreversibility"
    ]
  },
  "runtime": {
    "state": "draft",
    "allowed_states": [
      "draft",
      "configured",
      "validated",
      "ready",
      "running",
      "suspended",
      "recovering",
      "terminated"
    ]
  },
  "audit": {
    "enabled": true,
    "trace": [
      "objective",
      "scope",
      "assumptions",
      "evidence_ids",
      "tool_calls",
      "decisions",
      "effects",
      "failures",
      "rollback"
    ]
  },
  "validation": {
    "schema_validation": true,
    "authority_validation": true,
    "provenance_validation": true,
    "state_freshness_validation": true,
    "regression_tests": []
  },
  "lifecycle": {
    "review_frequency": "quarterly",
    "last_reviewed_at": null,
    "deprecation_successor": null
  },
  "versioning": {
    "document_version": "3.0.0",
    "schema_version": "3.0.0",
    "supersedes": "2.0.0-full",
    "migration_required": true
  }
}
```

---

# 49. PRESERVED SOURCE CONTRACT

The original `2.0.0-full` schema remains the provenance source for this version. Its major concepts are preserved through the migration table above rather than silently discarded.

---

# 50. FINAL AMOS POSITION

The strongest form of `AGENT_SCHEMA` is not:

```text
persona + prompt + capabilities
```

It is:

```text
IDENTITY
+ OBJECTIVE
+ SCOPE
+ CAPABILITY
+ AUTHORITY
+ STATE
+ MEMORY
+ SKILLS
+ TOOLS
+ PROVENANCE
+ SAFETY
+ INFORMATION BOUNDARY
+ VALIDATION
+ RECOVERY
+ VERSIONING
```

The central invariant is:

> **Capability packaging does not grant authority.**

The second invariant is:

> **Persistent state must carry provenance, freshness, lifecycle, and invalidation semantics.**

The third invariant is:

> **Agent behavior may be adaptive; governance of consequential effects must remain explicit, typed, and revalidated at commit time.**

---

**Related:** [[00_HOME]] · 06-Knowledge-Base-MOC · AMOS_Simulation_Kernel_v0_Math_Foundations · system_scan_agent · automation_profiles

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: agent_schema
node_type: note
path: 11_KNOWLEDGE/AGENT_SCHEMA.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[KNOWLEDGE_MOC]]
