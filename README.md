# CDCE website (cdce.org.uk)

Static website and brand kit for the **Centre for Diversity, Community & Enterprise**.
No database or CMS: plain HTML, CSS and a small script, so it can be hosted almost anywhere for free or very cheaply.

## Holding page (current mode)

The site is currently in **holding mode**: cdce.org.uk shows a simple "coming soon" page. The full site is shareable at **cdce.org.uk/draft**, which opens the full homepage (`/home.html`). All other pages are public as normal; only the preview homepage is kept out of search results.

To launch the full site, set `HOLDING = False` in `_source/build.py` and rebuild (or ask Claude to "take the site out of holding mode").

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
Home, Coworking Thursdays, About us, Contact, Privacy notice, Accessibility statement, a 404 page, and the brand guidelines page. The site was simplified in November 2026 around the first offer, Coworking Thursdays; more pages (programmes, news, policies) can come back later.

## Before you publish

Placeholders are highlighted **yellow with a dashed underline** and written in square brackets. In the HTML they look like `<mark class="ph">[...]</mark>`. Only one remains:

- `[Divercity Hub street address and postcode]` on the Coworking Thursdays and Contact pages (set `VENUE_ADDRESS` in `_source/parts.py`).

## Booking link

Every "Book a free desk" button uses `BOOKING_URL` in `_source/parts.py`. For now it opens an email to `hello@cdce.org.uk` with the subject filled in. Once the Google Form exists, replace it with the form's link and rebuild (or search and replace the `mailto:` link in the `.html` files). The first session date and the weekly capacity (20) are also set there.

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
