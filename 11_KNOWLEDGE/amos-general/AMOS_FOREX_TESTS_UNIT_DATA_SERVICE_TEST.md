---
title: AMOS FOREX TESTS UNIT DATA SERVICE TEST
tags: [amos-general, amos, general, canon/knowledge]
type: note
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture
---


# AMOS FOREX TESTS UNIT DATA SERVICE TEST

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
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
