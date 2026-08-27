---
title: AMOS PIPELINE VERIFICATION
tags: [amos-general]
type: document
source: 11_KNOWLEDGE/amos-general
---


# AMOS_Pipeline_Verification

```python
#!/usr/bin/env python3
"""
CosmoBrain Pipeline — AMOS Syntax Verification Pipeline
Uses py_compile for non-destructive Python syntax/bytecode validation.

Traverses all 19 neuroscience-focused Python modules listed in
/docs/AMOS/05 Verification/AMOS Test Framework/AMOS Verification Components List.md
Section 2.2 ("Python verification pipeline using py_compile").

Non-destructive: does not import modules into runtime, only compiles.

Usage:
    python3 AMOS_Pipeline_Verification.py              # run full pipeline
    python3 AMOS_Pipeline_Verification.py --verbose   # detailed per-module output
    python3 AMOS_Pipeline_Verification.py --help      # show usage
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import py_compile
import sys
import traceback
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# =============================================================================
# Configuration
# =============================================================================

ROOT_DIR = Path("/Users/mac/Downloads/stitch_project_cosmo/_00_Cosmo brain/python_modules")
LOG_DIR = Path("/Users/mac/Downloads/stitch_project_cosmo/_00_Cosmo brain/logs")
REPORT_PATH = LOG_DIR / "verification_reports" / "AMOS_PyCompile_Verification.json"


# =============================================================================
# Enums
# =============================================================================

class VerificationResult(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    SKIP = "SKIP"
    ERROR = "ERROR"


class Severity(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR_SEV = "ERROR"


# =============================================================================
# Dataclasses
# =============================================================================

@dataclass
class ModuleCheck:
    """Result of checking one Python module via py_compile."""
    module_path: str
    module_name: str
    relative_path: str
    syntax_ok: bool
    compiled_ok: bool
    file_size_bytes: int
    mtime: float
    result: VerificationResult
    error_message: Optional[str] = None
    duration_ms: float = 0.0
    timestamp: str = ""


@dataclass
class PipelineReport:
    """Full pipeline run report."""
    run_id: str
    timestamp: str
    pipeline_name: str
    version: str
    total_modules: int
    modules_checked: int
    passed: int
    failed: int
    skipped: int
    errors: int
    total_duration_ms: float
    module_results: List[ModuleCheck] = field(default_factory=list)
    summary: str = ""
    success: bool = False


# =============================================================================
# Module Registry
# =============================================================================

# 19 neuroscience-focused modules from Section 2.2
NEURO_MODULES: List[str] = [
    "AMOS_Pipeline_Verification.py",
    "AMOS_Automatic_Documentation.py",
    "AMOS_Biological_Network_Model.py",
    "AMOS_Cochlear_Model.py",
    "AMOS_Common_Experimental_Utils.py",
    "AMOS_DefaultDataset.py",
    "AMOS_Engine_Model_Trainer.py",
    "AMOS_Filtering_Module.py",
    "AMOS_Hamming_With_Threshold.py",
    "AMOS_MedCAT_Adaptor.py",
    "AMOS_Model_Signing.py",
    "AMOS_Normalization_Utils.py",
    "AMOS_Performance_Utils.py",
    "AMOS_Pipeline_Status.py",
    "AMOS_Spectrogram_Utils.py",
    "AMOS_Upload.py",
    "AMOS_Validation_Pipeline.py",
    "AMOS_Version_Control.py",
    "AMOS_Vision_Processing.py",
]


def get_module_paths() -> List[Path]:
    """Resolve all module paths from the registry."""
    paths: List[Path] = []
    for name in NEURO_MODULES:
        p = ROOT_DIR / name
        if p.exists():
            paths.append(p)
        else:
            print(f"WARNING: Module not found: {name}", file=sys.stderr)
    return paths


# =============================================================================
# Verification Logic
# =============================================================================

def verify_module(path: Path, verbose: bool = False) -> ModuleCheck:
    """Verify a single Python module using py_compile.

    Non-destructive: compiles to bytecode cache, does not import.
    """
    start = datetime.now()

    module_name = path.stem
    relative = str(path.relative_to(ROOT_DIR)) if path.exists() else str(path)
    file_size = path.stat().st_size if path.exists() else 0
    mtime = path.stat().st_mtime if path.exists() else 0.0

    if not path.exists():
        return ModuleCheck(
            module_path=str(path),
            module_name=module_name,
            relative_path=relative,
            syntax_ok=False,
            compiled_ok=False,
            file_size_bytes=0,
            mtime=0.0,
            result=VerificationResult.SKIP,
            error_message=f"File not found: {path}",
            timestamp=datetime.now().isoformat(),
        )

    if path.suffix != ".py":
        return ModuleCheck(
            module_path=str(path),
            module_name=module_name,
            relative_path=relative,
            syntax_ok=False,
            compiled_ok=False,
            file_size_bytes=file_size,
            mtime=mtime,
            result=VerificationResult.SKIP,
            error_message=f"Not a Python file: {path.suffix}",
            timestamp=datetime.now().isoformat(),
        )

    # Phase 1: py_compile — compile to bytecode
    compile_ok = False
    error_msg: Optional[str] = None

    try:
        py_compile.compile(str(path), doraise=True, quiet=1)
        compile_ok = True
    except py_compile.PyCompileError as e:
        error_msg = str(e)
        if verbose:
            print(f"  FAIL compile: {module_name}: {error_msg}", file=sys.stderr)
    except Exception as e:
        error_msg = f"Unexpected error during compile: {type(e).__name__}: {e}"
        if verbose:
            print(f"  ERROR: {module_name}: {error_msg}", file=sys.stderr)

    duration_ms = (datetime.now() - start).total_seconds() * 1000

    if compile_ok:
        result = VerificationResult.PASS
        syntax_ok = True
    else:
        result = VerificationResult.FAIL
        syntax_ok = False

    check = ModuleCheck(
        module_path=str(path),
        module_name=module_name,
        relative_path=relative,
        syntax_ok=syntax_ok,
        compiled_ok=compile_ok,
        file_size_bytes=file_size,
        mtime=mtime,
        result=result,
        error_message=error_msg,
        duration_ms=round(duration_ms, 2),
        timestamp=datetime.now().isoformat(),
    )

    if verbose and result == VerificationResult.PASS:
        print(f"  PASS: {module_name} ({file_size} bytes, {duration_ms:.1f}ms)")

    return check


# =============================================================================
# Report Generation
# =============================================================================

def generate_report(results: List[ModuleCheck], duration_ms: float, verbose: bool) -> PipelineReport:
    """Generate a PipelineReport from verification results."""
    total = len(results)
    passed = sum(1 for r in results if r.result == VerificationResult.PASS)
    failed = sum(1 for r in results if r.result == VerificationResult.FAIL)
    skipped = sum(1 for r in results if r.result == VerificationResult.SKIP)
    errors = sum(1 for r in results if r.result == VerificationResult.ERROR)

    run_id = hashlib.sha256(
        f"py_compile_{datetime.now().isoformat()}_{total}_{passed}".encode()
    ).hexdigest()[:16]

    pipeline_name = "AMOS Pipeline Verification"
    version = "v1.0.0"
    success = failed == 0 and errors == 0

    # Build summary
    if success:
        summary = f"All {total} modules passed py_compile verification."
    else:
        parts: List[str] = []
        if failed:
            parts.append(f"{failed} module(s) failed compilation")
        if errors:
            parts.append(f"{errors} module(s) had errors")
        if skipped:
            parts.append(f"{skipped} module(s) skipped")
        summary = "; ".join(parts) + f" out of {total} modules."

    report = PipelineReport(
        run_id=run_id,
        timestamp=datetime.now().isoformat(),
        pipeline_name=pipeline_name,
        version=version,
        total_modules=total,
        modules_checked=total,
        passed=passed,
        failed=failed,
        skipped=skipped,
        errors=errors,
        total_duration_ms=round(duration_ms, 2),
        module_results=results,
        summary=summary,
        success=success,
    )

    return report


def write_report(report: PipelineReport, path: Path) -> None:
    """Write the report as JSON to disk."""
    path.parent.mkdir(parents=True, exist_ok=True)

    # Convert to dict for JSON serialization
    data: Dict[str, Any] = {
        "run_id": report.run_id,
        "timestamp": report.timestamp,
        "pipeline_name": report.pipeline_name,
        "version": report.version,
        "total_modules": report.total_modules,
        "modules_checked": report.modules_checked,
        "passed": report.passed,
        "failed": report.failed,
        "skipped": report.skipped,
        "errors": report.errors,
        "total_duration_ms": report.total_duration_ms,
        "summary": report.summary,
        "success": report.success,
        "module_results": [
            {
                "module_path": r.module_path,
                "module_name": r.module_name,
                "relative_path": r.relative_path,
                "syntax_ok": r.syntax_ok,
                "compiled_ok": r.compiled_ok,
                "file_size_bytes": r.file_size_bytes,
                "mtime": r.mtime,
                "result": r.result.value,
                "error_message": r.error_message,
                "duration_ms": r.duration_ms,
                "timestamp": r.timestamp,
            }
            for r in report.module_results
        ],
    }

    with open(path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"\nReport written to: {path}", file=sys.stderr)


def print_summary(report: PipelineReport) -> None:
    """Print a human-readable summary to stdout."""
    print("\n" + "=" * 70)
    print(f"  {report.pipeline_name} — {report.version}")
    print(f"  Run ID: {report.run_id}")
    print(f"  Timestamp: {report.timestamp}")
    print("=" * 70)
    print(f"  Total modules:    {report.total_modules}")
    print(f"  Passed:           {report.passed}")
    print(f"  Failed:           {report.failed}")
    print(f"  Skipped:          {report.skipped}")
    print(f"  Errors:           {report.errors}")
    print(f"  Duration:         {report.total_duration_ms:.2f}ms")
    print("-" * 70)
    print(f"  Result: {'SUCCESS' if report.success else 'FAILURE'}")
    print(f"  Summary: {report.summary}")
    print("=" * 70)

    # Per-module detail if there were failures
    if report.failed > 0 or report.errors > 0:
        print("\n  Failed/Error modules:")
        for r in report.module_results:
            if r.result in (VerificationResult.FAIL, VerificationResult.ERROR):
                status = "FAIL" if r.result == VerificationResult.FAIL else "ERROR"
                print(f"    [{status}] {r.module_name}: {r.error_message}")


# =============================================================================
# CLI
# =============================================================================

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="AMOS_Pipeline_Verification",
        description="Verify all CosmoBrain pipeline Python modules using py_compile.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 AMOS_Pipeline_Verification.py              Run full pipeline
  python3 AMOS_Pipeline_Verification.py --verbose   Show per-module detail
  python3 AMOS_Pipeline_Verification.py --list      List modules without verifying
  python3 AMOS_Pipeline_Verification.py --help      Show this help
        """,
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show per-module verification detail during run.",
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List all registered modules without verifying.",
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=REPORT_PATH,
        help=f"Path for JSON report output (default: {REPORT_PATH}).",
    )

    return parser


def list_modules() -> None:
    """Print all registered module names."""
    print(f"\nRegistered modules ({len(NEURO_MODULES)}):")
    print("-" * 50)
    for i, name in enumerate(NEURO_MODULES, 1):
        path = ROOT_DIR / name
        exists = "✓" if path.exists() else "✗"
        size = path.stat().st_size if path.exists() else 0
        print(f"  {i:2d}. {exists} {name:<45s} {size:>8d} bytes")
    print("-" * 50)


def run_pipeline(verbose: bool, output_path: Path) -> int:
    """Run the full verification pipeline.

    Returns exit code: 0 if all pass, 1 if any fail.
    """
    print(f"\n{'='*70}")
    print(f"  AMOS Pipeline Verification — py_compile syntax check")
    print(f"  Target: {ROOT_DIR}")
    print(f"{'='*70}")
    print(f"\nVerifying {len(NEURO_MODULES)} neuroscience modules...\n")

    # Resolve paths
    paths = get_module_paths()
    missing = len(NEURO_MODULES) - len(paths)
    if missing:
        print(f"WARNING: {missing} module(s) not found on disk.", file=sys.stderr)

    # Verify each module
    results: List[ModuleCheck] = []
    start = datetime.now()

    for path in paths:
        check = verify_module(path, verbose=verbose)
        results.append(check)

    duration_ms = (datetime.now() - start).total_seconds() * 1000

    # Generate and write report
    report = generate_report(results, duration_ms, verbose)
    write_report(report, output_path)
    print_summary(report)

    # Also write a plain-text log alongside
    log_path = LOG_DIR / "verification_reports" / f"AMOS_PyCompile_{report.run_id}.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "w") as f:
        f.write(f"Run ID: {report.run_id}\n")
        f.write(f"Timestamp: {report.timestamp}\n")
        f.write(f"Duration: {report.total_duration_ms:.2f}ms\n")
        f.write(f"Result: {'SUCCESS' if report.success else 'FAILURE'}\n")
        f.write(f"Modules: {report.passed}/{report.total_modules} passed\n")
        f.write("\nPer-module:\n")
        for r in report.module_results:
            status = r.result.value
            f.write(f"  [{status}] {r.module_name}: {r.relative_path} ({r.file_size_bytes} bytes)\n")
            if r.error_message:
                f.write(f"    Error: {r.error_message}\n")
    print(f"Log written to: {log_path}", file=sys.stderr)

    return 0 if report.success else 1


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list:
        list_modules()
        return 0

    return run_pipeline(args.verbose, args.output)


if __name__ == "__main__":
    sys.exit(main())


```

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
