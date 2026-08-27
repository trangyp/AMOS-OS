---
tags: [amos-general]
---
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
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
