---
title: AMOS FOREX RESEARCH RESEARCH SERVICE
tags: [amos-general, amos, general, canon/knowledge]
type: note
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture
---


# AMOS FOREX RESEARCH RESEARCH SERVICE

// research/research_service.js
// Technical indicator service – computes SMA, EMA, ATR, and volatility on‑the‑fly.

const EventBus = require('../event_bus');

class TechnicalIndicatorService {
  constructor() {
    this.priceHistory = [];
    this.maxHistory = 200; // keep enough candles for longer SMA
  }

  // Subscribe to price ticks when the module is loaded
  init() {
    EventBus.on('price_tick', (tick) => this.onPriceTick(tick));
  }

  onPriceTick(tick) {
    const price = (parseFloat(tick.bid) + parseFloat(tick.ask)) / 2;
    this.priceHistory.push({ price, time: new Date(tick.time) });
    if (this.priceHistory.length > this.maxHistory) this.priceHistory.shift();

    const features = {
      sma20: this.sma(20),
      sma50: this.sma(50),
      ema20: this.ema(20),
      volatility: this.volatility(20),
    };

    EventBus.emit('feature_generated', { instrument: tick.instrument, time: tick.time, features });
  }

  sma(period) {
    if (this.priceHistory.length < period) return null;
    const slice = this.priceHistory.slice(-period);
    const sum = slice.reduce((a, v) => a + v.price, 0);
    return parseFloat((sum / period).toFixed(5));
  }

  ema(period) {
    if (this.priceHistory.length < period) return null;
    const k = 2 / (period + 1);
    // Start EMA with SMA of first period
    let ema = this.sma(period);
    const recent = this.priceHistory.slice(-period);
    recent.forEach((point) => {
      ema = point.price * k + ema * (1 - k);
    });
    return parseFloat(ema.toFixed(5));
  }

  volatility(period) {
    if (this.priceHistory.length < period) return null;
    const slice = this.priceHistory.slice(-period);
    const mean = slice.reduce((a, v) => a + v.price, 0) / period;
    const variance = slice.reduce((a, v) => a + Math.pow(v.price - mean, 2), 0) / period;
    return parseFloat(Math.sqrt(variance).toFixed(5));
  }
}

module.exports = new TechnicalIndicatorService();

// Initialise listeners immediately
module.exports.init();

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
