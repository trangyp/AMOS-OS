---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Kernel Causal Contract
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

# KERNEL CAUSAL CONTRACT

## 0. Status

Kernel-plane contract for **CAUSAL CONTRACT**. AMOS_MODEL; canonical status CONDITIONAL; implementation BOUNDED_PARTIAL. A structural causal-claim evidence gate exists; it validates evidence classes, scope/regime/version compatibility, and protected causal distinctions. It does not discover causal truth or validate domain identification assumptions by itself.

## 1. Scope

Governs proposed causal claims as they bear on kernel reasoning: association, temporal precedence, enabling conditions, mediation, confounding, necessity, sufficiency, mechanisms, and intervention effects. Conclusions inherit the weakest load-bearing premise and remain bound to scope, regime, state version, and evidence identity.

## 2. Causal hierarchy

The runtime keeps these claim classes distinct:

- `ASSOCIATION`
- `TEMPORAL_PRECEDENCE`
- `ENABLING_CONDITION`
- `MEDIATOR`
- `CONFOUNDER`
- `NECESSARY_CONDITION`
- `SUFFICIENT_CONDITION`
- `MECHANISM`
- `INTERVENTION_EFFECT`

This is not a single total ordering: mediator/confounder are causal roles, and necessity/sufficiency are logically different properties. A stronger-sounding label is not licensed by weaker evidence.

## 3. Hard invariants

- `ASSOCIATION != CAUSATION`.
- `TEMPORAL_PRECEDENCE != CAUSATION`.
- `GRAPH_REACHABILITY != CAUSATION`.
- `MODEL_FIT != INTERVENTION_EFFECT`.
- `CAUSAL_ROLE != EFFECT_STRENGTH`.
- `VALIDATED_CLAIM != DEPLOYMENT_AUTHORITY`.
- Reverse causation uncertainty remains explicit when unresolved.
- Scale and regime travel with causal claims.
- Causal direction, confounding, mediation, necessity, sufficiency, mechanism, and intervention effects require their own evidence classes.
- A causal graph edge is a model object until its interpretation and evidence are separately bound.
- Structural validation of evidence labels does not prove that the underlying study/design satisfies its identification assumptions.

## 4. Executed reference

Bounded executor and regression owners:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/causal_claim_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_causal_claim_runtime.py`

The runtime requires explicit claim/evidence scope, regime, and state version; rejects graph reachability or model fit as sole causal evidence; keeps mediator/confounder and necessary/sufficient claims separate; blocks effect-like claims when reverse causation remains unresolved; and requires intervention or natural-experiment evidence class for an `INTERVENTION_EFFECT` claim.

These are structural gates only. They do not independently verify randomization, exchangeability, positivity, consistency/SUTVA, exclusion restrictions, measurement validity, absence of unmeasured confounding, or any domain-specific identification assumption.

## 5. Evidence classes

The bounded gate recognizes explicit evidence categories including:

- observational association
- temporal order
- direction discrimination
- confounding assessment
- mediation assessment
- enabling-condition test
- necessity test
- sufficiency test
- mechanism evidence
- intervention
- natural experiment
- identification assumptions
- scale/regime binding
- negative controls
- sensitivity analysis

`GRAPH_REACHABILITY_ONLY` and `MODEL_FIT_ONLY` are explicit non-causal-identification states.

## 6. Gaps

OPEN (`UNKNOWN/GAP` where load-bearing): domain-specific causal discovery; DAG identification from observational data; adjustment-set computation; do-calculus; instrumental-variable validity; mediation estimands; transportability; longitudinal/time-varying confounding; interference; counterfactual identification; quantitative causal-effect estimation; uncertainty intervals; study-quality validation; empirical falsification. External algorithms may be added only with explicit assumptions and provenance.

## 7. Falsifiers

F1: canonical source defines different causal semantics. F2: association or temporal order alone licenses an effect/mechanism claim. F3: graph reachability is treated as causation. F4: mediator and confounder roles collapse. F5: necessity and sufficiency collapse. F6: an intervention-effect claim passes without intervention/natural-experiment evidence class. F7: scope/regime/state mismatch is ignored. F8: causal validation grants effect authority.

## Worked semantics

Given a proposed causal edge or causal statement:

1. **Type the claim** — choose the strongest specific causal class actually asserted.
2. **Bind scope/regime/version** — unresolved mismatch blocks support.
3. **Bind evidence identities and classes** — do not infer evidence from narrative wording.
4. **Check claim-specific requirements** — preserve distinct tests for confounding, mediation, necessity, sufficiency, mechanism, or intervention.
5. **Check direction uncertainty** — unresolved reverse causation blocks effect-like promotion.
6. **Preserve weaker licensed claims** — failure of a mechanism/effect claim may still leave an association claim supported.
7. **Return bounded classification** — supported within the declared structural evidence contract or not licensed by current evidence.
8. **Do not execute consequential intervention** without independent authority/risk/commit gates.

## Promotion-gate checklist

- [x] typed causal claim classes implemented
- [x] typed evidence classes implemented
- [x] scope/regime/state-version checks implemented
- [x] graph-reachability and model-fit-only causal firewalls implemented
- [x] reverse-causation blocker implemented for effect-like claims
- [x] intervention/natural-experiment class required for intervention-effect structural admission
- [ ] domain identification assumptions independently verified
- [ ] quantitative effect estimators implemented and validated
- [ ] causal discovery/adjustment algorithms provenance-bound
- [ ] empirical study-quality and sensitivity evidence integrated
- [ ] consequential intervention authority integrated

## Cross-plane bindings

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- Parent Kernel contract — [[02_KERNEL/02_KERNEL_CONTRACT|02_KERNEL_CONTRACT]]
- Control-plane gates — [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority
- Recovered via operations — [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

RSCF-NODE
node_id: amos_02_kernel_03_causal_kernel_causal_contract_md
node_type: note
path: 02_KERNEL/03_CAUSAL/KERNEL_CAUSAL_CONTRACT.md
claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[02_KERNEL/03_CAUSAL/03_CAUSAL_MOC|03_CAUSAL_MOC]]

______________________________________________________________________

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
