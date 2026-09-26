#!/usr/bin/env python3
"""Wire premium claim imagery + motion across UCS redesign mockup. Copy unchanged."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("/workspace/ucs-seo/ucspa-redesign-mockup-20260926")

# slug keyword → (rel_from_assets_root, alt)
SLUG_IMAGE = [
    ("water", "img/damage/water-interior.png", "Water damage interior after flooding"),
    ("mold", "img/damage/water-interior.png", "Water and mold damage interior"),
    ("flood", "img/scenes/incident.jpg", "Flood and storm incident damage"),
    ("fire", "img/scenes/fire.jpg", "Fire damage to property"),
    ("wildfire", "img/scenes/fire.jpg", "Wildfire damage to property"),
    ("roof", "img/damage/hail-roof.png", "Hail-damaged roof needing repair"),
    ("hail", "img/damage/hail-roof.png", "Hail damage on roof shingles"),
    ("hurricane", "img/damage/hurricane-palms.png", "Hurricane storm damage with palm trees"),
    ("tornado", "img/scenes/wind.jpg", "Wind and tornado storm damage"),
    ("wind", "img/scenes/wind.jpg", "Wind storm property damage"),
    ("storm", "img/scenes/wind.jpg", "Storm damage to residential property"),
    ("denied", "img/scenes/settle.jpg", "Successful insurance claim settlement"),
    ("about", "img/scenes/ops.jpg", "United Claims Specialists operations"),
    ("commercial", "img/scenes/ops.jpg", "Commercial property claims operations"),
    ("residential", "img/scenes/inspect.jpg", "Residential property claim inspection"),
    ("income", "img/scenes/ops.jpg", "Business income loss claim support"),
    ("contractor", "img/scenes/call.jpg", "Contractor claim services consultation"),
    ("appraisal", "img/scenes/inspect.jpg", "Insurance appraisal inspection"),
    ("theft", "img/scenes/incident.jpg", "Theft and vandalism property damage"),
    ("vandalism", "img/scenes/incident.jpg", "Vandalism property damage"),
    ("accidental", "img/scenes/incident.jpg", "Accidental property damage"),
    ("contact", "img/scenes/call.jpg", "Contact United Claims Specialists"),
    ("locations", "img/brand/ops-center.jpg", "UCS claims operations center"),
    ("public-adjuster", "img/scenes/inspect.jpg", "Public adjuster property inspection"),
    ("insurance-claim-help", "img/scenes/call.jpg", "Insurance claim help consultation"),
    ("property-damage", "img/scenes/inspect.jpg", "Property damage insurance claim"),
    ("blog", "img/damage/blog-hero.png", "UCS blog and claim resources"),
    ("privacy", "img/brand/ops-center.jpg", "United Claims Specialists"),
    ("terms", "img/brand/ops-center.jpg", "United Claims Specialists"),
]

DEFAULT_IMG = ("img/scenes/inspect.jpg", "Property damage claim inspection")

CLAIM_TYPE_MEDIA = [
    ("Storm Damage", "img/scenes/wind.jpg", "Storm and wind damage to a home"),
    ("Fire Damage", "img/scenes/fire.jpg", "Fire damage to residential property"),
    ("Water Damage", "img/damage/water-interior.png", "Interior water damage"),
    ("Roof Damage", "img/damage/hail-roof.png", "Hail-damaged roof"),
    ("Income Loss", "img/scenes/ops.jpg", "Commercial operations and income loss claims"),
    ("Flood Damage", "img/scenes/incident.jpg", "Flood and storm incident damage"),
]


def depth_prefix(rel: Path) -> str:
    # rel is path relative to ROOT, e.g. index.html or storm-damage/index.html
    parts = rel.parts
    if len(parts) == 1:
        return ""
    # number of directories
    return "../" * (len(parts) - 1)


def pick_image(slug: str) -> tuple[str, str]:
    s = slug.lower().strip("/")
    for key, path, alt in SLUG_IMAGE:
        if key in s:
            return path, alt
    return DEFAULT_IMG


def add_motion_script(html: str, prefix: str) -> str:
    motion = f'<script src="{prefix}assets/js/motion.js" defer></script>'
    if "assets/js/motion.js" in html:
        return html
    # Insert after nav.js
    html2, n = re.subn(
        r'(<script src="[^"]*assets/js/nav\.js" defer></script>)',
        rf"\1\n{motion}",
        html,
        count=1,
    )
    if n:
        return html2
    # Fallback before </body>
    if "</body>" in html:
        return html.replace("</body>", f"{motion}\n</body>", 1)
    return html


def update_index(html: str) -> str:
    # Hero → visual
    html = html.replace(
        '<section class="hero">\n  <div class="container hero__grid">',
        '''<section class="hero hero--visual">
  <div class="hero__media" aria-hidden="true">
    <img src="assets/img/damage/hero-storm-home.png" alt="Storm-damaged home with emergency tarp after severe weather">
  </div>
  <div class="container hero__grid">''',
        1,
    )

    # First img-placeholder (free inspection) → inspect scene
    html = html.replace(
        '<div class="img-placeholder" role="img" aria-label="Property inspection placeholder"></div>',
        '''<div class="media-frame reveal" style="aspect-ratio:16/10">
        <img src="assets/img/scenes/inspect.jpg" alt="Public adjuster inspecting storm-damaged property" loading="lazy">
      </div>''',
        1,
    )

    # Second placeholder (denied) → settle
    html = html.replace(
        '<div class="img-placeholder img-placeholder--square" role="img" aria-label=""></div>',
        '''<div class="media-frame reveal" style="aspect-ratio:1">
        <img src="assets/img/scenes/settle.jpg" alt="Successful insurance claim settlement paperwork" loading="lazy">
      </div>''',
        1,
    )

    # Claim-type cards: inject card__media after <article class="card"> for each claim type
    for title, img, alt in CLAIM_TYPE_MEDIA:
        # Match article that contains this h3
        pattern = (
            rf'(<article class="card">\s*)'
            rf'(<div class="card__icon"[^>]*>.*?</div>\s*'
            rf'<h3>{re.escape(title)}</h3>)'
        )

        def repl(m, img=img, alt=alt):
            return (
                f'<article class="card card--media reveal">\n'
                f'          <div class="card__media">\n'
                f'            <img src="assets/{img}" alt="{alt}" loading="lazy">\n'
                f'          </div>\n'
                f'          {m.group(2)}'
            )

        html2, n = re.subn(pattern, repl, html, count=1, flags=re.S)
        if n:
            html = html2
        else:
            print(f"  WARN: claim card not found: {title}")

    # Reveal on step cards and how-it-works / sections
    html = html.replace('<article class="card step-card">', '<article class="card step-card reveal">')
    html = html.replace(
        '<div class="section__header section__header--center">',
        '<div class="section__header section__header--center reveal">',
    )
    # Help cards (experience / present / negotiate) — articles without media
    html = re.sub(
        r'<article class="card">\s*<div class="card__icon"',
        '<article class="card reveal">\n          <div class="card__icon"',
        html,
    )

    return html


def enhance_page_hero(html: str, prefix: str, img_path: str, alt: str) -> str:
    """Add page-hero--visual with CSS background image, if page-hero exists and not already visual."""
    if "page-hero--visual" in html:
        return html
    url = f"{prefix}assets/{img_path}"
    # page-hero with optional whitespace
    html2, n = re.subn(
        r'<section class="page-hero">',
        f'<section class="page-hero page-hero--visual" style="--page-hero-img:url(\'{url}\')">',
        html,
        count=1,
    )
    if n:
        return html2
    return html


def enhance_claim_help(html: str, prefix: str) -> str:
    # Make compact hero visual
    if "hero--visual" not in html:
        html = html.replace(
            '<section class="hero hero--compact">\n  <div class="container">',
            f'''<section class="hero hero--compact hero--visual">
  <div class="hero__media" aria-hidden="true">
    <img src="{prefix}assets/img/damage/hero-storm-home.png" alt="Storm-damaged home with emergency tarp after severe weather">
  </div>
  <div class="container">''',
            1,
        )
    # Insert feature media before form-card
    if "feature-media" not in html and "form-card" in html:
        media = f'''<div class="feature-media reveal">
      <div class="media-frame">
        <img src="{prefix}assets/img/scenes/call.jpg" alt="Public adjuster consulting with a property owner about their claim" loading="lazy">
      </div>
    </div>
    '''
        html = html.replace('<div class="form-card">', media + '<div class="form-card">', 1)
    # Reveal on hero content
    html = html.replace(
        '<div class="hero__content" style="max-width:42rem">',
        '<div class="hero__content reveal" style="max-width:42rem">',
        1,
    )
    return html


def enhance_about(html: str, prefix: str) -> str:
    if "feature-media" in html or "media-frame" in html:
        return html
    # Insert ops image after first paragraph in main content section
    media = f'''<div class="feature-media reveal" style="max-width:40rem;margin:1.5rem 0 2rem">
  <div class="media-frame" style="aspect-ratio:16/10">
    <img src="{prefix}assets/img/scenes/ops.jpg" alt="United Claims Specialists claim operations team" loading="lazy">
  </div>
</div>
'''
    # After opening of first content section container's first <p>...</p>
    m = re.search(r'(<section class="section"><div class="container">\s*<p>.*?</p>)', html, re.S)
    if m:
        insert_at = m.end()
        html = html[:insert_at] + "\n" + media + html[insert_at:]
    return html


def enhance_blog_index(html: str, prefix: str) -> str:
    if "feature-media" in html or "blog-hero" in html:
        return html
    media = f'''<div class="feature-media reveal" style="max-width:48rem;margin:0 auto 2rem">
  <div class="media-frame" style="aspect-ratio:21/9">
    <img src="{prefix}assets/img/damage/blog-hero.png" alt="UCS resources and insurance claim guides" loading="lazy">
  </div>
</div>
'''
    # After page-hero section
    html2, n = re.subn(
        r'(</section>\s*<section class="trust-strip")',
        media + r"\1",
        html,
        count=1,
    )
    # Better: insert after trust-strip, before next section
    if n == 0:
        html2, n = re.subn(
            r'(</section>\s*)(<section class="section")',
            rf"\1{media}\2",
            html,
            count=1,
        )
    return html2 if n else html


def enhance_service_body(html: str, prefix: str, img_path: str, alt: str) -> str:
    """If no media yet in body, insert a featured frame after trust strip / first content."""
    if "media-frame" in html or "card__media" in html or "feature-media" in html:
        return html
    media = f'''<div class="container" style="padding-top:var(--space-8)">
  <div class="feature-media reveal" style="max-width:44rem">
    <div class="media-frame" style="aspect-ratio:16/10">
      <img src="{prefix}assets/{img_path}" alt="{alt}" loading="lazy">
    </div>
  </div>
</div>
'''
    # Insert after trust-strip closing, before next section
    html2, n = re.subn(
        r'(</section>\s*)(<section class="section")',
        rf"\1{media}\2",
        html,
        count=1,
    )
    return html2 if n else html


KEY_SERVICE_SLUGS = {
    "insurance-claim-help",
    "storm-damage",
    "water-damage",
    "fire-damage-insurance-claims",
    "roof-leak",
    "flood-damage",
    "denied-claims",
    "residential-public-adjuster",
    "commercial-public-adjuster",
    "about-us",
    "hurricane-damage",
    "hail-damage",
    "hail-damage-insurance-claims",
    "wind-damage-insurance-claims",
    "wildfire-damage",
    "mold-damage-insurance-claims",
    "income-loss",
    "tornado-damage-insurance-claims",
    "theft-vandalism-damage",
    "accidental-damage",
    "property-damage-insurance-claims",
    "contractor-claim-services",
    "appraisal-services",
}


def process_file(path: Path) -> str | None:
    rel = path.relative_to(ROOT)
    html = path.read_text(encoding="utf-8")
    original = html
    prefix = depth_prefix(rel)

    # Determine slug from parent dir name
    if rel.name == "index.html" and len(rel.parts) > 1:
        slug = rel.parts[0] if rel.parts[0] != "blog" else (
            "blog" if len(rel.parts) == 2 else "blog-post"
        )
    elif rel.name == "index.html":
        slug = "home"
    else:
        slug = rel.stem

    if slug == "home":
        html = update_index(html)
    else:
        img_path, alt = pick_image(slug if slug != "blog-post" else rel.parts[-2] if len(rel.parts) >= 2 else "blog")

        if slug == "insurance-claim-help":
            html = enhance_claim_help(html, prefix)
        elif slug == "about-us":
            html = enhance_page_hero(html, prefix, img_path, alt)
            html = enhance_about(html, prefix)
        elif slug == "blog":
            html = enhance_page_hero(html, prefix, "img/damage/blog-hero.png", "UCS blog and claim resources")
            html = enhance_blog_index(html, prefix)
        elif slug == "blog-post":
            # light: page hero visual only based on post slug keywords
            post_slug = rel.parts[-2]
            img_path, alt = pick_image(post_slug)
            html = enhance_page_hero(html, prefix, img_path, alt)
        elif slug in KEY_SERVICE_SLUGS or slug.startswith("public-adjuster"):
            html = enhance_page_hero(html, prefix, img_path, alt)
            html = enhance_service_body(html, prefix, img_path, alt)
        else:
            # locations, privacy, terms, contact, etc.
            html = enhance_page_hero(html, prefix, img_path, alt)

    html = add_motion_script(html, prefix)

    if html != original:
        path.write_text(html, encoding="utf-8")
        return str(rel)
    return None


def main():
    updated = []
    for path in sorted(ROOT.rglob("*.html")):
        if "_partials" in path.parts or "_previews" in path.parts:
            continue
        r = process_file(path)
        if r:
            updated.append(r)
    print(f"Updated {len(updated)} pages:")
    for u in updated:
        print(f"  - {u}")


if __name__ == "__main__":
    main()
