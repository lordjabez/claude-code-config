---
paths: "**/*.md"
---

# Markdown Formatting

When generating or editing markdown files, always follow these rules for proper rendering:

- Use `-` for unordered lists, `1.` for ordered lists (not `*` or other markers)
- Include a blank line before bulleted (`-`) or numbered (`1.`) lists
- Include a blank line before fenced code blocks (```)
- Include a blank line before headers (`#`, `##`, etc.) except at file start
- Include a blank line between headers and content
- Do not use emphasis (`**`) as a header
- Always specify a language in a fenced code block
- Include a blank line between lines that should be rendered on separate lines
- Escape dollar signs in Markdown with a slash (`\$`) to avoid accidentaly rendering confusion with mathematical expressions, unless the dollar signs are in fenced code blocks
