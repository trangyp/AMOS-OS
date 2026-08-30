---
title: 11k component map
type: reference
source: 07_SKILLS/amos-c10-tech-engineering-master/references
tags:
- reference
- amos-c10-tech-engineering-master
- type/skill
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# 11K Component Map

> Source: `/Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/Cosmo_Brain/COMPONENT_MAP.md`
> Epistemic class: SOURCE_DERIVED

# COSMO Component Map

This map defines all reusable UI components, their variants, and their usage across the application.

## Design Token Packages

### `@cosmo/tokens`
Color tokens, typography, spacing, radius, shadows, gradients, z-index, breakpoints.

**Color Palette:**
- `primary`: #b9c6e8 (Cosmo light blue)
- `primaryContainer`: #a7b5e2
- `secondary`: #ffade3 (Cosmo peach)
- `tertiary`: #eec066 (Cosmo gold)
- `surface`: #F5F5F5
- `surfaceContainer`: #E0E0E0
- `surfaceContainerLow`: #F9F9F9
- `surfaceContainerLowest`: #FAFAFA
- `onSurface`: #212121
- `onSurfaceVariant`: #777777
- `onPrimary`: #FFFFFF
- `onPrimaryContainer`: #212121
- `background`: #FFFFFF
- `error`: #B00020
- `onError`: #FFFFFF
- `outline`: #B0B0B0
- `backgroundScaffold`: #FAFafa

**Typography:**
- Font families: `Playfair Display`, `Manrope`
- Sizes: display, headline, title, body, caption
- Weights: light, regular, medium, bold

**Spacing:** xs(4), sm(8), md(16), lg(24), xl(32), xxl(48), xxxl(64)

**Radius:** sm(8), md(12), lg(16), xl(24), full(9999)

**Shadows:** elevation 0-12, spread radius, blur radius

**Gradients:** primary → primaryContainer, secondary → tertiary blends

**Breakpoints:** mobile, tablet, desktop

---

## UI Component Library (`@cosmo/ui`)

### Atoms

#### `Button`
- **Variants**: primary, secondary, tertiary, ghost, link
- **Sizes**: sm, md, lg
- **States**: default, loading, disabled, focused
- **Props**: `onPress`, `variant`, `size`, `disabled`, `testID`, `style`
- **Usage**: Primary actions throughout app (Begin Journey, Save, Start Practice, Send Gift)
- **Accessibility**: Minimum 44px touch target, focus-visible style, ARIA label support

#### `Input`
- **Variants**: standard, outlined, filled
- **Props**: `label`, `value`, `onChangeText`, `secureTextEntry`, `keyboardType`, `placeholder`, `autoCapitalize`, `testID`
- **Usage**: Email, password, display name, search
- **Accessibility**: Proper labels, error message association, placeholder fallback

#### `Text`
- **Variants**: display, headlineLg, headlineMd, headlineSm, bodyLg, bodyMd, bodySm, caption, overline, label
- **Props**: `children`, `style`, `testID`
- **Usage**: All text content throughout app

#### `Icon`
- **Props**: `name`, `size`, `color`, `fill`, `weight` (for font icons), `strokeWidth`
- **Usage**: Microphone, play, pause, gift, timeline, settings icons
- **Accessaria**: alt text via `testID`, aria-label prop

#### `Badge`
- **Variants**: primary, secondary, tertiary, success, warning, tertiary
- **Sizes**: xs, sm, md
- **Props**: `variant`, `size`, `children`
- **Usage**: Premium indicators, practice levels, gift status

#### `Card`
- **Variants**: elevated, outlined, flat
- **Props**: `children`, `variant`, `style`
- **Usage**: Practice cards, journey items, gallery items

#### `TopNav`
- **Props**: `showScanFab`, `onScanPress`, `user`
- **Usage**: Top navigation bar with user avatar, scan FAB

#### `BottomNav`
- **Props**: `showScanFAB`, `onScanPress`, `currentRoute`
- **Usage**: Bottom navigation bar with scan FAB

#### `Fab`
- **Props**: `onPress`, `variant`, `icon`, `ariaLabel`
- **Usage**: Primary FAB for new scan from home

#### `Toggle`
- **Props**: `onToggle`, `value`, `children`
- **Usage**: Sign up / sign in toggle, feature flag toggles

#### `Divider`
- **Props**: `children`, `orientation`, `style`
- **Usage**: Section separators

#### `ProgressBar`
- **Props**: `variant`, `value`, `max`, `style`
- **Usage**: Recording progress, timer progress

#### `Toast`
- **Props**: `message`, `type` (success, error, info), `duration`
- **Usage**: User feedback for all actions

#### `Modal`
- **Props**: `visible`, `onClose`, `children`, `transparent`, `animated`
- **Usage**: Confirmation modals, settings sheets

#### `BottomSheet`
- **Props**: `visible`, `onClose`, `children`, `dragHandle`
- **Usage**: Onboarding steps, permission education, gift customization

#### `Skeleton`
- **Props**: `width`, `height`, `shape` (line, circle, pulse), `animation`
- **Usa

---
**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c10-tech-engineering-master-11k-component-map
node_type: reference
path: 07_SKILLS/amos-c10-tech-engineering-master/references/11k_component_map.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
