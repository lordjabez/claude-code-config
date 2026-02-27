---
name: refactor
description: Perform simplification, deduplication, and optimization of a codebase
---

Examine the entire codebase and think deeply about ways that it could be improved,
across dimensions such as simplification, deduplication, performance optimization,
reorganization, or other architectural patterns. By default do not change any
externally-facing interfaces, contracts, or APIs; however, if an opportunity to
improve such an interface exists, inform me so we can discuss if I want to
accept your suggestion.

Make sure at the end of any such refactor that all tests pass (including writing
new tests should the refactor be worthy of it), linting and code quality passes,
and any relevant documentation updates have been made.
