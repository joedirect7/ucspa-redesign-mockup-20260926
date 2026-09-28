# APPROVED FORMAT — UCS Settlement Board (locked from v58)

**Canonical lock:** `v58-water-287k.png`  
**Copies (identical bytes):**
- `APPROVED-FORMAT-v58-water-287k.png`
- `APPROVED-FORMAT-TEMPLATE.png`

Do **not** change layout or check craft. New boards only swap the peril still (property/peril only — **no humans**).

## Craft rules (immutable)

1. **Canvas:** 1280×720, solid dark bg `(12,12,14)`.
2. **Headline:** `THE POLICY OWED. UCS RECOVERED.` (white, Open Sauce ExtraBold ~28).
3. **Amount:** lime `$…K` (Open Sauce Black ~72), centered under headline.
4. **Peril label:** muted caps under amount (e.g. `WATER DAMAGE · RESIDENTIAL`).
5. **Frame:** white 2px rect; content inset; **diagonal** peril | check.
6. **Diagonal:** `TOP_SPLIT_FRAC=0.62` / `BOT_SPLIT_FRAC=0.58` → peril avg **≥60%**. Separator drawn 1px into peril (never overpaints check glyphs).
7. **Check wording fully visible** (safe left = `top_split + 70px` at top labels):
   - Your Insurance Company
   - PAY TO THE ORDER OF
   - Policyholder
   - Circled amount box
   - MEMO: …
   - Authorized Signature line + year `2025`
8. **Signature:** `J. Hancock` Homemade Apple cursive (`_sig-stamp-hancock.png`), flush **on** the Authorized Signature line (blue).
9. **Peril:** FIT full-scene into diagonal zone (never aggressive cover-zoom). Furnished sudden damage; **empty of people**.
10. **Logo:** UCS 3D horizontal dark-keyed, bottom-left of peril only (masked to peril polygon).

## Generator

- Craft source: `gen_settlement_v58_v64.py`
- Approved batch: `gen_settlement_approved_v01_v08.py` (imports v58 builders; swaps peril + amount + memo only)

## Peril stills policy

- Property / peril only — **NO humans, adjusters, clients, faces, silhouettes**
- Sudden damage in furnished rooms (not dilapidated / abandoned)
- Generate with `grok-imagine-image-2.0` (16:9); store as `fit-approved-*.png` under `_peril-extracts/`
- No Magnific upscale unless Joe asks

## QA checklist (every board)

- [ ] No humans in peril photo
- [ ] Check labels fully clear of diagonal
- [ ] Hancock cursive present on signature line
- [ ] Headline + lime amount + UCS logo BL of peril
- [ ] Memo matches peril type
