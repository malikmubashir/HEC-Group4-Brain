"""Render Helium logo assets (PNG + SVG) with the 'lifted dot' motif.

Wordmark: 'Helium' set in a serif; the dot of the i is removed (dotless i) and
replaced by a circle in Helium Glow, floated higher than a normal tittle.
App icon: Glow rounded square, 'He' in Ink, with a Chalk lifted dot.
"""
import os
from PIL import Image, ImageDraw, ImageFont
import sys
sys.path.insert(0, os.path.dirname(__file__))
from helium_brand import PALETTE, hex_to_rgb

OUT = "/home/claude/helium-work/out/brand"
os.makedirs(OUT, exist_ok=True)
SERIF = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
SANS = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"


def wordmark(color_hex, bg_hex=None, fname="wordmark", size=400, with_tagline=False):
    font = ImageFont.truetype(SERIF, size)
    text = "Helıum"  # dotless i
    # measure
    tmp = Image.new("RGBA", (10, 10))
    d = ImageDraw.Draw(tmp)
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pad = int(size * 0.35)
    W, H = tw + 2 * pad, th + 2 * pad + (int(size * 0.45) if with_tagline else 0)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0) if bg_hex is None else hex_to_rgb(bg_hex) + (255,))
    d = ImageDraw.Draw(img)
    x0, y0 = pad - bbox[0], pad - bbox[1]
    d.text((x0, y0), text, font=font, fill=hex_to_rgb(color_hex))
    # locate the dotless i: measure prefix 'Hel' and 'Helı'
    pre = d.textbbox((x0, y0), "Hel", font=font)
    prei = d.textbbox((x0, y0), "Helı", font=font)
    i_left, i_right = pre[2], prei[2]
    # advance-based centre is more reliable than ink bbox
    adv_pre = font.getlength("Hel")
    adv_i = font.getlength("ı")
    cx = x0 + adv_pre + adv_i / 2 - int(size * 0.015)
    # x-height top approx: bbox of 'x'
    xb = d.textbbox((x0, y0), "x", font=font)
    cap = d.textbbox((x0, y0), "H", font=font)
    x_top = xb[1]
    cap_top = cap[1]
    r = int(size * 0.085)
    # lifted: sits above cap height, not at the usual tittle position
    cy = cap_top - int(size * 0.06)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=hex_to_rgb(PALETTE["glow"]))
    if with_tagline:
        tf = ImageFont.truetype(SANS, int(size * 0.17))
        tag = "Votre quotidien, plus léger."
        d.text((x0, pad + th + int(size * 0.14)), tag, font=tf, fill=hex_to_rgb(PALETTE["stone"]))
    img.save(os.path.join(OUT, f"{fname}.png"))
    return img


def app_icon(px=1024):
    img = Image.new("RGBA", (px, px), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    rad = int(px * 0.22)
    d.rounded_rectangle((0, 0, px - 1, px - 1), radius=rad, fill=hex_to_rgb(PALETTE["glow"]))
    font = ImageFont.truetype(SERIF, int(px * 0.56))
    text = "He"
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (px - tw) / 2 - bbox[0] - int(px * 0.04)
    y = (px - th) / 2 - bbox[1] + int(px * 0.04)
    d.text((x, y), text, font=font, fill=hex_to_rgb(PALETTE["ink"]))
    # lifted dot, chalk, above and right of the 'e'
    r = int(px * 0.045)
    cx, cy = x + tw + int(px * 0.045), y + int(px * 0.03)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=hex_to_rgb(PALETTE["chalk"]))
    img.save(os.path.join(OUT, "app_icon.png"))
    small = img.resize((256, 256), Image.LANCZOS)
    small.save(os.path.join(OUT, "app_icon_256.png"))
    return img


def svg_wordmark():
    """Designer-facing SVG; relies on the brand font being installed."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="1200" height="360">
  <title>Helium wordmark</title>
  <text x="40" y="270" font-family="Fraunces, Caladea, Georgia, serif" font-weight="700" font-size="300" fill="#{PALETTE['ink']}">Hel&#x131;um</text>
  <!-- lifted dot: replaces the tittle of the i, floats above cap height -->
  <circle cx="507" cy="38" r="26" fill="#{PALETTE['glow']}"/>
</svg>
"""
    with open(os.path.join(OUT, "wordmark.svg"), "w") as f:
        f.write(svg)


if __name__ == "__main__":
    wordmark(PALETTE["ink"], None, "wordmark_ink")
    wordmark(PALETTE["chalk"], PALETTE["ink"], "wordmark_on_ink")
    wordmark(PALETTE["ink"], PALETTE["chalk"], "wordmark_on_chalk_tagline", with_tagline=True)
    app_icon()
    svg_wordmark()
    print("assets written to", OUT, os.listdir(OUT))
