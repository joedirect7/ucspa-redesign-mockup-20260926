# UCS Website Redesign Mockup (2026-09-26)

**United Claims Specialists** — premium static HTML remake of [ucspa.com](https://www.ucspa.com) for Joe Suskind / Master Chief.

> **Mockup only.** Live WordPress/HubSpot site was **not** modified. No deploys, no outreach.

## Preview

```bash
cd /workspace/ucs-seo/ucspa-redesign-mockup-20260926
python3 -m http.server 8765
```

Open `http://localhost:8765/` — or open `index.html` directly in a browser (relative links work either way).

## What’s in the box

| Area | Count / notes |
|------|----------------|
| HTML pages | **67** (`*/index.html` scheme) |
| Blog posts | **29** under `blog/` |
| Design system | `assets/css/design-system.css` + `extras.css` |
| Nav JS | `assets/js/nav.js` (mobile menu only) |
| Docs | README, PAGE-RANKINGS, DESIGN-NOTES, CHANGELOG-vs-live, COPY-NOTES |

## What stayed the same

- Brand name: **United Claims Specialists (UCS)** — never “Upward Consulting”
- Navigation labels & order (Storm Damage, Property Damage, Residential Claims, Commercial Claims, Denied Claims, Contractor Claim Services, About Us + Locations)
- Substantive marketing copy / claims / CTAs (verbatim where fetched; see COPY-NOTES for light suggestions only)
- Phones as shown live: **855-321-LOSS (5677)** sitewide; **855-917-2449** on claim-help
- Email: claims@ucspa.com · FL Lic # W806268

## What changed visually

- 2026 premium light theme: deep navy + white + teal accent
- Sticky glass header, pill CTAs, cinematic hero, trust strip
- Card grids (not dated boxed tables), magazine blog reading, cleaned footer
- Premium claim-help form chrome (mock — does not submit)
- Mobile sticky call bar; WCAG-minded contrast & focus states

## URL scheme

Mirrored folders with `index.html`:

- Home → `index.html`
- `/insurance-claim-help` → `insurance-claim-help/index.html`
- `/blog/slug` → `blog/slug/index.html`

## Scripts

- `scripts/chrome.py` — shared header/footer/nav
- `scripts/build_all.py` — page generators (re-run regenerates)

## Important notes

- HubSpot bot-challenged sitemap/curl; inventory built via WebFetch + search.
- Some blog posts beyond the live blog index listing were discovered via search/related articles.
- `/denied-claims/` had no discoverable dedicated live slug (404s on common paths); page composed from live denial messaging + blog links.
- Hero images are CSS gradient placeholders (no CDN image scrape).
