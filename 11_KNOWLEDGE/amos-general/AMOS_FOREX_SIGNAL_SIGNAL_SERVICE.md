---
title: AMOS FOREX SIGNAL SIGNAL SERVICE
tags: [amos-general, amos, general, canon/knowledge]
type: note
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture

---


# AMOS FOREX SIGNAL SIGNAL SERVICE

// signal/signal_service.js
// Deterministic signal service – consumes feature events, runs the UKR engine, and emits trade signals.

const EventBus = require('../event_bus');
const UKREngine = require('./ukr_engine');

class SignalService {
  constructor() {
    EventBus.on('feature_generated', (data) => this.onFeature(data));
  }

  onFeature(data) {
    const signal = UKREngine.evaluate(data);
    if (signal) {
      EventBus.emit('signal_generated', signal);
      console.log(`[Signal] Generated ${signal.side} signal for ${signal.instrument}`);
    }
  }
}

module.exports = new SignalService();

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
