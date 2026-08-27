---
title: bizfin kernel
type: reference
source: 07_SKILLS/amos-c07-econ-finance-master/references
tags: [reference, amos-c07-econ-finance-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# AMOS BizFin Kernel v0

> Source: `_00_Cosmo brain/kernel/A/AMOS_Bizfin_Kernel_v0.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-bizfin-kernel-v0, kernel]
---

{
  "engine_id": "AMOS_BizFin_Kernel_vInfinity",
  "engine_type": "kernel",
  "created_at_utc": "2025-11-27T22:46:06.533822Z",
  "meta": {
    "name": "AMOS BizFin Market Intelligence & Forecasting Kernel vInfinity",
    "version": "vInfinity_1.0.0",
    "description": "Canonical business & finance kernel for global market sizing, market scan and economic forecasting across all sectors (micro + macro). Used as the base reasoning layer for BizFin SUPER engines.",
    "primary_domains": [
      "market_sizing",
      "market_scan",
      "economic_forecasting",
      "scenario_planning",
      "microeconomics",
      "macroeconomics"
    ],
    "language_default": "en",
    "supports_languages": [
      "en",
      "vi"
    ],
    "author": "Trang Phan (concept), AMOS Engine (formalization)"
  },
  "kernel": {
    "description": "BizFin kernel defining axes, dimensions, routing and policies for deterministic, structurally grounded market sizing, market scan and economic forecasting across sectors and geographies.",
    "axes": [
      {
        "key": "analysis_scope",
        "axis_id": "AX01",
        "name": "Scope of Analysis",
        "description": "Defines whether the engine is operating at macro, sector, industry, firm, or project level.",
        "value_source": "enum:[macro,sector,industry,company,project]"
      },
      {
        "key": "geo_level",
        "axis_id": "AX02",
        "name": "Geographic Level",
        "description": "Hierarchy of geography for the analysis: global, region, country, sub-national, city/cluster.",
        "value_source": "enum:[global,region,country,subnational,city_cluster]"
      },
      {
        "key": "time_horizon",
        "axis_id": "AX03",
        "name": "Time Horizon",
        "description": "Forecast window used for sizing and projections.",
        "value_source": "enum:[nowcast,short_term,medium_term,long_term,structural]"
      },
      {
        "key": "sector_classification",
        "axis_id": "AX04",
        "name": "Sector Classification System",
        "description": "Standard used to classify industries and sub-sectors.",
        "value_source": "enum:[GICS,NAICS,ISIC,custom]"
      },
      {
        "key": "market_boundary",
        "axis_id": "AX05",
        "name": "Market Boundary Type",
        "description": "Logical boundary definition of the market: product, use-case, customer segment, geography, channel.",
        "value_source": "enum:[product,solution,use_case,customer_segment,geography,channel,mixed]"
      },
      {
        "key": "sizing_methodology",
        "axis_id": "AX06",
        "name": "Sizing Methodology",
        "description": "Method used to compute market size and forecasts.",
        "value_source": "enum:[top_down,bottom_up,triangulated,proxy_based]"
      },
      {
        "key": "value_metric",
        "axis_id": "AX07",
        "name": "Value Metric",
        "description": "Metric used to express the market: revenue, volume, units, margin pool, asset base.",
        "value_source": "enum:[revenue,volume,units,margin_pool,asset_base,AUM,other]"
      },
      {
        "key": "price_basis",
        "axis_id": "AX08",
        "name": "Price Basis",
        "description": "Whether numbers are nominal or real, and base year for real terms.",
        "value_source": "enum:[nominal,real_indexed]"
      },
      {
        "key": "currency",
        "axis_id": "AX09",
        "name": "Currency",
        "description": "Reporting currency for all outputs.",
        "value_source": "iso_currency_code"
      },
      {
        "key": "granularity",
        "axis_id": "AX10",
        "name": "Granularity Level",
        "description": "Resolution of the analysis: annual, quarterly, monthly, or scenario-point only.",
        "value_source": "enum:[annual,quarterly,monthly,scenario_only]"
      },

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
