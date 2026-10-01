# Testimonials soft rotating hero — PREVIEW 2026-10-01

**Status:** Clickable preview only. **Not** published to HubSpot live.  
**Portal:** 20198825 · live path `/testimonials` → `/public-adjuster-reviews`  
**Joe locks:** soft-power · clickable https preview before ship · no license #s · no invented map CTAs · glass vibe like Claim Stories

---

## What this preview shows

1. **Live HubSpot chrome** (lime top bar + white nav) matching Claim Stories / site.
2. **NEW soft rotating hero** above the GBP review band — 3 slides only:
   - **Miami** → **Hackensack (NJ)** → **Tarrytown (NY)** (order locked)
3. **Existing GBP glass cards** (curated ≥4★ quotes + CID “See all on Google”) from the 2026-10-01 ship.

Hero sits **above** the GBP 3-column cards.

---

## Rotation / fade style

| Setting | Value |
|---|---|
| Pattern | Claim Stories `hero-media--dissolve` crossfade |
| Interval | **7000 ms** (`data-interval="7000"`) |
| Fade | **2s** `opacity` + `visibility` ease-in-out |
| Chrome | Soft lime pill dots (no arrows, no flashy carousel chrome) |
| Reduced motion | Auto-rotate off when `prefers-reduced-motion: reduce` |
| Location chip | Glass chip updates label: Miami · Hackensack · Tarrytown |

---

## Images used

| Slide | File | Source |
|---|---|---|
| Miami | `assets/img/hero-miami.jpg` | Live UCS HubFS `Public Adjuster Miami Florida.jpeg` (coastal aerial) — compressed ~1860×1200 |
| Hackensack | `assets/img/hero-hackensack.jpg` | Live HubSpot city-hero `20198825/city-heroes/hero-hackensack.jpg` (Bergen County Courthouse) |
| Tarrytown | `assets/img/hero-tarrytown.jpg` | Live HubSpot city-hero `20198825/city-heroes/hero-tarrytown.jpg` (marina + Tappan Zee / Cuomo Bridge) |
| Logo | `assets/img/ucs-logo.png` | Claim Stories mock pack (UCS brand) |

Workspace mockup PNGs (`hero-mockups-hackensack`, `hero-mockups-tarrytown`) were reviewed but **not** used as slide backgrounds — they bake in full page chrome. Live city-heroes are clean photography.

---

## Soft-power copy choices

- H1: **What policyholders say about UCS** (matches live GBP intro tone)
- Lede: calm, no bangs, no denial thesis — “calm guidance when a claim gets complicated”
- CTAs: **Free claim help** → live `/insurance-claim-help/` · **Browse reviews** → `#gbp` (in-page)
- Labels: plain place names only (Miami · Hackensack · Tarrytown) — not salesy city slogans
- No license numbers · no invented map CTAs (only existing GBP “See all on Google” CID links)

Glass: **A True frost** panel (`rgba(24,28,36,.40)` + blur 32 + lime edge) over soft veil — same lock as Claim Stories / glass-system.

---

## Local pack

```
/workspace/ucs-seo/testimonials-hero-rotator-20261001/
  index.html
  NOTES.md
  assets/css/preview.css
  assets/js/hero-carousel.js
  assets/img/hero-miami.jpg
  assets/img/hero-hackensack.jpg
  assets/img/hero-tarrytown.jpg
  assets/img/ucs-logo.png
  shots/preview-desktop.png
  shots/preview-mobile.png
```

Serve: `python3 -m http.server 8891` from this folder.

---

## GH Pages (clickable https)

Repo: `joedirect7/ucspa-redesign-mockup-20260926`  
Path: `/testimonials-hero-rotator-20261001/`  
URL: https://joedirect7.github.io/ucspa-redesign-mockup-20260926/testimonials-hero-rotator-20261001/

**Not** live on ucspa.com / HubSpot.

---

## Screenshot method

Headless Chrome only, throwaway profile — no DISPLAY=:8, no CDP 9223, no machineId.
