---
canon-group: cognition
canon-type: failure_contract
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_2026_09_14_URK_repair
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: L09 Inference Primitives Cognitive Matrix Failure Modes
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
canonical_status: CONDITIONAL
---

# L09 — Failure Modes and Repair Rules

**Package:** `L09_INFERENCE`  
**Origin architect / steward:** **Trang Phan**

## Failure registry

- `FM-L09-01 / REGIME_ESCAPE`  
  Failure: a rule is applied outside its declared scope or regime.  
  Detect: scope/regime compatibility check.  
  Repair: return `UNKNOWN/GAP`, rebind the rule, and re-evaluate dependent conclusions.

- `FM-L09-02 / CONDITIONAL_SLIPPAGE`  
  Failure: a conditional or model result is reused as unconditional fact.  
  Detect: dependency/RSCF edge audit.  
  Repair: restore `CONDITIONED_ON` ancestry and downgrade downstream status.

- `FM-L09-03 / FRAGMENT_OVERREACH`  
  Failure: a specification-only logic fragment is treated as executable.  
  Detect: `implementation_status(fragment)`.  
  Repair: fail closed with `UNKNOWN/GAP` until a checker and evidence receipt are bound.

- `FM-L09-04 / QUANTUM_REBIND_BYPASS`  
  Failure: the canonical bounded ALU-07 claim is mistaken for a locally available checker.  
  Detect: local checker/receipt identity missing.  
  Repair: retain `CANONICAL_BOUNDED_CLAIM_REBIND_PENDING`.

- `FM-L09-05 / P02_COLLAPSE`  
  Failure: `NonExistence` or `Distinction` is selected as the global P02 meaning without namespace/version authority.  
  Detect: P02-dependent request lacks a resolved binding.  
  Repair: return `COMPETING`; preserve both source lineages.

- `FM-L09-06 / UNKNOWN_AS_NONEXISTENCE`  
  Failure: missing evidence or `UNKNOWN` is interpreted as non-existence.  
  Detect: state-transition/type audit.  
  Repair: restore the separate unknown state and invalidate dependent conclusions only.

- `FM-L09-07 / NAMESPACE_COLLAPSE`  
  Failure: ULK ALUs, ULMK Atomic Logic Units, Core-19 semantics, and executable AST nodes are merged by matching names/counts.  
  Detect: namespace/owner check.  
  Repair: restore separate registries and explicit mappings.

- `FM-L09-08 / INVENTED_AST_NODE`  
  Failure: a 19th executable node is invented only to match the 19 semantic coordinates.  
  Detect: runtime enum/source comparison.  
  Repair: remove invented mapping; preserve count discrepancy until source evidence resolves it.

- `FM-L09-09 / REWRITE_SHADOWING`  
  Failure: bottom-up child normalization rewrites a single `NLOGIC` before `NLOGIC(NLOGIC(x))` is recognized.  
  Detect: involution/idempotence regression tests.  
  Repair: recognize double-NLOGIC before child descent.

- `FM-L09-10 / REWRITE_CYCLE`  
  Failure: inverse rewrite rules oscillate without a decreasing measure or canonical form.  
  Detect: iteration cap, repeated-state detector, or well-founded-measure check.  
  Repair: orient rewrites toward a declared normal form.

- `FM-L09-11 / PAIRWISE_GLOBAL_CONFUSION`  
  Failure: pairwise satisfiability is treated as proof of global consistency.  
  Detect: run satisfiability over the full conjunction.  
  Repair: reject inconsistent premise sets and preserve the counterexample.

- `FM-L09-12 / CONTRADICTION_ERASURE`  
  Failure: contradictory inputs are silently removed or averaged away.  
  Detect: contradiction/provenance audit.  
  Repair: retain contradiction state and return `INCONSISTENT_INPUT` or `COMPETING` as appropriate.

- `FM-L09-13 / NON_ENTAILMENT_AS_FALSE`  
  Failure: a conclusion not entailed by premises is labeled false.  
  Detect: countermodel/status audit.  
  Repair: return `NOT_ENTAILED`; falsity requires separate evidence.

- `FM-L09-14 / CAUSAL_OVERREACH`  
  Failure: implication, sequence, correlation, adjacency, prediction, or topology is promoted to causation.  
  Detect: causal claim without bound causal evidence/model.  
  Repair: return `UNKNOWN/GAP` and route to a causal engine.

- `FM-L09-15 / TOTAL_19X19_FABRICATION`  
  Failure: 361 pair coordinates are treated as 361 defined semantic equations.  
  Detect: cell-status audit.  
  Repair: restore partial-map semantics and mark undefined cells `UNBOUND`.

- `FM-L09-16 / TRUTH4_COLLAPSE`  
  Failure: `BOTH` or `NEITHER` evidence states are collapsed into one Boolean channel.  
  Detect: four-state round-trip/negation tests.  
  Repair: preserve both evidence-support bits.

- `FM-L09-17 / PARADOX_UNIVERSALIZATION`  
  Failure: a historical executable rewrite for `PARADOX` or `DLOGIC` is presented as a universal definition.  
  Detect: source-scope and rule-class audit.  
  Repair: label the rewrite `SOURCE_DEFINED` for the observed runtime snapshot only.

- `FM-L09-18 / TENSOR_AXIS_SWAP`  
  Failure: row, column, scale, context, or regime axes are exchanged or omitted.  
  Detect: tensor-coordinate type check.  
  Repair: reject the tensor state and reconstruct with explicit typed axes.

- `FM-L09-19 / NONSTANDARD_INFINITY_PROMOTION`  
  Failure: `1E∞` is used as standard mathematical dimension/cardinality notation.  
  Detect: math audit.  
  Repair: replace with an explicit typed index set and separately define any actual cardinality claim.

- `FM-L09-20 / PROVENANCE_LOSS`  
  Failure: an inference result loses premise/source ancestry.  
  Detect: missing dependency IDs/provenance fields.  
  Repair: block promotion and re-run from source-bound premises.

- `FM-L09-21 / STALE_BINDING_REUSE`  
  Failure: a result is reused after source version, scope, regime, or checker identity changes.  
  Detect: freshness/version mismatch.  
  Repair: mark dependent result `STALE` and revalidate the smallest affected closure.

- `FM-L09-22 / CONFIDENCE_INFLATION`  
  Failure: a conjunctive conclusion receives confidence above a necessary premise without a justified strengthening rule.  
  Detect: confidence-ceiling check.  
  Repair: cap or return unknown according to premise evidence.

- `FM-L09-23 / MISSING_CONFIDENCE_IMPUTATION`  
  Failure: missing confidence is silently replaced by a numeric value.  
  Detect: unknown-value audit.  
  Repair: preserve unknown ceiling.

- `FM-L09-24 / FRESHNESS_CANON_PROMOTION`  
  Failure: a newer repair file is treated as Canon solely because it is newer.  
  Detect: canon authority/promotion-evidence gate.  
  Repair: keep candidate status until explicit canon admission succeeds.

## Repair ordering

When several failures occur together, repair in this order:

```text
TYPE / NAMESPACE
-> SOURCE / VERSION
-> FRAGMENT CAPABILITY
-> P02 / CAUSAL BOUNDARIES
-> CONSISTENCY
-> REWRITE SEMANTICS
-> PROVENANCE / FRESHNESS
-> CONFIDENCE / STATUS
```

A downstream repair must not hide an unresolved upstream failure.

## Hard boundary

```text
LOCAL_REPAIR != CANON_PROMOTION
PASSING_TEST != UNIVERSAL_PROOF
STALE != FALSE
QUARANTINE != DELETE
```

RSCF-NODE

```text
node_id: l09_primitives_failure_modes
node_type: failure_contract
claim_class: AMOS_MODEL
rscf_state: DERIVED
canonical_status: CONDITIONAL
```

**MOC:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L09_INFERENCE/L09_INFERENCE_MOC|L09_INFERENCE_MOC]]
