#!/usr/bin/env python3
"""Governed AMOS OS bootstrap for Agent Reach.

This adapter installs only the pinned Agent Reach Python package into an isolated
user tool environment when --apply is explicitly supplied. It never invokes
Agent Reach with --system and therefore does not authorize system package,
global tool, browser-cookie, or optional-channel mutation.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Sequence

UPSTREAM_REPOSITORY = "Panniantong/Agent-Reach"
UPSTREAM_COMMIT = "da5044d26fc6adddb6554d5679c94ac22e76e428"
EXPECTED_VERSION = "1.5.0"
PACKAGE_URL = (
    f"https://github.com/{UPSTREAM_REPOSITORY}/archive/{UPSTREAM_COMMIT}.zip"
)
VENV_DIR = Path.home() / ".agent-reach-venv"


def _run(argv: Sequence[str], *, timeout: int = 300) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(argv),
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
    )


def _venv_cli() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "agent-reach.exe"
    return VENV_DIR / "bin" / "agent-reach"


def resolve_cli() -> str | None:
    discovered = shutil.which("agent-reach")
    if discovered:
        return discovered
    fallback = _venv_cli()
    return str(fallback) if fallback.exists() else None


def parse_version(output: str) -> str | None:
    text = output.strip()
    prefixes = ("Agent Reach v", "Agent Reach ")
    for prefix in prefixes:
        if text.startswith(prefix):
            return text[len(prefix) :].strip()
    return None


def probe(cli: str) -> tuple[bool, str]:
    result = _run([cli, "version"], timeout=30)
    version = parse_version(result.stdout)
    ok = result.returncode == 0 and version == EXPECTED_VERSION
    detail = version or result.stdout.strip() or f"exit={result.returncode}"
    return ok, detail


def install_pinned_package() -> str:
    pipx = shutil.which("pipx")
    if pipx:
        result = _run([pipx, "install", "--force", PACKAGE_URL])
        if result.returncode != 0:
            raise RuntimeError(f"pipx install failed:\n{result.stdout}")
        cli = resolve_cli()
        if not cli:
            raise RuntimeError("pipx completed but agent-reach is not on PATH")
        return cli

    # PEP 668-safe fallback: isolated user venv, never the AMOS repository env.
    if not VENV_DIR.exists():
        result = _run([sys.executable, "-m", "venv", str(VENV_DIR)])
        if result.returncode != 0:
            raise RuntimeError(f"venv creation failed:\n{result.stdout}")

    if os.name == "nt":
        pip = VENV_DIR / "Scripts" / "python.exe"
    else:
        pip = VENV_DIR / "bin" / "python"
    result = _run([str(pip), "-m", "pip", "install", "--upgrade", PACKAGE_URL])
    if result.returncode != 0:
        raise RuntimeError(f"venv install failed:\n{result.stdout}")
    cli = _venv_cli()
    if not cli.exists():
        raise RuntimeError("venv install completed but agent-reach CLI is missing")
    return str(cli)


def safe_health_check(cli: str) -> int:
    # Upstream default is safe/check-only because --system is intentionally absent.
    result = _run([cli, "install", "--env=auto"], timeout=180)
    print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Governed AMOS bootstrap/check for pinned Agent Reach"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Install/update the pinned Agent Reach package in pipx or ~/.agent-reach-venv",
    )
    parser.add_argument(
        "--skip-health-check",
        action="store_true",
        help="Verify package identity only; do not run Agent Reach safe diagnostics",
    )
    args = parser.parse_args()

    cli = resolve_cli()
    if cli:
        ok, detail = probe(cli)
        if ok:
            print(f"Agent Reach v{detail} already matches pinned AMOS version.")
        elif not args.apply:
            print(
                f"Agent Reach identity mismatch ({detail}); expected v{EXPECTED_VERSION}. "
                "Re-run with --apply to install the pinned source.",
                file=sys.stderr,
            )
            return 2
        else:
            cli = install_pinned_package()
    elif args.apply:
        cli = install_pinned_package()
    else:
        print(
            "Agent Reach is not installed. Re-run with --apply to install the pinned source.",
            file=sys.stderr,
        )
        return 2

    ok, detail = probe(cli)
    if not ok:
        print(
            f"Pinned package verification failed: expected {EXPECTED_VERSION}, got {detail}",
            file=sys.stderr,
        )
        return 3

    print(f"Verified Agent Reach v{EXPECTED_VERSION} from pinned upstream commit.")
    if args.skip_health_check:
        return 0
    return safe_health_check(cli)


if __name__ == "__main__":
    raise SystemExit(main())
