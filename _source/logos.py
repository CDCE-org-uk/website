"""Generate CDCE logo SVGs with text converted to outlines."""
import math, os, sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

FONTS = sys.argv[1]
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)

INK, TEAL, BERRY, AMBER = "#14304A", "#0E6E6B", "#B23A5F", "#F2A33A"
L_TEAL, L_BERRY = "#4FC1B8", "#EE7A9C"

_cache = {}
def font(wght):
    if wght not in _cache:
        f = TTFont(f"{FONTS}/fontsource-variable-plus-jakarta-sans-5.1.1/files/plus-jakarta-sans-latin-wght-normal.woff2")
        f.flavor = None
        _cache[wght] = instantiateVariableFont(f, {"wght": wght})
    return _cache[wght]

def text_path(s, wght, size, x, y, tracking=0.0):
    """Return (svg path d, advance width) for s with baseline at y."""
    f = font(wght)
    gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f["head"].unitsPerEm
    sc = size / upm
    pen = SVGPathPen(gs)
    cx = 0
    for ch in s:
        g = cmap[ord(ch)]
        tp = TransformPen(pen, (sc, 0, 0, -sc, x + cx, y))
        gs[g].draw(tp)
        cx += gs[g].width * sc + tracking * size
    return pen.getCommands(), cx - tracking * size

def cap_height(wght, size):
    f = font(wght); gs = f.getGlyphSet(); bp = BoundsPen(gs)
    gs[f.getBestCmap()[ord("C")]].draw(bp)
    return bp.bounds[3] * size / f["head"].unitsPerEm

def sector(cx, cy, r0, r1, a0, a1):
    def p(r, a):
        t = math.radians(a)
        return cx + r * math.cos(t), cy - r * math.sin(t)
    large = 1 if (a1 - a0) > 180 else 0
    x0, y0 = p(r1, a0); x1, y1 = p(r1, a1); x2, y2 = p(r0, a1); x3, y3 = p(r0, a0)
    return (f"M{x0:.2f} {y0:.2f}A{r1} {r1} 0 {large} 0 {x1:.2f} {y1:.2f}"
            f"L{x2:.2f} {y2:.2f}A{r0} {r0} 0 {large} 1 {x3:.2f} {y3:.2f}Z")

def mark(cx, cy, s, cols, dot):
    """The CDCE mark: a 'C' of three segments (Diversity, Community, Enterprise) around a centre dot."""
    r1, r0 = 50 * s, 30 * s
    gap = 9
    start, span = 42, 276                  # opening on the right
    seg = (span - 2 * gap) / 3
    out = []
    for i, c in enumerate(cols):
        a0 = start + i * (seg + gap)
        out.append(f'<path fill="{c}" d="{sector(cx, cy, r0, r1, a0, a0 + seg)}"/>')
    out.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{15 * s:.2f}" fill="{dot}"/>')
    return "".join(out)

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{body}</svg>\n')

NAME = "Centre for Diversity, Community &amp; Enterprise"
schemes = {
    "colour": dict(cols=(BERRY, TEAL, AMBER), dot=INK, word=INK, sub=INK, bg=None),
    "reversed": dict(cols=(L_BERRY, L_TEAL, AMBER), dot="#FFFFFF", word="#FFFFFF", sub="#FFFFFF", bg=None),
    "mono-ink": dict(cols=(INK, INK, INK), dot=INK, word=INK, sub=INK, bg=None),
    "mono-white": dict(cols=("#FFFFFF",) * 3, dot="#FFFFFF", word="#FFFFFF", sub="#FFFFFF", bg=None),
}

def horizontal(sc):
    H = 120
    m = mark(60, 60, 1.1, sc["cols"], sc["dot"])
    tx = 142
    d1, w1 = text_path("CDCE", 800, 66, tx, 66, tracking=0.02)
    d2, w2 = text_path("Centre for Diversity,", 560, 19.5, tx + 2, 92)
    d3, w3 = text_path("Community & Enterprise", 560, 19.5, tx + 2, 115)
    W = tx + max(w1, w2, w3) + 6
    body = m + f'<path fill="{sc["word"]}" d="{d1}"/><path fill="{sc["sub"]}" d="{d2} {d3}"/>'
    return svg(W, H + 6, body, "CDCE – " + NAME)

def stacked(sc):
    d2, w2 = text_path("Centre for Diversity, Community & Enterprise", 560, 17, 0, 0)
    W = max(w2, 260) + 20
    cx = W / 2
    m = mark(cx, 62, 1.1, sc["cols"], sc["dot"])
    d1, w1 = text_path("CDCE", 800, 60, 0, 0, tracking=0.02)
    d1, _ = text_path("CDCE", 800, 60, cx - w1 / 2, 186, tracking=0.02)
    d2, _ = text_path("Centre for Diversity, Community & Enterprise", 560, 17, cx - w2 / 2, 216)
    body = m + f'<path fill="{sc["word"]}" d="{d1}"/><path fill="{sc["sub"]}" d="{d2}"/>'
    return svg(W, 228, body, "CDCE – " + NAME)

for name, sc in schemes.items():
    open(f"{OUT}/cdce-logo-horizontal-{name}.svg", "w").write(horizontal(sc))
    open(f"{OUT}/cdce-logo-stacked-{name}.svg", "w").write(stacked(sc))
    open(f"{OUT}/cdce-mark-{name}.svg", "w").write(svg(120, 120, mark(60, 60, 1.1, sc["cols"], sc["dot"]), "CDCE"))

# Favicon: mark on cream rounded square for legibility in tabs
fav = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#FBF7F0"/>'
       f'{mark(32, 32, 0.56, (BERRY, TEAL, AMBER), INK)}</svg>\n')
open(f"{OUT}/favicon.svg", "w").write(fav)
# Inline mark for the site header (no text, so HTML text carries the name)
open(f"{OUT}/_mark_inline.txt", "w").write(mark(60, 60, 1.1, (BERRY, TEAL, AMBER), INK))
open(f"{OUT}/_mark_inline_rev.txt", "w").write(mark(60, 60, 1.1, (L_BERRY, L_TEAL, AMBER), "#FFFFFF"))
print("ok")
