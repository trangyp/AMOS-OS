#!/usr/bin/env python3
"""
AMOS Plane Contracts Upgrader
Transforms 102-line boilerplate placeholder contracts into rich, plane-specific,
authoritative governing contracts conforming to AGENTS.md v4.4 & Trang Phan origin architecture.
"""

import os
from pathlib import Path

vault = Path('/Users/mac/Library/CloudStorage/GoogleDrive-phanqtrang@gmail.com/My Drive/_AMOS_OS')

def ensure_file(rel_path, content):
    p = vault / rel_path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.strip() + '\n', encoding='utf-8')
    print(f"[CONTRACT UPGRADED] {rel_path} ({len(content.splitlines())} lines)")

# ==========================================
# 1. 22_RESEARCH CONTRACTS
# ==========================================

RESEARCH_RESEARCH_CONTRACT = """---
title: "22_RESEARCH Master Research & Scientific Governance Contract"
type: control_contract
source: 22_RESEARCH
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_GOVERNING_CONTRACT
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 01_CANON/01_CORE_LAWS/LAW_HIERARCHY
    - 22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY
  scope: research_governance
tags:
  - amos-os
  - research
  - contract
  - formal-methods
  - falsification
---

# 22_RESEARCH Master Research & Scientific Governance Contract

## 1. Scope & Domain Obligation

The `22_RESEARCH` plane governs the admission, formalization, empirical validation, and mathematical modeling of all hypotheses, proofs, experimental trials, and academic literature across the AMOS OS universe.

```text
RESEARCH != DOGMA
HYPOTHESIS != LAW
MATHEMATICAL_MODEL != EMPIRICAL_FACT
EVIDENCE_STRENGTH != EVIDENCE_VOLUME
```

## 2. Epistemic Gates & Invariant Rules

### 2.1 The 137 Math Registry Invariant
Every theoretical claim touching dynamical systems, causal loops, or multi-agent stability must declare explicit bindings to one or more of the 137 canonical mathematical formulations in [[22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY|AMOS_137_MATH_REGISTRY]].

### 2.2 Strict Falsifiability Criterion (Popperian Barrier)
No proposition may be admitted into `22_RESEARCH` unless it explicitly defines:
1. **At least two empirical falsifiers ($F_1, F_2$)**.
2. **The discriminating experiment or test fixture required to refute the claim**.
3. **The exact confidence ceiling ($\mathcal{C} \le 0.95$)**.

### 2.3 Competing Hypotheses Preservation
When observational data is insufficient to distinguish between competing models:
- Both models must be preserved side-by-side in `03_COMPETING_MODELS/`.
- Neither model may be promoted to canonical status until discriminating evidence is recorded.

## 3. Research Lifecycle & Promotion Sequence

```mermaid
graph LR
    H[HYPOTHESIS<br/>01_PAPERS] --> E[EXPERIMENT<br/>02_EXPERIMENTS]
    E --> V[VALIDATION<br/>04_VALIDATION]
    V --> B[BENCHMARK<br/>05_BENCHMARKS]
    B -->|Peer Verified & Math Bound| C[CANON ADMISSION<br/>01_CANON]
```

## 4. Failure Modes & Containment

- **Premise Invalidation**: If an underlying mathematical lemma or empirical assumption is refuted, all derived conclusions in `22_RESEARCH` are automatically flagged as `UNKNOWN/GAP`.
- **Confidence Inflation**: Any paper or experiment claiming $\mathcal{C} > 0.95$ without empirical grounding is quarantined by `17_OBSERVABILITY`.

## 5. Cross-Plane Bindings

- **Governed By:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Invariants Verified By:** [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL|DETERMINISTIC_LOGIC_KERNEL]]
- **Tested By:** [[19_TESTS/TESTS_README|TESTS_README]]
"""

RESEARCH_PAPERS_CONTRACT = """---
title: "Research Papers Ingestion & Peer Review Contract"
type: control_contract
source: 22_RESEARCH/01_PAPERS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_GOVERNING_CONTRACT
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 22_RESEARCH/RESEARCH_RESEARCH_CONTRACT
  scope: papers_ingestion
tags:
  - amos-os
  - research
  - papers
  - arxiv
---

# Research Papers Ingestion & Peer Review Contract

## 1. Mandate
Governs the intake, metadata extraction, mathematical parsing, and peer evaluation of scientific papers, arXiv preprints, and formal monographs.

## 2. Intake Invariants
1. Every ingested paper must be assigned an immutable RSCF identity: `arxiv-{arxiv_id}-{slug}`.
2. Abstract, methodology, proofs, and conclusions must be separated into distinct typed sections.
3. Claims cannot be promoted to verified truth merely by being published in high-impact venues (`M04: SOURCE_CLAIM != VERIFIED`).
"""

# ==========================================
# 2. 14_TOOLS CONTRACT
# ==========================================

TOOLS_TOOL_CONTRACT = """---
title: "14_TOOLS Master Tool Governance & Capability Isolation Contract"
type: control_contract
source: 14_TOOLS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_GOVERNING_CONTRACT
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 18_SECURITY/SECURITY_README
  scope: tools_governance
tags:
  - amos-os
  - tools
  - contract
  - sandboxing
  - capability-isolation
---

# 14_TOOLS Master Tool Governance & Capability Isolation Contract

## 1. Core Principle

```text
TOOL_ACCESS != TOOL_PERMISSION
CAPABILITY != AUTHORITY
EXECUTION != STATE_MUTATION
INVOCATION != SUCCESS
```

## 2. Sandboxed Execution Governance

All tool executions in AMOS OS are subject to strict isolation tiers:

| Tier | Isolation Level | Permitted Operations | Audit Overhead |
| :--- | :--- | :--- | :--- |
| **Tier 0** | Pure Inference | Token reasoning, internal calculations | Minimal |
| **Tier 1** | Read-Only Substrate | `read_file`, `view_file`, `grep_search`, `list_dir` | Event Logged |
| **Tier 2** | Bounded Workspace | `replace_file_content`, `write_to_file` (within workspace) | Pre/Post Snapshot |
| **Tier 3** | System Runtime | `run_command` (isolated child processes, sandboxed scripts) | Full Telemetry |
| **Tier 4** | High-Stakes Authority | Canon amendment, security policy changes, credential access | Epoch-Gated Multi-Sig |

## 3. Failure Containment & Rollback Basin

1. **Timeout Enforcement**: Every tool invocation has a hard execution ceiling ($T_{max} \le 30s$).
2. **Blast Radius Isolation**: If a tool crashes or returns an error, the executing agent's working memory is isolated and unaffected system state is preserved.
3. **Deterministic Error Translation**: Unhandled exceptions are translated into structured `TOOL_FAILURE` receipts with exact exit codes and stderr captures.
"""

# ==========================================
# 3. 15_INTERFACES CONTRACT
# ==========================================

INTERFACES_INTERFACE_CONTRACT = """---
title: "15_INTERFACES Master Interface & System Surface Contract"
type: control_contract
source: 15_INTERFACES
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_GOVERNING_CONTRACT
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 09_PROTOCOLS/PROTOCOLS_README
  scope: interfaces_governance
tags:
  - amos-os
  - interfaces
  - contract
  - boundaries
  - serialization
---

# 15_INTERFACES Master Interface & System Surface Contract

## 1. Scope & Domain Obligation

The `15_INTERFACES` plane governs all boundary crossing points between AMOS OS and external systems (Obsidian UI, MCP Clients, Terminal CLI, Web APIs, and File Systems).

```text
SURFACE != ENGINE
FORMAT != SEMANTICS
PRESENTATION != AUTHORITY
```

## 2. Interface Rules & Typing

1. **Strict Bidirectional Serialization**: All inter-system messages must serialize to validated JSON / YAML conforming to `16_SCHEMAS`.
2. **Wikilink Syntax Normalization**: All internal cross-references must use standard Obsidian wikilinks: `[[Path/To/File|Alias]]`.
3. **Frontmatter Integrity**: Markdown files crossing the interface barrier must include a complete YAML header with `type`, `origin_architect`, `amos_core_target`, and `rscf` blocks.
"""

# ==========================================
# 4. 18_SECURITY CONTRACT
# ==========================================

SECURITY_SECURITY_CONTRACT = """---
title: "18_SECURITY Master Security & Reality-Bound Authorization Contract"
type: control_contract
source: 18_SECURITY
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_GOVERNING_CONTRACT
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 01_CANON/01_CORE_LAWS/LAW_HIERARCHY
  scope: security_governance
tags:
  - amos-os
  - security
  - contract
  - reality-bound
  - anti-hallucination
---

# 18_SECURITY Master Security & Reality-Bound Authorization Contract

## 1. Hard Security Axioms

```text
CAPABILITY != PERMISSION
AUTHORITY != ARBITRARY_ACTION
PROPOSAL != COMMIT
TRUST != UNVERIFIED
```

## 2. Threat Mitigation & Enforcement

1. **Anti-Hallucination Firewall**: All agent capability assertions must be grounded in verified execution receipts.
2. **Ephemeral Capability Grants**: Tokens expire within the active causal epoch ($E_k$). Re-authorization is required for cross-epoch operations.
3. **Emergency Revocation Protocol**: The system maintains an instant shutdown kill-switch for compromised agent sub-trees.
"""

# ==========================================
# 5. 19_TESTS CONTRACT
# ==========================================

TESTS_TEST_CONTRACT = """---
title: "19_TESTS Master Validation & Invariant Testing Contract"
type: control_contract
source: 19_TESTS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_GOVERNING_CONTRACT
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 02_KERNEL/DETERMINISTIC_LOGIC_KERNEL
  scope: tests_governance
tags:
  - amos-os
  - tests
  - contract
  - invariant-testing
  - regression
---

# 19_TESTS Master Validation & Invariant Testing Contract

## 1. Testing Axioms

```text
TEST_SPECIFIED != TEST_EXECUTED
PASS != UNIVERSAL_PROOF
NEGATIVE_TEST != REDUNDANT
VALIDATION_SCOPE != GLOBAL_AUTHORITY
```

## 2. Mandatory Test Coverage Tiers

1. **Axiom Falsification Tests**: Test fixtures designed to attempt breaking M01–M20 invariants (must fail closed).
2. **Deterministic Regression Tests**: Replay historical transaction traces with exact bit-for-bit assertion.
3. **Graph Integrity Scans**: Automated tests scanning for broken wikilinks, unclosed code fences, and malformed frontmatter.
"""

def main():
    print("Beginning Contract Upgrades pass...")
    ensure_file('22_RESEARCH/RESEARCH_RESEARCH_CONTRACT.md', RESEARCH_RESEARCH_CONTRACT)
    ensure_file('22_RESEARCH/01_PAPERS/RESEARCH_PAPERS_CONTRACT.md', RESEARCH_PAPERS_CONTRACT)
    ensure_file('14_TOOLS/TOOLS_TOOL_CONTRACT.md', TOOLS_TOOL_CONTRACT)
    ensure_file('15_INTERFACES/INTERFACES_INTERFACE_CONTRACT.md', INTERFACES_INTERFACE_CONTRACT)
    ensure_file('18_SECURITY/SECURITY_SECURITY_CONTRACT.md', SECURITY_SECURITY_CONTRACT)
    ensure_file('19_TESTS/TESTS_TEST_CONTRACT.md', TESTS_TEST_CONTRACT)
    print("Contract Upgrades pass completed successfully!")

if __name__ == '__main__':
    main()
