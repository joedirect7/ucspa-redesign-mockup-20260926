# City hero bake process (locked 2026-09-28)

## Problem
Tall hero bands (`min-height: 520px+`) + `background-size: cover` / `object-fit: cover` on 4:3 (or even 2:1) photos **zoom into the center** and crop the establishing scene — same class of framing bug as the homepage hero before the z091 soft pass.

## Rule (all city heroes: Hackensack, Paramus, Englewood, Tarrytown, Westchester, …)
1. **Bake soft establishing frames first** — do not rely on CSS alone.
2. **Canvas:** `1920×960` (2:1). Matches the Paramus / Englewood / Westchester / Tarrytown lock size.
3. **Soft factor:** place the source at `cover_scale × soft` on that canvas, then **edge-strip extend** to fill letterboxing (no blur, no stretch of the subject).
   - Default soft ≈ **0.91** (~9% more scene than tight cover) — same intent as homepage `ucs-hero-20260928-z091`.
   - Use **0.85** when Joe flags a frame as “too zoomed in” (Hackensack courthouse).
4. **CSS band:** keep the on-page hero **short and wide** so cover does not re-zoom the bake:
   - `aspect-ratio: 2 / 1`
   - `min-height: clamp(18rem, 38vw, 26rem)`
   - `max-height: min(62vh, 520px)`
5. **Never** aggressive center-crop into a tall hero band. Prefer more sky/street context over filling a tall module.
6. Cache-bust the asset (`?v=soft3`, etc.) after rebake.

## Script sketch
See bake used 2026-09-28 (edge-extend soft cover → JPEG q88). Backups: `assets/img/city-hero-bak/`.

## Hackensack note
Locked subject remains **Bergen County courthouse**. Rebaked from `02-bergen-county-courthouse-wide.jpg` at soft **0.85** → `locations/hackensack/refs/hero-hackensack-courthouse.jpg` (and `locations/refs/` mirror).
