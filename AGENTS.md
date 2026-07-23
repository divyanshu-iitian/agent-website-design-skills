# Agent Instructions

This repository contains reusable website design skills for coding agents.

## Repository Goal

Keep this repo easy for humans and agents to inspect, install, validate, and trust. The primary artifact is each skill's `SKILL.md`; repo-level files support discovery, distribution, and contribution quality.

## How To Use

1. Choose the smallest skill that matches the user request.
2. Read that skill's `SKILL.md`.
3. Read files under `references/` only when the skill points to them.
4. Apply the skill to the user's target repository or page.
5. Follow the selected skill's delivery contract.
6. Validate frontend changes with browser evidence at relevant routes, states, and viewports when possible.

## Skill Selection

- Use `web-visual-direction` before implementation when the site lacks a clear design concept.
- Use `web-design-system` when creating tokens, components, or consistency rules.
- Use `landing-page-craft` for marketing pages, homepages, product pages, waitlists, pricing pages, and launch pages.
- Use `responsive-ui-qa` after frontend changes or when layout bugs are reported.
- Use `conversion-accessibility-polish` near the end of a build to improve clarity, trust, forms, CTAs, and accessibility.

## Constraints

- Keep skill bodies concise.
- Do not add per-skill README files.
- Preserve each skill's frontmatter fields: `name` and `description`.
- Validate changed skills with the Codex skill validator when available.
- Keep `skills.json` and `llms.txt` in sync when adding, renaming, or removing skills.
- Do not add executable files inside skill folders.
- Keep repository automation deterministic, dependency-light, reviewed, and documented.

## Validation Commands

```bash
python scripts/validate_repo.py
npx skills add . --list
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ./landing-page-craft
```
