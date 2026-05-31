#!/usr/bin/env python3
"""Validate the Claude marketplace package structure."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_NAME = "marco-claude-marketplace"
PLUGIN_NAME = "claude-tdd-cleancode-plugin"
PLUGIN_PATH = ROOT / "plugins" / PLUGIN_NAME


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    assert isinstance(payload, dict), f"{path} must contain a JSON object"
    return payload


class ClaudeMarketplaceStructureTest(unittest.TestCase):
    def test_marketplace_manifest(self) -> None:
        manifest = load_json(ROOT / ".claude-plugin" / "marketplace.json")
        plugin_source = f"./plugins/{PLUGIN_NAME}"
        self.assertEqual(manifest["name"], MARKETPLACE_NAME)
        self.assertEqual(manifest["owner"]["name"], "Marco Tedone")
        self.assertEqual(
            manifest["plugins"],
            [{"name": PLUGIN_NAME, "source": plugin_source}],
        )
        actual_source = manifest["plugins"][0]["source"]
        self.assertNotIn("..", actual_source)
        self.assertFalse(actual_source.startswith("/"))

    def test_plugin_manifest(self) -> None:
        manifest = load_json(PLUGIN_PATH / ".claude-plugin" / "plugin.json")
        self.assertEqual(manifest["name"], PLUGIN_NAME)
        self.assertTrue(manifest["description"])
        self.assertEqual(manifest["version"], "1.0.0")

    def test_plugin_assets_are_packaged(self) -> None:
        required_paths = [
            "CLAUDE.md",
            "README.md",
            "install.sh",
            "uninstall.sh",
            "skills/tdd-clean-code-workflow/SKILL.md",
            "skills/analyse-code-base-for-tdd/SKILL.md",
            "agents/planning-agent.md",
            "agents/testing-automation-agent.md",
            "agents/clean-code-agent.md",
            "agents/security-agent.md",
            "agents/audit-agent.md",
        ]
        for relative_path in required_paths:
            path = PLUGIN_PATH / relative_path
            self.assertTrue(path.is_file(), f"Missing {relative_path}")

    def test_scripts_are_executable(self) -> None:
        for script_name in ("install.sh", "uninstall.sh"):
            script = PLUGIN_PATH / script_name
            self.assertTrue(script.is_file(), f"Missing {script_name}")
            self.assertTrue(script.stat().st_mode & 0o111, f"{script_name} is not executable")

    def test_local_metadata_is_not_packaged(self) -> None:
        excluded_paths = [".git", ".idea", ".claude/settings.local.json"]
        for relative_path in excluded_paths:
            path = PLUGIN_PATH / relative_path
            self.assertFalse(path.exists(), f"Unexpected packaged metadata: {relative_path}")


if __name__ == "__main__":
    unittest.main()
