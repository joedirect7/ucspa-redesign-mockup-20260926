# UCS FAQ — Publish-Ready Package (HubSpot-chrome preview)

**Status:** Preview polish complete · **NOT published** to HubSpot `/faq`  
**Date:** 2026-09-30 (ET)  
**Cache-bust:** `v=20260930204457`

## Latest preview URLs

- **Primary (use this):** https://joedirect7.github.io/ucspa-redesign-mockup-20260926/faq-hubspot/?v=20260930204457
- Dated mirror: https://joedirect7.github.io/ucspa-redesign-mockup-20260926/faq-hubspot-preview-20260930/?v=20260930204457

## Local source

`/workspace/ucs-seo/faq-hubspot-preview-20260930/`

HubSpot paste helpers (when unlocked): `_chrome/`
- `faq-jsonld.html` — FAQPage JSON-LD
- `faq-hero-intro.html` — intro tile only
- `faq-body-snippet.html` — TOC + accordion + More-from + bottom CTA band + paste notes
- `css-urls.txt` — stylesheet link notes

## Counts & schema

| Item | Value |
|------|-------|
| Visible Q count | **20** |
| FAQPage `mainEntity` count | **20** |
| Schema ↔ visible Q titles | **Exact match** (Title Case) |
| Schema ↔ visible answer text | **Exact match** (links stripped to plain text in JSON-LD) |
| robots on preview | `noindex,nofollow` (preview only) |

## Final Q list (titles)

1. What Does a Public Adjuster Do?
2. How Is a Public Adjuster Different From the Insurance Company’s Adjuster?
3. How Is a Public Adjuster Different From My Insurance Agent or Broker?
4. Does UCS Handle Commercial Property Claims as Well as Residential?
5. When Does Hiring a Public Adjuster Usually Make Sense?
6. Is It Best to Involve a Public Adjuster From Claim Onset?
7. Should I Accept the Insurance Company’s First Offer?
8. Can My Contractor Negotiate the Insurance Claim for Me?
9. What If My Claim Was Underpaid or the First Scope Missed Damage?
10. How Does UCS Get Paid?
11. What Does United Claims Specialists Actually Do on a Claim?
12. What Is the Appraisal Clause?
13. What Are Additional Living Expenses (ALE)?
14. What Does “Matching” Mean for Undamaged Property?
15. What’s the Difference Between a Regular Storm Deductible and a Hurricane Deductible?
16. Are There Time Limits on Property Insurance Claims?
17. Where Does UCS Serve Policyholders?
18. What Should I Bring to a Free Claim Consult?
19. How Can I Check Reviews for UCS?
20. How Do I Get Claim Help From UCS?

## Hard locks checklist (do not regress)

- [x] **No site header** on this page (HubSpot header chrome removed from preview)
- [x] **Intro** = H1 (“Frequently Asked Questions”) + **Free Claim Consult** + **phone** only (no Browse 20 answers; no third intro CTA; no frost lede)
- [x] **Serve Q** = Q17 “Where Does UCS Serve Policyholders?” (no near-me SEO stuffing; no license numbers in answer)
- [x] **Socials** = platform links only (Facebook / X / Instagram in Q19; footer icons FB / X / IG / LinkedIn)
- [x] **More-from** = frost card grid titled “More from United Claims Specialists”
  - Cards: Free Claim Consult, Locations, Storm Damage, Blog & Resources
  - **No Reviews card**
  - State hubs row: New Jersey, New York, Pennsylvania, Florida
- [x] **No FL lic#** / no license-number copy in FAQ body or CTA band
- [x] **Q4** commercial: shopping plazas, restaurants, apartments, nursing homes, bowling alleys, industrial parks, **80+ buildings**
- [x] **Q8** UPPA: contractor negotiating claim without PA license illegal in most states / unlicensed practice of public adjusting (not legal advice)
- [x] No DIY / do-it-yourself framing
- [x] No inventing new CTAs; intro CTAs locked to Free Claim Consult + phone
- [x] Per-answer soft CTAs retained (point to Insurance Claim Help) — not intro CTAs

## QC notes (2026-09-30 final pass)

- Live + local HTML checked: no Browse 20, no Reviews More-from card, no FL lic#, no DIY.
- Main content links sampled HTTP 200 (Insurance Claim Help, Locations, Storm Damage, Blog, Reviews page, state hubs, Hurricane Damage, FB/X/IG). LinkedIn returned 999 from fetch egress (bot block); URL is valid company page.
- Schema answer text synced to visible answers (prior drift on Q2/Q6/Q7/Q11/Q15/Q17–Q20 fixed).
- Visual polish pushed: tighter intro top spacing after header removal; scroll-padding tuned for banner+TOC; More-from 4-card grid forced clean **2×2** (no orphan under 3-col); CTA band label aligned to **Free Claim Consult**; removed orphan `</div>` before CTA band.

## Remaining Joe unlock needed for HubSpot `/faq`

**Do NOT publish until Joe unlocks.** Remaining decisions / access:

1. **CMS unlock** — permission to replace or create live HubSpot page at proposed slug `/faq` (confirm slug vs `/public-adjuster-faq` / `/faqs` if still open).
2. **Header lock on live** — confirm live template can omit/hide global site header on `/faq` only (same as this preview).
3. **JSON-LD inject** — approve FAQPage script in `<head>` or SEO module (snippet ready in `_chrome/faq-jsonld.html`).
4. **CSS host** — upload `assets/css/faq-modern.css` to HubSpot Files and wire stylesheet on the page (cache-bust query).
5. **Footer form** — preview uses frost CTA substitute; decide whether to restore the live HubSpot claim form module in the footer column.
6. **robots** — flip preview `noindex` → indexable when going live; set canonical to `https://www.ucspa.com/faq` (already proposed).
7. **Final eyeball** — Joe sign-off on GH Pages URL above before any HubSpot publish.

## Explicitly NOT done

- HubSpot CMS `/faq` live publish
- Messaging Joe
- Redesign dark-chrome FAQ paths


## Box publish package (also ready)

`/workspace/ucs-seo/faq-hubspot-publish-package-20260930/` — `faq-module-body.html` · `faq-jsonld.json` · `assets/css/faq-modern.css` · `HUBSPOT-PUBLISH-NOTES.md`  
Mirror: `/workspace/ucs-seo/faq-hubspot-preview-20260930/publish-package/`

Overnight memo: `/workspace/ucs-seo/seo-agency-scoreboard/OVERNIGHT-2026-09-30.md`
