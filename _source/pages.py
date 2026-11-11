"""Page content for cdce.org.uk. Run build.py to write the site."""
from parts import *

PAGES = {}


def add(path, title, desc, body, **kw):
    PAGES[path] = page(path, title, desc, body, **kw)


WHO_CHIPS = "<li>Startups</li><li>Community projects</li><li>Social enterprises</li>"

# ======================================================================= HOME
add("index.html", "Home",
    "CDCE is a not-for-profit community organisation in Newcastle. Join us for free coworking every Thursday, 10am to 4pm, at DiverCity Hub.",
    f'''
<section class="hero"><div class="wrap">
  <div>
    <p class="eyebrow">Not-for-profit community organisation · Newcastle</p>
    <h1>Free space to work on <em>the things that make a difference</em></h1>
    <p class="lede">The Centre for Diversity, Community &amp; Enterprise (CDCE) supports startups, community projects and social enterprises. Join us for <strong>Coworking Thursdays</strong>: free hot desking every Thursday, 10am to 4pm, at DiverCity Hub in Newcastle.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="{BOOKING_URL}">Book a free desk</a>
      <a class="btn btn--ghost" href="coworking.html">How it works</a>
    </div>
    <p class="hero__note"><span>First session: <strong>{FIRST_SESSION}</strong>. Drop in, or book ahead to make sure of one of {CAPACITY} desks.</span></p>
  </div>
  <div class="hero__art">{HERO_ART}</div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head section-head--center">
    <p class="eyebrow">Coworking Thursdays</p>
    <h2>Everything you need to know</h2>
  </div>
  <div class="grid grid--4">
    <div class="card card--shadow">{icon("clock")}<h3>When</h3><p class="mb-0">Every Thursday, 10am to 4pm. Come for an hour or stay all day.</p></div>
    <div class="card card--shadow">{icon("pin", "berry")}<h3>Where</h3><p class="mb-0">DiverCity Hub, {VENUE_ADDRESS}</p></div>
    <div class="card card--shadow">{icon("pound", "amber")}<h3>Cost</h3><p class="mb-0">Free. No membership, no catch.</p></div>
    <div class="card card--shadow">{icon("users", "ink")}<h3>Places</h3><p class="mb-0">{CAPACITY} desks. Drop-ins are welcome, but book ahead so you don't miss out.</p></div>
  </div>
  <p style="margin-top:28px;text-align:center"><a class="link-arrow" href="coworking.html">More about Coworking Thursdays</a></p>
</div></section>

<section class="section bg-cream"><div class="wrap split">
  <div>
    <p class="eyebrow">Who it's for</p>
    <h2>Built for people starting something good</h2>
    <p>If you're building a business, running a community project or growing a social enterprise, you're welcome. Bring your laptop, meet people doing similar work, and get things done.</p>
    <ul class="chips">{WHO_CHIPS}</ul>
  </div>
  <div class="card bg-teal-wash" style="border:0">
    <h3>More from CDCE</h3>
    <p>Alongside coworking, we offer advice and guidance, training and events for small businesses, startups and community enterprises. We're also developing a dedicated CDCE building in Newcastle.</p>
    <a class="link-arrow" href="services.html">Our services</a>
  </div>
</div></section>

{cta("Join us on a Thursday", "Book your free desk and come and work alongside other founders and community organisers.", [("Book a free desk", BOOKING_URL, "btn--amber"), ("Contact us", "contact.html", "btn--ghost")])}
''')


# ======================================================================= COWORKING THURSDAYS
add("coworking.html", "Coworking Thursdays",
    "Free hot desking for startups, community projects and social enterprises every Thursday, 10am to 4pm, at DiverCity Hub in Newcastle.",
    f'''
{page_head("Coworking Thursdays", "Free hot desking for startups, community projects and social enterprises, every Thursday from 10am to 4pm at DiverCity Hub in Newcastle.", "hub", "Coworking Thursdays")}

<section class="section"><div class="wrap split split--top">
  <div>
    <h2>The details</h2>
    <ul class="contact-list">
      <li>{icon("calendar")}<div><strong>When</strong>Every Thursday, 10am to 4pm. First session {FIRST_SESSION}.</div></li>
      <li>{icon("pin", "berry")}<div><strong>Where</strong>DiverCity Hub, {VENUE_ADDRESS}</div></li>
      <li>{icon("pound", "amber")}<div><strong>Cost</strong>Free</div></li>
      <li>{icon("users", "ink")}<div><strong>Places</strong>{CAPACITY} desks each week</div></li>
    </ul>
    <p>The space is provided free of charge by our partner, DiverCity Hub, until CDCE opens its own building.</p>
  </div>
  <div class="card bg-cream" style="border:0" id="book">
    <h2 style="font-size:1.5rem">How to book</h2>
    <ol>
      <li>Book your free place for the Thursday you want to come. Drop-ins are welcome too, if there's space.</li>
      <li>Arrive any time between 10am and 4pm.</li>
      <li>Sign in when you arrive and find a desk.</li>
    </ol>
    <p>There are {CAPACITY} desks, so booking ahead is the best way to make sure you get one. If a week is full, we'll add you to the waiting list.</p>
    <a class="btn btn--primary" href="{BOOKING_URL}">Book a free desk</a>
  </div>
</div></section>

<section class="section bg-cream"><div class="wrap split split--top">
  <div>
    <p class="eyebrow">Who it's for</p>
    <h2>Is it for me?</h2>
    <p>Coworking Thursdays is for anyone working on something that benefits people and communities:</p>
    <ul class="chips">{WHO_CHIPS}</ul>
    <p style="margin-top:20px">Not sure if you fit? <a href="contact.html">Ask us</a>. We'd rather say yes.</p>
  </div>
  <div>
    <p class="eyebrow">While you're here</p>
    <h2>A few simple rules</h2>
    <ul class="ticks">
      <li>Be friendly and respectful to everyone</li>
      <li>Keep calls and noise to a reasonable level</li>
      <li>Leave your desk as you found it</li>
      <li>Let us know if you can't come, so someone else can have your place</li>
    </ul>
  </div>
</div></section>

<section class="section"><div class="wrap narrow">
  <h2>Questions</h2>
  <div class="faq">
    <details><summary>Is it really free?</summary><div><p>Yes. DiverCity Hub provides the space at no cost, so we can offer it free to you.</p></div></details>
    <details><summary>Do I need to book?</summary><div><p>You can drop in, but there are only {CAPACITY} desks, so we recommend booking ahead to make sure you get one.</p></div></details>
    <details><summary>Can I come every week?</summary><div><p>Of course. Just book for each week you plan to come.</p></div></details>
    <details><summary>I have access needs. Can you help?</summary><div><p>Please email <a href="mailto:{EMAIL}">{EMAIL}</a> before you visit and we'll do our best to make sure the space works for you.</p></div></details>
  </div>
</div></section>

{cta("Ready to join us?", "Book your free desk for a Thursday that suits you.", [("Book a free desk", BOOKING_URL, "btn--amber"), ("Contact us", "contact.html", "btn--ghost")])}
''')


# ======================================================================= SERVICES
add("services.html", "Services",
    "CDCE offers advice and guidance, training, events and free coworking for small businesses, startups, community projects and social enterprises in Newcastle.",
    f'''
{page_head("Our services", "Practical help for small businesses, startups, community projects and social enterprises in Newcastle and the North East.", "programmes", "Services")}

<section class="section"><div class="wrap">
  <div class="grid grid--2">
    <div class="card">{icon("bulb", "amber")}<h3>Advice and guidance</h3><p class="mb-0">Friendly, practical advice for small businesses and community enterprises, from shaping an idea and choosing a legal structure to planning, finance basics and finding funding.</p></div>
    <div class="card">{icon("book")}<h3>Training and workshops</h3><p class="mb-0">Sessions that build the skills you need to start, run and grow an organisation with a social purpose.</p></div>
    <div class="card">{icon("calendar", "berry")}<h3>Events and networking</h3><p class="mb-0">Opportunities to meet other founders, community organisers, partners and funders, share ideas and work together.</p></div>
    <div class="card">{icon("desk", "ink")}<h3>Coworking Thursdays</h3><p>Free hot desking every Thursday, 10am to 4pm, at DiverCity Hub in Newcastle.</p><a class="link-arrow" href="coworking.html">Find out more</a></div>
  </div>
</div></section>

{cta("Not sure where to start?", "Tell us what you're working on and we'll point you in the right direction.", [("Contact us", "contact.html", "btn--amber"), ("Book a free desk", BOOKING_URL, "btn--ghost")])}
''')


# ======================================================================= ABOUT
add("about.html", "About us",
    "Who we are and why CDCE exists: a not-for-profit community organisation in Newcastle supporting startups, community projects and social enterprises.",
    f'''
{page_head("About CDCE", "We are a not-for-profit community organisation in Newcastle, creating space, support and opportunity for the people and organisations that make our communities stronger.", "about", "About us")}

<section class="section"><div class="wrap split split--top">
  <div>
    <p class="eyebrow">Why we exist</p>
    <h2>Good ideas need a place to grow</h2>
    <p>Across the North East, people are starting businesses, running community projects and building social enterprises, often from kitchen tables and borrowed rooms. Finding space, support and the right people can be hard.</p>
    <p>CDCE was set up to change that. We run free coworking every Thursday, offer advice, guidance, training and events, and are developing a dedicated CDCE building in Newcastle.</p>
  </div>
  <div class="card card--teal"><p class="eyebrow">Our mission</p><p class="lede mb-0">To provide space, support and opportunity that help community organisations and enterprises thrive, and open up opportunity for local people.</p></div>
</div></section>

<section class="section bg-cream" id="values"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">Our name is our purpose</p>
    <h2>Diversity, community, enterprise</h2>
  </div>
  <div class="grid grid--3">
    <article class="card card--berry pillar pillar--berry">
      <div class="pillar__icon">{PILLAR_ART["diversity"]}</div>
      <p class="pillar__tag">Diversity</p>
      <h3>Open to everyone</h3>
      <p class="mb-0">People from every background are welcome in our space and in shaping what we do.</p>
    </article>
    <article class="card card--teal pillar pillar--teal">
      <div class="pillar__icon">{PILLAR_ART["community"]}</div>
      <p class="pillar__tag">Community</p>
      <h3>Stronger together</h3>
      <p class="mb-0">We bring people and organisations together so they can share ideas, resources and support.</p>
    </article>
    <article class="card card--amber pillar pillar--amber">
      <div class="pillar__icon">{PILLAR_ART["enterprise"]}</div>
      <p class="pillar__tag">Enterprise</p>
      <h3>Opportunity that lasts</h3>
      <p class="mb-0">We help good ideas become sustainable organisations, so the benefit stays in the community.</p>
    </article>
  </div>
</div></section>

{cta("Come and meet us", "The easiest way to get to know CDCE is to join us on a Thursday.", [("Book a free desk", BOOKING_URL, "btn--amber"), ("Contact us", "contact.html", "btn--ghost")])}
''')


# ======================================================================= CONTACT
add("contact.html", "Contact us",
    "Contact CDCE about Coworking Thursdays, partnerships or anything else.",
    f'''
{page_head("Contact us", "Questions about Coworking Thursdays, ideas for working together, or anything else: we'd love to hear from you.", "contact", "Contact us")}

<section class="section"><div class="wrap split split--top">
  <div>
    <h2>Get in touch</h2>
    <ul class="contact-list">
      <li>{icon("mail")}<div><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
      <li>{icon("pin", "berry")}<div><strong>Find us on Thursdays</strong>DiverCity Hub, {VENUE_ADDRESS}<br>10am to 4pm</div></li>
    </ul>
    <p class="muted">If you need information in another format or language, or support to get in touch, please tell us and we'll do our best to help.</p>
  </div>
  <div class="card bg-cream" style="border:0">
    <h2 style="font-size:1.5rem">Want a desk on Thursday?</h2>
    <p>Coworking Thursdays is free. Drop-ins are welcome, but there are {CAPACITY} desks, so it's best to book ahead.</p>
    <a class="btn btn--primary" href="{BOOKING_URL}">Book a free desk</a>
  </div>
</div></section>
''')


# ======================================================================= PRIVACY
add("privacy.html", "Privacy notice",
    "How the Centre for Diversity, Community & Enterprise collects, uses and protects your personal information.",
    f'''
{page_head("Privacy notice", "How we collect, use and protect your personal information.", "policy", "Privacy notice")}
<section class="section"><div class="wrap narrow prose">
  <h2>Who we are</h2>
  <p>{LEGAL} ("CDCE", "we", "us") is a not-for-profit community organisation and is responsible for the personal information described here. You can contact us about your data at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <h2>What we collect and why</h2>
  <ul>
    <li><strong>Bookings for Coworking Thursdays:</strong> your name, email address, organisation and the type of work you do, so we can manage places and contact you about your booking.</li>
    <li><strong>Signing in on the day:</strong> your name and the date, so we know who is in the building and can report how many people we support.</li>
    <li><strong>Emails:</strong> your name, email address and anything you include, so we can reply.</li>
  </ul>
  <p>We only send you news about CDCE if you have said you'd like it. You can unsubscribe at any time.</p>
  <h2>Who we share it with</h2>
  <p>We do not sell your information. We use trusted services to run CDCE, such as Google for email and forms. We may share anonymous numbers, such as how many people attended, with partners and funders.</p>
  <h2>How long we keep it</h2>
  <p>We keep your information only as long as we need it, and review it at least once a year.</p>
  <h2>Cookies</h2>
  <p>This website does not use cookies or tracking.</p>
  <h2>Your rights</h2>
  <p>You can ask to see, correct or delete your information, or withdraw your consent, by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>. If you are unhappy with how we have handled your information, you can complain to the Information Commissioner's Office at <a href="https://ico.org.uk/make-a-complaint/">ico.org.uk</a>.</p>
  <p class="muted">Last updated November 2026.</p>
</div></section>
''')


# ======================================================================= ACCESSIBILITY
add("accessibility.html", "Accessibility statement",
    "How CDCE makes its website accessible, and how to contact us if you have difficulty using it.",
    f'''
{page_head("Accessibility statement", "We want everyone to be able to use our website and our services.", "policy", "Accessibility")}
<section class="section"><div class="wrap narrow prose">
  <h2>Using this website</h2>
  <p>This website is run by {LEGAL}. It is designed to meet the Web Content Accessibility Guidelines (WCAG) 2.2 at level AA. You should be able to:</p>
  <ul>
    <li>zoom in up to 400% without text spilling off the screen</li>
    <li>navigate the website using just a keyboard or a screen reader</li>
    <li>change colours, contrast levels and fonts using your browser or device settings</li>
  </ul>
  <h2>Feedback and contact</h2>
  <p>If you find a problem with this website, or need information in another format such as large print or another language, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <h2>Visiting us</h2>
  <p>If you have access needs for Coworking Thursdays, please email us before you visit and we'll do our best to help.</p>
  <p class="muted">Last updated November 2026.</p>
</div></section>
''')


# ======================================================================= 404
add("404.html", "Page not found",
    "Sorry, we couldn't find that page.",
    f'''
<section class="section"><div class="wrap narrow center" style="margin:0 auto">
  <div style="width:140px;margin:0 auto 24px"><svg viewBox="0 0 120 120" aria-hidden="true">{MARK}</svg></div>
  <h1>Page not found</h1>
  <p class="lede">Sorry, we couldn't find the page you were looking for. It may have moved, or the address may be mistyped.</p>
  <div class="btn-row" style="justify-content:center"><a class="btn btn--primary" href="index.html">Go to the homepage</a><a class="btn btn--ghost" href="contact.html">Contact us</a></div>
</div></section>
''', noindex=True)

# ======================================================================= BRAND GUIDELINES (not in nav; noindex)
def swatch(name, hexv, role, text="#fff"):
    h = hexv.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return f'''<div class="card" style="padding:0;overflow:hidden"><div style="background:{hexv};color:{text};height:120px;padding:18px;font-family:var(--font-head);font-weight:700">{name}</div>
  <div style="padding:16px 18px"><p class="mb-0"><strong>{hexv}</strong><br><span class="muted">RGB {r} {g} {b}</span></p><p class="mb-0" style="font-size:.95rem;margin-top:6px">{role}</p></div></div>'''


def logo_tile(file, bg, label):
    return f'''<figure class="card" style="margin:0;padding:0;overflow:hidden"><div style="background:{bg};padding:36px;display:grid;place-items:center;min-height:200px"><img src="brand/logos/{file}.svg" alt="{label}" style="max-height:120px;width:auto"></div>
  <figcaption style="padding:14px 18px;font-size:.95rem"><strong>{label}</strong><br><a href="brand/logos/{file}.svg" download>SVG</a> · <a href="brand/logos/{file}.png" download>PNG</a></figcaption></figure>'''


add("brand.html", "Brand guidelines",
    "CDCE brand guidelines: logo, colours, typography and tone of voice.",
    f'''
{page_head("Brand guidelines", "How to use the CDCE logo, colours, type and voice consistently, on the website, in documents, on social media and in the building.", "about", "Brand guidelines")}

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Our mark</p><h2>The logo</h2>
  <p>The CDCE mark is a <strong>C</strong> made of three segments around a centre point. Each segment stands for one part of our name: <span style="color:var(--berry);font-weight:600">Diversity</span>, <span style="color:var(--teal);font-weight:600">Community</span> and <span style="color:var(--amber-dark);font-weight:600">Enterprise</span>. The navy dot is the Centre: the place, and the people, that bring them together. The opening on the right is deliberate: we are open to everyone.</p></div>
  <div class="grid grid--2">
    {logo_tile("cdce-logo-horizontal-colour", "#FFFFFF", "Primary logo, horizontal (full colour)")}
    {logo_tile("cdce-logo-horizontal-reversed", INK, "Horizontal, reversed for dark backgrounds")}
    {logo_tile("cdce-logo-stacked-colour", CREAM, "Stacked logo (full colour)")}
    {logo_tile("cdce-logo-stacked-mono-white", TEAL, "Stacked, single colour white")}
  </div>
  <div class="grid grid--4" style="margin-top:28px">
    {logo_tile("cdce-mark-colour", "#FFFFFF", "Mark only (colour)")}
    {logo_tile("cdce-mark-reversed", INK, "Mark only (reversed)")}
    {logo_tile("cdce-mark-mono-ink", SAND, "Mark only (navy)")}
    {logo_tile("cdce-logo-horizontal-mono-ink", "#FFFFFF", "Horizontal (navy, one colour)")}
  </div>
  <div class="grid grid--2" style="margin-top:40px">
    <div><h3>Using the logo</h3><ul class="ticks">
      <li>Use the full-colour logo on white or cream wherever possible.</li>
      <li>Use the reversed logo on navy or dark photography.</li>
      <li>Use single-colour versions for one-colour printing, embroidery or engraving.</li>
      <li>Leave clear space around the logo at least the width of the navy dot on every side.</li>
      <li>Minimum size: horizontal logo 120px (30mm) wide; mark alone 24px (6mm).</li>
      <li>Use the mark alone for social media avatars, favicons and small spaces.</li>
    </ul></div>
    <div><h3>Please don't</h3><ul>
      <li>stretch, squash, rotate or redraw the logo</li>
      <li>change the order or colours of the segments</li>
      <li>add shadows, outlines or effects</li>
      <li>place the colour logo on busy photos or mid-tone backgrounds</li>
      <li>type the name out in a different font to imitate the logo</li>
    </ul></div>
  </div>
</div></section>

<section class="section bg-cream"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Colour</p><h2>Colour palette</h2>
  <p>Navy is our anchor colour for text and backgrounds. The three accent colours come from the mark and should be used in roughly equal measure, so no single idea dominates.</p></div>
  <div class="grid grid--4">
    {swatch("Centre Navy", "#14304A", "Primary. Text, headers, footer, buttons.")}
    {swatch("Community Teal", "#0E6E6B", "Accent. Links, highlights, call-to-action panels.")}
    {swatch("Diversity Berry", "#B23A5F", "Accent. Highlights, tags, illustrations.")}
    {swatch("Enterprise Amber", "#F2A33A", "Accent. Buttons on dark backgrounds, highlights. Use navy text on amber.", INK)}
  </div>
  <div class="grid grid--4" style="margin-top:20px">
    {swatch("Cream", "#FBF7F0", "Page backgrounds and panels.", INK)}
    {swatch("Sand", "#F3EBDD", "Alternate panels and borders.", INK)}
    {swatch("Teal wash", "#E3F1EF", "Soft backgrounds for icons and notes.", INK)}
    {swatch("Amber text", "#9A5B00", "Amber-family colour for small text on light backgrounds.")}
  </div>
  <p style="margin-top:24px"><strong>Accessibility:</strong> navy, teal and berry text meet WCAG AA contrast on white and cream. Amber is for shapes, backgrounds and buttons with navy text; for amber-coloured text use Amber text (#9A5B00). Never put white text on amber.</p>
</div></section>

<section class="section"><div class="wrap split split--top">
  <div><p class="eyebrow">Typography</p><h2>Typefaces</h2>
    <p>Both typefaces are free, open-source fonts available from Google Fonts, so anyone in the team can install them.</p>
    <p><strong>Headings: Plus Jakarta Sans</strong> (Bold or ExtraBold). Modern, friendly and confident.</p>
    <p><strong>Body text: Source Sans 3</strong> (Regular, with Semibold for emphasis). Very readable at small sizes and on screen.</p>
    <p class="muted">In Microsoft Office, if the brand fonts are not installed, use Arial for both headings and body text.</p></div>
  <div class="card">
    <p style="font-family:var(--font-head);font-weight:800;font-size:2.6rem;line-height:1.1;margin-bottom:.2em">Aa Plus Jakarta Sans</p>
    <p class="muted" style="font-family:var(--font-head)">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789</p>
    <hr style="border:0;border-top:1px solid var(--line);margin:20px 0">
    <p style="font-size:2.2rem;line-height:1.1;margin-bottom:.2em">Aa Source Sans 3</p>
    <p class="muted">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789</p>
  </div>
</div></section>

<section class="section bg-sand"><div class="wrap split">
  <div><p class="eyebrow">Graphic language</p><h2>Building blocks</h2>
    <p>Our illustrations are made of simple square tiles: arches (buildings and doorways), people, circles, leaves (growth) and dots (networks). Combine them in grids using the brand palette. They work well on social media graphics, posters, signage and slide backgrounds.</p>
    <p>Use real photography of real people and places wherever you can. Choose warm, natural images that show the diversity of our communities, with people's consent.</p></div>
  <div style="max-width:380px">{HERO_ART}</div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Voice</p><h2>How we sound</h2></div>
  <div class="grid grid--3">
    <div class="card card--teal"><h3>Warm and welcoming</h3><p class="mb-0">Write as a neighbour, not an institution. Use "we" and "you". Say "join us", not "service users must register".</p></div>
    <div class="card card--berry"><h3>Clear and plain</h3><p class="mb-0">Short sentences and everyday words. Explain jargon the first time you use it.</p></div>
    <div class="card card--amber"><h3>Credible and honest</h3><p class="mb-0">Be specific about what we do and what we have achieved. Don't overclaim; funders and communities value honesty.</p></div>
  </div>
  <h3 style="margin-top:40px">Naming</h3>
  <p>Write <strong>Centre for Diversity, Community &amp; Enterprise</strong> in full the first time, then <strong>CDCE</strong>. The full name, <strong>{LEGAL}</strong>, should appear on official documents, invoices and the website footer. Always use UK English spelling ("centre", "organisation").</p>
  <h3 style="margin-top:28px">Downloads</h3>
  <p>All logo files are in the <code>brand/logos</code> folder of the website, in SVG (for web and print) and transparent PNG (for Office documents and social media).</p>
</div></section>
''', noindex=True)


# ======================================================================= HOLDING PAGE
# While HOLDING is on in build.py this replaces index.html; the full homepage moves to home.html
# and /draft/ redirects there, so the full site can be shared before launch.
HOLDING_PAGE = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CDCE | Centre for Diversity, Community &amp; Enterprise</title>
<meta name="description" content="The Centre for Diversity, Community &amp; Enterprise (CDCE) is a new community organisation in the North East. Our website is coming soon.">
<link rel="canonical" href="{DOMAIN}/">
<meta name="theme-color" content="#14304A">
<meta property="og:type" content="website">
<meta property="og:site_name" content="CDCE">
<meta property="og:title" content="CDCE | Centre for Diversity, Community &amp; Enterprise">
<meta property="og:description" content="A new community organisation in the North East. Our website is coming soon.">
<meta property="og:url" content="{DOMAIN}/">
<meta property="og:image" content="{DOMAIN}/assets/img/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.ico" sizes="32x32">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/plus-jakarta-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/styles.css">
<style>
  body {{ background: var(--cream); min-height: 100vh; min-height: 100dvh; display: flex; flex-direction: column; }}
  .hold {{ flex: 1; display: grid; place-items: center; padding: 48px var(--gutter); }}
  .hold__inner {{ max-width: 620px; text-align: center; }}
  .hold__logo {{ width: min(360px, 80vw); margin: 0 auto 40px; }}
  .hold h1 {{ font-size: clamp(1.9rem, 5vw, 2.6rem); margin-bottom: .4em; }}
  .hold .lede {{ margin: 0 auto 28px; }}
  .hold__art {{ display: flex; justify-content: center; gap: 10px; margin: 0 auto 36px; }}
  .hold__art svg {{ width: 40px; height: 40px; border-radius: 8px; }}
  .hold__foot {{ font-size: .9rem; color: var(--grey); padding: 20px var(--gutter) 28px; text-align: center; }}
</style>
</head>
<body>
<main class="hold" id="main">
  <div class="hold__inner">
    <img class="hold__logo" src="brand/logos/cdce-logo-stacked-colour.svg" alt="CDCE – Centre for Diversity, Community &amp; Enterprise" width="451" height="228">
    <h1>Our new website is coming soon</h1>
    <p class="lede">CDCE is a new not-for-profit community organisation in Newcastle supporting startups, community projects and social enterprises.</p>
    <div class="hold__art" aria-hidden="true">{PILLAR_ART["diversity"]}{PILLAR_ART["community"]}{PILLAR_ART["enterprise"]}</div>
    <p><strong>Free coworking every Thursday, 10am to 4pm, at DiverCity Hub, Newcastle.</strong> First session {FIRST_SESSION}. To book a desk or find out more, email us at</p>
    <p><a class="btn btn--primary" href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
</main>
<footer class="hold__foot">&copy; <span data-year>2026</span> Centre for Diversity, Community &amp; Enterprise</footer>
<div class="footer-stripe"></div>
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''


DRAFT_REDIRECT = '''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>CDCE website preview</title>
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url=/home.html">
<script>location.replace("/home.html");</script>
</head>
<body><p><a href="/home.html">Continue to the CDCE website preview</a></p></body>
</html>
'''
