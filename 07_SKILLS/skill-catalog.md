---
title: Skill Catalog
type: alias
source: 07_SKILLS
aliases:
  - skill-catalog
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_REDIRECT
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: active__AMOS_OS
---

# Skill Catalog

---

## Purpose

This file is an alias redirect to the authoritative skill registry catalog. It exists to preserve backward compatibility for references that use the `skill-catalog` path while the canonical content lives at `skill-registry-catalog`.

```text
DOCUMENTED != IMPLEMENTED
DERIVED != CANONICAL_LAW
```

---

## Redirect

The authoritative skill catalog is maintained at:

[[07_SKILLS/skill-registry-catalog|skill-registry-catalog]]

All references to `skill-catalog` should be resolved to `skill-registry-catalog` for canonical content.

---

## Overview

The skill catalog provides a structured index of all AMOS skills, organized by domain, family, and root master. It serves as the primary discovery surface for agents and workflows that need to locate and activate skills. The catalog is maintained as a living document and updated whenever new skills are added, renamed, or reclassified.

### Key Components

- **Skill registry** — The canonical listing of all skills with metadata, provenance, and dependency information.
- **Domain mapping** — Skills are mapped to their owning C-domain under the `21_DOMAINS` architecture.
- **Family index** — Skills are grouped into families for related capability sets.
- **Root masters** — 24 root master skills serve as the top-level capability nodes.
- **Dependency graph** — Skill-to-skill dependencies are tracked for activation ordering and conflict detection.
- **Provenance tracking** — Each skill records its origin, version, and sync status (e.g., Hermès counterpart).
- **Validation status** — Skills are validated for naming compliance, description completeness, and progressive-loading pass.

---

## Navigation

- **Authoritative catalog:** [[07_SKILLS/skill-registry-catalog|skill-registry-catalog]]
- **Skills MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Domain Architecture Index:** [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/DOMAIN_ARCHITECTURE_INDEX|DOMAIN_ARCHITECTURE_INDEX]]
- **Knowledge MOC:** [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE_MOC]]
- **Root MOC:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

---

## Status

- **RSCF State:** `DERIVED`
- **Alias type:** `ACTIVE_REDIRECT`
- **Origin Architect / Steward:** Trang Phan
- **AMOS_CORE Target:** `v4.4`
- This file is maintained as a redirect stub; all canonical content is in `skill-registry-catalog`.
- The redirect target is the authoritative source for skill discovery, domain mapping, and dependency tracking.
- Agents and workflows referencing `skill-catalog` are transparently redirected to `skill-registry-catalog`.
- No canonical content should be added to this file; it is a redirect stub only.
