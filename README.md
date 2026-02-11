# Claude Code Settings

A set of Claude configuration files suitable for global use. They do the following:

- Say a bit about who I am and what I'm about
- Establish rules for consistent and proper Markdown formatting
- Set up a post tool hook to lint Markdown to ensure those rules are followed
- Configure a status line full of useful information
- Provide set of fun spinner verbs based on LOTR, Star Trek, Star Wars, and Marvel

## Pre-requisites

- npx
- Python

## Installation

Symlink the configuration files into the global location with the following:

```bash
ln -s -t "$HOME/.claude" "$PWD/CLAUDE.md" "$PWD/settings.json" "$PWD/status.py"
```

If you want to use my config, you'll need to update the personal introduction
section of `CLAUDE.md` and the paths in `settings.json`.

## References

- [Claude Code settings](https://code.claude.com/docs/en/settings)
- [Customize your status line](https://code.claude.com/docs/en/statusline)
