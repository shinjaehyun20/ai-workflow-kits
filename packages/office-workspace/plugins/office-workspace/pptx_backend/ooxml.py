"""Low-level OOXML helpers for the PPTX backend.

A .pptx file is a ZIP archive of XML parts plus media. This module reads the
archive into an in-memory part map and gives small, dependency-free helpers
for the two structures that drive cross-file work:

* ``Rels``         -- a ``.rels`` relationship file (Id -> Type/Target)
* ``ContentTypes`` -- ``[Content_Types].xml`` (Default + Override entries)

Only the Python standard library is used (zipfile + xml.etree), so the engine
runs anywhere without ``python-pptx`` or ``lxml`` installed.
"""

from __future__ import annotations

import io
import re
import zipfile
from xml.etree import ElementTree as ET

# --- namespaces -------------------------------------------------------------
NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
# Keep prefixes stable on write so Office stays happy.
for _prefix, _uri in NS.items():
    ET.register_namespace(_prefix, _uri)

RELS_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"

RT_SLIDE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide"
RT_LAYOUT = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout"
RT_MASTER = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster"
RT_THEME = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme"
RT_IMAGE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"

CT_SLIDE = "application/vnd.openxmlformats-officedocument.presentationml.slide+xml"
CT_LAYOUT = "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"


def qn(tag: str) -> str:
    """Resolve a ``prefix:local`` tag to a Clark-notation name."""
    prefix, local = tag.split(":", 1)
    return f"{{{NS[prefix]}}}{local}"


# --- package read/write -----------------------------------------------------
def read_package(path: str) -> dict[str, bytes]:
    """Read every member of a .pptx ZIP into ``{part_name: bytes}``."""
    parts: dict[str, bytes] = {}
    with zipfile.ZipFile(path, "r") as zf:
        for name in zf.namelist():
            parts[name] = zf.read(name)
    return parts


def write_package(path: str, parts: dict[str, bytes]) -> None:
    """Write a part map back out as a deflated .pptx ZIP."""
    # [Content_Types].xml first is conventional and keeps some readers happy.
    ordered = sorted(parts, key=lambda n: (n != "[Content_Types].xml", n))
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        for name in ordered:
            zf.writestr(name, parts[name])


# --- XML helpers ------------------------------------------------------------
def parse_xml(data: bytes) -> ET.Element:
    return ET.fromstring(data)


def serialize_xml(elem: ET.Element) -> bytes:
    return ET.tostring(elem, encoding="UTF-8", xml_declaration=True)


def rels_name_for(part: str) -> str:
    """Return the .rels part name that governs ``part``."""
    if "/" in part:
        head, tail = part.rsplit("/", 1)
        return f"{head}/_rels/{tail}.rels"
    return f"_rels/{part}.rels"


# --- relationships ----------------------------------------------------------
class Rels:
    """A parsed ``.rels`` file as an ordered list of relationships."""

    def __init__(self, items: list[dict] | None = None) -> None:
        self.items: list[dict] = items or []

    @classmethod
    def parse(cls, data: bytes | None) -> "Rels":
        if not data:
            return cls([])
        root = ET.fromstring(data)
        items = []
        for rel in root:
            items.append(
                {
                    "Id": rel.get("Id"),
                    "Type": rel.get("Type"),
                    "Target": rel.get("Target"),
                    "TargetMode": rel.get("TargetMode"),
                }
            )
        return cls(items)

    def serialize(self) -> bytes:
        out = io.StringIO()
        out.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
        out.write(f'<Relationships xmlns="{RELS_NS}">')
        for it in self.items:
            out.write(f'<Relationship Id="{it["Id"]}" Type="{it["Type"]}" Target="{it["Target"]}"')
            if it.get("TargetMode"):
                out.write(f' TargetMode="{it["TargetMode"]}"')
            out.write("/>")
        out.write("</Relationships>")
        return out.getvalue().encode("utf-8")

    def by_type(self, rtype: str) -> list[dict]:
        return [it for it in self.items if it["Type"] == rtype]

    def target_for(self, rid: str) -> str | None:
        for it in self.items:
            if it["Id"] == rid:
                return it["Target"]
        return None

    def next_id(self) -> str:
        used = {int(m.group(1)) for it in self.items if (m := re.fullmatch(r"rId(\d+)", it["Id"] or ""))}
        n = 1
        while n in used:
            n += 1
        return f"rId{n}"

    def add(self, rtype: str, target: str, mode: str | None = None) -> str:
        rid = self.next_id()
        self.items.append({"Id": rid, "Type": rtype, "Target": target, "TargetMode": mode})
        return rid

    def remove_ids(self, ids: set[str]) -> None:
        self.items = [it for it in self.items if it["Id"] not in ids]


# --- content types ----------------------------------------------------------
class ContentTypes:
    """``[Content_Types].xml`` as Default(extension) + Override(part) entries."""

    def __init__(self, defaults: dict[str, str], overrides: dict[str, str]) -> None:
        self.defaults = defaults  # ext -> content type
        self.overrides = overrides  # /part/name.xml -> content type

    @classmethod
    def parse(cls, data: bytes) -> "ContentTypes":
        root = ET.fromstring(data)
        defaults, overrides = {}, {}
        for child in root:
            tag = child.tag.split("}", 1)[-1]
            if tag == "Default":
                defaults[child.get("Extension")] = child.get("ContentType")
            elif tag == "Override":
                overrides[child.get("PartName")] = child.get("ContentType")
        return cls(defaults, overrides)

    def serialize(self) -> bytes:
        out = io.StringIO()
        out.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
        out.write(f'<Types xmlns="{CT_NS}">')
        for ext, ct in self.defaults.items():
            out.write(f'<Default Extension="{ext}" ContentType="{ct}"/>')
        for part, ct in self.overrides.items():
            out.write(f'<Override PartName="{part}" ContentType="{ct}"/>')
        out.write("</Types>")
        return out.getvalue().encode("utf-8")

    def add_override(self, part_name: str, content_type: str) -> None:
        self.overrides["/" + part_name.lstrip("/")] = content_type

    def remove_override(self, part_name: str) -> None:
        self.overrides.pop("/" + part_name.lstrip("/"), None)

    def ensure_default(self, ext: str, content_type: str) -> None:
        self.defaults.setdefault(ext, content_type)
