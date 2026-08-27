---
title: 11k known gaps
type: reference
tags: [reference, amos-audit-repair-master]
---

# 11K Known Gaps

> Source: `/Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/Cosmo_Brain/KNOWN_GAPS.md`
> Epistemic class: SOURCE_DERIVED

# COSMO Known Gaps and Deferred Decisions

This document records all known gaps, unresolved decisions, and deferred features. Nothing is silently invented — every gap is recorded with a label and a safe reversible default where possible.

## Gap Classification Labels
- **Confirmed**: Decision made, documented, implemented
- **Inferred from design**: Derived from supplied Stitch screens/flows
- **Product assumption**: Assumed for MVP, can be refined later
- **Technical assumption**: Technical choice with reversible default
- **Needs founder decision**: Requires product founder input
- **Needs legal review**: Requires legal/compliance sign-off
- **Needs research review**: Requires scientific/ research validation
- **Blocked**: External dependency preventing completion

---

## GLOBAL GAPS

### GG-001: Founder Vision Alignment
- **Label**: Needs founder decision
- **Description**: Product positioning, core promises, and trade-off decisions need final founder validation
- **Impact**: All downstream decisions depend on this alignment
- **Default**: Continue with current architecture; record deviations

### GG-002: Brand Voice and Copy Tone
- **Label**: Inferred from design
- **Description**: Copy tone derived from Stitch design language: neutral, empathetic, non-diagnostic
- **Impact**: Affects all user-facing text, explanations, error messages
- **Default**: Neutral, empathetic, non-diagnostic (aligned with "Cosmo provides reflection, not diagnosis"); all copy goes through content-review layer

### GG-003: Artistic Style Direction
- **Label**: Needs founder decision
- **Description**: Final aesthetic for resonance artwork (abstract vs representational, color palette nuances)
- **Impact**: Artwork generation parameters and visual output
- **Default**: Use supplied design tokens and existing art-engine mapping; document deviations

### GG-004: Subscription Pricing
- **Label**: Needs founder decision
- **Description**: Final pricing tiers, trial periods, annual vs monthly emphasis
- **Impact**: Revenue, entitlement features, paywall copy
- **Default**: $9.99/mo / $79.99yr Premium, $19.99/mo / $159.99yr VIP (based on existing config)

### GG-005: Legal and Compliance Review
- **Label**: Needs legal review
- **Description**: Full privacy policy, terms of service, age restrictions, GDPR/CCPA compliance
- **Impact**: All user-facing legal text, data handling, consent architecture
- **Default**: Implement privacy-by-design; flag sensitive copy for review; do not delay core MVP

### GG-006: Research Validation
- **Label**: Needs research review
- **Description**: Acoustic feature mapping validated against research-grade audio analysis
- **Impact**: Feature extraction accuracy, artwork credibility
- **Default**: Use established libraries (librosa/essentia patterns); mark as inference; log uncertainty

### GG-007: Age Restrictions
- **Label**: Needs founder decision
- **Description**: Minimum age for app usage, parental consent requirements
- **Impact**: Onboarding flow, consent collection, subscription eligibility
- **Default**: Assume 18+ for MVP; add age gate if required by app store

---

## AUTHENTICATION GAPS

### AG-001: Apple Sign-in Full Implementation
- **Label**: Needs founder decision / Technical assumption
- **Description**: Full Apple OAuth flow with fallback if user declines share info
- **Impact**: Auth options for iOS users
- **Default**: Implement basic Apple OAuth; if user declines name/email, use "Guest" flow

### AG-002: Google Sign-in Scopes
- **Label**: Technical assumption
- **Description**: Profile email scope vs. full profile scope trade-off
- **Impact**: User data available on creation
- **Default**: Request email + profile name; if declined, prompt for display name on next screen

### AG-003: Guest-to-Account Upgrade
- **Label**: Technical assumption
- **Description**: Local guest scan data can be migrated into a new account; migration preserves the resonance session, artwork, and reflection; guest audio is not up

---
**MOC:** [[references_MOC]]
