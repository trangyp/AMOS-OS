---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Security Schema
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

# Security Schema

## 0. Status

`SECURITY_SCHEMA.md` is a **typed schema specification** for AMOS security artifacts under `18_SECURITY`. It is an `AMOS_MODEL` specification: NOT executed, NOT validated, NOT enforced as a validator. Implementation/validation `NOT_ESTABLISHED` / `PARTIAL`.

Governing boundaries preserved:

```text
CAPABILITY != AUTHORITY
TOOL_AVAILABLE != TOOL_AUTHORIZED
TRUST_SCORE != ROOT_KEY
AUTHORIZATION != COMMIT
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

---

## 1. Purpose

A security artifact types the primitives of access control — principal, identity, credential, credential permission, scope, and limits — together with revocation, provenance, least-privilege checks, and traceability. `SECURITY_SCHEMA.md` ensures that capability (knowing how) is never conflated with authority (being permitted), and that a tool being available is never treated as it being authorized.

---

## 2. Governing rules

- `CAPABILITY != AUTHORITY` — capability packaging never grants authority.
- `TOOL_AVAILABLE != TOOL_AUTHORIZED` — a tool's presence/availability does not imply a grant to use it.
- Least privilege: a grant is the minimal permission sufficient for the declared purpose.
- Every consequential authorization and every revocation is traceable and revocable.
- Fail closed: absence of an explicit grant means denial.

---

## 3. Security artifact schema

| name | type | required | description | constraints |
| :--- | :--- | :--- | :--- | :--- |
| `principal` | object | true | The entity acting | see §4 |
| `identity` | object | true | Identity that binds the principal | see §5 |
| `credential` | object | true | Secret/verifier used to authenticate | see §6 |
| `permission` | object | true | The authorization being granted | see §7 |
| `scope` | object | true | Resource/action bounds of the grant | see §8 |
| `limits` | object | true | Rate, budget, and temporal limits | see §9 |
| `valid_from` | string | true | Effective start of the grant | ISO-8601 |
| `valid_until` | string | false | Effective end of the grant (null = no expiry) | ISO-8601 |
| `revoked` | boolean | true | Whether the grant has been revoked | |
| `authority_ref` | string | true | Governing authority source | epoch-valid required |
| `provenance` | object | true | Source and lineage of the grant | see §11 |
| `least_privilege_checks` | array | false | Checks that the grant is minimal | see §12 |
| `revocability` | object | true | Whether and how the grant can be revoked | see §13 |
| `traceability` | object | true | Audit recording of the grant | see §14 |

---

## 4. Principal

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `principal_id` | string | true | Identifier of the acting entity |
| `principal_type` | string | true | enum: `agent` / `engine` / `user` / `process` / `service` |
| `endpoint` | string | false | Origin endpoint, if remote |

---

## 5. Identity

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `identity_id` | string | true | Stable identity identifier |
| `identity_class` | string | true | Class of identity (e.g. `verified`, `derived`, `unknown`) |
| `authentication_method` | string | false | Method used to establish identity |

A principal's identity must be bound and verifiable before any grant is issued.

---

## 6. Credential

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `credential_id` | string | true | Reference to the credential used |
| `credential_type` | string | true | enum: `token` / `key` / `certificate` / `session` |
| `secret_handling` | string | true | Policy for secret protection |
| `rotation` | string | false | Rotation schedule |

Credentials must never be logged or exposed in provenance trails.

---

## 7. Permission

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `allowed_actions` | array | true | Actions the grant permits |
| `forbidden_actions` | array | true | Actions explicitly denied |
| `resource_scope` | array | true | Resources covered by the grant |
| `recipient_scope` | array | false | Who the grant may be delegated to |
| `attenuation` | string | true | `only_tighten` — child grants never widen |
| `approval_required_for` | array | false | Irreversible actions needing approval |

Hard invariant: `ChildAuthority ⊆ ParentAuthority`.

---

## 8. Scope

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `scope_id` | string | true | Identifier of the declared scope |
| `in_scope` | array | true | What is within the grant |
| `out_of_scope` | array | true | What is excluded |
| `regime` | string | true | Regime under which the scope applies |

A grant's effect is empty outside its declared scope and regime.

---

## 9. Limits

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `rate_limit` | object | false | Max operations per window |
| `budget` | object | false | Token / memory / time budget |
| `cumulative_cap` | object | false | Cumulative exposure / consumption cap |

Hard invariant: `AllowedIndividually` does not imply `AllowedCumulatively`.

---

## 10. Freshness & revocation

A grant is actionable only while `valid_from ≤ now < valid_until` and `revoked = false`. Freshness is enforced at commit time:

- `AuthorizedAtPlanTime != AuthorizedAtCommitTime`
- High-impact effects require fresh authority at commit.

`revoked: true` immediately retracts all constraints tied to the grant.

---

## 11. Provenance

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `issuer` | string | true | Who issued the grant |
| `delegate` | string | false | Who delegated it (if any) |
| `policy_epoch` | string | true | Policy epoch in force at issuance |
| `authority_epoch` | string | true | Authority epoch in force at issuance |
| `timestamp` | string | true | Issuance timestamp |

---

## 12. Least-privilege checks

- `LPC1` — every `allowed_action` is necessary for the declared purpose.
- `LPC2` — `resource_scope` is the minimal sufficient set.
- `LPC3` — no forbidden action is silently shadowed by a broad allowed action.
- `LPC4` — the grant is not widened by any nested/delegated grant.

---

## 13. Revocability

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `revocable` | boolean | true | Whether the grant can be revoked |
| `revocation_supported` | boolean | true | Whether revocation mechanics exist |
| `revoked_by` | string | false | Who/which authority revoked it |
| `revoked_at` | string | false | When it was revoked |

Every grant MUST be revocable; non-revocable grants are disabled by default.

---

## 14. Traceability

Each authorization, use, and revocation event is recorded:

| name | type | required | description |
| :--- | :--- | :--- | :--- |
| `event_id` | string | true | Audit event identifier |
| `event_type` | string | true | enum: `grant` / `use` / `deny` / `revoke` / `expire` |
| `actor` | string | true | Who performed the event |
| `timestamp` | string | true | When the event occurred |
| `outcome` | string | true | Result of the event |

Full traceability supports replay and review; it never raises authority by itself.

---

## 15. Status / gaps

- Implementation status: `NOT_ESTABLISHED` — no security-schema validator exists.
- Validation status: `NOT_ESTABLISHED` — no executed receipt for this schema.
- The authz invariant engine ([[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]) is cited as pattern, not as evidence for this schema.

---

## 16. Cross-plane bindings

- Governed by canon — [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|AMOS Core Laws]] · [[01_CANON/01_CORE_LAWS/L7_AUTHORITY|L7_AUTHORITY]]
- Security layer — [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]] · [[18_SECURITY/SECURITY_CONTROL_ACCESS_BRIDGE_GOVERNOR|SECURITY_CONTROL_ACCESS_BRIDGE_GOVERNOR]]
- Control-plane gates — [[03_CONTROL_PLANE/04_AUTHORITY/04_AUTHORITY_MOC|04_AUTHORITY_MOC]] · [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ_ENGINE_VALIDATION_RECEIPT]]
- Tool boundary — [[14_TOOLS/TOOLS_TOOL_CONTRACT|TOOLS_TOOL_CONTRACT]] (Tool available ≠ authorized)
- Observed by — [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] · never treated as authority

---

```RSCF-NODE
node_id: amos_16_schemas_security_schema
node_type: schema
path: 16_SCHEMAS/SECURITY_SCHEMA.md
claim_class: AMOS_MODEL
rscf_state: derived
canonical_status: UNKNOWN/GAP
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
  - GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
  - GROUNDS: [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]]
```
