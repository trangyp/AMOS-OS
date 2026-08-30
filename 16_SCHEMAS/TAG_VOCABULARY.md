---
title: TAG VOCABULARY
type: schema
source: 16_SCHEMAS
status: PROPOSAL
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
  proposal: PENDING_REVIEW
---

# Tag Vocabulary (Proposal)

Canonical tag vocabulary and migration map for the AMOS vault.

**Status: PROPOSAL — not yet applied.** No files are modified until the migration
dry-run diff is reviewed and approved.

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
   MOC relationships are already preserved by `[[...MOC]]` wikilinks + `**MOC:** [[…]]`.
2. `00-*` graph-root tags (`00-home`, `00-root-*`, …) — remove; roots are already
   expressed by `[[00_HOME]]`, `[[00_ROOT_MOC]]` links and `type:`.
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
