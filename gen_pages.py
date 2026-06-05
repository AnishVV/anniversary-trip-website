#!/usr/bin/env python3
import os

# SVG icon definitions
WHEEL = '''<svg viewBox="0 0 70 70" fill="none" stroke="currentColor" stroke-width="1.8" xmlns="http://www.w3.org/2000/svg">
  <circle cx="35" cy="35" r="31"/><circle cx="35" cy="35" r="7"/>
  <line x1="35" y1="4" x2="35" y2="28"/><line x1="35" y1="42" x2="35" y2="66"/>
  <line x1="4" y1="35" x2="28" y2="35"/><line x1="42" y1="35" x2="66" y2="35"/>
  <line x1="13" y1="13" x2="30" y2="30"/><line x1="40" y1="40" x2="57" y2="57"/>
  <line x1="57" y1="13" x2="40" y2="30"/><line x1="30" y1="40" x2="13" y2="57"/>
</svg>'''

HAT = '''<svg viewBox="0 0 100 65" fill="none" stroke="currentColor" stroke-width="1.8" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="50" cy="52" rx="46" ry="12"/>
  <path d="M22,52 C22,52 20,18 50,12 C80,18 78,52 78,52"/>
  <path d="M4,51 C12,46 20,52 22,52"/><path d="M78,52 C80,52 88,46 96,51"/>
  <path d="M24,49 C35,43 65,43 76,49"/>
  <path d="M32,35 C38,28 62,28 68,35" stroke-width="1" opacity="0.6"/>
</svg>'''

SKULL = '''<svg viewBox="0 0 110 90" fill="none" stroke="currentColor" stroke-width="1.8" xmlns="http://www.w3.org/2000/svg">
  <path d="M22,32 C4,12 8,40 22,42" stroke-linecap="round"/>
  <path d="M88,32 C106,12 102,40 88,42" stroke-linecap="round"/>
  <ellipse cx="55" cy="50" rx="33" ry="28"/>
  <ellipse cx="42" cy="44" rx="8" ry="7"/>
  <ellipse cx="68" cy="44" rx="8" ry="7"/>
  <path d="M47,60 C48,57 62,57 63,60"/>
  <path d="M45,63 L45,68 M50,62 L50,68 M55,62 L55,68 M60,62 L60,68 M65,63 L65,68"/>
  <path d="M38,68 L45,73 L65,73 L72,68"/>
</svg>'''

HORSESHOE = '''<svg viewBox="0 0 80 85" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round" xmlns="http://www.w3.org/2000/svg">
  <path d="M16,75 L16,38 A24,24 0 1,1 64,38 L64,75"/>
  <circle cx="26" cy="33" r="3.5" fill="currentColor" stroke="none"/>
  <circle cx="54" cy="33" r="3.5" fill="currentColor" stroke="none"/>
  <circle cx="20" cy="54" r="3.5" fill="currentColor" stroke="none"/>
  <circle cx="60" cy="54" r="3.5" fill="currentColor" stroke="none"/>
</svg>'''

YUCCA = '''<svg viewBox="0 0 80 100" fill="none" stroke="currentColor" stroke-width="1.6" xmlns="http://www.w3.org/2000/svg">
  <line x1="40" y1="100" x2="40" y2="60" stroke-width="2.5"/>
  <path d="M40,60 C40,60 20,50 5,35" stroke-linecap="round"/>
  <path d="M40,60 C40,60 55,45 70,25" stroke-linecap="round"/>
  <path d="M40,60 C40,60 15,55 0,50" stroke-linecap="round"/>
  <path d="M40,60 C40,60 65,55 80,52" stroke-linecap="round"/>
  <path d="M40,65 C40,65 22,60 8,58" stroke-linecap="round"/>
  <path d="M40,65 C40,65 58,62 72,62" stroke-linecap="round"/>
  <path d="M40,70 C40,70 28,68 18,72" stroke-linecap="round"/>
  <path d="M40,70 C40,70 52,70 62,74" stroke-linecap="round"/>
  <path d="M40,55 C38,45 35,30 42,5" stroke-linecap="round"/>
  <path d="M42,5 L38,15 M42,5 L46,14" stroke-linecap="round"/>
</svg>'''

SUNBURST = '''<svg viewBox="0 0 80 80" fill="none" stroke="currentColor" stroke-width="1.6" xmlns="http://www.w3.org/2000/svg">
  <circle cx="40" cy="40" r="14"/>
  <line x1="40" y1="2" x2="40" y2="22"/><line x1="40" y1="58" x2="40" y2="78"/>
  <line x1="2" y1="40" x2="22" y2="40"/><line x1="58" y1="40" x2="78" y2="40"/>
  <line x1="10" y1="10" x2="24" y2="24"/><line x1="56" y1="56" x2="70" y2="70"/>
  <line x1="70" y1="10" x2="56" y2="24"/><line x1="24" y1="56" x2="10" y2="70"/>
  <line x1="40" y1="2" x2="34" y2="12"/><line x1="40" y1="2" x2="46" y2="12"/>
  <line x1="78" y1="40" x2="68" y2="34"/><line x1="78" y1="40" x2="68" y2="46"/>
</svg>'''

BOOTS = '''<svg viewBox="0 0 75 95" fill="none" stroke="currentColor" stroke-width="1.8" xmlns="http://www.w3.org/2000/svg">
  <path d="M50,8 L50,55 C50,58 60,62 65,70 L65,80 L20,80 L20,72 L30,65 L30,8 Z" stroke-linejoin="round"/>
  <path d="M30,8 L50,8" stroke-linecap="round"/>
  <path d="M20,80 L65,80 L68,85 L15,85 Z"/>
  <path d="M33,25 C36,20 44,20 47,25" stroke-width="1.2"/>
  <path d="M33,32 C36,27 44,27 47,32" stroke-width="1.2"/>
  <path d="M33,39 C36,34 44,34 47,39" stroke-width="1.2"/>
  <path d="M30,65 C35,62 45,62 50,65" stroke-width="1.2"/>
</svg>'''

SPUR = '''<svg viewBox="0 0 90 55" fill="none" stroke="currentColor" stroke-width="1.6" xmlns="http://www.w3.org/2000/svg">
  <path d="M5,28 C15,20 30,22 40,28 C50,34 65,36 80,28" stroke-linecap="round"/>
  <circle cx="72" cy="28" r="12"/>
  <line x1="72" y1="14" x2="72" y2="8"/><line x1="72" y1="42" x2="72" y2="48"/>
  <line x1="58" y1="28" x2="52" y2="28"/><line x1="86" y1="28" x2="80" y2="28"/>
  <line x1="62" y1="18" x2="58" y2="14"/><line x1="82" y1="38" x2="86" y2="42"/>
  <line x1="82" y1="18" x2="86" y2="14"/><line x1="62" y1="38" x2="58" y2="42"/>
  <path d="M5,28 C5,28 2,24 4,20 C6,16 12,18 12,22 L12,34 C12,38 6,40 4,36 C2,32 5,28 5,28 Z"/>
</svg>'''

AGAVE = '''<svg viewBox="0 0 80 95" fill="none" stroke="currentColor" stroke-width="1.6" xmlns="http://www.w3.org/2000/svg">
  <path d="M40,95 L40,58"/>
  <path d="M40,58 C30,50 8,45 2,30 L6,28 C12,42 32,47 40,55"/>
  <path d="M40,58 C50,50 72,45 78,30 L74,28 C68,42 48,47 40,55"/>
  <path d="M40,65 C30,60 12,58 4,50 L7,47 C15,55 32,57 40,62"/>
  <path d="M40,65 C50,60 68,58 76,50 L73,47 C65,55 48,57 40,62"/>
  <path d="M40,72 C33,68 20,68 12,63 L14,60 C22,65 34,65 40,69"/>
  <path d="M40,72 C47,68 60,68 68,63 L66,60 C58,65 46,65 40,69"/>
</svg>'''

DIAMOND = '''<svg viewBox="0 0 20 20" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <path d="M10,0 L12,8 L20,10 L12,12 L10,20 L8,12 L0,10 L8,8 Z"/>
</svg>'''

SMALL_DIAMOND = '''<svg viewBox="0 0 12 12" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <path d="M6,0 L7,5 L12,6 L7,7 L6,12 L5,7 L0,6 L5,5 Z"/>
</svg>'''

def icon_div(svg, top=None, bottom=None, left=None, right=None, size=55, opacity=0.72, rotate=0):
    style = f"position:absolute;width:{size}px;height:{size}px;color:var(--ink);opacity:{opacity};"
    if top is not None: style += f"top:{top}px;"
    if bottom is not None: style += f"bottom:{bottom}px;"
    if left is not None: style += f"left:{left}px;"
    if right is not None: style += f"right:{right}px;"
    if rotate: style += f"transform:rotate({rotate}deg);"
    return f'<div style="{style}">{svg}</div>\n'

def sparkle(top=None, bottom=None, left=None, right=None, size=14, op=0.45):
    style = f"position:absolute;width:{size}px;height:{size}px;color:var(--ink);opacity:{op};"
    if top is not None: style += f"top:{top}px;"
    if bottom is not None: style += f"bottom:{bottom}px;"
    if left is not None: style += f"left:{left}px;"
    if right is not None: style += f"right:{right}px;"
    return f'<div style="{style}">{DIAMOND}</div>\n'

def small_sp(top=None, bottom=None, left=None, right=None, size=8, op=0.3):
    style = f"position:absolute;width:{size}px;height:{size}px;color:var(--ink);opacity:{op};"
    if top is not None: style += f"top:{top}px;"
    if bottom is not None: style += f"bottom:{bottom}px;"
    if left is not None: style += f"left:{left}px;"
    if right is not None: style += f"right:{right}px;"
    return f'<div style="{style}">{SMALL_DIAMOND}</div>\n'

def build_page(title, eyebrow, script_line, big_name, subtitle, location, details_html, map_src, map_query, back_href="index.html"):
    icons_html = ""
    # Top row icons
    icons_html += icon_div(WHEEL,    top=8,  left=8,  size=58)
    icons_html += icon_div(SPUR,     top=14, left=72, size=52, rotate=-10)
    icons_html += icon_div(HAT,      top=8,  left=130, size=65, opacity=0.75)
    icons_html += icon_div(YUCCA,    top=6,  right=6, size=60)
    # Top sparkles
    icons_html += sparkle(top=22, left=200, size=13)
    icons_html += small_sp(top=8,  left=250, size=8)
    icons_html += small_sp(top=30, right=75, size=7)
    icons_html += sparkle(top=16, right=72, size=10, op=0.35)
    # Left side
    icons_html += icon_div(SKULL,    top=90,  left=4,  size=60, opacity=0.7)
    icons_html += small_sp(top=160, left=6,  size=9)
    icons_html += icon_div(SUNBURST, top=200, left=8,  size=52, opacity=0.68)
    icons_html += small_sp(top=265, left=12, size=7)
    icons_html += icon_div(AGAVE,    top=290, left=4,  size=58, opacity=0.7)
    # Right side
    icons_html += icon_div(HORSESHOE,top=95,  right=4, size=52, opacity=0.72)
    icons_html += small_sp(top=158, right=8, size=9)
    icons_html += icon_div(BOOTS,    top=200, right=5, size=52, opacity=0.72)
    icons_html += small_sp(top=270, right=14, size=7)
    icons_html += icon_div(SPUR,     top=310, right=4, size=50, rotate=15, opacity=0.68)
    # Bottom row
    icons_html += icon_div(SPUR,     bottom=10, left=6,  size=52, rotate=10, opacity=0.7)
    icons_html += icon_div(HAT,      bottom=8,  left=70, size=62, opacity=0.73)
    icons_html += icon_div(WHEEL,    bottom=8,  left=145, size=56)
    icons_html += icon_div(SKULL,    bottom=8,  right=6,  size=58, opacity=0.7)
    # Bottom sparkles
    icons_html += sparkle(bottom=55, left=68, size=11, op=0.4)
    icons_html += sparkle(bottom=22, left=210, size=13)
    icons_html += small_sp(bottom=40, right=70, size=8)
    icons_html += small_sp(bottom=18, left=240, size=7)
    # Extra scattered
    icons_html += small_sp(top=120, left=68, size=7, op=0.25)
    icons_html += small_sp(top=145, right=66, size=8, op=0.25)
    icons_html += small_sp(top=360, left=70, size=7, op=0.25)
    icons_html += small_sp(top=380, right=68, size=8, op=0.25)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Playfair+Display:wght@400;700;900&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{ --ink: #3a5234; --parchment: #e6ddc8; }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: #cbc4b0;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      padding: 1.5rem 1rem 3rem;
    }}

    .card {{
      position: relative;
      width: 100%;
      max-width: 440px;
      background: var(--parchment);
      min-height: 520px;
      overflow: hidden;
    }}

    /* Grain texture */
    .card::after {{
      content: '';
      position: absolute;
      inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='0.07'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 10;
    }}

    .content {{
      position: relative;
      z-index: 5;
      text-align: center;
      padding: 88px 80px 90px;
    }}

    /* Thin border inside */
    .border-frame {{
      position: absolute;
      inset: 5px;
      border: 1px solid rgba(58,82,52,.18);
      pointer-events: none;
      z-index: 6;
    }}

    .eyebrow-text {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: .42rem;
      letter-spacing: .38em;
      text-transform: uppercase;
      color: var(--ink);
      opacity: .7;
      margin-bottom: .6rem;
    }}

    .script-line {{
      font-family: 'Dancing Script', cursive;
      font-size: 1.55rem;
      color: var(--ink);
      line-height: 1.15;
      margin-bottom: .1rem;
    }}

    .big-name {{
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 2.4rem;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: .04em;
      color: var(--ink);
      line-height: 1.05;
      margin-bottom: .5rem;
    }}

    .venue-sub {{
      font-size: .48rem;
      letter-spacing: .3em;
      text-transform: uppercase;
      color: var(--ink);
      opacity: .65;
      margin-bottom: .2rem;
    }}

    .location-text {{
      font-family: 'Dancing Script', cursive;
      font-size: .95rem;
      color: var(--ink);
      opacity: .6;
      margin-bottom: 1rem;
    }}

    .ornament {{
      display: flex;
      align-items: center;
      gap: .5rem;
      margin: .9rem 0;
    }}
    .ornament::before, .ornament::after {{
      content: '';
      flex: 1;
      height: 1px;
      background: var(--ink);
      opacity: .25;
    }}
    .ornament span {{
      font-size: .38rem;
      color: var(--ink);
      opacity: .4;
      letter-spacing: .25em;
    }}

    /* Details */
    .details {{ text-align: left; margin-top: .5rem; }}
    .detail {{ padding: .65rem 0; border-bottom: 1px solid rgba(58,82,52,.1); }}
    .detail:last-child {{ border-bottom: none; }}
    .detail-label {{
      display: block;
      font-size: .38rem;
      letter-spacing: .32em;
      text-transform: uppercase;
      color: var(--ink);
      opacity: .6;
      margin-bottom: .2rem;
    }}
    .detail-value {{
      font-size: .85rem;
      line-height: 1.55;
      color: var(--ink);
    }}
    .detail-value.ph {{
      opacity: .4;
      font-style: italic;
    }}

    /* Map */
    .map-section {{ margin-top: 1.4rem; }}
    .map-label {{
      font-size: .38rem;
      letter-spacing: .32em;
      text-transform: uppercase;
      color: var(--ink);
      opacity: .5;
      text-align: center;
      margin-bottom: .6rem;
    }}
    .map-embed {{
      width: 100%;
      height: 160px;
      border: 1px solid rgba(58,82,52,.2);
      display: block;
      filter: sepia(20%) saturate(.7) brightness(1.05) hue-rotate(20deg);
    }}
    .map-link {{
      display: block;
      text-align: center;
      margin-top: .5rem;
      font-size: .38rem;
      letter-spacing: .28em;
      text-transform: uppercase;
      color: var(--ink);
      opacity: .55;
      text-decoration: none;
    }}
    .map-link:hover {{ opacity: .9; }}

    /* Footer */
    .footer {{
      margin-top: 1.2rem;
      padding-top: .9rem;
      border-top: 1px solid rgba(58,82,52,.15);
      text-align: center;
    }}
    .back-link {{
      font-size: .38rem;
      letter-spacing: .25em;
      text-transform: uppercase;
      color: var(--ink);
      opacity: .5;
      text-decoration: none;
    }}
    .back-link:hover {{ opacity: .85; }}
    .tagline {{
      font-family: 'Dancing Script', cursive;
      font-size: .85rem;
      color: var(--ink);
      opacity: .35;
      margin-top: .3rem;
    }}
  </style>
</head>
<body>
<div class="card">
  <div class="border-frame"></div>
  {icons_html}
  <div class="content">
    <p class="eyebrow-text">{eyebrow}</p>
    <p class="script-line">{script_line}</p>
    <h1 class="big-name">{big_name}</h1>
    <p class="venue-sub">{subtitle}</p>
    <p class="location-text">{location}</p>

    <div class="ornament"><span>&#9670; &nbsp; &#9670; &nbsp; &#9670;</span></div>

    <div class="details">
{details_html}
    </div>

    <div class="map-section">
      <p class="map-label">How to get there</p>
      <iframe class="map-embed"
        src="{map_src}"
        title="Map" loading="lazy"></iframe>
      <a class="map-link" href="https://www.google.com/maps/search/?api=1&query={map_query}" target="_blank" rel="noopener">Open in Google Maps &#8599;</a>
    </div>

    <footer class="footer">
      <a class="back-link" href="{back_href}">&#8592; Return to itinerary</a>
      <p class="tagline">Music City, Tennessee</p>
    </footer>
  </div>
</div>
</body>
</html>'''

def det(label, value, ph=False):
    ph_class = ' ph' if ph else ''
    return f'''      <div class="detail">
        <span class="detail-label">{label}</span>
        <div class="detail-value{ph_class}">{value}</div>
      </div>'''

BASE_MAP = "https://www.openstreetmap.org/export/embed.html?bbox=-86.8278%2C36.1488%2C-86.7578%2C36.1788&layer=mapnik&marker=36.1627%2C-86.7816"

pages = [
    dict(
        file="friday-dinner.html",
        title="Friday Dinner — Nashville",
        eyebrow="Dinner  ·  Friday Evening",
        script_line="An Evening at",
        big_name="The Capitol Grille",
        subtitle="The Hermitage Hotel",
        location="Downtown Nashville, Tennessee",
        details='\n'.join([
            det("When", "Friday, 7:30 in the evening"),
            det("Where", "231 6th Ave N<br>Nashville, TN 37219"),
            det("Reservation", "Under Williams &nbsp;·&nbsp; Conf. #CG-4891"),
            det("Dress", "Smart casual — look nice"),
            det("Notes", "Valet at the entrance. Award-winning Southern cuisine and wine list."),
        ]),
        map_src=BASE_MAP,
        map_query="231+6th+Ave+N+Nashville+TN",
    ),
    dict(
        file="saturday-brunch.html",
        title="Saturday Brunch — Nashville",
        eyebrow="Brunch  ·  Saturday Morning",
        script_line="Morning biscuits at",
        big_name="Biscuit Love",
        subtitle="Bonuts &amp; Southern Brunch · The Gulch",
        location="Nashville, Tennessee",
        details='\n'.join([
            det("When", "Saturday, 10:00 in the morning"),
            det("Where", "316 11th Ave S<br>Nashville, TN 37203"),
            det("Reservation", "Walk-in — aim to arrive by 9:45"),
            det("Notes", "Order the Bonuts — biscuit donuts with lemon mascarpone. Weekend waits move quickly."),
        ]),
        map_src=BASE_MAP,
        map_query="316+11th+Ave+S+Nashville+TN",
    ),
    dict(
        file="dance-class.html",
        title="Dance Class — Nashville",
        eyebrow="Activity  ·  Saturday Afternoon",
        script_line="Put on your boots for",
        big_name="Two-Step &amp; Line Dancing",
        subtitle="Nashville Dance Studios",
        location="Nashville, Tennessee",
        details='\n'.join([
            det("When", "Saturday, 2:00 in the afternoon"),
            det("Where", "1805 Division St<br>Nashville, TN 37203"),
            det("Style", "Country two-step &amp; classic line dances"),
            det("Duration", "90 minutes"),
            det("What to Wear", "Boots encouraged — comfortable clothes you can move in"),
            det("Notes", "No experience needed — total beginners more than welcome!"),
        ]),
        map_src=BASE_MAP,
        map_query="1805+Division+St+Nashville+TN",
    ),
    dict(
        file="saturday-dinner.html",
        title="Saturday Dinner — Nashville",
        eyebrow="Dinner  ·  Saturday Evening",
        script_line="Dinner with a view at",
        big_name="Marsh House",
        subtitle="Thompson Nashville · The Gulch",
        location="Nashville, Tennessee",
        details='\n'.join([
            det("When", "Saturday, 7:00 in the evening"),
            det("Where", "401 11th Ave S<br>Nashville, TN 37203"),
            det("Reservation", "Under Williams &nbsp;·&nbsp; Conf. #MH-7723"),
            det("Dress", "Smart casual"),
            det("Notes", "Rooftop terrace with stunning skyline views. Ask for the chilled seafood tower."),
        ]),
        map_src=BASE_MAP,
        map_query="401+11th+Ave+S+Nashville+TN",
    ),
    dict(
        file="concert.html",
        title="Concert — Nashville",
        eyebrow="Live Music  ·  Saturday Night",
        script_line="A night at",
        big_name="Live at the Ryman",
        subtitle="Ryman Auditorium",
        location="Downtown Nashville, Tennessee",
        details='\n'.join([
            det("When", "Saturday — doors 7:00 PM, show 8:00 PM"),
            det("Venue", "116 5th Ave N<br>Nashville, TN 37219"),
            det("Tickets", "Digital — check your email for QR codes"),
            det("Bag Policy", "Small clutch or clear bag only"),
            det("Getting There", "Rideshare recommended — parking very limited Saturday nights"),
            det("Notes", "\"The Mother Church of Country Music.\" Soak in every moment."),
        ]),
        map_src=BASE_MAP,
        map_query="116+5th+Ave+N+Nashville+TN",
    ),
    dict(
        file="sunday-brunch.html",
        title="Sunday Brunch — Nashville",
        eyebrow="Brunch  ·  Sunday Morning",
        script_line="A lazy morning at",
        big_name="The Southern",
        subtitle="Southern Comfort &amp; Cocktails",
        location="Downtown Nashville, Tennessee",
        details='\n'.join([
            det("When", "Sunday, 11:00 in the morning"),
            det("Where", "150 3rd Ave N<br>Nashville, TN 37201"),
            det("Reservation", "Under Williams &nbsp;·&nbsp; Conf. #TS-0291"),
            det("Notes", "The house bloody mary is non-negotiable. Try the shrimp and grits."),
        ]),
        map_src=BASE_MAP,
        map_query="150+3rd+Ave+N+Nashville+TN",
    ),
    dict(
        file="lodging.html",
        title="Lodging — Nashville",
        eyebrow="Your Stay  ·  Fri – Sun",
        script_line="Home for the weekend at",
        big_name="The Noelle",
        subtitle="Curio Collection by Hilton",
        location="Downtown Nashville, Tennessee",
        details='\n'.join([
            det("Address", "200 4th Ave N<br>Nashville, TN 37219"),
            det("Check-in", "Friday from 3:00 PM"),
            det("Check-out", "Sunday by 11:00 AM"),
            det("WiFi", "NoelleGuest &nbsp;/&nbsp; nashville24"),
            det("Parking", "Valet, $45/night — contact concierge on arrival"),
            det("Notes", "Rooftop bar on the 25th floor — don't miss sunset. Steps from Broadway."),
        ]),
        map_src=BASE_MAP,
        map_query="200+4th+Ave+N+Nashville+TN",
    ),
    dict(
        file="sunday-lodging.html",
        title="Sunday Lodging — Nashville",
        eyebrow="Your Stay  ·  Sunday Night",
        script_line="Rest your boots at",
        big_name="Graduate Nashville",
        subtitle="Vanderbilt / Music Row",
        location="West End, Nashville, Tennessee",
        details='\n'.join([
            det("Address", "101 20th Ave N<br>Nashville, TN 37203"),
            det("Check-in", "Sunday from 3:00 PM"),
            det("Check-out", "Monday by 12:00 noon"),
            det("WiFi", "GraduateGuest &nbsp;/&nbsp; welcome24"),
            det("Parking", "On-site garage, $30/night"),
            det("Notes", "Pool open until 10 PM. Walking distance to Music Row and Vanderbilt."),
        ]),
        map_src=BASE_MAP,
        map_query="101+20th+Ave+N+Nashville+TN",
    ),
    dict(
        file="extra-1.html",
        title="Extra — Nashville",
        eyebrow="Nashville",
        script_line="Coming up next:",
        big_name="<!-- Event Name -->",
        subtitle="<!-- Venue -->",
        location="Nashville, Tennessee",
        details='\n'.join([
            det("When", "Date &amp; time to be added", ph=True),
            det("Where", "Address to be added", ph=True),
            det("Details", "Details to follow", ph=True),
            det("Notes", "Notes to follow", ph=True),
        ]),
        map_src=BASE_MAP,
        map_query="Nashville+TN",
    ),
    dict(
        file="extra-2.html",
        title="Extra — Nashville",
        eyebrow="Nashville",
        script_line="Coming up next:",
        big_name="<!-- Event Name -->",
        subtitle="<!-- Venue -->",
        location="Nashville, Tennessee",
        details='\n'.join([
            det("When", "Date &amp; time to be added", ph=True),
            det("Where", "Address to be added", ph=True),
            det("Details", "Details to follow", ph=True),
            det("Notes", "Notes to follow", ph=True),
        ]),
        map_src=BASE_MAP,
        map_query="Nashville+TN",
    ),
    dict(
        file="extra-3.html",
        title="Extra — Nashville",
        eyebrow="Nashville",
        script_line="Coming up next:",
        big_name="<!-- Event Name -->",
        subtitle="<!-- Venue -->",
        location="Nashville, Tennessee",
        details='\n'.join([
            det("When", "Date &amp; time to be added", ph=True),
            det("Where", "Address to be added", ph=True),
            det("Details", "Details to follow", ph=True),
            det("Notes", "Notes to follow", ph=True),
        ]),
        map_src=BASE_MAP,
        map_query="Nashville+TN",
    ),
]

base = "/home/user/anniversary-trip-website"
for p in pages:
    html = build_page(
        title=p["title"],
        eyebrow=p["eyebrow"],
        script_line=p["script_line"],
        big_name=p["big_name"],
        subtitle=p["subtitle"],
        location=p["location"],
        details_html=p["details"],
        map_src=p["map_src"],
        map_query=p["map_query"],
    )
    path = os.path.join(base, p["file"])
    with open(path, "w") as f:
        f.write(html)
    print(f"Wrote {p['file']}")

print("Done.")
