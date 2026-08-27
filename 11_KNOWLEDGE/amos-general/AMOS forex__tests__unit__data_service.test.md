---
tags: [amos-general]
---
// tests/unit/data_service.test.js
const EventBus = require('../../event_bus');
const dataService = require('../../data/data_service');

jest.mock('../../data/oanda_data_service', () => ({
  start: jest.fn(() => console.log('Mock OANDA start')),
}));

describe('DataService wrapper', () => {
  test('starts OandaDataService when start() is called', () => {
    const OandaMock = require('../../data/oanda_data_service');
    dataService.start();
    expect(OandaMock.start).toHaveBeenCalled();
  });
});

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
