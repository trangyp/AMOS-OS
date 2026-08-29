---
title: Vault Domain Knowledge — Amos Forex Os
type: reference
source: 07_SKILLS/amos-forex-os/references
tags:
- reference
- amos-forex-os
- canon/skill
- amos-forex-os-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- references-moc
- 07-skills-moc
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-forex-os`

## Vault-Sourced Content

### Source 1: AMOS forex__signal__ukr_engine

> Path: `engine/A/AMOS forex__signal__ukr_engine.md` | Size: 1147 chars | Match score: 13 | content_hash: c7d31bcdc9a57b71

// signal/ukr_engine.js
// Deterministic UKR‑engine placeholder – applies simple rule set on features.
// In a full implementation this would evaluate the ULK meta‑laws, MURK primitives
// and the 19×19 interaction matrix. Here we provide a deterministic example:
//   * If SMA20 > SMA50 and volatility < 0.0005 → BUY
//   * If SMA20 < SMA50 and volatility < 0.0005 → SELL
//   * Otherwise → NO ACTION

const EventBus = require('../event_bus');

class UKREngine {
  evaluate({ instrument, time, features }) {
    const { sma20, sma50, volatility } = features;
    if (sma20 && sma50 && volatility !== null) {
      if (sma20 > sma50 && volatility < 0.0005) {
        return { instrument, time, side: 'BUY', reason: 'sma20> sma50 low vol' };
      }
      if (sma20 < sma50 && volatility < 0.0005) {
        return { instrument, time, side: 'SELL', reason: 'sma20< sma50 low vol' };
      }
    }
    return null; // no signal
  }
}

module.exports = new UKREngine();

---

---

### Source 2: AMOS forex__packages__ukr__recursive_kernel

> Path: `kernel/A/AMOS forex__packages__ukr__recursive_kernel.md` | Size: 9604 chars | Match score: 10 | content_hash: d36a271a4bce8b82

"""UKR recursive kernel – orchestrates the 17-stage pipeline.

The public function is ``process_ukr`` which receives a ``UKRState`` instance and
returns an updated ``UKRState`` together with a ``CanonPermission`` (imported
from ``ulk.contracts``).  The implementation follows the strict ordering defined
by ``STAGE_ORDER`` and applies the ULK meta‑law validators at the appropriate
points.  For brevity only a subset of stages perform non‑trivial calculations –
the rest simply record success and move on.
"""

from __future__ import annotations

from decimal import Decimal
from typing import List

from ..ulk.meta_laws import (
    consistency_passed,
    duality_passed,
    quadrant_passed,
    continuity_passed,
    identity_stable,
    load_capacity_passed,
    feedback_integrity_passed,
)
from ..ulk.contracts import CanonPermission, ValidatorResult
from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission
from ..ulk.contracts import ValidatorResult

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from ..ulk.contracts import ValidatorResult
from ..ulk.contracts import CanonPermission

from .

---

### Source 3: AMOS forex__run_tests

> Path: `amos-general/A/forex/AMOS forex__run_tests.md` | Size: 3736 chars | Match score: 10 | content_hash: 04c7b3df236b5588

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
    state = UKRState(instrument="EUR_USD"

---
**MOC:** 

## Related

- 
```

---

**Related:** [[amos-forex-os_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-forex-os-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-forex-os/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
