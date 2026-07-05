# Agent Website Design Skills

Professional **AI agent skills for website design**: visual direction, design systems, landing pages, responsive UI QA, accessibility, and conversion polish.

These skills give Codex-style coding agents practical design judgment for shipping web experiences that feel specific, usable, responsive, and credible.

[![Skills](https://img.shields.io/badge/skills-5-2563eb)](#skill-catalog)
[![AI Ready](https://img.shields.io/badge/AI-ready-111827)](llms.txt)
[![License: MIT](https://img.shields.io/badge/license-MIT-16a34a.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/divyanshu-iitian/agent-website-design-skills?style=social)](https://github.com/divyanshu-iitian/agent-website-design-skills/stargazers)

## What This Solves

AI agents can generate frontend code quickly, but the results often miss the work that makes websites feel professional:

- generic hero sections with weak hierarchy
- inconsistent spacing, color, type, and component states
- mobile overflow, clipped text, and broken responsive layouts
- vague copy, unclear CTAs, and low-trust conversion flows
- accessibility gaps in forms, navigation, focus states, and semantics

This repo packages reusable website design workflows as compact, agent-readable skills.

## Who It Is For

- Developers using Codex, Claude Code, Cursor, GitHub Copilot, Gemini CLI, OpenCode, or other skill-compatible agents.
- Builders who want AI-generated websites to look less generic and behave better across devices.
- Teams creating repeatable frontend design standards for AI-assisted development.

## Skill Catalog

| Skill | Best for | Default prompt |
| --- | --- | --- |
| [`web-visual-direction`](web-visual-direction/SKILL.md) | Art direction, typography, palette, imagery, first viewport | `Use $web-visual-direction to define the visual direction for this website.` |
| [`web-design-system`](web-design-system/SKILL.md) | Tokens, components, interaction states, layout rules | `Use $web-design-system to create a practical design system for this site.` |
| [`landing-page-craft`](landing-page-craft/SKILL.md) | Homepages, product pages, waitlists, pricing pages, launch sites | `Use $landing-page-craft to design and implement a strong landing page.` |
| [`responsive-ui-qa`](responsive-ui-qa/SKILL.md) | Mobile/desktop QA, overflow, overlap, broken responsive states | `Use $responsive-ui-qa to inspect and fix responsive UI issues.` |
| [`conversion-accessibility-polish`](conversion-accessibility-polish/SKILL.md) | CTAs, forms, copy clarity, trust, keyboard behavior, semantic HTML | `Use $conversion-accessibility-polish to improve this page's conversion and accessibility.` |

## Install

If your agent supports the Agent Skills CLI:

```bash
npx skills add divyanshu-iitian/agent-website-design-skills
```

Install one skill:

```bash
npx skills add divyanshu-iitian/agent-website-design-skills --skill landing-page-craft
```

Manual install:

```bash
cp -R web-visual-direction ~/.codex/skills/
cp -R web-design-system ~/.codex/skills/
cp -R landing-page-craft ~/.codex/skills/
cp -R responsive-ui-qa ~/.codex/skills/
cp -R conversion-accessibility-polish ~/.codex/skills/
```

For Windows PowerShell:

```powershell
Copy-Item -Recurse .\landing-page-craft "$env:USERPROFILE\.codex\skills\"
```

## Quick Start

Ask your coding agent:

```text
Use $web-visual-direction to create a visual direction for a premium AI SaaS homepage.
Use $landing-page-craft to implement the homepage.
Use $responsive-ui-qa to verify mobile and desktop layouts.
Use $conversion-accessibility-polish to improve CTAs, forms, trust, and accessibility.
```

For an existing app:

```text
Use $web-design-system to extract a practical design system from this codebase, then apply it to the dashboard.
```

## AI Discovery

Machine-readable entry points:

- [`llms.txt`](llms.txt): concise map for LLMs and AI agents.
- [`skills.json`](skills.json): structured catalog with skill names, paths, raw URLs, prompts, and tags.
- [`AGENTS.md`](AGENTS.md): instructions for coding agents working in this repository.

Raw fetch URLs:

```text
https://raw.githubusercontent.com/divyanshu-iitian/agent-website-design-skills/main/llms.txt
https://raw.githubusercontent.com/divyanshu-iitian/agent-website-design-skills/main/skills.json
https://raw.githubusercontent.com/divyanshu-iitian/agent-website-design-skills/main/AGENTS.md
```

Raw skill URLs:

```text
https://raw.githubusercontent.com/divyanshu-iitian/agent-website-design-skills/main/web-visual-direction/SKILL.md
https://raw.githubusercontent.com/divyanshu-iitian/agent-website-design-skills/main/web-design-system/SKILL.md
https://raw.githubusercontent.com/divyanshu-iitian/agent-website-design-skills/main/landing-page-craft/SKILL.md
https://raw.githubusercontent.com/divyanshu-iitian/agent-website-design-skills/main/responsive-ui-qa/SKILL.md
https://raw.githubusercontent.com/divyanshu-iitian/agent-website-design-skills/main/conversion-accessibility-polish/SKILL.md
```

## Repository Structure

```text
agent-website-design-skills/
  web-visual-direction/
    SKILL.md
    agents/openai.yaml
    references/
  web-design-system/
  landing-page-craft/
  responsive-ui-qa/
  conversion-accessibility-polish/
  AGENTS.md
  llms.txt
  skills.json
```

Each skill is intentionally small and uses progressive disclosure: agents load the skill metadata first, then `SKILL.md`, then references only when needed.

## Quality Principles

- Specific over generic: every page should communicate a real product, person, place, or outcome.
- Usable over decorative: layout, hierarchy, responsiveness, and accessibility come first.
- Compact over bloated: skill files stay short enough for agent context windows.
- Verifiable over vibes: responsive QA and browser screenshots are part of the workflow.
- Safe to inspect: no hidden scripts, no network calls, no destructive actions.

## Keywords

AI agent skills, Agent Skills, Codex skills, Claude Code skills, Cursor skills, GitHub Copilot skills, Gemini CLI skills, website design, web design, AI web design, landing page design, design system, design tokens, frontend design, responsive design, UI QA, accessibility audit, conversion rate optimization, UX writing, AI frontend agent.

## Contributing

Contributions are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for skill quality rules and PR expectations.

## Security

These skills are instruction-only and contain no executable scripts. If you find unsafe guidance or a security concern, see [`SECURITY.md`](SECURITY.md).

## License

MIT. See [`LICENSE`](LICENSE).
