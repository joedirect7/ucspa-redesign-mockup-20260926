# STATUS — Claim-help banner text swap (PREVIEW ONLY)

**When:** 2026-10-02 ~08:20 ET  
**Portal:** 20198825 (box-only — no JOE_HP2 / machineId)  
**Live HubSpot:** **NOT changed**  
**QC mindset:** ucs-hubspot-page-publish-qc-gate + ucs-copy-language-qc-gate (sentence case as Joe wrote; periods kept; no `!`)

## Ask
Joe (2026-10-02): top of `/insurance-claim-help` form banner — change lime H1 from current to **Lower Stress. Higher Settlement** (exact casing). Color/font/style unchanged; words only.

## Located
| Field | Value |
|-------|-------|
| Live URL | https://www.ucspa.com/insurance-claim-help |
| Page name | Get Claim Help |
| Page id | `53697315391` |
| Module | `dnd_area-module-3` (`@hubspot/rich_text`) |
| Color | `#99cc02` (inline on `<span>`) |
| Font | Theme `h1` → **GoodTimes** (display; reads ALL-CAPS-ish even when source is mixed case) |
| CSS text-transform | **None** on this module — prefer true source casing |

### BEFORE (live source, verified 2026-10-02)
```html
<h1><span style="color: #99cc02;">More money, less stress, no risk.</span></h1>
```

### AFTER (proposed draft — not in HubSpot)
```html
<h1><span style="color: #99cc02;">Lower Stress. Higher Settlement</span></h1>
```

## Preview (clickable)
**Index (GH Pages — may lag ~1–2 min after push):** https://joedirect7.github.io/ucspa-redesign-mockup-20260926/claim-help-banner-20261002/

**Instant fallbacks (work now):**
- Index: https://htmlpreview.github.io/?https://github.com/joedirect7/ucspa-redesign-mockup-20260926/blob/main/claim-help-banner-20261002/index.html
- BEFORE: https://htmlpreview.github.io/?https://github.com/joedirect7/ucspa-redesign-mockup-20260926/blob/main/claim-help-banner-20261002/before/index.html
- AFTER: https://htmlpreview.github.io/?https://github.com/joedirect7/ucspa-redesign-mockup-20260926/blob/main/claim-help-banner-20261002/after/index.html
- raw.githack index: https://raw.githack.com/joedirect7/ucspa-redesign-mockup-20260926/main/claim-help-banner-20261002/index.html
- raw.githack AFTER: https://raw.githack.com/joedirect7/ucspa-redesign-mockup-20260926/main/claim-help-banner-20261002/after/index.html

| | URL |
|--|-----|
| BEFORE | https://joedirect7.github.io/ucspa-redesign-mockup-20260926/claim-help-banner-20261002/before/ |
| AFTER | https://joedirect7.github.io/ucspa-redesign-mockup-20260926/claim-help-banner-20261002/after/ |

Mobile note: open AFTER, shrink ~390px — form 1-col, H1 wraps, no crush. Claim-help phone **855-917-2449** / 24/7 messaging **unchanged**.

Marker: `UCS-CLAIM-HELP-BANNER-20261002`

## Live verify (still old)
- `More money, less stress, no risk.` → **present**
- `Lower Stress` → **absent**
- Confirmed via live HTML fetch after preview build.

## Ship gate
**STOP** — do not PUT/publish HubSpot until Joe OK via parent. Proposed module HTML swap is one string change in `dnd_area-module-3` params.html only.
