# Marco Claude Marketplace

Local Claude Code plugin marketplace for Marco Tedone plugins.

## Included Plugins

- `claude-tdd-cleancode-plugin`: TDD and Clean Code workflow with planning, architecture, testing, security, implementation, refactoring, operational readiness, and audit gates.

## Validate

From this directory:

```bash
claude plugin validate .
```

You can also run the repository structural check:

```bash
python3 -m unittest tests/test_claude_marketplace_structure.py
```

## Add Marketplace

If you previously installed the old local plugin manually, remove the stale `local`
marketplace entry from Claude Code first. Current Claude Code rejects the legacy
`"source": "local"` marketplace source type.

```bash
claude plugin marketplace add /Users/marcotedone/dev/claude-tools/marco-claude-marketplace
```

## Install Plugin

```bash
claude plugin install claude-tdd-cleancode-plugin@marco-claude-marketplace
```

Reload plugins after installation:

```bash
/reload-plugins
```

The packaged plugin is under `plugins/claude-tdd-cleancode-plugin`.
