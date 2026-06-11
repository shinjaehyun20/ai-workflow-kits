"""Minimal checks for the workspace engine. Run with pytest, or directly:

    python tests/test_workspace.py

Requires python-pptx only to mint and re-validate the fixture.
"""

from __future__ import annotations

import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from workspace import Workspace  # noqa: E402
import make_fixture  # noqa: E402


def _donor(tmp: str) -> str:
    return make_fixture.build(os.path.join(tmp, "donor.pptx"))


def test_open_inventory():
    with tempfile.TemporaryDirectory() as tmp:
        ws = Workspace()
        d = ws.open(_donor(tmp))
        inv = d.inventory()
        assert len(inv["masters"]) == 1
        assert len(inv["layouts"]) == 11
        assert len(inv["slides"]) == 2


def test_create_clone_and_strip():
    with tempfile.TemporaryDirectory() as tmp:
        ws = Workspace()
        ws.open(_donor(tmp), alias="donor")
        out = os.path.join(tmp, "new.pptx")
        doc = ws.create(out, clone_from="donor")
        inv = doc.inventory()
        assert len(inv["slides"]) == 0          # fresh deck
        assert len(inv["layouts"]) == 11        # masters/layouts inherited


def test_copy_keeps_original():
    with tempfile.TemporaryDirectory() as tmp:
        donor = _donor(tmp)
        original = open(donor, "rb").read()
        ws = Workspace()
        out = os.path.join(tmp, "copy.pptx")
        doc = ws.copy(donor, out)
        assert doc.replace_text({"로그인": "회원가입"}) >= 1
        doc.save()
        assert open(donor, "rb").read() == original  # source untouched


def test_import_layout_cross_file():
    with tempfile.TemporaryDirectory() as tmp:
        ws = Workspace()
        donor = ws.open(_donor(tmp), alias="donor")
        out = os.path.join(tmp, "new.pptx")
        doc = ws.create(out, clone_from="donor")
        before = len(doc.inventory()["layouts"])
        doc.import_layout_from(donor, "Title and Content")
        doc.save()
        # re-validate relationships via python-pptx
        from pptx import Presentation
        assert len(Presentation(out).slide_layouts) == before + 1


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)
    print("all tests passed")
