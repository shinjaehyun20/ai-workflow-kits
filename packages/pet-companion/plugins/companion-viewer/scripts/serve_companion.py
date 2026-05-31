#!/usr/bin/env python3
"""Serve the public-safe pet companion viewer and repository assets."""

from __future__ import annotations

import argparse
import contextlib
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def build_handler(repo_root: Path, viewer_root: Path) -> type[SimpleHTTPRequestHandler]:
    class Handler(SimpleHTTPRequestHandler):
        def translate_path(self, path: str) -> str:
            clean = path.split("?", 1)[0].split("#", 1)[0]
            if clean.startswith("/viewer/"):
                relative = clean[len("/viewer/") :]
                target = viewer_root / relative
            elif clean.startswith("/repo/"):
                relative = clean[len("/repo/") :]
                target = repo_root / relative
            elif clean == "/" or not clean:
                target = viewer_root / "index.html"
            else:
                target = viewer_root / clean.lstrip("/")
            return os.fspath(target.resolve())

        def end_headers(self) -> None:
            self.send_header("Cache-Control", "no-store")
            super().end_headers()

    return Handler


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Serve the pet companion viewer.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8877, type=int)
    parser.add_argument(
      "--repo-root",
      default=str(Path(__file__).resolve().parents[5]),
      help="Repository root to expose under /repo/",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    viewer_root = Path(__file__).resolve().parents[1]
    handler = build_handler(repo_root, viewer_root)
    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"Serving viewer from {viewer_root}")
    print(f"Serving repo from {repo_root}")
    print(f"Open http://{args.host}:{args.port}/viewer/index.html")
    with contextlib.suppress(KeyboardInterrupt):
        server.serve_forever()
    server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
