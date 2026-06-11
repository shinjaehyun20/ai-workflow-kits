# Example: screen-design deck workflow

Reproduces the three target operations on a screen-design deck, end to end.
No binaries are committed; the demo mints its own donor and writes outputs to
a throwaway temp directory.

## Run

```bash
cd ../../plugins/office-workspace
python tests/demo_scenario.py
```

## What it does

1. Mints a donor `design-system.pptx` (one master, 11 named layouts, 2 slides).
2. Opens the donor and keeps it open as a template library.
3. **(1) Create** `screen-login.pptx` from the donor with clone-and-strip:
   inherits all 11 layouts and the theme, starts with 0 slides.
4. **(2) Copy** the donor to `screen-signup.pptx`, then replace `로그인` with
   `회원가입`; the donor stays byte-identical on disk.
5. **(3) Reuse** the "Title and Content" layout from the donor inside the login
   deck (cross-file transplant): layouts go 11 -> 12.
6. Saves changed decks and re-validates each by reopening with python-pptx.

## Expected output (abridged)

```text
== open donor (stays open as a template library) ==
  masters=1 layouts=11 slides=2
== (1) create new file from donor: clone-and-strip ==
  screen-login: masters=1 layouts=11 slides=0
== (2) copy existing file, then edit the copy (original untouched) ==
  screen-signup: replaced 2 text run(s) 로그인 -> 회원가입
== (3) reuse a layout from the donor inside the login deck (cross-file) ==
  imported 'ppt/slideLayouts/slideLayout12.xml': layouts 11 -> 12
  saved screen-login.pptx  -> OK: 0 slides, 12 layouts
  saved screen-signup.pptx -> OK: 2 slides, 11 layouts
  donor untouched on disk: design-system.pptx (byte-identical)
```
