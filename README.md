# Claude Code Settings

A set of Claude Code global configuration files that shape how Claude behaves,
writes, and operates across all projects. Designed to be opinionated but
adaptable: fork it, swap in your own details, and you have a solid baseline.

## What's Included

### CLAUDE.md (Global Instructions)

The main instruction file that Claude loads for every session. It covers:

- **Personal context**: Background, domain expertise, and professional identity
  so Claude can tailor its responses appropriately
- **Working style**: Preferences for simplicity over frameworks, minimal
  explanations for known topics, and no over-engineering
- **Engineering discipline**: Rules for capturing lessons in memory, verifying
  work like a staff engineer would, and fixing bugs without hand-holding
- **Tooling preferences**: Specific tools and patterns for Python (uv, pytest,
  ruff), JavaScript (node, npm), cloud providers (AWS first, GCP second),
  IaC (Terraform), databases (PostgreSQL), and git (rebase, signed commits)
- **Markdown formatting rules**: Enforced conventions for lists, code blocks,
  headers, and spacing to keep generated Markdown consistent
- **Security policy**: Hard rules against leaking sensitive information into
  repos or remote servers, with instructions to refuse even if asked
- **Anti-patterns**: A list of "Claude-isms" to avoid in writing (hollow
  affirmations, vague praise words, unnecessary recaps, unsolicited questions)
- **Temporary file hygiene**: Clean up after yourself, write scripts to files
  instead of executing inline

### settings.json (Settings and Hooks)

Runtime configuration including:

- **Hooks**:
  - `PostToolUse` on `Edit|MultiEdit|Write`: Runs `markdownlint-cli` against
    all Markdown files after every file edit, enforcing the formatting rules
    from CLAUDE.md
  - `UserPromptSubmit`, `Stop`, `Notification`, `SessionEnd`, `PostToolUse`:
    Notifies `claude-status` on every significant event for external monitoring
- **Permissions**: Pre-approved commands for common tools (git, npm, uv,
  python, docker, terraform, gh, and others) so Claude doesn't prompt
  repeatedly for routine operations
- **Spinner verbs**: 60 custom loading messages drawn from Lord of the Rings,
  Star Trek, Star Wars, and Marvel (replaces the defaults entirely)
- **Status line**: Points to `status.py` for a custom terminal status bar
- **MCP servers**: Connections to Playwright, AWS docs, AWS core, GitHub,
  Terraform, Google Cloud, Google developer docs, Microsoft Learn, and Azure
- **Environment**: Enables experimental agent teams

### status.py (Custom Status Line)

A Python script that reads Claude's session JSON from stdin and renders a
single-line status bar with:

- Model name and a color-coded context window usage bar (green/yellow/red)
- Running cost in USD and elapsed session time
- Current directory as a clickable hyperlink to the GitHub remote (when available)
- Current git branch

### writing-guide.md (Ghostwriting Reference)

A detailed style guide derived from analysis of 345 pieces of writing, used
when Claude needs to write prose, emails, articles, or social posts in the
user's voice. Covers voice, tone, sentence-level style, vocabulary, opening
and closing techniques, cultural references, and anti-patterns.

### workflow-profile.md (Workspace Context)

Reference document describing hardware (Logitech peripherals, ultrawide
monitor), software (iTerm2, bash, tmux, Sublime Text, Chrome), development
stack, AI tooling (including a custom Chief of Staff CLI), and daily workflow
patterns. Gives Claude useful context about the working environment.

### .claude.json (MCP Server Definitions)

Configures ten MCP servers:

- **Playwright**: Browser automation and testing
- **Simple Timeserver**: Time and date utilities
- **AWS Docs**: AWS documentation search and retrieval
- **AWS Core**: AWS API calls and command suggestions
- **GitHub**: GitHub API via Copilot MCP endpoint
- **Terraform**: HashiCorp Terraform MCP server (runs in Docker)
- **Google Cloud**: gcloud CLI integration
- **Google Dev Knowledge**: Google developer documentation
- **Microsoft Learn**: Microsoft/Azure documentation
- **Azure**: Azure CLI and service management

## Pre-requisites

- Python 3
- npx (for markdownlint-cli and some MCP servers)
- Docker (for the Terraform MCP server)
- uvx (for AWS MCP servers)

## Installation

Symlink the configuration files into the global location:

```bash
ln -s -t "$HOME/.claude" "$PWD/CLAUDE.md" "$PWD/settings.json" "$PWD/status.py" "$PWD/.claude.json"
```

The writing guide and workflow profile are referenced by relative path from
CLAUDE.md, so the symlink is sufficient to make them accessible.

To use this config as your own, you'll need to update:

- The personal sections of `CLAUDE.md` (overview, domain background, tooling preferences)
- `writing-guide.md` and `workflow-profile.md` with your own details
- The absolute path in `settings.json` for the status line command
- API tokens and profile names in `.claude.json` (AWS profile, GitHub token, Google API key)

## License

MIT

## References

- [Claude Code settings](https://code.claude.com/docs/en/settings)
- [Customize your status line](https://code.claude.com/docs/en/statusline)
- [Claude Status Tool](https://github.com/lordjabez/claude-status-tool)
