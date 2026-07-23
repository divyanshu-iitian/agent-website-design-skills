#!/usr/bin/env python3
"""Validate this repository's Agent Skills catalog using the standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
YAML_STRING_PATTERN = re.compile(r'^\s{2}([a-z_]+):\s+"([^"]*)"\s*$', re.MULTILINE)
EXECUTABLE_SUFFIXES = {".bat", ".cmd", ".js", ".mjs", ".ps1", ".py", ".sh"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(path: Path, errors: list[str]) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(errors, f"{path.relative_to(ROOT)}: missing opening frontmatter delimiter")
        return {}, text

    closing = text.find("\n---\n", 4)
    if closing == -1:
        fail(errors, f"{path.relative_to(ROOT)}: missing closing frontmatter delimiter")
        return {}, text

    fields: dict[str, str] = {}
    for line in text[4:closing].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(errors, f"{path.relative_to(ROOT)}: invalid frontmatter line {line!r}")
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")

    return fields, text[closing + 5 :]


def validate_links(path: Path, text: str, errors: list[str]) -> None:
    for target in LINK_PATTERN.findall(text):
        clean_target = target.split("#", 1)[0]
        if not clean_target or "://" in clean_target or clean_target.startswith("mailto:"):
            continue
        if not (path.parent / clean_target).resolve().exists():
            fail(
                errors,
                f"{path.relative_to(ROOT)}: broken relative link {target!r}",
            )


def validate_openai_yaml(
    skill_dir: Path, skill_name: str, errors: list[str]
) -> dict[str, str]:
    path = skill_dir / "agents" / "openai.yaml"
    if not path.is_file():
        fail(errors, f"{skill_name}: missing agents/openai.yaml")
        return {}

    text = path.read_text(encoding="utf-8")
    fields = dict(YAML_STRING_PATTERN.findall(text))
    required = {"display_name", "short_description", "default_prompt"}
    missing = required - fields.keys()
    if missing:
        fail(errors, f"{skill_name}: openai.yaml missing {sorted(missing)}")
    if not 25 <= len(fields.get("short_description", "")) <= 64:
        fail(errors, f"{skill_name}: short_description must be 25-64 characters")
    if f"${skill_name}" not in fields.get("default_prompt", ""):
        fail(errors, f"{skill_name}: default_prompt must mention ${skill_name}")
    return fields


def validate_skill(skill_dir: Path, errors: list[str]) -> dict[str, str]:
    path = skill_dir / "SKILL.md"
    fields, body = parse_frontmatter(path, errors)
    skill_name = fields.get("name", skill_dir.name)

    if set(fields) != {"name", "description"}:
        fail(errors, f"{skill_dir.name}: frontmatter must contain only name and description")
    if fields.get("name") != skill_dir.name:
        fail(errors, f"{skill_dir.name}: frontmatter name must match its directory")
    if not NAME_PATTERN.fullmatch(skill_dir.name):
        fail(errors, f"{skill_dir.name}: name must use lowercase hyphen-case")
    if len(fields.get("description", "")) < 80:
        fail(errors, f"{skill_dir.name}: description is too short for reliable discovery")
    if len(body.splitlines()) > 500:
        fail(errors, f"{skill_dir.name}: SKILL.md body exceeds 500 lines")
    if (skill_dir / "README.md").exists():
        fail(errors, f"{skill_dir.name}: per-skill README files are not allowed")

    validate_links(path, body, errors)
    interface = validate_openai_yaml(skill_dir, skill_name, errors)

    references = {
        item.relative_to(skill_dir).as_posix()
        for item in (skill_dir / "references").glob("*.md")
    } if (skill_dir / "references").exists() else set()
    linked_references = {
        target.split("#", 1)[0]
        for target in LINK_PATTERN.findall(body)
        if target.startswith("references/")
    }
    for reference in sorted(references - linked_references):
        fail(errors, f"{skill_dir.name}: unlinked reference {reference}")

    for file in skill_dir.rglob("*"):
        if file.is_file() and file.suffix.lower() in EXECUTABLE_SUFFIXES:
            fail(errors, f"{skill_dir.name}: unexpected executable file {file.name}")

    return {**fields, **{f"interface_{key}": value for key, value in interface.items()}}


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(
        path.parent
        for path in ROOT.glob("*/SKILL.md")
        if not path.parent.name.startswith(".")
    )
    if not skill_dirs:
        fail(errors, "No root-level skills found")

    metadata = {
        skill_dir.name: validate_skill(skill_dir, errors)
        for skill_dir in skill_dirs
    }

    for markdown_name in ("README.md", "CONTRIBUTING.md", "AGENTS.md", "SECURITY.md"):
        markdown_path = ROOT / markdown_name
        validate_links(
            markdown_path,
            markdown_path.read_text(encoding="utf-8"),
            errors,
        )

    catalog_path = ROOT / "skills.json"
    try:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(errors, f"skills.json: {error}")
        catalog = {"skills": []}

    entries = {entry.get("name"): entry for entry in catalog.get("skills", [])}
    if set(entries) != set(metadata):
        fail(
            errors,
            f"skills.json names {sorted(entries)} do not match skills {sorted(metadata)}",
        )

    repository = catalog.get("repository", "")
    for name, fields in metadata.items():
        entry = entries.get(name, {})
        expected_path = f"{name}/SKILL.md"
        if entry.get("path") != expected_path:
            fail(errors, f"{name}: catalog path must be {expected_path}")
        if entry.get("description") != fields.get("description"):
            fail(errors, f"{name}: catalog description is out of sync")
        if entry.get("display_name") != fields.get("interface_display_name"):
            fail(errors, f"{name}: catalog display_name is out of sync")
        if entry.get("default_prompt") != fields.get("interface_default_prompt"):
            fail(errors, f"{name}: catalog default_prompt is out of sync")
        expected_raw = (
            f"{repository.replace('github.com', 'raw.githubusercontent.com')}"
            f"/main/{expected_path}"
        )
        if entry.get("raw_url") != expected_raw:
            fail(errors, f"{name}: catalog raw_url is out of sync")

    llms_text = (ROOT / "llms.txt").read_text(encoding="utf-8")
    for name in metadata:
        if f"- {name}:" not in llms_text or f"{name}/SKILL.md" not in llms_text:
            fail(errors, f"{name}: missing or incomplete llms.txt entry")

    evals_path = ROOT / "evals" / "cases.json"
    try:
        evals = json.loads(evals_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(errors, f"evals/cases.json: {error}")
        evals = {"cases": []}

    case_ids: set[str] = set()
    cases_by_skill = {name: 0 for name in metadata}
    for case in evals.get("cases", []):
        case_id = case.get("id", "")
        skill_name = case.get("skill", "")
        if not case_id or case_id in case_ids:
            fail(errors, f"evals/cases.json: missing or duplicate case id {case_id!r}")
        case_ids.add(case_id)
        if skill_name not in metadata:
            fail(errors, f"{case_id}: unknown eval skill {skill_name!r}")
            continue
        cases_by_skill[skill_name] += 1
        if not case.get("prompt"):
            fail(errors, f"{case_id}: missing prompt")
        if not case.get("must_observe") or not case.get("must_not_observe"):
            fail(errors, f"{case_id}: must define positive and negative observations")

    for name, count in cases_by_skill.items():
        if count < 2:
            fail(errors, f"{name}: expected at least two qualitative eval cases")

    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"Validated {len(skill_dirs)} skills, {len(case_ids)} eval cases, "
        "and the repository catalog."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
