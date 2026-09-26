#!/usr/bin/env python3
"""Lock the home H1 pool and the America/New_York day rule (Python == JS)."""
from __future__ import annotations

import json
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

from hero_h1 import POOL_PATH, load_pool, ny_day_index, pick_line

ROOT = Path(__file__).resolve().parents[1]
HERO_PAGES = [
    ROOT / "index.html",
    ROOT / "hero-variants" / "still" / "index.html",
    ROOT / "hero-variants" / "dissolve" / "index.html",
    ROOT / "hero-variants" / "video" / "index.html",
]
PANEL = "THE SETTLEMENT YOU DESERVE. WITHOUT THE HEADACHES."
TAG = "Lower stress. Higher settlement."


def expect(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(msg)


def test_pool() -> None:
    cfg = load_pool()
    expect(
        cfg["lines"] == [
            "YOUR INSURANCE HAS AN ADJUSTER. SO SHOULD YOU.",
            "YOUR CLAIM. OUR MISSION.",
        ],
        f"unexpected pool: {cfg['lines']}",
    )
    expect(cfg["timezone"] == "America/New_York", "timezone")
    expect(cfg["cadence"] == "daily", "cadence")
    expect(cfg["fixed"]["panel"] == PANEL, "panel")
    expect(cfg["fixed"]["tag"] == TAG, "tag")


def test_day_rule() -> None:
    tz = "America/New_York"
    lines = load_pool()["lines"]
    # 04:00 UTC on 2026-09-26 is 00:00 EDT. One minute earlier is still the 25th.
    just_before = datetime(2026, 9, 26, 3, 59, tzinfo=timezone.utc)
    just_after = datetime(2026, 9, 26, 4, 0, tzinfo=timezone.utc)
    expect(ny_day_index(just_after, tz) - ny_day_index(just_before, tz) == 1, "midnight step")
    expect(pick_line(lines, just_before, tz) != pick_line(lines, just_after, tz), "adjacent days differ")
    same = datetime(2026, 9, 26, 18, 0, tzinfo=timezone.utc)
    expect(pick_line(lines, same, tz) == pick_line(lines, same.replace(hour=22), tz), "same NY day")
    # Two-line pool alternates, then wraps.
    day = just_after
    seen = [pick_line(lines, day + timedelta(days=i), tz) for i in range(4)]
    expect(seen[0] == seen[2] and seen[1] == seen[3] and seen[0] != seen[1], f"wrap {seen}")
    # Epoch: 1970-01-01 05:00 UTC is midnight EST.
    epoch = datetime(1970, 1, 1, 5, 0, tzinfo=timezone.utc)
    expect(ny_day_index(epoch, tz) == 0, f"epoch {ny_day_index(epoch, tz)}")
    before_epoch = datetime(1970, 1, 1, 4, 59, tzinfo=timezone.utc)
    expect(ny_day_index(before_epoch, tz) == -1, "day before epoch")
    expect(pick_line(lines, before_epoch, tz) == lines[-1], "negative index wraps")
    # DST fall-back 2026-11-01 stays on the same civil date.
    before_fallback = datetime(2026, 11, 1, 5, 30, tzinfo=timezone.utc)
    after_fallback = datetime(2026, 11, 1, 6, 30, tzinfo=timezone.utc)
    expect(
        ny_day_index(before_fallback, tz) == ny_day_index(after_fallback, tz),
        "DST fallback is one NY date",
    )


def test_js_matches() -> None:
    samples = [
        "1969-12-31T23:00:00Z",
        "1970-01-01T04:59:00Z",
        "1970-01-01T05:00:00Z",
        "2026-09-26T03:59:00Z",
        "2026-09-26T04:00:00Z",
        "2026-09-26T15:40:00Z",
        "2026-11-01T05:30:00Z",
        "2026-11-01T06:30:00Z",
        "2026-12-31T12:00:00Z",
    ]
    py = []
    lines = load_pool()["lines"]
    for iso in samples:
        when = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        py.append({
            "iso": iso,
            "day": ny_day_index(when),
            "line": pick_line(lines, when),
        })
    script = r"""
const h1 = require(process.argv[1]);
const lines = JSON.parse(process.argv[2]);
const samples = JSON.parse(process.argv[3]);
const out = samples.map((iso) => ({
  iso,
  day: h1.nyDayIndex(new Date(iso), "America/New_York"),
  line: h1.pickLine(lines, new Date(iso), "America/New_York"),
}));
process.stdout.write(JSON.stringify(out));
"""
    proc = subprocess.run(
        [
            "node",
            "-e",
            script,
            str(ROOT / "assets" / "js" / "hero-h1.js"),
            json.dumps(lines),
            json.dumps(samples),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    js = json.loads(proc.stdout)
    expect(js == py, f"JS/Python mismatch\njs={js}\npy={py}")


def test_pages() -> None:
    for path in HERO_PAGES:
        html = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        prefix = "" if rel == "index.html" else "../../"
        expect('data-ucs-hero-h1' in html, f"{rel} missing hook")
        expect(f'{prefix}content/hero-h1-pool.js' in html, f"{rel} missing pool script")
        expect(f'{prefix}assets/js/hero-h1.js' in html, f"{rel} missing rotator")
        expect(PANEL in html, f"{rel} panel changed")
        expect(TAG in html, f"{rel} tag changed")
        expect(">Licensed</strong>" in html, f"{rel} licensed stat")
        expect(">8+</strong>" in html and "States served" in html, f"{rel} states stat")
        expect(">0</strong>" in html and "Upfront fees" in html, f"{rel} fees stat")
        expect("700%" not in html and "MAXIMUM PAYOUT" not in html.upper(), f"{rel} loud headline")
        # Only the hero hook rotates; the panel h2 stays literal.
        expect(html.count("data-ucs-hero-h1") == 1, f"{rel} hook count")
    src = (ROOT / "scripts" / "build_all.py").read_text(encoding="utf-8")
    expect("hero_h1_markup()" in src and "hero_h1_scripts" in src, "generator hook")
    expect("<h1>YOUR INSURANCE HAS AN ADJUSTER" not in src, "generator baked a single H1")
    expect("700%" not in src and "MAXIMUM PAYOUT" not in src.upper(), "generator loud headline")
    expect(POOL_PATH.is_file(), "pool file")


if __name__ == "__main__":
    test_pool()
    test_day_rule()
    test_js_matches()
    test_pages()
    print("hero h1 rotation ok")
