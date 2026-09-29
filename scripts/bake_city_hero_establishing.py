#!/usr/bin/env python3
"""Bake city-hero establishing frames: height-fit ZOOM (default 0.80) + mild-blur fill.

Usage:
  python3 bake_city_hero_establishing.py SRC.jpg OUT.jpg [--zoom 0.80] [--size 1920x960]
"""
from __future__ import annotations
import argparse
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance

def bake(src: Path, dest: Path, zoom: float = 0.80, size=(1920, 960), blur: int = 28) -> None:
    W, H = size
    img = Image.open(src).convert("RGB")
    sw, sh = img.size
    cover = max(W / sw, H / sh)
    bw, bh = int(round(sw * cover)), int(round(sh * cover))
    back = img.resize((bw, bh), Image.Resampling.LANCZOS)
    left, top = (bw - W) // 2, (bh - H) // 2
    back = back.crop((left, top, left + W, top + H))
    back = ImageEnhance.Brightness(back.filter(ImageFilter.GaussianBlur(radius=blur))).enhance(0.92)
    scale = (H * zoom) / sh
    fw, fh = int(round(sw * scale)), int(round(sh * scale))
    fore = img.resize((fw, fh), Image.Resampling.LANCZOS)
    ox, oy = (W - fw) // 2, (H - fh) // 2
    if fw > W:
        x0 = (fw - W) // 2
        fore = fore.crop((x0, 0, x0 + W, fh))
        ox = 0
    canvas = back.copy()
    canvas.paste(fore, (ox, oy))
    dest.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dest, "JPEG", quality=88, optimize=True, progressive=True)
    print(f"OK {dest} {canvas.size} zoom={zoom}")

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src", type=Path)
    ap.add_argument("dest", type=Path)
    ap.add_argument("--zoom", type=float, default=0.80)
    ap.add_argument("--size", default="1920x960")
    ap.add_argument("--blur", type=int, default=28)
    args = ap.parse_args()
    w, h = map(int, args.size.lower().split("x"))
    bake(args.src, args.dest, zoom=args.zoom, size=(w, h), blur=args.blur)

if __name__ == "__main__":
    main()
