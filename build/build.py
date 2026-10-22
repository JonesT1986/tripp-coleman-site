#!/usr/bin/env python3
"""Builds the static site into ../public. Run: python3 build/build.py"""
import json, os, re, datetime, html
from site_data import *
from pages import SERVICE_PAGES, AREA_PAGES

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "..", "public")
TODAY = datetime.date.today().isoformat()
GA_ID = "G-LT49P4LT8C"
PLAUSIBLE_DOMAIN = "" # or a domain if using Plausible instead
GSC_VERIFY = ""       # Google Search Console HTML-tag verification code

tpl = open(os.path.join(ROOT, "home_template.html")).read()
esc = html.escape

# ------------------------------------------------------------------ assets
css = tpl[tpl.index("<style>") + 7: tpl.index("</style>")]
css += open(os.path.join(ROOT, "extra.css")).read()

js_all = tpl[tpl.index("<script>\n") + 9: tpl.rindex("</script>")]
home_js = js_all[js_all.index("/* ---------- card texture painter"): js_all.index("/* ---------- booking")]
home_js = (home_js
  .replace("const tex = loader.load('{{TRIPP}}'), depth = loader.load('{{DEPTH}}');\n  [tex, depth].forEach", "const tex = loader.load('/img/tripp.webp');\n  [tex].forEach")
  .replace("dmap:{value:depth}, ", "")
  .replace("uniform sampler2D dmap; ", "")
  .replace("float d=texture2D(dmap,uv).r;", "float d=0.;")
  .replace("{{TW}}", "625").replace("{{TH}}", "1100").replace("{{CU}}", "0.517").replace("{{CV}}", "0.56"))
assert "{{" not in home_js and "dmap" not in home_js
home_js = "(() => {\nconst REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;\n" + home_js + "\n})();\n"
site_js = open(os.path.join(ROOT, "site.js")).read()

def write(rel, content):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(content)

write("assets/site.css", css)
write("assets/home.js", home_js)
write("assets/site.js", site_js)

# ------------------------------------------------------------------ schema
ID_SITE, ID_PERSON, ID_BIZ = SITE + "/#website", SITE + "/#tripp", SITE + "/#business"
TOWNS = ["Regina", "Pilot Butte", "White City", "Emerald Park", "Balgonie", "Moose Jaw", "Radville"]
def base_graph():
    return [
      {"@type": "WebSite", "@id": ID_SITE, "url": SITE + "/", "name": BIZ_NAME, "publisher": {"@id": ID_BIZ}, "inLanguage": "en-CA"},
      {"@type": "Person", "@id": ID_PERSON, "name": NAME, "alternateName": ALT_NAME, "jobTitle": "Magician",
       "url": SITE + "/about/", "image": SITE + "/img/ace.webp", "sameAs": SAME_AS,
       "homeLocation": {"@type": "Place", "name": "Pilot Butte, Saskatchewan"},
       "knowsAbout": ["Close-up magic", "Sleight of hand", "Card magic", "Street magic", "Stage magic", "Comedy magic"],
       "worksFor": {"@id": ID_BIZ}},
      {"@type": "EntertainmentBusiness", "@id": ID_BIZ, "name": BIZ_NAME, "alternateName": ALT_NAME,
       "url": SITE + "/", "telephone": "+1-306-209-8861", "email": EMAIL,
       "image": SITE + "/img/og-tripp-coleman.jpg", "priceRange": "From " + PRICE_FROM,
       "address": {"@type": "PostalAddress", "addressLocality": "Pilot Butte", "addressRegion": "SK", "addressCountry": "CA"},
       "areaServed": [{"@type": "City", "name": t + ", SK"} for t in TOWNS],
       "founder": {"@id": ID_PERSON}, "employee": {"@id": ID_PERSON}, "sameAs": SAME_AS,
       "description": "Close-up and stage magician Tripp Coleman (Trippmagic), based in Pilot Butte, Saskatchewan, performing birthday parties, corporate events, weddings, school and library shows and community events across Regina and southern Saskatchewan."},
    ]

def page_graph(url, name, desc, crumbs, extra=(), faq=None):
    g = base_graph()
    g.append({"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": name, "description": desc,
              "isPartOf": {"@id": ID_SITE}, "about": {"@id": ID_BIZ}, "breadcrumb": {"@id": url + "#breadcrumb"}, "inLanguage": "en-CA"})
    g.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]})
    g.extend(extra)
    if faq:
        g.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False) + "</script>"

# ------------------------------------------------------------------ layout
def head(title, desc, path, schema, img="/img/og-tripp-coleman.jpg", home=False):
    assert len(title) <= 60, (len(title), title)
    assert len(desc) <= 155, (len(desc), desc)
    url = SITE + path
    analytics = ""
    if GA_ID:
        analytics = f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{GA_ID}");</script>'
    elif PLAUSIBLE_DOMAIN:
        analytics = f'<script defer data-domain="{PLAUSIBLE_DOMAIN}" src="https://plausible.io/js/script.js"></script>'
    verify = f'<meta name="google-site-verification" content="{GSC_VERIFY}">' if GSC_VERIFY else ""
    scripts = '<script defer src="/assets/site.js"></script>'
    if home:
        scripts = ('<script defer src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'
                   '<script defer src="/assets/home.js"></script>' + scripts)
    return f'''<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(BIZ_NAME)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{img}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}{img}">
<meta name="theme-color" content="#0d0a09">
<meta name="geo.region" content="CA-SK"><meta name="geo.placename" content="Pilot Butte">
{verify}
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='10' fill='%230d0a09'/%3E%3Ctext x='32' y='46' font-size='40' text-anchor='middle' fill='%23d24a3e'%3E%E2%99%A5%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400;1,6..96,500&family=Hanken+Grotesk:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/site.css">
{schema}
{analytics}
{scripts}
</head>
<body{' class="home"' if home else ''}>
<a class="skip" href="#main">Skip to content</a>
'''

def header():
    return f'''<header class="top" id="top">
  <div class="wrap">
    <a class="logo" href="/" aria-label="{NAME}, home"><b>{NAME}</b><small>Trippmagic · The art of impossible</small></a>
    <nav class="nav" id="nav" aria-label="Main">
      <a href="/#services">Services</a>
      <a href="/#areas">Areas</a>
      <a href="/about/">About</a>
      <a href="/#faq">FAQ</a>
      <a href="tel:{PHONE_E164}" class="tel">{PHONE}</a>
      <a href="/contact/" class="pill">Book Tripp</a>
    </nav>
    <button class="menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
  </div>
</header>
'''

def footer():
    svc = "".join(f'<li><a href="/{s["slug"]}/">{s["label"]}</a></li>' for s in SERVICES)
    ar = "".join(f'<li><a href="/{a["slug"]}/">Magician in {a["town"]}</a></li>' for a in AREAS)
    return f'''<footer class="site-foot">
  <div class="wrap foot-grid">
    <div class="foot-nap">
      <a class="logo" href="/"><b>{NAME}</b><small>Trippmagic · The art of impossible</small></a>
      <address>
        <strong>{BIZ_NAME}</strong><br>
        {AREA_LINE}<br>
        <a href="tel:{PHONE_E164}">{PHONE}</a><br>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
      </address>
      <a class="btn btn-primary" href="/contact/">Book Tripp</a>
    </div>
    <div><h2>Services</h2><ul>{svc}</ul></div>
    <div><h2>Areas served</h2><ul>{ar}</ul></div>
    <div><h2>Follow & book</h2><ul>
      <li><a href="{FACEBOOK}" rel="noopener" target="_blank">Facebook</a></li>
      <li><a href="{INSTAGRAM}" rel="noopener" target="_blank">Instagram</a></li>
      <li><a href="{GIGSALAD}" rel="noopener" target="_blank">GigSalad</a></li>
      <li><a href="{AGNT}" rel="noopener" target="_blank">AGNT</a></li>
      <li><a href="/about/">About Tripp</a></li>
    </ul></div>
  </div>
  <div class="wrap foot-base"><span>&copy; <span id="yr">{datetime.date.today().year}</span> {BIZ_NAME}. Sleight of hand, no camera tricks.</span></div>
</footer>
<div class="mobile-bar" role="navigation" aria-label="Quick contact">
  <a class="btn btn-ghost" href="tel:{PHONE_E164}">Call Tripp</a>
  <a class="btn btn-primary" href="/contact/">Book now</a>
</div>
</body>
</html>
'''

def crumbs_html(items):
    parts = []
    for i, (n, u) in enumerate(items):
        if i < len(items) - 1:
            parts.append(f'<a href="{u.replace(SITE, "") or "/"}">{esc(n)}</a><span aria-hidden="true">/</span>')
        else:
            parts.append(f'<span aria-current="page">{esc(n)}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + "".join(parts) + "</nav>"

def faq_html(faq, title="Frequently asked questions"):
    items = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq)
    return f'<section class="block faq-block" id="faq"><div class="wrap narrow"><div class="eyebrow">FAQ</div><h2 class="sec-h">{title}</h2><div class="faq">{items}</div></div></section>'

def cta_band(text="Ready to book the impossible?"):
    return f'''<section class="cta-band"><div class="wrap"><h2>{text}</h2><div class="ctas">
<a class="btn btn-primary" href="/contact/">Check availability</a><a class="btn btn-ghost" href="tel:{PHONE_E164}">Call {PHONE}</a></div></div></section>'''

def testimonials_html():
    q = ""
    for t in TESTIMONIALS:
        meta = " · ".join(x for x in [t["name"], t["event"], t["town"], t["date"]] if x)
        q += f'<blockquote><p>&ldquo;{esc(t["quote"])}&rdquo;</p><cite>{esc(meta)}</cite></blockquote>'
    return q

def page_hero(crumbs, eyebrow, h1, answer, img, alt, facts=None):
    f = ""
    if facts:
        f = '<dl class="facts">' + "".join(f"<div><dt>{esc(a)}</dt><dd>{esc(b)}</dd></div>" for a, b in facts) + "</dl>"
    return f'''<section class="page-hero"><div class="wrap">
  <div class="ph-copy">
    {crumbs_html(crumbs)}
    <div class="eyebrow">{eyebrow}</div>
    <h1>{h1}</h1>
    <p class="answer">{answer}</p>
    <div class="ctas"><a class="btn btn-primary" href="/contact/">Book Tripp <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 12h17M14 6l6 6-6 6"/></svg></a><a class="btn btn-ghost" href="tel:{PHONE_E164}">Call {PHONE}</a></div>
    {f}
  </div>
  <figure class="ph-img"><img src="/img/{img}" alt="{esc(alt)}" width="720" height="1080" fetchpriority="high"></figure>
</div></section>
'''

def side(related_links, title="Related"):
    rl = "".join(f'<li><a href="{u}">{esc(n)}</a></li>' for n, u in related_links)
    return f'''<aside class="side">
  <div class="side-card"><h2>Book Tripp</h2><p>Call or text <a href="tel:{PHONE_E164}">{PHONE}</a> or send your date through the booking form.</p><a class="btn btn-primary" href="/contact/">Check availability</a></div>
  <div class="side-card"><h2>{title}</h2><ul>{rl}</ul></div>
</aside>'''

SVC_BY_SLUG = {s["slug"]: s for s in SERVICES}
AREA_BY_SLUG = {a["slug"]: a for a in AREAS}
def label_for(path):
    s = path.strip("/")
    if s in SVC_BY_SLUG: return SVC_BY_SLUG[s]["label"]
    if s in AREA_BY_SLUG: return "Magician in " + AREA_BY_SLUG[s]["town"]
    return s

pages = []  # (path, priority)

# ------------------------------------------------------------------ service pages
for slug, p in SERVICE_PAGES.items():
    s = SVC_BY_SLUG[slug]; path = f"/{slug}/"; url = SITE + path
    crumbs = [("Home", SITE + "/"), (s["label"], url)]
    service = {"@type": "Service", "@id": url + "#service", "name": p["h1"], "serviceType": s["name"],
               "provider": {"@id": ID_BIZ}, "areaServed": [{"@type": "City", "name": t + ", SK"} for t in TOWNS],
               "description": p["answer"], "url": url}
    body = "".join(f"<h2>{h}</h2>{c}" for h, c in p["sections"])
    rel = [(label_for(u), u) for u in p["related"]] + [("Magician in " + a["town"], f'/{a["slug"]}/') for a in AREAS[:3]]
    doc = (head(p["title"], p["desc"], path, page_graph(url, p["title"], p["desc"], crumbs, [service], p["faq"]))
           + header() + '<main id="main">'
           + page_hero(crumbs, "Tripp Coleman · " + s["label"], p["h1"], p["answer"], s["img"], s["alt"], p["facts"])
           + f'<div class="wrap content"><article class="prose">{body}</article>{side(rel, "More from Tripp")}</div>'
           + faq_html(p["faq"]) + cta_band() + "</main>" + footer())
    write(slug + "/index.html", doc); pages.append((path, "0.9"))

# ------------------------------------------------------------------ area pages
for slug, p in AREA_PAGES.items():
    a = AREA_BY_SLUG[slug]; path = f"/{slug}/"; url = SITE + path
    crumbs = [("Home", SITE + "/"), ("Magician in " + a["town"], url)]
    body = "".join(f"<h2>{h}</h2>{c}" for h, c in p["sections"])
    q = a["map"].replace(" ", "+").replace(",", "%2C")
    body += f'<h2>Map: {esc(a["town"])} and area</h2><div class="map"><iframe title="Map of {esc(a["town"])}, Saskatchewan" src="https://maps.google.com/maps?q={q}&amp;z=11&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>'
    rel = [(s["label"], f'/{s["slug"]}/') for s in SERVICES] + [("Magician in " + o["town"], f'/{o["slug"]}/') for o in AREAS if o["slug"] != slug][:2]
    doc = (head(p["title"], p["desc"], path, page_graph(url, p["title"], p["desc"], crumbs, (), p["faq"]))
           + header() + '<main id="main">'
           + page_hero(crumbs, "Serving " + a["town"], p["h1"], p["answer"], a["img"], a["alt"])
           + f'<div class="wrap content"><article class="prose">{body}</article>{side(rel, "Services in " + a["town"])}</div>'
           + faq_html(p["faq"]) + cta_band(f"Booking a magician in {a['town']}?") + "</main>" + footer())
    write(slug + "/index.html", doc); pages.append((path, "0.8"))

# ------------------------------------------------------------------ about
about_faq = [
  ("Who is Tripp Coleman?", "Tripp Coleman, also known as Trippmagic, is a self-taught close-up and stage magician based in Pilot Butte, Saskatchewan, who has been performing since 2017."),
  ("Is Trippmagic the same as Tripp Coleman?", "Yes. Trippmagic is Tripp Coleman's stage name and the name he uses on GigSalad, AGNT and social media."),
  ("Has Tripp performed in Las Vegas?", "Yes. Tripp has performed street magic in Las Vegas several times."),
  ("Who has Tripp performed for?", "His clients include Capital GMC, John Deere, eXp Realty, the Conexus Arts Centre and the Regina Public Library."),
]
path = "/about/"; url = SITE + path
crumbs = [("Home", SITE + "/"), ("About Tripp", url)]
title = "About Tripp Coleman | Regina Magician (Trippmagic)"
desc = "Tripp Coleman (Trippmagic) is a self-taught magician from Pilot Butte, SK, performing since 2017 for Capital GMC, John Deere and Las Vegas street crowds."
clients = "".join(f"<li>{c}</li>" for c in CLIENTS)
about_body = f'''
<h2>Background</h2>
<p><strong>Tripp started with simple card tricks as a kid and taught himself the rest.</strong> He has been performing professionally since {SINCE}, building his skills one audience at a time instead of through a magic school.</p>
<p>He has performed street magic in Las Vegas several times. Working a sidewalk crowd that never planned to stop is one of the toughest tests in magic, and it shaped the fast, interactive style he brings to every show.</p>
<h2>Style</h2>
<p>Tripp's magic is <strong>close-up, interactive and funny</strong>. He blends sleight of hand, card magic, street magic and comedy, with illusions for bigger stage shows. Audience members don't just watch: they hold the cards, call the choices and are often the ones the magic happens to.</p>
<h2>Clients and notable shows</h2>
<ul>{clients}</ul>
<p>Recent shows include a free family magic show at the Regina Public Library's Sherwood Village branch (February 2026), a family BBQ and a nonprofit event in Radville (July 2026), a seniors and day care show (August 2026) and a private cocktail party in Regina.</p>
<h2>What's next</h2>
<p>Tripp is currently working on a brand-new show. Follow him on <a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a> and <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a> to see it first.</p>
<h2>Where he performs</h2>
<p>Tripp is based in <a href="/magician-pilot-butte/">Pilot Butte</a>, about 10 minutes from <a href="/magician-regina/">Regina</a>, and travels up to about 200 miles for events, including <a href="/magician-white-city-emerald-park/">White City and Emerald Park</a>, <a href="/magician-balgonie/">Balgonie</a> and <a href="/magician-moose-jaw/">Moose Jaw</a>.</p>
<h2>Photos</h2>
<div class="mini-gal">
<img src="/img/rain.webp" alt="Tripp Coleman throwing a deck of cards into the air" width="720" height="1081" loading="lazy">
<img src="/img/spring.webp" alt="Tripp Coleman springing cards between his hands" width="720" height="1080" loading="lazy">
<img src="/img/hands.webp" alt="Close-up of Tripp Coleman's hands cutting a deck" width="720" height="1081" loading="lazy">
</div>
'''
rel = [(s["label"], f'/{s["slug"]}/') for s in SERVICES]
person_page = {"@type": "ProfilePage", "@id": url + "#profile", "url": url, "mainEntity": {"@id": ID_PERSON}}
doc = (head(title, desc, path, page_graph(url, title, desc, crumbs, [person_page], about_faq))
       + header() + '<main id="main">'
       + page_hero(crumbs, "About Tripp", "About Tripp Coleman", f"Tripp Coleman, known on stage as Trippmagic, is a self-taught magician from Pilot Butte, Saskatchewan, who has been performing since {SINCE}. He has worked the streets of Las Vegas and performed for Capital GMC, John Deere, eXp Realty and the Conexus Arts Centre.", "levitate.webp", "Magician Tripp Coleman shaping his hands around an invisible floating object",
                   [("Performing since", str(SINCE)), ("Based in", "Pilot Butte, SK"), ("Style", "Close-up & stage"), ("Travel", "Up to ~200 miles")])
       + f'<div class="wrap content"><article class="prose">{about_body}</article>{side(rel, "Book Tripp for")}</div>'
       + '<section class="block reviews"><div class="wrap"><div class="eyebrow">What people say</div><div class="quotes">' + testimonials_html() + f'</div><p class="fine">Reviews from verified bookings on <a href="{GIGSALAD}" target="_blank" rel="noopener">GigSalad</a>.</p></div></section>'
       + faq_html(about_faq) + cta_band() + "</main>" + footer())
write("about/index.html", doc); pages.append((path, "0.8"))

# ------------------------------------------------------------------ booking form (shared)
FORM = f'''<form id="bookForm" class="book-form" novalidate>
  <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
  <div class="f"><label for="bName">Your name</label><input id="bName" name="name" autocomplete="name" required></div>
  <div class="f"><label for="bEmail">Email</label><input id="bEmail" name="email" type="email" autocomplete="email" required></div>
  <div class="f"><label for="bPhone">Phone (optional)</label><input id="bPhone" name="phone" type="tel" autocomplete="tel"></div>
  <div class="f"><label for="bDate">Event date</label><input id="bDate" name="date" type="date"></div>
  <div class="f"><label for="bType">Event type</label>
    <select id="bType" name="type"><option>Birthday party</option><option>Corporate event</option><option>Wedding</option><option>School or library show</option><option>Private party</option><option>Community event</option><option>Something else</option></select></div>
  <div class="f"><label for="bGuests">Guests (approx.)</label><input id="bGuests" name="guests" inputmode="numeric" placeholder="e.g. 25"></div>
  <div class="f full"><label for="bCity">Town / venue</label><input id="bCity" name="city" placeholder="e.g. Regina, White City, Moose Jaw"></div>
  <div class="f full"><label for="bMsg">Tell Tripp about it</label><textarea id="bMsg" name="message" placeholder="The occasion, the crowd, ages of kids, anything he should know."></textarea></div>
  <div class="f full"><div class="err" id="bErr" role="alert"></div><button class="btn btn-primary" type="submit">Send booking request <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 12h17M14 6l6 6-6 6"/></svg></button></div>
</form>'''

CONTACT_ROWS = f'''<div class="contacts">
  <div class="contact-row"><span>Call or text</span><a href="tel:{PHONE_E164}" class="cval">{PHONE}</a><button type="button" class="copy" data-copy="{PHONE}">Copy</button></div>
  <div class="contact-row"><span>Email</span><a href="mailto:{EMAIL}" class="cval">{EMAIL}</a><button type="button" class="copy" data-copy="{EMAIL}">Copy</button></div>
  <div class="contact-row"><span>Instagram</span><a href="{INSTAGRAM}" target="_blank" rel="noopener" class="cval">@trippcoleman317</a></div>
  <div class="contact-row"><span>Facebook</span><a href="{FACEBOOK}" target="_blank" rel="noopener" class="cval">TrippMagic317</a></div>
</div>
<div class="contact-line"><span>Or book through</span><div class="platforms"><a class="btn btn-ghost" href="{GIGSALAD}/contact" target="_blank" rel="noopener">GigSalad</a><a class="btn btn-ghost" href="{AGNT}" target="_blank" rel="noopener">AGNT</a></div></div>'''

# ------------------------------------------------------------------ contact
contact_faq = [
  ("How do I book Tripp Coleman?", f"Call or text {PHONE}, email {EMAIL}, or send the booking form on this page with your date, town and event type."),
  ("How quickly will Tripp reply?", "Tripp replies to booking requests personally. Calling or texting is the fastest way to check a date."),
  ("What details should I include?", "Your event date, town or venue, type of event, approximate number of guests and the ages of any kids."),
  ("Can I book through GigSalad or AGNT?", "Yes. Tripp is listed on both GigSalad and AGNT if you prefer to book through a platform."),
]
path = "/contact/"; url = SITE + path
crumbs = [("Home", SITE + "/"), ("Book Tripp", url)]
title = "Book Tripp Coleman | Magician Regina, SK | 306-209-8861"
desc = f"Book Regina-area magician Tripp Coleman for birthdays, corporate events and weddings. Call or text {PHONE} or send a booking request online."
contact_page = {"@type": "ContactPage", "@id": url + "#contact", "url": url, "about": {"@id": ID_BIZ}}
doc = (head(title, desc, path, page_graph(url, title, desc, crumbs, [contact_page], contact_faq))
       + header() + '<main id="main">'
       + f'''<section class="block contact-page"><div class="wrap book">
  <div class="book-side">
    {crumbs_html(crumbs)}
    <div class="eyebrow">Bookings</div>
    <h1>Book Tripp Coleman</h1>
    <p class="answer">To book Tripp Coleman, call or text {PHONE} or send the form with your date and town. He performs across Regina, Pilot Butte, White City, Emerald Park, Balgonie, Moose Jaw and southern Saskatchewan.</p>
    {CONTACT_ROWS}
  </div>
  {FORM}
</div></section>
<section class="block" style="padding-top:0"><div class="wrap"><h2 class="sec-h">Service area</h2><p class="fine" style="text-align:left;margin:10px 0 24px">Based in Pilot Butte, SK. Travels up to about 200 miles (320 km).</p>
<div class="map wide"><iframe title="Map of Tripp Coleman's service area around Pilot Butte and Regina, Saskatchewan" src="https://maps.google.com/maps?q=Pilot+Butte%2C+SK&amp;z=9&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>'''
       + faq_html(contact_faq, "Booking questions") + "</main>" + footer())
write("contact/index.html", doc); pages.append((path, "0.9"))

# ------------------------------------------------------------------ home
start = tpl.index('<section class="hero"'); end = tpl.index("<footer>")
hb = tpl[start:end]
def rep(a, b):
    global hb
    assert hb.count(a) == 1, a[:80]
    hb = hb.replace(a, b)
rep('<div class="eyebrow">Not your ordinary magician</div>\n      <h1>Magic that hits <em>different.</em></h1>',
    '<h1><span class="h1-kicker">Tripp Coleman · Magician in Regina, SK</span>Magic that hits <em>different.</em></h1>')
rep('<p class="lede">Forget everything you think you know about magic. Real reactions. Impossible moments. One unforgettable experience.</p>',
    f'<p class="lede">Tripp Coleman (Trippmagic) is a close-up and stage magician from Pilot Butte, SK, performing birthday parties, corporate events, weddings and library shows across Regina and southern Saskatchewan since {SINCE}. Real reactions. Impossible moments.</p>')
rep('<a class="btn btn-primary" href="#book">', '<a class="btn btn-primary" href="/contact/">')
i = hb.index('<a class="btn btn-ghost" href="#trick">'); j = hb.index("</a>", i) + 4
hb = hb[:i] + f'<a class="btn btn-ghost" href="tel:{PHONE_E164}">Call {PHONE} <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2"/></svg></a>' + hb[j:]
rep('<img class="hero-poster" src="{{TRIPP}}" alt="">', '<img class="hero-poster" src="/img/tripp.webp" alt="" width="625" height="1100">')
rep('<div class="hint"><i></i>', '<a class="trick-link" href="#trick">or try a little magic &darr;</a>\n  <div class="hint"><i></i>')
rep('<img src="{{ACE}}"', '<img src="/img/ace.webp" width="720" height="1078" loading="lazy"')
# services + areas replace experiences
i = hb.index('<section class="block" id="experiences"'); j = hb.index('<section class="block trick"')
cards = ""
for s in SERVICES:
    p = SERVICE_PAGES[s["slug"]]
    cards += f'<a class="svc" href="/{s["slug"]}/"><span class="suit{" red" if s["red"] else ""}" aria-hidden="true">{s["suit"]}</span><h3>{s["label"]}</h3><p>{esc(p["answer"].split(". ")[0])}.</p><span class="more">Learn more &rarr;</span></a>'
areas = "".join(f'<li><a href="/{a["slug"]}/"><b>{a["town"]}</b><span>{esc(AREA_PAGES[a["slug"]]["answer"].split(". ")[0])}.</span></a></li>' for a in AREAS)
svc_sec = f'''<section class="block" id="services" style="padding-top:0">
  <div class="wrap">
    <div class="exp-head">
      <h2>Magic for every kind of event</h2>
      <p>Tripp performs five kinds of events. Pick yours to see what's included, show lengths and pricing.</p>
    </div>
    <div class="svc-grid">{cards}<a class="svc svc-cta" href="/contact/"><span class="suit" aria-hidden="true">?</span><h3>Something else?</h3><p>Tell Tripp about your event and he'll build a show around it.</p><span class="more">Ask Tripp &rarr;</span></a></div>
  </div>
</section>
<section class="block" id="areas" style="padding-top:0">
  <div class="wrap">
    <div class="exp-head"><h2>Areas served</h2><p>Based in Pilot Butte, about 10 minutes from Regina. Travels up to about 200 miles (320 km).</p></div>
    <ul class="area-list">{areas}</ul>
  </div>
</section>
'''
hb = hb[:i] + svc_sec + hb[j:]
# testimonials with name/event/town/date
hb, n = re.subn(r'<div class="quotes">.*?</div>', lambda m: '<div class="quotes">' + testimonials_html() + '</div>', hb, count=1, flags=re.S)
assert n == 1
# FAQ before booking
i = hb.index('<section class="block" id="book"')
hb = hb[:i] + faq_html(HOME_FAQ, "Magician questions, answered") + "\n" + hb[i:]
# booking: replace side contacts and form with shared versions
i = hb.index('<div class="contacts">'); j = hb.index('<form id="bookForm"')
k = hb.index("</form>", j) + 7
hb = hb[:i] + CONTACT_ROWS + "\n    </div>\n    " + FORM + hb[k:]
hb = re.sub(r"\{\{(\w+)\}\}", lambda m: "/img/" + m.group(1).lower() + ".webp", hb)
hb = hb.replace('<img loading="lazy" src=', '<img loading="lazy" width="720" height="1080" src=')
assert "{{" not in hb
title = "Tripp Coleman | Magician in Regina, SK | Trippmagic"
desc = "Regina-area magician Tripp Coleman (Trippmagic) performs birthday parties, corporate events, weddings and library shows across southern Saskatchewan."
crumbs = [("Home", SITE + "/")]
doc = (head(title, desc, "/", page_graph(SITE + "/", title, desc, crumbs, (), HOME_FAQ), home=True)
       + header() + '<main id="main">' + hb + "</main>" + footer())
write("index.html", doc); pages.insert(0, ("/", "1.0"))

# ------------------------------------------------------------------ 404
svc_links = "".join(f'<li><a href="/{s["slug"]}/">{s["label"]}</a></li>' for s in SERVICES)
doc404 = (head("Page not found | Tripp Coleman, Magician", "This page vanished. Find Tripp Coleman's magic shows for birthdays, corporate events and weddings in Regina.", "/404", "")
          .replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
          + header() + f'''<main id="main"><section class="block nf"><div class="wrap narrow"><div class="eyebrow">Error 404</div>
<h1>This page vanished.</h1><p class="answer">Nice trick, but not one of Tripp's. The page you wanted isn't here. Try one of these instead:</p>
<ul class="nf-links">{svc_links}<li><a href="/about/">About Tripp</a></li><li><a href="/contact/">Book Tripp</a></li></ul>
<a class="btn btn-primary" href="/">Back to the home page</a></div></section></main>''' + footer())
write("404.html", doc404)

# ------------------------------------------------------------------ sitemap, robots, llms, vercel
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for path, pr in pages:
    sm += f"  <url><loc>{SITE}{path}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n"
sm += "</urlset>\n"
write("sitemap.xml", sm)

bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User", "Google-Extended", "Googlebot", "Bingbot", "Applebot", "Applebot-Extended"]
robots = "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n"
write("robots.txt", robots)

llms = f"""# {NAME} (Trippmagic)

> {NAME}, known on stage as Trippmagic, is a self-taught close-up and stage magician based in Pilot Butte, Saskatchewan, Canada, performing since {SINCE}. He performs birthday parties, corporate events, weddings, school and library shows, private parties and community events across Regina and southern Saskatchewan.

## Key facts
- Name: {NAME} (stage name: {ALT_NAME})
- Based in: Pilot Butte, SK, about 10 minutes from Regina
- Service area: Regina, Pilot Butte, White City, Emerald Park, Balgonie, Moose Jaw, Radville and communities within about 200 miles (320 km)
- Performing since: {SINCE}
- Style: close-up, sleight of hand, card magic, street magic, comedy magic; illusions for stage shows
- Experience: street magic in Las Vegas several times
- Clients include: Capital GMC, John Deere, eXp Realty, Conexus Arts Centre, Regina Public Library
- Show length: 60 to 120 minutes
- Family shows: ages 4 and up
- Pricing: shows start at around {PRICE_FROM}
- Stage shows use a wireless headset microphone and PA system; close-up magic needs no setup
- Phone: {PHONE}
- Email: {EMAIL}

## Pages
- [Home]({SITE}/): overview, services, areas served, FAQ
- [About Tripp Coleman]({SITE}/about/): background, style, clients
- [Book Tripp]({SITE}/contact/): phone, email, booking form
""" + "".join(f"- [{s['label']}]({SITE}/{s['slug']}/)\n" for s in SERVICES) + "".join(f"- [Magician in {a['town']}]({SITE}/{a['slug']}/)\n" for a in AREAS) + f"""
## Profiles
- Facebook: {FACEBOOK}
- Instagram: {INSTAGRAM}
- AGNT: {AGNT}
- GigSalad: {GIGSALAD}
"""
write("llms.txt", llms)

vercel = {"outputDirectory": "public", "framework": None, "buildCommand": None, "cleanUrls": True, "trailingSlash": True,
  "headers": [
    {"source": "/img/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
    {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=86400"}]},
    {"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}]}]}
open(os.path.join(ROOT, "..", "vercel.json"), "w").write(json.dumps(vercel, indent=2))
print("built", len(pages), "pages")
