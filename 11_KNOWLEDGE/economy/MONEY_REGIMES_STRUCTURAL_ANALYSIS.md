---
tags: [economy]
---
# MONEY REGIMES STRUCTURAL ANALYSIS

## PROOF
[PROOF] Wikipedia. "Gold Standard" - https://en.wikipedia.org/wiki/Gold_standard
[PROOF] Wikipedia. "Bretton Woods system" - https://en.wikipedia.org/wiki/Bretton_Woods_system  
[PROOF] Federal Reserve History. "Creation of the Bretton Woods System" - https://www.federalreservehistory.org/essays/bretton-woods-created
[PROOF] Winton. "The history of the modern international monetary system" - https://www.winton.com/news/the-history-of-the-modern-international-monetary-system
[PROOF] Cleveland Fed. "A Brief History of Central Banks" - https://www.clevelandfed.org/publications/economic-commentary/2007/ec-20071201-a-brief-history-of-central-banks
[PROOF] IMF. "Implications of Central Bank Digital Currency for Monetary Operations" - https://www.imf.org/en/publications/fintech-notes/issues/2024/10/04/implications-of-central-bank-digital-currency-for-monetary-operations-555883
[PROOF] IMF. "Understanding Stablecoins" - https://www.imf.org/-/media/files/publications/dp/2025/english/usea.pdf
[PROOF] ArXiv. "Central Bank Digital Currencies: A Survey" - https://arxiv.org/html/2507.08880v1

## SYMBOLS

- **GS**: Gold Standard
- **BW**: Bretton Woods System  
- **FIAT**: Fiat Money Regime
- **CB**: Central Bank
- **FX**: Foreign Exchange
- **M0**: Monetary Base
- **M1**: Money Supply (currency + demand deposits)
- **BOP**: Balance of Payments
- **IMF**: International Monetary Fund
- **WB**: World Bank
- **CBDC**: Central Bank Digital Currency
- **STABLE**: Stablecoins
- **CRYPTO**: Cryptocurrencies

## INVARIANTS

### Stock-Flow Consistency
- **ΔM0 = ΔFX + ΔDomesticCredit**: Monetary base changes equal foreign exchange changes plus domestic credit creation
- **BOP = Current Account + Capital Account + Financial Account**: Balance of payments identity
- **Assets = Liabilities + Equity**: Balance sheet identity for all monetary institutions

### Budget Constraints
- **Government Budget Constraint**: G - T + B + ΔM = 0 (where G = spending, T = taxes, B = borrowing, M = money creation)
- **External Constraint**: Current Account deficits must be financed by capital inflows or reserve depletion

### Price-Specie Flow Mechanism (Gold Standard)
- **Trade Imbalance**: Deficit countries lose gold, surplus countries gain gold
- **Automatic Adjustment**: Gold flows change money supply, affecting prices and competitiveness
- **Long-Run Equilibrium**: Trade balances return to zero through price adjustments

## EQUATIONS

### Gold Standard (1870-1914, 1925-1933, 1944-1971)
```
P = (M × V) / Y
Exchange Rate = Gold_Parity_1 / Gold_Parity_2
ΔGold_Reserves = -Trade_Deficit
```

### Bretton Woods (1944-1971)
```
$35/oz = Fixed Dollar-Gold Convertibility
Other_Currencies = Fixed to USD (±1%)
IMF_Resources = Total_Quotas × 25%
Balance_of_Payments_Crisis = Reserve_Losses > 20%
```

### Digital Currency Era (2020s-Present)
```
M = C + D + R + CBDC (Currency + Deposits + Reserves + CBDC)
i = r + π + ε + digital_risk_premium
Exchange_Rate = Flexible + Digital_Currency_Competition
Monetary_Base = M0 + CBDC_Stablecoin_Interaction
```

### CBDC Impact Equations
```
CBDC_Demand = f(Interest_Rate, Access_Limits, Remuneration)
Liquidity_Forecasting_Enhanced = Traditional + Digital_Flows
Policy_Rate_Effectiveness = f(CBDC_Design, Market_Penetration)
```

## LOOPS

### Civilisation Monetary Loop
1. **EXPANSION**: Credit growth → Investment → Economic growth → Trade imbalances
2. **LEVERAGE**: Rising debt-to-GDP ratios → Financial innovation → Risk accumulation  
3. **CRISIS**: Balance sheet stress → Confidence collapse → Currency attacks
4. **CONSOLIDATION**: Debt restructuring → Policy reform → New regime foundation
5. **REFORM**: Institutional changes → New monetary framework → Return to expansion

### Gold Standard Crisis Loop
- **Trigger**: War financing → Money supply expansion → Gold outflows
- **Amplification**: Speculative attacks → Reserve depletion → Banking panics
- **Resolution**: Abandonment of convertibility → Devaluation → Deflationary adjustment

### Digital Currency Crisis Loop
- **Trigger**: Stablecoin depegging → CBDC adoption pressure → Traditional banking disruption
- **Amplification**: Digital currency runs → Cross-border capital flows → Regulatory arbitrage
- **Resolution**: Digital monetary policy framework → International coordination → New regime foundation

## GRAPHS/TENSORS

### Monetary Regime Transition Tensor
```
Time: 1870 → 1914 → 1933 → 1944 → 1971 → Present
Regime: GS → Interwar → GS → BW → FIAT
Constraints: Gold → None → Gold → USD → None
Enforcement: Market → Political → Market → Institutional → Policy
```

### Credit Network Graph
- **Nodes**: Banks, Central Banks, Governments, International Institutions
- **Edges**: Credit relationships, Reserve holdings, Currency pegs
- **Weights**: Interest rates, Exchange rates, Capital flows

### Balance Sheet Identity Matrix
```
[Central Bank]  [Assets: Gold/FX Reserves]  [Liabilities: Base Money]
[Commercial Banks] [Assets: Loans]  [Liabilities: Deposits]
[Governments]  [Assets: Tax Revenue]  [Liabilities: Debt]
```

## REGIMES

### Gold Standard (Classical: 1870-1914)
- **Issuer Type**: Private banks (domestic) + Central banks (international)
- **Settlement Technology**: Physical gold coins and bullion
- **Backing**: 100% gold convertibility
- **Capital Controls**: Minimal (free capital movement)
- **Enforcement**: Market discipline + legal tender laws
- **Duration**: 44 years (1870-1914)

### Gold Standard (Interwar: 1925-1933)  
- **Issuer Type**: Central banks with limited convertibility
- **Settlement Technology**: Gold exchange standard
- **Backing**: Partial gold convertibility
- **Capital Controls**: Extensive (competitive devaluations)
- **Enforcement**: Political discretion
- **Duration**: 8 years (1925-1933)

### Bretton Woods (1944-1971)
- **Issuer Type**: Central banks (USD anchor) + IMF oversight
- **Settlement Technology**: Dollar convertibility to gold at $35/oz
- **Backing**: Dollar-gold convertibility + IMF quotas
- **Capital Controls**: Limited (current account convertibility)
- **Enforcement**: Institutional (IMF + World Bank)
- **Duration**: 27 years (1944-1971)

### Digital Currency Regime (Emerging: 2020s-Present)
- **Issuer Type**: Central banks (CBDC) + Private issuers (stablecoins)
- **Settlement Technology**: Distributed ledger + blockchain + traditional systems
- **Backing**: Algorithmic stablecoins + fiat-backed stablecoins + CBDC (full faith and credit)
- **Capital Controls**: Variable (digital border controls + DeFi protocols)
- **Enforcement**: Smart contracts + algorithmic governance + regulatory oversight
- **Duration**: Emerging (2020s-present)

## PROTOCOLS

### Gold Standard Protocol
1. **Fixed Exchange Rates**: Currency values tied to gold at par values
2. **Free Convertibility**: Unlimited gold exchange on demand
3. **Automatic Adjustment**: Price-specie flow mechanism for imbalances
4. **Limited Monetary Policy**: Money supply determined by gold flows

### Bretton Woods Protocol  
1. **Dollar Anchor**: USD convertible to gold at $35/ounce
2. **Fixed Exchange Rates**: Other currencies pegged to USD within ±1%
3. **IMF Surveillance**: Balance of payments monitoring and adjustment
4. **Capital Controls**: Current account convertibility, capital controls on financial flows

### Digital Currency Protocol
1. **Multi-Layered System**: CBDC (retail/wholesale) + Stablecoins + Cryptocurrencies
2. **Programmable Money**: Smart contracts + automated monetary policy execution
3. **Cross-Border Integration**: International CBDC networks + Interoperability standards
4. **Privacy-Preserving Transactions**: Zero-knowledge proofs + selective disclosure controls
5. **Real-Time Monetary Policy**: Algorithmic rate setting + instant liquidity provision

## HYPOTHESES

### HYP-4: Digital Currency Transition Acceleration
- **Hypothesis**: Digital currencies accelerate regime transitions from 25-30 years to 10-15 years
- **Evidence**: 85/93 central banks exploring CBDCs (2025 BIS survey) + stablecoin growth
- **Falsification Plan**: Track digital currency adoption rates vs. traditional banking metrics

### HYP-5: Multi-Currency Competition
- **Hypothesis**: Multiple currency coexistence creates new monetary regime dynamics
- **Evidence**: USD dominance challenged by digital alternatives + cross-border CBDC projects
- **Falsification Plan**: Calculate currency substitution elasticities across digital vs. traditional currencies

### HYP-6: Algorithmic Monetary Policy
- **Hypothesis**: Smart contracts enable automated, rule-based monetary policy with reduced discretion
- **Evidence**: CBDC design features for programmatic rate setting + automated liquidity management
- **Falsification Plan**: Compare policy transmission efficiency across traditional vs. digital monetary systems

## CONFLICTS

### Digital Currency vs. Traditional Banking
- **Conflict**: Algorithmic efficiency vs. human discretion in monetary policy
- **Evidence**: 85/93 central banks exploring CBDCs (2025 BIS survey)
- **Resolution**: Hybrid systems with digital-physical integration

### Global Digital Currency Competition
- **Conflict**: USD dominance vs. multi-polar digital currency system
- **Evidence**: Stablecoin growth + CBDC cross-border projects
- **Resolution**: International coordination on digital monetary standards

### Privacy vs. Transparency
- **Conflict**: Transaction privacy vs. regulatory oversight requirements
- **Evidence**: CBDC privacy design debates + DeFi anonymity concerns
- **Resolution**: Selective disclosure controls + audit trails

## NEXT TESTS

### Digital Currency Integration Tests
1. **CBDC Adoption Rates**: Measure central bank CBDC exploration vs. implementation rates
2. **Stablecoin Stability**: Test reserve adequacy and peg maintenance mechanisms
3. **Cross-Border Flows**: Measure digital currency capital flows vs. traditional flows
4. **DeFi Protocol Risk**: Assess smart contract vulnerabilities and systemic risk
5. **Privacy-Transparency Balance**: Evaluate CBDC privacy features vs. AML requirements

### Regime Transition Acceleration Tests
1. **Digital Currency Velocity**: Calculate velocity of digital vs. traditional currencies
2. **Policy Transmission Speed**: Compare monetary policy effectiveness across digital vs. traditional systems
3. **Financial Inclusion Impact**: Measure unbanked population access via digital currencies
4. **Systemic Risk Metrics**: Develop digital currency systemic risk indicators
5. **International Coordination**: Test cross-border CBDC interoperability standards
