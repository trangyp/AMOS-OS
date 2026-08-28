---
title: EMOTIONAL STABILITY MARKET RISK DASHBOARD
tags:
- economy
- finance
- market
- canon/knowledge
type: document
source: 11_KNOWLEDGE/economy
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: economic_model
---


# Emotional Stability → Market Risk Dashboard 
**Why We Need It**
This dashboard is a predictive early-warning system that monitors market behaviour, liquidity, leverage, sentiment, and on-chain flows to detect when the market becomes unstable.
**Why It Matters**
Protects Capital: Gives us hours or days of lead time before major market drops, letting us adjust exposure and preserve value.
Builds Trust: Shows users and investors that Educhain Fintech is professionally managed with institutional-grade risk controls.
Strengthens Decisions: Converts complex market data into a single, clear Market Risk Index (MRI) that management can act on.
Supports Growth: A stable, risk-aware platform attracts more partners and larger capital inflows because we can prove we manage volatility intelligently.
**Outcome**
By building this dashboard, Educhain Fintech positions itself as a safer, more professional ecosystem, capable of navigating volatile markets and protecting both investors and users — which directly increases confidence, adoption, and valuation.
## Goal
Build a **predictive early-warning system** for sharp drawdowns by converting market “emotional instability” into a 0–100 **Market Risk Index (MRI)** with actionable alerts.
* * *
## What is it? 
This model isn’t just “cool tech” — it’s a **decision-making weapon** :
  * Lets you **front-run liquidations** and avoid getting trapped.


  * Lets you **scale in or out strategically** rather than emotionally.


  * Gives you the confidence to speak with investors, partners, and boards with data, not guesswork.


# Core signals
  1. **Volatility Shock**


  * Realized vol (24h, 7d), ATR(14), Bollinger Band width.


  * Trigger: 7d vol / 30d vol > **1.6** or BB width > **2.2×** 90-day median.


  1. **Liquidity Fragility**


  * Order-book depth within ±1% and ±2% mid-price.


  * Bid/ask imbalance = (BidDepth − AskDepth) / (BidDepth + AskDepth).


  * Trigger: Depth/MarketCap in bottom **10%** of 1-year history or imbalance < **−0.35**.


  1. **Leverage Stress**


  * Perp funding rate (hourly, 8h), open interest (OI), OI/MarketCap.


  * “Crowded Longs” index = z-score(funding) + z-score(OI/MCAP).


  * Trigger: index > **2.0** and price momentum turns negative (5×1h EMAs cross down).


  1. **Liquidation Overhang**


  * Cumulative long liquidation levels (heatmap by price) from derivatives venues.


  * Trigger: ≥ **$X** notional liquidations sitting within **−3%** of spot and growing > **20%** d/d.


  1. **Flow & Breadth**


  * Net exchange inflows (spot) 24h & 7d.


  * % of majors above 20D MA (market breadth).


  * Trigger: inflows > **95th** percentile **and** breadth < **40%**.


  1. **Sentiment Instability**


  * News/Twitter/Reddit headline polarity (VADER/FinBERT) → rolling 1h & 24h averages.


  * “Tone whiplash” = |1h tone − 24h tone|.


  * Trigger: whiplash > **1.2σ** and tone < **−0.2**.


  1. **Search Anxiety**


  * Google Trends for “sell crypto”, “crypto crash”, “recession”, plus local language terms.


  * Trigger: 3-week MA crosses above 12-week MA by **> 25%**.


  1. **On-chain Stress (if L1 tokens)**


  * Exchange-bound flows, realized profit/loss (SOPR), age-band distribution (old coins waking up).


  * Trigger: SOPR > **1.05** then flips < **1.0** within 72h **and** dormant→active > **2σ**.  


  1. **Options Market Signals (if available)**
     * **Put/Call Skew** (25Δ options): When traders rush for downside protection.
     * **IV Rank:** Where implied volatility sits vs its 1y range → cheap/expensive hedging.
     * **Gamma Exposure:** Shows where dealers will need to sell more as price drops (gamma flip zones).


  2. **Correlated Asset Stress**
     * BTC-DXY (dollar index) correlation spikes → risk-off environments.
     * Nasdaq or S&P futures overnight → global macro sentiment feed.
     * Oil & gold moves — often trigger liquidity events in EM/crypto.


  3. **Stablecoin Health**
     * Supply changes in USDT/USDC/BUSD.
     * Peg deviations >0.3% (especially USDT on CEX/DEX).
     * On-chain mint/burn activity surges (signal of cash entering/leaving).


  4. **Whale Behaviour**
     * Top wallet cluster netflows (Glassnode/Nansen).
     * Whale CEX deposits > historical 90th percentile = dump risk.


  5. **Funding Mix / OI Quality**
     * Share of OI that’s perps vs dated futures (perps = more fragile).
     * Long/short ratio skew (if >70% long, big squeeze risk).


  6. **Cross-venue Stress**
     * Spread divergence (spot vs perp, CEX vs DEX) → market dislocation early warning.
     * Rising borrow rates on DeFi lending protocols → leverage getting expensive.


  7. **Regulatory / News Shocks**
     * Classify headlines: SEC actions, exchange hacks, insolvency rumours.
     * Give these a **shock score** (can spike MRI even if market is calm).


* * *
# Risk engine
  * Normalize each signal to 0–100 (min-max or robust z).


  * Weighted score (example weights):  
Vol 15, Liquidity 15, Leverage 15, Liquidations 15, Flow/Breadth 15, Sentiment 15, Search 5, On-chain 5.


  * **Market Risk Index (MRI)** bands:
    * 0–39: Stable
    * 40–59: Watch
    * 60–74: **Elevated**
    * 75–100: **Imminent Risk**


  * Add **Hysteresis** : need 2 consecutive intervals above a band to upgrade; 3 below to downgrade (reduces noise).


# Dashboard layout
  * **Top bar** : MRI gauge + 24h/7d trend sparkline, current band, last change.


  * **Heatmap** : Signals by venue (Binance/OKX/Bybit), by asset (BTC/ETH/EDC/majors).


  * **Panels** :
    1. Volatility & Liquidity (BB width, depth, imbalance)
    2. Leverage & Liquidations (funding, OI, liquidation map)
    3. Flows & Breadth (exchange netflows, % above MA)
    4. Sentiment & Search (tone, whiplash, GT)
    5. On-chain (if applicable)


  * **Event tape** : notable spikes/crosses with timestamps (“Funding z>2.5”, “Depth bottom decile”, etc.).


  * **What-if** : MRI components with weights (sliders) to test sensitivity.


# Alerts
  * Telegram/Slack: when MRI crosses **60** (Elevated) or **75** (Imminent), or any single signal breaches **99th** percentile.


  * Daily 09:00 ICT digest with key diffs vs. yesterday.


# Data & stack (pragmatic)
  * **Market/derivatives** : CCXT (spot), exchange APIs for depth/OI/funding; Kaiko/CoinGlass/Laevitas if you have subs.


  * **News/Social** : NewsAPI/Twitter/X API or Firehose alternative; run text through VADER/FinBERT.


  * **Search** : pytrends (Google Trends).


  * **On-chain** : Glassnode/Nansen/Dune (or node + ETL if you prefer).


  * Backend: Python (pandas, numpy), tasks via Airflow/Prefect;  
Store: Postgres/BigQuery;  
Frontend: Streamlit/Plotly Dash/Grafana for speed;  
Alerts: Bot to Telegram/Slack.


# Example formulas (for Long)
  * **Vol-shock** = (RealizedVol7d / RealizedVol30d).


  * **Depth ratio** = (Depth±1%) / MktCap.


  * **Leverage index** = z(funding) + z(OI/MktCap).


  * **Tone whiplash** = |Tone_1h − Tone_24h|.


  * **MRI** = Σ(weight_i × normalized_signal_i).


# Privacy & abuse guardrails
  * Log sources & transforms; show “confidence” next to each signal.


  * Rate-limit alerts to avoid spam; add manual override/snooze.


* * *
### Brief for the team
> Task: Build an Emotional Stability → Market Risk dashboard to warn of drawdowns.
> **Inputs:** price/vol, order-book depth & imbalance, funding & OI, liquidation levels, exchange netflows & market breadth, news/social sentiment, Google Trends, optional on-chain (SOPR, exchange flows).
> **Output:** A 0–100 **Market Risk Index** with bands (Stable/Watch/Elevated/Imminent), per-signal heatmap, and alerts (MRI≥60/75; 99th-percentile spikes).
> **Methods:** Normalize each signal, weighted sum (Vol 15, Liquidity 15, Leverage 15, Liquidations 15, Flow/Breadth 15, Sentiment 15, Search 5, On-chain 5). Add hysteresis on band changes.
> **Stack:** Python + Postgres/BigQuery; Streamlit/Plotly/Grafana UI; Telegram/Slack alerts.
> **Deliverables:** (1) Live dashboard, (2) JSON/CSV feed of MRI and components, (3) alert bot, (4) README with formulas and data sources.
# 1) Signal → Score (0–100)
Normalize each raw metric into a **tail-aware score** so spikes matter more than drift.
**Robust z-score (winsorized):**
  * Compute rolling median `m_t` and MAD `mad_t` over lookback L (e.g., 180d).


  * `rz_t = (x_t - m_t) / (1.4826 * mad_t)` clipped to [-5, +5].


  * Convert to 0–100 risk:
    * If higher = riskier: `s_t = 50 + 10*rz_t` → clamp [0,100].
    * If lower = riskier (e.g., depth): `s_t = 50 - 10*rz_t`.


  * Apply **EWMA smoothing** : `s*_t = α*s_t + (1-α)*s*_{t-1}` with α=0.3.


**Tail boost:** if `|rz_t| > 2.5`, add +5 (clamped), if >3.5 add +10.
This turns **rare events** into clear warnings.
# 2) Baseline Weights (start simple)
```
    Volatility 15
    Liquidity 15
    Leverage 15
    Liquidations 15
    Flows/Breadth 15
    Sentiment 15
    Search 5
    On-chain 5
    [Optional add-ons: Options 5, Stablecoin Health 5]  // if/when you ingest
    
```
**Market Risk Index (MRI):**
`MRI_t = Σ (w_i * s*_i,t) / Σ w_i` → 0–100.
**Bands + Hysteresis:**
  * Stable <40, Watch 40–59, **Elevated 60–74** , **Imminent ≥75**.


  * Upgrade if 2 consecutive intervals breach; downgrade if 3 below (reduces whipsaw).


# 3) Ground Truth (labels)
Create objective “risk event” labels for backtesting.
  * **Drawdown label:** `DD_k = 1` if max peak-to-trough in next `k` days ≤ −10% (test `k∈{3,5,7}` and −8/−12% too).


  * **Vol-shock label:** realized vol (next 3d) in top 10% of 1y history.  
Use drawdown as primary; vol-shock for sensitivity.


# 4) Backtest Framework
**Split:** rolling time windows to avoid look-ahead.
  * Train: months 1–6, Validate: month 7, Test: month 8; roll forward (walk-forward).


  * Or 70/15/15 chronological.


**Metrics:**
  * **AUROC** , **AUPRC** (imbalanced events), **Recall@fixed False Alarm Rate** (e.g., <=1 alert/week), **Lead time** (median hours between first Imminent alert and event).


  * **Economic** : cost-weighted loss: `Cost = 8*FN + 1*FP` (missing a crash hurts more).


**Calibration:**
  * Optimize α (EWMA), L (lookback), thresholds (60/75), and weights `w_i` to **maximize cost-adjusted F1** or **minimize cost** on validation.


  * Keep a **parsimonious** set (avoid overfitting): cap any weight ≤25 and ≥5.


# 5) Auto-Tuning (two layers)
**(A) Heuristic grid search:**
  * For each regime (low/high vol), test:
    * α ∈ {0.2, 0.3, 0.5}
    * L ∈ {120, 180, 360 days}
    * thresholds: Elevated ∈ {55,60,65}, Imminent ∈ {70,75,80}
    * reweight top 3 predictive signals by +5 each (others −2)


  * Pick combo with best **cost-min** \+ **lead time**.


**(B) Meta-model (optional, simple):**
  * Logistic regression (lasso) on the **individual scores** `s*_i,t` to predict label (next 3–5d drawdown).


  * Convert predicted prob to MRI via monotonic map (e.g., `MRI = 100*prob`).


  * Keep interpretability: inspect coefficients → these become **data-driven weights**.


  * For non-linear lift later: LightGBM with **monotonic constraints** (risk ↑ with worse signals).


# 6) Regime Detection (stability booster)
Market behaves differently in calm vs. wild regimes.
  * **Regime score:** `Regime = z(RealizedVol30d) + z(BB width 20d)`


  * If Regime > 1.5 → **High-vol regime** → increase weights on **Liquidity, Liquidations, Leverage** by +3 each; decrease **Search** by −2.


  * If Regime < 0 → **Calm regime** → up-weight **Sentiment & Search** (early retail anxiety) by +3.


# 7) Feature sanity (what you asked “what’s missing”)
Add when ready and allow the tuner to reweight:
  * **Options skew / IV rank / gamma flip** (if data available).


  * **Stablecoin health** (USDT/USDC peg drift, supply Δ).


  * **Whale CEX deposits** (90th pct spikes).


  * **Cross-venue spreads** (spot–perp dislocations).


  * **Macro link** (DXY↑ & Nasdaq↓ correlation spike).


  * **Regulatory shock score** (NER + keyword rules; cap a hard floor MRI≥65 for X hours).


# 8) Alert logic (precision over spam)
  * **Pre-alerts (“Watch”)** : MRI≥60 sustained 2 ticks **and** at least 2 of {Liquidity, Leverage, Liquidations, Sentiment} ≥70.


  * **Imminent** : MRI≥75 **or** (any of Liquidity/Leverage/Liquidations ≥85 and rising) **and** price < 5×1h EMA.


  * **Cooldown:** minimum 3h between identical alert types; merge duplicates.


**Telegram copy (clear & actionable):**
  * _ELEVATED RISK (MRI 66 ↑)_ – Liquidity thin (depth p10), funding crowded longs (z=2.3). Tighten risk, reduce leverage.


  * _IMMINENT RISK (MRI 78)_ – Liquidation overhang within −2.8%, sentiment whiplash high. Consider de-risking / hedge.


# 9) Drift & health checks
  * Weekly **PSI** (population stability index) on each signal to catch distribution drift.


  * Refit medians/MAD monthly; lock thresholds for a month to avoid jitter.


  * Backtest refresh weekly; human-in-the-loop approves weight shifts.


# 10) Config schema (portable & auditable)
```
    {
      "lookbacks": {"median_days": 180, "ewma_alpha": 0.3},
      "bands": {"watch": 60, "imminent": 75, "upgrade_ticks": 2, "downgrade_ticks": 3},
      "weights": {
        "volatility": 15, "liquidity": 15, "leverage": 15, "liquidations": 15,
        "flows_breadth": 15, "sentiment": 15, "search": 5, "onchain": 5,
        "options": 0, "stablecoin_health": 0
      },
      "tail_boost": {"z25": 5, "z35": 10},
      "regime": {"high_vol_threshold": 1.5, "calm_threshold": 0.0,
        "adjustments": {
          "high_vol": {"liquidity": 3, "leverage": 3, "liquidations": 3, "search": -2},
          "calm": {"sentiment": 3, "search": 3}
        }
      },
      "alerts": {"cooldown_minutes": 180, "component_tripwire": 85}
    }
    
```
# 11) Minimal backtest pseudocode (readable)
```
    # signals_df: time index, columns like s_vol, s_liq, s_lev, s_liqdn, s_flow, s_sent, s_search, s_onchain
    # price: close series; labels via future drawdown
    
    # 1. robust z + 0-100 scaling + EWMA
    for col in signals_df.columns:
        m = rolling_median(signals_df[col], L)
        mad = rolling_mad(signals_df[col], L)
        rz = (signals_df[col]-m)/(1.4826*mad)
        rz = rz.clip(-5,5)
        s = 50 + 10*rz * direction[col]   # direction +1/-1
        s = apply_tail_boost(s, rz)
        signals_df[col] = ewma(s, alpha=0.3).clip(0,100)
    
    # 2. regime-adjusted weights
    regime = z(realized_vol_30d) + z(bb_width_20d)
    W = base_weights.copy()
    W = adjust_by_regime(W, regime_t)
    
    # 3. MRI
    MRI = (signals_df @ W.values) / sum(W.values)
    
    # 4. labels
    label = future_drawdown(price, horizon_days=5, threshold=-0.10)  # 10% in 5d
    
    # 5. evaluate thresholds / weights via grid search
    best = None
    for thr_watch in [55,60,65]:
        for thr_imm in [70,75,80]:
            metrics = evaluate(MRI, label, cost_fn, lead_time)
            best = keep_if_better(best, metrics)
    
    # 6. (optional) logistic meta-model
    X = signals_df.values
    y = label.values
    logit = fit_l1_logistic(X_train, y_train)
    prob = logit.predict_proba(X_valid)[:,1]
    MRI2 = 100*prob
    
```
# 12) “What good looks like” (targets)
  * **Recall (Imminent)** ≥ 0.65 at ≤ 3 false Imminent alerts/week.


  * **Median lead time** ≥ 6–12 hours before −8%/−10% events.


  * **Cost reduction** vs. naive (price-only) alert by ≥ 30%.


* * *
\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[ECONOMY_MOC]]
