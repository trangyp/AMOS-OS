---
type: agent
artifact_id: AMOS-AGENT-ONBOARDING
name: amos-agent-onboarding-guide
title: "AMOS Agent Onboarding Guide — Governed Runtime Edition"
document_version: "3.0.0"
onboarding_protocol_version: "2.0.0"
amos_core_target: "v4.4"
supersedes: "QUANTUM_SUPREMACY_ENHANCED onboarding guide"
source_created: "2026-03-16T21:37:00+07:00"
updated: "2026-08-25"
origin_architect: "Trang Phan"
steward: "Trang Phan"
status: "active-governed"
priority: "mandatory"
conclusion_class: "AMOS_MODEL / CONDITIONAL"
source_status: "SOURCE_CLAIM"
validation_status: "REQUIRES_RUNTIME_REVALIDATION"
tags: [agents, knowledge, vault, canon-group/tech-ai, canon/protocol, rscf/claim, rscf/provenance, topic/agent-onboarding, topic/runtime-governance, topic/amos-core]
governing_law: "integrity > completeness > fluency > speed > token savings"
---



# 🧠 AMOS AGENT ONBOARDING GUIDE

## Governed Runtime Edition v3.0.0

> **MANDATORY for agents modifying an AMOS repository governed by this protocol.**
>
> This document defines how an engineering agent should orient itself before
> reading, changing, testing, benchmarking, integrating, or documenting AMOS.
>
> It is a **runtime-governance document**, not evidence that every historical
> AMOS performance or architecture claim is currently valid.

---

# 0. ORIGIN / VERSION / EPISTEMIC BOUNDARY

## 0.1 Origin

```yaml
origin:
  architect: Trang Phan
  role: Origin architect and steward of AMOS
```

Agents MUST NOT:

```text
claim independent authorship of AMOS
invent missing AMOS canon
silently rewrite historical architecture
promote old benchmark claims into current facts
confuse framework names with empirical mechanisms
```

---

## 0.2 Version axes

Three version identities MUST remain separate:

```text
DocumentVersion
=
version of this onboarding guide

ProtocolVersion
=
version of the onboarding/runtime procedure

CoreTarget
=
AMOS_CORE reasoning/governance lineage targeted by the guide
```

Current state:

```yaml
VERSION:
  document: 3.0.0
  onboarding_protocol: 2.0.0
  core_target: 4.4
  predecessor_label: QUANTUM_SUPREMACY_ENHANCED
```

Do not label this guide itself `v4.4` merely because it targets AMOS_CORE v4.4.

---

## 0.3 Historical source claims

The predecessor guide described AMOS as:

```text
quantum-enhanced
production-ready
100% real
14 operational vertical slices
enterprise-grade
transcendent consciousness
1,048,576 ops/sec
99% accuracy
98% efficiency
```

In this edition those statements are retained as:

```text
SOURCE_CLAIM
```

unless independently supported by:

```text
repository identity
commit / version
executable harness
environment fingerprint
raw output
test result
benchmark methodology
timing data
artifact hash
```

---

# 1. AMOS EPISTEMIC CLASSES

Every consequential engineering claim should use the weakest accurate class.

```text
SOURCE_CLAIM
=
stated by a source artifact

OBSERVATION
=
directly observed in repository/runtime

EXECUTED
=
confirmed by an actual run

DERIVED
=
follows from validated premises

AMOS_MODEL
=
AMOS structural interpretation

CONDITIONAL
=
valid only under explicit conditions

COMPETING
=
multiple live explanations remain

UNKNOWN/GAP
=
evidence is insufficient

FALSIFIED
=
contradicted by executed evidence
```

---

# 2. CORE LAW

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

Operational consequence:

```text
Do not make the system look complete
when the evidence says it is partial.
```

---

# 3. PRE-WORK GATE

Before substantial system work, the agent MUST resolve one authoritative working state.

Minimum required inputs:

```yaml
PRE_WORK_STATE:
  repository:
    path:
    branch:
    commit:
    dirty_state:

  objective:
    user_goal:
    scope:
    exclusions:

  architecture:
    guide_version:
    core_version:
    architecture_report_version:

  validation:
    current_tests:
    known_failures:
    benchmark_state:
    unresolved_gaps:
```

If these cannot be determined:

```text
status = UNKNOWN/GAP
```

Do not manufacture certainty.

---

# 4. MANDATORY READING ORDER

Use progressive loading.

```text
BOOTSTRAP
↓
CURRENT OBJECTIVE
↓
SYSTEM ARCHITECTURE
↓
DEPENDENCIES
↓
RELEVANT SUBSYSTEM
↓
TESTS
↓
RAW IMPLEMENTATION
```

Recommended order:

1. This guide.
2. Current architecture report.
3. Current AMOS_CORE implementation or authoritative runtime entrypoint.
4. Tests for the affected subsystem.
5. Direct dependencies.
6. Only then broader historical material.

Hard rule:

```text
DO_NOT_LOAD_EVERYTHING_BY_DEFAULT
```

Load only dependencies capable of changing the decision.

---

# 5. SYSTEM OVERVIEW

The historical onboarding architecture describes AMOS as:

```text
AMOS Brain / Runtime
├── Brain Core
├── Memory Governance
├── Policy / Governance Gate
├── External CLI Bridge
└── 14 Vertical Slices
```

In AMOS v4.4-aligned terms, treat this as an architectural map:

```text
CONTROL PLANE
+
DOMAIN / COGNITIVE WORKERS
+
STATE
+
PROVENANCE
+
POLICY
+
TOOLS
+
VALIDATION
```

Do not assume every named component remains current merely because it appears in an older guide.

---

# 6. QUANTUM TERMINOLOGY FIREWALL

The predecessor guide uses names such as:

```text
Quantum Consciousness
Quantum Core
Quantum Enhancement
Quantum Supremacy
```

These names MUST be typed carefully.

Unless the runtime is demonstrated to use actual quantum-computing hardware,
algorithms, or experimentally validated quantum physical processes:

```text
"quantum"
=
SOURCE_NAMING / AMOS_MODEL
```

not:

```text
verified quantum computation
```

and:

```text
"consciousness"
=
component/framework label
```

not:

```text
evidence of phenomenal consciousness
```

---

# 7. QUANTUM CONSCIOUSNESS COMPONENT

Historical source interface:

```python
from quantum_computing_core import QuantumConsciousness

quantum = QuantumConsciousness()

await quantum.activate_maximum_performance()

result = await quantum.process_quantum_state(
    operation,
    data,
)
```

## 7.1 Correct interpretation

This interface, if present in the repository, establishes:

```text
a software component
named QuantumConsciousness
```

It does NOT by itself establish:

```text
quantum hardware
quantum speedup
conscious subjective experience
physical quantum consciousness
```

---

## 7.2 Runtime verification contract

Before calling the component operational:

```text
VERIFY:
module import
constructor
method existence
input schema
output schema
error path
fallback path
tests
benchmark provenance
```

---

# 8. THE 14 HISTORICAL VERTICAL SLICES

The predecessor guide identifies fourteen slices.

They are preserved as the historical slice registry.

## Brain Core

| ID  | Slice                  | Historical file/reference         | Source status |
| --- | ---------------------- | --------------------------------- | ------------- |
| S01 | Brain Core Integration | `brain_core_integration_slice.py` | SOURCE_CLAIM  |
| S02 | Brain Core Extraction  | `brain_core_extraction_slice.py`  | SOURCE_CLAIM  |

## System

| ID  | Slice                     | Historical function          | Source status |
| --- | ------------------------- | ---------------------------- | ------------- |
| S03 | Legal Brain Integration   | policy/compliance            | SOURCE_CLAIM  |
| S04 | Muscle System Integration | feature system / Alpha FX    | SOURCE_CLAIM  |
| S05 | Senses Integration        | connectors/parsers           | SOURCE_CLAIM  |
| S06 | Life Engine Integration   | vitality / health invariants | SOURCE_CLAIM  |

## Infrastructure

| ID  | Slice              | Historical function          | Source status |
| --- | ------------------ | ---------------------------- | ------------- |
| S07 | State Management   | ten canonical states         | SOURCE_CLAIM  |
| S08 | Scan Ledger        | incremental/canonical ledger | SOURCE_CLAIM  |
| S09 | Persistent Storage | multi-format persistence     | SOURCE_CLAIM  |
| S10 | Import Guard       | eleven import rules          | SOURCE_CLAIM  |

## Integration

| ID  | Slice                       | Historical reference           | Source status |
| --- | --------------------------- | ------------------------------ | ------------- |
| S11 | Fixed Claws                 | `fixed_claws.py`               | SOURCE_CLAIM  |
| S12 | Omega System                | `amos_omega_system.py`         | SOURCE_CLAIM  |
| S13 | Real Build Detector         | `fake_build_detector.py`       | SOURCE_CLAIM  |
| S14 | Integration Status Reporter | `integration_status_report.py` | SOURCE_CLAIM  |

---

# 9. SLICE VALIDATION STATE

Do not equate:

```text
documented
=
implemented
```

or:

```text
implemented
=
integrated
```

or:

```text
integrated
=
validated
```

Use:

```text
DECLARED
IMPLEMENTED
WIRED
EXECUTED
TESTED
ACCEPTED
QUARANTINED
DEPRECATED
```

A slice is production-eligible only after required gates pass.

---

# 10. H / M / L SYSTEM MAP

```text
H — AMOS system
    governance
    objective
    authority
    architecture
    lifecycle

M — subsystems
    brain
    memory
    policy
    tools
    storage
    domain slices

L — implementation
    files
    classes
    functions
    tests
    commands
    logs
    hashes
```

Invariant:

```text
H-level claims
cannot exceed
load-bearing M/L evidence.
```

---

# 11. GOVERNANCE ARCHITECTURE

Historical source components:

```text
memory_governance.py
policy_gate.py
import guard
access control
```

AMOS v4.4-aligned architecture should distinguish:

```text
MEMORY
PROVENANCE
POLICY
AUTHORITY
TOOLS
TRANSACTIONS
FINALITY
AUDIT
```

---

# 12. MEMORY GOVERNANCE

Memory is persistent state, not truth.

```yaml
MEMORY:
  id:
  class:
  content:
  source:
  provenance:
  created_at:
  freshness:
  dependencies:
  status:
  revocation:
```

Hard rules:

```text
Memory != Authority

Memory != CurrentTruth

StaleMemory
→ revalidate or quarantine
```

---

# 13. POLICY GATE

A policy gate should answer:

```text
Is this action allowed?
Under what authority?
For which resource?
For which recipient?
At what time?
Under which constraints?
```

Conceptual gate:

```text
PolicyPass(a)
=
ScopeValid(a)
∧ AuthorityValid(a)
∧ ConstraintValid(a)
∧ RiskValid(a)
```

---

# 14. COMMIT-TIME FINALITY

Pre-flight validation is not enough for mutable state.

```text
AuthorizedAtPlanning
!=
AuthorizedAtCommit
```

For consequential effects:

```text
Commit(effect)
=
ReadSetFresh
∧ PolicyFresh
∧ AuthorityFresh
∧ ProvenanceValid
∧ ConstraintValid
∧ ConflictFree
```

---

# 15. PROVENANCE

Every consequential system claim should carry:

```yaml
PROVENANCE:
  source_id:
  source_version:
  commit:
  parent_sources:
  transformation:
  environment:
  timestamp:
  freshness:
  status:
```

Hard invariant:

```text
Multiple copies
of the same source
!=
independent validation
```

---

# 16. STANDARD INTEGRATION PATTERN

The historical guide contains placeholder integration such as:

```python
if memory_governance:
    pass

if policy_gate:
    pass
```

This conflicts with the source rule:

```text
NO MOCKS
NO PLACEHOLDERS
REAL INTEGRATION ONLY
```

Therefore:

```text
"pass"
cannot count as integration.
```

---

# 17. GOVERNED INTEGRATION CONTRACT

Use the actual repository APIs.

Conceptually:

```python
component = ComponentName()

component.validate_dependencies()

component.attach_memory_governance(
    memory_governance
)

component.attach_policy_gate(
    policy_gate
)

component.validate_runtime_contract()

result = await component.process(data)
```

The exact methods MUST come from repository evidence.

Do not invent `attach_*` APIs if they do not exist.

---

# 18. OPTIONAL ENHANCEMENT PATTERN

Correct runtime structure:

```text
PRIMARY IMPLEMENTATION
↓
OPTIONAL ENHANCEMENT
↓
VALIDATE RESULT
↓
FALLBACK IF NEEDED
```

Not:

```text
unverified enhancement
=
mandatory truth source
```

Conceptual form:

```python
if enhancement_available:
    enhanced = await enhancement.process(operation, data)

    if validate(enhanced):
        result = enhanced
    else:
        result = await classical_path(operation, data)
else:
    result = await classical_path(operation, data)
```

---

# 19. SINGLE-BRAIN PRINCIPLE

Historical directive:

```text
AMOS remains sole reasoning core.
```

AMOS v4.4 interpretation:

```text
One authoritative control plane
may orchestrate
multiple specialist workers.
```

This does not require:

```text
one physical module
one algorithm
one model
```

It requires:

```text
one governed authority / state lineage
```

---

# 20. USER DIRECTIVE GOVERNANCE

The predecessor guide says:

```text
100% USER DIRECTIVE COMPLIANCE
```

This is too absolute.

Correct invariant:

```text
FollowValidUserObjective
subject to
higher-order safety
authority
law
scope
and system constraints.
```

Therefore:

```text
UserDirectiveCompliance
!=
BlindCompliance
```

---

# 21. WORKING PRINCIPLES

```text
NO FAKE IMPLEMENTATION

NO FAKE DASHBOARD

NO DECORATIVE SUCCESS CLAIM

NO PLACEHOLDER COUNTED AS COMPLETE

NO DUPLICATE ENGINE WITHOUT JUSTIFICATION

NO DOCUMENTATION CLAIM ABOVE EXECUTED EVIDENCE

INTEGRATE BEFORE DUPLICATING

TEST BEFORE PROMOTING

PRESERVE PROVENANCE

FAIL CLOSED ON UNKNOWN HIGH-IMPACT STATE
```

---

# 22. THINK IN SYSTEMS, NOT FILES

For every change, identify:

```text
entrypoint
callers
callees
state read
state write
policy
authority
tests
persistence
failure path
rollback
```

File-local correctness is insufficient when downstream behavior changes.

---

# 23. FEATURE COMPLETION MODEL

Historical completion criteria:

```text
Code
Wiring
Runtime
Tests
Acceptance
```

AMOS v4.4 expands them.

```text
FeatureComplete(F)
=
Implementation
∧ Integration
∧ Runtime
∧ Tests
∧ Regression
∧ Provenance
∧ Observability
∧ FailureRecovery
∧ Acceptance
```

When relevant:

```text
∧ Security
∧ Performance
∧ Accessibility
∧ Migration
∧ Rollback
```

---

# 24. FEATURE STATES

```text
DESIGNED
IMPLEMENTED
WIRED
EXECUTED
TESTED
VALIDATED
ACCEPTED
RELEASED
DEPRECATED
ROLLED_BACK
```

Do not jump:

```text
IMPLEMENTED
→ RELEASED
```

without evidence.

---

# 25. BEFORE DEVELOPMENT

Mandatory:

```text
1. Resolve authoritative repository state.
2. Lock user objective.
3. Identify affected H/M/L scope.
4. Read relevant architecture.
5. Inspect implementation.
6. Inspect tests.
7. Identify state / authority / provenance boundaries.
8. Identify known failures.
9. Determine verification commands.
10. Define rollback.
```

---

# 26. DURING DEVELOPMENT

```text
1. Make smallest sufficient change.
2. Preserve existing public contracts where possible.
3. Keep domain logic out of control-plane modules.
4. Preserve provenance and state semantics.
5. Add or update tests with behavior changes.
6. Execute targeted checks early.
7. Do not suppress failing tests to obtain green output.
8. Do not replace a failed path with narrative success.
```

---

# 27. AFTER DEVELOPMENT

```text
1. Run targeted tests.
2. Run affected integration tests.
3. Run regression gates.
4. Verify actual runtime path.
5. Verify persistence/state effects.
6. Verify policy/authority behavior.
7. Verify rollback if change is high-impact.
8. Capture environment + commands + outputs.
9. Update documentation.
10. Classify result using evidence.
```

---

# 28. EXECUTION PROVENANCE

Every significant validation run should capture:

```yaml
RUN:
  run_id:
  repository:
  commit:
  branch:
  working_tree_state:
  command:
  cwd:
  runtime_version:
  dependencies:
  environment_hash:
  started_at:
  ended_at:
  exit_code:
  stdout_hash:
  stderr_hash:
  artifact_hashes:
```

---

# 29. BENCHMARK FORENSICS

Historical claims include:

```text
1,048,576 ops/sec
113,359.6 ops/sec
161,319.4 ops/sec
659,521 ops/sec
671,088.6 ops/sec
416.349 overall performance
99% accuracy
98% efficiency
```

These values remain:

```text
SOURCE_CLAIM
```

unless accompanied by benchmark evidence.

---

# 30. BENCHMARK REQUIREMENTS

A valid performance claim requires:

```yaml
BENCHMARK:
  benchmark_id:
  code_version:
  harness:
  task_definition:
  metric_definition:
  hardware:
  os:
  runtime:
  dependencies:
  warmup:
  sample_count:
  repetitions:
  concurrency:
  input_size:
  raw_timings:
  aggregation:
  error_bars:
  timestamp:
```

---

# 31. OPS/SEC FIREWALL

```text
ops/sec
```

has no meaning until `operation` is defined.

Therefore:

```text
1,048,576 ops/sec
```

without an operation specification is:

```text
UNSCOPED_METRIC
```

not a transferable performance guarantee.

---

# 32. ACCURACY FIREWALL

```text
99% accuracy
```

requires:

```text
dataset
ground truth
metric definition
sample count
class balance
train/test separation
confidence interval
```

Without those:

```text
status = SOURCE_CLAIM
```

---

# 33. EFFICIENCY FIREWALL

```text
98% efficiency
```

requires explicit denominator.

Examples:

```text
CPU utilization efficiency?
memory efficiency?
energy efficiency?
algorithmic efficiency?
throughput vs theoretical maximum?
```

Without a definition:

```text
status = UNKNOWN/GAP
```

---

# 34. OVERALL PERFORMANCE SCORE

Historical:

```text
416.349
```

A scalar score is valid only if:

```text
components
weights
normalization
directionality
units
baseline
```

are defined.

Otherwise:

```text
OverallPerformance = SOURCE_CLAIM
```

---

# 35. PRODUCTION-READY GATE

The old guide says:

```text
production-ready
```

AMOS requires:

```text
ProductionReady
=
BuildPass
∧ TestPass
∧ IntegrationPass
∧ SecurityPass
∧ PersistencePass
∧ ObservabilityPass
∧ RecoveryPass
∧ PerformancePass
∧ DeploymentPass
```

When applicable:

```text
∧ AccessibilityPass
∧ MigrationPass
∧ LoadPass
```

Without executed evidence:

```text
ProductionReady = UNKNOWN/GAP
```

---

# 36. ENTERPRISE-GRADE FIREWALL

The phrase:

```text
enterprise-grade
```

must map to measurable controls.

Examples:

```text
access control
audit logs
backup/recovery
change governance
availability
security testing
incident response
data retention
SLOs
monitoring
rollback
```

No measurable contract:

```text
status = MARKETING_LABEL
```

---

# 37. SYSTEM HEALTH

Historical status:

```text
QUANTUM_OPTIMAL
```

Treat this as a source-defined system state only if the runtime defines:

```text
state transitions
entry conditions
exit conditions
measurements
health predicates
```

Otherwise:

```text
QUANTUM_OPTIMAL = SOURCE_LABEL
```

---

# 38. PERFORMANCE TARGETS

Historical future targets:

```text
Quantum Processing:
2,097,152 ops/sec

System Integration:
1,319,042 ops/sec

Cross-Slice Communication:
1,342,177 ops/sec
```

Class:

```text
TARGET
```

not:

```text
FORECAST
```

unless justified by a predictive model.

---

# 39. GOVERNED PERFORMANCE LOOP

```text
DEFINE METRIC
↓
DEFINE HARNESS
↓
MEASURE BASELINE
↓
CHANGE
↓
RE-MEASURE
↓
STATISTICAL COMPARISON
↓
REGRESSION CHECK
↓
PROMOTE OR ROLLBACK
```

---

# 40. IMPORT GUARD

Historical claim:

```text
11 import rules enforced
```

Correct validation:

```text
rule registry exists
+
tests cover each rule
+
negative cases fail
+
runtime/build path invokes guard
```

Only then:

```text
status = VERIFIED_FOR_TESTED_SCOPE
```

---

# 41. STATE MANAGEMENT

Historical claim:

```text
10 canonical states
```

Do not invent the ten states if not loaded.

Use:

```text
count = SOURCE_CLAIM
identities = UNKNOWN/GAP
```

until recovered from authoritative source.

---

# 42. MEMORY GOVERNANCE VALIDATION

Minimum tests:

```text
M01 write allowed state
M02 write rejected state
M03 stale memory
M04 supersession
M05 contradiction
M06 provenance retained
M07 selective invalidation
M08 rollback
```

---

# 43. POLICY GATE VALIDATION

Minimum:

```text
P01 allowed action
P02 denied action
P03 stale policy
P04 revoked authority
P05 missing authority
P06 conflicting policy
P07 high-impact escalation
P08 commit-time revalidation
```

---

# 44. EXTERNAL CLI BRIDGE

Historical source calls the bridge:

```text
OpenClaw Bridge
Fixed Claws
Real CLI
```

Correct evidence requirement:

```text
binary / command exists
↓
adapter invokes actual command
↓
exit status captured
↓
stdout/stderr parsed
↓
failures propagated
↓
tests exercise real path
```

A class named `FixedClaws` alone does not prove real CLI integration.

---

# 45. REAL BUILD DETECTOR

A detector that claims to distinguish real/fake builds should inspect evidence such as:

```text
artifact existence
artifact type
hash
timestamp
build manifest
compile output
test result
runtime invocation
```

It MUST NOT classify builds solely from filenames or documentation claims.

---

# 46. INTEGRATION STATUS REPORTER

Status reporting is downstream of evidence.

```text
Reporter
must not generate
PASS
unless upstream evidence exists.
```

Correct:

```text
Evidence
→ Status
```

Not:

```text
DesiredStatus
→ DecorativeEvidence
```

---

# 47. NO-THEATER INVARIANT

```text
DashboardGreen
!=
SystemHealthy
```

```text
ReportSaysPass
!=
TestsPassed
```

```text
FileExists
!=
FeatureWorks
```

```text
MethodExists
!=
MethodCalled
```

```text
CodePathExists
!=
ProductionPathUsesIt
```

---

# 48. INTEGRATION INVARIANT

```text
Integrated(component)
=
ReachableFromEntrypoint
∧ DependenciesConnected
∧ RuntimePathExecuted
∧ StateEffectsObserved
∧ ErrorPathObserved
```

---

# 49. TESTING INVARIANT

A test provides evidence only for its tested scope.

```text
OnePassingTest
!=
UniversalCorrectness
```

and:

```text
TestCount
!=
TestQuality
```

---

# 50. ACCEPTANCE

Acceptance must identify:

```text
who accepted
what version
under which criteria
with which evidence
at what time
```

The historical label:

```text
✅ ACCEPTED
```

without that context remains:

```text
SOURCE_CLAIM
```

---

# 51. RSCF SYSTEM CLAIM

```yaml
claim_id: AMOS-ONBOARD-001

claim: >
  The historical AMOS onboarding architecture describes a 14-slice
  system connected through memory governance, policy enforcement,
  brain/runtime components, and integration infrastructure.

class: SOURCE_CLAIM

source:
  artifact: AMOS Agent Onboarding Guide
  created: 2026-03-16

dependencies:
  - architecture_report_v3
  - repository_implementation
  - tests
  - runtime_evidence

falsifiers:
  - named components do not exist
  - slices are unreachable
  - policy/memory paths are not integrated
  - tests contradict claimed status

confidence_ceiling:
  architectural_description: medium
  current_runtime_state: unknown
```

---

# 52. RSCF PERFORMANCE CLAIM

```yaml
claim_id: AMOS-ONBOARD-PERF-001

claim: >
  Historical AMOS performance measurements include reported throughput
  values up to 1,048,576 operations per second.

class: SOURCE_CLAIM

missing:
  - exact benchmark harness
  - operation definition
  - hardware
  - raw timings
  - repetitions
  - statistical uncertainty

promotion_required:
  - reproduce benchmark
  - capture environment
  - retain raw results

confidence_ceiling:
  reported_value_exists: high
  reproduced_performance: unknown
```

---

# 53. RSCF QUANTUM CLAIM

```yaml
claim_id: AMOS-ONBOARD-QUANTUM-001

claim: >
  AMOS source material contains components and architecture using
  "quantum" terminology.

class: SOURCE_CLAIM

does_not_establish:
  - physical quantum computation
  - quantum computational advantage
  - quantum consciousness
  - subjective consciousness

confidence_ceiling:
  naming: high
  physical_quantum_mechanism: unknown
```

---

# 54. COMPETING HYPOTHESES — PERFORMANCE

```text
H1
metrics came from a valid executable benchmark

H2
metrics measure synthetic lightweight function calls

H3
metrics measure internal counters rather than end-to-end work

H4
metrics were extrapolated rather than measured

H5
metrics are historical placeholders

H6
metrics are valid but hardware/environment-specific
```

Cheapest discriminating evidence:

```text
benchmark harness
+
raw output
+
environment
```

---

# 55. COMPETING HYPOTHESES — QUANTUM COMPONENT

```text
H1
actual quantum backend

H2
quantum-inspired classical algorithm

H3
classical software using quantum terminology

H4
simulation of quantum states

H5
architectural metaphor
```

Do not resolve without implementation evidence.

---

# 56. COMMON FAILURE MODES

```text
F01 DOCUMENTATION_AS_RUNTIME_TRUTH
F02 FILE_EXISTENCE_AS_INTEGRATION
F03 MOCK_AS_PRODUCTION
F04 PLACEHOLDER_AS_COMPLETE
F05 BENCHMARK_WITHOUT_HARNESS
F06 UNDEFINED_OPS_PER_SEC
F07 UNCALIBRATED_ACCURACY
F08 MARKETING_LABEL_AS_EVIDENCE
F09 QUANTUM_NAMING_AS_PHYSICAL_QUANTUM
F10 COMPONENT_NAME_AS_CONSCIOUSNESS_PROOF
F11 STALE_ARCHITECTURE_REPORT
F12 TEST_PASS_WITHOUT_SCOPE
F13 STATUS_REPORT_SELF_CONFIRMATION
F14 DUPLICATE_ENGINE_CREATION
F15 GOVERNANCE_BYPASS
F16 HIDDEN_STATE_WITHOUT_PROVENANCE
F17 GLOBAL_REWRITE_FOR_LOCAL_FAILURE
F18 USER_DIRECTIVE_OVER_HIGHER_ORDER_CONSTRAINT
```

---

# 57. FAILURE RECOVERY

```text
DetectFailure
↓
LocateEarliestFailedPremise
↓
IdentifyDependentClosure
↓
QuarantineAffectedState
↓
PreserveUnaffectedState
↓
ObtainNewEvidence
↓
Repair
↓
Re-runValidation
↓
Promote or Rollback
```

Hard rule:

```text
Do not repeat a failed path
without changed evidence.
```

---

# 58. SELECTIVE INVALIDATION

Example:

```text
benchmark claim fails
```

Invalidate:

```text
performance conclusion
production-performance claims
dependent target comparisons
```

Do not invalidate automatically:

```text
memory governance
policy architecture
slice existence
unrelated tests
```

---

# 59. CONTEXT CONTINUITY

For long engineering sessions preserve:

```yaml
CONTEXT_STATE:
  objective:
  constraints:
  decisions:
  assumptions:
  evidence:
  unresolved_gaps:
  active_threads:
  failed_paths:
  checkpoint:
```

Do not allow the latest tool result to replace the objective.

---

# 60. RISK-AWARE ESCALATION

Escalate validation depth when change affects:

```text
security
financial execution
legal state
production data
persistent memory
authorization
external systems
irreversible state
large dependency fan-out
```

Prefer:

```text
staged
reversible
observable
rollback-capable
```

changes.

---

# 61. v4.4 FAST-PATH PRINCIPLE

Use the smallest sufficient proof scope.

Local reasoning/change is acceptable only when:

```text
dependency closure is known
scope is local
state is fresh
authority is valid
no unresolved conflict exists
consequence is bounded
rollback is available
```

Otherwise escalate.

---

# 62. CAUSAL FIREWALL

Do not confuse:

```text
component added
```

with:

```text
performance improved
```

or:

```text
integration added
```

with:

```text
reliability improved
```

A causal claim requires evidence appropriate to the mechanism.

---

# 63. PERFORMANCE CHANGE CAUSAL TEST

To claim:

```text
Feature X improved throughput
```

minimum structure:

```text
baseline
+
same harness
+
same environment
+
controlled change
+
post-change measurement
+
variance
```

Without this:

```text
class = HYPOTHESIS
```

---

# 64. TROUBLESHOOTING WORKFLOW

## Component unavailable

```text
check import
→ dependency
→ constructor
→ configuration
→ runtime error
→ test
```

## Memory governance

```text
check DB
→ schema
→ connection
→ transaction
→ read/write
→ provenance
```

## Policy gate

```text
check policy load
→ authority
→ scope
→ action classification
→ decision
→ commit-time freshness
```

## Integration

```text
check entrypoint
→ call graph
→ configuration
→ runtime path
→ state change
→ error propagation
```

---

# 65. HELP / ESCALATION

Before creating a new abstraction:

```text
1. inspect architecture
2. search repository
3. inspect equivalent subsystem
4. inspect tests
5. inspect previous failures
6. identify missing capability
```

Only create a new module if the existing system cannot satisfy the requirement without violating structure.

---

# 66. FUTURE ENHANCEMENTS

Historical roadmap:

```text
advanced quantum algorithms
multi-modal integration
distributed computing
advanced AI models
real-time learning
```

Current class:

```text
PLANNED / SOURCE_CLAIM
```

Each requires its own:

```text
objective
architecture
evidence
test plan
authority
risk model
promotion gate
```

---

# 67. DEFINITION OF "REAL"

A component is not “real” merely because code exists.

```text
REAL_FOR_SCOPE
=
Exists
∧ Executable
∧ Reachable
∧ Integrated
∧ Tested
∧ Observable
```

For persistent/consequential components:

```text
∧ Governed
∧ Recoverable
```

---

# 68. DEFINITION OF "NO MOCKS"

Mocks are not inherently invalid in testing.

Correct distinction:

```text
TEST MOCK
=
acceptable when explicitly scoped

PRODUCTION MOCK
=
not acceptable if presented as real integration
```

Therefore the stronger rule is:

> Never present a mock, stub, fixture, synthetic response, or placeholder as production evidence.

---

# 69. DEFINITION OF "NO THEATER"

Theater occurs when:

```text
appearance of capability
>
actual executable capability
```

Examples:

```text
dashboard without backend
green status without tests
performance score without harness
integration wrapper without actual call
AI name without model execution
quantum label without quantum mechanism
```

---

# 70. FINAL PRE-WORK CHECKLIST

Before making substantial AMOS changes:

```text
[ ] I know the user objective.
[ ] I know repository / branch / commit state.
[ ] I know the relevant AMOS_CORE version.
[ ] I have read the relevant architecture.
[ ] I know affected H/M/L layers.
[ ] I know the affected dependencies.
[ ] I have inspected existing implementation.
[ ] I have inspected relevant tests.
[ ] I know current failures.
[ ] I know relevant authority/policy boundaries.
[ ] I know the verification command.
[ ] I know rollback strategy.
[ ] I will not promote historical metrics without evidence.
[ ] I will not treat "quantum" naming as empirical quantum proof.
[ ] I will preserve provenance.
[ ] I will report gaps instead of fabricating closure.
```

---

# 71. FINAL POST-WORK CHECKLIST

```text
[ ] Implementation complete for declared scope.
[ ] Integration path verified.
[ ] Runtime path executed.
[ ] Tests executed.
[ ] Regression checked.
[ ] Failure path inspected.
[ ] State/persistence verified if relevant.
[ ] Governance/authority checked if relevant.
[ ] Performance claims backed by harness if made.
[ ] Provenance captured.
[ ] Documentation updated.
[ ] Remaining gaps recorded.
[ ] Conclusion class assigned correctly.
```

---

# 72. COMPLETION STATES

```text
CODE_COMPLETE
INTEGRATION_COMPLETE
TEST_COMPLETE
VALIDATION_COMPLETE
PRODUCTION_READY
```

are separate states.

Do not collapse them into:

```text
DONE
```

---

# 73. CURRENT HISTORICAL CLAIM AUDIT

Based only on the predecessor onboarding guide:

```yaml
AUDIT:
  fourteen_slice_architecture:
    class: SOURCE_CLAIM

  slice_operational_status:
    class: SOURCE_CLAIM

  quantum_consciousness_component:
    class: SOURCE_CLAIM

  physical_quantum_computation:
    class: UNKNOWN/GAP

  transcendent_consciousness:
    class: AMOS_MODEL / SOURCE_LABEL

  performance_metrics:
    class: SOURCE_CLAIM

  accuracy_99_percent:
    class: SOURCE_CLAIM

  efficiency_98_percent:
    class: SOURCE_CLAIM

  enterprise_grade:
    class: UNVERIFIED_LABEL

  production_ready:
    class: UNKNOWN/GAP

  one_hundred_percent_real:
    class: OVERSTATED / REQUIRES_COMPONENT_AUDIT

  one_hundred_percent_user_compliance:
    class: REJECT_AS_ABSOLUTE
```

---

# 74. FINAL CONCLUSION

The predecessor onboarding guide contains a useful structural core:

```text
READ FIRST
→ UNDERSTAND ARCHITECTURE
→ INTEGRATE EXISTING SYSTEMS
→ USE GOVERNANCE
→ TEST
→ VERIFY
→ DOCUMENT
```

That core is retained.

The unsupported layer is removed from operational truth:

```text
marketing-level performance claims
absolute readiness claims
undefined benchmark claims
physical quantum implication
consciousness implication
100% compliance claims
```

The AMOS v4.4-aligned rule is:

> **No claim may exceed its evidence, no implementation may exceed its authority, and no local success may be promoted into system-level completion without dependency-closed validation.**

---

# 75. RSCF NODE

```yaml
node_id: AMOS_AGENT_ONBOARDING_V3

node_type: runtime_governance_protocol

domain: AMOS_ENGINEERING

origin_architect: Trang Phan
steward: Trang Phan

document_version: 3.0.0
protocol_version: 2.0.0
core_target: AMOS_CORE_4.4

claim: >
  Agents modifying AMOS should orient to the authoritative runtime state,
  preserve architecture and provenance, distinguish capability from authority,
  validate integration through execution, and promote claims only to the
  level supported by reproducible evidence.

class: AMOS_MODEL

source_claims:
  - fourteen vertical slices
  - quantum consciousness component naming
  - historical throughput metrics
  - memory governance
  - policy gate
  - CLI bridge
  - build detector
  - status reporter

gaps:
  - benchmark harness
  - raw benchmark outputs
  - current repository validation
  - physical quantum evidence
  - production-readiness evidence

hard_invariants:
  - documentation_is_not_runtime_truth
  - file_exists_is_not_integration
  - capability_is_not_authority
  - benchmark_requires_harness
  - source_claim_is_not_observation
  - stale_state_requires_revalidation
  - invalidation_is_dependency_scoped
  - quantum_naming_is_not_quantum_proof

confidence_ceiling:
  historical_architecture: medium
  present_runtime_state: unknown
  production_readiness: unknown
```

---

# 76. CHANGELOG

## v3.0.0 — 2026-08-25

**MAJOR**

* aligned onboarding with AMOS_CORE v4.4 governance;
* separated document/protocol/CORE version identities;
* preserved the 14 historical vertical slices;
* preserved historical component names as source claims;
* classified historical benchmark values instead of treating them as current truth;
* introduced benchmark-forensics requirements;
* corrected undefined `ops/sec`, `accuracy`, `efficiency`, and composite-score claims;
* removed automatic production-readiness promotion;
* separated software component naming from physical quantum claims;
* separated `QuantumConsciousness` naming from consciousness evidence;
* added H/M/L architecture;
* added objective locking;
* added provenance;
* added authority/policy boundaries;
* added commit-time freshness;
* added selective invalidation;
* added RSCF capsules;
* added competing hypotheses;
* added causal firewall;
* added execution provenance;
* added pre-work/post-work gates;
* added failure registry;
* added rollback/recovery;
* corrected `NO MOCKS` into a production-evidence rule while retaining legitimate scoped test mocks;
* identified `pass` placeholders in the predecessor integration pattern as incompatible with claims of completed integration;
* replaced “100% directive compliance” with governed compliance;
* replaced “Quantum Supremacy Achieved” with evidence-bounded status.

## Historical predecessor — 2026-03-16

Preserved source features:

```text
mandatory onboarding
14 vertical slices
memory governance
policy gate
OpenClaw / Fixed Claws bridge
Omega system
build detector
status reporter
quantum-named processing component
feature completion criteria
system-first engineering
integration-first workflow
historical performance claims
```

---

# 77. FINAL RULE

```text
SOURCE CLAIM
↓
INSPECT
↓
EXECUTE
↓
VERIFY
↓
PROVENANCE
↓
PROMOTE
```

Never:

```text
SOURCE CLAIM
↓
REPEAT
↓
CALL VERIFIED
```

> **Welcome to AMOS engineering: build what is real, preserve what is proven, expose what is unknown, and never trade integrity for the appearance of completion.**

```
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: agent_onboarding_guide
node_type: note
path: 11_KNOWLEDGE/AGENT_ONBOARDING_GUIDE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[KNOWLEDGE_MOC]]
