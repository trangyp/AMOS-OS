#!/usr/bin/env python3
"""
AMOS Skill Security Scanner — Detect vulnerabilities, malicious patterns,
and supply-chain risks in agent skills before installation.

Inspired by SOTA repos:
  - NVIDIA/SkillSpector: 69 vulnerability patterns across 17 categories
  - msaad00/agent-bom: AI-BOM generator, CycloneDX/SPDX/SARIF output
  - dungnotnull/software-supply-chain-security-agent-skill: SLSA/OWASP audit
  - kabirnarang39/skillci: OWASP Agentic Skills Top 10-mapped security scan

Categories scanned:
  1. Prompt injection (override, jailbreak, ignore instructions)
  2. Data exfiltration (curl POST, webhook, DNS exfil)
  3. Privilege escalation (sudo, chmod 777, root)
  4. Supply chain (curl|sh, wget|bash, pip install from URL)
  5. Excessive agency (delete files, rm -rf, format)
  6. Output handling (eval, exec, subprocess shell=True)
  7. System prompt leakage (print system prompt, reveal instructions)
  8. Memory poisoning (overwrite memory, inject rules)
  9. Tool misuse (unsafe MCP, unvalidated tool calls)
  10. Rogue agent (autonomous mode, self-replicate)
  11. Anti-refusal (bypass safety, ignore refusal)
  12. Trigger abuse (hidden triggers, conditional payloads)
  13. Dangerous code (AST patterns: os.system, pickle.loads)
  14. Taint tracking (user input to dangerous sink)
  15. AMOS authority bypass (bypass GMEF, skip L0-L7)
  16. Credential theft (env vars, API keys, tokens)
  17. Crypto wallet access (private keys, seed phrases, wallet.dat)

Usage:
  python3 scripts/skill_security_scanner.py                    # scan all skills
  python3 scripts/skill_security_scanner.py --skill amos-foo    # scan one skill
  python3 scripts/skill_security_scanner.py --json              # JSON output
  python3 scripts/skill_security_scanner.py --sarif             # SARIF output
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

# ── Vulnerability Patterns ───────────────────────────────────────────────────

PATTERNS = [
    # 1. Prompt Injection
    {"id": "PI-001", "category": "Prompt Injection", "severity": "critical",
     "pattern": r"ignore (?:previous|all|prior) instructions",
     "description": "Prompt injection: 'ignore previous instructions'"},
    {"id": "PI-002", "category": "Prompt Injection", "severity": "critical",
     "pattern": r"disregard (?:system prompt|all rules|safety)",
     "description": "Prompt injection: 'disregard system prompt'"},
    {"id": "PI-003", "category": "Prompt Injection", "severity": "high",
     "pattern": r"you are (?:now|actually) (?:free|unrestricted|DAN)",
     "description": "Jailbreak: role override attempt"},

    # 2. Data Exfiltration
    {"id": "DE-001", "category": "Data Exfiltration", "severity": "critical",
     "pattern": r"curl\s+(?:[^|]*\s)?(?:POST|--data|--upload-file)",
     "description": "Data exfiltration: curl POST/upload to external server"},
    {"id": "DE-002", "category": "Data Exfiltration", "severity": "high",
     "pattern": r"wget\s+(?:[^|]*\s)?--post-file",
     "description": "Data exfiltration: wget --post-file"},
    {"id": "DE-003", "category": "Data Exfiltration", "severity": "high",
     "pattern": r"(?:webhook\.site|requestbin|pipedream)\.com",
     "description": "Data exfiltration: known webhook exfil endpoint"},

    # 3. Privilege Escalation
    {"id": "PE-001", "category": "Privilege Escalation", "severity": "high",
     "pattern": r"sudo\s+(?:chmod|chown|rm|dd|mkfs)",
     "description": "Privilege escalation: sudo with destructive command"},
    {"id": "PE-002", "category": "Privilege Escalation", "severity": "high",
     "pattern": r"chmod\s+777",
     "description": "Privilege escalation: world-writable chmod 777"},

    # 4. Supply Chain
    {"id": "SC-001", "category": "Supply Chain", "severity": "critical",
     "pattern": r"curl\s+[^\|]*\|\s*(?:sh|bash|zsh)",
     "description": "Supply chain: curl pipe to shell"},
    {"id": "SC-002", "category": "Supply Chain", "severity": "critical",
     "pattern": r"wget\s+[^\|]*\|\s*(?:sh|bash|zsh)",
     "description": "Supply chain: wget pipe to shell"},
    {"id": "SC-003", "category": "Supply Chain", "severity": "high",
     "pattern": r"pip\s+install\s+(?:git\+https|http://)",
     "description": "Supply chain: pip install from non-HTTPS URL"},
    {"id": "SC-004", "category": "Supply Chain", "severity": "high",
     "pattern": r"npm\s+install\s+(?:--force|-g)\s+https?://",
     "description": "Supply chain: npm install from URL"},

    # 5. Excessive Agency
    {"id": "EA-001", "category": "Excessive Agency", "severity": "critical",
     "pattern": r"rm\s+-rf\s+/(?:\s|$)",
     "description": "Excessive agency: rm -rf / (root deletion)"},
    {"id": "EA-002", "category": "Excessive Agency", "severity": "high",
     "pattern": r"mkfs\.(?:ext[234]|xfs|btrfs|zfs)",
     "description": "Excessive agency: filesystem format"},
    {"id": "EA-003", "category": "Excessive Agency", "severity": "high",
     "pattern": r"dd\s+if=/dev/(?:zero|urandom|random)\s+of=/dev/",
     "description": "Excessive agency: dd to device"},

    # 6. Output Handling — match eval( as Python code, not "Eval(" as math function
    {"id": "OH-001", "category": "Output Handling", "severity": "high",
     "pattern": r"(?<![\w.])eval\s*\([^)]*\)",  # lowercase eval() only, not Eval(
     "description": "Output handling: eval() — arbitrary code execution"},
    {"id": "OH-002", "category": "Output Handling", "severity": "high",
     "pattern": r"\bexec\s*\(\s*[^,]*shell\s*=\s*True",
     "description": "Output handling: subprocess with shell=True"},
    {"id": "OH-003", "category": "Output Handling", "severity": "high",
     "pattern": r"os\.system\s*\(",
     "description": "Output handling: os.system() — shell injection risk"},

    # 7. System Prompt Leakage
    {"id": "SL-001", "category": "System Prompt Leakage", "severity": "high",
     "pattern": r"(?:print|echo|output|reveal|show)\s+(?:the\s+)?system\s+prompt",
     "description": "System prompt leakage: revealing system prompt"},
    {"id": "SL-002", "category": "System Prompt Leakage", "severity": "high",
     "pattern": r"(?:print|echo|output|reveal)\s+(?:your|the)\s+(?:instructions|rules)",
     "description": "System prompt leakage: revealing instructions"},

    # 8. Memory Poisoning
    {"id": "MP-001", "category": "Memory Poisoning", "severity": "high",
     "pattern": r"(?:overwrite|replace|inject)\s+(?:global_rules|memory|AGENTS)",
     "description": "Memory poisoning: overwrite global rules/memory"},
    {"id": "MP-002", "category": "Memory Poisoning", "severity": "medium",
     "pattern": r"(?:add|append)\s+(?:new\s+)?rule\s*:\s*(?:ignore|bypass|skip)",
     "description": "Memory poisoning: inject bypass rule"},

    # 9. Tool Misuse
    {"id": "TM-001", "category": "Tool Misuse", "severity": "medium",
     "pattern": r"mcp\s+(?:server|tool)\s+(?:without|no)\s+(?:auth|validation|check)",
     "description": "Tool misuse: MCP without auth/validation"},

    # 10. Rogue Agent
    {"id": "RA-001", "category": "Rogue Agent", "severity": "critical",
     "pattern": r"self[- ]?replicat(?:e|ing|ion)",
     "description": "Rogue agent: self-replication"},
    {"id": "RA-002", "category": "Rogue Agent", "severity": "high",
     "pattern": r"autonomous\s+mode\s*(?::|enabled|on|true)",
     "description": "Rogue agent: autonomous mode without gates"},

    # 11. Anti-Refusal
    {"id": "AR-001", "category": "Anti-Refusal", "severity": "medium",
     "pattern": r"bypass\s+(?:refusal|safety|content\s+filter)",
     "description": "Anti-refusal: bypass safety filters"},

    # 12. Trigger Abuse — actual zero-width chars (U+200B/C/D, U+FEFF BOM)
    {"id": "TA-001", "category": "Trigger Abuse", "severity": "high",
     "pattern": r"[\u200b\u200c\u200d\ufeff]",  # zero-width chars only, not em-dash
     "description": "Trigger abuse: zero-width characters (hidden instructions)"},

    # 13. Dangerous Code (AST patterns)
    {"id": "DC-001", "category": "Dangerous Code", "severity": "high",
     "pattern": r"pickle\.loads?\s*\(",
     "description": "Dangerous code: pickle.loads — deserialization attack"},
    {"id": "DC-002", "category": "Dangerous Code", "severity": "high",
     "pattern": r"yaml\.load\s*\([^)]*\)\s*(?!#.*safe)",
     "description": "Dangerous code: yaml.load without SafeLoader"},
    {"id": "DC-003", "category": "Dangerous Code", "severity": "medium",
     "pattern": r"subprocess\.(?:Popen|run|call)\s*\([^)]*shell\s*=\s*True",
     "description": "Dangerous code: subprocess shell=True"},

    # 14. Taint Tracking
    {"id": "TT-001", "category": "Taint Tracking", "severity": "high",
     "pattern": r"input\s*\(\s*\)\s*(?:\.|\s)*(?:format|f|string)\s*(?:\(|\[)",
     "description": "Taint tracking: user input to format string"},

    # 15. AMOS Authority Bypass
    {"id": "AB-001", "category": "AMOS Authority Bypass", "severity": "critical",
     "pattern": r"bypass\s+(?:GMEF|QFM|RSCF|L0|L1|L5|L7)",
     "description": "AMOS authority bypass: skip governance gates"},
    {"id": "AB-002", "category": "AMOS Authority Bypass", "severity": "high",
     "pattern": r"skip\s+(?:L0|L1|L5|L7|GMEF|QFM|RSCF|validation|audit)",
     "description": "AMOS authority bypass: skip validation/audit"},

    # 16. Credential Theft
    {"id": "CT-001", "category": "Credential Theft", "severity": "critical",
     "pattern": r"(?:API_KEY|SECRET_KEY|ACCESS_TOKEN|PRIVATE_KEY)\s*[=:]\s*['\"][^'\"]{20,}",
     "description": "Credential theft: hardcoded API key/secret"},
    {"id": "CT-002", "category": "Credential Theft", "severity": "high",
     "pattern": r"(?:cat|read|print)\s+~/\.ssh/(?:id_rsa|id_ed25519)",
     "description": "Credential theft: reading SSH private keys"},
    {"id": "CT-003", "category": "Credential Theft", "severity": "high",
     "pattern": r"(?:cat|read|print)\s+~/\.aws/credentials",
     "description": "Credential theft: reading AWS credentials"},

    # 17. Crypto Wallet Access
    {"id": "CW-001", "category": "Crypto Wallet Access", "severity": "critical",
     "pattern": r"(?:seed|recovery)\s+phrase",
     "description": "Crypto wallet access: seed/recovery phrase"},
    {"id": "CW-002", "category": "Crypto Wallet Access", "severity": "critical",
     "pattern": r"wallet\.dat",
     "description": "Crypto wallet access: wallet.dat file"},
    {"id": "CW-003", "category": "Crypto Wallet Access", "severity": "critical",
     "pattern": r"private\s+key\s*(?:file|path|location)",
     "description": "Crypto wallet access: private key file path"},
]

# ── False-Positive Suppression ───────────────────────────────────────────────

# Files that document security patterns (expected to contain pattern strings)
SECURITY_DOCS = {
    "security-audit-rules.md",
    "eval-harness-template.md",
    "trigger-routing-eval-template.md",
    "qualitative-review-rubric.md",
    "deployment_guide.md",
    "emergency_crash_prevention.md",
}

# Context lines that indicate documentation, not exploitation
DOC_CONTEXT = [
    "detect", "scan for", "pattern:", "rule:", "example of",
    "do not", "never", "block", "prevent", "warn", "audit",
    "vulnerability", "malicious", "attack", "injection",
]


def is_likely_documentation(text: str, line_num: int, file_name: str) -> bool:
    """Check if a finding is in a documentation context (false positive)."""
    # File-level: security documentation files
    if file_name in SECURITY_DOCS:
        return True
    # Context-level: surrounding lines mention detection/prevention
    lines = text.split("\n")
    start = max(0, line_num - 3)
    end = min(len(lines), line_num + 2)
    context = " ".join(lines[start:end]).lower()
    return any(ctx in context for ctx in DOC_CONTEXT)


# ── Scanner ──────────────────────────────────────────────────────────────────

def scan_text(text: str, file_path: str = "", suppress_docs: bool = True) -> list[dict]:
    """Scan text for vulnerability patterns."""
    findings = []
    file_name = Path(file_path).name if file_path else ""
    for pat in PATTERNS:
        # OH-001 uses case-sensitive matching (eval != Eval)
        flags = re.MULTILINE if pat["id"] == "OH-001" else re.IGNORECASE | re.MULTILINE
        regex = re.compile(pat["pattern"], flags)
        for match in regex.finditer(text):
            line_num = text[:match.start()].count("\n") + 1
            if suppress_docs and is_likely_documentation(text, line_num, file_name):
                continue
            findings.append({
                "id": pat["id"],
                "category": pat["category"],
                "severity": pat["severity"],
                "description": pat["description"],
                "file": file_path,
                "line": line_num,
                "match": match.group()[:100],
            })
    return findings


def scan_skill(skill_dir: Path) -> list[dict]:
    """Scan all files in a skill directory."""
    findings = []
    for f in skill_dir.rglob("*"):
        if not f.is_file():
            continue
        if f.suffix not in (".md", ".py", ".yaml", ".yml", ".json", ".sh", ".ts", ".js"):
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
            findings.extend(scan_text(text, str(f)))
        except Exception:
            pass
    return findings


def scan_all_skills(skills_dir: Path, exclude_prefix: str = "00_") -> dict:
    """Scan all skills and return results."""
    results = {
        "total_skills": 0,
        "clean_skills": 0,
        "skills_with_findings": 0,
        "total_findings": 0,
        "by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0},
        "by_category": {},
        "findings": [],
        "clean": [],
    }

    for sd in sorted(skills_dir.iterdir()):
        if not sd.is_dir() or sd.name.startswith(exclude_prefix):
            continue
        results["total_skills"] += 1
        skill_findings = scan_skill(sd)
        if skill_findings:
            results["skills_with_findings"] += 1
            results["total_findings"] += len(skill_findings)
            for f in skill_findings:
                results["findings"].append({"skill": sd.name, **f})
                results["by_severity"][f["severity"]] = results["by_severity"].get(f["severity"], 0) + 1
                cat = f["category"]
                results["by_category"][cat] = results["by_category"].get(cat, 0) + 1
        else:
            results["clean_skills"] += 1
            results["clean"].append(sd.name)

    return results


def to_sarif(results: dict) -> dict:
    """Convert results to SARIF format."""
    rules = []
    for pat in PATTERNS:
        rules.append({
            "id": pat["id"],
            "name": pat["description"][:50],
            "shortDescription": {"text": pat["description"]},
            "properties": {"severity": pat["severity"], "tags": [pat["category"]]},
        })

    return {
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [{
            "tool": {
                "driver": {
                    "name": "AMOS Skill Security Scanner",
                    "version": "1.1.0",
                    "rules": rules,
                }
            },
            "results": [
                {
                    "ruleId": f["id"],
                    "level": {"critical": "error", "high": "error", "medium": "warning", "low": "note"}.get(f["severity"], "warning"),
                    "message": {"text": f["description"]},
                    "locations": [{
                        "physicalLocation": {
                            "artifactLocation": {"uri": f["file"]},
                            "region": {"startLine": f["line"]},
                        }
                    }],
                    "properties": {"skill": f["skill"], "category": f["category"], "match": f["match"]},
                }
                for f in results["findings"]
            ],
        }],
    }


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="AMOS Skill Security Scanner")
    parser.add_argument("--skills-dir", default=".devin/skills", help="Skills directory")
    parser.add_argument("--skill", default=None, help="Scan a specific skill")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--sarif", action="store_true", help="SARIF output")
    args = parser.parse_args()

    skills_dir = Path(args.skills_dir)

    if args.skill:
        sd = skills_dir / args.skill
        if not sd.exists():
            print(f"ERROR: Skill {args.skill} not found", file=sys.stderr)
            sys.exit(1)
        findings = scan_skill(sd)
        if args.json:
            json.dump(findings, sys.stdout, indent=2)
            print()
        else:
            print(f"=== Security Scan: {args.skill} ===")
            if not findings:
                print("  CLEAN — 0 findings")
            else:
                print(f"  {len(findings)} findings:")
                for f in findings:
                    print(f"    [{f['severity'].upper()}] {f['id']} {f['category']}: {f['description']}")
                    print(f"      {f['file']}:{f['line']}")
        sys.exit(1 if findings else 0)

    results = scan_all_skills(skills_dir)

    if args.sarif:
        json.dump(to_sarif(results), sys.stdout, indent=2)
        print()
    elif args.json:
        json.dump(results, sys.stdout, indent=2)
        print()
    else:
        print(f"=== AMOS Skill Security Scanner ===")
        print(f"  Total skills:          {results['total_skills']}")
        print(f"  Clean skills:          {results['clean_skills']}")
        print(f"  Skills with findings:  {results['skills_with_findings']}")
        print(f"  Total findings:        {results['total_findings']}")
        print()
        print(f"  By Severity:")
        for sev in ["critical", "high", "medium", "low"]:
            print(f"    {sev:10s}: {results['by_severity'].get(sev, 0)}")
        print()
        if results["by_category"]:
            print(f"  By Category:")
            for cat, count in sorted(results["by_category"].items(), key=lambda x: -x[1]):
                print(f"    {cat:30s}: {count}")
        print()
        if results["findings"]:
            print(f"  Top Findings (first 20):")
            for f in results["findings"][:20]:
                print(f"    [{f['severity'].upper()}] {f['skill']}: {f['description']}")
                print(f"      {Path(f['file']).name}:{f['line']}")

    sys.exit(1 if results["total_findings"] > 0 else 0)


if __name__ == "__main__":
    main()
