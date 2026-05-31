# Marco Claude Marketplace

This repository packages Claude Code plugins for local marketplace installation.

## Plugin Audit Log

### 2026-05-31

Decision: Created a Claude Code-only marketplace for `claude-tdd-cleancode-plugin`.
Reason: The repository is intended to expose the existing TDD/Clean Code workflow plugin through Claude Code marketplace discovery, not Codex marketplace discovery.
Agents: planning-agent, architect-agent, testing-automation-agent, security-agent, clean-code-agent, operational-readiness-agent, technical-documentation-agent, audit-agent.
Quality Gates: Gate 1 PASSED, Gate 0 PASSED, Gate 2 PASSED, Gate 3 PASSED, Gate 4 PASSED, Gate 5 PASSED, Gate 6 PASSED, Gate 7 PASSED, Gate 8 PASSED.
Reusable Learning: Claude marketplaces use `.claude-plugin/marketplace.json`, while each plugin uses `.claude-plugin/plugin.json` inside its plugin directory. Same-repository plugin sources should stay relative to the marketplace root.
Rule Changes: None.
Follow-Up: Install locally with `claude plugin marketplace add /Users/marcotedone/dev/claude-tools/marco-claude-marketplace`, then install `claude-tdd-cleancode-plugin@marco-claude-marketplace`.

### 2026-05-31

Decision: Removed legacy `install.sh` and `uninstall.sh` from the packaged marketplace plugin.
Reason: The legacy installer registered a `local` marketplace using `"source": "local"`, which current Claude Code rejects with `local.source.source: Invalid input`.
Agents: testing-automation-agent, security-agent, clean-code-agent, audit-agent.
Quality Gates: Gate 2 PASSED, Gate 3 PASSED, Gate 4 PASSED, Gate 5 PASSED, Gate 6 PASSED, Gate 8 PASSED.
Reusable Learning: Marketplace plugins should be installed through `claude plugin marketplace add` and `claude plugin install`; package-local scripts that mutate `~/.claude/plugins/known_marketplaces.json` can corrupt marketplace state when schemas change.
Rule Changes: Do not package legacy home-directory installer scripts in Claude marketplace plugins.
Follow-Up: Remove the stale `local` marketplace entry from `~/.claude/plugins/known_marketplaces.json` before retrying installation.
