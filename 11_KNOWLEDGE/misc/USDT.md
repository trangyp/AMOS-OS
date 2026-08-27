---
title: USDT
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general

---


# Usdt
## UCIA™ Stablecoin Qualification Audit (USDT)
**Goal:** assess whether USDT qualifies as **institution-grade stable value infrastructure** under the Law of Law (boundary-closed invariants + deterministic fail-modes).
**Result format:** Facts → Gate checks → Termination (Valid / Bounded / Invalid).
* * *
# 1) Verifiable baseline facts (public, source-backed)
### Redemption / access constraints
  * Tether’s own redemption flow requires a **verified Tether.to account** and states a **minimum redemption amount of 100,000 USD equivalent**.


  * Tether’s fee page states **minimum acquisition/redemption 100,000 USD** , and **redemption fee is the greater of $1,000 or 0.1%**.


  * Tether states it maintains **sole discretion** to approve or not approve accounts (verification).


### Reserve reporting / assurance
  * Tether publishes quarterly reserve reports/attestations (their transparency page includes a disclaimer that the published reserve info is “for transparency purposes only” and “derived from the latest published reserves report” and “has not been updated regardless of any material changes” after the report date).


  * Tether’s Oct 31, 2025 post states the **Q3 2025 attestation** was prepared by **BDO** , and includes management assertions for Sept 30, 2025: reserves ~$181.223B, liabilities ~$174.445B, and excess ~$6.778B.


### Regulator enforcement history (New York)
  * NY Attorney General announcement (Feb 23, 2021) states Bitfinex and Tether must end trading activity with New Yorkers and references allegations about reserve representations and reporting requirements as part of the resolution.


### Third-party risk view (not a “proof,” but admissible as an external assessment)
  * Reporting on S&P Global’s stablecoin stability assessment indicates S&P downgraded USDT to **“weak”** and cites **reserve risk** and **disclosure gaps** as key concerns.


* * *
# 2) UCIA Gate Checks (institution-grade admissibility)
## Gate A — Authority + Identity closure
**Invariant:** authority must be identity-bound, role-scoped, revocable; end-user redemption must be broadly executable (not only for a narrow class).
**Observation:** direct redemption is gated by verified account approval and minimum size (100k) and fee structure; approval discretion exists.
**UCIA assessment:** **Bounded** (access is not universal; authority/eligibility is issuer-controlled).
* * *
## Gate B — Exit continuity (redeemability under stress)
**Invariant:** redemption must be enforceable and operationally executable across stress, not dependent on discretionary approval or narrow channels.
**Observation:** redemption is limited to verified customers and minimum thresholds.
**UCIA assessment:** **Bounded** (exit exists, but is not universally accessible; stress behavior is not defined in a deterministic public “fail-mode constitution”).
* * *
## Gate C — Reserve truth admissibility (audit-grade reality binding)
**Invariant:** reserves must be continuously verifiable at audit-grade depth with clear segregation/custody and stress-liquidation clarity.
**Observation:** Tether provides attestations and reserve reports; transparency page warns reserve info is management-prepared and not updated after report date.
**UCIA assessment:** **Bounded** (attestation is not the same as full-scope audit + real-time verifiability; temporal gaps remain by their own disclosure).
* * *
## Gate D — Governance sealing (no silent mutation)
**Invariant:** rules (issuance/redemption controls, reserve policy, discretionary powers) must be constitutionally constrained and change-controlled.
**Observation:** published materials show issuer discretion in account approval and operational processing; no publicly sealed constitution shown in the sources above.
**UCIA assessment:** **Bounded** (governance appears issuer-discretionary; constitution/invariant sealing is not publicly demonstrated here).
* * *
## Gate E — Jurisdictional portability
**Invariant:** cross-border enforceability must be explicit (who can sue where; how constraints apply by regime).
**Observation:** NY enforcement history exists; this supports the general point that jurisdictional constraints matter and can be imposed externally.
**UCIA assessment:** **Bounded** (institution-grade requires explicit portability mappings; not demonstrated in the cited public materials).
* * *
## Gate F — Independent risk assessment compatibility
**Invariant:** major external assessors should not flag structural disclosure gaps that threaten peg maintenance.
**Observation:** S&P-reported downgrade to “weak” citing reserve risk and disclosure gaps.
**UCIA assessment:** **Bounded** (external risk signal conflicts with institution-grade qualification).
* * *
# 3) UCIA Termination (current classification)
### USDT classification: **STRUCTURALLY BOUNDED (Not institution-grade)**
Reason: multiple core invariants are **not closed** at the system boundary:
  * redemption is **not universally executable** (eligibility + minimum size gate)


  * reserve truth is **time-bounded** and management-reported with explicit “not updated” disclaimer


  * governance/constitution sealing is **not demonstrated** in a way that closes rule-mutation and fail-mode requirements (based on the cited public materials)


This is not a claim of fraud. It is a qualification result: **USDT may function operationally** , but it does not meet **institution-grade capital admissibility** under Law-of-Law closure.
* * *
# 4) What would make USDT “Qualified” under your OS (minimal fixes)
To move from **Bounded → Valid** , the issuer would need to publish and enforce:
  1. **Constitution layer:** non-amendable invariants (reserve admissibility, segregation, redemption rules) + change-control.


  2. **Reserve truth system:** audit-grade scope + custody/segregation disclosure + higher-frequency verifiability (not just quarterly snapshots).


  3. **Redemption fail-modes:** deterministic, pre-committed behavior under stress (freeze/throttle/haircut rules), plus who is eligible and why.


  4. **Jurisdiction matrix:** enforceability mapping across regimes (who can redeem, where disputes settle, what happens under injunction/sanctions).


* * *
\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
