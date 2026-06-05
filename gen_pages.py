#!/usr/bin/env python3
import os

WHEEL = '''<svg viewBox="0 0 70 70" fill="none" stroke="currentColor" stroke-width="1.8" xmlns="http://www.w3.org/2000/svg"><circle cx="35" cy="35" r="31"/><circle cx="35" cy="35" r="7"/><line x1="35" y1="4" x2="35" y2="28"/><line x1="35" y1="42" x2="35" y2="66"/><line x1="4" y1="35" x2="28" y2="35"/><line x1="42" y1="35" x2="66" y2="35"/><line x1="13" y1="13" x2="30" y2="30"/><line x1="40" y1="40" x2="57" y2="57"/><line x1="57" y1="13" x2="40" y2="30"/><line x1="30" y1="40" x2="13" y2="57"/></svg>'''
HAT = '''<svg viewBox="0 0 100 65" fill="none" stroke="currentColor" stroke-width="1.8" xmlns="http://www.w3.org/2000/svg"><ellipse cx="50" cy="52" rx="46" ry="12"/><path d="M22,52 C22,52 20,18 50,12 C80,18 78,52 78,52"/><path d="M4,51 C12,46 20,52 22,52"/><path d="M78,52 C80,52 88,46 96,51"/><path d="M24,49 C35,43 65,43 76,49"/><path d="M32,35 C38,28 62,28 68,35" stroke-width="1" opacity="0.6"/></svg>'''
SKULL = '''<svg viewBox="0 0 110 90" fill="none" stroke="currentColor" stroke-width="1.8" xmlns="http://www.w3.org/2000/svg"><path d="M22,32 C4,12 8,40 22,42" stroke-linecap="round"/><path d="M88,32 C106,12 102,40 88,42" stroke-linecap="round"/><ellipse cx="55" cy="50" rx="33" ry="28"/><ellipse cx="42" cy="44" rx="8" ry="7"/><ellipse cx="68" cy="44" rx="8" ry="7"/><path d="M47,60 C48,57 62,57 63,60"/><path d="M45,63 L45,68 M50,62 L50,68 M55,62 L55,68 M60,62 L60,68 M65,63 L65,68"/><path d="M38,68 L45,73 L65,73 L72,68"/></svg>'''
HORSESHOE = '''<svg viewBox="0 0 80 85" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round" xmlns="http://www.w3.org/2000/svg"><path d="M16,75 L16,38 A24,24 0 1,1 64,38 L64,75"/><circle cx="26" cy="33" r="3.5" fill="currentColor" stroke="none"/><circle cx="54" cy="33" r="3.5" fill="currentColor" stroke="none"/><circle cx="20" cy="54" r="3.5" fill="currentColor" stroke="none"/><circle cx="60" cy="54" r="3.5" fill="currentColor" stroke="none"/></svg>'''
YUCCA = '''<svg viewBox="0 0 80 100" fill="none" stroke="currentColor" stroke-width="1.6" xmlns="http://www.w3.org/2000/svg"><line x1="40" y1="100" x2="40" y2="60" stroke-width="2.5"/><path d="M40,60 C40,60 20,50 5,35" stroke-linecap="round"/><path d="M40,60 C40,60 55,45 70,25" stroke-linecap="round"/><path d="M40,60 C40,60 15,55 0,50" stroke-linecap="round"/><path d="M40,60 C40,60 65,55 80,52" stroke-linecap="round"/><path d="M40,65 C40,65 22,60 8,58" stroke-linecap="round"/><path d="M40,65 C40,65 58,62 72,62" stroke-linecap="round"/><path d="M40,70 C40,70 28,68 18,72" stroke-linecap="round"/><path d="M40,70 C40,70 52,70 62,74" stroke-linecap="round"/><path d="M40,55 C38,45 35,30 42,5" stroke-linecap="round"/><path d="M42,5 L38,15 M42,5 L46,14" stroke-linecap="round"/></svg>'''
SUNBURST = '''<svg viewBox="0 0 80 80" fill="none" stroke="currentColor" stroke-width="1.6" xmlns="http://www.w3.org/2000/svg"><circle cx="40" cy="40" r="14"/><line x1="40" y1="2" x2="40" y2="22"/><line x1="40" y1="58" x2="40" y2="78"/><line x1="2" y1="40" x2="22" y2="40"/><line x1="58" y1="40" x2="78" y2="40"/><line x1="10" y1="10" x2="24" y2="24"/><line x1="56" y1="56" x2="70" y2="70"/><line x1="70" y1="10" x2="56" y2="24"/><line x1="24" y1="56" x2="10" y2="70"/><line x1="40" y1="2" x2="34" y2="12"/><line x1="40" y1="2" x2="46" y2="12"/><line x1="78" y1="40" x2="68" y2="34"/><line x1="78" y1="40" x2="68" y2="46"/></svg>'''
BOOTS = '''<svg viewBox="0 0 75 95" fill="none" stroke="currentColor" stroke-width="1.8" xmlns="http://www.w3.org/2000/svg"><path d="M50,8 L50,55 C50,58 60,62 65,70 L65,80 L20,80 L20,72 L30,65 L30,8 Z" stroke-linejoin="round"/><path d="M30,8 L50,8" stroke-linecap="round"/><path d="M20,80 L65,80 L68,85 L15,85 Z"/><path d="M33,25 C36,20 44,20 47,25" stroke-width="1.2"/><path d="M33,32 C36,27 44,27 47,32" stroke-width="1.2"/><path d="M33,39 C36,34 44,34 47,39" stroke-width="1.2"/><path d="M30,65 C35,62 45,62 50,65" stroke-width="1.2"/></svg>'''
SPUR = '''<svg viewBox="0 0 90 55" fill="none" stroke="currentColor" stroke-width="1.6" xmlns="http://www.w3.org/2000/svg"><path d="M5,28 C15,20 30,22 40,28 C50,34 65,36 80,28" stroke-linecap="round"/><circle cx="72" cy="28" r="12"/><line x1="72" y1="14" x2="72" y2="8"/><line x1="72" y1="42" x2="72" y2="48"/><line x1="58" y1="28" x2="52" y2="28"/><line x1="86" y1="28" x2="80" y2="28"/><line x1="62" y1="18" x2="58" y2="14"/><line x1="82" y1="38" x2="86" y2="42"/><line x1="82" y1="18" x2="86" y2="14"/><line x1="62" y1="38" x2="58" y2="42"/><path d="M5,28 C5,28 2,24 4,20 C6,16 12,18 12,22 L12,34 C12,38 6,40 4,36 C2,32 5,28 5,28 Z"/></svg>'''
AGAVE = '''<svg viewBox="0 0 80 95" fill="none" stroke="currentColor" stroke-width="1.6" xmlns="http://www.w3.org/2000/svg"><path d="M40,95 L40,58"/><path d="M40,58 C30,50 8,45 2,30 L6,28 C12,42 32,47 40,55"/><path d="M40,58 C50,50 72,45 78,30 L74,28 C68,42 48,47 40,55"/><path d="M40,65 C30,60 12,58 4,50 L7,47 C15,55 32,57 40,62"/><path d="M40,65 C50,60 68,58 76,50 L73,47 C65,55 48,57 40,62"/><path d="M40,72 C33,68 20,68 12,63 L14,60 C22,65 34,65 40,69"/><path d="M40,72 C47,68 60,68 68,63 L66,60 C58,65 46,65 40,69"/></svg>'''
DIAMOND = '''<svg viewBox="0 0 20 20" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M10,0 L12,8 L20,10 L12,12 L10,20 L8,12 L0,10 L8,8 Z"/></svg>'''
SMALL_DIAMOND = '''<svg viewBox="0 0 12 12" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M6,0 L7,5 L12,6 L7,7 L6,12 L5,7 L0,6 L5,5 Z"/></svg>'''

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

def build_icons():
    h = ""
    h += icon_div(WHEEL,    top=8,  left=8,  size=58)
    h += icon_div(SPUR,     top=14, left=72, size=52, rotate=-10)
    h += icon_div(HAT,      top=8,  left=130, size=65, opacity=0.75)
    h += icon_div(YUCCA,    top=6,  right=6, size=60)
    h += sparkle(top=22, left=200, size=13)
    h += small_sp(top=8,  left=250, size=8)
    h += small_sp(top=30, right=75, size=7)
    h += sparkle(top=16, right=72, size=10, op=0.35)
    h += icon_div(SKULL,    top=90,  left=4,  size=60, opacity=0.7)
    h += small_sp(top=160, left=6,  size=9)
    h += icon_div(SUNBURST, top=200, left=8,  size=52, opacity=0.68)
    h += small_sp(top=265, left=12, size=7)
    h += icon_div(AGAVE,    top=290, left=4,  size=58, opacity=0.7)
    h += icon_div(HORSESHOE,top=95,  right=4, size=52, opacity=0.72)
    h += small_sp(top=158, right=8, size=9)
    h += icon_div(BOOTS,    top=200, right=5, size=52, opacity=0.72)
    h += small_sp(top=270, right=14, size=7)
    h += icon_div(SPUR,     top=310, right=4, size=50, rotate=15, opacity=0.68)
    h += icon_div(SPUR,     bottom=10, left=6,  size=52, rotate=10, opacity=0.7)
    h += icon_div(HAT,      bottom=8,  left=70, size=62, opacity=0.73)
    h += icon_div(WHEEL,    bottom=8,  left=145, size=56)
    h += icon_div(SKULL,    bottom=8,  right=6,  size=58, opacity=0.7)
    h += sparkle(bottom=55, left=68, size=11, op=0.4)
    h += sparkle(bottom=22, left=210, size=13)
    h += small_sp(bottom=40, right=70, size=8)
    h += small_sp(bottom=18, left=240, size=7)
    h += small_sp(top=120, left=68, size=7, op=0.25)
    h += small_sp(top=145, right=66, size=8, op=0.25)
    h += small_sp(top=360, left=70, size=7, op=0.25)
    h += small_sp(top=380, right=68, size=8, op=0.25)
    return h

HAT_SVG_COVER = '''<svg style="width:80px;color:#3a5234;opacity:0.8;display:block;margin:0 auto 1.2rem;" viewBox="0 0 100 65" fill="none" stroke="currentColor" stroke-width="1.8" xmlns="http://www.w3.org/2000/svg"><ellipse cx="50" cy="52" rx="46" ry="12"/><path d="M22,52 C22,52 20,18 50,12 C80,18 78,52 78,52"/><path d="M4,51 C12,46 20,52 22,52"/><path d="M78,52 C80,52 88,46 96,51"/><path d="M24,49 C35,43 65,43 76,49"/></svg>'''

REVEAL_CSS = """
    #reveal-cover {
      position: fixed; inset: 0; z-index: 1000;
      background: #cbc4b0;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      transition: transform 0.85s cubic-bezier(.77,0,.18,1), opacity 0.7s ease;
    }
    #reveal-cover.revealed { transform: translateY(-100%); opacity: 0; }
    .cover-card {
      background: #e6ddc8;
      border: 1px solid rgba(58,82,52,.18);
      max-width: 310px; width: 88%;
      padding: 2.8rem 2rem 2.4rem;
      text-align: center; position: relative;
      box-shadow: 0 8px 40px rgba(58,82,52,.14);
    }
    .cover-eyebrow {
      font-size: .38rem; letter-spacing: .38em; text-transform: uppercase;
      color: #3a5234; opacity: .6; margin-bottom: .5rem;
    }
    .cover-title {
      font-family: 'Dancing Script', cursive;
      font-size: 1.85rem; color: #3a5234; line-height: 1.2; margin-bottom: 1.6rem;
    }
    .cover-ornament {
      display: flex; align-items: center; gap: .5rem; margin-bottom: 1.6rem;
    }
    .cover-ornament::before, .cover-ornament::after {
      content: ''; flex: 1; height: 1px; background: #3a5234; opacity: .22;
    }
    .cover-ornament span { font-size: .32rem; color: #3a5234; opacity: .38; letter-spacing: .2em; }
    #reveal-btn {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: .44rem; letter-spacing: .3em; text-transform: uppercase;
      color: #e6ddc8; background: #3a5234; border: none;
      padding: .9rem 2rem; cursor: pointer; width: 100%;
      transition: background 0.2s, transform 0.12s;
    }
    #reveal-btn:hover { background: #2e4029; transform: translateY(-1px); }
    #reveal-btn:active { transform: scale(0.97); }
    .cover-sp {
      position: absolute; color: #3a5234;
    }
    #confetti-canvas {
      position: fixed; inset: 0; width: 100%; height: 100%;
      pointer-events: none; z-index: 2000; display: none;
    }
"""

REVEAL_SCRIPT = r"""
<script>
(function(){
  var canvas=document.getElementById('confetti-canvas');
  var ctx=canvas.getContext('2d');
  var W,H,parts=[],running=false;
  function resize(){ W=canvas.width=window.innerWidth; H=canvas.height=window.innerHeight; }
  window.addEventListener('resize',resize); resize();
  var COLS=['#3a5234','#6a9c5e','#c8b060','#e6ddc8','#9a7a3a','#5c8c50','#b8a060','#4a7a40','#8fbc6a','#d4a83a'];
  function P(x,y){
    this.x=x; this.y=y;
    this.vx=(Math.random()-.5)*16;
    this.vy=-(Math.random()*20+10);
    this.g=0.6;
    this.col=COLS[Math.floor(Math.random()*COLS.length)];
    this.type=Math.floor(Math.random()*3);
    this.s=Math.random()*9+4;
    this.r=Math.random()*Math.PI*2;
    this.rs=(Math.random()-.5)*.28;
    this.op=1;
    this.fade=Math.random()*.013+.006;
  }
  P.prototype.tick=function(){
    this.vy+=this.g; this.x+=this.vx; this.y+=this.vy;
    this.vx*=.985; this.r+=this.rs; this.op-=this.fade;
  };
  P.prototype.draw=function(c){
    c.save(); c.globalAlpha=Math.max(0,this.op);
    c.fillStyle=this.col; c.translate(this.x,this.y); c.rotate(this.r);
    var s=this.s;
    if(this.type===0){
      c.beginPath(); c.moveTo(0,-s); c.lineTo(s*.55,0); c.lineTo(0,s); c.lineTo(-s*.55,0); c.closePath(); c.fill();
    } else if(this.type===1){
      c.fillRect(-s/2,-s/3,s,s*.6);
    } else {
      c.beginPath(); c.arc(0,0,s/2,0,Math.PI*2); c.fill();
    }
    c.restore();
  };
  function burst(x,y,n){ for(var i=0;i<n;i++) parts.push(new P(x,y)); }
  function loop(){
    if(!running) return;
    ctx.clearRect(0,0,W,H);
    for(var i=parts.length-1;i>=0;i--){
      parts[i].tick(); parts[i].draw(ctx);
      if(parts[i].op<=0||parts[i].y>H+60) parts.splice(i,1);
    }
    if(parts.length>0) requestAnimationFrame(loop);
    else { running=false; canvas.style.display='none'; }
  }
  function fire(x,y){
    canvas.style.display='block';
    burst(x,y,70);
    setTimeout(function(){ burst(W*.15,H*.4,35); },100);
    setTimeout(function(){ burst(W*.85,H*.4,35); },180);
    setTimeout(function(){ burst(W*.4,H*.25,45); },300);
    setTimeout(function(){ burst(W*.6,H*.3,35); },420);
    if(!running){ running=true; requestAnimationFrame(loop); }
  }
  document.getElementById('reveal-btn').addEventListener('click',function(e){
    var r=e.target.getBoundingClientRect();
    fire(r.left+r.width/2, r.top+r.height/2);
    var cover=document.getElementById('reveal-cover');
    cover.classList.add('revealed');
    setTimeout(function(){ cover.style.display='none'; },900);
  });
})();
</script>
"""

def sp(t,b,l,r,s,o):
    style=""
    if t is not None: style+=f"top:{t}px;"
    if b is not None: style+=f"bottom:{b}px;"
    if l is not None: style+=f"left:{l}px;"
    if r is not None: style+=f"right:{r}px;"
    return f'<div class="cover-sp" style="width:{s}px;height:{s}px;opacity:{o};{style}"><svg viewBox="0 0 20 20" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M10,0 L12,8 L20,10 L12,12 L10,20 L8,12 L0,10 L8,8 Z"/></svg></div>'

def reveal_cover(cover_eyebrow, cover_title):
    return f'''  <div id="reveal-cover">
    <canvas id="confetti-canvas"></canvas>
    <div class="cover-card">
      {sp(10,None,10,None,9,0.3)}{sp(12,None,None,12,7,0.22)}{sp(None,10,12,None,8,0.28)}{sp(None,12,None,10,10,0.32)}{sp(None,None,None,None,6,0.18)}
      {HAT_SVG_COVER}
      <p class="cover-eyebrow">{cover_eyebrow}</p>
      <p class="cover-title">{cover_title}</p>
      <div class="cover-ornament"><span>&#9670; &nbsp; &#9670; &nbsp; &#9670;</span></div>
      <button id="reveal-btn">Tap to Reveal &nbsp;&#9670;</button>
    </div>
  </div>'''

def det(label, value, ph=False):
    pc = ' ph' if ph else ''
    return f'''      <div class="detail">
        <span class="detail-label">{label}</span>
        <div class="detail-value{pc}">{value}</div>
      </div>'''

def build_page(title, cover_eyebrow, cover_title, eyebrow, script_line, big_name, subtitle,
               location, blurb, details_html, map_src, map_query, back_href="index.html"):
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
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
    :root{{--ink:#3a5234;--parchment:#e6ddc8;}}
    body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#cbc4b0;min-height:100vh;display:flex;justify-content:center;align-items:flex-start;padding:1.5rem 1rem 3rem;}}
    .card{{position:relative;width:100%;max-width:440px;background:var(--parchment);min-height:520px;overflow:hidden;}}
    .card::after{{content:'';position:absolute;inset:0;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='0.07'/%3E%3C/svg%3E");pointer-events:none;z-index:10;}}
    .content{{position:relative;z-index:5;text-align:center;padding:58px 50px 60px;}}
    .border-frame{{position:absolute;inset:5px;border:1px solid rgba(58,82,52,.18);pointer-events:none;z-index:6;}}
    .eyebrow-text{{font-size:.42rem;letter-spacing:.38em;text-transform:uppercase;color:var(--ink);opacity:.7;margin-bottom:.6rem;}}
    .script-line{{font-family:'Dancing Script',cursive;font-size:1.55rem;color:var(--ink);line-height:1.15;margin-bottom:.1rem;}}
    .big-name{{font-family:'Playfair Display',Georgia,serif;font-size:2.4rem;font-weight:900;text-transform:uppercase;letter-spacing:.04em;color:var(--ink);line-height:1.05;margin-bottom:.5rem;}}
    .venue-sub{{font-size:.46rem;letter-spacing:.28em;text-transform:uppercase;color:var(--ink);opacity:.62;margin-bottom:.2rem;}}
    .location-text{{font-family:'Dancing Script',cursive;font-size:.92rem;color:var(--ink);opacity:.58;margin-bottom:.8rem;}}
    .ornament{{display:flex;align-items:center;gap:.5rem;margin:.8rem 0;}}
    .ornament::before,.ornament::after{{content:'';flex:1;height:1px;background:var(--ink);opacity:.22;}}
    .ornament span{{font-size:.36rem;color:var(--ink);opacity:.38;letter-spacing:.22em;}}
    .blurb{{font-family:'Dancing Script',cursive;font-size:1.05rem;line-height:1.65;color:var(--ink);opacity:.78;margin-bottom:.9rem;text-align:center;}}
    .details{{text-align:left;margin-top:.4rem;}}
    .detail{{padding:.6rem 0;border-bottom:1px solid rgba(58,82,52,.1);}}
    .detail:last-child{{border-bottom:none;}}
    .detail-label{{display:block;font-size:.36rem;letter-spacing:.32em;text-transform:uppercase;color:var(--ink);opacity:.58;margin-bottom:.2rem;}}
    .detail-value{{font-size:.83rem;line-height:1.55;color:var(--ink);}}
    .detail-value.ph{{opacity:.38;font-style:italic;}}
    .map-section{{margin-top:1.3rem;}}
    .map-label{{font-size:.36rem;letter-spacing:.3em;text-transform:uppercase;color:var(--ink);opacity:.48;text-align:center;margin-bottom:.55rem;}}
    .map-embed{{width:100%;height:155px;border:1px solid rgba(58,82,52,.18);display:block;filter:sepia(20%) saturate(.7) brightness(1.05) hue-rotate(20deg);}}
    .map-link{{display:block;text-align:center;margin-top:.48rem;font-size:.36rem;letter-spacing:.26em;text-transform:uppercase;color:var(--ink);opacity:.52;text-decoration:none;}}
    .map-link:hover{{opacity:.88;}}
    .footer{{margin-top:1.1rem;padding-top:.8rem;border-top:1px solid rgba(58,82,52,.14);text-align:center;}}
    .back-link{{font-size:.36rem;letter-spacing:.22em;text-transform:uppercase;color:var(--ink);opacity:.46;text-decoration:none;}}
    .back-link:hover{{opacity:.82;}}
    .tagline{{font-family:'Dancing Script',cursive;font-size:.82rem;color:var(--ink);opacity:.32;margin-top:.3rem;}}
{REVEAL_CSS}
  </style>
</head>
<body>
{reveal_cover(cover_eyebrow, cover_title)}
<div class="card">
  <div class="border-frame"></div>
  {build_icons()}
  <div class="content">
    <p class="eyebrow-text">{eyebrow}</p>
    <p class="script-line">{script_line}</p>
    <h1 class="big-name">{big_name}</h1>
    <p class="venue-sub">{subtitle}</p>
    <p class="location-text">{location}</p>
    <div class="ornament"><span>&#9670; &nbsp; &#9670; &nbsp; &#9670;</span></div>
    <p class="blurb">{blurb}</p>
    <div class="ornament"><span>&#9670; &nbsp; &#9670; &nbsp; &#9670;</span></div>
    <div class="details">
{details_html}
    </div>
    <div class="map-section">
      <p class="map-label">How to get there</p>
      <iframe class="map-embed" src="{map_src}" title="Map" loading="lazy"></iframe>
      <a class="map-link" href="https://www.google.com/maps/search/?api=1&query={map_query}" target="_blank" rel="noopener">Open in Google Maps &#8599;</a>
    </div>
    <footer class="footer">
      <a class="back-link" href="{back_href}">&#8592; Return to itinerary</a>
      <p class="tagline">Music City, Tennessee</p>
    </footer>
  </div>
</div>
{REVEAL_SCRIPT}
</body>
</html>'''

# Map helpers
def osm(lat, lon, zoom=0.035):
    w = zoom * 1.5
    h = zoom
    return f"https://www.openstreetmap.org/export/embed.html?bbox={lon-w:.4f},{lat-h:.4f},{lon+w:.4f},{lat+h:.4f}&layer=mapnik&marker={lat:.4f},{lon:.4f}"

pages = [
    dict(
        file="friday-dinner.html",
        title="Friday Night — House of Cards",
        cover_eyebrow="Friday Night · Nashville",
        cover_title="Your first night in Music City awaits...",
        eyebrow="Dinner  ·  Friday Night",
        script_line="Kicking off the trip at",
        big_name="House of Cards",
        subtitle="Magic Speakeasy &amp; Fine Dining",
        location="119 3rd Ave S · Nashville, TN 37201",
        blurb="You made it — Nashville is officially on. House of Cards is one of a kind: a candlelit speakeasy hidden underground where some of America's top magicians work the room table to table all night. Classic American food, hand-crafted cocktails, and illusions up close. The perfect first night.",
        details='\n'.join([
            det("When", "Friday, June 5 · 9:00 PM"),
            det("Where", "119 3rd Ave S (below the Johnny Cash Museum)<br>Nashville, TN 37201"),
            det("Reservation", "Confirmation #199284 · (615) 730-8326"),
            det("Vibe", "Upscale magic speakeasy — fine dining, craft cocktails &amp; close-up illusions"),
            det("Why It's Special", "A 10,000 sq ft underground space where magicians perform table to table all evening — and an entrée includes a ticket to the magic showroom."),
            det("Heads Up", "Dress code is strictly enforced, so dress sharp. Fly in at 6:40 PM and you'll have plenty of time to drop bags first."),
        ]),
        map_src=osm(36.1597, -86.7757),
        map_query="House+of+Cards+119+3rd+Ave+S+Nashville+TN",
    ),
    dict(
        file="saturday-brunch.html",
        title="Saturday Brunch — Milk & Honey",
        cover_eyebrow="Saturday Morning · Nashville",
        cover_title="Rise &amp; shine — brunch awaits...",
        eyebrow="Brunch  ·  Saturday Morning",
        script_line="Morning biscuits at",
        big_name="Milk &amp; Honey",
        subtitle="Southern Brunch · Nashville",
        location="Nashville, Tennessee",
        blurb="One of Nashville's most-loved brunch spots. The honey butter biscuits are the stuff of legend and the cinnamon rolls run a close second. Come hungry — this is not the morning to hold back.",
        details='\n'.join([
            det("When", "Saturday, 11:00 AM"),
            det("Where", "214 11th Ave S (The Gulch)<br>Nashville, TN 37203"),
            det("Good to Know", "No reservations — first come, first served (open 6 AM–3 PM daily). Check in at the host stand for the wait."),
            det("Heads Up", "Biscuit Love is right around the corner at 316 11th Ave S if the wait is long — both are excellent"),
            det("Order", "Honey butter biscuits. Trust us."),
        ]),
        map_src=osm(36.1527, -86.7876),
        map_query="Milk+and+Honey+Nashville+TN",
    ),
    dict(
        file="dance-class.html",
        title="Line Dancing — Turn Their Heads",
        cover_eyebrow="Saturday Afternoon · Nashville",
        cover_title="Time to put on your dancing boots...",
        eyebrow="Activity  ·  Saturday Afternoon",
        script_line="Boot scootin' at",
        big_name="Turn Their Heads",
        subtitle="Line Dancing Lesson · Nashville",
        location="830 Fesslers Pkwy Ste 114 · Nashville, TN 37210",
        blurb="Y'all are about to become line dancers. Turn Their Heads is the only country-dance academy in Nashville with its own studio, and it's hyped as one of the best line dancing experiences in the city — five stars across hundreds of reviews. No experience required. Just show up ready to stomp, laugh, and look good doing it.",
        details='\n'.join([
            det("When", "Saturday, June 6 · 2:30 PM – 3:30 PM"),
            det("Where", "830 Fesslers Pkwy Ste 114<br>Nashville, TN 37210"),
            det("Booking", "#352878250 · (615) 676-1900"),
            det("Important", "Do NOT search the company name in Uber/Lyft — enter the address directly: 830 Fesslers Pkwy Ste 114"),
            det("Arrive", "15–30 min early to check in. If another class is running, relax in the lounge — take a right as you enter."),
            det("What to Wear", "Boots, sneakers, or smooth-soled shoes (no sandals). Clothes you can move in."),
            det("What to Bring", "BYOB welcome! They sell sodas &amp; snacks. Good energy — they'll handle the rest."),
        ]),
        map_src=osm(36.1395, -86.7608),
        map_query="830+Fesslers+Pkwy+Nashville+TN+37210",
    ),
    dict(
        file="saturday-dinner.html",
        title="Saturday Dinner — Zaytinya",
        cover_eyebrow="Saturday Evening · Nashville",
        cover_title="Dinner before the main event...",
        eyebrow="Dinner  ·  Saturday Evening",
        script_line="Small plates &amp; big flavors at",
        big_name="Zaytinya",
        subtitle="Chef José Andrés · W Nashville",
        location="300 12th Ave S · The Gulch, Nashville",
        blurb="Chef José Andrés brings his acclaimed Eastern Mediterranean small plates to Music City — and it's as good as it sounds. Mezes drawn from the traditions of Turkey, Greece, and Lebanon, all made for sharing. Order everything that looks interesting and pass it around the table.",
        details='\n'.join([
            det("When", "Saturday, June 6 · 6:00 PM"),
            det("Where", "300 12th Ave S (W Nashville)<br>Nashville, TN 37203"),
            det("Reservation", "OpenTable · confirm closer to the date if needed"),
            det("Style", "Eastern Mediterranean small plates — order generously, share everything"),
            det("Why It's Special", "The José Andrés Group's first Nashville restaurant, opened inside the W in the heart of the Gulch."),
        ]),
        map_src=osm(36.1503, -86.7903),
        map_query="Zaytinya+W+Nashville+300+12th+Ave+S",
    ),
    dict(
        file="concert.html",
        title="Station Inn — Saturday Night",
        cover_eyebrow="Saturday Night · Nashville",
        cover_title="The real Nashville is waiting...",
        eyebrow="Live Music  ·  Saturday Night",
        script_line="A legendary night at",
        big_name="Station Inn",
        subtitle="World-Famous Bluegrass · Est. 1974",
        location="402 12th Ave S · The Gulch, Nashville",
        blurb="This is not a tourist trap. The Station Inn is genuinely world-famous — Nashville's home of bluegrass since 1974, and one of the most respected rooms of its kind anywhere. Wooden chairs, cold beer, no frills, and music that will stop you cold. You don't leave the same.",
        details='\n'.join([
            det("When", "Saturday, June 6 · 8:00 PM"),
            det("Where", "402 12th Ave S<br>Nashville, TN 37203"),
            det("Tickets", "Most shows are cash at the door (~$15–25/person); a few sell advance tickets online — worth a quick check"),
            det("Vibe", "Intimate, no-frills, completely authentic — wooden chairs &amp; cold beer, just ~175 seats"),
            det("Why It's Special", "Going strong since 1974, the Station Inn was honored with its own Country Music Hall of Fame exhibit, 'Bluegrass Beacon.'"),
            det("Pro Tip", "Arrive 15–20 min early for a good seat. Shows go late — leave whenever feels right."),
            det("After", "Take the slow walk back through the Gulch — the night's still young."),
        ]),
        map_src=osm(36.1477, -86.7930),
        map_query="Station+Inn+402+12th+Ave+S+Nashville+TN",
    ),
    dict(
        file="sunday-brunch.html",
        title="Sunday Brunch — Nashville",
        cover_eyebrow="Sunday Morning · Nashville",
        cover_title="One last Nashville morning...",
        eyebrow="Brunch  ·  Sunday",
        script_line="A slow morning at",
        big_name="Milk &amp; Honey",
        subtitle="Or Biscuit Love — your call",
        location="Nashville, Tennessee",
        blurb="The last morning deserves the full treatment. Milk &amp; Honey for those biscuits again, or Biscuit Love for the legendary Bonuts. Either way, order the most indulgent thing on the menu. You've absolutely earned it.",
        details='\n'.join([
            det("When", "Sunday, 12:00 PM"),
            det("Option A", "Milk &amp; Honey — 214 11th Ave S, The Gulch"),
            det("Option B", "Biscuit Love — 316 11th Ave S, The Gulch<br><em style='font-size:.8em;opacity:.7'>Famous for their Bonuts — fried biscuit-dough topped with lemon mascarpone &amp; blueberry compote</em>"),
            det("Vibe", "Take it slow — no agenda for the morning"),
        ]),
        map_src=osm(36.1527, -86.7876),
        map_query="Milk+and+Honey+Nashville+TN+Gulch",
    ),
    dict(
        file="lodging.html",
        title="Your Hotel — Caption by Hyatt Nashville",
        cover_eyebrow="Your Home Base · Nashville",
        cover_title="Home for the weekend...",
        eyebrow="Your Stay  ·  Fri – Sun",
        script_line="Settle in at",
        big_name="Caption by Hyatt",
        subtitle="Nashville, The Gulch",
        location="118 12th Ave S · The Gulch, Nashville",
        blurb="Modern, comfortable, and perfectly planted in The Gulch — steps from everything you'll be doing this weekend. Drop your bags, take a breath, and get back out there. Nashville is waiting.",
        details='\n'.join([
            det("Check-in", "Friday from 3:00 PM"),
            det("Check-out", "Sunday — confirm with hotel"),
            det("Where", "118 12th Ave S<br>Nashville, TN 37203"),
            det("Location", "The Gulch — central to everything on the itinerary"),
            det("Access", "Front desk check-in — photo ID required"),
            det("Note", "A great home base — walkable to dinner, live music, brunch &amp; dessert right here in the Gulch"),
        ]),
        map_src=osm(36.1521, -86.7889),
        map_query="Caption+by+Hyatt+Downtown+Nashville+118+12th+Ave+S",
    ),
    dict(
        file="sunday-lodging.html",
        title="Sunday Night — Short Mountain Holiday",
        cover_eyebrow="Sunday Night · Liberty, TN",
        cover_title="A night in the Tennessee countryside...",
        eyebrow="Overnight Stay  ·  Sunday – Monday",
        script_line="Escaping to the hills at",
        big_name="Short Mountain Holiday",
        subtitle="215 Cove Ridge Ln · Liberty, TN",
        location="Liberty, Tennessee",
        blurb="Trade the Nashville skyline for Tennessee stars. Short Mountain Holiday is a secluded glamping dome set on private countryside acreage in Liberty, TN, with Amber &amp; Micah as your hosts. After a full weekend in the city, this is the perfect way to finish the trip — quiet, wide open, and completely peaceful.",
        details='\n'.join([
            det("Check-in", "Sunday, June 7 · 3:00 PM"),
            det("Check-out", "Monday, June 8 · 11:00 AM"),
            det("Where", "215 Cove Ridge Ln<br>Liberty, TN 37095"),
            det("Confirmation", "#59615488"),
            det("Hosts", "Amber &amp; Micah @ Short Mountain Holiday"),
            det("Why It's Special", "A geodesic glamping dome tucked away on private acreage — total seclusion under the Tennessee stars, about an hour east of Nashville."),
            det("Note", "Check-in instructions will be sent after final payment."),
        ]),
        map_src=osm(36.0148, -85.9680),
        map_query="215+Cove+Ridge+Ln+Liberty+TN+37095",
    ),
    dict(
        file="extra-1.html",
        title="Riverfront Park — Saturday",
        cover_eyebrow="Saturday · 3 PM",
        cover_title="A little detour worth taking...",
        eyebrow="A Quick Stop  ·  Saturday",
        script_line="Breathe it in at",
        big_name="Riverfront Park",
        subtitle="Along the Cumberland River",
        location="Downtown Nashville, Tennessee",
        blurb="A perfect 20–30 minute reset between the dance class and the evening ahead. Walk along the Cumberland River, take in the skyline, snap the inevitable bridge photo. This is the pause that makes the rest of the night better.",
        details='\n'.join([
            det("When", "Saturday, around 3:00 PM"),
            det("Where", "1 Riverfront Park, Nashville TN 37201<br>(Along the Cumberland River, downtown)"),
            det("Duration", "As long as you want — 20–30 minutes is plenty"),
            det("After", "Head back to the hotel by 3:30–4 PM to freshen up before dinner"),
            det("Don't Miss", "The John Seigenthaler Pedestrian Bridge — one of the longest pedestrian bridges in the world (built 1909). Best skyline shot in the city."),
        ]),
        map_src=osm(36.1627, -86.7716),
        map_query="Riverfront+Park+Nashville+TN",
    ),
    dict(
        file="extra-2.html",
        title="Dessert in The Gulch",
        cover_eyebrow="Saturday Night · After Station Inn",
        cover_title="End the night on something sweet...",
        eyebrow="Late Night  ·  The Gulch",
        script_line="One last sweet stop —",
        big_name="Dessert Route",
        subtitle="Between Station Inn &amp; the Hotel",
        location="The Gulch, Nashville",
        blurb="The Gulch is full of sweet spots within a couple of blocks. End the night on something good — pick whichever sounds right for the mood.",
        details='\n'.join([
            det("Right Here", "<strong>Five Daughters Bakery</strong><br>602 12th Ave S — the famous 100-layer donuts, a couple blocks down in the Gulch"),
            det("Worth the Hop", "<strong>Jeni's Splendid Ice Creams</strong><br>A true Nashville staple — the nearest scoop shop is a short rideshare away in 12 South"),
            det("Vibe", "Pick one (or two) and savor the last hours of Saturday in Nashville"),
        ]),
        map_src=osm(36.1483, -86.7906),
        map_query="Five+Daughters+Bakery+602+12th+Ave+S+Nashville",
    ),
    dict(
        file="extra-3.html",
        title="Monday — Free Day",
        cover_eyebrow="Monday · Nashville",
        cover_title="Nashville is all yours today...",
        eyebrow="Free Day  ·  Monday",
        script_line="No plans, no agenda —",
        big_name="Free Day",
        subtitle="Nashville, Tennessee",
        location="Nashville, Tennessee",
        blurb="No reservations. No schedule. Just Nashville and whatever sounds good. Some of the best moments of any trip happen when you stop trying to have them — wander, discover, and enjoy your last day in Music City.",
        details='\n'.join([
            det("Ideas", "Music Row walking tour · Centennial Park &amp; the Parthenon · Cheekwood Botanical Garden · 12 South neighborhood · East Nashville stroll"),
            det("Eats", "Hattie B's Hot Chicken (go spicy) · Pepperfire Hot Chicken · Mas Tacos Por Favor"),
            det("If You're Feeling It", "Day trip to Franklin (30 min) — beautiful historic downtown and great vintage shops"),
            det("Departure", "Leave enough time — Nashville airport can get busy on Mondays"),
        ]),
        map_src=osm(36.1627, -86.7816),
        map_query="Nashville+Tennessee",
    ),
]

base = "/home/user/anniversary-trip-website"
for p in pages:
    html = build_page(
        title=p["title"], cover_eyebrow=p["cover_eyebrow"], cover_title=p["cover_title"],
        eyebrow=p["eyebrow"], script_line=p["script_line"], big_name=p["big_name"],
        subtitle=p["subtitle"], location=p["location"], blurb=p["blurb"],
        details_html=p["details"], map_src=p["map_src"], map_query=p["map_query"],
    )
    with open(os.path.join(base, p["file"]), "w") as f:
        f.write(html)
    print(f"Wrote {p['file']}")

print("Done.")
