/* Home hero H1 rotation. Reads window.UCS_HERO_H1_POOL (content/hero-h1-pool.js).
   Picks one approved line for the America/New_York calendar day. */
(function (root) {
  var BANNED = /700\s*%|maximum payout|biggest payout|biggest possible payment/i;

  function nyDayIndex(date, timeZone) {
    var fmt = new Intl.DateTimeFormat("en-US", {
      timeZone: timeZone || "America/New_York",
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    });
    var parts = fmt.formatToParts(date);
    var y;
    var m;
    var d;
    for (var i = 0; i < parts.length; i++) {
      if (parts[i].type === "year") y = Number(parts[i].value);
      if (parts[i].type === "month") m = Number(parts[i].value);
      if (parts[i].type === "day") d = Number(parts[i].value);
    }
    return Math.floor(Date.UTC(y, m - 1, d) / 86400000);
  }

  function approvedLines(pool) {
    var raw = (pool && pool.lines) || [];
    var lines = [];
    for (var i = 0; i < raw.length; i++) {
      var line = String(raw[i]).trim();
      if (!line || BANNED.test(line)) continue;
      lines.push(line);
    }
    return lines;
  }

  function pickLine(lines, date, timeZone) {
    if (!lines || !lines.length) return "";
    var idx = nyDayIndex(date, timeZone);
    var n = lines.length;
    return lines[((idx % n) + n) % n];
  }

  function boot() {
    var pool = root.UCS_HERO_H1_POOL;
    if (!pool || (pool.cadence && pool.cadence !== "daily")) return;
    var nodes = document.querySelectorAll("[data-ucs-hero-h1]");
    if (!nodes.length) return;
    var line = pickLine(approvedLines(pool), new Date(), pool.timezone);
    if (!line) return;
    for (var i = 0; i < nodes.length; i++) nodes[i].textContent = line;
  }

  var api = { nyDayIndex: nyDayIndex, pickLine: pickLine, approvedLines: approvedLines, boot: boot };
  root.UCSHeroH1 = api;
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  if (typeof document !== "undefined") {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", boot);
    } else {
      boot();
    }
  }
})(typeof window !== "undefined" ? window : globalThis);
