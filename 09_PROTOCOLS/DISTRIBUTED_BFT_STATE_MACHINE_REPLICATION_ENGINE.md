---
title: Distributed Byzantine Fault-Tolerant (BFT) State Machine Replication Engine
type: protocol_specification
plane: 09_PROTOCOLS
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: FORMAL_PROOF
rscf:
  state: DERIVED
  claim_class: FORMAL_PROOF
  provenance:
    - 09_PROTOCOLS/09_PROTOCOLS_MOC
    - 09_PROTOCOLS/PROTOCOLS_README
    - 09_PROTOCOLS/PROTOCOLS_PROTOCOL_CONTRACT
    - 09_PROTOCOLS/DISTRIBUTED_RAFT_CONSENSUS_AND_CAS_SYNC_ENGINE
  scope: bft_state_machine_replication
tags:
  - amos-os
  - protocols
  - bft
  - pbft
  - state-machine-replication
  - byzantine-fault-tolerance
  - threshold-signatures
  - quorum-intersection
---

# Distributed Byzantine Fault-Tolerant (BFT) State Machine Replication Engine

## 1. Executive Summary & SMR Architecture

The **Distributed Byzantine Fault-Tolerant (BFT) State Machine Replication Engine** (`09_PROTOCOLS`) provides malicious-fault-resilient, linearizable consensus across distributed AMOS nodes.

Operating under the $3f + 1$ Byzantine threshold ($N = 7, f = 2$), it tolerates arbitrary adversarial packet corruption, equivocation, and silent node dropouts via **3-Phase Commit (Pre-Prepare, Prepare, Commit)** and **BLS12-381 Threshold Signature Aggregation**.

```
+----------------------------------------------------------------------------------------------------+
|                         7-NODE BYZANTINE FAULT-TOLERANT (BFT) SMR PIPELINE                         |
|                                                                                                    |
|    [ Cluster Topology: $\{N_1, N_2, \dots, N_7\}$ with $f = 2$ Malicious / Corrupted Nodes ]       |
|                                            ||                                                      |
|                                            \/                                                      |
|    [ Phase 1: Pre-Prepare — Primary Leader $L_v$ Broadcasts Proposal $\langle m, d, v, n \rangle$ ]|
|                                            ||                                                      |
|                                            \/                                                      |
|    [ Phase 2: Prepare — Replicas Broadcast Prepare $\langle \text{PREPARE}, v, n, d, i \rangle_{\sigma_i}$ ]|
|                                            ||                                                      |
|                   +------------------------+------------------------+                              |
|                   |                                                 |                              |
|                   \/ ($\ge 2f + 1 = 5$ Valid Prepare Signatures)    \/ (Byzantine Equivocation)    |
|    [ Phase 3: Commit — 2f+1 Signed Commit Messages Aggregated ]     [ Reject Corrupted Payload ]   |
|    - Aggregate BLS Threshold Signature Created                      - Trigger View Change $v+1$    |
|    - Monotonic State Mutation Sealed in `12_STATE`                  - Quarantine Malicious Nodes   |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Mathematical Formalism & Quorum Intersection

### 2.1 Quorum Intersection Property
For cluster size $N = 3f + 1$ and quorum size $Q = 2f + 1$:

$$|\mathcal{Q}_1 \cap \mathcal{Q}_2| = |\mathcal{Q}_1| + |\mathcal{Q}_2| - |\mathcal{Q}_1 \cup \mathcal{Q}_2| \ge (2f + 1) + (2f + 1) - (3f + 1) = f + 1$$

Since at most $f$ nodes are Byzantine, at least $(f + 1) - f = 1$ honest node exists in the intersection of any two quorums, preventing split-brain states and conflicting commits.

### 2.2 Threshold Signature Aggregation
Given partial signatures $\sigma_i = H(m)^{s_i}$, the aggregate signature is:

$$\sigma_{\text{agg}} = \prod_{i \in \mathcal{Q}} \sigma_i^{\lambda_i(0)}, \quad e(\sigma_{\text{agg}}, g_2) = e(H(m), \text{APK})$$

---

## 3. Operational Invariants & Performance SLAs

- `INV-PROT-BFT-001` (**Byzantine Safety Invariant**): Zero state divergence under any adversarial coalition of $\le f$ nodes.
- `INV-PROT-BFT-002` (**Quorum Intersection Barrier**): Quorum acknowledgment threshold strictly requires $|\mathcal{Q}| \ge 2f + 1 = 5$ signatures.
- `INV-PROT-BFT-003` (**Sub-10ms 3-Phase SLA**): Complete 3-phase consensus traversal executes in $\tau_{\text{BFT}} \le 10.0\text{ ms}$.

---

## 4. Master Navigation & Bindings

- **Protocols MOC:** [[09_PROTOCOLS/09_PROTOCOLS_MOC|09_PROTOCOLS_MOC]]
- **BFT SMR Ledger:** [[09_PROTOCOLS/BFT_SMR_EXECUTION_LEDGER|BFT_SMR_EXECUTION_LEDGER]]
- **RAFT Consensus Engine:** [[09_PROTOCOLS/DISTRIBUTED_RAFT_CONSENSUS_AND_CAS_SYNC_ENGINE|DISTRIBUTED_RAFT_CONSENSUS_AND_CAS_SYNC_ENGINE]]
- **Protocols Contract:** [[09_PROTOCOLS/PROTOCOLS_PROTOCOL_CONTRACT|PROTOCOLS_PROTOCOL_CONTRACT]]
