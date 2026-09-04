---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Agent Safety Architecture 2026
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# AGENT_SAFETY_ARCHITECTURE_2026 — Production Agent Safety Architecture

> [!ABSTRACT] Control Plane Specification
> Defines the comprehensive agent safety architecture for AMOS OS, integrating four production-grade patterns — MAOS, Polos, AgentOS (seL4), and Argentor — into a unified safety framework. Maps each pattern to AMOS control plane layers, establishes post-quantum cryptographic primitives for agent authentication, and aligns with the EU AI Act (fully applicable August 2, 2026).
> Enforces that no agent action escapes governance, no capability exceeds its scope, and no external effect occurs without a single, auditable chokepoint.

---

## 1. Architecture Overview

### 1.1 Threat Model

Agents operating within AMOS present a distinct threat surface compared to traditional software:

- **Prompt injection and goal hijacking** — adversarial inputs that redirect agent behavior.
- **Capability creep** — gradual accumulation of permissions beyond original scope.
- **Collusion** — coordinated misbehavior across multiple agent instances.
- **Side-channel leakage** — inference of sensitive state through timing or observation.
- **Emergent misalignment** — collective behavior not intended by any individual agent design.

### 1.2 Design Principles

1. **Single chokepoint** — all external effects flow through one commit layer; no agent writes directly to the outside world.
2. **Least authority** — every agent holds the smallest sufficient capability set; tokens are scoped, time-limited, and revocable.
3. **Structural separation of decision and action** — agents that reason hold no tools; agents that execute hold no discretionary policy.
4. **Deterministic enforcement** — critical safety checks execute in an LLM-independent Deterministic Security Core; LLM output never directly gates allow/deny.
5. **Cryptographic auditability** — every mutation emits a signed receipt; no state transition is unattributable.
6. **Post-quantum resilience** — authentication and capability tokens use lattice-based schemes resistant to quantum adversaries.

### 1.3 Pattern Integration Map

| Pattern | Primary Safety Role | AMOS Plane Binding |
|---------|-------------------|-------------------|
| MAOS | Commit chokepoint, capability tokens, WAL | `03_CONTROL_PLANE/09_COMMIT` |
| Polos | Decide/act separation, role-based oversight | `03_CONTROL_PLANE/01_TASK_CONTRACT` |
| AgentOS (seL4) | Hardware isolation, formally verified kernel | `04_RUNTIME/01_BOOT` |
| Argentor | WASM sandbox, compliance modules, TEE | `04_RUNTIME/06_EXECUTION` |

---

## 2. MAOS Pattern — Multi-Agent Operating System

### 2.1 Commit Layer

The Commit Layer is the **single chokepoint** through which every agent-initiated external effect must pass. No agent — regardless of privilege — may write to an external sink (file system, network, database, API) without traversing this layer.

```
AGENT_REQUEST
    │
    ▼
┌──────────────────────────────────────┐
│         COMMIT LAYER                 │
│  ┌────────────────────────────────┐  │
│  │  Capability Token Validator    │  │
│  │  (PQC signature + scope check) │  │
│  ├────────────────────────────────┤  │
│  │  Deterministic Security Core   │  │
│  │  (LLM-independent allow/deny)  │  │
│  ├────────────────────────────────┤  │
│  │  Write-Ahead Log Entry         │  │
│  │  (pre-mutation audit record)   │  │
│  ├────────────────────────────────┤  │
│  │  Effect Execution              │  │
│  │  (原子 apply + receipt)        │  │
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘
    │
    ▼
EXTERNAL WORLD
```

### 2.2 Capability Tokens

Every agent action requires a cryptographically signed capability token with the following structure:

```
CapabilityToken {
    agent_id:        AgentIdentifier,        // uniquely identifies the agent instance
    capability_set:  Vec<Capability>,         // scoped permissions (e.g., "fs:read:/data/*")
    not_before:      Timestamp,              // earliest activation
    not_after:       Timestamp,              // expiry (enforced at check time)
    scope:           ScopeBounds,            // domain, regime, H-M-L applicability
    delegation_chain: Vec<AgentIdentifier>,  // who authorized this (transparency)
    signature:       PQCSignature,           // lattice-based signature (ML-DSA-44 or ML-DSA-65)
    nonce:           U128,                   // single-use; prevents replay
    revocation_epoch: Epoch,                 // revocation check epoch
}
```

**Token invariants:**
- Tokens are **non-transferable** — bound to a specific agent identity.
- Tokens are **time-limited** — `not_after` is enforced at the Deterministic Security Core; expired tokens are rejected, not silently extended.
- Tokens are **scope-bounded** — a token for `fs:read` cannot authorize `fs:write`; scope is checked element-wise.
- Tokens carry **delegation chains** — full ancestry of who authorized this capability is inspectable and auditable.
- Tokens use **post-quantum signatures** (see §6) — resistant to Shor's algorithm.

### 2.3 Deterministic Security Core (DSC)

The DSC is a **purely deterministic** (no LLM, no ML) enforcement module that evaluates every mutation request against the active policy set:

```
DECIDE(request, policy_set, capability_token):
    1. Validate token signature (PQC)         → reject on failure
    2. Check token expiry against current epoch → reject if stale
    3. Check scope coverage (element-wise)      → reject on scope mismatch
    4. Check delegation chain depth             → reject if chain exceeds bound
    5. Evaluate policy rules (pure logic)       → deny if any rule denies
    6. Check rate limits and quotas             → deny if exceeded
    7. If all pass: EMIT receipt + ALLOW
    8. If any fail: EMIT receipt + DENY + quarantine signal
```

The DSC is **LLM-independent** — its decisions are fully deterministic given the same inputs. This is the critical safety boundary: the LLM proposes, the DSC disposes.

### 2.4 Sentry + 6 Gateways

The Sentry stands at the outermost boundary of the agent ecosystem, inspecting all inbound traffic:

```
EXTERNAL TRAFFIC
    │
    ▼
┌─────────┐
│  SENTRY │ ← initial classification, rate limiting, adversarial filtering
└────┬────┘
     │
     ├──► Gateway 1: Identity & Authentication (PQC key verification)
     ├──► Gateway 2: Capability Scoping (token scope validation)
     ├──► Gateway 3: Policy Evaluation (rule-set check)
     ├──► Gateway 4: Quota & Rate Enforcement (resource bounding)
     ├──► Gateway 5: Provenance Binding (RSCF trace linkage)
     └──► Gateway 6: Audit Emission (receipt generation)
```

Each gateway is independently deployable and independently auditable. Failure of any gateway **fails closed** — the request is held, not forwarded.

### 2.5 Write-Ahead Log (WAL)

Every mutation is recorded in the WAL **before** execution:

```
WAL_ENTRY {
    entry_id:        WALSequenceNumber,
    agent_id:        AgentIdentifier,
    mutation_intent: IntentDescription,     // what the agent intends to do
    capability_token: CapabilityToken,      // the token presented
    dsc_decision:    Allow | Deny,          // what the DSC decided
    pre_state_hash:  Hash,                  // state before mutation
    post_state_hash: Optional<Hash>,        // state after mutation (filled on success)
    receipt:         SignedReceipt,         // cryptographic proof of the entry
    timestamp:       EpochTimestamp,
}
```

**WAL properties:**
- **Append-only** — entries are never modified after write.
- **Cryptographically chained** — each entry includes the hash of the previous entry (tamper-evident).
- **Flush-before-commit** — the WAL entry is durably persisted before the mutation executes.
- **Rollback source** — on failure, the WAL provides the pre-state hash for recovery.

### 2.6 Security Profiles

| Profile | Use Case | DSC Strictness | Token Lifetime | Delegation Depth | Audit Frequency |
|---------|----------|---------------|----------------|-----------------|-----------------|
| **Standard** | General agent operations | Full policy evaluation | 1 hour | ≤ 3 | Every mutation |
| **Hardened** | High-stakes / consequential effects | Full policy + adversarial review | 15 minutes | ≤ 2 | Every mutation + periodic re-validation |
| **Isolated** | Untrusted / external-facing agents | Maximum restriction, explicit allowlist only | 5 minutes | ≤ 1 (no delegation) | Continuous monitoring |

### 2.7 EU AI Act Alignment

The MAOS pattern directly addresses EU AI Act requirements for general-purpose AI (GPAI) and high-risk systems:

- **Article 52 — Transparency**: Every agent interaction emits an AI-generated content marker via the Sentry; the audit trail is fully attributable.
- **Article 55 — GPAI Obligations**: The DSC serves as the systemic risk mitigation mechanism; its determinism satisfies the "safety assessment" requirement.
- **Annex III — High-Risk Classification**: Brain-interface AI (a core AMOS use case) is classified high-risk; the MAOS Commit Layer provides the required human oversight interception point.
- **Article 14 — Human Oversight**: The Commit Layer's single-chokepoint design provides a natural intervention point where human operators can pause, override, or revoke agent actions.

---

## 3. Polos Pattern — Governed-Agent Mesh

### 3.1 Architecture Principle

Polos enforces a **structural separation between reasoning and execution** through 14 specialized roles organized in a mesh topology. The key invariant: *agents that decide hold no tools; agents that act hold no policy.*

### 3.2 Role Registry

| # | Role | Tools? | Decision Authority | Description |
|---|------|--------|-------------------|-------------|
| 1 | **Planner** | No | Yes | Decomposes goals into task graphs |
| 2 | **Researcher** | Yes (read-only) | No | Gathers evidence; no mutation authority |
| 3 | **Writer** | Yes (write) | No | Executes mutations scoped by capability tokens |
| 4 | **Critic** | No | Yes | Challenges reasoning; can reject or rework |
| 5 | **Guardian** | No | Yes | Safety review; can quarantine or halt |
| 6 | **Auditor** | Yes (read-only) | No | Reads state for compliance verification |
| 7 | **Router** | No | Yes | Assigns tasks to optimal agents |
| 8 | **Synthesizer** | No | Yes | Merges outputs from parallel agents |
| 9 | **Negotiator** | No | Yes | Resolves conflicts between agents |
| 10 | **Sentinel** | No | Yes | Monitors for adversarial injection |
| 11 | **Witness** | Yes (append-only) | No | Appends to audit log; no read of other state |
| 12 | **Referee** | No | Yes | Final arbitration on disputed outcomes |
| 13 | **Constructor** | Yes (scoped write) | No | Builds artifacts under Planner's specification |
| 14 | **Archivist** | Yes (read/write) | No | Manages state lifecycle and archival |

### 3.3 Decide/Act Separation

The structural enforcement of separation:

```
┌─────────────────────────────────────────────────────┐
│                 REASONING TIER (No Tools)            │
│  Planner · Critic · Guardian · Router · Synthesizer  │
│  Negotiator · Sentinel · Referee                     │
│                                                      │
│  These roles produce DECISIONS: plan, approve, deny, │
│  rework, quarantine, route, merge, negotiate.        │
│  They NEVER hold write capabilities.                 │
│  They NEVER execute mutations directly.              │
└────────────────────────────┬────────────────────────┘
                             │ decisions flow down
                             ▼
┌─────────────────────────────────────────────────────┐
│                 EXECUTION TIER (Scoped Tools)         │
│  Researcher · Writer · Auditor · Witness ·           │
│  Constructor · Archivist                             │
│                                                      │
│  These roles execute actions under scoped tokens.    │
│  They NEVER hold discretionary policy authority.     │
│  They execute what the reasoning tier decides.       │
└─────────────────────────────────────────────────────┘
```

### 3.4 Guardian Protocol

Guardians are the safety-critical role with three powers:

1. **Reject** — block a proposed action before execution; emit a rejection receipt.
2. **Rework** — send a task back to the Planner with specific remediation instructions.
3. **Quarantine** — isolate an agent suspected of misalignment; revoke its capability tokens and hold its pending mutations.

```
GUARDIAN_REVIEW(proposed_action):
    if violates_safety_policy(proposed_action):
        REJECT(receipt=emit_rejection_receipt(proposed_action))
    elif violates_scope(proposed_action):
        REWORK(target=PLANNER, instructions=scope_correction)
    elif agent_behavior_suspicious(proposed_action.agent):
        QUARANTINE(agent=proposed_action.agent)
    else:
        APPROVE(receipt=emit_approval_receipt(proposed_action))
```

### 3.5 Bounded Self-Correcting Loops

When a task fails, the system enters a bounded retry loop:

```
SELF_CORRECT(task, max_retries=3):
    attempt = 0
    while attempt < max_retries:
        result = EXECUTE(task)
        if result.status == COMPLETED:
            return result
        elif result.status == FAILED:
            critique = CRITIC.review(task, result.error)
            task = PLANNER.rework(task, critique)
            attempt += 1
    # Exceeded retry bound — escalate to human
    ESCALATE(task, failure_history)
```

**Invariant:** Self-correcting loops are bounded; they never recurse unboundedly; every loop termination produces a receipt.

### 3.6 Model Lineage Diversity

Oversight agents (Critic, Guardian, Referee) must use **different model lineages** than the agents they oversee. This prevents correlated failure modes:

```
OVERSIGHT_CONSTRAINT:
    model_lineage(oversight_agent) ≠ model_lineage(overseen_agent)
    model_family(oversight_agent) ≠ model_family(overseen_agent)
```

If the working agent uses Model A, the Critic uses Model B, and the Guardian uses Model C. This diversity ensures that a systematic vulnerability in one model family does not compromise both execution and oversight.

---

## 4. AgentOS (seL4) Pattern — Formally Verified Capability Security

### 4.1 Core Principle

AgentOS provides **hardware-enforced isolation** for each agent using the formally verified seL4 microkernel as the foundation. Every agent runs in its own isolated address space with explicitly granted capabilities — the principle of least authority enforced at the hardware level.

### 4.2 Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    AGENTOS ARCHITECTURE                    │
│                                                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │  Agent A     │  │  Agent B     │  │  Agent C     │      │
│  │  Address     │  │  Address     │  │  Address     │      │
│  │  Space       │  │  Space       │  │  Space       │      │
│  │  (WASM VM)   │  │  (WASM VM)   │  │  (WASM VM)   │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                 │                 │              │
│         ▼                 ▼                 ▼              │
│  ┌──────────────────────────────────────────────────┐     │
│  │              seL4 Capability Space                 │     │
│  │  (Formally verified microkernel)                  │     │
│  │  - Every IPC requires a valid capability           │     │
│  │  - No agent can forge or escalate capabilities     │     │
│  │  - Information flow is provably confined           │     │
│  └──────────────────────────────────────────────────┘     │
│         │                                                  │
│         ▼                                                  │
│  ┌──────────────────────────────────────────────────┐     │
│  │              Hardware Boundary                     │     │
│  │  MMU-enforced memory isolation                     │     │
│  │  Capability-based I/O access                       │     │
│  └──────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────┘
```

### 4.3 Capability-Based Security

In seL4, every resource is accessed through an unforgeable capability token:

```
AgentCapability {
    object_id:   ObjectIdentifier,   // the resource
    rights:      Rights,             // read | write | execute | grant
    depth:       Nat,                // delegation depth
    cnode_slot:  Slot,               // location in the agent's capability space
}
```

- Agents cannot create capabilities they do not hold.
- Delegation is explicit and auditable.
- Revocation is immediate — the kernel removes the capability from all capability spaces.

### 4.4 WASM Hot-Swap

Agent code is compiled to WebAssembly and loaded into isolated VM instances. Hot-swapping allows upgrading an agent without destroying its address space:

```
HOT_SWAP(agent_id, new_wasm_module):
    1. Pause agent execution at a safe point (capability check)
    2. Verify new module hash against the signed manifest
    3. Replace code pages in the agent's address space
    4. Preserve heap state (if ABI-compatible)
    5. Resume execution
    6. Emit hot-swap receipt with old_hash → new_hash
```

**Invariant:** Hot-swap never escalates capabilities. The new module inherits exactly the capabilities of the old module, never more.

### 4.5 Vibe-Coding: Agent Self-Redesign

AgentOS supports "vibe-coding" — agents that redesign and recompile their own operational environment within their capability bounds:

```
VIBE_CODE(agent, redesign_intent):
    # Agent proposes a modification to its own code
    proposal = agent.generate_module(redesign_intent)
    
    # Validate against capability bounds (cannot self-escalate)
    if not capability_subset(proposal.required_caps, agent.current_caps):
        REJECT("self-redesign would escalate capabilities")
    
    # Compile and hash
    wasm_module = COMPILE(proposal)
    module_hash = SHA3_256(wasm_module)
    
    # Submit to Guardian for review
    GUARDIAN.review(proposal, module_hash)
    
    # If approved: hot-swap
    if GUARDIAN.approved:
        HOT_SWAP(agent.id, wasm_module)
        EMIT Receipt(agent=agent, redesign=proposal, hash=module_hash)
```

**Critical constraint:** Vibe-coding is confined to the agent's existing capability set. An agent cannot use vibe-coding to acquire new capabilities. The Guardian must approve all self-modifications.

---

## 5. Argentor Pattern — Rust/WASM Compliance Runtime

### 5.1 Architecture

Argentor provides a **Rust-based, WASM-sandboxed** agent execution environment with a 2ms overhead target, native compliance modules, and TEE (Trusted Execution Environment) support.

```
┌──────────────────────────────────────────────────────┐
│                 ARGENTOR RUNTIME                      │
│                                                       │
│  ┌──────────────────────────────────────────────┐    │
│  │  Rust Core (zero-cost abstractions)           │    │
│  │  - Capability enforcement                     │    │
│  │  - WASM sandbox management                    │    │
│  │  - Compliance module orchestrator              │    │
│  └──────────────────────────────────────────────┘    │
│                                                       │
│  ┌──────────────┐  ┌──────────────┐                  │
│  │  WASM Agent  │  │  WASM Agent  │  ...             │
│  │  Sandbox #1  │  │  Sandbox #2  │                  │
│  │  (isolated)  │  │  (isolated)  │                  │
│  └──────────────┘  └──────────────┘                  │
│                                                       │
│  ┌──────────────────────────────────────────────┐    │
│  │  Compliance Modules                            │    │
│  │  ┌───────┐ ┌─────────┐ ┌──────────────┐      │    │
│  │  │ GDPR  │ │ ISO     │ │ ISO 42001    │      │    │
│  │  │       │ │ 27001   │ │ (AI Mgmt)    │      │    │
│  │  └───────┘ └─────────┘ └──────────────┘      │    │
│  └──────────────────────────────────────────────┘    │
│                                                       │
│  ┌──────────────────────────────────────────────┐    │
│  │  TEE Layer (optional)                         │    │
│  │  AWS Nitro Enclaves | Intel SGX | AMD SEV-SNP │    │
│  └──────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────┘
```

### 5.2 Supported LLM Backends

Argentor abstracts across 14 LLM backends, providing a uniform agent interface regardless of the underlying model provider:

| # | Backend | Family | Notes |
|---|---------|--------|-------|
| 1 | OpenAI GPT-4o | Commercial | |
| 2 | Anthropic Claude 3.5 | Commercial | |
| 3 | Google Gemini 2.0 | Commercial | |
| 4 | Meta Llama 3.1 (405B) | Open | |
| 5 | Mistral Large 2 | Commercial | |
| 6 | Cohere Command R+ | Commercial | |
| 7 | Amazon Nova | Commercial | |
| 8 | Microsoft Phi-4 | Open | |
| 9 | DeepSeek V3 | Open | |
| 10 | Qwen 2.5 (72B) | Open | |
| 11 | DBRX | Open | |
| 12 | Jamba | Open | |
| 13 | Gemma 2 | Open | |
| 14 | Local/Private (self-hosted) | Any | air-gapped deployment |

### 5.3 Compliance Modules

Each compliance module is a standalone WASM module that can be loaded or unloaded at runtime:

**GDPR Module:**
- Enforces data minimization — agents cannot access data beyond what is strictly necessary.
- Tracks consent status — data processing stops when consent is withdrawn.
- Generates Data Protection Impact Assessment (DPIA) records.
- Supports right to erasure — state deletion propagates through WAL.

**ISO 27001 Module:**
- Maps agent operations to Annex A controls.
- Enforces access control policies aligned with ISMS requirements.
- Produces audit evidence artifacts suitable for certification review.
- Monitors for anomalous access patterns (detect-and-alert).

**ISO 42001 (AI Management System) Module:**
- Enforces AI risk management lifecycle per ISO 42001 clauses.
- Tracks model lineage, training data provenance, and deployment context.
- Supports impact assessments for high-risk AI systems.
- Monitors ongoing performance and fairness metrics.

### 5.4 TEE Support

For the highest security requirements, Argentor can deploy agent sandboxes within hardware-isolated Trusted Execution Environments:

```
TEE_DEPLOY(agent_config):
    1. Select TEE platform (AWS Nitro | Intel SGX | AMD SEV-SNP)
    2. Measure enclave code (remote attestation)
    3. Deploy WASM agent into enclave
    4. Establish encrypted channel between enclave and Commit Layer
    5. Agent operates within TEE — even the host OS cannot observe its state
    6. Remote attestation receipt emitted for external verification
```

**TEE properties:**
- **Confidentiality** — agent memory is encrypted; the host cannot read it.
- **Integrity** — remote attestation proves the code running inside the enclave is exactly what was expected.
- **Isolation** — compromised host OS cannot extract agent secrets.

---

## 6. Post-Quantum Cryptography for Agent Authentication

### 6.1 Threat

Shor's algorithm, executable on a cryptographically relevant quantum computer, breaks RSA, ECDSA, and ECDH. All current agent authentication (which relies on these schemes) would be compromised.

### 6.2 AMOS PQC Migration

AMOS adopts NIST PQC standards (FIPS 203/204/205) for all agent-facing cryptographic operations:

| Primitive | NIST Standard | Use in AMOS |
|-----------|--------------|-------------|
| **ML-KEM** (Kyber) | FIPS 203 | Key encapsulation for encrypted agent channels |
| **ML-DSA** (Dilithium) | FIPS 204 | Digital signatures for capability tokens and receipts |
| **SLH-DSA** (SPHINCS+) | FIPS 205 | Stateless hash-based signatures for long-term audit trails |
| **FN-DSA** (Falcon) | NIST PQC Round 3 | Compact signatures for bandwidth-constrained paths |

### 6.3 Capability Token PQC

Every capability token (§2.2) is signed with ML-DSA-44 (NIST security level 2) or ML-DSA-65 (NIST security level 3), depending on the security profile:

```
Standard profile:  ML-DSA-44  (1,280-byte signature, fast)
Hardened profile:  ML-DSA-65  (1,952-byte signature, stronger)
Isolated profile:  ML-DSA-87  (2,425-byte signature, maximum)
```

### 6.4 Hybrid Mode

During the transition period, AMOS supports hybrid signatures (classical + PQC) to maintain backward compatibility while providing quantum resistance:

```
HYBRID_SIGN(message, classical_key, pqc_key):
    classical_sig = ECDSA_SIGN(message, classical_key)
    pqc_sig = MLDSA_SIGN(message, pqc_key)
    return HybridSignature(classical=classical_sig, pqc=pqc_sig)

HYBRID_VERIFY(message, hybrid_sig, classical_pubkey, pqc_pubkey):
    return ECDSA_VERIFY(message, hybrid_sig.classical, classical_pubkey)
        && MLDSA_VERIFY(message, hybrid_sig.pqc, pqc_pubkey)
```

### 6.5 Audit Trail Longevity

The SLH-DSA (SPHINCS+) hash-based signatures are used exclusively for the WAL audit trail (§2.5) because:
- They are stateless — no counter or key state to manage across decades.
- They are conservative — security rests only on hash function properties.
- They are suitable for archival — audit records signed 20 years ago remain verifiable.

---

## 7. EU AI Act Compliance Integration

### 7.1 Regulatory Timeline

The EU AI Act entered into force August 1, 2024. The obligations for GPAI models (including agents) are **fully applicable from August 2, 2026**. AMOS must be compliant by this date.

### 7.2 Risk Classification for AMOS Agents

| AMOS Agent Type | EU AI Act Risk Level | Key Obligations |
|----------------|---------------------|-----------------|
| Brain-interface cognitive agent | **High-risk** (Annex III) | Conformity assessment, human oversight, transparency, robustness |
| Internal task-planning agent | **Limited risk** | Transparency obligations, AI-generated content marking |
| External-facing conversational agent | **Limited risk** | Disclosure that the user is interacting with AI |
| Research-only observational agent | **Minimal risk** | Voluntary codes of conduct |

### 7.3 Compliance Mapping

| EU AI Act Requirement | AMOS Implementation | Evidence Artifact |
|----------------------|---------------------|-------------------|
| Art. 5 — Prohibited practices | DSC deny rules for manipulative/deceptive behavior | WAL receipt (deny entry) |
| Art. 9 — Risk management | Argentor ISO 42001 compliance module | Compliance audit receipt |
| Art. 10 — Data governance | Argentor GDPR compliance module | DPIA record |
| Art. 11 — Technical documentation | WAL + provenance ledger | Provenance receipt |
| Art. 12 — Record-keeping | WAL append-only chain | WAL chain hash |
| Art. 13 — Transparency | Sentry AI-generated content markers | Sentry emission receipt |
| Art. 14 — Human oversight | Commit Layer single chokepoint | Commit gate receipt |
| Art. 15 — Accuracy, robustness, security | DSC deterministic enforcement | Security profile manifest |
| Art. 52/55 — GPAI obligations | Model lineage diversity + safety assessment | Oversight agent lineage record |

### 7.4 Conformity Assessment Readiness

AMOS maintains a **conformity dossier** that can be produced for EU AI Act assessment:

1. **System description** — this document (AGENT_SAFETY_ARCHITECTURE_2026.md).
2. **Risk assessment** — per-agent risk classification (§7.2).
3. **Testing evidence** — from AMOS test contract (`19_TESTS/TESTS_TEST_CONTRACT.md`).
4. **Human oversight mechanism** — Commit Layer design (§2.1).
5. **Post-market monitoring** — observability plane (`17_OBSERVABILITY/`).
6. **Incident reporting** — WAL receipts and quarantine records.

---

## 8. AMOS Integration — Control Plane Mapping

### 8.1 Pattern-to-Layer Binding

| AMOS Control Plane Layer | Primary Pattern Binding | Integration Mechanism |
|--------------------------|------------------------|-----------------------|
| `01_TASK_CONTRACT` | Polos | Task decomposition through Planner role; bounded self-correcting loops |
| `02_CAPABILITY` | MAOS + AgentOS | PQC-signed capability tokens; seL4 capability space enforcement |
| `03_POLICY` | MAOS DSC + Argentor compliance | Deterministic policy evaluation; GDPR/ISO compliance modules |
| `04_AUTHORITY` | MAOS + Polos | Delegation chains in capability tokens; Guardian authority enforcement |
| `05_PROVENANCE` | MAOS WAL + Argentor | WAL audit trail; provenance receipt signing |
| `06_SEMANTIC_TRANSACTION` | All patterns | Transaction isolation through seL4 address spaces + CAS at commit |
| `07_OBSERVABILITY` | All patterns | Sentry monitoring; audit receipts; Guardian quarantine signals |
| `08_EFFECTS` | MAOS Commit Layer | Single chokepoint for all external effects |
| `09_COMMIT` | MAOS + AgentOS | WAL flush-before-commit; CAS validation at commit gate |
| `10_EXPOSURE` | MAOS Sentry + 6 Gateways | Outbound traffic inspection and classification |
| `11_REPLAY` | MAOS WAL + Polos Witness | WAL replay for state reconstruction |
| `12_ROLLBACK` | MAOS WAL + Polos Guardian | Pre-state hashes from WAL; Guardian-initiated rollback |

### 8.2 Invariant Preservation

AMOS core invariants are preserved across all patterns:

- **CAPABILITY ≠ AUTHORITY** — capability tokens (MAOS) do not alone authorize; authority references must be epoch-valid (checked by DSC).
- **PROPOSAL ≠ COMMIT** — agents propose through Polos reasoning tier; only the Commit Layer (MAOS) commits.
- **OBSERVED ≠ CURRENT** — MVCC snapshot isolation (AgentOS) ensures reads are consistent; AgentOS address space isolation prevents stale-state contamination.
- **TEST_PASS ≠ TRUTH** — Argentor compliance modules provide evidence, not proof; full compliance requires ongoing monitoring.
- **LATEST ≠ AUTHORITATIVE** — WAL chain provides authoritative history; latest state is only authoritative if the WAL chain is intact.
- **MODEL ≠ DEPLOYED_RUNTIME** — seL4 formally verified kernel provides runtime guarantees beyond model-level reasoning.
- **DOCUMENTED ≠ IMPLEMENTED** — this document is AMOS_MODEL; implementation requires executed receipts per the promotion-gate checklist.

---

## 9. Invariants

- **SAFETY-01:** Every external effect traverses the Commit Layer (single chokepoint).
- **SAFETY-02:** Every capability token is PQC-signed, time-limited, and scope-bounded.
- **SAFETY-03:** The Deterministic Security Core is LLM-independent; its decisions are fully deterministic.
- **SAFETY-04:** Reasoning agents hold no tools; execution agents hold no discretionary policy.
- **SAFETY-05:** Guardian quarantine is immediate and irrecoverable without human intervention.
- **SAFETY-06:** Self-correcting loops are bounded; unbounded recursion is impossible by construction.
- **SAFETY-07:** Oversight agents use different model lineages than agents they oversee.
- **SAFETY-08:** seL4 address space isolation is hardware-enforced, not software-enforced.
- **SAFETY-09:** WASM hot-swap never escalates capabilities.
- **SAFETY-10:** Vibe-coding is confined to the agent's existing capability set.
- **SAFETY-11:** All WAL entries are append-only, cryptographically chained, and flush-before-commit.
- **SAFETY-12:** PQC signatures resist quantum adversaries (NIST FIPS 203/204/205).
- **SAFETY-13:** EU AI Act obligations are mapped to specific AMOS mechanisms with evidence artifacts.
- **SAFETY-14:** Fail closed on any gateway, DSC, or capability validation failure.

---

## 10. Falsifiers

- **F1:** An agent produces an external effect without a Commit Layer receipt.
- **F2:** A capability token without a valid PQC signature is accepted.
- **F3:** A reasoning-tier agent successfully executes a write tool.
- **F4:** The DSC produces different allow/deny decisions for identical inputs.
- **F5:** An agent successfully vibe-codes a capability escalation.
- **F6:** Two oversight agents share the same model lineage.
- **F7:** A WAL entry is modified after initial write.
- **F8:** The EU AI Act conformity dossier cannot be produced from existing artifacts.
- **F9:** A WASM hot-swap results in an agent holding more capabilities than before.
- **F10:** A seL4 capability is forged or escalated through software alone.

---

## 11. Promotion-Gate Checklist

- [ ] Typed schema bound to each pattern's data structures
- [ ] Identity + versioning implemented for all agent roles
- [ ] Negative cases covered (missing · malformed · stale · unauthorized · quantum-adversary input)
- [ ] Provenance edges persisted and validated for all patterns
- [ ] Rollback basin demonstrated for Commit Layer and WAL
- [ ] Executed validation receipt specific to this architecture
- [ ] Unresolved critical gaps registered as UNKNOWN/GAP (visible)
- [ ] EU AI Act conformity dossier populated with evidence artifacts
- [ ] PQC migration plan with timeline and hybrid-mode fallback

---

## 12. Cross-Vault References

- Control plane contract — [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTROL_PLANE_CONTRACT]]
- Capability contract — [[03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_CONTRACT|CAPABILITY_CONTRACT]]
- Authz engine — [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]
- Commit layer — [[03_CONTROL_PLANE/09_COMMIT/CONTROL_PLANE_COMMIT_CONTRACT|CONTROL_PLANE_COMMIT_CONTRACT]]
- Effects contract — [[03_CONTROL_PLANE/08_EFFECTS/CONTROL_PLANE_EFFECTS_CONTRACT|CONTROL_PLANE_EFFECTS_CONTRACT]]
- Observability — [[03_CONTROL_PLANE/07_OBSERVABILITY/CONTROL_PLANE_OBSERVABILITY_CONTRACT|CONTROL_PLANE_OBSERVABILITY_CONTRACT]]
- Rollback contract — [[03_CONTROL_PLANE/12_ROLLBACK/CONTROL_PLANE_ROLLBACK_CONTRACT|CONTROL_PLANE_ROLLBACK_CONTRACT]]
- Runtime contract — [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|RUNTIME_RUNTIME_CONTRACT]]
- CAS version vector — [[04_RUNTIME/CAS_VERSION_VECTOR|CAS_VERSION_VECTOR]]
- Multi-epoch coordination — [[04_RUNTIME/MULTI_EPOCH_COORDINATION|MULTI_EPOCH_COORDINATION]]
- MVCC causal concurrency — [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]]
- Test contract — [[19_TESTS/TESTS_TEST_CONTRACT|TESTS_TEST_CONTRACT]]
- AMOS core laws — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Trang Framework — [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: cp_03_agent_safety_architecture_2026_md
node_type: specification
path: 03_CONTROL_PLANE/AGENT_SAFETY_ARCHITECTURE_2026.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
