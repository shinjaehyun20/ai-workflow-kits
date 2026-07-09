#!/usr/bin/env python3
"""Validate Markdown links and repo-relative context path references.

The check is intentionally read-only. It reports stale real references while
allowing explicit template placeholders used by package-authoring docs.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")
# Optional explicit context-path markers. Ordinary inline-code examples are
# intentionally not treated as blocking path references.
EXPLICIT_PATH_RE = re.compile(
    r"(?:context_path|context-file|context_file|source_truth|target_truth)\s*[:=]\s*`?([^`\s]+)`?",
    re.IGNORECASE,
)

PLACEHOLDER_MARKERS = ("<", ">", "*", "YYYY", "<package-id>", "<skill-id>", "<name>")
IGNORE_PARTS = {".git", "__pycache__", "node_modules", ".venv", "venv", "dist", "build"}


def git_files() -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-z"],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        return [p for p in ROOT.rglob("*.md") if not any(part in IGNORE_PARTS for part in p.parts)]
    return [ROOT / item for item in result.stdout.split("\0") if item]


def is_placeholder(ref: str) -> bool:
    return any(marker in ref for marker in PLACEHOLDER_MARKERS)


def exists_from(source: Path, ref: str) -> bool:
    clean = ref.split("#", 1)[0].strip().strip("<>")
    if not clean or is_placeholder(clean):
        return True
    candidates = [ROOT / clean, source.parent / clean]
    return any(candidate.exists() for candidate in candidates)


def check_file(path: Path) -> list[dict[str, object]]:
    if path.suffix.lower() != ".md":
        return []
    text = path.read_text(encoding="utf-8", errors="ignore")
    findings: list[dict[str, object]] = []
    in_fence = False
    for lineno, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in MARKDOWN_LINK_RE.finditer(line):
            ref = match.group(1).strip()
            if not exists_from(path, ref):
                findings.append({"file": str(path.relative_to(ROOT)), "line": lineno, "kind": "markdown_link", "ref": ref})
        for match in EXPLICIT_PATH_RE.finditer(line):
            ref = match.group(1).strip().rstrip(".,;)")
            if not exists_from(path, ref):
                findings.append({"file": str(path.relative_to(ROOT)), "line": lineno, "kind": "explicit_context_path", "ref": ref})
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate context links and path references.")
    parser.add_argument("--json", action="store_true", help="emit JSON findings")
    args = parser.parse_args()

    findings: list[dict[str, object]] = []
    for path in git_files():
        if path.exists() and path.suffix.lower() == ".md":
            findings.extend(check_file(path))

    if args.json:
        print(json.dumps({"ok": not findings, "finding_count": len(findings), "findings": findings}, ensure_ascii=False, indent=2))
    elif findings:
        print("Context path validation failed:")
        for item in findings:
            print(f"- {item['file']}:{item['line']}: {item['kind']}: {item['ref']}")
    else:
        print("Context path validation passed.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
