"""Home hero H1 pool shared by generators and the static pages.

Source of truth: content/hero-h1-pool.js
The browser snippet (assets/js/hero-h1.js) uses the same day-index rule.
"""
from __future__ import annotations

import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
POOL_PATH = ROOT / "content" / "hero-h1-pool.js"

BANNED = re.compile(
    r"700\s*%|maximum payout|biggest payout|biggest possible payment",
    re.IGNORECASE,
)
_POOL_RE = re.compile(
    r"window\.UCS_HERO_H1_POOL\s*=\s*(\{.*\})\s*;",
    re.DOTALL,
)
_EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


def load_pool(path: Path | None = None) -> dict:
    """Load the approved pool. Rejects empty lists and retired loud headlines."""
    raw = (path or POOL_PATH).read_text(encoding="utf-8")
    match = _POOL_RE.search(raw)
    if not match:
        raise ValueError(f"No UCS_HERO_H1_POOL object in {path or POOL_PATH}")
    cfg = json.loads(match.group(1))
    if cfg.get("cadence") != "daily":
        raise ValueError("hero H1 pool cadence must be 'daily'")
    tz_name = cfg.get("timezone") or ""
    if not tz_name:
        raise ValueError("hero H1 pool timezone is required")
    ZoneInfo(tz_name)  # fail loud on a bad timezone name
    lines = []
    for line in cfg.get("lines") or []:
        text = str(line).strip()
        if not text:
            continue
        if BANNED.search(text):
            raise ValueError(f"hero H1 pool rejects retired headline: {text}")
        lines.append(text)
    if not lines:
        raise ValueError("hero H1 pool has no approved lines")
    fixed = cfg.get("fixed") or {}
    panel = str(fixed.get("panel") or "").strip()
    tag = str(fixed.get("tag") or "").strip()
    if not panel or not tag:
        raise ValueError("hero H1 pool fixed.panel and fixed.tag are required")
    if BANNED.search(panel) or BANNED.search(tag):
        raise ValueError("hero H1 fixed panel/tag must stay soft-power copy")
    cfg["lines"] = lines
    cfg["fixed"] = {"panel": panel, "tag": tag}
    return cfg


def ny_day_index(when: datetime, tz_name: str = "America/New_York") -> int:
    """UTC day number of the civil date in tz_name. Matches assets/js/hero-h1.js."""
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    local = when.astimezone(ZoneInfo(tz_name))
    civil = datetime(local.year, local.month, local.day, tzinfo=timezone.utc)
    return (civil - _EPOCH).days


def pick_line(lines: list[str], when: datetime | None = None, tz_name: str = "America/New_York") -> str:
    if not lines:
        raise ValueError("empty hero H1 pool")
    when = when or datetime.now(timezone.utc)
    idx = ny_day_index(when, tz_name)
    n = len(lines)
    return lines[((idx % n) + n) % n]


def hero_h1_markup() -> str:
    """Static fallback is the first approved line. The snippet swaps in today's."""
    cfg = load_pool()
    fallback = html.escape(cfg["lines"][0], quote=False)
    return f'<h1 data-ucs-hero-h1>{fallback}</h1>'


def hero_h1_scripts(prefix: str = "") -> str:
    pool = html.escape(f"{prefix}content/hero-h1-pool.js", quote=True)
    snippet = html.escape(f"{prefix}assets/js/hero-h1.js", quote=True)
    return (
        f'<script src="{pool}" defer></script>\n'
        f'<script src="{snippet}" defer></script>'
    )


def fixed_copy() -> dict:
    return load_pool()["fixed"]
