# PREVIEW NOTES — for-agents WebPage JSON-LD (2026-10-02)

**Status:** PREVIEW ONLY · **NOT shipped to HubSpot** · Holding for Joe OK  
**Live URL (unchanged):** https://www.ucspa.com/for-agents  
**Live gap:** 0 JSON-LD blocks (confirmed fetch 2026-10-02)

## What changes (when Joe OKs)

| Layer | Change? |
|-------|---------|
| Visible visitor copy | **No** — page body / H1 / tables / CTAs stay as live |
| `<head>` JSON-LD | **Yes** — add one `WebPage` block (soft Organization pointer) |
| Meta title / description | No (this preview retitles only for review chrome) |
| HubSpot modules | No until apply |

**Head-only / invisible:** when shipped, the schema is a `<script type="application/ld+json">` in head — not rendered as visible copy.

## Clickable preview
> **Note (2026-10-02 ~08:17 ET):** GitHub Pages may briefly still serve the earlier standalone draft (~11KB). Raw/main + htmlpreview already have the live-HTML mirror (~53KB). Prefer htmlpreview until Pages catches up.


- **GH Pages:** https://joedirect7.github.io/ucspa-redesign-mockup-20260926/for-agents-schema-preview-20261002/
- **htmlpreview fallback:** https://htmlpreview.github.io/?https://github.com/joedirect7/ucspa-redesign-mockup-20260926/blob/main/for-agents-schema-preview-20261002/index.html
- **Box self-contained:** `/workspace/ucs-seo/seo-agency-scoreboard/schema-drafts/for-agents-20261002/preview/index.html`
- **GH deploy copy:** `/workspace/ucs-seo/gh-pages-deploy/for-agents-schema-preview-20261002/index.html`

Preview chrome (yellow badge banner + “Proposed head addition” panel) is **review-only** and must **not** ship.

## Exact JSON-LD (draft)

Source: `for-agents.WebPage.jsonld`

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://www.ucspa.com/for-agents#webpage",
  "url": "https://www.ucspa.com/for-agents",
  "name": "United Claims Specialists — agent / LLM feed",
  "description": "Canonical facts for AI agents and assistants about United Claims Specialists: licensed public adjusters for property insurance claims in NJ, NY, PA, and FL. Soft-power claim help; contingency fee; no DIY claim coaching.",
  "isPartOf": {
    "@type": "WebSite",
    "@id": "https://www.ucspa.com/#website",
    "url": "https://www.ucspa.com/",
    "name": "United Claims Specialists"
  },
  "about": {
    "@type": "Organization",
    "@id": "https://www.ucspa.com/#organization",
    "name": "United Claims Specialists",
    "url": "https://www.ucspa.com/",
    "telephone": "+1-855-321-5677",
    "email": "claims@ucspa.com",
    "sameAs": [
      "https://www.facebook.com/UCSPA19/",
      "https://x.com/UCS_PA",
      "https://www.instagram.com/ucs.pa/"
    ]
  },
  "significantLink": [
    "https://www.ucspa.com/llms.txt",
    "https://www.ucspa.com/llms-full.txt",
    "https://www.ucspa.com/insurance-claim-help",
    "https://www.ucspa.com/faq",
    "https://www.ucspa.com/recent-settlements"
  ],
  "inLanguage": "en-US"
}
```

## Suggested apply method

Idempotent marker (same overnight schema scripts):

```html
<!-- ucs-schema-jsonld -->
<script type="application/ld+json">
{ …draft… }
</script>
<!-- /ucs-schema-jsonld -->
```

Place in page head or HubSpot HTML module that renders in `<head>`. Do not duplicate if marker already present. Portal 20198825 · page id live body class `hs-content-id-223136673693`.

Snippet file: `preview/proposed-head-snippet.html`

## QC — visitor jargon scan

**Mirrored live body (chrome + schema stripped):** zero hits for soft-power / Brand line / Soft CTA / score notes / DIY / denial thesis.  
(Only “PREVIEW” appears in the review-only `<title>` override.)

**JSON-LD `description` string (agent/crawler-visible, invisible to humans):** contains the words **“Soft-power”** and **“DIY”**. Flag for Joe — draft kept as written; optional scrub before ship, e.g. drop those two phrases from `description` while keeping the soft-power *intent* (no denial thesis, no DIY coaching as policy).

## Confirmation

- **NOT shipped** to HubSpot / live CDN  
- Box-only build; no `machineId`  
- Parent holds ship until Joe OK  
