---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_executable_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: 04 Runtime Moc
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
---

# 04 Runtime — Map of Content

**Path:** `04_RUNTIME`  
**Role:** Governed state-transition, session execution, boot sequencing, bounded reference execution, and causal finalization environment under AMOS Core v4.4.

## 1. Runtime execution lifecycle architecture

```text
BOOTSTRAP & INITIALIZATION (01_BOOT)
                 ↓
DETERMINISTIC ROUTING & DISPATCH (02_ROUTER)
                 ↓
BOUNDED REFERENCE IMPLEMENTATION (01_REFERENCE_IMPLEMENTATION)
                 ↓
MULTI-REGIME EXECUTION & COMPLEXITY ADAPTATION (06_EXECUTION)
                 ↓
CAUSAL FINALIZATION & PROOF COMMIT (09_FINALIZATION)
```

The execution-flow diagram is not an authority hierarchy. Durable effects remain subordinate to the AMOS infrastructure/control plane and commit-time authority checks.

## 2. MECE component matrix

### 2.1 Boot & substrate initialization (`01_BOOT`)

- [[04_RUNTIME/01_BOOT/CANON_BOOTSTRAP|CANON_BOOTSTRAP]] — loads candidate/active canon inputs under admission rules; path presence alone is not canon authority.
- [[04_RUNTIME/01_BOOT/FULL_BRAIN_BOOTSTRAP|FULL_BRAIN_BOOTSTRAP]] — boots the Full Brain OS container beneath infrastructure authority.
- [[04_RUNTIME/01_BOOT/UBI_BOOTSTRAP|UBI_BOOTSTRAP]] — hydrates the UBI substrate where applicable.
- [[04_RUNTIME/01_BOOT/UNIVERSE_CANON_BOOTSTRAP|UNIVERSE_CANON_BOOTSTRAP]] — binds universe-canon coordinates only under current canon status.
- [[04_RUNTIME/01_BOOT/01_BOOT_MOC|01_BOOT_MOC]] — subdirectory MOC.

### 2.2 Deterministic routing engine (`02_ROUTER`)

- [[04_RUNTIME/02_ROUTER/CANON_ROUTER|CANON_ROUTER]] — routes normative checks to canon-governed authorities.
- [[04_RUNTIME/02_ROUTER/FRAMEWORK_ROUTER|FRAMEWORK_ROUTER]] — dispatches framework-specific work without merging their semantics.
- [[04_RUNTIME/02_ROUTER/HML_ROUTER|HML_ROUTER]] — routes H/M/L scale work.
- [[04_RUNTIME/02_ROUTER/RSCF_ROUTER|RSCF_ROUTER]] — routes claim/evidence work.
- [[04_RUNTIME/02_ROUTER/02_ROUTER_MOC|02_ROUTER_MOC]] — subdirectory MOC.

### 2.3 Bounded reference implementation (`01_REFERENCE_IMPLEMENTATION`)

- [[04_RUNTIME/01_REFERENCE_IMPLEMENTATION/README|Runtime Reference Implementation]] — status, boundaries, evidence, and remaining gaps.
- `core19_runtime.py` — executable bounded URK/Core-19 repair projection.
- `test_core19_runtime.py` — deterministic/property/adversarial regression suite.

Current verified scope is intentionally narrow: Core-19 registry typing, P02 competing lineage binding, Truth4 evidence state, unary `ATOM | NOT | NLOGIC` normalization, 19×19 coordinate counting, typed tensor coordinates, logic-fragment status, and promotion gates.

This layer does **not** establish that every ULK fragment or every AMOS runtime subsystem is executable.

### 2.4 Multi-regime execution & adaptive scaling (`06_EXECUTION`)

- [[04_RUNTIME/06_EXECUTION/FAST_PATH_RUNTIME|FAST_PATH_RUNTIME]] — coordination-avoidance proposal/contract where preconditions hold.
- [[04_RUNTIME/06_EXECUTION/ADAPTIVE_COMPLEXITY_RUNTIME|ADAPTIVE_COMPLEXITY_RUNTIME]] — scaled reasoning tiers.
- [[04_RUNTIME/06_EXECUTION/FRACTAL_RUNTIME|FRACTAL_RUNTIME]] — recursive multi-scale evaluation.
- [[04_RUNTIME/06_EXECUTION/UNCERTAINTY_VECTOR_RUNTIME|UNCERTAINTY_VECTOR_RUNTIME]] — uncertainty-state tracking.
- [[04_RUNTIME/06_EXECUTION/ADVERSARIAL_VALIDATION_RUNTIME|ADVERSARIAL_VALIDATION_RUNTIME]] — challenge paths for consequential proposals.
- [[04_RUNTIME/06_EXECUTION/SENSITIVITY_RUNTIME|SENSITIVITY_RUNTIME]] — perturbation testing.
- [[04_RUNTIME/06_EXECUTION/06_EXECUTION_MOC|06_EXECUTION_MOC]] — subdirectory MOC.

### 2.5 Causal finalization & commit gates (`09_FINALIZATION`)

- [[04_RUNTIME/09_FINALIZATION/CAUSAL_EPOCH_FINALIZER|CAUSAL_EPOCH_FINALIZER]] — causal-lineage finalization contract.
- [[04_RUNTIME/09_FINALIZATION/LOCAL_PROOF_FINALIZER|LOCAL_PROOF_FINALIZER]] — local proof finalization where independence/preconditions are established.
- [[04_RUNTIME/09_FINALIZATION/PROOF_CAPSULE_FINALIZER|PROOF_CAPSULE_FINALIZER]] — proof/evidence capsule packaging.
- [[04_RUNTIME/09_FINALIZATION/09_FINALIZATION_MOC|09_FINALIZATION_MOC]] — subdirectory MOC.

## 3. Runtime evidence boundary

```text
DOCUMENTED_COMPONENT != EXECUTABLE_COMPONENT
EXECUTABLE_COMPONENT != SYSTEM_WIDE_CLOSURE
BOUNDED_TEST_PASS != UNIVERSAL_CORRECTNESS
CANON_SOURCE != CANON_PROMOTION
COGNITIVE_CAPABILITY != EFFECT_AUTHORITY
```

The active bounded Core-19 implementation is a runtime projection from admissible candidate semantics. It does not supersede `K_CANON`, AMOS_CORE v4.4 lineage rules, or the canonical ULK v2.1.0 source by freshness.

## 4. Plane contracts & infrastructure documentation

- [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|Runtime Plane Contract]]
- [[04_RUNTIME/RUNTIME_README|Runtime Operating Model README]]
- [[04_RUNTIME/00_INDEX/RUNTIME_MAP|Runtime Navigation Map]]
- [[01_CANON/07_PROVENANCE/URK_CORE19_REPAIR_CANDIDATE_2026-09-14|URK/Core-19 Repair Candidate Provenance]]

**Parent:** [[AMOS_HOME|AMOS_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

**Related:** [[01_CANON/01_CANON_MOC|01_CANON_MOC]] · [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] · [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] · [[12_STATE/12_STATE_MOC|12_STATE_MOC]] · [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
