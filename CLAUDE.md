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
