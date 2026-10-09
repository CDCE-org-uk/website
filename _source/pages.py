"""Page content for cdce.org.uk. Run build.py to write the site."""
from parts import *

PAGES = {}


def add(path, title, desc, body, **kw):
    PAGES[path] = page(path, title, desc, body, **kw)


def space_art(kind, fg, bg, accent):
    return art([(kind, fg, bg, 0), ("dots", accent, bg, 0), (kind, accent, bg, 0), ("circle", fg, bg, 0)], 4)


NEWS = [
    ("tag", "Announcement", "CDCE launches with plans for a North East community hub",
     "We are delighted to introduce the Centre for Diversity, Community &amp; Enterprise, a new community interest company creating space and support for local organisations.",
     ph("Publish date"), ("arch", TEAL, CREAM)),
    ("tag tag--berry", "Get involved", "Have your say: what should the Hub offer?",
     "We want the Hub to reflect the needs of the people who will use it. Tell us what space, facilities and support would make a difference to you.",
     ph("Publish date"), ("person", BERRY, BERRY_W)),
    ("tag tag--amber", "Funding", "An update on our development funding",
     "What our funding applications will make possible for the Hub and our first programmes, and how partners can help.",
     ph("Publish date"), ("leaf", "#C07A10", AMBER_W)),
]


def news_card(n):
    tag_cls, tag, title, summary, date, (k, fg, bg) = n
    a = art([(k, fg, bg, 0), ("dots", INK, bg, 0), ("circle", fg, bg, 0), ("quarter", INK, bg, 0)], 4)
    return f'''<article class="post"><div class="post__art">{a}</div><div class="post__body">
  <p class="post__meta"><span class="{tag_cls}">{tag}</span>{date}</p>
  <h3>{title}</h3><p>{summary}</p>
  <p class="mb-0" style="margin-top:auto">{ph("Link to full article once written")}</p>
</div></article>'''


NEWS_CARDS = "".join(news_card(n) for n in NEWS)

# ======================================================================= HOME
add("index.html", "Home",
    "CDCE is a community interest company in the North East creating a hub of affordable space, practical support and opportunity for social enterprises, charities, community groups and local people.",
    f'''
<section class="hero"><div class="wrap">
  <div>
    <p class="eyebrow">Community interest company · North East England</p>
    <h1>A home for the organisations that <em>hold our communities together</em></h1>
    <p class="lede">The Centre for Diversity, Community &amp; Enterprise (CDCE) brings social enterprises, charities and community groups under one roof, with affordable space, practical support and routes into work for local people.</p>
    <div class="btn-row">
      <a class="btn btn--primary" href="hub.html">Explore the Hub</a>
      <a class="btn btn--ghost" href="contact.html#interest">Register your interest</a>
    </div>
    <p class="hero__note"><span>We are currently developing our hub in {ph("Town or city")}. {ph("Opening date or status, e.g. 'Opening spring 2027'")}. Register your interest to hear first about space and programmes.</span></p>
  </div>
  <div class="hero__art">{HERO_ART}</div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head section-head--center">
    <p class="eyebrow">What we stand for</p>
    <h2>Three ideas, one centre</h2>
    <p class="lede">Our name is our purpose. Everything we do brings these three things together in one place.</p>
  </div>
  <div class="grid grid--3">
    <article class="card card--berry pillar pillar--berry">
      <div class="pillar__icon">{PILLAR_ART["diversity"]}</div>
      <p class="pillar__tag">Diversity</p>
      <h3>Open to everyone</h3>
      <p>We make sure people from every background, culture and walk of life can use our space, join our programmes and shape what we do.</p>
      <a class="link-arrow" href="about.html#values">Our values</a>
    </article>
    <article class="card card--teal pillar pillar--teal">
      <div class="pillar__icon">{PILLAR_ART["community"]}</div>
      <p class="pillar__tag">Community</p>
      <h3>Stronger together</h3>
      <p>We bring charities, community groups and residents into one shared space, so they can work together, share resources and reach more people.</p>
      <a class="link-arrow" href="hub.html">The Hub</a>
    </article>
    <article class="card card--amber pillar pillar--amber">
      <div class="pillar__icon">{PILLAR_ART["enterprise"]}</div>
      <p class="pillar__tag">Enterprise</p>
      <h3>Opportunity that lasts</h3>
      <p>We help people into work and help social enterprises start, grow and become sustainable, so that the benefit stays in the community.</p>
      <a class="link-arrow" href="programmes.html">Programmes</a>
    </article>
  </div>
</div></section>

<section class="section bg-cream"><div class="wrap split">
  <div>
    <p class="eyebrow">The Hub</p>
    <h2>Affordable space for social purpose</h2>
    <p>Too many good organisations spend their energy finding somewhere to work. The CDCE Hub gives them a professional, accessible and affordable base, with neighbours who share their values.</p>
    <ul class="ticks">
      <li><strong>Private offices</strong> for established charities and social enterprises</li>
      <li><strong>Co-working desks</strong> for start-ups, freelancers and small teams</li>
      <li><strong>Meeting and training rooms</strong> to hire by the hour or day</li>
      <li><strong>Community and event space</strong> for activities, workshops and gatherings</li>
    </ul>
    <div class="btn-row"><a class="btn btn--primary" href="hub.html">See spaces and rates</a></div>
  </div>
  <div class="grid grid--2">
    <div class="card card--shadow">{icon("building")}<h3>Offices</h3><p class="mb-0">Lockable rooms for teams of {ph("2 to 8")}.</p></div>
    <div class="card card--shadow">{icon("desk", "berry")}<h3>Desks</h3><p class="mb-0">Flexible and fixed desk memberships.</p></div>
    <div class="card card--shadow">{icon("users", "amber")}<h3>Rooms</h3><p class="mb-0">Meeting rooms for up to {ph("12")} people.</p></div>
    <div class="card card--shadow">{icon("calendar", "ink")}<h3>Events</h3><p class="mb-0">A flexible hall for up to {ph("60")} people.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap split split--top">
  <div>
    <p class="eyebrow">Who we're for</p>
    <h2>Built for the people doing the work</h2>
    <p>CDCE is for anyone working to improve life in our communities, and for the people those organisations serve.</p>
    <ul class="chips">
      <li>Social enterprises</li><li>Charities</li><li>Community groups</li><li>CICs and co-operatives</li>
      <li>Start-ups with a social mission</li><li>Faith and cultural groups</li><li>People looking for work</li><li>Funders and partners</li>
    </ul>
    <div class="card bg-teal-wash" style="border:0;margin-top:28px">
      <h3>Not sure if we're the right fit?</h3>
      <p>If your work benefits people and communities in the North East, we would like to hear from you. We will always try to help or point you to someone who can.</p>
      <a class="link-arrow" href="contact.html">Start a conversation</a>
    </div>
  </div>
  <div>
    <p class="eyebrow">Programmes</p>
    <h2>Support, not just space</h2>
    <div class="grid">
      <div class="card" style="flex-direction:row;gap:16px">{icon("briefcase")}<div><h3>Employability</h3><p class="mb-0">Coaching, skills and work experience that help local people into good jobs.</p></div></div>
      <div class="card" style="flex-direction:row;gap:16px">{icon("bulb", "amber")}<div><h3>Enterprise support</h3><p class="mb-0">Workshops, mentoring and advice to start and grow social enterprises.</p></div></div>
      <div class="card" style="flex-direction:row;gap:16px">{icon("heart", "berry")}<div><h3>Community and inclusion</h3><p class="mb-0">Events, networks and projects led by and for our diverse communities.</p></div></div>
    </div>
    <p style="margin-top:20px"><a class="link-arrow" href="programmes.html">All programmes</a></p>
  </div>
</div></section>

<section class="section bg-ink"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">How it works</p>
    <h2>From first conversation to thriving tenant</h2>
  </div>
  <ol class="steps">
    <li><h3>Get in touch</h3><p>Tell us about your organisation or what you are looking for.</p></li>
    <li><h3>Visit and talk</h3><p>Look round the Hub and talk through space, support and costs.</p></li>
    <li><h3>Move in or join</h3><p>Take a desk, an office or a place on one of our programmes.</p></li>
    <li><h3>Grow with us</h3><p>Use our network, training and partners to grow your impact.</p></li>
  </ol>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">Our ambitions</p>
    <h2>What we aim to achieve in our first three years</h2>
    <p class="muted">These targets will be confirmed by the board and reported each year in our community interest report.</p>
  </div>
  <div class="stats">
    <div class="stat"><div class="stat__num">{ph("25")}</div><p>organisations based at or supported by the Hub</p></div>
    <div class="stat"><div class="stat__num">{ph("300")}</div><p>local people supported towards work or training</p></div>
    <div class="stat"><div class="stat__num">{ph("40")}</div><p>new social enterprises helped to start or grow</p></div>
    <div class="stat"><div class="stat__num">{ph("100")}%</div><p>of surplus reinvested in our community purpose</p></div>
  </div>
</div></section>

<section class="section bg-cream"><div class="wrap">
  <div class="section-head section-head--center">
    <p class="eyebrow">Working together</p>
    <h2>Our funders and partners</h2>
    <p>We are grateful to the organisations who support our work. {ph("Add funder and partner logos once agreements are confirmed")}</p>
  </div>
  <div class="logos">
    <div class="logos__item">Funder logo</div><div class="logos__item">Partner logo</div><div class="logos__item">Partner logo</div><div class="logos__item">Partner logo</div><div class="logos__item">Partner logo</div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head" style="display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap;max-width:none">
    <div><p class="eyebrow">News</p><h2 class="mb-0">Latest from CDCE</h2></div>
    <a class="link-arrow" href="news.html">All news</a>
  </div>
  <div class="grid grid--3">{NEWS_CARDS}</div>
</div></section>

{cta("Interested in space at the Hub?", "Register your interest now and we will keep you updated on availability, rates and opening plans.", [("Register interest", "contact.html#interest", "btn--amber"), ("Talk to us", "contact.html", "btn--ghost")])}
''')


# ======================================================================= ABOUT
def person(role, tone, blurb):
    av = art([("person", {"teal": TEAL, "berry": BERRY, "amber": "#C07A10", "ink": INK}[tone],
                {"teal": TEAL_W, "berry": BERRY_W, "amber": AMBER_W, "ink": "#E4EAF0"}[tone], 0)], 1)
    return f'''<article class="card person"><div class="person__avatar" style="border-radius:50%;overflow:hidden">{av}</div>
  <h3>{ph("Full name")}</h3><p class="person__role">{role}</p><p>{blurb}</p></article>'''


add("about.html", "About us",
    "Who we are, why CDCE exists, our values and how we are governed as a community interest company.",
    f'''
{page_head("About CDCE", "We are a community interest company creating a shared home for social purpose in the North East, where diversity is a strength, communities work together and enterprise creates lasting opportunity.", "about", "About us")}

<section class="section"><div class="wrap split split--top">
  <div>
    <p class="eyebrow">Why we exist</p>
    <h2>Good work needs a good home</h2>
    <p>Across the North East, charities, community groups and social enterprises do remarkable work, often from spare rooms, borrowed halls and short-term lets. Many spend precious time and money finding space instead of serving people.</p>
    <p>At the same time, too many local people face barriers to work and enterprise because of where they live, their background or their circumstances.</p>
    <p>CDCE was set up to tackle both. By bringing organisations together in one accessible, affordable hub and connecting them with practical support, we can help them achieve more, and open up opportunity for the communities they serve.</p>
  </div>
  <div class="grid">
    <div class="card card--teal"><p class="eyebrow">Our mission</p><p class="lede mb-0">To provide space, support and opportunity that help community organisations thrive and help local people into meaningful work and enterprise.</p></div>
    <div class="card card--berry"><p class="eyebrow" style="color:var(--berry)">Our vision</p><p class="lede mb-0">Inclusive, confident communities where everyone can contribute, and where the organisations that support them are strong and sustainable.</p></div>
  </div>
</div></section>

<section class="section bg-cream" id="values"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">Our values</p>
    <h2>What guides us</h2>
  </div>
  <div class="grid grid--3">
    <div class="card">{icon("globe", "berry")}<h3>Inclusive</h3><p>We welcome everyone and remove barriers so that people of all backgrounds can take part and lead.</p></div>
    <div class="card">{icon("pin")}<h3>Rooted locally</h3><p>We listen to our communities and shape what we do around local needs and local strengths.</p></div>
    <div class="card">{icon("bulb", "amber")}<h3>Enterprising</h3><p>We look for practical, sustainable solutions and reinvest what we earn in our purpose.</p></div>
    <div class="card">{icon("handshake", "ink")}<h3>Collaborative</h3><p>We achieve more together, so we share space, knowledge and opportunities with our partners.</p></div>
    <div class="card">{icon("shield")}<h3>Accountable</h3><p>We are open about how we are run, how we spend our money and the difference we make.</p></div>
    <div class="card">{icon("heart", "berry")}<h3>Caring</h3><p>We put people's wellbeing and safety first, in everything from our building to our programmes.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap split">
  <div>
    <p class="eyebrow">Our story</p>
    <h2>How CDCE began</h2>
    <p>CDCE was founded in {ph("year")} by people with long experience of the voluntary, community and enterprise sectors in the North East. {ph("Add a short founding story: who saw the need, what conversations led to CDCE, and what you have done so far.")}</p>
    <p>We are now working with partners and funders to secure and develop our hub building in {ph("Town or city")}, and to design our first programmes with the communities they will serve.</p>
  </div>
  <div class="photo-ph" role="img" aria-label="Photo placeholder"><div><strong>Photo placeholder</strong>A photo of the founding team, the building or a community event.<br>Recommended: 1200 × 900px.</div></div>
</div></section>

<section class="section bg-sand" id="governance"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">Governance</p>
    <h2>How we are run</h2>
    <p>CDCE is a community interest company (CIC) limited by guarantee. CICs are a special type of company designed for social enterprises that want to use their profits and assets for the public good.</p>
  </div>
  <div class="grid grid--3">
    <div class="card">{icon("lock", "ink")}<h3>An asset lock</h3><p>Our assets and any surplus are protected by law and must be used for the benefit of the community. They cannot be distributed for private gain.</p></div>
    <div class="card">{icon("file")}<h3>Public reporting</h3><p>Every year we file accounts and a community interest report with the CIC Regulator, explaining how we have benefited the community.</p></div>
    <div class="card">{icon("users", "berry")}<h3>An independent board</h3><p>Our board of directors sets our strategy, oversees our finances and safeguarding, and holds our management to account.</p></div>
  </div>
  <p style="margin-top:28px">Company number {ph("company number")}. You can view our filings on <a href="https://find-and-update.company-information.service.gov.uk/">Companies House</a>. Read our <a href="policies.html">policies</a> and <a href="policies.html#reports">community interest reports</a>.</p>
</div></section>

<section class="section" id="team"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">Our people</p>
    <h2>Board and team</h2>
    <p>{ph("Confirm names, roles and short bios with each person before publishing, and add photos if they are happy to be pictured.")}</p>
  </div>
  <h3>Board of directors</h3>
  <div class="grid grid--4" style="margin-bottom:48px">
    {person("Chair", "teal", ph("Short bio, one or two sentences"))}
    {person("Director", "berry", ph("Short bio, one or two sentences"))}
    {person("Non-executive director", "amber", ph("Short bio, one or two sentences"))}
    {person("Non-executive director", "ink", ph("Short bio, one or two sentences"))}
  </div>
  <h3>Management team</h3>
  <div class="grid grid--4">
    {person(ph("Managing Director or Operations Director"), "teal", ph("Short bio, one or two sentences"))}
    {person(ph("Role"), "amber", ph("Short bio, one or two sentences"))}
  </div>
</div></section>

{cta("Want to work with us?", "Whether you are a funder, a partner or an organisation looking for a home, we would love to talk.", [("Get involved", "get-involved.html", "btn--amber"), ("Contact us", "contact.html", "btn--ghost")])}
''')


# ======================================================================= HUB
def space(title, art_svg, meta, text):
    m = "".join(f"<li>{x}</li>" for x in meta)
    return f'''<article class="space"><div class="space__art">{art_svg}</div><div class="space__body">
  <h3>{title}</h3><ul class="space__meta">{m}</ul><p class="mb-0">{text}</p></div></article>'''


add("hub.html", "The Hub",
    "The CDCE Hub offers affordable offices, co-working desks, meeting rooms and community space for social enterprises, charities and community groups in the North East.",
    f'''
{page_head("The Hub", "A professional, accessible and affordable base for social enterprises, charities and community groups, with shared facilities and a community of like-minded neighbours.", "hub", "The Hub")}

<section class="section--tight bg-amber-note" style="background:var(--amber-wash)"><div class="wrap">
  <p class="mb-0"><strong>Status:</strong> {ph("e.g. 'We are currently securing our building. Register your interest and we will contact you as soon as spaces are available.'")} <a href="#interest-cta">Register interest</a></p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">Spaces</p>
    <h2>Space that works for you</h2>
    <p>Whether you need a permanent base, a desk a few days a week or a room for an afternoon, there is a space for you at the Hub.</p>
  </div>
  <div class="grid grid--2">
    {space("Private offices", space_art("arch", TEAL, TEAL_W, INK), [f"Teams of {ph('2 to 8')}", "Monthly licence", "24/7 access"], "Lockable, furnished offices for charities and social enterprises that need a settled home. Includes utilities, Wi-Fi, cleaning and use of shared facilities.")}
    {space("Co-working desks", space_art("stripes", BERRY, BERRY_W, INK), ["Flexible or fixed", "Day passes", "Monthly plans"], "A friendly shared workspace for start-ups, freelancers and small teams, with the option of a dedicated desk and storage.")}
    {space("Meeting and training rooms", space_art("ring", "#C07A10", AMBER_W, TEAL), [f"Up to {ph('12')} people", "Hourly or daily", "Screen and video calls"], "Bookable rooms for board meetings, interviews, one-to-one support sessions and training courses.")}
    {space("Community and event space", space_art("person", INK, SAND, BERRY), [f"Up to {ph('60')} people", "Evenings and weekends", "Kitchen access"], "A flexible hall for community activities, workshops, celebrations and public events, available to tenants and local groups.")}
  </div>
</div></section>

<section class="section bg-cream"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">Facilities</p>
    <h2>Everything included</h2>
    <p>{ph("Confirm facilities once the building is secured")}</p>
  </div>
  <div class="grid grid--4">
    <div class="card">{icon("wifi")}<h3>Fast Wi-Fi</h3><p class="mb-0">Reliable business broadband throughout.</p></div>
    <div class="card">{icon("access", "berry")}<h3>Accessible</h3><p class="mb-0">Step-free access and accessible toilets.</p></div>
    <div class="card">{icon("coffee", "amber")}<h3>Shared kitchen</h3><p class="mb-0">Tea, coffee and space to eat together.</p></div>
    <div class="card">{icon("mail", "ink")}<h3>Business address</h3><p class="mb-0">Mail handling and a registered address.</p></div>
    <div class="card">{icon("lock", "ink")}<h3>Secure access</h3><p class="mb-0">Key fob entry and secure storage.</p></div>
    <div class="card">{icon("users")}<h3>Reception</h3><p class="mb-0">A welcoming front door for your visitors.</p></div>
    <div class="card">{icon("car", "berry")}<h3>Travel</h3><p class="mb-0">{ph("Parking, bus and Metro links")}</p></div>
    <div class="card">{icon("calendar", "amber")}<h3>Tenant events</h3><p class="mb-0">Regular networking, training and socials.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">Rates</p>
    <h2>Fair, transparent pricing</h2>
    <p>We keep our rates affordable so organisations can spend more on their mission. Charities, CICs and community groups receive our social rate.</p>
  </div>
  <div class="table-wrap"><table>
    <thead><tr><th scope="col">Space</th><th scope="col">Social rate</th><th scope="col">Standard rate</th><th scope="col">What's included</th></tr></thead>
    <tbody>
      <tr><th scope="row">Private office</th><td>from {ph("£ per month")}</td><td>from {ph("£ per month")}</td><td>Furniture, utilities, Wi-Fi, cleaning, shared facilities</td></tr>
      <tr><th scope="row">Dedicated desk</th><td>{ph("£ per month")}</td><td>{ph("£ per month")}</td><td>Your own desk, storage, Wi-Fi, kitchen</td></tr>
      <tr><th scope="row">Flexible desk</th><td>{ph("£ per day")}</td><td>{ph("£ per day")}</td><td>Any available desk, Wi-Fi, kitchen</td></tr>
      <tr><th scope="row">Meeting room</th><td>{ph("£ per hour")}</td><td>{ph("£ per hour")}</td><td>Screen, video calling, refreshments on request</td></tr>
      <tr><th scope="row">Event space</th><td>{ph("£ per hour")}</td><td>{ph("£ per hour")}</td><td>Chairs, tables, kitchen access</td></tr>
    </tbody>
  </table></div>
  <p class="muted" style="margin-top:14px">Prices {ph("include or exclude")} VAT. Tenants receive discounted room hire. Ask us about free or reduced-cost space for grassroots community groups.</p>
</div></section>

<section class="section bg-sand"><div class="wrap split split--top">
  <div>
    <p class="eyebrow">Questions</p>
    <h2>Frequently asked questions</h2>
    <p>Can't find what you need? <a href="contact.html">Get in touch</a>.</p>
  </div>
  <div class="faq">
    <details><summary>Who can rent space at the Hub?</summary><div><p>We prioritise charities, social enterprises, CICs, community groups and start-ups with a social purpose. We also welcome other organisations whose work fits our values.</p></div></details>
    <details><summary>How long is the minimum commitment?</summary><div><p>Office licences start from {ph("e.g. three months")}, with one month's notice after that. Desks and rooms can be booked with no long-term commitment.</p></div></details>
    <details><summary>Can I visit before deciding?</summary><div><p>Yes. Once the Hub is open we will be happy to show you round. Register your interest and we will invite you to an open day.</p></div></details>
    <details><summary>Is the building accessible?</summary><div><p>Accessibility is central to our plans. {ph("Describe step-free access, lifts, accessible toilets and parking once confirmed.")}</p></div></details>
    <details><summary>Can community groups use the space for free?</summary><div><p>We aim to offer free or reduced-cost space to small grassroots groups where we can. Please talk to us about what you need.</p></div></details>
  </div>
</div></section>

<div id="interest-cta"></div>
{cta("Register your interest in the Hub", "Tell us what kind of space you need and we will be in touch with availability, rates and an invitation to visit.", [("Register interest", "contact.html#interest", "btn--amber")])}
''')


# ======================================================================= PROGRAMMES
def programme(id_, tone, tag, title, intro, items, who, icon_name):
    li = "".join(f"<li>{x}</li>" for x in items)
    return f'''<section class="section{" bg-cream" if tone == "berry" else ""}" id="{id_}"><div class="wrap split split--top">
  <div>
    {icon(icon_name, tone)}
    <p class="eyebrow" style="color:var(--{"amber-dark" if tone == "amber" else tone})">{tag}</p>
    <h2>{title}</h2>
    <p class="lede">{intro}</p>
    <p><strong>Who it's for:</strong> {who}</p>
    <div class="btn-row"><a class="btn btn--primary" href="contact.html">Ask about this programme</a></div>
  </div>
  <div class="card card--{tone}"><h3>What we offer</h3><ul class="ticks">{li}</ul></div>
</div></section>'''


add("programmes.html", "Programmes",
    "CDCE's programmes in employability, enterprise support and community inclusion help local people into work and help social enterprises start and grow.",
    f'''
{page_head("Programmes", "Alongside our space, we offer practical programmes that help local people into work, help social enterprises start and grow, and bring our diverse communities together.", "programmes", "Programmes")}

<section class="section--tight"><div class="wrap">
  <div class="notice mb-0"><strong>Programme development:</strong> our programmes are being designed with partners and local people, and will launch as funding is confirmed. {ph("Update with launch dates or remove this note")}</div>
</div></section>

{programme("employability", "teal", "Employability", "Routes into good work",
    "We support people who face barriers to employment to build confidence, gain skills and find work that suits them.",
    ["One-to-one coaching and personal action plans", "CV writing, applications and interview practice", "Digital skills and basic IT training", "Work placements and volunteering with Hub organisations", "Introductions to local employers and training providers", "Ongoing support in your first months at work"],
    "adults of any age who are unemployed, returning to work, changing careers or new to the UK.", "briefcase")}

{programme("enterprise", "berry", "Enterprise support", "Start, grow and sustain a social enterprise",
    "We help people with an idea for social change turn it into a sustainable organisation, and help existing organisations become stronger.",
    ["Start-up workshops: from idea to first customers", "Choosing the right legal structure, including CICs and charities", "Business planning, pricing and finance basics", "Funding and bid-writing clinics", "Governance, policies and safeguarding support", "Mentoring from experienced social entrepreneurs"],
    "aspiring social entrepreneurs, new CICs and charities, and community groups that want to grow.", "bulb")}

{programme("community", "amber", "Community and inclusion", "Bringing people together",
    "We create welcoming spaces and activities where people from different backgrounds can meet, share and build things together.",
    ["Cultural celebrations and community events", "Networks for women, young people and under-represented entrepreneurs", "Space and support for community-led projects", "Equality, diversity and inclusion training for organisations", "Partnership projects with local services and groups"],
    "residents, community groups and organisations across " + ph("Town or city") + " and the wider North East.", "users")}

{cta("Refer someone or partner on a programme", "We work with job centres, local services, charities and employers. Get in touch to make a referral or explore a partnership.", [("Contact us", "contact.html", "btn--amber"), ("Partner with us", "get-involved.html#partner", "btn--ghost")])}
''')


# ======================================================================= GET INVOLVED
def way(id_, ic, tone, title, text, bullets, link_text, link):
    li = "".join(f"<li>{b}</li>" for b in bullets)
    return f'''<article class="card card--{tone}" id="{id_}">{icon(ic, tone)}<h3>{title}</h3><p>{text}</p><ul class="ticks">{li}</ul><a class="link-arrow" href="{link}">{link_text}</a></article>'''


add("get-involved.html", "Get involved",
    "Fund, partner with, volunteer for or move into CDCE. Find out how you can help build a stronger, more inclusive North East.",
    f'''
{page_head("Get involved", "CDCE is built on partnership. There are many ways to be part of what we are creating, whatever your organisation or background.", "involved", "Get involved")}

<section class="section"><div class="wrap">
  <div class="grid grid--2">
    {way("fund", "pound", "teal", "Fund our work", "Grants and investment help us secure our building, keep our rates affordable and deliver free programmes for local people.", ["Capital funding for the Hub", "Programme and core funding", "Multi-year partnerships"], "Talk to us about funding", "contact.html")}
    {way("partner", "handshake", "berry", "Partner with us", "We work with councils, housing associations, colleges, employers and voluntary organisations to reach more people.", ["Deliver services from the Hub", "Co-design programmes", "Refer people to our support"], "Explore a partnership", "contact.html")}
    {way("business", "briefcase", "amber", "Support us as a business", "Local businesses can make a real difference through sponsorship, mentoring, work placements and supply-chain opportunities.", ["Sponsor an event or programme", "Offer mentoring or placements", "Buy from Hub social enterprises"], "Become a supporter", "contact.html")}
    {way("volunteer", "heart", "ink", "Volunteer", "Share your time and skills, from welcoming visitors to mentoring entrepreneurs or helping at events.", ["Flexible roles to suit you", "Training and references", "Meet people and build skills"], "Register as a volunteer", "contact.html")}
  </div>
</div></section>

<section class="section bg-ink"><div class="wrap split">
  <div>
    <p class="eyebrow">For funders</p>
    <h2>Why fund CDCE?</h2>
    <p class="lede">Every pound invested in CDCE works twice: it strengthens the organisations based at the Hub and the communities they serve.</p>
  </div>
  <ul class="ticks">
    <li><strong>Protected for the community.</strong> As a CIC, our assets are locked for community benefit.</li>
    <li><strong>Built to last.</strong> Income from space hire supports a sustainable model that reduces reliance on grants over time.</li>
    <li><strong>Measured impact.</strong> We track outcomes and publish an annual community interest report.</li>
    <li><strong>Local leadership.</strong> Our board and team have deep roots in the North East's voluntary and enterprise sectors.</li>
  </ul>
</div></section>

<section class="section"><div class="wrap split">
  <div class="photo-ph" role="img" aria-label="Photo placeholder"><div><strong>Photo placeholder</strong>People taking part in a CDCE event or workshop.<br>Recommended: 1200 × 900px.</div></div>
  <blockquote class="quote">
    "{ph("Add a short quote from a partner, funder or future tenant about why the Hub matters.")}"
    <footer>{ph("Name, role, organisation")}</footer>
  </blockquote>
</div></section>

{cta("Let's build something together", "Tell us a little about yourself and how you would like to be involved, and we will get back to you.", [("Get in touch", "contact.html", "btn--amber")])}
''')


# ======================================================================= NEWS
add("news.html", "News",
    "News, updates and stories from the Centre for Diversity, Community & Enterprise.",
    f'''
{page_head("News and updates", "The latest from CDCE: our progress on the Hub, programme launches, events and stories from our community.", "news", "News")}
<section class="section"><div class="wrap">
  <div class="notice">{ph("These are suggested first articles. Write them up, add dates and link each card to a full article page, or remove any you don't need.")}</div>
  <div class="grid grid--3">{NEWS_CARDS}</div>
</div></section>
<section class="section bg-cream"><div class="wrap narrow center" style="margin:0 auto">
  <h2>Stay in touch</h2>
  <p>Follow us for updates on the Hub, events and opportunities.</p>
  <div class="btn-row" style="justify-content:center">
    <a class="btn btn--ghost" href="#">LinkedIn</a><a class="btn btn--ghost" href="#">Facebook</a><a class="btn btn--ghost" href="#">Instagram</a>
  </div>
  <p class="muted" style="margin-top:16px">{ph("Add social media links, or a newsletter sign-up")}</p>
</div></section>
''')


# ======================================================================= CONTACT
FORM_ACTION = "https://formspree.io/f/YOUR_FORM_ID"
add("contact.html", "Contact us",
    "Contact CDCE about space at the Hub, our programmes, partnerships, funding or volunteering.",
    f'''
{page_head("Contact us", "Whether you are looking for space, want to join a programme or would like to work with us, we would love to hear from you.", "contact", "Contact us")}

<section class="section"><div class="wrap split split--top">
  <div id="interest">
    <h2>Send us a message</h2>
    <p>Fill in the form and we will reply within {ph("five working days")}. Fields marked <span class="req">*</span> are required.</p>
    <form class="form" action="{FORM_ACTION}" method="POST" data-cdce-form novalidate>
      <div class="form__row">
        <div><label for="name">Your name <span class="req">*</span></label><input id="name" name="name" type="text" autocomplete="name" required></div>
        <div><label for="email">Email address <span class="req">*</span></label><input id="email" name="email" type="email" autocomplete="email" required></div>
      </div>
      <div class="form__row">
        <div><label for="org">Organisation (if any)</label><input id="org" name="organisation" type="text" autocomplete="organization"></div>
        <div><label for="phone">Phone (optional)</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
      </div>
      <div>
        <label for="topic">What is your enquiry about? <span class="req">*</span></label>
        <select id="topic" name="topic" required>
          <option value="">Please choose</option>
          <option>Office or desk space at the Hub</option>
          <option>Booking a meeting room or event space</option>
          <option>Employability support</option>
          <option>Enterprise support</option>
          <option>Funding or partnership</option>
          <option>Volunteering</option>
          <option>Media enquiry</option>
          <option>Something else</option>
        </select>
      </div>
      <div><label for="message">Your message <span class="req">*</span></label><textarea id="message" name="message" required></textarea></div>
      <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
      <label class="check"><input type="checkbox" name="consent" required> <span>I agree to CDCE using these details to respond to my enquiry, as explained in the <a href="privacy.html">privacy notice</a>. <span class="req">*</span></span></label>
      <div><button class="btn btn--primary" type="submit">Send message</button></div>
      <div class="form__status" role="status" tabindex="-1"></div>
    </form>
  </div>
  <aside>
    <div class="card bg-cream" style="border:0">
      <h2 style="font-size:1.5rem">Other ways to reach us</h2>
      <ul class="contact-list">
        <li>{icon("mail")}<div><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
        <li>{icon("phone", "berry")}<div><strong>Phone</strong>{ph("Phone number")}</div></li>
        <li>{icon("pin", "amber")}<div><strong>Address</strong>{ph("Hub address")}<br>{ph("Town or city")}, {ph("Postcode")}</div></li>
        <li>{icon("clock", "ink")}<div><strong>Opening hours</strong>{ph("e.g. Monday to Friday, 9am to 5pm")}</div></li>
      </ul>
      <p class="mb-0 muted">If you need information in another format or language, or need support to get in touch, please tell us and we will do our best to help.</p>
    </div>
    <div class="photo-ph" style="aspect-ratio:16/10;margin-top:24px" role="img" aria-label="Map placeholder"><div><strong>Map placeholder</strong>Add a map image or embed once the Hub address is confirmed.</div></div>
  </aside>
</div></section>
''')


# ======================================================================= POLICIES
def pol(title, text):
    return f'<div class="card">{icon("file", "ink")}<h3>{title}</h3><p>{text}</p><p class="mb-0">{ph("Add PDF link once approved by the board")}</p></div>'


add("policies.html", "Policies",
    "CDCE's governance documents and policies, including safeguarding, equality, complaints and community interest reports.",
    f'''
{page_head("Policies and governance", "We are committed to being open and accountable. Our key policies and reports are published here.", "policy", "Policies")}
<section class="section"><div class="wrap">
  <div class="grid grid--3">
    {pol("Safeguarding policy", "How we keep children, young people and adults at risk safe in our building and programmes.")}
    {pol("Equality, diversity and inclusion", "Our commitment to fairness, inclusion and tackling discrimination in everything we do.")}
    {pol("Complaints procedure", "How to raise a concern or complaint, and how we will respond.")}
    {pol("Conflicts of interest", "How our directors declare and manage interests so decisions are always made in CDCE's best interest.")}
    {pol("Health and safety", "How we keep everyone who uses the Hub safe.")}
    {pol("Volunteer policy", "How we recruit, support and value our volunteers.")}
    <div class="card">{icon("lock", "ink")}<h3>Privacy notice</h3><p>How we collect, use and protect personal information.</p><a class="link-arrow" href="privacy.html">Read the privacy notice</a></div>
    <div class="card">{icon("access", "ink")}<h3>Accessibility statement</h3><p>How we make this website usable for as many people as possible.</p><a class="link-arrow" href="accessibility.html">Read the statement</a></div>
    <div class="card">{icon("file", "ink")}<h3>Articles of association</h3><p>Our governing document, available from Companies House.</p><a class="link-arrow" href="https://find-and-update.company-information.service.gov.uk/">View on Companies House</a></div>
  </div>
</div></section>
<section class="section bg-cream" id="reports"><div class="wrap narrow">
  <h2>Community interest reports</h2>
  <p>As a CIC we publish an annual community interest report explaining what we have done to benefit the community. Our first report will be published after the end of our first financial year, {ph("financial year end date")}.</p>
  <h3>Safeguarding concerns</h3>
  <p>If you have a concern about the safety of a child or adult connected with CDCE, contact our Designated Safeguarding Lead at {ph("safeguarding email")}. If someone is in immediate danger, call 999.</p>
</div></section>
''')


# ======================================================================= PRIVACY
add("privacy.html", "Privacy notice",
    "How the Centre for Diversity, Community & Enterprise CIC collects, uses and protects your personal information.",
    f'''
{page_head("Privacy notice", "How we collect, use and protect your personal information.", "policy", "Privacy notice")}
<section class="section"><div class="wrap narrow prose">
  <div class="notice">This is a starting template. {ph("Have it reviewed and approved by the board before publishing, and update it if you add new forms, newsletters or analytics.")} Last updated: {ph("date")}.</div>
  <h2>Who we are</h2>
  <p>{LEGAL} ("CDCE", "we", "us") is the data controller for personal information collected through this website and our activities. Company number {ph("company number")}. Registered office: {ph("registered office address")}. ICO registration number: {ph("ICO registration number")}.</p>
  <p>You can contact us about data protection at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <h2>Information we collect</h2>
  <ul>
    <li><strong>Enquiries:</strong> your name, email address and any details you include when you contact us through our website, by email or by phone.</li>
    <li><strong>Tenants and room hire:</strong> contact and billing details needed to provide space and services.</li>
    <li><strong>Programme participants:</strong> information needed to provide support, which may include information about your circumstances. Where we collect sensitive information we will explain why and ask for your consent where required.</li>
    <li><strong>Volunteers and partners:</strong> contact details and information needed to manage the relationship.</li>
  </ul>
  <h2>How we use it and our lawful basis</h2>
  <p>We use your information to respond to enquiries, provide our services, manage tenancies and bookings, run programmes, meet our legal obligations and report on our impact (using anonymised information wherever possible). Our lawful bases under UK GDPR are consent, contract, legal obligation and legitimate interests, depending on the activity.</p>
  <h2>Website forms</h2>
  <p>Messages sent through our contact form are processed by {ph("form provider, e.g. Formspree")} on our behalf and delivered to our email inbox. We do not use your details for marketing unless you have asked us to.</p>
  <h2>Cookies and analytics</h2>
  <p>This website does not use cookies or tracking technologies. Fonts are hosted on our own website, so no information is sent to third parties when you browse. {ph("Update this section if you add analytics, maps or video embeds.")}</p>
  <h2>Sharing your information</h2>
  <p>We do not sell your information. We share it only with trusted service providers who help us run CDCE (such as IT, email and finance providers), with funders in anonymised form, or where the law requires it, for example to protect someone from harm.</p>
  <h2>How long we keep it</h2>
  <p>We keep personal information only as long as we need it. {ph("Add retention periods, e.g. enquiries for 2 years, financial records for 6 years.")}</p>
  <h2>Your rights</h2>
  <p>You have the right to access, correct or delete your information, to object to or restrict how we use it, to data portability, and to withdraw consent at any time. To make a request, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <p>If you are unhappy with how we have handled your information, please tell us. You can also complain to the Information Commissioner's Office at <a href="https://ico.org.uk/make-a-complaint/">ico.org.uk</a> or on 0303 123 1113.</p>
</div></section>
''')


# ======================================================================= ACCESSIBILITY
add("accessibility.html", "Accessibility statement",
    "How CDCE makes its website accessible, and how to contact us if you have difficulty using it.",
    f'''
{page_head("Accessibility statement", "We want everyone to be able to use our website and our services.", "policy", "Accessibility")}
<section class="section"><div class="wrap narrow prose">
  <h2>Using this website</h2>
  <p>This website is run by {LEGAL}. It has been designed to meet the Web Content Accessibility Guidelines (WCAG) 2.2 at level AA. You should be able to:</p>
  <ul>
    <li>zoom in up to 400% without text spilling off the screen</li>
    <li>navigate the website using just a keyboard</li>
    <li>navigate the website using a screen reader</li>
    <li>change colours, contrast levels and fonts using your browser or device settings</li>
  </ul>
  <h2>Our approach</h2>
  <ul>
    <li>Text and background colours meet contrast standards.</li>
    <li>Pages use clear headings, landmarks and a "skip to main content" link.</li>
    <li>Forms have visible labels and clear error messages.</li>
    <li>We avoid moving content and respect your device's reduced-motion setting.</li>
  </ul>
  <h2>Known issues</h2>
  <p>Some documents we link to, such as older PDFs, may not be fully accessible. If you need information in a different format, please contact us.</p>
  <h2>Feedback and contact</h2>
  <p>If you find a problem with this website or need information in another format, such as large print, easy read or another language, email <a href="mailto:{EMAIL}">{EMAIL}</a>. We aim to respond within {ph("five working days")}.</p>
  <h2>Our building</h2>
  <p>{ph("Describe physical accessibility of the Hub once confirmed: step-free access, lifts, accessible toilets, hearing loop, quiet spaces and parking.")}</p>
  <p class="muted">This statement was prepared on {ph("date")}.</p>
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
    <div class="card card--berry"><h3>Clear and plain</h3><p class="mb-0">Short sentences and everyday words. Explain jargon such as "CIC" or "asset lock" the first time you use it.</p></div>
    <div class="card card--amber"><h3>Credible and honest</h3><p class="mb-0">Be specific about what we do and what we have achieved. Don't overclaim; funders and communities value honesty.</p></div>
  </div>
  <h3 style="margin-top:40px">Naming</h3>
  <p>Write <strong>Centre for Diversity, Community &amp; Enterprise</strong> in full the first time, then <strong>CDCE</strong>. The legal name is <strong>{LEGAL}</strong> and should appear on official documents, invoices and the website footer. Always use UK English spelling ("centre", "organisation").</p>
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
    <p class="lede">CDCE is a new not-for-profit community organisation in the North East creating space, support and opportunity for social enterprises, charities, community groups and local people.</p>
    <div class="hold__art" aria-hidden="true">{PILLAR_ART["diversity"]}{PILLAR_ART["community"]}{PILLAR_ART["enterprise"]}</div>
    <p>To find out more, or to register your interest, email us at</p>
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
