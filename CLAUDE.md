# Global Claude Code Instructions

## Working Style

- Prefer simple implementations over heavy frameworks. Don't assume I want
  something because it's popular. If in doubt, ask me.
- Don't over-engineer. Do exactly what's asked, nothing more.
- Keep explanations minimal for topics I know well (back-end, AWS, Python, JS).
  Give more detail for unfamiliar areas (advanced front-end, etc.).
- Back-end developer first. Comfortable with front-end but it's not my strength.

## Tooling Preferences

- **Python**: uv, pytest, ruff, FastAPI, full type hints always
- **JavaScript**: node + npm, plain JS (not TypeScript unless project requires it)
- **Cloud**: AWS first (all services), GCP second, minimal Azure knowledge
- **IaC**: Terraform
- **Database**: PostgreSQL by default
- **AWS compute**: right tool for the job (Lambda, ECS/Fargate, EC2 — no default)

## Languages I Know

- Strong: Python, JavaScript, Java
- Familiar: C#, C++

## Git

Normally I sign all my git commits, which requires interactivity, so don't try
to commit anything unless guidance in the specific project says to do so.

## Domain Background

Public sector career: defense, elections, labor, workforce development,
unemployment, wage and hour enforcement. Good at translating government policy
into technical solutions. Also experienced in engineering management (teams up
to 30, Amazon Bar Raiser).

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
