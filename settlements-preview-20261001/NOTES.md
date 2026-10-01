# Settlements homepage module — PREVIEW ONLY (2026-10-01)

**Status:** Preview only. Not published to HubSpot / ucspa.com. Served from this GitHub Pages mockup repo.

## Clickable URLs (GitHub Pages)
- **Primary:** https://joedirect7.github.io/ucspa-redesign-mockup-20260926/settlements/
- Dated mirror: https://joedirect7.github.io/ucspa-redesign-mockup-20260926/settlements-preview-20261001/

## Paths
- Preview page: `settlements-preview-20261001/index.html` (identical copy at `settlements/index.html`)
- Source screenshots and the raw live curl were not part of this Pages publish.

## Placement
- **Recommendation:** immediately under the homepage hero, before the next content block.
- **Insertion selector / needle used:** after the hero’s closing `</div><!--end row-wrapper -->` that ends the first DnD row containing `.Hero-Section`, and **before** `<div class="row-fluid-wrapper row-depth-1 row-number-2 ">` (the row that wraps `.Three-column-section`).
- Preview HTML shows live UCS header + hero + this Settlements band in one continuous page chrome (not a naked card strip).
- Measured (1280×1600 viewport): hero bottom ≈ **960.6px**; Settlements `#ucs-settlements-preview` top matches that exactly; module height ≈ **529px**.

## CTA /recent-settlements
- URL: https://www.ucspa.com/recent-settlements
- **HTTP 200** (verified 2026-10-01). Title: “Recent Settlements By United Claims Specialists | Public Adjusters”. Not a 404.
- Button label: **View more settlements** → that URL.

## Joe lock copy (2026-10-01)
- Heading: Settlements
- Sub: Initial payment vs final recovery with UCS
- Card 1: Westchester doctor’s office — Initial payment $200,000 → Final recovery $2,000,000
- Card 2: Paramus fire — Initial $62,000 → Final $390,000
- Helper (soft-power, no bang): Your insurance has an adjuster, so should you.
- Only these two cards — no invented cases.

## Visual treatment
- **A True frost / glass** matching helping-cards frost + glass-system lock:
  - Translucent frosted cards (`rgba(255,255,255,~0.18)` fill + white→lime-tint gradient)
  - `backdrop-filter: blur(44px) saturate(1.8)`
  - Large rounded corners (**26px** radius; helping frost uses 18px; nav glass pills use large radius)
  - Soft lime edge ring `#98cc00` / accent CTA `#99cc02`
  - Soft power, no exclamation marks, no denial thesis
- Section sits on a darkened kitchen-fire photo (live HubSpot hero asset) so glass blur-through reads clearly against texture (same approach as helping-cards frost scene).
- Fonts: Lato (site face already present in live HTML); lime/CTAs aligned with live header glass / theme lime.

## Screenshot method
- Headless Chrome only:
  `google-chrome --headless --disable-gpu --window-size=1280,1600 --screenshot=... file://...`
- Throwaway `--user-data-dir=/tmp/ucs-settlements-chrome-preview`
- Did **not** use `DISPLAY=:8`, `/home/box/chrome-profile`, remote-debugging-port **9223**, or kill any existing Chrome.

## Marker
`UCS-SETTLEMENTS-PREVIEW-20261001` in injected `<style id="ucs-settlements-preview-css">` and section comment.
