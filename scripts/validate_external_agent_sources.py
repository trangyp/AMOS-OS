#!/usr/bin/env python3
"""Validate the AMOS external agent/skill source registry.

This validator is intentionally network-free. A pinned external source is evidence
of what AMOS inspected, not proof that the source is currently safe, available,
or authorized. Remote freshness checks belong in a separate observation workflow.
"""

from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
from typing import Any

DEFAULT_REGISTRY = Path("11_KNOWLEDGE/EXTERNAL_AGENT_SOURCE_REGISTRY.json")
SHA40 = re.compile(r"^[0-9a-f]{40}$")
REPOSITORY = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
SOURCE_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_STATES = {"REFERENCE_ONLY", "CANDIDATE", "QUARANTINED", "ADMITTED"}
FORBIDDEN_TRUTHY_KEYS = {
    "auto_admit",
    "auto_admission",
    "auto_install",
    "auto_installation",
    "auto_merge",
    "authority_granted",
    "inherits_authority",
}


def load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"registry not found: {path}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON at {path}:{exc.lineno}:{exc.colno}: {exc.msg}") from None
    if not isinstance(payload, dict):
        raise ValueError("registry root must be a JSON object")
    return payload


def walk_truthy_forbidden(value: Any, pointer: str = "$") -> list[str]:
    errors: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_pointer = f"{pointer}.{key}"
            if key in FORBIDDEN_TRUTHY_KEYS and bool(child):
                errors.append(f"{child_pointer}: external sources may not grant or auto-exercise authority")
            errors.extend(walk_truthy_forbidden(child, child_pointer))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            errors.extend(walk_truthy_forbidden(child, f"{pointer}[{index}]"))
    return errors


def require_nonempty_string(obj: dict[str, Any], key: str, pointer: str, errors: list[str]) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{pointer}.{key}: required non-empty string")
        return ""
    return value.strip()


def require_string_list(obj: dict[str, Any], key: str, pointer: str, errors: list[str]) -> list[str]:
    value = obj.get(key)
    if not isinstance(value, list) or not value:
        errors.append(f"{pointer}.{key}: required non-empty list")
        return []
    if not all(isinstance(item, str) and item.strip() for item in value):
        errors.append(f"{pointer}.{key}: every item must be a non-empty string")
        return []
    return [item.strip() for item in value]


def validate_date(value: str, pointer: str, errors: list[str]) -> None:
    if not value:
        return
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        errors.append(f"{pointer}: expected ISO date YYYY-MM-DD")
        return
    if parsed > date.today():
        errors.append(f"{pointer}: verification date is in the future")


def validate_registry(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if payload.get("registry_id") != "AMOS_EXTERNAL_AGENT_SOURCE_REGISTRY":
        errors.append("$.registry_id: unexpected registry identity")
    if payload.get("epistemic_class") not in {"OBSERVATION", "SOURCE_CLAIM"}:
        errors.append("$.epistemic_class: external source registry must remain OBSERVATION or SOURCE_CLAIM")

    verified_at = require_nonempty_string(payload, "verified_at", "$", errors)
    validate_date(verified_at, "$.verified_at", errors)

    governance = payload.get("governance")
    if not isinstance(governance, dict):
        errors.append("$.governance: required object")
        governance = {}

    hard_false = ("automatic_admission", "automatic_installation", "automatic_merge")
    for key in hard_false:
        if governance.get(key) is not False:
            errors.append(f"$.governance.{key}: must be false")
    if governance.get("source_is_not_authority") is not True:
        errors.append("$.governance.source_is_not_authority: must be true")
    if governance.get("source_is_not_canon") is not True:
        errors.append("$.governance.source_is_not_canon: must be true")
    if governance.get("commit_pin_required") is not True:
        errors.append("$.governance.commit_pin_required: must be true")

    allowed_resource_classes_raw = governance.get("allowed_resource_classes")
    if not isinstance(allowed_resource_classes_raw, list) or not allowed_resource_classes_raw:
        errors.append("$.governance.allowed_resource_classes: required non-empty list")
        allowed_resource_classes: set[str] = set()
    else:
        allowed_resource_classes = {
            item for item in allowed_resource_classes_raw if isinstance(item, str) and item
        }
        if len(allowed_resource_classes) != len(allowed_resource_classes_raw):
            errors.append("$.governance.allowed_resource_classes: values must be unique non-empty strings")

    sources = payload.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("$.sources: required non-empty list")
        return errors + walk_truthy_forbidden(payload)

    source_ids: set[str] = set()
    repositories: set[str] = set()
    pins: set[tuple[str, str]] = set()

    for index, source in enumerate(sources):
        pointer = f"$.sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{pointer}: expected object")
            continue

        source_id = require_nonempty_string(source, "source_id", pointer, errors)
        repository = require_nonempty_string(source, "repository", pointer, errors)
        url = require_nonempty_string(source, "url", pointer, errors)
        sha = require_nonempty_string(source, "commit_sha", pointer, errors)
        item_verified_at = require_nonempty_string(source, "verified_at", pointer, errors)
        license_name = require_nonempty_string(source, "license", pointer, errors)
        require_nonempty_string(source, "license_scope", pointer, errors)
        resource_classes = require_string_list(source, "resource_classes", pointer, errors)
        require_string_list(source, "mechanisms", pointer, errors)
        require_string_list(source, "amos_targets", pointer, errors)

        if source_id:
            if not SOURCE_ID.fullmatch(source_id):
                errors.append(f"{pointer}.source_id: expected lowercase-hyphenated identifier")
            if source_id in source_ids:
                errors.append(f"{pointer}.source_id: duplicate {source_id!r}")
            source_ids.add(source_id)

        if repository:
            if not REPOSITORY.fullmatch(repository):
                errors.append(f"{pointer}.repository: expected owner/name")
            if repository.lower() in repositories:
                errors.append(f"{pointer}.repository: duplicate repository {repository!r}")
            repositories.add(repository.lower())
            expected_url = f"https://github.com/{repository}"
            if url and url.rstrip("/") != expected_url:
                errors.append(f"{pointer}.url: must match repository identity ({expected_url})")

        if sha and not SHA40.fullmatch(sha):
            errors.append(f"{pointer}.commit_sha: expected lowercase 40-hex commit SHA")
        if repository and sha:
            pin = (repository.lower(), sha)
            if pin in pins:
                errors.append(f"{pointer}.commit_sha: duplicate source pin")
            pins.add(pin)

        validate_date(item_verified_at, f"{pointer}.verified_at", errors)
        if license_name == "MIXED" and "per imported path" not in str(source.get("license_scope", "")):
            errors.append(f"{pointer}.license_scope: MIXED licensing must require path-level verification")

        unknown_classes = set(resource_classes) - allowed_resource_classes
        if unknown_classes:
            errors.append(
                f"{pointer}.resource_classes: unknown classes {sorted(unknown_classes)}"
            )

        state = source.get("admission_state")
        if state not in ALLOWED_STATES:
            errors.append(f"{pointer}.admission_state: expected one of {sorted(ALLOWED_STATES)}")
        if state == "ADMITTED" and not source.get("promotion_evidence"):
            errors.append(f"{pointer}: ADMITTED source requires promotion_evidence")

        if source.get("authority_effect") != "NONE":
            errors.append(f"{pointer}.authority_effect: external source registration may not grant authority")

    errors.extend(walk_truthy_forbidden(payload))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args()

    try:
        payload = load_json(args.registry)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors = validate_registry(payload)
    if errors:
        print("External agent source registry: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    source_count = len(payload["sources"])
    class_count = len(payload["governance"]["allowed_resource_classes"])
    print(
        "External agent source registry: PASS "
        f"({source_count} pinned sources; {class_count} resource classes; no authority grant)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
