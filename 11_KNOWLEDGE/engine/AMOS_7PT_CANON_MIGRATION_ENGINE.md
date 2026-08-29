---
title: AMOS 7PT CANON MIGRATION ENGINE
tags:
- engine
- processing
- runtime
- canon/knowledge
- canon
- trang-framework-recursive-ontology-dynamics
type: document
source: 11_KNOWLEDGE/engine
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: engine_specification
---

# AMOS 7PT CANON MIGRATION ENGINE

"""
AMOS 7PT Canon Migration Engine
================================

Purpose
-------
Deterministically repair the seven 7PT canon notes while preserving existing
part-specific analysis and enforcing the canonical seven-question structure.

Transformation classes
----------------------
1. FLOW + ENFORCEMENT
   Ensure literal links exist for:
   - 2026-08-22 7-Part Universe Canon.md
   - 7PT_Complete_Canon_Audit_Reaudit.md

2. CONSTRAINT + STRUCTURE + TIME + ADAPTATION + TERMINATION
   Replace the legacy five-question "Canonical test" with the canonical
   seven-question test.

3. Preserve the legacy five-question material as:
       ## <Part>-specific analysis

4. Make the transformation deterministic and idempotent:
       patch(patch(x)) == patch(x)

AMOS status
-----------
MODEL / deterministic migration utility.

This script edits canon artifacts. It does NOT by itself prove that the
resulting content is canonical, empirically valid, or admitted into the
active AMOS runtime.

Authority boundary
------------------
Filesystem mutation is an execution effect. In a governed AMOS deployment,
the patch result should be treated as a candidate artifact until validation,
provenance checks, authority checks, and commit admission succeed.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Final


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

VAULT: Final = Path(
    "/Users/mac/Downloads/stitch_project_cosmo/_00_Cosmo brain/md"
)

HOME_FILENAME: Final = "2026-08-22 7-Part Universe Canon.md"
REAUDIT_FILENAME: Final = "7PT_Complete_Canon_Audit_Reaudit.md"

PARTS: Final = (
    "CONSTRAINT",
    "FLOW",
    "STRUCTURE",
    "ENFORCEMENT",
    "TIME",
    "ADAPTATION",
    "TERMINATION",
)

PART_DISPLAY: Final = {
    "CONSTRAINT": "Constraint",
    "FLOW": "Flow",
    "STRUCTURE": "Structure",
    "ENFORCEMENT": "Enforcement",
    "TIME": "Time",
    "ADAPTATION": "Adaptation",
    "TERMINATION": "Termination",
}

CANONICAL_QUESTIONS: Final = (
    "Where are the constraints?",
    "What is the flow?",
    "What structure stabilizes it?",
    "How is it enforced?",
    "How does time stress it?",
    "How does it adapt without drift?",
    "What are its termination conditions?",
)

PART_OWNED_QUESTION: Final = {
    "CONSTRAINT": 0,
    "FLOW": 1,
    "STRUCTURE": 2,
    "ENFORCEMENT": 3,
    "TIME": 4,
    "ADAPTATION": 5,
    "TERMINATION": 6,
}

# Critical inverse mapping.
# The original implementation did not do this correctly.
QUESTION_OWNER: Final = {
    question_index: part
    for part, question_index in PART_OWNED_QUESTION.items()
}


# ---------------------------------------------------------------------------
# Typed result state
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PatchResult:
    path: Path
    changed: bool
    reason: str


# ---------------------------------------------------------------------------
# Canonical source text
# ---------------------------------------------------------------------------

OWNED_ANSWERS: Final = {
    "CONSTRAINT":
        "Constraint IS the definition of constraints: scarcity, boundaries, "
        "non-infinite capacity, and irreversibility — the existence of limits "
        "that make a system possible rather than noise. Without constraint, "
        "there is no system — only noise.",

    "FLOW":
        "Flow IS constrained throughput across a system: input → "
        "transformation → output, with bottlenecks, leakage, and queues as "
        "first-class properties. Power exists only while it is moving.",

    "STRUCTURE":
        "Structure IS the arrangement that stabilizes flow — architecture, "
        "hierarchy, interfaces, and load-bearing elements that make flow "
        "repeatable rather than dissipating. Flow without structure "
        "dissipates; structure without flow decays.",

    "ENFORCEMENT":
        "Enforcement IS the mechanism that prevents deviation from structure "
        "— mechanical correction, not morality. Rule consistency, boundary "
        "correction, deviation cost, and predictability. Unenforced structure "
        "is not structure.",

    "TIME":
        "Time IS irreversible sequencing under constraint — the dimension in "
        "which structure accumulates stress, assumptions are exposed, and "
        "systems move without the ability to return to the exact prior state. "
        "Time exposes all unenforced assumptions.",

    "ADAPTATION":
        "Adaptation IS bounded change under pressure — adjustment, learning, "
        "and reconfiguration that preserve the invariants defining what the "
        "system IS. Adaptation at the core destroys identity; adaptation at "
        "the edge preserves survival.",

    "TERMINATION":
        "Termination IS the resolution of accumulated deviation — the point "
        "at which a system's correction capacity is exceeded and it trends "
        "toward collapse, stabilization, extinction, or reconstitution. "
        "Systems do not fail randomly; they terminate when correction "
        "capacity is exceeded.",
}


SHARPEN: Final = {
    "CONSTRAINT": {
        1: "Flow is constrained throughput; without constraint, flow is unbounded noise.",
        2: "Structure requires constraints to remain bounded.",
        3: "Enforcement operates inside finite constraints.",
        4: "Time converts finite capacity into accumulated stress.",
        5: "Constraint defines the invariants adaptation must preserve.",
        6: "Termination becomes meaningful because capacity is finite.",
    },

    "FLOW": {
        0: "Constraint bounds throughput.",
        2: "Structure stabilizes flow into repeatable form.",
        3: "Enforcement protects flow against leakage and drift.",
        4: "Sustained flow accumulates temporal stress.",
        5: "Adaptation keeps flow viable under changing conditions.",
        6: "Loss of recoverable throughput can become a termination pathway.",
    },

    "STRUCTURE": {
        0: "Constraint bounds the architecture.",
        1: "Flow is what the structure stabilizes.",
        3: "Enforcement protects structural invariants.",
        4: "Time exposes structural fatigue.",
        5: "Adaptation changes structure while preserving load-bearing identity.",
        6: "Structural failure becomes terminal when correction capacity is exceeded.",
    },

    "ENFORCEMENT": {
        0: "Constraints define what enforcement must preserve.",
        1: "Enforcement prevents throughput from degrading through uncontrolled deviation.",
        2: "Structure defines the state enforcement protects.",
        4: "Time exposes assumptions that were never actually enforced.",
        5: "Adaptation creates candidate changes that enforcement must bound.",
        6: "Persistent enforcement failure can push the system beyond recovery.",
    },

    "TIME": {
        0: "Finite constraints make temporal accumulation consequential.",
        1: "Flow under sustained time accumulates stress, queues, and leakage.",
        2: "Structure experiences fatigue through time.",
        3: "Enforcement must remain fresh as conditions change.",
        5: "Adaptation must respond to temporal change without losing invariants.",
        6: "Termination can result from deviation accumulated faster than it can be repaired.",
    },

    "ADAPTATION": {
        0: "Constraints bound the space of valid adaptation.",
        1: "Flow supplies changing operating conditions to which the system responds.",
        2: "Structure determines what can change and what remains load-bearing.",
        3: "Enforcement prevents adaptation from becoming uncontrolled drift.",
        4: "Time supplies the changing regime across which adaptation is tested.",
        6: "Termination becomes possible when valid adaptation can no longer restore viability.",
    },

    "TERMINATION": {
        0: "Finite capacity creates a meaningful exhaustion boundary.",
        1: "Loss of recoverable flow can drive termination.",
        2: "Collapse of load-bearing structure can make recovery impossible.",
        3: "Enforcement failure allows deviation to accumulate.",
        4: "Time accumulates unresolved deviation.",
        5: "Adaptation determines whether the system can return to a viable basin.",
    },
}


PART_SPECIFIC_CONTENT: Final = {
    "CONSTRAINT": """## Constraint-specific analysis

For any system, answer:

1. **What is scarce?**
2. **What are the boundaries?**
3. **What is the non-infinite capacity?**
4. **What is irreversible?**
5. **What happens without constraint?**

Failure to answer all five = the system's existence is structurally undefined.""",

    "STRUCTURE": """## Structure-specific analysis

For any system, answer:

1. **What is the architecture?**
2. **What is the hierarchy?**
3. **What are the interfaces?**
4. **What are the load-bearing elements?**
5. **Does structure have flow?**

Failure to answer all five = the system's structure is undefined.""",

    "TIME": """## Time-specific analysis

For any system, answer:

1. **What is the direction of time?**
2. **What accumulates over time?**
3. **What is the delay?**
4. **What is exposed by time?**
5. **What is the fatigue point?**

Failure to answer all five = the system's temporal dimension is undefined.""",

    "ADAPTATION": """## Adaptation-specific analysis

For any system, answer:

1. **What is the pressure?**
2. **What are the invariants?**
3. **What is the feedback?**
4. **Where is the adaptation happening?**
5. **Is the adaptation bounded?**

Failure to answer all five = the system's adaptation is undefined.""",

    "TERMINATION": """## Termination-specific analysis

For any system, answer:

1. **What is the correction capacity?**
2. **What is the accumulated deviation?**
3. **What is the threshold?**
4. **What is the recovery basin?**
5. **What is the irreversibility zone?**

Failure to answer all five = the system's termination is undefined.""",
}


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_configuration() -> None:
    """Fail closed if the static architecture is internally inconsistent."""

    if len(PARTS) != 7:
        raise RuntimeError("7PT invariant violated: expected exactly seven parts.")

    if set(PARTS) != set(PART_DISPLAY):
        raise RuntimeError("PART_DISPLAY does not cover exactly the seven parts.")

    if set(PARTS) != set(PART_OWNED_QUESTION):
        raise RuntimeError(
            "PART_OWNED_QUESTION does not cover exactly the seven parts."
        )

    if set(PART_OWNED_QUESTION.values()) != set(range(7)):
        raise RuntimeError(
            "Each canonical question must have exactly one owning part."
        )

    if len(CANONICAL_QUESTIONS) != 7:
        raise RuntimeError("Expected exactly seven canonical questions.")


# ---------------------------------------------------------------------------
# Canonical rendering
# ---------------------------------------------------------------------------

def question_owner(index: int) -> str:
    try:
        return QUESTION_OWNER[index]
    except KeyError as exc:
        raise ValueError(f"Invalid canonical question index: {index}") from exc


def owned_answer(part: str) -> str:
    try:
        return OWNED_ANSWERS[part]
    except KeyError as exc:
        raise ValueError(f"Missing owned answer for {part}") from exc


def sharpen_answer(part: str, index: int) -> str:
    try:
        return SHARPEN[part][index]
    except KeyError as exc:
        raise ValueError(
            f"Missing sharpen answer for part={part}, question={index}"
        ) from exc


def build_7q_canonical_test(part: str) -> str:
    display = PART_DISPLAY[part]
    owned_index = PART_OWNED_QUESTION[part]

    lines = [
        f"## Canonical test ({display.lower()}-specific)",
        "",
        "For any system, answer all seven canonical questions:",
        "",
    ]

    for index, question in enumerate(CANONICAL_QUESTIONS):
        if index == owned_index:
            lines.append(
                f"{index + 1}. **{question}** — **PASS.** "
                f"{owned_answer(part)}"
            )
        else:
            owner = question_owner(index)

            lines.append(
                f"{index + 1}. **{question}** — **△ SHARPEN.** "
                f"{sharpen_answer(part, index)} "
                f"See `7PT_{owner}_CANON.md`."
            )

        lines.append("")

    lines.append(
        "Failure to answer all seven = structural invalidity."
    )

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Section manipulation
# ---------------------------------------------------------------------------

def section_bounds(text: str, heading: str) -> tuple[int, int]:
    """Return [start, end) for a level-2 Markdown section."""

    pattern = re.compile(
        rf"(?m)^{re.escape(heading)}\s*\$"
    )

    match = pattern.search(text)

    if match is None:
        raise ValueError(f"Section heading not found: {heading}")

    start = match.start()

    next_heading = re.search(
        r"(?m)^##\s+",
        text[match.end():],
    )

    if next_heading is None:
        return start, len(text)

    end = match.end() + next_heading.start()

    return start, end


def replace_section(
    text: str,
    heading: str,
    replacement: str,
) -> str:
    start, end = section_bounds(text, heading)

    prefix = text[:start].rstrip()
    suffix = text[end:].lstrip("\n")

    result = prefix + "\n\n" + replacement.rstrip() + "\n"

    if suffix:
        result += "\n" + suffix

    return result


# ---------------------------------------------------------------------------
# Cross-link patching
# ---------------------------------------------------------------------------

def ensure_linked_vault_items(text: str) -> str:
    heading = "## Linked vault items"

    start, end = section_bounds(text, heading)
    section = text[start:end]

    required_lines = (
        f"- `{HOME_FILENAME}` — 7-part canon home note",
        f"- `{REAUDIT_FILENAME}` — re-audit confirming this canon part "
        "is structurally coherent",
    )

    missing = [
        line
        for line in required_lines
        if line not in section
    ]

    if not missing:
        return text

    heading_end = section.find("\n")

    if heading_end == -1:
        patched_section = (
            section.rstrip()
            + "\n\n"
            + "\n".join(missing)
            + "\n"
        )
    else:
        patched_section = (
            section[:heading_end + 1]
            + "\n".join(missing)
            + "\n"
            + section[heading_end + 1:]
        )

    return text[:start] + patched_section + text[end:]


# ---------------------------------------------------------------------------
# Part-specific patch
# ---------------------------------------------------------------------------

def patch_canonical_test(text: str, part: str) -> str:
    heading = (
        f"## Canonical test ({PART_DISPLAY[part].lower()}-specific)"
    )

    canonical = build_7q_canonical_test(part)
    analysis = PART_SPECIFIC_CONTENT[part]

    replacement = canonical + "\n\n" + analysis

    return replace_section(
        text=text,
        heading=heading,
        replacement=replacement,
    )


# ---------------------------------------------------------------------------
# File mutation
# ---------------------------------------------------------------------------

def write_if_changed(path: Path, new_text: str) -> PatchResult:
    old_text = path.read_text(encoding="utf-8")

    if new_text == old_text:
        return PatchResult(
            path=path,
            changed=False,
            reason="already compliant",
        )

    path.write_text(new_text, encoding="utf-8")

    return PatchResult(
        path=path,
        changed=True,
        reason="patched",
    )


def patch_crosslinks(path: Path) -> PatchResult:
    old = path.read_text(encoding="utf-8")
    new = ensure_linked_vault_items(old)

    return write_if_changed(path, new)


def patch_part(path: Path, part: str) -> PatchResult:
    old = path.read_text(encoding="utf-8")
    new = patch_canonical_test(old, part)

    return write_if_changed(path, new)


# ---------------------------------------------------------------------------
# Postcondition validation
# ---------------------------------------------------------------------------

def validate_note(path: Path, part: str) -> None:
    text = path.read_text(encoding="utf-8")

    if part in {"FLOW", "ENFORCEMENT"}:
        if HOME_FILENAME not in text:
            raise RuntimeError(
                f"{path.name}: missing home canon cross-link."
            )

        if REAUDIT_FILENAME not in text:
            raise RuntimeError(
                f"{path.name}: missing re-audit cross-link."
            )

    if part in PART_SPECIFIC_CONTENT:
        heading = (
            f"## Canonical test "
            f"({PART_DISPLAY[part].lower()}-specific)"
        )

        start, end = section_bounds(text, heading)
        canonical_section = text[start:end]

        for question in CANONICAL_QUESTIONS:
            if question not in canonical_section:
                raise RuntimeError(
                    f"{path.name}: canonical question missing: "
                    f"{question}"
                )

        analysis_heading = (
            f"## {PART_DISPLAY[part]}-specific analysis"
        )

        if analysis_heading not in text:
            raise RuntimeError(
                f"{path.name}: missing preserved analysis section."
            )


# ---------------------------------------------------------------------------
# Idempotency validation
# ---------------------------------------------------------------------------

def validate_idempotency(path: Path, part: str) -> None:
    """
    Validate the transformation in memory without performing a second write.

    Required invariant:
        T(T(x)) == T(x)
    """

    once = path.read_text(encoding="utf-8")

    if part in {"FLOW", "ENFORCEMENT"}:
        twice = ensure_linked_vault_items(once)
    else:
        twice = patch_canonical_test(once, part)

    if twice != once:
        raise RuntimeError(
            f"{path.name}: patch is not idempotent."
        )


# ---------------------------------------------------------------------------
# Transaction-style orchestrator
# ---------------------------------------------------------------------------

def patch_all() -> list[PatchResult]:
    validate_configuration()

    missing = [
        VAULT / f"7PT_{part}_CANON.md"
        for part in PARTS
        if not (VAULT / f"7PT_{part}_CANON.md").exists()
    ]

    if missing:
        names = ", ".join(path.name for path in missing)

        raise FileNotFoundError(
            "Fail-closed: required canon notes are missing: "
            + names
        )

    results: list[PatchResult] = []

    for part in PARTS:
        path = VAULT / f"7PT_{part}_CANON.md"

        if part in {"FLOW", "ENFORCEMENT"}:
            result = patch_crosslinks(path)
        else:
            result = patch_part(path, part)

        results.append(result)

        validate_note(path, part)
        validate_idempotency(path, part)

    return results


def main() -> int:
    results = patch_all()

    changed = [r.path.name for r in results if r.changed]
    unchanged = [r.path.name for r in results if not r.changed]

    print("AMOS 7PT canon migration complete.")
    print(f"Changed: {len(changed)}")

    for name in changed:
        print(f"  PATCHED  {name}")

    print(f"Already compliant: {len(unchanged)}")

    for name in unchanged:
        print(f"  PASS     {name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### What was actually wrong

The most important bug is `_other_part_for_question()`. In the supplied version:

```python
for part, owned in PART_OWNED_QUESTION.items():
    if owned != idx:
        return part
```

That does **not** answer “which part owns this question?” It returns the first part that *doesn't* own it. So a Flow question can point to Constraint, a Structure question can also point to Constraint, etc. The correct mapping is the inverse:

```python
QUESTION_OWNER = {
    question_index: part
    for part, question_index in PART_OWNED_QUESTION.items()
}
```

and then:

```python
owner = QUESTION_OWNER[idx]
```

There is also a hard runtime bug: `_patch_part_specific_canonical_test()` calls `re.search()`, but `re` is imported only locally inside `_patch_all()`. A local import does not populate the module global namespace used by another function. The fixed version imports `re` at module scope.

The undefined `display` fallbacks are another latent failure:

```python
return answers[part].get(idx, f"{display} ...")
```

and:

```python
return sharpen_map[part].get(idx, f"{display} ...")
```

Even if those paths “should never happen,” validator/migration code should fail closed rather than carry broken fallback paths. The rewritten implementation raises an explicit `ValueError`.

### AMOS architectural correction

The deeper improvement is to stop treating this as a loose text-replacement script. It is a **canon-state migration**:

[
C_t
\xrightarrow{;T_{7PT};}
C_{t+1}
]

with invariants:

[
\boxed{
I =
I_{7Questions}
\land
I_{Ownership}
\land
I_{Preservation}
\land
I_{CrossLinks}
\land
I_{Idempotency}
}
]

The crucial deterministic invariant is:

[
\boxed{T(T(C))=T(C)}
]

Running the repair twice must produce exactly the same state as running it once.

The second invariant is ownership:

[
Owner(q_i)=p_i
]

with the bijection:

```text
Q1 → CONSTRAINT
Q2 → FLOW
Q3 → STRUCTURE
Q4 → ENFORCEMENT
Q5 → TIME
Q6 → ADAPTATION
Q7 → TERMINATION
```

The third is preservation:

[
CanonicalUpgrade
\neq
LegacyKnowledgeDeletion
]

The five-question analysis is therefore **demoted from canonical-test status but preserved as part-specific analysis**.

And the AMOS authority boundary should be explicit:

```text
source note
    ↓
deterministic transform
    ↓
candidate patched note
    ↓
structural validator
    ↓
idempotency validator
    ↓
canon admission / authority gate
    ↓
committed canon
```

A successful Python execution proves only that the transformation executed and its programmed postconditions passed. It does **not** prove that the resulting note has automatically become authoritative AMOS canon. That distinction is consistent with AMOS infrastructure rules: configuration/canon artifacts are candidate control-plane inputs until provenance, semantic validation, authority, compatibility, and commit requirements are satisfied.

**Conclusion class: DERIVED for the code defects; MODEL for the strengthened AMOS migration architecture.** The strongest next improvement would be adding atomic staging/rollback and hashing all seven source/output notes so the migration becomes a provenance-bound transaction rather than seven independent filesystem writes.
```

---
**Links:** [[ENGINE_MOC]] | [[KNOWLEDGE_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---

**MOC:** [[KERNEL_MOC]] · [[00_HOME]]
