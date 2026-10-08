"""Shared building blocks for the CDCE site: layout, illustrations, icons."""
import os

HERE = os.path.dirname(__file__)
LOGOS = os.path.join(HERE, "..", "logos")
MARK = open(os.path.join(LOGOS, "_mark_inline.txt")).read()
MARK_REV = open(os.path.join(LOGOS, "_mark_inline_rev.txt")).read()

DOMAIN = "https://cdce.org.uk"
LEGAL = "Centre for Diversity, Community &amp; Enterprise CIC"
EMAIL = "hello@cdce.org.uk"

INK, TEAL, BERRY, AMBER = "#14304A", "#0E6E6B", "#B23A5F", "#F2A33A"
CREAM, SAND, TEAL_W, BERRY_W, AMBER_W = "#FBF7F0", "#F3EBDD", "#E3F1EF", "#F8E6EC", "#FDF0DC"
L_TEAL, L_BERRY = "#4FC1B8", "#EE7A9C"


def ph(text):
    """Visible placeholder the CDCE team must replace or confirm."""
    return f'<mark class="ph">[{text}]</mark>'


# ---------------------------------------------------------------- Icons
_ICON_PATHS = {
    "building": '<path d="M4 21V5a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v16"/><path d="M15 9h4a1 1 0 0 1 1 1v11"/><path d="M2 21h20"/><path d="M8 8h3M8 12h3M8 16h3"/>',
    "desk": '<rect x="3" y="4" width="18" height="11" rx="1.5"/><path d="M8 20h8M12 15v5"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.6a3.5 3.5 0 0 1 0 6.8"/><path d="M18 14.2A6.5 6.5 0 0 1 21.5 20"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/><path d="M3 13h18"/>',
    "sprout": '<path d="M12 21v-9"/><path d="M12 12C12 7 8.5 4 4 4c0 5 3.5 8 8 8Z"/><path d="M12 14c0-4 3-7 8-7 0 4.5-3 7-8 7Z"/>',
    "bulb": '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3Z"/>',
    "wifi": '<path d="M2 9a15 15 0 0 1 20 0"/><path d="M5.5 12.5a10 10 0 0 1 13 0"/><path d="M9 16a5 5 0 0 1 6 0"/><circle cx="12" cy="19.5" r=".8" fill="currentColor"/>',
    "access": '<circle cx="12" cy="4.5" r="1.8"/><path d="M5 8.5l7 1.5 7-1.5"/><path d="M12 10v4l-3.5 7M12 14l3.5 7"/>',
    "coffee": '<path d="M4 9h13v5a6 6 0 0 1-6 6h-1a6 6 0 0 1-6-6Z"/><path d="M17 11h1.5a2.5 2.5 0 0 1 0 5H17"/><path d="M8 3v3M12 3v3"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 7 8.5-7"/>',
    "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2Z"/>',
    "pin": '<path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12Z"/><circle cx="12" cy="9" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "heart": '<path d="M12 20s-8-4.6-8-10.5A4.5 4.5 0 0 1 12 7a4.5 4.5 0 0 1 8 2.5C20 15.4 12 20 12 20Z"/>',
    "handshake": '<path d="m11 7-2-2H5L2 9l7 7"/><path d="m13 7 2-2h4l3 4-7 7"/><path d="M9 16l1.5 1.5a1.5 1.5 0 0 0 2 0L15 15"/><path d="M8 11.5 11 9l3 2.5"/>',
    "book": '<path d="M4 4h6a2 2 0 0 1 2 2v14a2 2 0 0 0-2-2H4Z"/><path d="M20 4h-6a2 2 0 0 0-2 2v14a2 2 0 0 1 2-2h6Z"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6Z"/><path d="m9 12 2 2 4-4"/>',
    "file": '<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8Z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "megaphone": '<path d="M3 10v4a1 1 0 0 0 1 1h3l6 4V5L7 9H4a1 1 0 0 0-1 1Z"/><path d="M17 8a5 5 0 0 1 0 8"/>',
    "pound": '<path d="M17 20H7c2-2 2-4 2-6V8a4 4 0 0 1 7.5-2"/><path d="M6 13h8"/>',
    "star": '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9Z"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "car": '<path d="M5 16V11l2-5h10l2 5v5"/><path d="M3 16h18v3H3z"/><circle cx="7.5" cy="13" r=".8" fill="currentColor"/><circle cx="16.5" cy="13" r=".8" fill="currentColor"/>',
    "lock": '<rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
}


def icon(name, tone="teal"):
    return (f'<span class="icon icon--{tone}" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{_ICON_PATHS[name]}</svg></span>')


# ---------------------------------------------------------------- Geometric illustrations
def _tile(kind, x, y, s, fg, bg, rot=0):
    cx, cy = x + s / 2, y + s / 2
    out = f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{bg}"/>' if bg else ""
    t = f' transform="rotate({rot} {cx} {cy})"' if rot else ""
    r = s / 2
    if kind == "circle":
        out += f'<circle cx="{cx}" cy="{cy}" r="{r * .78}" fill="{fg}"/>'
    elif kind == "quarter":
        out += f'<path{t} d="M{x} {y + s}V{y}A{s} {s} 0 0 1 {x + s} {y + s}Z" fill="{fg}"/>'
    elif kind == "half":
        out += f'<path{t} d="M{x} {cy}A{r} {r} 0 0 1 {x + s} {cy}Z" fill="{fg}"/>'
    elif kind == "arch":
        out += f'<path{t} d="M{x + s*.18} {y + s}V{y + s*.5}A{s*.32} {s*.32} 0 0 1 {x + s*.82} {y + s*.5}V{y + s}Z" fill="{fg}"/>'
    elif kind == "ring":
        out += f'<circle cx="{cx}" cy="{cy}" r="{r * .6}" fill="none" stroke="{fg}" stroke-width="{s * .16}"/>'
    elif kind == "dots":
        for i in range(3):
            for j in range(3):
                out += f'<circle cx="{x + s*(.22 + i*.28)}" cy="{y + s*(.22 + j*.28)}" r="{s*.06}" fill="{fg}"/>'
    elif kind == "leaf":
        out += f'<path{t} d="M{x} {y + s}C{x} {y + s*.4} {x + s*.4} {y} {x + s} {y}C{x + s} {y + s*.6} {x + s*.6} {y + s} {x} {y + s}Z" fill="{fg}"/>'
    elif kind == "stripes":
        for i in range(4):
            out += f'<rect x="{x + s*.12}" y="{y + s*(.16 + i*.2)}" width="{s*.76}" height="{s*.09}" rx="{s*.045}" fill="{fg}"/>'
    elif kind == "person":
        out += (f'<circle cx="{cx}" cy="{y + s*.36}" r="{s*.16}" fill="{fg}"/>'
                f'<path d="M{x + s*.2} {y + s}A{s*.3} {s*.3} 0 0 1 {x + s*.8} {y + s}Z" fill="{fg}"/>')
    elif kind == "mark":
        out += f'<g transform="translate({x} {y}) scale({s / 120})">{MARK}</g>'
    return out


def art(spec, cols, size=100, label=""):
    """spec: list of (kind, fg, bg, rot) row-major."""
    rows = (len(spec) + cols - 1) // cols
    body = []
    for i, (kind, fg, bg, rot) in enumerate(spec):
        body.append(_tile(kind, (i % cols) * size, (i // cols) * size, size, fg, bg, rot))
    a = f' role="img" aria-label="{label}"' if label else ' aria-hidden="true"'
    return (f'<svg viewBox="0 0 {cols * size} {rows * size}" xmlns="http://www.w3.org/2000/svg"{a} '
            f'preserveAspectRatio="xMidYMid slice">{"".join(body)}</svg>')


HERO_ART = art([
    ("quarter", TEAL, CREAM, 0), ("circle", AMBER, INK, 0), ("arch", BERRY, SAND, 0),
    ("person", INK, AMBER_W, 0), ("mark", None, "#FFFFFF", 0), ("half", TEAL, BERRY_W, 180),
    ("arch", AMBER, TEAL, 0), ("dots", INK, TEAL_W, 0), ("leaf", TEAL, AMBER, 0),
], 3, label="Abstract illustration of the CDCE building blocks: people, places and enterprise")

HEAD_ART = {
    "about": art([("circle", BERRY, CREAM, 0), ("quarter", INK, TEAL_W, 90), ("person", TEAL, AMBER_W, 0), ("half", AMBER, INK, 0)], 2),
    "hub": art([("arch", TEAL, SAND, 0), ("arch", BERRY, AMBER_W, 0), ("stripes", INK, TEAL_W, 0), ("arch", AMBER, INK, 0)], 2),
    "programmes": art([("leaf", TEAL, AMBER_W, 0), ("circle", AMBER, TEAL, 0), ("quarter", BERRY, CREAM, 270), ("dots", INK, BERRY_W, 0)], 2),
    "involved": art([("person", BERRY, TEAL_W, 0), ("person", TEAL, AMBER_W, 0), ("person", AMBER, INK, 0), ("person", INK, BERRY_W, 0)], 2),
    "news": art([("stripes", INK, AMBER_W, 0), ("circle", BERRY, TEAL_W, 0), ("half", TEAL, SAND, 0), ("quarter", AMBER, INK, 180)], 2),
    "contact": art([("ring", TEAL, AMBER_W, 0), ("quarter", BERRY, CREAM, 0), ("circle", INK, TEAL_W, 0), ("half", AMBER, BERRY, 90)], 2),
    "policy": art([("stripes", TEAL, CREAM, 0), ("ring", INK, AMBER_W, 0), ("quarter", BERRY, TEAL_W, 180), ("dots", AMBER, INK, 0)], 2),
}

PILLAR_ART = {
    "diversity": art([("circle", BERRY, BERRY_W, 0)], 1),
    "community": art([("person", TEAL, TEAL_W, 0)], 1),
    "enterprise": art([("leaf", "#C07A10", AMBER_W, 0)], 1),
}


def banner(kinds, bgs, fgs):
    """Wide 16:9 art made of tiles for cards."""
    spec = [(k, f, b, 0) for k, f, b in zip(kinds, fgs, bgs)]
    return art(spec, 4, label="")


# ---------------------------------------------------------------- Layout
NAV = [
    ("index.html", "Home"),
    ("about.html", "About us"),
    ("hub.html", "The Hub"),
    ("programmes.html", "Programmes"),
    ("get-involved.html", "Get involved"),
    ("news.html", "News"),
]


def brand_link(rev=False):
    return (f'<a class="brand" href="index.html" aria-label="CDCE home">'
            f'<svg viewBox="0 0 120 120" aria-hidden="true">{MARK_REV if rev else MARK}</svg>'
            f'<span class="brand__text"><span class="brand__abbr">CDCE</span>'
            f'<span class="brand__name">Centre for Diversity,<br>Community &amp; Enterprise</span></span></a>')


def header(active):
    items = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<a class="skip" href="#main">Skip to main content</a>
<div class="topbar"><div class="wrap">
  <p class="topbar__msg mb-0">A community interest company for {ph("Town or city")} and the North East</p>
  <div class="topbar__links"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="accessibility.html">Accessibility</a></div>
</div></div>
<header class="site-header"><div class="wrap" style="position:relative">
  {brand_link()}
  <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav"><span class="nav-toggle__bars"></span>Menu</button>
  <nav class="nav" id="site-nav" aria-label="Main">
    <ul class="nav__list">{items}</ul>
    <a class="btn btn--primary" href="contact.html"{" aria-current=\"page\"" if active == "contact.html" else ""}>Contact us</a>
  </nav>
</div></header>'''


def footer():
    return f'''<footer class="site-footer">
<div class="footer-stripe"></div>
<div class="wrap footer-top">
  <div class="footer-brand">
    {brand_link(rev=True)}
    <p>Space, support and opportunity for the people and organisations that make our communities stronger.</p>
  </div>
  <div>
    <h2>Explore</h2>
    <ul>
      <li><a href="about.html">About us</a></li>
      <li><a href="hub.html">The Hub</a></li>
      <li><a href="programmes.html">Programmes</a></li>
      <li><a href="get-involved.html">Get involved</a></li>
      <li><a href="news.html">News</a></li>
    </ul>
  </div>
  <div>
    <h2>Governance</h2>
    <ul>
      <li><a href="about.html#governance">How we're run</a></li>
      <li><a href="policies.html">Policies</a></li>
      <li><a href="policies.html#reports">Community interest reports</a></li>
      <li><a href="privacy.html">Privacy notice</a></li>
      <li><a href="accessibility.html">Accessibility</a></li>
    </ul>
  </div>
  <div>
    <h2>Contact</h2>
    <ul>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{ph("Phone number")}</li>
      <li>{ph("Hub address, North East")}</li>
      <li><a href="{ph_href("LinkedIn URL")}">LinkedIn</a> · <a href="{ph_href("Facebook URL")}">Facebook</a> · <a href="{ph_href("Instagram URL")}">Instagram</a></li>
    </ul>
  </div>
</div>
<div class="wrap footer-bottom">
  <p>{LEGAL} is a community interest company limited by guarantee, registered in England and Wales. Company number {ph("company number")}. Registered office: {ph("registered office address")}.</p>
  <nav aria-label="Legal"><ul>
    <li>&copy; <span data-year>2026</span> CDCE</li>
    <li><a href="privacy.html">Privacy</a></li>
    <li><a href="accessibility.html">Accessibility</a></li>
    <li><a href="policies.html">Policies</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul></nav>
</div>
</footer>'''


def ph_href(_label):
    # Social links: replace '#' with the real profile URLs (listed in README).
    return "#"


def page(path, title, desc, body, active=None, noindex=False):
    full_title = "CDCE | Centre for Diversity, Community &amp; Enterprise" if path == "index.html" else f"{title} | CDCE"
    canonical = f"{DOMAIN}/" if path == "index.html" else f"{DOMAIN}/{path}"
    robots = '\n<meta name="robots" content="noindex">' if noindex else ""
    ld = ""
    if path == "index.html":
        ld = f'''
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Centre for Diversity, Community & Enterprise CIC","alternateName":"CDCE","url":"{DOMAIN}/","logo":"{DOMAIN}/brand/logos/cdce-logo-stacked-colour.svg","email":"{EMAIL}","areaServed":"North East England"}}</script>'''
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">{robots}
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#14304A">
<meta property="og:type" content="website">
<meta property="og:site_name" content="CDCE">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/img/og-image.png">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.ico" sizes="32x32">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="assets/fonts/plus-jakarta-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/styles.css">{ld}
</head>
<body>
{header(active or path)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''


def page_head(title, lede, art_key, crumb):
    return f'''<section class="page-head"><div class="wrap">
  <div>
    <p class="crumbs"><a href="index.html">Home</a><span aria-hidden="true">/</span>{crumb}</p>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
  </div>
  <div class="page-head__art">{HEAD_ART[art_key]}</div>
</div></section>'''


def cta(title, text, btns):
    b = "".join(f'<a class="btn {cls}" href="{h}">{t}</a>' for t, h, cls in btns)
    return f'''<section class="section--tight"><div class="wrap"><div class="cta">
  <div><h2>{title}</h2><p>{text}</p></div>
  <div class="btn-row">{b}</div>
  <svg class="cta__deco" viewBox="0 0 120 120" aria-hidden="true">{MARK_REV}</svg>
</div></div></section>'''
