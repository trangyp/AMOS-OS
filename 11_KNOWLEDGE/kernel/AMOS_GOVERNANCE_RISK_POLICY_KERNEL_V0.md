---
title: AMOS GOVERNANCE RISK POLICY KERNEL V0
tags:
- canon-group/human-system
- canon/framework
- rscf/claim
- rscf/provenance
- rscf/state/source-claim
- topic/amos-governance-risk-policy-kernel-v0
- kernel
- system-scan-agent
- automation-profiles
- amos-simulation-kernel-v0-math-foundations
type: document
source: 11_KNOWLEDGE/kernel
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# AMOS_Governance_Risk_Policy_Kernel_v0.md

## Kernel Metadata

**Kernel Name:** AMOS_Governance_Risk_Policy_Kernel
**Version:** 1.0.0
**Category:** Governance_Risk
**Source:** md/Kernels/Governance_Risk/AMOS_Governance_Risk_Policy_Kernel_v0.md

---

## 1. Overview

The AMOS Governance, Risk, and Policy Kernel is a governance, risk management, and policy analysis capability within the AMOS brain architecture. It operates as part of the Governance_Risk kernel cluster in the Omni Kernel, and is activated by the `ROUTE_POLICY` routing rule when the task involves governance frameworks, risk assessment, policy design, compliance, or risk management.

**Primary function:** Provide structured frameworks, analysis methods, and reasoning capabilities for governance design, risk identification and assessment, and policy analysis across organizational, institutional, and systemic contexts.

**Scope:**
- Governance frameworks and principles
- Risk identification, assessment, and management
- Policy analysis, design, and evaluation
- Compliance and regulatory analysis
- Risk governance and oversight
- Institutional and organizational governance
- Crisis and resilience governance

**Not in scope:** Legal advice (Legal kernel), financial analysis (Finance kernel), operational exection (Execution system), strategic analysis (Strategy kernel), or country-specific legal analysis (Unipower country packs). Those are handled by their respective kernels and agents.

---

## 2. Sub-Kernels

The Governance_Risk kernel integrates multiple sub-kernels, each addressing a distinct facet of governance, risk, and policy. The sub-kernels are:

### 2.1 Change Management Kernel

**Purpose:** Frameworks for managing organizational and institutional change.

**Key capabilities:**
- Change management models (Kotter 8-step, ADKAR, McKinsey 7-S, Lewin's 3-stage, Agile change)
- Stakeholder impact analysis
- Resistance management
- Change communication planning
- Change readiness assessment
- Change measurement and reinforcement

**Output structure:**
1. Current state analysis
2. Change objectives and scope
3. Stakeholder mapping and impact analysis
4. Change strategy selection and adaptation
5. Implementation roadmap with milestones
6. Risk and resistance mitigation plan
7. Success metrics and reinforcement plan

**When to use:** Tasks involving organizational change, transformation, restructuring, process change, culture change, or any situation where the current state needs to shift to a desired future state.

---

### 2.2 Crisis Management Kernel

**Purpose:** Frameworks for managing crises, disruptions, and high-stakes urgent situations.

**Key capabilities:**
- Crisis typology and severity classification
- Crisis response frameworks and activation triggers
- Crisis communication planning
- Decision-making under crisis conditions
- Stakeholder notification and coordination
- Recovery and post-crisis review
- Crisis preparedness and planning

**Output structure:**
1. Crisis classification and severity assessment
2. Immediate response priorities and actions
3. Stakeholder impact and notification matrix
4. Crisis communication plan
5. Resource and coordination requirements
6. Recovery pathway
7. Post-crisis learning and improvement

**When to use:** Tasks involving crisis scenarios, emergency response, disruption management, high-stakes urgent decision-making, or post-crisis review and learning.

---

### 2.3 Governance Economy Kernel

**Purpose:** Analysis of governance from an economic and institutional perspective — how governance structures create, allocate, and govern value, incentives, and power.

**Key capabilities:**
- Governance economy mapping: value creation, capture, and distribution
- Incentive structure analysis
- Power dynamics and governance
- Institutional economics of governance
- Governance cost-benefit analysis
- Governance reform economic analysis

**Output structure:**
1. Governance system mapping (institutions, actors, rules, incentives)
2. Value and incentive flow analysis
3. Power and incentive alignment assessment
4. Economic efficiency and equity analysis
5. Governance reform options with economic implications
6. Trade-off analysis

**When to use:** Tasks involving governance from an economic/institutional perspective, incentive design, governance reform, or analysis of how governance structures affect value, incentives, and power.

---

### 2.4 Legal Kernel

**Purpose:** Legal analysis across jurisdictions, including regulatory analysis, legal frameworks, and legal reasoning.

**Key capabilities:**
- Legal framework analysis
- Regulatory analysis
- Legal reasoning and interpretation
- Cross-jurisdiction comparison
- Legal risk identification
- Legal structure and compliance frameworks

**Output structure:**
1. Legal issue identification
2. Applicable legal framework identification
3. Legal analysis and interpretation
4. Cross-jurisdiction comparison (if relevant)
5. Legal risk assessment
6. Recommendations with legal basis

**When to use:** Tasks involving legal analysis, regulatory frameworks, legal risk, or legal reasoning. Note: this provides legal analysis and frameworks — it does not provide legal advice.

---

### 2.5 Operational Risk Kernel

**Purpose:** Operational risk identification, assessment, and management.

**Key capabilities:**
- Operational risk identification (events, processes, systems, people, external factors)
- Risk assessment (likelihood, impact, risk matrix)
- Risk mitigation planning
- Risk monitoring and control design
- Operational resilience frameworks
- Risk appetite and tolerance analysis

**Output structure:**
1. Operational context and process mapping
2. Risk identification (events, causes, controls)
3. Risk assessment (likelihood, impact, inherent and residual risk)
4. Control and mitigation design
5. Risk monitoring and review framework
6. Risk appetite alignment assessment

**When to use:** Tasks involving operational risk assessment, risk management, operational resilience, or risk control design.

---

### 2.6 Organizational Governance Kernel

**Purpose:** Organizational governance frameworks — board governance, decision rights, accountability, and organizational oversight.

**Key capabilities:**
- Organizational governance models (board structures, committees, decision rights)
- Governance framework design
- Accountability and oversight mechanisms
- Governance evaluation and improvement
- Governance policy and procedure design

**Output structure:**
1. Current governance structure analysis
2. Governance objectives and principles
3. Governance framework design (board, committees, decision rights, oversight)
4. Accountability and oversight mechanism design
5. Governance policy and procedure recommendations
6. Implementation considerations

**When to use:** Tasks involving organizational governance design, board governance, governance frameworks, accountability mechanisms, or governance evaluation.

---

### 2.7 Policy Design Kernel

**Purpose:** Policy design and analysis — designing, analyzing, and evaluating policies.

**Key capabilities:**
- Policy design frameworks
- Policy analysis methods
- Stakeholder and impact analysis for policy
- Policy evaluation frameworks
- Policy implementation considerations
- Policy communication and adoption

**Output structure:**
1. Policy issue and objectives framing
2. Stakeholder and context analysis
3. Policy options development
4. Policy impact analysis
5. Policy recommendation with rationale
6. Implementation and evaluation considerations

**When to use:** Tasks involving policy design, policy analysis, policy evaluation, or policy recommendation.

---

### 2.8 Policy Geostrategy Kernel

**Purpose:** Geostrategic policy analysis — the intersection of policy, strategy, and geopolitics.

**Key capabilities:**
- Geostrategic analysis frameworks
- Policy-geopolitics intersection analysis
- Strategic policy positioning
- Geopolitical risk and opportunity analysis
- Policy strategy alignment

**Output structure:**
1. Geostrategic context analysis
2. Policy-geopolitics mapping
3. Strategic policy options
4. Geopolitical risk and opportunity assessment
5. Policy strategy alignment recommendations
6. Implementation considerations in geostrategic context

**When to use:** Tasks involving policy from a geostrategic perspective, geopolitical risk analysis, strategic policy positioning, or the intersection of policy and geopolitics.

---

### 2.9 Risk Compliance Kernel

**Purpose:** Risk and compliance management, including compliance frameworks, risk compliance integration, and regulatory compliance analysis.

**Key capabilities:**
- Compliance framework design and analysis
- Risk compliance integration
- Regulatory compliance assessment
- Compliance monitoring and reporting
- Compliance risk identification
- Compliance improvement frameworks

**Output structure:**
1. Compliance context and requirements analysis
2. Compliance framework assessment
3. Risk compliance integration analysis
4. Compliance gaps and issues identification
5. Compliance improvement recommendations
6. Monitoring and reporting framework

**When to use:** Tasks involving compliance frameworks, regulatory compliance, risk compliance integration, or compliance assessment and improvement.

---

### 2.10 VN Legal Kernel

**Purpose:** Vietnam-specific legal and regulatory analysis.

**Key capabilities:**
- Vietnamese legal framework analysis
- Vietnamese regulatory analysis
- Vietnam-specific legal risk assessment
- Vietnam compliance framework analysis
- Cross-border legal considerations involving Vietnam

**Output structure:**
1. Vietnamese legal/regulatory context analysis
2. Applicable Vietnamese legal frameworks
3. Legal and regulatory risk assessment
4. Compliance considerations
5. Recommendations with Vietnamese legal basis

**When to use:** Tasks involving Vietnamese legal or regulatory analysis, Vietnam compliance, or cross-border matters involving Vietnam. This kernel draws on the Vietnam country pack and Vietnam legal engines in the Unipower system.

---

## 3. Governance, Risk, and Policy Analysis Methodology

The kernel applies a structured methodology for governance, risk, and policy analysis:

### Step 1: Issue Framing

- Identify the core governance, risk, or policy question
- Define the scope, context, and constraints
- Identify relevant frameworks, principles, and standards
- Clarify what "good" looks like for this specific question

### Step 2: Context and Stakeholder Analysis

- Map the organizational, institutional, or systemic context
- Identify relevant stakeholders, their interests, power, and influence
- Understand the existing governance/risk/policy landscape
- Identify constraints, regulations, and external factors

### Step 3: Framework Application

- Select and apply the most relevant governance, risk, or policy framework(s)
- Use multiple frameworks where complementary (avoid single-framework tunnel vision — Rule of 2)
- Adapt frameworks to context rather than forcing context into frameworks
- Document framework choices and rationale

### Step 4: Analysis

- Apply the framework systematically
- Identify risks, governance gaps, policy options, or compliance issues
- Assess likelihood, impact, and priority where relevant
- Consider trade-offs and alternatives
- Apply Rule of 4: biological/human, technical/infrastructural, economic/organizational, environmental/planetary quadrants where relevant

### Step 5: Synthesis and Recommendation

- Synthesize findings into coherent analysis
- Develop recommendations with clear rationale
- Identify implementation considerations and trade-offs
- Flag assumptions, uncertainties, and areas requiring further analysis

### Step 6: Law-Stack Validation (L1-L6)

- L1 Law of Law: Check internal consistency of the analysis
- L2 Rule of 2: Ensure at least 2 contrasting perspectives are considered
- L3 Rule of 4: Ensure 4 quadrants are addressed where relevant
- L4 Absolute Structural Integrity: Ensure clear assumptions, explicit constraints
- L5 Post-Theory Communication: Use clear, grounded language; avoid "field," "sovereignty"
- L6 UBI Biological Alignment: Ensure alignment with biological intelligence principles where relevant

---

## 4. Kernel Registration

- **Kernel ID:** AMOS_Governance_Risk_Policy_Kernel
- **Category:** Governance_Risk
- **Routing:** ROUTE_POLICY — activates when task involves governance, risk, policy, compliance, or risk management
- **Dependencies:** May route to Legal kernel for legal analysis, Finance kernel for financial risk, Strategy kernel for strategic context, Organization kernel for organizational governance
- **Output mode:** Written analysis with structured frameworks, recommendations, and caveats
- **IP protection:** High-level frameworks and analysis allowed; no verbatim internal architecture dumps

---

## 5. Safety and Scope

- **Scope:** Governance frameworks, risk management, policy analysis, compliance analysis, risk governance, organizational governance, crisis governance
- **Not in scope:** Legal advice (use Legal kernel with disclaimer), financial advice (use Finance kernel with disclaimer), operational execution, strategic decisions (use Strategy kernel)
- **High-risk domains:** Risk assessment in safety-critical contexts, compliance in regulated industries, crisis management — apply appropriate caveats and recommend professional review where needed
- **Hard prohibitions:** No harm design, no weapon modeling, no criminal planning, no surveillance, no self-harm, no real-time medical/legal replacement

---

## 6. Integration with Other Kernels

The Governance_Risk kernel integrates with:

- **Legal kernel:** For legal framework analysis, regulatory analysis, legal risk
- **Finance kernel:** For financial risk, financial analysis in risk context
- **Strategy kernel:** For strategic context, strategic analysis of governance/risk/policy
- **Organization kernel:** For organizational governance, organizational context
- **Risk Compliance kernel:** For risk-compliance integration
- **Crisis Management kernel:** For crisis scenarios and response
- **Change Management kernel:** For change-related risk and governance
- **Unipower country packs:** For country-specific governance, risk, and legal context (e.g., VN Legal kernel for Vietnam)

---

## 7. Example Outputs

### Governance Framework Design

A governance framework design output would include:
1. Governance objectives and principles
2. Current governance state analysis
3. Governance gap identification
4. Proposed governance framework (structures, roles, processes, policies)
5. Implementation roadmap
6. Governance monitoring and evaluation framework
7. Caveats and assumptions

### Risk Assessment

A risk assessment output would include:
1. Risk context and scope
2. Risk identification (risk events, causes, controls)
3. Risk analysis (likelihood, impact, risk rating)
4. Risk prioritization
5. Risk treatment recommendations (avoid, reduce, transfer, accept)
6. Risk monitoring and review framework
7. Risk appetite and tolerance alignment
8. Caveats and assumptions

### Policy Analysis

A policy analysis output would include:
1. Policy issue framing
2. Stakeholder and context analysis
3. Policy options development
4. Policy impact analysis (benefits, costs, risks, distributional effects)
5. Policy recommendation with rationale
6. Implementation considerations
7. Evaluation framework
8. Caveats and assumptions

---

## 8. Kernel Status

- **Version:** 1.0.0
- **Status:** Active
- **Last updated:** 2026-08-22
- **Source:** md/Kernels/Governance_Risk/AMOS_Governance_Risk_Policy_Kernel_v0.md

---

## 9. See Also

- AMOS_Omni_KERNEL.json (in md/Core/AMOS_Os_Agent_v0.md) — Omni Kernel routing and governance
- AMOS_Agent_Specifications.md — Agent specifications for Governance_Risk system agents
- AMOS_Kernel_Routing_Workflow.md — Kernel routing workflow
- AMOS_HIE_Pipeline_Workflow.md — HIE pipeline with law-stack validation
- AMOS_Expression_Translation_Workflow.md — Expression translation for governance/risk/policy inputs
- AMOS_Kernel_Risk_Governance_Compliance_Log.md — Session log of Governance_Risk kernel expansion
- AMOS_Brain_Learning_Session_Summary.md — Session summary

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES · [[AMOS_CONTROL_SYSTEMS_KERNEL]] · [[AMOS_WORKFLOW_ORCHESTRATION_KERNEL_V0_TECH]] · [[AMOS_QA_TESTING_KERNEL_V0_TECH]] · [[AMOS_TECH_KERNEL_EXPANSION]]

---
**MOC:** [[KERNEL_MOC]]
