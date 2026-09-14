"""Bounded executable ULK semantic fragments for AMOS OS.

Origin architect / steward: Trang Phan.
Implementation class: AMOS_MODEL / executable bounded reference.

This module fills three currently missing bounded fragment surfaces without
claiming complete canonical equivalence:
- LTLf evaluation over explicit finite traces;
- finite multi-agent relational Kripke modal evaluation;
- Dung abstract argumentation grounded semantics.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from types import MappingProxyType
from typing import FrozenSet, Mapping, Sequence, Tuple


ALGORITHM_PROVENANCE = {
    "ltlf_finite_trace_semantics": {
        "authors": "Giuseppe De Giacomo; Moshe Y. Vardi",
        "year": 2013,
        "source": "IJCAI 2013, pp. 854-860",
        "status": "ESTABLISHED_LOGIC_SEMANTICS",
    },
    "dung_grounded_argumentation": {
        "author": "Phan Minh Dung",
        "year": 1995,
        "doi": "10.1016/0004-3702(94)00041-X",
        "status": "ESTABLISHED_ARGUMENTATION_SEMANTICS",
    },
    "kripke_modal_semantics": {
        "status": "ESTABLISHED_MODAL_SEMANTICS",
        "note": "Finite relational Kripke semantics; no S5 properties are assumed unless validated.",
    },
}


class LogicDomainError(ValueError):
    """Raised when an input violates the declared finite semantic domain."""


class LTLKind(Enum):
    ATOM = "atom"
    NOT = "not"
    AND = "and"
    OR = "or"
    NEXT = "next"
    EVENTUALLY = "eventually"
    ALWAYS = "always"
    UNTIL = "until"


@dataclass(frozen=True)
class LTLFormula:
    kind: LTLKind
    atom_id: str | None = None
    children: Tuple["LTLFormula", ...] = ()

    def __post_init__(self) -> None:
        arity = {
            LTLKind.ATOM: 0,
            LTLKind.NOT: 1,
            LTLKind.AND: 2,
            LTLKind.OR: 2,
            LTLKind.NEXT: 1,
            LTLKind.EVENTUALLY: 1,
            LTLKind.ALWAYS: 1,
            LTLKind.UNTIL: 2,
        }[self.kind]
        if len(self.children) != arity:
            raise LogicDomainError(f"{self.kind.value} requires arity {arity}")
        if self.kind is LTLKind.ATOM:
            if not self.atom_id or not self.atom_id.strip():
                raise LogicDomainError("LTL atom requires a non-empty identifier")
        elif self.atom_id is not None:
            raise LogicDomainError("non-atomic LTL formula cannot carry atom_id")

    @staticmethod
    def atom(name: str) -> "LTLFormula":
        return LTLFormula(LTLKind.ATOM, atom_id=name.strip())

    @staticmethod
    def not_(x: "LTLFormula") -> "LTLFormula":
        return LTLFormula(LTLKind.NOT, children=(x,))

    @staticmethod
    def and_(a: "LTLFormula", b: "LTLFormula") -> "LTLFormula":
        return LTLFormula(LTLKind.AND, children=(a, b))

    @staticmethod
    def or_(a: "LTLFormula", b: "LTLFormula") -> "LTLFormula":
        return LTLFormula(LTLKind.OR, children=(a, b))

    @staticmethod
    def next_(x: "LTLFormula") -> "LTLFormula":
        return LTLFormula(LTLKind.NEXT, children=(x,))

    @staticmethod
    def eventually(x: "LTLFormula") -> "LTLFormula":
        return LTLFormula(LTLKind.EVENTUALLY, children=(x,))

    @staticmethod
    def always(x: "LTLFormula") -> "LTLFormula":
        return LTLFormula(LTLKind.ALWAYS, children=(x,))

    @staticmethod
    def until(a: "LTLFormula", b: "LTLFormula") -> "LTLFormula":
        return LTLFormula(LTLKind.UNTIL, children=(a, b))


def evaluate_ltlf(
    formula: LTLFormula,
    trace: Sequence[Sequence[str] | FrozenSet[str]],
    *,
    position: int = 0,
) -> bool:
    """Evaluate strong-next LTLf semantics on a finite non-empty trace."""
    states = tuple(frozenset(state) for state in trace)
    if not states:
        raise LogicDomainError("LTLf trace must be non-empty")
    if not 0 <= position < len(states):
        raise LogicDomainError("LTLf position is outside the trace")

    @lru_cache(maxsize=None)
    def sat(node: LTLFormula, i: int) -> bool:
        if node.kind is LTLKind.ATOM:
            assert node.atom_id is not None
            return node.atom_id in states[i]
        if node.kind is LTLKind.NOT:
            return not sat(node.children[0], i)
        if node.kind is LTLKind.AND:
            return sat(node.children[0], i) and sat(node.children[1], i)
        if node.kind is LTLKind.OR:
            return sat(node.children[0], i) or sat(node.children[1], i)
        if node.kind is LTLKind.NEXT:
            return i + 1 < len(states) and sat(node.children[0], i + 1)
        if node.kind is LTLKind.EVENTUALLY:
            return any(sat(node.children[0], j) for j in range(i, len(states)))
        if node.kind is LTLKind.ALWAYS:
            return all(sat(node.children[0], j) for j in range(i, len(states)))
        if node.kind is LTLKind.UNTIL:
            left, right = node.children
            return any(
                sat(right, j) and all(sat(left, k) for k in range(i, j))
                for j in range(i, len(states))
            )
        raise AssertionError(f"unhandled LTL kind: {node.kind}")

    return sat(formula, position)


class ModalKind(Enum):
    ATOM = "atom"
    NOT = "not"
    AND = "and"
    OR = "or"
    BOX = "box"
    DIAMOND = "diamond"


@dataclass(frozen=True)
class ModalFormula:
    kind: ModalKind
    atom_id: str | None = None
    agent: str | None = None
    children: Tuple["ModalFormula", ...] = ()

    def __post_init__(self) -> None:
        arity = {
            ModalKind.ATOM: 0,
            ModalKind.NOT: 1,
            ModalKind.AND: 2,
            ModalKind.OR: 2,
            ModalKind.BOX: 1,
            ModalKind.DIAMOND: 1,
        }[self.kind]
        if len(self.children) != arity:
            raise LogicDomainError(f"{self.kind.value} requires arity {arity}")
        if self.kind is ModalKind.ATOM:
            if not self.atom_id or not self.atom_id.strip():
                raise LogicDomainError("modal atom requires non-empty atom_id")
            if self.agent is not None:
                raise LogicDomainError("modal atom cannot carry agent")
        elif self.kind in (ModalKind.BOX, ModalKind.DIAMOND):
            if not self.agent or not self.agent.strip():
                raise LogicDomainError("modal operator requires non-empty agent")
            if self.atom_id is not None:
                raise LogicDomainError("modal operator cannot carry atom_id")
        elif self.atom_id is not None or self.agent is not None:
            raise LogicDomainError("boolean modal connective cannot carry atom/agent")

    @staticmethod
    def atom(name: str) -> "ModalFormula":
        return ModalFormula(ModalKind.ATOM, atom_id=name.strip())

    @staticmethod
    def not_(x: "ModalFormula") -> "ModalFormula":
        return ModalFormula(ModalKind.NOT, children=(x,))

    @staticmethod
    def and_(a: "ModalFormula", b: "ModalFormula") -> "ModalFormula":
        return ModalFormula(ModalKind.AND, children=(a, b))

    @staticmethod
    def or_(a: "ModalFormula", b: "ModalFormula") -> "ModalFormula":
        return ModalFormula(ModalKind.OR, children=(a, b))

    @staticmethod
    def box(agent: str, x: "ModalFormula") -> "ModalFormula":
        return ModalFormula(ModalKind.BOX, agent=agent.strip(), children=(x,))

    @staticmethod
    def diamond(agent: str, x: "ModalFormula") -> "ModalFormula":
        return ModalFormula(ModalKind.DIAMOND, agent=agent.strip(), children=(x,))


@dataclass(frozen=True)
class KripkeModel:
    worlds: Tuple[str, ...]
    valuation: Mapping[str, FrozenSet[str]]
    accessibility: Mapping[str, FrozenSet[Tuple[str, str]]]

    def __init__(
        self,
        *,
        worlds: Sequence[str],
        valuation: Mapping[str, Sequence[str] | FrozenSet[str]],
        accessibility: Mapping[str, Sequence[Tuple[str, str]] | FrozenSet[Tuple[str, str]]],
    ) -> None:
        world_tuple = tuple(str(w).strip() for w in worlds)
        if not world_tuple or any(not w for w in world_tuple):
            raise LogicDomainError("Kripke worlds must be explicit non-empty ids")
        if len(set(world_tuple)) != len(world_tuple):
            raise LogicDomainError("Kripke world ids must be unique")
        world_set = set(world_tuple)
        if set(valuation) != world_set:
            raise LogicDomainError("valuation must define every and only declared world")
        val = {w: frozenset(valuation[w]) for w in world_tuple}
        rel: dict[str, FrozenSet[Tuple[str, str]]] = {}
        for agent, edges in accessibility.items():
            agent_id = str(agent).strip()
            if not agent_id:
                raise LogicDomainError("agent id must be non-empty")
            frozen = frozenset((str(a).strip(), str(b).strip()) for a, b in edges)
            if any(a not in world_set or b not in world_set for a, b in frozen):
                raise LogicDomainError("accessibility edge references unknown world")
            rel[agent_id] = frozen
        object.__setattr__(self, "worlds", world_tuple)
        object.__setattr__(self, "valuation", MappingProxyType(val))
        object.__setattr__(self, "accessibility", MappingProxyType(rel))

    def successors(self, agent: str, world: str) -> FrozenSet[str]:
        if world not in self.valuation:
            raise LogicDomainError("unknown Kripke world")
        if agent not in self.accessibility:
            raise LogicDomainError("unknown modal agent")
        return frozenset(v for u, v in self.accessibility[agent] if u == world)

    def relation_is_s5(self, agent: str) -> bool:
        """Check whether an agent relation is an equivalence relation."""
        if agent not in self.accessibility:
            raise LogicDomainError("unknown modal agent")
        rel = self.accessibility[agent]
        worlds = self.worlds
        reflexive = all((w, w) in rel for w in worlds)
        symmetric = all((v, u) in rel for u, v in rel)
        transitive = all(
            (u, w) in rel
            for u, v in rel
            for v2, w in rel
            if v == v2
        )
        return reflexive and symmetric and transitive


def evaluate_modal(formula: ModalFormula, model: KripkeModel, world: str) -> bool:
    """Evaluate a modal formula under explicitly supplied accessibility relations."""
    if world not in model.valuation:
        raise LogicDomainError("unknown evaluation world")

    @lru_cache(maxsize=None)
    def sat(node: ModalFormula, w: str) -> bool:
        if node.kind is ModalKind.ATOM:
            assert node.atom_id is not None
            return node.atom_id in model.valuation[w]
        if node.kind is ModalKind.NOT:
            return not sat(node.children[0], w)
        if node.kind is ModalKind.AND:
            return sat(node.children[0], w) and sat(node.children[1], w)
        if node.kind is ModalKind.OR:
            return sat(node.children[0], w) or sat(node.children[1], w)
        assert node.agent is not None
        successors = model.successors(node.agent, w)
        if node.kind is ModalKind.BOX:
            return all(sat(node.children[0], v) for v in successors)
        if node.kind is ModalKind.DIAMOND:
            return any(sat(node.children[0], v) for v in successors)
        raise AssertionError(f"unhandled modal kind: {node.kind}")

    return sat(formula, world)


@dataclass(frozen=True)
class ArgumentationFramework:
    arguments: Tuple[str, ...]
    attacks: FrozenSet[Tuple[str, str]]

    def __init__(
        self,
        *,
        arguments: Sequence[str],
        attacks: Sequence[Tuple[str, str]] | FrozenSet[Tuple[str, str]],
    ) -> None:
        args = tuple(str(a).strip() for a in arguments)
        if not args or any(not a for a in args):
            raise LogicDomainError("argument ids must be non-empty")
        if len(set(args)) != len(args):
            raise LogicDomainError("argument ids must be unique")
        arg_set = set(args)
        edges = frozenset((str(a).strip(), str(b).strip()) for a, b in attacks)
        if any(a not in arg_set or b not in arg_set for a, b in edges):
            raise LogicDomainError("attack references unknown argument")
        object.__setattr__(self, "arguments", args)
        object.__setattr__(self, "attacks", edges)

    def attackers(self, argument: str) -> FrozenSet[str]:
        if argument not in self.arguments:
            raise LogicDomainError("unknown argument")
        return frozenset(a for a, b in self.attacks if b == argument)

    def attacked_by(self, arguments: FrozenSet[str]) -> FrozenSet[str]:
        if not arguments.issubset(self.arguments):
            raise LogicDomainError("candidate set contains unknown argument")
        return frozenset(b for a, b in self.attacks if a in arguments)

    def conflict_free(self, arguments: FrozenSet[str]) -> bool:
        if not arguments.issubset(self.arguments):
            raise LogicDomainError("candidate set contains unknown argument")
        return not any(a in arguments and b in arguments for a, b in self.attacks)

    def defended_by(self, argument: str, defenders: FrozenSet[str]) -> bool:
        if argument not in self.arguments:
            raise LogicDomainError("unknown argument")
        attacked = self.attacked_by(defenders)
        return self.attackers(argument).issubset(attacked)

    def characteristic(self, defenders: FrozenSet[str]) -> FrozenSet[str]:
        """Dung characteristic function F(S): arguments acceptable w.r.t. S."""
        if not defenders.issubset(self.arguments):
            raise LogicDomainError("defender set contains unknown argument")
        return frozenset(a for a in self.arguments if self.defended_by(a, defenders))

    def grounded_extension(self) -> FrozenSet[str]:
        """Least fixed point of the characteristic function for finite AFs."""
        current: FrozenSet[str] = frozenset()
        for _ in range(len(self.arguments) + 1):
            nxt = self.characteristic(current)
            if nxt == current:
                return current
            if not current.issubset(nxt):
                raise AssertionError("Dung characteristic iteration lost monotonicity")
            current = nxt
        raise AssertionError("finite grounded iteration failed to converge")


def validate_semantic_fragment_invariants() -> Tuple[str, ...]:
    failures: list[str] = []

    p = LTLFormula.atom("p")
    trace = (frozenset(), frozenset({"p"}))
    if not evaluate_ltlf(LTLFormula.eventually(p), trace):
        failures.append("LTLF_EVENTUALLY")
    if evaluate_ltlf(LTLFormula.next_(p), trace, position=1):
        failures.append("LTLF_STRONG_NEXT_BOUNDARY")

    model = KripkeModel(
        worlds=("w0", "w1"),
        valuation={"w0": ("p",), "w1": ("p",)},
        accessibility={
            "a": (("w0", "w0"), ("w0", "w1"), ("w1", "w0"), ("w1", "w1"))
        },
    )
    if not evaluate_modal(ModalFormula.box("a", ModalFormula.atom("p")), model, "w0"):
        failures.append("MODAL_BOX")
    if not model.relation_is_s5("a"):
        failures.append("MODAL_S5_CHECK")

    af = ArgumentationFramework(
        arguments=("A", "B", "C"), attacks=(("A", "B"), ("B", "C"))
    )
    if af.grounded_extension() != frozenset({"A", "C"}):
        failures.append("DUNG_GROUNDED")

    return tuple(dict.fromkeys(failures))
