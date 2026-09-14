---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Causal Kernel Readme
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
updated: 2026-09-14
---
---
---

# CAUSAL KERNEL README

## Purpose

`02_KERNEL/03_CAUSAL` owns AMOS causal-claim structure, evidence-class boundaries, causal-role distinctions, and bounded validation rules. It does not infer causal truth from graph structure, sequence, correlation, analogy, or model fit.

The current executable owner for the generic causal evidence gate is:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/causal_claim_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_causal_claim_runtime.py`

## Core distinction set

```text
ASSOCIATION != CAUSATION
TEMPORAL_PRECEDENCE != CAUSATION
GRAPH_REACHABILITY != CAUSATION
MODEL_FIT != INTERVENTION_EFFECT
MEDIATOR != CONFOUNDER
NECESSARY != SUFFICIENT
VALIDATED_CLAIM != DEPLOYMENT_AUTHORITY
```

Causal conclusions remain bound to source/target identity, scope, regime, state version, evidence identity, identification assumptions, and unresolved reverse-causation state.

## Sibling artifacts

- [[02_KERNEL/03_CAUSAL/KERNEL_CAUSAL_CONTRACT|KERNEL_CAUSAL_CONTRACT]] — current generic causal evidence gate contract
- [[02_KERNEL/03_CAUSAL/K_CAUSAL_CLOSURE|K_CAUSAL_CLOSURE]] — closure claims; require explicit boundary/intervention semantics
- [[02_KERNEL/03_CAUSAL/K_CAUSAL_EPOCH|K_CAUSAL_EPOCH]] — causal epoch/state concepts
- [[02_KERNEL/03_CAUSAL/K_CAUSAL_HIERARCHY|K_CAUSAL_HIERARCHY]] — causal claim classification
- [[02_KERNEL/03_CAUSAL/K_CROSS_SCALE_CAUSALITY|K_CROSS_SCALE_CAUSALITY]] — cross-scale source/model material; structural analogy does not prove cross-scale mechanism
- [[02_KERNEL/03_CAUSAL/K_BIOLOGICAL_CAUSALITY|K_BIOLOGICAL_CAUSALITY]] — biological source/model material; requires domain evidence
- [[02_KERNEL/03_CAUSAL/K_QUANTUM_CAUSALITY|K_QUANTUM_CAUSALITY]] — source/model material; do not import quantum terminology into ordinary causal claims without physics-grounded definitions

## Contract discipline

- Type the causal claim before assessing it.
- Keep observational association, temporal precedence, enabling condition, mediation, confounding, necessity, sufficiency, mechanism, and intervention effects distinct.
- Prefer intervention/natural-experiment evidence when claiming intervention effects.
- Preserve reverse-causation uncertainty.
- Preserve scale/regime and target population.
- Make identification assumptions explicit.
- Use the weakest accurate conclusion class.
- Keep causal validation separate from authority to intervene.

## Current implementation boundary

The generic runtime validates whether declared evidence classes are structurally sufficient for the declared causal claim. It does **not** independently establish that a study satisfies exchangeability, positivity, consistency/SUTVA, exclusion restrictions, measurement validity, correct adjustment, transportability, or absence of unmeasured confounding.

Domain causal estimators/discovery algorithms remain `UNKNOWN/GAP` unless separately implemented and validated.

## Worked semantics

1. Resolve source, target, claim class, scope, regime, and state version.
2. Bind evidence identities and evidence classes.
3. Reject graph reachability/model fit as sole causal identification evidence.
4. Check claim-specific evidence requirements.
5. Block effect-like claims when reverse causation remains unresolved.
6. Preserve any weaker supported claim instead of promoting or discarding evidence wholesale.
7. Return bounded support/not-licensed classification.
8. Route consequential interventions through independent risk/authority/commit controls.

## Promotion-gate checklist

- [x] typed generic causal-claim schema
- [x] typed generic evidence-class schema
- [x] scope/regime/version checks
- [x] association/temporal/graph/model-fit causal firewalls
- [x] reverse-causation blocker
- [ ] domain-specific causal identification verification
- [ ] quantitative estimators and uncertainty
- [ ] discovery/adjustment algorithms
- [ ] external empirical validation
- [ ] intervention authority/deployment validity

## Cross-plane bindings

- Parent Kernel — [[02_KERNEL/02_KERNEL_CONTRACT|02_KERNEL_CONTRACT]]
- Canon — [[01_CANON/01_CANON_MOC|01_CANON_MOC]]
- Control plane — [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- Runtime — [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]]
- Observability — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]]

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

RSCF-NODE
node_id: amos_02_kernel_03_causal_causal_kernel_readme_md
node_type: note
path: 02_KERNEL/03_CAUSAL/CAUSAL_KERNEL_README.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[02_KERNEL/03_CAUSAL/03_CAUSAL_MOC|03_CAUSAL_MOC]]

______________________________________________________________________

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
