"""SI PAINT: paints a Blockbench box-UV texture PNG from a small JSON, no extra packages.

    python si_paint.py paint.json

paint.json: {"out": "models/fox_tex.png", "width": 64, "height": 64, "background": "#00000000",
             "rects": [{"x": 0, "y": 0, "w": 16, "h": 8, "color": "#e8792b", "noise": 0.08}]}
Each rect is a filled area (box-UV regions of a cube start at its uv_offset). "noise" adds a little
per-pixel shade variation (0 to 0.3) so flat colours look like Minecraft pixel art.
"""
import json
import random
import struct
import sys
import zlib


def rgba(hexcol):
    h = hexcol.lstrip("#")
    if len(h) == 6:
        h += "ff"
    return [int(h[i:i + 2], 16) for i in (0, 2, 4, 6)]


def write_png(path, w, h, px):
    raw = b"".join(b"\x00" + bytes(v for p in px[y * w:(y + 1) * w] for v in p) for y in range(h))

    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
                + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def main():
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    w, h = spec.get("width", 64), spec.get("height", 64)
    rnd = random.Random(spec.get("seed", 7))
    px = [rgba(spec.get("background", "#00000000"))] * (w * h)
    for r in spec["rects"]:
        base, n = rgba(r["color"]), float(r.get("noise", 0))
        for y in range(max(0, r["y"]), min(h, r["y"] + r["h"])):
            for x in range(max(0, r["x"]), min(w, r["x"] + r["w"])):
                k = 1 + rnd.uniform(-n, n)
                px[y * w + x] = [min(255, int(c * k)) for c in base[:3]] + [base[3]]
    write_png(spec["out"], w, h, px)
    print(f"painted {len(spec['rects'])} areas -> {spec['out']} ({w}x{h})")


if __name__ == "__main__":
    main()
