---
title: "Vault Domain Knowledge — Amos Source Reading Rscf Engine"
type: reference
source: 07_SKILLS/amos-source-reading-rscf-engine/references
tags: [reference, amos-source-reading-rscf-engine, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-source-reading-rscf-engine`

## Vault-Sourced Content

### Source 1: AMOS 7-Part Universe Canon — Source Canon + Infrastructure Mapping

> Path: `amos-general/A/PART/AMOS_7_PART_UNIVERSE_CANON_REFINED.md` | Size: 19986 chars | Match score: 7

# AMOS 7-Part Universe Canon — Source Canon + Infrastructure Mapping


---

## 1. What the 7-Part Canon is for in AMOS

The 7-Part Universe Canon is best treated inside AMOS as a **persistence axis**.

It asks:

> What functions must be represented, in the source model, for a system to emerge, operate, change, persist, collapse, or recover?

The seven parts are:

1. **Constraint**
2. **Flow**
3. **Structure**
4. **Enforcement**
5. **Time**
6. **Adaptation**
7. **Termination**
AMOS uses this canon to test **structural coverage**, not to convert source-canon statements into empirical proof.

### Core distinction

```text
SOURCE_CANON != ESTABLISHED_SCIENTIFIC_LAW
STRUCTURAL_COMPLETENESS != EMPIRICAL_TRUTH
ALL_SEVEN_MAPPED != CAUSAL_PROOF
ANALOGY_ACROSS_DOMAINS != MECHANISM
```

---

# PART I — CONSTRAINT

## Source definition (3)


The source canon associates Constraint with:

- scarcity
- boundaries
- finite capacity
- irreversibility
- ceilings
- null spaces / non-applicability

### Source-canon law

> If there are no constraints, there is no bounded system in the canon model.

### AMOS interpretation

Constraint defines the **admissible state space**.

For an AMOS-controlled system, this includes:

- capability limits
- authority limits
- resource budgets
- context budgets
- temporal limits
- policy constraints
- effect boundaries
- scope/regime limits
- hard invariants

### Infrastructure mapping

```text
Constraint
→ capability envelope
→ authority envelope
→ resource / context budget
→ effect class
→ scope / regime / freshness bounds
```

### Failure signature

A system claims freedom or capability that its actual limits do not support.

### AMOS check

```text
ConstraintPass =
 HardLimitsDeclared
 AND AuthorityBounded
 AND ResourceBoundsKnown
 AND ScopeBounded
 AND EffectClassKnown
```

---

# PART II — FLOW

## Source definition (2)


The source canon emphasizes:

- input → transformation → output
- bottlenecks
- leakage
- queues
- conversion under limits

### Source-canon law

> Flow that cannot move through a bounded path cannot sustain system operation.

### AMOS interpretation

Flow is the movement of:

- information
- evidence
- state
- authority requests
- tool calls
- provenance
- decisions
- effects
- feedback
- recovery signals

### Infrastructure mapping

```text
Input
→ admission
→ transformation
→ validation
→ decision
→ effect proposal
→ commit / reject / rollback
```

### AMOS flow firewall

```text
DATA_FLOW != AUTHORITY_FLOW
EVIDENCE_FLOW != EFFECT_PERMISSION
TOOL_OUTPUT != ACCEPTED_KNOWLEDGE
MODEL_PROPOSAL != COMMITTED_ACTION
```

### Failure signature
- bottleneck
- stale queue
- provenance loss
- unauthorized information crossing
- evidence/action conflation
- partial state transfer

---

# PART III — STRUCTURE

## Source definition


The source canon associates Structure with:

- architecture
- hierarchy
- interfaces
- load-bearing elements
- repeatable organization

### Source-canon laws

> Flow without structu

---

### Source 2: **MANDATORY READING
- AGENT WORKING INSTRUCTIONS**
> Path: `agents/AGENT_WORKING_INSTRUCTIONS.md` | Size: 8637 chars | Match score: 7

# **MANDATORY READING - AGENT WORKING INSTRUCTIONS**
## IMMEDIATE ACTIONS REQUIRED

### **Step 1: Read the System Architecture Report**

Complete system architecture overview
- Status of all 10 vertical slices
- API endpoint reference
- Component performance metrics
- Working guidelines for agents

### **Step 2: Verify Component Status**
Before working on any component:

1. **Check Health Status**: Use `/health` endpoint to verify component is operational
2. **Identify Vertical Slice**: Know which component you're working with
3. **Understand Limitations**: Know what works and what doesn't
4. **Use Bridge Layers**: Access components through bridge layers, not directly

### **Step 3: Follow Working Guidelines**

Use established vertical slice architecture
- Follow bridge layer and API patterns
- Implement proper error handling
- Use audit logging for important operations
- Run acceptance tests before deploying
- Document any architectural changes

---

## COMPONENT STATUS SUMMARY

### ** FULLY OPERATIONAL COMPONENTS (Safe for Production)**

1. **Runtime Vertical Slice** (100% pass rate)
2. **Tools Vertical Slice** (functional integration)
3. **Governance Vertical Slice** (85% pass rate)
4. **Memory Vertical Slice** (84.2% pass rate)
5. **Brain Intelligence Vertical Slice** (91.3% pass rate)
6. **Audit & Security Vertical Slice** (91.7% pass rate)

### ** NEAR-COMPLETE COMPONENTS (Use with Caution)**

7. **Quantum Meta-Cognitive** (72.0% pass rate) - Minor syntax issues
8. **Metrics & Monitoring** (77.8% pass rate) - Minor syntax issues

### ** PARTIAL SUCCESS COMPONENTS (Limited Functionality)**

9. **Organ System** (42.1% pass rate) - Syntax errors in source files
10. **Super-Agent & Energy** (52.9% pass rate) - Syntax errors in source files

---

## CRITICAL WARNINGS

### ** HIGH RISK COMPONENTS**

Have syntax errors in source files
- Limited functionality available
- Use only for testing, not production
- Bridge layers provide basic fallback functionality

### ** MODERATE RISK COMPONENTS**

Minor syntax issues in source files
- Near-complete functionality available
- Bridge layers provide fallback functionality
- Use with caution

### ** LOW RISK COMPONENTS**

Fully operational and tested
- Safe for production use
- Recommended for all production work

---

## RECOMMENDED WORKFLOW

### **For Production Work:**

1. **Use Fully Operational Components** only
2. **Check Health Status** before use
3. **Follow API Patterns** exactly
4. **Implement Error Handling** with fallbacks
5. **Log All Operations** via audit endpoints
6. **Run Acceptance Tests** before deployment

### **For Development/Testing:**

1. **Can Use All Components** with appropriate caution
2. **Understand Limitations** of partial components
3. **Use Bridge Layers** for integration
4. **Test Fallback Systems** thoroughly
5. **Document Issues** found during testing

---

## Quick

---

### Source 3: 1) Resolve source folder (from cleaned zip in Downloads)

> Path: `amos-general/A/amos/amos_setup_mega.md` | Size: 3893 chars | Match score: 7

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "=== AMOS MEGA SETUP START ==="

# 1) Resolve source folder (from cleaned zip in Downloads)
SRC_BASE="$HOME/Downloads/AMOS-PUBLIC-AUTO-CLEAN"
if [ -d "$SRC_BASE/AMOS-PUBLIC" ]; then
 SRC="$SRC_BASE/AMOS-PUBLIC"
elif [ -d "$HOME/Downloads/AMOS-PUBLIC" ]; then
 SRC="$HOME/Downloads/AMOS-PUBLIC"
else
 echo "ERROR: Could not find cleaned AMOS-PUBLIC in Downloads."
 echo "Expected: \$HOME/Downloads/AMOS-PUBLIC-AUTO-CLEAN/AMOS-PUBLIC"
 exit 1
fi

echo "Source repo: $SRC"

# 2) Destination in Documents/GitHub
DEST_ROOT="$HOME/Documents/GitHub"
mkdir -p "$DEST_ROOT"

DEST="$DEST_ROOT/AMOS-PUBLIC-CLEAN"
if [ -d "$DEST" ]; then
 TS="$(date +"%Y%m%d_%H%M%S")"
 BACKUP="${DEST_ROOT}/AMOS-PUBLIC-CLEAN.bak_${TS}"
 echo "Existing AMOS-PUBLIC-CLEAN found. Moving to backup:"
 echo " $BACKUP"
 mv "$DEST" "$BACKUP"
fi

echo "Copying cleaned repo to: $DEST"
mkdir -p "$DEST"
rsync -a "$SRC"/ "$DEST"/

cd "$DEST"
echo "Now in: $(pwd)"

# 3) Virtual environment
if [ ! -d "amos_env" ]; then
 echo "Creating virtualenv amos_env..."
 python3 -m venv amos_env
else
 echo "Using existing amos_env..."
fi

echo "Upgrading pip/setuptools/wheel..."
./amos_env/bin/python -m ensurepip --upgrade || true
./amos_env/bin/python -m pip install --upgrade pip setuptools wheel || true

if [ -f "requirements.txt" ]; then
 echo "Installing from requirements.txt..."
 ./amos_env/bin/python -m pip install -r requirements.txt || true
fi

echo "Installing core runtime packages..."
./amos_env/bin/python -m pip install requests flask rich psutil uvicorn || true

# 4) Core folders
mkdir -p _AMOS_REPORTS _AMOS_QUARANTINE _AMOS_STATE_LOG

# 5) Reports + cleanup (if scripts exist)
if [ -f "scripts/dev/amos_reports_scan.py" ]; then
 echo "Running scripts/dev/amos_reports_scan.py..."
 ./amos_env/bin/python scripts/dev/amos_reports_scan.py || true
fi

if [ -x "scripts/dev/amos_clean_mega.sh" ]; then
 echo "Running scripts/dev/amos_clean_mega.sh..."
 bash scripts/dev/amos_clean_mega.sh || true
fi

# 6) Restart GOD_MODE + dashboards if scripts exist
echo "Restarting GOD_MODE + dashboards (if available)..."

pkill -f "AMOS_ORGANISM_OS.runtime_core.god_mode_ultra_core" >/dev/null 2>&1 || true
pkill -f "AMOS_ORGANISM_OS.runtime_core.god_mode_introspect_daemon" >/dev/null 2>&1 || true
pkill -f "AMOS_ORGANISM_OS.dashboard_live_fast" >/dev/null 2>&1 || true
pkill -f "AMOS_ORGANISM_OS.dashboard_live_hyper" >/dev/null 2>&1 || true
pkill -f "night_god_mode.sh" >/dev/null 2>&1 || true

sleep 1

if [ -x "scripts/run/night_god_mode.sh" ]; then
 echo "Starting scripts/run/night_god_mode.sh..."
 scripts/run/night_god_mode.sh > /tmp/night_god_mode.log 2>&1 &
 sleep 3
else
 echo "NOTE: scripts/run/night_god_mode.sh not found or not executable."
fi

if [ -x "scripts/run/god_mode_introspect_daemon.sh" ]; then
 echo "Starting scripts/run/god_mode_introspect_daemon.sh..."
 scripts/run/god_mode_introspect_daemon.sh > /tmp/god_mode_introspect_daemon.log 2>&1 &
```

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
