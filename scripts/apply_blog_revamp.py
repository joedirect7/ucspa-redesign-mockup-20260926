#!/usr/bin/env python3
"""Apply Refresh+Redate + soft-power + index demotion on mockup blog only.
Joe date rule 2026-09-26: no future dates; spread through end-2025 → 2026-09-26.
"""
from __future__ import annotations

import calendar
import re
from datetime import date
from pathlib import Path

ROOT = Path("/workspace/ucs-seo/ucspa-redesign-mockup-20260926")
BLOG = ROOT / "blog"
CACHE = "v20260926c"
TODAY = date(2026, 9, 26)

# Keep-as-is: preserve existing publish dates
KEEP_DATES = {
    "behind-the-claims-insiders-reveal-altered-reports-after-hurricanes": date(2024, 10, 2),
    "quick-guide-to-the-differences-between-the-types-of-adjusters-0": date(2024, 9, 24),
    "common-mistakes-on-insurance-claims": date(2024, 9, 3),
    "frozen-pipe-insurance-claims-what-to-do": date(2025, 1, 2),
}

# Full plan Refresh+Redate schedule (past only). Includes posts not yet on mockup.
PLAN_DATES: dict[str, date] = {
    "difference-in-coverage-for-regular-storms-vs-hurricanes-0": date(2025, 11, 4),
    "burden-of-proof-in-florida": date(2025, 11, 11),
    "signs-of-water-damage-in-your-walls-0": date(2025, 11, 18),
    "signs-of-water-damage-in-your-walls": date(2025, 11, 18),
    "bad-faith-insurance-claims": date(2025, 11, 25),
    "civil-remedy-notices": date(2025, 12, 2),
    "when-does-homeowners-insurance-cover-roof-replacements-0": date(2025, 12, 9),
    "when-does-homeowners-insurance-cover-roof-replacements": date(2025, 12, 9),
    "churn-and-burn-insurance-adjusting": date(2025, 12, 16),
    "what-happens-when-you-dont-call-a-public-adjuster-0": date(2026, 1, 6),
    "what-happens-when-you-dont-call-a-public-adjuster": date(2026, 1, 6),
    "what-you-need-to-know-about-sworn-statement-in-proof-of-loss": date(2026, 1, 13),
    "top-five-tips-on-filing-a-mold-damage-claim-0": date(2026, 1, 20),
    "top-five-tips-on-filing-a-mold-damage-claim": date(2026, 1, 20),
    "preparing-for-examination-under-oat": date(2026, 1, 27),
    "why-you-should-not-accept-an-insurance-companys-first-offer-0": date(2026, 2, 3),
    "appraisals-in-hurricane-damage-insurance-claim-disputes": date(2026, 2, 10),
    "insurance-claim-denied-these-are-the-next-steps-0": date(2026, 2, 17),
    "top-reasons-to-hire-a-public-adjuster": date(2026, 2, 24),
    "top-5-benefits-for-hiring-a-public-insurance-adjuster-0": date(2026, 3, 3),
    "how-to-dispute-a-home-insurance-claim-settlement-or-denial": date(2026, 3, 10),
    "how-do-i-reopen-an-insurance-claim": date(2026, 3, 17),
    "condo-insurance-claims": date(2026, 3, 24),
    "does-homeowners-insurance-cover-land-erosion": date(2026, 3, 31),
    "casualty-loss-deduction": date(2026, 4, 7),
    "canine-liability-exclusion": date(2026, 4, 14),
    "completing-a-total-loss-inventory": date(2026, 4, 21),
    "for-property-loss-claims-what-is-replacement-cost-vs-actual-cash-value": date(2026, 4, 28),
    "top-five-tips-on-hurricane-preparation-0": date(2026, 5, 12),
    "top-five-tips-on-hurricane-preparation": date(2026, 5, 12),
    "an-ounce-of-prevention-minimizing-hurricane-damage": date(2026, 5, 19),
    "5-things-your-insurance-company": date(2026, 6, 2),
    "5-things-your-insurance-company-may-not-want-you-to-know": date(2026, 6, 2),
    "how-to-manage-a-denied-homeowners-insurance-claim": date(2026, 6, 16),
    "what-you-need-to-know-about-hail-damage-claims": date(2026, 7, 7),
    "how-can-i-find-a-public-adjuster-near-me": date(2026, 7, 21),
    "why-reopen-a-denied-insurance-claim": date(2026, 8, 11),
    "contractors-legally-negotiate-insurance-claims": date(2026, 9, 9),
}

# Priority C — demote/hide from mockup index (files kept)
DEMOTE = {
    "how-to-fast-track-your-insurance-claims",
    "how-to-handle-homeowners-insurance-denial",
    "why-you-should-employ-a-private-insurance-adjuster-in-miami",
    "a-florida-public-adjuster-can-help-after-storm-damage",
}

# Topic alts for heroes
TOPIC_ALT = {
    "signs-of-water-damage-in-your-walls": "Moisture meter reading high humidity on water-damaged wall",
    "top-five-tips-on-filing-a-mold-damage-claim": "Dehumidifier running in a mold-damaged interior room",
    "when-does-homeowners-insurance-cover-roof-replacements": "Storm-damaged roof with emergency tarp and ladder",
    "what-you-need-to-know-about-hail-damage-claims": "Hail impact marks circled on asphalt roof shingles",
    "top-five-tips-on-hurricane-preparation": "Plywood, sandbags, and lanterns staged for hurricane prep",
    "frozen-pipe-insurance-claims-what-to-do": "Burst frozen copper pipe with ice and water damage",
    "behind-the-claims-insiders-reveal-altered-reports-after-hurricanes": "Hurricane storm damage to residential property",
    "does-homeowners-insurance-cover-land-erosion": "Coastal or storm-related property and ground damage",
    "a-florida-public-adjuster-can-help-after-storm-damage": "Florida storm damage to a home exterior",
    "insurance-claim-denied-these-are-the-next-steps-0": "Homeowner reviewing insurance claim documents",
    "how-to-manage-a-denied-homeowners-insurance-claim": "Reviewing a denied homeowners insurance claim",
    "how-to-dispute-a-home-insurance-claim-settlement-or-denial": "Disputing a home insurance claim settlement",
    "why-reopen-a-denied-insurance-claim": "Reopening a denied insurance claim paperwork",
    "burden-of-proof-in-florida": "Documenting property damage for a Florida insurance claim",
    "what-you-need-to-know-about-sworn-statement-in-proof-of-loss": "Insurance proof-of-loss claim documentation",
    "condo-insurance-claims": "Condominium building property damage claim",
    "contractors-legally-negotiate-insurance-claims": "Contractor and insurance claim documentation",
    "common-mistakes-on-insurance-claims": "Avoiding common homeowners insurance claim mistakes",
    "quick-guide-to-the-differences-between-the-types-of-adjusters-0": "Public adjuster inspecting property damage",
    "top-reasons-to-hire-a-public-adjuster": "Public adjuster helping a homeowner with a claim",
    "top-5-benefits-for-hiring-a-public-insurance-adjuster-0": "Benefits of hiring a public insurance adjuster",
    "how-can-i-find-a-public-adjuster-near-me": "Finding a licensed public adjuster near you",
    "how-do-i-reopen-an-insurance-claim": "Steps to reopen an underpaid insurance claim",
    "why-you-should-not-accept-an-insurance-companys-first-offer-0": "Reviewing an insurance company's first settlement offer",
    "5-things-your-insurance-company-may-not-want-you-to-know": "Homeowners reviewing insurance policy details",
    "what-happens-when-you-dont-call-a-public-adjuster": "Property damage claim without a public adjuster",
    "how-to-fast-track-your-insurance-claims": "Insurance claims process documentation",
    "how-to-handle-homeowners-insurance-denial": "Handling a homeowners insurance denial letter",
    "why-you-should-employ-a-private-insurance-adjuster-in-miami": "Miami property damage public adjuster inspection",
}

PULLQUOTE_OLD = (
    "GET HELP WITH YOUR CLAIM — A public adjuster can make a 700% difference in your payout."
)
PULLQUOTE_NEW = (
    "GET HELP WITH YOUR CLAIM — A public adjuster can be the difference between an underpaid claim and the settlement you deserve."
)

MONTH_NAMES = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def fmt_display(d: date) -> str:
    return f"{MONTH_NAMES[d.month]} {d.day}, {d.year}"


def iso(d: date) -> str:
    return d.isoformat()


def assert_not_future(d: date, label: str) -> None:
    if d > TODAY:
        raise SystemExit(f"Future date forbidden: {label}={d} > {TODAY}")


def replace_time(html: str, d: date) -> str:
    assert_not_future(d, "replace_time")
    disp = fmt_display(d)
    # Replace existing <time datetime="...">...</time>
    html2, n = re.subn(
        r'<time datetime="[^"]*">[^<]*</time>',
        f'<time datetime="{iso(d)}">{disp}</time>',
        html,
        count=1,
    )
    if n:
        return html2
    # Insert into article-meta Written by … · 5 mins pattern
    html2, n = re.subn(
        r'(<div class="article-meta"><span>Resources</span><span>Written by [^<]*?)( · \d+ mins</span></div>)',
        rf'\1 · <time datetime="{iso(d)}">{disp}</time>\2',
        html,
        count=1,
    )
    if n:
        return html2
    # Fallback: replace bare "5 mins" meta span
    html2, n = re.subn(
        r'(<div class="article-meta"><span>Resources</span><span>)([^<]*?)(</span></div>)',
        rf'\1\2 · <time datetime="{iso(d)}">{disp}</time>\3',
        html,
        count=1,
    )
    return html2 if n else html


def soft_power(html: str) -> tuple[str, int]:
    n = 0
    if PULLQUOTE_OLD in html:
        html = html.replace(PULLQUOTE_OLD, PULLQUOTE_NEW)
        n += 1
    # Phrase map (hero/CTA style marketing lines only — keep OPPAGA 747% body cite)
    replacements = [
        (r"the maximum payment you deserve", "the payment you deserve"),
        (r"get the maximum settlement", "get the settlement you deserve"),
        (r"the maximum settlement your policy allows", "the fair settlement your policy allows"),
        (r"negotiate for the maximum settlement", "negotiate for the settlement you deserve"),
        (r"help you get the maximum settlement", "help you get the settlement you deserve"),
        (r"get you the maximum payout", "get you the settlement you deserve"),
        (r"the maximum payout", "the settlement you deserve"),
        (r"maximum payout", "fair settlement"),
    ]
    for pat, repl in replacements:
        html2, c = re.subn(pat, repl, html, flags=re.I)
        if c:
            html = html2
            n += c
    return html, n


def light_polish(slug: str, html: str) -> tuple[str, list[str]]:
    notes: list[str] = []
    if slug == "behind-the-claims-insiders-reveal-altered-reports-after-hurricanes":
        if "Hurricane Helen" in html:
            html = html.replace("Hurricane Helen", "Hurricane Helene")
            notes.append("Helen→Helene")
        if "### The Hidden Battle" in html:
            html = html.replace(
                "### The Hidden Battle: Navigating Insurance Claims After Hurricane Helene…",
                "Insiders reveal how altered reports can undercut hurricane claims.",
            )
            notes.append("cleaned meta markdown excerpt")
    if slug == "what-you-need-to-know-about-sworn-statement-in-proof-of-loss":
        if "errors or accuracies" in html:
            html = html.replace("errors or accuracies", "errors or inaccuracies")
            notes.append("accuracies→inaccuracies")
    if slug == "does-homeowners-insurance-cover-land-erosion":
        # only whole-word lighting → lightning if present as typo
        if re.search(r"\blighting\b", html) and "lightning" not in html.lower():
            html2, c = re.subn(r"\blighting\b", "lightning", html)
            if c:
                html = html2
                notes.append("lighting→lightning")
        elif " lighting " in html.lower() or ">lighting<" in html.lower():
            html2, c = re.subn(r"(?i)\blighting\b", "lightning", html)
            if c:
                html = html2
                notes.append("lighting→lightning")
    if slug == "frozen-pipe-insurance-claims-what-to-do":
        if "vacant of unoccupied" in html:
            html = html.replace("vacant of unoccupied", "vacant or unoccupied")
            notes.append("vacant of→or")
    # Strip leftover markdown hashes from related-card Helen excerpt if present
    if "### The Hidden Battle" in html:
        html = html.replace(
            "### The Hidden Battle: Navigating Insurance Claims After Hurricane Helen…",
            "Insiders reveal how altered reports can undercut hurricane claims.",
        )
        html = html.replace(
            "### The Hidden Battle: Navigating Insurance Claims After Hurricane Helene…",
            "Insiders reveal how altered reports can undercut hurricane claims.",
        )
        notes.append("related-card Helen excerpt cleaned")
    return html, notes


def set_hero_alt(slug: str, html: str) -> str:
    alt = TOPIC_ALT.get(slug, "Property damage insurance claim resources")
    # article hero img
    html = re.sub(
        rf'(src="[^"]*blog-heroes/{re.escape(slug)}\.webp\?v=)[^"]*(" alt=")[^"]*(")',
        rf'\1{CACHE}\2{alt}\3',
        html,
    )
    # also bump any remaining blog-heroes cache + empty alt on this page's main frame
    html = re.sub(
        r'(assets/img/blog-heroes/[^"?]+\.webp)\?v=[^"\']+',
        rf'\1?v={CACHE}',
        html,
    )
    return html


def card_html(slug: str, title: str, excerpt: str, d: date | None, hero_exists: bool) -> str:
    alt = TOPIC_ALT.get(slug, "Property damage insurance claim resources")
    if hero_exists:
        thumb = (
            f'<div class="blog-card__thumb blog-card__thumb--img">'
            f'<img src="../assets/img/blog-heroes/{slug}.webp?v={CACHE}" alt="{alt}" '
            f'loading="lazy" width="640" height="360"></div>'
        )
    else:
        thumb = '<div class="blog-card__thumb" aria-hidden="true"></div>'
    if d:
        meta = f'<div class="article-meta"><span><time datetime="{iso(d)}">{fmt_display(d)}</time></span></div>'
    else:
        meta = '<div class="article-meta"><span>Resources</span></div>'
    excerpt = excerpt.replace("### ", "").strip()
    if len(excerpt) > 160:
        excerpt = excerpt[:157].rsplit(" ", 1)[0] + "…"
    # escape
    excerpt = (
        excerpt.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
    title_esc = (
        title.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
    return (
        f'<article class="blog-card">\n'
        f'      {thumb}\n'
        f'      <div class="blog-card__body">\n'
        f'        {meta}\n'
        f'        <h3><a href="{slug}/">{title_esc}</a></h3>\n'
        f'        <p class="blog-card__excerpt">{excerpt}</p>\n'
        f'        <a class="card__link" href="{slug}/">Read article</a>\n'
        f'      </div>\n'
        f'    </article>'
    )


def extract_title(html: str, slug: str) -> str:
    m = re.search(r"<h1>([^<]+)</h1>", html)
    if m:
        return m.group(1).strip()
    return slug.replace("-", " ").title()


def extract_excerpt(html: str) -> str:
    # first prose paragraph
    m = re.search(r'<div class="prose">\s*(?:<p>)?([^<]{40,280})', html)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()
    m = re.search(r'<meta name="description" content="([^"]+)"', html)
    if m:
        return m.group(1).replace("### ", "").strip()
    return "Insights from United Claims Specialists."


def update_plan_md() -> None:
    path = ROOT / "BLOG-REVAMP-PLAN.md"
    text = path.read_text(encoding="utf-8")
    # Update header note
    note = (
        "**Date rule (Joe 2026-09-26):** Proposed publish/updated dates must **not** be in the future. "
        "Refresh+Redate window = end of 2025 through **2026-09-26** (today, America/New_York). "
        "Prior Oct 2026–Jan 2027 draft dates were replaced.\n\n"
    )
    if "Date rule (Joe 2026-09-26)" not in text:
        text = text.replace(
            "**Canonical conversion URL:** https://www.ucspa.com/insurance-claim-help\n",
            "**Canonical conversion URL:** https://www.ucspa.com/insurance-claim-help\n\n" + note,
        )
    # Replace the Priority B table date column values via known old→new map from prior plan
    old_to_slug_date = [
        ("difference-in-coverage-for-regular-storms-vs-hurricanes-0", "2026-10-06", PLAN_DATES["difference-in-coverage-for-regular-storms-vs-hurricanes-0"]),
        ("burden-of-proof-in-florida", "2026-10-08", PLAN_DATES["burden-of-proof-in-florida"]),
        ("signs-of-water-damage-in-your-walls-0", "2026-10-13", PLAN_DATES["signs-of-water-damage-in-your-walls-0"]),
        ("bad-faith-insurance-claims", "2026-10-15", PLAN_DATES["bad-faith-insurance-claims"]),
        ("civil-remedy-notices", "2026-10-16", PLAN_DATES["civil-remedy-notices"]),
        ("when-does-homeowners-insurance-cover-roof-replacements-0", "2026-10-20", PLAN_DATES["when-does-homeowners-insurance-cover-roof-replacements-0"]),
        ("churn-and-burn-insurance-adjusting", "2026-10-22", PLAN_DATES["churn-and-burn-insurance-adjusting"]),
        ("what-happens-when-you-dont-call-a-public-adjuster-0", "2026-10-27", PLAN_DATES["what-happens-when-you-dont-call-a-public-adjuster-0"]),
        ("what-you-need-to-know-about-sworn-statement-in-proof-of-loss", "2026-10-29", PLAN_DATES["what-you-need-to-know-about-sworn-statement-in-proof-of-loss"]),
        ("top-five-tips-on-filing-a-mold-damage-claim-0", "2026-11-03", PLAN_DATES["top-five-tips-on-filing-a-mold-damage-claim-0"]),
        ("preparing-for-examination-under-oat", "2026-11-05", PLAN_DATES["preparing-for-examination-under-oat"]),
        ("why-you-should-not-accept-an-insurance-companys-first-offer-0", "2026-11-10", PLAN_DATES["why-you-should-not-accept-an-insurance-companys-first-offer-0"]),
        ("appraisals-in-hurricane-damage-insurance-claim-disputes", "2026-11-12", PLAN_DATES["appraisals-in-hurricane-damage-insurance-claim-disputes"]),
        ("insurance-claim-denied-these-are-the-next-steps-0", "2026-11-17", PLAN_DATES["insurance-claim-denied-these-are-the-next-steps-0"]),
        ("top-reasons-to-hire-a-public-adjuster", "2026-11-19", PLAN_DATES["top-reasons-to-hire-a-public-adjuster"]),
        ("top-5-benefits-for-hiring-a-public-insurance-adjuster-0", "2026-11-24", PLAN_DATES["top-5-benefits-for-hiring-a-public-insurance-adjuster-0"]),
        ("how-to-dispute-a-home-insurance-claim-settlement-or-denial", "2026-12-01", PLAN_DATES["how-to-dispute-a-home-insurance-claim-settlement-or-denial"]),
        ("how-do-i-reopen-an-insurance-claim", "2026-12-03", PLAN_DATES["how-do-i-reopen-an-insurance-claim"]),
        ("condo-insurance-claims", "2026-12-08", PLAN_DATES["condo-insurance-claims"]),
        ("does-homeowners-insurance-cover-land-erosion", "2026-12-10", PLAN_DATES["does-homeowners-insurance-cover-land-erosion"]),
        ("casualty-loss-deduction", "2026-12-15", PLAN_DATES["casualty-loss-deduction"]),
        ("canine-liability-exclusion", "2026-12-17", PLAN_DATES["canine-liability-exclusion"]),
        ("completing-a-total-loss-inventory", "2026-12-22", PLAN_DATES["completing-a-total-loss-inventory"]),
        ("for-property-loss-claims-what-is-replacement-cost-vs-actual-cash-value", "2026-12-29", PLAN_DATES["for-property-loss-claims-what-is-replacement-cost-vs-actual-cash-value"]),
        ("5-things-your-insurance-company", "2027-01-05", PLAN_DATES["5-things-your-insurance-company"]),
        ("how-to-manage-a-denied-homeowners-insurance-claim", "2027-01-07", PLAN_DATES["how-to-manage-a-denied-homeowners-insurance-claim"]),
        ("what-you-need-to-know-about-hail-damage-claims", "2027-01-12", PLAN_DATES["what-you-need-to-know-about-hail-damage-claims"]),
        ("how-can-i-find-a-public-adjuster-near-me", "2027-01-14", PLAN_DATES["how-can-i-find-a-public-adjuster-near-me"]),
        ("why-reopen-a-denied-insurance-claim", "2027-01-19", PLAN_DATES["why-reopen-a-denied-insurance-claim"]),
        ("contractors-legally-negotiate-insurance-claims", "2027-01-21", PLAN_DATES["contractors-legally-negotiate-insurance-claims"]),
        ("top-five-tips-on-hurricane-preparation-0", "2026-05-15", PLAN_DATES["top-five-tips-on-hurricane-preparation-0"]),
        ("an-ounce-of-prevention-minimizing-hurricane-damage", "2026-05-22", PLAN_DATES["an-ounce-of-prevention-minimizing-hurricane-damage"]),
    ]
    for slug, old, new in old_to_slug_date:
        assert_not_future(new, slug)
        # table cells look like | **2026-10-06** |
        text = text.replace(f"**{old}**", f"**{iso(new)}**")
    # Fix intro line about Oct 2026–Jan 2027
    text = text.replace(
        "Spread across revamp window (Oct 2026–Jan 2027) + pre-hurricane season for prep posts.",
        "Spread across revamp window (**2025-11-04 → 2026-09-09**, no future dates) + pre-hurricane season for prep posts (May 2026).",
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for d in list(PLAN_DATES.values()) + list(KEEP_DATES.values()):
        assert_not_future(d, "schedule")

    update_plan_md()

    folders = sorted(p.name for p in BLOG.iterdir() if p.is_dir())
    stats = {
        "redated": 0,
        "kept": 0,
        "soft_power": 0,
        "polish": [],
        "demoted_from_index": [],
        "index_shown": [],
        "heroes_alt": 0,
    }

    show_cards: list[tuple[date, str, str]] = []

    for slug in folders:
        path = BLOG / slug / "index.html"
        html = path.read_text(encoding="utf-8")

        if slug in KEEP_DATES:
            d = KEEP_DATES[slug]
            html = replace_time(html, d)
            stats["kept"] += 1
            bucket = "keep"
        elif slug in DEMOTE:
            d = None
            bucket = "demote"
            stats["demoted_from_index"].append(slug)
        elif slug in PLAN_DATES:
            d = PLAN_DATES[slug]
            html = replace_time(html, d)
            stats["redated"] += 1
            bucket = "refresh"
        else:
            d = None
            bucket = "other"

        html, sp_n = soft_power(html)
        stats["soft_power"] += sp_n

        html, polish_notes = light_polish(slug, html)
        for n in polish_notes:
            stats["polish"].append(f"{slug}: {n}")

        if (ROOT / "assets/img/blog-heroes" / f"{slug}.webp").exists():
            html = set_hero_alt(slug, html)
            stats["heroes_alt"] += 1

        # bump css cache on blog pages lightly
        html = html.replace("?v=v20260926b", f"?v={CACHE}")

        path.write_text(html, encoding="utf-8")

        if bucket in ("keep", "refresh") and d is not None:
            title = extract_title(html, slug)
            excerpt = extract_excerpt(html)
            show_cards.append((d, slug, card_html(
                slug, title, excerpt, d,
                (ROOT / "assets/img/blog-heroes" / f"{slug}.webp").exists(),
            )))
            stats["index_shown"].append(f"{iso(d)} {slug}")

    # Sort index: newest first
    show_cards.sort(key=lambda x: x[0], reverse=True)

    index_path = BLOG / "index.html"
    index_html = index_path.read_text(encoding="utf-8")
    cards_block = "".join(c for _, _, c in show_cards)
    new_index, n = re.subn(
        r'(<div class="card-grid card-grid--3">).*?(</div>\s*</div></section>\s*<section class="cta-band">)',
        rf'\1{cards_block}\2',
        index_html,
        count=1,
        flags=re.S,
    )
    if not n:
        raise SystemExit("Failed to rebuild blog index card grid")
    new_index = new_index.replace("?v=v20260926b", f"?v={CACHE}")
    # Soft-power on index if any
    new_index, _ = soft_power(new_index)
    index_path.write_text(new_index, encoding="utf-8")

    # Notes
    notes = []
    notes.append("# Blog apply notes — mockup only")
    notes.append("")
    notes.append(f"**Applied:** Sat Sep 26, 2026 (ET) · cache `{CACHE}`")
    notes.append("**Scope:** `/workspace/ucs-seo/ucspa-redesign-mockup-20260926/` — NOT live HubSpot/ucspa.com CMS.")
    notes.append("**Date rule:** No future dates. Refresh+Redate = 2025-11-04 → 2026-09-09 (plan) / mockup articles through 2026-09-09.")
    notes.append("")
    notes.append("## Counts")
    notes.append("")
    notes.append(f"| Metric | Count |")
    notes.append(f"|--------|------:|")
    notes.append(f"| Mockup article folders | {len(folders)} |")
    notes.append(f"| Index cards shown (Keep + Refresh) | {len(show_cards)} |")
    notes.append(f"| Redated (Refresh+Redate on mockup) | {stats['redated']} |")
    notes.append(f"| Keep-as-is date preserved | {stats['kept']} |")
    notes.append(f"| Demoted/hidden from index (files kept) | {len(stats['demoted_from_index'])} |")
    notes.append(f"| Soft-power replacements (700%/maximum headline) | {stats['soft_power']} |")
    notes.append(f"| Topic hero alts/cache refreshed | {stats['heroes_alt']} |")
    notes.append(f"| Light polish fixes | {len(stats['polish'])} |")
    notes.append("")
    notes.append("## Index shown (newest first)")
    notes.append("")
    for line in sorted(stats["index_shown"], reverse=True):
        notes.append(f"- `{line}`")
    notes.append("")
    notes.append("## Demoted from index (not deleted)")
    notes.append("")
    for s in stats["demoted_from_index"]:
        notes.append(f"- `{s}`")
    notes.append("")
    notes.append("## Soft-power")
    notes.append("")
    notes.append("- Replaced blog pullquote `700% difference in your payout` → settlement-you-deserve line (COPY-FAIR-DESERVE-DRAFT).")
    notes.append("- Softened marketing `maximum payout/settlement` phrasing in blog heroes/CTAs.")
    notes.append("- **Kept** OPPAGA **747%** body citation in `top-reasons-to-hire-a-public-adjuster` (historical cite OK).")
    notes.append("")
    notes.append("## Light polish")
    notes.append("")
    if stats["polish"]:
        for p in stats["polish"]:
            notes.append(f"- {p}")
    else:
        notes.append("- (none matched in mockup bodies)")
    notes.append("")
    notes.append("## Heroes")
    notes.append("")
    notes.append("- Existing topic webps under `assets/img/blog-heroes/` retained (water/mold/roof/hail/hurricane/pipe etc.).")
    notes.append("- Added descriptive `alt` text; cache-busted to `?v=v20260926c`.")
    notes.append("- Stale named-storm / COVID / 2012 Citizens posts were **not** in this mockup set — N/A to hide.")
    notes.append("")
    notes.append("## Out of scope")
    notes.append("")
    notes.append("- Live HubSpot / ucspa.com CMS — untouched.")
    notes.append("- No wholesale rewrites; no invented legal claims/stats.")
    notes.append("- Pillars not yet in mockup folders (storm-vs-hurricane, RCV/ACV, slab leaks, CRN, etc.) — plan dates updated only.")
    notes.append("")

    (ROOT / "BLOG-APPLY-NOTES.md").write_text("\n".join(notes) + "\n", encoding="utf-8")
    print("OK", stats["redated"], "redated,", len(show_cards), "index cards,", len(stats["demoted_from_index"]), "demoted")
    print("soft_power", stats["soft_power"])
    for p in stats["polish"]:
        print("polish:", p)


if __name__ == "__main__":
    main()
