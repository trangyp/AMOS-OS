---
title: BUSINESS LOGIC VULNS
tags:
- logic
- reasoning
- formal
- canon/knowledge
type: document
source: 11_KNOWLEDGE/logic
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: logic_kernel
---


# Business Logic Vulns

## Overview
Business logic vulnerabilities are flaws in the design and implementation of application logic that allow attackers to manipulate legitimate functionality to achieve malicious goals. Unlike technical vulnerabilities (e.g., SQL injection, XSS), these exploit the intended behaviour of the application itself.

## Common Patterns

### Price Manipulation
- Bypassing price checks by manipulating client-side values
- Negative quantity or price values in order processing
- Currency confusion (submitting prices in wrong currency unit)

### Privilege Escalation via Logic
- Skipping mandatory workflow steps (e.g., checkout without payment)
- Accessing restricted features by manipulating state transitions
- Race conditions in multi-step processes (TOCTOU)

### Quantity & Inventory Abuse
- Ordering negative or fractional quantities
- Exceeding purchase limits via parallel requests
- Inventory exhaustion via cart reservation abuse

### Coupon & Discount Abuse
- Reusing single-use coupons across sessions
- Stacking incompatible discounts
- Applying expired promotions via parameter tampering

### Authentication Bypass
- Forced browsing past authentication checkpoints
- Session state manipulation to assume other user roles
- Password reset poisoning via logic flaws

## Detection
- Threat modelling against business workflows
- State machine analysis for invalid transitions
- Fuzzing business-critical parameters (quantities, prices, states)
- Race condition testing on concurrent operations

## Mitigation
- Server-side validation of all business constraints
- Enforce workflow state machine on server
- Implement idempotency for financial operations
- Rate limiting and anomaly detection on business actions
- Audit logging for all state transitions

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[LOGIC_MOC]]
