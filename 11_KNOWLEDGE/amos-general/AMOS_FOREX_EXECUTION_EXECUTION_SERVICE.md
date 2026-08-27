---
title: AMOS FOREX EXECUTION EXECUTION SERVICE
tags: [amos-general]
type: note
source: 11_KNOWLEDGE/amos-general
---


// execution/execution_service.js
// Sends validated trades to OANDA via REST API and records them in the DB.

const EventBus = require('../event_bus');
const fetch = require('node-fetch');
const knex = require('../db/database');
require('dotenv').config();

class ExecutionService {
  constructor() {
    EventBus.on('trade_validated', this.onTradeValidated.bind(this));
  }

  async onTradeValidated(signal) {
    const { instrument, side, units = 1000 } = signal;
    // Build a simple market order payload
    const orderPayload = {
      order: {
        units: side === 'BUY' ? String(units) : String(-units),
        instrument,
        timeInForce: 'FOK',
        type: 'MARKET',
        positionFill: 'DEFAULT',
      },
    };

    try {
      const response = await fetch(
        `${process.env.OANDA_API_URL}/${process.env.OANDA_ACCOUNT_ID}/orders`,
        {
          method: 'POST',
          headers: {
            Authorization: `Bearer ${process.env.OANDA_TOKEN}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(orderPayload),
        }
      );
      const data = await response.json();

      if (response.ok) {
        // Store position (simplified – only opening price)
        const priceOpen = data?.orderFillTransaction?.price || null;
        await knex('positions').insert({
          instrument,
          side,
          units,
          price_open: priceOpen,
        });
        EventBus.emit('order_executed', { ...signal, oandaResponse: data });
        console.log(`[Execution] Executed ${side} ${units} ${instrument} @ ${priceOpen}`);
      } else {
        EventBus.emit('order_failed', { ...signal, error: data });
        console.error('[Execution] Order rejected:', data);
      }
    } catch (err) {
      EventBus.emit('order_failed', { ...signal, error: err.message });
      console.error('[Execution] Exception while sending order:', err);
    }
  }
}

module.exports = new ExecutionService();

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
