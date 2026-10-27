"""Helium brand constants shared by all generators (docx, pptx, xlsx, svg).

Palette story: the emission spectrum of helium. A helium discharge tube glows
peach-orange; its strongest visible line, D3, is yellow (587.6 nm). The
secondary green line sits at 501.6 nm. No blue, no purple: the AI clichés are
deliberately excluded.
"""

PALETTE = {
    "ink":        "201C19",   # primary text, dark surfaces (warm near-black)
    "chalk":      "F7F3EC",   # page and slide background
    "glow":       "F0916A",   # primary accent: helium glow (peach)
    "glow_deep":  "D9734F",   # pressed / emphasis state of glow
    "d3":         "E9C46A",   # secondary accent: the D3 yellow line
    "eucalyptus": "6B8F7A",   # tertiary accent, 501.6 nm green, used for "ok" states
    "stone":      "8A8178",   # mid neutral: captions, secondary text
    "linen":      "E4DDD2",   # light neutral: rules, table borders
    "mist":       "EFE9E0",   # subtle fill for table headers / callouts
    "white":      "FFFFFF",
}

FONTS = {
    # Brand typefaces (free, Google Fonts) with the fallbacks used in Office files
    "display": "Fraunces",     # headlines; fallback Georgia
    "display_fallback": "Georgia",
    "text": "Inter",           # body; fallback Arial
    "text_fallback": "Arial",
}

# Fonts actually written into generated Office files (must exist on any Mac/PC)
OFFICE_DISPLAY = "Georgia"
OFFICE_TEXT = "Arial"

BRAND = {
    "name": "Helium",
    "symbol": "He",
    "tagline_fr": "Votre quotidien, plus léger.",
    "tagline_en": "Life, lighter.",
    "promise_fr": "Votre quotidien personnel, organisé et anticipé. Vous gardez la main, il s'occupe du reste.",
}


def hex_to_rgb(h: str):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
