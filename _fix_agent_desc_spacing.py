#!/usr/bin/env python3
"""Fix spacing and redundancy issues in enhanced agent descriptions."""
import json, re
from pathlib import Path

AGENTS_DIR = Path("/Users/mac/Documents/AMOS_OS/.devin/agents")

fixed = 0
for af in sorted(AGENTS_DIR.glob("*.json")):
    try:
        data = json.loads(af.read_text())
        desc = data.get('description', '')
        original = desc
        
        # Fix 1: "Use when<word>" -> "Use when <word>"
        desc = re.sub(r'Use when([a-z])', r'Use when \1', desc)
        
        # Fix 2: "Agent that executes Executes ..." -> "Agent that executes ..."
        desc = re.sub(r'^Agent that executes (Executes|Orchestrates|Runs|Validates|Analyzes|Traces|Assesses|Generates|Builds|Transforms|Coordinates|Govern|Govern|Operates|Implements|Computes|Evaluates|Monitors|Detects|Classifies|Maps|Routes|Resolves|Compiles|Manages|Performs|Applies|Processes|Derives|Extracts|Constructs|Maintains|Queries|Assumes|Integrates|Bridges|Balances|Preserves|Enforces|Controls|Schedules|Dispatches|Allocates|Optimizes|Calibrates|Adjusts|Adapts|Evolves|Learns|Reasons|Infers|Deduces|Induces|Abstracts|Decomposes|Synthesizes|Composes|Combines|Merges|Splits|Forks|Clones|Replicates|Mirrors|Reflects|Projects|Extends|Expands|Contracts|Shrinks|Grows|Develops|Matures|Ages|Decays|Degrades|Recovers|Restores|Repairs|Heals|Regenerates|Renews|Refreshes|Reloads|Reboots|Restarts|Resumes|Continues|Pauses|Suspends|Halts|Stops|Starts|Begins|Initiates|Launches|Triggers|Fires|Activates|Deactivates|Disables|Enables|Toggles|Switches|Transitions|Migrates|Moves|Shifts|Transfers|Conveys|Carries|Delivers|Sends|Receives|Accepts|Rejects|Filters|Purges|Cleans|Wipes|Clears|Resets|Reinitializes)\s+', 'Agent that ', desc)
        
        # Fix 3: "Agent that executes <Name> defines ..." -> "Agent that enforces <Name> defines ..."
        # Actually better: "Agent that executes L26 defines..." -> "Agent for L26: defines..."
        desc = re.sub(r'^Agent that executes (L\d+|P\d+|K_|DMER|URTA|CAS|GMEF|RSCF|UBI|QLS|QCLA|BEI|NBI|NEI|SI|COSMO|TRANG)\s+', r'Agent for \1: ', desc)
        
        # Fix 4: Double spaces
        desc = re.sub(r'  +', ' ', desc)
        
        if desc != original:
            data['description'] = desc
            # Also fix role if it contains the same issues
            role = data.get('role', '')
            if role:
                role = re.sub(r'Use when([a-z])', r'Use when \1', role)
                role = re.sub(r'  +', ' ', role)
                data['role'] = role
            af.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
            fixed += 1
            print(f"  FIXED {af.stem}: {original[:60]}... -> {desc[:60]}...")
    except Exception as e:
        print(f"  ERROR {af.stem}: {e}")

print(f"\nFixed: {fixed}")
