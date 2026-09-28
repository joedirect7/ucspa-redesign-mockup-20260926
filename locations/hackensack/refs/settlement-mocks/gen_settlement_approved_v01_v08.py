#!/usr/bin/env python3
"""UCS settlement boards approved-v01–v08 — LOCKED v58 craft; peril photos only swap."""
from __future__ import annotations

import importlib.util
from pathlib import Path

OUT = Path("/workspace/ucs-content/marketing/city-pages-mockup/refs/settlement-mocks")
EXTRACTS = OUT / "_peril-extracts"

# Reuse locked craft from v58 generator (diagonal, check wording, Hancock, FIT, logo)
spec = importlib.util.spec_from_file_location(
    "gen_v58", OUT / "gen_settlement_v58_v64.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def main():
    sig = mod.make_hancock_stamp()
    sig.save(OUT / "_sig-stamp-hancock.png")

    boards = [
        dict(
            peril=EXTRACTS / "fit-approved-water-living-cascade-alt.png",
            amount_k="$245K",
            amount_full="$245,000.00",
            peril_label="WATER DAMAGE · RESIDENTIAL",
            memo="WATER DAMAGE CLAIM",
            check_no="1101",
            out="approved-v01-water-245k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-approved-pipe-bathroom.png",
            amount_k="$76K",
            amount_full="$76,000.00",
            peril_label="WATER DAMAGE · RESIDENTIAL",
            memo="PIPE BURST CLAIM",
            check_no="1108",
            out="approved-v02-pipe-bath-76k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-approved-kitchen-fire.png",
            amount_k="$198K",
            amount_full="$198,000.00",
            peril_label="FIRE DAMAGE · RESIDENTIAL",
            memo="FIRE DAMAGE CLAIM",
            check_no="1115",
            out="approved-v03-fire-198k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-approved-wind-tree-living.png",
            amount_k="$165K",
            amount_full="$165,000.00",
            peril_label="WIND DAMAGE · RESIDENTIAL",
            memo="WIND DAMAGE CLAIM",
            check_no="1122",
            out="approved-v04-wind-165k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-approved-condo-flood.png",
            amount_k="$318K",
            amount_full="$318,000.00",
            peril_label="WATER DAMAGE · CONDO",
            memo="UNIT FLOOD CLAIM",
            check_no="1130",
            out="approved-v05-condo-flood-318k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-approved-master-ceiling.png",
            amount_k="$112K",
            amount_full="$112,000.00",
            peril_label="WATER DAMAGE · RESIDENTIAL",
            memo="CEILING COLLAPSE CLAIM",
            check_no="1137",
            out="approved-v06-bedroom-ceiling-112k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-approved-garage-flood.png",
            amount_k="$48K",
            amount_full="$48,000.00",
            peril_label="WATER DAMAGE · RESIDENTIAL",
            memo="WATER DAMAGE CLAIM",
            check_no="1144",
            out="approved-v07-garage-flood-48k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-approved-attic-roof-leak.png",
            amount_k="$401K",
            amount_full="$401,000.00",
            peril_label="WATER DAMAGE · RESIDENTIAL",
            memo="ROOF LEAK CLAIM",
            check_no="1151",
            out="approved-v08-attic-leak-401k.png",
        ),
    ]

    # Bonus 9th still available (laundry) — not in primary 8 filenames
    for b in boards:
        assert b["peril"].exists(), b["peril"]
        mod.build_board(
            b["peril"],
            b["amount_k"],
            b["amount_full"],
            b["peril_label"],
            b["memo"],
            b["check_no"],
            b["out"],
            sig,
        )

    # Proof crop from approved-v01 (same check craft as v58)
    from PIL import Image
    v01 = Image.open(OUT / "approved-v01-water-245k.png")
    crop = v01.crop((830, 155, 1260, 700))
    crop.save(OUT / "approved-v01-check-crop.png")
    print("wrote approved-v01-check-crop.png", crop.size)


if __name__ == "__main__":
    main()
