# AMOS OS Agent & Workflow Integration

This workspace contains the complete AMOS OS cognitive architecture, including:
- **678 Canonical Agents**: Defined in `.devin/agents/` as structured JSON specifications adhering to `amos-{descriptive-name}-agent.json`.
- **200+ Canonical Workflows**: Defined in `.devin/workflows/` as step-by-step procedures in markdown (`amos-{name}-workflow.md`).
- **Core Canon and MOCs**: Rooted in `00_ROOT/`, `01_CANON/`, `02_KERNEL/`, `03_CONTROL_PLANE/`, `11_KNOWLEDGE/`, and `25_COGNITIVE_MATRIX/`.

## Agent & Workflow Discovery Guidelines

When asked to execute tasks, analyze systems, or adopt specialized roles:
1. **Consult the Agent Registry**: Look up relevant specialized agents in [`.devin/agents/amos-agent-registry-index.md`](file:///Users/mac/Documents/AMOS_OS/.devin/agents/amos-agent-registry-index.md) or directly search [`.devin/agents/`](file:///Users/mac/Documents/AMOS_OS/.devin/agents).
2. **Execute Matching Workflows**: Find the corresponding procedure in [`.devin/workflows/`](file:///Users/mac/Documents/AMOS_OS/.devin/workflows) and follow its sequential verification, gate checks, and commit rules.
3. **Respect Invariants**:
   - `CAPABILITY != AUTHORITY`
   - `UNKNOWN/GAP != PASS`
   - `MODEL != OBSERVATION`
   - `SOURCE_CLAIM != VERIFIED`
   - `PROPOSAL != COMMIT`
