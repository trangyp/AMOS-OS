# Formal boundaries

Let `O` be the set of effects observed by the bounded static analyzer and `A` the declared allowed-effect set.

The implemented containment predicate is the set inclusion test `C := O subseteq A`.

This is established mathematics over the analyzer-produced sets. The difficult premise is analyzer completeness: `O` may omit runtime behavior hidden behind reflection, dynamic imports, native code, external tools, generated code, or unsupported languages. Therefore `C` proves only containment of the analyzer's observed effect abstraction.

Verdicts:
- `VIOLATION`: `O` contains an effect outside `A`, or source cannot be parsed.
- `UNKNOWN`: no violation found but unresolved dynamic behavior exists.
- `CONTAINED`: `O subseteq A` and no modeled dynamic gap was detected.

Never infer semantic correctness, maliciousness absence, runtime authorization, or deployment safety from `CONTAINED`.
