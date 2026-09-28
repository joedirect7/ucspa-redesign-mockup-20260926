# Copy Notes

## City hero soft establishing 2026-09-28 (ET)

Joe: Hackensack courthouse was too zoomed in (same class of bug as home).

- Rebaked courthouse to **1920×960 soft 0.85** establishing frame (edge-strip fill).
- Soft-rebaked Paramus / Englewood / White Plains / Tarrytown heroes at soft **0.91**.
- Softened city hero CSS band (2:1 aspect, shorter min-height) so cover does not re-zoom.
- Process documented in `locations/HERO-BAKE.md` — use for all future city heroes.


## City mockups visual pass 2026-09-28 (ET)

Applied the same treatment to Paramus, Hackensack, Englewood, White Plains, Tarrytown (folder `locations/<city>/index.html` + flat `locations/<city>.html`) and confirmed locations index:

- Real keyed 3D UCS logo in header (`../../assets/img/ucs-logo-3d.png` / `../assets/img/…`) — replaces `refs/icons/logo.jpg`
- More indented top gutters: wrap padding + extra inset on topbar / site-header / hero
- Locations index already uses premium photo tiles (prior commit)

HubSpot untouched.

## Homepage + locations visual pass 2026-09-28 (ET)

Mockup-only (GitHub Pages). HubSpot / live WordPress **not** touched in this pass.

1. **Hero imagery:** Homepage (and dissolve variant) now dissolve-rotates the locked zoom-out 16×9 set from `home-hero-options` / HubSpot `ucs-hero-20260928-z091`: HF-01, HF-20, HF-17, HF-06, HF-12, HF-07, HF-13, LIVE-01f — plus **kept** the prior blue-tarp still (`KEEP-blue-tarp-storm-home.png`) as the 9th slide. Assets live under `assets/img/heroes/`.
2. **Top inset:** `--gutter-top` + extras rules indent header + hero content further from the edges.
3. **Real UCS logo:** Header uses `assets/img/ucs-logo-3d.png`; footer uses chrome keyed `assets/img/ucs-3d-chrome-keyed.png` (from PR #6 / brand assets). Placeholder `.logo__mark` plate removed sitewide.
4. **Locations:** Replaced weak white pin / “Learn more →” card grid with premium treatment — large photo tiles for **Florida / New Jersey / New York**, compact photo cards for LA / TX / LA / GA / PA. Photos from live UCS location page HubSpot assets, stored in `assets/img/locations/`.

Preview: https://joedirect7.github.io/ucspa-redesign-mockup-20260926/ · Locations: https://joedirect7.github.io/ucspa-redesign-mockup-20260926/locations/

## Applied 2026-09-26 (Joe)

Soft-power / deserve / owed copy from `COPY-FAIR-DESERVE-DRAFT.md` is **APPLIED** on the mockup (Joe Suskind, 2026-09-26).

- Home H1: daily rotation from `content/hero-h1-pool.js` (starts with YOUR INSURANCE HAS AN ADJUSTER. SO SHOULD YOU. and YOUR CLAIM. OUR MISSION.). See `HERO-H1-POOL.md`.
- Hero panel: THE SETTLEMENT YOU DESERVE. WITHOUT THE HEADACHES. Tag: Lower stress. Higher settlement. These do not rotate.
- Stat row: Licensed · 8+ States served · 0 Upfront fees. No percent-payout tile.
- Sitewide: “maximum payout / 700% difference / higher payouts” lines replaced with deserve, owed, fair settlement, and what the policy covers.
- Generators (`scripts/build_all.py`, `scripts/chrome.py`, `scripts/hero_h1.py`) read the H1 pool so a regenerate keeps the rotation and does not bring the old headlines back.
- OPPAGA **747%** stays a historical source note in `BLOG-COPY-RATINGS.md` and `BLOG-REVAMP-PLAN.md` only. It is not a marketing headline in HTML.

Live ucspa.com WordPress was not edited.

## City pages pass 2026-09-28

Applied the same phrase map to all five city location mocks (Hackensack, Paramus, Englewood, White Plains, Tarrytown — both `locations/<city>/index.html` and flat `locations/<city>.html`):

- `Get your maximum payout…` → `Get the settlement you deserve…`
- `pursue the maximum payout for property damage` → `pursue the settlement you deserve for property damage`
- `UCS gets you the biggest payout.` → `UCS fights for what you're actually owed.`
- `A public adjuster can make a 700% difference…` → `A public adjuster can be the difference between an underpaid claim and the settlement you deserve.`

Local `_hero-preview/*.html` under Hackensack/Paramus cleaned the H2 line only (untracked WIP). Marketing mirrors under `ucs-content/marketing/city-pages-mockup/` updated the same way (not this Pages repo). Live HubSpot/WordPress untouched. Paramus hero rotator CSS/JS not modified.

## City H2 Recover lock 2026-09-28

Joe: lock the loud city/section band H2 to **Recover** (not Get).

- Pattern: `Recover the settlement you deserve with our {City} public adjusters!`
- Replaced `Get the settlement you deserve with our` on all city mocks (Hackensack, Paramus, Englewood, White Plains, Tarrytown — flat + folder `index.html`).
- Local untracked `_hero-preview/*.html` under Hackensack/Paramus updated the same way (WIP, not committed).
- Marketing mirrors: `ucs-content/marketing/city-pages-mockup/{hackensack,paramus}.html` updated the same way (filesystem only; not this Pages repo).
- Re-scanned sitewide HTML for leftover phrase-map sources (`maximum payout` / `maximum settlement` / `biggest payout`): **0** remaining. Other locked lines kept (settlement you deserve / fair settlement / actually owed).
- HubSpot / live WordPress **not** touched.

## Earlier notes (still open)

These were light notes from before the soft-power pass. They are not a second rewrite.

| Item | Suggestion |
|------|------------|
| Footer copyright | Live still shows **© 2009–2022**; mockup uses **2009–2026** in footer for currency. Confirm preferred year range. |
| Typos | e.g. “underpaid of denied” → “or”; “local knowledge us” → “local knowledge is how”. “it’s maximum potential” was corrected in the 2026-09-26 pass. |
| Clarity | Long homepage paragraphs could use subheads (structure only — not new claims) |
| Stats | Marketing “700%” headlines are retired on the mockup. OPPAGA 747% remains a source citation in the blog planning docs only — do not put it back on a page as a promise. |
| Denied Claims nav | No dedicated live service URL found (common slugs 404); mockup `/denied-claims/` uses live denial messaging + blog links |
| Blog stubs | Some older/related posts use shorter verbatim excerpts from search/fetch when full HTML wasn’t available (HubSpot/rate limits). Prefer full paste from CMS when implementing live. |
| SMS / legal | Privacy & Terms kept; keep SMS consent language aligned with counsel |

Do **not** invent new legal claims, fake stats, or new service promises in production.
