import os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages import PAGES, HOLDING_PAGE

# Holding mode: a "coming soon" page sits at the root and the full site is unlisted.
# Set to False at launch and rebuild.
HOLDING = True
from parts import DOMAIN

S = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = sys.argv[1]
SITE = os.path.join(OUT, "site")
shutil.rmtree(OUT, ignore_errors=True)
for d in ["assets/css", "assets/js", "assets/fonts", "assets/img", "brand/logos"]:
    os.makedirs(os.path.join(SITE, d), exist_ok=True)

for name, html in PAGES.items():
    if HOLDING:
        if name == "index.html":
            name = "home.html"
        html = html.replace('href="index.html"', 'href="home.html"')
        if '<meta name="robots"' not in html:
            html = html.replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"')
    if name == "404.html":  # served from any path, so resolve links from the site root
        html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<base href="/">')
    open(os.path.join(SITE, name), "w").write(html)

if HOLDING:
    open(os.path.join(SITE, "index.html"), "w").write(HOLDING_PAGE)
shutil.copy(f"{S}/build/styles.css", f"{SITE}/assets/css/styles.css")
shutil.copy(f"{S}/build/main.js", f"{SITE}/assets/js/main.js")
F = f"{S}/fonts"
for pkg, files in [("fontsource-variable-plus-jakarta-sans-5.1.1", ["plus-jakarta-sans-latin-wght-normal.woff2"]),
                   ("fontsource-variable-source-sans-3-5.1.1", ["source-sans-3-latin-wght-normal.woff2", "source-sans-3-latin-wght-italic.woff2"])]:
    for f in files:
        shutil.copy(f"{F}/{pkg}/files/{f}", f"{SITE}/assets/fonts/{f}")
    lic = [x for x in os.listdir(f"{F}/{pkg}") if x.upper().startswith("LICENSE")][0]
    shutil.copy(f"{F}/{pkg}/{lic}", f"{SITE}/assets/fonts/{pkg.split('variable-')[1].rsplit('-', 1)[0]}-OFL.txt")
for f in os.listdir(f"{S}/logos"):
    if f.endswith(".svg"):
        shutil.copy(f"{S}/logos/{f}", f"{SITE}/brand/logos/{f}")
shutil.copy(f"{S}/logos/favicon.svg", f"{SITE}/assets/img/favicon.svg")
R = f"{S}/raster"
for f in ["apple-touch-icon.png", "icon-192.png", "icon-512.png", "og-image.png"]:
    shutil.copy(f"{R}/{f}", f"{SITE}/assets/img/{f}")
shutil.copy(f"{R}/favicon.ico", f"{SITE}/favicon.ico")
for f in os.listdir(f"{R}/png"):
    shutil.copy(f"{R}/png/{f}", f"{SITE}/brand/logos/{f}")

urls = ["index.html"] if HOLDING else [p for p in PAGES if p not in ("404.html", "brand.html")]
open(f"{SITE}/sitemap.xml", "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{DOMAIN}/{'' if p == 'index.html' else p}</loc></url>\n" for p in urls) + "</urlset>\n")
open(f"{SITE}/CNAME", "w").write("cdce.org.uk\n"); open(f"{SITE}/.nojekyll", "w").close()
open(f"{SITE}/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
open(f"{SITE}/site.webmanifest", "w").write('''{
  "name": "Centre for Diversity, Community & Enterprise",
  "short_name": "CDCE",
  "icons": [
    { "src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ],
  "theme_color": "#14304A",
  "background_color": "#FBF7F0",
  "display": "standalone",
  "start_url": "/"
}
''')
print("built", len(PAGES), "pages")
