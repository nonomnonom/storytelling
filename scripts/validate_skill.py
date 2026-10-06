"""Validate skill metadata and local reference navigation without network access."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml


ALLOWED_FRONTMATTER = {
    "name", "description", "license", "allowed-tools", "metadata"
}
MARKDOWN_LINK = re.compile(r"\]\(([^)]+)\)")


def validate_skill(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    entrypoint = root / "SKILL.md"
    if not entrypoint.is_file():
        return ["SKILL.md is missing."]

    documents: dict[Path, str] = {}
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", ".venv", ".preview"} for part in path.relative_to(root).parts):
            continue
        if not path.resolve().is_relative_to(root):
            errors.append(f"Markdown file leaves the package: {path.relative_to(root)}")
            continue
        try:
            documents[path.resolve()] = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read {path.relative_to(root)} as UTF-8: {exc}")

    content = documents.get(entrypoint, "")
    frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
    if frontmatter is None:
        errors.append("SKILL.md must begin with YAML frontmatter.")
    else:
        try:
            metadata = yaml.safe_load(frontmatter.group(1))
        except yaml.YAMLError as exc:
            errors.append(f"Invalid skill YAML: {exc}")
        else:
            if not isinstance(metadata, dict):
                errors.append("Skill frontmatter must be a mapping.")
            else:
                unknown = set(metadata) - ALLOWED_FRONTMATTER
                if unknown:
                    errors.append(f"Unsupported frontmatter fields: {sorted(map(str, unknown))}")
                name = metadata.get("name")
                if not isinstance(name, str) or not re.fullmatch(
                    r"[a-z0-9]+(?:-[a-z0-9]+)*", name
                ) or len(name) > 64:
                    errors.append("Skill name must use lowercase words or digits separated by hyphens, up to 64 characters.")
                elif name != root.name:
                    errors.append("Skill name must match its folder name.")
                description = metadata.get("description")
                if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                    errors.append("Skill description must contain 1 to 1024 characters.")
                elif description.startswith("[TODO:") or "<" in description or ">" in description:
                    errors.append("Skill description contains scaffold text or unsupported angle brackets.")
                if re.search(r"(?m)^\[TODO:[^\n]*\][ \t]*$", content[frontmatter.end():]):
                    errors.append("SKILL.md contains an unfinished scaffold placeholder.")

    ui_path = root / "agents" / "openai.yaml"
    if ui_path.exists():
        try:
            ui = yaml.safe_load(ui_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, yaml.YAMLError) as exc:
            errors.append(f"Cannot read agent metadata: {exc}")
        else:
            interface = ui.get("interface") if isinstance(ui, dict) else None
            if not isinstance(interface, dict):
                errors.append("Agent metadata must have an interface mapping.")
            else:
                display_name = interface.get("display_name")
                if not isinstance(display_name, str) or not display_name.strip():
                    errors.append("Agent display_name must be a nonempty string.")
                short = interface.get("short_description")
                if not isinstance(short, str) or not 25 <= len(short) <= 64:
                    errors.append("Agent short_description must have 25 to 64 characters.")
                prompt = interface.get("default_prompt")
                if not isinstance(prompt, str) or f"${root.name}" not in prompt:
                    errors.append("Agent default_prompt must mention the skill by name.")

    graph: dict[Path, set[Path]] = {}
    for path, text in documents.items():
        graph[path] = set()
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            parsed = urlsplit(target)
            if parsed.scheme in {"https", "http", "mailto"}:
                if re.search(r"\s", target):
                    errors.append(f"Malformed external link in {path.relative_to(root)}: {target}")
                continue
            if not parsed.path and parsed.fragment:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if parsed.scheme or not destination.is_relative_to(root):
                errors.append(f"Local link leaves the package in {path.relative_to(root)}: {target}")
            elif not destination.is_file():
                errors.append(f"Missing local link target in {path.relative_to(root)}: {target}")
            elif destination in documents:
                graph[path].add(destination)

    reachable: set[Path] = set()
    pending = [entrypoint]
    while pending:
        current = pending.pop()
        if current not in reachable:
            reachable.add(current)
            pending.extend(graph.get(current, set()) - reachable)
    for reference in sorted((root / "references").rglob("*.md")):
        if reference.resolve() not in reachable:
            errors.append(f"Reference is not reachable from SKILL.md: {reference.relative_to(root)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_skill(args.path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: skill frontmatter, agent metadata, local links, and reference navigation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
