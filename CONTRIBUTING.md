# Contributing

Thanks for helping improve Agent Website Design Skills.

## What Belongs Here

Good contributions improve practical website design outcomes for AI coding agents:

- clearer skill instructions
- better trigger descriptions
- sharper design, accessibility, or responsive QA guidance
- useful one-level reference files
- machine-readable catalog improvements
- examples that help agents choose the right skill

## What To Avoid

- large generic design theory dumps
- per-skill README files
- hidden automation, telemetry, or network calls
- duplicate content across `SKILL.md` and `references/`
- huge reference files that make agents waste context
- advice that encourages inaccessible or deceptive UI patterns

## Skill Rules

Each skill must:

1. Live in a lowercase hyphen-case folder.
2. Include a `SKILL.md` file.
3. Use YAML frontmatter with only `name` and `description`.
4. Put trigger phrases in `description`, because agents see that before loading the full file.
5. Keep `SKILL.md` concise and action-oriented.
6. Link references directly from `SKILL.md`.
7. Keep references one level deep.
8. Include `agents/openai.yaml` with display metadata.

## Validation

Run the Codex skill validator when available:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ./landing-page-craft
```

Validate all changed skills before opening a PR.

## Pull Requests

Before submitting:

- Explain what changed and why.
- List which skills were changed.
- Confirm validation passed.
- Keep PRs focused.

## New Skills

Open an issue first for a new skill. Include:

- proposed skill name
- target user request examples
- why it should be separate from existing skills
- likely references or assets
