#!/usr/bin/env python3
"""Build form-lander polish previews from live HTML. PREVIEW ONLY — no HubSpot publish."""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LIVE = ROOT / "_live"
MARKER = "UCS-FORM-LANDERS-POLISH-20261001"
BRAND_PHONE_DISPLAY = "855-321-LOSS (5677)"
BRAND_PHONE_TEL = "8553215677"
CALLRAIL_DISPLAY = "855-917-2449"
CALLRAIL_TEL = "8559172449"

# Soft-power FAQ strip (4 Qs) — from FAQ-PAGE-DRAFT-20260930, shortened, no DIY/scare
FAQ_COMMON = [
  {
    "q": "What Does a Public Adjuster Do?",
    "a": "A licensed public adjuster represents you — the policyholder — on a property insurance claim: inspecting and documenting damage, preparing a supported estimate package, explaining coverage in plain language, and communicating with the carrier so you are less likely to misspeak on the record. Soft next step: <a href=\"https://www.ucspa.com/insurance-claim-help\">Insurance Claim Help</a>.",
  },
  {
    "q": "How Does UCS Get Paid?",
    "a": "We get paid when you get paid — contingency aligned with recovery, with fees disclosed under applicable state rules. Fee percentages vary by state. No outcome is guaranteed. Ask during a free consult what applies where your property sits.",
  },
  {
    "q": "Should I Accept the Insurance Company’s First Offer?",
    "a": "Often a first offer is a starting scope after a short inspection — not a complete repair budget. Pausing for a second look before you treat the number as final can matter. A licensed public adjuster can compare a first offer to a supported estimate. Soft path: <a href=\"https://www.ucspa.com/insurance-claim-help\">Insurance Claim Help</a>.",
  },
  {
    "q": "What Should I Bring to a Free Claim Consult?",
    "a": "Helpful when you have them: declarations page, carrier correspondence or estimate sheets, photos, contractor bids, claim or policy numbers, and a short timeline. Missing pieces are ok — we can still start. Call or use the form above.",
  },
]

FAQ_WATER = [
  {
    "q": "What Will My Policy Cover for Water Damage?",
    "a": "Each policy is unique. Some cover open-perils or storm/roof-related water; others are narrower. United Claims Specialists reads your declarations with you so coverage questions stay accurate — without DIY claim coaching. Soft path: <a href=\"https://www.ucspa.com/insurance-claim-help\">Insurance Claim Help</a>.",
  },
  {
    "q": "How Can a Public Adjuster Help After Water Damage?",
    "a": "Water and secondary mold issues make claims documentation-heavy. A licensed public adjuster inspects, documents, prepares a supported package, and handles carrier communication so you are less likely to misspeak on the record. Soft path: <a href=\"https://www.ucspa.com/insurance-claim-help\">Insurance Claim Help</a> or call <a href=\"tel:8553215677\">(855) 321-5677</a>.",
  },
  FAQ_COMMON[1],
  FAQ_COMMON[3],
]

FAQ_NJ = [
  {
    "q": "Is UCS Licensed for New Jersey Property Claims?",
    "a": "Hire (and verify) a licensed public adjuster where the damaged property sits. UCS serves New Jersey with local licensed public adjusters. Soft path: <a href=\"https://www.ucspa.com/insurance-claim-help\">Insurance Claim Help</a> or call <a href=\"tel:8553215677\">(855) 321-5677</a>. See also <a href=\"https://www.ucspa.com/locations\">Locations</a>.",
  },
  FAQ_COMMON[0],
  FAQ_COMMON[1],
  FAQ_COMMON[2],
]

SOFT_LINKS_CLAIM = [
  ("Insurance Claim Help", "https://www.ucspa.com/insurance-claim-help", "Free claim consult"),
  ("Water Damage Claims", "https://www.ucspa.com/water-damage-insurance-claims", "Damage type hub"),
  ("Public Adjuster NJ", "https://www.ucspa.com/public-adjuster-new-jersey", "State hub"),
  ("Public Adjuster NY", "https://www.ucspa.com/public-adjuster-new-york", "State hub"),
  ("Storm Damage", "https://www.ucspa.com/storm-damage", "Related damage"),
  ("FAQ (draft)", "https://joedirect7.github.io/ucspa-redesign-mockup-20260926/faq/", "Full FAQ mock"),
]

SOFT_LINKS_NJ = [
  ("Insurance Claim Help", "https://www.ucspa.com/insurance-claim-help", "Start a free consult"),
  ("Locations", "https://www.ucspa.com/locations", "All UCS markets"),
  ("Public Adjuster NY", "https://www.ucspa.com/public-adjuster-new-york", "Neighboring state"),
  ("Water Damage Claims", "https://www.ucspa.com/water-damage-insurance-claims", "Common NJ loss"),
  ("Storm Damage", "https://www.ucspa.com/storm-damage", "Related damage"),
  ("Recent Settlements", "https://www.ucspa.com/recent-settlements", "Proof strip"),
]

SOFT_LINKS_WATER = [
  ("Insurance Claim Help", "https://www.ucspa.com/insurance-claim-help", "Start a free consult"),
  ("Flood Damage", "https://www.ucspa.com/flood-damage", "Related peril"),
  ("Mold Damage", "https://www.ucspa.com/mold-damage-insurance-claims", "Secondary damage"),
  ("Pipe Burst", "https://www.ucspa.com/pipe-burst", "Sudden water loss"),
  ("Public Adjuster NJ", "https://www.ucspa.com/public-adjuster-new-jersey", "State hub"),
  ("Public Adjuster NY", "https://www.ucspa.com/public-adjuster-new-york", "State hub"),
]


def faq_html(faqs: list[dict], title: str, sub: str) -> str:
    items = []
    for f in faqs:
        items.append(
            f'<details class="ucs-faq-item"><summary>{f["q"]}</summary>'
            f'<div class="ucs-faq-a">{f["a"]}</div></details>'
        )
    return f'''
<!-- {MARKER} FAQ STRIP -->
<section class="ucs-faq-strip" aria-label="Frequently asked questions" id="ucs-faq-strip">
  <div class="ucs-faq-strip__inner">
    <p class="ucs-faq-strip__eyebrow">Quick answers</p>
    <h2 class="ucs-faq-strip__title">{title}</h2>
    <p class="ucs-faq-strip__sub">{sub}</p>
    {''.join(items)}
  </div>
</section>
'''


def soft_links_html(links: list[tuple], label: str = "Explore related pages") -> str:
    lis = []
    for title, href, hint in links:
        lis.append(
            f'<li><a href="{href}" rel="noopener"><strong>{title}</strong><span>{hint}</span></a></li>'
        )
    return f'''
<!-- {MARKER} SOFT LINKS -->
<nav class="ucs-soft-links" aria-label="Related pages">
  <div class="ucs-soft-links__inner">
    <p class="ucs-soft-links__label">{label}</p>
    <ul class="ucs-soft-links__grid">
      {''.join(lis)}
    </ul>
  </div>
</nav>
'''


def faq_schema(faqs: list[dict], page_url: str) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": re.sub(r"<[^>]+>", "", f["a"]),
                },
            }
            for f in faqs
        ],
        "url": page_url,
    }
    return (
        f'<!-- {MARKER} FAQPage schema -->\n'
        f'<script type="application/ld+json">\n{json.dumps(data, indent=2)}\n</script>\n'
    )


MOCK_FORM = '''
<!-- {marker} STATIC FORM MOCK — layout/fields mirror live; does NOT post -->
<div class="ucs-mock-form" data-form-lock="untouched-layout">
  <div class="hs-form stacked hs-custom-form">
    <div class="hs-form-field"><label>First name*</label><input type="text" name="firstname" autocomplete="given-name" placeholder=""></div>
    <div class="hs-form-field"><label>Last name*</label><input type="text" name="lastname" autocomplete="family-name"></div>
    <div class="hs-form-field"><label>Email*</label><input type="email" name="email" autocomplete="email"></div>
    <div class="hs-form-field"><label>Phone number*</label><input type="tel" name="phone" autocomplete="tel"></div>
    <div class="hs-form-field"><label>Property address</label><input type="text" name="address" autocomplete="street-address"></div>
    <div class="hs-form-field"><label>Tell us about the damage</label><textarea name="message" rows="4"></textarea></div>
    <div class="hs_submit"><button type="button" class="hs-button primary large" onclick="alert('Preview only — form does not submit. Live HubSpot unchanged.')">Submit</button></div>
  </div>
  <p class="ucs-mock-note">Preview mock — identical field stack &amp; live chrome colors. Does not post to HubSpot.</p>
</div>
'''.format(marker=MARKER)


def absolutize(html: str) -> str:
    """Point relative HS assets at live origin so GH Pages still paints."""
    html = html.replace('href="/hubfs/', 'href="https://www.ucspa.com/hubfs/')
    html = html.replace('src="/hubfs/', 'src="https://www.ucspa.com/hubfs/')
    html = html.replace('src="/_hcms/', 'src="https://www.ucspa.com/_hcms/')
    html = html.replace('src="/hs/', 'src="https://www.ucspa.com/hs/')
    html = html.replace("url(/_hcms/", "url(https://www.ucspa.com/_hcms/")
    html = html.replace("url('/_hcms/", "url('https://www.ucspa.com/_hcms/")
    html = html.replace('href="//', 'href="https://')
    html = html.replace('src="//', 'src="https://')
    return html


def neutralize_forms(html: str, inject_static_into: str | None = None) -> str:
    """Remove live hbspt.forms.create so preview cannot submit; optionally inject static mock."""
    # Remove form create scripts (keep other scripts)
    html = re.sub(
        r"<script data-hs-allowed=\"true\">\s*var options = \{.*?hbspt\.forms\.create\(options\);\s*</script>",
        "<!-- neutralized live form create for preview -->",
        html,
        flags=re.S,
    )
    # Also strip forms v2 loader to avoid 404 noise on GH Pages for /_hcms/forms
    html = re.sub(
        r'<script[^>]*src="[^"]*forms/v2[^"]*"[^>]*></script>',
        "<!-- forms v2 skipped in preview -->",
        html,
    )
    html = re.sub(
        r'<script[^>]*src="[^"]*forms/v2-legacy[^"]*"[^>]*></script>',
        "<!-- forms v2-legacy skipped in preview -->",
        html,
    )
    if inject_static_into:
        # Inject static mock into first matching form target container
        needle = f'<div id="{inject_static_into}"></div>'
        if needle in html:
            html = html.replace(
                needle,
                f'<div id="{inject_static_into}">{MOCK_FORM}</div>',
                1,
            )
        else:
            # claim-help uses hs_form_target_dnd_area-module-4 without self-close sometimes
            pat = rf'<div id="{re.escape(inject_static_into)}"[^>]*>\s*</div>'
            html = re.sub(pat, f'<div id="{inject_static_into}">{MOCK_FORM}</div>', html, count=1)
    return html


def inject_head(html: str, extras: str) -> str:
    banner_css = f'<link rel="stylesheet" href="../assets/css/lander-polish.css?v=20261001b" />\n'
    banner_css += f'<meta name="robots" content="noindex,nofollow" />\n'
    banner_css += f'<meta name="generator" content="{MARKER} — PREVIEW ONLY, not HubSpot published" />\n'
    insert = banner_css + extras
    if "</head>" in html:
        return html.replace("</head>", insert + "</head>", 1)
    return insert + html


def inject_banner(html: str, label: str) -> str:
    banner = (
        f'<div class="ucs-preview-banner" id="{MARKER}">'
        f'<strong>PREVIEW ONLY</strong> — {label} · marker <code>{MARKER}</code> · '
        f'live <a href="https://www.ucspa.com/" rel="noopener">ucspa.com</a> unchanged · no HubSpot publish'
        f"</div>\n"
    )
    # After <body...>
    return re.sub(r"(<body[^>]*>)", r"\1\n" + banner, html, count=1, flags=re.I)


def inject_body_class(html: str, extra: str = "") -> str:
    cls = "ucs-polish" + (f" {extra}" if extra else "")
    def repl(m):
        attrs = m.group(1)
        if re.search(r'class=', attrs, re.I):
            return re.sub(r'class="([^"]*)"', lambda mm: f'class="{mm.group(1)} {cls}"', m.group(0), count=1)
        return f'<body{attrs} class="{cls}">'
    return re.sub(r"<body([^>]*)>", repl, html, count=1, flags=re.I)


def inject_before_footer(html: str, block: str) -> str:
    # Prefer before footer global resource
    markers = [
        'data-global-resource-path="UCS - Theme/templates/partials/footer.html"',
        'class="Footer-Section',
        "<footer",
    ]
    for m in markers:
        idx = html.find(m)
        if idx != -1:
            # back up to nearest opening tag start for footer wrapper if possible
            cut = html.rfind("<div", 0, idx)
            if cut == -1 or idx - cut > 400:
                cut = idx
            return html[:cut] + block + html[cut:]
    # fallback: before </main>
    if "</main>" in html:
        return html.replace("</main>", block + "</main>", 1)
    return html + block


def strip_directions_ctas(html: str) -> str:
    """Remove Directions / Google Maps CTA links if present (Joe lock: no Directions Map CTAs)."""
    def _kill(m: re.Match) -> str:
        tag = m.group(0)
        low = tag.lower()
        text = re.sub(r"<[^>]+>", " ", tag).lower()
        if (
            "get direction" in text
            or "directions" in text
            or "maps.google" in low
            or "goo.gl/maps" in low
            or "maps.app.goo" in low
        ):
            return "<!-- directions CTA removed in polish preview -->"
        return tag

    html = re.sub(r"<a\b[^>]*>.*?</a>", _kill, html, flags=re.I | re.S)
    return html


def build_claim_help():
    html = (LIVE / "claim-help.html").read_text(encoding="utf-8", errors="replace")
    html = absolutize(html)
    # FORM UNTOUCHED: do not change form module CSS, padding, or order.
    # Only neutralize submit + inject static fields into the SAME target div.
    html = neutralize_forms(html, inject_static_into="hs_form_target_dnd_area-module-4")
    # Add form-lock badge near the CallRail phone (after phone h3) — cosmetic only
    badge = f'<p class="ucs-form-lock-badge" style="text-align:center">Form untouched — layout &amp; fields locked</p>'
    html = html.replace(
        f'<a href="tel:{CALLRAIL_TEL}"',
        f'<a href="tel:{CALLRAIL_TEL}"',
        1,
    )
    # Insert badge after CallRail phone block closing </h3></span></div> pattern once
    phone_pat = r'(855-917-2449</strong></span></a></h3></span></div>)'
    html = re.sub(phone_pat, r"\1\n" + badge, html, count=1)

    schema = faq_schema(FAQ_COMMON, "https://www.ucspa.com/insurance-claim-help")
    html = inject_head(html, schema)
    html = inject_banner(
        html,
        "Claim-help polish: FAQ strip + soft links + frost · <strong>FORM UNTOUCHED</strong> (CallRail phone kept)",
    )
    html = inject_body_class(html, "ucs-claim-help")

    block = (
        faq_html(
            FAQ_COMMON,
            "Questions Before You Start",
            "Soft answers only — no DIY claim coaching. Form and offer above stay exactly as live.",
        )
        + soft_links_html(SOFT_LINKS_CLAIM)
    )
    html = inject_before_footer(html, block)
    html = strip_directions_ctas(html)

    out = ROOT / "insurance-claim-help" / "index.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out, "bytes", out.stat().st_size)


def build_nj():
    html = (LIVE / "pa-nj.html").read_text(encoding="utf-8", errors="replace")
    html = absolutize(html)
    # Brand phone already 855-321 on this page; keep. Neutralize forms.
    # Inject static mock into first lead form target if present
    # Find first hs_form_target_
    m = re.search(r'id="(hs_form_target_[^"]+)"', html)
    target = m.group(1) if m else None
    html = neutralize_forms(html, inject_static_into=target)

    schema = faq_schema(FAQ_NJ, "https://www.ucspa.com/public-adjuster-new-jersey")
    html = inject_head(html, schema)
    html = inject_banner(
        html,
        "NJ PA lander polish (thinner chrome vs NY) · brand phone 855-321-5677 · frost + FAQ + soft links",
    )
    html = inject_body_class(html, "ucs-pa-nj")

    block = (
        faq_html(
            FAQ_NJ,
            "New Jersey Claim Help FAQ",
            "Licensed public adjusters where your NJ property sits. Soft-power answers — free consult anytime.",
        )
        + soft_links_html(SOFT_LINKS_NJ)
    )
    html = inject_before_footer(html, block)
    html = strip_directions_ctas(html)

    # Ensure brand phone display consistency in mid-page CTAs (already brand)
    out = ROOT / "public-adjuster-new-jersey" / "index.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out, "bytes", out.stat().st_size)


def build_water():
    html = (LIVE / "water-claims.html").read_text(encoding="utf-8", errors="replace")
    html = absolutize(html)
    m = re.search(r'id="(hs_form_target_[^"]+)"', html)
    target = m.group(1) if m else None
    html = neutralize_forms(html, inject_static_into=target)

    schema = faq_schema(FAQ_WATER, "https://www.ucspa.com/water-damage-insurance-claims")
    html = inject_head(html, schema)
    html = inject_banner(
        html,
        "Water-damage claims polish · frost FAQ/helping cards · soft links · brand phone 855-321-5677",
    )
    html = inject_body_class(html, "ucs-water")

    # Live already has FAQ section — we still add polished frost FAQ strip + soft links below for consistency.
    # Also frost the existing FAQ-col-Innr / cHelping via .ucs-polish CSS.
    block = (
        faq_html(
            FAQ_WATER,
            "Water Damage Claim FAQ",
            "Soft-power answers on coverage nuance and how a public adjuster helps — form offer unchanged.",
        )
        + soft_links_html(SOFT_LINKS_WATER)
    )
    html = inject_before_footer(html, block)
    html = strip_directions_ctas(html)

    out = ROOT / "water-damage-insurance-claims" / "index.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out, "bytes", out.stat().st_size)


def build_index():
    index = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Form landers polish preview — UCS (NOT LIVE)</title>
<meta name="robots" content="noindex,nofollow" />
<meta name="generator" content="{MARKER}" />
<link rel="stylesheet" href="assets/css/lander-polish.css?v=20261001b" />
<style>
  body {{ margin:0; background:#eef1ea; color:#181c24; font:400 16px/1.55 Lato, system-ui, sans-serif; }}
  .wrap {{ max-width:980px; margin:0 auto; padding:28px 18px 64px; }}
  h1 {{ font:700 28px/1.2 Poppins, system-ui, sans-serif; margin:0 0 8px; }}
  h2 {{ font:700 20px/1.25 Poppins, system-ui, sans-serif; margin:28px 0 10px; }}
  .card {{
    background:rgba(255,255,255,.55); border:1px solid rgba(255,255,255,.7);
    border-radius:18px; padding:18px 20px; margin:12px 0;
    box-shadow:0 0 0 1px rgba(152,204,0,.3), inset 0 1px 0 rgba(255,255,255,.6), 0 12px 28px rgba(0,0,0,.06);
    backdrop-filter:blur(20px) saturate(1.4);
  }}
  .card a {{ color:#181c24; font-weight:600; }}
  .tag {{ display:inline-block; font:600 11px/1 Poppins,system-ui,sans-serif; letter-spacing:.04em; text-transform:uppercase;
    background:rgba(152,204,0,.18); color:#3a5200; border:1px solid rgba(152,204,0,.45); border-radius:999px; padding:4px 10px; margin-right:6px; }}
  .tag.lock {{ background:rgba(24,28,36,.08); color:#181c24; border-color:rgba(24,28,36,.2); }}
  table {{ width:100%; border-collapse:collapse; font-size:14px; }}
  th, td {{ text-align:left; padding:8px 10px; border-bottom:1px solid rgba(24,28,36,.08); vertical-align:top; }}
  th {{ font-size:12px; text-transform:uppercase; letter-spacing:.04em; color:#5a6472; }}
  code {{ background:rgba(24,28,36,.06); padding:1px 5px; border-radius:4px; font-size:12px; }}
  .muted {{ color:#5a6472; }}
</style>
</head>
<body>
<div class="ucs-preview-banner"><strong>PREVIEW ONLY</strong> — Form-fill lander polish pack · <code>{MARKER}</code> · do NOT publish HubSpot</div>
<div class="wrap">
  <h1>Form landers polish — 3 top converters</h1>
  <p class="muted">Source: <code>FORM-LANDINGS-2026.md</code> · fills YTD · PPC-heavy. Soft-power chrome only. No Directions Map CTAs. Box-only HubSpot (this pack never touches CMS).</p>

  <div class="card">
    <span class="tag lock">Form untouched</span>
    <span class="tag">#1 · 115 fills</span>
    <h2 style="margin-top:10px"><a href="insurance-claim-help/">/insurance-claim-help</a></h2>
    <p>Highest fills. <strong>Form layout / fields / position / CallRail 855-917-2449 locked.</strong> Mock adds FAQ frost strip + soft links + FAQPage schema only.</p>
    <p><a href="https://www.ucspa.com/insurance-claim-help">Live ↗</a> · <a href="insurance-claim-help/">Mock preview ↗</a></p>
  </div>

  <div class="card">
    <span class="tag">#5 · 21 fills · thinner chrome</span>
    <h2 style="margin-top:10px"><a href="public-adjuster-new-jersey/">/public-adjuster-new-jersey</a></h2>
    <p>Picked NJ over NY (live HTML ~63.4KB vs NY ~67.7KB — thinner chrome). Brand phone <strong>855-321-5677</strong>. Frost helping cards + FAQ strip + soft links + FAQPage schema.</p>
    <p><a href="https://www.ucspa.com/public-adjuster-new-jersey">Live ↗</a> · <a href="public-adjuster-new-jersey/">Mock preview ↗</a></p>
  </div>

  <div class="card">
    <span class="tag">#6 · 16 fills</span>
    <h2 style="margin-top:10px"><a href="water-damage-insurance-claims/">/water-damage-insurance-claims</a></h2>
    <p>Frost existing FAQ/helping cards + polished FAQ strip + soft links + FAQPage schema. Brand phone 855-321-5677. Offer/form stack unchanged.</p>
    <p><a href="https://www.ucspa.com/water-damage-insurance-claims">Live ↗</a> · <a href="water-damage-insurance-claims/">Mock preview ↗</a></p>
  </div>

  <h2>Side-by-side — what changed vs live</h2>
  <div class="card" style="overflow:auto">
  <table>
    <thead><tr><th>Page</th><th>Visual</th><th>Head-only</th><th>Untouched</th></tr></thead>
    <tbody>
      <tr>
        <td><code>claim-help</code></td>
        <td>FAQ frost strip below phone; soft-links nav; form-lock badge</td>
        <td>FAQPage JSON-LD; robots noindex; preview banner/meta</td>
        <td><strong>Form layout, fields, position, H1/copy, CallRail phone, offer</strong></td>
      </tr>
      <tr>
        <td><code>PA-NJ</code></td>
        <td>Helping-card frost; FAQ frost strip; soft-links; no Directions CTAs</td>
        <td>FAQPage JSON-LD; preview meta</td>
        <td>Hero H1/copy; claim-eval offer; brand phone; IRR steps</td>
      </tr>
      <tr>
        <td><code>water-claims</code></td>
        <td>Frost on live FAQ cols + helping cards; extra FAQ strip; soft-links</td>
        <td>FAQPage JSON-LD; preview meta</td>
        <td>Hero H1/copy; lead form stack; brand phone; do/don’t</td>
      </tr>
    </tbody>
  </table>
  </div>

  <p class="muted">Notes: <a href="NOTES.md">NOTES.md</a> · Marker <code>{MARKER}</code> · GH Pages under <code>joedirect7/ucspa-redesign-mockup-20260926</code>.</p>
</div>
</body>
</html>
'''
    out = ROOT / "index.html"
    out.write_text(index, encoding="utf-8")
    print("wrote", out)


if __name__ == "__main__":
    build_claim_help()
    build_nj()
    build_water()
    build_index()
    print("done")
