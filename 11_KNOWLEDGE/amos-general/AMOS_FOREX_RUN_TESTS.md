---
title: AMOS FOREX RUN TESTS
tags: [amos-general, amos, general]
type: document
source: 11_KNOWLEDGE/amos-general
---




# AMOS forex__run_tests

```python
#!/usr/bin/env python3
"""Simple test harness for the newly added governance modules.
It runs a handful of assertions and exits with code 0 if all pass, otherwise
non‑zero.  This is a lightweight replacement for a full pytest suite.
"""
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


import sys
from decimal import Decimal
from datetime import datetime

# Import the packages – the repository root is in the PYTHONPATH when executed.
from packages.ulk.atoms import ULKAtomicState, atomic_state_valid
from packages.ulk.meta_laws import (
    consistency_passed,
    duality_passed,
    quadrant_passed,
    continuity_passed,
    identity_stable,
    load_capacity_passed,
    feedback_integrity_passed,
)
from packages.ulk.contracts import CanonPermission
from packages.murk.primitives import Primitive
from packages.murk.matrix import unresolved_interaction
from packages.murk.compiler import compile_interaction
from packages.ukr.state import UKRState, STAGE_ORDER
from packages.ukr.recursive_kernel import process_ukr


def test_ulk_atomic_state():
    state = ULKAtomicState(
        exists=True,
        difference=Decimal("0.1"),
        relations=("rel1",),
        boundary_id="EUR_USD",
        observed_at=datetime.utcnow().replace(tzinfo=datetime.utcnow().astimezone().tzinfo),
        load=Decimal("0.3"),
        capacity=Decimal("1.0"),
        feedback_quality=Decimal("0.9"),
    )
    assert atomic_state_valid(state)


def test_meta_laws():
    # consistency – empty list passes
    assert consistency_passed([])
    # duality – simple pair passes
    assert duality_passed([("bull", "bear")])
    # quadrant – all above threshold
    assert quadrant_passed(Decimal("0.8"), Decimal("0.9"), Decimal("0.85"), Decimal("0.86"), Decimal("0.75"))
    # continuity – full order passes
    assert continuity_passed(STAGE_ORDER, STAGE_ORDER)
    # identity – same hash passes
    assert identity_stable("hash", "hash")
    # load capacity – pass when load <= capacity
    assert load_capacity_passed(Decimal("0.5"), Decimal("1"))
    # feedback integrity – above minimum passes
    assert feedback_integrity_passed(Decimal("0.9"), Decimal("0.5"))


def test_murk_interaction():
    # defined rule – provide required evidence keys
    result = compile_interaction(
        Primitive.CAUSALITY,
        Primitive.TEMPORAL,
        evidence={"cause_timestamp": 1, "effect_timestamp": 2},
    )
    assert result.valid and result.permission == "ALLOW"

    # missing evidence
    result2 = compile_interaction(
        Primitive.CAUSALITY,
        Primitive.TEMPORAL,
        evidence={},
    )
    assert not result2.valid and result2.permission == "NO_TRADE"

    # undefined cell – should use unresolved_interaction
    result3 = compile_interaction(Primitive.EXISTENCE, Primitive.NULL_LOGIC)
    assert not result3.valid and result3.permission == "NO_TRADE"


def test_ukr_pipeline():
    state = UKRState(instrument="EUR_USD", timeframe="H1")
    permission = process_ukr(state)
    # permission should be a CanonPermission and approved should be True based on our stub data
    assert isinstance(permission, CanonPermission)
    assert permission.approved


def main():
    try:
        test_ulk_atomic_state()
        test_meta_laws()
        test_murk_interaction()
        test_ukr_pipeline()
    except AssertionError as e:
        print("Test failed:", e)
        sys.exit(1)
    print("All tests passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()


```

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
