# Home hero H1 pool

The home hero headline rotates once per **America/New_York** calendar day.
The soft-power panel and tag do not rotate.

Mockup only. Live HubSpot / ucspa.com is not part of this.

## Pool file

`content/hero-h1-pool.js`

Approved lines, in rotation order:

1. YOUR INSURANCE HAS AN ADJUSTER. SO SHOULD YOU.
2. YOUR CLAIM. OUR MISSION.

Rule: `dayIndex % lines.length`, where `dayIndex` is the America/New_York civil date as a UTC day number. Every visitor on that calendar day sees the same H1. Nothing is added automatically — only strings in `lines` can appear.

`scripts/build_all.py` reads this file (via `scripts/hero_h1.py`) and writes a rotation hook, not a single baked headline. `assets/js/hero-h1.js` applies the same rule in the browser, so GitHub Pages does not need a rebuild each day.

The hook is on the home page and the still / dissolve / video hero variants.

## Add a third H1

1. Open `content/hero-h1-pool.js`.
2. Append the new line to `lines` (comma after the previous string, no trailing comma after the last one):

```javascript
  "lines": [
    "YOUR INSURANCE HAS AN ADJUSTER. SO SHOULD YOU.",
    "YOUR CLAIM. OUR MISSION.",
    "THE NEW APPROVED HEADLINE."
  ],
```

3. Commit and push. The next page load uses the longer pool. No daily rebuild, and no edit to the HTML.

Appending keeps today’s index stable for the lines already in the list. Inserting or reordering changes which day shows which line.

Do not put candidate headlines in the HTML, in `scripts/build_all.py`, or on the panel. Retired lines (700%, maximum payout) are rejected by the loader.

## Stays fixed

- Panel: THE SETTLEMENT YOU DESERVE. WITHOUT THE HEADACHES.
- Tag: Lower stress. Higher settlement.
- Stats: Licensed · 8+ States served · 0 Upfront fees

Those live under `fixed` in the pool file so a regenerate keeps the same panel and tag. They are not part of the rotation.
