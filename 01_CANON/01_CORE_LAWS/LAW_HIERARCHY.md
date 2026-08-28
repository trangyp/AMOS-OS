---
type: law
source: 01_CANON/01_CORE_LAWS
artifact_id: AMOS-LAW-HIERARCHY
name: LAW_HIERARCHY
title: "AMOS Law Hierarchy — Authority, Precedence, Scope, Conflict, and Supersession"
document_version: "2.0.0"
hierarchy_version: "4.4"
amos_core_target: "v4.4"
status: ACTIVE_CANON_CANDIDATE
conclusion_class: AMOS_MODEL
rscf_state: derived
canon_group: tech-ai
canon_type: law-hierarchy
origin_architect: Trang Phan
steward: Trang Phan
created: 2026-08-25
updated: 2026-08-25
tags:
- amos
- canon
- universe
- amos-os
- amos-core
- amos-core-v4-4
- law
- law-hierarchy
- authority
- precedence
- governance
- scope
- regime
- provenance
- supersession
- invariants
- conflict-resolution
- rscf
- canon-group/tech-ai
- canon/framework
- canon/law
- rscf/claim
- rscf/provenance
- rscf/state/derived
- topic/law-hierarchy
aliases: "- AMOS Law Hierarchy
  - AMOS Canon Law Hierarchy
  - AMOS Authority Hierarchy
  - AMOS Precedence M..."
related: "see body"
---
# AMOS Law Hierarchy
**Origin architect / steward:** Trang Phan
> **Status:** `ACTIVE_CANON_CANDIDATE`  
> **AMOS Core target:** `v4.4`  
> **Conclusion class:** `AMOS_MODEL`
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: core_laws
---

# AMOS Law Hierarchy — Authority, Precedence, Scope, Conflict, and Supersession

## 0. Purpose

The `LAW_HIERARCHY` defines how governing AMOS rules relate by:

- authority;
- precedence;
- scope;
- regime;
- specificity;
- version;
- provenance;
- lifecycle state;
- supersession;
- conflict resolution.

Its purpose is to prevent a lower-authority artifact, runtime behavior, model output, agent decision, workflow, memory entry, or implementation detail from silently overriding higher-order AMOS law.

```text
LAW
↓
INVARIANT
↓
POLICY
↓
CONTRACT
↓
IMPLEMENTATION
↓
EXECUTION
↓
OBSERVATION
```

This is a governance hierarchy.

It is **not** a claim that every current AMOS artifact has already been validated and promoted into one of these levels.

---

# 1. Constitutional Boundary

The first hierarchy rule is:

```text
AUTHORITY
!=
CAPABILITY
```

A component's ability to perform an operation does not establish its authority to define, modify, override, or commit governing law.

Likewise:

```text
IMPLEMENTATION != LAW
RUNTIME != CANON
MODEL != AUTHORITY
MEMORY != CANON
TOOL != PERMISSION
AGENT != GOVERNANCE
PROPOSAL != COMMIT
OBSERVATION != LAW
```

---

# 2. Canonical Authority Stack

The conceptual AMOS law stack is:

```text
L0  CORE INTEGRITY LAW
│
├── L1  CONSTITUTIONAL / ROOT LAWS
│
├── L2  CANONICAL INVARIANTS
│
├── L3  GOVERNANCE / AUTHORITY POLICIES
│
├── L4  SYSTEM & PLANE CONTRACTS
│
├── L5  DOMAIN / REGIME RULES
│
├── L6  COMPONENT CONTRACTS
│
├── L7  EXECUTION / WORKFLOW RULES
│
├── L8  LOCAL CONFIGURATION
│
└── L9  RUNTIME DECISIONS / PROPOSALS
```

Lower levels operate inside the envelope established by higher levels.

They do not automatically possess authority to rewrite them.

---

# 3. L0 — Core Integrity Law

The highest-order governing priority is:

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

This ordering constrains every lower layer.

No optimization, workflow, model, runtime policy, agent strategy, or implementation convenience may legitimately invert it.

Associated hard laws include:

```text
UNKNOWN/GAP != PASS

MISSING_EVIDENCE
!=
LICENSE_TO_INVENT

OPTIMIZATION
MUST NOT
WEAKEN INTEGRITY
```

---

# 4. L1 — Constitutional / Root Laws

L1 contains architectural laws defining fundamental AMOS separations and authority boundaries.

Examples:

```text
CANON != KERNEL
KERNEL != CONTROL_PLANE
CONTROL_PLANE != RUNTIME
RUNTIME != COGNITION

ORGAN != AGENT
AGENT != SKILL
SKILL != WORKFLOW
WORKFLOW != PROTOCOL

MEMORY != CANON
KNOWLEDGE != AUTHORITY
MODEL != AUTHORITY
TOOL != PERMISSION

CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
```

These are structural firewalls.

A lower-level component cannot erase them by implementation.

---

# 5. L2 — Canonical Invariants

Canonical invariants operationalize constitutional laws as testable or enforceable constraints.

Canonical source:

```text
INVARIANT_REGISTRY
```

Examples:

```text
SOURCE_CLAIM != VERIFIED
MODEL != FACT
STRUCTURAL_SIMILARITY != CAUSATION
CORRELATION != CAUSAL_EFFECT

INDEPENDENCE MUST BE DEMONSTRATED
UNKNOWN/GAP != PASS

INVALID(PREMISE)
→
INVALID(DEPENDENT_CONCLUSIONS)
```

An invariant may constrain multiple lower planes simultaneously.

---

# 6. L3 — Governance / Authority Policies

Governance policies define:

```text
WHO MAY DECIDE
WHO MAY PROPOSE
WHO MAY APPROVE
WHO MAY COMMIT
WHO MAY OVERRIDE
WHO MAY ROLLBACK
WHO MAY PROMOTE
```

These normally belong to the control-plane authority boundary.

```text
CANON
↓ constrains
CONTROL PLANE
↓ authorizes
RUNTIME
```

The control plane may enforce canon.

It may not silently redefine canon unless a canon-authorized governance mechanism explicitly permits the transition.

---

# 7. L4 — System and Plane Contracts

System contracts define obligations for major AMOS planes.

Examples:

```text
KERNEL CONTRACT
CONTROL PLANE CONTRACT
RUNTIME CONTRACT
COGNITIVE ORGANISM CONTRACT
MEMORY CONTRACT
STATE CONTRACT
PROVENANCE CONTRACT
SECURITY CONTRACT
OBSERVABILITY CONTRACT
```

A plane contract is subordinate to applicable constitutional law and canonical invariants.

```text
PLANE_CONTRACT
MUST_SATISFY
HIGHER_ORDER_LAWS
```

---

# 8. L5 — Domain and Regime Rules

Domain-specific rules may specialize general law for a valid scope.

Examples:

```text
LEGAL
FINANCE
RESEARCH
CODING
GOVERNANCE
OPERATIONS
SECURITY
COUNTRY OVERLAY
```

A valid specialization may be more restrictive than a general rule.

It may not silently weaken a higher-order invariant.

```text
SPECIALIZATION
CAN NARROW

SPECIALIZATION
CANNOT SILENTLY INVALIDATE
PARENT LAW
```

---

# 9. L6 — Component Contracts

Component-level rules govern:

```text
AGENTS
SKILLS
TOOLS
MODELS
MEMORIES
PROTOCOLS
INTERFACES
SCHEMAS
```

Example:

```text
AGENT CONTRACT
↓
ROLE
CAPABILITY
INPUT
OUTPUT
DEPENDENCIES
AUTHORITY BOUNDARY
FAILURE SEMANTICS
```

A component contract cannot grant itself authority merely by declaring it.

```text
SELF_DECLARED_AUTHORITY
!=
GOVERNED_AUTHORITY
```

---

# 10. L7 — Workflow and Execution Rules

Workflow rules determine execution ordering and orchestration.

```text
STEP
→
GATE
→
TRANSITION
→
NEXT STEP
```

Workflow ordering does not supersede higher authority.

For example:

```text
WORKFLOW_SAYS_EXECUTE
+
AUTHORITY_GATE_FAILS
→
DO_NOT_EXECUTE
```

---

# 11. L8 — Local Configuration

Local configuration may alter permitted behavior inside an existing authority envelope.

Examples:

```text
TIMEOUT
RETRY COUNT
MODEL SELECTION
ROUTING WEIGHT
DISPLAY MODE
LOCAL FEATURE FLAG
```

Configuration cannot legitimately transform:

```text
FORBIDDEN
→
AUTHORIZED
```

unless the governing authority explicitly defines that configuration as an authorization mechanism.

---

# 12. L9 — Runtime Decisions and Proposals

Runtime outputs occupy the lowest governing level.

Examples:

```text
MODEL OUTPUT
AGENT RECOMMENDATION
PROPOSAL
WORKING HYPOTHESIS
LOCAL DECISION
CANDIDATE STATE
```

These may influence higher-level governance processes.

They do not automatically rewrite those processes.

```text
RUNTIME_PROPOSAL
→
GOVERNANCE_GATE
→
COMMIT
```

not:

```text
RUNTIME_PROPOSAL
=
CANON
```

---

# 13. Authority Is Typed

Authority is not a single scalar.

AMOS should distinguish authority types where material:

```text
DEFINITION_AUTHORITY
INTERPRETATION_AUTHORITY
VALIDATION_AUTHORITY
EXECUTION_AUTHORITY
COMMIT_AUTHORITY
OVERRIDE_AUTHORITY
ROLLBACK_AUTHORITY
PROMOTION_AUTHORITY
SUPERSESSION_AUTHORITY
```

Possession of one authority type does not automatically imply another.

Example:

```text
EXECUTION_AUTHORITY
!=
CANON_MODIFICATION_AUTHORITY
```

---

# 14. Authority Is Scoped

Authority exists within an applicability envelope.

```yaml
authority_scope:
  system:
  plane:
  domain:
  environment:
  operation:
  state_class:
  regime:
  temporal_window:
  version:
```

Therefore:

```text
AUTHORIZED(SCOPE_A)
!=
AUTHORIZED(SCOPE_B)
```

unless the authority explicitly spans both.

---

# 15. Precedence Is Not Determined by Filename

Never infer authority solely from:

```text
FILE NAME
DIRECTORY DEPTH
NUMBER PREFIX
CREATION DATE
FILE SIZE
DOCUMENT LENGTH
VERSION-LIKE STRING
```

Repository placement may provide structural evidence.

It does not independently prove authority.

```text
PLACEMENT
!=
AUTHORITY
```

Authority requires valid canonical/governance provenance.

---

# 16. Precedence Resolution Function

When two rules appear to conflict, resolve using a typed precedence sequence.

Conceptually:

```text
VALIDITY
↓
AUTHORITY CLASS
↓
SCOPE APPLICABILITY
↓
REGIME APPLICABILITY
↓
SPECIFICITY
↓
VERSION / SUPERSESSION
↓
TEMPORAL VALIDITY
↓
PROVENANCE
```

This is not equivalent to:

```text
NEWEST FILE ALWAYS WINS
```

or:

```text
MOST SPECIFIC ALWAYS WINS
```

Specificity only matters after higher-order compatibility is established.

---

# 17. Conflict Resolution Protocol

For candidate rules `A` and `B`:

```text
1. ARE BOTH VALID?
2. ARE BOTH APPLICABLE?
3. DO THEY ACTUALLY CONFLICT?
4. WHAT AUTHORITY CLASS DOES EACH HOLD?
5. WHAT IS EACH RULE'S SCOPE?
6. WHAT REGIME DOES EACH RULE GOVERN?
7. IS ONE A VALID SPECIALIZATION?
8. IS ONE SUPERSEDED?
9. ARE THEIR PROVENANCE CHAINS VALID?
10. DOES AN EXPLICIT OVERRIDE EXIST?
```

Only then may precedence be determined.

---

# 18. Apparent Conflict

Two laws may differ without conflicting.

Example:

```text
LAW_A applies to REGIME_A
LAW_B applies to REGIME_B
```

If:

```text
REGIME_A != REGIME_B
```

then both may remain valid.

Do not force unnecessary supersession.

---

# 19. Genuine Conflict

A genuine conflict exists when two simultaneously applicable rules require incompatible outcomes.

```text
A requires X
B requires NOT X
```

within the same relevant:

```text
SCOPE
REGIME
TIME
VERSION
AUTHORITY CONTEXT
```

Such conflicts require explicit resolution.

---

# 20. Unresolved Conflict

If precedence cannot be validly established:

```text
STATE = COMPETING
```

or:

```text
STATE = UNKNOWN/GAP
```

depending on the evidence topology.

Never resolve an authority conflict through fluent guesswork.

---

# 21. Higher Authority Rule

A valid higher-order law normally constrains a lower-order law.

```text
HIGHER_AUTHORITY
↓
LOWER_AUTHORITY
```

But this does not mean the higher-level rule automatically answers every local question.

A lower-level specialization may legitimately provide detail when:

```text
PARENT LAW PERMITS SPECIALIZATION
∧
SPECIALIZATION REMAINS IN SCOPE
∧
SPECIALIZATION DOES NOT VIOLATE PARENT INVARIANTS
```

---

# 22. Specificity Rule

Specific rules may refine general rules.

Example:

```text
GENERAL:
External effects require authority.

SPECIFIC:
Production deployment requires
DEPLOYMENT_COMMIT_AUTHORITY.
```

The specific rule specializes the general one.

It does not replace the constitutional law:

```text
CAPABILITY != AUTHORITY
```

---

# 23. Restrictive Specialization

Where governance permits:

```text
CHILD_RULE
```

may impose stronger constraints than its parent.

Example:

```text
PARENT:
Human approval required for high-risk commits.

CHILD:
Two independent approvals required
for irreversible production migration.
```

This is compatible if the parent defines a minimum rather than an exclusive requirement.

---

# 24. Weakening Rule

A lower-authority rule may not silently weaken a higher-order constraint.

```text
HIGHER:
AUTHORITY_REQUIRED

LOWER:
AUTHORITY_OPTIONAL
```

is invalid unless an explicit higher-authority exception licenses it.

---

# 25. Exception Contract

An exception must be explicit and typed.

```yaml
exception:
  exception_id:
  parent_law:
  authority:
  scope:
  regime:
  condition:
  justification:
  effective_from:
  expires_at:
  evidence:
  rollback:
  provenance:
```

No implicit exception exists merely because implementation behaves differently.

---

# 26. Override Contract

Override is stronger than specialization.

An override should declare:

```text
WHAT IS OVERRIDDEN
WHO AUTHORIZED IT
WHY
WHERE
WHEN
FOR HOW LONG
WHAT RISK IT CREATES
HOW IT IS AUDITED
HOW IT IS REVOKED
```

Conceptually:

```yaml
override:
  override_id:
  target_law:
  target_version:

  authority:
  authority_provenance:

  scope:
  regime:

  reason:

  effective_at:
  expires_at:

  risk_class:

  evidence: []

  rollback:

  audit_record:
```

---

# 27. Non-Overrideable Laws

Some laws may be designated:

```text
NON_OVERRIDEABLE
```

within the AMOS governance model.

Examples of candidate constitutional constraints include:

```text
UNKNOWN/GAP != PASS
NO FABRICATED EVIDENCE
CAPABILITY != AUTHORITY
PROVENANCE MUST NOT BE FABRICATED
OPTIMIZATION MUST NOT WEAKEN INTEGRITY
```

Final non-overrideable status must be bound through canon governance rather than inferred solely from this document.

---

# 28. Supersession

Law evolution uses explicit supersession.

```text
LAW_A v1
↓
SUPERSEDED_BY
↓
LAW_A v2
```

Supersession does not erase history.

```text
SUPERSEDED
!=
DELETED
```

Required lineage should remain recoverable.

---

# 29. Supersession Record

```yaml
supersession:
  supersession_id:

  predecessor:
    artifact_id:
    semantic_id:
    version:

  successor:
    artifact_id:
    semantic_id:
    version:

  reason:

  compatibility:
    backward_compatible:
    breaking_change:

  affected_dependencies: []

  migration_requirements: []

  effective_at:

  authority:

  provenance:
```

---

# 30. Semantic Identity Rule

The following identities remain distinct:

```text
FILENAME
ARTIFACT_ID
SEMANTIC_ID
VERSION_ID
PROVENANCE_ID
RUNTIME_INSTANCE_ID
```

Therefore:

```text
RENAME
!=
SUPERSESSION
```

and:

```text
FILE_REPLACEMENT
!=
VALID_CANON_PROMOTION
```

---

# 31. Version Precedence

Version number alone does not determine authority.

```text
v2
```

does not automatically supersede:

```text
v1
```

unless valid lineage establishes:

```text
v1
→ SUPERSEDED_BY
→ v2
```

Unknown lineage remains:

```text
UNKNOWN/GAP
```

---

# 32. Temporal Rule

A law may have:

```text
effective_from
effective_until
review_at
deprecated_at
superseded_at
```

A newer law does not retroactively invalidate all historical states unless the governing semantics explicitly require it.

```text
INVALID_NOW
!=
INVALID_THEN
```

---

# 33. Regime Rule

Rules inherit regime validity.

```text
LAW_VALID(REGIME_A)
```

does not imply:

```text
LAW_VALID(REGIME_B)
```

A detected regime shift may require:

```text
REVALIDATION
REINTERPRETATION
NEW SPECIALIZATION
OR
GOVERNANCE ESCALATION
```

---

# 34. Scope Rule

Every consequential law should eventually expose its applicability envelope.

Possible dimensions:

```text
SYSTEM
PLANE
DOMAIN
POPULATION
ENVIRONMENT
SCALE
TIME
REGIME
OPERATION
STATE CLASS
ASSUMPTIONS
```

Silent scope expansion is prohibited.

---

# 35. Provenance Rule

A governing law should retain sufficient provenance to determine:

```text
ORIGIN
AUTHORITY
REVISION
SUPERSESSION
DEPENDENCIES
VALIDATION STATE
```

Repetition does not create authority.

```text
ONE CANONICAL SOURCE
→
100 COPIES
!=
100 AUTHORITIES
```

---

# 36. Provenance Topology

Authority analysis must account for shared ancestry.

Example:

```text
CANON_LAW_A
├── POLICY_B
├── README_C
├── AGENT_PROMPT_D
└── WORKFLOW_E
```

The four descendants do not constitute four independent canonical laws.

They remain downstream derivatives unless separately governed.

---

# 37. Canon / Kernel Relationship

```text
CANON
=
WHAT MUST HOLD

KERNEL
=
DETERMINISTIC MACHINERY
THAT MAY ENFORCE
WHAT MUST HOLD
```

Therefore:

```text
CANON != KERNEL
```

Kernel behavior does not automatically become canon merely because it is implemented.

---

# 38. Kernel / Control Plane Relationship

```text
KERNEL
=
DETERMINISTIC OPERATORS / INVARIANTS

CONTROL PLANE
=
AUTHORITY / POLICY / COMMIT GOVERNANCE
```

Therefore:

```text
KERNEL != CONTROL_PLANE
```

A deterministic operator does not automatically possess commit authority.

---

# 39. Control Plane / Runtime Relationship

```text
CONTROL_PLANE
=
WHO / WHEN / UNDER WHAT POLICY

RUNTIME
=
HOW EXECUTION OCCURS
```

Therefore:

```text
CONTROL_PLANE != RUNTIME
```

Runtime capability remains subordinate to authority gates.

---

# 40. Runtime / Cognition Relationship

```text
RUNTIME
=
EXECUTION HARNESS

COGNITION
=
REASONING / INTERPRETATION / MODELING
```

Therefore:

```text
RUNTIME != COGNITION
```

A cognitive conclusion does not automatically authorize execution.

---

# 41. Agent Authority Boundary

Agents are role-based workers.

```text
AGENT
=
ROLE + CAPABILITY + CONTRACT
```

not:

```text
AGENT
=
SOVEREIGN AUTHORITY
```

An agent's effective authority is inherited or delegated through governed contracts.

---

# 42. Skill Authority Boundary

A skill defines a reusable procedure.

```text
SKILL
=
PROCEDURAL CAPABILITY
```

not:

```text
SKILL
=
PERMISSION
```

Calling a skill does not bypass authorization.

---

# 43. Workflow Authority Boundary

A workflow coordinates multiple steps.

```text
WORKFLOW
=
ORCHESTRATION
```

not:

```text
WORKFLOW
=
CANON
```

Workflow structure cannot silently redefine governing laws.

---

# 44. Model Authority Boundary

Models may provide:

```text
PREDICTIONS
CLASSIFICATIONS
ESTIMATES
HYPOTHESES
RECOMMENDATIONS
```

but:

```text
MODEL OUTPUT
!=
GOVERNED AUTHORITY
```

A high-confidence model result does not independently authorize a state transition.

---

# 45. Memory Authority Boundary

Memory stores retained information.

```text
MEMORY
!=
CANON
```

Memory may contain:

```text
OBSERVATIONS
CLAIMS
DERIVED KNOWLEDGE
HISTORICAL DECISIONS
```

but persistence does not promote those records to governing law.

---

# 46. Knowledge Authority Boundary

```text
KNOWLEDGE
!=
AUTHORITY
```

A knowledge artifact can explain law without possessing authority to change it.

---

# 47. Tool Authority Boundary

```text
TOOL
=
CAPABILITY
```

not:

```text
TOOL
=
AUTHORIZATION
```

The presence of an executable connector or external effector does not establish permission to use it.

---

# 48. State Authority Boundary

State records what the system currently treats as state.

State itself does not define the law governing state transitions.

```text
STATE
!=
STATE_TRANSITION_AUTHORITY
```

---

# 49. Evidence Authority Boundary

Evidence supports claims.

```text
EVIDENCE
!=
GOVERNANCE AUTHORITY
```

Strong evidence can justify changing a law through the governed process.

It does not silently rewrite the law.

---

# 50. RSCF Law Binding

An RSCF may bind applicable law explicitly.

```yaml
rscf:
  node_id:

  claim:
  claim_class:

  governing_laws:
    - law_id:
      version:
      applicability:

  invariants: []

  premises: []
  evidence: []
  provenance: []

  scope:
  regime:
  freshness:

  dependencies: []

  conclusion:
```

A conclusion violating an applicable higher-order law cannot be promoted merely because its local reasoning is internally coherent.

---

# 51. Multi-RSCF Authority

Where multiple RSCFs jointly support a governed decision:

```text
RSCF_A
+
RSCF_B
+
RSCF_C
→
DECISION
```

their authority and dependencies must not be treated as independent merely because they are separate nodes.

Shared ancestry, common assumptions, and causal coupling remain material.

---

# 52. Fast-Path Law

The AMOS v4.4 fast path does not bypass hierarchy.

Local reasoning may avoid broader coordination only when required conditions are established:

```text
DEPENDENCY_CLOSURE
∧
PROVENANCE_INDEPENDENCE
∧
SCOPE_COMPATIBILITY
∧
REGIME_COMPATIBILITY
∧
FRESHNESS
∧
NON_CONFLICT
∧
AUTHORITY_COMPATIBILITY
```

Fast path means:

```text
SMALLER SUFFICIENT PROOF
```

not:

```text
WEAKER LAW
```

---

# 53. Proof-Based Coordination Avoidance

Coordination may be avoided only when independence is demonstrated.

```text
PROVEN_LOCAL_INDEPENDENCE
→
LOCAL_FINALIZATION_MAY_BE_ALLOWED
```

but:

```text
ASSUMED_INDEPENDENCE
↛
LOCAL_FINALIZATION
```

Authority hierarchy remains applicable even when coordination is unnecessary.

---

# 54. Causal Epoch Finality

A causal epoch cannot be considered final merely because execution has completed.

Finality requires relevant dependency closure under its governing contract.

```text
EXECUTION_COMPLETE
!=
CAUSAL_FINALITY
```

Material unresolved upstream dependencies may block finality.

---

# 55. Law Conflict States

Law resolution uses:

```text
NO_CONFLICT
SPECIALIZATION
EXCEPTION
OVERRIDE
SUPERSEDED
COMPETING
UNKNOWN/GAP
INVALID
```

Do not collapse these into a binary valid/invalid model.

---

# 56. Conflict Record

```yaml
law_conflict:
  conflict_id:

  law_a:
  law_b:

  scope:
  regime:
  time:

  conflict_type:
    - apparent
    - direct
    - scope
    - regime
    - version
    - authority
    - provenance
    - interpretation

  precedence_result:

  evidence: []

  unresolved_questions: []

  authority_required:

  resolution:

  provenance:
```

---

# 57. Promotion Hierarchy

Artifacts should not jump directly from existence to canon.

Conceptually:

```text
PLACEHOLDER
↓
SOURCE_CLAIM
↓
MODEL / PROPOSED
↓
REVIEWED
↓
VALIDATED
↓
CANON_CANDIDATE
↓
ACTIVE_CANON
```

Exact lifecycle vocabulary may differ by registry.

The governing invariant is:

```text
EXISTS != CANONICAL
```

---

# 58. Demotion

A law may move downward in authority state if:

```text
PROVENANCE FAILS
VALIDATION FAILS
SCOPE CHANGES
REGIME CHANGES
CONTRADICTION EMERGES
AUTHORITY IS REVOKED
SUPERSESSION OCCURS
```

Demotion should preserve lineage.

---

# 59. Law Invalidation

Invalidation should identify:

```text
FAILED PREMISE
FAILED PROVENANCE EDGE
FAILED AUTHORITY
SCOPE FAILURE
REGIME FAILURE
VERSION FAILURE
SUPERSESSION
CONTRADICTION
```

Dependent conclusions are then invalidated selectively.

```text
INVALIDATE DESCENDANTS
PRESERVE UNAFFECTED BRANCHES
```

---

# 60. Rollback

When a law transition fails:

```text
FAILED LAW STATE
↓
NEAREST VALID PREDECESSOR
```

where safe and supported by provenance.

Global rollback is a last resort when local dependency repair is insufficient.

---

# 61. Anti-Regression Gate

A law change must not weaken:

```text
FACTUAL SUPPORT
SCOPE CORRECTNESS
CONTRADICTION VISIBILITY
PROVENANCE RECOVERABILITY
CAUSAL DISCIPLINE
AUTHORITY INTEGRITY
SAFETY
RECOVERY
```

A performance improvement is insufficient justification for integrity regression.

---

# 62. Change Proposal Contract

```yaml
law_change_proposal:
  proposal_id:

  target_law:
  current_version:
  proposed_version:

  change_type:
    - clarification
    - extension
    - restriction
    - correction
    - breaking_change
    - deprecation
    - supersession

  rationale:

  evidence: []

  affected_invariants: []
  affected_dependencies: []
  affected_planes: []

  scope_effect:
  regime_effect:
  authority_effect:

  backward_compatibility:

  migration_plan:
  rollback_plan:

  proposed_by:
  required_authority:

  status:
```

Hard rule:

```text
LAW_CHANGE_PROPOSAL
!=
LAW_CHANGE_COMMIT
```

---

# 63. Law Commit Gate

Conceptually:

```text
PROPOSAL
↓
PROVENANCE CHECK
↓
DEPENDENCY CHECK
↓
CONFLICT CHECK
↓
SCOPE / REGIME CHECK
↓
INVARIANT CHECK
↓
AUTHORITY CHECK
↓
VALIDATION
↓
COMMIT
↓
SUPERSESSION RECORD
↓
DEPENDENT REVALIDATION
```

Any load-bearing:

```text
FAIL
```

blocks promotion.

Material:

```text
UNKNOWN/GAP
```

blocks promotion unless governing canon explicitly permits a conditional state.

---

# 64. Authoritative State

The repository may contain many artifacts describing law.

Only the authoritative-state mechanism should determine which are currently treated as governing.

Relevant root artifact:

```text
AUTHORITATIVE_STATE
```

Therefore:

```text
PRESENT_IN_REPOSITORY
!=
CURRENTLY_AUTHORITATIVE
```

---

# 65. Law Registry Requirements

A mature law registry should eventually track:

```yaml
law:
  law_id:
  semantic_id:
  title:

  version:
  lifecycle_state:

  authority_level:
  authority_type:

  statement:

  scope:
  regime:

  parent_laws: []
  child_laws: []

  invariants: []

  exceptions: []
  overrides: []

  supersedes: []
  superseded_by:

  effective_from:
  effective_until:

  provenance:

  validation:

  dependencies: []

  enforcement_points: []

  failure_semantics:
```

---

# 66. Minimum AMOS Hierarchy Laws

The minimum hierarchy set is:

```text
LH-001  INTEGRITY DOMINATES OPTIMIZATION
LH-002  HIGHER AUTHORITY CONSTRAINS LOWER AUTHORITY
LH-003  CAPABILITY != AUTHORITY
LH-004  PROPOSAL != COMMIT
LH-005  MODEL != AUTHORITY
LH-006  MEMORY != CANON
LH-007  KNOWLEDGE != AUTHORITY
LH-008  TOOL != PERMISSION
LH-009  RUNTIME != CANON
LH-010  IMPLEMENTATION != LAW
LH-011  SPECIFICITY DOES NOT BYPASS HIGHER LAW
LH-012  VERSION NUMBER ALONE DOES NOT ESTABLISH SUPERSESSION
LH-013  PLACEMENT DOES NOT ALONE ESTABLISH AUTHORITY
LH-014  UNKNOWN AUTHORITY != AUTHORIZED
LH-015  UNKNOWN/GAP != PASS
LH-016  SUPERSEDED != DELETED
LH-017  INVALIDATE DEPENDENTS, PRESERVE UNAFFECTED BRANCHES
LH-018  FAST PATH != WEAKER GOVERNANCE
LH-019  OVERRIDE REQUIRES EXPLICIT AUTHORITY
LH-020  LAW EVOLUTION MUST PRESERVE PROVENANCE
```

---

# 67. AMOS v4.4 Evolution Alignment

The law hierarchy supports the v3.0 → v4.4 evolution spine:

```text
DETERMINISTIC LOGIC
↓
RECURSIVE RSCF / H-M-L
↓
GOVERNED EVOLUTION
↓
CAUSAL LINEAGE
↓
EPISTEMIC REGIMES
↓
COMPETING HYPOTHESES
↓
PROVENANCE TOPOLOGY
↓
SYBIL HARDENING
↓
PERSISTENT PROVENANCE
↓
VERSION-AWARE STATE
↓
MVCC / CAS CONCEPTS
↓
ATOMIC MULTI-RSCF REASONING
↓
CAUSAL EPOCH FINALITY
↓
HARDENED SHARD-LOCAL FINALIZATION
↓
PROOF-BASED COORDINATION AVOIDANCE
```

The hierarchy constrains these mechanisms through governance and authority boundaries.

It does not claim that repository documentation alone proves their complete runtime implementation.

---

# 68. RSCF Node

```yaml
node_id: AMOS_LAW_HIERARCHY

functional_type:
  - CANONICAL_GOVERNANCE_MODEL
  - AUTHORITY_HIERARCHY
  - PRECEDENCE_MODEL

lifecycle_stage:
  CANON_CANDIDATE

origin_architect:
  Trang Phan

steward:
  Trang Phan

amos_core_target:
  v4.4

claim_class:
  AMOS_MODEL

claim: >
  AMOS law is governed through typed authority, scope, regime,
  precedence, provenance, versioning, conflict resolution,
  exception, override, and supersession relationships rather than
  filename order or runtime implementation alone.

dependencies:
  - "AMOS_CORE_LAWS"
  - "INVARIANT_REGISTRY"
  - "CANON_MAP"
  - "AUTHORITATIVE_STATE"
  - "ARCHITECTURE"

critical_invariants:
  - INTEGRITY > COMPLETENESS
  - UNKNOWN/GAP != PASS
  - CAPABILITY != AUTHORITY
  - PROPOSAL != COMMIT
  - MODEL != AUTHORITY
  - MEMORY != CANON
  - TOOL != PERMISSION
  - RUNTIME != CANON
  - IMPLEMENTATION != LAW
  - SUPERSEDED != DELETED
  - OPTIMIZATION MUST NOT WEAKEN INTEGRITY

does_not_establish:
  - implementation completeness
  - empirical validation of all laws
  - universal formal correctness
  - automatic authority of every referenced artifact
  - automatic promotion to final canon
```

---

# 69. Promotion Gate

This artifact may move:

```text
ACTIVE_CANON_CANDIDATE
→
ACTIVE_CANON
```

only after canonical review establishes:

```text
AUTHORITY MODEL
PRECEDENCE MODEL
SCOPE MODEL
REGIME MODEL
EXCEPTION MODEL
OVERRIDE MODEL
SUPERSESSION MODEL
VERSION MODEL
PROVENANCE MODEL
CONFLICT MODEL
DEPENDENCY CLOSURE
INVARIANT ALIGNMENT
```

Any unresolved load-bearing contradiction remains:

```text
COMPETING
```

or:

```text
UNKNOWN/GAP
```

rather than being silently normalized.

---

# 70. Changelog

## v2.0.0 — 2026-08-25

Expanded placeholder into an AMOS v4.4 law-hierarchy model.

Added:

- constitutional authority stack;
- L0–L9 hierarchy;
- typed authority;
- scoped authority;
- precedence semantics;
- conflict-resolution protocol;
- specificity and specialization rules;
- exception contracts;
- override contracts;
- supersession semantics;
- semantic identity firewall;
- version and temporal precedence;
- regime and scope firewalls;
- provenance topology;
- plane authority boundaries;
- RSCF law binding;
- multi-RSCF authority;
- fast-path governance;
- proof-based coordination avoidance;
- causal epoch finality;
- promotion/demotion;
- selective invalidation;
- rollback;
- anti-regression;
- law-change proposal and commit gates;
- authoritative-state separation;
- minimum hierarchy-law registry.

## v1.0.0 — 2026-08-25

Initial placeholder reserved the canonical AMOS OS location.

---

# 71. Final Law

The AMOS law hierarchy reduces to one governing constraint:

```text
NO LOWER-AUTHORITY COMPONENT
MAY SILENTLY REDEFINE
A HIGHER-AUTHORITY LAW.
```

A legitimate change requires:

```text
VALID PROPOSAL
+
VALID PROVENANCE
+
DEPENDENCY CLOSURE
+
SCOPE / REGIME COMPATIBILITY
+
INVARIANT SATISFACTION
+
REQUIRED AUTHORITY
+
VALIDATION
+
EXPLICIT COMMIT
+
SUPERSESSION LINEAGE
```

Therefore:

```text
IMPLEMENTATION
!=
LAW

EXECUTION
!=
AUTHORITY

REPETITION
!=
CANON

NEWER
!=
SUPERSEDING

CAPABILITY
!=
AUTHORITY

PROPOSAL
!=
COMMIT
```

and when governing authority cannot be established:

```text
UNKNOWN/GAP
!=
PASS
```

---

**Related:** README|AMOS OS · 00_ROOT_MOC|MOC · ARCHITECTURE|Architecture · SYSTEM_MAP|System Map · AUTHORITATIVE_STATE|Authoritative State · PLACEMENT_RULES|Placement Rules · 00_ROOT_NAMING_STANDARD|Naming Standard · AMOS Canon · CANON_MAP|Canon Map · [[AMOS_CORE_LAWS|AMOS Core Laws]] · INVARIANT_REGISTRY|Invariant Registry · KERNEL_MAP|Kernel Map · CONTROL_PLANE_MAP|Control Plane Map · RUNTIME_MAP|Runtime Map · MEMORY_MEMORY_MAP|Memory Map · [[AMOS_FULL_BRAIN_OS_ARCHITECTURE|AMOS Full Brain OS Architecture]] · STATE_STATE_MAP|State Map · SCHEMA_MAP|Schema Map · OBSERVABILITY_OBSERVABILITY_MAP|Observability Map · SECURITY_MAP|Security Map · TEST_MAP|Tests · OPERATIONS_MAP|Operations

```
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: law_hierarchy
node_type: note
path: 01_CANON/01_CORE_LAWS/LAW_HIERARCHY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[01_CORE_LAWS_MOC]]
