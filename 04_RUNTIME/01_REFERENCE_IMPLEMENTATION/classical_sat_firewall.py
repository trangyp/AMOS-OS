"""Bounded classical satisfiability firewall for AMOS Core-19 repair.

Origin architect / steward: Trang Phan.

This is an AMOS_MODEL executable reference. It establishes only exact bounded
propositional satisfiability for the syntax implemented here.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from itertools import product
from typing import Mapping, Optional, Sequence, Tuple


class BoolKind(Enum):
    ATOM = "atom"
    NOT = "not"
    AND = "and"
    OR = "or"
    IMPLIES = "implies"
    BOTTOM = "bottom"


@dataclass(frozen=True)
class BoolFormula:
    kind: BoolKind
    atom_id: Optional[str] = None
    children: Tuple["BoolFormula", ...] = ()

    def __post_init__(self) -> None:
        arity = {
            BoolKind.ATOM: 0,
            BoolKind.BOTTOM: 0,
            BoolKind.NOT: 1,
            BoolKind.AND: 2,
            BoolKind.OR: 2,
            BoolKind.IMPLIES: 2,
        }[self.kind]
        if len(self.children) != arity:
            raise ValueError(f"{self.kind.value} requires arity {arity}")
        if self.kind is BoolKind.ATOM:
            if not self.atom_id or not self.atom_id.strip():
                raise ValueError("Boolean atom requires non-empty atom_id")
        elif self.atom_id is not None:
            raise ValueError(f"{self.kind.value} must not carry atom_id")

    @staticmethod
    def atom(name: str) -> "BoolFormula":
        return BoolFormula(BoolKind.ATOM, atom_id=name.strip())

    @staticmethod
    def bottom() -> "BoolFormula":
        return BoolFormula(BoolKind.BOTTOM)

    @staticmethod
    def not_(x: "BoolFormula") -> "BoolFormula":
        return BoolFormula(BoolKind.NOT, children=(x,))

    @staticmethod
    def and_(a: "BoolFormula", b: "BoolFormula") -> "BoolFormula":
        return BoolFormula(BoolKind.AND, children=(a, b))

    @staticmethod
    def or_(a: "BoolFormula", b: "BoolFormula") -> "BoolFormula":
        return BoolFormula(BoolKind.OR, children=(a, b))

    @staticmethod
    def implies(a: "BoolFormula", b: "BoolFormula") -> "BoolFormula":
        return BoolFormula(BoolKind.IMPLIES, children=(a, b))


def _atoms(formula: BoolFormula) -> Tuple[str, ...]:
    atoms = set()

    def visit(node: BoolFormula) -> None:
        if node.kind is BoolKind.ATOM:
            assert node.atom_id is not None
            atoms.add(node.atom_id)
        for child in node.children:
            visit(child)

    visit(formula)
    return tuple(sorted(atoms))


def _evaluate(formula: BoolFormula, assignment: Mapping[str, bool]) -> bool:
    if formula.kind is BoolKind.ATOM:
        assert formula.atom_id is not None
        return assignment[formula.atom_id]
    if formula.kind is BoolKind.BOTTOM:
        return False
    if formula.kind is BoolKind.NOT:
        return not _evaluate(formula.children[0], assignment)
    if formula.kind is BoolKind.AND:
        return _evaluate(formula.children[0], assignment) and _evaluate(formula.children[1], assignment)
    if formula.kind is BoolKind.OR:
        return _evaluate(formula.children[0], assignment) or _evaluate(formula.children[1], assignment)
    if formula.kind is BoolKind.IMPLIES:
        return (not _evaluate(formula.children[0], assignment)) or _evaluate(formula.children[1], assignment)
    raise AssertionError(f"unhandled Boolean kind: {formula.kind}")


def is_satisfiable(formula: BoolFormula, *, max_atoms: int = 20) -> bool:
    """Exact truth-table SAT for an intentionally bounded classical fragment."""
    atoms = _atoms(formula)
    if len(atoms) > max_atoms:
        raise ValueError(f"bounded SAT supports at most {max_atoms} distinct atoms")
    for bits in product((False, True), repeat=len(atoms)):
        assignment = dict(zip(atoms, bits))
        if _evaluate(formula, assignment):
            return True
    return False


def conjunction(formulas: Sequence[BoolFormula]) -> BoolFormula:
    if not formulas:
        return BoolFormula.not_(BoolFormula.bottom())
    out = formulas[0]
    for formula in formulas[1:]:
        out = BoolFormula.and_(out, formula)
    return out


def pairwise_compatible(formulas: Sequence[BoolFormula], *, max_atoms: int = 20) -> bool:
    """Diagnostic pairwise SAT. True does not imply global consistency."""
    for i in range(len(formulas)):
        for j in range(i + 1, len(formulas)):
            if not is_satisfiable(BoolFormula.and_(formulas[i], formulas[j]), max_atoms=max_atoms):
                return False
    return True


def globally_consistent(formulas: Sequence[BoolFormula], *, max_atoms: int = 20) -> bool:
    """Exact bounded satisfiability of the conjunction of every formula."""
    return is_satisfiable(conjunction(formulas), max_atoms=max_atoms)
