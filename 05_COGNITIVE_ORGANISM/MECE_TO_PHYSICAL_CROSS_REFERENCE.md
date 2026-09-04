---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Mece To Physical Cross Reference
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# 05 Cognitive Organism — MECE-to-Physical Cross-Reference

> [!abstract] Architecture Mapping
> Maps the MECE functional architecture of the Cognitive Organism (8 groups: A-H) to the physical folder structure (8 subdirectories).
> **Key insight:** Physical folders are NOT the MECE groups — they are storage locations that may contain artifacts from multiple MECE groups.

---

## 1. The Misalignment Problem

The Cognitive Organism defines **8 MECE functional groups** (A-H) in its MOC:

```text
MECE FUNCTIONAL GROUPS (from 05_COGNITIVE_ORGANISM_MOC)
══════════════════════════════════════════════════════════
A. INPUT & REPRESENTATION
B. INTERPRETATION & REASONING
C. AFFECT & DRIVE
D. ACTION FORMATION
E. CONTINUITY & ADAPTATION
F. SOCIAL & EXPRESSION
G. REGULATION & ASSURANCE
H. UBI SUBSTRATE BINDINGS
```

But the physical folder structure is:

```text
PHYSICAL FOLDERS (05_COGNITIVE_ORGANISM/)
══════════════════════════════════════════
00_INDEX
01_IDENTITY
04_COGNITION
06_WORLD_MODEL
07_EMOTION_REGULATION
15_HOMEOSTASIS
16_REPAIR
18_LIFECYCLE
```

**These are NOT the same.** The physical folders are historical/operational storage locations, not MECE functional groups.

---

## 2. MECE-to-Physical Mapping

| MECE Group | Functional Description | Physical Folder(s) | Notes |
| :--- | :--- | :--- | :--- |
| **A. INPUT & REPRESENTATION** | Perception, Attention, World Model | `06_WORLD_MODEL/` | World Model Engine lives here |
| **B. INTERPRETATION & REASONING** | Cognition, Prediction, Metacognitive, Super Mind, Super Consciousness | `04_COGNITION/` | Primary reasoning engines |
| **C. AFFECT & DRIVE** | Emotion, Instinct, Intuition | `07_EMOTION_REGULATION/` | Emotional processing |
| **D. ACTION FORMATION** | Planning, Action Proposal, Agency Governor | *(distributed)* | No dedicated folder — engines at root level |
| **E. CONTINUITY & ADAPTATION** | Memory, Identity, Lifecycle | `01_IDENTITY/`, `18_LIFECYCLE/` | Split across two folders |
| **F. SOCIAL & EXPRESSION** | Cross-Species, Social, Interface Adapters | *(distributed)* | Cross-Species Engine at root |
| **G. REGULATION & ASSURANCE** | Homeostasis, Repair | `15_HOMEOSTASIS/`, `16_REPAIR/` | Split across two folders |
| **H. UBI SUBSTRATE BINDINGS** | UBI, BEI, NBI, NEI, SI, NeuroSyncAI, FullBrainOS | *(root level)* | Binding files at root |

---

## 3. Physical Folder Contents

### `00_INDEX/`
- Navigation maps and indexes
- **MECE Group:** None (meta-navigation)

### `01_IDENTITY/`
- Identity Continuity Model
- **MECE Group:** E (Continuity & Adaptation)

### `04_COGNITION/`
- Human Intelligence Engine
- First Principles Reasoning
- **MECE Group:** B (Interpretation & Reasoning)

### `06_WORLD_MODEL/`
- World Model Engine
- **MECE Group:** A (Input & Representation)

### `07_EMOTION_REGULATION/`
- Emotion-related engines
- **MECE Group:** C (Affect & Drive)

### `15_HOMEOSTASIS/`
- Homeostasis Engine
- **MECE Group:** G (Regulation & Assurance)

### `16_REPAIR/`
- Repair Engine
- **MECE Group:** G (Regulation & Assurance)

### `18_LIFECYCLE/`
- Lifecycle management
- **MECE Group:** E (Continuity & Adaptation)

### Root Level (no dedicated folder)
- Perception Engine, Attention Engine (Group A)
- Cognition Engine, Prediction Engine, Metacognitive Engine, Super Mind Engine, Super Consciousness Engine (Group B)
- Emotion Engine, Instinct Engine, Intuition Engine (Group C)
- Memory Engine, Identity Engine (Group E)
- Cross-Species Mode Engine (Group F)
- Homeostasis Engine, Repair Engine (Group G)
- All UBI/BEI/NBI/NEI/SI/NeuroSyncAI bindings (Group H)

---

## 4. Why This Matters

### 4.1 For Navigation
When searching for "emotion" artifacts, check both:
- `07_EMOTION_REGULATION/` (physical location)
- Group C: Affect & Drive (functional classification)

### 4.2 For Architecture Decisions
When adding a new engine, ask:
1. Which MECE group does it belong to?
2. Is there a physical folder for that group?
3. If not, should it go at root level or create a new folder?

### 4.3 For MECE Compliance
The partition invariant requires:

```text
{All engines in 05_COGNITIVE_ORGANISM} = A ∪ B ∪ C ∪ D ∪ E ∪ F ∪ G ∪ H
A ∩ B ∩ C ∩ D ∩ E ∩ F ∩ G ∩ H = ∅
```

Each engine must belong to exactly one MECE group, regardless of its physical folder.

---

## 5. Recommendations

### 5.1 Current State (Accept)
The physical folder structure is historical and changing it would be disruptive. The current state is acceptable **if and only if**:
- The MOC clearly documents the MECE groups
- Cross-reference documents (like this one) map physical to functional
- New engines are classified by MECE group, not physical folder

### 5.2 Future State (理想)
If the vault is ever reorganized, physical folders should align with MECE groups:

```text
PROPOSED FOLDER STRUCTURE
══════════════════════════
00_INDEX/              (meta)
A_INPUT_REPRESENTATION/
B_INTERPRETATION_REASONING/
C_AFFECT_DRIVE/
D_ACTION_FORMATION/
E_CONTINUITY_ADAPTATION/
F_SOCIAL_EXPRESSION/
G_REGULATION_ASSURANCE/
H_UBI_SUBSTRATE/
```

---

## 6. Cross-Vault References

- [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
- [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
- [[00_ROOT/PLANE_OWNERSHIP_MATRIX|PLANE_OWNERSHIP_MATRIX]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

---

**Parent:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
