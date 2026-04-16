#!/usr/bin/env python3
"""
Atlas Roofing & Restoration — Commercial & Multi-Family Page Generator
Generates commercial/multi-family phrase types for:
  - All 57 existing residential cities (commercial phrases added)
  - 15 new wider commercial cities
"""

import os, re
from city_data import CITIES, COMMERCIAL_CITIES, ALL_COMMERCIAL_CITIES

SITE_DIR = "/home/claude/site"

# ── Review pool ───────────────────────────────────────────────────────────────
REVIEW_POOL = [
    {"text": "I asked them to take a look at my roof based on my home inspection report. They were very honest when inspecting and only recommended the exact work that needed to be done, and nothing more.", "author": "Benjamin Kaplan", "source": "Northeast Ohio · Google Review"},
    {"text": "Quick and professional roofing service. Great communication throughout the entire process and left a very clean job site.", "author": "Tawn Kramer", "source": "Northeast Ohio · Google Review"},
    {"text": "What a divine appointment from beginning to completion. Trustworthy, competent, efficient, polite, orderly team work. A big smile comes on my face every time I leave and return to my home and see my beautiful new roof.", "author": "Lorna Joy Larkin", "source": "South Euclid, OH · Google Review"},
    {"text": "I had such a great experience with Atlas Roofing and truly can't recommend them enough. They replaced my entire roof in just one day. Everything was done so efficiently and the quality of the work is excellent.", "author": "Adina Forouzan", "source": "Northeast Ohio · Google Review"},
    {"text": "They literally put a roof over our heads. Great communication. Employees were pleasant and were there when they said they would be there.", "author": "Robert Schloss", "source": "Northeast Ohio · Google Review"},
    {"text": "Andrew is fantastic — called him about a roof leak, he came out the same day, assessed what needed to be done, and had everything sorted out quickly. Highly recommend.", "author": "Jimmy Valencia", "source": "Northeast Ohio · Google Review"},
]
_rc = [0]
def next_review():
    r = REVIEW_POOL[_rc[0] % len(REVIEW_POOL)]
    _rc[0] += 1
    return r

# ── Shared CSS ────────────────────────────────────────────────────────────────
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
.btn-white { background: #fff; color: var(--blue); }
.btn-outline-blue { background: transparent; color: var(--blue); border: 2px solid var(--blue); }
.btn-outline-blue:hover { background: var(--blue); color: #fff; }
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
<div><div class="footer-logo"><img src="../logo-dark.png" alt="Atlas Roofing &amp; Restoration"></div><p class="footer-desc">Cleveland and Northeast Ohio's trusted roofing contractor. GAF certified, BBB A+ rated.</p><div class="footer-contact"><a href="tel:2168883208">☎ (216) 888-3208</a><a href="mailto:office@atlasroofingrestoration.com">✉ office@atlasroofingrestoration.com</a><a href="#">📍 23945 Mercantile Rd, Suite D, Beachwood OH 44122</a></div>
<div style="display:flex;gap:12px;margin-top:14px;">
<a href="https://www.facebook.com/atlasroofingrestoration" target="_blank" rel="noopener" style="width:34px;height:34px;border-radius:8px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.12);display:flex;align-items:center;justify-content:center;font-size:16px;color:rgba(255,255,255,0.6);" title="Facebook">f</a>
<a href="https://www.instagram.com/atlasroofingrestoration" target="_blank" rel="noopener" style="width:34px;height:34px;border-radius:8px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.12);display:flex;align-items:center;justify-content:center;font-size:14px;color:rgba(255,255,255,0.6);" title="Instagram">📷</a>
<a href="https://www.google.com/maps/place/Atlas+Roofing+%26+Restoration/@41.4608547,-81.5060061,707m" target="_blank" rel="noopener" style="width:34px;height:34px;border-radius:8px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.12);display:flex;align-items:center;justify-content:center;font-size:14px;color:rgba(255,255,255,0.6);" title="Google Reviews">⭐</a>
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
<div class="trust-item"><span class="trust-icon blue">✓</span> 2026 GAF Certified™ Contractor</div>
<div class="trust-item"><span class="trust-icon green">🏢</span> Commercial &amp; Multi-Family</div>
<div class="trust-item"><span class="trust-icon blue">📋</span> Free Inspections &amp; Proposals</div>
</div></div>"""

def build_page(c, slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text,
               hero_p, cta_btn, checklist_items, info_box_title, info_box_body,
               faq_items, section2_h, section2_body, final_h, final_p):
    r = next_review()
    name = c["name"]
    checklist_html = "\n".join([f'<li><span>{item}</span></li>' for item in checklist_items])
    faq_html = "\n".join([f'''<div class="faq-item">
<div class="faq-q" onclick="toggleFaq(this)">{q}<span class="faq-toggle">+</span></div>
<div class="faq-a">{a}</div>
</div>''' for q, a in faq_items])

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
<style>{SHARED_CSS}</style>
</head>
<body>
{nav_html()}
<div class="breadcrumb"><div class="wrap"><a href="/">Home</a> <span>›</span> <a href="/commercial-roofing/">Commercial Roofing</a> <span>›</span> <span>{h1_line1} {name}</span></div></div>
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
<h2 class="section-h" style="margin-bottom:20px;">Why {name} Property Owners Choose Atlas</h2>
<ul class="checklist">{checklist_html}</ul>
<br>
<div style="background:var(--green-lt);border:1px solid rgba(101,196,123,0.4);border-radius:var(--r-lg);padding:20px 22px;margin-top:24px;">
<h4 style="font-size:16px;font-weight:700;color:var(--dark);margin-bottom:8px;">{info_box_title}</h4>
<p style="font-size:13px;color:#2d6e42;line-height:1.6;">{info_box_body}</p>
</div>
</div>
<div>
<div class="review-box">
<div class="review-stars">★★★★★</div>
<p class="review-text">"{r['text']}"</p>
<div class="review-author">{r['author']}</div>
<div class="review-source">{r['source']}</div>
</div>
<br>
<div style="background:var(--gray-lt);border-radius:var(--r-lg);padding:28px;">
<h4 style="font-size:17px;font-weight:700;color:var(--dark);margin-bottom:14px;">Request a Free Commercial Inspection</h4>
<p style="font-size:14px;color:var(--gray);margin-bottom:18px;line-height:1.6;">Free inspection, detailed written proposal, no commitment. We'll respond within 2 business hours.</p>
<a href="/contact/" class="btn btn-blue" style="width:100%;text-align:center;display:block;">Request Free Inspection</a>
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
<div class="faq-list" style="max-width:760px;margin:0 auto;">{faq_html}</div>
<div class="cta-box">
<h3>Free Commercial Roof Inspection in {name}</h3>
<p>Detailed written proposal. No commitment. We serve all of Northeast Ohio.</p>
<div class="cta-box-btns"><a href="/contact/" class="btn btn-white">Request Free Inspection</a><a href="tel:2168883208" class="btn btn-outline-white">Call (216) 888-3208</a></div>
</div>
</div></section>
<section class="final-cta"><div class="wrap"><h2>{final_h}</h2><p>{final_p}</p><div class="final-btns"><a href="/contact/" class="btn btn-white">Free Inspection & Proposal</a><a href="tel:2168883208" class="btn btn-outline-white">Call (216) 888-3208</a></div></div></section>
{footer_html()}
</body></html>"""

# ── PAGE TYPE FUNCTIONS ───────────────────────────────────────────────────────

def page_commercial_roof_repair(c):
    name, slug, county = c["name"], c["slug"], c["county"]
    st1 = c["streets"][0]
    slug_out = f"commercial-roof-repair-{slug}-oh"
    title = f"Commercial Roof Repair {name} Ohio | Atlas Roofing & Restoration"
    desc = f"Commercial roof repair in {name}, Ohio. Leaks, membrane failures, storm damage fixed fast. GAF certified, BBB A+. Free inspection & proposal. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Commercial Roof Repair in"; h1_line2 = f"{name}, Ohio"
    badge_text = f"Commercial Repair — {name}, OH"
    hero_p = f"Commercial roof leaking or damaged in {name}? Atlas Roofing & Restoration responds fast to commercial repair needs throughout {name} and {county}. We service all flat roof systems — TPO, EPDM, modified bitumen, and built-up roofs — with minimal disruption to your business operations. Free inspection and written proposal before any work starts."
    cta_btn = f"Free Commercial Inspection — {name}"
    checklist_items = [
        "<strong>All flat roof systems</strong> — TPO, EPDM, modified bitumen, built-up",
        "<strong>Fast response</strong> — minimize business disruption",
        "<strong>Leak diagnosis</strong> — find the source, not just patch symptoms",
        "<strong>Insurance claim support</strong> — storm damage handled",
        "<strong>Preventive maintenance</strong> — extend roof life significantly",
        "<strong>Free inspection & written proposal</strong> — no surprises",
    ]
    info_box_title = f"Commercial roof leaks cost {name} businesses more than just repair"
    info_box_body = f"A leaking commercial roof in {name} means inventory damage, equipment exposure, liability risk, and business interruption. Early repair is always a fraction of the cost of full replacement. We inspect commercial properties for free and give you a clear repair plan."
    faq_items = [
        (f"How quickly can you respond to a commercial roof leak in {name}?", f"We prioritize commercial leaks. Call (216) 888-3208 — we aim for same-day or next-day response throughout {name} and {county}."),
        ("What commercial roof systems do you repair?", "We repair all common commercial systems: TPO, EPDM, modified bitumen, built-up (BUR), and metal roofing. We assess and recommend the right repair approach for your specific system."),
        ("Can you work around our business hours?", f"Yes — we schedule commercial repairs in {name} to minimize disruption, including early morning, evening, and weekend work when needed."),
        ("Do you handle commercial insurance claims?", f"Yes — we manage the full commercial insurance claim process for storm and hail damage to commercial properties in {name}."),
    ]
    section2_h = f"Commercial Roof Systems We Repair in {name}"
    section2_body = f"Atlas Roofing & Restoration repairs all commercial flat roof systems found on {name} properties: TPO single-ply membrane repairs including seam failures and punctures, EPDM rubber roof repairs including shrinkage and lap seam issues, modified bitumen repair including blistering and alligatoring, built-up roof repairs including gravel displacement and membrane cracking, and metal roof repairs including fastener failures and panel seam leaks. We document all damage thoroughly for insurance purposes and provide written proposals before starting any work."
    final_h = f"Commercial Roof Repair in {name} — Fast & Professional."
    final_p = "Free inspection. Written proposal. Minimal business disruption."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p

def page_commercial_roof_replacement(c):
    name, slug, county = c["name"], c["slug"], c["county"]
    st1 = c["streets"][0]
    slug_out = f"commercial-roof-replacement-{slug}-oh"
    title = f"Commercial Roof Replacement {name} Ohio | Atlas Roofing & Restoration"
    desc = f"Full commercial roof replacement in {name}, Ohio. TPO, EPDM, flat roof systems. GAF certified, BBB A+. Free inspection & detailed proposal. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Commercial Roof Replacement in"; h1_line2 = f"{name}, Ohio"
    badge_text = f"Commercial Replacement — {name}, OH"
    hero_p = f"Time to replace your commercial roof in {name}? Atlas Roofing & Restoration provides full commercial roof replacement throughout {name} and {county}. We install TPO, EPDM, modified bitumen, and other commercial systems — with detailed written proposals, project management from start to finish, and the same GAF certified quality we bring to every job. Free inspection and proposal, no obligation."
    cta_btn = f"Free Commercial Proposal — {name}"
    checklist_items = [
        "<strong>TPO & EPDM systems</strong> — energy-efficient, long-lasting flat roof solutions",
        "<strong>Modified bitumen</strong> — proven performance for commercial buildings",
        "<strong>Full tear-off or recover</strong> — we assess and recommend the right approach",
        "<strong>Detailed written proposals</strong> — line-item pricing, no surprises",
        "<strong>Project management</strong> — one point of contact start to finish",
        "<strong>Insurance claims handled</strong> — storm damage replacement coordinated",
    ]
    info_box_title = f"When is commercial roof replacement the right call in {name}?"
    info_box_body = f"Commercial roofs typically last 15-25 years depending on the system. If your {name} property's roof is approaching that age, has been repaired multiple times, or has widespread membrane failure, replacement is often more cost-effective than continued repair. We give you an honest assessment — repair vs. replace — during our free inspection."
    faq_items = [
        ("What commercial roofing systems do you install?", f"We install TPO single-ply, EPDM rubber, modified bitumen, and built-up roofing systems. We assess your {name} building and recommend the system that best fits your budget, building type, and performance requirements."),
        ("How long does commercial roof replacement take?", f"Timeline depends on building size and system selected. Most commercial replacements in {name} are completed in 2-5 days. We minimize disruption to your operations throughout."),
        ("Do you provide warranties on commercial replacements?", "Yes — we provide manufacturer warranties on materials and our own workmanship warranty. Details are outlined in your proposal."),
        ("Can you handle large commercial or multi-building projects?", f"Yes — we handle commercial projects of all sizes in {name} and throughout Northeast Ohio, including multi-building property management portfolios."),
    ]
    section2_h = f"Commercial Roof Replacement Process in {name}"
    section2_body = f"Our commercial roof replacement process for {name} properties starts with a free, thorough inspection and detailed written proposal. Once approved, we handle complete tear-off and disposal of the existing system, deck inspection and repair as needed, installation of the new roofing system with manufacturer-specified materials, all flashing, curb, and penetration details, and final inspection and warranty documentation. We work around your business schedule and keep you informed at every stage."
    final_h = f"Commercial Roof Replacement in {name} — Done Right."
    final_p = "Free inspection. Detailed proposal. Quality installation."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p

def page_flat_roof(c):
    name, slug, county = c["name"], c["slug"], c["county"]
    slug_out = f"flat-roof-{slug}-oh"
    title = f"Flat Roof {name} Ohio | Repair & Replacement — Atlas Roofing"
    desc = f"Flat roof repair and replacement in {name}, Ohio. TPO, EPDM, modified bitumen. GAF certified, BBB A+. Free inspection & proposal. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Flat Roof Repair & Replacement in"; h1_line2 = f"{name}, Ohio"
    badge_text = f"Flat Roof Specialist — {name}, OH"
    hero_p = f"Flat roof problems in {name}? Atlas Roofing & Restoration specializes in flat and low-slope roofing throughout {name} and {county}. Whether you need a targeted repair on an existing TPO or EPDM system, or a full flat roof replacement, we bring the same certified quality and transparent pricing to every commercial and residential flat roof project. Free inspection, written proposal."
    cta_btn = f"Free Flat Roof Inspection — {name}"
    checklist_items = [
        "<strong>TPO installation & repair</strong> — energy-efficient single-ply membrane",
        "<strong>EPDM rubber roofing</strong> — durable, cost-effective flat roof solution",
        "<strong>Modified bitumen</strong> — proven performance in Ohio's climate",
        "<strong>Drainage assessment</strong> — proper slope and drain placement critical",
        "<strong>Ponding water solutions</strong> — tapered insulation and drain upgrades",
        "<strong>Free inspection & proposal</strong> — honest assessment, no obligation",
    ]
    info_box_title = f"Flat roofs in {name} need specialist attention"
    info_box_body = f"Flat and low-slope roofs have different failure modes than pitched roofs — ponding water, membrane seam failures, and drain blockages are the most common issues in {name}. These require a contractor who understands flat roof systems specifically, not just a general roofer. Atlas specializes in all major flat roof systems."
    faq_items = [
        ("What flat roof systems do you install?", f"We install and repair TPO, EPDM, modified bitumen, and built-up roofing systems on {name} commercial and residential flat roofs."),
        ("How long do flat roofs last in Ohio?", "TPO and EPDM systems typically last 15-25 years with proper maintenance. Modified bitumen systems last 15-20 years. We'll tell you honestly where your current system stands during our free inspection."),
        ("What causes flat roofs to leak?", f"The most common causes on {name} flat roofs: seam failures where membrane sections are joined, punctures from foot traffic or debris, drain blockages causing ponding water, and flashing failures at parapet walls and penetrations."),
        ("Can a flat roof be repaired or does it need full replacement?", f"Often repaired — isolated seam failures, punctures, and flashing issues are all repairable. Widespread membrane failure or a roof over 20 years old typically warrants replacement. We give you an honest assessment at no charge."),
    ]
    section2_h = f"Flat Roof Services in {name}"
    section2_body = f"Atlas Roofing & Restoration provides complete flat roof services for {name} commercial properties, apartment buildings, and flat-roofed residential homes: TPO single-ply membrane installation and repair, EPDM rubber roof installation and repair, modified bitumen torch-down systems, built-up roofing maintenance and replacement, tapered insulation systems to eliminate ponding water, drain installation and replacement, and parapet wall and curb flashing. We assess, propose, and deliver — with full transparency at every step."
    final_h = f"Flat Roof Specialist in {name}, Ohio."
    final_p = "All major flat roof systems. Free inspection. Written proposal."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p

def page_tpo_roofing(c):
    name, slug, county = c["name"], c["slug"], c["county"]
    slug_out = f"tpo-roofing-{slug}-oh"
    title = f"TPO Roofing {name} Ohio | Installation & Repair — Atlas Roofing"
    desc = f"TPO roofing installation and repair in {name}, Ohio. Energy-efficient, durable single-ply membrane. GAF certified, BBB A+. Free inspection. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "TPO Roofing in"; h1_line2 = f"{name}, Ohio"
    badge_text = f"TPO Roofing — {name}, OH"
    hero_p = f"Looking for TPO roofing in {name}? Atlas Roofing & Restoration installs and repairs TPO single-ply membrane roofing throughout {name} and {county}. TPO is one of the most popular commercial roofing systems today — energy-efficient, UV-resistant, and highly durable in Ohio's climate. We provide free inspections, detailed proposals, and certified installation. Call (216) 888-3208."
    cta_btn = f"Free TPO Roof Inspection — {name}"
    checklist_items = [
        "<strong>TPO installation</strong> — properly heat-welded seams, no gaps or failures",
        "<strong>TPO repair</strong> — seam failures, punctures, and membrane damage fixed",
        "<strong>Energy efficient</strong> — reflective white membrane reduces cooling costs",
        "<strong>Durable in Ohio climate</strong> — UV and weather resistant",
        "<strong>Lightweight system</strong> — minimal structural load",
        "<strong>Free inspection & proposal</strong> — full assessment before commitment",
    ]
    info_box_title = f"Why TPO is popular for {name} commercial buildings"
    info_box_body = f"TPO's reflective white surface reduces heat absorption, lowering cooling costs for {name} commercial buildings in summer. It's also highly resistant to UV degradation, chemical exposure, and punctures — making it one of the best long-term value flat roof systems available. Properly installed TPO lasts 20+ years."
    faq_items = [
        ("What is TPO roofing?", "TPO (Thermoplastic Polyolefin) is a single-ply membrane roofing system popular for commercial flat roofs. It's installed in large sheets that are heat-welded at the seams to create a watertight bond."),
        ("How long does TPO roofing last?", f"Properly installed TPO roofing in {name}'s climate typically lasts 15-25 years. We install TPO to manufacturer specifications to ensure maximum lifespan."),
        ("Can TPO be repaired or does it always need full replacement?", "Isolated seam failures, punctures, and small membrane damage are very repairable on TPO systems. We assess your {name} roof and give you an honest repair vs. replace recommendation."),
        ("Is TPO better than EPDM?", "Both are excellent systems with different strengths. TPO is more energy-efficient due to its white reflective surface. EPDM has a longer track record and can be more cost-effective in some applications. We'll recommend the right system for your specific building."),
    ]
    section2_h = f"TPO Roofing Installation & Repair in {name}"
    section2_body = f"Atlas Roofing & Restoration installs and repairs TPO roofing systems on commercial buildings, apartment complexes, and flat-roofed properties throughout {name} and {county}. Our TPO installations include proper substrate preparation, insulation installation where required, TPO membrane installation with heat-welded seams, all flashing and termination details at walls and penetrations, and thorough final inspection. We use quality TPO materials and follow manufacturer installation specifications to ensure your warranty is valid and your roof performs."
    final_h = f"TPO Roofing in {name} — Installed Right."
    final_p = "Energy-efficient. Durable. Free inspection and proposal."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p

def page_epdm_roofing(c):
    name, slug, county = c["name"], c["slug"], c["county"]
    slug_out = f"epdm-roofing-{slug}-oh"
    title = f"EPDM Roofing {name} Ohio | Rubber Roof Installation & Repair — Atlas Roofing"
    desc = f"EPDM rubber roofing installation and repair in {name}, Ohio. Durable, cost-effective flat roof solution. GAF certified, BBB A+. Free inspection. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "EPDM Roofing in"; h1_line2 = f"{name}, Ohio"
    badge_text = f"EPDM Rubber Roofing — {name}, OH"
    hero_p = f"Looking for EPDM rubber roofing in {name}? Atlas Roofing & Restoration installs and repairs EPDM roofing systems throughout {name} and {county}. EPDM is one of the most proven commercial flat roof systems — highly durable, flexible in cold temperatures, and cost-effective for Ohio's demanding climate. Free inspection, detailed proposal, certified installation."
    cta_btn = f"Free EPDM Inspection — {name}"
    checklist_items = [
        "<strong>EPDM installation</strong> — fully adhered and mechanically fastened systems",
        "<strong>EPDM repair</strong> — lap seam failures, shrinkage, and punctures fixed",
        "<strong>Cold-weather performance</strong> — stays flexible in Ohio winters",
        "<strong>Proven durability</strong> — 20+ year track record",
        "<strong>Cost-effective</strong> — lower installed cost than many alternatives",
        "<strong>Free inspection & proposal</strong> — no obligation assessment",
    ]
    info_box_title = f"EPDM is well-suited for {name}'s climate"
    info_box_body = f"EPDM rubber roofing maintains flexibility in sub-zero temperatures — critical for {name}'s Ohio winters where other membranes can crack or become brittle. Its long track record of performance and relatively low installed cost make it a popular choice for commercial buildings and apartment complexes throughout Northeast Ohio."
    faq_items = [
        ("What is EPDM roofing?", "EPDM (Ethylene Propylene Diene Monomer) is a synthetic rubber membrane used on flat and low-slope roofs. It's one of the most widely used commercial roofing materials in the US."),
        ("How long does EPDM roofing last?", f"EPDM systems in {name}'s climate typically last 20-25 years with proper installation and maintenance. We install to manufacturer specifications for maximum lifespan."),
        ("What are common EPDM repair needs?", "The most common EPDM repairs: lap seam failures where sections join, shrinkage pulling away from flashings, punctures from foot traffic or debris, and flashing failures at walls and penetrations."),
        ("EPDM vs TPO — which is better?", "Both are excellent. EPDM has a longer track record and performs well in cold climates. TPO offers better UV reflectivity for energy savings. We assess your specific building and recommend the right system during our free inspection."),
    ]
    section2_h = f"EPDM Roofing Services in {name}"
    section2_body = f"Atlas Roofing & Restoration installs and repairs EPDM roofing systems on commercial properties, multi-family buildings, and flat-roofed structures throughout {name} and {county}. Our EPDM services include fully adhered and mechanically fastened installation options, proper seam and lap bonding, all flashing and termination bar details, repair of existing EPDM systems including seam re-bonding and patch work, and complete replacement when the system has reached end of life. We provide written proposals and warranties on all EPDM work."
    final_h = f"EPDM Roofing in {name} — Durable & Cost-Effective."
    final_p = "Proven flat roof system. Free inspection and proposal."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p

def page_multi_family(c):
    name, slug, county = c["name"], c["slug"], c["county"]
    slug_out = f"multi-family-roofing-{slug}-oh"
    title = f"Multi-Family Roofing {name} Ohio | Apartment & Condo Roofing — Atlas Roofing"
    desc = f"Multi-family roofing contractor in {name}, Ohio. Apartment buildings, condos, HOAs. GAF certified, BBB A+. Free inspection & proposal. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Multi-Family Roofing in"; h1_line2 = f"{name}, Ohio"
    badge_text = f"Multi-Family Roofing — {name}, OH"
    hero_p = f"Need a roofing contractor for a multi-family property in {name}? Atlas Roofing & Restoration works with property managers, HOAs, and building owners throughout {name} and {county} on apartment buildings, condominiums, duplexes, and larger multi-family complexes. We understand the unique requirements of multi-family roofing — coordinating around tenants, managing large scopes, and delivering consistent quality across multiple buildings. Free inspection and detailed proposal."
    cta_btn = f"Free Multi-Family Inspection — {name}"
    checklist_items = [
        "<strong>Apartment & condo roofing</strong> — all building types and sizes",
        "<strong>HOA roofing</strong> — familiar with association requirements and processes",
        "<strong>Tenant-considerate scheduling</strong> — minimize disruption to residents",
        "<strong>Multi-building coordination</strong> — phased projects managed efficiently",
        "<strong>Insurance claims</strong> — storm damage on multi-family properties handled",
        "<strong>Free inspection & detailed proposal</strong> — line-item pricing for your board",
    ]
    info_box_title = f"Multi-family roofing in {name} requires the right contractor"
    info_box_body = f"Multi-family roofing projects in {name} involve more complexity than single-family work — multiple units, tenant considerations, HOA or board approval processes, and larger scopes. Atlas has the crew size, project management experience, and commercial-grade materials to handle multi-family projects of any size throughout {county}."
    faq_items = [
        ("Do you work with HOAs and property management companies?", f"Yes — we regularly work with HOAs and property managers throughout {name} and {county}. We provide detailed written proposals suitable for board approval and can present to HOA boards directly."),
        ("Can you handle a complex with multiple buildings?", f"Absolutely. We manage multi-building roofing projects in {name} with phased scheduling to minimize disruption and stay within budget timelines."),
        ("How do you minimize disruption to tenants?", "We schedule work to avoid early morning or late evening hours, protect tenant entry/exit points, complete cleanup daily, and communicate the schedule clearly to property managers."),
        ("Do you handle storm damage claims for multi-family properties?", f"Yes — we manage the full commercial insurance claim process for hail, wind, and storm damage to multi-family properties in {name} and {county}."),
    ]
    section2_h = f"Multi-Family Roofing Services in {name}"
    section2_body = f"Atlas Roofing & Restoration provides complete roofing services for multi-family properties in {name}: apartment building roof replacement and repair, condominium complex roofing, HOA community roofing projects, duplex and triplex roofing, flat and low-slope roof systems for larger multi-family buildings, and storm damage restoration with insurance claim management. We work with property managers, building owners, and HOA boards to deliver quality roofing on schedule and within budget — with the professionalism and documentation your stakeholders require."
    final_h = f"Multi-Family Roofing in {name} — Professional & Reliable."
    final_p = "Property managers & HOAs welcome. Free inspection & proposal."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p

def page_apartment_roofing(c):
    name, slug, county = c["name"], c["slug"], c["county"]
    slug_out = f"apartment-roofing-{slug}-oh"
    title = f"Apartment Building Roofing {name} Ohio | Atlas Roofing & Restoration"
    desc = f"Apartment building roofing contractor in {name}, Ohio. Repairs, replacement, flat roofs. GAF certified, BBB A+. Free inspection & proposal. Call (216) 888-3208."
    canonical = f"https://atlasroofingrestoration.com/{slug_out}/"
    h1_line1 = "Apartment Building Roofing in"; h1_line2 = f"{name}, Ohio"
    badge_text = f"Apartment Roofing — {name}, OH"
    hero_p = f"Own or manage an apartment building in {name}? Atlas Roofing & Restoration provides apartment building roofing services throughout {name} and {county} — from emergency leak repairs to full roof replacements on buildings of all sizes. We work efficiently around your tenants, provide detailed proposals for ownership approval, and handle everything from permits to cleanup. Free inspection, no obligation."
    cta_btn = f"Free Apartment Roof Inspection — {name}"
    checklist_items = [
        "<strong>All building sizes</strong> — from small multi-unit to large complexes",
        "<strong>Flat & pitched roof systems</strong> — TPO, EPDM, shingles, metal",
        "<strong>Emergency repairs</strong> — tenant leaks addressed fast",
        "<strong>Full replacements</strong> — detailed proposals for owner/board approval",
        "<strong>Permit management</strong> — we handle all required permits",
        "<strong>Clean, professional crew</strong> — tenant and property respectful",
    ]
    info_box_title = f"Apartment roof failures in {name} create liability"
    info_box_body = f"A leaking roof on an apartment building in {name} isn't just a maintenance issue — it's a potential liability, habitability concern, and tenant relations problem. Atlas responds fast to apartment roof emergencies and provides long-term repair and replacement solutions to protect your investment and your tenants."
    faq_items = [
        ("Do you work on large apartment complexes?", f"Yes — we handle apartment roofing projects of all sizes in {name}, from small 4-unit buildings to large complexes with multiple buildings. We have the crew and project management to handle any scope."),
        ("How do you handle tenant concerns during roofing?", "We communicate the work schedule to property management, avoid early morning start times, protect building entries and common areas, and complete thorough cleanup each day."),
        ("Can you handle emergency roof leaks for occupied apartments?", f"Yes — we prioritize emergency calls for occupied buildings in {name}. Call (216) 888-3208 and we'll respond same-day or next-day."),
        ("Do you provide documentation for property owners?", "Yes — we provide detailed written proposals, permits, and completion documentation suitable for your property management records and insurance files."),
    ]
    section2_h = f"Apartment Roofing in {name} — What We Handle"
    section2_body = f"Atlas Roofing & Restoration handles the full range of apartment building roofing needs in {name}: emergency leak repairs with fast tenant-considerate response, flat roof repair and replacement on larger buildings using TPO, EPDM, or modified bitumen systems, pitched roof replacement on garden-style apartments using GAF shingles, gutters and drainage on multi-unit properties, storm damage repair and insurance claim management, and scheduled maintenance programs to extend roof life and prevent emergency calls. We work with individual building owners, property management companies, and real estate investors throughout {county}."
    final_h = f"Apartment Roofing in {name} — Protecting Your Investment."
    final_p = "Fast response. Professional crew. Free inspection & proposal."
    return slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text, hero_p, cta_btn, checklist_items, info_box_title, info_box_body, faq_items, section2_h, section2_body, final_h, final_p


# ── All commercial page types ─────────────────────────────────────────────────
COMMERCIAL_PAGE_TYPES = [
    page_commercial_roof_repair,
    page_commercial_roof_replacement,
    page_flat_roof,
    page_tpo_roofing,
    page_epdm_roofing,
    page_multi_family,
    page_apartment_roofing,
]

def update_sitemap(new_slugs):
    sitemap_path = os.path.join(SITE_DIR, "sitemap.xml")
    with open(sitemap_path, "r") as f:
        content = f.read()
    new_entries = ""
    for slug in new_slugs:
        url = f"https://atlasroofingrestoration.com/{slug}/"
        if url not in content:
            new_entries += f"  <url>\n    <loc>{url}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n"
    if new_entries:
        content = content.replace("</urlset>", new_entries + "</urlset>")
        with open(sitemap_path, "w") as f:
            f.write(content)
    return len(new_slugs)

def generate_commercial(cities=None, page_types=None, dry_run=False):
    if cities is None:
        cities = ALL_COMMERCIAL_CITIES
    if page_types is None:
        page_types = COMMERCIAL_PAGE_TYPES

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
                # Unpack result and build HTML
                (slug_out, title, desc, canonical, h1_line1, h1_line2, badge_text,
                 hero_p, cta_btn, checklist_items, info_box_title, info_box_body,
                 faq_items, section2_h, section2_body, final_h, final_p) = result
                html = build_page(c, slug_out, title, desc, canonical, h1_line1, h1_line2,
                                  badge_text, hero_p, cta_btn, checklist_items,
                                  info_box_title, info_box_body, faq_items,
                                  section2_h, section2_body, final_h, final_p)
                with open(out_file, "w", encoding="utf-8") as f:
                    f.write(html)

            generated.append(slug_out)

    return generated, skipped


if __name__ == "__main__":
    import sys
    dry = "--dry-run" in sys.argv
    print("Starting commercial generation (DRY RUN)..." if dry else "Starting commercial generation ...")
    generated, skipped = generate_commercial(dry_run=dry)
    print(f"\nGenerated: {len(generated)} pages")
    print(f"Skipped (already exist): {len(skipped)} pages")
    if generated and not dry:
        added = update_sitemap(generated)
        print(f"Sitemap updated: {added} new URLs added")
    if dry:
        print(f"\nTotal cities: {len(ALL_COMMERCIAL_CITIES)}")
        print(f"Page types: {len(COMMERCIAL_PAGE_TYPES)}")
        print(f"Expected total: {len(ALL_COMMERCIAL_CITIES) * len(COMMERCIAL_PAGE_TYPES)}")
        print("\nSample slugs:")
        for s in generated[:14]:
            print(f"  /{s}/")
