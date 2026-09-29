# Blog LIVE HubSpot chrome preview — 2026-09-29

**Joe lock:** Matches **CURRENT live** HubSpot site on https://www.ucspa.com — NOT the redesign mockup (`ucspa-redesign-mockup` / `blog-site-preview-20260929` redesign chrome).

**Not published to HubSpot.** Local preview only (port **8767**).

## What this pack is

- Cloned live header + footer HTML from production blog posts (fetched 2026-09-29).
- Same production CSS/CDN URLs (Header module, layout, slick, theme-overrides).
- Featured image placement matches live: `.section.post-header` → `.headerLeft.span6` (topics + H1 + author) + `.featuredImage.span6` with `background:url(...) center top/cover` (min-height from theme-overrides).
- KEEP rewrite bodies from `blog-rewrites-hubspot-ready-20260926/html/`.
- Soft titles (why-reopen H1 = **Why Reopen an Insurance Claim?**).
- Topic-fit heroes under `assets/img/blog-heroes/` (same images as blog-site-preview pack; **not** live `Denied.jpg`).

## Local URLs (port 8767)

Base: http://127.0.0.1:8767/

| Short | Soft H1 | URL |
|-------|---------|-----|
| near-me | How Can I Find a Public Adjuster Near Me? | http://127.0.0.1:8767/blog/how-can-i-find-a-public-adjuster-near-me/ |
| top-5-benefits-0 | Top 5 Benefits for Hiring a Public Insurance Adjuster | http://127.0.0.1:8767/blog/top-5-benefits-for-hiring-a-public-insurance-adjuster-0/ |
| top-reasons | Top Reasons to Hire a Public Adjuster | http://127.0.0.1:8767/blog/top-reasons-to-hire-a-public-adjuster/ |
| how-do-i-reopen | How Do I Reopen an Insurance Claim? | http://127.0.0.1:8767/blog/how-do-i-reopen-an-insurance-claim/ |
| why-reopen | Why Reopen an Insurance Claim? | http://127.0.0.1:8767/blog/why-reopen-a-denied-insurance-claim/ |

Index: http://127.0.0.1:8767/blog/

## Heroes

| Slug | Local hero | Alt |
|------|------------|-----|
| near-me | `assets/img/blog-heroes/how-can-i-find-a-public-adjuster-near-me.webp` | Navigating storm-damaged streets while searching for a local public adjuster |
| top-5-benefits-0 | `assets/img/blog-heroes/top-5-benefits-for-hiring-a-public-insurance-adjuster-0.webp` | Homeowner and public adjuster shaking hands over claim paperwork at a storm-damaged home |
| top-reasons | `assets/img/blog-heroes/top-reasons-to-hire-a-public-adjuster.webp` | Public adjuster inspecting interior damage with flashlight while homeowner looks on |
| how-do-i-reopen | `assets/img/blog-heroes/how-do-i-reopen-an-insurance-claim.webp` | Signing claim reopen and supplement paperwork at a desk with a public adjuster |
| why-reopen | `assets/img/blog-heroes/why-reopen-a-denied-insurance-claim.webp` | Reviewing closed-claim file photos and paperwork to reopen or supplement a property loss |

Live site’s `Denied.jpg` intentionally **not** used for why-reopen.

## Chrome sources

Fetched live HTML:

- https://www.ucspa.com/blog/how-do-i-reopen-an-insurance-claim
- https://www.ucspa.com/blog/top-reasons-to-hire-a-public-adjuster
- (also peeked near-me, top-5, why-reopen for featured-image URLs + topics)

Saved under `_chrome/header.html`, `_chrome/footer.html`, `_chrome/css-urls.txt`.

## CSS CDN (production)

- `module_Header_Section_-_UCS.min.css`
- `template_layout.min.css` (HubSpot default asset CDN)
- `template_slick.min.css`
- `template_theme-overrides.min.css`

## Serve

```bash
python3 -m http.server 8767 --bind 127.0.0.1 --directory /workspace/ucs-seo/blog-live-hs-preview-20260929
```

## GH Pages (optional, later)

Deploy under a path that will **not** confuse with redesign mockup, e.g.:

- `blog-live-hs-preview-20260929/` on the GH Pages branch
- **Do not** overwrite redesign mockup paths or `blog-site-preview-20260929`

## Explicitly NOT used

- `ucspa-redesign-mockup-20260926` templates
- `blog-site-preview-20260929` redesign site-header / design-system.css chrome
- HubSpot publish / content API updates
