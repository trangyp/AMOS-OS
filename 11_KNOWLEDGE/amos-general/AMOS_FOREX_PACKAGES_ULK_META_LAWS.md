---
tags: [amos-general]
---
"""ULK meta‑law validator implementations.

Each validator receives the primitive inputs it needs and returns a simple ``bool``
indicating whether the hard‑gate passes.  The validators are deliberately pure –
they do **not** rely on external state so they are easy to unit‑test.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Sequence

# ---------------------------------------------------------------------------
# Helper contracts
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Contradiction:
    code: str
    left_claim: str
    right_claim: str
    severity: str  # e.g. "HARD", "CRITICAL", "WARNING"

# ---------------------------------------------------------------------------
# 1. L₀ – Consistency Law
# ---------------------------------------------------------------------------

def consistency_passed(contradictions: Sequence[Contradiction]) -> bool:
    """No *hard* contradictions are allowed.

    ``contradictions`` is a collection of ``Contradiction`` objects detected by the
    earlier reasoning layers.  If any item has a severity of ``HARD`` or
    ``CRITICAL`` the consistency check fails.
    """
    return not any(c.severity in {"HARD", "CRITICAL"} for c in contradictions)

# ---------------------------------------------------------------------------
# 2. L₂ – Duality Law / Rule of 2
# ---------------------------------------------------------------------------

def duality_passed(pairs: Sequence[tuple[str, str]]) -> bool:
    """Each actionable conclusion must involve a comparison of **two** sides.

    The function receives a list of ``(left, right)`` tuples; a missing or empty
    tuple is considered a failure.
    """
    return all(left and right for left, right in pairs)

# ---------------------------------------------------------------------------
# 3. L₄ – Quadrant Law / Rule of 4
# ---------------------------------------------------------------------------

def quadrant_passed(q1: Decimal, q2: Decimal, q3: Decimal, q4: Decimal, threshold: Decimal) -> bool:
    """All four quadrant scores must meet ``threshold``.

    ``q*`` values are normalised scores in ``[0, 1]``.  The function returns ``True``
    only when the *minimum* alignment meets the threshold – no averaging.
    """
    minimum = min(q1, q2, q3, q4)
    return minimum >= threshold

# ---------------------------------------------------------------------------
# 4. L∞ – Continuity Law
# ---------------------------------------------------------------------------

def continuity_passed(passed_stages: Sequence[str], required_order: Sequence[str]) -> bool:
    """Enforces that the pipeline stages appear **exactly** in the required order.

    ``passed_stages`` is the list of stage identifiers that have been completed for a
    particular trade candidate.  ``required_order`` is the canonical order (see the
    spec).  The function returns ``True`` only when ``passed_stages`` is a prefix of
    ``required_order`` with no gaps.
    """
    return required_order[: len(passed_stages)] == tuple(passed_stages)

# ---------------------------------------------------------------------------
# 5. Lᵢ – Identity Stability Law
# ---------------------------------------------------------------------------

def identity_stable(current_hash: str, previous_hash: str) -> bool:
    """Identity is stable when the two hashes match exactly.

    The hash is expected to be computed over the immutable fields that define a
    trade (instrument, direction, strategy version, etc.).
    """
    return current_hash == previous_hash

# ---------------------------------------------------------------------------
# 6. LΩ – Load–Capacity Law
# ---------------------------------------------------------------------------

def load_capacity_passed(load: Decimal, capacity: Decimal) -> bool:
    """Returns ``True`` when ``load`` does not exceed ``capacity``.
    """
    return load <= capacity

# ---------------------------------------------------------------------------
# 7. LΦ – Feedback Integrity Law
# ---------------------------------------------------------------------------

def feedback_integrity_passed(integrity_score: Decimal, minimum: Decimal) -> bool:
    """Simple threshold check for feedback integrity.
    """
    return integrity_score >= minimum

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
