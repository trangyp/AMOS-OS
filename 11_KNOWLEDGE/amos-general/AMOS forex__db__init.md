---
tags: [amos-general]
---
// db/init.js
// Run simple migrations to ensure tables exist.

const knex = require('./database');

async function runMigrations() {
  const existsPositions = await knex.schema.hasTable('positions');
  if (!existsPositions) {
    await knex.schema.createTable('positions', (table) => {
      table.increments('id').primary();
      table.string('instrument');
      table.string('side');
      table.decimal('units');
      table.timestamp('opened_at').defaultTo(knex.fn.now());
      table.timestamp('closed_at').nullable();
      table.decimal('price_open');
      table.decimal('price_close').nullable();
    });
    console.log('[DB] positions table created');
  }

  const existsRisk = await knex.schema.hasTable('risk_metrics');
  if (!existsRisk) {
    await knex.schema.createTable('risk_metrics', (table) => {
      table.increments('id').primary();
      table.string('instrument');
      table.decimal('current_exposure').defaultTo(0);
      table.decimal('max_exposure').defaultTo(10000);
    });
    console.log('[DB] risk_metrics table created');
  }

  const existsAudit = await knex.schema.hasTable('audit_log');
  if (!existsAudit) {
    await knex.schema.createTable('audit_log', (table) => {
      table.increments('id').primary();
      table.timestamp('timestamp').defaultTo(knex.fn.now());
      table.string('event');
      table.json('payload');
    });
    console.log('[DB] audit_log table created');
  }
}

module.exports = { runMigrations };

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
