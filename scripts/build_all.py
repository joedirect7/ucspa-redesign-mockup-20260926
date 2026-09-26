#!/usr/bin/env python3
"""Generate complete UCS 2026 static mockup. Verbatim copy + modern chrome."""
from __future__ import annotations
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from chrome import (
    write_page, trust_strip, cta_band, depth_prefix, esc,
    PHONE_DISPLAY, PHONE_TEL, PHONE_ALT, PHONE_ALT_TEL, EMAIL, NAV, LOCATIONS,
)

BASE = Path(__file__).resolve().parents[1]

def p(*paras):
    return "\n".join(f"<p>{esc(x)}</p>" if not x.startswith("<") else x for x in paras)

def checklist(items):
    return '<ul class="check-list">' + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"

def cards(items, cols=3):
    # items: (icon, title, body, href?)
    html = [f'<div class="card-grid card-grid--{cols}">']
    for it in items:
        icon, title, body = it[0], it[1], it[2]
        href = it[3] if len(it) > 3 else None
        link = f'<a class="card__link" href="{href}">Learn more</a>' if href else ""
        html.append(f'''<article class="card">
          <div class="card__icon" aria-hidden="true">{icon}</div>
          <h3>{esc(title)}</h3>
          <p>{esc(body)}</p>
          {link}
        </article>''')
    html.append("</div>")
    return "\n".join(html)

def page_hero(title, lead, crumbs=None):
    bc = ""
    if crumbs:
        parts = "".join(f"<li><a href=\"{h}\">{esc(t)}</a></li>" if h else f"<li><span>{esc(t)}</span></li>" for t,h in crumbs)
        bc = f'<ol class="page-hero__breadcrumb">{parts}</ol>'
    return f'''<section class="page-hero">
  <div class="container">
    {bc}
    <h1>{esc(title)}</h1>
    <p class="page-hero__lead">{esc(lead)}</p>
  </div>
</section>'''

def steps_irr():
    return '''<div class="card-grid card-grid--3">
      <article class="card step-card">
        <div class="step-card__num">1</div>
        <h3>Inspect</h3>
        <p>We send a professional to the property as soon as possible to inspect and accurately document damage.</p>
      </article>
      <article class="card step-card">
        <div class="step-card__num">2</div>
        <h3>Respond</h3>
        <p>We take care of the entire claims process and negotiate with the insurance to ensure your damage is covered.</p>
      </article>
      <article class="card step-card">
        <div class="step-card__num">3</div>
        <h3>Recover</h3>
        <p>Insurances are in the business of paying as little as possible for damages that occur. UCS gets you the biggest payout.</p>
      </article>
    </div>'''

def do_dont(do_items, dont_items):
    do = "".join(f"<li>{esc(i)}</li>" for i in do_items)
    dont = "".join(f"<li>{esc(i)}</li>" for i in dont_items)
    return f'''<div class="do-dont">
      <div class="do-dont__panel do-dont__panel--do"><h3>WHAT TO DO</h3><ul>{do}</ul></div>
      <div class="do-dont__panel do-dont__panel--dont"><h3>WHAT NOT TO DO</h3><ul>{dont}</ul></div>
    </div>'''

def faq(pairs):
    bits = []
    for q,a in pairs:
        bits.append(f'''<details><summary>{esc(q)}</summary><div class="faq__body"><p>{esc(a)}</p></div></details>''')
    return '<div class="faq">' + "".join(bits) + "</div>"

def benefit_three():
    return cards([
        ("🛡️", "We Work for You", "Insurance companies have expert adjusters working for them, so should you! We make sure you get the coverage and payout you need for repairs."),
        ("🏆", "We're Experienced", "We're a team of expert public adjusters that makes sure you have the best insurance claim experience."),
        ("✓", "Free Consultation", "Whether you have a residential or commercial claim, we will start our relationship with a free inspection. We don't get paid, unless you get paid."),
    ], 3)

# ---------- HOME ----------
def build_home():
    body = f'''
<section class="hero">
  <div class="container hero__grid">
    <div class="hero__content">
      <div class="hero__eyebrow">Public Adjusters You Can Trust</div>
      <h1>ON AVERAGE, PEOPLE WHO USE A PUBLIC ADJUSTER GET 700% HIGHER PAYMENTS</h1>
      <p class="hero__lead">We help homeowners, building owners, property managers and contractors file property damage claims, get higher payments and eliminate the headaches of dealing with insurance companies.</p>
      <div class="hero__actions">
        <a class="btn btn--primary btn--lg" href="insurance-claim-help/">Claim Free Inspection</a>
        <a class="btn btn--secondary btn--lg" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      </div>
      <div class="hero__stat">
        <div class="hero__stat-item"><strong>700%</strong><span>Higher avg. payments</span></div>
        <div class="hero__stat-item"><strong>8+</strong><span>States served</span></div>
        <div class="hero__stat-item"><strong>0</strong><span>Upfront fees</span></div>
      </div>
    </div>
    <div class="hero__panel">
      <h2>WE HELP YOU GET THE MAXIMUM PAYOUT, FAST!</h2>
      <p style="margin-bottom:1.5rem">Inspect → Respond → Recover. Your insurance has an adjuster. So should you.</p>
      <a class="btn btn--primary btn--block" href="insurance-claim-help/">Get Started</a>
      <p style="margin-top:1rem;margin-bottom:0;font-size:var(--text-xs);text-align:center;color:rgba(255,255,255,.55)">Or call <a href="tel:{PHONE_TEL}" style="color:var(--ucs-teal-300)">{PHONE_DISPLAY}</a></p>
    </div>
  </div>
</section>
{trust_strip()}
<section class="section">
  <div class="container">
    <div class="section__header section__header--center">
      <span class="section__eyebrow">How it works</span>
      <h2>WE HELP YOU GET THE MAXIMUM PAYOUT, FAST!</h2>
    </div>
    {steps_irr()}
  </div>
</section>
<section class="section section--soft">
  <div class="container">
    <div class="split">
      <div>
        <span class="section__eyebrow">Free inspection</span>
        <h2>CLAIM YOUR FREE INSPECTION</h2>
        <p>United Claims Specialists has licensed adjusters in multiple states so that we can help as many people as possible get the settlements they deserve from their insurance providers.</p>
        <p>Insurance companies rely on the fact that most policyholders don't know what they're actually entitled to and most people accept whatever settlement is offered. Whether you are at the beginning of filing a claim, or if you have already filed your claim- WE CAN HELP!</p>
        {checklist([
          "New property damage that needs an inspection and a claim filed.",
          "Claim has already been filed but you need help negotiating more money for repairs.",
          "You have already accepted a settlement, but you need more for repairs or don't believe you received everything you were entitled to.",
          "Your property damage claim has been denied by the insurance, but you believe it is their responsibility.",
        ])}
        <a class="btn btn--primary" href="insurance-claim-help/">Schedule Free Inspection</a>
      </div>
      <div class="img-placeholder" role="img" aria-label="Property inspection placeholder"></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section__header section__header--center">
      <span class="section__eyebrow">Claim types</span>
      <h2>No matter the type of damage, we've got you covered. Don't file another claim without us!</h2>
    </div>
    {cards([
      ("⛈️", "Storm Damage", "Did you know that weather-related disasters affect more than 80% of the population? With the increase in the Earth's climate- more severe storms and heat waves are expected. We help homeowners, property managers and contractors manage their insurance claims that come along with these severe weather events so that you get complete coverage for damages. No matter the storm type- we'll make sure you're protected.", "storm-damage/"),
      ("🔥", "Fire Damage", "Fire damage can result from lightning strikes, electrical problems, appliance malfunction, wildfires and more. Whatever the cause of your fire damage, United Claims experts can help you get the money you need to rebuild.", "fire-damage-insurance-claims/"),
      ("💧", "Water Damage", "We work with all types of water damage claims. Clean water, gray water containing biological contaminants and black water that contains bacteria all cause different damage situations.", "water-damage/"),
      ("🏠", "Roof Damage", "Most homeowners are shocked to see the destruction to their roof following a storm and are even more shocked to find out that their insurance provider isn't willing to cover the full cost of repairs. As public adjusters, we're prepared to fight for a payment that covers the cost of all the damage.", "roof-leak/"),
      ("📊", "Income Loss", "Running a business is hard enough. If you own a business and have had disaster strike, we know how frustrating that can be. Allow our adjusters to get involved, taking the added stress of handling a complicated insurance claim off of your shoulders, enabling you to get back to business while experts handle your claim.", "income-loss/"),
      ("🌊", "Flood Damage", "The processes behind flood damage insurance claims can be excessively complicated. One wrong form or improper step can result in a claim being underpaid or even outright denied.", "flood-damage/"),
    ], 3)}
  </div>
</section>
<section class="section section--navy">
  <div class="container text-center" style="max-width:40rem;margin-inline:auto">
    <h2>A public adjuster can make a 700% difference in your payout.</h2>
    <p style="margin-bottom:2rem">Don't file another claim without us.</p>
    <a class="btn btn--primary btn--lg" href="insurance-claim-help/">Get Claim Help</a>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section__header section__header--center">
      <h2>HOW CAN A PUBLIC ADJUSTER HELP?</h2>
      <p>Public adjusters are similar to property loss attorneys, but we have a deep understanding of the contractor's repair costs- making us better able to inspect, estimate and maximize insurance policies.</p>
    </div>
    {cards([
      ("📋", "EXPERIENCE IN THE PROCESS", "UCS Public adjusters have decades of experience representing property claims. These skills are utilized on every claim to ensure the best possible results."),
      ("📸", "PRESENT CLAIMS PROPERLY", "Presentation is key when it comes to property damage claims. UCS Public adjusters leave no stone unturned when it comes to documenting ALL property damages associated with our client's losses."),
      ("🤝", "NEGOTIATE CLAIMS", "Our adjusters have successfully negotiated tens of thousands of property claims. Rest assured, you are in good hands allowing our firm to represent your property claim."),
    ], 3)}
  </div>
</section>
<section class="section section--soft">
  <div class="container">
    <div class="split">
      <div>
        <h2>Insurance Claim Was Denied- What Now?</h2>
        <p>You're not alone if you've received a denial for property damage from your insurance. Here's what you need to do.</p>
        <p>We help homeowners, building owners, property managers and contractors file property damage claims, get higher payouts, and eliminate the headaches of dealing with insurance claims. Don't file another claim without us!</p>
        <a class="btn btn--primary" href="denied-claims/">Denied Claims Help</a>
      </div>
      <div class="img-placeholder img-placeholder--square" role="img" aria-label=""></div>
    </div>
  </div>
</section>
{cta_band("")}
'''
    write_page(BASE, "", "index.html",
        "Public Adjusters You Can Trust | United Claims Specialists",
        "We help homeowners, building owners, property managers and contractors file property damage claims and get higher payments.",
        body)

# ---------- CLAIM HELP ----------
def build_claim_help():
    body = f'''
<section class="hero hero--compact">
  <div class="container">
    <div class="hero__content" style="max-width:40rem">
      <div class="hero__eyebrow">Primary conversion</div>
      <h1>More money, less stress, no risk.</h1>
      <p class="hero__lead">Hiring a public adjuster to manage your property damage claim is the best thing you can do. We'll help you from estimating damage all the way to getting paid and make sure that your insurance gives you the payout you deserve. Submit your information below or call us for more information on your new, low-balled or denied insurance claim!</p>
    </div>
  </div>
</section>
{trust_strip()}
<section class="section">
  <div class="container claim-help-layout">
    <div>
      <h2>Tell us about your property damage and we'll be in touch the same day.</h2>
      <p>We help homeowners, building owners, property managers and contractors file property damage claims, get higher payouts, and eliminate the headaches of dealing with insurance claims. Don't file another claim without us!</p>
      <div style="margin:2rem 0;padding:1.5rem;border-radius:var(--radius-xl);background:var(--ucs-slate-50);border:1px solid var(--color-border)">
        <p class="section__eyebrow" style="margin:0 0 .5rem">Need help immediately? Call or chat with us.</p>
        <p class="phone-lg" style="margin:0"><a href="tel:{PHONE_ALT_TEL}">{PHONE_ALT}</a></p>
        <p style="margin:.75rem 0 0;font-size:var(--text-sm);color:var(--color-text-muted)">Also: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY} (5677)</a></p>
      </div>
      {checklist([
        "New, low-balled, or denied insurance claims",
        "Free inspection — no upfront cost",
        "We don't get paid unless you get paid",
      ])}
    </div>
    <div class="form-card glass-panel">
      <h3>Request your free inspection</h3>
      <p>Mockup form — same fields as a typical UCS lead form. Does not submit to live systems.</p>
      <form action="#" method="get" onsubmit="event.preventDefault();alert('Mockup only — form does not submit. Call '+'{PHONE_ALT}'+' or '+'{PHONE_DISPLAY}.');">
        <div class="form-grid form-grid--2">
          <div class="form-field"><label for="fn">First name</label><input id="fn" name="firstname" required autocomplete="given-name"></div>
          <div class="form-field"><label for="ln">Last name</label><input id="ln" name="lastname" required autocomplete="family-name"></div>
        </div>
        <div class="form-grid form-grid--2" style="margin-top:1rem">
          <div class="form-field"><label for="em">Email</label><input id="em" name="email" type="email" required autocomplete="email"></div>
          <div class="form-field"><label for="ph">Phone</label><input id="ph" name="phone" type="tel" required autocomplete="tel"></div>
        </div>
        <div class="form-field" style="margin-top:1rem"><label for="addr">Property address</label><input id="addr" name="address" autocomplete="street-address"></div>
        <div class="form-field" style="margin-top:1rem"><label for="dtype">Damage type</label>
          <select id="dtype" name="damage_type">
            <option value="">Select…</option>
            <option>Storm / Hurricane</option><option>Water</option><option>Fire</option>
            <option>Roof</option><option>Flood</option><option>Mold</option><option>Other</option>
          </select>
        </div>
        <div class="form-field" style="margin-top:1rem"><label for="msg">Tell us about your claim</label><textarea id="msg" name="message" placeholder="New claim, low-balled offer, or denial…"></textarea></div>
        <div class="form-field" style="margin-top:1rem;flex-direction:row;align-items:flex-start;gap:.6rem">
          <input type="checkbox" id="sms" name="sms_consent" style="width:auto;margin-top:.2rem">
          <label for="sms" style="font-weight:500;font-size:var(--text-xs)">I consent to receive SMS messages from United Claims Specialists about my claim. Msg &amp; data rates may apply. Reply STOP to opt out. See Terms.</label>
        </div>
        <button class="btn btn--primary btn--lg btn--block" style="margin-top:1.25rem" type="submit">Submit — Free Inspection</button>
        <p class="form-note">This is a design mockup. No data is sent. For real help call {PHONE_ALT}.</p>
      </form>
    </div>
  </div>
</section>
{cta_band("../")}
'''
    # fix cta prefix for nested page
    body = body.replace(cta_band("../"), cta_band("../").replace('href="../insurance', 'href="../insurance'))  # noop-ish
    # Actually write with correct relative - depth_prefix handles assets; internal links in body need ../
    body = f'''
<section class="hero hero--compact">
  <div class="container">
    <div class="hero__content" style="max-width:42rem">
      <div class="hero__eyebrow">Insurance claim help</div>
      <h1>More money, less stress, no risk.</h1>
      <p class="hero__lead">Hiring a public adjuster to manage your property damage claim is the best thing you can do. We'll help you from estimating damage all the way to getting paid and make sure that your insurance gives you the payout you deserve. Submit your information below or call us for more information on your new, low-balled or denied insurance claim!</p>
    </div>
  </div>
</section>
{trust_strip()}
<section class="section">
  <div class="container claim-help-layout">
    <div>
      <h2>Tell us about your property damage and we'll be in touch the same day.</h2>
      <p>We help homeowners, building owners, property managers and contractors file property damage claims, get higher payouts, and eliminate the headaches of dealing with insurance claims. Don't file another claim without us!</p>
      <div style="margin:2rem 0;padding:1.5rem;border-radius:var(--radius-xl);background:var(--ucs-slate-50);border:1px solid var(--color-border)">
        <p class="section__eyebrow" style="margin:0 0 .5rem">need help immediately? call or chat with us.</p>
        <p class="phone-lg" style="margin:0"><a href="tel:{PHONE_ALT_TEL}">{PHONE_ALT}</a></p>
        <p style="margin:.75rem 0 0;font-size:var(--text-sm);color:var(--color-text-muted)">Also: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY} (5677)</a></p>
      </div>
    </div>
    <div class="form-card">
      <h3>Request your free inspection</h3>
      <p>Tell us about your property damage and we'll be in touch the same day.</p>
      <form action="#" method="get" onsubmit="event.preventDefault();alert('Mockup only — does not submit to live UCS systems.');">
        <div class="form-grid form-grid--2">
          <div class="form-field"><label for="fn">First name</label><input id="fn" name="firstname" required></div>
          <div class="form-field"><label for="ln">Last name</label><input id="ln" name="lastname" required></div>
        </div>
        <div class="form-grid form-grid--2" style="margin-top:1rem">
          <div class="form-field"><label for="em">Email</label><input id="em" name="email" type="email" required></div>
          <div class="form-field"><label for="ph">Phone</label><input id="ph" name="phone" type="tel" required></div>
        </div>
        <div class="form-field" style="margin-top:1rem"><label for="addr">Property address</label><input id="addr" name="address"></div>
        <div class="form-field" style="margin-top:1rem"><label for="dtype">Damage type</label>
          <select id="dtype" name="damage_type"><option value="">Select…</option><option>Storm</option><option>Water</option><option>Fire</option><option>Roof</option><option>Flood</option><option>Mold</option><option>Other</option></select>
        </div>
        <div class="form-field" style="margin-top:1rem"><label for="msg">Message</label><textarea id="msg" name="message"></textarea></div>
        <div class="form-field" style="margin-top:1rem;flex-direction:row;gap:.6rem;align-items:flex-start">
          <input type="checkbox" id="sms" style="width:auto;margin-top:.25rem">
          <label for="sms" style="font-weight:500;font-size:var(--text-xs)">I consent to receive SMS from United Claims Specialists. Msg &amp; data rates may apply. Reply STOP to opt out.</label>
        </div>
        <button class="btn btn--primary btn--lg btn--block" style="margin-top:1.25rem" type="submit">Submit</button>
        <p class="form-note">Design mockup — form does not post. Call {PHONE_ALT} for real help.</p>
      </form>
    </div>
  </div>
</section>
''' + cta_band("../")
    write_page(BASE, "insurance-claim-help", "index.html",
        "More money, less stress, no risk. | United Claims Specialists",
        "Hiring a public adjuster to manage your property damage claim is the best thing you can do.",
        body)

print("Building home + claim-help...")
build_home()
build_claim_help()
print("OK home + claim-help")

# ========== GENERIC SERVICE PAGE ==========
def service_page(slug, title, meta_desc, h1, lead, bullets=None, body_paras=None, faq_pairs=None, extra_html="", do_items=None, dont_items=None):
    crumbs = [("Home", "../index.html"), (title, None)]
    parts = [page_hero(h1, lead, crumbs), trust_strip()]
    parts.append('<section class="section"><div class="container">')
    if bullets:
        parts.append(checklist(bullets))
    if body_paras:
        for para in body_paras:
            parts.append(f"<p>{esc(para)}</p>")
    parts.append(extra_html)
    parts.append('</div></section>')
    parts.append(f'''<section class="section section--soft"><div class="container">
      <div class="section__header section__header--center"><h2>YOUR INSURANCE HAS AN ADJUSTER, SO SHOULD YOU.</h2></div>
      {steps_irr()}
    </div></section>''')
    if do_items and dont_items:
        parts.append(f'<section class="section"><div class="container">{do_dont(do_items, dont_items)}</div></section>')
    parts.append('''<section class="section section--navy"><div class="container text-center" style="max-width:36rem;margin-inline:auto">
      <h2>A public adjuster can make a 700% difference.</h2>
      <p style="margin-bottom:1.5rem">We don't get paid, unless you get paid.</p>
    </div></section>''')
    if faq_pairs:
        parts.append(f'<section class="section"><div class="container"><div class="section__header"><h2>FAQ</h2><p>Most common questions.</p></div>{faq(faq_pairs)}</div></section>')
    parts.append(f'<section class="section section--soft"><div class="container">{benefit_three()}</div></section>')
    parts.append(cta_band("../"))
    write_page(BASE, slug, "index.html", title, meta_desc, "\n".join(parts))

def location_page(slug, state_name, city_line, address_lines, local_phone=None):
    phone_show = local_phone or f"{PHONE_DISPLAY} (5677)"
    phone_tel = PHONE_TEL if not local_phone else "".join(c for c in local_phone if c.isdigit())
    h1 = f"Public Adjusters in {state_name}" if "Los Angeles" not in state_name else "Public Adjuster Los Angeles, CA"
    lead = f"HIRE A {state_name.upper()} PUBLIC ADJUSTER TO GET THE MAXIMUM PAYOUT FOR YOUR PROPERTY DAMAGE CLAIM!"
    body = f'''
{page_hero(h1, "YOUR INSURANCE HAS AN ADJUSTER, SO SHOULD YOU!", [("Home","../index.html"),("Locations","../locations/"),(state_name, None)])}
{trust_strip()}
<section class="section"><div class="container split">
  <div>
    <h2>{esc(lead)}</h2>
    <p><strong>United Claims Specialists in {esc(state_name)}</strong><br>
    {"<br>".join(esc(a) for a in address_lines)}</p>
    <p><a class="btn btn--primary" href="tel:{phone_tel}">GET CLAIMS HELP {esc(phone_show)}</a></p>
    <h3>HOW CAN A PUBLIC ADJUSTER IN {esc(state_name.upper())} HELP?</h3>
    <p>There are many ways a {esc(state_name)} public adjuster can help if you've had damage to your home or business. Before worrying about the large amounts of repairs needed, it's best to speak with a team of professionals. At United Claims Specialists we're here to help get you the compensation you deserve for whatever damage has occurred. From hurricane damage to a roof leak to mold or a pipe burst, our team can help with your claim.</p>
    <p>When you hire the services of a public adjuster you won't have to worry about fighting your insurance company when filing a claim. That's where we step in. We'll make sure to properly document all damages and quickly file your claim on time and correctly. This will help ensure that you get the proper compensation and will help you avoid your claim being underpaid of denied.</p>
    <p>United Claims Specialists is here for you. Call us today at {PHONE_DISPLAY}(5677) to learn more about how we can help throughout the entire claims filing process.</p>
    <h3>GET A BIGGER PAYOUT WITH A {esc(state_name.upper())} PUBLIC ADJUSTER!</h3>
    <p>Insurance companies are in the business of paying as little as possible for repairs, this is how they are profitable. We are in the business of getting you the largest payment possible for the damages your property sustained.</p>
    <p>Our decades of experience can make you thousands of dollars more than trying to file and negotiate your own claim.</p>
    <p><strong>We get paid when you get paid. No risks. All reward.</strong></p>
  </div>
  <div>
    <div class="form-card">
      <h3>GET YOUR FREE INSPECTION</h3>
      <p>United Claims Specialists has local, licensed public adjusters in {esc(state_name)} who understand the market, damage types, repair costs, and more. Our deep claim expertise combined with local knowledge us is how we make sure you get the maximum payout from your insurance for property damage.</p>
      <p>Insurance companies rely on the fact that most policyholders don't know what they're actually entitled to and just accept whatever settlement is offered. Whether you are at the beginning of filing a claim, or if you have already filed your claim- WE CAN HELP!</p>
      {checklist([
        "New property damage that needs an inspection and a claim filed.",
        "Claim has already been filed but you need help negotiating more money for repairs.",
        "You have already accepted a settlement, but you need more for repairs or don't believe you received everything you were entitled to.",
        "Your property damage claim has been denied by the insurance, but you believe it is their responsibility.",
      ])}
      <a class="btn btn--primary btn--block" href="../insurance-claim-help/">Claim Free Inspection</a>
    </div>
  </div>
</div></section>
<section class="section section--soft"><div class="container">
  <div class="section__header section__header--center"><h2>YOUR INSURANCE HAS AN ADJUSTER, SO SHOULD YOU.</h2></div>
  {steps_irr()}
</div></section>
<section class="section section--navy"><div class="container text-center">
  <h2>New, Low-Balled &amp; Denied Claims</h2>
  <p>A public adjuster in {esc(state_name)} can make a 700% difference in your payout.</p>
  <p style="margin-top:1.5rem"><a class="btn btn--primary" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}(5677)</a></p>
</div></section>
''' + cta_band("../")
    write_page(BASE, slug, "index.html",
        f"Public Adjusters in {state_name} | United Claims Specialists",
        f"United Claims Specialists has local, licensed public adjusters in {state_name}.",
        body)

# ---- Storm / property services (verbatim-leaning from live fetches) ----
service_page(
  "storm-damage",
  "Storm Damage Insurance Claims | United Claims Specialists",
  "United Claims Specialists can help you evaluate your property damage, file your storm damage insurance claim and get you the maximum payout.",
  "Storm Damage Insurance Claims",
  "PEOPLE WHO USE A PUBLIC ADJUSTER TO MANAGE THEIR CLAIM HAVE A 700% HIGHER PAYMENT, ON AVERAGE.",
  bullets=[
    "Eliminate the headaches of dealing with insurance",
    "Make sure your claim gets submitted correctly and approved",
    "Ensure you get ALL damage covered",
    "Expedite repairs and payment",
    "Maximize your coverage and get the largest payout possible",
  ],
  body_paras=[
    "Storm damage and natural disasters are happening more often and are stronger than ever. United Claims Specialists can help you evaluate your property damage, file your storm damage insurance claim and get you the maximum payout from your property or homeowners insurance.",
    "Storm damage happens to 8 out of 10 homeowners at some point during their homeownership. Dealing with the insurance company is confusing, complicated, stressful and often doesn't provide a big enough payout for repairs.",
    "An insurance adjuster works for the insurance! They oftentimes write lower estimates than the contractors you hire for repairs, making you think you need to pay out of pocket.",
    "Your insurance company will try to pay as little as possible for your claim and may not cover all the damages. People who use a public adjuster get 700% higher payouts, on average.",
    "According to Florida state law, if 25% of your roof is damaged, your whole roof must be replaced. Insurances often argue that your roof is just under 25% damaged - we make sure you're covered.",
    "Denied claims are more common than you may think. Insurances have the rights to deny claims based on installation, design or construction errors. Our experts know how to file storm damage claims to avoid denials.",
  ],
  do_items=["Make a list of everything damaged.", "Take pictures & video of all wind damage.", "Contact UCS for immediate inspection."],
  dont_items=["Avoid moving or disturbing the debris and damage before an insurance adjuster arrives.", "Do not make any repairs before an insurance adjuster arrives.", "Do not submit a claim without a public adjuster to guide you!"],
  faq_pairs=[
    ("Do I really need a storm and hurricane damage insurance claims public adjuster?",
     "Your insurance company has years of experience in working with claims. But, the average home or business owner does not have this much experience with claims processes. This is why it's crucial to hire a storm and hurricane damage insurance claims adjuster. Our knowledgeable public adjusters at United Claims Specialists understand how to fight for your claim. We know the tricks insurance companies use to deny or underpay storm damage claims, and we know how to work at making the most of your claim."),
    ("What can a certified public adjuster do for my claim?",
     "When you're dealing with storm damage claims, it's all too easy to feel alone. Policyholders are left to the mercy of insurance companies, but a certified public adjuster from our team at United Claims Specialists can help level the playing field. Insurance processes can be confusing and difficult to navigate. Our storm and hurricane damage insurance claims public adjusters are here to help fight for your claim. We understand the insurance processes and runarounds, and we know how to navigate claims on your behalf. If you are ready to get the maximum settlement for your storm damage claim, it's time to call our team at United Claims Specialists for your no cost, no obligation consultation."),
  ],
)

# Batch of similar damage pages with unique leads from live
DAMAGE_PAGES = [
  ("hurricane-damage", "Hurricane Damage", "If your home or business has hurricane damage, contact our public adjusters today! We're experts at managing property damage claims. We'll inspect the damage, file your hurricane damage insurance claim, and negotiate payment so that you can get the best recovery - as quickly as possible."),
  ("tornado-damage-insurance-claims", "Tornado Damage", "If your home or business has recently been damaged by a tornado contact our public adjusters today! We're experts at managing tornado damage insurance claims. We'll inspect the damage, file your claim, and negotiate payment so that you can get the maximum payout- fast!"),
  ("hail-damage-insurance-claims", "Hail Damage", "Most homeowners are shocked to see the destruction following a storm and are even more shocked to find that their insurance provider isn't willing to cover the full cost of repairs. The next time hail comes crashing down on your property, contact the skilled public adjusters at United Claims Specialists."),
  ("wind-damage-insurance-claims", "Wind Damage", "If your home or business has recently been through a storm and received wind or other impact damage, contact our public adjusters today! We're experts at managing property damage claims from wind and other severe storms. We'll inspect the damage, file your claim, and negotiate payment so that you can get the maximum payout- fast!"),
  ("flood-damage", "Flood Damage", "Flooding damage is more common than many people realize. Whether it's the rainy season or dry season, many properties are one major storm away from flood damage. Has your property been damaged by flooding? If so, your next step should be to call a public adjuster for flood damage claims. At United Claims Specialists, we offer comprehensive services for residential and commercial claims regarding flood damage."),
  ("water-damage", "Water Damage", "DON'T LET WATER DAMAGE KEEP YOU DOWN. We're experts at managing water damage insurance claims. We'll inspect the water damaged area, file your claim, and negotiate payment so that you can get the maximum payout- fast!"),
  ("mold-damage-insurance-claims", "Mold Damage", "Mold damage can seriously impact your health. Some mold damage is covered by your homeowners insurance or property insurance. United Claims Specialists can help you evaluate your mold damage, file your mold insurance claim and get you the maximum payout for repairs."),
  ("fire-damage-insurance-claims", "Fire Damage", "Fire damage can be devastating. We've seen it destroy entire towns. Even smaller fires can cause significant damage along with the smoke. United Claims Specialists can help you evaluate your property damage, file your fire damage insurance claim and get you the maximum payout from your property or homeowners insurance."),
  ("wildfire-damage", "Wildfire Damage", "We're experts at managing wildfire property damage claims. We'll inspect the damage, file your claim, and negotiate payment so that you can get the maximum payout!"),
  ("roof-leak", "Roof Leak", "Roof leaks and roof damage can happen from all types of storms as well as wear-and-tear. United Claims Specialists can help you evaluate your roof leak damage, file your roof insurance claim and get you the maximum payout from your homeowners or property insurance."),
  ("income-loss", "Income Loss", "At United Claims Specialists we know that you want to get your business back up and running as quickly as possible. During the time that your business was down, you've experienced income loss. It's important that you document income loss and get the proper settlement for your insurance claim."),
  ("accidental-damage", "Accidental Damage", "There are many different types of accidental damage claims, and no matter the claim, you need a skilled public adjuster to make the most of your claim."),
  ("theft-vandalism-damage", "Theft & Vandalism Damage", "Burglaries cause many types of damages, such as structural damages and property losses. Luckily, many homeowners and residential insurance policies offer coverage for burglaries."),
]

for slug, name, lead in DAMAGE_PAGES:
    if slug == "water-damage":
        # richer content from fetch
        service_page(
          slug, f"{name} Insurance Claims | United Claims Specialists", lead[:140],
          "DON'T LET WATER DAMAGE KEEP YOU DOWN",
          "We're experts at managing water damage insurance claims. We'll inspect the water damaged area, file your claim, and negotiate payment so that you can get the maximum payout- fast!",
          bullets=["Eliminate the headaches of dealing with insurance","Make sure your claim gets submitted correctly and approved","Ensure you get ALL water damage covered","Expedite repairs and payment","Maximize your coverage and get the largest payout possible"],
          body_paras=[
            "Water damage is the most common type of insurance claim filed. If you have water damage, whether you have a new claim or you're working with an existing claim, it's time to call a water damage insurance claim public adjuster. Our adjusters at United Claims Specialists are experts at getting you paid. A skilled public adjuster is crucial for your insurance claim to be approved and paid.",
            "At United Claims Specialists, we understand how catastrophic even the smallest water damages can be. There are many sources of water damage, including: Faulty appliances, Pipe bursts, Cracked foundation, Toilet & pipe clogs, Roof leaks, Storm damage, Flooding.",
            "These damages can be costly to repair, but a skilled water damage insurance claim adjuster can help with your claim. Our adjusters at United Claims Specialists will work to obtain the highest payment for your water damage claim. We understand the insurance processes and red tape, and we know how to work to make the most of claims for our clients.",
            "At United Claims Specialists, we work for you, the policyholder. We work with all types of water damage claims. Clean water, gray water containing biological contaminants and black water that contains bacteria all cause different damage situations. No matter your type of water damage, a knowledgeable public adjuster is critical.",
          ],
          do_items=["Make a list of everything damaged.","Take pictures & video of all water damage.","Contact UCS for immediate inspection."],
          dont_items=["Avoid moving or disturbing the debris and damage before an insurance adjuster arrives.","Do not make any repairs before an insurance adjuster arrives.","Do not submit a claim without a public adjuster to guide you!"],
          faq_pairs=[
            ("What will my policy cover?", "Each policy is unique to the property owner. At United Claims Specialists, our public adjusters understand how to maximize your policy for your claim. Some policies cover open perils, all risk or comprehensive situations. These types of policies may cover water damage caused by storms or roofing issues. Other policies or independent flood coverage may address varying types of water damage."),
            ("How else can water damage insurance claims adjusters help me?", "The processes behind insurance claims can be daunting, especially when water and mold damage are involved. A knowledgeable public adjuster from our team at United Claims Specialists can make all the difference with your claim and claims process. We're here to bring ease to your processes along with maximum payments. We offer no cost, no obligation consultations. Call our expert water damage claims adjusters today to schedule your consultation. Even if you have an existing claim, we are here to help.."),
          ],
        )
        continue
    service_page(
      slug,
      f"{name} Insurance Claims | United Claims Specialists",
      lead[:155],
      f"{name} Insurance Claims",
      lead,
      bullets=["Eliminate the headaches of dealing with insurance","Make sure your claim gets submitted correctly and approved","Ensure you get ALL damage covered","Expedite repairs and payment","Maximize your coverage and get the largest payout possible"],
      body_paras=[
        lead,
        "An insurance adjuster works for the insurance! They oftentimes write lower estimates than the contractors you hire for repairs, making you think you need to pay out of pocket.",
        "Your insurance company will try to pay as little as possible for your claim and may not cover all the damages. People who use a public adjuster get 700% higher payouts, on average.",
        "Denied claims are more common than you may think. Insurances have the rights to deny claims based on installation, design or construction errors. Our experts know how to file claims to avoid denials.",
      ],
      do_items=["Make a list of everything damaged.","Take pictures & video of all damage.","Contact UCS for immediate inspection."],
      dont_items=["Avoid moving or disturbing the debris and damage before an insurance adjuster arrives.","Do not make any repairs before an insurance adjuster arrives.","Do not submit a claim without a public adjuster to guide you!"],
    )

# Fix hail nav slug - update chrome already has hail-damage/; create redirect-style page at hail-damage too
service_page(
  "hail-damage",
  "Hail Damage Insurance Claims | United Claims Specialists",
  "Hail damage homeowners insurance claims help from United Claims Specialists.",
  "Hail Damage Insurance Claims",
  "Most homeowners are shocked to see the destruction following a storm and are even more shocked to find that their insurance provider isn't willing to cover the full cost of repairs.",
  bullets=["Eliminate the headaches of dealing with insurance","Ensure you get ALL hail damage covered","Maximize your coverage and get the largest payout possible"],
  body_paras=[
    "Most homeowners are shocked to see the destruction following a storm and are even more shocked to find that their insurance provider isn't willing to cover the full cost of repairs.",
    "The best part about working with a hail damage public adjuster is there's no risk! We only get paid if we get you paid so call with confidence knowing that your claim compensation will be arriving shortly. A public adjuster works for you first and foremost, not your insurance provider. Our goal is to get you compensation for hail damage from a reluctant insurance company.",
  ],
)

print("Damage pages done")
