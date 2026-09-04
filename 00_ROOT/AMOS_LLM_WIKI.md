---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: Amos Llm Wiki
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# AMOS LLM Wiki

Schema for an LLM-maintained, compounding knowledge wiki inside the AMOS Obsidian vault, adapted from Andrej Karpathy's [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

> **Integrity boundary:** This artifact is classified by the supplied source as `DECISION / AMOS_MODEL`, with `confidence: DERIVED` and RSCF state `SOURCE_CLAIM`. The external gist is provenance for the adaptation; it does not by itself validate AMOS-specific implementation, runtime behavior, or canonical authority.

______________________________________________________________________

## Core idea

The AMOS vault is already a structured knowledge base. This schema adds a dedicated **compounding wiki** subsystem where the LLM reads a source once, extracts the key information, and integrates it into an evolving, cross-linked set of markdown pages.

Queries are answered from the wiki, not by re-parsing raw sources. Good answers are filed back into the wiki so explorations also compound.

### Source-declared processing spine

\[
\\boxed{
\\text{Raw Source}
\\rightarrow
\\text{Extract}
\\rightarrow
\\text{Integrate}
\\rightarrow
\\text{Cross-Link}
\\rightarrow
\\text{Wiki}
\\rightarrow
\\text{Query}
\\rightarrow
\\text{Reusable Knowledge}
}
\]

The final feedback step is:

\[
\\boxed{
\\text{Useful Answer}
\\rightarrow
\\text{Wiki Update}
}
\]

so the conceptual system forms a recursive knowledge-maintenance loop:

\[
\\boxed{
W_t
\\xrightarrow{\\text{ingest/query}}
W\_{t+1}
}
\]

where (W_t) denotes the wiki state at logical time (t).

This notation is a **DERIVED FORMALIZATION** of the supplied workflow, not a claim that the current vault implements an executable state-transition engine.

______________________________________________________________________

## 1. Layers

| Layer       | Path                          | Owner                  | Rule                                                                  |
| ----------- | ----------------------------- | ---------------------- | --------------------------------------------------------------------- |
| Raw sources | `11_KNOWLEDGE/LLM_WIKI/raw/`  | Human / clipping tools | Immutable. Source of truth. Do not edit after first write.            |
| The wiki    | `11_KNOWLEDGE/LLM_WIKI/wiki/` | LLM                    | Generated and maintained by the LLM on every ingest, query, and lint. |
| The schema  | `00_ROOT/AMOS_LLM_WIKI.md`    | Human + LLM            | Conventions, workflows, and file formats.                             |

## 1.1 Layer separation

Let:

\[
R=\\text{raw-source layer}
\]

\[
W=\\text{wiki layer}
\]

\[
S=\\text{schema layer}
\]

The supplied architecture establishes three distinct roles:

\[
\\boxed{
R\\neq W\\neq S
}
\]

More precisely:

\[
\\operatorname{Owner}(R)=\\text{Human / clipping tools}
\]

\[
\\operatorname{Owner}(W)=\\text{LLM}
\]

\[
\\operatorname{Owner}(S)=\\text{Human + LLM}
\]

and:

\[
\\boxed{
\\operatorname{Immutable}(R)
}
\]

is source-declared.

Therefore a derived wiki page must not silently replace its raw provenance:

\[
\\boxed{
W_i \\neq R_j
}
\]

even when:

\[
W_i \\xleftarrow{\\mathrm{DERIVED_FROM}} R_j
\]

______________________________________________________________________

## 2. Raw-Source Integrity

The raw-source layer is declared immutable after first write.

For raw source (r):

\[
r\\in R
\\Rightarrow
\\operatorname{Immutable}(r)
\]

After initial persistence:

\[
\\boxed{
\\Delta r = 0
}
\]

for wiki-maintenance operations.

This does **not** mathematically prove that the filesystem enforces immutability. It expresses the source-declared schema rule.

Therefore:

\[
\\boxed{
\\text{DECLARED IMMUTABLE}
\\neq
\\text{EXECUTABLY ENFORCED IMMUTABLE}
}
\]

unless an implementation binding independently establishes enforcement.

______________________________________________________________________

## 3. Source of Truth vs Derived Knowledge

The raw layer is declared the source of truth.

Thus the knowledge topology is conceptually:

\[
R
\\rightarrow
W
\]

rather than:

\[
W
\\rightarrow
R
\]

for provenance authority.

A wiki synthesis (w) derived from raw sources:

\[
r_1,\\ldots,r_n
\]

can be represented:

\[
w=f(r_1,\\ldots,r_n)
\]

but:

\[
\\boxed{
w
\\not\\equiv
{r_1,\\ldots,r_n}
}
\]

The synthesis remains a derived representation.

A load-bearing conclusion (c) contained in (w) should therefore remain traceable to its supporting provenance:

\[
c
\\rightarrow
P(c)
\\subseteq
{r_1,\\ldots,r_n}
\]

where (P(c)) denotes the source dependencies supporting (c).

______________________________________________________________________

## 4. Conventions

Source-declared conventions:

- Use the standard AMOS YAML frontmatter: `title`, `type`, `source`, `tags`, `rscf`.
- Use Obsidian wikilinks for cross-references.
- One concept per page. Keep pages focused enough to link.
- Raw-source pages use `rscf.state: SOURCE_CLAIM` and `rscf.claim_class: SOURCE_CLAIM`.
- Synthesized/derived pages use `rscf.state: DERIVED` and `rscf.claim_class: AMOS_MODEL`.
- Store attachments under `raw/assets/`.
- Use the `LLM_WIKI_` filename prefix for wiki-wide files to avoid name collisions.

## 4.1 Epistemic typing

For raw-source page (r):

\[
\\boxed{
\\operatorname{RSCFState}(r)=\\texttt{SOURCE_CLAIM}
}
\]

\[
\\boxed{
\\operatorname{ClaimClass}(r)=\\texttt{SOURCE_CLAIM}
}
\]

For synthesized page (w):

\[
\\boxed{
\\operatorname{RSCFState}(w)=\\texttt{DERIVED}
}
\]

\[
\\boxed{
\\operatorname{ClaimClass}(w)=\\texttt{AMOS_MODEL}
}
\]

Therefore:

## \[ \\boxed{ \\operatorname{DerivedFrom}(w,r) \\not\\Rightarrow \\operatorname{ClaimClass}(w)

\\operatorname{ClaimClass}(r)
}
\]

The provenance relationship and epistemic classification are separate dimensions.

______________________________________________________________________

## 5. One Concept Per Page

Let:

\[
C={c_1,\\ldots,c_n}
\]

be concepts represented in the wiki and:

\[
P={p_1,\\ldots,p_m}
\]

be wiki pages.

The source convention aims conceptually toward:

\[
f:C\\rightarrow P
\]

where each focused concept has a page suitable for linking.

This should not be strengthened into a strict bijection because the source does not state that every page must contain exactly one and only one atomic semantic object.

The strongest safe interpretation is:

\[
\\boxed{
\\text{page focus}
\\rightarrow
\\text{concept-level linkability}
}
\]

______________________________________________________________________

## 6. Wikilink Graph

The wiki can be represented as a knowledge graph:

\[
G_W=(V,E)
\]

where:

\[
V=\\text{wiki pages}
\]

and:

\[
E=\\text{Obsidian wikilinks}
\]

A link:

\[
p_i\\rightarrow p_j
\]

establishes a navigational/declared relation.

It does **not** automatically establish:

\[
\\operatorname{Supports}(p_i,p_j)
\]

nor:

\[
\\operatorname{Causes}(p_i,p_j)
\]

nor:

\[
\\operatorname{Validates}(p_i,p_j)
\]

Thus:

\[
\\boxed{
\\text{WIKILINK}
\\neq
\\text{EVIDENCE EDGE}
}
\]

unless explicitly typed as such.

______________________________________________________________________

## 7. Operations

## Ingest

1. Place or clip the source into `11_KNOWLEDGE/LLM_WIKI/raw/`.
1. Create or update a source-summary page in `11_KNOWLEDGE/LLM_WIKI/wiki/`.
1. Update relevant entity, concept, and synthesis pages.
1. Update the wiki index.
1. Append an entry to the wiki log.

### 7.1 Formal ingest transformation

Let:

\[
I(r,W_t)
\]

denote ingestion of raw source (r) into wiki state (W_t).

Then conceptually:

\[
\\boxed{
I(r,W_t)
\\rightarrow
W\_{t+1}
}
\]

subject to:

\[
r\\in R
\]

and:

\[
\\operatorname{Immutable}(r)
\]

The wiki update may affect a subset:

## \[ \\Delta W

{
\\text{summary},
\\text{entities},
\\text{concepts},
\\text{syntheses},
\\text{index},
\\text{log}
}
\]

where only result-relevant elements need change.

The raw source itself is outside that mutation set:

\[
\\boxed{
r\\notin\\Delta W
}
\]

______________________________________________________________________

## 8. Ingest Provenance

For every derived page (w) materially updated from source (r), provenance should conceptually preserve:

\[
r
\\xrightarrow{\\mathrm{DERIVED_INTO}}
w
\]

If multiple wiki pages derive from the same raw source:

\[
r\\rightarrow w_1
\]

\[
r\\rightarrow w_2
\]

then (w_1) and (w_2) are not independent evidence merely because they are distinct pages.

Thus:

\[
\\boxed{
\\operatorname{SharedSource}(w_1,w_2)
\\Rightarrow
\\neg\\operatorname{AssumeIndependent}(w_1,w_2)
}
\]

This is a **DERIVED AMOS provenance requirement** consistent with the supplied raw/derived separation.

______________________________________________________________________

## 9. Query

Source-declared workflow:

1. Read the wiki index to find relevant pages.
1. Read those pages and synthesize an answer with citations.
1. If the answer has lasting value, file it back as a new wiki page and update the index/log.

Conceptually:

\[
q
\\rightarrow
\\operatorname{Retrieve}(q,W)
\\rightarrow
W_q
\\rightarrow
\\operatorname{Synthesize}(W_q)
\\rightarrow
a
\]

where:

- (q) = query;
- (W) = available wiki;
- (W_q\\subseteq W) = retrieved relevant pages;
- (a) = synthesized answer.

The architecture explicitly prefers:

\[
\\boxed{
\\text{Query}
\\rightarrow
\\text{Wiki}
}
\]

rather than repeatedly:

\[
\\text{Query}
\\rightarrow
\\text{Raw corpus re-parsing}
\]

under ordinary operation.

______________________________________________________________________

## 10. Smallest Sufficient Retrieval

**DERIVED AMOS FORMALIZATION**

For query (q), let:

\[
W_q^\*
\\subseteq
W
\]

be the smallest sufficient set of wiki pages whose dependency closure can materially determine the answer.

Then:

## \[ \\boxed{ A(q)

F(q,W_q^\*)
}
\]

when the wiki contains sufficient support.

Raw evidence should be escalated to only when required by:

- unresolved provenance;
- contradiction;
- stale synthesis;
- missing detail;
- source-verification need;
- scope/regime mismatch;
- consequential validation;
- or absent wiki support.

Thus:

\[
\\boxed{
\\text{Wiki first}
\\rightarrow
\\text{Raw evidence when required}
}
\]

This is a derived AMOS runtime interpretation of the source architecture.

______________________________________________________________________

## 11. Query Provenance

An answer should not cite a derived page as though it were independent raw evidence when the underlying source is decision-relevant.

For answer (a):

\[
P(a)={p_1,\\ldots,p_n}
\]

should preserve enough lineage to recover the load-bearing source ancestry.

A conceptual dependency chain is:

\[
a
\\rightarrow
w
\\rightarrow
r
\]

where:

\[
a=\\text{answer}
\]

\[
w=\\text{wiki synthesis}
\]

\[
r=\\text{raw source}
\]

This supports provenance recovery without requiring raw-source loading for every ordinary query.

______________________________________________________________________

## 12. Filing Valuable Answers Back

If synthesized answer (a) has lasting value, the source workflow permits:

\[
a\\rightarrow w\_{new}
\]

followed by:

\[
W\_{t+1}=W_t\\cup{w\_{new}}
\]

plus index/log updates.

However:

\[
\\boxed{
\\text{ANSWER}
\\rightarrow
\\text{WIKI PAGE}
}
\]

does not mean:

\[
\\boxed{
\\text{ANSWER}
\\rightarrow
\\text{VERIFIED FACT}
}
\]

The resulting page must retain its correct epistemic classification.

For synthesized pages:

## \[ \\operatorname{RSCFState}(w\_{new})

\\texttt{DERIVED}
\]

## \[ \\operatorname{ClaimClass}(w\_{new})

\\texttt{AMOS_MODEL}
\]

unless a different classification is independently justified.

______________________________________________________________________

## 13. Compounding Knowledge

The supplied design describes a compounding wiki.

A derived structural representation is:

## \[ W\_{t+1}

\\mathcal U(W_t,E_t,Q_t)
\]

where:

- (E_t) = newly ingested source information;
- (Q_t) = lasting knowledge generated through queries;
- (\\mathcal U) = wiki update operation.

The term “compounding” here describes accumulation and integration of reusable knowledge.

It does not establish monotonic truth growth:

\[
\\boxed{
|W\_{t+1}|>|W_t|
\\not\\Rightarrow
\\operatorname{Truth}(W\_{t+1})

>

\\operatorname{Truth}(W_t)
}
\]

More pages can increase stored information while also introducing duplication, stale claims, or contradiction.

Hence lint and provenance remain necessary.

______________________________________________________________________

## 14. Lint

Source-declared lint workflow:

1. Scan for orphan pages, broken wikilinks, and missing concept pages.
1. Flag contradictions between pages and stale claims that newer sources have superseded.
1. Suggest new questions or sources to close gaps.
1. Append findings to the wiki log.

Let:

\[
L(W)
\]

be the conceptual lint operation.

Then:

\[
L(W)
\\rightarrow
(
O,
B,
M,
C,
S,
G
)
\]

where, as a **DERIVED FORMALIZATION**:

- (O) = orphan findings;
- (B) = broken-link findings;
- (M) = missing-concept findings;
- (C) = contradiction findings;
- (S) = stale-claim findings;
- (G) = identified knowledge gaps.

______________________________________________________________________

## 15. Contradiction Preservation

If two pages support incompatible claims:

\[
w_1\\models c
\]

and:

\[
w_2\\models\\neg c
\]

lint should flag the contradiction rather than silently collapse it.

If neither claim dominates through provenance, scope, freshness, or stronger evidence:

\[
\\boxed{
\\operatorname{State}(c)=\\texttt{COMPETING}
}
\]

If support is insufficient:

\[
\\boxed{
\\operatorname{State}(c)=\\texttt{UNKNOWN/GAP}
}
\]

Therefore:

\[
\\boxed{
\\text{LINT}
\\neq
\\text{FORCED CONSENSUS}
}
\]

______________________________________________________________________

## 16. Stale Claims

Let claim (c) be derived from source state at time (t_0).

A newer source at (t_1>t_0) does not automatically falsify (c), but it can invalidate its freshness assumptions.

Thus:

\[
\\operatorname{Newer}(r_2,r_1)
\\not\\Rightarrow
\\operatorname{False}(r_1)
\]

while:

\[
\\operatorname{Supersedes}(r_2,r_1)
\]

may require descendants of (r_1) to be revalidated.

Only dependent conclusions should be invalidated:

\[
\\boxed{
\\operatorname{Invalidate}(r_1)
\\Rightarrow
\\operatorname{Revalidate}(\\operatorname{Descendants}(r_1))
}
\]

not the entire wiki.

______________________________________________________________________

## 17. Gap Closure

Lint may suggest questions or sources to close gaps.

Let:

\[
G={g_1,\\ldots,g_n}
\]

be unresolved gaps.

A high-information source (e) is useful when it discriminates among competing possibilities:

\[
\\operatorname{IG}(e;G)>0
\]

where (\\operatorname{IG}) denotes conceptual information gain.

This is a **DERIVED FORMALIZATION**, not a source-defined numerical metric.

The architecture should prefer evidence that can change the conclusion over redundant repetition.

______________________________________________________________________

## 18. Special Files

Source-declared:

- `11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_INDEX.md` — content-oriented catalog of all wiki pages.
- `11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG.md` — chronological, append-only activity log.

## 18.1 Index

Let:

\[
\\mathcal I_W
\]

denote the wiki index.

Conceptually:

\[
\\mathcal I_W:
\\text{concept/query}
\\rightarrow
\\text{candidate wiki pages}
\]

The index supports retrieval.

It is not itself equivalent to the knowledge content:

\[
\\boxed{
\\mathcal I_W\\neq W
}
\]

______________________________________________________________________

## 19. Append-Only Log

Let:

\[
\\mathcal L_t
\]

denote the activity log at logical time (t).

Append-only semantics can be represented:

## \[ \\boxed{ \\mathcal L\_{t+1}

\\mathcal L_t
\\Vert
e\_{t+1}
}
\]

where (\\Vert) denotes ordered append.

Therefore previous entries remain part of the historical record.

The source declares append-only behavior, but executable append-only enforcement is not established by this schema alone.

Thus:

\[
\\boxed{
\\text{DECLARED APPEND-ONLY}
\\neq
\\text{PROVEN STORAGE IMMUTABILITY}
}
\]

______________________________________________________________________

## 20. Index/Log Separation

The index and log have different semantics:

\[
\\boxed{
\\text{INDEX}
\\neq
\\text{LOG}
}
\]

The index answers approximately:

\[
\\text{“What knowledge pages exist and where?”}
\]

The log answers approximately:

\[
\\text{“What wiki activity occurred over time?”}
\]

Therefore an index update must not substitute for historical logging, and log presence does not establish content validity:

\[
\\boxed{
\\text{LOGGED}
\\neq
\\text{VALIDATED}
}
\]

______________________________________________________________________

## 21. Optional Tooling

Source-declared optional tooling:

- Obsidian Web Clipper for clipping web sources to markdown.
- `qmd` (local hybrid search) when the wiki grows beyond a few hundred pages.
- Dataview for dynamic tables over YAML frontmatter.

These are optional:

\[
\\boxed{
\\operatorname{Useful}(T)
\\not\\Rightarrow
\\operatorname{Required}(T)
}
\]

unless a later canonical workflow explicitly promotes the tool to a required dependency.

The source phrase “beyond a few hundred pages” is guidance, not a validated universal performance threshold.

______________________________________________________________________

## 22. AMOS Canonical Bindings

The source declares that the LLM Wiki is operationalized through AMOS canonical skill/workflow/agent bindings:

- Skill: `.devin/skills/amos-llm-wiki/SKILL.md` — runtime capability
- Workflow: `.devin/workflows/amos-llm-wiki-workflow.md` — operational sequence
- Agent: `.devin/agents/amos-llm-wiki-agent.json` — execution contract
- Tools: `14_TOOLS/AMOS_LLM_WIKI_TOOL.md` — supporting tooling

Let:

\[
K=\\text{skill binding}
\]

\[
F=\\text{workflow binding}
\]

\[
A=\\text{agent binding}
\]

\[
T=\\text{tool binding}
\]

The source architecture is therefore:

\[
\\boxed{
\\text{Schema}
\+
K
\+
F
\+
A
\+
T
}
\]

as its declared operational binding structure.

However, the supplied note does not independently demonstrate that each referenced file exists, is current, is executable, or has passed validation.

Therefore:

\[
\\boxed{
\\text{DECLARED BINDING}
\\neq
\\text{INDEPENDENTLY VERIFIED BINDING}
}
\]

within this artifact alone.

______________________________________________________________________

## 23. Capability vs Authority

The skill is described as runtime capability.

AMOS integrity requires:

\[
\\boxed{
\\operatorname{Capability}(K)
\\not\\Rightarrow
\\operatorname{Authority}(K)
}
\]

Thus possession of a wiki-maintenance skill does not by itself authorize every possible vault mutation.

Operational authority must remain separately governed where consequential actions require it.

______________________________________________________________________

## 24. Workflow vs Execution

A workflow describes an operational sequence.

Therefore:

\[
\\boxed{
\\operatorname{WorkflowDefined}(F)
\\not\\Rightarrow
\\operatorname{WorkflowExecuted}(F)
}
\]

and:

\[
\\boxed{
\\operatorname{WorkflowExecuted}(F)
\\not\\Rightarrow
\\operatorname{WorkflowValidated}(F)
}
\]

unless execution and validation evidence independently establish those states.

______________________________________________________________________

## 25. Agent Contract vs Runtime Compliance

The agent binding is described as an execution contract.

Therefore:

\[
\\boxed{
\\operatorname{ContractExists}(A)
\\not\\Rightarrow
\\operatorname{RuntimeCompliant}(A)
}
\]

Runtime compliance requires evidence from actual execution or a valid enforcement mechanism.

______________________________________________________________________

## 26. Tool Binding vs Tool Correctness

Similarly:

\[
\\boxed{
\\operatorname{ToolDeclared}(T)
\\not\\Rightarrow
\\operatorname{ToolValidated}(T)
}
\]

A tooling reference establishes architectural placement, not empirical correctness.

______________________________________________________________________

## 27. Wiki Query Sufficiency

A query should be answered from the wiki when the wiki contains sufficient support.

Let:

\[
E_W(q)
\]

denote the evidence available through retrieved wiki pages.

If:

\[
\\operatorname{Sufficient}(E_W(q))
\]

then ordinary raw-source reparsing is unnecessary.

If:

\[
\\neg\\operatorname{Sufficient}(E_W(q))
\]

then the architecture should expose the gap or escalate to raw evidence.

Thus:

\[
\\boxed{
\\neg\\operatorname{Sufficient}(E_W(q))
\\Rightarrow
\\texttt{GAP}
\\lor
\\operatorname{EscalateToRaw}
}
\]

This is a **DERIVED operational formalization**.

______________________________________________________________________

## 28. Confidence Ceiling

For derived answer (a) depending on load-bearing claims:

\[
c_1,\\ldots,c_n
\]

the AMOS confidence ceiling is:

\[
\\boxed{
\\operatorname{Conf}(a)
\\le
\\min_i
\\operatorname{Conf}(c_i)
}
\]

unless a weak premise is independently revalidated.

A wiki synthesis cannot increase confidence merely by repeating the same underlying source across multiple descendant pages.

______________________________________________________________________

## 29. Provenance Topology

Suppose:

\[
r\\rightarrow w_1
\]

\[
r\\rightarrow w_2
\]

\[
w_1,w_2\\rightarrow a
\]

Then the answer does not have two independent source roots.

Its provenance root count is still:

\[
1
\]

for that evidence branch.

Therefore:

\[
\\boxed{
|\\text{citations}|
\\neq
|\\text{independent provenance roots}|
}
\]

This protects the wiki against apparent confirmation created by recursive self-citation.

______________________________________________________________________

## 30. Recursive Self-Citation Firewall

A compounding wiki creates a specific provenance risk.

Suppose:

\[
r\\rightarrow w_1
\]

then:

\[
w_1\\rightarrow w_2
\]

then:

\[
w_2\\rightarrow w_3
\]

The presence of three wiki pages does not create three confirmations:

\[
\\boxed{
w_1+w_2+w_3
\\neq
3\\times\\text{independent evidence}
}
\]

Their ancestry must remain recoverable to (r).

This is essential for preventing provenance amplification.

______________________________________________________________________

## 31. Wiki Update Atomicity

**DERIVED / PROPOSED**

An ingest may logically affect:

\[
{
\\text{summary},
\\text{concept pages},
\\text{entity pages},
\\text{synthesis pages},
\\text{index},
\\text{log}
}
\]

If partial mutation could leave the wiki inconsistent, a future implementation should treat the logically coupled update as one governed mutation unit.

Conceptually:

\[
U=
{
u_1,\\ldots,u_n
}
\]

with desired invariant:

\[
\\boxed{
\\operatorname{Commit}(U)
\\Rightarrow
\\bigwedge_i
\\operatorname{Valid}(u_i)
}
\]

This is a proposed implementation property, **not** a claim that the current wiki has transactional or distributed atomicity.

______________________________________________________________________

## 32. Failure Recovery

If an update fails at one dependent component, unaffected valid knowledge should be preserved.

For failed premise (p):

\[
\\neg\\operatorname{Valid}(p)
\]

invalidate only conclusions whose dependency graph includes (p):

\[
\\operatorname{Invalidate}
\\left(
\\operatorname{Descendants}(p)
\\right)
\]

while:

\[
\\boxed{
\\operatorname{Preserve}
\\left(
W\\setminus\\operatorname{Descendants}(p)
\\right)
}
\]

This is a **DERIVED AMOS recovery formalization**.

______________________________________________________________________

## 33. Wiki Quality Is Not Page Count

Let:

\[
N_W=|W|
\]

be the number of wiki pages.

Then:

\[
\\boxed{
N_W\\uparrow
\\not\\Rightarrow
\\text{knowledge quality}\\uparrow
}
\]

because page growth may include:

- duplication;
- stale information;
- unsupported synthesis;
- broken provenance;
- contradiction;
- orphan pages.

Thus the architecture is better represented as compounding **maintained knowledge**, not simply compounding document count.

______________________________________________________________________

## 34. Decision-Relevant Knowledge Density

**DERIVED MODEL**

A conceptual AMOS wiki efficiency quantity may be written:

## \[ \\eta_W

\\frac{
\\text{decision-relevant valid reusable knowledge}
}{
\\text{retrieval + reprocessing + maintenance cost}
}
\]

No numerical definition or benchmark for (\\eta_W) is supplied.

Therefore:

## \[ \\boxed{ \\eta_W

\\text{MODEL ONLY}
}
\]

It must not be presented as a validated universal metric.

______________________________________________________________________

## 35. Source-to-Wiki Semantic Preservation

Let:

\[
E:R\\rightarrow W
\]

represent extraction/integration from raw source to wiki representation.

A desirable property is preservation of load-bearing distinctions:

\[
D(E(r))
\\supseteq
D^\*(r)
\]

where (D^\*(r)) denotes the source distinctions necessary for supported downstream conclusions.

A conceptual semantic-loss quantity is:

## \[ L\_{\\mathrm{sem}}

d(D^\*(r),D(E(r)))
\]

with desired behavior:

\[
L\_{\\mathrm{sem}}\\rightarrow 0
\]

for load-bearing distinctions.

This is a **DERIVED MODEL**, not a source-defined metric.

______________________________________________________________________

## 36. No Canonicalization by Repetition

Repeated wiki use does not automatically promote a derived page into canon.

If page (w) is queried (n) times:

\[
Q(w)=n
\]

then:

\[
\\boxed{
Q(w)\\gg1
\\not\\Rightarrow
\\operatorname{Canonical}(w)
}
\]

Similarly:

\[
\\boxed{
\\operatorname{Popular}(w)
\\not\\Rightarrow
\\operatorname{Verified}(w)
}
\]

Canonicality and verification require their own governance/evidence paths.

______________________________________________________________________

## 37. External Provenance Boundary

The supplied artifact identifies:

```text
provenance:
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
```

and:

```text
rscf.provenance: karpathy_gist
```

Therefore the external gist is a declared provenance root for the adaptation.

However:

$$
\boxed{
\operatorname{AdaptedFrom}(AMOS\_LLM\_WIKI,G)
\not\Rightarrow
\operatorname{AllAMOSRulesAuthoredBy}(G)
}
$$

The supplied artifact contains AMOS-specific paths, RSCF classifications, bindings, and conventions beyond what can be attributed to the external provenance without source comparison.

Those AMOS-specific adaptations remain part of this artifact's declared model.

______________________________________________________________________

## 38. Source Verification Boundary

This reformat does not independently establish:

- the exact current contents of the external gist;
- whether the gist has changed since adaptation;
- whether every AMOS-specific statement directly corresponds to the gist;
- whether every declared skill/workflow/agent/tool binding currently exists;
- whether those bindings are implemented;
- whether they are validated;
- whether runtime immutability or append-only enforcement exists.

Therefore these remain outside the verified scope of this transformation.

______________________________________________________________________

## 39. Gaps

## Source-visible / directly implied gaps

```yaml
external_source_current_content: NOT_INDEPENDENTLY_VALIDATED
raw_immutability_runtime_enforcement: NOT_ESTABLISHED
log_append_only_runtime_enforcement: NOT_ESTABLISHED
skill_binding_runtime_validation: NOT_ESTABLISHED
workflow_binding_runtime_validation: NOT_ESTABLISHED
agent_binding_runtime_validation: NOT_ESTABLISHED
tool_binding_runtime_validation: NOT_ESTABLISHED
```

## Derived / proposed gap register

```yaml
wiki_transaction_model: UNKNOWN/GAP
wiki_atomic_update_binding: NOT_ESTABLISHED
provenance_graph_storage_schema: UNKNOWN/GAP
provenance_independence_validator: NOT_ESTABLISHED
freshness_policy: UNKNOWN/GAP
supersession_policy: UNKNOWN/GAP
conflict_resolution_policy: UNKNOWN/GAP
scope_compatibility_policy: UNKNOWN/GAP
regime_compatibility_policy: UNKNOWN/GAP
query_sufficiency_threshold: UNKNOWN/GAP
raw_escalation_policy: UNKNOWN/GAP
semantic_loss_metric: MODEL_ONLY
knowledge_density_metric: MODEL_ONLY
rollback_binding: NOT_ESTABLISHED
```

______________________________________________________________________

## 40. Derived Validation Conditions

The following are **DERIVED VALIDATION CONDITIONS**, not source-declared falsifiers.

### DVC1 — Raw source mutated by wiki maintenance

$$
r_t\neq r_{t+1}
$$

because an ordinary wiki-maintenance operation rewrote the source.

This violates the source-declared raw immutability rule.

### DVC2 — Derived page represented as raw source

$$
w\in W
\Rightarrow
\operatorname{ClaimClass}(w)=\texttt{SOURCE\_CLAIM}
$$

without independent basis.

Invalid under the supplied conventions.

### DVC3 — Raw page represented as synthesized model

A raw-source page is silently reclassified as `DERIVED / AMOS_MODEL`.

Invalid unless explicitly transformed into a separate derived artifact.

### DVC4 — Multiple descendants treated as independent evidence

$$
r\rightarrow w_1,w_2
$$

and (w_1,w_2) are counted as independent confirmation.

Invalid.

### DVC5 — Wiki link treated as evidence

$$
w_1\rightarrow w_2
\Rightarrow
\operatorname{Supports}(w_1,w_2)
$$

without a typed support relation.

Invalid.

### DVC6 — More pages treated as higher truth

$$
|W|\uparrow
\Rightarrow
\operatorname{Truth}(W)\uparrow
$$

Invalid.

### DVC7 — Old claim silently overwritten

A newer source changes a claim and historical/provenance lineage disappears.

Invalid under provenance-preserving AMOS operation.

### DVC8 — Contradiction silently merged

Incompatible supported claims become one fluent conclusion without discriminating evidence.

Invalid.

### DVC9 — Skill capability treated as authority

$$
\operatorname{SkillAvailable}
\Rightarrow
\operatorname{AuthorizedMutation}
$$

Invalid.

### DVC10 — Answer filing treated as verification

$$
\operatorname{FiledIntoWiki}(a)
\Rightarrow
\operatorname{Verified}(a)
$$

Invalid.

______________________________________________________________________

## 41. Derived / Proposed Operational State Machine

The supplied workflows can be represented conceptually as:

$$
\texttt{RAW\_CAPTURED}
\rightarrow
\texttt{SUMMARIZED}
\rightarrow
\texttt{INTEGRATED}
\rightarrow
\texttt{INDEXED}
\rightarrow
\texttt{QUERYABLE}
$$

with recurring:

$$
\texttt{QUERYABLE}
\xrightarrow{\text{query}}
\texttt{ANSWER}
$$

and, where lasting value exists:

$$
\texttt{ANSWER}
\rightarrow
\texttt{INTEGRATED}
$$

Lint creates a parallel maintenance loop:

$$
\texttt{QUERYABLE}
\xrightarrow{\text{lint}}
\{
\texttt{CLEAN},
\texttt{GAP},
\texttt{STALE},
\texttt{COMPETING},
\texttt{BROKEN\_LINK},
\texttt{ORPHAN}
\}
$$

These labels are **DERIVED / PROPOSED** and are not source-declared canonical AMOS state enums.

______________________________________________________________________

## 42. RSCF

## Source-declared RSCF

```yaml
rscf:
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance: karpathy_gist
  scope: AMOS_knowledge
```

## Derived / proposed RSCF expansion

```yaml
RSCF:
  artifact:
    artifact_id: AMOS-LLM-WIKI
    title: AMOS LLM Wiki
    name: AMOS LLM Wiki
    type: schema
    source: 00_ROOT
    status: active

  stewardship:
    origin_architect: Trang Phan
    steward: Trang Phan

  epistemic:
    conclusion_class: DECISION / AMOS_MODEL
    confidence: DERIVED
    source_state: SOURCE_CLAIM
    source_claim_class: AMOS_MODEL

  provenance:
    declared_root:
      - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
    rscf_provenance: karpathy_gist
    independence: NOT_ESTABLISHED

  H:
    domain: AMOS_knowledge

    purpose: >
      Maintain a compounding, cross-linked LLM wiki over immutable
      raw knowledge sources inside the AMOS Obsidian vault.

    architecture:
      raw_layer: 11_KNOWLEDGE/LLM_WIKI/raw/
      wiki_layer: 11_KNOWLEDGE/LLM_WIKI/wiki/
      schema: 00_ROOT/AMOS_LLM_WIKI.md

    primary_boundary:
      - RAW_SOURCE_NOT_DERIVED_PAGE
      - SOURCE_CLAIM_NOT_DERIVED
      - WIKILINK_NOT_EVIDENCE
      - CAPABILITY_NOT_AUTHORITY
      - LOGGED_NOT_VALIDATED

  M:
    operations:
      ingest:
        source: raw/
        outputs:
          - source_summary
          - entity_pages
          - concept_pages
          - synthesis_pages
          - index_update
          - log_append

      query:
        retrieval_source: wiki
        output: cited_synthesis
        persistent_value:
          action: FILE_BACK_TO_WIKI

      lint:
        checks:
          - orphan_pages
          - broken_wikilinks
          - missing_concept_pages
          - contradictions
          - stale_claims
          - gaps

    epistemic_typing:
      raw:
        state: SOURCE_CLAIM
        claim_class: SOURCE_CLAIM

      synthesis:
        state: DERIVED
        claim_class: AMOS_MODEL

    special_files:
      index:
        path: 11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_INDEX.md
        role: content_catalog

      log:
        path: 11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG.md
        role: chronological_activity_log
        mutation: APPEND_ONLY_DECLARED

    bindings:
      skill:
        path: .devin/skills/amos-llm-wiki/SKILL.md
        role: runtime_capability
        runtime_validation: NOT_ESTABLISHED_FROM_THIS_ARTIFACT

      workflow:
        path: .devin/workflows/amos-llm-wiki-workflow.md
        role: operational_sequence
        runtime_validation: NOT_ESTABLISHED_FROM_THIS_ARTIFACT

      agent:
        path: .devin/agents/amos-llm-wiki-agent.json
        role: execution_contract
        runtime_validation: NOT_ESTABLISHED_FROM_THIS_ARTIFACT

      tools:
        path: 14_TOOLS/AMOS_LLM_WIKI_TOOL.md
        role: supporting_tooling
        runtime_validation: NOT_ESTABLISHED_FROM_THIS_ARTIFACT

  L:
    invariants:
      - RAW_SOURCE_IMMUTABLE_BY_SCHEMA
      - RAW_PROVENANCE_PRESERVED
      - DERIVED_PAGES_TYPED_DERIVED
      - SOURCE_PAGES_TYPED_SOURCE_CLAIM
      - QUERY_FROM_WIKI_BY_DEFAULT
      - LASTING_ANSWERS_MAY_COMPOUND
      - LINT_PRESERVES_CONTRADICTIONS
      - SHARED_ANCESTRY_NOT_INDEPENDENT_CONFIRMATION

    gaps:
      executable_immutability: NOT_ESTABLISHED
      executable_append_only_log: NOT_ESTABLISHED
      freshness_policy: UNKNOWN/GAP
      conflict_resolution_policy: UNKNOWN/GAP
      provenance_independence_validator: NOT_ESTABLISHED
      atomic_update_binding: NOT_ESTABLISHED
      rollback_binding: NOT_ESTABLISHED
```

______________________________________________________________________

## 43. RSCF-NODE

Source-declared:

```yaml
RSCF-NODE:
  node_id: amos_llm_wiki
  node_type: schema
  path: 00_ROOT/AMOS_LLM_WIKI.md
  claim_class: AMOS_MODEL
```

______________________________________________________________________

## 44. RSCF-RELATIONS

## Source-declared relations

```yaml
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT_MOC|00_ROOT_MOC]]
  - INDEXED_BY: [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
  - INDEXED_BY: [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]]
  - INDEXED_BY: [[11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC|LLM_WIKI_MOC]]
```

## Derived / proposed relations

```yaml
derived_relations:
  classification: DERIVED

  relations:
    - USES_INDEX:
        target: [[11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_INDEX|LLM_WIKI_INDEX]]

    - APPENDS_ACTIVITY_TO:
        target: [[11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG|LLM_WIKI_LOG]]

    - KNOWLEDGE_CONTEXT:
        target: [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]]

    - OPERATIONALIZED_BY_SKILL:
        target: .devin/skills/amos-llm-wiki/SKILL.md
        verification: NOT_ESTABLISHED_FROM_THIS_ARTIFACT

    - OPERATIONALIZED_BY_WORKFLOW:
        target: .devin/workflows/amos-llm-wiki-workflow.md
        verification: NOT_ESTABLISHED_FROM_THIS_ARTIFACT

    - OPERATIONALIZED_BY_AGENT:
        target: .devin/agents/amos-llm-wiki-agent.json
        verification: NOT_ESTABLISHED_FROM_THIS_ARTIFACT

    - SUPPORTED_BY_TOOL:
        target: 14_TOOLS/AMOS_LLM_WIKI_TOOL.md
        verification: NOT_ESTABLISHED_FROM_THIS_ARTIFACT

    - ADAPTED_FROM:
        target: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
        relation_class: SOURCE_PROVENANCE
```

______________________________________________________________________

## 45. Machine Representation

```yaml
amos_llm_wiki:
  identity:
    artifact_id: AMOS-LLM-WIKI
    title: AMOS LLM Wiki
    type: schema
    source: 00_ROOT
    path: 00_ROOT/AMOS_LLM_WIKI.md
    node_id: amos_llm_wiki

  stewardship:
    origin_architect: Trang Phan
    steward: Trang Phan

  epistemic:
    conclusion_class: DECISION / AMOS_MODEL
    confidence: DERIVED
    rscf_state: SOURCE_CLAIM
    rscf_claim_class: AMOS_MODEL

  provenance:
    declared:
      - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
    symbolic: karpathy_gist

  layers:
    raw:
      path: 11_KNOWLEDGE/LLM_WIKI/raw/
      owner: Human / clipping tools
      immutable: DECLARED
      runtime_enforcement: NOT_ESTABLISHED

    wiki:
      path: 11_KNOWLEDGE/LLM_WIKI/wiki/
      owner: LLM
      maintained_on:
        - ingest
        - query
        - lint

    schema:
      path: 00_ROOT/AMOS_LLM_WIKI.md
      owner:
        - Human
        - LLM

  page_typing:
    raw:
      rscf_state: SOURCE_CLAIM
      claim_class: SOURCE_CLAIM

    synthesized:
      rscf_state: DERIVED
      claim_class: AMOS_MODEL

  operations:
    ingest:
      - capture_raw
      - create_or_update_summary
      - update_entities
      - update_concepts
      - update_syntheses
      - update_index
      - append_log

    query:
      - retrieve_from_index
      - read_relevant_pages
      - synthesize_with_citations
      - persist_if_lasting_value
      - update_index
      - append_log

    lint:
      - detect_orphans
      - detect_broken_links
      - detect_missing_concepts
      - detect_contradictions
      - detect_stale_claims
      - suggest_gap_closure
      - append_log

  special_files:
    index: 11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_INDEX.md
    log: 11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG.md

  attachments:
    path: 11_KNOWLEDGE/LLM_WIKI/raw/assets/

  filename_policy:
    wiki_wide_prefix: LLM_WIKI_

  optional_tools:
    - Obsidian Web Clipper
    - qmd
    - Dataview

  bindings:
    skill: .devin/skills/amos-llm-wiki/SKILL.md
    workflow: .devin/workflows/amos-llm-wiki-workflow.md
    agent: .devin/agents/amos-llm-wiki-agent.json
    tools: 14_TOOLS/AMOS_LLM_WIKI_TOOL.md

  integrity:
    raw_not_derived: true
    derived_not_source_claim: true
    wikilink_not_evidence: true
    shared_ancestry_not_independent: true
    capability_not_authority: true
    wiki_growth_not_truth_growth: true
    filing_not_verification: true
    contradiction_visibility: required
```

______________________________________________________________________

## 46. Canonical Compression

The source architecture compresses to:

$$
\boxed{
\text{RAW}
\rightarrow
\text{EXTRACT}
\rightarrow
\text{WIKI}
\rightarrow
\text{LINK}
\rightarrow
\text{QUERY}
\rightarrow
\text{SYNTHESIZE}
\rightarrow
\text{COMPOUND}
}
$$

with maintenance:

$$
\boxed{
\text{WIKI}
\xrightarrow{\text{LINT}}
\{
\text{ORPHANS},
\text{BROKEN LINKS},
\text{CONTRADICTIONS},
\text{STALE CLAIMS},
\text{GAPS}
\}
}
$$

and epistemic separation:

$$
\boxed{
\text{RAW}
=
\texttt{SOURCE\_CLAIM}
}
$$

$$
\boxed{
\text{SYNTHESIS}
=
\texttt{DERIVED / AMOS\_MODEL}
}
$$

The provenance spine is:

$$
\boxed{
\text{RAW SOURCE}
\rightarrow
\text{DERIVED PAGE}
\rightarrow
\text{SYNTHESIS}
\rightarrow
\text{ANSWER}
}
$$

while preserving ancestry:

$$
\boxed{
\text{multiple descendants}
\neq
\text{multiple independent sources}
}
$$

The operational principle is therefore:

$$
\boxed{
\text{capture once}
\rightarrow
\text{integrate}
\rightarrow
\text{reuse}
\rightarrow
\text{maintain}
}
$$

rather than repeated full raw-source parsing.

______________________________________________________________________

## 47. Integrity Boundary

The strongest source-supported conclusion is:

$$
\boxed{
\text{AMOS LLM Wiki is a schema for a compounding,
LLM-maintained knowledge wiki inside the AMOS Obsidian vault.}
}
$$

Its source-declared architecture separates:

$$
\boxed{
\text{immutable raw sources}
}
$$

from:

$$
\boxed{
\text{LLM-maintained derived wiki pages}
}
$$

and from:

$$
\boxed{
\text{the governing schema}
}
$$

with explicit epistemic typing:

$$
\boxed{
\text{RAW PAGE}
\rightarrow
\texttt{SOURCE\_CLAIM}
}
$$

$$
\boxed{
\text{SYNTHESIZED PAGE}
\rightarrow
\texttt{DERIVED / AMOS\_MODEL}
}
$$

The compounding loop is:

$$
\boxed{
W_t
\rightarrow
\text{INGEST / QUERY / LINT}
\rightarrow
W_{t+1}
}
$$

but:

$$
\boxed{
\text{compounding knowledge}
\neq
\text{automatic compounding truth}
}
$$

and:

$$
\boxed{
\text{wiki reuse}
\neq
\text{loss of raw provenance}
}
$$

The principal integrity constraints are:

$$
\boxed{
\text{RAW}
\neq
\text{DERIVED}
}
$$

$$
\boxed{
\text{WIKILINK}
\neq
\text{EVIDENCE}
}
$$

$$
\boxed{
\text{REPETITION}
\neq
\text{INDEPENDENT CONFIRMATION}
}
$$

$$
\boxed{
\text{FILED ANSWER}
\neq
\text{VERIFIED CLAIM}
}
$$

$$
\boxed{
\text{CAPABILITY}
\neq
\text{AUTHORITY}
}
$$

$$
\boxed{
\text{DECLARED BINDING}
\neq
\text{VALIDATED EXECUTION}
}
$$

$$
\boxed{
\text{PAGE COUNT}
\neq
\text{KNOWLEDGE QUALITY}
}
$$

The declared skill, workflow, agent, and tool paths establish the artifact's intended AMOS operational bindings. Their actual existence, current content, executable behavior, and validation are **not independently established by this source alone**.

Accordingly, the artifact remains accurately bounded by its supplied classifications:

$$
\boxed{
\operatorname{ConclusionClass}
=
\texttt{DECISION / AMOS\_MODEL}
}
$$

$$
\boxed{
\operatorname{Confidence}
=
\texttt{DERIVED}
}
$$

$$
\boxed{
\operatorname{RSCFState}
=
\texttt{SOURCE\_CLAIM}
}
$$

$$
\boxed{
\operatorname{RSCFClaimClass}
=
\texttt{AMOS\_MODEL}
}
$$

No stronger empirical, implementation, or external-source-verification claim is implied.

______________________________________________________________________

## Related

Source-declared:

- [[00_ROOT_MOC|00_ROOT_MOC]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]]
- [[11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC|LLM_WIKI_MOC]]
- [[11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_INDEX|LLM_WIKI_INDEX]]
- [[11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG|LLM_WIKI_LOG]]

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC|LLM_WIKI_MOC]]

```
```
