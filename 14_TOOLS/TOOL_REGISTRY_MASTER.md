---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: Tool Registry Master
source: 14_TOOLS
type: registry
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 14_TOOLS/14_TOOLS_MOC
    - 14_TOOLS/00_INDEX/TOOL_MAP
    - 14_TOOLS/TOOLS_README
    - 14_TOOLS/TOOLS_TOOL_CONTRACT
  scope: 14_tools_registry
tags:
  - amos-os
  - 14_tools
  - registry
  - tool
  - sandbox
---

# Tool Registry Master

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Epistemic Class:** `AMOS_MODEL`
> **Conclusion Class:** `DERIVED`

---

## 1. Scope

`TOOL_REGISTRY_MASTER` is the canonical list of all tools that have passed the `14_TOOLS` admission criteria and are approved for invocation by AMOS agents. It binds each tool to a formal identifier, a sandbox tier, a version hash, and a capability envelope. The registry is `AMOS_MODEL` until each entry has a separately verified implementation receipt.

```text
DOCUMENTED != IMPLEMENTED
CAPABILITY != AUTHORITY
REGISTRY != ADMISSION
```

---

## 2. Admission Criteria

A tool is admitted to this master registry only after:
1. A formal JSON schema defining parameters and return types is published.
2. Bounded failure mode and timeout specifications are documented.
3. Full execution telemetry is emitted to `17_OBSERVABILITY`.
4. Least-privilege scoping is enforceable at runtime.
5. Security Council review is recorded with a receipt.

See [[14_TOOLS/TOOLS_README|TOOLS_README]] and [[14_TOOLS/TOOLS_TOOL_CONTRACT|TOOLS_TOOL_CONTRACT]] for the full contract.

---

## 3. Admitted Tools

| Tool ID | Entry | Tier | Scope Note |
|---------|-------|------|------------|
| `amos-llm-wiki` | [[14_TOOLS/AMOS_LLM_WIKI_TOOL|AMOS_LLM_WIKI_TOOL]] | T1 | Read-only Obsidian LLM wiki query tool. |
| `amos-obsidian-linking` | [[14_TOOLS/AMOS_OBSIDIAN_LINKING_PLUGINS|AMOS_OBSIDIAN_LINKING_PLUGINS]] | T2 | Internal vault linking and validation helpers. |
| `amos-wasi-micro-sandbox` | [[14_TOOLS/AMOS_SELF_HEALING_AUTONOMOUS_WASI_MICRO_SANDBOX_GUIDE|AMOS_SELF_HEALING_AUTONOMOUS_WASI_MICRO_SANDBOX_GUIDE]] | T2 | WebAssembly component model sandbox guide. |
| `amos-sandbox-execution` | [[14_TOOLS/SANDBOX_TOOL_EXECUTION_PROTOCOL|SANDBOX_TOOL_EXECUTION_PROTOCOL]] | T2 | Sandboxed execution protocol. |
| `amos-simulation-kernel` | [[14_TOOLS/SIMULATION_KERNEL_DISCRETE_SYSTEM_DYNAMICS|SIMULATION_KERNEL_DISCRETE_SYSTEM_DYNAMICS]] | T2 | Discrete system dynamics simulation. |
| `tool-map` | [[14_TOOLS/00_INDEX/TOOL_MAP|TOOL_MAP]] | T0 | Navigation map for the 14_TOOLS plane. |
| `tools-moc` | [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]] | T0 | Plane MOC and structural hub. |
| `tools-readme` | [[14_TOOLS/TOOLS_README|TOOLS_README]] | T0 | Plane readme. |
| `tools-contract` | [[14_TOOLS/TOOLS_TOOL_CONTRACT|TOOLS_TOOL_CONTRACT]] | T0 | Normative tool contract. |

---

## 4. Operational Rules

- **R-001 (Version Binding):** Every tool entry is version-locked; updates require a supersession record.
- **R-002 (Tier Enforcement):** A tool MUST NOT be invoked above its declared tier without explicit tier-escalation authority.
- **R-003 (Telemetry Closure):** No tool is considered active until an observability binding is demonstrated.
- **R-004 (Unknown/GAP):** A tool not present in this registry is treated as `UNKNOWN/GAP` and fails closed.

---

## 5. Navigation

- [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]] — plane MOC
- [[14_TOOLS/00_INDEX/TOOL_MAP|TOOL_MAP]] — live tool navigation map
- [[14_TOOLS/TOOLS_README|TOOLS_README]] — architecture and admission criteria
- [[14_TOOLS/TOOLS_TOOL_CONTRACT|TOOLS_TOOL_CONTRACT]] — binding contract
- [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]] — security plane
