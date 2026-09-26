"""Shared header/footer/nav for UCS 2026 mockup. Exact live nav labels/order."""
from pathlib import Path
import html as htmlmod

NAV = {
  "Storm Damage": {
    "href": "storm-damage/",
    "children": [
      ("Hurricane Damage", "hurricane-damage/"),
      ("Tornado Damage", "tornado-damage-insurance-claims/"),
      ("Hail Damage", "hail-damage/"),
      ("Wind Damage", "wind-damage-insurance-claims/"),
      ("Flood Damage", "flood-damage/"),
    ],
  },
  "Property Damage": {
    "href": "property-damage-insurance-claims/",
    "children": [
      ("Roof Leak Damage", "roof-leak/"),
      ("Water Damage", "water-damage/"),
      ("Mold Damage", "mold-damage-insurance-claims/"),
      ("Fire Damage", "fire-damage-insurance-claims/"),
      ("Wildfire Damage", "wildfire-damage/"),
      ("Theft & Vandalism Damage", "theft-vandalism-damage/"),
      ("Flood Damage", "flood-damage/"),
      ("Accidental Damage", "accidental-damage/"),
      ("Income Loss", "income-loss/"),
    ],
  },
  "Residential Claims": {"href": "residential-public-adjuster/", "children": []},
  "Commercial Claims": {"href": "commercial-public-adjuster/", "children": []},
  "Denied Claims": {"href": "denied-claims/", "children": []},
  "Contractor Claim Services": {"href": "contractor-claim-services/", "children": []},
  "About Us": {"href": "about-us/", "children": []},
}

LOCATIONS = [
  ("Florida", "public-adjuster-florida/"),
  ("Los Angeles", "public-adjuster-los-angeles/"),
  ("Texas", "public-adjuster-texas/"),
  ("Louisiana", "public-adjuster-louisiana/"),
  ("New York", "public-adjuster-new-york/"),
  ("New Jersey", "public-adjuster-new-jersey/"),
  ("Georgia", "public-adjuster-georgia/"),
  ("Pennsylvania", "public-adjuster-pennsylvania/"),
]

PHONE_DISPLAY = "855-321-LOSS"
PHONE_TEL = "8553215677"
PHONE_ALT = "855-917-2449"
PHONE_ALT_TEL = "8559172449"
EMAIL = "claims@ucspa.com"
LIC = "FLORIDA LIC# W806268"

def esc(s):
    return htmlmod.escape(str(s), quote=True)

def depth_prefix(rel_path: str) -> str:
    p = (rel_path or "").strip("/")
    if not p or p == "index.html":
        return ""
    parts = Path(p).parts
    dirs = len(parts) - 1 if parts[-1].endswith(".html") else len(parts)
    return "../" * dirs

def header_html(prefix: str) -> str:
    items = []
    for label, meta in NAV.items():
        href = prefix + meta["href"]
        kids = meta.get("children") or []
        if kids:
            wide = " dropdown--wide" if len(kids) > 5 else ""
            links = "\n".join(f'<li><a href="{prefix}{h}">{esc(t)}</a></li>' for t, h in kids)
            items.append(f'''<li>
              <button type="button" aria-haspopup="true">{esc(label)}
                <svg class="chev" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
              </button>
              <ul class="dropdown{wide}">{links}</ul>
            </li>''')
        else:
            items.append(f'<li><a href="{href}">{esc(label)}</a></li>')
    loc_links = "\n".join(f'<li><a href="{prefix}{h}">{esc(t)}</a></li>' for t, h in LOCATIONS)
    items.append(f'''<li>
      <button type="button" aria-haspopup="true">Locations
        <svg class="chev" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
      </button>
      <ul class="dropdown">{loc_links}<li><a href="{prefix}locations/">All Locations</a></li></ul>
    </li>''')
    items.append(f'<li><a href="{prefix}contact-us/">Contact Us</a></li>')

    mobile = []
    for label, meta in NAV.items():
        href = prefix + meta["href"]
        kids = meta.get("children") or []
        if kids:
            sub = "".join(f'<a href="{prefix}{h}">{esc(t)}</a>' for t, h in kids)
            mobile.append(f'<details><summary>{esc(label)}</summary>{sub}<a href="{href}">Overview</a></details>')
        else:
            mobile.append(f'<a href="{href}">{esc(label)}</a>')
    mobile.append('<details><summary>Locations</summary>' + "".join(f'<a href="{prefix}{h}">{esc(t)}</a>' for t,h in LOCATIONS) + f'<a href="{prefix}locations/">All Locations</a></details>')
    mobile.append(f'<a href="{prefix}contact-us/">Contact Us</a>')
    mobile.append(f'<a href="{prefix}appraisal-services/">Appraisal Services</a>')
    mobile.append(f'<a href="{prefix}blog/">Resources</a>')

    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="header-top">
    <div class="container">
      <a class="header-top__phone" href="tel:{PHONE_TEL}">📞 {PHONE_DISPLAY} (5677)</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
  <div class="container header-main">
    <a class="logo" href="{prefix}index.html">
      <span class="logo__mark">UCS</span>
      <span class="logo__text">United Claims Specialists<span>Public Adjusters</span></span>
    </a>
    <ul class="nav-desktop">{"".join(items)}</ul>
    <div class="header-cta">
      <a class="btn btn--outline btn--sm" href="tel:{PHONE_TEL}">Call Now</a>
      <a class="btn btn--primary btn--sm" href="{prefix}insurance-claim-help/">Free Inspection</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu"><span></span></button>
    </div>
  </div>
  <nav class="nav-mobile" id="mobile-nav" aria-label="Mobile">
    {"".join(mobile)}
    <div class="nav-mobile__cta">
      <a class="btn btn--primary btn--block" href="{prefix}insurance-claim-help/">Claim Free Inspection</a>
      <a class="btn btn--outline btn--block" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </nav>
</header>'''

def footer_html(prefix: str) -> str:
    menu = "\n".join(f'<li><a href="{prefix}{meta["href"]}">{esc(label)}</a></li>' for label, meta in NAV.items())
    locs = "\n".join(f'<li><a href="{prefix}{h}">{esc(t)}</a></li>' for t, h in LOCATIONS)
    return f'''<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <a class="logo" href="{prefix}index.html" style="color:#fff">
        <span class="logo__mark">UCS</span>
        <span class="logo__text" style="color:#fff">United Claims Specialists<span style="color:rgba(255,255,255,.55)">Public Adjusters</span></span>
      </a>
      <p>We help homeowners, building owners, property managers and contractors file property damage claims, get higher payouts, and eliminate the headaches of dealing with insurance claims. Don't file another claim without us!</p>
      <span class="lic-badge">{LIC}</span>
    </div>
    <div>
      <h4>Menu</h4>
      <ul>{menu}</ul>
    </div>
    <div>
      <h4>Locations</h4>
      <ul>{locs}</ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul class="footer-contact">
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY} (5677)</a></li>
        <li>Mon–Fri: 9:00am–5:00pm</li>
      </ul>
      <p style="margin-top:1rem"><a class="btn btn--primary btn--sm" href="{prefix}insurance-claim-help/">Schedule Free Inspection</a></p>
      <div class="footer-social" style="margin-top:1.25rem">
        <a href="https://www.facebook.com/UnitedClaimsSpecialistsFL" aria-label="Facebook" rel="noopener" target="_blank">f</a>
        <a href="https://twitter.com/ucs_pa" aria-label="X / Twitter" rel="noopener" target="_blank">𝕏</a>
        <a href="https://www.linkedin.com/company/united-claims-specialists/" aria-label="LinkedIn" rel="noopener" target="_blank">in</a>
      </div>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>© 2009–2026 United Claims Specialists. All Rights Reserved.</p>
    <p>
      <a href="{prefix}privacy-policy/">Privacy policy</a> ·
      <a href="{prefix}terms-and-conditions/">Terms &amp; conditions</a>
    </p>
  </div>
</footer>
<div class="mobile-cta-bar" aria-label="Quick actions">
  <a class="btn btn--outline btn--sm" style="flex:1" href="tel:{PHONE_TEL}">Call</a>
  <a class="btn btn--primary btn--sm" style="flex:1" href="{prefix}insurance-claim-help/">Free Inspection</a>
</div>
<script src="{prefix}assets/js/nav.js" defer></script>'''

def page_shell(title, description, rel_path, body):
    prefix = depth_prefix(rel_path)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="robots" content="noindex, nofollow">
  <link rel="stylesheet" href="{prefix}assets/css/design-system.css">
  <link rel="stylesheet" href="{prefix}assets/css/extras.css">
</head>
<body>
{header_html(prefix)}
<main id="main">
{body}
</main>
{footer_html(prefix)}
</body>
</html>
'''

def write_page(base: Path, rel_dir: str, filename: str, title: str, description: str, body: str):
    """Write page at base/rel_dir/filename (usually index.html)."""
    out_dir = base / rel_dir if rel_dir else base
    out_dir.mkdir(parents=True, exist_ok=True)
    rel_path = f"{rel_dir}/{filename}" if rel_dir else filename
    html = page_shell(title, description, rel_path, body)
    (out_dir / filename).write_text(html, encoding="utf-8")
    return rel_path

def trust_strip():
    return '''<section class="trust-strip" aria-label="Trust signals">
  <div class="container">
    <ul class="trust-strip__grid">
      <li><span class="trust-strip__icon">✓</span> Licensed public adjusters</li>
      <li><span class="trust-strip__icon">✓</span> FL Lic # W806268</li>
      <li><span class="trust-strip__icon">✓</span> Multiple states served</li>
      <li><span class="trust-strip__icon">✓</span> No fee unless you get paid</li>
      <li><span class="trust-strip__icon">✓</span> Free inspection</li>
    </ul>
  </div>
</section>'''

def cta_band(prefix, headline="Claim your free inspection", sub="Whether you are at the beginning of filing a claim, or if you have already filed your claim—WE CAN HELP!"):
    return f'''<section class="cta-band">
  <div class="container">
    <div>
      <h2>{esc(headline)}</h2>
      <p>{esc(sub)}</p>
    </div>
    <div class="cta-band__actions">
      <a class="btn btn--primary btn--lg" href="{prefix}insurance-claim-help/">Free Inspection</a>
      <a class="btn btn--secondary btn--lg" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>'''
