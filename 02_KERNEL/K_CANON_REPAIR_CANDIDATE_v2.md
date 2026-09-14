---
title: K Canon Governance Kernel Repair Candidate v2
origin_architect: Trang Phan
amos_core_target: v4.4
status: ACTIVE_REPAIR_CANDIDATE_NOT_CANON
canonical_parent: 02_KERNEL/K_CANON.md
conclusion_class: MODEL
epistemic_class: DERIVED
---

# K Canon Governance Kernel Repair Candidate v2

This candidate repairs the current K_CANON promotion logic without modifying the canonical parent in place. It treats Canon as an **AMOS authority state**, not a synonym for universal truth.

## 1. Rejected promotion rule

The current parent repeats a rule of the form

`IsVerified(phi) AND Confidence(phi) >= 0.95 => PromoteToCanon(phi)`.

This is rejected as a governance rule. A confidence score is metadata about an assessment; it is neither a proof rule nor an authority witness. No fixed scalar confidence threshold may create Canon authority.

## 2. Typed proposal state

For proposal `p`, define the promotion state

`P(p) = (I,T,S,R,F,Pr,E,V,X,A,C,G)`

where:

- `I`: stable proposal and payload identity;
- `T`: epistemic class and conclusion class are valid and distinct coordinates;
- `S`: scope is explicit;
- `R`: regime is explicit;
- `F`: freshness is established;
- `Pr`: proof capsule passes under its declared formal/empirical scope;
- `E`: at least two provenance-independent evidence roots exist;
- `V`: at least two distinct validators pass;
- `X`: no active load-bearing contradiction remains unresolved;
- `A`: an authority witness is valid and bound to the exact claim/effect;
- `C`: compare-and-swap epoch equals the current Canon epoch;
- `G`: the authority signature verifies over the exact payload digest and epoch.

All coordinates are Boolean predicates after type validation. Then

`Eligible(p) := I AND T AND S AND R AND F AND Pr AND E AND V AND X AND A AND C AND G`.

This is a **definition of commit eligibility**, not an empirical theorem.

## 3. Canon transition

Let `K_t` be the immutable Canon object set at epoch `t` and `p` a candidate object.

If `Eligible(p)=False`, then

`K_(t+1) = K_t`.

If `Eligible(p)=True`, the in-process gate may emit `COMMIT_ELIGIBLE`, but the Canon state changes only after a provider-side durable commit receipt verifies the exact payload, authority witness, expected epoch, and resulting object identity.

Therefore:

`ELIGIBLE != COMMITTED`

`COMMITTED != EMPIRICALLY_TRUE`

`CANONICAL != UNIVERSALLY_TRUE`

`SIGNATURE_VALID != SIGNER_AUTHORIZED`

The signer public key must itself resolve through the current authority registry/trust root.

## 4. Rule of 2 as provenance topology

Two evidence objects are not independent merely because they have different filenames, URLs, validators, or paraphrases.

For evidence roots `e_i,e_j`, independence requires at minimum:

1. different semantic/root origins;
2. neither root is an ancestor of the other;
3. their ancestry intersection is empty after removing explicitly declared common trust roots.

Repeated descendants of one source count as one origin. Sybil/alias/paraphrase multiplication does not satisfy Rule of 2.

## 5. Evidence topology versus conclusion class

Evidence topology uses:

`SOURCE_CLAIM | OBSERVATION | DERIVED | MODEL | DECISION | UNKNOWN`.

Conclusion class uses:

`VERIFIED | DERIVED | MODEL | CONDITIONAL | COMPETING | UNKNOWN/GAP`.

The two axes must never be collapsed. `VERIFIED` is not an epistemic-origin type. `SOURCE_CLAIM` is not a conclusion class.

## 6. Proof capsule boundary

A proof capsule must identify:

- exact claim/payload hash;
- assumptions;
- scope and regime;
- checker/prover/test identity and version/hash;
- evidence/provenance roots;
- falsifiers and invalidation conditions;
- result state including `UNKNOWN` where applicable.

A formal proof licenses only the encoded formal proposition under its assumptions. Empirical claims require empirical evidence appropriate to their domain.

## 7. Cryptographic commitment

The executable candidate uses:

- SHA-256 canonical payload digests;
- RFC-9162-style Merkle leaf/internal-node domain separation (`0x00` leaf, `0x01` internal node) for append commitments;
- Ed25519 signature verification consistent with RFC 8032 primitives.

Merkle inclusion/consistency proves commitment relationships, not semantic truth. Signature verification proves possession/use of a corresponding private key, not that the signer had AMOS authority unless the key is independently bound to current authority.

## 8. Immutable update semantics

Canonical objects are immutable after durable commit. Correction does not overwrite history. A correction creates a new object with an explicit relation such as:

`SUPERSEDES(new, old)`

or

`REVOKES(new, old)`.

Currentness is determined by the authority/version graph, not by latest-filename-wins.

## 9. Contradiction handling

An active load-bearing contradiction blocks promotion. Contradiction must be resolved by evidence, scope partitioning, conditionalization, supersession, or explicit `COMPETING`; not by averaging confidence or selecting the more popular source.

## 10. Confidence semantics

A bounded confidence value `c in [0,1]` may be stored as metadata. It is deliberately excluded from `Eligible(p)`.

Thus for otherwise identical proposal states and any `c1,c2 in [0,1]`:

`Eligible(p,c1) = Eligible(p,c2)`.

If a domain uses calibrated probabilities, those probabilities remain domain evidence; they do not create Canon authority.

## 11. Executable candidate

Reference implementation:

`04_RUNTIME/01_REFERENCE_IMPLEMENTATION/canon_promotion_gate_v2.py`

Observed bounded validation in this repair pass:

- 1,016 deterministic/property checks pass;
- low versus high confidence cannot flip an otherwise identical eligibility result;
- stale proof/freshness, contradiction, correlated evidence, failed validator, epoch mismatch, bad signature, and expired authority all fail closed;
- Merkle hashing is deterministic, ordered, and domain-separated.

## 12. External algorithm provenance

- RFC 8032: EdDSA / Ed25519 primitives.
- RFC 9162: Merkle Tree Hash inclusion/consistency construction used as the commitment pattern.
- in-toto Attestation Framework is retained as an external provenance/attestation reference family, not copied into Canon by reference.

## 13. Promotion status

This file is a repair candidate only.

`K_CANON_REPAIR_CANDIDATE != K_CANON`

Actual Canon promotion requires a separate, current, authorized K_CANON transition after review and durable commit evidence.
