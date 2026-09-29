#!/usr/bin/env python3
"""DRAFT — live HubSpot social fix for UCS header/footer (portal 20198825).

STATUS: NOT PUBLISHED. Parent must confirm before running with --apply.

Findings (2026-09-29, public HTML + CMS source-code API via chrome-cookie-seed / CDP 9230):
  LIVE header+footer socials today:
    - Facebook  https://www.facebook.com/UnitedClaimsSpecialistsFL
    - Twitter   https://twitter.com/ucs_pa   (old bird URL + Twitter-Green.png / FA Twitter glyph)
    - LinkedIn  https://www.linkedin.com/company/united-claims-specialists/
    - Instagram MISSING
    - YouTube / TikTok / etc. NOT present on live (do not invent)

Target (Joe):
    - X         https://x.com/UCS_PA   (site UCS_PA — NOT Joe personal @JoeDirect77)
    - Instagram https://www.instagram.com/ucs.pa/
    - Facebook / LinkedIn unchanged
    - X branding (not Twitter bird)

Exact modules / files (portal 20198825):
  Header (global module, hasGlobalContent=true):
    id   50485963365
    path /UCS - Theme/modules/Header Section - UCS
    partial UCS - Theme/templates/partials/header.html
      -> module_162883720295314
    source  UCS - Theme/modules/Header Section - UCS.module/module.html
    fields  locked group icon_group (image + link)

  Footer (global module, hasGlobalContent=true):
    id   50694621511
    path /United Claims Specialists/Custom Modules/Footer Section - UCS
    partial UCS - Theme/templates/partials/footer.html
      -> module_162883581065366
    source  .../Footer Section - UCS.module/module.html
    fields  locked group social_icon_group (FA icon + link)

Why source-level draft (same pattern as STATUS-FOOTER-DAMAGE-ASSESSMENT-20260929):
  Social URL values live in locked global-module content. Hardcoding the four links
  in module.html is the reliable published fix path.

Auth: CDP 9230 cookie refresh -> PUT
  https://app.hubspot.com/api/cms/v3/source-code/published/content/<path>?portalId=20198825

Also upload File Manager assets before apply:
  Home Page/X-Green.png , Home Page/Instagram-Green.png
  (preview drafts: assets/img/social/)

Usage:
  python3 DRAFT-fix-LIVE-SOCIALS-20260929.py            # dry-run
  CONFIRM_LIVE_SOCIAL_FIX=1 python3 ... --apply           # PUT (parent confirm required)
"""
from __future__ import annotations

import json, os, re, sys, time, urllib.request, urllib.error, urllib.parse
from pathlib import Path

PORTAL = "20198825"
SEED = Path("/home/box/agent-data/chrome-cookie-seed.json")
CDP_COOKIES = Path("/tmp/hs-cookies-from-cdp.json")
OUT = Path(__file__).resolve().parent
STAMP = time.strftime("%Y%m%d-%H%M%S")
BAK = OUT / f"social-fix-backup-{STAMP}"

HEADER_PATH = "UCS - Theme/modules/Header Section - UCS.module/module.html"
FOOTER_PATH = "United Claims Specialists/Custom Modules/Footer Section - UCS.module/module.html"

SOCIALS = [
  ("facebook", "https://www.facebook.com/UnitedClaimsSpecialistsFL",
   "https://www.ucspa.com/hubfs/Home%20Page/facebook-Green.png", "Facebook"),
  ("x", "https://x.com/UCS_PA",
   "https://www.ucspa.com/hubfs/Home%20Page/X-Green.png", "X (formerly Twitter)"),
  ("instagram", "https://www.instagram.com/ucs.pa/",
   "https://www.ucspa.com/hubfs/Home%20Page/Instagram-Green.png", "Instagram"),
  ("linkedin", "https://www.linkedin.com/company/united-claims-specialists/",
   "https://www.ucspa.com/hubfs/Home%20Page/LinkedIn-Green.png", "LinkedIn"),
]

SVGS = {
  "facebook": '<svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512" aria-hidden="true"><path d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"/></svg>',
  "x": '<svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" aria-hidden="true"><path d="M389.2 48h70.6L305.6 224.2 487 464H345L233.7 318.6 106.5 464H35.8L200.7 275.5 26.8 48H172.4L272.9 180.9 389.2 48zM364.4 421.8h39.1L151.1 88h-42L364.4 421.8z"/></svg>',
  "instagram": '<svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" aria-hidden="true"><path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/></svg>',
  "linkedin": '<svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" aria-hidden="true"><path d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"/></svg>',
}


def load_auth():
  cookies = []
  if CDP_COOKIES.exists():
    cookies = json.loads(CDP_COOKIES.read_text()).get("cookies") or []
  if not cookies and SEED.exists():
    d = json.loads(SEED.read_text())
    cookies = [c for c in d.get("cookies", []) if "hubspot" in (c.get("domain") or "").lower()]
  csrf = next(c["value"] for c in cookies if c["name"] in ("hubspotapi-csrf", "csrf.app"))
  cookie_hdr = "; ".join(f"{c['name']}={c['value']}" for c in cookies)
  return cookie_hdr, csrf


def api(method, url, body=None, content_type=None):
  cookie_hdr, csrf = load_auth()
  headers = {
    "Cookie": cookie_hdr,
    "X-HubSpot-CSRF-hubspotapi": csrf,
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0",
    "Origin": "https://app.hubspot.com",
    "Referer": f"https://app.hubspot.com/design-manager/{PORTAL}",
  }
  if content_type:
    headers["Content-Type"] = content_type
  req = urllib.request.Request(url, data=body, headers=headers, method=method)
  try:
    with urllib.request.urlopen(req, timeout=120) as resp:
      return resp.status, resp.read()
  except urllib.error.HTTPError as e:
    return e.code, e.read()


def src_url(path: str) -> str:
  q = urllib.parse.quote(path, safe="/")
  return f"https://app.hubspot.com/api/cms/v3/source-code/published/content/{q}?portalId={PORTAL}"


def fetch(path: str) -> bytes:
  st, raw = api("GET", src_url(path))
  if st != 200:
    raise SystemExit(f"GET {path} -> {st}: {raw[:300]}")
  return raw


def put(path: str, raw: bytes) -> int:
  st, body = api("PUT", src_url(path), body=raw, content_type="text/html")
  print(f"PUT {path} -> {st} {body[:120]!r}")
  return st


def build_header_module_html(existing: str) -> str:
  items = []
  for _k, href, src, alt in SOCIALS:
    items.append(
      "\n            <li>\n"
      f'            <a href="{href}" target="_blank" rel="noopener">\n'
      f'              <img src="{src}" alt="{alt}" loading="lazy" style="max-width: 100%; height: auto;">\n'
      "            </a>\n            </li>"
    )
  new_ul = "<ul>\n" + "\n".join(items) + "\n          </ul>"
  pat = re.compile(
    r'(<div class="Header-Top-Right">\s*)\{%\s*for item in module\.icon_group\s*%\}.*?\{%\s*endfor\s*%\}\s*</ul>',
    re.S,
  )
  if pat.search(existing):
    return pat.sub(r"\1" + new_ul, existing, count=1)
  pat2 = re.compile(r'(<div class="Header-Top-Right">\s*)<ul>.*?</ul>', re.S)
  if pat2.search(existing):
    return pat2.sub(r"\1" + new_ul, existing, count=1)
  raise SystemExit("Could not locate Header-Top-Right social list in header module.html")


def build_footer_module_html(existing: str) -> str:
  items = []
  for key, href, _src, _alt in SOCIALS:
    items.append(
      "\n            <li>\n"
      f'              <a href="{href}" target="_blank" rel="noopener">\n'
      f"                {SVGS[key]}\n"
      "              </a>\n            </li>"
    )
  new_ul = "<ul>\n" + "\n".join(items) + "\n            </ul>"
  pat = re.compile(
    r'(<div class="Footer-Row-Icons">\s*)\{%\s*for item in module\.social_icon_group\s*%\}.*?\{%\s*endfor\s*%\}\s*</ul>',
    re.S,
  )
  if pat.search(existing):
    return pat.sub(r"\1" + new_ul, existing, count=1)
  pat2 = re.compile(r'(<div class="Footer-Row-Icons">\s*)<ul>.*?</ul>', re.S)
  if pat2.search(existing):
    return pat2.sub(r"\1" + new_ul, existing, count=1)
  raise SystemExit("Could not locate Footer-Row-Icons social list in footer module.html")


def main():
  apply = "--apply" in sys.argv
  if apply and os.environ.get("CONFIRM_LIVE_SOCIAL_FIX") != "1":
    print("Refusing --apply without CONFIRM_LIVE_SOCIAL_FIX=1 (parent must confirm).")
    sys.exit(2)

  BAK.mkdir(parents=True, exist_ok=True)
  header_before = fetch(HEADER_PATH)
  footer_before = fetch(FOOTER_PATH)
  (BAK / "header.module.html.before").write_bytes(header_before)
  (BAK / "footer.module.html.before").write_bytes(footer_before)

  header_after = build_header_module_html(header_before.decode("utf-8", "replace"))
  footer_after = build_footer_module_html(footer_before.decode("utf-8", "replace"))
  (BAK / "header.module.html.after").write_text(header_after)
  (BAK / "footer.module.html.after").write_text(footer_after)

  summary = {
    "stamp": STAMP,
    "apply": apply,
    "socials": [{"key": k, "href": h} for k, h, *_ in SOCIALS],
    "files": [HEADER_PATH, FOOTER_PATH],
    "modules": {
      "header_id": 50485963365,
      "footer_id": 50694621511,
      "header_partial_module": "module_162883720295314",
      "footer_partial_module": "module_162883581065366",
    },
    "note": "Upload X-Green.png + Instagram-Green.png to hubfs Home Page/ before/with apply.",
    "published": False,
  }
  (BAK / "draft-summary.json").write_text(json.dumps(summary, indent=2))
  print("Backups + after drafts ->", BAK)

  if not apply:
    print("Dry-run only. Re-run with CONFIRM_LIVE_SOCIAL_FIX=1 --apply after parent confirms.")
    return

  st1 = put(HEADER_PATH, header_after.encode("utf-8"))
  st2 = put(FOOTER_PATH, footer_after.encode("utf-8"))
  summary["published"] = st1 == 200 and st2 == 200
  summary["puts"] = {"header": st1, "footer": st2}
  (BAK / "result.json").write_text(json.dumps(summary, indent=2))
  print("DONE published=", summary["published"])


if __name__ == "__main__":
  main()
