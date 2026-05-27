# Public Safety

This repository is public.

Do not publish:

- private local paths
- private project labels
- credentials
- local logs
- local audit trails
- generated delivery bundles

Before pushing:

```powershell
python tools/public-safety-scan.py --history
```

If sensitive content was pushed, rotate exposed credentials first, then remove the content and review whether history cleanup is needed.
