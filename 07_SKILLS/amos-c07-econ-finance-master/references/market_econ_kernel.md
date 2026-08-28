---
title: market econ kernel
type: reference
source: 07_SKILLS/amos-c07-econ-finance-master/references
tags: [reference, amos-c07-econ-finance-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# AMOS Market Econ Kernel v0

> Source: `_00_Cosmo brain/kernel/A/AMOS_Market_Econ_Kernel_v0.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-market-econ-kernel-v0, kernel]
---

{
  "engine_id": "AMOS_Market_Econ_Kernel_vInfinity",
  "engine_type": "market_econ_kernel",
  "created_at_utc": "2025-11-27T10:13:26.992816+00:00",
  "meta": {
    "name": "AMOS Global Market & Economic Kernel vInfinity",
    "version": "vInfinity_1.0.0",
    "description": "Global market sizing, market scan, and economic forecasting kernel for all sectors and regions, micro and macro integrated. Designed as a deterministic, MECE, multi-layer reasoning core."
  },
  "kernel": {
    "axes": [
      {
        "key": "task_type",
        "axis_id": "AX01",
        "name": "Analysis Task Type",
        "description": "Primary purpose of the analysis: market sizing, market scan, economic forecast, scenario analysis, benchmarking, or mixed.",
        "values": [
          "market_sizing",
          "market_scan",
          "economic_forecast",
          "scenario_analysis",
          "benchmarking",
          "mixed"
        ]
      },
      {
        "key": "geo_level",
        "axis_id": "AX02",
        "name": "Geographic Level",
        "description": "Granularity of geography: global, region, country, sub-national, city/cluster.",
        "values": [
          "global",
          "region",
          "multi_country",
          "country",
          "subnational",
          "city_cluster"
        ]
      },
      {
        "key": "geo_region",
        "axis_id": "AX03",
        "name": "Geographic Region",
        "description": "High-level region for context: e.g., North America, EU, ASEAN, MENA, LATAM, Sub-Saharan Africa, Global.",
        "values": [
          "global",
          "north_america",
          "europe",
          "asia_pacific",
          "asean",
          "mena",
          "latam",
          "sub_saharan_africa",
          "other"
        ]
      },
      {
        "key": "sector",
        "axis_id": "AX04",
        "name": "Sector Classification",
        "description": "Macro-sector using a converged taxonomy (e.g., agriculture, manufacturing, services, technology, health, energy, finance, public sector).",
        "values": [
          "agriculture",
          "mining",
          "manufacturing",
          "construction",
          "transport_logistics",
          "energy",
          "finance",
          "ict_telecom",
          "healthcare",
          "consumer_retail",
          "hospitality_tourism",
          "public_sector",
          "education",
          "creative_media",
          "other"
        ]
      },
      {
        "key": "subsector",
        "axis_id": "AX05",
        "name": "Sub-Sector / Industry",
        "description": "Narrower industry segment (e.g., EVs, batteries, SaaS, fintech, FMCG beverages, semiconductors, renewable energy).",
        "values": [
          "unspecified_subsector"
        ]
      },
      {
        "key": "value_chain_stage",
        "axis_id": "AX06",
        "name": "Value Chain Stage",
        "description": "Where in the value chain the analysis is focused: upstream, midstream, downstream, end-customer, full-stack.",
        "values": [
          "upstream",
          "midstream",
          "downstream",
          "end_customer",
          "full_stack"
        ]
      },
      {
        "key": "market_side",
        "axis_id": "AX07",
        "name": "Market Side",
        "description": "Demand-side, supply-side, or integrated market view.",
        "values": [
          "demand",
          "supply",
          "integrated"
        ]
      },
      {
        "key": "customer_type",
        "axis_id": "AX08",
        "name": "Customer Type",
        "description": "Dominant buyer type: B2C, B2B, B2G, mixed.",
        "values": [
          "b2c",
          "b2b",
          "b2g",
          "mixed"
        ]
      },
      {
        "key": "market_maturity",
        "axis_id": "AX09",
        "name": "Market Maturity

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c07-econ-finance-master-market-econ-kernel
node_type: reference
path: 07_SKILLS/amos-c07-econ-finance-master/references/market_econ_kernel.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
