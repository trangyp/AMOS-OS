# AMOS OS — 00 Root Dependencies

```yaml
---
title: "AMOS OS Root Dependencies"
artifact: "00_ROOT_DEPENDENCIES.md"
artifact_id: "AMOS_ROOT_DEPENDENCIES_000"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
domain: "ROOT GOVERNANCE / DEPENDENCY ARCHITECTURE"
artifact_class: "ROOT_DEPENDENCY_SPECIFICATION"
version: "1.0.0"
updated: "2026-08-26"

status: "PROPOSED_SPECIFICATION"
epistemic_class: "MODEL"

canonical_status: "UNKNOWN/GAP"
implementation_status: "UNKNOWN/GAP"
validation_status: "UNKNOWN/GAP"
---
```

## 0. Purpose

`00_ROOT_DEPENDENCIES.md` defines the governed dependency model for the AMOS OS root layer.

Its purpose is to specify how root artifacts, control planes, capabilities, policies, authority structures, state, provenance, workflows, Skills, agents, validators, and runtime effects may depend upon one another without allowing hidden assumptions or unresolved prerequisites to masquerade as a complete system.

The central dependency law is:

```text
A DECLARED OBJECT
does not imply
ITS DEPENDENCIES EXIST.

A DEPENDENCY THAT EXISTS
does not imply
IT IS COMPATIBLE.

A COMPATIBLE DEPENDENCY
does not imply
IT IS VALIDATED.

A VALIDATED DEPENDENCY
does not imply
IT IS AUTHORIZED FOR THIS USE.
```

Therefore:

```text
DEPENDENCY_NAME
!=
DEPENDENCY_RESOLUTION
!=
DEPENDENCY_VALIDATION
!=
DEPENDENCY_AUTHORITY
```

---

# 1. Root Dependency Objective

The root dependency layer answers:

```text
What does this object require?

Why does it require it?

Is the dependency mandatory or optional?

What type of dependency is it?

Where is the dependency resolved?

Which version/state is required?

Which scope and regime apply?

Is the dependency fresh?

Is its provenance recoverable?

Is it independently validated?

What happens if it disappears?

Which downstream claims become invalid?

Can operation continue in degraded mode?

Can the dependency be substituted?

Who may authorize the substitution?

What must be revalidated after substitution?
```

Dependency resolution is therefore a governed state transition, not simple reference lookup.

---

# 2. Root Dependency Boundary

This specification applies to dependencies among root-level AMOS objects and their downstream execution surfaces.

The dependency universe MAY include:

```text
ROOT CONTRACT
ROOT BOUNDARIES
ROOT AUTHORIZATION
ROOT COVERAGE
ROOT CHANGE LOG

SYSTEM MAP
CONTROL PLANE MAP

CAPABILITY CONTRACT
CAPABILITY MANIFEST

AUTHORIZATION SPEC
AUTHORITY RESOLVER
AUTHORITY WITNESS
DELEGATION
REVOCATION

POLICY ENGINE
POLICY REGISTRY
POLICY DECISION

PROVENANCE
RSCF
MEMORY
STATE

TRANSACTION CONTROL
COMMIT CONTROL
FINALIZATION

AGENTS
SKILLS
WORKFLOWS
PROTOCOLS

TESTS
VALIDATORS
AUDIT

REPAIR
RECOVERY
ROLLBACK

CANON GOVERNANCE
CHANGE GOVERNANCE
```

The exact authoritative root inventory remains subject to repository/canon reconciliation.

---

# 3. Dependency Primitive

The smallest dependency object SHOULD be represented as:

```yaml
dependency:
  dependency_id: string

  consumer_id: string
  provider_id: string

  dependency_type: string

  requirement:
    required: boolean
    criticality: string

  interface:
    expected_type: string | null
    expected_schema: string | null
    expected_version: string | null

  scope: {}
  regime: {}

  provenance: []

  freshness:
    observed_at: null
    valid_until: null

  authority_requirement: null

  resolution_state: "UNKNOWN/GAP"
  validation_state: "UNKNOWN/GAP"

  fallback: null
  failure_effect: null
```

---

# 4. Dependency Classes

AMOS SHOULD distinguish dependency classes rather than treating all edges identically.

```text
STRUCTURAL
SEMANTIC
DATA
STATE
CONTROL
POLICY
AUTHORITY
PROVENANCE
TEMPORAL
RUNTIME
IMPLEMENTATION
VALIDATION
RESOURCE
SECURITY
TRANSACTIONAL
CAUSAL
WORKFLOW
PROTOCOL
CANON
```

---

# 5. Structural Dependency

A structural dependency means:

```text
Object A requires architectural object B
to exist within the declared system structure.
```

Example:

```text
POLICY_ENGINE
→
POLICY_REGISTRY
```

This relationship alone does not prove implementation.

---

# 6. Semantic Dependency

A semantic dependency exists when interpretation of one artifact requires another artifact's definitions or contract.

Example:

```text
POLICY_DECISION
→
POLICY_ENGINE semantics
```

If the upstream meaning changes, downstream interpretation MAY become stale even when no code changes.

---

# 7. Data Dependency

A data dependency exists where one component consumes information produced or maintained elsewhere.

```text
Consumer
← data ←
Provider
```

Data dependencies SHOULD declare:

```text
schema;

type;

units where applicable;

scope;

freshness;

provenance;

validation;

privacy/access requirements.
```

---

# 8. State Dependency

State dependencies exist when behavior depends upon mutable state.

Examples include:

```text
authority state;

revocation state;

policy state;

transaction state;

memory state;

workflow state;

runtime configuration.
```

Mutable dependency state MUST NOT be treated as permanently valid.

---

# 9. Control Dependency

A control dependency exists when one component cannot validly proceed without a governing control.

Example:

```text
EFFECTFUL ACTION
→
AUTHORIZATION
→
POLICY
→
COMMIT GATE
```

Control dependencies are usually promotion-critical.

---

# 10. Authority Dependency

Any operation requiring permission has an authority dependency.

```text
Capability
+
Authority
→
Eligible Action Proposal
```

but:

```text
Capability
without
Authority
→
NOT AUTHORIZED
```

Authority dependency MUST remain distinct from capability dependency.

---

# 11. Policy Dependency

Policy-controlled operations depend upon:

```text
applicable policy;

policy version;

policy precedence;

policy decision;

enforcement point.
```

A missing applicable policy cannot silently become:

```text
ALLOW
```

unless a governing policy explicitly defines that default.

---

# 12. Provenance Dependency

Claims, decisions, memories, policies, evidence objects, and derived state MAY depend upon provenance.

The dependency is not merely:

```text
claim → source
```

but potentially:

```text
claim
→ evidence
→ transformation
→ source
→ source ancestry
```

AMOS MUST preserve enough ancestry to detect correlated evidence.

---

# 13. Validation Dependency

A promotion claim may depend on validators.

Example:

```text
IMPLEMENTED
→ executed tests
→ required validators
→ validation scope
→ VALIDATED
```

Removing or invalidating a validator MAY invalidate the dependent validation claim.

---

# 14. Transaction Dependency

Durable effects MAY depend upon:

```text
proposal;

read state;

authority witness;

policy decision;

constraint validation;

commit gate;

finalization.
```

These dependencies MUST remain visible through commit.

---

# 15. Temporal Dependency

Some dependencies are valid only during a bounded time interval.

```yaml
temporal_dependency:
  valid_from: null
  valid_until: null
  freshness_requirement: null
  revalidation_trigger: []
```

Expired evidence does not necessarily become false.

It becomes:

```text
STALE / REVALIDATION_REQUIRED
```

where freshness is load-bearing.

---

# 16. Regime Dependency

A dependency MAY be valid only under a particular regime.

Examples:

```text
development;

testing;

production;

offline;

online;

single-agent;

multi-agent;

single-user;

multi-user;

normal operation;

degraded operation;

recovery.
```

Therefore:

```text
DependencyValid(regime_A)
!=>
DependencyValid(regime_B)
```

---

# 17. H/M/L Dependency Structure

Root dependencies SHOULD be traceable across:

```text
H — governing architecture
M — subsystem/control mechanism
L — executable/evidence implementation
```

Example:

```text
H:
Root authorization is required.

M:
Authority resolver and revocation mechanism provide authorization control.

L:
Executable authority evaluation and commit-time validation implement the mechanism.
```

A dependency resolved at H does not automatically establish its L implementation.

---

# 18. Dependency Direction

Dependencies MUST have explicit direction.

```text
A → B
```

means:

```text
A depends upon B.
```

It does not mean:

```text
B depends upon A.
```

Bidirectional dependence MUST be represented explicitly:

```text
A → B
B → A
```

and reviewed for circularity.

---

# 19. Dependency Graph

Let:

```text
G_D = (V, E)
```

where:

```text
V = governed AMOS objects

E = typed dependency edges
```

An edge:

```text
e = (consumer, provider, type, conditions)
```

represents a declared dependency.

This is an AMOS MODEL representation, not a claim of empirical mathematics.

---

# 20. Dependency Closure

For object `X`, define conceptual dependency closure:

```text
D*(X)
```

as all load-bearing dependencies reachable from `X`.

A claim about `X` is dependency-closed only if every load-bearing dependency needed for that claim is sufficiently resolved.

```text
DependencyClosed(X, claim)
=
TRUE
```

only when:

```text
∀ d ∈ RequiredDependencies(X, claim):
    SufficientlyResolved(d)
```

---

# 21. Claim-Specific Closure

Dependency closure is claim-specific.

For example:

```text
"artifact exists"
```

may require only structural dependencies.

But:

```text
"artifact is runtime-authorized"
```

may require:

```text
implementation
+
policy
+
authority
+
fresh state
+
validation
+
commit controls.
```

Therefore:

```text
Closure(X)
```

without a declared claim is underspecified.

---

# 22. Required vs Optional Dependencies

Every dependency SHOULD be classified:

```text
REQUIRED

OPTIONAL

CONDITIONAL

ALTERNATIVE

ADVISORY
```

`OPTIONAL` MUST NOT be used merely because a dependency is inconvenient to resolve.

---

# 23. Critical Dependency

A dependency is critical when its absence invalidates a load-bearing system property.

Examples MAY include:

```text
authorization for irreversible actions;

policy enforcement;

transaction finalization;

provenance for evidence-sensitive promotion;

rollback for high-risk mutation.
```

Criticality is scoped to the claim and operating regime.

---

# 24. Dependency Criticality Levels

```text
CRITICAL

HIGH

MEDIUM

LOW

INFORMATIONAL
```

Recommended interpretation:

```text
CRITICAL:
failure blocks operation/promotion.

HIGH:
failure materially degrades integrity.

MEDIUM:
failure degrades capability or confidence.

LOW:
failure has bounded local effect.

INFORMATIONAL:
non-operational descriptive relationship.
```

---

# 25. Dependency Resolution States

```text
UNKNOWN/GAP

DECLARED

DISCOVERED

RESOLVED

TYPE_COMPATIBLE

VALIDATED

AUTHORIZED

ACTIVE

DEGRADED

STALE

CONFLICTED

QUARANTINED

FAILED

SUPERSEDED
```

These states MUST remain distinct.

---

# 26. Resolution Law

```text
DECLARED
!=
RESOLVED

RESOLVED
!=
VALIDATED

VALIDATED
!=
AUTHORIZED

AUTHORIZED
!=
ACTIVE
```

---

# 27. Type Compatibility

A resolved provider MUST satisfy the expected dependency contract.

Conceptually:

```text
ProviderOutputType
⊆
ConsumerAcceptedInputType
```

where applicable.

Type compatibility MAY include:

```text
schema;

unit;

domain;

scale;

scope;

version;

authority class;

provenance requirements.
```

---

# 28. Version Compatibility

Dependencies SHOULD carry version constraints.

Example:

```yaml
version_requirement:
  minimum: null
  maximum: null
  exact: null
  compatible_family: null
```

A new version MUST NOT automatically be assumed compatible.

---

# 29. Supersession

When provider `B1` is superseded by `B2`:

```text
B1 → SUPERSEDED
B2 → CURRENT_CANDIDATE
```

dependents MUST be evaluated for compatibility.

```text
Superseded(provider)
→
Revalidate(dependents)
```

when the supersession affects load-bearing semantics.

---

# 30. Dependency Freshness

Dependencies based on mutable information SHOULD carry freshness.

```yaml
freshness:
  source_timestamp: null
  observed_at: null
  valid_until: null
  maximum_age: null
  freshness_state: "UNKNOWN/GAP"
```

A stale dependency SHOULD not silently remain active when freshness is a precondition.

---

# 31. Dependency Provenance

Every consequential dependency SHOULD preserve:

```text
provider identity;

source identity;

version;

transformation history;

validation evidence;

authority source where applicable;

supersession lineage.
```

---

# 32. Provenance Independence

Two dependencies are not independent merely because they have different filenames or IDs.

If:

```text
B1 ← source S
B2 ← source S
```

then:

```text
B1 + B2
```

must not automatically count as two independent confirmations.

---

# 33. Root Dependency Hierarchy

A proposed root dependency hierarchy is:

```text
ROOT CONTRACT
│
├── ROOT BOUNDARIES
│
├── ROOT AUTHORIZATION
│   ├── AUTHORIZATION SPEC
│   ├── AUTHORITY RESOLVER
│   ├── AUTHORITY WITNESS
│   ├── DELEGATION
│   └── REVOCATION
│
├── POLICY CONTROL
│   ├── POLICY REGISTRY
│   ├── POLICY ENGINE
│   └── POLICY DECISION
│
├── CAPABILITY CONTROL
│   ├── CAPABILITY CONTRACT
│   └── CAPABILITY MANIFEST
│
├── SYSTEM MAP
├── CONTROL PLANE MAP
├── ROOT COVERAGE
├── PROVENANCE
├── STATE
├── RSCF
├── TRANSACTION / COMMIT
├── AUDIT
└── REPAIR / RECOVERY
```

This is a proposed architecture map and MUST NOT be represented as recovered final canon without source confirmation.

---

# 34. Authorization Dependency Chain

A proposed effectful-action dependency chain is:

```text
REQUEST
   ↓
IDENTITY
   ↓
CAPABILITY RESOLUTION
   ↓
AUTHORITY RESOLUTION
   ↓
POLICY EVALUATION
   ↓
CONSTRAINT VALIDATION
   ↓
PROPOSAL
   ↓
COMMIT-TIME REVALIDATION
   ↓
COMMIT
   ↓
AUDIT / PROVENANCE
```

Each arrow represents a potential load-bearing dependency.

---

# 35. Capability Dependencies

Capability resolution MAY depend upon:

```text
CAPABILITY_CONTRACT

CAPABILITY_MANIFEST

agent identity

Skill identity

tool availability

runtime environment

policy

authority
```

But:

```text
CapabilityAvailable
```

does not imply:

```text
CapabilityPermitted
```

---

# 36. Policy Dependencies

`POLICY_ENGINE` SHOULD conceptually depend upon:

```text
POLICY_REGISTRY

policy identity

policy version

applicability context

subject identity

resource identity

requested action

authority context

environment/regime

fresh state
```

The exact executable implementation remains `UNKNOWN/GAP`.

---

# 37. Policy Decision Dependencies

A `POLICY_DECISION` SHOULD bind at least:

```text
policy version;

request;

subject;

resource;

action;

context;

decision;

reason/evidence;

timestamp;

provenance.
```

If any load-bearing binding changes before commit, re-evaluation MAY be required.

---

# 38. Authority Resolver Dependencies

`AUTHORITY_RESOLVER` MAY depend upon:

```text
principal identity;

authority grants;

delegation chain;

scope constraints;

resource constraints;

temporal constraints;

revocation state;

policy;

provenance.
```

A missing revocation dependency is potentially critical.

---

# 39. Authority Witness Dependencies

An `AUTHORITY_WITNESS` SHOULD be bound to:

```text
principal;

authority source;

delegation ancestry;

allowed action;

resource;

scope;

constraints;

validity interval;

revocation state;

generation time;

provenance.
```

A witness detached from these bindings MUST NOT be treated as universal permission.

---

# 40. Delegation Dependencies

Delegation SHOULD depend upon:

```text
delegator authority;

delegation permission;

delegate identity;

scope;

allowed capabilities/actions;

constraints;

validity period;

revocation mechanism;

provenance.
```

The delegated authority MUST NOT exceed what the delegator is permitted to delegate.

Conceptually:

```text
Authority(delegate)
⊆
DelegableAuthority(delegator)
```

---

# 41. Revocation Dependencies

Revocation MAY depend upon:

```text
revocation authority;

target authority object;

effective time;

scope;

propagation rules;

dependent witnesses;

dependent transactions;

audit/provenance.
```

Revocation SHOULD invalidate dependent authority state according to governing semantics.

---

# 42. Commit Dependency

A commit SHOULD NOT depend solely on a previously valid proposal.

```text
ProposalValid(t0)
```

does not imply:

```text
CommitValid(t1)
```

if load-bearing dependencies changed between `t0` and `t1`.

---

# 43. Commit-Time Dependency Revalidation

Before durable effects, AMOS SHOULD revalidate mutable load-bearing dependencies such as:

```text
authority;

revocation;

policy;

resource state;

critical constraints;

transaction preconditions.
```

Conceptually:

```text
CommitEligible(t)
=
ProposalValid
∧
AuthorityFresh(t)
∧
PolicyFresh(t)
∧
ConstraintsSatisfied(t)
∧
RequiredDependenciesValid(t)
```

This is a proposed MODEL contract.

---

# 44. Mutable Dependency Rule

Any dependency capable of changing after read time MUST be treated as mutable unless guaranteed otherwise.

Examples:

```text
authority;

policy;

resource ownership;

revocation;

workflow state;

transaction state;

environment configuration.
```

---

# 45. Dependency Observation

A dependency read SHOULD conceptually carry:

```yaml
dependency_observation:
  dependency_id: string
  version: string | null
  state_hash: string | null
  observed_at: timestamp
  observer: string
  scope: {}
  provenance: []
```

This enables later freshness checks.

---

# 46. Dependency Epoch

Where the architecture uses epochs, dependency validity MAY be tied to an epoch.

```text
ObservationEpoch
!=
CommitEpoch
```

may require revalidation when the dependency is mutable.

Exact runtime epoch semantics require implementation evidence.

---

# 47. Circular Dependency

A cycle exists when:

```text
A → B → C → A
```

Cycles are not automatically invalid.

They MUST be classified.

Possible categories:

```text
BENIGN_REFERENCE_CYCLE

BOOTSTRAP_CYCLE

STATE_FEEDBACK_CYCLE

CONTROL_CYCLE

INVALID_DEFINITIONAL_CYCLE
```

---

# 48. Invalid Circularity

Example:

```text
A is valid because B is valid.
B is valid because A is valid.
```

with no independent grounding is:

```text
CIRCULAR_VALIDATION
```

and MUST NOT produce `VALIDATED`.

---

# 49. Bootstrap Dependencies

Some root systems may require bootstrap relationships.

Bootstrap MUST define:

```text
initial trusted state;

bootstrap authority;

bootstrap policy;

initial provenance;

termination condition;

transition to normal governance.
```

Undefined bootstrap authority is a root-level gap.

---

# 50. Dependency Conflict

A dependency conflict occurs when:

```text
consumer requires version X

but

provider exposes incompatible version Y
```

or:

```text
policy requires action A

while

authority constraint prohibits A.
```

Conflict MUST become visible.

Recommended state:

```text
CONFLICTED
```

not arbitrary precedence unless precedence is governed.

---

# 51. Dependency Ambiguity

If multiple providers satisfy the same dependency:

```text
A → {B1, B2, B3}
```

AMOS MUST determine whether they are:

```text
alternatives;

replicas;

fallbacks;

competing implementations;

different regimes;

or ambiguous duplicates.
```

Do not choose silently.

---

# 52. Alternative Dependencies

A dependency MAY allow alternatives:

```yaml
alternative_dependency:
  requirement_id: string
  acceptable_providers:
    - B1
    - B2
  selection_policy: string
  fallback_policy: string
```

Alternative providers SHOULD satisfy equivalent required contracts, not merely similar names.

---

# 53. Fallback Dependencies

Fallback behavior MUST be explicit.

```text
Primary fails
→
Fallback
```

is valid only if:

```text
fallback is allowed;

fallback satisfies required type;

fallback satisfies authority;

fallback satisfies policy;

fallback is validated for the regime.
```

---

# 54. Degraded Dependency Mode

Some noncritical dependency failures MAY permit degraded operation.

Example:

```yaml
degraded_mode:
  dependency: optional_observability_extension
  failure_effect: reduced_diagnostics
  allowed: true
  blocked_operations: []
```

Critical dependency failure SHOULD normally fail closed.

---

# 55. Fail-Closed Rule

For authority, policy, or safety-critical dependency uncertainty:

```text
UNKNOWN/GAP
```

MUST NOT automatically become:

```text
ALLOW
```

Recommended outcome:

```text
BLOCK
or
ESCALATE
```

according to governing policy.

---

# 56. Dependency Failure Propagation

If:

```text
A → B
```

and `B` fails, AMOS SHOULD invalidate only claims about `A` that actually depend upon `B`.

```text
Invalidate(B)
→
Invalidate(Descendants dependent on B)
```

not:

```text
InvalidateEntireSystem
```

unless B is globally load-bearing.

---

# 57. Selective Invalidation

Each dependency edge SHOULD identify affected claims or state.

```yaml
dependency_effect:
  dependency_id: B
  invalidates:
    - claim_A1
    - state_A2
  preserves:
    - claim_A3
```

This supports local recovery.

---

# 58. Dependency Blast Radius

Conceptually:

```text
BlastRadius(d)
=
ReachableLoadBearingDependents(d)
```

This MAY be used to prioritize validation and repair.

It is a MODEL diagnostic unless operationalized and tested.

---

# 59. Dependency Repair Priority

Repair priority SHOULD increase with:

```text
criticality;

dependency fan-out;

authority impact;

irreversibility;

runtime reachability;

number of blocked claims;

absence of fallback;

recovery-window pressure.
```

---

# 60. Dependency Failure Modes

```text
RD-FM01
missing required dependency

RD-FM02
unresolved dependency identity

RD-FM03
wrong dependency version

RD-FM04
type mismatch

RD-FM05
scope mismatch

RD-FM06
regime mismatch

RD-FM07
stale dependency

RD-FM08
revoked authority dependency

RD-FM09
missing policy dependency

RD-FM10
circular validation

RD-FM11
hidden transitive dependency

RD-FM12
dependency substitution without authorization

RD-FM13
correlated provenance treated as independent

RD-FM14
fallback incompatibility

RD-FM15
optional dependency incorrectly treated as required

RD-FM16
critical dependency incorrectly treated as optional

RD-FM17
dependency failure without downstream invalidation

RD-FM18
global invalidation when local invalidation is sufficient

RD-FM19
commit using stale dependency state

RD-FM20
superseded provider used as current
```

---

# 61. Additional Failure Modes

```text
RD-FM21
dependency exists only as placeholder

RD-FM22
documentation treated as executable provider

RD-FM23
test fixture treated as production dependency

RD-FM24
environment-specific provider generalized globally

RD-FM25
authority witness detached from authority source

RD-FM26
revocation not propagated

RD-FM27
policy version changed after evaluation

RD-FM28
dependency provenance missing

RD-FM29
provider identity collision

RD-FM30
ambiguous provider silently selected
```

---

# 62. Dependency Recovery

Recovery SHOULD follow:

```text
DETECT FAILURE
      ↓
IDENTIFY FAILED DEPENDENCY
      ↓
IDENTIFY AFFECTED EDGES
      ↓
IDENTIFY DEPENDENT CLAIMS
      ↓
INVALIDATE ONLY AFFECTED STATE
      ↓
CONTAIN EFFECTS
      ↓
RESOLVE / REPAIR / SUBSTITUTE
      ↓
REVALIDATE
      ↓
RESTORE ELIGIBLE DEPENDENTS
```

---

# 63. Dependency Substitution

Substitution MUST NOT occur solely because another provider is available.

A substitute SHOULD pass:

```text
identity check;

type check;

semantic compatibility;

scope check;

regime check;

version check;

provenance check;

authority check;

policy check;

validation check.
```

---

# 64. Rollback

If a dependency change causes failure:

```text
NewProvider
→ failure
```

AMOS SHOULD preserve the ability, where safe and permitted, to restore:

```text
PreviousKnownValidProvider
```

Rollback MUST preserve:

```text
change history;

failure evidence;

dependency lineage;

validation results.
```

---

# 65. Dependency Change Governance

Dependency changes SHOULD be treated as governed changes.

Examples:

```text
provider replacement;

version upgrade;

schema change;

policy dependency change;

authority dependency change;

fallback modification;

criticality change.
```

Consequential changes SHOULD trigger affected validation.

---

# 66. Dependency Change Record

```yaml
dependency_change:
  change_id: string

  dependency_id: string

  previous_provider: null
  new_provider: null

  reason: string

  affected_dependents: []

  authority: null

  validators: []

  rollback_target: null

  provenance: []

  status: "PROPOSED"
```

---

# 67. Root Dependency Registry

AMOS SHOULD maintain or derive a registry containing:

```yaml
dependency_registry:
  version: string
  entries: []

  provenance: []
  updated_at: null
```

Each entry SHOULD be uniquely identifiable.

---

# 68. Dependency Registry Law

The registry is descriptive/control metadata.

```text
REGISTERED
!=
AVAILABLE

REGISTERED
!=
VALIDATED

REGISTERED
!=
AUTHORIZED
```

---

# 69. Dependency Ownership

Each load-bearing dependency SHOULD have an accountable owner or governing subsystem.

Possible fields:

```yaml
ownership:
  semantic_owner: null
  runtime_owner: null
  policy_owner: null
  authority_owner: null
```

Ownership itself does not grant authority.

---

# 70. Dependency Authority Boundary

No component may create authority merely by depending upon another component.

```text
A depends on AuthorityResolver
```

does not mean:

```text
A is authorized.
```

Authorization requires a valid authority result bound to the specific requested effect.

---

# 71. Dependency and Capability Boundary

```text
Dependency available
→ capability may become technically executable
```

but:

```text
technically executable
!=
authorized
```

This boundary is mandatory.

---

# 72. Dependency and Proposal Boundary

A fully resolved dependency graph MAY support a proposal.

It does not automatically authorize durable execution.

```text
DependencyClosure
→ proposal eligibility
```

not necessarily:

```text
DependencyClosure
→ commit
```

---

# 73. Dependency and Commit Boundary

Commit eligibility MAY require stronger closure than planning.

Example:

```text
PLAN:
cached policy may be sufficient.

COMMIT:
current policy may be required.
```

Therefore dependency requirements MAY vary by execution phase.

---

# 74. Dependency Phase Model

Recommended phases:

```text
DISCOVERY

PLANNING

PROPOSAL

VALIDATION

COMMIT

POST-COMMIT

RECOVERY
```

Each dependency SHOULD declare the phases where it is load-bearing.

---

# 75. Root Dependency Validators

Recommended validators:

```text
validate_dependency_identity()

validate_dependency_type()

validate_dependency_direction()

validate_required_dependencies()

validate_transitive_closure()

validate_dependency_version()

validate_scope_compatibility()

validate_regime_compatibility()

validate_dependency_freshness()

validate_provenance()

validate_independence_claims()

validate_authority_dependencies()

validate_policy_dependencies()

validate_revocation_state()

validate_fallbacks()

validate_circularity()

validate_supersession()

validate_commit_dependencies()

validate_recovery_dependencies()
```

---

# 76. Dependency Tests

```text
RD-T001
A missing critical dependency MUST block dependent promotion.

RD-T002
An optional dependency failure MUST NOT invalidate unrelated required behavior.

RD-T003
A placeholder dependency MUST NOT count as implementation.

RD-T004
An incompatible provider MUST fail type validation.

RD-T005
A stale authority dependency MUST trigger revalidation.

RD-T006
A revoked authority MUST invalidate dependent commit eligibility.

RD-T007
A changed policy version MUST trigger applicable re-evaluation.

RD-T008
A circular validation chain MUST NOT produce VALIDATED.

RD-T009
A fallback MUST satisfy the same required contract.

RD-T010
An unauthorized substitute MUST NOT become active.
```

---

# 77. Additional Tests

```text
RD-T011
A shared-origin source pair MUST NOT be counted as independent evidence.

RD-T012
A provider valid in TEST MUST NOT automatically satisfy PRODUCTION.

RD-T013
Supersession MUST preserve lineage.

RD-T014
A dependency failure MUST invalidate only dependent claims where possible.

RD-T015
An unresolved dependency MUST remain UNKNOWN/GAP.

RD-T016
A capability dependency MUST NOT create authority.

RD-T017
Proposal dependency closure MUST NOT automatically produce COMMIT.

RD-T018
A commit MUST reject stale load-bearing dependency state when freshness is required.

RD-T019
Ambiguous providers MUST trigger resolution rather than arbitrary selection.

RD-T020
Dependency rollback MUST preserve the failed change record.
```

---

# 78. Dependency Falsifiers

The root dependency contract is violated if:

```text
a missing required dependency is treated as present;

a placeholder is treated as implementation;

an incompatible provider is accepted;

an expired authority dependency permits commit;

revocation is ignored;

policy changes are ignored at a required freshness boundary;

a circular proof validates itself;

shared provenance is counted as independent confirmation;

a substitute is installed without required authority;

a critical dependency failure produces PASS;

a transitive dependency is omitted from closure;

a scope-specific dependency is generalized universally.
```

---

# 79. Dependency Coverage

Dependency coverage SHOULD be evaluated per claim.

```yaml
dependency_coverage:
  declared_dependencies: []
  resolved_dependencies: []
  unresolved_dependencies: []
  critical_gaps: []
  stale_dependencies: []
  conflicted_dependencies: []
```

A percentage MAY be calculated for diagnostics, but critical gaps override scalar completeness.

---

# 80. Dependency Gap Classes

```text
CRITICAL

DECISION_RELEVANT

EXPLANATORY

COSMETIC
```

Examples:

```text
missing authority dependency
→ CRITICAL

missing runtime implementation binding
→ CRITICAL for runtime claims

missing explanatory diagram
→ potentially COSMETIC
```

---

# 81. Dependency Gap Matrix

```yaml
gap_matrix:

  AUTHORITATIVE_ROOT_DEPENDENCY_GRAPH:
    state: UNKNOWN/GAP
    severity: CRITICAL_FOR_CANONICAL_CLAIM

  AUTHORITATIVE_ROOT_INVENTORY:
    state: UNKNOWN/GAP
    severity: CRITICAL_FOR_EXACT_CLOSURE

  EXECUTABLE_DEPENDENCY_RESOLVER:
    state: UNKNOWN/GAP
    severity: CRITICAL_FOR_IMPLEMENTATION_CLAIM

  RUNTIME_DEPENDENCY_REGISTRY:
    state: UNKNOWN/GAP

  VERSION_COMPATIBILITY_RULES:
    state: UNKNOWN/GAP

  COMMIT_TIME_REVALIDATION:
    state: UNKNOWN/GAP

  REVOCATION_PROPAGATION:
    state: UNKNOWN/GAP

  FALLBACK_IMPLEMENTATION:
    state: UNKNOWN/GAP

  EXECUTED_VALIDATION:
    state: UNKNOWN/GAP

  CANON_APPROVAL:
    state: UNKNOWN/GAP
```

---

# 82. Dependency RSCF

```yaml
rscf:

  claim:
    id: "AMOS_ROOT_DEPENDENCIES"
    class: MODEL

    text: >
      AMOS OS root dependencies should be represented as typed,
      directional, provenance-aware, scope-aware, regime-aware and
      freshness-aware relationships whose load-bearing closure must be
      established for the specific claim or action being evaluated.

  premises:
    - dependency_presence_is_not_dependency_validity
    - dependency_validity_is_claim_specific
    - mutable_dependencies_can_become_stale
    - authority_and_policy_dependencies_may_change
    - dependency_failure_should_selectively_invalidate_dependents
    - provenance_correlation_affects_evidence_independence

  evidence: []

  provenance:
    origin_architect: "Trang Phan"
    artifact: "00_ROOT_DEPENDENCIES.md"

  scope:
    system: "AMOS OS"
    layer: "ROOT DEPENDENCIES"

  regime:
    - ARCHITECTURE
    - GOVERNANCE
    - DEPENDENCY_MODEL

  dependencies:
    - 00_ROOT_CONTRACT
    - 00_ROOT_BOUNDARIES
    - 00_ROOT_AUTHORIZATION
    - 00_ROOT_COVERAGE
    - SYSTEM_MAP
    - CONTROL_PLANE_MAP
    - PROVENANCE
    - RSCF

  competing:
    - flat_file_dependency_model
    - dependency_name_equals_resolution
    - static_dependency_validity
    - global_recomputation_after_every_failure
    - optimistic_missing_dependency

  falsifiers:
    - missing_dependency_treated_as_resolved
    - stale_dependency_used_without_required_revalidation
    - dependency_scope_mismatch_ignored
    - revoked_authority_dependency_allows_commit
    - circular_validation_self_promotes
    - shared_origin_treated_as_independent

  confidence_ceiling: 0
```

---

# 83. Root Dependency Invariants

```text
RD-I01:
PLACEHOLDER != IMPLEMENTED

RD-I02:
ADDRESSABLE != RESOLVED

RD-I03:
RESOLVED != VALIDATED

RD-I04:
VALIDATED != AUTHORIZED

RD-I05:
CAPABILITY != AUTHORITY

RD-I06:
PROPOSAL != COMMIT

RD-I07:
UNKNOWN/GAP != PASS

RD-I08:
DEPENDENCY NAME != DEPENDENCY CLOSURE

RD-I09:
SHARED ORIGIN != INDEPENDENT CONFIRMATION

RD-I10:
STALE != CURRENT
```

---

# 84. Additional Invariants

```text
RD-I11:
Critical unresolved dependencies block dependent promotion.

RD-I12:
Dependency validity inherits scope.

RD-I13:
Dependency validity inherits regime.

RD-I14:
Mutable dependencies require freshness semantics.

RD-I15:
Supersession preserves dependency lineage.

RD-I16:
Dependency substitution requires compatibility.

RD-I17:
Authority-sensitive substitution requires authority.

RD-I18:
Failure invalidation propagates only through actual dependency edges.

RD-I19:
Commit-time dependencies may be stricter than planning dependencies.

RD-I20:
A dependency graph cannot self-certify its own correctness.
```

---

# 85. Dependency Decision States

Dependency evaluation SHOULD return one of:

```text
SATISFIED

PARTIALLY_SATISFIED

DEGRADED

BLOCKED

STALE

CONFLICTED

QUARANTINED

UNKNOWN/GAP
```

---

# 86. SATISFIED

Use `SATISFIED` only when all load-bearing requirements for the declared claim have sufficient support.

This does not imply universal validity.

---

# 87. PARTIALLY_SATISFIED

Use when:

```text
some dependency requirements are resolved
but
remaining gaps do not yet justify full closure.
```

Missing dependencies MUST remain explicit.

---

# 88. BLOCKED

Use when a critical dependency is:

```text
missing;

failed;

revoked;

incompatible;

or unresolved.
```

and operation cannot safely continue.

---

# 89. STALE

Use when:

```text
dependency was previously valid
but
freshness requirements no longer hold.
```

`STALE` requires revalidation rather than automatic rejection unless policy specifies otherwise.

---

# 90. CONFLICTED

Use when dependency requirements cannot simultaneously be satisfied or multiple providers have incompatible claims.

Preserve the conflict until discriminating evidence or governing precedence resolves it.

---

# 91. UNKNOWN/GAP

Use when available evidence is insufficient to classify dependency validity.

```text
UNKNOWN/GAP
```

is a legitimate governed result.

It MUST NOT be converted to `SATISFIED` merely to complete a workflow.

---

# 92. Root Dependency Workflow

```text
IDENTIFY CONSUMER
        ↓
IDENTIFY CLAIM / ACTION
        ↓
ENUMERATE DIRECT DEPENDENCIES
        ↓
TYPE DEPENDENCIES
        ↓
CLASSIFY CRITICALITY
        ↓
EXPAND LOAD-BEARING TRANSITIVE DEPENDENCIES
        ↓
RESOLVE PROVIDERS
        ↓
CHECK TYPE / VERSION
        ↓
CHECK SCOPE / REGIME
        ↓
CHECK PROVENANCE
        ↓
CHECK FRESHNESS
        ↓
CHECK POLICY / AUTHORITY
        ↓
CHECK CONFLICTS / CYCLES
        ↓
CLASSIFY GAPS
        ↓
DETERMINE CLOSURE
        ↓
SATISFIED / BLOCKED / UNKNOWN
```

---

# 93. Fast-Path Dependency Resolution

A local fast path MAY be used only when:

```text
dependency identity is known;

dependency closure is bounded;

provider is current;

scope matches;

regime matches;

provenance is sufficient;

no material conflict exists;

freshness is valid;

no authority-sensitive mutation occurred.
```

Otherwise escalate to deeper dependency resolution.

---

# 94. Dependency Sensitivity

For consequential decisions, AMOS SHOULD identify:

```text
the smallest dependency failure
capable of changing the result.
```

That dependency should receive priority validation.

Example:

```text
If current authority validity alone determines whether commit is allowed,
validate authority before inspecting noncritical descriptive dependencies.
```

---

# 95. Dependency Repair Strategy

Prefer:

```text
local resolution;

local substitution;

local revalidation;

selective rollback;

selective invalidation.
```

Avoid global recomputation unless dependency structure actually requires it.

---

# 96. Dependency Audit Record

```yaml
dependency_audit:

  audit_id: string

  consumer: string

  requested_claim_or_action: string

  dependency_snapshot: []

  unresolved: []

  stale: []

  conflicts: []

  critical_blockers: []

  authority_state: "UNKNOWN/GAP"
  policy_state: "UNKNOWN/GAP"

  result: "UNKNOWN/GAP"

  provenance: []

  timestamp: null
```

---

# 97. Relationship to Root Coverage

`00_ROOT_COVERAGE.md` asks:

```text
Are the required dependencies sufficiently covered?
```

`00_ROOT_DEPENDENCIES.md` defines:

```text
what a dependency is;

how dependency closure is evaluated;

how dependency failure propagates;

how dependency validity changes.
```

Therefore:

```text
ROOT COVERAGE
→ consumes
ROOT DEPENDENCY STATE
```

but neither artifact alone proves runtime implementation.

---

# 98. Relationship to Root Authorization

Authorization depends upon dependency integrity.

An authority decision based upon:

```text
stale revocation state;

wrong principal;

wrong resource;

wrong policy version;
```

cannot be assumed valid merely because an authority resolver returned `ALLOW`.

Authorization inherits the integrity of its load-bearing dependencies.

---

# 99. Relationship to Root Boundaries

Dependencies MUST respect system boundaries.

A provider outside the authorized boundary requires explicit admission semantics.

```text
EXTERNAL PROVIDER
→
BOUNDARY CHECK
→
PROVENANCE CHECK
→
POLICY CHECK
→
ADMISSION / REJECTION
```

External availability alone does not grant admission.

---

# 100. Relationship to Provenance

Dependency graphs and provenance graphs overlap but are not identical.

```text
dependency:
A requires B.

provenance:
A was derived from B.
```

These are different relations.

AMOS MUST NOT silently collapse them.

---

# 101. Relationship to Causality

Dependency is not automatically causation.

```text
A depends on B
```

means B is required under the declared architecture.

It does not necessarily mean:

```text
B empirically causes A.
```

This preserves the causal firewall.

---

# 102. Relationship to Memory

Persistent memory MAY become a dependency when later reasoning or execution relies upon it.

Such dependency SHOULD preserve:

```text
memory identity;

semantic origin;

freshness;

scope;

confidence;

supersession;

provenance.
```

A stale or conflicted memory SHOULD not silently remain load-bearing.

---

# 103. Relationship to Agents

Agents MAY consume dependencies but MUST NOT redefine root dependency validity merely through local reasoning.

Agents may:

```text
discover;

propose;

validate;

report;

request substitution.
```

Root governance retains authority over consequential dependency promotion.

---

# 104. Relationship to Skills

Skills MAY declare:

```yaml
skill_dependencies:
  required: []
  optional: []
  tools: []
  control_planes: []
  authority: []
  policies: []
```

A Skill being installed or addressable does not establish that its dependencies are currently satisfied.

---

# 105. Relationship to Workflows

Workflows SHOULD expose dependencies at each transition.

```text
STEP A
→ requires X

STEP B
→ requires Y

COMMIT
→ requires Z
```

This prevents late-stage hidden dependencies.

---

# 106. Relationship to Protocols

Protocol dependencies MAY include:

```text
participant identity;

message schema;

transport;

state;

authority;

timeout;

acknowledgement;

recovery mechanism.
```

A protocol with unresolved load-bearing dependencies remains partially specified or blocked.

---

# 107. Relationship to Tests

Tests SHOULD map directly to dependency requirements.

Example:

```text
Requirement:
revoked authority blocks commit.

Dependency:
commit gate → current revocation state.

Test:
revoke authority after proposal but before commit.

Expected:
COMMIT_REJECTED.
```

This tests the dependency edge, not merely isolated components.

---

# 108. Relationship to Recovery

Recovery depends upon knowing:

```text
what failed;

which dependents consumed it;

which state was derived from it;

which valid checkpoint precedes failure.
```

Therefore dependency provenance materially supports selective recovery.

---

# 109. Root Dependency Completion Criterion

This artifact is specification-complete for its declared MODEL scope when it defines:

```text
dependency identity;

dependency types;

direction;

criticality;

closure;

scope;

regime;

freshness;

provenance;

authority interaction;

policy interaction;

failure propagation;

repair;

rollback;

validators;

tests;

falsifiers;

gap state.
```

It does **not** establish that the actual AMOS OS dependency graph has been implemented or validated.

---

# 110. Current Completion State

```yaml
current_completion_state:

  artifact:
    name: "00_ROOT_DEPENDENCIES.md"

  specification:
    state: "COMPLETE_FOR_DECLARED_MODEL_SCOPE"

  epistemic_class:
    state: "MODEL"

  dependency_schema:
    state: "SPECIFIED"

  dependency_classes:
    state: "SPECIFIED"

  dependency_closure_model:
    state: "SPECIFIED"

  failure_propagation_model:
    state: "SPECIFIED"

  repair_model:
    state: "SPECIFIED"

  validators:
    state: "SPECIFIED_NOT_EXECUTED"

  tests:
    state: "SPECIFIED_NOT_EXECUTED"

  authoritative_repository_mapping:
    state: "UNKNOWN/GAP"

  executable_dependency_runtime:
    state: "UNKNOWN/GAP"

  empirical_validation:
    state: "UNKNOWN/GAP"

  canon_alignment:
    state: "UNKNOWN/GAP"

  canon_approval:
    state: "UNKNOWN/GAP"

  confidence_ceiling: 0
```

---

# 111. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

DECLARED != RESOLVED

RESOLVED != VALIDATED

VALIDATED != AUTHORIZED

CAPABILITY != AUTHORITY

DEPENDENCY != CAUSATION

PROPOSAL != COMMIT

STALE != CURRENT

UNKNOWN/GAP != PASS
```

---

# 112. Final Root Dependency Contract

> **AMOS OS shall treat dependencies as typed, directional, scoped, regime-bound, provenance-aware and potentially time-varying relationships. No object, claim, capability, authorization, policy decision, workflow transition, or commit may inherit validity merely because its dependencies are named or structurally present. Load-bearing dependencies must be resolved to the level required by the specific claim or action. Mutable dependencies must satisfy applicable freshness requirements. Dependency failures must propagate only through genuine dependency edges wherever possible, preserving unaffected state. Critical unresolved dependencies block dependent promotion. Substitution requires compatibility and, where applicable, authority. UNKNOWN/GAP remains UNKNOWN/GAP until sufficient evidence exists.**

---

# END — `00_ROOT_DEPENDENCIES.md`

**Status:** `PROPOSED_SPECIFICATION`
**Specification:** `COMPLETE_FOR_DECLARED_MODEL_SCOPE`
**Epistemic class:** `MODEL`
**Implementation:** `UNKNOWN/GAP`
**Executed validation:** `UNKNOWN/GAP`
**Canon alignment:** `UNKNOWN/GAP`
**Origin architect / steward:** **Trang Phan**

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 00_root_dependencies
node_type: note
path: 00_ROOT/00_ROOT_DEPENDENCIES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
