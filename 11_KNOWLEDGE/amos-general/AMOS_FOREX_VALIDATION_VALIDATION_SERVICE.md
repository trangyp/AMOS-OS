---
title: AMOS FOREX VALIDATION VALIDATION SERVICE
tags: [amos-general, amos, general, canon/knowledge]
type: note
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture
---


# AMOS FOREX VALIDATION VALIDATION SERVICE

// validation/validation_service.js
// Performs order validation and duplicate checks before risk assessment.

const EventBus = require('../event_bus');

class ValidationService {
  constructor() {
    this.seenSignals = new Set(); // simple duplicate detection
    EventBus.on('signal_generated', this.onTradeSignal.bind(this));
  }

  onTradeSignal(signal) {
    const key = `${signal.instrument}-${signal.time}-${signal.side}`;
    // Duplicate check
    if (this.seenSignals.has(key)) {
      console.log('[Validation] Duplicate signal detected, rejecting.');
      EventBus.emit('trade_rejected', { reason: 'DUPLICATE', signal });
      return;
    }
    this.seenSignals.add(key);

    // Basic field verification
    const required = ['instrument', 'side', 'price'];
    for (const field of required) {
      if (!signal[field]) {
        console.log(`[Validation] Missing ${field}, rejecting.`);
        EventBus.emit('trade_rejected', { reason: `MISSING_${field.toUpperCase()}`, signal });
        return;
      }
    }

    // Stub SL/TP logic – in a real system these would be supplied by the signal.
    const stopLoss = signal.stopLoss || null;
    const takeProfit = signal.takeProfit || null;
    if (!stopLoss || !takeProfit) {
      console.log('[Validation] Missing SL/TP, rejecting.');
      EventBus.emit('trade_rejected', { reason: 'MISSING_SL_TP', signal });
      return;
    }

    // Forward validated trade
    EventBus.emit('trade_validated', { ...signal, stopLoss, takeProfit });
  }
}

module.exports = new ValidationService();

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
