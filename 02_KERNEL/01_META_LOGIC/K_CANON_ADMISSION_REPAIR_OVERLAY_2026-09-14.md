---
title: K_CANON Admission Repair Overlay — 2026-09-14
origin_architect: Trang Phan
type: kernel_repair_overlay
status: ACTIVE_REPAIR_OVERLAY
conclusion_class: AMOS_MODEL
canonical_status: NOT_CANON_PROMOTION
amos_core_target: v4.4
created: 2026-09-14
---

# K_CANON Admission Repair Overlay — 2026-09-14

## Purpose

This overlay repairs the active interpretation of `02_KERNEL/K_CANON.md` without deleting the preserved historical source artifact.

The historical expression

```text
IsVerified(phi) AND Confidence(phi) >= 0.95 -> PromoteToCanon(phi)
```

is **not** sufficient as an executable canon-promotion rule. Confidence is neither authority nor provenance independence, contradiction resolution, source identity, semantic typing, implementation evidence, nor commit-time freshness.

Origin architect / steward: **Trang Phan**.

## Bounded admission model

For a candidate `c`, define the following Boolean evidence predicates:

```text
SR(c)  source identity/version/hash resolved
PT(c)  provenance traceable
ST(c)  semantics typed
AB(c)  assumptions/boundaries bound
CF(c)  no unresolved contradiction under the same scope
EQ(c)  equations checked when c makes mathematical claims
CE(c)  counterexamples/boundaries checked when required
IR(c)  implementation receipt present when implementation is claimed
```

Then define candidate evidence eligibility as an AMOS control-plane definition:

```text
Eligible(c)
  := SR(c) AND PT(c) AND ST(c) AND AB(c) AND CF(c)
     AND (NOT MathClaim(c) OR (EQ(c) AND CE(c)))
     AND (NOT ImplementationClaim(c) OR IR(c)).
```

If an unresolved competing claim exists, the candidate remains `COMPETING`. If an unresolved contradiction exists under the same scope/assumptions, the candidate is quarantined pending repair or discrimination.

## Authority boundary

Let `w` be an authority witness and `p` the current canon-policy identity.

```text
AuthorizedForPrepare(w, p)
  := HasScope(w, "canon:promote")
     AND PolicyHash(w) = Hash(p).
```

Evidence can establish eligibility. It cannot manufacture authority.

The prepare condition is:

```text
PrepareAllowed(c, w, p)
  := Eligible(c) AND AuthorizedForPrepare(w, p).
```

`PrepareAllowed` does **not** itself mutate Canon.

## Commit-time freshness

A prepared candidate must bind at least:

```text
candidate_id
source_hash
canon_policy_hash
baseline_id
baseline_hash
authority_id
authority_policy_hash
```

At commit, revalidate the current source, policy, baseline, and authority identities.

```text
Committable
  := Prepared
     AND SourceFresh
     AND PolicyFresh
     AND BaselineFresh
     AND AuthorityFresh.
```

Any changed bound identity returns a revalidation state rather than silently committing.

## Confidence firewall

`confidence` may be retained as evidence metadata, calibration information, or ranking support. It is intentionally absent from the necessary-and-sufficient admission formula above.

Therefore:

```text
Confidence(c) = 1
```

cannot compensate for a failed provenance, contradiction, semantic, evidence, authority, or freshness gate.

## Executable binding

Bounded reference implementation:

- `03_CONTROL_PLANE/03_POLICY/canon_admission_gate.py`

Tests:

- `03_CONTROL_PLANE/03_POLICY/test_canon_admission_gate.py`

The executable gate returns eligibility/prepare/commit decisions. A `COMMITTABLE` result is still not itself a durable canon write; the actual write remains subordinate to the infrastructure commit/release plane.

## Historical-source handling

`02_KERNEL/K_CANON.md` remains preserved for provenance. Repeated numbered rules or confidence-threshold formulas inside it must not be interpreted as current executable promotion authority where they conflict with this governed repair overlay and the current control-plane contract.

## Status boundary

`ACTIVE_REPAIR_OVERLAY / AMOS_MODEL`

`SYSTEM_WIDE_CANON_ENFORCEMENT = PARTIAL`

`AUTO_PROMOTION_BY_CONFIDENCE = REJECTED`
