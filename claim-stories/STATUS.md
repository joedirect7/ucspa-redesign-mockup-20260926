# Claim Stories mock — STATUS 2026-09-30 ~10:52 EDT

## Locked (Joe 2026-09-30 feedback)
- H1/title: **Claim Stories** (not Claim Social) — one H1 only
- Glass: **A True frost** on hero + CTA panels
- Hero: **PA plight journey** slow crossfade (6 sharp stills) behind frost — not blurry muted damage alone
- Beats: (1) getting the call (2) inspecting (3) helping distraught owners (4) researching/scoping (5) estimating (6) negotiating hard for insureds
- Soft-power not fight-hype; furnished sudden-occurrence; UCS lime/blue polo; match ucs-claim-scene-stills look; no AI logo text in frame
- Veil lightened so stills stay crisp; frost card still readable; 2s dissolve / 7s interval
- Messaging: no visitor jargon (no soft power / beta / from the field / Denied); **no HubSpot publish**; no Joe message from this pass
- Social: icon links only; live-style nav

## Engine
- Higgsfield `gpt_image_2_5` · flare · high · 2k · 16:9
- folder_id `50176a29-0dd5-4f20-a354-ec9cad7ce40a`
- Masters PNG + web JPG: `assets/img/hero-journey/`
- Job ids: `_gen/job-ids.json`

## Fix this pass (Joe: PA plight contact sheet bottom-left)
- **Beat fixed:** `04` Researching & scoping (contact-sheet bottom-left)
- **Issue:** cabinet showed unfinished BACK panel as if FRONT
- **Regen:** `c59cb232-1125-44bd-8eca-991c7b4be9d3` — furnished kitchen, sudden under-sink damage, finished grey shaker **FRONT** doors/faces + hardware, UCS navy polo PA scoping
- Updated: hero-journey master PNG/JPG, preview, CONTACT-SHEET, carousel asset, shots (`desktop-hero.png`, `desktop-full-viewport.png` forced to beat 4)
- BOX only — no HubSpot, no Joe message

## Paths
- Local box: `/workspace/ucs-seo/claim-stories-mock-20260930/`
- Local preview: `http://127.0.0.1:8877/`
- GH Pages: https://joedirect7.github.io/ucspa-redesign-mockup-20260926/claim-stories/
- Dated mirror: https://joedirect7.github.io/ucspa-redesign-mockup-20260926/claim-stories-mock-20260930/

## Shots
- `shots/desktop-hero.png` (reshot 2026-09-30 ~10:52 EDT — beat 4 Researching & scoping behind frost)
- Contact sheet: `_gen/previews/CONTACT-SHEET-pa-journey.jpg`

## Face polish 2026-10-02 (Joe: 100% should look like 75%)
- Issue: distressed insured face (esp. slide 01 phone/cream sweater) looked harsh/grainy at 100% browser zoom; OK at 75%.
- Fix: reprocessed all 6 `hero-journey/*.jpg` — LANCZOS downscale 0.75 + BILINEAR upscale (browser 75% look at 100%). Masters PNG unchanged (not served).
- Kept: auto crossfade dissolve (7s / 2s), no dots, A True frost, H1 Claim Stories, object-position 28% 28% (insured left of frost).
- **Not HubSpot.** Preview only.
- Face crops: `_gen/face-polish-20261002/face-01-BEFORE-100pct.png`, `face-01-AFTER-100pct.png`, `face-01-COMPARE.png`
