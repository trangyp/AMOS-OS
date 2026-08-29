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
