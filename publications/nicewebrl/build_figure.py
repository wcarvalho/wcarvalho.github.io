# /// script
# requires-python = ">=3.10"
# dependencies = ["Pillow>=10", "requests>=2.31"]
# ///
"""Build a shuffling GIF of every NiceWebRL environment image.

Reads the environments.csv from the NiceWebRL repo, downloads each
environment image (gif/png), pads each to a uniform canvas, and stitches
them into a single cycling GIF for the publications page.

Run:  uv run build_figure.py [--csv PATH] [--out PATH]
"""

from __future__ import annotations

import argparse
import csv
import io
import random
from pathlib import Path

import requests
from PIL import Image, ImageSequence

CANVAS = (480, 360)
BG = (252, 250, 250)  # matches nicewebrl home BG_MAIN
FRAME_MS = 700


def to_raw(url: str) -> str:
    if "github.com" in url and "/blob/" in url:
        url = url.replace("github.com", "raw.githubusercontent.com").replace(
            "/blob/", "/"
        )
    if "?raw=true" in url:
        url = url.replace("?raw=true", "")
    return url


def fetch(url: str) -> bytes | None:
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        return r.content
    except Exception as e:
        print(f"  skip ({e.__class__.__name__}): {url}")
        return None


def first_frame(data: bytes) -> Image.Image | None:
    try:
        im = Image.open(io.BytesIO(data))
    except Exception:
        return None
    frame = next(ImageSequence.Iterator(im)).convert("RGBA")
    return frame


def fit(frame: Image.Image) -> Image.Image:
    canvas = Image.new("RGB", CANVAS, BG)
    f = frame.copy()
    f.thumbnail(CANVAS, Image.LANCZOS)
    x = (CANVAS[0] - f.width) // 2
    y = (CANVAS[1] - f.height) // 2
    canvas.paste(f, (x, y), f if f.mode == "RGBA" else None)
    return canvas


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--csv",
        default="/tmp/nicewebrl/home/environments.csv",
        help="Path to NiceWebRL environments.csv",
    )
    parser.add_argument(
        "--out",
        default=str(Path(__file__).parent / "figure.gif"),
        help="Output GIF path",
    )
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        raise SystemExit(f"CSV not found: {csv_path}")

    urls: list[tuple[str, str]] = []
    with csv_path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = (row.get("environment_url") or "").strip()
            domain = (row.get("domain") or "").strip()
            env = (row.get("environment") or "").strip()
            label = f"{domain}: {env}" if env else domain
            if url:
                urls.append((label, to_raw(url)))

    if not urls:
        raise SystemExit("No environment_url entries found in CSV")

    random.seed(args.seed)
    random.shuffle(urls)

    frames: list[Image.Image] = []
    for label, url in urls:
        data = fetch(url)
        if data is None:
            continue
        frame = first_frame(data)
        if frame is None:
            print(f"  unreadable: {label}")
            continue
        frames.append(fit(frame))
        print(f"  ok: {label}")

    if not frames:
        raise SystemExit("No frames produced")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        out,
        save_all=True,
        append_images=frames[1:],
        duration=FRAME_MS,
        loop=0,
        optimize=True,
        disposal=2,
    )
    print(f"\nWrote {out} ({len(frames)} frames)")


if __name__ == "__main__":
    main()
