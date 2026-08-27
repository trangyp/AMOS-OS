---
tags: [amos-general]
---
// monitoring/monitoring_service.js
// Simple monitoring service – logs events and provides a health endpoint.

const http = require('http');
const EventBus = require('../event_bus');

class MonitoringService {
  constructor() {
    // Subscribe to key events for logging
    const events = ['price_tick', 'feature_generated', 'trade_signal', 'trade_validated', 'trade_rejected', 'order_executed', 'order_failed'];
    events.forEach(ev => EventBus.on(ev, data => console.log(`[Monitoring] ${ev}:`, JSON.stringify(data)));
    this.startHttpServer();
  }

  startHttpServer() {
    const server = http.createServer((req, res) => {
      if (req.method === 'GET' && req.url === '/health') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ status: 'ok', timestamp: new Date().toISOString() }));
      } else {
        res.writeHead(404);
        res.end();
      }
    });
    const port = process.env.MONITOR_PORT || 3001;
    server.listen(port, () => console.log(`[Monitoring] Health endpoint listening on port ${port}`));
  }
}

module.exports = new MonitoringService();

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
