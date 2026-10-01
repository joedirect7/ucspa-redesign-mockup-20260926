# Testimonials soft rotating hero — PREVIEW 2026-10-01 (Joe fix pass)

**Status:** Clickable preview only. **Not** published to HubSpot live.  
**Portal:** 20198825 · live path `/testimonials` → `/public-adjuster-reviews`

## Joe fix pass (2026-10-01 ~6:40 AM ET)

1. **State labels** on GBP cards: primary titles = **Florida / New Jersey / New York** (city stays in NAP address line only).
2. **Hero frost = title only**: lime kicker + H1. Removed lede, location pill, CTAs, and body copy under the title. Soft dots sit under the card (non-word UI).
3. **Rotate fixed**: removed `loading="lazy"` on hidden slides (they never decoded); opacity-only crossfade (no `visibility:hidden`); eager preload + `decode()`; script without `defer` race; cache-bust `?v=20261001c`.

## Rotation / fade

| Setting | Value |
|---|---|
| Interval | **6000 ms** |
| Fade | **1.8s** opacity ease-in-out |
| Order | Florida (Miami aerial) → New Jersey (Hackensack courthouse) → New York (Tarrytown marina) |
| Verified | CDP real-time: active 0→1→2; opacities `[1,0,0]`→`[0,1,0]`→`[0,0,1]`; shots `shots/verify-slide*.png` |

## Images

| Slide | File | Source |
|---|---|---|
| FL | `hero-miami.jpg` | Live UCS HubFS Public Adjuster Miami Florida |
| NJ | `hero-hackensack.jpg` | HubSpot city-heroes/hero-hackensack.jpg |
| NY | `hero-tarrytown.jpg` | HubSpot city-heroes/hero-tarrytown.jpg |

## GH Pages

https://joedirect7.github.io/ucspa-redesign-mockup-20260926/testimonials-hero-rotator-20261001/

**Not** live on ucspa.com / HubSpot.
