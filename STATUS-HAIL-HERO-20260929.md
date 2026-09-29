# Hail scrub + city hero blur fix — 2026-09-29 ~8:30 AM ET

## Mock (GH Pages) — DONE this pass
Repo: `joedirect7/ucspa-redesign-mockup-20260926` (commit pending push)

### Heroes — kill blur-fill pillarbox
- Bake script `scripts/bake_city_hero_establishing.py` rewritten: **true cover crop only** (no Gaussian blur letterbox).
- **Cherry Hill:** swapped municipal brick office → South Jersey residential suburb (`locations/cherry-hill/hero-temp-suburb-residential.jpg?v=cover1`).
- **Philadelphia / Tarrytown / Westchester / Englewood / Hackensack / Paramus:** rebaked cover / strip-pillar; cache-bust `?v=cover1`.
- Flat + folder twins updated.

### Hail $1.4M — mock audit
- HTML/JS: **zero** refs to `1.4M`, `1,400,000`, `orig-style-hail`, CDN `206595696_…_n.png`, “Hail Storm Claims”.
- City + HubSpot NJ/NY state previews already on approved-v09/v03/v01 rotator only.
- Archived leftover `orig-style-fire-1.4m*.png` out of active `settlement-mocks/` (not referenced).

## Live HubSpot — BLOCKED on auth (cookie 401)
Portal `20198825`. Cookie seed present but CMS API returns **401 Unauthorized** (session stale; Google SSO needed).

### Confirmed live hail CDN hits (2026-09-29 audit)
All still serve `hubfs/206595696_4136872553054948_4036581170947666532_n.png` ($1.4M Hail Storm Claims board):

| Page ID | URL |
|---|---|
| 189810364998 | /public-adjuster-pennsylvania |
| 52019329158 | /public-adjuster-new-jersey |
| 52019329150 | /public-adjuster-new-york |
| 52017061227 | /public-adjuster-florida |
| 69407781452 | /public-adjuster-texas |
| 189751189830 | /public-adjuster-georgia |
| 54151405389 | /public-adjuster-louisiana |
| 69407781468 | /public-adjuster-los-angeles |

Home + damage/service pages: clean.

### Ready script (run after fresh HubSpot login / cookie seed)
1. Upload `assets/img/settlement/approved-v0{9,3,1}-*.png` to HubSpot File Manager under `ucs-settlement/` (or edit URLs in script).
2. `python3 live-copy-port-20260928/scrub_hail_boards_live.py`
3. Hard-refresh each URL; confirm zero `206595696` / “Hail Storm Claims” / `$1.4M`.

## GH Pages URLs (after push)
- https://joedirect7.github.io/ucspa-redesign-mockup-20260926/locations/cherry-hill.html
- https://joedirect7.github.io/ucspa-redesign-mockup-20260926/locations/philadelphia.html
- https://joedirect7.github.io/ucspa-redesign-mockup-20260926/locations/tarrytown.html
- https://joedirect7.github.io/ucspa-redesign-mockup-20260926/locations/westchester.html
- https://joedirect7.github.io/ucspa-redesign-mockup-20260926/locations/englewood.html
- https://joedirect7.github.io/ucspa-redesign-mockup-20260926/locations/hackensack.html
- https://joedirect7.github.io/ucspa-redesign-mockup-20260926/locations/paramus.html
