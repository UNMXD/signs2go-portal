#!/usr/bin/env python3
"""Generates the Signs2Go Portal static site. Run: python3 build.py"""
import os
ROOT = os.path.dirname(os.path.abspath(__file__))

NAV = [("index.html","Home"),("start.html","Start Here"),("manager.html","Manager"),
       ("printer.html","Printer Operator"),("products.html","Products & Pricing"),
       ("marketing.html","Marketing"),("standards.html","Standards & Files")]

def page(title, hero_title, hero_sub, body, active):
    nav = "".join(f'<a href="{h}"{" class=active" if h==active else ""}>{t}</a>' for h,t in NAV)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Signs2Go Portal</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="topbar">
  <a class="brand" href="index.html"><img src="images/logo-white.png" alt="Signs2Go"></a>
  <div class="portalname">Signs2Go <span>Portal</span></div>
  <nav>{nav}</nav>
</header>
<section class="hero">
  <h1>{hero_title}</h1>
  <p>{hero_sub}</p>
</section>
<main>
{body}
</main>
<footer>
  <img src="images/logo-black.png" alt="Signs2Go">
  <p>Signs2Go Portal — the internal team site. Team use only. No passwords or sensitive documents live here.</p>
</footer>
<script src="steps.js"></script>
</body>
</html>
"""
    return html

def steps(items):
    lis = "".join(
        f'<label class="step"><input type="checkbox" class="stepcheck"><span>'
        f'<span class="steptitle">{t}</span><p>{d}</p></span></label>' for t,d in items)
    return (f'<div class="progresswrap"><span class="progresstext">0 of {len(items)} steps done</span>'
            f'<div class="progress"><div class="bar"></div></div></div>'
            f'<div class="steps">{lis}</div>'
            f'<p class="alldone" hidden>All steps done. Nice work.</p>')

def card(img, href, title, desc):
    return (f'<a class="card" href="{href}"><img class="cardimg" src="{img}" alt="">'
            f'<span class="cardbody"><strong>{title}</strong><span>{desc}</span></span></a>')

PAGES = {}

# ---------------- Home ----------------
home_cards = "".join([
    card("images/shop.jpg","start.html","Start Here","How Signs2Go works, in one page. New here? Start with this."),
    card("images/coroplast.webp","manager.html","Manager","Orders, customers, pricing calls, shipping and pickup."),
    card("images/maxmetal.webp","printer.html","Printer Operator","The Digitech Texas printer, production, quality and packing."),
    card("images/foamboard.webp","products.html","Products & Pricing","What we sell, and the pricing rules that never change."),
    card("images/logo-black.png","marketing.html","Marketing","Our brand, our look, photos, posts and outreach — done the Signs2Go way."),
    card("images/shop.jpg","standards.html","Standards & Files","The rules, the files, and where everything lives."),
])
PAGES["index.html"] = page("Home","One team. Two jobs. <em>Every answer in one place.</em>",
    "The Signs2Go team portal. Slick and simple: find your job below, follow the steps, done.",
    f'<div class="grid">{home_cards}</div>'
    '<section class="band"><h2>The whole company, on one page</h2>'
    '<p>Signs2Go has two employees: a <strong>manager</strong> and a <strong>printer operator</strong>. '
    'This portal is built for exactly those two jobs — nothing extra. If a page here ever disagrees with '
    'Dad\'s price sheets, the sheets win. Tell Bobby so the page gets fixed.</p></section>',
    "index.html")

# ---------------- Start Here ----------------
PAGES["start.html"] = page("Start Here","Start Here",
    "How Signs2Go works, end to end.",
    '<section class="band"><h2>Signs2Go in plain words</h2>'
    '<p>We sell signs online first: customers order yard signs and political signs with instant pricing, '
    'and banners come through Sign 365 drop-ship. We print in-house, check every job, pack it right, '
    'and ship it or hold it for pickup. Small team, tight system — that is the whole point of this portal: '
    'how we run lives here, not just in somebody\'s head.</p></section>'
    '<h2 class="sect">Every order, step by step</h2>' +
    steps([
        ("Order comes in","An online order, a call, or a quote request. The manager takes it in and checks the details."),
        ("Artwork check","We check every file before printing. No file yet? The customer can send artwork after payment."),
        ("Print","The printer operator runs the job on the Digitech Texas printer (or the banner goes to Sign 365)."),
        ("Quality check","Look at the finished signs before they get packed. Crooked, faded or damaged does not ship."),
        ("Pack, ship or pickup","Pack it so it arrives clean. Ship it, or hold it at the shop for pickup."),
    ]) +
    '<section class="band"><h2>Your job</h2><p><strong>Manager?</strong> Your pages are Manager, Products &amp; Pricing, and Marketing. '
    '<strong>Printer operator?</strong> Your home is Printer Operator. Both of you: Standards &amp; Files is the rulebook.</p></section>',
    "start.html")

# ---------------- Manager ----------------
PAGES["manager.html"] = page("Manager","Manager",
    "Orders in, orders out — handled right, every time.",
    '<img class="pageimg" src="images/shop.jpg" alt="">'
    '<h2 class="sect">Taking an order</h2>' +
    steps([
        ("Get the full picture","Product, size, quantity, single or double sided, artwork status, due date, ship or pickup."),
        ("Price it from the sheets","Prices come from Bobby and Dad's price sheets only. Never guess a price, never invent one."),
        ("Respect the minimums","24x18: 10 piece minimum. 4x4: 2 pieces, pairs only. 4x8: 1 piece. 18x12 wholesale: multiples of 16 only."),
        ("Confirm artwork","We check every file before printing. Customers can send artwork after payment — we check it before it prints."),
        ("Hand it to production","Clear notes: what, how many, what material, when it is due. No guessing on the print floor."),
    ]) +
    '<h2 class="sect">Shipping &amp; pickup</h2>' +
    steps([
        ("Check before it leaves","Match the packed signs against the order. Count them."),
        ("Pack it clean","Flat, protected corners, nothing that can rub or bend in transit."),
        ("Mark it clearly","Customer name and order on the outside. Pickup orders go in the pickup spot, easy to find."),
    ]) +
    '<section class="band"><h2>Remember</h2><p>The line "Yard signs as low as $1.99" is advertising copy that gets the phone ringing — '
    'it is not a price you can sell at. Real pricing always comes from the sheets.</p></section>',
    "manager.html")

# ---------------- Printer Operator ----------------
PAGES["printer.html"] = page("Printer Operator","Printer Operator",
    "Print it right, check it, pack it. Your machines live here.",
    '<h2 class="sect">Our machines</h2><div class="grid">' +
    card("images/maxmetal.webp","digitech.html","Digitech Texas Printer","Our main printer. Photo and full steps coming — Bobby is getting the machine photos.",
         ) +
    '</div>'
    '<h2 class="sect">Every job, step by step</h2>' +
    steps([
        ("Read the job first","Product, size, quantity, material, due time. If anything is unclear, ask the manager before printing."),
        ("Check the file","Right size, right design, print-ready. A bad file makes a bad sign — catch it here."),
        ("Load and print","Load the right material, run the job, stay with the first piece until it looks right."),
        ("Quality check","Sharp print, right colors, clean cuts. Compare against the order, not just the screen."),
        ("Pack for the handoff","Stack flat and neat, protect the faces, label it for shipping or pickup."),
    ]),
    "printer.html")

# ---------------- Digitech ----------------
PAGES["digitech.html"] = page("Digitech Texas Printer","Digitech Texas Printer",
    "Our main production printer.",
    '<a class="back" href="printer.html">&larr; Back to Printer Operator</a>'
    '<div class="photospot"><strong>Photo coming</strong><span>Bobby is getting photos of our Digitech. '
    'When they land, the real machine goes right here — the same shot the team sees every day.</span></div>'
    '<section class="band"><h2>About this machine</h2>'
    '<p>This page will hold how <em>we</em> run our Digitech Texas printer: starting it up, loading material, '
    'the settings we use, cleaning, and what to do when something looks off. Those steps get written with our '
    'printer operator, from the real machine — not copied from a manual.</p>'
    '<p><strong>Exact model:</strong> to be confirmed from the machine nameplate photo.</p></section>'
    '<h2 class="sect">Until the full steps land</h2>' +
    steps([
        ("First piece check","Run one, look at it hard, then run the job."),
        ("Keep it clean","Wipe down and keep the print area clear at the end of every run."),
        ("Something looks off?","Stop and tell the manager. Do not push a bad run through."),
    ]),
    "printer.html")

# ---------------- Products & Pricing ----------------
PAGES["products.html"] = page("Products & Pricing","Products &amp; Pricing",
    "What we sell — and the rules that never bend.",
    '<div class="grid">'
    + card("images/coroplast.webp","products.html","Coroplast Yard Signs","Our main product. Instant online ordering with live pricing.")
    + card("images/foamboard.webp","products.html","Political Signs","Campaign season is our season. Priced from Dad's sheets.")
    + card("images/maxmetal.webp","products.html","Banners","Handled through Sign 365 drop-ship.")
    + '</div>'
    '<section class="band dark"><h2>Dad\'s minimums — no exceptions</h2>'
    '<ul class="biglist"><li><strong>24 x 18</strong> — 10 piece minimum</li>'
    '<li><strong>4 x 4</strong> — 2 pieces, pairs only</li>'
    '<li><strong>4 x 8</strong> — 1 piece</li>'
    '<li><strong>18 x 12 wholesale</strong> — multiples of 16 only, in the cart too</li></ul></section>'
    '<section class="band"><h2>Where prices live</h2>'
    '<p>All prices come from <strong>Bobby and Dad\'s price sheets</strong>. Those sheets are the master tables. '
    'Nothing on this page — or anywhere in this portal — replaces them, and nobody changes a price value without Dad. '
    'The "as low as $1.99" line is advertising, not a sellable price.</p></section>',
    "products.html")

# ---------------- Marketing ----------------
PAGES["marketing.html"] = page("Marketing","Marketing",
    "One brand, one look — everywhere Signs2Go shows up.",
    '<section class="band"><h2>Brand Standards — start here</h2>'
    '<img class="brandlogo" src="images/logo-black.png" alt="Signs2Go logo">'
    '<div class="swatches">'
    '<div class="sw black"><strong>True Black</strong><span>#000000</span></div>'
    '<div class="sw white"><strong>True White</strong><span>#FFFFFF</span></div>'
    '<div class="sw green"><strong>S2G Green</strong><span>#ACE50E</span></div></div>'
    '<ul class="biglist"><li>Black logo on light backgrounds. White-letter logo on black. Never the black logo on a dark background — it disappears.</li>'
    '<li>Only black, white and S2G green. No other brand colors, ever.</li>'
    '<li>Mostly white, clean and modern. White text is true white, never cream.</li></ul></section>'
    '<h2 class="sect">Photos &amp; posts</h2>' +
    steps([
        ("Shoot the work","Finished signs, the printer running, a packed order. The work sells the work."),
        ("Keep it on brand","Clean shot, good light, logo looking right. If it would not go on our own site, it does not get posted."),
        ("One theme","Radio, Instagram, email — everything sounds and looks like the same company."),
    ]) +
    '<h2 class="sect">Outreach &amp; promos</h2>'
    '<section class="band"><p><strong>Outreach email</strong> runs through our outreach program — approved templates only, in our voice. '
    '<strong>Price lists and promos</strong> are branded and Dad-approved before they go out. If it has a price on it and Dad has not seen it, it does not ship.</p></section>',
    "marketing.html")

# ---------------- Standards & Files ----------------
PAGES["standards.html"] = page("Standards & Files","Standards &amp; Files",
    "The rulebook — short, because the team is small.",
    '<h2 class="sect">How we work</h2><ul class="biglist">'
    '<li><strong>Check every file before printing.</strong> No exceptions.</li>'
    '<li><strong>Prices come from the sheets.</strong> Nobody invents or changes a price.</li>'
    '<li><strong>Quality before speed.</strong> A bad sign reprinted is slower than a check done right.</li>'
    '<li><strong>Write it down here.</strong> If a way of doing something changes, this portal changes the same day — that is how we stay franchise-ready.</li></ul>'
    '<section class="band"><h2>Where files live</h2>'
    '<p>Working files, price sheets and company documents live in the Signs2Go Drive folders (the Franchise Operations library). '
    'This portal links to them and explains them — it does not store sensitive documents, and <strong>passwords never go on this site</strong>.</p></section>'
    '<section class="band"><h2>About this portal</h2>'
    '<p>Built for Signs2Go\'s two-person team: the manager and the printer operator. '
    'Run by Bobby. To change something, tell Bobby — updates publish here the same way, in S2G black, white and green.</p></section>',
    "standards.html")

for name, html in PAGES.items():
    with open(os.path.join(ROOT, name), "w") as f:
        f.write(html)
    print("wrote", name)
