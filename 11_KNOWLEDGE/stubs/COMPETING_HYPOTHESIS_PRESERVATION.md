---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Competing Hypothesis Preservation
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

# COMPETING HYPOTHESIS PRESERVATION

## 0. Status

Knowledge-plane artifact. `AMOS_MODEL` · `CONDITIONAL` · implementation `PARTIAL`.

This is a **governing invariant** sourced from the AMOS Core Laws (L1 — Epistemic, L6 — Uncertainty/Sensitivity) and the MECE architecture's governed end-to-end loop. It is a constitutional requirement that competing explanations for an observation must be preserved until discriminating evidence exists to resolve them.

## 1. Purpose

`COMPETING HYPOTHESIS PRESERVATION` mandates that when multiple hypotheses explain the same evidence, none may be silently discarded, merged, or promoted to canonical truth merely because one is more convenient, faster, or more fluent. All competing explanations must remain visible in the RSCF record until a discriminating observation, proof, or falsification event resolves the competition.

This invariant exists because premature hypothesis collapse — selecting one explanation before evidence distinguishes it — produces **confidence inflation** and **silent knowledge loss**. The system would commit to a possibly-wrong model without the ability to detect or recover from the error.

### Failure modes prevented

- `CONFIDENCE_INFLATION` — a single hypothesis is treated as certain when alternatives remain viable.
- `SILENT_PARTIAL_COMMIT` — a knowledge claim is committed based on a collapsed hypothesis without recording the alternatives that were discarded.
- `REGIME_DRIFT` — a hypothesis validated in one regime is silently promoted to another regime where it may not hold.

## 2. Definition

The invariant is formalized in the AMOS architecture's RSCF reasoning architecture, which requires every decision-relevant claim to carry:

```text
competing explanations
falsifiers
invalidation conditions
confidence ceiling
```

And in the governed end-to-end loop:

```text
→ REASON
→ PRESERVE COMPETING HYPOTHESES
→ SIMULATE / PLAN
```

The "PRESERVE COMPETING HYPOTHESES" step is an explicit, mandatory phase — not an optional annotation. It sits between reasoning and simulation/planning, ensuring that the downstream phases operate on the full hypothesis space, not a prematurely collapsed subset.

**Competing hypothesis** = an alternative explanation for the same evidence set that has not been falsified, merged, or resolved by discriminating evidence. A hypothesis remains "competing" as long as:

1. It is consistent with the observed evidence.
2. No discriminating observation has been made that falsifies it while confirming another.
3. Its confidence ceiling has not been independently reduced below the relevance threshold.

## 3. AMOS Architecture Context

| Domain | Planes | Role |
|---|---|---|
| **C — Cognitive Capability & Orchestration** | `05_COGNITIVE_ORGANISM`, `25_COGNITIVE_MATRIX` | The cognitive loop's interpretation/reasoning group generates and preserves hypotheses |
| **D — Information, Memory, State & Model Substrate** | `11_KNOWLEDGE`, `13_MODELS` | Knowledge and model substrates store competing explanations with full RSCF metadata |
| **F — Assurance, Learning & Lifecycle Evidence** | `17_OBSERVABILITY`, `19_TESTS` | Observability and tests provide discriminating evidence that can resolve competitions |

The cognitive-organism functional partition explicitly includes "competing hypotheses" in the INTERPRETATION / REASONING group:

```text
INTERPRETATION / REASONING
  cognition · structural reasoning · competing hypotheses · causal analysis · simulation
```

## 4. Invariants / Rules

1. **INV-CHP-01**: `∀ evidence_set E, |Hypotheses(E)| > 1 ∧ ¬DiscriminatingEvidence(E) ⇒ PreserveAll(Hypotheses(E))`
2. **INV-CHP-02**: A hypothesis may only be retired when (a) falsified by discriminating evidence, (b) merged with another via governed synthesis, or (c) its confidence ceiling drops below the relevance threshold — and the retirement must be recorded.
3. **INV-CHP-03**: Conclusion confidence ≤ weakest load-bearing premise; if premises depend on an unresolved hypothesis, the conclusion carries the full uncertainty.
4. **INV-CHP-04**: No hypothesis may be silently promoted from `COMPETING` to `DECISION` class; promotion requires explicit evidence closure.
5. **INV-CHP-05**: Cross-regime transfer of a hypothesis requires an explicit bridge; a hypothesis resolved in one regime remains `COMPETING` in another until independently resolved.
6. **INV-CHP-06**: The `UNKNOWN/GAP` state is itself a valid competing hypothesis and must not be silently replaced with a fabricated explanation.

## 5. Relationships

- **Governs**: [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] — the cognitive loop's reasoning phase.
- **Constrained by**: [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]] — L1 (Epistemic), L6 (Uncertainty/Sensitivity).
- **Stored in**: [[11_KNOWLEDGE/11_KNOWLEDGE_README|KNOWLEDGE_README]] — knowledge substrate preserves competing explanations with RSCF metadata.
- **Resolved by**: [[17_OBSERVABILITY/17_OBSERVABILITY_README|17_OBSERVABILITY_README]] · [[19_TESTS/19_TESTS_README|19_TESTS_README]] — discriminating evidence from observation and testing.
- **Related concept**: [[11_KNOWLEDGE/stubs/MODEL_IDENTITY_PRESERVATION|MODEL_IDENTITY_PRESERVATION]] — model identity must be preserved across hypothesis competition; models are not silently merged.
- **Architecture reference**: [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]] — Section 6 (governed loop), Section 10 (RSCF).

## 6. What Happens When Violated

| Violation | Consequence |
|---|---|
| Hypothesis silently discarded | `CONFIDENCE_INFLATION` — downstream decisions built on a false singleton |
| Premature collapse to one hypothesis | `SILENT_PARTIAL_COMMIT` — committed effect based on unresolved epistemic state |
| `UNKNOWN/GAP` replaced with fabrication | `UNKNOWN_AS_VALID` — missing evidence treated as confirmed evidence |
| Cross-regime hypothesis transfer without bridge | `REGIME_DRIFT` — hypothesis valid in one context applied in another where it fails |

In all cases, the system must **fail closed** for consequential paths: the effect is held, the competing hypothesis set is restored, and a receipt recording the violation is emitted.

## 7. Worked Semantics

Given a reasoning operation within the Knowledge plane that produces hypotheses:

1. **Admit** — resolve the evidence set and prior hypothesis state by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.
2. **Generate** — cognitive reasoning produces candidate hypotheses, each typed with RSCF metadata (scope, regime, confidence ceiling, falsifiers).
3. **Preserve** — all hypotheses consistent with evidence are retained; none is silently discarded.
4. **Check for discriminating evidence** — if new observation or test result falsifies some hypotheses while confirming others, record the resolution event.
5. **Propose** — any downstream decision based on the hypothesis set carries the full uncertainty envelope (`PROPOSAL ≠ COMMIT`).
6. **Commit or hold** — on any unresolved load-bearing hypothesis: preserve unaffected state, mark the conclusion as `COMPETING`, record receipt.

## 8. Promotion-Gate Checklist

- [ ] typed schema bound to this artifact
- [ ] identity + versioning implemented
- [ ] negative cases covered (missing · malformed · stale · unauthorized input)
- [ ] provenance edges persisted and validated
- [ ] rollback basin demonstrated for consequential effects
- [ ] executed validation receipt specific to this artifact
- [ ] unresolved critical gaps registered as `UNKNOWN/GAP` (visible)

## 9. Validation

No artifact-specific executor yet; executed OS validators exist as pattern ([[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]). Required tests before promotion: identity, type-contract, negative-case (missing/malformed/stale input), authority boundary, rollback.

## 10. Gaps

Implementation binding, empirical validation, and cross-artifact consistency checks remain `OPEN` (`UNKNOWN/GAP`). The MURK reasoning engine (19-primitive Absolute Logic kernel) provides the structural framework for hypothesis generation and collapse detection, but OS-wide closure of the hypothesis preservation enforcement chain is not yet established.

## 11. Falsifiers

- **F1**: canonical source contradicts declared semantics.
- **F2**: executed test violates a stated invariant (e.g., a hypothesis is silently discarded without a resolution event).
- **F3**: artifact promotes `UNKNOWN` to `PASS`.

## 12. RSCF Status

```text
state:          DERIVED
claim_class:    DERIVED
provenance:     AMOS_corpus
scope:          AMOS_general
```

This artifact is a `DERIVED` knowledge-plane representation of the `SOURCE_CLAIM` invariant in [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]] (L1, L6). It does not promote to `SOURCE_CLAIM` without governed successor evidence.

## 13. Cross-Plane Bindings

- Governed by canon — [[01_CANON/01_CANON_README|01_CANON_README]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Kernel interaction — [[02_KERNEL/02_KERNEL_README|KERNEL_README]]
- Control-plane gates — [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/17_OBSERVABILITY_README|17_OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/20_OPERATIONS_README|20_OPERATIONS_README]]
