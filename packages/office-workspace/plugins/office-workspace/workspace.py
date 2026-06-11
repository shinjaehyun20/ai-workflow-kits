"""office-workspace -- a stateful "open file" layer for office documents.

Phase 1 covers PPTX and the three frictions that show up when building
screen-design decks:

  1. create a new file (from a donor deck so masters/layouts/theme are reused)
  2. copy an existing file, then edit the copy (original stays untouched)
  3. reuse a slide master/layout from one deck inside another (cross-file)

The point of a *workspace* is that documents stay open: each one is parsed
into an in-memory part map and is only re-zipped on ``save``. Several files
live in the workspace at once and can reference each other -- which is exactly
what slide-master reuse needs (a donor deck open beside the target deck).

Pure standard library. No python-pptx / lxml required at runtime.
"""

from __future__ import annotations

import os
import shutil
from dataclasses import dataclass, field
from xml.etree import ElementTree as ET

from pptx_backend import ooxml as ox
from pptx_backend.ooxml import qn

PRESENTATION = "ppt/presentation.xml"


@dataclass
class Document:
    """One open PPTX, held as an in-memory part map until ``save``."""

    path: str
    parts: dict[str, bytes]
    dirty: bool = False

    # -- internal lookups ---------------------------------------------------
    def _pres_rels(self) -> ox.Rels:
        return ox.Rels.parse(self.parts.get(ox.rels_name_for(PRESENTATION)))

    def _content_types(self) -> ox.ContentTypes:
        return ox.ContentTypes.parse(self.parts["[Content_Types].xml"])

    def _layout_parts(self) -> list[str]:
        return sorted(
            n for n in self.parts
            if n.startswith("ppt/slideLayouts/slideLayout") and n.endswith(".xml")
        )

    def master_parts(self) -> list[str]:
        rels = self._pres_rels()
        return ["ppt/" + r["Target"].lstrip("/") for r in rels.by_type(ox.RT_MASTER)]

    def _slide_parts(self) -> list[str]:
        rels = self._pres_rels()
        return ["ppt/" + r["Target"].lstrip("/") for r in rels.by_type(ox.RT_SLIDE)]

    # -- inventory ----------------------------------------------------------
    def inventory(self) -> dict:
        """Structured list of masters, layouts (with names), and slides."""
        layouts = []
        for part in self._layout_parts():
            root = ox.parse_xml(self.parts[part])
            csld = root.find(qn("p:cSld"))
            name = csld.get("name") if csld is not None else None
            layouts.append({"part": part, "name": name})
        return {
            "path": self.path,
            "masters": self.master_parts(),
            "layouts": layouts,
            "slides": self._slide_parts(),
        }

    def layout_names(self) -> list[str]:
        return [l["name"] for l in self.inventory()["layouts"]]

    # -- operation: strip every slide (clone-and-strip target) --------------
    def strip_slides(self) -> int:
        pres = ox.parse_xml(self.parts[PRESENTATION])
        lst = pres.find(qn("p:sldIdLst"))
        removed_rids = set()
        if lst is not None:
            for sld in list(lst):
                rid = sld.get(qn("r:id"))
                if rid:
                    removed_rids.add(rid)
                lst.remove(sld)
        self.parts[PRESENTATION] = ox.serialize_xml(pres)

        rels = self._pres_rels()
        slide_targets = {r["Id"]: "ppt/" + r["Target"].lstrip("/") for r in rels.by_type(ox.RT_SLIDE)}
        rels.remove_ids(set(slide_targets))
        self.parts[ox.rels_name_for(PRESENTATION)] = rels.serialize()

        ct = self._content_types()
        n = 0
        for rid, part in slide_targets.items():
            for victim in (part, ox.rels_name_for(part)):
                self.parts.pop(victim, None)
            ct.remove_override(part)
            n += 1
        # notes slides only made sense with the slides we just dropped
        for part in [p for p in self.parts if p.startswith("ppt/notesSlides/")]:
            self.parts.pop(part, None)
            ct.remove_override(part)
        self.parts["[Content_Types].xml"] = ct.serialize()
        self.dirty = True
        return n

    # -- operation: replace text on slides ----------------------------------
    def replace_text(self, mapping: dict[str, str]) -> int:
        hits = 0
        for part in self._slide_parts():
            if part not in self.parts:
                continue
            root = ox.parse_xml(self.parts[part])
            changed = False
            for t in root.iter(qn("a:t")):
                if t.text:
                    new = t.text
                    for old, repl in mapping.items():
                        if old in new:
                            new = new.replace(old, repl)
                    if new != t.text:
                        t.text = new
                        changed = True
                        hits += 1
            if changed:
                self.parts[part] = ox.serialize_xml(root)
        if hits:
            self.dirty = True
        return hits

    # -- operation: import one layout from another open document ------------
    def import_layout_from(self, donor: "Document", layout_name: str) -> str:
        """Transplant ``layout_name`` from ``donor`` onto this deck's master.

        Copies the layout part, rewires its relationships to *this* deck's
        master, copies any media it needs, and registers it in the master's
        ``sldLayoutIdLst`` -- the cross-reference syncing python-pptx will not
        do for you.
        """
        # locate donor layout part
        donor_part = None
        for l in donor.inventory()["layouts"]:
            if l["name"] == layout_name:
                donor_part = l["part"]
                break
        if donor_part is None:
            raise KeyError(f"layout {layout_name!r} not found in donor {donor.path}")

        master_part = self.master_parts()[0]
        master_base = master_part.rsplit("/", 1)[-1]

        # allocate a fresh layout part name
        used = {
            int(n.rsplit("slideLayout", 1)[-1].split(".")[0])
            for n in self._layout_parts()
        }
        idx = 1
        while idx in used:
            idx += 1
        new_part = f"ppt/slideLayouts/slideLayout{idx}.xml"
        self.parts[new_part] = donor.parts[donor_part]

        # rebuild the layout's rels, repointed at our master + our media
        donor_rels = ox.Rels.parse(donor.parts.get(ox.rels_name_for(donor_part)))
        ct = self._content_types()
        new_items = []
        for it in donor_rels.items:
            if it["Type"] == ox.RT_MASTER:
                new_items.append({**it, "Target": f"../slideMasters/{master_base}"})
            elif it["Type"] == ox.RT_IMAGE:
                donor_media = "ppt/media/" + it["Target"].rsplit("/", 1)[-1]
                new_media_name = self._alloc_media(donor.parts.get(donor_media, b""))
                self.parts[f"ppt/media/{new_media_name}"] = donor.parts.get(donor_media, b"")
                ext = new_media_name.rsplit(".", 1)[-1].lower()
                donor_ct = donor._content_types()
                ct.ensure_default(ext, donor_ct.defaults.get(ext, "application/octet-stream"))
                new_items.append({**it, "Target": f"../media/{new_media_name}"})
            else:
                new_items.append(dict(it))
        self.parts[ox.rels_name_for(new_part)] = ox.Rels(new_items).serialize()

        # register the layout in our master
        master = ox.parse_xml(self.parts[master_part])
        lst = master.find(qn("p:sldLayoutIdLst"))
        if lst is None:
            lst = ET.SubElement(master, qn("p:sldLayoutIdLst"))
        existing_ids = [int(c.get("id")) for c in lst if c.get("id")]
        new_id = (max(existing_ids) + 1) if existing_ids else 2147483649

        master_rels = ox.Rels.parse(self.parts.get(ox.rels_name_for(master_part)))
        rid = master_rels.add(ox.RT_LAYOUT, f"../slideLayouts/{new_part.rsplit('/', 1)[-1]}")
        self.parts[ox.rels_name_for(master_part)] = master_rels.serialize()

        sld_layout_id = ET.SubElement(lst, qn("p:sldLayoutId"))
        sld_layout_id.set("id", str(new_id))
        sld_layout_id.set(qn("r:id"), rid)
        self.parts[master_part] = ox.serialize_xml(master)

        ct.add_override(new_part, ox.CT_LAYOUT)
        self.parts["[Content_Types].xml"] = ct.serialize()
        self.dirty = True
        return new_part

    def _alloc_media(self, data: bytes) -> str:
        existing = {n.rsplit("/", 1)[-1] for n in self.parts if n.startswith("ppt/media/")}
        i = 1
        while f"import_image{i}.png" in existing:
            i += 1
        return f"import_image{i}.png"

    # -- save ---------------------------------------------------------------
    def save(self, path: str | None = None) -> str:
        target = path or self.path
        ox.write_package(target, self.parts)
        self.path = target
        self.dirty = False
        return target


@dataclass
class Workspace:
    """A set of open documents that can reference each other."""

    docs: dict[str, Document] = field(default_factory=dict)

    def open(self, path: str, alias: str | None = None) -> Document:
        handle = alias or path
        doc = Document(path=path, parts=ox.read_package(path))
        self.docs[handle] = doc
        return doc

    def create(self, path: str, clone_from: str, alias: str | None = None) -> Document:
        """Create a new deck by cloning a donor and stripping its slides.

        The new deck keeps every master, layout and theme of the donor -- the
        robust way to "start from a template" that python-pptx lacks.
        """
        donor = self.docs.get(clone_from) or self.open(clone_from)
        doc = Document(path=path, parts=dict(donor.parts))
        doc.strip_slides()
        handle = alias or path
        self.docs[handle] = doc
        return doc

    def copy(self, src: str, dst: str, alias: str | None = None) -> Document:
        """Copy a file on disk and open the copy (original untouched)."""
        os.makedirs(os.path.dirname(os.path.abspath(dst)), exist_ok=True)
        shutil.copyfile(src, dst)
        return self.open(dst, alias=alias)

    def get(self, handle: str) -> Document:
        return self.docs[handle]

    def list(self) -> list[dict]:
        return [{"handle": h, "path": d.path, "dirty": d.dirty} for h, d in self.docs.items()]

    def save_all(self, force: bool = False) -> list[str]:
        """Write changed documents back to disk. Clean docs (e.g. a read-only
        donor) are left untouched unless ``force`` is set."""
        return [d.save() for d in self.docs.values() if d.dirty or force]

    def close(self, handle: str) -> None:
        self.docs.pop(handle, None)
