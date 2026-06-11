"""End-to-end demo of the three target operations on a screen-design deck.

Run:  python tests/demo_scenario.py
All artifacts are written to a throwaway temp dir, so nothing binary lands in
the repository.
"""

from __future__ import annotations

import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))  # the plugin root (has workspace.py)

from workspace import Workspace  # noqa: E402
import make_fixture  # noqa: E402


def reopen_ok(path: str) -> str:
    """Validate an output by reopening it with python-pptx (checks rels)."""
    try:
        from pptx import Presentation
    except Exception:
        return "python-pptx not installed (skipped validation)"
    prs = Presentation(path)
    return f"OK: {len(prs.slides)} slides, {len(prs.slide_layouts)} layouts"


def main() -> int:
    work = tempfile.mkdtemp(prefix="office-ws-")
    donor = os.path.join(work, "design-system.pptx")
    login = os.path.join(work, "screen-login.pptx")
    signup = os.path.join(work, "screen-signup.pptx")
    make_fixture.build(donor)
    donor_bytes = open(donor, "rb").read()

    ws = Workspace()

    print("== open donor (stays open as a template library) ==")
    d = ws.open(donor, alias="donor")
    inv = d.inventory()
    print(f"  masters={len(inv['masters'])} layouts={len(inv['layouts'])} slides={len(inv['slides'])}")
    print(f"  layout names: {[l['name'] for l in inv['layouts']]}")

    print("\n== (1) create new file from donor: clone-and-strip ==")
    lg = ws.create(login, clone_from="donor", alias="login")
    inv = lg.inventory()
    print(f"  screen-login: masters={len(inv['masters'])} layouts={len(inv['layouts'])} slides={len(inv['slides'])}")
    assert len(inv["slides"]) == 0, "new file should start with no slides"
    assert len(inv["layouts"]) >= 1, "masters/layouts must be inherited"

    print("\n== (2) copy existing file, then edit the copy (original untouched) ==")
    su = ws.copy(donor, signup, alias="signup")
    hits = su.replace_text({"로그인": "회원가입"})
    print(f"  screen-signup: replaced {hits} text run(s) 로그인 -> 회원가입")
    assert hits >= 1

    print("\n== (3) reuse a layout from the donor inside the login deck (cross-file) ==")
    before = len(lg.inventory()["layouts"])
    new_part = lg.import_layout_from(d, "Title and Content")
    after = len(lg.inventory()["layouts"])
    print(f"  imported '{new_part}': layouts {before} -> {after}")
    assert after == before + 1

    print("\n== save changed documents (read-only donor is left untouched) ==")
    for p in ws.save_all():
        print(f"  saved {os.path.basename(p)} -> {reopen_ok(p)}")
    assert open(donor, "rb").read() == donor_bytes, "donor must be byte-identical"
    print(f"  donor untouched on disk: {os.path.basename(donor)} (byte-identical)")

    print("\nworkspace handles:", [h["handle"] for h in ws.list()])
    print("\nALL GOOD. artifacts in:", work)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
