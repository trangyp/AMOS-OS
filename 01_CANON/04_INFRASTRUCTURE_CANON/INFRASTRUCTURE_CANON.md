---
artifact_id: AMOS-INFRASTRUCTURE-CANON
name: INFRASTRUCTURE_CANON
title: "AMOS Infrastructure Canon — Substrate, Resource, Deployment, Resilience, and Operational Foundations"

document_version: "2.0.0"
canon_version: "4.4"
amos_core_target: "v4.4"

status: ACTIVE_CANON_CANDIDATE
conclusion_class: AMOS_MODEL
rscf_state: derived

canon_group: infrastructure
canon_type: infrastructure-canon

origin_architect: Trang Phan
steward: Trang Phan

created: 2026-08-25
updated: 2026-08-25

tags:
  - amos
  - amos-os
  - amos-core
  - amos-core-v4-4
  - infrastructure
  - substrate
  - compute
  - storage
  - network
  - deployment
  - runtime
  - resilience
  - availability
  - durability
  - resource-governance
  - topology
  - isolation
  - fault-domain
  - persistence
  - state
  - provenance
  - observability
  - security
  - recovery
  - rollback
  - rscf
  - causal-lineage
  - canon-group/infrastructure
  - canon/framework
  - canon/model
  - rscf/claim
  - rscf/provenance
  - rscf/state/derived
  - topic/infrastructure-canon

aliases:
  - AMOS Infrastructure Canon
  - Infrastructure Canon
  - AMOS Infrastructure Foundation
  - AMOS Operational Substrate Canon
---

# AMOS Infrastructure Canon

**Origin architect / steward:** Trang Phan

> **Status:** `ACTIVE_CANON_CANDIDATE`  
> **AMOS Core target:** `v4.4`  
> **Conclusion class:** `AMOS_MODEL`

---

# 0. Purpose

The **AMOS Infrastructure Canon** defines the architectural rules governing the physical, virtual, computational, storage, network, deployment, and operational substrates upon which AMOS OS components may execute.

It establishes the boundary between:

```text
LOGICAL SYSTEM ARCHITECTURE
```

and:

```text
EXECUTION SUBSTRATE
```

The infrastructure layer provides capabilities.

It does not acquire authority merely by providing those capabilities.

Canonical law:

```text
INFRASTRUCTURE != AUTHORITY
```

Supporting law:

```text
CAPABILITY != AUTHORITY
```

---

# 1. Architectural Position

AMOS OS separates logical authority from execution substrate.

```text
CANON
↓
KERNEL
↓
CONTROL PLANE
↓
RUNTIME
↓
COGNITIVE ORGANISM
↓
AGENTS / SKILLS / WORKFLOWS
↓
TOOLS / MODELS / DOMAIN ADAPTERS
↓
EXTERNAL EFFECTS
```

Infrastructure exists beneath and across these logical planes as an enabling substrate.

Conceptually:

```text
                    AMOS OS
                       │
       ┌───────────────┼───────────────┐
       │               │               │
    COMPUTE          STORAGE         NETWORK
       │               │               │
       └───────────────┼───────────────┘
                       │
                 INFRASTRUCTURE
                       │
                 HOST ENVIRONMENT
```

Infrastructure must not silently redefine higher-level canon.

---

# 2. Infrastructure Boundary

```text
INFRASTRUCTURE != CANON

INFRASTRUCTURE != KERNEL

INFRASTRUCTURE != CONTROL_PLANE

INFRASTRUCTURE != RUNTIME

INFRASTRUCTURE != COGNITION

INFRASTRUCTURE != AUTHORITY

INFRASTRUCTURE != KNOWLEDGE

INFRASTRUCTURE != MEMORY

INFRASTRUCTURE != STATE
```

Infrastructure may host these components.

Hosting does not make them equivalent.

---

# 3. Core Infrastructure Law

```text
RESOURCE AVAILABILITY
!=
PERMISSION TO USE RESOURCE
```

Therefore:

```text
RESOURCE EXISTS
↓
RESOURCE DISCOVERED
↓
CAPABILITY IDENTIFIED
↓
AUTHORITY CHECKED
↓
POLICY CHECKED
↓
RESOURCE ALLOCATED
↓
WORK EXECUTED
```

not:

```text
RESOURCE EXISTS
↓
USE RESOURCE
```

---

# 4. Infrastructure Domains

The infrastructure canon conceptually covers:

```text
COMPUTE

STORAGE

NETWORK

PROCESS ISOLATION

CONTAINERIZATION

VIRTUALIZATION

RESOURCE SCHEDULING

DEPLOYMENT

SERVICE DISCOVERY

CONFIGURATION

SECRETS DELIVERY

PERSISTENCE

BACKUP

RESTORE

FAILURE DOMAINS

RESILIENCE

CAPACITY

SCALING

OBSERVABILITY SUBSTRATE

SECURITY SUBSTRATE

EXTERNAL CONNECTIVITY
```

Exact implementations remain environment-specific.

---

# 5. H/M/L Infrastructure Decomposition

Infrastructure should support AMOS fractal decomposition.

```text
H — INFRASTRUCTURE DOMAIN
↓
M — INFRASTRUCTURE SUBSYSTEM
↓
L — RESOURCE / COMPONENT
```

Example:

```text
H: STORAGE
↓
M: AUTHORITATIVE STATE STORAGE
↓
L: SPECIFIC STORE / VOLUME / OBJECT / SHARD
```

Another example:

```text
H: COMPUTE
↓
M: RUNTIME WORKER POOL
↓
L: WORKER INSTANCE
```

The H/M/L model is architectural organization, not proof that a particular deployment implements these exact layers.

---

# 6. Infrastructure Topology

Conceptual topology:

```text
INFRASTRUCTURE
├── COMPUTE
├── STORAGE
├── NETWORK
├── RESOURCE CONTROL
├── ISOLATION
├── DEPLOYMENT
├── PERSISTENCE
├── RESILIENCE
├── SECURITY
├── OBSERVABILITY
└── RECOVERY
```

Each branch may recursively decompose.

---

# 7. Compute Substrate

Compute provides execution capacity for:

```text
KERNEL OPERATORS

CONTROL-PLANE SERVICES

RUNTIME WORKERS

COGNITIVE COMPONENTS

AGENTS

SKILLS

WORKFLOWS

MODELS

TOOLS

INTERFACES

OBSERVABILITY SERVICES
```

Compute capacity does not imply authorization to execute arbitrary work.

---

# 8. Compute Identity

Every consequential compute unit should eventually have a distinguishable identity.

Conceptually:

```yaml
compute_unit:
  resource_id:
  resource_type:
  environment:
  trust_domain:
  fault_domain:
  runtime_class:
  capabilities: []
  authority_scope: []
  lifecycle_state:
  provenance:
```

Identity and authority remain separate.

```text
RESOURCE_IDENTITY != RESOURCE_AUTHORITY
```

---

# 9. Compute Classes

Possible conceptual classes:

```text
CONTROL-PLANE COMPUTE

RUNTIME COMPUTE

COGNITIVE COMPUTE

MODEL COMPUTE

AGENT COMPUTE

TOOL COMPUTE

BATCH COMPUTE

BACKGROUND COMPUTE

TEST COMPUTE

RECOVERY COMPUTE
```

These classes describe functional placement.

They do not assert a specific deployment topology.

---

# 10. Resource Isolation

Components with different trust, authority, failure, or workload characteristics should not be assumed safe to colocate.

Isolation dimensions may include:

```text
PROCESS

CONTAINER

VIRTUAL MACHINE

HOST

NETWORK

STORAGE

CREDENTIAL

IDENTITY

TENANT

FAULT DOMAIN

SECURITY DOMAIN
```

Required isolation depends on risk and implementation evidence.

---

# 11. Isolation Firewall

```text
LOGICAL SEPARATION
!=
PHYSICAL ISOLATION
```

and:

```text
PROCESS SEPARATION
!=
SECURITY ISOLATION
```

and:

```text
CONTAINERIZATION
!=
PROVEN SECURITY BOUNDARY
```

No stronger infrastructure guarantee should be inferred without supporting evidence.

---

# 12. Storage Substrate

Storage may support:

```text
CANON ARTIFACTS

CONFIGURATION

AUTHORITATIVE STATE

WORKING STATE

MEMORY

KNOWLEDGE

RSCFS

GMEFS

PROVENANCE

LOGS

TRACES

CHECKPOINTS

BACKUPS

MODEL ARTIFACTS

TEST EVIDENCE
```

These categories must not be silently conflated.

---

# 13. Storage Firewall

```text
STORED
!=
AUTHORITATIVE
```

```text
PERSISTED
!=
CANONICAL
```

```text
AVAILABLE
!=
CURRENT
```

```text
BACKED UP
!=
VALIDATED
```

```text
REPLICATED
!=
INDEPENDENTLY PROVEN
```

---

# 14. Persistence Boundary

Persistence describes survival across a defined lifecycle boundary.

Examples:

```text
REQUEST

PROCESS

SESSION

RUNTIME

HOST

DEPLOYMENT

REGION

SYSTEM LIFETIME
```

A claim of persistence must specify the boundary.

```text
PERSISTENT
```

without a scope is incomplete.

---

# 15. Durability Boundary

```text
PERSISTENCE != DURABILITY
```

Persistence means data survives a particular lifecycle transition.

Durability concerns resistance to loss under specified failure conditions.

Therefore:

```text
DURABLE
```

must inherit a failure envelope.

---

# 16. Authoritative State Storage

Authoritative state must remain distinguishable from:

```text
CACHE

REPLICA

SHADOW STATE

WORKING STATE

RECOVERY STATE

CHECKPOINT

DERIVED VIEW
```

Canonical rule:

```text
COPY OF AUTHORITATIVE STATE
!=
AUTHORITATIVE STATE
```

unless authority is explicitly transferred or established.

---

# 17. State Identity

Consequential state should conceptually preserve:

```yaml
state_identity:
  state_id:
  state_class:
  version:
  authority:
  scope:
  regime:
  causal_epoch:
  provenance:
  created_at:
  supersedes:
  validity_conditions: []
```

---

# 18. Storage Versioning

Infrastructure storage must not silently erase semantic version identity.

Canonical firewall:

```text
FILE VERSION
!=
STATE VERSION
!=
CANON VERSION
!=
SCHEMA VERSION
!=
RUNTIME VERSION
```

A storage revision may contain a semantic change, but the two identities remain distinct.

---

# 19. MVCC Infrastructure Support

AMOS Core v4.4 includes MVCC concepts.

Infrastructure may support state-version isolation such as:

```text
READ V42
↓
PROCESS
↓
ATTEMPT WRITE AGAINST V42
```

If current authoritative state remains:

```text
V42
```

the transition may continue.

If it becomes:

```text
V43
```

the caller must not silently overwrite the newer state.

---

# 20. CAS Infrastructure Support

Conceptual compare-and-swap:

```text
EXPECTED
=
CURRENT
↓
WRITE MAY PROCEED
```

otherwise:

```text
EXPECTED
!=
CURRENT
↓
CONFLICT
```

Infrastructure may provide primitives supporting this pattern.

This canon does not claim a specific implementation exists.

---

# 21. Atomicity Boundary

Atomicity must be explicitly scoped.

Possible scopes:

```text
SINGLE OBJECT

SINGLE STATE UNIT

SINGLE RSCF

MULTI-RSCF

SINGLE SHARD

MULTI-SHARD

SINGLE SERVICE

CROSS-SERVICE
```

Canonical rule:

```text
ATOMIC LOCALLY
!=
ATOMIC GLOBALLY
```

---

# 22. Multi-RSCF Infrastructure

Where atomic multi-RSCF reasoning requires persistent coordination, infrastructure must preserve the relevant dependency relationship.

Conceptually:

```text
RSCF A
RSCF B
RSCF C
   │
   ↓
ATOMIC DECISION BOUNDARY
```

Infrastructure must not expose partial persistence as successful composite finalization where all components are load-bearing.

---

# 23. Network Substrate

Network infrastructure enables communication between:

```text
CONTROL-PLANE COMPONENTS

RUNTIME COMPONENTS

WORKERS

AGENTS

TOOLS

MODELS

STORAGE

INTERFACES

EXTERNAL SYSTEMS
```

Connectivity is capability.

```text
NETWORK REACHABILITY
!=
AUTHORIZATION
```

---

# 24. Network Trust Firewall

```text
REACHABLE
!=
TRUSTED
```

```text
INTERNAL
!=
SAFE
```

```text
ENCRYPTED
!=
AUTHORIZED
```

```text
AUTHENTICATED
!=
AUTHORIZED FOR EVERY ACTION
```

Trust remains local and typed.

---

# 25. Network Dependency

Network dependencies should be represented where they can alter correctness.

Conceptually:

```text
SERVICE A
↓
NETWORK EDGE
↓
SERVICE B
```

If B is load-bearing for A:

```text
NETWORK FAILURE
```

may invalidate or defer A's operation.

---

# 26. Partial Failure

Distributed infrastructure must assume partial failure is possible.

Conceptually:

```text
NODE A = HEALTHY
NODE B = FAILED
NODE C = DEGRADED
NETWORK A↔C = PARTITIONED
```

Therefore:

```text
SYSTEM RESPONDING
!=
SYSTEM FULLY HEALTHY
```

---

# 27. Fault Domains

Infrastructure should explicitly model fault domains where consequential.

Possible domains:

```text
PROCESS

HOST

RACK

ZONE

REGION

NETWORK SEGMENT

STORAGE SYSTEM

CREDENTIAL DOMAIN

PROVIDER

DEPENDENCY SERVICE
```

Independence between replicas or workers must not be assumed merely because identifiers differ.

---

# 28. Correlated Failure

Canonical law:

```text
MULTIPLE INSTANCES
!=
MULTIPLE INDEPENDENT FAILURE DOMAINS
```

Example:

```text
INSTANCE A ─┐
INSTANCE B ─┼→ SAME HOST
INSTANCE C ─┘
```

These instances share host-level failure ancestry.

---

# 29. Provenance Topology Applied to Infrastructure

Infrastructure redundancy should use the same independence discipline as evidence provenance.

```text
REPLICA COUNT
!=
INDEPENDENT FAILURE COUNT
```

A topology may contain:

```text
N LOGICAL COPIES
```

but only:

```text
M INDEPENDENT FAILURE DOMAINS
```

where:

```text
M <= N
```

---

# 30. Resource Provenance

Consequential infrastructure resources should eventually preserve provenance such as:

```yaml
resource_provenance:
  resource_id:
  created_by:
  creation_process:
  configuration_source:
  image_or_artifact:
  version:
  hash:
  environment:
  parent_resources: []
  deployment_record:
  last_verified:
```

Missing fields remain `UNKNOWN/GAP`.

---

# 31. Artifact Integrity

Executable or load-bearing artifacts should eventually support integrity verification.

Conceptually:

```text
ARTIFACT
↓
IDENTITY
↓
VERSION
↓
HASH / DIGEST
↓
PROVENANCE
↓
VALIDATION
↓
LOAD
```

A filename alone is insufficient proof of identity.

---

# 32. Infrastructure Identity Firewall

```text
FILENAME
!=
ARTIFACT ID

ARTIFACT ID
!=
RESOURCE ID

RESOURCE ID
!=
DEPLOYMENT ID

DEPLOYMENT ID
!=
SEMANTIC VERSION

SEMANTIC VERSION
!=
HASH
```

These may be linked but must not be silently collapsed.

---

# 33. Configuration

Infrastructure configuration is operational state.

```text
CONFIGURATION
!=
CANON
```

Canon may constrain configuration.

Configuration realizes a particular environment-specific choice.

---

# 34. Configuration Provenance

Consequential configuration should eventually preserve:

```text
SOURCE

VERSION

AUTHOR / AUTHORITY

TARGET

ENVIRONMENT

EFFECTIVE TIME

SUPERSESSION

ROLLBACK TARGET
```

Configuration without provenance should not automatically be treated as authoritative.

---

# 35. Configuration Drift

Conceptually:

```text
EXPECTED CONFIGURATION
!=
OBSERVED CONFIGURATION
```

means:

```text
DRIFT
```

Drift should become observable when it can materially affect system correctness or security.

---

# 36. Environment Identity

Infrastructure decisions inherit environment.

Examples:

```text
DEVELOPMENT

TEST

STAGING

PRODUCTION

RECOVERY

SIMULATION

SANDBOX
```

Canonical firewall:

```text
VALID IN TEST
!=
VALID IN PRODUCTION
```

---

# 37. Environment Promotion

Promotion should conceptually follow:

```text
ARTIFACT
↓
TEST
↓
VALIDATION
↓
APPROVAL
↓
PROMOTION
↓
DEPLOYMENT
↓
OBSERVATION
```

Existence in one environment does not automatically authorize promotion to another.

---

# 38. Deployment

Deployment is the realization of an approved artifact/configuration into an environment.

```text
BUILD
!=
DEPLOYMENT

DEPLOYMENT
!=
ACTIVATION

ACTIVATION
!=
VALIDATION
```

---

# 39. Deployment Envelope

A consequential deployment should eventually carry:

```yaml
deployment:
  deployment_id:
  artifact:
  artifact_version:
  artifact_hash:
  target_environment:
  configuration:
  authority_ref:
  policy_ref:
  prior_deployment:
  rollback_target:
  health_gate:
  created_at:
```

---

# 40. Deployment Atomicity

Deployment atomicity must be scoped.

```text
ONE PROCESS
```

may be atomic while:

```text
MULTI-SERVICE SYSTEM
```

is not.

Do not infer system-wide atomicity from component-level deployment success.

---

# 41. Rollout Strategy

Infrastructure may support staged rollout patterns such as:

```text
CANARY

PHASED

BLUE/GREEN

SHADOW

READ-ONLY

LIMITED SCOPE

FEATURE-GATED
```

These are implementation strategies, not mandatory claims about current AMOS deployment.

---

# 42. Reversibility Preference

Under uncertainty, infrastructure changes should prefer:

```text
STAGED

REVERSIBLE

OBSERVABLE

BOUNDED

ROLLBACK-CAPABLE
```

where practical.

This follows AMOS action governance.

---

# 43. Rollback

Infrastructure rollback should restore the nearest valid recoverable deployment or state rather than blindly reverting everything.

Conceptually:

```text
BAD DEPLOYMENT
↓
IDENTIFY AFFECTED SCOPE
↓
FREEZE
↓
ROLL BACK LOCAL DEPENDENTS
↓
PRESERVE UNAFFECTED COMPONENTS
↓
REVALIDATE
```

---

# 44. Recovery

Canonical recovery pattern:

```text
DETECT
↓
ISOLATE
↓
IDENTIFY FAILURE DOMAIN
↓
PRESERVE VALID STATE
↓
RESTORE REQUIRED DEPENDENCIES
↓
REVALIDATE
↓
RESUME
```

---

# 45. No Blind Restart

```text
FAILED COMPONENT
+
UNCHANGED FAILURE CONDITION
=
DO NOT EXPECT RESTART TO SOLVE ROOT CAUSE
```

Restart may be a valid action only when its assumptions are justified.

---

# 46. Failure Locality

AMOS recovery law applies to infrastructure:

```text
FAILURE
↓
INVALIDATE AFFECTED RESOURCE / EDGE
↓
INVALIDATE DEPENDENTS
↓
PRESERVE UNAFFECTED INFRASTRUCTURE
```

Global teardown is a last resort.

---

# 47. Dependency Graph

Infrastructure should eventually expose load-bearing dependency relationships.

Example:

```text
API
↓
RUNTIME
↓
STATE STORE
↓
STORAGE
```

and:

```text
RUNTIME
↓
MODEL SERVICE
```

and:

```text
CONTROL PLANE
↓
AUTHORITY STORE
```

Dependency edges should be typed where material.

---

# 48. Dependency Types

Possible infrastructure dependency types:

```text
REQUIRED

OPTIONAL

DEGRADED-MODE

BOOTSTRAP

RUNTIME

PERSISTENCE

SECURITY

OBSERVABILITY

RECOVERY

NETWORK

CAPACITY
```

A dependency's existence alone does not specify its semantics.

---

# 49. Dependency Closure

Before declaring a service operational, load-bearing dependencies should be resolved sufficiently.

Conceptually:

```text
SERVICE
↓
REQUIRED DEPENDENCIES
↓
TRANSITIVE LOAD-BEARING DEPENDENCIES
↓
DEPENDENCY CLOSURE
```

Do not traverse unrelated infrastructure.

---

# 50. Health

Health is typed and scoped.

```text
PROCESS HEALTH

SERVICE HEALTH

DEPENDENCY HEALTH

DATA HEALTH

SECURITY HEALTH

CONTROL-PLANE HEALTH

NETWORK HEALTH

STORAGE HEALTH
```

Canonical firewall:

```text
PROCESS ALIVE
!=
SERVICE HEALTHY
```

---

# 51. Readiness

```text
ALIVE
!=
READY
```

A component may be running but unable to safely serve work.

Readiness should account for load-bearing dependencies.

---

# 52. Liveness

```text
READY
!=
LIVE
```

Liveness and readiness answer different questions.

Conceptually:

```text
LIVENESS:
CAN THE COMPONENT CONTINUE OPERATING?
```

```text
READINESS:
CAN THE COMPONENT SAFELY ACCEPT WORK?
```

---

# 53. Observability

Infrastructure observability should eventually expose:

```text
RESOURCE HEALTH

RESOURCE UTILIZATION

DEPENDENCY HEALTH

DEPLOYMENT STATE

ERRORS

LATENCY

THROUGHPUT

QUEUE DEPTH

STORAGE CAPACITY

NETWORK STATE

RESTARTS

FAILOVERS

ROLLBACKS

CONFIGURATION DRIFT

SECURITY EVENTS
```

Metrics must be interpreted within environment and workload scope.

---

# 54. Observability Firewall

```text
METRIC
!=
EXPLANATION
```

```text
ALERT
!=
ROOT CAUSE
```

```text
CORRELATION
!=
CAUSATION
```

Infrastructure telemetry is observation until stronger inference is justified.

---

# 55. Capacity

Capacity must be typed.

Possible dimensions:

```text
CPU

MEMORY

GPU

STORAGE

IOPS

BANDWIDTH

CONNECTIONS

QUEUE CAPACITY

REQUEST RATE

MODEL CONTEXT

WORKER COUNT
```

A single aggregate capacity number is usually insufficient.

---

# 56. Capacity Envelope

A capacity claim should specify:

```text
WORKLOAD

ENVIRONMENT

CONFIGURATION

HARDWARE

SOFTWARE VERSION

MEASUREMENT METHOD

TIME WINDOW

FAILURE CONDITIONS
```

Canonical law:

```text
BENCHMARK RESULT
!=
UNIVERSAL CAPACITY
```

---

# 57. Scaling

Scaling may be:

```text
VERTICAL

HORIZONTAL

FUNCTIONAL

SHARD-BASED

QUEUE-BASED

ELASTIC
```

Scaling increases resources.

It does not automatically improve correctness, availability, or independence.

---

# 58. Scaling Firewall

```text
MORE INSTANCES
!=
MORE INDEPENDENCE
```

```text
MORE COMPUTE
!=
MORE AUTHORITY
```

```text
MORE REPLICAS
!=
MORE TRUTH
```

```text
MORE CAPACITY
!=
LOWER RISK
```

---

# 59. Resource Governance

Resource allocation should remain governed.

Conceptually:

```text
REQUEST
↓
RESOURCE CLASS
↓
QUOTA / LIMIT
↓
POLICY
↓
AUTHORITY
↓
ALLOCATION
```

This prevents uncontrolled consumption from becoming implicit policy.

---

# 60. Resource Limits

Potential controls:

```text
CPU LIMIT

MEMORY LIMIT

GPU LIMIT

STORAGE LIMIT

NETWORK LIMIT

CONCURRENCY LIMIT

TIME LIMIT

REQUEST LIMIT

COST LIMIT
```

Limits should be explicit where exhaustion can affect system integrity.

---

# 61. Backpressure

Infrastructure should support bounded behavior under load.

Conceptually:

```text
INPUT RATE
>
SAFE PROCESSING RATE
↓
BACKPRESSURE
```

rather than:

```text
UNBOUNDED QUEUE GROWTH
```

where unbounded growth creates failure risk.

---

# 62. Load Shedding

Under constrained conditions, controlled rejection may be safer than uncontrolled collapse.

```text
OVERLOAD
↓
PRIORITIZE
↓
SHED NONCRITICAL WORK
↓
PRESERVE CRITICAL PATHS
```

Exact priority policy belongs to governance/control layers.

---

# 63. Availability

Availability is scoped.

A claim such as:

```text
HIGHLY AVAILABLE
```

requires an explicit failure and measurement envelope.

Potential dimensions:

```text
TIME WINDOW

REGION

DEPENDENCY SET

WORKLOAD

SERVICE LEVEL

FAILURE DOMAIN
```

---

# 64. Resilience

Resilience concerns the system's ability to preserve or recover required function under specified disturbance.

```text
RESILIENCE
!=
INVULNERABILITY
```

and:

```text
RECOVERY CAPABILITY
!=
NO FAILURE
```

---

# 65. Redundancy

Redundancy may improve resilience only when failure correlation is sufficiently controlled.

```text
REDUNDANCY
+
SHARED FAILURE DOMAIN
```

may provide less protection than apparent instance count suggests.

---

# 66. Replication

Replication may support:

```text
READ SCALE

FAILOVER

DURABILITY

LOCALITY

RECOVERY
```

but:

```text
REPLICATION
!=
BACKUP
```

and:

```text
REPLICATION
!=
INDEPENDENT PROVENANCE
```

---

# 67. Backup

Backup should be treated as a recovery artifact.

```text
BACKUP EXISTS
!=
BACKUP RESTORABLE
```

Therefore restore validation is required before strong recoverability claims.

---

# 68. Restore

A restore process should conceptually validate:

```text
BACKUP IDENTITY

INTEGRITY

VERSION

SCHEMA COMPATIBILITY

DEPENDENCY COMPATIBILITY

AUTHORITY

TARGET ENVIRONMENT

RESTORED STATE
```

---

# 69. Recovery Point and Recovery Time

Where relevant, infrastructure may define:

```text
RPO
=
ACCEPTABLE DATA LOSS WINDOW
```

```text
RTO
=
ACCEPTABLE RECOVERY TIME TARGET
```

These remain operational targets until validated by evidence.

---

# 70. Disaster Recovery

Disaster recovery should eventually define:

```text
FAILURE SCENARIOS

RECOVERY AUTHORITY

BACKUP SOURCES

RESTORE ORDER

DEPENDENCY ORDER

ALTERNATE INFRASTRUCTURE

COMMUNICATION PATH

VALIDATION TESTS

RETURN-TO-NORMAL PROCEDURE
```

A document alone does not prove disaster recovery capability.

---

# 71. Security Substrate

Infrastructure provides security-enabling primitives such as:

```text
IDENTITY

CREDENTIAL STORAGE

SECRET DELIVERY

NETWORK SEGMENTATION

ENCRYPTION

ACCESS CONTROL

AUDIT LOGGING

ISOLATION

PATCHING

ARTIFACT INTEGRITY
```

But:

```text
SECURITY CAPABILITY
!=
SECURITY POLICY
```

Policy and authority remain governed separately.

---

# 72. Secret Handling

Secrets should remain distinct from ordinary configuration.

```text
SECRET
!=
CONFIGURATION
```

Consequential secret systems should eventually support:

```text
SCOPED ACCESS

ROTATION

REVOCATION

AUDITABILITY

MINIMUM EXPOSURE

LIFETIME CONTROL
```

---

# 73. Least Privilege

Infrastructure permissions should be bounded to the smallest sufficient scope.

Conceptually:

```text
REQUIRED CAPABILITY
↓
MINIMUM RESOURCE
↓
MINIMUM ACTION SET
↓
MINIMUM DURATION
```

This is an architectural principle, not proof of implementation.

---

# 74. External Connectivity

External infrastructure edges are trust-boundary crossings.

Examples:

```text
INTERNET

CLOUD API

MODEL PROVIDER

DATABASE

MCP SERVER

SAAS CONNECTOR

USER DEVICE

THIRD-PARTY TOOL
```

Every external edge should be treated as independently governed where consequential.

---

# 75. External Dependency Firewall

```text
EXTERNAL SERVICE AVAILABLE
!=
EXTERNAL SERVICE TRUSTED
```

```text
API RESPONSE
!=
VERIFIED FACT
```

```text
THIRD-PARTY SLA
!=
AMOS GUARANTEE
```

---

# 76. Infrastructure Provenance and RSCF

Infrastructure observations may enter RSCFs as:

```text
OBSERVATION
```

Examples:

```text
NODE UNAVAILABLE

DISK CAPACITY 91%

DEPLOYMENT HASH X

NETWORK EDGE FAILED

SERVICE LATENCY Y
```

Interpretation remains separate:

```text
OBSERVATION
↓
DERIVED CLAIM
↓
DECISION
```

---

# 77. Evidence Typing

Infrastructure evidence should distinguish:

```text
SOURCE_CLAIM

OBSERVATION

DERIVED

MODEL

DECISION

UNKNOWN
```

For example:

```text
"Provider guarantees 99.99%"
=
SOURCE_CLAIM
```

until the claim's status and applicability are independently established.

---

# 78. Freshness

Infrastructure state is often highly time-sensitive.

```text
HEALTHY AT T1
!=
HEALTHY AT T2
```

Therefore infrastructure observations require freshness bounds appropriate to their use.

---

# 79. Regime Awareness

Infrastructure behavior may change across regimes such as:

```text
NORMAL LOAD

PEAK LOAD

DEGRADED MODE

NETWORK PARTITION

FAILOVER

RECOVERY

MAINTENANCE

SECURITY INCIDENT
```

A conclusion valid under normal operation may fail during another regime.

---

# 80. Causal Firewall

Infrastructure correlation must not be automatically interpreted as cause.

Example:

```text
CPU ↑
LATENCY ↑
```

does not alone prove:

```text
CPU CAUSED LATENCY
```

Potential alternatives include:

```text
QUEUE SATURATION

LOCK CONTENTION

NETWORK DELAY

STORAGE LATENCY

DOWNSTREAM FAILURE

COMMON LOAD DRIVER
```

---

# 81. Sensitivity

For consequential infrastructure decisions, identify the smallest condition capable of changing the decision.

Examples:

```text
FREE STORAGE THRESHOLD

LATENCY THRESHOLD

ERROR RATE

DEPENDENCY HEALTH

REPLICA COUNT

FAULT-DOMAIN COUNT

RESOURCE QUOTA

STATE VERSION
```

Test decision-flipping conditions first.

---

# 82. Causal Epoch Integration

Infrastructure may provide state and topology information used by causal epoch reasoning.

Conceptually:

```text
EPOCH E1
=
TOPOLOGY / STATE / DEPENDENCY CONDITIONS
```

If a material infrastructure transition creates:

```text
EPOCH E2
```

dependent conclusions may require revalidation.

---

# 83. Infrastructure and Local Finality

Shard-local finalization may depend on infrastructure guarantees such as:

```text
SHARD IDENTITY

STATE VERSION

LOCAL DURABILITY

DEPENDENCY AVAILABILITY

FAILURE DOMAIN

NETWORK VISIBILITY
```

Infrastructure can support finalization.

It does not independently define semantic finality.

---

# 84. Coordination Avoidance

Infrastructure should not force global coordination where proof establishes safe locality.

Conceptually:

```text
DISJOINT RESOURCES
+
DISJOINT MUTABLE STATE
+
NO SHARED INVARIANT
+
NO CROSS-DEPENDENCY
↓
LOCAL EXECUTION MAY PROCEED
```

This supports AMOS v4.4 proof-based coordination avoidance.

---

# 85. Coordination Escalation

Infrastructure coordination becomes necessary where operations share:

```text
MUTABLE STATE

RESOURCE LOCK

QUOTA

FAULT DOMAIN

NETWORK DEPENDENCY

STORAGE INVARIANT

CROSS-SHARD STATE

GLOBAL CONFIGURATION

SECURITY AUTHORITY
```

and the shared dependency is load-bearing.

---

# 86. Infrastructure Lifecycle

Conceptual resource lifecycle:

```text
DECLARED
↓
PROVISIONED
↓
CONFIGURED
↓
VALIDATED
↓
ACTIVE
↓
DEGRADED
↓
DRAINING
↓
RETIRED
↓
ARCHIVED / DESTROYED
```

Not every resource requires every state.

---

# 87. Provisioning

```text
PROVISIONED
!=
READY
```

A newly provisioned resource may still require:

```text
CONFIGURATION

IDENTITY

SECURITY

DEPENDENCY VALIDATION

HEALTH CHECK

REGISTRATION
```

before use.

---

# 88. Decommissioning

Resource retirement should preserve required lineage.

Conceptually:

```text
DRAIN
↓
REMOVE AUTHORITY
↓
MIGRATE REQUIRED STATE
↓
VERIFY DEPENDENTS
↓
REVOKE CREDENTIALS
↓
ARCHIVE REQUIRED PROVENANCE
↓
DESTROY
```

Deletion must not silently erase required audit history.

---

# 89. Infrastructure Registry

A future infrastructure registry should minimally track:

```yaml
resource:
  resource_id:
  resource_type:
  environment:
  lifecycle_state:
  trust_domain:
  fault_domain:
  dependencies: []
  capabilities: []
  authority_ref:
  configuration_ref:
  provenance_ref:
  health_ref:
  deployment_ref:
  created_at:
  updated_at:
```

---

# 90. Topology Registry

A topology registry should represent:

```text
RESOURCE NODES

DEPENDENCY EDGES

NETWORK EDGES

FAULT-DOMAIN MEMBERSHIP

TRUST-DOMAIN MEMBERSHIP

STATE OWNERSHIP

REPLICATION RELATIONSHIPS

RECOVERY RELATIONSHIPS
```

where these relationships materially affect system reasoning.

---

# 91. Infrastructure Invariants

```text
INF-001  INFRASTRUCTURE != AUTHORITY

INF-002  RESOURCE AVAILABILITY != PERMISSION

INF-003  REACHABILITY != TRUST

INF-004  STORED != AUTHORITATIVE

INF-005  PERSISTED != CANONICAL

INF-006  REPLICATION != BACKUP

INF-007  REPLICA COUNT != INDEPENDENT FAILURE COUNT

INF-008  LOGICAL ISOLATION != PROVEN SECURITY ISOLATION

INF-009  PROCESS ALIVE != SERVICE HEALTHY

INF-010  ALIVE != READY

INF-011  TEST VALIDITY != PRODUCTION VALIDITY

INF-012  DEPLOYED != VALIDATED

INF-013  BUILD != DEPLOYMENT

INF-014  DEPLOYMENT != ACTIVATION

INF-015  LOCAL ATOMICITY != GLOBAL ATOMICITY

INF-016  LOCAL DURABILITY != GLOBAL DURABILITY

INF-017  BACKUP EXISTS != BACKUP RESTORABLE

INF-018  MORE INSTANCES != MORE INDEPENDENCE

INF-019  MORE COMPUTE != MORE AUTHORITY

INF-020  NETWORK ENCRYPTION != AUTHORIZATION

INF-021  METRIC != EXPLANATION

INF-022  ALERT != ROOT CAUSE

INF-023  BENCHMARK RESULT != UNIVERSAL CAPACITY

INF-024  CONFIGURATION != CANON

INF-025  FILE VERSION != STATE VERSION

INF-026  RESOURCE ID != SEMANTIC VERSION

INF-027  FAILED RESOURCE INVALIDATES DEPENDENTS, NOT EVERYTHING

INF-028  RECOVERY MUST PRESERVE VALID UNAFFECTED STATE

INF-029  INFRASTRUCTURE OBSERVATIONS ARE FRESHNESS-BOUNDED

INF-030  OPTIMIZATION MUST NOT WEAKEN INTEGRITY
```

---

# 92. Infrastructure Failure Classes

Conceptual classes:

```text
COMPUTE_FAILURE

STORAGE_FAILURE

NETWORK_FAILURE

RESOURCE_EXHAUSTION

CONFIGURATION_FAILURE

DEPLOYMENT_FAILURE

DEPENDENCY_FAILURE

IDENTITY_FAILURE

AUTHORIZATION_FAILURE

SECRET_FAILURE

DATA_CORRUPTION

VERSION_CONFLICT

TOPOLOGY_FAILURE

OBSERVABILITY_FAILURE

BACKUP_FAILURE

RESTORE_FAILURE

CORRELATED_FAILURE

UNKNOWN_FAILURE
```

---

# 93. Failure Severity

Severity should depend on impact, not merely component type.

Conceptually:

```text
LOCAL

DEGRADED

SERVICE-AFFECTING

SYSTEM-AFFECTING

CRITICAL
```

Severity thresholds require operational definition.

---

# 94. Degraded Mode

Infrastructure may support degraded operation when:

```text
CRITICAL INVARIANTS HOLD
```

despite loss of noncritical capabilities.

Conceptually:

```text
FULL MODE
↓ failure
DEGRADED SAFE MODE
```

rather than uncontrolled partial behavior.

---

# 95. Fail Closed vs Fail Open

The correct failure posture depends on function.

Examples:

```text
AUTHORITY UNKNOWN
→ FAIL CLOSED
```

while some non-authoritative informational services may permit:

```text
DEGRADED READ
```

Exact behavior belongs to policy and risk classification.

---

# 96. Infrastructure Governance Boundary

Infrastructure components may enforce decisions.

They must not invent policy.

```text
CONTROL PLANE
↓
AUTHORIZED INFRASTRUCTURE ACTION
↓
INFRASTRUCTURE
↓
EXECUTION
```

Canonical law:

```text
ENFORCEMENT MECHANISM
!=
POLICY SOURCE
```

---

# 97. Runtime Boundary

```text
INFRASTRUCTURE
=
WHERE / ON WHAT EXECUTION OCCURS
```

```text
RUNTIME
=
HOW AUTHORIZED COMPUTATION IS ORCHESTRATED
```

The two interact but remain distinct.

---

# 98. Operations Boundary

```text
INFRASTRUCTURE
!=
OPERATIONS
```

Infrastructure is the substrate and its technical resource architecture.

Operations governs:

```text
RUNBOOKS

DEPLOYMENTS

INCIDENT RESPONSE

MAINTENANCE

SERVICE MANAGEMENT

RECOVERY PROCEDURES
```

---

# 99. Security Boundary

```text
INFRASTRUCTURE SECURITY PRIMITIVE
!=
SECURITY GOVERNANCE
```

Infrastructure may provide encryption or isolation.

Security architecture determines required protections, threat models, and policies.

---

# 100. Observability Boundary

```text
INFRASTRUCTURE TELEMETRY
!=
OBSERVABILITY GOVERNANCE
```

Infrastructure emits signals.

The observability plane defines collection, semantics, retention, correlation, and interpretation.

---

# 101. Minimum Infrastructure Contract

Every consequential AMOS infrastructure implementation should eventually define:

| Contract             | Requirement                           |
| -------------------- | ------------------------------------- |
| Resource identity    | Stable typed resource identity        |
| Environment identity | Explicit environment                  |
| Trust domain         | Security/trust placement              |
| Fault domain         | Correlated-failure placement          |
| Dependency map       | Load-bearing dependencies             |
| Configuration        | Versioned operational configuration   |
| Provenance           | Resource/artifact lineage             |
| Health               | Liveness/readiness semantics          |
| Capacity             | Resource envelope                     |
| Persistence          | Lifecycle survival semantics          |
| Durability           | Failure envelope                      |
| Backup               | Recovery source                       |
| Restore              | Tested recovery path                  |
| Rollback             | Nearest valid prior deployment        |
| Observability        | Health and transition evidence        |
| Security             | Identity/access/isolation integration |
| Lifecycle            | Provision-to-retirement states        |

---

# 102. Infrastructure Test Families

Expected test families include:

```text
RESOURCE IDENTITY TESTS

CONFIGURATION PROVENANCE TESTS

ARTIFACT HASH TESTS

DEPENDENCY CLOSURE TESTS

HEALTH CHECK TESTS

READINESS TESTS

LIVENESS TESTS

RESOURCE EXHAUSTION TESTS

BACKPRESSURE TESTS

NETWORK FAILURE TESTS

PARTITION TESTS

STORAGE FAILURE TESTS

STATE VERSION CONFLICT TESTS

MVCC TESTS

CAS TESTS

REPLICATION TESTS

FAULT-DOMAIN TESTS

CORRELATED FAILURE TESTS

BACKUP TESTS

RESTORE TESTS

ROLLBACK TESTS

DEPLOYMENT FAILURE TESTS

DEGRADED MODE TESTS

RECOVERY TESTS

SECRET ROTATION TESTS

AUTHORITY BYPASS TESTS

ENVIRONMENT ISOLATION TESTS

CONFIGURATION DRIFT TESTS

OBSERVABILITY FAILURE TESTS
```

---

# 103. Adversarial Infrastructure Tests

High-value adversarial scenarios:

```text
RESOURCE EXISTS AND IS USED WITHOUT AUTHORIZATION

TEST CONFIGURATION IS PROMOTED DIRECTLY TO PRODUCTION

REPLICAS SHARE ONE FAILURE DOMAIN BUT ARE COUNTED AS INDEPENDENT

BACKUP EXISTS BUT CANNOT BE RESTORED

STALE CONFIGURATION OVERRIDES NEWER STATE

RUNTIME WRITES AGAINST STALE VERSION

NETWORK REACHABILITY IS TREATED AS TRUST

INTERNAL SERVICE IS ASSUMED SAFE WITHOUT AUTHENTICATION

MODEL WORKLOAD EXHAUSTS CONTROL-PLANE RESOURCES

OBSERVABILITY FAILURE IS INTERPRETED AS SERVICE FAILURE

SERVICE PROCESS IS ALIVE BUT DEPENDENCY IS CORRUPT

ROLLBACK DESTROYS VALID NEWER STATE

DEPLOYMENT SUCCEEDS BUT HEALTH VALIDATION FAILS

LOCAL STORAGE ATOMICITY IS CLAIMED AS SYSTEM ATOMICITY

RESOURCE RESTART REPEATS UNCHANGED FAILURE PATH

REPLICA CORRUPTION PROPAGATES TO EVERY COPY

SECRET ROTATION LEAVES OLD AUTHORITY ACTIVE

RESOURCE DECOMMISSIONING ERASES REQUIRED PROVENANCE
```

---

# 104. Proof Obligations

Strong infrastructure claims require corresponding evidence.

Examples:

| Claim                | Minimum evidence class              |
| -------------------- | ----------------------------------- |
| Resource exists      | observation                         |
| Resource configured  | configuration evidence              |
| Resource healthy     | fresh health observation            |
| Resource ready       | dependency-aware readiness evidence |
| Deployment succeeded | deployment evidence                 |
| Deployment valid     | post-deployment validation          |
| Backup exists        | backup record                       |
| Backup restorable    | restore test                        |
| Replica independent  | topology/failure-domain evidence    |
| State durable        | failure-tested durability evidence  |
| Highly available     | scoped availability evidence        |
| Secure               | threat-model-specific evidence      |
| Disaster recoverable | tested recovery evidence            |

---

# 105. Implementation Firewall

This canon does **not** by itself establish:

```text
A SPECIFIC CLOUD PROVIDER

KUBERNETES

DOCKER

VMWARE

AWS

AZURE

GCP

BARE-METAL DEPLOYMENT

MULTI-REGION DEPLOYMENT

MULTI-CLOUD DEPLOYMENT

PRODUCTION DATABASE TECHNOLOGY

DISTRIBUTED CONSENSUS

RAFT

PAXOS

BYZANTINE FAULT TOLERANCE

FORMAL MVCC IMPLEMENTATION

FORMAL CAS IMPLEMENTATION

ZERO-DOWNTIME DEPLOYMENT

FIVE-NINES AVAILABILITY

DISASTER-RECOVERY READINESS

CRYPTOGRAPHIC ARTIFACT SIGNING

HARDWARE TRUST ROOT

FORMAL SECURITY ISOLATION
```

These require separate repository, runtime, deployment, test, or operational evidence.

---

# 106. Known Gaps

Current canon-level gaps include:

```text
EXACT DEPLOYMENT TOPOLOGY

EXACT COMPUTE PLATFORM

EXACT STORAGE PLATFORM

EXACT NETWORK TOPOLOGY

EXACT SHARD TOPOLOGY

EXACT RESOURCE REGISTRY

EXACT FAULT-DOMAIN MODEL

EXACT TRUST-DOMAIN MODEL

EXACT BACKUP SYSTEM

EXACT RESTORE PROCEDURE

EXACT RPO/RTO

EXACT CAPACITY LIMITS

EXACT SCALING POLICY

EXACT DEPLOYMENT STRATEGY

EXACT SECRET INFRASTRUCTURE

EXACT MVCC/CAS IMPLEMENTATION

EXACT CAUSAL-EPOCH INFRASTRUCTURE BINDING
```

These remain:

```text
UNKNOWN/GAP
```

until canonical or implementation evidence is bound.

---

# 107. Promotion Gate

Promotion:

```text
ACTIVE_CANON_CANDIDATE
→
ACTIVE_CANON
```

requires binding this model to authoritative AMOS sources for at least:

```text
AMOS CORE LAWS

INVARIANT REGISTRY

LAW HIERARCHY

PERSISTENCE CANON

AUTHORITY CANON

CONTROL PLANE CANON

RUNTIME ARCHITECTURE

STATE ARCHITECTURE

MEMORY ARCHITECTURE

PROVENANCE ARCHITECTURE

SECURITY ARCHITECTURE

OBSERVABILITY ARCHITECTURE

OPERATIONS ARCHITECTURE

DEPLOYMENT CONTRACTS

RECOVERY CONTRACTS

TEST EVIDENCE
```

---

# 108. RSCF Node

```yaml
node_id: AMOS_INFRASTRUCTURE_CANON

functional_type:
  - INFRASTRUCTURE_MODEL
  - SUBSTRATE_MODEL
  - RESOURCE_MODEL
  - RESILIENCE_MODEL
  - DEPLOYMENT_FOUNDATION_MODEL

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
  AMOS infrastructure provides the governed compute, storage,
  network, persistence, isolation, deployment, resilience,
  recovery, security-enabling, and observability substrates
  required by higher AMOS OS planes while remaining distinct
  from semantic authority, canon, control-plane governance,
  runtime orchestration, cognition, knowledge, and state.

critical_invariants:
  - INFRASTRUCTURE != AUTHORITY
  - RESOURCE AVAILABILITY != PERMISSION
  - REACHABILITY != TRUST
  - STORED != AUTHORITATIVE
  - PERSISTED != CANONICAL
  - REPLICATION != BACKUP
  - REPLICA COUNT != INDEPENDENT FAILURE COUNT
  - ALIVE != READY
  - TEST VALIDITY != PRODUCTION VALIDITY
  - DEPLOYED != VALIDATED
  - LOCAL ATOMICITY != GLOBAL ATOMICITY
  - BACKUP EXISTS != BACKUP RESTORABLE
  - CONFIGURATION != CANON
  - METRIC != EXPLANATION
  - FAILURE MUST REMAIN LOCAL WHERE DEPENDENCIES PERMIT

dependencies:
  - AMOS_CORE_LAWS
  - INVARIANT_REGISTRY
  - LAW_HIERARCHY
  - PERSISTENCE_CANON
  - AUTHORITY_CANON
  - CONTROL_PLANE_CANON
  - RUNTIME
  - STATE
  - SECURITY
  - OBSERVABILITY
  - OPERATIONS

known_gaps:
  - Exact infrastructure topology requires deployment evidence.
  - Exact resource types require repository/environment evidence.
  - Exact fault-domain topology requires infrastructure evidence.
  - Exact persistence guarantees require implementation and tests.
  - Exact recovery guarantees require restore and failure tests.
  - Exact availability claims require scoped operational evidence.

does_not_establish:
  - implementation completeness
  - production readiness
  - specific cloud architecture
  - high availability
  - disaster recovery readiness
  - formal distributed guarantees
  - formal security guarantees
```

---

# 109. Changelog

## v2.0.0 — 2026-08-25

Expanded the infrastructure placeholder into an AMOS Core v4.4-aligned canon candidate.

Added:

* infrastructure authority firewall;
* H/M/L infrastructure decomposition;
* compute, storage, and network substrates;
* resource identity and provenance;
* isolation and trust boundaries;
* authoritative-state storage separation;
* persistence and durability boundaries;
* MVCC/CAS infrastructure support concepts;
* atomicity scope;
* multi-RSCF persistence requirements;
* fault-domain and correlated-failure topology;
* configuration and environment governance;
* deployment and rollout architecture;
* rollback and recovery;
* dependency closure;
* health, liveness, and readiness distinctions;
* capacity and scaling;
* resource governance and backpressure;
* availability and resilience;
* replication, backup, and restore distinctions;
* security substrate;
* external dependency firewall;
* RSCF evidence typing;
* freshness and regime awareness;
* causal firewall;
* causal epoch integration;
* proof-based coordination avoidance;
* lifecycle and topology registries;
* infrastructure invariants;
* test families and adversarial tests;
* proof obligations;
* implementation firewall;
* promotion gate.

## v1.0.0 — 2026-08-25

Initial placeholder reserved the canonical AMOS OS infrastructure location.

---

# 110. Canonical Summary

```text
AMOS LOGICAL PLANES
↓
GOVERNED EXECUTION REQUIREMENTS
↓
INFRASTRUCTURE
├── COMPUTE
├── STORAGE
├── NETWORK
├── ISOLATION
├── RESOURCE CONTROL
├── DEPLOYMENT
├── PERSISTENCE
├── RESILIENCE
├── SECURITY SUBSTRATE
├── OBSERVABILITY SUBSTRATE
└── RECOVERY
```

The infrastructure layer provides:

```text
CAPACITY

LOCATION

CONNECTIVITY

PERSISTENCE

ISOLATION

RESOURCE CONTROL

FAILURE BOUNDARIES

RECOVERY MECHANISMS
```

but does not independently provide:

```text
CANONICAL TRUTH

SEMANTIC AUTHORITY

POLICY

DECISION RIGHTS

KNOWLEDGE VALIDITY

CAUSAL VALIDITY

GLOBAL FINALITY
```

Core laws:

```text
INFRASTRUCTURE != AUTHORITY

RESOURCE AVAILABILITY != PERMISSION

REACHABILITY != TRUST

STORED != AUTHORITATIVE

PERSISTED != CANONICAL

REPLICATION != BACKUP

REPLICA COUNT != INDEPENDENT FAILURE COUNT

ALIVE != READY

TEST VALIDITY != PRODUCTION VALIDITY

DEPLOYED != VALIDATED

LOCAL ATOMICITY != GLOBAL ATOMICITY

BACKUP EXISTS != BACKUP RESTORABLE

CONFIGURATION != CANON

METRIC != EXPLANATION

CAPABILITY != AUTHORITY
```

Canonical objective:

```text
PROVIDE CAPACITY
WITHOUT INVENTING AUTHORITY.

PROVIDE CONNECTIVITY
WITHOUT ASSUMING TRUST.

PROVIDE STORAGE
WITHOUT CONFUSING PERSISTENCE WITH CANON.

PROVIDE REPLICATION
WITHOUT INVENTING INDEPENDENCE.

PROVIDE LOCALITY
WITHOUT CLAIMING GLOBAL GUARANTEES.

PROVIDE SCALING
WITHOUT HIDING SHARED FAILURE DOMAINS.

PROVIDE DEPLOYMENT
WITHOUT EQUATING DEPLOYMENT WITH VALIDATION.

PROVIDE RECOVERY
WITHOUT ERASING PROVENANCE.

PROVIDE OPTIMIZATION
WITHOUT WEAKENING INTEGRITY.

PRESERVE IDENTITY.
PRESERVE STATE.
PRESERVE PROVENANCE.
PRESERVE DEPENDENCY TOPOLOGY.
PRESERVE FAILURE BOUNDARIES.
PRESERVE AUTHORITY BOUNDARIES.
PRESERVE RECOVERABILITY.

WHEN AN INFRASTRUCTURE GUARANTEE IS NOT ESTABLISHED,
KEEP IT UNKNOWN/GAP.
```

---

**Related:** [[00_ROOT/README.md|AMOS OS]] · [[00_ROOT/ARCHITECTURE.md|Architecture]] · [[00_ROOT/SYSTEM_MAP.md|System Map]] · [[00_ROOT/PLACEMENT_RULES.md|Placement Rules]] · [[01_CANON/00_INDEX/CANON_MAP.md|Canon Map]] · [[AMOS_CORE_LAWS|AMOS Core Laws]] · [[INVARIANT_REGISTRY|Invariant Registry]] · [[LAW_HIERARCHY|Law Hierarchy]] · [[PERSISTENCE_CANON|Persistence Canon]] · [[AUTHORITY_CANON|Authority Canon]] · [[CONTROL_PLANE_CANON|Control Plane Canon]] · [[02_KERNEL/00_INDEX/KERNEL_MAP.md|Kernel Map]] · [[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP.md|Control Plane Map]] · [[04_RUNTIME/00_INDEX/RUNTIME_MAP.md|Runtime Map]] · [[10_MEMORY/00_INDEX/MEMORY_MEMORY_MAP.md|Memory Map]] · [[12_STATE/00_INDEX/STATE_STATE_MAP.md|State Map]] · [[14_TOOLS/00_INDEX/TOOL_MAP.md|Tool Map]] · [[15_INTERFACES/00_INDEX/INTERFACE_MAP.md|Interface Map]] · [[16_SCHEMAS/00_INDEX/SCHEMA_MAP.md|Schema Map]] · [[17_OBSERVABILITY/00_INDEX/OBSERVABILITY_OBSERVABILITY_MAP.md|Observability Map]] · [[18_SECURITY/00_INDEX/SECURITY_MAP.md|Security Map]] · [[19_TESTS/00_INDEX/TEST_MAP.md|Test Map]] · [[20_OPERATIONS/00_INDEX/OPERATIONS_MAP.md|Operations Map]] · [[23_OPERATING_MODEL/00_INDEX/OPERATING_MODEL.md|Operating Model]]

```text
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00_ROOT/00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: infrastructure_canon
node_type: note
path: 01_CANON/04_INFRASTRUCTURE_CANON/INFRASTRUCTURE_CANON.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[04_INFRASTRUCTURE_CANON_MOC]]
