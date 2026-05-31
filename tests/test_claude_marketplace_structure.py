#!/usr/bin/env python3
"""Validate the Claude marketplace catalog structure."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_NAME = "marco-claude-marketplace"
PLUGIN_NAME = "claude-tdd-cleancode-plugin"
PLUGIN_REPO = "mtedone/claude-tdd-workflow-java"


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    assert isinstance(payload, dict), f"{path} must contain a JSON object"
    return payload


class ClaudeMarketplaceStructureTest(unittest.TestCase):
    def test_marketplace_manifest(self) -> None:
        manifest = load_json(ROOT / ".claude-plugin" / "marketplace.json")
        plugin_source = {"source": "github", "repo": PLUGIN_REPO}
        self.assertEqual(manifest["name"], MARKETPLACE_NAME)
        self.assertEqual(manifest["owner"]["name"], "Marco Tedone")
        self.assertEqual(
            manifest["plugins"],
            [{"name": PLUGIN_NAME, "source": plugin_source}],
        )
        actual_source = manifest["plugins"][0]["source"]
        self.assertEqual(actual_source["source"], "github")
        self.assertEqual(actual_source["repo"], PLUGIN_REPO)

    def test_marketplace_does_not_vendor_plugins(self) -> None:
        self.assertFalse((ROOT / "plugins").exists(), "Marketplace should reference plugin repos")


if __name__ == "__main__":
    unittest.main()
