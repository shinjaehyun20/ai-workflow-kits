#!/usr/bin/env python3
"""Public safety scanner for ai-workflow-kits.

The scanner is intentionally conservative. It checks tracked text files, optional
Git history, binary-like tracked extensions, and public JSON/YAML files.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

BLOCKED_PATTERNS = [
    ("windows_drive_path", re.compile(r"\b[A-Za-z]:\\[^\s`\"']+")),
    ("windows_user_path", re.compile(r"\\Users\\|C:\\Users", re.IGNORECASE)),
    ("unix_user_path", re.compile(r"/Users/|/home/")),
    ("private_drive_label", re.compile(r"내 드라이브|Downloads|Desktop|Obsidian|AppData", re.IGNORECASE)),
    ("private_person_or_project", re.compile(r"Wylie|HF_|AXinnovation|조가인|신재현|재현|jaehy|shinjaehyun2018")),
    ("workspace_ids", re.compile(r"data_source_id|SLACK_WEBHOOK_URL|NOTION_TOKEN", re.IGNORECASE)),
    ("secret_words", re.compile(r"client_secret|refresh_token|access_token|authorization:|bearer\s+|password\s*[:=]|passwd\s*[:=]|api_key\s*[:=]|private[_-]?key", re.IGNORECASE)),
    ("provider_key_env", re.compile(r"OPENAI_API_KEY|ANTHROPIC_API_KEY|GOOGLE_API_KEY|GEMINI_API_KEY", re.IGNORECASE)),
    ("private_key_block", re.compile(r"BEGIN (RSA|OPENSSH|PRIVATE) KEY")),
    ("github_token", re.compile(r"ghp_[A-Za-z0-9_]+|github_pat_[A-Za-z0-9_]+")),
    ("openai_key", re.compile(r"sk-[A-Za-z0-9_-]{20,}")),
]

ALLOWED_PATTERNS = [
    re.compile(r"https://github\.com/shinjaehyun20/ai-workflow-kits/"),
    re.compile(r"\bshinjaehyun20\b"),
    re.compile(r"\bGEMINI\.md\b"),
    re.compile(r"\bAGENTS\.md\b"),
    re.compile(r"\.github/copilot-instructions\.md"),
]

ALLOWLIST = {
    ".gitignore": [
        re.compile(r"\.env"),
        re.compile(r"secret", re.IGNORECASE),
        re.compile(r"secrets/"),
        re.compile(r"desktop", re.IGNORECASE),
    ],
    "docs/publication-guard.md": [
        re.compile(r"\.env"),
        re.compile(r"secret", re.IGNORECASE),
        re.compile(r"token", re.IGNORECASE),
        re.compile(r"password", re.IGNORECASE),
        re.compile(r"private key", re.IGNORECASE),
        re.compile(r"Notion|Slack|Google Drive"),
        re.compile(r"Downloads|Desktop|Obsidian|AppData"),
        re.compile(r"Windows drive paths"),
        re.compile(r"shinjaehyun20"),
        re.compile(r"GEMINI\.md|AGENTS\.md|\.github/copilot-instructions\.md"),
    ],
    "tools/public-safety-scan.py": [
        re.compile(r"BLOCKED_PATTERNS|ALLOWED_PATTERNS|ALLOWLIST"),
        re.compile(r"secret", re.IGNORECASE),
        re.compile(r"token", re.IGNORECASE),
        re.compile(r"password", re.IGNORECASE),
        re.compile(r"private[_ -]?key", re.IGNORECASE),
        re.compile(r"OPENAI_API_KEY|ANTHROPIC_API_KEY|GOOGLE_API_KEY|GEMINI_API_KEY"),
        re.compile(r"SLACK_WEBHOOK_URL|NOTION_TOKEN"),
        re.compile(r"Downloads|Desktop|Obsidian|AppData"),
        re.compile(r"desktop", re.IGNORECASE),
        re.compile(r"Users", re.IGNORECASE),
        re.compile(r"/home/"),
        re.compile(r"D:\\workspace"),
        re.compile(r"D:\\\\workspace"),
        re.compile(r"windows_drive_path|windows_user_path|unix_user_path"),
        re.compile(r"Wylie|HF_|AXinnovation|조가인|신재현|재현|jaehy|shinjaehyun2018"),
        re.compile(r"workspace"),
        re.compile(r"https://github\.com/shinjaehyun20/ai-workflow-kits/"),
        re.compile(r"GEMINI\.md|AGENTS\.md|\.github/copilot-instructions\.md"),
    ],
    "packages/keepworking/gemini/examples/research-synthesis-case.ko.md": [
        re.compile(r"<username>"),
        re.compile(r"<conv-id>"),
        re.compile(r"\[project_root\]"),
        re.compile(r"\[로컬_프로젝트_경로\]"),
        re.compile(r"D:\\workspace"),
        re.compile(r"C:\\Users\\<username>"),
        re.compile(r"file:///C:/Users/<username>"),
    ],
}

BINARY_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".pdf",
    ".pptx",
    ".xlsx",
    ".docx",
    ".hwp",
    ".hwpx",
    ".zip",
    ".7z",
    ".rar",
    ".mp4",
    ".mov",
    ".webm",
}

REQUIRED_JSON = [
    "core/task-envelope.schema.json",
    "core/audit-event.schema.json",
    "core/companion-state.schema.json",
    "core/runtime-adapters.schema.json",
    "examples/keepworking-basic/task-envelope.example.json",
    "packages/pet-companion/examples/nori-public-case/runtime-adapters.json",
    "packages/pet-companion/examples/nori-public-case/state/codex.example.json",
]

REQUIRED_YAML = [
    "registry.yaml",
    "packages/keepworking/manifest.yaml",
    "packages/pet-companion/manifest.yaml",
    "packages/teamwork-preview/manifest.yaml",
    "packages/agent-team-ops/manifest.yaml",
    "templates/manifest.template.yaml",
]


def run_git(args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=check,
    )


def tracked_files() -> list[str]:
    result = run_git(["ls-files", "-z"])
    return [item for item in result.stdout.split("\0") if item]


def is_allowed(path: str, line: str) -> bool:
    if path == "tools/public-safety-scan.py" and "re.compile(" in line:
        return True
    if any(pattern.search(line) for pattern in ALLOWED_PATTERNS):
        return True
    return any(pattern.search(line) for pattern in ALLOWLIST.get(path, []))


def scan_file(path: str) -> list[str]:
    file_path = ROOT / path
    findings: list[str] = []
    try:
        text = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return findings
    for lineno, line in enumerate(text.splitlines(), start=1):
        if is_allowed(path, line):
            continue
        for name, pattern in BLOCKED_PATTERNS:
            if pattern.search(line):
                findings.append(f"{path}:{lineno}: {name}: {line.strip()}")
    return findings


def scan_current() -> list[str]:
    findings: list[str] = []
    for path in tracked_files():
        findings.extend(scan_file(path))
    return findings


def scan_history() -> list[str]:
    findings: list[str] = []
    revs = run_git(["rev-list", "--all"]).stdout.splitlines()
    for rev in revs:
        files_result = run_git(["ls-tree", "-r", "--name-only", rev], check=False)
        if files_result.returncode != 0:
            findings.append(f"{rev}: git ls-tree failed: {(files_result.stderr or '').strip()}")
            continue
        for path in files_result.stdout.splitlines():
            blob = run_git(["show", f"{rev}:{path}"], check=False)
            if blob.returncode != 0:
                continue
            if "\ufffd" in blob.stdout:
                continue
            for lineno, line in enumerate(blob.stdout.splitlines(), start=1):
                if is_allowed(path, line):
                    continue
                for name, pattern in BLOCKED_PATTERNS:
                    if pattern.search(line):
                        findings.append(f"{rev[:12]}:{path}:{lineno}: {name}: {line.strip()}")
    return findings


def scan_binary_extensions() -> list[str]:
    findings: list[str] = []
    for path in tracked_files():
        suffixes = Path(path).suffixes
        if "".join(suffixes[-2:]).lower() == ".tar.gz" or Path(path).suffix.lower() in BINARY_EXTENSIONS:
            findings.append(f"{path}: tracked binary or large artifact extension")
    return findings


def validate_json_yaml() -> list[str]:
    findings: list[str] = []
    for path in REQUIRED_JSON:
        try:
            json.loads((ROOT / path).read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            findings.append(f"{path}: JSON parse failed: {exc}")

    try:
        import yaml  # type: ignore
    except Exception:
        findings.append("YAML parser unavailable: install PyYAML for YAML validation")
        return findings

    for path in REQUIRED_YAML:
        try:
            yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            findings.append(f"{path}: YAML parse failed: {exc}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan public repo content for private data.")
    parser.add_argument("--history", action="store_true", help="scan all Git history in addition to the current tree")
    args = parser.parse_args()

    findings: list[str] = []
    findings.extend(scan_current())
    findings.extend(scan_binary_extensions())
    findings.extend(validate_json_yaml())
    if args.history:
        findings.extend(scan_history())

    if findings:
        print("Public safety scan failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Public safety scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
