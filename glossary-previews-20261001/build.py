#!/usr/bin/env python3
"""Build UCS glossary spoke HTML previews (no HubSpot publish)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
V = "20261001193737"
BRAND_PHONE = "(855) 321-5677"
BRAND_TEL = "tel:18553215677"
CLAIM_HELP = "https://www.ucspa.com/insurance-claim-help"
FOR_AGENTS = "https://www.ucspa.com/for-agents"
FAQ = "https://www.ucspa.com/faq"
SETTLEMENTS = "https://www.ucspa.com/recent-settlements"
SLOGAN = "Your insurance has an adjuster, so should you."

PAGES = [
  {
    "slug": "what-is-a-public-adjuster",
    "title": "What Is a Public Adjuster? | United Claims Specialists",
    "h1": "What Is a Public Adjuster?",
    "meta": "A public adjuster is a state-licensed professional who represents you—the policyholder—on a property insurance claim. Learn the definition, when it matters, and how UCS helps.",
    "canonical_future": "https://www.ucspa.com/what-is-a-public-adjuster",
    "hero_img": "https://www.ucspa.com/hubfs/flood%20damage.jpg",
    "answer_first": (
      "A public adjuster is a state-licensed professional who represents "
      "<strong>you—the policyholder</strong>—on a property insurance claim, not the insurance company. "
      "Typical work includes inspecting and documenting damage, preparing a supported estimate package, "
      "and communicating with the carrier in claim language so you are not carrying the file alone."
    ),
    "schema_def": "A public adjuster is a state-licensed professional who represents the policyholder on a property insurance claim. They inspect and document damage, prepare a supported estimate package, and communicate with the insurer on the policyholder's behalf.",
    "body_html": """
<section class="section-card ucs-glass" id="definition">
  <h2>Clear definition</h2>
  <p>Insurance claims involve several kinds of adjusters. A <strong>staff adjuster</strong> works for the insurer. An <strong>independent adjuster</strong> is typically hired by the insurer or a third-party administrator. A <strong>public adjuster</strong> is licensed to represent the policyholder on the property claim file itself.</p>
  <p>Same loss file, different side of the table. United Claims Specialists (UCS) is on <strong>your</strong> side of the file—documenting scope, explaining coverage issues in plain language, and handling carrier communication within license rules.</p>
  <p>This is not the same job as your insurance agent or broker (who helps place and service the policy), and it is not the same as a contractor (who repairs and bids physical work). Claim advocacy is a licensed role in most states.</p>
</section>

<section class="section-card ucs-glass" id="when-it-matters">
  <h2>When it matters for a property claim</h2>
  <p>Hiring often helps when the loss is large or complex, the first offer feels thin next to real repair estimates, documentation and calls would consume hours you do not have, or you want claim advocacy without jumping straight to litigation. Small, clear losses where a trusted local bid already matches the carrier number can still move forward without counsel.</p>
  <div class="when-grid">
    <div class="when-tile"><strong>Large or complex losses</strong><span>Storm, water, fire, commercial, or multi-building scopes that need careful documentation.</span></div>
    <div class="when-tile"><strong>Thin first scope</strong><span>Missed damage, depreciation gaps, or contractor bids that diverge from the carrier sheet.</span></div>
    <div class="when-tile"><strong>Time &amp; claim language</strong><span>Someone in your corner who already negotiates files like yours—so you are not alone on the calls.</span></div>
    <div class="when-tile"><strong>Same-loss second look</strong><span>Underpayment or incomplete scope on the original date of loss—often addressed with a supplement path.</span></div>
  </div>
  <p style="margin-top:14px">Property claims and policies are nuanced and complex. UCS recommends involving a licensed public adjuster early on larger files so the record starts clean.</p>
</section>

<section class="section-card ucs-glass" id="what-ucs-does">
  <h2>What United Claims Specialists does</h2>
  <ul>
    <li>Inspect and document the loss with photos, measurements, and claim-ready notes</li>
    <li>Prepare a supported estimate package aligned to the policy and the damage</li>
    <li>Communicate with the carrier on your behalf in claim language</li>
    <li>Help at new-claim, already-filed / underpaid, or incomplete prior settlement stages for the <em>same</em> loss</li>
  </ul>
  <p>Fees are contingency-aligned where allowed—UCS gets paid when you get paid—with disclosure under applicable state rules. No outcome is guaranteed. Ask during a free consult what applies where your property sits.</p>
</section>
""",
    "related": [
      ("../what-is-an-insurance-claim-supplement/", "What is an insurance claim supplement?", "Same-loss underpayment / thin scope"),
      ("../what-is-an-appraisal-clause/", "What is an appraisal clause?", "Amount-of-loss disagreements"),
      (FAQ, "Public adjuster FAQ", "Licensing, ALE, matching &amp; more"),
      (SETTLEMENTS, "Recent settlements", "Real property claim outcomes"),
      (FOR_AGENTS, "For agents / AI", "Entity facts for partners"),
    ],
  },
  {
    "slug": "what-is-an-insurance-claim-supplement",
    "title": "What Is an Insurance Claim Supplement? | United Claims Specialists",
    "h1": "What Is an Insurance Claim Supplement?",
    "meta": "An insurance claim supplement adds documentation and scope on the same date of loss when the first estimate looks thin, incomplete, or underpaid. Soft-power guidance from UCS—no DIY coaching.",
    "canonical_future": "https://www.ucspa.com/what-is-an-insurance-claim-supplement",
    "hero_img": "https://www.ucspa.com/hubfs/water%20damage.jpg",
    "answer_first": (
      "An <strong>insurance claim supplement</strong> is additional documentation and scope submitted on the "
      "<strong>same date of loss</strong> when the first estimate looks thin, incomplete, or underpaid relative to real repair needs. "
      "It is not a brand-new claim—it is a second look at what the original file missed, with a licensed public adjuster preparing the package."
    ),
    "schema_def": "An insurance claim supplement is additional documentation and scope submitted on the same date of loss when the first estimate is thin, incomplete, or underpaid relative to repair needs. It updates the original claim file rather than opening a new claim.",
    "body_html": """
<section class="section-card ucs-glass" id="definition">
  <h2>Clear definition</h2>
  <p>After a property loss, the carrier’s first estimate is often a <strong>starting scope</strong>—built from a short inspection—not a complete repair budget. A supplement adds supported line items, photos, and explanations for damage or costs that belong to that <strong>same loss</strong> but were not fully captured the first time.</p>
  <p>Common drivers: hidden water paths found during demolition, roofing layers missed on a walk, code-required upgrades, matching issues, ALE documentation gaps, or contractor bids that materially diverge from the carrier sheet.</p>
  <p><strong>Soft-power framing:</strong> UCS talks about reopen and supplement in terms of <em>underpayment</em>, <em>thin first scope</em>, and <em>missed damage</em>—not a denial thesis. The goal is a complete, supported file for the loss you already have.</p>
</section>

<section class="section-card ucs-glass" id="when-it-matters">
  <h2>When it matters for a property claim</h2>
  <p>A second look often makes sense when repair reality outruns the first number, when new damage related to the original event surfaces as work opens up, or when depreciation and scope assumptions leave you short of a trustworthy bid.</p>
  <div class="when-grid">
    <div class="when-tile"><strong>Underpayment signal</strong><span>Trusted contractor numbers sit well above the carrier estimate for the same damage.</span></div>
    <div class="when-tile"><strong>Missed / hidden damage</strong><span>Moisture, structural, or secondary damage that was not visible on day one.</span></div>
    <div class="when-tile"><strong>Incomplete first scope</strong><span>Line items, quantities, or code items left out of the opening sheet.</span></div>
    <div class="when-tile"><strong>Same date of loss</strong><span>Supplement stays tied to the original event—not a separate occurrence.</span></div>
  </div>
</section>

<section class="section-card ucs-glass" id="no-diy">
  <h2>Why not DIY the supplement?</h2>
  <p>Property claims and policies are nuanced and complex. Homeowner letter templates, reason-code homework, and “write the carrier yourself” checklists can misspeak coverage, waive options, or leave the file thinner than it should be.</p>
  <p>United Claims Specialists steers you to a <strong>licensed public adjuster</strong> who re-inspects, documents, prepares a supported supplement package, and handles carrier communication within license rules—the craft that comes from decades of files like yours.</p>
  <p>We do not coach DIY claim or supplement steps on this page. If a second look may be warranted, start a free consult and let UCS evaluate the file with you.</p>
</section>
""",
    "related": [
      ("../what-is-a-public-adjuster/", "What is a public adjuster?", "Who prepares a supported package"),
      ("../what-is-an-appraisal-clause/", "What is an appraisal clause?", "When amount-of-loss still disagrees"),
      ("https://www.ucspa.com/blog/how-do-i-reopen-an-insurance-claim", "How do I reopen an insurance claim?", "Soft reopen / supplement path"),
      (FAQ, "Public adjuster FAQ", "First offers, ALE &amp; more"),
      (SETTLEMENTS, "Recent settlements", "Outcomes on property files"),
    ],
  },
  {
    "slug": "what-is-an-appraisal-clause",
    "title": "What Is an Appraisal Clause in Insurance? | United Claims Specialists",
    "h1": "What Is an Appraisal Clause (Insurance)?",
    "meta": "An appraisal clause is a policy provision that can resolve disagreements about the amount of loss—not every coverage dispute—via appraisers and often an umpire. UCS explains when it matters.",
    "canonical_future": "https://www.ucspa.com/what-is-an-appraisal-clause",
    "hero_img": "https://www.ucspa.com/hubfs/fire%20damage.jpg",
    "answer_first": (
      "An <strong>appraisal clause</strong> is a provision in many property insurance policies that can resolve disagreements about the "
      "<strong>amount of loss</strong>—not every coverage dispute—through a contractual process with appraisers and often an umpire. "
      "It is separate from litigation and has notice, selection, and timeline rules that vary by policy and state."
    ),
    "schema_def": "An appraisal clause is a property insurance policy provision that can resolve disagreements about the amount of loss through a contractual process involving appraisers and often an umpire. It typically does not decide every coverage dispute and is separate from litigation.",
    "body_html": """
<section class="section-card ucs-glass" id="definition">
  <h2>Clear definition</h2>
  <p>When you and the carrier agree that a loss is covered but disagree on <strong>how much</strong> it should cost to repair or replace, many policies point to appraisal. Each side typically names an appraiser; if those appraisers cannot agree, they may select an <strong>umpire</strong>. The resulting award often addresses the amount of loss under the policy’s rules.</p>
  <p>Appraisal is <strong>not</strong> a catch-all for every claim disagreement. Coverage questions (what the policy includes or excludes), liability disputes, and some legal issues may sit outside appraisal—exact boundaries depend on the policy wording and state law.</p>
  <p>United Claims Specialists can explain whether appraisal appears to be in play on your file during a free consult, and help document the amount of loss if it is. This page is educational—not legal advice.</p>
</section>

<section class="section-card ucs-glass" id="when-it-matters">
  <h2>When it matters for a property claim</h2>
  <p>Appraisal tends to matter after documentation and negotiation have clarified the gap on dollars—and both sides still disagree on the number—not as a first move before the file is fully scoped.</p>
  <div class="when-grid">
    <div class="when-tile"><strong>Amount-of-loss gap</strong><span>Coverage is clearer than the dollars; estimates still diverge widely.</span></div>
    <div class="when-tile"><strong>Policy has the clause</strong><span>Not every form is identical—read the declarations and appraisal wording.</span></div>
    <div class="when-tile"><strong>Notice &amp; timelines</strong><span>Appraisal has selection and deadline rules worth getting right.</span></div>
    <div class="when-tile"><strong>Documented support</strong><span>Strong photos, estimates, and scopes make appraisal more coherent.</span></div>
  </div>
  <p style="margin-top:14px">Before appraisal talk, many files still benefit from a licensed public adjuster’s inspection and a supported estimate—or a <a href="../what-is-an-insurance-claim-supplement/">supplement</a> if the first scope was thin. UCS appraisal-related services focus on documenting amount of loss within license rules; see also <a href="https://www.ucspa.com/appraisal-services">Appraisal Services</a>.</p>
</section>

<section class="section-card ucs-glass" id="soft-path">
  <h2>Soft path with UCS</h2>
  <p>We do not push litigation hype or “fight the carrier” framing. Soft-power means educating when appraisal may be relevant, confirming licensing for your property’s state, and inviting a free claim consult so a licensed public adjuster can review your documents with you.</p>
  <p>Claim help is available <strong>24/7</strong>—call or start online anytime. Bring what you have (declarations page, estimates, photos, bids); missing pieces are okay.</p>
</section>
""",
    "related": [
      ("../what-is-a-public-adjuster/", "What is a public adjuster?", "Advocacy on the claim file"),
      ("../what-is-an-insurance-claim-supplement/", "What is a claim supplement?", "Thin first scope / underpayment"),
      ("https://www.ucspa.com/appraisal-services", "Appraisal services", "UCS amount-of-loss support"),
      (FAQ, "Public adjuster FAQ", "Appraisal Q&amp;A on FAQ"),
      (SETTLEMENTS, "Recent settlements", "Property claim outcomes"),
    ],
  },
]


CHROME_NAV = f"""
<ul class="chrome-nav" aria-label="Preview nav">
  <li><a href="../index.html">Glossary hub</a></li>
  <li><a href="{FAQ}">FAQ</a></li>
  <li><a href="{SETTLEMENTS}">Settlements</a></li>
  <li><a href="{FOR_AGENTS}">For agents</a></li>
</ul>
"""


def css_href(depth: int) -> str:
    return f"https://cdn.jsdelivr.net/gh/joedirect7/ucspa-redesign-mockup-20260926@main/glossary-previews-20261001/assets/css/glossary-frost.css?v={V}"


def page_html(p: dict, depth: int = 1) -> str:
    rel_css = css_href(depth)
    hub = "../index.html" if depth else "index.html"
    related_links = "\n".join(
        f'<a href="{href}">{label}<small>{sub}</small></a>'
        for href, label, sub in p["related"]
    )
    schema = f"""{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "DefinedTerm",
      "name": {p["h1"]!r},
      "description": {p["schema_def"]!r},
      "inDefinedTermSet": "https://www.ucspa.com/"
    }},
    {{
      "@type": "WebPage",
      "name": {p["h1"]!r},
      "description": {p["meta"]!r},
      "isPartOf": {{"@type": "WebSite", "name": "United Claims Specialists", "url": "https://www.ucspa.com/"}},
      "about": {{"@type": "Organization", "name": "United Claims Specialists", "telephone": "+1-855-321-5677", "url": "https://www.ucspa.com/"}}
    }},
    {{
      "@type": "FAQPage",
      "mainEntity": [{{
        "@type": "Question",
        "name": {p["h1"]!r},
        "acceptedAnswer": {{"@type": "Answer", "text": {p["schema_def"]!r}}}
      }}]
    }}
  ]
}}"""

    # relative paths for sibling glossary
    if depth == 1:
        chrome_nav = f"""
<ul class="chrome-nav" aria-label="Preview nav">
  <li><a href="{hub}">Glossary hub</a></li>
  <li><a href="{FAQ}">FAQ</a></li>
  <li><a href="{SETTLEMENTS}">Settlements</a></li>
  <li><a href="{FOR_AGENTS}">For agents</a></li>
</ul>"""
        brand_href = hub
    else:
        chrome_nav = CHROME_NAV
        brand_href = "index.html"

    return f"""<!DOCTYPE html>
<html class="no-js" lang="en">
<head>
<meta charset="utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{p["title"]}</title>
<meta name="description" content="{p["meta"]}" />
<meta name="robots" content="noindex,nofollow" />
<meta name="generator" content="glossary-previews-20261001 — PREVIEW ONLY, not HubSpot published" />
<link rel="canonical" href="{p["canonical_future"]}" />
<link rel="shortcut icon" href="https://www.ucspa.com/hubfs/new%20logo%20(5)-1.jpg" />
<link rel="stylesheet" href="https://7052064.fs1.hubspotusercontent-na1.net/hubfs/7052064/hub_generated/template_assets/DEFAULT_ASSET/1790670504241/template_layout.min.css" />
<link rel="stylesheet" href="https://www.ucspa.com/hubfs/hub_generated/template_assets/1/52794869832/1790819786203/template_theme-overrides.min.css" />
<link rel="stylesheet" href="{rel_css}" />
<style>
  .glossary-hero::before {{ background-image: url('{p["hero_img"]}'); }}
</style>
<script type="application/ld+json">
{schema}
</script>
</head>
<body class="glossary-preview">
<div class="preview-banner" role="status">
  <strong>PREVIEW ONLY</strong> — UCS glossary spoke · A True frost chrome ·
  <strong>not published</strong> to HubSpot / live ucspa.com ·
  <a href="{hub}">Hub</a>
</div>

<header class="site-chrome" aria-label="Site chrome preview">
  <div class="site-chrome__inner">
    <a class="brand" href="{brand_href}">
      <img src="https://www.ucspa.com/hubfs/new%20logo%20(5)-1.jpg" alt="" width="48" height="22" />
      United Claims Specialists
      <span>Public Adjusters</span>
    </a>
    {chrome_nav}
    <div class="chrome-cta">
      <a class="btn-ghost" href="{BRAND_TEL}">{BRAND_PHONE}</a>
      <a class="btn-lime" href="{CLAIM_HELP}">Free Claim Consult</a>
    </div>
  </div>
</header>

<main id="main">
  <section class="glossary-hero" aria-label="Glossary definition">
    <div class="glossary-hero__inner">
      <ol class="crumbs">
        <li><a href="https://www.ucspa.com/">Home</a></li>
        <li><a href="{hub}">Glossary preview</a></li>
        <li><span>{p["h1"]}</span></li>
      </ol>
      <div class="hero-panel ucs-glass">
        <h1>{p["h1"]}</h1>
        <p class="answer-first">{p["answer_first"]}</p>
        <div class="hero-actions">
          <a class="btn-lime" href="{CLAIM_HELP}">Start free claim consult</a>
          <a class="btn-ghost" href="{BRAND_TEL}">Call {BRAND_PHONE}</a>
        </div>
      </div>
    </div>
  </section>

  <div class="glossary-main">
    {p["body_html"]}

    <section class="cta-frost ucs-glass" id="soft-cta" aria-label="Soft call to action">
      <p class="slogan">{SLOGAN}</p>
      <h2>Talk with a licensed public adjuster</h2>
      <p>United Claims Specialists helps homeowners and commercial owners document property damage, prepare supported claim packages, and communicate with the carrier—without DIY claim coaching. Claim help is available <strong>24/7</strong>.</p>
      <div class="hero-actions">
        <a class="btn-lime" href="{CLAIM_HELP}">Insurance Claim Help</a>
        <a class="btn-ghost" href="{BRAND_TEL}">Call {BRAND_PHONE}</a>
        <a class="btn-outline" href="{FOR_AGENTS}">For agents</a>
      </div>
      <p class="cta-meta">Brand line: <a href="{BRAND_TEL}">{BRAND_PHONE}</a> (855-321-LOSS) · Email <a href="mailto:claims@ucspa.com">claims@ucspa.com</a> · Soft CTA → <a href="{CLAIM_HELP}">/insurance-claim-help</a></p>
    </section>

    <section class="section-card ucs-glass" id="related">
      <h2>Related reading</h2>
      <div class="related">
        {related_links}
      </div>
    </section>
  </div>
</main>

<footer class="site-foot">
  <div class="site-foot__inner">
    <div class="foot-row">
      <div>
        <h3>Claim Help</h3>
        <p>Available 24/7 — call or chat anytime</p>
        <p><a href="{BRAND_TEL}">{BRAND_PHONE}</a> · <a href="{CLAIM_HELP}">ucspa.com/insurance-claim-help</a></p>
      </div>
      <div>
        <h3>United Claims Specialists</h3>
        <p>Licensed public adjusters · FL LIC# W806268 · Licensed in multiple states</p>
        <p>{SLOGAN}</p>
      </div>
    </div>
    <p class="foot-legal">© 2009–2026 United Claims Specialists. Preview mock only — not a live site page. No Joe Suskind byline. Soft-power CTAs only.</p>
  </div>
</footer>
</body>
</html>
"""


def hub_html() -> str:
    cards = []
    for p in PAGES:
        cards.append(
            f"""<a class="related" style="display:block" href="{p['slug']}/">
  <div class="section-card ucs-glass" style="margin:0">
    <h2 style="font-size:1.15rem;margin:0 0 8px">{p['h1']}</h2>
    <p style="margin:0;font-size:14px;color:#5a6270">{p['schema_def'][:160]}…</p>
    <p style="margin:12px 0 0;font-weight:600;color:#5f8600;font-size:13px">Open clickable preview →</p>
  </div>
</a>"""
        )
    cards_html = "\n".join(f'<div style="margin:14px 0">{c}</div>' for c in cards)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>UCS Glossary Spoke Previews (2026-10-01) | PREVIEW ONLY</title>
<meta name="robots" content="noindex,nofollow" />
<meta name="generator" content="glossary-previews-20261001" />
<link rel="shortcut icon" href="https://www.ucspa.com/hubfs/new%20logo%20(5)-1.jpg" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/joedirect7/ucspa-redesign-mockup-20260926@main/glossary-previews-20261001/assets/css/glossary-frost.css?v={V}" />
</head>
<body class="glossary-preview">
<div class="preview-banner"><strong>PREVIEW ONLY</strong> — three soft-power glossary spokes · no HubSpot publish · no live site edits</div>
<header class="site-chrome">
  <div class="site-chrome__inner">
    <a class="brand" href="index.html">
      <img src="https://www.ucspa.com/hubfs/new%20logo%20(5)-1.jpg" alt="" width="48" height="22" />
      United Claims Specialists
      <span>Glossary previews</span>
    </a>
    <div class="chrome-cta">
      <a class="btn-ghost" href="{BRAND_TEL}">{BRAND_PHONE}</a>
      <a class="btn-lime" href="{CLAIM_HELP}">Claim Help</a>
    </div>
  </div>
</header>
<main class="glossary-main" style="padding-top:28px">
  <div class="hero-panel ucs-glass">
    <h1 style="margin:0 0 10px;font-size:clamp(1.5rem,3vw,2.1rem)">Glossary spoke previews</h1>
    <p class="answer-first" style="margin-bottom:8px">Clickable https previews for Joe — soft-power definitions only. Slogan lock: <em>{SLOGAN}</em></p>
    <p style="margin:0;font-size:13px;color:#5a6270">Work path: <code>glossary-previews-20261001/</code> · Scores in SCORECARDS.md · All ≥8 before Joe review</p>
  </div>
  {cards_html}
  <section class="section-card ucs-glass">
    <h2>Locks honored</h2>
    <ul>
      <li>Soft-power CTAs; reopen = supplement/underpayment framing (no denial thesis)</li>
      <li>No DIY claim/supplement coaching — steer to licensed public adjuster</li>
      <li>Brand United Claims Specialists; no Joe Suskind byline</li>
      <li>Brand phone {BRAND_PHONE}; CallRail only on live claim-help path</li>
      <li>Claim help available 24/7</li>
      <li>A True frost nav/content chrome · Preview first — never ship without Joe OK</li>
    </ul>
  </section>
</main>
<footer class="site-foot"><div class="site-foot__inner">
  <p>Claim Help available 24/7 · <a href="{BRAND_TEL}">{BRAND_PHONE}</a> · <a href="{CLAIM_HELP}">/insurance-claim-help</a></p>
  <p class="foot-legal">© 2009–2026 United Claims Specialists · PREVIEW ONLY</p>
</div></footer>
</body>
</html>
"""


def main():
    (ROOT / "index.html").write_text(hub_html(), encoding="utf-8")
    for p in PAGES:
        out = ROOT / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page_html(p, depth=1), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
    print("wrote index.html")


if __name__ == "__main__":
    main()
