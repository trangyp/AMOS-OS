import os
from pathlib import Path

vault = Path('/Users/mac/Library/CloudStorage/GoogleDrive-phanqtrang@gmail.com/My Drive/_AMOS_OS')
domains = vault / '21_DOMAINS'

domain_specs = {
    "35_BUSINESS_ANALYSIS": {
        "fn": "BUSINESS_ANALYSIS_DOMAINS_DOMAIN_SPEC.md",
        "title": "35_BUSINESS_ANALYSIS — Domain Specification",
        "family": "C07_ECON_FINANCE",
        "content": """---
title: "35_BUSINESS_ANALYSIS — Domain Specification"
type: domain_specification
domain: 35_BUSINESS_ANALYSIS
family: C07_ECON_FINANCE
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
---

# 35_BUSINESS_ANALYSIS — Domain Specification & Enterprise Modeling

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Domain Overview & Enterprise Economics

The Business Analysis domain models unit economics, capital allocation efficiency, cash-flow discount modeling, and enterprise capability maturity.

### Core Mathematical Model (Discounted Cash Flow & Return on Invested Capital)
Enterprise Free Cash Flow ($FCF_t$) and ROIC are formalized as:
$$FCF_t = \text{NOPAT}_t + \text{D\&A}_t - \Delta \text{NWC}_t - \text{CapEx}_t$$
$$\text{Enterprise Value} (EV) = \sum_{t=1}^{T} \frac{FCF_t}{(1 + \text{WACC})^t} + \frac{FCF_T (1 + g)}{(\text{WACC} - g)(1 + \text{WACC})^T}$$
where $\text{WACC} = \frac{E}{V} K_e + \frac{D}{V} K_d (1 - \tau_c)$.

---

## 2. Subdomain Decomposition (MECE)

1. **Unit Economics & Margin Optimization (`ECON-01`)**:
   - Customer Lifetime Value ($LTV$) to Customer Acquisition Cost ($CAC$) ratio optimization: $\frac{LTV}{CAC} \ge 3.0$.
   - Contribution margin sensitivity across multi-product portfolios.
2. **Process Bottleneck Analysis (`PROC-02`)**:
   - Little's Law throughput analysis: $L = \lambda \cdot W$.
   - Theory of Constraints (TOC) flow optimization across operational nodes.
"""
    },
    "36_MARKET_INTELLIGENCE": {
        "fn": "MARKET_INTELLIGENCE_DOMAINS_DOMAIN_SPEC.md",
        "title": "36_MARKET_INTELLIGENCE — Domain Specification",
        "family": "C07_ECON_FINANCE",
        "content": """---
title: "36_MARKET_INTELLIGENCE — Domain Specification"
type: domain_specification
domain: 36_MARKET_INTELLIGENCE
family: C07_ECON_FINANCE
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
---

# 36_MARKET_INTELLIGENCE — Domain Specification & Signal Processing

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Domain Overview & Signal Extraction

Market Intelligence formalizes multi-source signal ingestion, sentiment entropy decomposition, competitor move forecasting, and supply chain telemetry.

### Core Mathematical Model (Information Entropy & Market Surprise)
Let $P(X)$ represent the prior distribution of market events and $Q(X)$ the observed realization. The Kullback-Leibler divergence (Market Surprise) is:
$$D_{KL}(Q \parallel P) = \sum_{x \in \mathcal{X}} Q(x) \log\left(\frac{Q(x)}{P(x)}\right)$$

---

## 2. Subdomain Breakdown (MECE)

1. **Sentiment & NLP Signal Extraction (`SIGNAL-01`)**:
   - Entity recognition and event extraction from unstructured filings, earnings transcripts, and news feeds.
2. **Competitive Landscape Topology (`COMP-02`)**:
   - High-dimensional vector space positioning of competitor feature sets and pricing surfaces.
"""
    },
    "37_TECH_ARCHITECTURE": {
        "fn": "TECH_ARCHITECTURE_DOMAINS_DOMAIN_SPEC.md",
        "title": "37_TECH_ARCHITECTURE — Domain Specification",
        "family": "C10_TECH_ENGINEERING",
        "content": """---
title: "37_TECH_ARCHITECTURE — Domain Specification"
type: domain_specification
domain: 37_TECH_ARCHITECTURE
family: C10_TECH_ENGINEERING
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
---

# 37_TECH_ARCHITECTURE — Domain Specification & Distributed Systems

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Domain Overview & Systems Topology

The Technical Architecture domain defines high-availability distributed systems, event-driven messaging backbones, shard topology, and failure recovery domains.

### Core Mathematical Model (Availability & MTBF / MTTR)
System availability $A$ for series-parallel distributed node topologies is:
$$A_{parallel} = 1 - \prod_{i=1}^n (1 - A_i), \quad A_{series} = \prod_{i=1}^n A_i \quad \text{where} \quad A_i = \frac{\text{MTBF}_i}{\text{MTBF}_i + \text{MTTR}_i}$$

---

## 2. Subdomain Breakdown (MECE)

1. **Event Mesh & Shard Partitioning (`MESH-01`)**:
   - Consistent hashing with virtual nodes to minimize rebalancing overhead during shard scale-out.
2. **Fault Tolerance & Chaos Engineering (`FAULT-02`)**:
   - Automated circuit breaker trip thresholds and graceful degradation fallbacks.
"""
    },
    "38_API_INTEGRATION": {
        "fn": "API_INTEGRATION_DOMAINS_DOMAIN_SPEC.md",
        "title": "38_API_INTEGRATION — Domain Specification",
        "family": "C10_TECH_ENGINEERING",
        "content": """---
title: "38_API_INTEGRATION — Domain Specification"
type: domain_specification
domain: 38_API_INTEGRATION
family: C10_TECH_ENGINEERING
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
---

# 38_API_INTEGRATION — Domain Specification & Connector Fabric

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Domain Overview & Protocol Gateways

API Integration manages schema validation, rate-limiting algorithms, idempotent webhook processing, and external vendor connector mediation.

### Core Mathematical Model (Token Bucket & Leaky Bucket Rate Limiting)
The token bucket depth $B(t)$ with capacity $C$ and refill rate $r$:
$$B(t) = \min(C, B(t - \Delta t) + r \cdot \Delta t) - \text{TokensConsumed}$$
with non-negativity constraint $B(t) \ge 0$ for request admission.

---

## 2. Subdomain Breakdown (MECE)

1. **Webhook Ingestion Engine (`HOOK-01`)**:
   - Idempotent signature verification using HMAC-SHA256 and replay window validation.
2. **Schema Translation Pipeline (`TRANS-02`)**:
   - Bidirectional JSON-LD / Protobuf / GraphQL schema mapping.
"""
    },
    "39_POLITICS_POWER": {
        "fn": "POLITICS_POWER_DOMAINS_DOMAIN_SPEC.md",
        "title": "39_POLITICS_POWER — Domain Specification",
        "family": "C06_SOCIETY_CULTURE",
        "content": """---
title: "39_POLITICS_POWER — Domain Specification"
type: domain_specification
domain: 39_POLITICS_POWER
family: C06_SOCIETY_CULTURE
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
---

# 39_POLITICS_POWER — Domain Specification & Political Economy

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Domain Overview & Power Dynamics

The Politics and Power domain analyzes coalition formation, institutional veto players, regulatory capture, and political risk exposure.

### Core Mathematical Model (Shapley-Shubik & Banzhaf Power Indices)
The Shapley-Shubik voting power index $\phi_i(v)$ for player $i$ in voting game $v$:
$$\phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|! (|N| - |S| - 1)!}{|N|!} (v(S \cup \{i\}) - v(S))$$
"""
    },
    "40_HSE_SAFETY": {
        "fn": "HSE_SAFETY_DOMAINS_DOMAIN_SPEC.md",
        "title": "40_HSE_SAFETY — Domain Specification",
        "family": "C12_EARTH_ECOLOGY",
        "content": """---
title: "40_HSE_SAFETY — Domain Specification"
type: domain_specification
domain: 40_HSE_SAFETY
family: C12_EARTH_ECOLOGY
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
---

# 40_HSE_SAFETY — Domain Specification & Industrial Safety

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Domain Overview & Safety Engineering

HSE Safety formalizes hazardous identification, quantitative risk assessment (QRA), environmental compliance, and occupational health metrics.

### Core Mathematical Model (Risk Matrix & ALARP Thresholds)
Risk $\mathcal{R}$ is the product of incident frequency $F$ and severity consequence $C$:
$$\mathcal{R} = \sum_{k=1}^K F_k \cdot C_k \quad \text{s.t.} \quad \mathcal{R} \le \text{ALARP}_{\text{acceptable}}$$
"""
    },
    "41_QUANTUM_SYSTEMS": {
        "fn": "QUANTUM_SYSTEMS_DOMAINS_DOMAIN_SPEC.md",
        "title": "41_QUANTUM_SYSTEMS — Domain Specification",
        "family": "C03_PHYSICS_COSMOS",
        "content": """---
title: "41_QUANTUM_SYSTEMS — Domain Specification"
type: domain_specification
domain: 41_QUANTUM_SYSTEMS
family: C03_PHYSICS_COSMOS
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
---

# 41_QUANTUM_SYSTEMS — Domain Specification & Quantum Logic

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Domain Overview & Quantum Information

The Quantum Systems domain models density matrix evolution, quantum circuit compilation, and non-commutative operator algebras.

### Core Mathematical Model (Lindblad Master Equation & Von Neumann Entropy)
The open quantum system density matrix $\rho$ evolves according to:
$$\frac{d\rho}{dt} = -\frac{i}{\hbar}[H, \rho] + \sum_k \left( L_k \rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\} \right)$$
with Von Neumann entropy $S(\rho) = -\text{Tr}(\rho \log \rho)$.
"""
    },
    "42_SECTOR_VALUE_CHAIN": {
        "fn": "SECTOR_VALUE_CHAIN_DOMAINS_DOMAIN_SPEC.md",
        "title": "42_SECTOR_VALUE_CHAIN — Domain Specification",
        "family": "C07_ECON_FINANCE",
        "content": """---
title: "42_SECTOR_VALUE_CHAIN — Domain Specification"
type: domain_specification
domain: 42_SECTOR_VALUE_CHAIN
family: C07_ECON_FINANCE
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
---

# 42_SECTOR_VALUE_CHAIN — Domain Specification & Vertical Integration

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Domain Overview & Input-Output Leontief Models

The Sector Value Chain domain models industrial supply chains, value capture along vertical tiers, and input-output interdependencies.

### Core Mathematical Model (Leontief Input-Output Matrix)
The total gross output vector $X$ required to satisfy final demand $D$ with input coefficient matrix $A$:
$$X = (I - A)^{-1} D$$
where $(I - A)^{-1}$ is the Leontief inverse multiplier matrix.
"""
    },
    "43_GEO_GEOPOLITICS": {
        "fn": "GEO_GEOPOLITICS_DOMAINS_DOMAIN_SPEC.md",
        "title": "43_GEO_GEOPOLITICS — Domain Specification",
        "family": "C06_SOCIETY_CULTURE",
        "content": """---
title: "43_GEO_GEOPOLITICS — Domain Specification"
type: domain_specification
domain: 43_GEO_GEOPOLITICS
family: C06_SOCIETY_CULTURE
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
---

# 43_GEO_GEOPOLITICS — Domain Specification & Strategic Geopolitics

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Domain Overview & Geostrategic Equilibrium

Geopolitics analyzes territorial sovereignty, chokepoint control, critical mineral supply chain security, and multi-polar balance of power.

### Core Mathematical Model (Gravity Model of Trade & Geopolitical Tension)
Bilateral trade and strategic interaction $T_{ij}$ between nations $i$ and $j$:
$$T_{ij} = G \cdot \frac{Y_i^\alpha Y_j^\beta}{D_{ij}^\theta} \cdot \exp(-\gamma \cdot \text{GeopoliticalDistance}_{ij})$$
"""
    },
    "44_EV_INFRASTRUCTURE": {
        "fn": "EV_INFRASTRUCTURE_DOMAINS_DOMAIN_SPEC.md",
        "title": "44_EV_INFRASTRUCTURE — Domain Specification",
        "family": "C10_TECH_ENGINEERING",
        "content": """---
title: "44_EV_INFRASTRUCTURE — Domain Specification"
type: domain_specification
domain: 44_EV_INFRASTRUCTURE
family: C10_TECH_ENGINEERING
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
---

# 44_EV_INFRASTRUCTURE — Domain Specification & Grid Balancing

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Domain Overview & Electrification Dynamics

EV Infrastructure formalizes smart charging networks, vehicle-to-grid (V2G) bidirectional power flow, battery degradation models, and transformer thermal loads.

### Core Mathematical Model (V2G Optimal Dispatch & Battery Degradation)
Optimal charging power $P_{ch}(t)$ minimizing cost and battery state-of-health ($\text{SoH}$) loss:
$$\min \int_0^T \left( C_{grid}(t) \cdot P_{ch}(t) + \kappa \cdot \left| \frac{d\text{SoC}}{dt} \right|^\gamma \right) dt \quad \text{s.t.} \quad \text{SoC}_{min} \le \text{SoC}(t) \le \text{SoC}_{max}$$
"""
    },
    "45_MODES": {
        "fn": "MODES_DOMAINS_DOMAIN_SPEC.md",
        "title": "45_MODES — Domain Specification",
        "family": "C01_META_LOGIC",
        "content": """---
title: "45_MODES — Domain Specification"
type: domain_specification
domain: 45_MODES
family: C01_META_LOGIC
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
---

# 45_MODES — Domain Specification & Cognitive Operational Modes

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Domain Overview & Cognitive State Machine

The Modes domain defines the operating regimes of the AMOS OS brain (e.g., Deep Research Mode, Live Trading Execution Mode, Emergency Incident Response Mode, Pedagogical Tutoring Mode).

### Core Mathematical Model (Markov Decision Process Mode Transitions)
Mode transition probability between operating modes $m, m' \in \mathcal{M}$ given stimulus context $c$:
$$P(m' \mid m, c) = \frac{\exp(\beta \cdot Q(m, m', c))}{\sum_{m'' \in \mathcal{M}} \exp(\beta \cdot Q(m, m'', c))}$$
"""
    }
}

for d_name, data in domain_specs.items():
    d_dir = domains / d_name
    d_dir.mkdir(parents=True, exist_ok=True)
    p = d_dir / data["fn"]
    p.write_text(data["content"].strip() + "\n", encoding="utf-8")
    print(f"[CREATED SPEC] 21_DOMAINS/{d_name}/{data['fn']} ({len(data['content'].splitlines())} lines)")

print("All missing domain specifications created and enriched successfully!")
