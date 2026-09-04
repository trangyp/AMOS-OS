---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: First Principles Reasoning
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

# First-Principles Reasoning — Cognitive Organism

> **Status:** `ACTIVE_REFERENCE` · **AMOS Core target:** `v4.4`  
> **Origin architect / steward:** Trang Phan  
> **Conclusion class:** `AMOS_MODEL` · **Canonical status:** `SOURCE_GROUNDED_CANON_CANDIDATE`

______________________________________________________________________

## 1. Source-Grounded Definition

**First-Principles Reasoning (FPR)** in `05_COGNITIVE_ORGANISM/04_COGNITION` is the cognitive-organism level contract for reasoning upward from irreducible physical, biological, and mathematical invariants rather than inheriting conclusions from analogy, convention, or accumulated heuristics.

It operationalizes the Knowledge Plane framework defined in [[11_KNOWLEDGE/05_FRAMEWORKS/FPR_FIRST_PRINCIPLE_REASONING|FPR_FIRST_PRINCIPLE_REASONING]] and [[11_KNOWLEDGE/05_FRAMEWORKS/FIRST_PRINCIPLES_ARTICULATION|FIRST_PRINCIPLES_ARTICULATION]]: strip away secondary analogies, expose the substrate constraints, surface biological limits (`e = i²`), and re-derive the solution space from foundational invariants.

```text
CONVENTIONAL HEURISTIC / ANALOGY / DOMAIN ASSUMPTION
                    │
                    ▼
         AXION INVERSION (can it be contradicted?)
                    │
                    ▼
      IRREDUCIBLE PHYSICAL / BIOLOGICAL CONSTRAINT (P0)
                    │
                    ▼
         SUBSTRATE-ROOTED CONSTRUCTIVE THEOREM (T)
```

FPR is not a claim that any current implementation *produces* a formal proof; it is a disciplined reasoning posture that forces every load-bearing assertion to disclose the invariant it rests on.

______________________________________________________________________

## 2. Deconstructive Protocol

Derived from [[11_KNOWLEDGE/05_FRAMEWORKS/FIRST_PRINCIPLES_ARTICULATION|FIRST_PRINCIPLES_ARTICULATION]]:

```text
COMPLEX PROBLEM STATEMENT / SYSTEM
                 │
                 ▼
FPR DECONSTRUCTION PIPELINE:
├── Phase 1: Strip Secondary Analogies & Unsubstantiated Conventions
├── Phase 2: Identify Irreducible Physical / Thermodynamic Constraints
├── Phase 3: Surface Biological Substrate Limits (e = i²)
└── Phase 4: Re-Derive Solution Space from Foundational Invariants (S₀)
                 │
                 ▼
      SUBSTRATE-ROOTED FIRST-PRINCIPLE PROOF / MODEL
```

______________________________________________________________________

## 3. Computational Operationalization

From [[11_KNOWLEDGE/05_FRAMEWORKS/FPR_FIRST_PRINCIPLE_REASONING|FPR_FIRST_PRINCIPLE_REASONING]], the FPR pipeline is:

$$\text{Domain Heuristic } (H) \xrightarrow{\text{Axiom Inversion}} \text{Irreducible Physical Constraint } (P_0) \xrightarrow{\text{Proof Derivation}} \text{Constructive Theorem } (T)$$

1. **Axiom Inversion:** Test whether a conventional heuristic can be contradicted without violating physical or mathematical laws. If it can, it is not a first principle.
2. **Substrate Rooting:** Bind every functional assertion to measurable energy, entropy, or biological limits (`e = i²`).
3. **Formal Synthesis:** Use [[11_KNOWLEDGE/05_FRAMEWORKS/LDAI_LOGICALLY_DETERMINISTIC_AI|LDAI_LOGICALLY_DETERMINISTIC_AI]] to generate logically deterministic implementation logic where the domain admits it.

The output of FPR in the Cognitive Organism is an **RSCF-typed constructive theorem** whose confidence ceiling is `SOURCE_BOUND`, not independently validated.

______________________________________________________________________

## 4. Firewalls and Non-Purpose

FPR reasoning must not be used to claim:

```text
ANALOGY          != PROOF
CONVENTION       != CONSTRAINT
MODEL            != SUBSTRATE
SOURCE_CLAIM     != VERIFIED
PROPOSAL         != COMMIT
CAPABILITY       != AUTHORITY
ADDRESSABLE      != VALIDATED
LOGGED           != APPROVED
UNKNOWN/GAP      != PASS
```

- FPR does **not** establish universal laws of reality, biological truth, or mathematical theoremhood.
- FPR does **not** by itself enforce runtime behavior; it supplies the substrate-rooted reasoning contract that enforcement mechanisms can later implement.
- FPR does **not** collapse into analogy; analogies are permitted as pedagogical scaffolding, never as load-bearing justification.

______________________________________________________________________

## 5. Inter-Plane & Vault Connections

- **Canonical articulation master:** [[11_KNOWLEDGE/05_FRAMEWORKS/FIRST_PRINCIPLES_ARTICULATION|FIRST_PRINCIPLES_ARTICULATION]]
- **Computational operationalization:** [[11_KNOWLEDGE/05_FRAMEWORKS/FPR_FIRST_PRINCIPLE_REASONING|FPR_FIRST_PRINCIPLE_REASONING]]
- **Deterministic logic engine:** [[11_KNOWLEDGE/05_FRAMEWORKS/LDAI_LOGICALLY_DETERMINISTIC_AI|LDAI_LOGICALLY_DETERMINISTIC_AI]]
- **Structural integrity guard:** [[11_KNOWLEDGE/05_FRAMEWORKS/ABSOLUTE_STRUCTURAL_INTEGRITY|ABSOLUTE_STRUCTURAL_INTEGRITY]] · [[01_CANON/01_CORE_LAWS/ABSOLUTE_STRUCTURAL_INTEGRITY_CANON|ABSOLUTE_STRUCTURAL_INTEGRITY_CANON]]
- **Logic scaffold:** [[11_KNOWLEDGE/05_FRAMEWORKS/QLS_FRAMEWORK|QLS_FRAMEWORK]]
- **Cognitive matrix routing:** [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25_COGNITIVE_MATRIX_MOC]]

______________________________________________________________________

## 6. RSCF Contract and Gaps

```yaml
RSCF:
  node_id: amos_05_cognitive_organism_04_cognition_first_principles_reasoning
  node_type: reasoning
  claim_class: AMOS_MODEL
  state: DERIVED
  H:
    identity: "First-Principles Reasoning"
    role: "Cognitive-organism contract for substrate-rooted, invariant-first reasoning"
  M:
    phases: [strip_analogies, identify_physical_constraints, surface_biological_limits, re_derive_from_invariants]
    pipeline_steps: [axiom_inversion, substrate_rooting, formal_synthesis]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
    independent_validation: NOT_ESTABLISHED
  executable_binding: NOT_ESTABLISHED
```

**Gaps / promotion conditions:**

- [x] substantive content populated from native-canon sources
- [ ] typed schema bound and validated for runtime ingestion
- [ ] executable proof-generation / verification harness (`LDAI` binding not established)
- [ ] negative cases (contradiction, unsupported convention, missing substrate) covered in tests
- [ ] validation receipt: [[25_COGNITIVE_MATRIX/11_VALIDATION/ROUTING_POLICY_VALIDATION_RECEIPT|ROUTING_POLICY_VALIDATION_RECEIPT]] · [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]

______________________________________________________________________

## 7. Cross-Plane Bindings

- **Governing canon:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[01_CANON/03_COGNITION_CANON/COGNITIVE_ORGANISM_CANON|COGNITIVE_ORGANISM_CANON]]
- **Kernel anchors:** [[02_KERNEL/01_META_LOGIC/K_META_LOGIC|K_META_LOGIC]] · [[02_KERNEL/04_STATE/K_IDENTITY|K_IDENTITY]]
- **Downstream consumers:** [[05_COGNITIVE_ORGANISM/COGNITION_ENGINE|COGNITION_ENGINE]] · [[05_COGNITIVE_ORGANISM/ATTENTION_ENGINE|ATTENTION_ENGINE]]
- **Control-plane gates:** [[03_CONTROL_PLANE/CONTROL_PLANE_README|CONTROL_PLANE_README]]
- **Observed by:** [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] (never treated as authority)
- **Recovered via operations:** [[20_OPERATIONS/OPERATIONS_README|OPERATIONS_README]]

______________________________________________________________________

**MOC:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/00_HOME|00_HOME]]
