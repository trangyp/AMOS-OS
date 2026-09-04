---
title: SCOPE_REGIME_FIREWALL — Epistemic Regime Boundary Law
type: law
source: 01_CANON/01_CORE_LAWS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
updated: 2026-09-04
tags:
  - canon
  - core_law
  - firewall
  - epistemic_boundary
  - law/L0-integrity
  - provenance-x-confidence
  - law/L5-scope-regime
  - law/L21-epistemic-regime
  - epistemic-regimes
  - law/L30-authority-boundary
  - persistent-provenance
  - fail-closed-governance
  - scope-regime-validation-receipt
rscf:
  state: CANON_LAW
  claim_class: CANONICAL_INVARIANT
  provenance: AMOS_CANON
---

# SCOPE_REGIME_FIREWALL — Epistemic Regime Boundary Law

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Epistemic Class:** `CANONICAL_INVARIANT`
> **Status:** `ACTIVE_CANON_LAW`

The SCOPE_REGIME_FIREWALL strictly prohibits reasoning principles, heuristics, or confidence ratings valid in one regime (e.g. theoretical modeling) from leaking un-gated into distinct operational regimes (e.g. safety-critical execution).

______________________________________________________________________

## 1. Architectural Scope

`SCOPE_REGIME_FIREWALL` governs the epistemic regime boundary subsystem of the AMOS Full OS MECE architecture. It applies to all cross-regime transfers of claims, confidence ratings, and reasoning principles. The law enforces a **fail-closed** default: absent an explicit boundary witness, no cross-regime transfer is permitted.

This law binds to [[01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME|L5_SCOPE_REGIME]], [[01_CANON/01_CORE_LAWS/L21_EPISTEMIC_REGIME|L21_EPISTEMIC_REGIME]], and [[01_CANON/01_CORE_LAWS/L30_AUTHORITY_BOUNDARY|L30_AUTHORITY_BOUNDARY]].

______________________________________________________________________

## 2. Formal Definition

A **regime transfer** is the movement of a claim $C$ from epistemic regime $\text{Regime}_A$ to $\text{Regime}_B$:

$$\text{RegimeTransfer}(C, \text{Regime}_A, \text{Regime}_B) \le \text{Gate}(\text{BoundaryWitness})$$

where $\text{Gate}(\text{BoundaryWitness})$ is a gating function that evaluates whether a valid boundary witness authorizes the transfer. The gate returns `TRUE` only when:

1. A boundary witness (authority signature, test evidence, or independent corroboration) is present.
2. The witness is valid for the target regime $\text{Regime}_B$.
3. The witness is current (not stale or expired).
4. The witness is independent of the agent requesting the transfer.

Absent a valid witness, the gate returns `FALSE` and the transfer is blocked (fail-closed).

______________________________________________________________________

## 3. Governing Invariants

$$\text{RegimeTransfer}(C, \text{Regime}_A, \text{Regime}_B) \le \text{Gate}(\text{BoundaryWitness})$$

- **SRF-1 Fail-Closed Default:** In the absence of a valid boundary witness, all cross-regime transfers are blocked. The system defaults to denial, not permission.
- **SRF-2 No Silent Leak:** Any cross-regime transfer must produce an auditable boundary witness record in the provenance log.
- **SRF-3 Scope Monotonic Shrink:** Authorized scope can only shrink or stay constant within a session; it cannot self-expand without a fresh authority grant.
- **SRF-4 Regime Isolation:** Concurrent agents operating in distinct regimes observe isolated projections; no un-gated cross-contamination is permitted.
- **SRF-5 Asymmetric Transfer:** Transferring from a stricter regime to a laxer regime (downgrade) is permitted with audit; transferring from a laxer regime to a stricter regime (upgrade) requires a boundary witness.

______________________________________________________________________

## 4. Mathematical Formulation

### 4.1 Regime Transfer Gate

$$\text{Gate}(\text{BoundaryWitness}) = \begin{cases} \text{TRUE} & \text{if witness is present, valid, current, and independent} \\ \text{FALSE} & \text{otherwise} \end{cases}$$

### 4.2 Fail-Closed Law

$$\neg \text{Gate}(\text{BoundaryWitness}) \implies \text{RegimeTransfer}(C, A, B) = \text{BLOCKED}$$

### 4.3 Scope Monotonicity

$$\text{Scope}(t_{n+1}) \subseteq \text{Scope}(t_n) \quad \text{(within a session without fresh authority)}$$

### 4.4 Regime Strictness Ordering

$$\text{SafetyCritical} \succ \text{Operational} \succ \text{Theoretical} \succ \text{Exploratory}$$

where $\succ$ denotes "stricter than". Downgrade ($\succ$ direction) is permitted with audit; upgrade ($\prec$ direction) requires witness.

______________________________________________________________________

## 5. MECE Mapping to AMOS Full Brain OS

| Firewall Dimension | Affected AMOS Stage | Canonical Gate |
|-------------------|---------------------|----------------|
| Fail-closed default | Route / Execute | `L0_INTEGRITY` |
| Boundary witness | Plan / Commit | `L7_AUTHORITY` |
| Scope monotonicity | Perceive / Route | `L5_SCOPE_REGIME` |
| Regime isolation | Execute / Observe | `L21_EPISTEMIC_REGIME` |
| Asymmetric transfer | Admit / Plan | `L30_AUTHORITY_BOUNDARY` |

______________________________________________________________________

## 6. Safety Invariants

- `INV-SRF-001` (**No bypass:**) A regime boundary cannot be bypassed by reclassifying the regime of a claim without an authority witness.
- `INV-SRF-002` (**No silent transfer:**) Every cross-regime transfer produces an auditable record; un-audited transfers are treated as violations.
- `INV-SRF-003` (**No scope self-expansion:**) An agent may not widen its authorized scope without a fresh authority grant from an independent source.
- `INV-SRF-004` (**No cross-contamination under concurrency:**) Concurrent agents in distinct regimes observe isolated projections; shared state is mediated by the firewall.
- `INV-SRF-005` (**Witness independence:**) The boundary witness must be independent of the agent requesting the transfer; self-issued witnesses are invalid.

______________________________________________________________________

## 7. Navigation & Bindings

- **Master MOC:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- **Partition Architecture:** [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
- **Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Core Laws MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]
- **Index MOC:** [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]]
- **Validation Receipt:** [[01_CANON/01_CORE_LAWS/SCOPE_REGIME_VALIDATION_RECEIPT|SCOPE_REGIME_VALIDATION_RECEIPT]]
- **Related Laws:** [[01_CANON/01_CORE_LAWS/L0_INTEGRITY|L0_INTEGRITY]] · [[01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME|L5_SCOPE_REGIME]] · [[01_CANON/01_CORE_LAWS/L21_EPISTEMIC_REGIME|L21_EPISTEMIC_REGIME]] · [[01_CANON/01_CORE_LAWS/L30_AUTHORITY_BOUNDARY|L30_AUTHORITY_BOUNDARY]] · [[01_CANON/01_CORE_LAWS/PERSISTENT_PROVENANCE|PERSISTENT_PROVENANCE]] · [[01_CANON/01_CORE_LAWS/FAIL_CLOSED_GOVERNANCE|FAIL_CLOSED_GOVERNANCE]]
- **Related Matrices:** [[25_COGNITIVE_MATRIX/PROVENANCE_X_CONFIDENCE|PROVENANCE_X_CONFIDENCE]] · [[01_CANON/01_CORE_LAWS/EPISTEMIC_REGIMES|EPISTEMIC_REGIMES]]

______________________________________________________________________

## 8. Known Gaps & Falsifiers

- `GAP-SRF-001`: The regime strictness ordering (SafetyCritical $\succ$ Operational $\succ$ Theoretical $\succ$ Exploratory) is a declared hierarchy; novel regimes not in this ordering default to `BLOCK` until classified.
- `GAP-SRF-002`: The boundary witness independence requirement assumes a supply of trustworthy independent validators; in single-source or low-trust environments, all transfers default to `BLOCK`.
- `GAP-SRF-003`: Concurrent regime isolation assumes the runtime correctly enforces projection isolation; if the runtime substrate is compromised, isolation may be violated.
- **Falsifier:** If any claim transfers from a laxer regime to a stricter regime without a valid boundary witness, the fail-closed invariant (`SRF-1`) is falsified.
- **Falsifier:** If any agent widens its authorized scope without a fresh authority grant, the scope monotonicity invariant (`SRF-3`) is falsified.

______________________________________________________________________

**Related:** [[01_CANON/01_CORE_LAWS/L0_INTEGRITY|L0_INTEGRITY]] · [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]] · [[25_COGNITIVE_MATRIX/PROVENANCE_X_CONFIDENCE|PROVENANCE_X_CONFIDENCE]] · [[01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME|L5_SCOPE_REGIME]] · [[01_CANON/01_CORE_LAWS/L21_EPISTEMIC_REGIME|L21_EPISTEMIC_REGIME]] · [[01_CANON/01_CORE_LAWS/EPISTEMIC_REGIMES|EPISTEMIC_REGIMES]] · [[01_CANON/01_CORE_LAWS/L30_AUTHORITY_BOUNDARY|L30_AUTHORITY_BOUNDARY]] · [[01_CANON/01_CORE_LAWS/PERSISTENT_PROVENANCE|PERSISTENT_PROVENANCE]] · [[01_CANON/01_CORE_LAWS/FAIL_CLOSED_GOVERNANCE|FAIL_CLOSED_GOVERNANCE]] · [[01_CANON/01_CORE_LAWS/SCOPE_REGIME_VALIDATION_RECEIPT|SCOPE_REGIME_VALIDATION_RECEIPT]]

**MOC:** [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] · [[00_ROOT/00_HOME|00_HOME]]

______________________________________________________________________

RSCF-NODE
node_id: scope_regime_firewall
node_type: core_law
path: 01_CANON/01_CORE_LAWS/SCOPE_REGIME_FIREWALL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- RELATED_TO: [[01_CANON/01_CORE_LAWS/L0_INTEGRITY|L0_INTEGRITY]]
- RELATED_TO: [[01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME|L5_SCOPE_REGIME]]
- RELATED_TO: [[01_CANON/01_CORE_LAWS/L21_EPISTEMIC_REGIME|L21_EPISTEMIC_REGIME]]
- RELATED_TO: [[01_CANON/01_CORE_LAWS/L30_AUTHORITY_BOUNDARY|L30_AUTHORITY_BOUNDARY]]
- RELATED_TO: [[01_CANON/01_CORE_LAWS/PERSISTENT_PROVENANCE|PERSISTENT_PROVENANCE]]
- RELATED_TO: [[01_CANON/01_CORE_LAWS/FAIL_CLOSED_GOVERNANCE|FAIL_CLOSED_GOVERNANCE]]
- RELATED_TO: [[01_CANON/01_CORE_LAWS/SCOPE_REGIME_VALIDATION_RECEIPT|SCOPE_REGIME_VALIDATION_RECEIPT]]
