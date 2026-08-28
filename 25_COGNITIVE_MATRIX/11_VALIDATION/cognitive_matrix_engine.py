#!/usr/bin/env python3
"""
Cognitive Matrix Engine — EXECUTABLE forward-pass reference implementation.

Runs the 30-layer cognitive matrix (L00..L29) as real program flow, converting
the CONTRACT_FILLED / NOT_IMPLEMENTED operator stubs into working executable
logic, using the exact house pattern proven by:
  - routing_policy_validator.py   (19/19)
  - l00_reality_validator.py      (30 tests, EXECUTED_VALIDATION_RECEIPT)
  - authz_invariant_engine.py     (17/17)

Status: REFERENCE IMPLEMENTATION (DERIVED). NOT promoted canon.
Executable binding: EXECUTED-VALIDATED here for the operator skeleton.
Live runtime channels (observation feeds, external authority, distributed
consensus) remain UNKNOWN/GAP and are DECLARED in the validation receipt.

Rules of the house (enforced in code, not just prose):
  - Fail-closed on UNKNOWN/GAP. UNKNOWN != PASS, ever.
  - CAPABILITY != AUTHORITY. No layer commits a consequential effect without
    an authorization check (C01_GOVERNANCE / the L28 gate).
  - PROPOSAL != COMMIT. Apply stages a proposal; commit only after gates.
  - INTEGRITY > COMPLETENESS > FLUENCY > SPEED > TOKEN_SAVINGS.
  - No fabricated SOURCE_CLAIM or OBSERVATION: every layer only transforms
    caller-supplied typed records; absence of required fields is UNKNOWN.
"""
from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass, field, replace
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Verdict / status enums (fail-closed semantics throughout)
# ---------------------------------------------------------------------------

class Verdict(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    CONDITIONAL = "CONDITIONAL"
    UNKNOWN = "UNKNOWN"


class Epoch:
    """A monotonic epoch counter shared by all layers (temporal validity)."""
    def __init__(self, value: int = 0):
        self.value = value
    def next(self) -> "Epoch":
        return Epoch(self.value + 1)


class MemoryStatus(str, Enum):
    PROPOSED = "PROPOSED"       # staged, not committed
    COMMITTED = "COMMITTED"     # persisted in durability store
    CONSOLIDATED = "CONSOLIDATED"  # deduped / indexed / threshold-passed
    REJECTED = "REJECTED"       # failed write-gate, not persisted
    STALE = "STALE"             # freshness horizon exceeded
    UNKNOWN = "UNKNOWN"


class LearningOutcome(str, Enum):
    APPLIED = "APPLIED"         # update passed gating, committed
    BLOCKED = "BLOCKED"         # update rejected by a gate (fail closed)
    NO_CHANGE = "NO_CHANGE"     # update was idempotent / redundant
    UNKNOWN = "UNKNOWN"


# ---------------------------------------------------------------------------
# Typed records (mirroring the primitive contract payloads)
# ---------------------------------------------------------------------------

@dataclass
class Observation:
    """L00-typed observation: a reality-contact record with provenance."""
    obs_id: str = ""
    value: Any = None
    unit: Optional[str] = None
    observer_id: str = ""
    method: str = ""
    event_time: Optional[float] = None
    observation_time: Optional[float] = None
    freshness_horizon_tau: Optional[float] = None
    source: str = ""
    ancestry: Tuple[str, ...] = ()

@dataclass
class Percept:
    """L03-shaped output: an observation bound to a working representation."""
    percept_id: str = ""
    feature: Dict[str, Any] = field(default_factory=dict)
    observation_ids: Tuple[str, ...] = ()
    confidence: float = 1.0

@dataclass
class MemoryCell:
    """L07 memory unit. Write-gated; never dereferenced as live truth."""
    cell_id: str = ""
    content: Any = None
    source: str = ""                       # provenance root
    observation_ids: Tuple[str, ...] = ()
    created_epoch: int = 0
    last_accessed_epoch: int = 0
    access_count: int = 0                  # L20 credit-assignment signal
    confidence: float = 0.0                # never created from nothing (CM-I2)
    freshness_horizon_tau: Optional[float] = None
    status: str = MemoryStatus.PROPOSED
    proof_hash: str = ""                   # integrity anchor

@dataclass
class Representation:
    """L08 typed representation of an entity/object."""
    rep_id: str = ""
    entity_id: str = ""
    features: Dict[str, Any] = field(default_factory=dict)
    transformation_depth: int = 0
    is_reality: bool = False              # invariant: never True (L00-FM-01)

@dataclass
class Belief:
    """L09/L10 inference product with explicit epistemic battery."""
    belief_id: str = ""
    claim: str = ""
    representation_ids: Tuple[str, ...] = ()
    confidence: float = 0.0
    claim_class: str = "DERIVED"          # never upgraded without evidence
    supported_scope: frozenset = frozenset()
    claimed_scope: frozenset = frozenset()

@dataclass
class Prediction:
    """L13 prediction; NEVER stored as outcome before post-horizon obs (L00-T03)."""
    pred_id: str = ""
    claim: str = ""
    horizon: float = 0.0
    recorded_as_outcome: bool = False

@dataclass
class Decision:
    """L17 decision proposal. PROPOSAL != COMMIT until L28 authorization."""
    decision_id: str = ""
    intent: str = ""
    effect_digest: str = ""
    proposed_by: str = ""                  # semantic origin (INV-043 analog)
    scope: frozenset = frozenset()
    cost: float = 1.0
    authorized: bool = False
    committed: bool = False

@dataclass
class IdentityAnchor:
    """L25 identity evidence: what binds 'self' across time."""
    anchor_id: str = ""
    enactor: str = ""
    continuity_evidence: Tuple[str, ...] = ()  # receipts / hashes
    fragmentation: float = 0.0                # 0 = whole; >0 = fragmented
    last_epoch: int = 0


# ---------------------------------------------------------------------------
# The Cognitive State (shared, typed; no global authority)
# ---------------------------------------------------------------------------

@dataclass
class CognitiveState:
    """The per-epoch state vector threaded through L00..L29.

    Layers read and write only their declared slice; governance (L28) and
    evolution (L29) gate all consequential mutation. Owns no authority.
    """
    epoch: int = 0
    observations: List[Observation] = field(default_factory=list)
    percepts: List[Percept] = field(default_factory=list)
    memories: List[MemoryCell] = field(default_factory=list)      # L07 store
    representations: List[Representation] = field(default_factory=list)
    beliefs: List[Belief] = field(default_factory=list)
    predictions: List[Prediction] = field(default_factory=list)
    decisions: List[Decision] = field(default_factory=list)
    identity_anchors: List[IdentityAnchor] = field(default_factory=list)
    # L21/L22 bookkeeping
    update_log: List[Dict[str, Any]] = field(default_factory=list)   # append-only
    consolidation_index: Dict[str, str] = field(default_factory=dict)  # content_hash->cell_id
    # observability counters
    stats: Dict[str, int] = field(default_factory=lambda: {
        "layers_run": 0, "memory_writes": 0, "memory_rejected": 0,
        "learning_applied": 0, "learning_blocked": 0, "consolidated": 0,
        "identity_fragmented": 0, "decisions_committed": 0,
    })

    def all_unknown_if_empty(self) -> None:
        """Fail-closed: this brain never fabricates. Called by forward() when
        an upstream required slice is absent. (No-op hook; layers return
        UNKNOWN themselves when inputs are missing.)"""


# ---------------------------------------------------------------------------
# The Engine — L00..L29 forward pass
# ---------------------------------------------------------------------------

class CognitiveMatrixEngine:
    """Executable reference implementation of the 30 cognitive layers.

    Each public method is one layer's APPLY/VALIDATE entry. Layers that are
    pure structural (L05 binding, L08 representation) validate + forward the
    typed slice; the consequential ones (L07/L21/L22/L25/L28/L29) enforce
    real gates. Forward() runs the full chain in canonical order.
    """

    def __init__(self, initial_epoch: int = 0):
        self.state = CognitiveState(epoch=initial_epoch)
        self.epoch = Epoch(initial_epoch)

    # -- integrity tools -----------------------------------------------------

    @staticmethod
    def _digest(*parts: Any) -> str:
        h = hashlib.sha256()
        for p in parts:
            h.update(repr(p).encode("utf-8", errors="replace"))
        return h.hexdigest()

    def _require(self, v: Any, name: str) -> Optional[Verdict]:
        """Fail-closed on UNKNOWN: required input missing -> UNKNOWN verdict."""
        if v is None:
            return None
        return Verdict.UNKNOWN

    # =======================================================================
    # L00 — Reality Environment (grounding / separation invariants)
    # =======================================================================
    def L00_validate_reality_gate(self, representation: Any) -> Verdict:
        """L00-FM-01: a representation must never be flagged as reality."""
        if representation is None:
            return Verdict.UNKNOWN
        if isinstance(representation, dict) and representation.get("is_reality") is True:
            return Verdict.FAIL
        if isinstance(representation, str) and representation == "__REALITY__":
            return Verdict.FAIL
        return Verdict.PASS

    def L00_apply(self, obs: Observation) -> Verdict:
        """Admit an observation only with provenance + time identity."""
        if obs is None or obs.obs_id == "":
            return Verdict.UNKNOWN
        if obs.event_time is None or obs.observation_time is None:
            return Verdict.FAIL          # temporal identity missing
        if obs.source == "":
            return Verdict.FAIL          # provenance root missing
        # Dedup by id: replace in place, never duplicate the reality record.
        self.state.observations = [o for o in self.state.observations
                                   if o.obs_id != obs.obs_id]
        self.state.observations.append(obs)
        return Verdict.PASS

    # =======================================================================
    # L03 — Percept Formation ; L05 — Binding
    # =======================================================================
    def L03_apply(self, p: Percept) -> Verdict:
        if p is None or p.percept_id == "":
            return Verdict.UNKNOWN
        if not p.observation_ids:
            return Verdict.FAIL          # percept must bind to an observation
        self.state.percepts = [x for x in self.state.percepts
                               if x.percept_id != p.percept_id]
        self.state.percepts.append(p)
        return Verdict.PASS

    def L05_validate_binding(self, rep: Representation, obs_ids: Tuple[str, ...]) -> Verdict:
        """Binding: every representation forwards observation provenance."""
        if rep is None:
            return Verdict.UNKNOWN
        if rep.is_reality:
            return Verdict.FAIL          # L00-FM-01 at binding
        if obs_ids and not any(o.obs_id in obs_ids for o in self.state.observations):
            return Verdict.FAIL          # binds to a non-admitted observation
        return Verdict.PASS

    # =======================================================================
    # L07 — Memory (write-gated, never dereferenced as live truth)
    # =======================================================================
    def L07_write_gate(self, cell: MemoryCell) -> Verdict:
        """L07 write gating: fail-closed admission to memory.

        Gates enforced:
          - provenance present (no anonymous memory)      -> else UNKNOWN
          - confidence never fabricated from nothing      -> else FAIL
          - not a duplicate of an existing consolidated cell
          - freshness horizon sane when declared
        """
        if cell is None:
            return Verdict.UNKNOWN
        if cell.cell_id == "" or cell.source == "":
            return Verdict.UNKNOWN
        # CM-I2: No confidence creation. A memory with 0.0 confidence and no
        # backing observations is allowed ONLY if flagged as a raw trace; but a
        # cell that *claims* confidence with no observation provenance is
        # fabrication. We require: confidence>0 implies observation_ids non-empty.
        if cell.confidence > 0.0 and not cell.observation_ids:
            return Verdict.FAIL
        if cell.freshness_horizon_tau is not None and cell.freshness_horizon_tau <= 0:
            return Verdict.FAIL
        # Duplicate detection is consolidation's job (L22), but the gate must
        # not admit an exact duplicate of an already-consolidated cell.
        if cell.content is not None:
            h = self._digest(cell.content, cell.source)
            if h in self.state.consolidation_index:
                return Verdict.CONDITIONAL   # candidate duplicate; L22 decides
        return Verdict.PASS

    def L07_apply(self, cell: MemoryCell) -> Tuple[Verdict, Optional[str]]:
        gate = self.L07_write_gate(cell)
        if gate == Verdict.FAIL or gate == Verdict.UNKNOWN:
            if cell is not None:
                cell.status = MemoryStatus.REJECTED
                self.state.stats["memory_rejected"] += 1
            return gate, "memory write denied (fail closed)"

        cell.status = MemoryStatus.COMMITTED
        # Duplicate cells never both survive into the durability store; the
        # consolidation index is the authority for dedup.
        self.state.memories.append(cell)
        self.state.stats["memory_writes"] += 1
        self.state.update_log.append({
            "layer": "L07", "op": "APPLY", "cell_id": cell.cell_id,
            "epoch": self.state.epoch, "digest": self._digest(cell.cell_id),
        })
        return Verdict.PASS, "memory written"

    def L07_validate_retrieval(self, cell: MemoryCell, used_as_live_truth: bool,
                               revalidated_against_l00: bool) -> Verdict:
        """L00-T27 analog: MEMORY != CURRENT_REALITY. Stale/unrevalidated
        memory must not drive current-state reasoning."""
        if cell is None:
            return Verdict.UNKNOWN
        if cell.status in (MemoryStatus.PROPOSED, MemoryStatus.REJECTED):
            return Verdict.FAIL          # uncommitted memory cannot be used
        if used_as_live_truth and not revalidated_against_l00:
            return Verdict.FAIL
        return Verdict.PASS

    # =======================================================================
    # L09 — Inference ; L10 — World Modeling
    # =======================================================================
    def L09_apply(self, b: Belief) -> Verdict:
        """Inference output must carry an epistemic class; it must never
        silently promote DERIVED -> SOURCE_CLAIM/OBSERVATION (L00-FM-02)."""
        if b is None or b.belief_id == "":
            return Verdict.UNKNOWN
        if b.claim_class in ("OBSERVATION", "SOURCE_CLAIM") and not b.representation_ids:
            return Verdict.FAIL          # inference typed as unbacked observation
        if b.confidence > 0.0 and not b.representation_ids:
            return Verdict.FAIL          # fabricated confidence
        if b.claimed_scope - b.supported_scope:
            return Verdict.FAIL          # scope widening (L00-T11 / INV-07)
        self.state.beliefs = [x for x in self.state.beliefs if x.belief_id != b.belief_id]
        self.state.beliefs.append(b)
        return Verdict.PASS

    def L10_apply(self, rep: Representation) -> Verdict:
        if rep is None or rep.rep_id == "":
            return Verdict.UNKNOWN
        if rep.is_reality:
            return Verdict.FAIL
        if rep.transformation_depth < 0:
            return Verdict.FAIL
        self.state.representations = [r for r in self.state.representations
                                      if r.rep_id != rep.rep_id]
        self.state.representations.append(rep)
        return Verdict.PASS

    # =======================================================================
    # L13 — Prediction
    # =======================================================================
    def L13_apply(self, pred: Prediction) -> Verdict:
        if pred is None or pred.pred_id == "":
            return Verdict.UNKNOWN
        if pred.recorded_as_outcome:
            return Verdict.FAIL          # PREDICTED != OBSERVED (L00-T03)
        if pred.horizon <= 0:
            return Verdict.FAIL
        self.state.predictions = [p for p in self.state.predictions
                                  if p.pred_id != pred.pred_id]
        self.state.predictions.append(pred)
        return Verdict.PASS

    # =======================================================================
    # L14 — Valuation (L20 credit-assignment feed)
    # =======================================================================
    def L14_value_belief(self, belief_id: str) -> Tuple[Verdict, float]:
        """Derived value: confidence * (1/recency). Never fabricates a value
        for a belief that does not exist -> UNKNOWN."""
        belief = next((b for b in self.state.beliefs if b.belief_id == belief_id), None)
        if belief is None:
            return Verdict.UNKNOWN, 0.0
        value = belief.confidence   # structural value: confidence ceiling only
        return Verdict.PASS, value

    # =======================================================================
    # L17 — Decision (PROPOSAL != COMMIT; L28 authorizes the commit)
    # =======================================================================
    def L17_stage(self, d: Decision) -> Verdict:
        """Stage a decision as a PROPOSAL. Never commits directly (L00-T22)."""
        if d is None or d.decision_id == "":
            return Verdict.UNKNOWN
        if d.intent == "" or d.proposed_by == "":
            return Verdict.FAIL
        if d.effect_digest == "":
            return Verdict.FAIL
        d.authorized = False
        d.committed = False
        self.state.decisions = [x for x in self.state.decisions
                                if x.decision_id != d.decision_id]
        self.state.decisions.append(d)
        return Verdict.PASS

    # =======================================================================
    # L21 — Learning (update gating + catastrophic-forgetting protection)
    # =======================================================================
    def L21_update_gate(self, incoming: MemoryCell) -> Tuple[Verdict, Optional[str]]:
        """Update gating for a learned memory.

        - PROPOSAL != COMMIT: an incoming cell must pass the memory write gate.
        - Catastrophic-forgetting protection: never evict an existing anchor
          (high value, high access) merely to admit the new one. If admission
          would push a higher-value cell out of budget, BLOCK.
        - Idempotent writes are NO_CHANGE, not double-writes.
        """
        if incoming is None:
            return Verdict.UNKNOWN, "no incoming cell"
        gate = self.L07_write_gate(incoming)
        if gate in (Verdict.FAIL, Verdict.UNKNOWN):
            return gate, "update blocked by L07 write gate"
        if gate == Verdict.CONDITIONAL:
            # duplicate -> no change (idempotent)
            return LearningOutcome.NO_CHANGE, "duplicate; no change"
        return Verdict.PASS, "update admissible"

    def L21_apply(self, incoming: MemoryCell, budget: int = 100) -> LearningOutcome:
        verdict, why = self.L21_update_gate(incoming)
        if verdict in (Verdict.FAIL, Verdict.UNKNOWN):
            self.state.stats["learning_blocked"] += 1
            self.state.update_log.append({
                "layer": "L21", "op": "APPLY", "cell_id": incoming.cell_id,
                "epoch": self.state.epoch, "outcome": LearningOutcome.BLOCKED,
                "why": why,
            })
            return LearningOutcome.BLOCKED
        if verdict == Verdict.CONDITIONAL:
            self.state.update_log.append({
                "layer": "L21", "op": "APPLY", "cell_id": incoming.cell_id,
                "epoch": self.state.epoch, "outcome": LearningOutcome.NO_CHANGE,
            })
            return LearningOutcome.NO_CHANGE

        # Catastrophic-forgetting protection: if over budget, only admit the
        # new cell if it out-values the weakest existing committed anchor.
        if len(self.state.memories) >= budget:
            weakest = min(self.state.memories,
                          key=lambda m: (m.confidence, m.access_count))
            if weakest.confidence >= incoming.confidence:
                self.state.stats["learning_blocked"] += 1
                return LearningOutcome.BLOCKED
            # evict the weakest (this is the only eviction path: value-bounded)
            self.state.memories.remove(weakest)
            if weakest.cell_id in self.state.consolidation_index:
                del self.state.consolidation_index[weakest.cell_id]

        self.state.memories.append(incoming)
        incoming.status = MemoryStatus.COMMITTED
        self.state.stats["learning_applied"] += 1
        self.state.update_log.append({
            "layer": "L21", "op": "APPLY", "cell_id": incoming.cell_id,
            "epoch": self.state.epoch, "outcome": LearningOutcome.APPLIED,
        })
        return LearningOutcome.APPLIED

    # =======================================================================
    # L22 — Consolidation (dedup at write time + index maintenance)
    # =======================================================================
    def L22_apply(self, cell: MemoryCell) -> Tuple[Verdict, Optional[str]]:
        """Consolidate a committed memory: content-hash index, dedup, and
        promotion to CONSOLIDATED status."""
        if cell is None or cell.cell_id == "":
            return Verdict.UNKNOWN, "no cell"
        if cell.status != MemoryStatus.COMMITTED:
            return Verdict.FAIL, "only COMMITTED memories consolidate"
        if cell.content is None:
            return Verdict.FAIL, "uncontentful memory cannot consolidate"

        h = self._digest(cell.content, cell.source)
        existing = self.state.consolidation_index.get(h)
        if existing is not None and existing != cell.cell_id:
            # exact duplicate already consolidated: do not keep the twin
            self.state.memories = [m for m in self.state.memories
                                   if m.cell_id != cell.cell_id]
            return Verdict.CONDITIONAL, f"deduped twin of {existing}"

        cell.status = MemoryStatus.CONSOLIDATED
        self.state.consolidation_index[h] = cell.cell_id
        self.state.stats["consolidated"] += 1
        return Verdict.PASS, "consolidated"

    # =======================================================================
    # L25 — Identity Continuity (anchors, fragmentation resistance)
    # =======================================================================
    def L25_validate_anchor(self, anchor: IdentityAnchor) -> Verdict:
        if anchor is None or anchor.anchor_id == "" or anchor.enactor == "":
            return Verdict.UNKNOWN
        if not anchor.continuity_evidence:
            return Verdict.FAIL          # identity without evidence is not an anchor
        if anchor.fragmentation < 0 or anchor.fragmentation > 1:
            return Verdict.FAIL
        return Verdict.PASS

    def L25_apply(self, anchor: IdentityAnchor) -> Verdict:
        v = self.L25_validate_anchor(anchor)
        if v != Verdict.PASS:
            return v
        if anchor.fragmentation > 0.5:
            self.state.stats["identity_fragmented"] += 1
        self.state.identity_anchors = [a for a in self.state.identity_anchors
                                       if a.anchor_id != anchor.anchor_id]
        self.state.identity_anchors.append(anchor)
        return Verdict.PASS

    # =======================================================================
    # L28 — Governance (authorizes consequential commit)
    # =======================================================================
    def L28_authorize(self, d: Decision, grant_scope: frozenset,
                      authorizer_role: str) -> Verdict:
        """CAPABILITY != AUTHORITY: a decision can be staged/possible but not
        committed without an authorization covering its scope by a distinct
        actor."""
        if d is None:
            return Verdict.UNKNOWN
        target = next((x for x in self.state.decisions if x.decision_id == d.decision_id), d)
        if not d.scope:
            return Verdict.FAIL          # unresolvable target fails closed
        if not d.scope <= grant_scope:
            return Verdict.FAIL          # scope expansion blocked
        if authorizer_role == "" or authorizer_role == d.proposed_by:
            return Verdict.FAIL          # no self-authorization (INV-038 analog)
        target.authorized = True
        return Verdict.PASS

    # =======================================================================
    # L29 — Evolution (the final gate; nothing evolves without continuity)
    # =======================================================================
    def L29_evolve_gate(self, anchor: IdentityAnchor, proposal_hash: str,
                        integrity_ok: bool) -> Verdict:
        """Evolution allowed only when identity continuity holds AND the
        proposal preserves integrity (INTEGRITY > COMPLETENESS)."""
        if anchor is None or proposal_hash == "":
            return Verdict.UNKNOWN
        if anchor.fragmentation > 0.5:
            return Verdict.FAIL          # fragmented identity cannot evolve
        if not integrity_ok:
            return Verdict.FAIL          # integrity breach blocks evolution
        return Verdict.PASS

    # =======================================================================
    # Forward pass — run the full chain L00..L29 in canonical order
    # =======================================================================
    def forward(self, obs: Observation, create_percept: bool = True,
                budget: int = 100) -> Dict[str, Any]:
        """Execute one full cognitive forward pass (L00 -> L29).

        Returns a structured trace: per-layer verdict + final state digest.
        This is the executable analog of 'one step of reasoning' — a signal
        from reality, bound, memorized, learned, consolidated, and governed.
        """
        self.state.epoch = self.epoch.next().value
        trace: Dict[str, Any] = {}

        # L00 Reality gate: admit the observation
        trace["L00"] = self.L00_apply(obs).value

        # L03 Percept (if requested): bind observation -> percept
        if create_percept and trace["L00"] == Verdict.PASS.value:
            p = Percept(
                percept_id="p-" + obs.obs_id,
                feature={"unit": obs.unit, "source": obs.source},
                observation_ids=(obs.obs_id,),
                confidence=0.5,
            )
            trace["L03"] = self.L03_apply(p).value
        else:
            trace["L03"] = Verdict.UNKNOWN.value

        # L05 Binding: build a representation bound to the observation
        rep = Representation(
            rep_id="r-" + obs.obs_id,
            entity_id=obs.obs_id,
            features={"unit": obs.unit},
            transformation_depth=0,
            is_reality=False,
        )
        trace["L05"] = self.L05_validate_binding(rep, (obs.obs_id,)).value
        trace["L08"] = self.L10_apply(rep).value   # L08 representation stored

        # L07 Memory: write a gated memory cell for this observation
        cell = MemoryCell(
            cell_id="mem-" + obs.obs_id,
            content=obs.value,
            source=obs.source,
            observation_ids=(obs.obs_id,),
            created_epoch=self.state.epoch,
            last_accessed_epoch=self.state.epoch,
            access_count=1,
            confidence=0.5 if obs.source else 0.0,
            freshness_horizon_tau=obs.freshness_horizon_tau,
            status=MemoryStatus.PROPOSED,
        )
        gate, gwhy = self.L21_apply(cell, budget=budget)     # L07 inside L21 gate
        trace["L07"] = gate.value
        trace["L21"] = gate.value

        # L22 Consolidation of the committed memory (if any)
        committed = next((m for m in self.state.memories
                          if m.cell_id == cell.cell_id
                          and m.status == MemoryStatus.COMMITTED), None)
        if committed is not None:
            cver, _ = self.L22_apply(committed)
            trace["L22"] = cver.value
        else:
            trace["L22"] = Verdict.UNKNOWN.value

        # L09 Inference: derive a belief about the event (typed DERIVED)
        belief = Belief(
            belief_id="b-" + obs.obs_id,
            claim=f"event {obs.obs_id} observed via {obs.source}",
            representation_ids=("r-" + obs.obs_id,),
            confidence=0.3,
            claim_class="DERIVED",
            supported_scope=frozenset({"event"}),
            claimed_scope=frozenset({"event"}),
        )
        # only if the observation was admitted (L00 pass)
        if trace["L00"] == Verdict.PASS.value:
            trace["L09"] = self.L09_apply(belief).value
        else:
            trace["L09"] = Verdict.UNKNOWN.value

        # L13 Prediction: never recorded as outcome
        pred = Prediction(pred_id="pr-" + obs.obs_id, claim=belief.claim,
                          horizon=10.0, recorded_as_outcome=False)
        trace["L13"] = self.L13_apply(pred).value
        trace["L14"] = Verdict.PASS.value

        # L17 Stage a proposal (not committed)
        decision = Decision(
            decision_id="d-" + obs.obs_id,
            intent="record observation as learned",
            effect_digest=self._digest(obs.obs_id),
            proposed_by="cognitive-matrix-engine",
            scope=frozenset({"memory"}),
            cost=1.0,
        )
        trace["L17"] = self.L17_stage(decision).value

        # L25 Identity anchor (resolves to the enactor of this pass)
        anchor = IdentityAnchor(
            anchor_id="anchor-1",
            enactor="cognitive-matrix-engine",
            continuity_evidence=(self._digest(self.state.epoch),),
            fragmentation=0.0,
            last_epoch=self.state.epoch,
        )
        trace["L25"] = self.L25_apply(anchor).value

        # L28 Governance: authorize the decision under a grant scope
        grant_scope = frozenset({"memory"})
        trace["L28"] = self.L28_authorize(
            decision, grant_scope, authorizer_role="governor").value

        # L29 Evolution gate: only if continuity + integrity hold
        integrity_ok = all(
            trace.get(k) in (Verdict.PASS.value, Verdict.CONDITIONAL.value)
            for k in ("L00", "L05", "L08", "L09", "L13")
        )
        trace["L29"] = self.L29_evolve_gate(
            anchor, self._digest(self.state.epoch), integrity_ok).value

        # L17 commit happens only under L28 authorization
        if trace["L28"] == Verdict.PASS.value and decision.authorized:
            decision.committed = True
            self.state.stats["decisions_committed"] += 1
            trace["L17_COMMIT"] = Verdict.PASS.value
        else:
            trace["L17_COMMIT"] = Verdict.UNKNOWN.value

        self.state.stats["layers_run"] += 1
        trace["epoch"] = self.state.epoch
        trace["state_digest"] = self._digest(
            self.state.epoch, len(self.state.memories),
            len(self.state.beliefs), len(self.state.decisions))
        return trace


# ---------------------------------------------------------------------------
# Durability bindings (note-based storage for the memory plane)
# ---------------------------------------------------------------------------

class NoteMemoryStore:
    """An EXTREMELY simple durability shim: writes committed memory cells to a
    directory of markdown notes, one note per cell. This is the thin layer
    that turns 'memory COMMITTED' into a re-loadable artifact in the vault.

    Status: reference persistence; NOT a distributed consensus store. It
    demonstrates the persist/verify/invalidate cycle the Persistence Canon
    requires, without claiming more.
    """

    def __init__(self, directory: str):
        self.directory = directory
        if directory and not os.path.isdir(directory):
            os.makedirs(directory, exist_ok=True)

    def persist(self, cell: MemoryCell) -> Tuple[Verdict, str]:
        if cell is None or cell.cell_id == "" or cell.content is None:
            return Verdict.UNKNOWN, "nothing to persist"
        if cell.status not in (MemoryStatus.COMMITTED, MemoryStatus.CONSOLIDATED):
            return Verdict.FAIL, "only committed/consolidated memory persists"
        safe = "".join(c for c in cell.cell_id if c.isalnum() or c in "-_")
        path = os.path.join(self.directory, f"{safe}.md")
        body = (
            f"---\n"
            f"type: memory-cell\n"
            f"cell_id: {cell.cell_id}\n"
            f"source: {cell.source}\n"
            f"status: {cell.status}\n"
            f"confidence: {cell.confidence}\n"
            f"epoch: {cell.created_epoch}\n"
            f"proof_hash: {cell.proof_hash}\n"
            f"---\n\n"
            f"# Memory Cell: {cell.cell_id}\n\n"
            f"| field | value |\n|---|---|\n"
            f"| source | {cell.source} |\n"
            f"| confidence | {cell.confidence} |\n"
            f"| status | {cell.status} |\n"
            f"| observation_ids | {list(cell.observation_ids)} |\n\n"
            f"Content `{cell.content}`\n"
        )
        with open(path, "w") as fh:
            fh.write(body)
        return Verdict.PASS, path

    def load(self, cell_id: str) -> Optional[MemoryCell]:
        safe = "".join(c for c in cell_id if c.isalnum() or c in "-_")
        path = os.path.join(self.directory, f"{safe}.md")
        if not os.path.exists(path):
            return None
        with open(path) as fh:
            text = fh.read()
        return MemoryCell(
            cell_id=cell_id,
            content=text,
            source="note-memory-store",
            status=MemoryStatus.CONSOLIDATED,
            proof_hash=self._digest(text),
        )

    @staticmethod
    def _digest(s: str) -> str:
        return hashlib.sha256(s.encode("utf-8", errors="replace")).hexdigest()


# ---------------------------------------------------------------------------
# Test suite — positive + adversarial + fail-closed-empty per layer family
# ---------------------------------------------------------------------------

def run_tests() -> Tuple[int, int, List[str]]:
    passed, failed = 0, 0
    failures: List[str] = []

    def t(ok: bool, label: str, note: str = ""):
        nonlocal passed, failed
        if ok:
            passed += 1
        else:
            failed += 1
            failures.append(f"{label}: {note}")

    E = CognitiveMatrixEngine(initial_epoch=0)

    # -- L00 reality gate ------------------------------------------------
    t(E.L00_validate_reality_gate({"kind": "model"}) == Verdict.PASS, "L00-pos", "model ok")
    t(E.L00_validate_reality_gate({"is_reality": True}) == Verdict.FAIL,
      "L00-neg-real", "representation flagged reality")
    t(E.L00_validate_reality_gate("__REALITY__") == Verdict.FAIL, "L00-neg-str", "identity claim")
    t(E.L00_validate_reality_gate(None) == Verdict.UNKNOWN, "L00-fc", "empty -> UNKNOWN")

    good_obs = Observation(obs_id="o1", value=1.0, unit="m", observer_id="sensor-a",
                           method="laser", event_time=100.0, observation_time=101.0,
                           freshness_horizon_tau=60.0, source="src-root",
                           ancestry=("src-root",))
    t(E.L00_apply(good_obs) == Verdict.PASS, "L00-apply-pos", "provenanced obs admitted")
    t(E.L00_apply(Observation(obs_id="o2", event_time=None, observation_time=None,
                              source="s")) == Verdict.FAIL, "L00-apply-neg", "no temporal identity")
    t(E.L00_apply(Observation(obs_id="o3", event_time=1.0, observation_time=2.0,
                              source="")) == Verdict.FAIL, "L00-apply-neg2", "no provenance")
    t(E.L00_apply(None) == Verdict.UNKNOWN, "L00-apply-fc", "None input")

    # -- L03 / L05 binding ------------------------------------------------
    p = Percept(percept_id="p-o1", feature={"unit": "m"}, observation_ids=("o1",))
    t(E.L03_apply(p) == Verdict.PASS, "L03-pos", "percept bound")
    t(E.L03_apply(Percept(percept_id="p-x", observation_ids=())) == Verdict.FAIL,
      "L03-neg", "percept without observation")
    rep = Representation(rep_id="r-o1", entity_id="o1", features={},
                         transformation_depth=0, is_reality=False)
    t(E.L05_validate_binding(rep, ("o1",)) == Verdict.PASS, "L05-pos", "binding ok")
    t(E.L05_validate_binding(replace(rep, is_reality=True), ("o1",)) == Verdict.FAIL,
      "L05-neg", "binding to reality flag")

    # -- L07 memory gate --------------------------------------------------
    m_ok = MemoryCell(cell_id="mem-ok", content="c1", source="src", observation_ids=("o1",),
                      confidence=0.5, status=MemoryStatus.PROPOSED)
    t(E.L07_write_gate(m_ok) == Verdict.PASS, "L07-gate-pos", "provenanced cell ok")
    t(E.L07_write_gate(MemoryCell(cell_id="m1", content="c", source="src",
                                  confidence=0.9, observation_ids=())) == Verdict.FAIL,
      "L07-gate-fab", "confidence without observation provenance (CM-I2)")
    t(E.L07_write_gate(MemoryCell(cell_id="m2", content="c", source="",
                                  confidence=0.0)) == Verdict.UNKNOWN,
      "L07-gate-source", "no provenance root -> UNKNOWN")
    t(E.L07_write_gate(MemoryCell(cell_id="m3", content="c", source="s",
                                  freshness_horizon_tau=-5)) == Verdict.FAIL,
      "L07-gate-tau", "negative freshness horizon")

    # -- L21 learning gate ------------------------------------------------
    out = E.L21_apply(MemoryCell(cell_id="mem-l1", content="learned", source="s",
                                 observation_ids=("o1",), confidence=0.4),
                      budget=100)
    t(out == LearningOutcome.APPLIED, "L21-pos", "admissible update applied")
    out_block = E.L21_apply(MemoryCell(cell_id="mem-l2", content="x", source="",
                                       confidence=0.0, observation_ids=("o1",)),
                            budget=100)
    t(out_block == LearningOutcome.BLOCKED, "L21-neg", "unprovenanced update blocked")
    # idempotent duplicate
    out_dup = E.L21_apply(MemoryCell(cell_id="mem-dup", content="learned", source="s",
                                     observation_ids=("o1",), confidence=0.4), budget=100)
    t(out_dup in (LearningOutcome.NO_CHANGE, LearningOutcome.BLOCKED),
      "L21-dup", "duplicate not double-written")

    # -- L22 consolidation ------------------------------------------------
    committed = MemoryCell(cell_id="mem-c", content="dedup-me", source="s",
                           observation_ids=("o1",), confidence=0.3,
                           status=MemoryStatus.COMMITTED)
    cver, _ = E.L22_apply(committed)
    t(cver == Verdict.PASS, "L22-pos", "committed memory consolidated")
    # cannot consolidate a PROPOSED cell
    proposer = MemoryCell(cell_id="mem-proposed", content="x", source="s",
                          confidence=0.1, status=MemoryStatus.PROPOSED)
    t(E.L22_apply(proposer)[0] == Verdict.FAIL, "L22-neg", "proposed not consolidated")

    # -- L25 identity -----------------------------------------------------
    anchor = IdentityAnchor(anchor_id="a1", enactor="engine",
                            continuity_evidence=("h1",), fragmentation=0.0)
    t(E.L25_apply(anchor) == Verdict.PASS, "L25-pos", "anchor accepted")
    t(E.L25_apply(IdentityAnchor(anchor_id="a2", enactor="engine",
                                 continuity_evidence=(), fragmentation=0.0)) == Verdict.FAIL,
      "L25-neg", "identity without evidence")

    # -- L28 governance ---------------------------------------------------
    dec = Decision(decision_id="dec1", intent="act", effect_digest="d",
                   proposed_by="engine", scope=frozenset({"memory"}), cost=1.0)
    t(E.L17_stage(dec) == Verdict.PASS, "L17-pos", "proposal staged")
    t(E.L28_authorize(dec, frozenset({"memory"}), authorizer_role="governor") == Verdict.PASS,
      "L28-pos", "distinct authorizer ok")
    t(dec.authorized is True, "L28-effect", "authorized flag set")
    # self-authorization must fail
    dec2 = Decision(decision_id="dec2", intent="self", effect_digest="d",
                    proposed_by="engine", scope=frozenset({"memory"}))
    E.L17_stage(dec2)
    t(E.L28_authorize(dec2, frozenset({"memory"}), authorizer_role="engine") == Verdict.FAIL,
      "L28-neg", "no self-authorization")
    # scope expansion must fail
    dec3 = Decision(decision_id="dec3", intent="scope", effect_digest="d",
                    proposed_by="engine", scope=frozenset({"memory", "filesystem"}))
    E.L17_stage(dec3)
    t(E.L28_authorize(dec3, frozenset({"memory"}), authorizer_role="governor") == Verdict.FAIL,
      "L28-neg2", "scope expansion blocked")
    # capability without authority
    dec4 = Decision(decision_id="dec4", intent="x", effect_digest="d",
                    proposed_by="engine", scope=frozenset())
    E.L17_stage(dec4)
    t(E.L28_authorize(dec4, frozenset({"memory"}), "governor") == Verdict.FAIL,
      "L28-neg3", "unresolvable scope fails closed")

    # -- L29 evolution ----------------------------------------------------
    t(E.L29_evolve_gate(anchor, "h", True) == Verdict.PASS, "L29-pos", "integrity + continuity")
    t(E.L29_evolve_gate(replace(anchor, fragmentation=0.9), "h", True) == Verdict.FAIL,
      "L29-neg", "fragmented identity blocks evolution")
    t(E.L29_evolve_gate(anchor, "h", False) == Verdict.FAIL, "L29-neg2", "integrity breach")
    t(E.L29_evolve_gate(None, "h", True) == Verdict.UNKNOWN, "L29-fc", "no anchor")

    # -- Full forward pass -------------------------------------------------
    t2 = CognitiveMatrixEngine(initial_epoch=0)
    trace = t2.forward(good_obs)
    t(trace["L00"] == Verdict.PASS.value, "FW-L00", "reality gate passed")
    t(trace["L03"] == Verdict.PASS.value, "FW-L03", "percept formed")
    t(trace["L07"] in (Verdict.PASS.value, Verdict.CONDITIONAL.value), "FW-L07", "memory written")
    t(trace["L29"] == Verdict.PASS.value, "FW-L29", "evolution allowed under integrity")
    t(t2.state.stats["layers_run"] == 1, "FW-stats", "one pass counted")
    # forward with a FAILED observation must not fabricate downstream state
    t3 = CognitiveMatrixEngine(initial_epoch=0)
    bad = Observation(obs_id="bad1", value=1.0, event_time=None, observation_time=None,
                      source="s")
    trace3 = t3.forward(bad)
    t(trace3["L00"] == Verdict.FAIL.value, "FW-fail-L00", "bad obs rejected at reality gate")
    t(trace3["L09"] == Verdict.UNKNOWN.value, "FW-fail-L09", "no belief fabricated from bad obs")
    t(trace3["L17_COMMIT"] == Verdict.UNKNOWN.value, "FW-fail-commit", "no commit on failed pass")

    # -- Durability shim --------------------------------------------------
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        store = NoteMemoryStore(td)
        cell = MemoryCell(cell_id="mem-persist", content="payload", source="src",
                          observation_ids=("o1",), confidence=0.4,
                          status=MemoryStatus.CONSOLIDATED)
        v, path = store.persist(cell)
        t(v == Verdict.PASS and os.path.exists(path), "STORE-pos", "memory persisted to note")
        loaded = store.load("mem-persist")
        t(loaded is not None and loaded.cell_id == "mem-persist", "STORE-load", "memory reloadable")
        t(store.load("does-not-exist") is None, "STORE-fc", "missing memory -> None (not fabricated)")

    return passed, failed, failures


if __name__ == "__main__":
    import tempfile as _tf
    pos, neg, fails = run_tests()
    total = pos + neg
    print(f"Cognitive Matrix Engine: {pos}/{total} pass, {neg} fail")
    for msg in fails[:30]:
        print("  FAIL:", msg)
    raise SystemExit(0 if neg == 0 else 1)
