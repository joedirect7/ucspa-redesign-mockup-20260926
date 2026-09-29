#!/usr/bin/env python3
"""Bake city-hero frames: true ultrawide cover crop. NO blur-fill / edge letterbox.

Usage:
  python3 bake_city_hero_establishing.py SRC.jpg OUT.jpg [--size 1920x960]
  python3 bake_city_hero_establishing.py SRC.jpg OUT.jpg --extract-sharp   # strip baked blur sides first
"""
from __future__ import annotations
import argparse
from pathlib import Path
from PIL import Image
import numpy as np


def sharp_cols(img: Image.Image) -> np.ndarray:
    g = np.asarray(img.convert("L"), dtype=np.float32)
    # horizontal gradient magnitude per column
    dx = np.abs(g[:, 1:] - g[:, :-1])
    return dx.mean(axis=0)


def extract_sharp_region(img: Image.Image, floor_ratio: float = 0.22) -> Image.Image:
    """Drop near-zero-detail left/right blur pillars if present."""
    cols = sharp_cols(img)
    # pad to width
    cols = np.concatenate([cols[:1], cols])
    med = float(np.median(cols[len(cols)//4 : 3*len(cols)//4]))
    thr = max(med * floor_ratio, 1.0)
    good = np.where(cols >= thr)[0]
    if good.size < img.width * 0.35:
        return img  # can't confidently detect; leave alone
    # expand a bit
    x0 = max(0, int(good[0]) - 2)
    x1 = min(img.width, int(good[-1]) + 3)
    if (x1 - x0) < img.width * 0.4:
        return img
    return img.crop((x0, 0, x1, img.height))


def cover_bake(src: Path, dest: Path, size=(1920, 960), extract_sharp: bool = False) -> None:
    W, H = size
    img = Image.open(src).convert("RGB")
    if extract_sharp:
        img = extract_sharp_region(img)
    sw, sh = img.size
    scale = max(W / sw, H / sh)
    nw, nh = int(round(sw * scale)), int(round(sh * scale))
    resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left, top = (nw - W) // 2, (nh - H) // 2
    out = resized.crop((left, top, left + W, top + H))
    dest.parent.mkdir(parents=True, exist_ok=True)
    out.save(dest, "JPEG", quality=90, optimize=True, progressive=True)
    print(f"OK {dest} {out.size} from {sw}x{sh} extract_sharp={extract_sharp}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src", type=Path)
    ap.add_argument("dest", type=Path)
    ap.add_argument("--size", default="1920x960")
    ap.add_argument("--extract-sharp", action="store_true")
    # legacy no-ops so old callers don't break
    ap.add_argument("--zoom", type=float, default=None)
    ap.add_argument("--blur", type=int, default=None)
    args = ap.parse_args()
    w, h = map(int, args.size.lower().split("x"))
    cover_bake(args.src, args.dest, size=(w, h), extract_sharp=args.extract_sharp)


if __name__ == "__main__":
    main()
