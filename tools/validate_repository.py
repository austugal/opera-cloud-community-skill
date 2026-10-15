#!/usr/bin/env python3
"""Dependency-free structural and conservative secret checks for this repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".toml", ".json", ".txt"}
IGNORED_DIRECTORIES = {".git", ".venv", "__pycache__"}
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^)\s]+)(?:\s+[^)]*)?\)")
ROUTE_PATTERN = re.compile(r"`((?:references|subskills)/[^`\s]+)`")
SECRET_PATTERNS = (
    ("private-key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("aws-access-key-id", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("github-fine-grained-token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    ("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("google-api-key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("stripe-live-secret", re.compile(r"\bsk_live_[A-Za-z0-9]{20,}\b")),
)


def _without_code(text: str) -> str:
    """Mask fenced and inline code while preserving line numbers."""
    lines = text.splitlines(keepends=True)
    in_fence = False
    fence_marker = ""
    output: list[str] = []
    for line in lines:
        stripped = line.lstrip()
        marker = re.match(r"(`{3,}|~{3,})", stripped)
        if marker:
            current = marker.group(1)
            if not in_fence:
                in_fence = True
                fence_marker = current[0]
            elif current[0] == fence_marker:
                in_fence = False
            output.append("\n" if line.endswith("\n") else "")
            continue
        if in_fence:
            output.append("\n" if line.endswith("\n") else "")
        else:
            output.append(re.sub(r"`+[^`\n]*`+", "", line))
    return "".join(output)


def validate_frontmatter(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []
    if not lines or lines[0].strip() != "---":
        return [f"{path}:1: missing opening YAML frontmatter delimiter"]
    try:
        closing = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return [f"{path}:1: missing closing YAML frontmatter delimiter"]

    fields: dict[str, tuple[int, str]] = {}
    for line_number, line in enumerate(lines[1:closing], start=2):
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if not match:
            continue
        key = match.group(1)
        value = (match.group(2) or "").strip()
        if key in fields:
            errors.append(f"{path}:{line_number}: duplicate frontmatter key '{key}'")
        fields[key] = (line_number, value)

    for required in ("name", "description"):
        if required not in fields:
            errors.append(f"{path}:1: missing frontmatter '{required}'")
            continue
        line_number, value = fields[required]
        if value in {"|", ">", "|-", ">-"}:
            block_end = next(
                (
                    index
                    for index in range(line_number, closing)
                    if re.match(r"^[A-Za-z][A-Za-z0-9_-]*:", lines[index])
                ),
                closing,
            )
            has_content = any(line.strip() for line in lines[line_number:block_end])
        else:
            has_content = bool(value)
        if not has_content:
            errors.append(f"{path}:{line_number}: empty frontmatter '{required}'")
    return errors


def _repository_files(root: Path):
    for path in root.rglob("*"):
        if any(part in IGNORED_DIRECTORIES for part in path.relative_to(root).parts):
            continue
        if path.is_file() and not path.is_symlink():
            yield path


def validate_routes(root: Path) -> list[str]:
    router = root / "SKILL.md"
    errors: list[str] = []
    if not router.is_file():
        return [f"{router}:1: missing root skill router"]
    text = router.read_text(encoding="utf-8")
    routed = set(ROUTE_PATTERN.findall(text))
    for path in root.joinpath("references").glob("*.md"):
        relative = path.relative_to(root).as_posix()
        if relative not in routed:
            errors.append(f"{router}:1: reference file is not routed: {relative}")
    for path in root.joinpath("subskills").glob("*/SKILL.md"):
        relative = path.relative_to(root).as_posix()
        if relative not in routed:
            errors.append(f"{router}:1: specialist skill is not routed: {relative}")
    for route in sorted(routed):
        target = root / Path(route)
        if not target.is_file():
            errors.append(f"{router}:1: routed file does not exist: {route}")
    return errors


def validate_markdown_links(root: Path) -> list[str]:
    errors: list[str] = []
    for path in _repository_files(root):
        if path.suffix.lower() != ".md":
            continue
        text = _without_code(path.read_text(encoding="utf-8"))
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in LINK_PATTERN.finditer(line):
                target = match.group(1)
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                target = target.replace(r"\(", "(").replace(r"\)", ")")
                parts = urlsplit(target)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                decoded_path = unquote(parts.path)
                if decoded_path.startswith("/"):
                    resolved = (root / decoded_path.lstrip("/")).resolve()
                else:
                    resolved = (path.parent / decoded_path).resolve()
                try:
                    resolved.relative_to(root.resolve())
                except ValueError:
                    errors.append(
                        f"{path}:{line_number}: relative link escapes repository: {target}"
                    )
                    continue
                if not resolved.exists():
                    errors.append(f"{path}:{line_number}: broken relative link: {target}")
    return errors


def scan_secrets(root: Path) -> list[str]:
    findings: list[str] = []
    for path in _repository_files(root):
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        content = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(content.splitlines(), start=1):
            for label, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    findings.append(f"{path}:{line_number}: possible {label} pattern")
    return findings


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    skill_files = sorted(
        path
        for path in _repository_files(root)
        if path.name == "SKILL.md"
    )
    if not skill_files:
        errors.append(f"{root}: no SKILL.md files found")
    for path in skill_files:
        errors.extend(validate_frontmatter(path))
    errors.extend(validate_routes(root))
    errors.extend(validate_markdown_links(root))
    errors.extend(scan_secrets(root))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the parent of this script)",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()
    errors = validate(root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"Validation failed: {len(errors)} issue(s).", file=sys.stderr)
        return 1
    print("Repository validation passed (frontmatter, routing, relative links, secret patterns).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
