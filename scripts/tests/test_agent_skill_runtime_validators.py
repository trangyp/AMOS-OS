#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = REPO_ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import validate_agent_skill_surface as skill_surface
import validate_external_agent_sources as source_registry
import validate_workflow_references as workflow_refs


class ExternalSourceRegistryTests(unittest.TestCase):
    def valid_payload(self) -> dict:
        return {
            "registry_id": "AMOS_EXTERNAL_AGENT_SOURCE_REGISTRY",
            "schema_version": "1.0.0",
            "verified_at": "2026-09-14",
            "origin_architect": "Trang Phan",
            "steward": "Trang Phan",
            "epistemic_class": "OBSERVATION",
            "purpose": "test",
            "governance": {
                "default_admission_state": "REFERENCE_ONLY",
                "source_is_not_authority": True,
                "source_is_not_canon": True,
                "automatic_admission": False,
                "automatic_installation": False,
                "automatic_merge": False,
                "commit_pin_required": True,
                "allowed_resource_classes": ["SKILL"],
            },
            "sources": [
                {
                    "source_id": "test-source",
                    "repository": "owner/repo",
                    "url": "https://github.com/owner/repo",
                    "commit_sha": "a" * 40,
                    "verified_at": "2026-09-14",
                    "license": "MIT",
                    "license_scope": "Repository license.",
                    "resource_classes": ["SKILL"],
                    "mechanisms": ["portable skill"],
                    "amos_targets": ["07_SKILLS"],
                    "admission_state": "REFERENCE_ONLY",
                    "authority_effect": "NONE",
                }
            ],
        }

    def test_valid_reference_only_registry_passes(self) -> None:
        self.assertEqual(source_registry.validate_registry(self.valid_payload()), [])

    def test_bad_commit_pin_fails(self) -> None:
        payload = self.valid_payload()
        payload["sources"][0]["commit_sha"] = "main"
        errors = source_registry.validate_registry(payload)
        self.assertTrue(any("40-hex" in error for error in errors))

    def test_external_source_cannot_grant_authority(self) -> None:
        payload = self.valid_payload()
        payload["sources"][0]["authority_effect"] = "WRITE"
        payload["sources"][0]["authority_granted"] = True
        errors = source_registry.validate_registry(payload)
        self.assertTrue(any("authority_effect" in error for error in errors))
        self.assertTrue(any("may not grant" in error for error in errors))

    def test_admitted_source_requires_promotion_evidence(self) -> None:
        payload = self.valid_payload()
        payload["sources"][0]["admission_state"] = "ADMITTED"
        errors = source_registry.validate_registry(payload)
        self.assertTrue(any("promotion_evidence" in error for error in errors))


class SkillSurfaceTests(unittest.TestCase):
    def test_modern_skill_requires_existing_bundled_reference(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            skill_dir = Path(temporary) / "sample-skill"
            skill_dir.mkdir()
            path = skill_dir / "SKILL.md"
            path.write_text(
                "---\n"
                "name: sample-skill\n"
                "description: Use when a sufficiently concrete sample capability is required.\n"
                "---\n\n"
                "Load `references/missing.md`.\n",
                encoding="utf-8",
            )
            errors, warnings, name = skill_surface.validate_skill(path, strict_legacy=False)
            self.assertEqual(name, "sample-skill")
            self.assertFalse(warnings)
            self.assertTrue(any("does not exist" in error for error in errors))

    def test_legacy_skill_is_warning_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            skill_dir = Path(temporary) / "legacy"
            skill_dir.mkdir()
            path = skill_dir / "SKILL.md"
            path.write_text("# Legacy Skill\n", encoding="utf-8")
            errors, warnings, name = skill_surface.validate_skill(path, strict_legacy=False)
            self.assertFalse(errors)
            self.assertIsNone(name)
            self.assertTrue(warnings)


class WorkflowReferenceTests(unittest.TestCase):
    def test_missing_local_script_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            workflow = root / ".github" / "workflows" / "test.yml"
            workflow.parent.mkdir(parents=True)
            workflow.write_text(
                "name: test\n"
                "permissions:\n  contents: read\n"
                "jobs:\n  test:\n    steps:\n"
                "      - run: python3 scripts/missing.py\n",
                encoding="utf-8",
            )
            errors, _ = workflow_refs.validate_workflow(workflow, root, False)
            self.assertTrue(any("missing" in error for error in errors))

    def test_present_local_script_passes_reference_check(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            script = root / "scripts" / "check.py"
            script.parent.mkdir()
            script.write_text("print('ok')\n", encoding="utf-8")
            workflow = root / ".github" / "workflows" / "test.yml"
            workflow.parent.mkdir(parents=True)
            workflow.write_text(
                "name: test\n"
                "permissions:\n  contents: read\n"
                "jobs:\n  test:\n    steps:\n"
                "      - run: python3 scripts/check.py\n",
                encoding="utf-8",
            )
            errors, _ = workflow_refs.validate_workflow(workflow, root, False)
            self.assertFalse(errors)


if __name__ == "__main__":
    unittest.main()
