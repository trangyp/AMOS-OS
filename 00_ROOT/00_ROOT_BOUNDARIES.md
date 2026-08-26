# 00 Root Boundaries

```yaml
---
title: "AMOS OS Root Boundaries"
artifact: "00_ROOT_BOUNDARIES.md"
artifact_id: "AMOS_ROOT_BOUNDARIES_000"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
domain: "ROOT GOVERNANCE / CONTROL PLANE"
artifact_class: "ROOT_BOUNDARY_SPECIFICATION"
version: "1.0.0"
updated: "2026-08-26"

status: "PROPOSED_SPECIFICATION"
epistemic_class: "MODEL"

canonical_status: "UNKNOWN/GAP"
implementation_status: "UNKNOWN/GAP"
validation_status: "UNKNOWN/GAP"
---
```

# AMOS OS — 00 Root Boundaries

## 0. Purpose

`00_ROOT_BOUNDARIES.md` defines the highest-level structural boundaries governing AMOS OS.

Its purpose is to establish what the AMOS root layer:

* contains;
* does not contain;
* may govern;
* may delegate;
* may observe;
* may modify;
* may authorize;
* may commit;
* may expose;
* may inherit;
* and must never silently cross.

The root boundary exists to prevent architecture, cognition, policy, authority, capability, evidence, memory, execution, and external effects from collapsing into an undifferentiated system.

The central contract is:

```text
DISTINCTION BEFORE COMPOSITION
BOUNDARY BEFORE TRANSFER
AUTHORITY BEFORE EFFECT
VALIDATION BEFORE PROMOTION
REVALIDATION BEFORE COMMIT
```

A boundary is not merely a directory or namespace.

Within this specification, a boundary is a governed distinction between states or domains for which crossing the distinction can alter:

```text
meaning
scope
authority
trust
provenance
risk
information exposure
system state
or external consequence
```

---

# 1. Root Boundary Law

AMOS SHALL preserve the following root distinctions:

```text
SOURCE != CANON

CANON != MODEL

MODEL != EVIDENCE

EVIDENCE != DECISION

DECISION != ACTION

ACTION != COMMIT

PROPOSAL != COMMIT

CAPABILITY != AUTHORITY

AUTHORITY != AUTHORIZATION

AUTHORIZATION != EXECUTION

EXECUTION != VALIDATION

OBSERVATION != CAUSATION

MEMORY != CURRENT_TRUTH

RETRIEVAL != ADMISSION

ADDRESSABLE != VALIDATED

IMPLEMENTED != VERIFIED

LOCAL_SUCCESS != SYSTEM_VALIDITY

UNKNOWN/GAP != PASS
```

These distinctions are non-cosmetic.

They prevent one system state from being silently promoted into another.

---

# 2. Boundary Objective

The root-boundary subsystem exists to preserve:

```text
system identity;

scope integrity;

authority integrity;

information integrity;

provenance integrity;

epistemic integrity;

execution integrity;

transaction integrity;

memory integrity;

control-plane separation;

external-effect governance;

and recoverability.
```

---

# 3. Boundary Model

For an AMOS object `x`, define the MODEL boundary envelope:

```text
B(x) =
<
identity,
domain,
scope,
authority,
provenance,
epistemic_class,
regime,
time,
information_class,
effect_class,
governance_state
>
```

A transfer:

```text
x : B_A → B_B
```

is admissible only when the transition satisfies the applicable boundary predicates.

Conceptually:

```text
AdmissibleTransfer(x,A,B)
=
IdentityPreserved
∧ ScopeCompatible
∧ AuthoritySatisfied
∧ ProvenancePreserved
∧ PolicySatisfied
∧ InformationFlowAllowed
∧ EffectAllowed
∧ GovernanceSatisfied
```

This equation is an **AMOS MODEL**, not an externally validated universal law.

---

# 4. Root Boundary Classes

AMOS root governance SHOULD distinguish at least the following boundary classes:

```text
B01 SYSTEM_BOUNDARY
B02 CANON_BOUNDARY
B03 EPISTEMIC_BOUNDARY
B04 AUTHORITY_BOUNDARY
B05 CAPABILITY_BOUNDARY
B06 POLICY_BOUNDARY
B07 INFORMATION_BOUNDARY
B08 MEMORY_BOUNDARY
B09 PROVENANCE_BOUNDARY
B10 CONTROL_PLANE_BOUNDARY
B11 EXECUTION_BOUNDARY
B12 TRANSACTION_BOUNDARY
B13 COMMIT_BOUNDARY
B14 AGENT_BOUNDARY
B15 SKILL_BOUNDARY
B16 WORKFLOW_BOUNDARY
B17 TOOL_BOUNDARY
B18 EXTERNAL_EFFECT_BOUNDARY
B19 SCALE_BOUNDARY
B20 REGIME_BOUNDARY
B21 TEMPORAL_BOUNDARY
B22 TRUST_BOUNDARY
B23 SECURITY_BOUNDARY
B24 RECOVERY_BOUNDARY
```

These classes may overlap in one operation.

An operation crossing several boundaries must satisfy all load-bearing boundary requirements.

---

# 5. System Boundary

The system boundary distinguishes:

```text
AMOS_INTERNAL
```

from:

```text
AMOS_EXTERNAL
```

External objects may include:

```text
users;

organizations;

APIs;

websites;

repositories;

databases;

cloud services;

devices;

financial systems;

communication systems;

external agents;

external models;

and external data stores.
```

Crossing the system boundary must never be treated as an ordinary internal state transition when external consequences differ.

---

# 6. Internal Does Not Mean Trusted

The following implication is invalid:

```text
INTERNAL
→
TRUSTED
```

Internal objects may still be:

```text
stale;

malformed;

unauthorized;

unvalidated;

poisoned;

superseded;

conflicting;

compromised;

or outside scope.
```

Trust remains typed and local.

---

# 7. External Does Not Mean Untrusted

Likewise:

```text
EXTERNAL
→
UNTRUSTED
```

is not universally valid.

External evidence may be authoritative for a particular claim.

Trust must depend on:

```text
source;

provenance;

scope;

freshness;

independence;

validation;

and applicable regime.
```

---

# 8. Canon Boundary

AMOS SHALL distinguish:

```text
SOURCE MATERIAL
        ↓
CANON CANDIDATE
        ↓
CANON REVIEW
        ↓
CANON ADMISSION
        ↓
CANON
```

Source material does not become canon merely because it is:

```text
uploaded;

stored;

indexed;

retrieved;

quoted;

generated;

or referenced.
```

Therefore:

```text
SOURCE_PRESENT
!=
CANONICAL
```

---

# 9. Canon Modification Boundary

Modification of canonical state requires the applicable:

```text
authority;

provenance;

version lineage;

conflict analysis;

supersession semantics;

dependency analysis;

and commit procedure.
```

An agent cannot modify canon merely because it can write a file.

---

# 10. Epistemic Boundary

AMOS SHALL distinguish epistemic classes.

At minimum:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN/GAP
```

Where required by a subsystem, conclusion status may additionally use:

```text
VERIFIED
CONDITIONAL
COMPETING
```

No class may be silently promoted.

Examples:

```text
SOURCE_CLAIM != VERIFIED

MODEL != OBSERVATION

DERIVED != SOURCE_CLAIM

DECISION != FACT

UNKNOWN/GAP != NEGATIVE_FACT
```

---

# 11. Evidence Boundary

Evidence entering a reasoning process SHOULD retain:

```yaml
evidence_object:
  evidence_id: string
  source_id: string
  source_type: string
  provenance: {}
  observed_at: timestamp | null
  retrieved_at: timestamp | null
  scope: {}
  regime: {}
  freshness: {}
  independence: {}
  epistemic_class: string
  confidence: number | null
```

Evidence without sufficient provenance may remain usable as a hypothesis source but must not silently become high-confidence proof.

---

# 12. Provenance Boundary

Every consequential transformation SHOULD preserve lineage:

```text
SOURCE
  ↓
EXTRACTION
  ↓
NORMALIZATION
  ↓
DERIVATION
  ↓
DECISION
  ↓
ACTION
```

The system should be able to answer:

```text
Where did this originate?

What transformations occurred?

What assumptions were introduced?

What evidence was discarded?

What dependencies remain?

What authority governed the effect?
```

---

# 13. Provenance Loss

If a transformation destroys required provenance:

```text
PROVENANCE_REQUIRED
∧
PROVENANCE_LOST
→
QUARANTINE / REJECT / RECONSTRUCT
```

Fluent reconstruction is not a valid substitute for lost lineage.

---

# 14. Authority Boundary

Authority defines whether a principal may authorize a class of effect.

The authority boundary SHALL preserve:

```text
CAPABILITY != AUTHORITY

ROLE != AUTHORITY

IDENTITY != AUTHORITY

ACCESS != AUTHORITY

POLICY_ALLOW != AUTHORITY

MODEL_PROPOSAL != AUTHORITY
```

Authority must derive from an admissible authority source.

---

# 15. Authorization Boundary

Even valid authority does not imply authorization for every effect.

Authorization binds authority to:

```text
principal;

operation;

resource;

effect;

recipient;

purpose;

environment;

time;

constraints.
```

Therefore:

```text
GENERAL_AUTHORITY
!=
ACTION_SPECIFIC_AUTHORIZATION
```

---

# 16. Capability Boundary

Capabilities describe what a component can potentially do.

Examples:

```text
read file;

write file;

query database;

call API;

send message;

execute code;

create agent;

invoke Skill;

modify repository;

deploy service.
```

Capability is never sufficient authorization.

```text
CAN(x)
!=
MAY(x)
```

---

# 17. Policy Boundary

Policy determines constraints applicable to actions.

Policy may:

```text
ALLOW
DENY
CONSTRAIN
ESCALATE
REQUIRE_REVIEW
REQUIRE_REVALIDATION
```

Policy cannot create authority where authority does not exist.

```text
NO_AUTHORITY
+
POLICY_ALLOW
=
NO_AUTHORITY
```

---

# 18. Control-Plane Boundary

AMOS SHALL distinguish:

```text
WORKER / DOMAIN COGNITION
```

from:

```text
CONTROL PLANE
```

Workers may:

```text
analyze;

predict;

retrieve;

classify;

generate;

recommend;

propose.
```

The control plane owns or governs functions such as:

```text
authority resolution;

policy enforcement;

capability admission;

transaction state;

commit eligibility;

revocation;

provenance requirements;

cross-step validation;

state freshness;

and durable effect finalization.
```

---

# 19. Cognition Does Not Own Commit

A cognitive worker may produce:

```text
PROPOSED_ACTION
```

It MUST NOT convert that proposal directly into:

```text
COMMITTED_EFFECT
```

unless the applicable control-plane gates are satisfied.

---

# 20. Information Boundary

Information flow SHALL be evaluated across:

```text
origin;

classification;

transformation;

recipient;

purpose;

authority;

cumulative exposure;

and destination.
```

A locally permissible disclosure does not guarantee that repeated disclosures remain permissible.

---

# 21. Semantic Origin

Transforming information does not necessarily erase its origin.

Example:

```text
CONFIDENTIAL SOURCE
       ↓
SUMMARY
       ↓
DERIVED TABLE
       ↓
MODEL OUTPUT
```

The downstream objects may remain constrained by source-derived information boundaries.

Therefore:

```text
TRANSFORMATION
!=
DECLASSIFICATION
```

---

# 22. Memory Boundary

AMOS SHALL distinguish:

```text
CURRENT OBSERVATION

WORKING STATE

PERSISTENT MEMORY

RETRIEVED MEMORY

VALIDATED CURRENT STATE
```

A memory object represents a stored claim or state from some prior context.

It is not automatically current.

```text
MEMORY(x)
!=
CURRENT_TRUTH(x)
```

---

# 23. Memory Admission Boundary

Before persistent admission, memory SHOULD be evaluated for:

```text
provenance;

scope;

freshness;

sensitivity;

authority;

contradiction;

future action influence;

retention class;

and revocation requirements.
```

---

# 24. Memory-to-Action Boundary

Persistent memory that materially influences consequential action SHOULD be revalidated where appropriate.

Especially:

```text
old permission;

old identity;

old recipient;

old financial constraint;

old system state;

old security state;

old policy;

old authority.
```

---

# 25. Agent Boundary

Every agent SHALL have a bounded identity and authority envelope.

```yaml
agent_boundary:
  agent_id: string
  parent: string | null
  capabilities: []
  authority: []
  resources: []
  tools: []
  memory_access: []
  disclosure_scope: []
  effect_scope: []
  delegation_scope: []
  lifecycle_state: string
```

Agent creation must not expand authority.

```text
Authority(child)
⊆
DelegableAuthority(parent)
```

unless the child independently obtains another valid authority path.

---

# 26. Agent Isolation

Agent-local state SHOULD remain isolated unless an explicit transfer is permitted.

This includes:

```text
private working state;

credentials;

sensitive memory;

temporary evidence;

uncommitted proposals;

tool outputs;

and transaction-local state.
```

---

# 27. Skill Boundary

A Skill is a bounded capability/workflow package.

Installing or invoking a Skill does not automatically grant:

```text
new authority;

new disclosure rights;

new persistent memory rights;

new commit rights;

or new governance exemptions.
```

Therefore:

```text
SKILL_AVAILABLE
!=
SKILL_AUTHORIZED
```

---

# 28. Skill Composition Boundary

For Skills:

```text
S1 + S2 + S3
```

the composite workflow MUST be evaluated for effects not visible from each Skill independently.

This includes:

```text
information reconstruction;

authority amplification;

cross-domain transfer;

unexpected persistence;

recipient expansion;

and irreversible effects.
```

---

# 29. Workflow Boundary

A workflow is a sequence of governed transitions.

Example:

```text
INPUT
 ↓
RETRIEVE
 ↓
ANALYZE
 ↓
PROPOSE
 ↓
AUTHORIZE
 ↓
EXECUTE
 ↓
VALIDATE
 ↓
COMMIT
```

Each transition may have a distinct boundary contract.

Workflow existence does not imply workflow authorization.

---

# 30. Tool Boundary

A tool is an execution capability.

Tool output SHOULD be classified as:

```text
OBSERVATION
```

when it directly reports environment state, subject to the tool's reliability and provenance.

Tool success means:

```text
EXECUTION_SUCCEEDED
```

not necessarily:

```text
ACTION_WAS_AUTHORIZED
```

or:

```text
OUTCOME_IS_CORRECT
```

---

# 31. Execution Boundary

AMOS SHALL distinguish:

```text
PLAN
PROPOSAL
EXECUTION_ATTEMPT
EXECUTION_RESULT
VALIDATED_RESULT
COMMIT
```

Example:

```text
code generated
!=
code executed

code executed
!=
tests passed

tests passed
!=
production safe

production safe
!=
deployment authorized
```

---

# 32. Transaction Boundary

Consequential multi-step operations SHOULD execute inside a transaction envelope where feasible.

```yaml
transaction_boundary:
  transaction_id: string
  principal: string
  requested_effect: {}
  read_set: []
  write_set: []
  authority_witness: {}
  policy_decision: {}
  constraints: []
  state_version: {}
  status: string
```

---

# 33. Commit Boundary

The commit boundary separates:

```text
PROPOSED / PREPARED STATE
```

from:

```text
DURABLE EFFECT
```

Commit requires the applicable final conditions.

AMOS MODEL:

```text
CommitEligible(T)
=
ExecutionValid(T)
∧ AuthorityFresh(T)
∧ PolicyFresh(T)
∧ ConstraintsSatisfied(T)
∧ StateCompatible(T)
∧ ProvenanceComplete(T)
```

---

# 34. Commit-Time Revalidation

If load-bearing mutable state changed after proposal or authorization:

```text
STATE_CHANGED
→
REVALIDATE_AFFECTED_DEPENDENCIES
```

Do not automatically recompute the entire system when only one dependency changed.

---

# 35. External Effect Boundary

An external effect includes actions such as:

```text
sending;

publishing;

deploying;

transferring;

deleting;

purchasing;

trading;

sharing;

revoking;

granting;

modifying external state.
```

External effects generally require stronger governance than internal reasoning.

---

# 36. Reversibility Boundary

Actions SHOULD be classified by reversibility.

```text
R0 READ_ONLY

R1 LOCALLY_REVERSIBLE

R2 REVERSIBLE_WITH_COST

R3 DIFFICULT_TO_REVERSE

R4 EFFECTIVELY_IRREVERSIBLE
```

As irreversibility increases, validation requirements SHOULD increase.

---

# 37. Risk Boundary

Risk classes may include:

```text
LOW

MODERATE

HIGH

CRITICAL
```

Risk classification must not itself create authority.

It determines governance intensity.

---

# 38. Scale Boundary

AMOS H/M/L decomposition MUST preserve scale distinctions.

```text
H = governing / system level

M = subsystem / relational level

L = local / operational detail
```

A valid observation at `L` does not automatically establish a claim at `H`.

```text
LOCAL_PATTERN
!=
SYSTEM_LAW
```

---

# 39. H/M/L Propagation

Upward propagation requires aggregation or structural justification.

Downward propagation requires applicability.

Conceptually:

```text
L → M → H
```

and:

```text
H → M → L
```

are transformations, not identity mappings.

---

# 40. Regime Boundary

Claims SHOULD carry regime applicability when relevant.

Examples:

```text
NORMAL

STRESSED

EMERGENCY

DEGRADED

RECOVERY

SIMULATION

TEST

PRODUCTION
```

A conclusion valid in one regime must not silently transfer to another.

---

# 41. Simulation Boundary

AMOS SHALL preserve:

```text
SIMULATED_EFFECT
!=
REAL_EFFECT
```

and:

```text
SIMULATION_SUCCESS
!=
DEPLOYMENT_VALIDATION
```

Simulation may provide evidence, but its applicability envelope must remain explicit.

---

# 42. Temporal Boundary

AMOS SHALL distinguish:

```text
event time;

observation time;

retrieval time;

decision time;

authorization time;

execution time;

commit time.
```

These timestamps may differ materially.

---

# 43. Freshness Boundary

A claim or authorization valid at `t0` may become stale at `t1`.

Therefore:

```text
VALID(t0)
```

does not imply:

```text
VALID(t1)
```

without a persistence assumption or revalidation.

---

# 44. Trust Boundary

Trust is local and typed.

AMOS SHALL NOT use a universal scalar:

```text
TRUSTED = TRUE
```

as sufficient evidence for all domains.

Trust SHOULD instead be contextual:

```yaml
trust:
  source: {}
  claim_type: string
  scope: {}
  regime: {}
  freshness: {}
  provenance: {}
  independence: {}
  confidence_ceiling: number
```

---

# 45. Cross-Domain Boundary

Cross-domain mappings are especially sensitive.

Example:

```text
BIOLOGICAL PATTERN
        ↓
COMPUTATIONAL ANALOGY
```

does not establish:

```text
BIOLOGICAL MECHANISM
=
COMPUTATIONAL MECHANISM
```

Cross-domain structural resemblance remains `MODEL` unless independently validated.

---

# 46. Causal Boundary

AMOS SHALL preserve:

```text
association

correlation

sequence

enabling condition

necessary condition

sufficient condition

mediator

confounder

feedback

mechanism

causal effect
```

These are not interchangeable.

```text
CORRELATION
!=
CAUSATION
```

remains a root epistemic boundary.

---

# 47. Observer Boundary

An observation is always produced through some observation process.

Where material, preserve:

```text
observer;

sensor;

measurement method;

sampling process;

representation;

resolution;

uncertainty.
```

The representation is not identical to the represented system.

---

# 48. Representation Boundary

```text
REAL SYSTEM
      ↓
MEASUREMENT
      ↓
REPRESENTATION
      ↓
MODEL
      ↓
PREDICTION
```

Each arrow introduces possible loss or distortion.

Therefore:

```text
MODEL_STATE
!=
REALITY_STATE
```

---

# 49. Security Boundary

Security-sensitive objects SHOULD have explicit handling boundaries.

Examples:

```text
credentials;

private keys;

security findings;

private data;

sensitive infrastructure;

privileged tool interfaces;

revocation material.
```

Access must be governed independently of mere discoverability.

---

# 50. Secret Boundary

Secrets SHOULD NOT propagate into:

```text
logs;

prompts;

memory;

reports;

generated artifacts;

external messages
```

unless specifically required and authorized.

---

# 51. Namespace Boundary

Namespaces prevent semantic collisions.

Example:

```text
AUTHORITY.STATUS
```

must not silently equal:

```text
POLICY.STATUS
```

merely because both use values such as `ACTIVE`.

Typed namespaces are required where ambiguity can alter behavior.

---

# 52. Identity Boundary

Objects with similar labels are not automatically identical.

```text
NAME_EQUALITY
!=
ENTITY_IDENTITY
```

Identity should depend on stable identifiers and provenance where material.

---

# 53. Version Boundary

Versions must remain distinct.

```text
v1
!=
v2
```

unless equivalence has been explicitly established.

A newer version may:

```text
supersede;

extend;

repair;

fork;

or conflict with
```

an older version.

---

# 54. Supersession Boundary

Supersession SHOULD preserve:

```text
predecessor;

successor;

reason;

effective time;

affected dependencies;

migration requirements;

rollback conditions.
```

Old content should not simply disappear from provenance.

---

# 55. Validation Boundary

AMOS SHALL distinguish:

```text
STRUCTURALLY_VALID

SCHEMA_VALID

LOGICALLY_CONSISTENT

TESTED

EMPIRICALLY_SUPPORTED

SECURITY_VALIDATED

PRODUCTION_VALIDATED

CANON_APPROVED
```

Passing one does not imply passing all.

---

# 56. Implementation Boundary

```text
SPECIFIED
!=
IMPLEMENTED

IMPLEMENTED
!=
TESTED

TESTED
!=
VERIFIED

VERIFIED_FOR_SCOPE_A
!=
VERIFIED_FOR_SCOPE_B
```

---

# 57. Addressability Boundary

A component may be addressable in architecture before implementation exists.

Therefore:

```text
ADDRESSABLE
!=
IMPLEMENTED
```

This preserves the ability to model incomplete systems without fabricating functionality.

---

# 58. Placeholder Boundary

A placeholder reserves structure.

It does not prove:

```text
canon;

logic;

implementation;

validation;

authority;

or completeness.
```

Therefore:

```text
PLACEHOLDER
!=
IMPLEMENTED
```

---

# 59. Proposal Boundary

Generated recommendations, patches, policies, architecture changes, canon changes, delegations, and transactions SHOULD initially remain proposals.

```text
PROPOSAL
→
VALIDATE
→
AUTHORIZE
→
COMMIT
```

where applicable.

---

# 60. Generator Boundary

Generators may produce candidate artifacts.

They MUST NOT self-certify those artifacts.

```text
GENERATOR
!=
VALIDATOR
```

unless a formally accepted architecture explicitly combines those roles with independent validation mechanisms.

---

# 61. Validator Boundary

Validation SHOULD be independent enough to detect the failure modes of the producer.

Using identical assumptions may produce false confirmation.

Therefore:

```text
SECOND_CHECK
!=
INDEPENDENT_CHECK
```

---

# 62. Provenance Independence Boundary

Multiple sources may share ancestry.

```text
SOURCE A
   ↓
ARTICLE B
   ↓
SUMMARY C
```

B and C do not independently confirm A.

AMOS SHOULD resolve ancestry before aggregating confidence.

---

# 63. Confidence Boundary

Derived confidence cannot exceed its weakest load-bearing premise unless independently revalidated.

AMOS MODEL:

```text
C(conclusion)
≤
min(
  C(load_bearing_premises)
)
```

subject to the chosen confidence representation.

---

# 64. Unknown Boundary

`UNKNOWN/GAP` represents unresolved state.

It MUST NOT silently become:

```text
TRUE

FALSE

ALLOW

DENY

VALID

INVALID

PASS
```

unless another governing rule explicitly maps unknown state to a safe operational outcome.

---

# 65. Fail-Closed Boundary

For high-consequence operations:

```text
UNKNOWN AUTHORITY
→
NO COMMIT

UNKNOWN RECIPIENT
→
NO DISCLOSURE

UNKNOWN POLICY STATE
→
NO COMMIT

UNKNOWN CRITICAL CONSTRAINT
→
NO COMMIT
```

The underlying epistemic state remains `UNKNOWN/GAP`.

---

# 66. Boundary Crossing Request

A generic boundary crossing MAY be represented:

```yaml
boundary_crossing_request:
  crossing_id: string

  principal: string

  source_boundary: string
  destination_boundary: string

  object: {}

  operation: string
  intended_effect: {}

  purpose: {}

  recipient: {}

  authority_witness: {}

  policy_context: {}

  provenance: {}

  requested_at: timestamp
```

---

# 67. Boundary Decision

```yaml
boundary_decision:
  crossing_id: string

  applicable_boundaries: []

  satisfied_constraints: []

  violated_constraints: []

  unresolved_constraints: []

  provenance_checks: []

  authority_checks: []

  policy_checks: []

  freshness_checks: []

  result:
    - ALLOW
    - ALLOW_WITH_CONSTRAINTS
    - DENY
    - QUARANTINE
    - REVALIDATE
    - ESCALATE
    - UNKNOWN/GAP
```

---

# 68. Boundary Crossing Protocol

```text
REQUEST
   ↓
IDENTIFY OBJECT
   ↓
IDENTIFY SOURCE BOUNDARY
   ↓
IDENTIFY DESTINATION BOUNDARY
   ↓
CLASSIFY EFFECT
   ↓
RESOLVE AUTHORITY
   ↓
RESOLVE POLICY
   ↓
CHECK INFORMATION FLOW
   ↓
CHECK PROVENANCE
   ↓
CHECK SCOPE / REGIME / TIME
   ↓
CHECK CUMULATIVE EFFECT
   ↓
ALLOW / CONSTRAIN / DENY / QUARANTINE
```

---

# 69. Boundary Registry

AMOS SHOULD maintain an addressable boundary registry.

```yaml
boundary_registry:
  registry_id: "AMOS_ROOT_BOUNDARY_REGISTRY"

  boundaries:
    - boundary_id: B01
      type: SYSTEM_BOUNDARY

    - boundary_id: B02
      type: CANON_BOUNDARY

    - boundary_id: B03
      type: EPISTEMIC_BOUNDARY

    - boundary_id: B04
      type: AUTHORITY_BOUNDARY

    - boundary_id: B05
      type: CAPABILITY_BOUNDARY

    - boundary_id: B06
      type: POLICY_BOUNDARY

    - boundary_id: B07
      type: INFORMATION_BOUNDARY

    - boundary_id: B08
      type: MEMORY_BOUNDARY

    - boundary_id: B09
      type: PROVENANCE_BOUNDARY

    - boundary_id: B10
      type: CONTROL_PLANE_BOUNDARY

    - boundary_id: B11
      type: EXECUTION_BOUNDARY

    - boundary_id: B12
      type: TRANSACTION_BOUNDARY

    - boundary_id: B13
      type: COMMIT_BOUNDARY

    - boundary_id: B14
      type: AGENT_BOUNDARY

    - boundary_id: B15
      type: SKILL_BOUNDARY

    - boundary_id: B16
      type: WORKFLOW_BOUNDARY

    - boundary_id: B17
      type: TOOL_BOUNDARY

    - boundary_id: B18
      type: EXTERNAL_EFFECT_BOUNDARY
```

---

# 70. Root Boundary State

```yaml
root_boundary_state:
  system_boundary: ACTIVE_SPECIFICATION
  canon_boundary: ACTIVE_SPECIFICATION
  epistemic_boundary: ACTIVE_SPECIFICATION
  authority_boundary: ACTIVE_SPECIFICATION
  capability_boundary: ACTIVE_SPECIFICATION
  policy_boundary: ACTIVE_SPECIFICATION
  information_boundary: ACTIVE_SPECIFICATION
  memory_boundary: ACTIVE_SPECIFICATION
  provenance_boundary: ACTIVE_SPECIFICATION
  control_plane_boundary: ACTIVE_SPECIFICATION
  execution_boundary: ACTIVE_SPECIFICATION
  transaction_boundary: ACTIVE_SPECIFICATION
  commit_boundary: ACTIVE_SPECIFICATION

  runtime_enforcement: UNKNOWN/GAP
```

`ACTIVE_SPECIFICATION` means defined in this artifact.

It does **not** mean runtime enforcement has been implemented.

---

# 71. H/M/L Applicability

## H — Root / System

At H scale, boundaries govern:

```text
system identity;

canon;

root authority;

control-plane ownership;

external effect classes;

trust domains;

global invariants;

cross-domain composition.
```

## M — Subsystem

At M scale, boundaries govern:

```text
agents;

Skills;

memory systems;

policy systems;

authorization systems;

workflows;

repositories;

domain runtimes;

transaction managers.
```

## L — Local

At L scale, boundaries govern:

```text
individual tool calls;

records;

files;

claims;

messages;

memory entries;

function calls;

transactions;

data fields.
```

---

# 72. Cross-Scale Boundary Law

A boundary decision at one scale does not automatically settle all other scales.

Example:

```text
L: tool call permitted
```

does not prove:

```text
M: workflow permitted
```

or:

```text
H: system objective authorized
```

---

# 73. Control-Plane Requirements

Root-boundary enforcement depends on control-plane capabilities including:

```text
identity resolution;

authority resolution;

policy evaluation;

capability resolution;

provenance tracking;

scope validation;

information-flow validation;

transaction control;

commit-time revalidation;

revocation;

state versioning;

audit;

recovery.
```

---

# 74. Agents

Agents interacting with root boundaries MAY act as:

```text
PROPOSER

ANALYST

VALIDATOR

EXECUTOR

AUDITOR

RECOVERY_AGENT
```

No role name itself grants authority.

---

# 75. Skills

Relevant Skills MAY include:

```text
boundary validation;

authority resolution;

policy evaluation;

provenance auditing;

information exposure control;

transaction validation;

memory admission;

canon consistency checking;

repair auditing;

risk governance.
```

Skill presence remains separate from authorization.

---

# 76. Workflow

Recommended root-boundary workflow:

```text
1. Receive object/action.

2. Determine relevant boundaries.

3. Resolve identity.

4. Resolve source and destination.

5. Determine semantic effect.

6. Resolve authority.

7. Resolve policy.

8. Resolve scope/regime/time.

9. Check provenance.

10. Check information constraints.

11. Check transaction dependencies.

12. Produce boundary decision.

13. Execute only permitted transitions.

14. Revalidate before consequential commit.

15. Record provenance and audit state.
```

---

# 77. Boundary Invariants

## ROOT-BND-INV-001

No boundary crossing may silently alter epistemic class.

## ROOT-BND-INV-002

No boundary crossing may silently enlarge authority.

## ROOT-BND-INV-003

No boundary crossing may silently erase provenance.

## ROOT-BND-INV-004

No boundary crossing may silently widen scope.

## ROOT-BND-INV-005

No boundary crossing may silently change recipient.

## ROOT-BND-INV-006

No boundary crossing may silently change semantic effect.

## ROOT-BND-INV-007

No boundary crossing may silently convert proposal to commit.

## ROOT-BND-INV-008

No boundary crossing may silently convert memory into current fact.

## ROOT-BND-INV-009

No boundary crossing may silently convert model output into observation.

## ROOT-BND-INV-010

No boundary crossing may silently convert capability into authority.

---

# 78. Additional Invariants

## ROOT-BND-INV-011

Transformation does not automatically declassify information.

## ROOT-BND-INV-012

Cross-domain analogy does not establish mechanism.

## ROOT-BND-INV-013

Local validity does not establish global validity.

## ROOT-BND-INV-014

Simulation does not establish deployment validity.

## ROOT-BND-INV-015

Implementation does not establish validation.

## ROOT-BND-INV-016

Retrieval does not establish admission.

## ROOT-BND-INV-017

File presence does not establish canon status.

## ROOT-BND-INV-018

Agent creation does not expand authority.

## ROOT-BND-INV-019

Skill composition does not bypass boundary checks.

## ROOT-BND-INV-020

Workflow composition does not bypass boundary checks.

---

# 79. Transaction Invariants

## ROOT-BND-INV-021

Commit requires current load-bearing authorization.

## ROOT-BND-INV-022

Changed dependencies require selective revalidation.

## ROOT-BND-INV-023

Revoked authority cannot cross the commit boundary.

## ROOT-BND-INV-024

Stale policy cannot authorize a changed effect where policy freshness is load-bearing.

## ROOT-BND-INV-025

A transaction cannot commit an effect outside its authorized envelope.

---

# 80. Provenance Invariants

## ROOT-BND-INV-026

Material source transformations preserve lineage.

## ROOT-BND-INV-027

Correlated evidence must not be counted as independent confirmation without ancestry analysis.

## ROOT-BND-INV-028

Supersession preserves historical provenance.

## ROOT-BND-INV-029

Unknown source ancestry constrains independence claims.

## ROOT-BND-INV-030

Evidence class and decision class remain distinguishable.

---

# 81. Failure Modes

```text
FM-BND-001 boundary collapse

FM-BND-002 authority leakage

FM-BND-003 scope leakage

FM-BND-004 provenance loss

FM-BND-005 epistemic promotion without validation

FM-BND-006 memory treated as current truth

FM-BND-007 model treated as observation

FM-BND-008 proposal treated as commit

FM-BND-009 capability treated as authority

FM-BND-010 policy treated as authority

FM-BND-011 source treated as canon

FM-BND-012 implementation treated as validation

FM-BND-013 local result generalized globally

FM-BND-014 cross-regime leakage

FM-BND-015 cross-scale leakage

FM-BND-016 cross-domain causal overreach

FM-BND-017 semantic-origin laundering

FM-BND-018 recipient laundering

FM-BND-019 purpose laundering

FM-BND-020 tool-success validation fallacy
```

---

# 82. Extended Failure Modes

```text
FM-BND-021 stale authorization crosses commit boundary

FM-BND-022 revoked authority remains cached

FM-BND-023 untrusted memory steers irreversible action

FM-BND-024 Skill composition reconstructs restricted information

FM-BND-025 agent composition expands effective authority

FM-BND-026 workflow bypasses policy

FM-BND-027 generated artifact self-certifies

FM-BND-028 registry rollback resurrects invalid state

FM-BND-029 version confusion

FM-BND-030 identity alias collision

FM-BND-031 simulation result treated as production evidence

FM-BND-032 test environment authority leaks to production

FM-BND-033 confidential transformation treated as declassification

FM-BND-034 unknown state treated as pass

FM-BND-035 evidence descendants counted as independent sources

FM-BND-036 control-plane responsibility delegated to worker accidentally

FM-BND-037 external effect executed before final authorization

FM-BND-038 partial transaction exposes invalid intermediate state

FM-BND-039 recovery restores stale/revoked state

FM-BND-040 boundary metadata itself becomes stale
```

---

# 83. Repair / Recovery

When a boundary violation is detected:

```text
DETECT
  ↓
STOP AFFECTED TRANSFER
  ↓
IDENTIFY VIOLATED BOUNDARY
  ↓
IDENTIFY DEPENDENT STATE
  ↓
QUARANTINE AFFECTED OBJECTS
  ↓
RESTORE LAST VALID STATE
  ↓
RECONSTRUCT PROVENANCE
  ↓
REVALIDATE AUTHORITY / POLICY / SCOPE
  ↓
INVALIDATE DEPENDENT CLAIMS OR TRANSACTIONS
  ↓
RETRY THROUGH VALID BOUNDARY
  ↓
AUDIT
```

---

# 84. Selective Recovery

Recovery SHOULD invalidate only affected dependency descendants.

Example:

```text
Boundary B7 failed
```

does not imply:

```text
invalidate entire AMOS state
```

if dependency closure demonstrates that unrelated state remains valid.

---

# 85. Boundary Quarantine

Objects SHOULD enter quarantine when:

```text
origin is uncertain;

scope is ambiguous;

authority is unresolved;

provenance is broken;

classification is uncertain;

conflicts remain unresolved;

or the object may contaminate downstream state.
```

Quarantine means:

```text
PRESERVED
+
NON-PROMOTED
+
NON-COMMITTED
```

not deletion.

---

# 86. Boundary Validators

Minimum validators SHOULD include:

```text
validate_boundary_identity

validate_source_destination

validate_epistemic_transition

validate_scope_transition

validate_authority_transition

validate_policy_transition

validate_capability_transition

validate_provenance_transition

validate_information_flow

validate_memory_transition

validate_agent_boundary

validate_skill_boundary

validate_workflow_boundary

validate_tool_boundary

validate_transaction_boundary

validate_commit_boundary

validate_external_effect

validate_regime_transition

validate_temporal_freshness

validate_cross_scale_transition
```

---

# 87. Core Tests

```text
T-BND-001 SOURCE_CLAIM cannot silently become VERIFIED

T-BND-002 MODEL cannot silently become OBSERVATION

T-BND-003 CAPABILITY cannot become AUTHORITY

T-BND-004 POLICY_ALLOW cannot create authority

T-BND-005 PROPOSAL cannot become COMMIT without required gates

T-BND-006 MEMORY cannot become current truth without required validation

T-BND-007 PLACEHOLDER cannot become IMPLEMENTED by rename

T-BND-008 IMPLEMENTED cannot become VERIFIED by declaration

T-BND-009 local authorization cannot silently widen scope

T-BND-010 transformation preserves semantic origin
```

---

# 88. Extended Tests

```text
T-BND-011 revoked authority blocks commit

T-BND-012 stale witness triggers revalidation

T-BND-013 recipient change triggers boundary re-evaluation

T-BND-014 purpose change triggers boundary re-evaluation

T-BND-015 resource change triggers boundary re-evaluation

T-BND-016 effect change triggers boundary re-evaluation

T-BND-017 Skill composition cannot bypass disclosure boundary

T-BND-018 child agent cannot exceed parent delegable authority

T-BND-019 cross-regime claim is rejected without applicability evidence

T-BND-020 cross-scale generalization is rejected without support

T-BND-021 correlated sources do not increase independence count

T-BND-022 provenance loss triggers quarantine

T-BND-023 simulation output remains simulation-class evidence

T-BND-024 test authority does not authorize production

T-BND-025 UNKNOWN/GAP never silently passes a hard boundary
```

---

# 89. Adversarial Tests

```text
AT-BND-001 relabel MODEL as VERIFIED

AT-BND-002 relabel tool access as authority

AT-BND-003 use Skill chain to reconstruct protected information

AT-BND-004 spawn child agents to bypass authority ceiling

AT-BND-005 split prohibited action across individually permitted operations

AT-BND-006 replay stale authorization

AT-BND-007 replay stale policy decision

AT-BND-008 replace recipient after authorization

AT-BND-009 replace resource after authorization

AT-BND-010 alter purpose after authorization

AT-BND-011 erase provenance during summarization

AT-BND-012 use multiple descendants of one source as independent evidence

AT-BND-013 inject production action through test workflow

AT-BND-014 restore revoked authority through rollback

AT-BND-015 convert UNKNOWN/GAP into default ALLOW
```

---

# 90. Falsifiers

This root-boundary specification fails its declared purpose if the governed architecture permits any of the following without detection:

```text
capability manufacturing authority;

policy manufacturing authority;

agents manufacturing their own authority;

proposals becoming commits without required gates;

memory being treated as automatically current;

models being represented as observations;

source material becoming canon without admission;

provenance being erased across material transformations;

scope widening without authorization;

semantic effect changing after authorization without revalidation;

revoked authority producing durable effects;

restricted information being reconstructed through allowed fragments;

cross-scale inference being silently generalized;

cross-regime evidence being silently reused;

or UNKNOWN/GAP being treated as PASS.
```

---

# 91. Dependencies

Root boundaries depend conceptually on:

```text
00_ROOT_AUTHORIZATION

AUTHORITY_RESOLVER

AUTHORITY_WITNESS

AUTHORIZATION_SPEC

DELEGATION

REVOCATION

CAPABILITY_CONTRACT

CAPABILITY_MANIFEST

POLICY_ENGINE

POLICY_REGISTRY

POLICY_DECISION

PROVENANCE

INFORMATION_BOUNDARY_CONTROL

MEMORY_GOVERNANCE

TRANSACTION_CONTROL

COMMIT_CONTROL

AUDIT

RECOVERY

CANON_GOVERNANCE
```

The exact repository paths and implementation bindings remain subject to the authoritative AMOS repository structure.

---

# 92. Boundary Interaction Map

```text
                         ┌──────────────────┐
                         │   ROOT CANON     │
                         └────────┬─────────┘
                                  │
                         CANON BOUNDARY
                                  │
                                  ▼
┌──────────┐             ┌──────────────────┐
│ EVIDENCE │────────────▶│ REASONING / MODEL│
└──────────┘ EPISTEMIC   └────────┬─────────┘
             BOUNDARY              │
                                   │ PROPOSAL
                                   ▼
                         ┌──────────────────┐
                         │  CONTROL PLANE   │
                         └───────┬──────────┘
                                 │
                   ┌─────────────┼──────────────┐
                   │             │              │
                   ▼             ▼              ▼
              AUTHORITY       POLICY       CAPABILITY
                   │             │              │
                   └─────────────┼──────────────┘
                                 ▼
                         AUTHORIZATION
                                 │
                                 ▼
                           TRANSACTION
                                 │
                         COMMIT BOUNDARY
                                 │
                                 ▼
                         EXTERNAL EFFECT
```

---

# 93. Boundary Decision Equation

AMOS MODEL:

```text
D_boundary(x)
=
ALLOW
iff
∀ b ∈ RequiredBoundaries(x):
    Satisfied(b,x)
```

For hard boundaries:

```text
∃ b :
Required(b,x)
∧ Failed(b,x)
→
DENY / BLOCK
```

For unresolved hard boundaries:

```text
∃ b :
Required(b,x)
∧ Unknown(b,x)
→
NO_COMMIT
```

---

# 94. Boundary Composition Equation

For a composite operation:

```text
X = {x1, x2, ..., xn}
```

AMOS MUST evaluate not only:

```text
Valid(x1)
∧
Valid(x2)
...
∧
Valid(xn)
```

but also:

```text
ValidComposition(X)
```

because:

```text
∀i Valid(xi)
```

does not necessarily imply:

```text
ValidComposition(X)
```

This is essential for:

```text
distributed disclosure;

authority composition;

multi-agent behavior;

Skill composition;

workflow composition;

and cumulative external effects.
```

---

# 95. Boundary Sensitivity

For consequential decisions, identify the smallest boundary condition capable of flipping the decision.

Examples:

```text
recipient identity;

authority freshness;

resource identity;

classification;

purpose;

regime;

state version;

revocation status.
```

Check these before spending effort on non-decisive background information.

---

# 96. Boundary Audit Record

```yaml
boundary_audit:
  audit_id: string
  transaction_id: string | null

  principal: string

  boundaries_evaluated: []

  decisions: []

  violations: []

  unresolved: []

  authority_witness: {}

  policy_decision: {}

  provenance: {}

  state_versions: []

  final_result:
    - PASS
    - CONDITIONAL
    - FAIL
    - UNKNOWN/GAP

  timestamp: timestamp
```

---

# 97. RSCF

```yaml
rscf:
  claim:
    id: "AMOS_ROOT_BOUNDARY_SPEC"
    class: MODEL

    text: >
      AMOS OS requires explicit governed boundaries between source,
      canon, evidence, model, memory, authority, capability, policy,
      cognition, execution, transaction and durable effect so that
      state cannot silently gain epistemic status, authority, scope,
      trust, persistence or consequence through composition or
      representation change.

  premises:
    - distinct_governance_states_exist
    - boundary_crossings_can_change_risk
    - capability_is_not_authority
    - proposals_are_not_commits
    - provenance_is_required_for_governed_reuse
    - mutable_state_can_invalidate_prior_decisions
    - composite_effects_can_exceed_local_effects

  evidence: []

  provenance:
    origin_architect: "Trang Phan"
    artifact: "00_ROOT_BOUNDARIES.md"

  scope:
    system: "AMOS OS"
    layer: "Root Governance"

  regime:
    - ARCHITECTURE
    - GOVERNANCE_MODEL

  dependencies:
    - ROOT_AUTHORIZATION
    - AUTHORITY_RESOLVER
    - AUTHORIZATION_SPEC
    - POLICY_ENGINE
    - CAPABILITY_CONTRACT
    - PROVENANCE
    - TRANSACTION_CONTROL
    - COMMIT_CONTROL

  competing:
    - implicit_trust_boundary
    - capability_equals_authority
    - static_authorization
    - monolithic_worker_control
    - unrestricted_composition

  falsifiers:
    - unauthorized_boundary_crossing
    - silent_scope_expansion
    - silent_epistemic_promotion
    - provenance_erasure
    - stale_authorization_commit
    - unknown_state_passes_hard_boundary

  confidence_ceiling: 0
```

---

# 98. Gap Matrix

```yaml
gap_matrix:

  ROOT_BOUNDARY_SPECIFICATION:
    state: COMPLETE_FOR_DECLARED_SCOPE

  SOURCE_CANON_ALIGNMENT:
    state: UNKNOWN/GAP
    severity: DECISION_RELEVANT

  CANON_ADMISSION:
    state: UNKNOWN/GAP
    severity: DECISION_RELEVANT

  BOUNDARY_REGISTRY_IMPLEMENTATION:
    state: UNKNOWN/GAP
    severity: CRITICAL_FOR_RUNTIME

  AUTHORITY_BOUNDARY_ENFORCEMENT:
    state: UNKNOWN/GAP
    severity: CRITICAL_FOR_RUNTIME

  INFORMATION_BOUNDARY_ENFORCEMENT:
    state: UNKNOWN/GAP
    severity: CRITICAL_FOR_RUNTIME

  MEMORY_BOUNDARY_ENFORCEMENT:
    state: UNKNOWN/GAP

  TRANSACTION_BOUNDARY_ENFORCEMENT:
    state: UNKNOWN/GAP
    severity: CRITICAL_FOR_RUNTIME

  COMMIT_BOUNDARY_ENFORCEMENT:
    state: UNKNOWN/GAP
    severity: CRITICAL_FOR_RUNTIME

  CROSS_SKILL_COMPOSITION_VALIDATION:
    state: UNKNOWN/GAP

  CROSS_AGENT_COMPOSITION_VALIDATION:
    state: UNKNOWN/GAP

  EXECUTED_TESTS:
    state: UNKNOWN/GAP

  ADVERSARIAL_TESTS:
    state: UNKNOWN/GAP

  PRODUCTION_VALIDATION:
    state: UNKNOWN/GAP
```

---

# 99. Promotion Requirements

Before runtime promotion, AMOS SHOULD establish executable implementations for:

```text
boundary registry;

boundary classification;

authority resolution;

policy evaluation;

capability validation;

provenance validation;

information-flow enforcement;

memory admission;

transaction management;

commit-time revalidation;

revocation propagation;

cross-agent composition;

cross-Skill composition;

audit;

rollback;

and recovery.
```

Then validate through:

```text
schema tests;

unit tests;

integration tests;

adversarial tests;

race-condition tests;

revocation tests;

rollback tests;

cross-boundary leakage tests;

and governance review.
```

---

# 100. Promotion State

```text
SPECIFIED
    ↓
SOURCE_ALIGNED
    ↓
CANON_REVIEWED
    ↓
IMPLEMENTED
    ↓
UNIT_TESTED
    ↓
INTEGRATION_TESTED
    ↓
ADVERSARIALLY_TESTED
    ↓
GOVERNANCE_APPROVED
    ↓
RUNTIME_ACTIVE
```

No transition is automatic.

---

# 101. Current Status

```yaml
current_status:
  artifact: "00_ROOT_BOUNDARIES.md"

  specification:
    state: PROPOSED_SPECIFICATION

  implementation:
    state: UNKNOWN/GAP

  empirical_validation:
    state: UNKNOWN/GAP

  runtime_enforcement:
    state: UNKNOWN/GAP

  canon_status:
    state: UNKNOWN/GAP

  authority_to_promote:
    state: UNKNOWN/GAP
```

---

# 102. Final Root Boundary Contract

AMOS SHALL preserve explicit distinctions wherever collapsing two states could change:

```text
truth status;

authority;

scope;

trust;

information exposure;

provenance;

persistence;

system state;

or consequence.
```

The root boundary chain is:

```text
SOURCE
  ↓
ADMISSION
  ↓
EVIDENCE / CANON / MEMORY
  ↓
REASONING
  ↓
PROPOSAL
  ↓
AUTHORITY + POLICY + CAPABILITY
  ↓
AUTHORIZATION
  ↓
TRANSACTION
  ↓
EXECUTION
  ↓
VALIDATION
  ↓
COMMIT
  ↓
DURABLE / EXTERNAL EFFECT
```

At every material transition:

```text
IDENTITY MUST REMAIN EXPLICIT

SCOPE MUST REMAIN EXPLICIT

PROVENANCE MUST REMAIN RECOVERABLE

AUTHORITY MUST NOT EXPAND SILENTLY

EPISTEMIC STATUS MUST NOT INFLATE SILENTLY

INFORMATION ORIGIN MUST NOT DISAPPEAR SILENTLY

MUTABLE DEPENDENCIES MUST REMAIN REVALIDATABLE

UNKNOWN/GAP MUST REMAIN VISIBLE
```

The governing root law is:

> **Nothing crosses an AMOS root boundary merely because it can. A crossing is valid only when the object's identity, provenance, scope, authority, policy, information constraints, regime, temporal validity, and intended effect remain compatible with the destination boundary. Composition must never be allowed to manufacture authority, certainty, disclosure rights, or irreversible consequence that the constituent parts did not validly possess.**

---

# END — `00_ROOT_BOUNDARIES.md`

```
```
