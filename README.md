# Agent Website Design Skills

Open-source **AI agent skills for website design, landing pages, design systems, responsive UI QA, accessibility, and conversion polish**.

These skills help Codex-style coding agents design and ship better web experiences: sharper visual direction, practical design tokens, landing page structure, responsive testing, and accessibility-aware conversion improvements.

[![Skills](https://img.shields.io/badge/skills-5-blue)](#skills)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![AI Ready](https://img.shields.io/badge/AI-ready-black)](llms.txt)

## Why This Exists

AI agents can write frontend code quickly, but websites often fail in the design details: generic heroes, weak hierarchy, broken mobile layouts, vague copy, poor CTAs, inaccessible forms, and inconsistent components.

This repository gives agents reusable website design judgment in a compact skill format.

## Skills

| Skill | Use it for | Entry file |
| --- | --- | --- |
| `web-visual-direction` | Art direction, mood, typography, palette, imagery, first viewport | [`SKILL.md`](web-visual-direction/SKILL.md) |
| `web-design-system` | Tokens, components, states, layout rules, accessibility defaults | [`SKILL.md`](web-design-system/SKILL.md) |
| `landing-page-craft` | Landing pages, product pages, waitlists, pricing pages, launch sites | [`SKILL.md`](landing-page-craft/SKILL.md) |
| `responsive-ui-qa` | Desktop/mobile QA, overflow, overlap, blank canvas, broken responsive states | [`SKILL.md`](responsive-ui-qa/SKILL.md) |
| `conversion-accessibility-polish` | CTAs, forms, trust, copy clarity, semantic HTML, keyboard behavior | [`SKILL.md`](conversion-accessibility-polish/SKILL.md) |

## AI Discovery

Machine-readable entry points:

- [`llms.txt`](llms.txt): concise map for LLMs and AI agents.
- [`AGENTS.md`](AGENTS.md): instructions for coding agents using this repo.
- [`skills.json`](skills.json): structured catalog with names, paths, prompts, and tags.

Raw fetch URLs:

```text
https://raw.githubusercontent.com/divyanshu-iitian/agent-website-design-skills/main/llms.txt
https://raw.githubusercontent.com/divyanshu-iitian/agent-website-design-skills/main/skills.json
https://raw.githubusercontent.com/divyanshu-iitian/agent-website-design-skills/main/AGENTS.md
```

## Install

Copy one or more skill folders into your Codex skills directory:

```bash
cp -R web-visual-direction ~/.codex/skills/
cp -R web-design-system ~/.codex/skills/
cp -R landing-page-craft ~/.codex/skills/
cp -R responsive-ui-qa ~/.codex/skills/
cp -R conversion-accessibility-polish ~/.codex/skills/
```

Or reference a skill folder directly from an agent that supports local skills.

## Example Prompts

```text
Use $web-visual-direction to define a premium but practical visual direction for this SaaS homepage.
Use $web-design-system to create tokens and component rules for this Next.js dashboard.
Use $landing-page-craft to design and implement a landing page for this AI product.
Use $responsive-ui-qa to inspect and fix mobile layout issues.
Use $conversion-accessibility-polish to improve copy, CTAs, forms, trust, and accessibility.
```

## Repository Keywords

AI agent skills, Codex skills, website design, landing page design, frontend design system, responsive UI testing, accessibility audit, conversion rate optimization, UX design, UI design, web design automation, AI web design, design agent, frontend agent.

## License

MIT
