# CDCE website (cdce.org.uk)

Static website and brand kit for the **Centre for Diversity, Community & Enterprise CIC**.
No database or CMS: plain HTML, CSS and a small script, so it can be hosted almost anywhere for free or very cheaply.

## What's here

| Path | What it is |
|---|---|
| `site/` | The finished website. Upload the **contents** of this folder to your host. |
| `site/brand.html` | Brand guidelines (logo, colours, fonts, tone of voice). Not linked from the menu and hidden from search engines. Open `cdce.org.uk/brand.html` to share with designers. |
| `site/brand/logos/` | All logo files, SVG and transparent PNG: horizontal, stacked and mark-only, in colour, reversed, navy and white. |
| `site/assets/img/og-image.png` | The preview image shown when the site is shared on LinkedIn, Facebook, WhatsApp etc. |
| `cdce-website.zip` | The `site/` folder zipped, ready to upload. |
| `_source/` | The scripts that generated the site (only needed if Claude makes further changes). |

### Pages
Home, About us, The Hub, Programmes, Get involved, News, Contact, Policies, Privacy notice, Accessibility statement, a 404 page, and the brand guidelines page.

## Before you publish: fill in the placeholders

Everything you need to fill in or confirm is highlighted **yellow with a dashed underline** on the pages and written in square brackets, e.g. `[company number]`. In the HTML they look like `<mark class="ph">[company number]</mark>`. Replace the whole `<mark ...>...</mark>` tag with your text. Searching all files for `class="ph"` finds every one (VS Code: *Edit → Replace in Files*).

**On every page (header/footer), replace these across all files at once:**
- `[Town or city]`: where the Hub will be
- `[Phone number]`
- `[Hub address, North East]`
- `[company number]`: from Companies House
- `[registered office address]`
- Social media links: the footer's LinkedIn / Facebook / Instagram links currently point to `#`. Replace with your profile URLs, or delete any you don't use.

**Home (`index.html`)**: opening date/status line; office size (`[2 to 8]`), meeting room (`[12]`) and hall (`[60]`) capacities; three-year targets (`[25]`, `[300]`, `[40]`, `[100]`%), which are suggestions for the board to confirm; funder/partner logos; news dates and links.

**About (`about.html`)**: founding year and story; board and management names, roles and bios (please get each person's OK before publishing); a photo.

**The Hub (`hub.html`)**: status banner; capacities; facilities and travel links; all prices (social and standard rates) and VAT; minimum licence term; accessibility details.

**Programmes**: the "programme development" note (update with launch dates or remove).

**Get involved**: a partner or funder quote and photo.

**News**: dates and full articles for the three suggested posts, or remove them; social links.

**Contact**: address, postcode, opening hours, response time, map.

**Policies**: links to each approved policy (PDF), financial year end, safeguarding contact email.

**Privacy notice**: ICO registration number, form provider, retention periods, date. Have the board review it before going live.

**Accessibility statement**: building accessibility details and date.

### Assumptions to check
- **Email**: the site uses `hello@cdce.org.uk` throughout. If you choose a different address, search and replace it in all `.html` files and in `assets/js/main.js`.
- **Legal name**: the footer and privacy notice say "Centre for Diversity, Community & Enterprise CIC". Check this matches Companies House exactly.
- **Hub status**: the copy is written for a hub that is still being developed (register interest, opening soon). Update it once the building is secured.
- **No real photos yet**: dashed boxes mark where photos should go. Real photos of people and the building will make the biggest difference to how professional the site feels.

## Contact form setup

The contact form needs a form service to deliver messages by email (static sites can't send email themselves). Until it's set up, pressing *Send* shows a message asking people to email `hello@cdce.org.uk` instead.

1. Create a free account at **formspree.io** using a CDCE email address (not a personal one).
2. Create a form and copy its ID (looks like `xyzabcde`).
3. In `site/contact.html`, replace `YOUR_FORM_ID` in `action="https://formspree.io/f/YOUR_FORM_ID"` with your ID.

(If you host on Netlify you can use Netlify Forms instead. Ask Claude to switch it.)

## Automated publishing with GitHub (recommended)

This folder is ready to be a GitHub repository. Every time a change is pushed to the `main` branch, `.github/workflows/deploy.yml` checks the links and publishes `site/` to GitHub Pages at cdce.org.uk. Hosting is free.

**One-time setup**
1. Create a free GitHub **organisation** for CDCE (e.g. `cdce-org`) using a CDCE email address, and add at least two board members as owners. Don't host it under a personal account.
2. Create a **public** repository in it, e.g. `website`, and upload the contents of this folder (including the hidden `.github` folder). Claude can do this step for you once GitHub is connected.
3. In the repository, go to **Settings → Pages** and set **Source** to **GitHub Actions**. The first deployment runs automatically.
4. At your domain registrar, add these DNS records for `cdce.org.uk`:
   - Four `A` records for `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - One `CNAME` record for `www` pointing to `<your-org>.github.io`
5. Back in **Settings → Pages**, enter `cdce.org.uk` as the custom domain, wait for the DNS check to pass (minutes to a few hours), then tick **Enforce HTTPS**.
6. Recommended: in the organisation's settings, verify the domain under **Pages → Verified domains** so no one else can claim it.

**Making changes afterwards**: edit files on github.com (pencil icon) or ask Claude, commit to `main`, and the site updates within a couple of minutes. The *Actions* tab shows each deployment.

## Other hosting options

Any static host works. Good free options:
- **Cloudflare Pages** or **Netlify**: drag and drop the `site` folder (or the zip) in the dashboard, then add `cdce.org.uk` as a custom domain. Free HTTPS is included.
- **GitHub Pages**: free, needs a GitHub account.
- **Your domain registrar's hosting** (cPanel etc.): upload the contents of `site/` into `public_html`.

Then point the domain at the host using the DNS records the host gives you. Set up both `cdce.org.uk` and `www.cdce.org.uk`.

**Ownership:** register the domain, hosting, email and form accounts in CDCE's name with a CDCE email address, and give at least two board members admin access. Avoid using anyone's personal accounts.

### Good to know
- No cookies, analytics or third-party trackers, so no cookie banner is needed. Fonts are self-hosted (no Google Fonts calls). If you add analytics later, update the privacy notice.
- Built to WCAG 2.2 AA: keyboard navigation, skip link, contrast-checked colours, reduced-motion support, mobile-friendly.
- `sitemap.xml` and `robots.txt` are included. After launch, add the site to **Google Search Console** and submit the sitemap.
- Fonts: Plus Jakarta Sans and Source Sans 3, both under the SIL Open Font License (licence files in `site/assets/fonts/`).
