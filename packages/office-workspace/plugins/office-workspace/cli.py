"""Thin CLI over the workspace engine.

Each subcommand opens what it needs, performs one operation, and saves. For
multi-step sessions an agent should import :class:`workspace.Workspace`
directly and keep documents open across calls.

  python cli.py inventory <file.pptx>
  python cli.py create <new.pptx> --from <donor.pptx>
  python cli.py copy <src.pptx> <dst.pptx>
  python cli.py import-layout <target.pptx> --from <donor.pptx> --name "Title and Content"
  python cli.py replace <file.pptx> --map 로그인=회원가입 --map v1=v2
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from workspace import Workspace  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="office-workspace")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("inventory", help="list masters, layouts, slides")
    sp.add_argument("file")

    sp = sub.add_parser("create", help="new deck from a donor (reuses masters/layouts)")
    sp.add_argument("file")
    sp.add_argument("--from", dest="donor", required=True)

    sp = sub.add_parser("copy", help="copy a deck then it can be edited")
    sp.add_argument("src")
    sp.add_argument("dst")

    sp = sub.add_parser("import-layout", help="reuse one layout from another deck")
    sp.add_argument("file")
    sp.add_argument("--from", dest="donor", required=True)
    sp.add_argument("--name", required=True)

    sp = sub.add_parser("replace", help="replace text across slides")
    sp.add_argument("file")
    sp.add_argument("--map", action="append", default=[], metavar="OLD=NEW")

    args = p.parse_args(argv)
    ws = Workspace()

    if args.cmd == "inventory":
        print(json.dumps(ws.open(args.file).inventory(), ensure_ascii=False, indent=2))
    elif args.cmd == "create":
        doc = ws.create(args.file, clone_from=ws.open(args.donor, alias="donor").path)
        doc.save()
        print(f"created {args.file} from {args.donor}: {len(doc.inventory()['layouts'])} layouts, 0 slides")
    elif args.cmd == "copy":
        ws.copy(args.src, args.dst)
        print(f"copied {args.src} -> {args.dst}")
    elif args.cmd == "import-layout":
        donor = ws.open(args.donor, alias="donor")
        doc = ws.open(args.file, alias="target")
        part = doc.import_layout_from(donor, args.name)
        doc.save()
        print(f"imported '{args.name}' as {part} into {args.file}")
    elif args.cmd == "replace":
        mapping = dict(kv.split("=", 1) for kv in args.map)
        doc = ws.open(args.file)
        hits = doc.replace_text(mapping)
        doc.save()
        print(f"replaced {hits} run(s) in {args.file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
