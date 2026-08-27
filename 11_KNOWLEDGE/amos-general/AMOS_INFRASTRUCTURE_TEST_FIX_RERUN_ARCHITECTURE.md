---
title: AMOS INFRASTRUCTURE TEST FIX RERUN ARCHITECTURE
tags: [amos-general, amos, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture

---


# AMOS Infrastructure Layer — Test, Fix, Rerun & Architecture Enhancement

**Origin architect / steward:** Trang Phan  
**System position:** AMOS infrastructure/control layer above Full Brain OS, domain skills, agents, tools, memory, and external effectors  
**Baseline lineage:** AMOS_CORE v4.4  
**Status:** VERIFIED where execution evidence exists; DERIVED/CONDITIONAL where architecture or external-runtime integration remains unexecuted

---

## 1. Executive Conclusion

AMOS is treated as the infrastructure and governance layer above cognition and domain execution.

The validated authority structure is:

**User/System Authority → AMOS Infrastructure / Control Plane → Full Brain OS Orchestration → Domain Skills / Agents → Tools / Adapters → External Effects**

Full Brain OS may reason, decompose, route, synthesize, and propose actions. It does **not** own durable-state commit authority, provenance admission, authorization freshness, observability finality, transaction semantics, rollback/finality, or external-effect release.

The executable AMOS_CORE v4.4 artifact was tested, repaired at the smallest causal boundary, and rerun with expanded adversarial coverage.

---

## 2. Baseline Findings

The initial executable baseline exposed four load-bearing infrastructure defects.

### 2.1 Runtime identity drift

The composed v4.4 artifact reported an older internal version identity:

`3.8.0-iterative-provenance-runtime`

This violated runtime identity and lineage consistency.

### 2.2 Durable effects could enter FAST_FINAL

`fast_finalize(..., durable_local=True)` accepted a durability flag but did not enforce it.

A durable effect could therefore incorrectly use proof-based local fast finalization instead of escalating to the infrastructure release boundary.

### 2.3 Commit survived ownership revocation

A fast permit issued during prepare could still commit after ownership/authority conditions changed.

This meant prepare-time validity was being treated as durable commit-time authority.

### 2.4 Commit survived consequence escalation

A permit could also remain valid after consequence risk rose beyond the fast-lane threshold.

This violated freshness and commit-time revalidation.

---

## 3. Root Cause

The defects shared one causal target:

> **Prepare-time proof was being treated as commit-time authority.**

The repair therefore avoided four unrelated patches and instead introduced a single infrastructure invariant:

## PREPARE_PERMIT != COMMIT_AUTHORITY

Any fast-lane decision must be revalidated immediately before publication or durable state transition.

---

## 4. Repair Applied

The repaired v4.4 runtime now enforces:

- Correct composed runtime identity:
  - `4.4.0-proof-coordination-avoidance`
- Durable effects are excluded from local proof-based fast finalization.
- Commit-time fast-lane freshness is rechecked.
- Ownership must still be valid.
- Target state/CAS assumptions must still be valid.
- Consequence level must still satisfy fast-lane limits.
- Reversibility assumptions must still hold.
- Conflict probability must still remain below the accepted threshold.
- Transaction identity must remain stable and non-equivocating.

Fast-lane eligibility is now a **fresh commit-time predicate**, not a reusable permit token.

---

## 5. Test → Fix → Rerun Evidence

### Baseline

**5 / 7 PASS**

Failures:

1. Runtime identity mismatch.
2. Durable effect incorrectly entered FAST_FINAL.

Expanded adversarial testing then exposed:

3. Owner revocation not revalidated.
4. Consequence-risk escalation not revalidated.

### Repaired Expanded Suite

**12 / 12 PASS**

Coverage included:

- compile/import
- v4.4 runtime identity
- normal fast-path success
- stale-state rejection
- owner mismatch rejection
- cross-shard rejection
- durable-effect escalation
- commit-time owner revalidation
- commit-time consequence revalidation
- commit-time reversibility revalidation
- conflict-risk revalidation
- transaction-ID equivocation rejection

### Independent pytest regression

**9 / 9 PASS**

Observed runtime:

`9 passed in 0.10s`

This establishes correctness only for the exact artifact, environment, and tested contract surface.

It does **not** prove universal distributed-system correctness.

---

## 6. AMOS Infrastructure Architecture v2

The repaired architecture formalizes five effect classes:

```text
PURE
REVERSIBLE_INTERNAL
DURABLE_STATE
EXTERNAL_EFFECT
MODEL_PROMOTION
```

### Fast-lane policy

Only sufficiently bounded:

- `PURE`
- `REVERSIBLE_INTERNAL`

operations may use proof-based coordination avoidance.

The following must escalate:

- `DURABLE_STATE`
- `EXTERNAL_EFFECT`
- `MODEL_PROMOTION`

### Infrastructure-owned components

The architecture separates cognition from governance through the following control-plane roles:

- **Policy / Authority Resolver**
- **Commit Governor**
- **Effect Executor**
- **Observability / Replay Agent**
- **Recovery Governor**
- **Provenance / Evidence Admission**
- **Semantic Transaction Validator**
- **Release Ledger / Finality Layer**

Normal agents are **proposal-only** by default.

Capability does not imply authority.

---

## 7. Agent Architecture Enhancement

### Agent default authority

```text
AGENT_CAPABILITY != COMMIT_AUTHORITY
```

Planner, analyst, researcher, coding, domain, and Full Brain agents may produce:

- candidate results
- evidence
- proposed effects
- risk estimates
- capability requests
- repair proposals

They may not independently finalize consequential effects.

### Agent-to-infrastructure handoff

```text
Agent Proposal
→ Evidence Admission
→ Policy / Authority Resolution
→ Semantic Transaction Validation
→ Observability Check
→ Commit-Time Freshness
→ Effect Release
→ Receipt / Replay / Recovery State
```

This keeps stochastic cognition separate from deterministic effect governance.

---

## 8. Skill Architecture Enhancement

The AMOS Skill Builder now requires consequential skills to declare a stronger control contract.

### Required skill contract

A consequential skill should define:

- identity
- version
- provenance
- applicability envelope
- typed inputs
- typed outputs
- dependencies
- evidence classes
- effect class
- observability requirements
- authority requirements
- deterministic validators where feasible
- falsifiers
- invalidation conditions
- rollback / recovery expectations
- environment compatibility
- freshness assumptions

### New hard distinctions

```text
SKILL_RETRIEVED != SKILL_APPLICABLE
SKILL_APPLICABLE != SKILL_EFFECTIVE
SKILL_SUCCESS != UPDATE_CREDIT
DECLARED_CAPABILITY != OBSERVED_CAPABILITY
POLICY_DECISION != EFFECT_EXECUTION
PREPARE_PERMIT != COMMIT_AUTHORITY
TOOL_AVAILABLE != TOOL_EXECUTED
REPLAY_SUCCESS != SEMANTIC_CORRECTNESS
```

### Skill promotion rule

A skill should only be promoted when it contributes a non-duplicative capability and has sufficient:

- typed state
- invariants
- protocol/equation/metric
- provenance
- falsifiers
- deterministic or externally verifiable validation
- effect-boundary declaration
- rollback / invalidation semantics

Topic overlap alone is insufficient.

---

## 9. Full Brain OS Placement

Full Brain OS remains the cognition/orchestration layer below infrastructure authority.

Execution flow may be represented as:

```text
Full Brain OS
→ AMOS_CORE v4.4 Reasoning Runtime
→ AMOS Infrastructure Control Plane
→ Host Deployment / Tool Runtime
→ World Effect
```

Authority precedence at the effect boundary remains:

```text
User/System Authority
→ AMOS Infrastructure
→ Full Brain OS
→ Specialist Skill / Agent
→ Tool
```

These two views are related but must not be flattened into one hierarchy.

---

## 10. Open-Source Architecture Mapping

Open-source systems are used as interoperability substrates, not replacements for AMOS semantics.

### OpenTelemetry

Mapped to:

- traces
- metrics
- logs
- resource identity
- execution correlation
- observability envelopes

Hard boundary:

```text
TRACE_PRESENT != SEMANTIC_PROOF
OBSERVED != CORRECT
```

### Open Policy Agent (OPA)

Mapped to:

- policy-as-code
- deterministic policy decisions
- policy versioning
- decision logging
- fail-closed evaluation

Hard boundary:

```text
POLICY_DECISION != POLICY_ENFORCEMENT
POLICY_ALLOW != EFFECT_COMMIT
```

Effect commit still requires fresh AMOS authority, transaction validity, state freshness, and release controls.

### Temporal

Mapped to:

- durable workflow execution
- retryable work units
- event history
- long-running work-item continuity

Hard boundary:

```text
WORKFLOW_RETRY != SAFE_EFFECT_RETRY
```

Ambiguous external effects must reconcile through AMOS effect-release state rather than blind retry.

### Supply-chain attestation

Patterns from Sigstore/SLSA-style architectures are compatible with:

- artifact digests
- signer identity
- builder/source lineage
- provenance attestations
- revocation/freshness

Hard boundary:

```text
SIGNATURE_VALID != ARTIFACT_SAFE
ATTESTATION_PRESENT != REQUIRED_PROPERTY_PROVEN
```

---

## 11. Knowledge and Provenance Rules

AMOS infrastructure preserves:

```text
Ephemeral Code
→ Persistent Evidence
→ Validated Knowledge
```

Evidence, interpretation, and persistent knowledge remain separate.

Important conclusions should retain:

- claim class
- source identity
- ancestry
- dependencies
- environment
- version
- scope
- regime
- freshness
- falsifiers
- confidence ceiling

Correlated descendants of one source do not count as independent confirmation.

---

## 12. Current Conclusion Classes

### VERIFIED

- Runtime patch construction
- Corrected v4.4 identity
- Durable-effect fast-lane exclusion
- Commit-time fast-lane revalidation
- Expanded 12/12 test suite
- Independent 9/9 pytest regression
- Architecture v2 artifact generation
- Test/fix/rerun ledger generation
- Updated orchestration execution plan
- Skill Builder control-contract update

### DERIVED

- Cross-system architecture combining AMOS control semantics with OPA, OpenTelemetry, Temporal, and supply-chain patterns.
- Agent proposal-only authority model.
- Skill effect-class and observability contracts.

### CONDITIONAL

- Production OpenTelemetry integration
- OPA runtime enforcement integration
- Temporal crash/replay integration
- Receiver-attested effect completion
- External release-ledger finality

These remain conditional until executed in the target runtime.

---

## 13. Remaining Gaps

The highest-value remaining work is:

1. Real release-ledger integration.
2. Receiver-attested completion receipts.
3. OPA policy-gate execution and negative testing.
4. OpenTelemetry trace-closure testing.
5. Temporal crash / retry / replay / reconciliation testing.
6. Cross-skill authority-composition tests.
7. Cross-repository dependency and architecture-conformance testing.
8. Runtime environment drift detection.
9. Tool-output admission / taint containment.
10. Executable documentation synchronization.
11. Deployment topology reconstruction.
12. Recovery-root and break-glass validation.
13. Artifact attestation verification with real signing tooling.
14. Multi-agent composition conflict testing.

These are **UNKNOWN/GAP or CONDITIONAL**, not PASS.

---

## 14. Core Infrastructure Laws

```text
INTEGRITY > COMPLETENESS > FLUENCY > SPEED > TOKEN SAVINGS

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

PREPARE_PERMIT != COMMIT_AUTHORITY

POLICY_DECISION != EFFECT_EXECUTION

OBSERVABILITY != CORRECTNESS

REPLAY_SUCCESS != SEMANTIC_CORRECTNESS

SIGNATURE_VALID != SAFETY

TOOL_AVAILABLE != TOOL_EXECUTED

UNKNOWN/GAP != PASS
```

---

## 15. Final Architecture

```text
                    USER / SYSTEM AUTHORITY
                              │
                              ▼
                 AMOS INFRASTRUCTURE CONTROL
        ┌────────────────────────────────────────┐
        │ Provenance / Evidence Admission        │
        │ Capability & Applicability Resolution  │
        │ Policy / Authority Resolver            │
        │ Semantic Transaction Validator         │
        │ Observability Envelope                 │
        │ Commit-Time Freshness / CAS            │
        │ Release Ledger / Effect Finality       │
        │ Replay / Recovery / Rollback           │
        └────────────────────────────────────────┘
                              │
                              ▼
                    AMOS FULL BRAIN OS
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
              Specialist Skills     Agents
                    │                   │
                    └─────────┬─────────┘
                              ▼
                         Tools / MCP
                              │
                              ▼
                       External World
```

The architecture intentionally keeps reasoning flexibility high while keeping effect authority narrow, typed, freshness-bound, provenance-bound, and reversible wherever possible.

---

## 16. Promotion Decision

**Conclusion class: VERIFIED + DERIVED + CONDITIONAL**

The repaired v4.4 fast-finalization boundary is **VERIFIED for the executed test scope**.

The broader infrastructure architecture is **DERIVED from AMOS lineage, Drive material, and open-source system patterns**.

External runtime integrations remain **CONDITIONAL** until their actual binaries/services are executed and validated in the target deployment.

No unexecuted capability is credited as PASS.

---
**Links:** [[AMOS-GENERAL_MOC]] | [[KNOWLEDGE_MOC]]
