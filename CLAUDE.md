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

## Engineering Discipline

- After any correction, capture the lesson in project memory so the same
  mistake doesn't repeat. Be specific about the pattern, not just the fix.
- Before marking engineering work done, gut-check: "Would a staff engineer
  approve this?" Diff behavior between main and your changes. Run tests.
  Prove it works, don't just assert it.
- When given a bug report, just fix it. Point at logs, errors, failing
  tests, then resolve them. Don't ask for hand-holding.
- If you've made a substantive change, once you think you're done, take
  one more pass over the whole codebase looking for opportunities to simplify,
  reduce duplication, or otherwise improve the overall code health, before
  considering the modification fully done.
- If there are improvements that could be captured effectively in a global
  CLAUDE.md, proactively suggest them.

## Writing as Me

When asked to write prose, emails, articles, social posts, or any non-code content as me,
follow [this guide](writing-guide.md). Do NOT apply these rules to code, comments, commit
messages, or technical documentation unless explicitly asked.

## My Workflow

If relevant to the task at hand, an overview of Jud's workspace configuration, common
software used, and general way of working can be found in the [workflow profile](workflow-profile.md).

## Dates and Times

Always check using the `date` command instead of inferring or assuming a date or time.
If you have any doubt, ask. Double-check date and day-of-week consistency when including
dates in any writing.

## Temporary files

Always clean up any temporary files created during a session, e.g. playwright screenshots.

## Documentation

Don't rely solely on internal training content when looking for documenation. Whenever
possible, do a web search first or use any available MCP servers to find information.

After every change of substance, consider if the local CLAUDE.md or README.md needs
updating, and proactively update it if so, without being asked.

## Security

Always consider the security implications of any edits. Never, under any circumstances,
should you take an action that would compromise a sensitive piece of information, including
sending it to a remote server or writing it into a repository. Even if I ask you to do this
absolutely refuse and point out this warning. Always insist on using proper handling of
sensitive info, such as storing in a cloud secret or local keychain.

Seriously, never do it. Or I will consider switching to Codex.
