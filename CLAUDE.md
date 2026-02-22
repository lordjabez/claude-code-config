# Global Claude Code Instructions

## Personal Overview

Technologist building both systems and organizations that are secure, scalable, cost-effective, and most of all, promote human flourishing. Well-versed in programming languages, cloud technologies, people management, and business development, especially in the public sector. Experienced with the entire engineering lifecycle, from ideation and sales, to requirements development, to architecture and implementation, to maintenance and support. Also an avid runner, amateur musician, and owner of every iteration of the Raspberry Pi.

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
software used, and general way of working can be found in the [workflow profile](workflow-profile.md).

## Domain Background

Public sector career: defense, elections, labor, workforce development,
unemployment, wage and hour enforcement. Good at translating government policy
into technical solutions. Also experienced in engineering management (teams up
to 30, manager of managers, Amazon Bar Raiser). Deep election security background
(chaired DHS Election Infrastructure Cybersecurity Working Group, participated
in NIST standards groups). Hands-on Amazon Connect, GenAI/ML (vector stores,
LLM-based evaluation, NL querying), and IoT experience. Comfortable with
microservices, strangler migrations, event-driven architectures, and distributed
systems design.

## Languages I Know

- Strong: Python, JavaScript, Java, Bash
- Familiar: C#, C++, LaTeX

## Tooling Preferences

- **Python**: uv, pytest, ruff, FastAPI, full type hints always; always execute with `uv run` instead of using scripts in .venv
- **JavaScript**: node + npm, plain JS/TypeScript; avoid front-end frameworks as a default, only use if complexity demands it
- **Cloud**: AWS first (all services, multiple specialty certs including security, networking, data, ML), GCP second (Professional Cloud Architect level), minimal Azure knowledge
- **IaC**: Terraform prefered, but consider CDK for AWS-specific work
- **Containers**: Docker, Kubernetes, Helm, Serverless on managed cloud services like AWS Fargate or Google Cloud Run
- **Database/Data**: PostgreSQL by default; experienced with MySQL, MongoDB, Cassandra, Elasticsearch, BigQuery, Pandas, NumPy
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

## Temporary Scripts

When writing small scripts to explore a repository or do investigation or research
or other processing, favor writing them to a temporary file and then running that
as a script file vs executing the command directly. Also favor doing this in Python
vs Bash, but if you have to use the latter, use a consistent name every name
so that you don't have to keep asking permission for every action.

## Anti-Patterns To Avoid

Try hard to avoid "Claude-isms" in all writing, such as

- M dashes in situations where other punctuation will work
- Clusters of 3 examples (vary the number and way they're punctuated)
- Phrases like "core insight", "key principle", "sharp observation"
- Describing the importance of something before stating what it is (e.g. "This matters...")
- Excessive throat-clearing or making statements complex when simpler will do
- Starting with "Let's" or "Let me" (e.g. "Let's dive in", "Let me break this down")
- Hollow affirmations like "Great question!" before answering
- "It's worth noting that..." — just state the thing
- Vague praise words: "robust", "elegant", "comprehensive", "streamlined"
- "Here's the thing:" as a conversational stall before making a point
- Starting paragraphs or sections with "So,"
- Recapping what the user just said before answering (e.g. "You're asking about X")
- Ending with an unsolicited question back ("Would you like me to...", "Shall I also...")
- Calling things "straightforward" as filler
