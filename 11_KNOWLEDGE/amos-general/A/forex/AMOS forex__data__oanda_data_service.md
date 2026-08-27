---
tags: [amos-general]
---
// data/oanda_data_service.js
// Connects to OANDA pricing stream via WebSocket and emits `price_tick` events.

const WebSocket = require('ws');
const EventBus = require('../event_bus');
require('dotenv').config();

const OANDA_ACCOUNT_ID = process.env.OANDA_ACCOUNT_ID;
const OANDA_API_URL = process.env.OANDA_API_URL || 'https://stream-fxpractice.oanda.com/v3/accounts';

class OandaDataService {
  constructor() {
    this.ws = null;
    this.instruments = ['EUR_USD']; // can be extended via env variable
  }

  start() {
    const instrumentsParam = this.instruments.join('%2C');
    const url = `${OANDA_API_URL}/${OANDA_ACCOUNT_ID}/pricing/stream?instruments=${instrumentsParam}`;
    const headers = { Authorization: `Bearer ${process.env.OANDA_TOKEN}` };

    this.ws = new WebSocket(url, { headers });

    this.ws.on('open', () => console.log('[Data] OANDA pricing stream connected'));
    this.ws.on('message', (data) => this.handleMessage(data));
    this.ws.on('error', (err) => console.error('[Data] WebSocket error:', err));
    this.ws.on('close', () => console.log('[Data] WebSocket closed – reconnecting in 5s') && setTimeout(() => this.start(), 5000));
  }

  handleMessage(raw) {
    try {
      const msg = JSON.parse(raw);
      if (msg.type === 'PRICE') {
        const tick = {
          instrument: msg.instrument,
          time: msg.time,
          bids: msg.bids.map((b) => parseFloat(b.price)),
          asks: msg.asks.map((a) => parseFloat(a.price)),
          closeoutBid: parseFloat(msg.closeoutBid),
          closeoutAsk: parseFloat(msg.closeoutAsk),
        };
        EventBus.emit('price_tick', tick);
      }
    } catch (e) {
      // ignore non‑JSON keep‑alive messages
    }
  }
}

// Auto‑start when required
module.exports = new OandaDataService();

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
