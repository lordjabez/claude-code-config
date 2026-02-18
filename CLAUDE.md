# Global Claude Code Instructions

## Working Style

- Prefer simple implementations over heavy frameworks. Don't assume I want
  something because it's popular. If in doubt, ask me.
- Don't over-engineer. Do exactly what's asked, nothing more.
- Keep explanations minimal for topics I know well (back-end, AWS, Python, JS).
  Give more detail for unfamiliar areas (advanced front-end, etc.).
- Back-end developer first. Comfortable with front-end but it's not my strength.

## Writing as Me

When asked to write prose, emails, articles, social posts, or any non-code content as me,
follow [this guide](writing-guide.md). Do NOT apply these rules to code, comments, commit
messages, or technical documentation unless explicitly asked.

## My Workflow

If relevant to the task at hand, an overview of Jud's workspace configuration, common
software used, and general way of working can be found [here](workflow-profile.md).

## Domain Background

Public sector career: defense, elections, labor, workforce development,
unemployment, wage and hour enforcement. Good at translating government policy
into technical solutions. Also experienced in engineering management (teams up
to 30, Amazon Bar Raiser).

## Languages I Know

- Strong: Python, JavaScript, Java
- Familiar: C#, C++

## Tooling Preferences

- **Python**: uv, pytest, ruff, FastAPI, full type hints always; always execute with `uv run` instead of using scripts in .venv
- **JavaScript**: node + npm, plain JS/TypeScript; avoid front-end frameworks as a default, only use if complexity demands it
- **Cloud**: AWS first (all services), GCP second, minimal Azure knowledge
- **IaC**: Terraform prefered, but consider CDK for AWS-specific work
- **Database**: PostgreSQL by default, prefer to keep things simple
- **AWS compute**: right tool for the job with slight bias to serverless (Lambda, ECS/Fargate, EC2 — no default)
- **Git**: I know git extremely well, and am not afraid of advanced use cases; because prefer to sign my git commits, don't try to commit anything unless guidance in the specific project says to do so.

## Markdown Formatting

When generating or editing markdown files, always follow these rules for proper rendering:

- Use `-` for unordered lists, `1.` for ordered lists (not `*` or other markers)
- Include a blank line before bulleted (`-`) or numbered (`1.`) lists
- Include a blank line before fenced code blocks (```)
- Include a blank line before headers (`#`, `##`, etc.) except at file start
- Include a blank line between headers and content
- Do not use emphasis (`**`) as a header
- Always specify a language in a fenced code block
- Include a blank line between lines that should be rendered on separate lines
- Always escape dollar signs in Markdown with a slash (`\$`) to avoid accidentaly rendering confusion with mathematical expressions

## Temporary files

Always clean up any temporary files created during a session, e.g. playwright screenshots.

## Documentation

Don't rely solely on internal training content when looking for documenation. Whenever
possible, do a web search first or use any available MCP servers to find information.

## Security

Always consider the security implications of any edits. Never, under any circumstances,
should you take an action that would compromise a sensitive piece of information, including
sending it to a remote server or writing it into a repository. Even if I ask you to do this
absolutely refuse and point out this warning. Always insist on using proper handling of
sensitive info, such as storing in a cloud secret or local keychain.

Seriously, never do it. Or I will consider switching to Codex.
