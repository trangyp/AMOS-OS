---
tags: [amos-general]
---
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
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
