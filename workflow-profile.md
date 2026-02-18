# Workflow Profile

Reference document describing hardware, software, and workflow patterns.
Useful context for any project.

## Hardware

- **Keyboard**: Logitech MX Mechanical Mini (standard F-row: media, volume,
  brightness, DND, mic mute, screenshot, emoji, dictation)
- **Mouse**: Logitech MX Master 4 (haptic feedback, Actions Ring)
- **Keypad/Dial**: Logitech MX Creative Console (9-key LCD keypad + dialpad,
  configured via Logi Options+)
- **Display**: Single 49" ultrawide monitor, laptop closed
- **All Logi devices managed through Logi Options+**

## Operating System

- macOS (primary and only development platform)
- Window management: macOS Spaces + Mission Control (no third-party tiling app)
- Launcher: Spotlight (no Raycast/Alfred)

## Terminal and Shell

- **Terminal**: iTerm2
- **Shell**: bash
- **Multiplexer**: tmux (used heavily by the `cos` Chief of Staff system)
- Common terminal patterns: split panes, named tabs, tmux sessions

## Editors

- **Primary**: Sublime Text (not an IDE user, prefers simplicity)
- **Quick edits**: nano in terminal
- **No VS Code, no JetBrains**

## Browser

- Google Chrome (only browser in rotation)
- Heavy Google Workspace user: Gmail, Calendar, Drive, Docs, Sheets, Meet
- Also uses Microsoft Office apps: Word, Excel, PowerPoint

## Communication Tools

Multiple tools depending on customer context (not locked into one ecosystem):

- Zoom
- Microsoft Teams
- Discord
- Google Meet
- Slack
- Apple Messages

## Development Stack

- **Python**: uv, pytest, ruff, FastAPI, full type hints always; execute with
  `uv run`
- **JavaScript**: Node + npm, plain JS (not TypeScript unless project requires)
- **Java**: familiar, not primary
- **Cloud**: AWS first (all services), GCP second, minimal Azure
- **IaC**: Terraform
- **Database**: PostgreSQL by default
- **Containers**: Docker
- **Compute bias**: slight preference for serverless (Lambda, Fargate) but
  right tool for the job
- **Git**: signs all commits (requires interactivity), standard GitHub workflow

## AI Tooling

- **Claude Code**: heavy daily user for both software development and
  non-coding workflows
- **Chief of Staff (`cos`)**: custom bash CLI at `/usr/local/bin/cos` that
  integrates tmux + Claude Code for AI-powered executive assistant workflows
  - `cos session <name>` -- start/resume named AI sessions in tmux
  - `cos inbox "text"` -- quick capture notes, files, clipboard contents
  - `cos inbox --clipboard` -- capture clipboard to inbox
  - `cos task morning-briefing` -- generate AI-synthesized daily briefing
  - `cos ls` -- list active sessions
  - Source repo: `/Users/jud/Projects/ips/chief-of-staff`
  - Everything is git-tracked and auto-pushed

## Work Profile

- 60/40 code/management split in a typical week
- Public sector domain: defense, elections, labor, workforce development,
  unemployment, wage and hour enforcement
- Engineering management experience: teams up to 30, Amazon Bar Raiser
- Remote worker

## Workflow Patterns

- Starts the day with a `cos task morning-briefing` that synthesizes tracking
  files into an emailed briefing
- Uses named cos sessions for focused work blocks (research, writing,
  strategic review)
- Captures thoughts and tasks throughout the day via `cos inbox` (text notes,
  clipboard captures, file drops)
- Switches between coding and meeting contexts frequently
- Multiple macOS Spaces for context separation on the ultrawide
- MX Creative Console keypad pages organized per-app with auto-switching
  profiles in Logi Options+
