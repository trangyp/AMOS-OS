---
title: AMOS C07 Econ Finance Master
aliases:
  - amos-c07-econ-finance-master
  - 07_SKILLS/amos-c07-econ-finance-master
type: redirect
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 07_SKILLS/amos-c07-econ-finance-master/SKILL.md
  scope: 07_SKILLS
---
# AMOS C07 Econ Finance Master

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Domain:** `c07`
> **Epistemic Class:** `AMOS_MODEL`
> **Claim Class:** `DERIVED`
> **Governing Plane:** `07_SKILLS`

---

## Purpose

This redirect anchors the AMOS C07 Econ and Finance master skill, the root authority for unit economics, forex, investment, wealth, business analysis, market dynamics, and trade. The BizFin Engine enforces unit-economics-first reasoning before scaling. It routes all econ-finance queries to the canonical SKILL.md and its 44 consolidated sub-skills.

## Domain Coverage

1. Market dynamics analysis: price formation, regime shifts, fractal economics, chaos diagnostics
2. Economic claim validation: scope regime, empirical calibration vs theoretical model, overclaim
3. Financial risk computation: tail risk, conformal prediction, investment decision metrics
4. Provenance tracing to market data, fractal analysis, and vault sources
5. Economic claim assessment: empirical support, model validity, scope, falsifier
6. Economic lifecycle management: analyze, model, validate, calibrate, finalize
7. Drift detection: regime shift, model decay, market change, calibration loss

## Key Capabilities

| Capability | Function |
| :--- | :--- |
| `c07_econ_finance.analyze_market` | Analyze market dynamics: price formation, regime shifts, fractal economics |
| `c07_econ_finance.validate_econ` | Validate economic claims for scope regime and overclaim |
| `c07_econ_finance.compute_risk` | Compute financial risk: tail risk, conformal prediction, decision metrics |
| `c07_econ_finance.assess_econ_claim` | Assess economic claims for empirical support and model validity |
| `c07_econ_finance.detect_econ_drift` | Detect regime shift, model decay, market change, calibration loss |

## MECE Mapping to AMOS Planes

- **11_KNOWLEDGE**: Knowledge base for economic and financial domain content
- **01_CANON**: Canon laws governing economic claim boundaries
- **07_SKILLS**: Procedural capability registry (this plane)
- **03_CONTROL_PLANE**: Economic governance and resource allocation authority
- **17_OBSERVABILITY**: Receipt sealing for financial decision events

## Epistemic Boundaries

- `CAPABILITY != AUTHORITY`: Implementing a procedure does not confer execution rights
- `DOCUMENTED != IMPLEMENTED`: Skill specification presence does not prove runtime deployment
- `SKILL != AGENT`: This skill is a passive procedure; agents invoke it, it never self-triggers
- Domain claims remain `DERIVED` until independently validated against vault sources

## Sub-Skill Consolidation

This master skill consolidates 44 sub-skills under the `c07` domain. Each sub-skill inherits the master's epistemic boundaries and RSCF state classification while maintaining its own capability scope and validation gates.

## Navigation

- **Canonical SKILL:** [[07_SKILLS/amos-c07-econ-finance-master/SKILL.md|AMOS C07 Econ Finance Master SKILL.md]]
- **Agent Template:** [[07_SKILLS/amos-c07-econ-finance-master/AGENT_TEMPLATE.md|AMOS C07 Econ Finance Master AGENT_TEMPLATE]]
- **MOC:** [[07_SKILLS/amos-c07-econ-finance-master/amos-c07-econ-finance-master_MOC|amos-c07-econ-finance-master_MOC]]
- **Skills MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Skill Contract:** [[07_SKILLS/SKILLS_SKILL_CONTRACT|SKILLS_SKILL_CONTRACT]]
- **Vault Source:** [[11_KNOWLEDGE/AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE|AMOS_C07_ECON_FINANCE_MASTER_KNOWLEDGE]]
- **AMOS Home:** [[00_ROOT/00_HOME|00_HOME]]
- **RSCF Registry:** [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
