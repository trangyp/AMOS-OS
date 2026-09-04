---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 10 Rscf Moc
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

# 10 Rscf — Map of Content

## 0. Status

RSCF (Reasoning-with-Source-Claims-and-Falsifiers) schema family MOC. AMOS_MODEL · CONDITIONAL · implementation PARTIAL.
All six schema slots are present and typed; each is currently an `ADD_ONLY` placeholder (`canonical_status UNKNOWN/GAP`, `implementation NOT_ESTABLISHED`). This MOC maps how the six schemas compose into the RSCF epistemic guardrails. `PLACEHOLDER != IMPLEMENTED`, `DOCUMENTED != ENFORCED`, `UNKNOWN/GAP != PASS`.

## 1. Purpose

The RSCF family defines the typed schemas for **reasoning over source claims, evidence, competing hypotheses, proof, and falsifiers**. Together they implement the AMOS epistemic discipline: every claim is classified, scoped, premised, evidence-bound, provenance-stamped, and falsifiable — and competing hypotheses remain visible until discriminating evidence exists.

**Path:** `16_SCHEMAS/10_RSCF` · **Files:** 6 · **Subdirectories:** 0

## 2. The Six RSCF Schemas

| Schema | Defines |
|---|---|
| [[16_SCHEMAS/10_RSCF/framework_node.schema|framework_node.schema]] | The core framework node: claim, epistemic class, H/M/L, premises, evidence, provenance, scope, regime, dependencies, competing hypotheses, falsifiers, confidence ceiling, consequence, status |
| [[16_SCHEMAS/10_RSCF/proof_capsule.schema|proof_capsule.schema]] | A self-contained proof-capsule: the bounded, verifiable justification supporting a claim's promotion |
| [[16_SCHEMAS/10_RSCF/causal_epoch.schema|causal_epoch.schema]] | Causal ordering / finality context — which causal epoch a claim/state belongs to |
| [[16_SCHEMAS/10_RSCF/provenance_topology.schema|provenance_topology.schema]] | Ancestry, transformation, and correlation topology — lineage that defeats provenance laundering |
| [[16_SCHEMAS/10_RSCF/competing_hypothesis.schema|competing_hypothesis.schema]] | Typed representation of competing hypotheses H1/H2 with support and falsifiers; no fabricated convergence |
| [[16_SCHEMAS/10_RSCF/rscf_transaction.schema|rscf_transaction.schema]] | Atomic multi-RSCF transaction semantics — committing a proposal across a load-bearing set of RSCFs |

## 3. How the Schemas Compose

The six schemas compose along the RSCF reasoning pipeline:

```text
FRAMEWORK_NODE
   │  (claim + class + scope + regime + dependencies)
   ▼
PROOF_CAPSULE
   │  (verifiable justification for promotion)
   ▼
CAUSAL_EPOCH + PROVENANCE_TOPOLOGY
   │  (ordering context + ancestry/transformation lineage)
   ▼
COMPETING_HYPOTHESIS
   │  (H1/H2 preserved until evidence discriminates)
   ▼
RSCF_TRANSACTION
   │  (atomic multi-RSCF commit)
   ▼
COMMITTED/HELD (receipt)
```

Composition invariants:

- **Atomic multi-RSCF** — where a mutation depends on RSCF_A + RSCF_B + RSCF_C, `VALID(A) ∧ VALID(B) ∧ VALID(C)` must hold at the relevant validation point; a single `UNKNOWN` load-bearing RSCF ⇒ HOLD, not partial commit.
- **Causal epochs distinct** — `state_version ≠ causal_epoch ≠ policy_epoch ≠ provenance_epoch` unless an explicit mapping licenses equivalence.
- **Provenance union** — `Prov(composed) ⊇ ∪ Prov(inputs)`; ancestry is retained, transformation ≠ new independent origin.
- **Local finality requires proof** — demonstrated dependency closure may avoid coordination; assumed independence may not.

## 4. Epistemic Guardrails

The RSCF family enforces the plane's core guardrails:

- **`UNKNOWN/GAP != PASS`** — critical gaps are recorded and remain visible; never silently promoted.
- **Confidence ceiling** — confidence of any conclusion ≤ confidence of its weakest load-bearing premise (ceiling 0.95).
- **Competing hypotheses preserved** — `COMPETING` remains visible when evidence does not discriminate; no fabricated convergence.
- **Selective invalidation** — failure invalidates dependent descendants (e.g. stale jurisdiction ⇒ dependent legal conclusions only).
- **`CAPABILITY != AUTHORITY`** — a valid proof/framework node does not, by itself, authorize consequential action; authority_ref must be epoch-valid at commit time.
- **Causal firewall** — no promotion across causal levels without evidence appropriate to the target type.

## 5. MECE Gap Callout — UNKNOWN/GAP

The RSCF family is present and typed. However, **executable binding for each schema is NOT established**:

> [!WARNING] UNKNOWN/GAP — RSCF execution not established
> - Executed RSCF schema parser/validator per schema — `UNKNOWN/GAP`
> - Executed atomic multi-RSCF commit engine (`rscf_transaction`) — `UNKNOWN/GAP`
> - Executed causal epoch finalization — `UNKNOWN/GAP`
> - Executed provenance-topology / proof-capsule validation — `UNKNOWN/GAP`
> - Artifact-specific executed validation receipts — `UNKNOWN/GAP`

The six slots being addressable does **not** constitute canon, validity, or runtime enforcement.

## 6. Validation

No RSCF-specific executor yet. Existing executed OS validators cited as pattern (not as evidence for these schemas): [[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]] (19/19) · [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]] (17/17). `rscf_transaction.schema` links a canonical-law reference — [[01_CANON/01_CORE_LAWS/ATOMIC_MULTI_RSCF|ATOMIC_MULTI_RSCF]] — and validation receipt — [[01_CANON/01_CORE_LAWS/ATOMIC_MULTI_RSCF_VALIDATION_RECEIPT|ATOMIC_MULTI_RSCF_VALIDATION_RECEIPT]] — which are the governing law references for that schema's transaction semantics.

## 7. Falsifiers

- F1: a schema's declared semantics contradict canonical law.
- F2: an executed test violates a stated RSCF invariant (atomicity, selectivity, confidence ceiling).
- F3: a schema promotes `UNKNOWN/GAP` to PASS without evidence.
- F4: competing hypotheses are silently collapsed into a single belief without discriminating evidence.

## 8. Cross-plane Bindings

- Schemas plane — [[16_SCHEMAS/16_SCHEMAS_MOC|16_SCHEMAS_MOC]] (parent)
- RSCF law — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY (LAW_HIERARCHY)]] · [[01_CANON/01_CORE_LAWS/L17_RSCF|L17_RSCF]] · [[01_CANON/01_CORE_LAWS/ATOMIC_MULTI_RSCF|ATOMIC_MULTI_RSCF]]
- Kernel — [[02_KERNEL/K_ATOMIC_MULTI_RSCF|K_ATOMIC_MULTI_RSCF]]
- Control-plane gates — [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/17_OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/20_OPERATIONS_README|OPERATIONS_README]]

## 9. Promotion-Gate Checklist

- [ ] typed schema bound to each RSCF schema
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] atomic multi-RSCF commit exercised (rscf_transaction)
- [ ] executed validation receipt specific to each schema
- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)

______________________________________________________________________

**Parent:** [[16_SCHEMAS/16_SCHEMAS_MOC|16_SCHEMAS_MOC]]
