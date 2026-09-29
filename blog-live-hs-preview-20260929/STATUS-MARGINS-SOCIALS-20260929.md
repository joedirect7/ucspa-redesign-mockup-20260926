# STATUS — Margins + Socials (live HubSpot chrome preview) — 2026-09-29

Joe feedback on **LIVE HubSpot chrome** blog previews (`blog-live-hs-preview-20260929/`). Preview-only unless noted. **Live social PUT not published** (draft only; parent confirm required).

## 1) Margins / content column (CSS)

File: `assets/css/preview-tweaks.css` (local overrides; does not replace production theme CSS).

Changes:
- Cap `.body-container` / blog `.wrapper` / mainblog span at **1100px**, centered, 20px side padding (less empty side space on wide viewports).
- `.Post-Content` → flex row; left CTA fixed ~200px; **`.post-body` max-width 820px** (theme had ~650px / 50% width feel).
- Mobile ≤991px: stack CTA + body full width.

Aim: normal readable blog width for what we’ll target on HubSpot.

## 2) Preview chrome socials (header + footer)

Updated in `_chrome/header.html`, `_chrome/footer.html`, and all five post HTML pages.

| Network   | URL | Notes |
|-----------|-----|--------|
| Facebook  | https://www.facebook.com/UnitedClaimsSpecialistsFL | Unchanged (live) |
| **X**     | https://x.com/UCS_PA | Was `twitter.com/ucs_pa` + Twitter bird; now X mark. Site account **UCS_PA** (not @JoeDirect77). |
| **Instagram** | https://www.instagram.com/ucs.pa/ | **Added** (was missing) |
| LinkedIn  | https://www.linkedin.com/company/united-claims-specialists/ | Unchanged (live) |

Icons:
- Header PNGs: local `assets/img/social/X-Green.png`, `Instagram-Green.png` (lime #98cc00 glyphs matching live FB/LI/Twitter assets). FB/LI still from hubfs.
- Footer: inline SVGs (FA-style X + Instagram; FB/LI paths kept).

**Not invented:** no YouTube / TikTok / etc. (none on live header/footer HTML).

## 3) LIVE site audit — needs the same social fix?

**YES.** Public HTML on https://www.ucspa.com (home + blog post) still has:

- `https://twitter.com/ucs_pa` + Twitter bird (`Twitter-Green.png` header / FA `Twitter2` footer SVG)
- **No Instagram**
- Facebook + LinkedIn only otherwise

Exact modules/files (portal **20198825**):

| Piece | ID / path |
|-------|-----------|
| Header module | **50485963365** — `/UCS - Theme/modules/Header Section - UCS` |
| Header partial | `UCS - Theme/templates/partials/header.html` → `module_162883720295314` |
| Header source | `UCS - Theme/modules/Header Section - UCS.module/module.html` (locked `icon_group`) |
| Footer module | **50694621511** — `/United Claims Specialists/Custom Modules/Footer Section - UCS` |
| Footer partial | `UCS - Theme/templates/partials/footer.html` → `module_162883581065366` |
| Footer source | `.../Footer Section - UCS.module/module.html` (locked `social_icon_group`) |

Draft fix (cookie-auth CMS source-code API, CDP 9230 / chrome-cookie-seed):

- Script: `_chrome/live-audit/DRAFT-fix-LIVE-SOCIALS-20260929.py`
- Dry-run backups: `_chrome/live-audit/social-fix-backup-*/`
- **Not applied.** Requires `CONFIRM_LIVE_SOCIAL_FIX=1` + `--apply` after parent confirms.
- Also upload `Home Page/X-Green.png` + `Instagram-Green.png` to File Manager before apply.

## 4) Serve + GH Pages

Local (port **8767**):

```bash
python3 -m http.server 8767 --bind 127.0.0.1 --directory /workspace/ucs-seo/blog-live-hs-preview-20260929
```

Curl-verified 200: `/`, post HTML, `preview-tweaks.css`, `X-Green.png`, `Instagram-Green.png`.

GH Pages path (repo `joedirect7/ucspa-redesign-mockup-20260926`, branch `main`):

- https://joedirect7.github.io/ucspa-redesign-mockup-20260926/blog-live-hs-preview-20260929/
- Posts under `.../blog-live-hs-preview-20260929/blog/<slug>/`

## Explicitly NOT done

- Live HubSpot publish of socials
- Redesign mockup / `blog-site-preview-20260929` chrome
- Inventing socials not on live (YouTube, etc.)
