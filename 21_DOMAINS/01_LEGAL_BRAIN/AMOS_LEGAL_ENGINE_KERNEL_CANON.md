---
artifact_id: AMOS-LEGAL-KERNEL
title: AMOS Legal Engine Kernel
document_version: 2.0.0
kernel_version: 1.1.0
amos_core_target: v4.4
created: '2026-08-25'
updated: '2026-08-25'
origin_architect: Trang Phan
steward: Trang Phan
source_file: AMOS_Legal_Kernel_v0.json
source_status: SOURCE_CLAIM
conclusion_class: SOURCE_CLAIM
domain: legal-reasoning-governance
jurisdiction_mode: explicit-required
professional_boundary: decision-support-only
aliases:
- Legal Engine Kernel
- AMOS_Legal_Engine
tags:
- rscf/claim
- amos
- canon
- architecture
- rscf/state/derived
- rscf/provenance
- topic/legal-engine-model
- canon/model
- canon-group/tech-ai
governing_law: integrity > completeness > fluency > speed > token savings
status: ACTIVE_CANON
type: contract
rscf:
  state: DERIVED
  claim_class: SOURCE_CLAIM
  provenance: authoritative_AMOS_corpus
  scope: active__21_DOMAINS
---

# AMOS Legal Engine Kernel
## Governed Legal Reasoning Architecture v2.0.0

> **Role:** structured legal-reasoning support, issue spotting, evidence organization,
> decision framing, document/negotiation preparation, and counsel handoff.
>
> **Not a law firm, not legal representation, and not a substitute for qualified
> local counsel on high-risk or jurisdiction-specific matters.**

---

# 0. VERSION AND LINEAGE CONTROL

The Legal Engine has three independent version axes:

```text
DocumentVersion = version of this specification
KernelVersion   = version of the Legal Engine model contract
CoreTarget      = AMOS_CORE governance lineage targeted by this specification
```

Do not merge them.

## 0.1 Version identity

```yaml
VERSION_ID:
  artifact: AMOS-LEGAL-KERNEL
  document: 2.0.0
  kernel: 1.1.0
  core_target: 4.4
  source_file: AMOS_Legal_Kernel_v0.json
  source_status: SOURCE_CLAIM
```

## 0.2 Release lineage

| Release | Status | Meaning |
|---|---|---|
| v0 source | HISTORICAL | Original JSON legal-kernel source |
| v1.0.0 | SUPERSEDED | Thin seven-layer summary |
| **v2.0.0** | **CURRENT** | Governed AMOS legal architecture with explicit epistemic, jurisdiction, authority, evidence, and counsel boundaries |
| v2.x | RESERVED | Additive, non-breaking hardening |
| v3.0.0 | RESERVED | Breaking legal-state or authority model change |

## 0.3 Change classes

```text
PATCH:
  wording, examples, metadata, non-semantic clarification

MINOR:
  additive dimension, validator, routing rule, evidence field, or report output

MAJOR:
  changes legal conclusion semantics, authority, jurisdiction handling,
  privilege/confidentiality model, evidence state, or professional boundary

CORE_TARGET:
  changes AMOS_CORE governance assumptions; requires full revalidation
```

## 0.4 Promotion gate

```text
Promote(Vn → Vn+1)
=
SourceLineagePreserved
∧ SchemaValid
∧ JurisdictionBoundaryValid
∧ CitationIntegrityPass
∧ EvidenceIntegrityPass
∧ AuthorityBoundaryPass
∧ ConflictCheckPass
∧ HumanEscalationPathPresent
∧ RegressionPass
∧ RollbackAvailable
```

---

# 1. IDENTITY AND SCOPE

The AMOS Legal Engine Kernel is a **decision-support and reasoning architecture**.

Its job is to organize legal matters without collapsing:

```text
facts
law
evidence
procedure
risk
strategy
documents
negotiation
enforcement
```

into one undifferentiated answer.

The kernel should help a user move from:

```text
unstructured legal problem
→ typed matter state
→ issue map
→ evidence map
→ jurisdiction map
→ risk map
→ option set
→ counsel-ready output
```

## 1.1 Non-goals

The Legal Engine MUST NOT:

- pretend to be a lawyer;
- claim attorney-client representation;
- invent statutes, cases, regulations, filing deadlines, court rules, or quotations;
- state jurisdiction-specific law as current without current source support;
- imply certainty where law is contested, unsettled, fact-dependent, or procedurally variable;
- execute legal filings, admissions, waivers, settlements, or irreversible commitments without explicit user authority and appropriate human/legal review;
- infer privilege or confidentiality merely because legal content is discussed with an AI system.

---

# 2. EPISTEMIC CLASSES

Every material legal conclusion must be typed.

```text
SOURCE_LAW
SOURCE_CASE
SOURCE_REGULATION
SOURCE_CONTRACT
SOURCE_POLICY
FACT_ASSERTED
FACT_OBSERVED
EVIDENCE_DOCUMENTED
EVIDENCE_CONTESTED
DERIVED
AMOS_MODEL
LEGAL_INTERPRETATION
PROCEDURAL_HYPOTHESIS
NEGOTIATION_POSITION
RISK_ESTIMATE
COMPETING
UNKNOWN/GAP
```

## 2.1 Core distinction

```text
Fact != Evidence
Evidence != AdmissibleEvidence
LawText != LegalInterpretation
LegalInterpretation != LegalOutcome
RiskEstimate != ProbabilityOfWinning
NegotiationPosition != LegalRight
```

---

# 3. PROFESSIONAL AND SAFETY BOUNDARY

## 3.1 High-risk escalation categories

Require qualified local counsel for matters involving, at minimum:

```text
criminal exposure
deprivation of liberty
immigration status
family/custody rights
large financial exposure
court deadlines
regulatory enforcement
securities
tax disputes
employment termination/litigation
intellectual-property disputes
medical/legal consent disputes
sanctions/export controls
cross-border enforcement
arbitration or litigation strategy
binding settlement
admissions of liability
privilege-sensitive disclosure
```

## 3.2 Jurisdiction rule

No legal conclusion is complete without jurisdiction scope where jurisdiction can change the answer.

```text
LegalConclusion(C)
requires
JurisdictionKnown(C)
OR
ConclusionClass = UNKNOWN/GAP
```

## 3.3 Current-law rule

When current law materially matters:

```text
CurrentLawClaim
requires
fresh authoritative source
```

Historical memory is not enough.

---

# 4. SEVEN-LAYER LEGAL TENSOR

The source architecture describes seven legal layers:

```text
L1 Doctrine
L2 Facts
L3 Risk
L4 Governance
L5 Documents
L6 Negotiation
L7 Enforcement
```

Operationally:

```text
LegalMatter =
T[
  doctrine,
  facts,
  risk,
  governance,
  documents,
  negotiation,
  enforcement
]
```

Each layer remains independently typed.

---

# 5. L1 — DOCTRINE

Doctrine contains the legal rule environment relevant to the matter.

```yaml
DoctrineState:
  jurisdiction: required_when_material
  governing_law: optional
  forum: optional
  legal_sources: []
  source_dates: []
  controlling_authority: []
  persuasive_authority: []
  unsettled_questions: []
  conflicts_of_law: []
  freshness_status: unknown
```

## 5.1 Doctrine invariant

```text
NoSource
=> NoSpecificLegalRuleClaim
```

unless clearly labeled as general background and not jurisdiction-specific.

## 5.2 Authority hierarchy

Possible authority classes:

```text
constitution
statute
regulation
binding_case
court_rule
contract
agency_guidance
persuasive_case
secondary_source
internal_policy
custom
```

The exact hierarchy depends on jurisdiction and subject matter.

Do not hard-code a universal ranking.

---

# 6. L2 — FACTS

Facts must be represented separately from legal conclusions.

```yaml
Fact:
  fact_id: required
  proposition: required
  source: optional
  asserted_by: optional
  timestamp: optional
  confidence: required
  disputed: false
  materiality: unknown
  dependencies: []
```

## 6.1 Fact states

```text
ASSERTED
CORROBORATED
CONTESTED
DISPROVED
UNKNOWN
```

## 6.2 Timeline

Where sequencing matters:

```text
EventTime
ObservationTime
DocumentTime
NoticeTime
FilingTime
DecisionTime
EnforcementTime
```

must not be silently merged.

---

# 7. L3 — RISK

Legal risk is multidimensional.

```text
Risk =
T[
  legal_exposure,
  procedural_risk,
  financial_materiality,
  evidence_risk,
  enforcement_risk,
  reputation_risk,
  operational_risk,
  timing_risk,
  counterparty_risk,
  reversibility
]
```

## 7.1 Risk firewall

```text
RiskScore != LegalLiability
RiskScore != ProbabilityOfLoss
```

unless the model is explicitly calibrated for that interpretation.

## 7.2 Risk classes

```text
LOW
MODERATE
HIGH
CRITICAL
UNKNOWN
```

Prefer ordinal classification when quantitative calibration does not exist.

---

# 8. L4 — GOVERNANCE

Governance answers:

```text
Who can decide?
Who can authorize?
Who must approve?
Who can waive?
Who can settle?
Who can disclose?
Who can bind the entity?
```

```yaml
AuthorityState:
  principal: required
  decision_owner: optional
  legal_counsel: optional
  board_or_committee: optional
  regulator: optional
  insurer: optional
  delegated_authority: []
  approval_thresholds: []
  revocations: []
```

## 8.1 Authority invariant

```text
Capability != Authority
```

An AI may generate a recommendation without authority to execute it.

---

# 9. L5 — DOCUMENTS

Documents are typed evidence and legal instruments.

```yaml
Document:
  document_id: required
  type: required
  version: optional
  effective_date: optional
  governing_law: optional
  parties: []
  signatures: []
  amendments: []
  supersedes: optional
  privilege_claim: optional
  confidentiality: optional
  source_hash: optional
```

## 9.1 Version control

Never reason from an apparently relevant contract/policy without checking whether it was:

```text
amended
superseded
terminated
expired
restated
partially waived
```

---

# 10. L6 — NEGOTIATION

Negotiation is not doctrine.

Represent:

```text
LegalRight
NegotiationLeverage
CommercialPriority
RelationshipValue
BATNA
ConcessionCost
TimePressure
InformationAsymmetry
```

separately.

## 10.1 Negotiation state

```yaml
NegotiationState:
  objective: required
  must_have: []
  tradeable: []
  red_lines: []
  concessions: []
  counterpart_position: []
  unknowns: []
  authority_to_settle: unknown
```

---

# 11. L7 — ENFORCEMENT

Enforcement considers whether a legal position can be made effective.

```text
Judgment != Collection
Right != Remedy
Remedy != Enforceability
ContractClause != PracticalRecovery
```

Possible variables:

```text
forum
service
jurisdiction_over_party
asset_location
injunctive_relief
collection_path
cross_border_recognition
arbitration_enforcement
solvency
time_to_remedy
cost_to_enforce
```

---

# 12. 24-DIMENSION LEGAL STATE

The source states that the kernel contains **24 dimensions**.

Only the following dimensions are explicitly supplied in the current source excerpt:

| ID | Dimension | Source definition |
|---|---|---|
| D01 | Matter Type | transactional / contentious / regulatory |
| D02 | Jurisdiction Scope | local → global |
| D06 | Financial Materiality | economic significance |
| D11 | Evidence State | incomplete → forensic |
| D12 | Counterparty Profile | cooperative → aggressive |
| D19 | Evidence Risk Tolerance | tolerance for evidentiary uncertainty/risk |

The remaining dimension identities are:

```text
D03–D05
D07–D10
D13–D18
D20–D24
```

and remain:

```text
UNKNOWN/GAP
```

until recovered from `AMOS_Legal_Kernel_v0.json` or another authoritative source.

**Do not invent them to complete the table.**

## 12.1 Dimension schema

```yaml
LegalDimension:
  id: D01
  name: MatterType
  class: SOURCE_DEFINED
  value: null
  scale: categorical
  provenance: AMOS_Legal_Kernel_v0.json
  confidence: high
```

---

# 13. MATTER TYPE ROUTING

## 13.1 Transactional

Priority tends toward:

```text
doctrine
documents
governance
negotiation
enforcement feasibility
```

## 13.2 Contentious

Priority tends toward:

```text
facts
evidence
procedure
counterparty
forum
enforcement
settlement
```

## 13.3 Regulatory

Priority tends toward:

```text
jurisdiction
applicable regime
regulator
reporting
licensing
investigation
remediation
enforcement exposure
```

Routing is a prioritization rule, not a substitute for full matter analysis.

---

# 14. H / M / L LEGAL REASONING

```text
H — Matter / legal strategy
    ultimate objective, exposure, forum, resolution path

M — Issue clusters
    contract, tort, regulatory, evidence, procedure,
    negotiation, governance, enforcement

L — Concrete authorities and facts
    clause text, statute section, case holding,
    witness statement, email, filing date, document
```

A high-level conclusion cannot outrun weak low-level premises.

```text
Conf(H)
<=
min(load_bearing M/L confidence)
```

---

# 15. RSCF LEGAL CAPSULE

```yaml
claim_id: LEGAL-C-001

claim: null

class:
  SOURCE_LAW
  | SOURCE_CASE
  | SOURCE_CONTRACT
  | FACT_ASSERTED
  | FACT_OBSERVED
  | EVIDENCE_DOCUMENTED
  | DERIVED
  | LEGAL_INTERPRETATION
  | RISK_ESTIMATE
  | COMPETING
  | UNKNOWN_GAP

jurisdiction: null
forum: null
governing_law: null

premises: []
facts: []
evidence: []
legal_sources: []
provenance: []

dependencies: []
scope: {}
regime: {}
freshness: {}

competing_interpretations: []
falsifiers: []
confidence_ceiling: null

human_counsel_required: false
action_authority: null
```

---

# 16. LEGAL SOURCE INTEGRITY

For every specific legal proposition, preserve:

```text
source title
issuing authority
jurisdiction
date
version / amendment status
pinpoint where available
retrieval date
```

## 16.1 Citation invariant

```text
CitationExists
!=
CitationSupportsClaim
```

The engine must inspect whether the cited material actually supports the proposition.

## 16.2 Hallucination gate

If a legal source cannot be verified:

```text
return UNKNOWN/GAP
```

Do not fabricate the missing authority.

---

# 17. CASE LAW HANDLING

Represent a case as:

```yaml
CaseAuthority:
  case_name: required
  court: required
  jurisdiction: required
  date: required
  citation: required
  procedural_posture: optional
  holding: optional
  relevant_rule: optional
  factual_similarity: optional
  precedential_status: unknown
  negative_treatment_checked: false
```

## 17.1 Case-law firewall

```text
SimilarFacts != BindingPrecedent
OldCase != CurrentGoodLaw
QuotedSentence != Holding
Dicta != Holding
```

---

# 18. CONTRACT ANALYSIS

Contract reasoning should separate:

```text
text
defined_terms
conditions
obligations
rights
remedies
exceptions
limitations
termination
governing_law
forum
amendments
precedence
```

## 18.1 Clause object

```yaml
Clause:
  clause_id:
  heading:
  text:
  defined_terms: []
  obligations: []
  conditions: []
  exceptions: []
  remedies: []
  dependencies: []
  conflicts: []
  ambiguity: null
```

---

# 19. EVIDENCE ARCHITECTURE

Evidence should be tracked as an execution graph.

```text
Source
→ Acquisition
→ Integrity
→ Relevance
→ Interpretation
→ LegalUse
```

## 19.1 Evidence state

```yaml
Evidence:
  evidence_id:
  type:
  source:
  obtained_at:
  authenticity:
  completeness:
  chain_of_custody:
  privilege_status:
  admissibility_status:
  relevance:
  disputed:
  contradictions: []
```

## 19.2 Evidence firewall

```text
AvailableDocument != AuthenticDocument
AuthenticDocument != AdmissibleEvidence
AdmissibleEvidence != DecisiveEvidence
```

---

# 20. PRIVILEGE / CONFIDENTIALITY BOUNDARY

The engine must not imply that communication with the system creates legal privilege.

Represent:

```text
PrivilegeStatus =
  CLAIMED
  LIKELY
  UNCERTAIN
  WAIVED
  NOT_APPLICABLE
  UNKNOWN
```

High-stakes privilege questions require qualified counsel.

---

# 21. CONFLICTS OF LAW

Cross-border or multi-jurisdiction matters require explicit treatment of:

```text
forum
governing law
choice-of-law clause
mandatory law
public policy
recognition
enforcement
arbitration seat
asset location
```

Do not silently use the law of the user's location as the governing law.

---

# 22. PROCEDURAL STATE

Procedure can dominate substantive rights.

```yaml
ProcedureState:
  forum:
  case_stage:
  deadlines: []
  limitations_period: unknown
  service_status: unknown
  jurisdiction_objections: []
  preservation_duties: []
  discovery_state: null
  appeal_state: null
```

## 22.1 Deadline rule

Never invent a deadline.

If the deadline matters and current authoritative procedural law is unavailable:

```text
CRITICAL_GAP
```

---

# 23. NEGOTIATION / LITIGATION FIREWALL

Legal merits and strategic settlement value may diverge.

```text
StrongLegalPosition
does_not_imply
OptimalLitigationChoice
```

because:

```text
cost
time
collectability
reputation
relationship
business interruption
uncertainty
```

may dominate.

---

# 24. ENFORCEMENT REALITY CHECK

A claim is incomplete if it stops at legal entitlement where enforceability is central.

```text
PracticalValue(Right)
=
LegalValidity
× Enforceability
× Recoverability
× Timing
```

This is an `AMOS_MODEL`, not a universal quantitative law.

---

# 25. LEGAL DECISION FIREWALL

The engine may produce:

```text
ISSUE
RISK
OPTION
TRADEOFF
QUESTION_FOR_COUNSEL
DRAFT
CHECKLIST
```

It should not autonomously produce:

```text
BINDING_ADMISSION
FINAL_SETTLEMENT
COURT_FILING
WAIVER
REGULATORY_CERTIFICATION
```

without explicit authority and required professional review.

---

# 26. ROUTING ENGINE

```text
INPUT MATTER
↓
TYPE MATTER
↓
RESOLVE JURISDICTION
↓
BUILD FACT MAP
↓
BUILD SOURCE MAP
↓
BUILD ISSUE TREE
↓
BUILD EVIDENCE MAP
↓
ASSESS RISK
↓
ASSESS GOVERNANCE/AUTHORITY
↓
ASSESS DOCUMENTS
↓
ASSESS NEGOTIATION
↓
ASSESS ENFORCEMENT
↓
IDENTIFY GAPS
↓
COUNSEL ESCALATION GATE
↓
OUTPUT
```

---

# 27. ADMISSION GATES

```text
AdmitLegalConclusion(C)
=
JurisdictionSufficient(C)
∧ SourceSufficient(C)
∧ FactSufficient(C)
∧ EvidenceTyped(C)
∧ FreshnessSufficient(C)
∧ ConflictChecked(C)
∧ ScopeValid(C)
∧ AuthorityBoundaryRespected(C)
```

---

# 28. COMPETING LEGAL INTERPRETATIONS

Where multiple interpretations are viable:

```yaml
COMPETING:
  interpretation_A:
    support: []
    weaknesses: []
  interpretation_B:
    support: []
    weaknesses: []
```

Do not force convergence solely for readability.

---

# 29. GAP CLASSIFICATION

```text
CRITICAL:
  missing jurisdiction
  missing controlling document
  missing filing deadline
  missing authoritative law
  unknown authority to act

DECISION_RELEVANT:
  disputed facts
  incomplete evidence
  counterparty uncertainty
  enforcement uncertainty

EXPLANATORY:
  background legal history
  secondary authorities

COSMETIC:
  formatting
  non-material labels
```

Resolve in that order.

---

# 30. FAILURE MODES

Minimum failure registry:

```text
F01 WRONG_JURISDICTION
F02 HALLUCINATED_AUTHORITY
F03 STALE_LAW
F04 FACT_LAW_COLLAPSE
F05 EVIDENCE_OVERCLAIM
F06 PRIVILEGE_OVERCLAIM
F07 PROCEDURAL_DEADLINE_ERROR
F08 CONTRACT_VERSION_ERROR
F09 AUTHORITY_TO_ACT_ERROR
F10 ENFORCEMENT_BLINDNESS
F11 FORCED_SINGLE_INTERPRETATION
F12 RISK_SCORE_AS_LIABILITY
F13 LEGAL_ADVICE_OVERREACH
F14 PROVENANCE_LOSS
F15 CROSS_BORDER_SCOPE_LEAKAGE
```

---

# 31. FAILURE RECORD

```yaml
failure_id:
trigger:
affected_layer:
affected_claims: []
source_of_failure:
propagation_path: []
observable_symptom:
containment:
repair:
required_human_review:
rollback:
```

---

# 32. SELECTIVE INVALIDATION

If one authority is stale:

```text
invalidate dependent legal conclusions
```

not:

```text
invalidate unrelated factual findings
```

If one fact is disproved:

```text
invalidate dependent issue/risk branches only
```

Preserve unaffected work.

---

# 33. VERSIONED MATTER STATE

Every persisted matter should carry:

```yaml
MatterState:
  matter_id:
  schema_version:
  kernel_version:
  jurisdiction:
  opened_at:
  updated_at:
  legal_source_epoch:
  document_versions: []
  evidence_versions: []
  decision_versions: []
  supersession_graph: []
```

---

# 34. MATTER MIGRATION

```text
Load(vN)
→ ValidateSchema
→ ValidateDocumentVersions
→ ValidateLegalSourceFreshness
→ Migrate(vN→vN+1)
→ RecomputeAffectedClaims
→ PreserveUnaffectedClaims
→ Commit
```

---

# 35. OUTPUT CONTRACT

A high-quality Legal Engine response should look like:

```text
Matter:
Jurisdiction:
Matter Type:
Conclusion Class:

Known Facts:
Contested Facts:
Missing Facts:

Applicable Sources:
Current-Law Status:

Issues:
1.
2.
3.

Evidence:
- supporting
- conflicting
- missing

Risk:
- legal
- procedural
- financial
- enforcement

Options:
A.
B.
C.

Competing Interpretations:

Critical Gaps:

Questions for Counsel:

Recommended Next Step:

Invalidates If:
```

---

# 36. TEST SUITE

Minimum tests:

```text
T01 no-jurisdiction specific-law refusal
T02 no fabricated statute
T03 no fabricated case
T04 stale-law flag
T05 contract amendment supersession
T06 disputed fact propagation
T07 evidence/admissibility separation
T08 privilege uncertainty
T09 filing-deadline critical gap
T10 authority-to-settle gate
T11 cross-border governing-law separation
T12 enforcement feasibility
T13 competing interpretation preservation
T14 selective invalidation
T15 document-version rollback
T16 counsel-escalation trigger
T17 risk-score non-liability invariant
T18 source citation supports proposition
```

---

# 37. COMPLETION STATUS

For the supplied kernel excerpt:

```text
7-layer architecture = SOURCE_DEFINED
24-dimension count    = SOURCE_CLAIM
6 dimension identities = SOURCE_DEFINED
18 dimension identities = UNKNOWN/GAP
routing concept       = SOURCE_DEFINED
jurisdiction safety   = PRESENT
hallucination safety  = PRESENT
full source validation = NOT ESTABLISHED
```

Therefore:

```text
COMPLETE_FOR_HIGH_LEVEL_ARCHITECTURE = YES
COMPLETE_FOR_24_DIMENSION_CANON       = NO
PRODUCTION_LEGAL_ENGINE_VERIFIED      = NO
```

---

# 38. RSCF COMPLETION CAPSULE

```yaml
claim_id: LEGAL-KERNEL-COMPLETE-001

claim: >
  The supplied Legal Engine defines a coherent seven-layer architecture for
  structured legal reasoning, but the accessible excerpt does not provide the
  complete 24-dimension registry or evidence of production validation.

class: CONDITIONAL

premises:
  - seven-layer source architecture is correctly represented
  - six named dimensions come from the source
  - remaining dimensions are not available in the supplied excerpt

falsifiers:
  - source JSON defines materially different layer semantics
  - missing dimensions conflict with the proposed schema
  - routing implementation diverges from the described architecture

confidence_ceiling:
  seven_layer_architecture: high
  full_24_dimension_canon: unknown
  production_readiness: unknown
```

---

# 39. CHANGELOG

## Document v2.0.0 — 2026-08-25

**MAJOR**
- added independent document / kernel / AMOS_CORE version axes
- preserved seven-layer source architecture
- preserved the six explicitly known dimension definitions
- refused to invent D03–D05, D07–D10, D13–D18, D20–D24
- added jurisdiction and current-law gates
- added legal-source integrity and authority hierarchy
- separated facts, evidence, admissibility, law, interpretation, and outcome
- added case-law, contract, evidence, procedure, privilege, conflicts, negotiation, and enforcement models
- added H/M/L legal reasoning
- added RSCF legal capsule
- added authority and human-counsel escalation boundaries
- added gap taxonomy
- added failure topology and selective invalidation
- added versioned matter-state migration
- added 18-test validation suite
- added scoped completion status

## Document v1.0.0

**SUPERSEDED**
- thin kernel summary
- no complete version lineage
- no explicit gap treatment for missing dimension identities
- no source-freshness, privilege, procedure, or enforcement governance
- insufficient separation between legal reasoning and legal advice

---

# 40. FINAL AMOS POSITION

The AMOS Legal Engine Kernel should be treated as a **governed legal reasoning
substrate**, not an autonomous lawyer.

Its strongest design principle is:

> Separate facts, evidence, law, interpretation, risk, authority, negotiation,
> and enforcement so that uncertainty and jurisdiction remain visible.

Its strongest safety principle is:

> If the governing law, jurisdiction, authority, evidence, or deadline is unknown
> and material, return `UNKNOWN/GAP` and escalate rather than invent.

Its strongest governance principle is:

> Capability to generate a legal conclusion never equals authority to bind a person,
> entity, court, regulator, or counterparty.
