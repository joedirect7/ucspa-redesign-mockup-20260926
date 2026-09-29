# City hero bake process (updated 2026-09-29)

## Problem (Joe 2026-09-29 ~8:14 AM ET)
Soft-bake with **Gaussian blur-fill / mirrored edge letterboxing** produced smudged pillarbox sides on city heroes (Cherry Hill, Philadelphia, Tarrytown, Westchester, …). Live home fix pattern: **edge-to-edge cover, no blur backdrop**.

## Rule
1. **Never** blur-fill, edge-strip smudge, or mirrored letterbox.
2. Bake with **true cover crop** to `1920×960` (2:1): scale with `max(W/sw, H/sh)`, center-crop. Sharp pixels edge-to-edge.
3. Optional `--extract-sharp` / center keep-fraction only when an older asset already has baked blur pillars.
4. On-page CSS band stays short/wide:
   - `aspect-ratio: 2 / 1`
   - `min-height: clamp(18rem, 38vw, 26rem)`
   - `max-height: min(62vh, 520px)`
   - `background-size: cover` (or `<img object-fit:cover>`)
5. Cache-bust after rebake (`?v=cover1`, …).

## Script
`scripts/bake_city_hero_establishing.py` — cover-only (blur args are no-ops for old callers).

## Wave lock 2026-09-29
| City | Asset |
|---|---|
| Cherry Hill | `hero-temp-suburb-residential.jpg` (South Jersey residential; replaced municipal brick office) |
| Philadelphia | `hero-temp-philly-skyline.jpg` cover from PA skyline src |
| Tarrytown | marina / Tappan Zee — center-crop strip of prior blur bake |
| Westchester | downtown aerial — center-crop strip |
| Englewood | GWB basin — sharp-content crop |
| Hackensack | courthouse cover from flickr src |
| Paramus | GSP entrance / wide-day rotator |
