---
tags: [amos-general]
---
# AMOS Infrastructure Layer — Agent Architecture Test / Fix / Rerun Record

**Date:** 2026-08-25  
**Origin architect / steward:** Trang Phan  
**Runtime interpretation:** AMOS Full Brain OS + AMOS infrastructure/control-plane boundary  
**Conclusion class:** CONDITIONAL / IMPROVED / EXECUTION_GAP

---

## 1. Architecture Boundary

AMOS is treated as the infrastructure/control plane above the cognitive and domain layers:

```text
User / System Authority
        ↓
AMOS Infrastructure / Control Plane
        ↓
AMOS Full Brain OS
        ↓
Specialist Agents / Skills
        ↓
Tools / External Effect Executors
```

Full Brain OS and specialist agents may:

- reason;
- plan;
- retrieve;
- synthesize;
- stage proposals;
- create candidate evidence;
- request effects.

They do **not** independently own:

- durable commit authority;
- canon admission;
- final authorization;
- release/finality;
- authority issuance;
- irreversible effect approval.

Those remain infrastructure responsibilities.

---

## 2. Governing AMOS Contracts

The infrastructure layer should own or validate at minimum:

- `TASK_CONTRACT`
- `AUTHORITY_WITNESS`
- `OBSERVABILITY_ENVELOPE`
- `EVIDENCE_BUNDLE`
- `OBSERVED_READ_SET`
- `EFFECT_INTENT`
- `PROVENANCE_CAPSULE`
- `RSCF_STATE`
- `COMMIT_RESULT`
- rollback / recovery state
- validation epoch / freshness state

Core rule:

```text
Capability != Authority
Proposal != Admission
Execution != Commit
Structural consistency != Empirical validity
```

---

## 3. GitHub Defect Found

Repository:

```text
trangyp/AMOS-SYSTEM
```

A concrete constructor-contract defect was identified in the agent layer.

Several repository-aware agents called:

```python
super().__init__(name, repo_root)
```

while the shared base `Agent` constructor accepted only:

```python
Agent(name)
```

This could cause agent construction and registry initialization to fail before orchestration begins.

---

## 4. First Repair

The base agent contract was changed conceptually to:

```python
Agent(name, repo_root=None)
```

This preserves compatibility with name-only agents while supporting repository-aware agents.

Focused regression coverage was added for:

- `CodeAgent`
- `PlannerAgent`
- `RefactorAgent`
- `RepairAgent`
- `ResearchAgent`
- `DefaultAgent`

A local focused contract rerun previously produced:

```text
1 passed
```

That result is scoped only to the focused constructor contract.

---

## 5. Stale-Branch Detection

The first repair branch was later found to have diverged from `main`:

```text
ahead: 4 commits
behind: 5 commits
```

The repair was therefore **not** promoted from the stale branch.

A fresh branch was created from current `main`:

```text
amos-infra-architecture-20260824-v2
```

This preserved the repair while avoiding stale-state promotion.

---

## 6. ResearchAgent Governance Repair

The original `ResearchAgent` behavior treated external inputs too optimistically.

It could report external material as:

```text
processed
mapped to canon
```

without a separate evidence-admission or control-plane decision.

This violates the intended AMOS infrastructure boundary.

The hardened behavior now treats research outputs as candidate evidence.

Required semantics:

```text
status = proposed
admission_state = pending_control_plane
commit_authority = false
```

Additional rules:

- reject research input without source identity;
- retain explicit source/provenance metadata;
- do not silently default mapping target to admitted canon;
- distinguish mapping from admission;
- preserve external-source ancestry;
- require infrastructure validation before durable knowledge promotion.

---

## 7. Agent Registry Regressions

Additional regression checks were added around:

- construction of the full `AgentRegistry`;
- preservation of agent names and repository roots;
- routing of research-mode work to `ResearchAgent`;
- research evidence remaining pending rather than self-admitted.

This changes the architecture from merely “many agent classes exist” toward:

```text
typed contract
→ constructible agent
→ governed routing
→ evidence staging
→ infrastructure admission
```

---

## 8. CI Test / Fix / Rerun Evidence

A focused GitHub Actions lane was added for the governed agent contracts.

### Run 1

GitHub Actions run:

```text
32753263687
```

Result:

```text
FAILURE
```

However, no step-level execution evidence was exposed.

Therefore it was not valid to classify the cause as a Python-test failure.

### Discriminating repair

The hypothesis that third-party Actions caused the failure was tested.

The workflow was simplified to remove:

- `actions/checkout`
- `actions/setup-python`

and use runner-native:

- `git`
- `python`

without weakening the test assertions.

### Run 2

GitHub Actions run:

```text
32753461529
```

Result:

```text
FAILURE
```

Again, failure occurred before usable step-level evidence was exposed.

### Current CI conclusion

```text
EXECUTION_GAP
```

The evidence currently supports:

- workflow/run failure observed;
- cause not yet localized to AMOS Python tests;
- focused tests remain encoded;
- no green result is fabricated;
- assertions were not weakened to manufacture a pass.

---

## 9. Open-Source Interoperability Layer

Open-source tools and standards should be used as interoperability/support layers, not silently promoted into AMOS canon.

### W3C PROV

Candidate use:

- provenance interchange;
- entity/activity/agent representation;
- lineage export/import;
- external provenance compatibility.

AMOS retains additional semantics for:

- RSCF dependencies;
- ancestry independence;
- regime;
- freshness;
- scope;
- confidence ceilings.

### OpenTelemetry

Candidate use:

- traces;
- metrics;
- logs;
- resources;
- span context;
- exporter/collector integration.

AMOS retains infrastructure-specific semantics for:

- authority;
- semantic transaction state;
- effect binding;
- finality;
- commit status.

### Open Policy Agent (OPA)

Candidate use:

- deterministic policy decision substrate;
- policy distribution;
- policy query/evaluation;
- decision logging.

OPA must not replace AMOS-specific:

- authority witnesses;
- causal priority;
- freshness;
- observed-read-set validation;
- semantic transactions;
- effect authorization.

### SLSA / in-toto / Sigstore

Candidate use:

- artifact provenance;
- supply-chain attestations;
- build/source identity;
- CI artifact signing;
- release verification.

AMOS should bind these attestations into its own provenance and release state rather than treating them as sufficient proof of system correctness.

---

## 10. Drive Research Material Incorporated

The architecture direction is consistent with the AMOS execution-plan material that prioritizes:

- bounded agents;
- deterministic infrastructure gates;
- authoritative typed state;
- persistent memory;
- executable RSCF;
- provenance completeness;
- authority freshness;
- atomic transactions;
- rollback;
- security;
- regression;
- reproducibility.

Additional Drive research on **Code as Agent Harness** supports the shift from descriptive agent abstractions toward:

- executable state;
- code as operational substrate;
- test-based verification;
- runtime feedback;
- shared repositories;
- memory;
- tools;
- multi-agent coordination;
- human oversight.

Research on **JustAct+** supports separating:

```text
actor proposal/action
```

from:

```text
policy-regulated permission / justification / audit
```

This maps well onto the AMOS separation between specialist agents and infrastructure authority.

---

## 11. Skill Architecture Direction

AMOS Skills should remain compact domain capability packages.

They should produce:

- structured observations;
- source-grounded evidence;
- typed derivations;
- candidate decisions;
- proposed actions;
- explicit uncertainty;
- falsifiers.

Skills should not independently own:

- global authority;
- durable state;
- canon admission;
- final commit;
- cross-skill transaction finality.

Recommended flow:

```text
Skill Input
→ Skill Evidence / Proposal
→ Infrastructure Validation
→ RSCF / Provenance Binding
→ Authority / Freshness Check
→ Commit or Reject
```

---

## 12. Agent Architecture Direction

Recommended agent contract:

```text
Agent
├── identity
├── role
├── repo_root / environment scope
├── capability manifest
├── authority ceiling
├── input contract
├── output contract
├── evidence requirements
├── provenance requirements
├── observability hooks
├── failure states
└── no implicit commit authority
```

Recommended separation:

```text
Planner      → proposes plans
Researcher   → proposes evidence
Coder        → proposes code changes
Repairer     → proposes repairs
Reviewer     → produces challenge evidence
Safety       → produces risk findings
Supervisor   → coordinates cognitive work
Infrastructure → validates / authorizes / commits
```

---

## 13. Architecture Enhancements Still Needed

High-priority unresolved gates:

- [ ] CI runner exposes step-level evidence.
- [ ] Focused agent-contract tests pass in an external runner.
- [ ] Full repository regression passes.
- [ ] Cross-repository architecture-conformance CI.
- [ ] Real OPA integration.
- [ ] OpenTelemetry collector/export pipeline.
- [ ] SLSA/in-toto/Sigstore release attestation.
- [ ] Durable infrastructure release ledger.
- [ ] Receiver-attested completion receipts.
- [ ] End-to-end deterministic/replay validation where applicable.
- [ ] Host runtime + Python engines + agent registry + MD brain replay test.
- [ ] Explicit agent capability manifests.
- [ ] Explicit tool/effect authorization envelopes.
- [ ] Persistent failure evidence and rollback validation.
- [ ] Skill-to-agent-to-infrastructure ABI conformance tests.

---

## 14. Promotion Gate

Do not promote an architecture change merely because it is coherent.

Use:

```text
ArchitectureCompatible
AND ContractCompatible
AND HardInvariantsPass
AND FocusedTestsPass
AND RegressionPass
AND ProvenanceValid
AND AuthorityValid
AND FreshnessValid
AND RollbackAvailable
```

For high-impact or durable effects, also require:

```text
ObservabilityComplete
AND EffectBound
AND CommitAuthorized
```

---

## 15. Current State

### VERIFIED / observed

- constructor-contract mismatch existed;
- a compatibility repair was defined;
- stale-branch divergence was detected;
- repair was restaged from newer `main`;
- ResearchAgent admission semantics were hardened;
- registry/research regressions were added;
- two GitHub Actions runs failed before useful step-level evidence was available.

### DERIVED

- AMOS should keep durable authority in infrastructure rather than cognitive/domain agents;
- research and Skill outputs should be staged before admission;
- open-source standards are best treated as adapters/interoperability layers around AMOS-specific semantics.

### UNKNOWN / GAP

- whether the focused branch tests pass in GitHub Actions;
- why the Actions jobs fail before step-level evidence;
- full repository regression state;
- cross-runtime replay correctness;
- production-readiness of the architecture.

---

## 16. Conclusion

AMOS is becoming stronger when development moves from:

```text
more concepts
→ more executable contracts
→ more evidence
→ stronger authority boundaries
→ testable state
→ controlled commit
```

rather than simply increasing the number of Skills or agents.

The next high-information step is:

```text
repair CI execution plane
→ run focused contracts
→ run registry tests
→ run full regression
→ inspect failures
→ minimal repair
→ rerun
→ only then promote
```

**Conclusion class:** `CONDITIONAL / IMPROVED / EXECUTION_GAP`
