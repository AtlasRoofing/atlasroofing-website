#!/usr/bin/env python3
"""
Atlas Roofing & Restoration — Hyper-Local SEO Page Generator
Generates all 9 phrase types × 45 cities = 405 pages
Each page matches the exact HTML/CSS structure of existing site pages.
"""

import os, re
from city_data import CITIES

SITE_DIR = "/home/claude/site"

# ── Shared CSS (exact match from existing pages) ─────────────────────────────
SHARED_CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; font-size: 16px; }
body { font-family: 'Manrope', sans-serif; color: #111827; background: #fff; line-height: 1.6; overflow-x: hidden; }
a { text-decoration: none; color: inherit; }
img { max-width: 100%; height: auto; display: block; }
:root {
  --blue: #0076c1; --blue-dk: #005a94; --blue-lt: #e8f4fb;
  --green: #65c47b; --green-dk: #4aab61; --green-lt: #eaf7ed;
  --navy: #003d6b; --dark: #111827; --gray: #6b7280;
  --gray-lt: #f3f6f9; --border: #e2e8f0; --white: #ffffff;
  --grad: linear-gradient(135deg, #003d6b 0%, #005a94 60%, #0a6b52 100%);
  --grad-accent: linear-gradient(135deg, #0076c1, #65c47b);
  --shadow: 0 4px 20px rgba(0,0,0,0.10); --shadow-lg: 0 8px 40px rgba(0,0,0,0.15);
  --r: 8px; --r-lg: 14px;
}
.wrap { max-width: 1140px; margin: 0 auto; padding: 0 24px; }
.btn { display: inline-block; font-family: 'Manrope', sans-serif; font-weight: 700; font-size: 15px; padding: 13px 26px; border-radius: var(--r); cursor: pointer; transition: transform 0.15s, opacity 0.15s; white-space: nowrap; border: none; }
.btn:hover { transform: translateY(-1px); opacity: 0.92; }
.btn-blue { background: var(--blue); color: #fff; }
.btn-green { background: var(--green); color: #fff; }
.btn-outline-white { background: transparent; color: #fff; border: 2px solid rgba(255,255,255,0.5); }
.btn-outline-white:hover { border-color: #fff; }
.btn-outline-blue { background: transparent; color: var(--blue); border: 2px solid var(--blue); }
.btn-outline-blue:hover { background: var(--blue); color: #fff; }
.btn-white { background: #fff; color: var(--blue); }
.topbar { background: #0a1520; padding: 8px 0; }
.topbar .wrap { display: flex; align-items: center; justify-content: space-between; gap: 12px; }
.topbar-left { font-size: 12px; color: rgba(255,255,255,0.45); display: flex; align-items: center; gap: 20px; }
.topbar-left span { display: flex; align-items: center; gap: 5px; }
.topbar-left span::before { content: ''; display: inline-block; width: 5px; height: 5px; border-radius: 50%; background: var(--green); }
.topbar-phone { font-size: 17px; font-weight: 800; color: #fff; display: flex; align-items: center; gap: 7px; }
.topbar-phone:hover { color: var(--green); }
.nav { background: #fff; border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 100; box-shadow: 0 1px 12px rgba(0,0,0,0.06); }
.nav .wrap { display: flex; align-items: center; justify-content: space-between; height: 70px; gap: 16px; }
.nav-logo img { height: 42px; width: auto; display: block; }
.nav-links { display: flex; align-items: center; gap: 2px; list-style: none; }
.nav-links a { font-size: 14px; font-weight: 500; color: var(--gray); padding: 7px 12px; border-radius: 6px; transition: all 0.2s; }
.nav-links a:hover, .nav-links a.active { color: var(--blue); background: var(--blue-lt); }
.nav-right { display: flex; align-items: center; gap: 10px; flex-shrink: 0; }
.nav-tel { font-size: 14px; font-weight: 700; color: var(--blue); display: flex; align-items: center; gap: 5px; }
.hamburger { display: none; background: none; border: none; cursor: pointer; padding: 4px; flex-direction: column; gap: 5px; }
.hamburger span { display: block; width: 22px; height: 2px; background: var(--dark); border-radius: 2px; }
.mobile-nav { display: none; flex-direction: column; background: #fff; border-top: 1px solid var(--border); padding: 12px 24px 20px; gap: 2px; }
.mobile-nav.open { display: flex; }
.mobile-nav a { font-size: 15px; font-weight: 500; color: var(--dark); padding: 10px 0; border-bottom: 1px solid #f3f4f6; }
.mobile-nav .m-btn { margin-top: 12px; text-align: center; background: var(--blue); color: #fff; padding: 13px; border-radius: var(--r); font-weight: 700; font-size: 15px; border: none; display: block; }
.breadcrumb { background: var(--gray-lt); border-bottom: 1px solid var(--border); padding: 10px 0; }
.breadcrumb .wrap { display: flex; align-items: center; gap: 8px; font-size: 13px; color: var(--gray); }
.breadcrumb a { color: var(--blue); }
.section { padding: 80px 0; }
.section.gray { background: var(--gray-lt); }
.section-label { font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--blue); display: block; margin-bottom: 10px; }
.section-h { font-size: clamp(26px, 4vw, 42px); font-weight: 800; color: var(--dark); letter-spacing: -0.02em; line-height: 1.1; }
.section-sub { font-size: 16px; color: var(--gray); line-height: 1.7; max-width: 560px; margin-top: 12px; }
.section-header { margin-bottom: 48px; }
.section-header.center { text-align: center; }
.section-header.center .section-sub { margin: 12px auto 0; }
.trustbar { background: var(--gray-lt); border-bottom: 1px solid var(--border); padding: 14px 0; }
.trustbar .wrap { display: flex; align-items: center; justify-content: space-around; flex-wrap: wrap; gap: 10px; }
.trust-item { display: flex; align-items: center; gap: 9px; font-size: 13px; font-weight: 600; color: var(--dark); }
.trust-icon { width: 30px; height: 30px; border-radius: 7px; display: flex; align-items: center; justify-content: center; font-size: 14px; flex-shrink: 0; }
.trust-icon.blue { background: var(--blue-lt); }
.trust-icon.green { background: var(--green-lt); }
.final-cta { background: var(--grad-accent); padding: 80px 0; text-align: center; }
.final-cta h2 { font-size: clamp(30px, 5vw, 50px); font-weight: 800; color: #fff; letter-spacing: -0.02em; margin-bottom: 14px; }
.final-cta p { font-size: 17px; color: rgba(255,255,255,0.78); max-width: 460px; margin: 0 auto 34px; }
.final-btns { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
.footer { background: #0a1520; padding: 56px 0 26px; }
.footer-grid { display: grid; grid-template-columns: 1.5fr 1fr 1fr 1fr; gap: 40px; padding-bottom: 40px; border-bottom: 1px solid rgba(255,255,255,0.07); margin-bottom: 26px; }
.footer-logo img { height: 36px; margin-bottom: 14px; }
.footer-desc { font-size: 13px; color: rgba(255,255,255,0.4); line-height: 1.7; margin-bottom: 18px; }
.footer-contact { display: flex; flex-direction: column; gap: 8px; }
.footer-contact a { font-size: 13px; color: rgba(255,255,255,0.45); transition: color 0.2s; }
.footer-contact a:hover { color: var(--green); }
.footer-col-title { font-size: 10px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: rgba(255,255,255,0.22); margin-bottom: 14px; }
.footer-links { display: flex; flex-direction: column; gap: 8px; }
.footer-links a { font-size: 13px; color: rgba(255,255,255,0.45); transition: color 0.2s; }
.footer-links a:hover { color: var(--green); }
.footer-bottom { display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; font-size: 12px; color: rgba(255,255,255,0.25); }
.footer-badges { display: flex; gap: 8px; }
.fbadge { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.09); border-radius: 5px; padding: 3px 10px; font-size: 11px; color: rgba(255,255,255,0.35); }
.mob-bar { display: none; position: fixed; bottom: 0; left: 0; right: 0; z-index: 200; background: #0a1520; border-top: 2px solid var(--blue); padding: 10px 16px; gap: 10px; }
.mob-call { flex: 1; background: var(--grad-accent); color: #fff; font-weight: 800; font-size: 14px; padding: 12px; border-radius: var(--r); text-align: center; border: none; cursor: pointer; }
.mob-insp { flex: 1; background: transparent; color: #fff; font-weight: 700; font-size: 14px; padding: 12px; border-radius: var(--r); text-align: center; border: 1.5px solid rgba(255,255,255,0.25); cursor: pointer; }
.faq-list { display: flex; flex-direction: column; }
.faq-item { border-bottom: 1px solid var(--border); }
.faq-q { display: flex; justify-content: space-between; align-items: center; gap: 12px; padding: 17px 0; cursor: pointer; font-size: 15px; font-weight: 700; color: var(--dark); user-select: none; transition: color 0.2s; }
.faq-q:hover { color: var(--blue); }
.faq-toggle { width: 24px; height: 24px; border-radius: 50%; background: #e2e8f0; display: flex; align-items: center; justify-content: center; font-size: 18px; color: var(--gray); flex-shrink: 0; line-height: 1; transition: background 0.2s, transform 0.2s; }
.faq-item.open .faq-toggle { background: var(--blue); color: #fff; transform: rotate(45deg); }
.faq-a { font-size: 14px; color: var(--gray); line-height: 1.7; padding: 0 0 16px; display: none; }
.faq-item.open .faq-a { display: block; }
@media (max-width: 1000px) { .footer-grid { grid-template-columns: 1fr 1fr; } }
@media (max-width: 680px) { .topbar-left { display: none; } .nav-links, .nav-right .btn, .nav-tel { display: none; } .hamburger { display: flex; } .footer-grid { grid-template-columns: 1fr; } .mob-bar { display: flex; } body { padding-bottom: 64px; } .trustbar .wrap { justify-content: center; } }
.hero { background: var(--grad); padding: 64px 0; position: relative; overflow: hidden; }
.hero::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse at 80% 50%, rgba(101,196,123,0.12) 0%, transparent 60%); pointer-events: none; }
.hero-inner { position: relative; z-index: 1; max-width: 760px; }
.hero-badge { display: inline-flex; align-items: center; gap: 7px; background: rgba(101,196,123,0.15); border: 1px solid rgba(101,196,123,0.3); border-radius: 100px; padding: 5px 14px; font-size: 11px; font-weight: 700; letter-spacing: 0.1em; color: #a0eab0; text-transform: uppercase; margin-bottom: 18px; }
.hero-badge-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--green); }
.hero-h1 { font-size: clamp(32px,5vw,52px); font-weight: 800; color: #fff; line-height: 1.05; letter-spacing: -0.025em; margin-bottom: 16px; }
.hero-h1 .green { color: var(--green); }
.hero-p { font-size: 17px; color: rgba(255,255,255,0.68); line-height: 1.7; margin-bottom: 28px; max-width: 620px; }
.hero-btns { display: flex; gap: 12px; flex-wrap: wrap; }
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 52px; align-items: start; }
.checklist { list-style: none; display: flex; flex-direction: column; gap: 10px; }
.checklist li { display: flex; align-items: flex-start; gap: 10px; font-size: 15px; color: var(--gray); line-height: 1.55; }
.checklist li::before { content: '✓'; display: flex; align-items: center; justify-content: center; width: 20px; height: 20px; min-width: 20px; background: var(--green-lt); color: var(--green-dk); font-weight: 800; font-size: 11px; border-radius: 50%; margin-top: 2px; }
.checklist li strong { color: var(--dark); font-weight: 600; }
.review-box { background: var(--gray-lt); border-radius: var(--r-lg); padding: 24px 28px; border-left: 4px solid var(--green); }
.review-stars { color: #ffc93c; font-size: 16px; letter-spacing: 2px; margin-bottom: 10px; }
.review-text { font-size: 15px; color: var(--gray); line-height: 1.7; font-style: italic; margin-bottom: 14px; }
.review-author { font-size: 13px; font-weight: 700; color: var(--dark); }
.review-source { font-size: 12px; color: var(--gray); }
.cta-box { background: var(--grad-accent); border-radius: var(--r-lg); padding: 40px; text-align: center; margin-top: 48px; }
.cta-box h3 { font-size: 26px; font-weight: 800; color: #fff; margin-bottom: 10px; }
.cta-box p { font-size: 16px; color: rgba(255,255,255,0.8); margin-bottom: 24px; }
.cta-box-btns { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
@media(max-width:900px){ .two-col{grid-template-columns:1fr;gap:32px;} }
"""

# ── Nav/Footer shared HTML ────────────────────────────────────────────────────
def nav_html():
    return """<div class="topbar"><div class="wrap"><div class="topbar-left"><span>23945 Mercantile Rd, Suite D — Beachwood, OH</span><span>BBB A+ Accredited</span><span>GAF Certified</span></div><a href="tel:2168883208" class="topbar-phone">☎ (216) 888-3208</a></div></div>
<nav class="nav"><div class="wrap"><a href="/" class="nav-logo"><img src="../logo.png" alt="Atlas Roofing &amp; Restoration — Cleveland Ohio Roofing Contractor"></a><ul class="nav-links"><li><a href="/residential-roofing/">Residential</a></li>
<li><a href="/commercial-roofing/">Commercial</a></li>
<li><a href="/gutters/">Gutters</a></li>
<li><a href="/siding/">Siding</a></li>
<li><a href="/insurance-claims/">Insurance</a></li>
<li><a href="/#instant-estimates">Estimate</a></li>
<li><a href="/about/">About</a></li></ul><div class="nav-right"><a href="tel:2168883208" class="nav-tel">☎ (216) 888-3208</a><a href="/contact/" class="btn btn-blue">Free Inspection</a></div><button class="hamburger" onclick="document.getElementById('mobileNav').classList.toggle('open')" aria-label="Menu"><span></span><span></span><span></span></button></div>
<div class="mobile-nav" id="mobileNav"><a href="/residential-roofing/">Residential Roofing</a><a href="/commercial-roofing/">Commercial Roofing</a><a href="/gutters/">Gutters</a><a href="/siding/">Siding</a><a href="/insurance-claims/">Insurance Claims</a><a href="/#instant-estimates">Instant Estimate</a><a href="/financing/">Financing</a><a href="/about/">About Us</a><a href="/contact/" class="m-btn">Get Free Inspection</a></div></nav>"""

def footer_html():
    return """<footer class="footer"><div class="wrap">
<div class="footer-grid">
<div><div class="footer-logo"><img src="../logo-dark.png" alt="Atlas Roofing &amp; Restoration — Cleveland Ohio Roofing Contractor"></div><p class="footer-desc">Cleveland and Northeast Ohio's trusted roofing contractor. GAF certified, BBB A+ rated.</p><div class="footer-contact"><a href="tel:2168883208">☎ (216) 888-3208</a><a href="mailto:office@atlasroofingrestoration.com">✉ office@atlasroofingrestoration.com</a><a href="#">📍 23945 Mercantile Rd, Suite D, Beachwood OH 44122</a></div>
<div style="display:flex;gap:12px;margin-top:14px;">
<a href="https://www.facebook.com/atlasroofingrestoration" target="_blank" rel="noopener" style="width:34px;height:34px;border-radius:8px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.12);display:flex;align-items:center;justify-content:center;font-size:16px;color:rgba(255,255,255,0.6);transition:all 0.2s;" title="Facebook">f</a>
<a href="https://www.instagram.com/atlasroofingrestoration" target="_blank" rel="noopener" style="width:34px;height:34px;border-radius:8px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.12);display:flex;align-items:center;justify-content:center;font-size:14px;color:rgba(255,255,255,0.6);transition:all 0.2s;" title="Instagram">📷</a>
<a href="https://www.google.com/maps/place/Atlas+Roofing+%26+Restoration/@41.4608547,-81.5060061,707m/data=!3m2!1e3!5s0x883102a495403b37:0xfd9c252c052527cd!4m8!3m7!1s0x883102bd2b5a73b9:0x92937d2914e8a622!8m2!3d41.4608547!4d-81.5060061!9m1!1b1!16s%2Fg%2F11vkr36yfr?entry=ttu&g_ep=EgoyMDI2MDQxMi4wIKXMDSoASAFQAw%3D%3D" target="_blank" rel="noopener" style="width:34px;height:34px;border-radius:8px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.12);display:flex;align-items:center;justify-content:center;font-size:14px;color:rgba(255,255,255,0.6);transition:all 0.2s;" title="Google Reviews">⭐</a>
</div></div>
<div><div class="footer-col-title">Services</div><div class="footer-links"><a href="/residential-roofing/">Residential Roofing</a><a href="/commercial-roofing/">Commercial Roofing</a><a href="/gutters/">Gutters</a><a href="/siding/">Siding</a><a href="/multi-family-roofing/">Multi-Family Roofing</a><a href="/insurance-claims/">Insurance Claims</a><a href="/financing/">Financing</a></div></div>
<div><div class="footer-col-title">Company</div><div class="footer-links"><a href="/about/">About Us</a><a href="/past-jobs/">Past Jobs</a><a href="/faq/">FAQ</a><a href="/blog/">Blog</a><a href="/warranty/">Warranty</a><a href="/contact/">Contact</a></div></div>
<div><div class="footer-col-title">Service Areas</div><div class="footer-links"><a href="/cleveland-ohio/">Cleveland</a><a href="/beachwood-ohio/">Beachwood</a><a href="/roofing-shaker-heights/">Shaker Heights</a><a href="/roofing-solon-ohio/">Solon</a><a href="/lyndhurst-ohio/">Lyndhurst</a><a href="/roofing-south-euclid-oh/">South Euclid</a><a href="/parma-ohio/">Parma</a><a href="/contact/">+ More Areas</a></div></div>
</div>
<div class="footer-bottom"><p>© 2026 Atlas Roofing &amp; Restoration. All rights reserved. | <a href="/privacy-policy/" style="color:rgba(255,255,255,0.25);">Privacy Policy</a></p><div class="footer-badges"><span class="fbadge">BBB A+</span><span class="fbadge">GAF Certified</span><span class="fbadge">Licensed &amp; Insured</span></div></div>
</div></footer>
<div class="mob-bar"><a href="tel:2168883208" class="mob-call">☎ Call Now</a><a href="/contact/" class="mob-insp">Free Inspection</a></div>
<script>function toggleFaq(el){var item=el.parentElement;var isOpen=item.classList.contains('open');document.querySelectorAll('.faq-item.open').forEach(function(i){i.classList.remove('open');});if(!isOpen)item.classList.add('open');}</script>"""

def trustbar_html():
    return """<div class="trustbar"><div class="wrap">
<div class="trust-item"><span class="trust-icon blue">🛡</span> Licensed, Bonded &amp; Insured</div>
<div class="trust-item"><span class="trust-icon green">★</span> BBB A+ Accredited</div>
<div class="trust-item"><span class="trust-icon blue">✓</span> 2026 GAF Certified™ Residential Roofing Contractor</div>
<div class="trust-item"><span class="trust-icon green">💳</span> Flexible Financing</div>
<div class="trust-item"><span class="trust-icon blue">📅</span> Most Roofs Done in 1 Day</div>
</div></div>"""

def review_html(c):
    r = c["review"]
    return f"""<div class="review-box">
<div class="review-stars">★★★★★</div>
<p class="review-text">"{r['text']}"</p>
<div class="review-author">{r['author']}</div>
<div class="review-source">{r['source']}</div>
</div>"""

def nearby_cities_html(c):
    neighbors = c.get("neighbors", [])[:5]
    links = []
    for n in neighbors:
        slug_guess = n.lower().replace(" ", "-").replace("'","").replace(".","")
        links.append(f'<a href="/contact/" style="background:#fff;border:2px solid var(--border);border-radius:100px;padding:7px 18px;font-size:13px;font-weight:500;color:var(--dark);">{n}</a>')
    return "\n".join(links)

# ── Page type definitions ─────────────────────────────────────────────────────

def page_roof_repair(c):
    name, slug, county, era, streets = c["name"], c["slug"], c["county"], c["housing_era"], c["streets"]
    st1, st2 = streets[0], streets[1] if len(streets) > 1 else streets[0]
    slug_out = f"roof-repair-{slug}-oh"
    title = f"Roof Repair {name} Ohio | Atlas Roofing & Restoration"
    desc = f"Fast, professional roof repair in {name}, Ohio. Leaks, storm damage, missing shingles — Atlas Roofing responds quickly. GAF certified, BBB A+. Free inspections. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Roof Repair in"
    h1_line2 = f"{name}, Ohio"
    badge_text = f"Roof Repair — {name}, {c['state']}"
    hero_p = f"Roof leaking? Missing shingles after a storm? Atlas Roofing & Restoration provides fast, reliable roof repair throughout {name} and {county}. We serve homes along {st1}, {st2}, and all surrounding neighborhoods. Whether it's a minor patch or extensive storm damage, we give you an honest assessment and get it fixed right — the same day when possible. GAF certified. BBB A+ rated. Free inspection, no pressure."
    cta_btn = f"Get Free Roof Inspection in {name}"
    checklist_items = [
        f"<strong>Emergency response</strong> — fast same-day or next-day service in {name}",
        f"<strong>Leak diagnosis</strong> — we find the source, not just patch the symptom",
        "<strong>Storm damage specialists</strong> — hail, wind, ice damage repairs",
        "<strong>GAF certified materials</strong> — manufacturer-backed repair quality",
        "<strong>Honest assessments</strong> — we tell you repair vs. replace upfront",
        "<strong>Free inspections</strong> — no cost, no commitment, no pressure",
    ]
    info_box_title = f"Is your {name} roof leaking?"
    info_box_body = f"Don't wait. Water intrusion causes exponentially more damage over time — insulation, drywall, framing. Most {name} homeowners are surprised at how affordable a quality repair is when caught early. We inspect for free and give you a clear, honest quote."
    faq_items = [
        (f"How quickly can you respond to a roof repair in {name}?",
         f"For urgent leaks in {name} and the surrounding {county} area, we aim for same-day or next-day response. Call (216) 888-3208 and let us know it's urgent."),
        ("How do I know if I need repair or full replacement?",
         f"We'll tell you honestly after a free inspection. Many {name} homeowners discover their roof has years of life left and only needs targeted repairs. We never recommend replacement unless it's truly needed."),
        ("Does homeowner's insurance cover roof repairs in Ohio?",
         f"Storm-related damage — hail, wind, fallen branches — is generally covered. We help {name} homeowners navigate the insurance claim process at no extra cost."),
        (f"What's the average cost of roof repair in {name}?",
         "Minor repairs typically range from a few hundred dollars. We give you a written quote before any work starts."),
    ]
    section2_h = f"Common Roof Repair Issues in {name}"
    section2_body = f"Homes in {name} were largely built during the {era} era, which means many roofs are at or past their expected lifespan. Common issues we see include: worn or cracked flashing around chimneys and skylights, granule loss on aging shingles, wind-lifted or missing shingles after Lake Erie storms, ice dam damage along eaves and valleys, and slow leaks around pipe boots and vents. Whatever the issue, we diagnose it accurately and fix it to last."
    final_h = f"Fast Roof Repair in {name}, Ohio."
    final_p = f"We serve {name} and all of {county}. Free inspection, honest quote, quality work."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p, c

def page_roof_replacement(c):
    name, slug, county, era, streets = c["name"], c["slug"], c["county"], c["housing_era"], c["streets"]
    st1, st2 = streets[0], streets[1] if len(streets) > 1 else streets[0]
    slug_out = f"roof-replacement-{slug}-oh"
    title = f"Roof Replacement {name} Ohio | Atlas Roofing & Restoration"
    desc = f"Full roof replacement in {name}, Ohio. GAF certified contractor, BBB A+ rated. GAF System Plus Limited Warranty. Free inspections. Most roofs done in 1 day. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Roof Replacement in"
    h1_line2 = f"{name}, Ohio"
    badge_text = f"Roof Replacement — {name}, {c['state']}"
    hero_p = f"Ready to replace your roof in {name}? Atlas Roofing & Restoration is {county}'s trusted choice for full residential roof replacements. We serve homeowners along {st1}, {st2}, and throughout {name} — delivering quality workmanship, GAF certified materials, and a warranty you can count on. Most replacements are completed in a single day. Free inspection, upfront pricing, zero pressure."
    cta_btn = f"Get Free Roof Estimate in {name}"
    checklist_items = [
        f"<strong>One-day installation</strong> — most {name} roofs replaced start to finish in a day",
        "<strong>GAF System Plus Limited Warranty</strong> — one of the best warranties available",
        f"<strong>Local expertise</strong> — we know {name} homes, styles, and HOA requirements",
        "<strong>Full tear-off & cleanup</strong> — we haul everything away, leave zero mess",
        "<strong>Upfront written quotes</strong> — no surprises, no hidden fees",
        "<strong>BBB A+ accredited</strong> — independently verified trustworthiness",
    ]
    info_box_title = f"Homes in {name} built in the {era} era"
    info_box_body = f"Many {name} homes from the {era} period are now on their second or third roof cycle. If your home was built during this era and hasn't had a replacement in 20+ years, a free inspection will tell you exactly where you stand. No obligation."
    faq_items = [
        (f"How long does a roof replacement take in {name}?",
         f"Most residential roofs in {name} are completed in a single day. Larger or more complex rooflines may take two days. We'll give you a clear timeline upfront."),
        ("What warranty comes with a new roof from Atlas?",
         "We offer the GAF System Plus Limited Warranty — a manufacturer-backed warranty on both materials and workmanship. Ask us for full details during your free inspection."),
        ("Do you handle the permit process?",
         f"Yes. We handle all required permits for {name} and {county}. You don't need to worry about the paperwork."),
        ("Can I finance my roof replacement?",
         "Yes — we offer flexible financing options. Many homeowners in {name} are surprised at how manageable monthly payments are. Ask us during your free inspection."),
    ]
    section2_h = f"The Atlas Roof Replacement Process in {name}"
    section2_body = f"We start with a free, no-pressure inspection of your {name} home. If replacement is the right call, we walk you through shingle options, colors, and warranty tiers — no upselling, just honest recommendations for your home and budget. On installation day, our crew handles complete tear-off, deck inspection and repair if needed, ice and water shield installation, full shingle installation with GAF certified materials, and complete cleanup. We typically finish before dinner."
    final_h = f"New Roof in {name}, Ohio — Done Right."
    final_p = f"GAF certified, BBB A+, and backed by a real warranty. Serving {name} and all of {county}."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p, c

def page_roofing_contractor(c):
    name, slug, county, era, streets = c["name"], c["slug"], c["county"], c["housing_era"], c["streets"]
    st1 = streets[0]
    slug_out = f"roofing-contractor-{slug}-oh"
    title = f"Roofing Contractor {name} Ohio | Atlas Roofing & Restoration"
    desc = f"Top-rated roofing contractor in {name}, Ohio. GAF certified, BBB A+ accredited. Residential & commercial. Free inspections. Atlas Roofing & Restoration. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Roofing Contractor in"
    h1_line2 = f"{name}, Ohio"
    badge_text = f"GAF Certified Contractor — {name}, {c['state']}"
    hero_p = f"Looking for a roofing contractor in {name}? Atlas Roofing & Restoration is {county}'s GAF certified, BBB A+ accredited roofing contractor serving homeowners throughout {name} and the surrounding area. We handle residential roof replacements, repairs, gutters, siding, and insurance claims — all with the same commitment to honest work and quality results. Free inspection, written quotes, no pressure."
    cta_btn = f"Get Free Inspection — {name}"
    checklist_items = [
        "<strong>2026 GAF Certified™</strong> — officially certified residential roofing contractor",
        "<strong>BBB A+ Accredited</strong> — independently verified through the Better Business Bureau",
        "<strong>Licensed, bonded & insured</strong> — full coverage, zero risk to you",
        f"<strong>Locally operated</strong> — based in Beachwood, serving {name} daily",
        "<strong>Insurance claim experts</strong> — we handle hail, wind, and storm claims",
        "<strong>No-pressure free inspections</strong> — honest assessment, always",
    ]
    info_box_title = "What sets Atlas apart from other contractors?"
    info_box_body = f"In {name} and across {county}, homeowners tell us the same thing: other contractors either oversold them, didn't show up on time, or left a mess. Atlas runs every job the way we'd want our own home done — honest assessment, quality materials, professional crew, complete cleanup."
    faq_items = [
        ("Is Atlas Roofing licensed and insured in Ohio?",
         "Yes. We are fully licensed, bonded, and insured to operate throughout Ohio, including {name} and {county}."),
        ("What certifications does Atlas hold?",
         "We are a 2026 GAF Certified™ Residential Roofing Contractor (GAF ID: 1148301) and hold a BBB A+ Accreditation."),
        (f"Do you offer free estimates in {name}?",
         f"Yes — all inspections and estimates in {name} and the surrounding area are completely free and come with no obligation."),
        ("Do you handle insurance claims?",
         f"Absolutely. We work directly with insurance adjusters on behalf of {name} homeowners for hail, wind, and storm damage claims."),
    ]
    section2_h = f"Full-Service Roofing in {name}"
    section2_body = f"Atlas Roofing & Restoration provides complete exterior services to {name} homeowners — residential roof replacement and repair, commercial roofing, gutter installation and repair, siding installation, and insurance claim management. Whether you need a quick repair on {st1} or a full roof replacement for a larger {name} property, our crew handles it with the same level of care and professionalism."
    final_h = f"Your {name} Roofing Contractor — Certified & Trusted."
    final_p = "GAF certified. BBB A+. Free inspection. Honest work."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p, c

def page_roof_leak(c):
    name, slug, county, era, streets = c["name"], c["slug"], c["county"], c["housing_era"], c["streets"]
    st1 = streets[0]
    slug_out = f"roof-leak-{slug}-oh"
    title = f"Roof Leak {name} Ohio | Emergency Roof Leak Repair — Atlas Roofing"
    desc = f"Roof leaking in {name}, Ohio? Atlas Roofing responds fast. Emergency leak repair, honest assessment, free inspection. GAF certified, BBB A+. Call now: (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Roof Leak Repair in"
    h1_line2 = f"{name}, Ohio"
    badge_text = f"Emergency Roof Leak — {name}, {c['state']}"
    hero_p = f"Roof leaking in {name}? Call Atlas Roofing & Restoration now at (216) 888-3208. We respond fast to roof leaks throughout {name} and {county}, diagnosing the source accurately and repairing it right — not just covering it up. Water damage compounds quickly. Don't wait. Free inspection, honest quote, same-day response available."
    cta_btn = f"Call Now — Roof Leak in {name}"
    checklist_items = [
        "<strong>Fast response</strong> — same-day and next-day service available",
        "<strong>Accurate leak diagnosis</strong> — we find the actual source, not just symptoms",
        "<strong>Temporary protection</strong> — tarping available for severe cases",
        "<strong>Insurance coordination</strong> — storm-related leaks may be covered",
        "<strong>Repair or replace</strong> — honest recommendation after inspection",
        "<strong>Free inspection</strong> — no charge to assess your leak",
    ]
    info_box_title = "A roof leak costs more the longer you wait"
    info_box_body = f"In {name}, a small roof leak can saturate insulation, rot decking, and cause mold within days of a heavy rain. The repair cost today is a fraction of what it becomes in a month. Call us at (216) 888-3208 — we'll get there fast."
    faq_items = [
        (f"How quickly can you respond to a roof leak in {name}?",
         f"We prioritize active leaks. Call (216) 888-3208 and tell us you have an active leak in {name} — we'll work to get someone out same-day or next-day."),
        ("What causes most roof leaks in Ohio homes?",
         f"The most common causes we see in {name} area homes: failed flashing around chimneys and skylights, worn pipe boots, cracked or missing shingles after storms, and ice dam damage along eaves during winter."),
        ("Will my homeowner's insurance cover a roof leak?",
         "If the leak was caused by a covered event — storm, hail, wind, or ice — your insurance likely covers the repair. We help you file the claim."),
        ("Can a leaking roof be temporarily patched until I can afford replacement?",
         "In many cases, yes. We can make a quality repair to stop the leak and buy you time. We'll be honest if we believe replacement is the better long-term decision."),
    ]
    section2_h = f"Where Roof Leaks Commonly Occur in {name} Homes"
    section2_body = f"Most {name} homes were built in the {era} era, and we consistently see leaks in the same spots: around chimney flashing that has lifted or cracked over decades of freeze-thaw cycles, at pipe boots and vents that weren't resealed during prior roof work, in valleys where water concentrates, and along the eave edges where ice dams form every winter. A free inspection will tell you exactly what's happening on your roof."
    final_h = f"Roof Leaking in {name}? We're On It."
    final_p = "Call now for fast response. Free inspection. No obligation."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p, c

def page_roof_inspection(c):
    name, slug, county, era, streets = c["name"], c["slug"], c["county"], c["housing_era"], c["streets"]
    slug_out = f"roof-inspection-{slug}-oh"
    title = f"Free Roof Inspection {name} Ohio | Atlas Roofing & Restoration"
    desc = f"Free roof inspection in {name}, Ohio. No obligation, honest assessment. GAF certified, BBB A+ rated. Atlas Roofing & Restoration. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Free Roof Inspection in"
    h1_line2 = f"{name}, Ohio"
    badge_text = f"Free Inspection — {name}, {c['state']}"
    hero_p = f"Not sure about the condition of your {name} roof? Atlas Roofing & Restoration offers free, no-obligation roof inspections throughout {name} and {county}. Our certified inspector will assess your roof honestly — giving you a clear picture of what's there, what might need attention, and what can wait. No sales pressure, no inflated findings. Just straight answers."
    cta_btn = f"Schedule Free Inspection in {name}"
    checklist_items = [
        "<strong>Completely free</strong> — no charge, ever, for the inspection",
        "<strong>No obligation</strong> — get the report and decide on your own timeline",
        "<strong>Certified inspector</strong> — GAF certified eyes on your roof",
        "<strong>Photo documentation</strong> — we show you exactly what we found",
        "<strong>Written report</strong> — clear summary of findings and recommendations",
        "<strong>Insurance pre-check</strong> — we identify potential storm damage before you file",
    ]
    info_box_title = f"When should {name} homeowners get a roof inspection?"
    info_box_body = f"We recommend an inspection if: your home was built in the {era} era and hasn't had recent roofwork, you've had a hail or wind storm in {name} within the past year, you're preparing to sell or buy a home, or you notice curling, missing, or granule-shedding shingles. A free inspection gives you the facts."
    faq_items = [
        (f"Is the roof inspection really free in {name}?",
         f"Yes — completely free, with no obligation. We inspect your {name} roof, give you a written summary of findings, and leave the decision entirely up to you."),
        ("How long does the inspection take?",
         "Most residential inspections take 30–45 minutes. We'll walk you through what we found when we come down."),
        ("Will you try to sell me a new roof?",
         "Only if you actually need one. Many of our inspections result in 'your roof is in good shape — come back to us in a few years.' We'd rather earn your trust than push an unnecessary sale."),
        ("Do you document the inspection with photos?",
         "Yes. We photograph the areas of concern so you can see exactly what we found, not just take our word for it."),
    ]
    section2_h = f"What We Check During a {name} Roof Inspection"
    section2_body = f"Our certified inspectors thoroughly evaluate: shingle condition, granule loss, and age indicators; flashing at chimneys, skylights, vents, and valleys; soffit and fascia condition; gutter attachment and slope; attic ventilation adequacy; and any visible signs of prior water intrusion. For {name} homes built during the {era} era, we pay special attention to areas that commonly fail at that stage of a roof's life."
    final_h = f"Free Roof Inspection in {name} — No Strings Attached."
    final_p = "Honest assessment from a GAF certified inspector. Free, always."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p, c

def page_new_roof_cost(c):
    name, slug, county, era, streets = c["name"], c["slug"], c["county"], c["housing_era"], c["streets"]
    slug_out = f"new-roof-cost-{slug}-oh"
    title = f"New Roof Cost {name} Ohio | Roof Replacement Pricing — Atlas Roofing"
    desc = f"How much does a new roof cost in {name}, Ohio? Get honest pricing from Atlas Roofing. Free estimates, written quotes, no surprises. GAF certified, BBB A+. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "New Roof Cost in"
    h1_line2 = f"{name}, Ohio"
    badge_text = f"Honest Pricing — {name}, {c['state']}"
    hero_p = f"Wondering what a new roof costs in {name}? Atlas Roofing & Restoration provides free, written estimates with no hidden fees and no pressure. Roof costs vary based on size, pitch, shingle selection, and whether decking repairs are needed — but we give {name} homeowners clear, itemized quotes so there are no surprises. GAF certified contractor. BBB A+ rated."
    cta_btn = f"Get Free Estimate in {name}"
    checklist_items = [
        "<strong>Free written estimate</strong> — itemized, no obligations",
        "<strong>No hidden fees</strong> — the number we quote is the number you pay",
        "<strong>Multiple shingle tiers</strong> — from value to premium GAF options",
        "<strong>Financing available</strong> — manageable monthly payment options",
        "<strong>Insurance coordination</strong> — we handle claims if storm damage is involved",
        "<strong>GAF System Plus Limited Warranty</strong> — manufacturer-backed coverage",
    ]
    info_box_title = f"What factors affect roof cost in {name}?"
    info_box_body = f"The main cost drivers are: roof size (square footage), pitch and complexity of the roofline, shingle type and tier selected, condition of the decking underneath, and any required repairs to flashing or ventilation. {name} homes from the {era} era often have decking that needs spot repair. We assess this upfront and include it in your quote."
    faq_items = [
        (f"What does a new roof cost in {name}, Ohio?",
         f"Costs vary by home size and material choice. We give you a free, written, itemized estimate after inspecting your {name} property — no guesses, no ranges, just your actual number."),
        ("Does insurance cover roof replacement?",
         f"If your {name} roof was damaged by hail, wind, or a storm event, your homeowner's insurance may cover partial or full replacement. We help you through the claims process at no extra charge."),
        ("What shingle options do you offer?",
         "We install the full GAF shingle lineup — from dimensional value shingles to premium designer options. We'll show you samples and help you find the right fit for your home and budget."),
        ("Is financing available?",
         f"Yes. We offer financing options for {name} homeowners. Many find that monthly payments are very manageable compared to delaying a needed replacement."),
    ]
    section2_h = f"Honest Roof Pricing for {name} Homeowners"
    section2_body = f"Atlas Roofing gives {name} homeowners full transparency on pricing. Our written estimates include: tear-off and disposal, deck inspection and any identified repairs, ice and water shield installation, full shingle installation with GAF certified materials, new flashing at all penetrations and valleys, ridge cap installation, and complete cleanup and haul-away. No surprises at the end of the job."
    final_h = f"Get an Honest Roof Estimate in {name}."
    final_p = "Free written quote. No pressure. No hidden fees."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p, c

def page_hail_damage(c):
    name, slug, county, era, streets = c["name"], c["slug"], c["county"], c["housing_era"], c["streets"]
    slug_out = f"hail-damage-roof-{slug}-oh"
    title = f"Hail Damage Roof Repair {name} Ohio | Insurance Claims — Atlas Roofing"
    desc = f"Hail damage to your roof in {name}, Ohio? Atlas Roofing handles the inspection and insurance claim. GAF certified, BBB A+. Free inspection. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Hail Damage Roof Repair in"
    h1_line2 = f"{name}, Ohio"
    badge_text = f"Hail & Storm Damage — {name}, {c['state']}"
    hero_p = f"Hail storm hit {name}? Atlas Roofing & Restoration specializes in storm damage inspection and insurance claim support for {county} homeowners. We'll inspect your roof for free, document every hail impact and wind-related damage with photos, and work directly with your insurance adjuster to ensure you receive a fair settlement. Many {name} homeowners pay only their deductible. GAF certified. BBB A+."
    cta_btn = f"Free Hail Damage Inspection — {name}"
    checklist_items = [
        "<strong>Free storm damage inspection</strong> — thorough, photo-documented",
        "<strong>Insurance claim management</strong> — we work with your adjuster directly",
        "<strong>Most pay only deductible</strong> — insurance covers the rest",
        "<strong>GAF certified replacement</strong> — quality materials backed by warranty",
        "<strong>Fast turnaround</strong> — most insurance jobs completed within 2 weeks of approval",
        "<strong>No out-of-pocket surprises</strong> — we review your coverage upfront",
    ]
    info_box_title = f"Did a storm hit {name} recently?"
    info_box_body = f"Northeast Ohio storms frequently cause roof damage that isn't visible from the ground. Hail damage often appears subtle — small dents on shingles, damaged flashing, or granule loss — but it compromises your roof's lifespan significantly. A free inspection after any storm is always worthwhile."
    faq_items = [
        (f"How do I know if my {name} roof has hail damage?",
         f"Hail damage is often subtle and not visible from the ground. Signs include dented gutters and downspouts, granule loss in gutters, damaged window screens, and bruised or cracked shingles. Our free inspection documents everything with photos."),
        ("How does the insurance claim process work?",
         f"After our free inspection, if damage is found we'll help you file the claim, meet with your adjuster at your {name} property, and advocate for a fair settlement. Atlas manages the entire process."),
        ("How long do I have to file a hail damage claim in Ohio?",
         "Most Ohio homeowner's insurance policies allow 1–2 years from the storm date. Don't wait — evidence of damage can degrade over time. Get inspected now."),
        ("What if my insurance denies the claim?",
         "We can help you appeal and provide additional documentation. Our track record on successful claims in the Cleveland area is strong."),
    ]
    section2_h = f"Storm History and {name} Roofs"
    section2_body = f"Northeast Ohio — including {name} and {county} — is in an active hail corridor. Storms tracking from the Great Plains frequently produce golf ball to baseball sized hail as they cross the Great Lakes region. Homes in {name} built during the {era} era have often accumulated multiple storm events with undetected damage. Even if you didn't see the storm, your roof may have taken impacts. Our free inspection catches what you can't see from the yard."
    final_h = f"Hail Damage in {name}? Get Your Free Inspection."
    final_p = "Insurance claim experts. Free inspection. Most homeowners pay only their deductible."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p, c

def page_gutter(c):
    name, slug, county, era, streets = c["name"], c["slug"], c["county"], c["housing_era"], c["streets"]
    slug_out = f"gutter-installation-{slug}-oh"
    title = f"Gutter Installation {name} Ohio | Atlas Roofing & Restoration"
    desc = f"Professional gutter installation and replacement in {name}, Ohio. Seamless gutters, proper drainage, quality materials. GAF certified, BBB A+. Free inspections. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Gutter Installation in"
    h1_line2 = f"{name}, Ohio"
    badge_text = f"Gutters & Drainage — {name}, {c['state']}"
    hero_p = f"Protect your {name} home from water damage with properly installed gutters from Atlas Roofing & Restoration. We install seamless aluminum gutters throughout {name} and {county}, ensuring proper slope, downspout placement, and drainage away from your foundation. Whether you need new gutters, full replacement, or repairs, we get it done right. Free inspection, honest pricing."
    cta_btn = f"Free Gutter Inspection in {name}"
    checklist_items = [
        "<strong>Seamless aluminum gutters</strong> — custom fabricated on-site to exact fit",
        "<strong>Proper slope & pitch</strong> — engineered to drain correctly, every time",
        "<strong>Downspout placement</strong> — routed to protect your foundation",
        "<strong>Fascia board assessment</strong> — we check and repair rotted fascia before install",
        f"<strong>Local expertise</strong> — we know {name} homes and common drainage challenges",
        "<strong>Free inspection</strong> — honest assessment of your current system",
    ]
    info_box_title = f"Are your {name} gutters protecting your home?"
    info_box_body = f"Failed or missing gutters allow water to saturate soil directly against your foundation, causing settling, basement leaks, and landscaping erosion. In {name}'s climate, where heavy spring rains and snowmelt are common, a properly functioning gutter system is essential. We inspect for free."
    faq_items = [
        ("What type of gutters do you install?",
         f"We primarily install seamless aluminum gutters, which are custom-formed on-site to the exact length of your {name} home's roofline — no seams means no leaks."),
        ("How long does gutter installation take?",
         "Most residential gutter installations in {name} are completed in a single day."),
        ("Do you replace fascia boards?",
         f"Yes. Rotted fascia is common on {name} homes, especially those from the {era} era. We assess and replace damaged fascia as part of the gutter installation."),
        ("Do you install gutter guards?",
         "Yes — we offer gutter guard options to reduce clogging, especially for {name} homes with heavy tree coverage."),
    ]
    section2_h = f"Why {name} Homes Need Quality Gutters"
    section2_body = f"Northeast Ohio receives significant rainfall and snowmelt each year, and homes in {name} are no exception. Without properly functioning gutters, water cascades off the roofline directly against your foundation, erodes landscaping, and can cause basement moisture intrusion. Older homes in {name} from the {era} era often have original gutters that have sagged, separated at seams, or are simply too small for modern rainfall events. A free inspection tells you exactly what your home needs."
    final_h = f"Quality Gutter Installation in {name}, Ohio."
    final_p = "Seamless gutters, proper drainage, lasting protection for your home."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p, c

def page_siding(c):
    name, slug, county, era, streets = c["name"], c["slug"], c["county"], c["housing_era"], c["streets"]
    slug_out = f"siding-contractor-{slug}-oh"
    title = f"Siding Contractor {name} Ohio | Atlas Roofing & Restoration"
    desc = f"Professional siding installation and replacement in {name}, Ohio. Vinyl, fiber cement & more. GAF certified, BBB A+. Free inspections. Atlas Roofing & Restoration. (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Siding Contractor in"
    h1_line2 = f"{name}, Ohio"
    badge_text = f"Siding Installation — {name}, {c['state']}"
    hero_p = f"Looking for a trusted siding contractor in {name}? Atlas Roofing & Restoration installs and replaces siding throughout {name} and {county}. New siding dramatically improves curb appeal, insulation, and protection from Ohio's harsh winters. We work with vinyl, fiber cement, and other quality siding products — with the same commitment to honest work and quality results that defines every Atlas project."
    cta_btn = f"Free Siding Inspection in {name}"
    checklist_items = [
        "<strong>Vinyl & fiber cement options</strong> — multiple styles and colors available",
        "<strong>Full tear-off & disposal</strong> — old siding removed and hauled away",
        "<strong>Weather barrier installation</strong> — proper house wrap for Ohio winters",
        "<strong>Trim and corner detail</strong> — clean, professional finish",
        f"<strong>Local expertise</strong> — familiar with {name} home styles and HOA guidelines",
        "<strong>Free written estimate</strong> — no surprises, no hidden costs",
    ]
    info_box_title = f"New siding is one of the best ROI projects for {name} homeowners"
    info_box_body = f"New siding consistently ranks among the highest return-on-investment exterior improvements. In {name}'s active real estate market, fresh siding can significantly boost curb appeal and resale value — while also reducing heating and cooling costs year-round."
    faq_items = [
        ("What siding materials do you install?",
         f"We install vinyl siding, fiber cement siding (including James Hardie products), and other quality exterior cladding products suitable for {name}'s climate."),
        ("How long does siding installation take?",
         "Most residential siding projects in {name} are completed in 2–4 days depending on the size of the home and materials selected."),
        ("Does new siding improve energy efficiency?",
         f"Yes. New siding with proper house wrap installation reduces air infiltration significantly, which can noticeably lower heating bills for {name} homes through Ohio winters."),
        ("Does homeowner's insurance cover siding damage?",
         "Storm-related siding damage — hail, wind, falling trees — is generally covered. We help {name} homeowners navigate the claim process."),
    ]
    section2_h = f"Siding Services for {name} Homes"
    section2_body = f"Atlas Roofing & Restoration handles the complete siding job for your {name} home — from removal of your existing siding to installation of the new material with proper weather barrier, trim work, and cleanup. Homes in {name} from the {era} era often have original or first-replacement siding that has cracked, warped, faded, or is no longer effectively sealing out moisture. New siding solves all of these issues while giving your home a dramatically refreshed appearance."
    final_h = f"New Siding in {name}, Ohio — Done Right."
    final_p = "Professional installation, quality materials, free written estimate."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p, c

# ── All 9 page type functions ─────────────────────────────────────────────────
PAGE_TYPES = [
    page_roof_repair,
    page_roof_replacement,
    page_roofing_contractor,
    page_roof_leak,
    page_roof_inspection,
    page_new_roof_cost,
    page_hail_damage,
    page_gutter,
    page_siding,
]

# ── HTML builder ──────────────────────────────────────────────────────────────
def build_html(slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text,
               hero_p, cta_btn, checklist_items, info_box_title, info_box_body,
               faq_items, section2_h, section2_body, final_h, final_p, c):

    checklist_html = "\n".join([f'<li><span>{item}</span></li>' for item in checklist_items])
    faq_html = "\n".join([
        f'''<div class="faq-item">
<div class="faq-q" onclick="toggleFaq(this)">{q}<span class="faq-toggle">+</span></div>
<div class="faq-a">{a}</div>
</div>''' for q, a in faq_items
    ])
    nearby_html = nearby_cities_html(c)
    name = c["name"]

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
{SHARED_CSS}
</style>
</head>
<body>
{nav_html()}
<div class="breadcrumb"><div class="wrap"><a href="/">Home</a> <span>›</span> <a href="/service-areas/">Service Areas</a> <span>›</span> <span>{h1_line1} {name}</span></div></div>

<section class="hero"><div class="wrap"><div class="hero-inner">
<div class="hero-badge"><span class="hero-badge-dot"></span> {badge_text}</div>
<h1 class="hero-h1">{h1_line1}<br><span class="green">{h1_line2}</span></h1>
<p class="hero-p">{hero_p}</p>
<div class="hero-btns"><a href="/contact/" class="btn btn-green">{cta_btn}</a><a href="tel:2168883208" class="btn btn-outline-white">Call (216) 888-3208</a></div>
</div></div></section>

{trustbar_html()}

<section class="section"><div class="wrap">
<div class="two-col">
<div>
<span class="section-label">Why Atlas</span>
<h2 class="section-h" style="margin-bottom:20px;">Why {name} Homeowners Choose Atlas</h2>
<ul class="checklist">
{checklist_html}
</ul>
<br>
<div style="background:var(--green-lt);border:1px solid rgba(101,196,123,0.4);border-radius:var(--r-lg);padding:20px 22px;margin-top:24px;">
<h4 style="font-size:16px;font-weight:700;color:var(--dark);margin-bottom:8px;">{info_box_title}</h4>
<p style="font-size:13px;color:#2d6e42;line-height:1.6;">{info_box_body}</p>
</div>
</div>
<div>
{review_html(c)}
<br>
<div style="background:var(--gray-lt);border-radius:var(--r-lg);padding:28px;margin-top:0;">
<h4 style="font-size:17px;font-weight:700;color:var(--dark);margin-bottom:14px;">Ready to get started?</h4>
<p style="font-size:14px;color:var(--gray);margin-bottom:18px;line-height:1.6;">Free inspection, honest assessment, written quote. No pressure — ever. We'll call within 2 business hours.</p>
<a href="/contact/" class="btn btn-blue" style="width:100%;text-align:center;display:block;">Schedule Free Inspection</a>
<br>
<a href="tel:2168883208" class="btn btn-outline-blue" style="width:100%;text-align:center;display:block;">Call (216) 888-3208</a>
</div>
</div>
</div>
</div></section>

<section class="section gray"><div class="wrap">
<div class="section-header">
<span class="section-label">{name}, Ohio</span>
<h2 class="section-h">{section2_h}</h2>
</div>
<p style="font-size:16px;color:var(--gray);line-height:1.8;max-width:820px;">{section2_body}</p>
</div></section>

<section class="section"><div class="wrap">
<div class="section-header center">
<span class="section-label">Common Questions</span>
<h2 class="section-h">Frequently Asked Questions</h2>
</div>
<div class="faq-list" style="max-width:760px;margin:0 auto;">
{faq_html}
</div>
<div class="cta-box">
<h3>Ready for a Free Inspection in {name}?</h3>
<p>No commitment. No pressure. Just an honest assessment from a trusted local contractor.</p>
<div class="cta-box-btns"><a href="/contact/" class="btn btn-white">Request Free Inspection</a><a href="tel:2168883208" class="btn btn-outline-white">Call (216) 888-3208</a></div>
</div>
</div></section>

<section class="section gray"><div class="wrap">
<div class="section-header center"><span class="section-label">Also serving nearby</span><h2 class="section-h">We Serve All of Northeast Ohio</h2><p class="section-sub">In addition to {name}, we serve homeowners throughout the greater Cleveland area.</p></div>
<div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:8px;">
{nearby_html}
<a href="/service-areas/" style="background:#fff;border:2px solid var(--border);border-radius:100px;padding:7px 18px;font-size:13px;font-weight:500;color:var(--dark);">View All Areas →</a>
</div>
</div></section>

<section class="final-cta"><div class="wrap"><h2>{final_h}</h2><p>{final_p}</p><div class="final-btns"><a href="/contact/" class="btn btn-white">Get Free Inspection</a><a href="tel:2168883208" class="btn btn-outline-white">Call (216) 888-3208</a></div></div></section>
{footer_html()}
</body></html>"""

# ── Generator ─────────────────────────────────────────────────────────────────
def generate_all(cities=None, page_types=None, dry_run=False):
    if cities is None:
        cities = CITIES
    if page_types is None:
        page_types = PAGE_TYPES

    generated = []
    skipped = []

    for c in cities:
        for page_fn in page_types:
            result = page_fn(c)
            slug_out = result[0]
            out_dir = os.path.join(SITE_DIR, slug_out)
            out_file = os.path.join(out_dir, "index.html")

            if os.path.exists(out_file):
                skipped.append(slug_out)
                continue

            if not dry_run:
                os.makedirs(out_dir, exist_ok=True)
                html = build_html(*result)
                with open(out_file, "w", encoding="utf-8") as f:
                    f.write(html)

            generated.append(slug_out)

    return generated, skipped

def update_sitemap(new_slugs):
    sitemap_path = os.path.join(SITE_DIR, "sitemap.xml")
    with open(sitemap_path, "r") as f:
        content = f.read()

    new_entries = ""
    for slug in new_slugs:
        url = f"https://atlasroofingrestoration.com/{slug}/"
        if url not in content:
            new_entries += f"""  <url>
    <loc>{url}</loc>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>\n"""

    if new_entries:
        content = content.replace("</urlset>", new_entries + "</urlset>")
        with open(sitemap_path, "w") as f:
            f.write(content)
        return len(new_slugs)
    return 0

def write_tracker(all_slugs_existing, new_slugs):
    tracker_path = os.path.join(SITE_DIR, "PAGE_TRACKER.md")
    from datetime import date

    # Read existing tracker
    existing_entries = []
    if os.path.exists(tracker_path):
        with open(tracker_path, "r") as f:
            existing_entries = f.read()
    else:
        existing_entries = ""

    # Count totals
    total = len(all_slugs_existing) + len(new_slugs)

    new_lines = ""
    today = date.today().isoformat()
    for slug in new_slugs:
        page_type = slug.split("-")[0] + "-" + slug.split("-")[1] if "-" in slug else slug
        new_lines += f"| /{slug}/ | {today} |\n"

    if "## Generated Pages" not in existing_entries:
        header = f"""# Atlas Roofing — SEO Page Tracker
Last updated: {today}
Total hyper-local pages: {total}

## Generated Pages
| URL | Date Added |
|-----|------------|
"""
        content = header + new_lines
    else:
        content = existing_entries.replace(
            "## Generated Pages\n| URL | Date Added |\n|-----|------------|\n",
            f"## Generated Pages\n| URL | Date Added |\n|-----|------------|\n" + new_lines
        )
        # Update total count
        content = re.sub(r"Total hyper-local pages: \d+", f"Total hyper-local pages: {total}", content)
        content = re.sub(r"Last updated: [\d-]+", f"Last updated: {today}", content)

    with open(tracker_path, "w") as f:
        f.write(content)

if __name__ == "__main__":
    import sys
    dry = "--dry-run" in sys.argv

    print(f"Starting generation {'(DRY RUN)' if dry else ''}...")
    generated, skipped = generate_all(dry_run=dry)

    print(f"\nGenerated: {len(generated)} pages")
    print(f"Skipped (already exist): {len(skipped)} pages")

    if generated and not dry:
        added = update_sitemap(generated)
        print(f"Sitemap updated: {added} new URLs added")
        write_tracker(skipped, generated)
        print("PAGE_TRACKER.md updated")

    if dry:
        print("\nSample slugs that would be created:")
        for s in generated[:15]:
            print(f"  /{s}/")
        print(f"  ... and {len(generated)-15} more")
