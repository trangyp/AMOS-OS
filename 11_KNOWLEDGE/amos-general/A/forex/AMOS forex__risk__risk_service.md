---
tags: [amos-general]
---
// risk/risk_service.js
// Simple portfolio‑level risk manager stub — deterministic demo implementation.

const EventBus = require('../event_bus');

class RiskService {
  constructor() {
    this.maxPositionSize = 1000; // units, for demo purposes
    this.currentExposure = {}; // instrument -> units
    EventBus.on('trade_validated', this.onTradeValidated.bind(this));
  }

  onTradeValidated(trade) {
    const { instrument, side, units = 100 } = trade; // assume units field or default
    const exposure = this.currentExposure[instrument] || 0;
    const newExposure = side === 'LONG' ? exposure + units : exposure - units;
    if (Math.abs(newExposure) > this.maxPositionSize) {
      console.log('[Risk] Position size limit exceeded, rejecting trade.');
      EventBus.emit('trade_rejected', { reason: 'RISK_LIMIT', trade });
      return;
    }
    this.currentExposure[instrument] = newExposure;
    // Pass through to execution
    EventBus.emit('trade_risk_approved', trade);
  }
}

module.exports = new RiskService();

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
