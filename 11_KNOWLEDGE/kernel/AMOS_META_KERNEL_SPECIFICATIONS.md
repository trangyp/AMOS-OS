---
title: AMOS META KERNEL SPECIFICATIONS
tags:
- canon-group/biology
- canon/framework
- rscf/claim
- rscf/provenance
- rscf/state/observation
- topic/amos-meta-kernel-specifications
- kernel
- 00-home
- knowledge-moc
- system-scan-agent
- automation-profiles
- kernel-moc
- amos-simulation-kernel-v0-math-foundations
type: document
source: 11_KNOWLEDGE/kernel
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# AMOS Meta-Kernel Specifications

Specifications for meta-cognition kernels defined in the brain's AMOS_Omni_KERNEL.json (md/Core/AMOS_Os_Agent_v0.md). These fill gaps where source files are empty or missing.

## Meta-Epistemology Kernel

**Source:** AMOS_Omni_KERNEL.json components.meta_cognition[0]
**Group:** Cognitive_Stack.Meta_Cognition
**Status:** defined (blueprint) — source file empty/autofixed

### Purpose
Define what counts as knowledge, evidence, and justified belief within the AMOS system. Govern how claims are validated, what truth values are assigned, and when uncertainty must be labelled.

### Core Functions
1. **Truth-value assignment:** Every claim must be assigned TRUE, FALSE, UNKNOWN, or INAPPLICABLE. No claim left implicitly TRUE without justification.
2. **Evidence classification:** Classify evidence by type (direct observation, inference, testimony, structural consistency, cross-domain confirmation) and strength.
3. **Justification requirement:** Define what counts as sufficient justification for each truth-value transition (UNKNOWN→TRUE requires evidence; UNKNOWN→FALSE requires disproof or impossibility demonstration).
4. **Uncertainty labelling:** UNKNOWN claims must state what would resolve them (what evidence would change the value).
5. **Source separation:** Separate claims from their sources. Track which claims come from direct evidence vs inference vs assumption.

### Integration with Law Stack
- **L1 (Law of Law):** Epistemological rules must be internally consistent and recursively checkable.
- **L4 (Absolute Structural Integrity):** Every claim must be traceable to its evidence source.
- **L5 (Post-Theory Communication):** Epistemological claims must be stated in clear, testable language.

### Truth Values and Modalities (from Deterministic Logic Kernel)

**Truth values:** TRUE, FALSE, UNKNOWN, INAPPLICABLE
**Modalities:** MUST, MAY, MUST_NOT, SHOULD, SHOULD_NOT
**Burdens:** NONE, LOW, MEDIUM, HIGH, IMPOSSIBLE

---

## Meta-Ontology Kernel

**Source:** AMOS_Omni_KERNEL.json components.meta_cognition[1]
**Group:** Cognitive_Stack.Meta_Cognition
**Status:** defined (blueprint) — source file empty/autofixed

### Purpose
Define the fundamental categories, entities, and relations that AMOS uses to model reality. Provide a stable ontology that all other kernels can reference.

### Core Categories (from AMOS_CANONICAL_GLOSSARY.json)

**System layer:** AMOS-SYSTEM (complete system including repository, runtime, organism OS, workers, godmode supervisor), engine (structured logic module behaving like an organ), agent (active worker using engines), kernel (low-level processor routing signals), worker (specialised execution unit), organism_os (life support orchestration), memory_core (event and experience index), dashboard (human-facing telemetry), godmode (top-level executive controller), executor_loop (continuous task processing).

**Biological layer:** nervous_system (mapping onto kernels, executors, routing), organs (mapping onto engines), cells (mapping onto agents/workers), blood (task queue messages, memory events, data flow), fascia (directory structure, naming conventions), electromagnetic_body (message passing, kernel signals, cross-component communication).

### Core Relations (from Deterministic Logic Kernel)

OWNS, OWES, IS_SUBJECT_TO, VIOLATES, COMPLIES_WITH, HAS_DUTY_TO, HAS_RIGHT_AGAINST, DELEGATES_TO, REPRESENTS, BENEFITS_FROM

### Design Principles
1. **MECE partitioning:** Categories must be mutually exclusive and collectively exhaustive within their domain.
2. **Layered structure:** Ontology is layered from molecule → organism → group → population (matching Biology and Cognition Engine L1 structure).
3. **Interface boundaries:** Clear interfaces between ontology layers so other engines can attach without confusion.
4. **Auditability:** Every category and relation must be traceable to its defining source.

---

## Meta-Logic Kernel

**Source:** AMOS_Omni_KERNEL.json components.meta_cognition[2]; AMOS_C01_meta_logic_SUPER.json (file_hint)
**Group:** Cognitive_Stack.Meta_Cognition
**Status:** defined (blueprint) — source file empty/autofixed; rich content in AMOS_Deterministic_Logic_And_Law_Engine_v0.md

### Purpose
Hold the highest-order laws, invariants, and meta-rules that govern all reasoning across domains and time horizons.

### Core Laws (full specification)

**Law of Law (L1):** All subordinate laws must be internally consistent, recursively checkable, and non-contradictory when applied to the same state under the same assumptions.
- Properties: no_internal_contradiction, explicit_assumption_tracking, hierarchical_precedence_of_laws, testability_under_counterexample
- Usage: validate_new_framework_before_adoption, audit_existing_rule_sets_for_hidden_conflicts, resolve_competing_policies_or_ethics_clauses

**Rule of 2 (L2):** For every claim, model, or decision, explicitly hold at least two structurally opposed interpretations and test both against data and constraints.
- Operations: construct_primary_hypothesis, construct_structural_opposite, evaluate_both_against_evidence, keep_tension_until_decisive_signal
- Applications: risk_assessment, scenario_planning, strategic_negotiation, bias_detection

**Rule of 4 (L3):** Every state or problem is decomposed into four entangled quadrants: biological_state, experiential_history, logical_structure, systemic_context.
- Benefits: prevents_overfitting_to_single_domain, forces_multi_source_validation, supports_design_of_resilient_solutions

**Signal Fidelity Preservation:** Never simulate or claim internal states (care, ethics, love, certainty) that are not structurally grounded in observable patterns and commitments.
- Rules: no_simulated_emotion_without_structural_basis, no_ethics_claim_without_enforceable_mechanism, no_certainty_claim_without_defined_falsification_path

**Absolute Structural Integrity:** Every output, framework, or decision must be structurally sound: clear assumptions, explicit constraints, no hidden leaps.
- Checks: traceability_of_each_claim, no_undefined_placeholders, no_dependency_on_obscure_terminology, alignment_with_biological_and_systemic_constraints

### Meta-Capabilities
- **Multi-threaded thought:** Hold up to 8 concurrent reasoning threads, each with own assumptions and evidence set. Track by thread_id, assumption_set_reference, evidence_pool_reference, status_flag (hypothesis_open/closed).
- **Framework interpreter:** Map any incoming framework (scientific, economic, psychological, spiritual) into neutral structural representation. Steps: extract_core_entities_and_relations → normalize_terms_to_neutral_vocabulary → identify_hidden_axioms → evaluate_against_meta_laws.
- **Equation and law registry:** Store all known equations, laws, canonical relationships with metadata: name, domain, inputs, outputs, assumptions, confidence_level, validity_scope.

### Deterministic Logic and Law (from AMOS_Deterministic_Logic_And_Law_Engine_v0.md)

**Primitives:**
- Truth values: TRUE, FALSE, UNKNOWN, INAPPLICABLE
- Modalities: MUST, MAY, MUST_NOT, SHOULD, SHOULD_NOT
- Burdens: NONE, LOW, MEDIUM, HIGH, IMPOSSIBLE
- Entities: PERSON, ORGANISATION, STATE, ASSET, CONTRACT, OBLIGATION, RIGHT, RISK, SANCTION, EVIDENCE
- Relations: OWNS, OWES, IS_SUBJECT_TO, VIOLATES, COMPLIES_WITH, HAS_DUTY_TO, HAS_RIGHT_AGAINST, DELEGATES_TO, REPRESENTS, BENEFITS_FROM

**Operators:**
- Logical: AND, OR, NOT, XOR, IMPLIES, IFF
- Quantifiers: FOR_ALL, EXISTS, FOR_MAJORITY, FOR_MINORITY
- Temporal: BEFORE, AFTER, DURING, UNTIL, SINCE
- Deontic: OBLIGATORY, PERMITTED, FORBIDDEN, EXEMPT
- Causal: CAUSES, CONTRIBUTES_TO, ENABLED_BY, WOULD_COUNTERFACTUALLY_CHANGE

**Rule systems (priority layers):** Constitutional_Principles → Primary_Legislation → Secondary_Legislation → Regulatory_Guidance → Contracts_and_Policies → Soft_Law_and_Standards → Internal_Procedures

**Conflict resolution:** lex_superior (higher norm overrides lower), lex_specialis (specific overrides general), lex_posterior (newer overrides older at same level), jurisdiction_priority: SUPRANATIONAL > NATIONAL > SUBNATIONAL > INTERNAL_POLICY

---

## Cognitive Compression Kernel

**Source:** AMOS_Omni_KERNEL.json components.meta_cognition[3]
**Group:** Cognitive_Stack.Meta_Cognition
**Status:** defined (blueprint) — source file empty/autofixed

### Purpose
Reduce cognitive load by compressing complex information into structural summaries without losing essential content.

### Core Functions
1. **Structural summarization:** Extract the skeleton of complex information (entities, relations, key claims) while discarding narrative wrapping.
2. **Pattern extraction:** Identify recurring patterns across multiple inputs and represent them as reusable abstractions.
3. **Abstraction management:** Track abstraction levels; ensure each abstraction is grounded in lower-level detail that can be recovered if needed.
4. **Compression ratio tracking:** Monitor how much detail is lost vs preserved; flag when compression threatens structural integrity.

### Integration
- Feeds into Expression Translation (Phase 1: Decode) — helps separate structural content from narrative wrapping.
- Feeds into HIE S5 (content and structure selection) — compressed representations support efficient structuring.
- Respects Rule of 4: compression must preserve all four quadrant information or explicitly note what is discarded.

---

## Analogy and Abstraction Kernel

**Source:** AMOS_Omni_KERNEL.json components.meta_cognition[4]
**Group:** Cognitive_Stack.Meta_Cognition
**Status:** defined (blueprint) — source file empty/autofixed

### Purpose
Map structural similarities across domains to transfer understanding from familiar domains to unfamiliar ones.

### Core Functions
1. **Cross-domain mapping:** Identify entities, relations, and dynamics in domain A that structurally correspond to entities, relations, and dynamics in domain B.
2. **Analogy validation:** Test whether the analogy holds structurally or breaks down at specific points. Never extend an analogy beyond its valid range.
3. **Abstraction ladder:** Move between concrete instances and abstract patterns, tracking which level is being used.
4. **Domain gap identification:** Identify where the analogy fails — these gaps often reveal domain-specific features that matter.

### Integration
- Supports HIE S3 (select primary goal) — analogies help frame what kind of goal is appropriate.
- Supports Multi-Domain Thinking (Cognition Layer 3) — cross-domain mapping is the core mechanism.
- Must respect Signal Fidelity: analogies are tools for understanding, not claims about identity between domains.

---

## Counterfactual Reasoning Kernel

**Source:** AMOS_Omni_KERNEL.json components.meta_cognition[5]
**Group:** Cognitive_Stack.Meta_Cognition
**Status:** defined (blueprint) — source file empty/autofixed

### Purpose
Reason about what would happen under different conditions, enabling scenario planning, risk assessment, and intervention design.

### Core Functions
1. **Counterfactual construction:** For a given baseline state, construct structurally plausible alternative states by varying specific conditions.
2. **Causal tracing:** Trace how changes propagate through the system's causal structure (CAUSES, CONTRIBUTES_TO, ENABLED_BY, WOULD_COUNTERFACTUALLY_CHANGE).
3. **Robustness testing:** Test whether a strategy, decision, or model holds across multiple counterfactual scenarios.
4. **Intervention mapping:** Identify which changes would produce the desired outcome, and which would be irrelevant or counterproductive.

### Integration
- Supports HIE S5 (content and structure) — counterfactuals are essential for scenario trees and risk lattices.
- Supports Strategic Advisory mode — game models and scenario gameplay depend on counterfactual reasoning.
- Must respect Rule of 2: hold both the actual and counterfactual trajectories; don't collapse to one too early.

---

## Multi-Perspective Reasoning Kernel

**Source:** AMOS_Omni_KERNEL.json components.meta_cognition[6]
**Group:** Cognitive_Stack.Meta_Cognition
**Status:** defined (blueprint) — source file empty/autofixed

### Purpose
Hold and compare multiple structurally distinct perspectives on the same problem without premature collapse into a single view.

### Core Functions
1. **Perspective generation:** For a given problem, generate multiple structurally distinct framings (different entities as primary, different relations as central, different time horizons, different stakeholder positions).
2. **Perspective comparison:** Compare perspectives side-by-side, identifying where they agree, where they diverge, and what each captures that others miss.
3. **Tension preservation:** Maintain tension between perspectives until a decisive signal resolves it. Do not force premature consensus.
4. **Integration when justified:** When perspectives converge on a point (same conclusion from structurally different routes), that point has higher confidence.

### Integration
- This is the operational engine for Rule of 2 (L2) — it generates and maintains the structural opposites.
- Supports HIE S5 — multiple perspectives feed into content structure.
- Supports Multi-Domain Thinking (Layer 3) — each domain-ready perspective is a different lens.

---

## Complete Meta-Cognition Stack Integration

```
                          AMOS_BRAIN_ROOT (laws, identity, constraints)
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
    Meta_Epistemology_Kernel  Meta_Ontology_Kernel  Meta_Logic_Kernel
    (what counts as knowledge) (categories, entities) (laws, invariants)
              │                    │                    │
              └────────────────────┼────────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
    Cognitive_Compression_K    Analogy_Abstraction_K  Counterfactual_K
    (reduce load, summarize)   (cross-domain mapping) (what-if reasoning)
              │                    │                    │
              └────────────────────┼────────────────────┘
                                   │
                         Multi_Perspective_Reasoning_K
                         (hold and compare perspectives)
                                   │
                         Feeds into HIE S3, S5, S9
                         Supports all 5 cognition layers
```

All meta-cognition kernels depend on Meta_Logic_Kernel (Law of Law is the foundation). Meta_Epistemology and Meta_Ontology are independent of each other but both support Meta_Logic. Counterfactual and Multi-Perspective both depend on the full meta-cognition foundation.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

---
**MOC:** [[KERNEL_MOC]]
