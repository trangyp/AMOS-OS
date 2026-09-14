"""Bounded finite Kripke-model evaluator for AMOS ULK ALU-04.

Origin architect / steward: Trang Phan.

Implements a finite multi-relation normal modal-logic K subfragment with explicit
worlds, agent/modality-indexed accessibility relations, valuations, and BOX/DIAMOND.
No accessibility property is inferred. K/T/S4/S5 frame labels are diagnostics over
explicit relations, not claims about real knowledge, belief, agents, or reality.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from typing import Any, FrozenSet, Mapping, Optional, Tuple


class ModalStatus(Enum):
    SATISFIED = "SATISFIED"
    VIOLATED = "VIOLATED"
    REJECT_MALFORMED_REQUEST = "REJECT_MALFORMED_REQUEST"
    RESOURCE_BOUND_EXCEEDED = "RESOURCE_BOUND_EXCEEDED"


class ModalKind(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
    ATOM = "ATOM"
    NOT = "NOT"
    AND = "AND"
    OR = "OR"
    IMPLIES = "IMPLIES"
    BOX = "BOX"
    DIAMOND = "DIAMOND"


class ModalError(ValueError):
    pass


class ModalResourceBound(ModalError):
    pass


@dataclass(frozen=True)
class ModalFormula:
    kind: ModalKind
    atom: Optional[str] = None
    agent: Optional[str] = None
    children: Tuple["ModalFormula", ...] = ()


@dataclass(frozen=True)
class ModalBounds:
    max_worlds: int = 512
    max_edges: int = 50_000
    max_formula_nodes: int = 10_000
    max_formula_depth: int = 256

    def __post_init__(self) -> None:
        if min(self.max_worlds, self.max_edges, self.max_formula_nodes, self.max_formula_depth) <= 0:
            raise ValueError("modal bounds must be positive")


@dataclass(frozen=True)
class KripkeModel:
    worlds: Tuple[str, ...]
    relations: Mapping[str, Tuple[Tuple[str, str], ...]]
    valuations: Mapping[str, FrozenSet[str]]

    def validate(self, bounds: ModalBounds) -> None:
        if not self.worlds or len(self.worlds) != len(set(self.worlds)):
            raise ModalError("worlds must be non-empty and unique")
        if len(self.worlds) > bounds.max_worlds:
            raise ModalResourceBound("world count bound exceeded")
        world_set = set(self.worlds)
        if set(self.valuations) != world_set:
            raise ModalError("valuations must cover exactly the declared worlds")
        edge_count = 0
        for world in self.worlds:
            if not world.strip():
                raise ModalError("world ids must be non-empty")
            if any(not atom.strip() for atom in self.valuations[world]):
                raise ModalError("atomic proposition names must be non-empty")
        for agent, edges in self.relations.items():
            if not agent.strip():
                raise ModalError("relation/agent ids must be non-empty")
            edge_count += len(edges)
            if edge_count > bounds.max_edges:
                raise ModalResourceBound("accessibility edge bound exceeded")
            for src, dst in edges:
                if src not in world_set or dst not in world_set:
                    raise ModalError("accessibility edge references undeclared world")


@dataclass(frozen=True)
class ModalResult:
    status: ModalStatus
    value: Optional[bool]
    world: Optional[str]
    reason: str
    semantics: str = "FINITE_KRIPKE_NORMAL_MODAL_K"
    epistemic_knowledge_claim: bool = False
    empirical_truth_claim: bool = False
    effect_authority: bool = False
    canon_promoted: bool = False


@dataclass(frozen=True)
class FrameAudit:
    agent: str
    reflexive: bool
    symmetric: bool
    transitive: bool
    euclidean: bool

    @property
    def satisfies_K(self) -> bool:
        return True

    @property
    def satisfies_T(self) -> bool:
        return self.reflexive

    @property
    def satisfies_S4(self) -> bool:
        return self.reflexive and self.transitive

    @property
    def satisfies_S5(self) -> bool:
        return self.reflexive and self.symmetric and self.transitive


def parse_formula(value: Any, *, bounds: ModalBounds, _depth: int = 0, _counter: Optional[list[int]] = None) -> ModalFormula:
    if _counter is None:
        _counter = [0]
    _counter[0] += 1
    if _counter[0] > bounds.max_formula_nodes:
        raise ModalResourceBound("formula node bound exceeded")
    if _depth > bounds.max_formula_depth:
        raise ModalResourceBound("formula depth bound exceeded")
    if not isinstance(value, dict) or len(value) != 1:
        raise ModalError("formula must be a single-key object")
    key, payload = next(iter(value.items()))
    if key == "true" and payload is True:
        return ModalFormula(ModalKind.TRUE)
    if key == "false" and payload is True:
        return ModalFormula(ModalKind.FALSE)
    if key == "atom" and isinstance(payload, str) and payload.strip():
        return ModalFormula(ModalKind.ATOM, atom=payload)
    if key == "not":
        return ModalFormula(ModalKind.NOT, children=(parse_formula(payload, bounds=bounds, _depth=_depth + 1, _counter=_counter),))
    if key in {"and", "or", "implies"} and isinstance(payload, list) and len(payload) == 2:
        kind = {"and": ModalKind.AND, "or": ModalKind.OR, "implies": ModalKind.IMPLIES}[key]
        return ModalFormula(kind, children=tuple(parse_formula(x, bounds=bounds, _depth=_depth + 1, _counter=_counter) for x in payload))
    if key in {"box", "diamond"} and isinstance(payload, dict) and set(payload) == {"agent", "formula"}:
        agent = payload["agent"]
        if not isinstance(agent, str) or not agent.strip():
            raise ModalError("modal operator requires explicit non-empty agent/relation id")
        child = parse_formula(payload["formula"], bounds=bounds, _depth=_depth + 1, _counter=_counter)
        return ModalFormula(ModalKind.BOX if key == "box" else ModalKind.DIAMOND, agent=agent, children=(child,))
    raise ModalError("unsupported or malformed modal formula")


def evaluate(model: KripkeModel, formula: ModalFormula, world: str, *, bounds: ModalBounds = ModalBounds()) -> bool:
    model.validate(bounds)
    if world not in set(model.worlds):
        raise ModalError("evaluation world is undeclared")
    successors = {agent: {w: [] for w in model.worlds} for agent in model.relations}
    for agent, edges in model.relations.items():
        for src, dst in edges:
            successors[agent][src].append(dst)

    @lru_cache(maxsize=None)
    def ev(node: ModalFormula, w: str) -> bool:
        if node.kind is ModalKind.TRUE:
            return True
        if node.kind is ModalKind.FALSE:
            return False
        if node.kind is ModalKind.ATOM:
            assert node.atom is not None
            return node.atom in model.valuations[w]
        if node.kind is ModalKind.NOT:
            return not ev(node.children[0], w)
        if node.kind is ModalKind.AND:
            return ev(node.children[0], w) and ev(node.children[1], w)
        if node.kind is ModalKind.OR:
            return ev(node.children[0], w) or ev(node.children[1], w)
        if node.kind is ModalKind.IMPLIES:
            return (not ev(node.children[0], w)) or ev(node.children[1], w)
        if node.kind in {ModalKind.BOX, ModalKind.DIAMOND}:
            assert node.agent is not None
            if node.agent not in successors:
                raise ModalError(f"undeclared accessibility relation: {node.agent}")
            succ = successors[node.agent][w]
            if node.kind is ModalKind.BOX:
                return all(ev(node.children[0], v) for v in succ)
            return any(ev(node.children[0], v) for v in succ)
        raise AssertionError(node.kind)

    return ev(formula, world)


def audit_frame(model: KripkeModel, agent: str, *, bounds: ModalBounds = ModalBounds()) -> FrameAudit:
    model.validate(bounds)
    if agent not in model.relations:
        raise ModalError("undeclared accessibility relation")
    worlds = set(model.worlds)
    relation = set(model.relations[agent])
    reflexive = all((w, w) in relation for w in worlds)
    symmetric = all((b, a) in relation for a, b in relation)
    transitive = all((a, c) in relation for a, b in relation for x, c in relation if x == b)
    euclidean = all((b, c) in relation for a, b in relation for x, c in relation if x == a)
    return FrameAudit(agent, reflexive, symmetric, transitive, euclidean)


def run_request(request: Any, *, bounds: ModalBounds = ModalBounds()) -> ModalResult:
    if not isinstance(request, dict) or set(request) != {"model", "formula", "world"}:
        return ModalResult(ModalStatus.REJECT_MALFORMED_REQUEST, None, None, "request must contain exactly model, formula, world")
    try:
        raw = request["model"]
        if not isinstance(raw, dict) or set(raw) != {"worlds", "relations", "valuations"}:
            raise ModalError("model must contain worlds, relations, valuations")
        worlds = tuple(raw["worlds"])
        if not isinstance(raw["relations"], dict) or not isinstance(raw["valuations"], dict):
            raise ModalError("relations and valuations must be objects")
        relations = {str(a): tuple(tuple(edge) for edge in edges) for a, edges in raw["relations"].items()}
        valuations = {str(w): frozenset(vals) for w, vals in raw["valuations"].items()}
        model = KripkeModel(worlds, relations, valuations)
        model.validate(bounds)
        formula = parse_formula(request["formula"], bounds=bounds)
        world = request["world"]
        if not isinstance(world, str):
            raise ModalError("world must be a string")
        value = evaluate(model, formula, world, bounds=bounds)
        return ModalResult(ModalStatus.SATISFIED if value else ModalStatus.VIOLATED, value, world, "formula evaluated in explicit finite Kripke model")
    except ModalResourceBound as exc:
        return ModalResult(ModalStatus.RESOURCE_BOUND_EXCEEDED, None, None, str(exc))
    except (ModalError, TypeError, ValueError) as exc:
        return ModalResult(ModalStatus.REJECT_MALFORMED_REQUEST, None, None, str(exc))
