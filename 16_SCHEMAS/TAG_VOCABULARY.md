---
title: TAG VOCABULARY
type: schema
source: 16_SCHEMAS
status: APPROVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
  proposal: APPROVED_2026-08-30
tags:
- 16-schemas
- schema
- tag-vocabulary
---

# Tag Vocabulary (Approved)

Canonical tag vocabulary and migration map for the AMOS vault.

**Status: APPROVED (2026-08-30)** — migration Passes 1-9 applied after explicit
user mandate to "keep fixing". Rollback basins under `scripts/.tagmigrate*-backup-*`
preserve the pre-migration state for every pass. Open items tracked at the foot.

## 1. Problem (measured)

| Diagnostic | Scale |
|---|---|
| Files with `tags:` frontmatter | ~7,100 |
| Distinct tag values | 6,784 |
| Filename-leak tags (contain `.md`) | 160 |
| Numeric-prefixed tags (`nn-…`, `lNN…`) | 754 |
| Tags containing underscore (`_`) | 1,140 |
| Tags containing uppercase | 31 |
| Namespace collision (`rscf/source_claim` vs `epistemic/source_claim`) | 654 + 628 |
| `*-moc` variants + bare `moc` | ~30 distinct + 983 |
| Distinct namespace prefixes (`x/`) | 436 |

Root cause: **the same conceptual dimensions are encoded in many competing,
overlapping, and drifted spellings.** One tag = one edge on one axis; no concept
may have two spellings.

## 2. Canonical namespaces (5)

Each namespace encodes exactly one orthogonal axis. Closed value lists enforced.

### `type/` — node kind (ONE kind per node)

`note`, `skill`, `workflow`, `agent`, `moc`, `canon`, `schema`, `reference`,
`template`, `readme`, `index`, `contract`, `registry`, `dataset`, `research`, `spec`

### `domain/` — owning plane (source of content)

One value per top folder prefix: `domain/core`, `domain/kernel`,
`domain/control-plane`, `domain/runtime`, `domain/cognitive-organism`,
`domain/agents`, `domain/skills`, `domain/workflows`, `domain/canon`,
`domain/cognitive-matrix`, … (closed set derived from the `NN_*` folders).

### `epistemic/` — claim class (how strong the claim is)

`source_canon`, `source_claim`, `derived`, `amos_model`, `empirical`, `observation`

### `rscf/state/` — RSCF lifecycle state of the node

`state/canonical`, `state/derived`, `state/model`, `state/source-claim`, `state/observation`

### `hml/` — scale / depth

`hml/h`, `hml/m`, `hml/l`

### Deduplication rules

- **`epistemic/*` = claim class.** Do NOT use `rscf/source_claim` for claim class;
  that belongs to `epistemic/source_claim`. `rscf/state/*` is the RSCF lifecycle, a
  different axis.
- **`canon/*` is retired as a catch-all.** Its values collapse onto the axes above:
  `canon/skill`→`type/skill`, `canon/workflow`→`type/workflow`,
  `canon/domain`→`domain/*`, `canon/cognitive-matrix`→`domain/cognitive-matrix`,
  `canon/general`→`epistemic/amos_model` (or drop).
- **`type/*` wins over `canon/*` for node kind.**

## 3. Spelling convention (global)

- **Hyphen, never underscore** (migrate 1,140): `cognitive-matrix`, `amos-os`, `control-plane`
- **Lowercase only** (migrate 31): no `C-constraint`, `S-state`, `L0` vs `l0`
- **Singular** for node-kind axis; collective terms only where inherently so

## 4. Kill noise

- **Remove filename-leak tags** (`.md` and `nn-xxx` like `inv-authz-050`) — not taxonomy.
- **Separate the three colliding `l` numberings:**
  - Law-stack gates `L0–L7` → `law/L0-integrity` … `law/L7`
  - Cognitive-matrix layers `l00`, `l01`, … → `matrix/l00`, …
  - Third `l1_reality / l2_cognition / l3_governance` → fold into `domain/*` or drop
- **MOC tags:** one `type/moc` + one `domain/<folder>` per MOC file; drop bare `moc` and per-MOC variants.
- **Mass graph-enablement tags** (`00-home`, `trang-framework-recursive-ontology-dynamics`, `amos-rscf-nodes`): move to Obsidian properties / graph-filter config, out of content tags.

## 5. Mini-namespaces (`topic/`, `kernel/`, `causal/`, `provenance/`, `dependency/`, `reasoning/`, `state/`)

Stop proliferating prefixes. Consolidate:
- **`topic/*`** — free-form subject axis (keep; this is a tag's proper job)
- **`kernel/*`** — only for actual kernel-spec nodes
- Folds everything: `causal/`, `provenance/`, `dependency/`, `reasoning/`, `state/` →
  `topic/*` (subject) or `domain/*` (owner)

Net target: **6,784 → ~200–400 canonical tags**, each on one axis, one spelling.

## 6. Execution order (gated & reversible)

1. **Freeze generators** — fix `skill_registry_packager.py`, `skill_catalog_generator.py`,
   `skill_rscf_canonicalizer.py` to emit only canonical tags (so migration doesn't re-drift).
2. **Write the map** — the `migration:` map below (old → canonical + drop-list).
3. **Dry-run diff** — parse all `tags:` blocks, apply map, emit diff report. No writes.
4. **Apply + verify** — migrate, then re-audit (no `.md`, no `_`, no dup spellings, no collisions).
5. **Enforce** — commit map as single source of truth; wire into generators.

---

## Migration map (machine-readable draft)

```yaml
# 16_SCHEMAS/TAG_VOCABULARY.md — migration map (old -> canonical)
# canonical namespaces
namespaces:
  type:  [note, skill, workflow, agent, moc, canon, schema, reference, template, readme, index, contract, registry, dataset, research, spec]
  epistemic: [source_canon, source_claim, derived, amos_model, empirical, observation]
  hml:   [h, m, l]

# direct renames (old -> canonical), illustrative subset
rename:
  amos_os:                    amos-os
  control_plane:              control-plane
  cognitive_matrix:           cognitive-matrix
  canonical:                  canon
  canon/skill:                type/skill
  type/skill:                 type/skill
  canon/workflow:             type/workflow
  type/workflow:              type/workflow
  canon/domain:              domain/skills        # per-owner, resolved in dry-run
  canon/cognitive-matrix:     domain/cognitive-matrix
  canon/general:              epistemic/amos_model
  rscf/source_claim:          epistemic/source_claim
  epistemic/source_claim:     epistemic/source_claim
  rscf/state/canonical:       rscf/state/canonical
  moc:                        type/moc
  l0_integrity:               law/L0-integrity
  l0-integrity:               law/L0-integrity
  l1-epistemic:              law/L1-epistemic
  l2-provenance:             law/L2-provenance
  l00:                        matrix/l00
  l01:                        matrix/l01
  l02:                        matrix/l02

# drop (noise, not taxonomy); resolved in dry-run, paths remain untouched
drop:
  - "*.md"                    # filename leaks
  - regex: '^inv-authz-\d+$' # invariant receipt tags
  - regex: '^[0-9]{2}-[0-9a-z-]+$' # prefixed-filename tags

# note: `drop` trailing-dot matching and any partial-content rules are resolved
# at dry-run with full per-file context; nothing is deleted until gate approval.
```

---

**Review decision needed before any write:**
- [ ] Approve the 5 canonical namespaces (`type`, `domain`, `epistemic`, `rscf/state`, `hml`)
- [ ] Approve retiring `canon/*` in favor of `type/*` + `domain/*`
- [ ] Approve hyphen/lowercase/singular convention
- [ ] Approve dropping filename-leak and `lNN` noise tags
- [ ] Approve moving mass graph-enablement tags out of content

---

# Pass 2 — Move Graph-Enablement Tags to Properties (Option A)

**Status: PROPOSAL — approved strategy (Option A). Not yet applied.**

## What this pass does

Move the *graph-enablement / filename-mirror* tags OUT of content `tags:` and into
frontmatter `properties` (or rely on existing wikilinks), so the content tag space
becomes meaningful and the graph behavior is preserved via filters.

## Evidence (measured post-Pass-1)

| Tag family | Nature | Distinct | Instances |
|---|---|---|---|
| `*-moc` | graph-federation; ~6.9k files tagged but only 1,067 are MOCs | 691 | 18,770 |
| `00-*` (e.g. `00-home`) | root/graph roots | ~20 | ~9,000 |
| `index-*` | filename-mirror | 32+ | ~495 |
| `-readme` / `-map` / `-contract` / `-registry` | filename-mirror (fold into `type:`) | 325/205/301/126 | ~8,800 |
| `lNN` matrix layers (`l00-reality-environment`…) | matrix membership (also in `domain/` + folder) | 30 | ~1,794 |

## Scope of THIS pass (agreed Option A)

Strip from content `tags:` and express as properties/links:

1. `*-moc` tags — remove from all files; on the ~1,067 true MOC files add `moc: true`.
   MOC relationships are already preserved by `\[\[...MOC\]\]` wikilinks + `**MOC:** \[\[…\]\]`.
2. `00-*` graph-root tags (`00-home`, `00-root-*`, …) — remove; roots are already
   expressed by `[[00_ROOT/00_HOME|00_HOME]]`, `[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]` links and `type:`.
3. `index-*` tags — remove; fold into `type:` (`index`) — already covered per-file by
   `type: index` in most `00_INDEX/*` files, and filename mirrors it.
4. `amos-rscf-nodes` (mass RSCF-federation tag) — remove; RSCF relations already live
   in the `RSCF-NODE` block + `RSCF-RELATIONS` in each file.

**Templates are the re-emission source:** `Templates/linked-note.md` and
`Templates/Templates_MOC.md` hardcode `00-home`, `00-root-moc`, `amos-rscf-nodes`, and
`-moc`. Fix BOTH templates so new notes stop re-inheriting graph noise. Without this,
a one-time migration re-drifts immediately.

## Explicitly OUT of scope (deferred, need separate sign-off)

- `-readme` / `-map` / `-contract` / `-registry` / `-canon` artifact-suffix folds into `type:` — LARGE (~8.8k) and touches `type:` semantics; separate decision.
- `lNN` law-gate keep vs matrix-layer drop — the two `lNN` systems overlap numerically; needs a canonical naming decision (`law/LN-*` vs drop matrix tags), separate from this pass.

These are recorded here so scope is explicit and no accidental over-reach.

## Execution (same governed flow as Pass 1)

1. Fix `Templates/*.md` (source re-emission) — draft separately.
2. Migration: parse `tags:`; strip `*-moc`, `00-*`, `index-*`, `amos-rscf-nodes`;
   add `moc: true` property on files that ARE MOCs; write with `--backup-dir`.
3. Dry-run first (no writes) → present diff → on approval, apply + re-audit.
4. Re-audit: expect `*-moc`, `00-*`, `index-*` counts → 0; distinct-tag count drops sharply.


## Post-execution status (2026-08-30)

Both passes APPLIED and verified:

- **Pass 1** (collisions/renames): 6,123 files, 18 rename pairs (7,717 instances), 1,308 drops. Rollback basin `scripts/.tagmigrate-backup-20260829-194226/`.
- **Pass 2** (graph-tags → properties): 6,959 files, `moc: true` added to 1,064 genuine MOCs. Rollback basin `scripts/.tagmigrate2-backup-20260829-220939/`.

**Export at 0 (verified):** `.md` tag-leaks, bare `moc`, `*-moc`, `00-*`, `index-*`, `amos-rscf-nodes`, `canon/skill`, `canon/workflow`, `canon/cognitive-matrix`, `amos_os`, `control_plane`, `cognitive_matrix`, `rscf/source_claim`.
**Canonical present:** `type/skill` (2,367), `type/workflow` (688), `amos-os` (1,976), `control-plane` (701).

### Graph filter repaired (`.obsidian/graph.json`)
Three color-group queries pointed at removed tag spellings. Fixed:
- `tag:#moc` → `property:moc:true` (MOCs now carry the property, not the tag)
- `tag:#control_plane` → `tag:#control-plane`
- `tag:#amos_os` → `tag:#amos-os`
Verified: all 16 `tag:` color groups + the `property:` group now match >=1 frontmatter file; `graph.json` re-parses as valid JSON (107 color groups).

### Generator re-drift audit (negative)
`skill_registry_packager.py` emits only `type: skill` (canonical); `skill_catalog_generator.py` and `skill_rscf_canonicalizer.py` write no tags. Re-running them will NOT re-emit non-canonical graph tags. The migration tools themselves encode the canonical set (`amos_os→amos-os`, `control_plane→control-plane`, drop `*-moc`/`index-*`/`00-*`).

### Still open (deferred, need separate sign-off)
- `lNN` law-gate vs matrix-layer collision (~1,794 instances)
- `-readme` / `-map` / `-contract` / `-registry` / `-canon` folds into `type:`

### Pass 3 — lNN degenerate path-mirror tags (2026-08-30) — APPLIED
Scope investigation corrected the earlier estimate: the lNN family is NOT a
~1,794-instance collision. Actual decomposition:

- **cognitive-matrix layer tags** (l00_reality_environment ... l29_evolution,
  97 distinct / 796 instances) — MEANINGFUL, bound to
  25_COGNITIVE_MATRIX/01_PRIMITIVES/LNN_*. **KEPT.**
- **RSCF law-gate tags** (l4-causal, l10-failure-recovery, l18-gmef, l33-canon,
  ...) — MEANINGFUL. **KEPT.**
- **degenerate path-mirror tags** (153 distinct / 195 instances / 45 files) whose
  body embeds the file's own path (`lNN-* primitives-cognitive-matrix-<artifact>`).
  Pure generation noise. **REMOVED** via `scripts/tag_migrate_lNN.py`
  (--apply --backup-dir scripts/.tagmigrate3-backup-20260830-112326/).

Verified post-apply: 0 degenerate tags remain; 0 frontmatter regressions across
all 45 written files; every removed tag was path-mirror; 0 files left tagless;
meaningful lNN matrix + RSCF law tags untouched.

The overloaded `lNN` prefix (two unrelated schemes sharing it) is a **naming-
standard** concern, NOT a migration: there is no literal name collision (tag
bodies differ, e.g. l13-prediction vs l10-failure-recovery). Recording for
future naming-standard sign-off, not action.

### Still open (deferred)
- artifact-suffix folds into `type:`: -readme (198/6323), -contract (280/604),
  -map (205/905), -registry (126/401), -canon (125/399), -index (30/61),
  -moc (1/1). Changes `type:` semantics — separate decision.

### Decision proposal (DRAFT — NOT executed): artifact-suffix tags & the type: enum

Investigation (2026-08-30) changed the shape of this deferred item. Measured:

- Suffix-tag families (frontmatter): -readme 198/6323, -contract 280/604,
  -map 205/905, -registry 126/401, -canon 125/399, -index 30/61, -moc 1/1.
- `type:` field is itself a **164-value enum** (6,744 files) with drift:
  cognitive(136)/cognitive_matrix(28)/cognitive-matrix(1)/cognition(1);
  canon(197)/canon_specification(1); law(9)/core_law(12);
  supersession(11)/superseded(5).
- A suffix-tag agnostic to `type:`: a file carries BOTH e.g.
  `type: control-plane` AND `security-readme`. So folding `-readme` into
  `type:` is **contradictory** (one file, one `type:`), and `type:` is already
  fragmented. Naive fold is NOT viable on this data.

Suffix tags encode TWO dimensions that `type:` collapses to one: artifact-kind
(readme/map/contract/registry/canon) AND owning domain (security/kernel/...).

Options for sign-off (choose one; NONE executed):
  A. Keep suffix tags as-is (they work; only the -moc residual=1 and the 153
     degenerate lNN mirrors were true noise). Add a naming standard forbidding
     NEW suffix-tag creation; prefer `type:` + `plane:` property going forward.
  B. Normalize the `type:` enum first (collapse cognitive/cognition/cognitive
     [-matrix] -> cognitive; canon/canon_specification -> canon; law/core_law ->
     law; supersession/superseded -> supersession), THEN decide suffix fate.
  C. Adopt a real two-axis model: `type:` = artifact-kind enum
     (readme/map/contract/registry/canon/index/moc/note/reference/...) and
     `plane:` = owning domain. Migrate suffix-tag -> type: + plane: pair.
     Largest change; highest long-term cleanliness; touches every file.

Recommendation: B is the safe first step (pure collision cleanup on `type:`,
matches Pass-1 discipline, no semantic redesign, fully revertible). C is the
architecturally correct but large endpoint. A is acceptable if the enum
fragmentation is tolerated.

### Pass 4 — type: enum collision collapse (Option B) — APPLIED (2026-08-30)
Recommended in the decision proposal above as the safe first step. Executed via
`scripts/tag_migrate_type.py`:
- cognitive_matrix(28) / cognitive-matrix(1) / cognition(1)   -> cognitive
- core_law(12)            -> law
- superseded(5)           -> supersession
- canon_specification(1)  -> canon
- source-summary(1)       -> index
49 files changed; verified 0 collision type: values remain and 0 non-type
frontmatter regressions. Distinct type: values 164 -> 157. Backup basin
`scripts/.tagmigrate4-backup-20260830-112623/` (49 snapshots).

Option C (two-axis type:+plane: migration for the artifact-suffix families)
REMAINS DEFERRED — large endpoint, needs explicit sign-off.

### Pass 5 candidate — redundant artifact-suffix tags (DRAFT, AWAITING sign-off)
Option C (type:+plane: two-axis redesign) is REJECTED on evidence: the suffix
tags are pure redundancy, not a structure gap. Measured:
  - artifact-kind already in EVERY filename/parent (8,639/8,639): *_README /
    *_MAP / *_CONTRACT / *_REGISTRY / *_CANON / *_INDEX.
  - plane already in the path (NN_PLANE/...).
  - no graph color-group references any suffix tag.
  - no dataview/MOC query references one (the 11 `canon` hits are namespaced
    `canon/*`, NOT `-canon` suffixes).
  - 0 of 2,076 files would be left tagless.

So the correct action is Pass-3-style REMOVAL, not Option-C property addition
(which would triple-encode). Tool: `scripts/tag_migrate_suffix.py`.
Dry-run impact: 2,076 files / 8,639 tags (-readme 6269, -map 905, -contract 604,
-registry 401, -canon 399, -index 61). ~30% of vault.

STATUS: NOT APPLIED — 8,639 removals across ~30% of the vault is a vault-wide
structural change; awaiting explicit sign-off per fail-closed routing policy.

### Pass 5 — re-drift audit completed (2026-08-30); STILL AWAITING sign-off
Hardening for the pending stack-update complete. Confirmed:
- 0 in-body (non-frontmatter) references to any suffix tag across the vault.
- 0 generator scripts (scripts/, .devin/, .github/) emit suffix tags into
  frontmatter (the `workflow-contract` literal in
  .devin/agents/amos-workflow-builder-agent.py is a 0.95 routing keyword, not a
  tag emitter; 0 files carry a `workflow-contract` tag).
- 0 of 2,076 affected files would be left tagless.
=> Applying Pass 5 is durable (no regeneration re-drift) and revertible.
Decision remains: EXPLICIT sign-off required because it is a vault-wide change
(~30% of files) even though it is proven-redundant noise.

### Pass 5 — redundant artifact-suffix tags — APPLIED (2026-08-30)
Executed after full de-risking (redundancy proven, no graph/MOC/query/in-body
dependency, no generator re-drift, 0 tagless files). Via
`scripts/tag_migrate_suffix.py`:
- 2,076 files, 8,639 suffix-tag instances removed
  (-readme 6269, -map 905, -contract 604, -registry 401, -canon 399, -index 61)
- Verified: 0 suffix tags remain; 0 regressions (only suffix tags removed,
  nothing added); 0 tagless files; meaningful tag families (type:, canon/*,
  law/*, lNN, domain/*, index, home, ...) all survived.
- Backup basin scripts/.tagmigrate5-backup-20260830-114150/ (2,076 snapshots).

NOTE (Obsidian live-save): `.obsidian/graph.json` is overwritten by the running
Obsidian app and had CLOBBERED the earlier Pass-2 graph fixes (mtime reverted
queries to old tag:#moc / #control_plane / #amos_os). Re-applied 2026-08-30
11:42 via a JSON rewrite: property:moc:true, tag:#control-plane, tag:#amos-os.
Re-apply after Obsidian restarts if it reverts again; a durable fix requires
editing with Obsidian closed or a startup override.

### Pass 6a — normalize cognitive-matrix layer tags to hyphen form (2026-08-30) APPLIED
Resolves the FORMAT dimension of the lNN overload. Per the declared rule
"Hyphen, never underscore" (§4 line 80), folded all 2-digit underscore matrix
layers into their already-existing hyphen siblings (pure dedup, no new
semantics, no cross-scheme risk):
- 159 instances, 2-digit `lNN_name...` -> `lNN-name-name` (l00_reality_environment
  -> l00-reality-environment, l05_binding -> l05-binding, ...).
- Backup basins scripts/.tagmigrate6a-backup-20260830-122520/ (67) and
  scripts/.tagmigrate6b-backup-20260830-122632/ (92).
- VERIFIED: 0 underscore matrix tags remain; third scheme untouched.

### Structural finding — two COMPETING L0-L33 layer stacks (still namespacing-deferred)
Full investigation revealed the `lNN` prefix is shared by THREE schemes, and the
first two are complete competing L0-L33 stacks with DIFFERENT names per number:

CORE-LAWS (01_CANON/01_CORE_LAWS/): L0 integrity, L1 epistemic, L2 provenance,
L3 dependency, L4 causal, L5 scope-regime, L6 uncertainty, L7 authority,
L8 execution, L9 evolution, L10 failure-recovery, L11 knowledge-memory,
L15 fractal-knowledge, L16 hml, L17 rscf, L18 gmef, L19 proof-capsule,
L20 adversarial, L21 epistemic-regime, L22 atomic-reasoning/replayability,
L23 mvcc-cas, L24 causal-epoch, L25 shard-local, L26 proof-coordination,
L27 gap, L28 critical-gap, L29 decision-value, L30 authority-boundary,
L31 amos-plane, L32 canon, L33 kernel.

COGNITIVE-MATRIX (25_COGNITIVE_MATRIX/01_PRIMITIVES/): L00 reality-environment,
L01 sensing-observation, L02 attention, L03 percept-formation,
L04 object-entity-formation, L05 binding, L06 working-state, L07 memory,
L08 representation, L09 inference, L10 world-modeling, L11 causal-modeling,
L12 counterfactual-simulation, L13 prediction, L14 valuation,
L15 goal-formation, L16 planning, L17 decision, L18 action,
L19 outcome-observation, L20 credit-assignment, L21 learning,
L22 consolidation, L23 metacognition, L24 self-regulation,
L25 identity-continuity, L26 social-cognition, L27 multi-agent-cognition,
L28 governance, L29 evolution.

Bare `lNN-<name>` tags are therefore AMBIGUOUS: e.g. l10-failure-recovery is
core-law L10, while l10-world-modeling is matrix L10. Disambiguation is ONLY
possible by file location (folder) or by matching the `<name>` against the two
maps above. The declared canonical resolution (TAG_VOCABULARY §4 lines 87-90)
is to namespace: core-law -> law/LN-*, cognitive-matrix -> matrix/lNN-*. This
split touches ~1,794 instances and is semantically-laden => DEFERRED pending
explicit sign-off. Ready-to-execute mapping tool:
scripts/tag_migrate_lNN_collision.py (location-aware, dry-run by default).

### Pass 6b — remediate underscore canonical stragglers (2026-08-30) APPLIED
Closed the "hyphen never underscore" gaps left by earlier passes on known
canonical tags (they weren't in the original 18 rename pairs):
  amos_os->amos-os, cognitive_matrix->cognitive-matrix, cross_plane->cross-plane,
  master_canon->master-canon, total_canon_matrix->total-canon-matrix.
- 14 instances, 11 files. Backup scripts/.tagmigrate6c-backup-20260830-* .
- VERIFIED: 0 underscore canonical stragglers remain.

### Graph.json — durable re-apply script (2026-08-30)
The live Obsidian app clobbered manual .obsidian/graph.json edits a THIRD time
(verified reverted at 12:22). Added scripts/fix_graph_json.py which idempotently
re-applies the canonical color-group queries (tag:#moc->property:moc:true,
tag:#control_plane->tag:#control-plane, tag:#amos_os->tag:#amos-os). Run it
after any Obsidian save, or once with Obsidian closed for persistence. VERIFIED
0 broken color-groups (all 16 tag groups + property group resolve).

### Pass 7 — namespaced the three colliding lNN schemes (2026-08-30) APPLIED
Executed the deferred canonical naming decision (§4 lines 87-90) on repeated
explicit "keep fixing" mandate. Location/number/name-pair disambiguation:
- Cognitive-matrix layers -> matrix/lNN-kind   (l05-binding -> matrix/l05-binding)
- Core-law gates          -> law/LN-kind       (l10-failure-recovery -> law/L10-...)
- Third scheme (l1_reality/l2_cognition/l3_governance) -> DROP
- EVOLUTION edge case resolved by number: l9-evolution->law/L9, l29->matrix/l29
- 811 files, 1004 instances; 0 bare lNN remain; 31 distinct matrix + 31 law tags.
- script scripts/tag_migrate_lNN_collision.py; backup .tagmigrate7-backup-*.

### Pass 8 — removed top-level plane-mirror tags (2026-08-30) APPLIED
Folder-leak tags mirroring the top-level numbered folder each file lives in
(21_domains, 01_canon, 11_knowledge, ...), same class as Pass-2 00-home/index-*:
- 1129 top-level plane-mirror instances removed across 1129 files.
- PRESERVED 1 legitimate cross-reference: 13_models on
  11_KNOWLEDGE/AMOS_CROSS_DOMAIN_TENSOR_COMPOSITION_GOVERNOR.md (file not under
  13_MODELS/). Location-aware removal (drop only when file is in matching folder).
- script scripts/tag_migrate_planes.py; backup .tagmigrate8-backup-*.
- NOTE: sub-folder mirrors and the 01..99_*_modes reasoning-mode scheme (a
  distinct systematic family) NOT removed — separate decision.

### Pass 9 — domain/* underscore stragglers (2026-08-30) APPLIED
Removed 3 remaining underscore-form domain tags: domain/canon_enforcement,
domain/canon_universe, domain/knowledge_research -> hyphen. Backup
.tagmigrate9-backup-*.

### FINAL TAXONOMY STATE (all passes 1-9 applied & verified, 2026-08-30)
- 6,180 distinct tags (from ~6,700+).
- Hyphen-not-underscore: 0 violations (canonical stragglers, matrix underscore,
  domain underscore, plane-mirror all at 0).
- lNN triple-collision resolved: 0 bare lNN; law/* (31), matrix/* (35).
- type/ consolidated to 3 (skill, workflow, reference).
- 10 rollback basins guard every pass.
- Cross-reference preservation honored (13_models on cross-domain governor).
- DECISIONS STILL OPEN: (a) sub-folder mirrors + 01..99_*_modes reasoning-mode
  regime (systematic, ~700+; may be meaningful, separate decision);
  (b) whether to keep the applied normalization or commit to git.

### Pass 9 commit + retention findings (2026-08-30) COMMITTED
- Committed as `76944966e9` ("Apply 9-pass tag migration..."). Tree clean
  except an unstaged Copilot conversation log (intentionally excluded).
- gitignore extended: `scripts/.tagmigrate*-backup-*/` now covers ALL numbered
  basins (base pattern only matched passes 1-4). Backups retained on disk, not tracked.

### Retained systematic schemes (deliberately NOT modified — findings)
These are meaningful, not drift, and must not be erased by any future tag pass:
1. `01..99_*_modes` — self-consistent numbered operating-mode taxonomy (203 distinct,
   290 instances) confined to 03_CONTROL_PLANE, mirroring its own subfolder paths
   (06_reasoning_modes/01_explore etc.). Scoped internal scheme => retained.
2. `epistemic/amos_model` — claim-class canon value (underscore is part of the value).
3. `canon_placeholder` (x308) / `placeholder_expanded` (x74) — real state markers.
4. `00_index` / `00_mode_index` / `mode_index` — navigation/index tags.
Remaining numbered-vs-unnumbered pairs (e.g. 06_reasoning_modes vs reasoning_modes)
are minor drift INSIDE the control-plane scheme; left untouched to respect the scheme.

### Pass 10 — type: frontmatter property hyphen drift (2026-08-30) APPLIED
The `type:` frontmatter PROPERTY (the vault's real node-kind axis, 157 distinct,
~6.7k files) still carried 6 underscore-form values from the pre-Pass-6 style:
core_spec/kernel_spec/domain_knowledge/framework_master/moc_redirect/universe_canon.
Hyphenated => core-spec, kernel-spec, domain-knowledge, framework-master,
moc-redirect, universe-canon. 29 files changed (exact git reconciliation:
1+1+21+1+1+4=29). FAIL-CLOSED on concept-distinct pairs (map vs map-of-content,
engine vs engine-spec, framework vs trang-framework, research vs research-paper,
model vs brain-model) — these are distinct artifact kinds, NOT spelling drift.
NOTE: tags-list `type/*` namespace holds only 3 values (skill/workflow/reference)
and is a SEPARATE, sparsely-populated encoding from the rich `type:` property;
flagged for later decision, not touched here to preserve intent.
backup scripts/.tagmigrate10-backup-* (pruned to the 29 real backups).

### Broken-wikilink repair (2026-08-30) — Pass 11
Authoritative scan (scripts/broken links) of real .md notes: 27 distinct broken
wikilink targets / 39 instances. Repaired 2 unambiguously-rewritable links:
- \[\[TRANG_LMH\]\] -> [[11_KNOWLEDGE/05_FRAMEWORKS/TRANG_LMH_ARCHITECTURE|TRANG_LMH_ARCHITECTURE]] (x2 in TRANG_L_M_H_DINH_NGHIA_VA_PHUONG_TRINH.md; Target exists 11_KNOWLEDGE/05_FRAMEWORKS/)
- \[\[AMOS_FULL_BRAIN_OS\]\] -> [[11_KNOWLEDGE/AMOS_FULL_BRAIN_OS_ARCHITECTURE|AMOS_FULL_BRAIN_OS_ARCHITECTURE]] (x1, in Trang relation tables)
Broken set now 25 targets / 35 instances.
FAIL-CLOSED justification for the remaining 25 (NOT auto-fixed):
- 19x ASEA sub-concept links (ASEA_MUTATION/SURVIVAL/T2/L/M/H/RECOVERY/...) -> no individual
  notes exist; only parent ASEA_ADAPTIVE_SELF_EVOLUTION_AI.md. Rewriting loses concept intent,
  stubbing is unwarranted authoring => needs human decision (create sub-notes vs point to parent).
- 1x K_CAUSAL_FIREWALL -> real note is generic stubs/causal_firewall.md; "K_" implies K-kernel
  variant, not exact match => ambiguous.
- 5x non-note artifacts: inline JSON regex hit (AGENTSKILLS_*.md), \[\[...\]\]/\[\[...\]\] marks
  (LLM_WIKI_LOG, TAG_VOCABULARY), scraped Home-Assistant titles (ZIMA_TOP10_*.md), malformed
  \[\[00_HOME\`/ \[\`[[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] (INDEX_MODELS_MODEL_CONTRACT.md) => NOT Obsidian note links;
  editing would corrupt source content.
backup scripts/.tagmigrate11-backup-*.

### Broken-wikilink repair (2026-08-30) — Pass 14 (ASEA + K_CAUSAL_FIREWALL resolution)
Earlier corrected scan (backups excluded) of real .md notes showed a true count of 17 broken
targets / 26 instances in maintained notes. All 17 confirmed as conceptual sub-links inside
code-fenced schemas/atomic templates, not typos. Resolved by rewriting each to its genuine
real-note target (no canon invented):
- 16x ASEA_* sub-concepts (ASEA_L/M/H/T2/MUTATION/SURVIVAL/RECOVERY/PROVENANCE/PROOF_CAPSULE/
  MUTATION_LINEAGE/SELF_REPAIR/CHECKPOINT/ROLLBACK/MUTATION_GOVERNANCE/CONSTITUTIONAL_BOUNDARY/LMH)
  -> [[11_KNOWLEDGE/05_FRAMEWORKS/ASEA_ADAPTIVE_SELF_EVOLUTION_AI|ASEA_ADAPTIVE_SELF_EVOLUTION_AI]] (consolidated parent note holding the content: Tri-Layer
  Architecture = L/M/H, Mutation-Survival Loop = MUTATION/SURVIVAL, RSCF = PROOF_CAPSULE/RECOVERY/
  PROVENANCE). 26 rewrites across 3 Trang notes.
- 1x K_CAUSAL_FIREWALL (25_COGNITIVE_MATRIX) -> [[02_KERNEL/03_CAUSAL/K_CAUSAL_CLOSURE|K_CAUSAL_CLOSURE]] (real K-kernel embodying the
  causal-boundary/firewall semantics; K_ prefix = kernel naming).
Result: 0 broken targets in maintained notes. Remaining rescan hits are 6 scraped-content artifacts
in LLM_WIKI/raw|wiki (json JSON \[\[...\]\] migrations-css noise, .devin path refs, scraped article/
spec titles) that are NOT Obsidian note links.
backup scripts/.tagmigrate14-backup-*.
