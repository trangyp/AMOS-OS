---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Business Logic Vulns
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

# Business Logic Vulnerabilities

> Source: `_00_Cosmo brain/logic/Business_Logic_Vulns.md`
> Epistemic class: SOURCE_DERIVED

______________________________________________________________________

## tags: [logic]

## Business Logic Vulns

## Overview

Business logic vulnerabilities are flaws in the design and implementation of application logic that allow attackers to manipulate legitimate functionality to achieve malicious goals. Unlike technical vulnerabilities (e.g., SQL injection, XSS), these exploit the intended behaviour of the application itself. They are particularly dangerous because they often bypass traditional security controls — the attacker is using the application exactly as designed, but in ways the designers never anticipated.

## Common Patterns

### Price Manipulation

- Bypassing price checks by manipulating client-side values (tampering with hidden form fields, API request payloads, or JavaScript variables)
- Negative quantity or price values in order processing (submitting `-1` items to trigger refund logic)
- Currency confusion (submitting prices in wrong currency unit, exploiting floating-point precision in multi-currency systems)
- Price anchoring attacks where a legitimate initial price is submitted then modified mid-transaction

### Privilege Escalation via Logic

- Skipping mandatory workflow steps (e.g., checkout without payment, publishing without review)
- Accessing restricted features by manipulating state transitions (direct URL access to later pipeline stages)
- Race conditions in multi-step processes (TOCTOU — time-of-check to time-of-use)
- Exploiting assumption that workflow steps are always sequential and user-initiated

### Quantity & Inventory Abuse

- Ordering negative or fractional quantities (triggers edge cases in inventory deduction)
- Exceeding purchase limits via parallel requests (race condition on limit counter)
- Inventory exhaustion via cart reservation abuse (holding all stock in carts without completing purchase)
- Bulk order manipulation to trigger volume discounts then splitting orders post-discount

### Coupon & Discount Abuse

- Reusing single-use coupons across sessions (exploiting lack of server-side coupon state tracking)
- Stacking incompatible discounts (combining promotions that were designed to be mutually exclusive)
- Applying expired promotions via parameter tampering (sending expired coupon codes that the backend fails to validate)
- Referral abuse (creating self-referral loops to stack referral bonuses)

### Authentication Bypass

- Forced browsing past authentication checkpoints (accessing authenticated endpoints directly)
- Session state manipulation to assume other user roles (modifying session tokens or JWT claims)
- Password reset poisoning via logic flaws (exploiting race conditions in reset token generation)
- Account takeover via business logic in account recovery flows (manipulating recovery question validation)

### Trust Boundary Violations

- Exploiting assumptions about trusted internal APIs (calling internal endpoints from external context)
- B2B integration logic flaws (manipulating partner API assumptions about data format or origin)
- Webhook signature bypass (exploiting logic in verification rather than cryptography)
- Multi-tenant isolation failures via business logic (accessing other tenants' data through legitimate query parameters)

## Detection

- **Threat modelling against business workflows**: Map every legitimate workflow path, then systematically explore deviations, shortcuts, and reverse traversals
- **State machine analysis for invalid transitions**: Model the application as a finite state machine and test all transitions not explicitly allowed
- **Fuzzing business-critical parameters**: Systematically vary quantities, prices, states, currencies, and identifiers
- **Race condition testing on concurrent operations**: Send parallel requests to exploit TOCTOU windows in multi-step processes
- **Business rule inversion**: For every business rule, ask "what happens if this rule is violated?" and test the violation path
- **Data flow tracing**: Track how business-critical values (price, quantity, discount, user_id) flow through the system and identify points where they could be altered

## Mitigation

- **Server-side validation of all business constraints**: Never trust client-side validation. Every business rule (price > 0, quantity is integer, coupon is valid and not expired) must be enforced on the server
- **Enforce workflow state machine on server**: Track workflow state server-side. Reject any transition not explicitly in the allowed transition table. Log all attempted invalid transitions
- **Implement idempotency for financial operations**: Use idempotency keys for all payment, refund, and transfer operations to prevent double-execution from retries or replays
- **Rate limiting and anomaly detection on business actions**: Monitor for patterns that violate business norms (too many carts, too many coupon attempts, unusual purchase patterns)
- **Audit logging for all state transitions**: Every state change in a business workflow must be logged with timestamp, user, previous state, new state, and justification
- **Defense in depth for trust boundaries**: Validate data at every trust boundary crossing, even for internal APIs. Do not assume internal callers are trusted
- **Business logic review in CI/CD**: Include business logic review as a mandatory step in code review, separate from security review

## Relationship to AMOS Meta-Logic

Business logic vulnerabilities are a direct manifestation of what the AMOS Meta-Logic Kernel (C01) is designed to detect: hidden assumptions, incomplete state machine coverage, and framework boundary violations. The Meta-Logic Kernel's F06 family (Conflict & Contradiction Detection) and F03 family (Assumption Graphs & Epistemic Status) provide the reasoning primitives for systematic business logic vulnerability analysis.

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

______________________________________________________________________

## **MOC:** references_MOC

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-c01-meta-logic-master-business-logic-vulns
node_type: reference
path: 07_SKILLS/amos-c01-meta-logic-master/references/business_logic_vulns.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
