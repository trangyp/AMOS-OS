---
title: 2026 08 23 DEPENDENCY STABILIZATION AND GREEN BASELINE
tags: [dated, dated/2026-08-23]
type: document
source: 11_KNOWLEDGE/dated
---



# 2026-08-23 — Dependency Stabilization & Green Baseline

## Context
Session goal: drive COSMO monorepo to production readiness. Blocker found: `node_modules` kept getting torn down by an external process.

## Root Cause Chain (verified)
1. The Antigravity IDE (Cloud Code language server, PID parent of repeated `npm install`) auto-restores dependencies whenever `package.json` / `node_modules` change.
2. Its plain `npm install` failed with ERESOLVE → watcher retried forever → each retry wiped `node_modules/.bin` mid-cycle.
3. ERESOLVE cause: `@testing-library/react-native@12.9.0` (devDep of `@cosmo/ui`) has open peers `react-test-renderer >=16.8` and `react-native >=0.59`. npm resolved latest (`react-test-renderer@19.2.8` → needs `react@^19.2.8`; `react-native@0.87.6` → drags skia/reanimated@4 → RN 0.86+) against the tree's pinned `react@18.2.0` / RN `~0.73.6`.

## Durable Fix (applied)
Root `package.json` overrides:
```json
"overrides": {
  "react-test-renderer": "18.2.0",
  "@testing-library/react-native": { "react-native": "0.73.6" }
}
```
With these, PLAIN `npm install` succeeds → the IDE restore loop terminates on its own. Do not rely on `--legacy-peer-deps` alone; it masks the failure but the IDE keeps retrying plain installs.

## Operational Rules Learned
- NEVER run two npm processes concurrently in this workspace: shared `~/.npm/_cacache` races produce `EEXIST` rename errors; in-workspace races produce `ENOTEMPTY` renames (e.g. `node_modules/eslint`).
- When installs collide: kill all `npm install` PIDs, wait for idle, run ONE serial install.
- The IDE reverts externally-edited config files sometimes; verify edits persist via `git diff package.json` after writing.
- A stale `package-lock.json` can carry a dead manifest snapshot (it once contained Babel 8 presets not present in any package.json). Trust the manifests, not a hand-built lockfile; regenerate via install.

## Code Fixes Applied This Session
- `packages/testing/package.json`: added missing devDep `@testing-library/react-native@^12.4.0` (was used in `src/index.tsx` but undeclared → TS2307 + TS7031 cascade).
- `cosmo-brain/.eslintrc.json`: added `AMOS_Kafka_Brain_Buffer_v1.0.ts`, `.test.ts`, `vitest.kafka.config.ts` to `ignorePatterns` (matches existing convention of excluding root kernel artifacts like `AMOS_OS_KERNEL/`).

## Verified Baseline (2026-08-23)
| Check | Result |
|---|---|
| `npx turbo run type-check` | 17/17 pass |
| `npx turbo run test` | 9/9 pass (1253 brain tests, 74 files) |
| `npx turbo run lint` | 6/6 pass |
| `npx turbo run build` | 5/5 pass |

## Next
Gap analysis vs MVP PRD Phase 35 (P0 loop), then implementation per BUILD_PROTOCOL.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[DATED_MOC]]
