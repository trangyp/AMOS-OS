---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Cross Domain Tensor Composition Governor Workflow
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

# Workflow: Cross-Domain Tensor Composition Governor

## Identity

Origin architect: **Trang Phan**. Domain: workflow. Parent: none. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## Preconditions

- The `amos-cross-domain-tensor-composition-governor` skill exists and is loaded.
- The `amos-cross-domain-tensor-composition-governor-agent` agent is available and has valid content_hash.
- The query involves composition across two or more AMOS domains (C01-C12).
- All required vault sources are accessible ([[11_KNOWLEDGE/TENSOR_CONTRACTS|TENSOR_CONTRACTS]].md, domain master knowledge files).
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).
- The domain axis registry is available for semantic compatibility checks.

## Steps

1. **Intake**: Identify the problem and confirm it matches the Cross-Domain Tensor Composition Governor scope.

   - Classify the query: identify source domains (C01-C12) involved
   - Identify the tensors being composed (T_R, T_F, T_E, T_C, T_G, T_M)
   - Identify the composition operation (merge, join, propagate, infer)
   - Gate: `scope_confirmed` — query spans 2+ domains; fail closed if intra-domain

1. **Axis Compatibility Check**: Validate that shared axes between source domain tensors are semantically compatible.

   - For each shared axis (scope, regime, causal_level, time, observer, provenance, confidence, consequence):
     - Look up axis semantics in each source domain's master knowledge
     - Check semantic compatibility (not lexical identity)
     - Flag same-name-different-meaning collisions
   - Gate: `axes_compatible` — all shared axes verified; collisions flagged; composition blocked if unresolved

1. **Bridge Classification**: Classify the type of cross-domain bridge being attempted.

   - Determine bridge type: ANALOGY / ISOMORPHISM / CAUSAL / INFORMATIONAL / STRUCTURAL
   - Assign confidence ceiling based on bridge type (≤0.50 / ≤0.95 / ≤0.80 / ≤0.60 / ≤0.55)
   - Record bridge type in provenance
   - Gate: `bridge_classified` — bridge type identified and confidence ceiling assigned

1. **Epistemic Overreach Detection**: Detect cross-domain epistemic overreach.

   - Check for class promotion (MODEL in domain A → VERIFIED in domain B)
   - Check for scope expansion (claim used beyond its declared scope in target domain)
   - Check for regime mismatch (claim valid in regime R_A used in regime R_B where R_A ∩ R_B = ∅)
   - Check for falsifier neglect (falsifiers from domain A not carried to domain B)
   - Gate: `overreach_checked` — no overreach detected; violations flagged and composition blocked if critical

1. **Weakest Edge Enforcement**: Enforce the weakest-load-bearing-edge confidence rule.

   - Identify all load-bearing premises across all domain boundaries
   - Compute min(confidence) across all load-bearing premises
   - Set composition confidence ceiling = min(load_bearing_confidence, bridge_type_ceiling)
   - Gate: `confidence_bounded` — composition confidence does not exceed weakest edge

1. **Cross-Domain Provenance Tracing**: Trace provenance chains across domain boundaries.

   - Record source domain for each tensor
   - Record source path, content hash, epistemic class at each hop
   - Record bridge type and compatibility verification result
   - Record any UNKNOWN/GAP markers from source domains
   - Gate: `provenance_traced` — full provenance chain recorded with all metadata

1. **Scope and Regime Intersection**: Compute the valid scope and regime for the composition.

   - Composed scope ⊆ scope(T_A) ∩ scope(T_B)
   - Composed regime ⊆ regime(T_A) ∩ regime(T_B)
   - Flag if intersection is empty (composition produces no valid domain)
   - Gate: `scope_intersected` — composed scope and regime are valid intersections

1. **Validation**: Check results against all 10 validation gates (G1-G10).

   - G1: No contradictions within or across composed domains
   - G2: All claims labeled with epistemic class (no cross-domain promotion)
   - G3: Provenance recorded for every derived claim including domain of origin
   - G4: No claim beyond declared scope
   - G5: Composition law tagged as AMOS_MODEL
   - G6: Failure mode handled (downgrade, flag, escalate)
   - G7: All shared axes verified semantically compatible
   - G8: Confidence ≤ weakest load-bearing premise
   - G9: Bridge type classified with confidence ceiling
   - G10: Scope and regime are valid intersections
   - Gate: `gates_passed` — all 10 gates pass; failures block composition

1. **Output**: Present results with composition verdict, confidence ceiling, provenance chain, and gap flags.

   - Include composition verdict (PERMITTED / BLOCKED / CONDITIONAL)
   - Include confidence ceiling and weakest edge identification
   - Include full

______________________________________________________________________

**MOC:** [[26_WORKFLOWS/26_WORKFLOWS_MOC|26_WORKFLOWS_MOC]]

## Operations

1. **Intake**: Identify the problem and confirm it matches the Cross-Domain Tensor Composition Governor scope. - Classify the query: identify source domains (C01-C12) involved - Identify the tensors being composed (T_R, T_F, T_E, T_C, T_G,...
1. **Axis Compatibility Check**: Validate that shared axes between source domain tensors are semantically compatible. - For each shared axis (scope, regime, causal_level, time, observer, provenance, confidence, consequence): - Look up axis...
1. **Bridge Classification**: Classify the type of cross-domain bridge being attempted. - Determine bridge type: ANALOGY / ISOMORPHISM / CAUSAL / INFORMATIONAL / STRUCTURAL - Assign confidence ceiling based on bridge type (≤0.50 / ≤0.95 / ≤...
1. **Epistemic Overreach Detection**: Detect cross-domain epistemic overreach. - Check for class promotion (MODEL in domain A → VERIFIED in domain B) - Check for scope expansion (claim used beyond its declared scope in target domain) - Chec...
1. **Weakest Edge Enforcement**: Enforce the weakest-load-bearing-edge confidence rule. - Identify all load-bearing premises across all domain boundaries - Compute min(confidence) across all load-bearing premises - Set composition confidenc...
1. **Cross-Domain Provenance Tracing**: Trace provenance chains across domain boundaries. - Record source domain for each tensor - Record source path, content hash, epistemic class at each hop - Record bridge type and compatibility verifica...
1. **Scope and Regime Intersection**: Compute the valid scope and regime for the composition. - Composed scope ⊆ scope(T_A) ∩ scope(T_B) - Composed regime ⊆ regime(T_A) ∩ regime(T_B) - Flag if intersection is empty (composition produces no...
1. **Validation**: Check results against all 10 validation gates (G1-G10). - G1: No contradictions within or across composed domains - G2: All claims labeled with epistemic class (no cross-domain promotion) - G3: Provenance recorded for eve...
1. **Output**: Present results with composition verdict, confidence ceiling, provenance chain, and gap flags. - Include composition verdict (PERMITTED / BLOCKED / CONDITIONAL) - Include confidence ceiling and weakest edge identification - I...

## Orchestration Pattern

**Pattern**: Single-Agent with Validation Gates

This workflow follows a single-agent orchestration with explicit validation gates between steps:

1. **Intake** -> validation gate -> **Skill Invocation** -> validation gate -> **Application** -> validation gate -> **Output**
1. Each gate checks: epistemic labeling, provenance, scope compliance, confidence ceiling
1. On gate failure: route to error handling or escalate to parent workflow

## Evaluation Gates

### Gate 1: Intake Validation

- Query matches skill scope
- Required inputs present
- No scope violations detected

### Gate 2: Skill Load Validation

- Skill file exists and is valid
- Agent binding is valid
- Required vault sources accessible

### Gate 3: Output Validation

- Epistemic class labels present
- Provenance recorded for all derived claims
- Confidence ceiling not exceeded
- No unresolved CRITICAL_GAPs
- Scope compliance verified

## Error Handling

| Error Type       | Detection                    | Recovery                              |
| ---------------- | ---------------------------- | ------------------------------------- |
| Scope violation  | Gate 1 check                 | Route to parent skill                 |
| Missing evidence | Gate 3 check                 | Flag as GAP, reduce confidence to 0.5 |
| Contradiction    | Gate 3 check                 | Flag as CRITICAL_GAP, halt            |
| Provenance loss  | Gate 3 check                 | Mark as UNKNOWN, request human review |
| Timeout          | Step budget exceeded         | Return partial result with warnings   |
| Drift            | Confidence calibration check | Trigger drift alignment governor      |

## Human-in-the-Loop

- **Default**: Automated execution without human intervention
- **Escalation triggers**:
  - CRITICAL_GAP detected
  - Confidence below 0.3
  - Scope violation requiring reclassification
  - Contradiction that cannot be auto-resolved
- **Review checkpoint**: After Gate 3, if any warnings are present

## Monitoring

- **Trace level**: Full (inputs, outputs, intermediate steps)
- **Metrics**: Step count, token usage, confidence, gap count, execution time
- **Alerts**: CRITICAL_GAP, confidence < 0.3, scope violation, timeout
- **Provenance**: Every output traces back to source evidence via provenance chain

## Composition

- **Skill**: `amos-cross-domain-tensor-composition-governor`
- **Agent**: `amos-cross-domain-tensor-composition-governor-agent`
- **Parent workflow**: Routes via `AMOS_HOME` or parent skill workflow
- **Chain depth**: Maximum 3 workflows in sequence without orchestrator approval
- **Parallel execution**: Supported when independent capabilities are invoked
