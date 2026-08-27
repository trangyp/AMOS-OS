---
tags: [fractal]
---
DETERMINISTIC_RULES = [
    "Every feature must have one clear intention.",
    "Every feature must define input contract.",
    "Every feature must define state or memory usage.",
    "Every feature must define output contract.",
    "Every transformation must be named.",
    "Same input under same memory and constraints must produce same output.",
    "Data flow must be explicit from input to output.",
    "No hidden state unless documented.",
    "No fake dependency.",
    "No fake application programming interface.",
    "No fake feature.",
    "No output before validation.",
    "No feature outside specification unless explicitly marked as proposed."
]

ENTROPY_RULES = [
    "Missing input creates entropy.",
    "Malformed input creates entropy.",
    "Ambiguous intention creates entropy.",
    "Conflicting constraints create entropy.",
    "External services create entropy.",
    "Unknown package versions create entropy.",
    "Unmapped dependency creates entropy.",
    "Hidden state creates entropy.",
    "Overgenerated feature creates entropy.",
    "Too many coupled modules without dependency graph create entropy.",
    "Entropy is layered deterministic complexity, not pure randomness."
]

VALIDATION_RULES = [
    "Check feature reality.",
    "Check data flow.",
    "Check dependency existence.",
    "Check state contract.",
    "Check output contract.",
    "Check error handling.",
    "Check forbidden claims.",
    "Check whether confidence must be lowered.",
    "Check whether entropy events were ignored."
]

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
