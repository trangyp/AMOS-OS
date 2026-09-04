---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Qls Qcla Variable Registry
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

# QLS/QCLA Variable Registry

## 0. Purpose

This registry prevents silent symbol collision between QLS/QIC substrate variables and QCLA quantum/chemical/causal variables.

```text
SAME SYMBOL != SAME VARIABLE
SAME NAME != SAME UNITS
SAME UNITS != SAME SEMANTICS
SYMBOLIC VARIABLE != MEASURED VARIABLE
```

## 1. Required variable record

```yaml
QLSQCLAVariable:
  variable_id:
  symbol:
  canonical_name:
  aliases:
  source_family: QLS|QIC|QCLA|SHARED_DERIVED
  semantic_class:
  domain:
  units:
  dimension:
  value_domain:
  scale:
  time_index:
  regime:
  observer_or_measurement:
  observed_or_latent_or_symbolic:
  source_anchor:
  equation_bindings:
  allowed_transformations:
  uncertainty:
  provenance:
  lifecycle:
  supersession:
```

## 2. Semantic classes

Use one primary semantic class:
- `STATE`
- `OBSERVATION`
- `LATENT_STATE`
- `CONTROL`
- `CONSTRAINT`
- `ENERGY_OR_RESOURCE`
- `PROBABILITY`
- `LOGICAL`
- `CAUSAL`
- `TOPOLOGICAL`
- `MATERIAL_OR_CHEMICAL`
- `INFORMATION`
- `TIMING`
- `SECURITY`
- `SYMBOLIC_MODEL`
- `UNKNOWN/GAP`

## 3. QLS/QIC boundary

QLS/QIC substrate variables represent generic units, relations, transforms, memory, discrimination, prediction/correction and propagation only within their declared model semantics.

They do not automatically become QCLA physical variables.

```text
QIC UNIT != MOLECULE
QLS TRANSFORM != QUANTUM GATE
QLS FIELD != PHYSICAL FIELD
```

A mapping requires an explicit translation rule and translation-loss state.

## 4. QCLA boundary

QCLA variables may refer to molecular/chemical states, coherence/state logic, causal constraints or architecture-level quantities.

Every physical interpretation requires:
- unit;
- measurement method;
- hardware/material system;
- environment;
- temporal regime;
- uncertainty.

Absent those, the variable remains model/symbolic.

## 5. Cross-framework mapping object

```yaml
VariableMapping:
  source_variable:
  target_variable:
  mapping_type: IDENTICAL|UNIT_CONVERSION|APPROXIMATION|ANALOGY|EMBEDDING|UNKNOWN
  assumptions:
  information_loss:
  scope:
  regime:
  evidence:
  provenance:
  falsifier:
```

`ANALOGY` mappings cannot be used inside physical equations as if identity were proven.

## 6. Equation admission

Before a QLS/QCLA equation is reusable:
1. resolve every symbol;
2. resolve units/dimensions;
3. classify each variable as observed/latent/symbolic;
4. verify domain and regime;
5. verify equation source;
6. classify equation as formal identity / definition / model / hypothesis / empirical fit.

## 7. Collision examples to block

- `E` used for entropy vs energy;
- `S` used for system/state vs entropy;
- `C` used for constraint/coherence/capacity;
- `Q` used for quantum state/quality/charge;
- `I` used for information/current/identity;
- `P` used for probability/power/policy.

Name collisions must be resolved with qualified logical IDs.

## 8. Full-Brain and domain routing

This registry is infrastructure for reasoning; it is not a Full-Brain peer.

Physical QCLA variables route to C03/C10, formal variables to C02, and biological variables to C04 only when the semantic mapping is evidence-supported.

## 9. Validation tests

- same symbol, different domain;
- same name, different units;
- unitless symbolic variable promoted to physical variable;
- QLS analogy mapped to QCLA identity;
- stale source variable after supersession;
- equation with undefined symbol;
- dimensionally inconsistent equation;
- incompatible time/regime composition.

## 10. Current gaps

A complete symbol-by-symbol census of all QLS/QCLA source equations is not yet materialized. This registry defines the governing contract and must be progressively populated from source-faithful parsing.

---
RSCF-NODE
node_id: amos_01_canon_05_variable_registry_qls_qcla_variable_registry
node_type: variable_registry
claim_class: AMOS_MODEL
