# Security Policy

## Scope

The installable skill folders contain only instructions, display metadata, and references. They do not include executable code, credentials, package dependencies, telemetry, hooks, or runtime services.

The repository includes one dependency-free Python validator under `scripts/` for contributor and CI use. It reads local repository files and does not modify files or access the network. It is not bundled inside any skill.

## Reporting A Concern

Please open a GitHub issue if you find:

- unsafe or destructive agent instructions
- guidance that could leak secrets or private data
- accessibility advice that creates user harm
- hidden executable behavior
- misleading installation or usage instructions

For sensitive reports, contact the repository owner through GitHub before posting details publicly.

## Safety Expectations

Contributions should not add:

- credential collection
- telemetry
- hidden network calls
- shell commands that modify unrelated files
- instructions that bypass user consent
- dark patterns or deceptive conversion tactics

## Review Notes

Users should inspect any downloaded skill before installing it into an agent environment. Agent Skills can influence coding-agent behavior, so keep installed skills trusted, minimal, and relevant.
