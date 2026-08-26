#!/usr/bin/env python3
"""Fill placeholder contracts pass 2 — deterministic, additive, fail-safe.

Upgrades ~1190 PROPOSED_SPECIFICATION / 'Stub for' notes (<1KB) into typed,
plane-aware contract specs. Preserves YAML frontmatter and RSCF-NODE /
Related footers verbatim. Epistemic class stays AMOS_MODEL · CONDITIONAL;
executable binding stays PARTIAL unless an executed receipt exists.
"""
import os, re, sys

ROOT = "/Users/mac/Documents/AMOS_OS"

PLANES = {
    "00_ROOT": ("Root", "vault-wide identity, architecture map, authoritative state pointers, and release governance"),
    "01_CANON": ("Canon", "canonical laws, universe/cognition/infrastructure canons, variable registry, glossary, provenance lineage, and supersession"),
    "02_KERNEL": ("Kernel", "kernel-plane reasoning primitives: meta-logic, cognition, causality, state, memory, risk-repair, authority, provenance, integration"),
    "03_CONTROL_PLANE": ("Control Plane", "governance surfaces that gate effects: task contracts, capability, policy, authority, provenance, semantic transactions, observability, effects, commit, exposure, replay, rollback"),
    "04_RUNTIME": ("Runtime", "execution substrate binding kernel contracts to runnable operators under v4.4 runtime rules"),
    "05_COGNITIVE_ORGANISM": ("Cognitive Organism", "the organism-level cognitive assembly above kernels and below agents"),
    "06_AGENTS": ("Agents", "agent specifications, capability envelopes, and delegation boundaries"),
    "07_SKILLS": ("Skills", "host skill packages exposing workflows; deployment infrastructure, never truth authorities"),
    "08_WORKFLOWS": ("Workflows", "multi-step orchestration definitions with typed stages and rollback basins"),
    "09_PROTOCOLS": ("Protocols", "inter-component communication and handshake protocols"),
    "10_MEMORY": ("Memory", "durable memory stores, trust classes, admission, retrieval, and conflict policy"),
    "11_KNOWLEDGE": ("Knowledge", "knowledge base integration (excluded from this pass)"),
    "12_STATE": ("State", "authoritative state records and state-versioned artifacts"),
    "13_MODELS": ("Models", "model registries and model-output vs observation firewalls"),
    "14_TOOLS": ("Tools", "tool bindings; tool availability is never permission"),
    "15_INTERFACES": ("Interfaces", "cross-boundary message schemas and interface contracts"),
    "16_SCHEMAS": ("Schemas", "typed artifact schemas and compatibility rules"),
    "17_OBSERVABILITY": ("Observability", "metrics, logs, traces, health signals — observations, never authority"),
    "18_SECURITY": ("Security", "threat surface, fail-closed gates, attestation, and secrets status"),
    "19_TESTS": ("Tests", "test taxonomy, coverage declarations, negative coverage, and receipts"),
    "20_OPERATIONS": ("Operations", "operational runbooks, recovery procedures, maintenance passes"),
    "21_DOMAINS": ("Domains", "C-family domain engine mappings (C01–C12) onto the OS planes"),
    "22_RESEARCH": ("Research", "research questions, experiments, competing models, validation, benchmarks"),
    "23_OPERATING_MODEL": ("Operating Model", "roles, decision rights, governance forums, escalation paths, service levels"),
    "24_ARCHIVE": ("Archive", "superseded artifacts (excluded from this pass)"),
    "25_COGNITIVE_MATRIX": ("Cognitive Matrix", "primitives L00–L29, lifecycle operations O00–O16, control planes C01–C09, scales, cell registry, routing, validation, generators"),
}

DISCIPLINE = ("Typed artifacts · provenance stamped · epistemic class declared · "
              "confidence ceiling · fail-closed on UNKNOWN/GAP · receipts for "
              "consequential effects · rollback basin before mutation.")

RECEIPTS = ("[[ROUTING_POLICY_VALIDATION_RECEIPT]] · [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]")

def plane_of(path):
    top = path.split("/")[0]
    return PLANES.get(top, ("Unknown Plane", "unclassified plane"))

def classify(basename):
    b = basename[:-3] if basename.endswith(".md") else basename
    ub = b.upper()
    if ub.startswith("INDEX_"):
        return "INDEX"
    for token, kind in (("README","README"),("CONTRACT","CONTRACT"),("MAP","MAP"),
                        ("REGISTRY","REGISTRY"),("_LEDGER","LEDGER"),("_LOG","LOG"),
                        ("_HISTORY","HISTORY"),("_AUDIT","AUDIT"),("_POLICY","POLICY"),
                        ("_LIFECYCLE","LIFECYCLE"),("_SPEC","SPEC"),("_TESTS","TESTS"),
                        ("_RULES","RULES"),("_GATES","GATES")):
        if token in ub:
            return kind
    return "ARTIFACT"

def pretty(name):
    n = re.sub(r"\.md$", "", name)
    n = re.sub(r"^INDEX_", "", n)
    n = re.sub(r"^(KERNEL|CONTROL_PLANE|CANON|RESEARCH|OPERATING_MODEL|COGNITIVE_MATRIX|PRIMITIVES|LIFECYCLE_OPERATIONS|CONTROL_PLANES|SCALES|STATE|MEMORY|PROVENANCE|SECURITY|INTERFACES|TESTS|RUNTIME|EFFECTS|COMMIT|TASK_CONTRACT|CAPABILITY|POLICY|AUTHORITY|SEMANTIC_TRANSACTION|OBSERVABILITY|EXPOSURE|REPLAY|ROLLBACK|VALIDATION|COMPETING_MODELS|BENCHMARKS|GOVERNANCE_FORUMS|DECISION_RIGHTS|SERVICE_LEVELS|ESCALATION|ROLES|VARIABLE_REGISTRY|GLOSSARY|SUPERSESSION)_", r"\1 · ", n)
    n = n.replace("_", " ").strip()
    n = re.sub(r"\s+", " ", n)
    return n

def siblings(relpath):
    d = os.path.dirname(os.path.join(ROOT, relpath))
    out = []
    try:
        for f in sorted(os.listdir(d)):
            if f.endswith(".md") and f != os.path.basename(relpath):
                out.append(f)
    except OSError:
        pass
    return out

def rel_link(from_rel, to_rel):
    """Obsidian shortest-path link target."""
    return os.path.splitext(os.path.basename(to_rel))[0]

# ---------- body builders ----------

def body_status(plane_name):
    return (f"STATUS: PROPOSED_SPECIFICATION\n"
            f"epistemic_class: AMOS_MODEL\ncanonical_status: CONDITIONAL\n"
            f"updated: 2026-08-26\nplane: {plane_name}\n")

def build_readme(title, relpath):
    pname, pdesc = plane_of(relpath)
    sibs = siblings(relpath)
    lines = [
        f"## Purpose",
        f"`{title}` is the package readme for the **{pname}** plane segment at `{os.path.dirname(relpath) or '.'}`.",
        f"The {pname} plane governs {pdesc}. Normative load-bearing content lives in the sibling contract(s); this readme orients navigation.",
        "",
        "## Sibling artifacts",
    ]
    if sibs:
        for s in sibs[:24]:
            lines.append(f"- [[{rel_link(relpath, s)}]]")
        if len(sibs) > 24:
            lines.append(f"- … {len(sibs)-24} more")
    else:
        lines.append("- (none)")
    lines += ["", "## Contract discipline", DISCIPLINE, "", "## Gaps",
              f"Executable binding PARTIAL unless an executed validation receipt exists for this subsystem ({RECEIPTS})."]
    return "\n".join(lines)

def build_contract(title, relpath):
    pname, pdesc = plane_of(relpath)
    seg = pretty(os.path.basename(relpath)).split("·")[-1].strip()
    return "\n".join([
        "## 0. Status",
        f"{pname}-plane contract for **{seg}**. AMOS_MODEL; canonical status CONDITIONAL; implementation PARTIAL.",
        "",
        "## 1. Scope",
        f"Governs {pdesc} as they bear on `{seg}`. Bounded by dependency closure: conclusions inherit the weakest load-bearing premise.",
        "",
        "## 2. Contract terms",
        "- **Typed artifacts** — every artifact declares artifact_type, epistemic class, scope, regime.",
        "- **Firewalls preserved** — CAPABILITY ≠ AUTHORITY · PROPOSAL ≠ COMMIT · OBSERVED ≠ CURRENT · TEST_PASS ≠ TRUTH.",
        "- **Epochs distinct** — state_version ≠ causal_epoch ≠ policy_epoch ≠ provenance_epoch unless an explicit mapping licenses equivalence.",
        "- **Local finality requires proof** — demonstrated dependency closure may avoid coordination; assumed independence may not.",
        "- **Selective invalidation** — failure invalidates dependent descendants only; unrelated state is preserved.",
        "",
        "## 3. Invariants",
        "- Fail closed on UNKNOWN/GAP; gaps stay visible, never promoted to PASS.",
        "- Confidence of any conclusion ≤ confidence of its weakest load-bearing premise (ceiling 0.95).",
        "- Consequential effects emit receipts; rollback basin exists before mutation.",
        "- Competing hypotheses remain visible when evidence does not discriminate.",
        "",
        "## 4. Executed reference",
        f"No subsystem-local executor yet. Existing executed validators for the OS: routing-policy validator 19/19 ([[ROUTING_POLICY_VALIDATION_RECEIPT]]) and authz invariant engine 17/17 ([[AUTHZ_ENGINE_VALIDATION_RECEIPT]]) — cited as pattern, not as evidence for this artifact.",
        "",
        "## 5. Gaps",
        "Runtime enforcement, persistence binding, and empirical validation remain OPEN (UNKNOWN/GAP). Promotion beyond AMOS_MODEL requires the promotion-gate checklist plus an executed receipt specific to this contract.",
        "",
        "## 6. Falsifiers",
        "F1: canonical source defines different semantics for this surface. F2: an executed test contradicts a declared invariant. F3: this contract silently collapses a protected firewall.",
    ])

def build_map(title, relpath):
    pname, _ = plane_of(relpath)
    here = os.path.dirname(relpath)
    entries = []
    for f in siblings(relpath):
        b = f.upper()
        if "_CONTRACT" in b or b.endswith("CONTRACT.MD"):
            entries.append(("Contract", f))
        elif "README" in b:
            entries.append(("Readme", f))
        else:
            entries.append(("Artifact", f))
    lines = [f"## Map — {pretty(os.path.basename(relpath))}",
             f"Navigation map for the `{here or '.'}` segment of the {pname} plane.", ""]
    for kind, f in entries:
        lines.append(f"- **{kind}** — [[{rel_link(relpath, f)}]]")
    if not entries:
        lines.append("- (no sibling artifacts)")
    lines += ["", "## Reading order", "1. Readme → orientation.  2. Contract → normative terms.  3. Artifacts → instances bound by the contract.",
              "", "## Gaps", f"This map covers its own directory only; cross-segment edges live in [[00_ROOT_MAP]] and [[AMOS_RSCF_NODES]]. Executable graph validation remains PARTIAL ({RECEIPTS})."]
    return "\n".join(lines)

def build_index(title, relpath):
    # INDEX_X indexes X in same dir
    m = re.match(r"INDEX_(.+)\.md$", os.path.basename(relpath))
    target = m.group(1) if m else None
    tgt_path = None
    if target:
        cand = os.path.join(os.path.dirname(relpath), target + ".md")
        if os.path.exists(os.path.join(ROOT, cand)):
            tgt_path = cand
    lines = ["## Index"]
    if tgt_path:
        lines.append(f"- Primary target — [[{rel_link(relpath, tgt_path)}]] (indexed artifact).")
    for f in siblings(relpath):
        if f != os.path.basename(relpath):
            lines.append(f"- See also — [[{rel_link(relpath, f)}]]")
    lines += ["", "## Indexing rule", "This index resolves by basename within its own directory. Cross-plane resolution goes through [[00-Home]] and [[AMOS_RSCF_NODES]].",
              "", "## Gaps", f"Automated link-integrity execution for this index is PARTIAL ({RECEIPTS})."]
    return "\n".join(lines)

def build_registry(title, relpath):
    pname, pdesc = plane_of(relpath)
    seg = pretty(os.path.basename(relpath)).split("·")[-1].strip()
    return "\n".join([
        "## Purpose",
        f"Registry for **{seg}** within the {pname} plane ({pdesc} context).",
        "",
        "## Entry schema",
        "```yaml",
        "entry_id: null          # unique within registry",
        "version: null           # explicit; material change ⇒ new version",
        "artifact_type: null     # typed",
        "epistemic_class: MODEL  # SOURCE | DERIVED | MODEL | UNKNOWN/GAP",
        "scope: null             # domain / regime / H-M-L applicability",
        "provenance: []          # source lineage, transformations",
        "authority_ref: null     # granting authority, epoch-bound",
        "freshness: null         # valid_until / max_age",
        "status: REGISTERED      # REGISTERED | SUPERSEDED | REVOKED | QUARANTINED",
        "```",
        "",
        "## Current contents",
        "Registry population is EMPTY-BY-HONESTY: no fabricated entries. Entries are added only with provenance and authority refs.",
        "",
        "## Registry laws",
        "- ADDRESSABLE ≠ IMPLEMENTED ≠ VALIDATED ≠ AUTHORIZED.",
        "- Same id + changed semantics ⇒ version bump, never silent overwrite.",
        "- Revocation preserves history (append-only).",
        "",
        "## Gaps",
        f"Registry backend, uniqueness enforcement, and automated schema validation remain OPEN ({RECEIPTS}).",
    ])

def build_generic(title, relpath, kind):
    pname, pdesc = plane_of(relpath)
    seg = pretty(os.path.basename(relpath))
    kinddesc = {
        "LEDGER": "append-only ledger — entries are never rewritten, only superseded",
        "LOG": "event log — observations recorded with timestamps and actor identity; logs are evidence, not authority",
        "HISTORY": "historical record — prior states remain addressable; rewriting history is prohibited",
        "AUDIT": "audit record — must be capable of answering who/what/when/which authority/which evidence",
        "POLICY": "policy artifact — governs admissibility within declared scope and epochs",
        "LIFECYCLE": "lifecycle definition — legal transitions, illegal transitions, and required gates between states",
        "SPEC": "specification — intended semantics; implementation status tracked separately",
        "TESTS": "test declarations — coverage matrix over invariants including negative cases",
        "RULES": "rule set — ordered, precedence-declared rules with conflict surfacing",
        "GATES": "gate definitions — pass conditions, fail behavior, and escalation paths",
    }.get(kind, "typed artifact specification")
    return "\n".join([
        "## 0. Status",
        f"{pname}-plane artifact. AMOS_MODEL · CONDITIONAL · implementation PARTIAL.",
        "",
        "## 1. Purpose",
        f"`{seg}` defines {kinddesc}, serving the {pname} plane's obligation: {pdesc}.",
        "",
        "## 2. Semantics",
        "- Every load-bearing field is typed; unknown values are recorded as `UNKNOWN/GAP`, never invented.",
        "- Scope and regime are declared on every claim; cross-regime transfer requires an explicit bridge.",
        "- Confidence ceiling 0.95; conclusion confidence ≤ weakest load-bearing premise.",
        "",
        "## 3. Failure modes guarded",
        "STALE_READ · SCOPE_LEAK · REGIME_DRIFT · CONFIDENCE_INFLATION · AUTHORITY_ESCALATION · PROVENANCE_LOSS · SILENT_PARTIAL_COMMIT · UNKNOWN_AS_VALID.",
        "",
        "## 4. Validation",
        f"No artifact-specific executor yet; executed OS validators exist as pattern ({RECEIPTS}). Required tests before promotion: identity, type-contract, negative-case (missing/malformed/stale input), authority boundary, rollback.",
        "",
        "## 5. Gaps",
        "Implementation binding, empirical validation, and cross-artifact consistency checks remain OPEN (UNKNOWN/GAP).",
        "",
        "## 6. Falsifiers",
        "F1: canonical source contradicts declared semantics. F2: executed test violates a stated invariant. F3: artifact promotes UNKNOWN to PASS.",
    ])

def enrichment(title, relpath, kind):
    """Shared deep sections appended to every artifact class."""
    pname, _ = plane_of(relpath)
    seg = pretty(os.path.basename(relpath))
    return "\n".join([
        "",
        "## Worked semantics",
        f"Given an operation touching `{seg}` within the {pname} plane:",
        "1. **Admit** — resolve the artifact by id + version; unresolved id ⇒ `UNKNOWN/GAP`, fail closed.",
        "2. **Bind scope** — declare domain / regime / H-M-L applicability before any mutation.",
        "3. **Check authority** — authority_ref must be epoch-valid; capability alone never authorizes.",
        "4. **Validate preconditions** — dependency closure traversed to the smallest result-changing set.",
        "5. **Propose** — candidate state is non-authoritative until gates pass (`PROPOSAL ≠ COMMIT`).",
        "6. **Commit or hold** — on any failed premise: preserve unaffected state, invalidate dependent descendants only, record receipt.",
        "",
        "## Promotion-gate checklist",
        "- [ ] typed schema bound to this artifact",
        "- [ ] identity + versioning implemented",
        "- [ ] negative cases covered (missing · malformed · stale · unauthorized input)",
        "- [ ] provenance edges persisted and validated",
        "- [ ] rollback basin demonstrated for consequential effects",
        "- [ ] executed validation receipt specific to this artifact",
        "- [ ] unresolved critical gaps registered as UNKNOWN/GAP (visible)",
        "",
        "## Cross-plane bindings",
        f"- Governed by canon — [[01_CANON_README]] · [[LAW_HIERARCHY]]",
        f"- Kernel interaction — [[KERNEL_README]]",
        f"- Control-plane gates — [[CONTROL_PLANE_README]]",
        f"- Observed by — [[17_OBSERVABILITY_README]] · never treated as authority",
        f"- Recovered via operations — [[20_OPERATIONS_README]]",
    ])

def generate_body(title, relpath):
    base = os.path.basename(relpath)
    kind = classify(base)
    if kind == "README":
        core = build_readme(title, relpath)
    elif kind == "CONTRACT":
        core = build_contract(title, relpath)
    elif kind == "MAP":
        core = build_map(title, relpath)
    elif kind == "INDEX":
        core = build_index(title, relpath)
    elif kind == "REGISTRY":
        core = build_registry(title, relpath)
    else:
        core = build_generic(title, relpath, kind)
    return core + enrichment(title, relpath, kind)

TITLE_RE = re.compile(r"^#{1,2} .+$", re.M)

def process(path):
    relpath = os.path.relpath(path, ROOT)
    text = open(path, encoding="utf-8").read()
    orig_len = len(text)

    # locate title line (first '# ' heading)
    m = re.search(r"^#{1,2} .*$", text, re.M)
    if not m:
        return False, "no-title"
    title_end = m.end()

    # locate footer start: first '---' line followed by Related/RSCF after the body,
    # i.e. the last occurrence of '\n---\n' before RSCF-NODE or the standalone footer.
    footer_idx = len(text)
    for marker in ("\n---\n\n[[00_ROOT", "\n---\n\n**Related:**", "\n---\n\nRSCF-NODE",
                   "\n---\n[[00_ROOT", "\nRSCF-NODE", "\n---\n\n[["):
        i = text.find(marker, title_end)
        if i != -1:
            footer_idx = min(footer_idx, i)
    head = text[:title_end]
    tail = text[footer_idx:]

    title_text = m.group(0).lstrip("# ").strip()
    new_body = generate_body(title_text, relpath)
    new_text = head.rstrip() + "\n\n" + new_body + "\n" + tail.lstrip("\n")
    if len(new_text) <= orig_len:
        return False, "not-grown"
    open(path, "w", encoding="utf-8").write(new_text)
    return True, f"{orig_len}->{len(new_text)}"

def main():
    targets = [l.strip().lstrip('./') for l in open('/tmp/stub_files.txt') if l.strip() and l.strip() != '.']
    ok = skip = 0
    errors = []
    for rel in targets:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            errors.append((rel, "missing")); continue
        try:
            changed, msg = process(p)
            if changed: ok += 1
            else: skip += 1; errors.append((rel, msg))
        except Exception as e:
            errors.append((rel, str(e)[:80]))
    print(f"filled={ok} skipped={skip} errors={len(errors)}")
    for e in errors[:30]:
        print("ERR", e)

if __name__ == "__main__":
    main()
