#!/usr/bin/env python3
"""UCS settlement diagonal boards v51–v57 — Hancock sig + FIT full-scene perils."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np

OUT = Path("/workspace/ucs-content/marketing/city-pages-mockup/refs/settlement-mocks")
EXTRACTS = OUT / "_peril-extracts"
LOGO = Path("/workspace/ucs-content/marketing/brand/ucs-logo-3d/ucs-3d-horizontal-dark-keyed.png")

W, H = 1280, 720
LIME = (182, 255, 65)
WHITE = (255, 255, 255)
DARK = (12, 12, 14)
CHECK_INK = (20, 20, 24)
MUTED = (170, 175, 180)
SIG_BLUE = (25, 60, 155)

FONT_DIR = Path("/usr/share/fonts/truetype/sand-box")
OSS = FONT_DIR / "custom/Open Sauce Sans"
HAND = FONT_DIR / "google/Homemade Apple/HomemadeApple-Regular.ttf"


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size=size)


def oss(weight: str, size: int) -> ImageFont.FreeTypeFont:
    name = {
        "bold": "OpenSauceSans-Bold.ttf",
        "extrabold": "OpenSauceSans-ExtraBold.ttf",
        "black": "OpenSauceSans-Black.ttf",
        "semibold": "OpenSauceSans-SemiBold.ttf",
        "regular": "OpenSauceSans-Regular.ttf",
        "medium": "OpenSauceSans-Medium.ttf",
        "light": "OpenSauceSans-Light.ttf",
    }[weight]
    return font(OSS / name, size)


def make_hancock_stamp(width: int = 380, height: int = 90) -> Image.Image:
    """Readable 'J. Hancock' in realistic human cursive, transparent bg."""
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    f = font(HAND, 64)
    text = "J. Hancock"
    bbox = draw.textbbox((0, 0), text, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (width - tw) // 2 - bbox[0]
    y = (height - th) // 2 - bbox[1] - 2
    # crisp ink (avoid huge translucent wash)
    draw.text((x, y), text, font=f, fill=(*SIG_BLUE, 255))
    # tiny secondary stroke for pen weight
    draw.text((x + 1, y), text, font=f, fill=(*SIG_BLUE, 90))
    # trim to opaque bbox
    a = np.array(canvas)
    ys, xs = np.where(a[:, :, 3] > 20)
    if len(xs):
        pad = 4
        canvas = canvas.crop(
            (
                max(0, xs.min() - pad),
                max(0, ys.min() - pad),
                min(width, xs.max() + pad + 1),
                min(height, ys.max() + pad + 1),
            )
        )
    return canvas


def fit_image(src: Image.Image, box_w: int, box_h: int, fill=(12, 12, 14)) -> Image.Image:
    """FIT full scene into the diagonal peril zone.

    Landscape sources: classic contain (letterbox falls under check).
    Square/tall sources: scale to fill ~peril width with only mild vertical
    trim so the wedge isn't a black band — still shows ceiling+furniture+floor.
    NEVER aggressive cover-zoom on the damage blob.
    """
    src = src.convert("RGB")
    sw, sh = src.size
    aspect = sw / sh
    box_aspect = box_w / box_h
    out = Image.new("RGB", (box_w, box_h), fill)

    if aspect >= 1.35:
        # Landscape like locked water — pure contain, left-align
        fitted = ImageOps.contain(src, (box_w, box_h), method=Image.Resampling.LANCZOS)
        out.paste(fitted, (0, (box_h - fitted.height) // 2))
        return out

    # Square / portrait: fill the peril wedge width (~62% of content) with light vertical trim
    target_w = min(box_w, int(box_w * 0.62))
    # Scale so width == target_w
    scale = target_w / sw
    new_h = int(sh * scale)
    scaled = src.resize((target_w, new_h), Image.Resampling.LANCZOS)
    if new_h <= box_h:
        out.paste(scaled, (0, (box_h - new_h) // 2))
    else:
        # Mild crop — bias slightly upward to keep ceiling in frame
        extra = new_h - box_h
        top = int(extra * 0.35)
        cropped = scaled.crop((0, top, target_w, top + box_h))
        out.paste(cropped, (0, 0))
    return out


def draw_check_into(
    base: Image.Image,
    origin: tuple[int, int],
    cw: int,
    ch: int,
    amount_str: str,
    memo: str,
    check_no: str,
    sig_stamp: Image.Image,
    content_left_visible: int,
) -> None:
    """
    Draw check graphics into base at origin covering cw x ch.
    content_left_visible = x offset within check where diagonal reveals check
    (so we right-align readable fields into the visible wedge).
    """
    layer = Image.new("RGB", (cw, ch), (248, 250, 252))
    draw = ImageDraw.Draw(layer)
    for y in range(0, ch, 3):
        draw.line([(0, y), (cw, y)], fill=(210, 218, 228), width=1)

    # Right-pad margin; left content starts near visible edge
    right = cw - 22
    # Keep important text in the visible right portion
    # Keep fields well inside visible check wedge (right of bottom diagonal)
    left = max(content_left_visible + 36, int(cw * 0.58))

    draw.text((left, 18), "Your Insurance Company", font=oss("bold", 20), fill=CHECK_INK)
    no_font = oss("regular", 13)
    no_txt = f"No. {check_no}"
    nb = draw.textbbox((0, 0), no_txt, font=no_font)
    draw.text((right - (nb[2] - nb[0]), 20), no_txt, font=no_font, fill=(90, 95, 105))

    draw.text((left, 58), "PAY TO THE ORDER OF", font=oss("semibold", 10), fill=(110, 115, 125))
    draw.text((left, 70), "Policyholder", font=oss("bold", 24), fill=CHECK_INK)

    # amount box near right
    box_w, box_h = 160, 38
    box_x = right - box_w
    box_y = 62
    draw.rectangle([box_x, box_y, box_x + box_w, box_y + box_h], outline=CHECK_INK, width=2)
    amt_font = oss("bold", 17)
    ab = draw.textbbox((0, 0), amount_str, font=amt_font)
    aw, ah = ab[2] - ab[0], ab[3] - ab[1]
    draw.text(
        (box_x + (box_w - aw) / 2, box_y + (box_h - ah) / 2 - 2),
        amount_str,
        font=amt_font,
        fill=CHECK_INK,
    )
    for t in range(3):
        draw.ellipse(
            [box_x - 10 - t, box_y - 8 - t, box_x + box_w + 10 + t, box_y + box_h + 8 + t],
            outline=(200, 30, 35),
            width=2,
        )

    draw.text((left, 120), f"MEMO: {memo}", font=oss("bold", 14), fill=CHECK_INK)

    # Signature line — flush bottom-right of visible check
    sig_y = ch - 52
    draw.text((left, sig_y - 6), "2025", font=oss("regular", 12), fill=(100, 105, 115))
    line_x0 = left + 20
    line_x1 = right
    draw.line([(line_x0, sig_y), (line_x1, sig_y)], fill=(30, 30, 35), width=2)
    lab = "Authorized Signature"
    lf = oss("regular", 11)
    lb = draw.textbbox((0, 0), lab, font=lf)
    draw.text((line_x1 - (lb[2] - lb[0]), sig_y + 5), lab, font=lf, fill=(90, 95, 105))

    # Hancock flush ON the line — right half of signature line so full name stays in wedge
    stamp = sig_stamp.copy()
    max_sw = min(260, int((line_x1 - line_x0) * 0.75))
    stamp.thumbnail((max_sw, 46), Image.Resampling.LANCZOS)
    sx = line_x1 - stamp.width - 8
    sy = sig_y - stamp.height + 12  # sit on line
    layer_rgba = layer.convert("RGBA")
    layer_rgba.alpha_composite(stamp, (sx, sy))
    base.paste(layer_rgba.convert("RGB"), origin)


def build_board(
    peril_path: Path,
    amount_k: str,
    amount_full: str,
    peril_label: str,
    memo: str,
    check_no: str,
    out_name: str,
    sig_stamp: Image.Image,
) -> Path:
    canvas = Image.new("RGB", (W, H), DARK)
    draw = ImageDraw.Draw(canvas)

    # Header
    title = "THE POLICY OWED. UCS RECOVERED."
    tf = oss("extrabold", 28)
    tb = draw.textbbox((0, 0), title, font=tf)
    draw.text(((W - (tb[2] - tb[0])) / 2, 18), title, font=tf, fill=WHITE)

    af = oss("black", 72)
    ab = draw.textbbox((0, 0), amount_k, font=af)
    draw.text(((W - (ab[2] - ab[0])) / 2, 48), amount_k, font=af, fill=LIME)

    sf = oss("semibold", 14)
    sb = draw.textbbox((0, 0), peril_label, font=sf)
    draw.text(((W - (sb[2] - sb[0])) / 2, 122), peril_label, font=sf, fill=MUTED)

    # Content frame
    fx0, fy0, fx1, fy1 = 22, 148, W - 22, H - 18
    draw.rectangle([fx0, fy0, fx1, fy1], outline=WHITE, width=2)
    ix0, iy0, ix1, iy1 = fx0 + 3, fy0 + 3, fx1 - 3, fy1 - 3
    cw, ch = ix1 - ix0, iy1 - iy0

    # ~60/40 diagonal (peril ≥60%)
    top_split = int(cw * 0.68)
    bot_split = int(cw * 0.54)

    peril_poly = [
        (ix0, iy0),
        (ix0 + top_split, iy0),
        (ix0 + bot_split, iy1),
        (ix0, iy1),
    ]
    check_poly = [
        (ix0 + top_split, iy0),
        (ix1, iy0),
        (ix1, iy1),
        (ix0 + bot_split, iy1),
    ]

    # FIT peril into full content, mask to diagonal
    peril_fitted = fit_image(Image.open(peril_path), cw, ch, fill=DARK)
    peril_layer = Image.new("RGB", (W, H), DARK)
    peril_layer.paste(peril_fitted, (ix0, iy0))
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).polygon(peril_poly, fill=255)
    canvas.paste(peril_layer, (0, 0), mask)

    # Check layer same size as content; fields right-aligned into visible wedge
    check_layer = Image.new("RGB", (W, H), DARK)
    # leftmost visible check x at top = top_split; use that as guide
    draw_check_into(
        check_layer,
        (ix0, iy0),
        cw,
        ch,
        amount_full,
        memo,
        check_no,
        sig_stamp,
        content_left_visible=bot_split,  # conservative: ensure fields clear of bottom diagonal
    )
    cmask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(cmask).polygon(check_poly, fill=255)
    canvas.paste(check_layer, (0, 0), cmask)

    # Diagonal separator
    draw = ImageDraw.Draw(canvas)
    draw.line([(ix0 + top_split, iy0), (ix0 + bot_split, iy1)], fill=WHITE, width=2)

    # UCS logo bottom-left of peril only
    logo = Image.open(LOGO).convert("RGBA")
    target_w = 210
    logo = logo.resize(
        (target_w, max(1, int(logo.height * target_w / logo.width))),
        Image.Resampling.LANCZOS,
    )
    lx, ly = ix0 + 14, iy1 - logo.height - 12
    logo_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    logo_layer.paste(logo, (lx, ly), logo)
    la = logo_layer.split()[-1]
    la = Image.composite(la, Image.new("L", (W, H), 0), mask)
    logo_layer.putalpha(la)
    canvas = Image.alpha_composite(canvas.convert("RGBA"), logo_layer).convert("RGB")

    out_path = OUT / out_name
    canvas.save(out_path, "PNG", optimize=True)
    print(f"wrote {out_path.name}")
    return out_path


def main():
    sig = make_hancock_stamp()
    sig.save(OUT / "_sig-stamp-hancock.png")

    boards = [
        dict(
            peril=EXTRACTS / "fit-water-cascade-sofa.png",
            amount_k="$287K",
            amount_full="$287,000.00",
            peril_label="WATER DAMAGE · RESIDENTIAL",
            memo="WATER DAMAGE CLAIM",
            check_no="1025",
            out="v51-water-287k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-water-living-full.png",
            amount_k="$94K",
            amount_full="$94,000.00",
            peril_label="WATER DAMAGE · RESIDENTIAL",
            memo="CEILING LEAK CLAIM",
            check_no="1038",
            out="v52-water-94k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-fire-lux-kitchen.png",
            amount_k="$168K",
            amount_full="$168,000.00",
            peril_label="FIRE DAMAGE · RESIDENTIAL",
            memo="FIRE DAMAGE CLAIM",
            check_no="1044",
            out="v53-fire-168k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-wind-tree-living.png",
            amount_k="$189K",
            amount_full="$189,000.00",
            peril_label="WIND DAMAGE · RESIDENTIAL",
            memo="WIND DAMAGE CLAIM",
            check_no="1052",
            out="v54-wind-189k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-pipe-nursery-full.png",
            amount_k="$142K",
            amount_full="$142,000.00",
            peril_label="WATER DAMAGE · RESIDENTIAL",
            memo="PIPE BURST CLAIM",
            check_no="1060",
            out="v55-pipe-142k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-fire-thanksgiving-full.png",
            amount_k="$425K",
            amount_full="$425,000.00",
            peril_label="FIRE DAMAGE · RESIDENTIAL",
            memo="FIRE DAMAGE CLAIM",
            check_no="1071",
            out="v56-fire-425k.png",
        ),
        dict(
            peril=EXTRACTS / "fit-wind-aftermath-full.png",
            amount_k="$72K",
            amount_full="$72,000.00",
            peril_label="WIND DAMAGE · RESIDENTIAL",
            memo="WIND DAMAGE CLAIM",
            check_no="1083",
            out="v57-wind-72k.png",
        ),
    ]

    for b in boards:
        assert b["peril"].exists(), b["peril"]
        build_board(
            b["peril"],
            b["amount_k"],
            b["amount_full"],
            b["peril_label"],
            b["memo"],
            b["check_no"],
            b["out"],
            sig,
        )

    v51 = Image.open(OUT / "v51-water-287k.png")
    crop = v51.crop((920, 575, 1255, 698))
    crop.save(OUT / "v51-sig-crop.png")
    print("wrote v51-sig-crop.png", crop.size)


if __name__ == "__main__":
    main()
