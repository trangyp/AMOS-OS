---
title: legal kernel org risk
type: reference
tags: [reference, amos-c09-org-law-policy-master]
---

# AMOS Legal Kernel v0 Org Risk Policy

> Source: `_00_Cosmo brain/kernel/A/AMOS_Legal_Kernel_v0_Org_Risk_Policy7_4.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-legal-kernel-v0, kernel]
---

[
  {
    "engine_id": "AMOS_Legal_Kernel_vInfinity",
    "engine_type": "legal_kernel",
    "created_at_utc": "2025-11-27T09:46:55.191647+00:00",
    "meta": {
      "name": "AMOS Legal Kernel vInfinity",
      "version": "vInfinity_Legal_Kernel_1.0.0",
      "description": "Canonical legal kernel for AMOS legal engines. Defines the full axis set, 24 legal dimensions, reasoning tensor, routing logic, and governance policies. This is the minimal, clean, final kernel used as the base for all higher legal SUPER engines."
    },
    "kernel": {
      "axes": [
        {
          "key": "cluster_id",
          "axis_id": "AX01",
          "name": "Legal Domain Cluster",
          "description": "High-level legal practice area (e.g., corporate, finance, disputes, regulatory, IP/data, ESG, legal ops).",
          "value_source": "external_list:clusters_legal"
        },
        {
          "key": "matter_type",
          "axis_id": "AX02",
          "name": "Matter Type",
          "description": "Nature of work: advisory, transactional, contentious, regulatory, investigations.",
          "value_source": "dimensions_24.d01_matter_type"
        },
        {
          "key": "jurisdiction_scope",
          "axis_id": "AX03",
          "name": "Jurisdiction Scope",
          "description": "Geographic spread of the matter: local, multi-province, cross-border, multi-region, global.",
          "value_source": "dimensions_24.d02_jurisdiction_scope"
        },
        {
          "key": "client_type",
          "axis_id": "AX04",
          "name": "Client Type",
          "description": "Who the client is: individual, SME, corporate, financial institution, state entity, NGO.",
          "value_source": "dimensions_24.d03_client_type"
        },
        {
          "key": "industry",
          "axis_id": "AX05",
          "name": "Industry Context",
          "description": "Economic sector most relevant to the matter (e.g., tech, finance, energy, public).",
          "value_source": "dimensions_24.d04_industry"
        },
        {
          "key": "risk_level",
          "axis_id": "AX06",
          "name": "Legal Risk Level",
          "description": "Overall legal risk severity: low, moderate, high, critical.",
          "value_source": "dimensions_24.d05_risk_level"
        },
        {
          "key": "materiality",
          "axis_id": "AX07",
          "name": "Financial Materiality",
          "description": "Financial size or impact of the matter (e.g., under 1m, 1m\u201310m, 10m\u2013100m, over 100m).",
          "value_source": "dimensions_24.d06_materiality"
        },
        {
          "key": "time_pressure",
          "axis_id": "AX08",
          "name": "Time Pressure",
          "description": "Urgency of execution: normal, expedited, urgent, emergency.",
          "value_source": "dimensions_24.d07_time_pressure"
        },
        {
          "key": "regulatory_intensity",
          "axis_id": "AX09",
          "name": "Regulatory Intensity",
          "description": "Degree of regulatory oversight or special regimes.",
          "value_source": "dimensions_24.d08_regulatory_intensity"
        },
        {
          "key": "dispute_stage",
          "axis_id": "AX10",
          "name": "Dispute / Case Stage",
          "description": "Position on the dispute lifecycle: none, pre-dispute, filed, trial, appeal, enforcement.",
          "value_source": "dimensions_24.d09_dispute_stage"
        },
        {
          "key": "contract_stage",
          "axis_id": "AX11",
          "name": "Contract Lifecycle Stage",
          "description": "Where the contract is: structuring, drafting, negotiation, signing, amendment, termination.",
          "value_source": "dimensions_24.d10_contract_stage"
        },
        {
          "key": "evidence_state",
          "axis_id": "AX12",

---
**MOC:** [[references_MOC]]
