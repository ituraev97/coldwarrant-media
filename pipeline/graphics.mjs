// COLD WARRANT graphics renderer: builds HTML per graphic, renders intro frames + hold frame with Playwright.
// usage: node graphics.mjs <spec.json> <outdir>
import fs from "fs";
import path from "path";
import { createRequire } from "module";
import * as d3 from "d3-geo";
import * as topo from "topojson-client";
const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const NM = path.resolve("node_modules");
const world = JSON.parse(fs.readFileSync(`${NM}/world-atlas/countries-50m.json`));
const states = JSON.parse(fs.readFileSync(`${NM}/us-atlas/states-10m.json`));
const countries = topo.feature(world, world.objects.countries).features;
const usStates = topo.feature(states, states.objects.states).features;
const W = 1920, H = 1080;

const FONTS = `
@font-face{font-family:Anton;src:url(file://${NM}/@fontsource/anton/files/anton-latin-400-normal.woff2)}
@font-face{font-family:Oswald;font-weight:500;src:url(file://${NM}/@fontsource/oswald/files/oswald-latin-500-normal.woff2)}
@font-face{font-family:Oswald;font-weight:700;src:url(file://${NM}/@fontsource/oswald/files/oswald-latin-700-normal.woff2)}
@font-face{font-family:Plex;font-weight:500;src:url(file://${NM}/@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-500-normal.woff2)}
@font-face{font-family:Plex;font-weight:600;src:url(file://${NM}/@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-600-normal.woff2)}`;

const CSS = `${FONTS}
:root{--ink:#0A0A0B;--bone:#ECE7DC;--red:#D3212D;--amber:#E8A33D;--steel:#7A8089}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:${W}px;height:${H}px;overflow:hidden;background:var(--ink);color:var(--bone)}
.stage{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,#1b1b1f 0%,#0A0A0B 70%)}
.grain::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.18;mix-blend-mode:overlay;
 background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 1.6 -.3'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.mono{font-family:Plex;font-weight:600;letter-spacing:.32em;color:var(--steel)}
.anton{font-family:Anton;letter-spacing:.01em}
.osw{font-family:Oswald;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.red{color:var(--red)}.amber{color:var(--amber)}
.stamp{border:8px solid var(--red);color:var(--red);font-family:Plex;font-weight:600;letter-spacing:.3em;padding:10px 26px;display:inline-block}
.a{will-change:transform,opacity}
svg text{font-family:Oswald;font-weight:700;letter-spacing:.08em}
`;

const ANIM = `
<script>
function clamp(x){return Math.max(0,Math.min(1,x))}
function ease(x){return 1-Math.pow(1-x,3)}
window.setT=function(t){
 document.querySelectorAll('[data-d]').forEach(el=>{
  const d=parseFloat(el.dataset.d), dur=parseFloat(el.dataset.dur||'0.45'), k=el.dataset.k||'fade';
  const p=ease(clamp((t-d)/dur));
  if(k==='fade'){el.style.opacity=p;el.style.transform='translateY('+(24*(1-p))+'px)'}
  else if(k==='pop'){el.style.opacity=p;el.style.transform=(el.dataset.base||'')+' scale('+(1.35-0.35*p)+')'}
  else if(k==='slam'){el.style.opacity=p>0?1:0;el.style.transform=(el.dataset.base||'')+' scale('+(1.6-0.6*p)+')'}
  else if(k==='draw'){const L=el.getTotalLength();el.style.strokeDasharray=L;el.style.strokeDashoffset=L*(1-p);el.style.opacity=p>0?1:0}
  else if(k==='wipe'){el.style.clipPath='inset(0 '+(100-100*p)+'% 0 0)'}
  else if(k==='count'){const to=parseFloat(el.dataset.to);const v=to*p;el.textContent=(el.dataset.pre||'')+Math.round(v).toLocaleString('en-US')+(el.dataset.suf||'')}
 });
};
</script>`;

function page(body) {
  return `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body><div class="stage grain">${body}</div>${ANIM}</body></html>`;
}

// ---------- map helpers ----------
const byId = (id) => countries.find((f) => +f.id === id);
function mapSvg({ bounds, highlight = {}, dim = [], cities = [], arcs = [], labels = [], usHighlight = [], useUS = false, pad = 80, topPad = 0 }) {
  let proj, feats;
  if (useUS) {
    proj = d3.geoAlbersUsa().fitExtent([[pad, pad + 40], [W - pad, H - pad]], topo.feature(states, states.objects.states));
    feats = usStates;
  } else {
    const box = { type: "MultiPoint", coordinates: bounds };
    proj = d3.geoMercator().fitExtent([[pad + (topPad ? 40 : 0), pad + topPad], [W - pad, H - pad - 40]], box);
    feats = countries;
  }
  const g = d3.geoPath(proj);
  let s = `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" style="position:absolute;inset:0">`;
  s += `<defs><filter id="glow"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>`;
  for (const f of feats) {
    const id = useUS ? f.id : +f.id;
    const hl = useUS ? usHighlight.includes(id) : highlight[id];
    const fill = hl ? (useUS ? "#5a1217" : hl) : "#1c1c20";
    s += `<path d="${g(f)}" fill="${fill}" stroke="${hl ? "#D3212D" : "#34343a"}" stroke-width="${hl ? 2 : 1}" ${hl ? `data-d="${0.15}" data-dur="0.6"` : ""}/>`;
  }
  for (const a of arcs) {
    const p1 = proj(a.from), p2 = proj(a.to);
    const mx = (p1[0] + p2[0]) / 2, my = (p1[1] + p2[1]) / 2;
    const dx = p2[0] - p1[0], dy = p2[1] - p1[1];
    const bend = a.bend ?? 0.25;
    const cx = mx - dy * bend, cy = my + dx * bend;
    s += `<path d="M${p1[0]},${p1[1]} Q${cx},${cy} ${p2[0]},${p2[1]}" fill="none" stroke="${a.color || "#E8A33D"}" stroke-width="5" stroke-linecap="round" filter="url(#glow)" data-k="draw" data-d="${a.d ?? 0.4}" data-dur="${a.dur ?? 1.1}"/>`;
  }
  for (const c of cities) {
    const p = proj(c.ll);
    if (!p) continue;
    const ax = c.anchor || "start";
    const dx = ax === "end" ? -22 : 22;
    s += `<g data-d="${c.d ?? 0.3}"><circle cx="${p[0]}" cy="${p[1]}" r="10" fill="${c.color || "#ECE7DC"}" filter="url(#glow)"/>`;
    const dy = c.dy || 0;
    s += `<text x="${p[0] + dx}" y="${p[1] + 12 + dy}" text-anchor="${ax}" font-size="${c.size || 38}" fill="#ECE7DC">${c.name}</text>`;
    if (c.sub) s += `<text x="${p[0] + dx}" y="${p[1] + 50 + dy}" text-anchor="${ax}" font-size="24" fill="#7A8089" style="font-family:Plex;letter-spacing:.2em">${c.sub}</text>`;
    s += `</g>`;
  }
  for (const l of labels) {
    const p = proj(l.ll);
    s += `<text x="${p[0]}" y="${p[1]}" text-anchor="middle" font-size="${l.size || 30}" fill="${l.color || "#7A8089"}" data-d="${l.d ?? 0.2}" style="letter-spacing:.3em">${l.t}</text>`;
  }
  return s + `</svg>`;
}

function header(kicker, title, d = 0.1) {
  return `<div style="position:absolute;left:110px;top:90px">
   <div class="mono a" data-d="${d}" style="font-size:24px">${kicker}</div>
   <div class="osw a" data-d="${d + 0.12}" style="font-size:64px;margin-top:10px">${title}</div></div>`;
}
const footer = (src) => `<div class="mono a" data-d="0.9" style="position:absolute;left:110px;bottom:150px;font-size:21px;letter-spacing:.16em">${src}</div>`;

// ---------- graphic builders ----------
const B = {
  title: (o) => page(`
   <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
    <div class="stamp a" data-d="0.05" data-k="slam" style="font-size:34px;transform:rotate(-4deg)" data-base="rotate(-4deg)">CASE FILE ${o.case || "001"}</div>
    <div class="anton a" data-d="0.35" data-k="pop" style="font-size:${o.size || 330}px;line-height:.9;margin-top:30px;text-align:center">${o.title || 'MS-<span class="red">13</span>'}</div>
    <div class="osw a" data-d="0.75" style="font-size:54px;letter-spacing:.5em;margin-top:10px;padding-left:.5em">${o.sub || "BORN IN L.A."}</div>
   </div>
   <div class="a" data-d="1.0" style="position:absolute;bottom:70px;left:0;right:0;text-align:center"><span class="anton" style="font-size:36px">COLD</span> <span class="anton" style="font-size:36px;background:#D3212D;padding:0 10px">WARRANT</span></div>`),

  chapter: (o) => page(`
   <div style="position:absolute;left:180px;top:50%;transform:translateY(-50%)">
     <div class="mono a" data-d="0.05" style="font-size:30px">CASE FILE ${o.case || "001"} · PART ${o.n}</div>
     <div class="a" data-d="0.2" data-k="wipe" style="height:10px;width:220px;background:var(--red);margin:28px 0"></div>
     <div class="anton a" data-d="0.3" style="font-size:200px;line-height:.95">${o.t}</div>
   </div>`),

  stat: (o) => {
    const m = o.a.match(/^([\d,]+)(.*)$/);
    const num = m ? `<span class="a" data-d="0.15" data-k="count" data-dur="1.1" data-to="${m[1].replace(/,/g, "")}" data-suf="${m[2]}">${o.a}</span>` : `<span class="a" data-d="0.15" data-k="pop">${o.a}</span>`;
    return page(`<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding-left:180px">
     <div class="anton" style="font-size:300px;line-height:.9">${num}</div>
     <div class="a" data-d="0.5" data-k="wipe" style="height:10px;width:260px;background:var(--red);margin:34px 0 30px"></div>
     <div class="osw a" data-d="0.6" style="font-size:60px">${o.b}</div>
     <div class="mono a" data-d="0.8" style="font-size:26px;margin-top:20px">${o.c || ""}</div></div>`);
  },

  name: () => page(`<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
     <div class="mono a" data-d="0.05" style="font-size:28px">LOS ANGELES · EARLY 1980s</div>
     <div class="anton a" data-d="0.2" data-k="pop" style="font-size:210px;margin-top:20px">MARA <span class="red">SALVATRUCHA</span></div>
     <div class="osw a" data-d="0.7" style="font-size:44px;color:var(--amber);margin-top:10px">A GANG OF THEIR OWN</div></div>`),

  name2: () => page(`${header("WHAT THE NAME MEANS", "MARA · SALVA · TRUCHA")}
   <div style="position:absolute;left:110px;right:110px;top:330px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px">
    ${[["MARA", "Central American slang for <b>gang</b>", "possibly from <i>marabunta</i> — a swarm of army ants"], ["SALVA", "<b>Salvadoran</b>", "the refugees who founded it"], ["TRUCHA", "street slang for <b>sharp, alert</b>", "watch your back"]].map((c, i) => `
     <div class="a" data-d="${0.3 + i * 0.25}" style="border-top:8px solid ${i === 0 ? "#D3212D" : i === 1 ? "#ECE7DC" : "#E8A33D"};padding-top:30px">
       <div class="anton" style="font-size:130px">${c[0]}</div>
       <div class="osw" style="font-size:40px;margin-top:10px;text-transform:none;letter-spacing:.02em">${c[1]}</div>
       <div style="font-family:Plex;font-size:24px;color:#7A8089;margin-top:16px;line-height:1.4">${c[2]}</div></div>`).join("")}
   </div>${footer("ETYMOLOGY DISPUTED · SOURCES: WIKIPEDIA, INSIGHT CRIME")}`),

  thirteen: () => {
    const letters = "ABCDEFGHIJKLM".split("");
    return page(`${header("WHY 13", "M IS THE 13TH LETTER")}
     <div style="position:absolute;left:110px;right:110px;top:380px;display:flex;justify-content:space-between">
      ${letters.map((l, i) => `<div class="a" data-d="${0.2 + i * 0.07}" style="text-align:center">
        <div class="anton" style="font-size:${l === "M" ? 190 : 110}px;color:${l === "M" ? "#D3212D" : "#3a3a40"};line-height:1">${l}</div>
        <div class="mono" style="font-size:22px;letter-spacing:.1em;color:${l === "M" ? "#ECE7DC" : "#55555c"}">${i + 1}</div></div>`).join("")}
     </div>
     <div class="osw a" data-d="1.3" style="position:absolute;left:110px;bottom:150px;font-size:44px;color:var(--amber)">MARA SALVATRUCHA + SUREÑOS → MS-13</div>
     ${footer("BELIEVED TO SIGNAL ALLEGIANCE TO THE SUREÑOS / MEXICAN MAFIA")}`);
  },

  cliques: () => {
    let boxes = "";
    const names = ["CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE", "CLIQUE"];
    names.forEach((n, i) => {
      const col = i % 6, row = Math.floor(i / 6);
      boxes += `<div class="a" data-d="${0.2 + i * 0.06}" data-k="pop" style="position:absolute;left:${170 + col * 270}px;top:${380 + row * 230}px;width:230px;height:170px;border:4px solid #ECE7DC;display:flex;flex-direction:column;align-items:center;justify-content:center">
       <div class="osw" style="font-size:34px">${n}</div><div class="mono" style="font-size:18px;margin-top:8px;letter-spacing:.15em">TERRITORY ${String(i + 1).padStart(2, "0")}</div></div>`;
    });
    return page(`${header("STRUCTURE", "BUILT FROM CLIQUES")}${boxes}${footer("EACH CLIQUE: ITS OWN LEADERS · ITS OWN TERRITORY · ITS OWN CRIMES")}`);
  },

  ranfla: () => {
    let s = `${header("STRUCTURE", "THE BOARD OF DIRECTORS")}
     <div class="a" data-d="0.25" data-k="pop" style="position:absolute;left:560px;top:300px;width:800px;height:170px;background:#D3212D;display:flex;flex-direction:column;align-items:center;justify-content:center">
      <div class="anton" style="font-size:72px">RANFLA NACIONAL</div><div class="mono" style="font-size:20px;color:#ECE7DC;letter-spacing:.2em">SENIOR LEADERS · MOSTLY INSIDE SALVADORAN PRISONS</div></div>
     <svg width="${W}" height="${H}" style="position:absolute;inset:0">`;
    for (let i = 0; i < 8; i++) {
      const x = 180 + i * 222 + 90;
      s += `<path d="M960,470 L960,560 L${x},560 L${x},640" fill="none" stroke="#7A8089" stroke-width="3" data-k="draw" data-d="${0.6 + i * 0.05}" data-dur="0.5"/>`;
    }
    s += `</svg>`;
    for (let i = 0; i < 8; i++) {
      s += `<div class="a" data-d="${0.9 + i * 0.05}" style="position:absolute;left:${180 + i * 222}px;top:640px;width:180px;height:120px;border:3px solid #ECE7DC;display:flex;align-items:center;justify-content:center" class="osw"><span class="osw" style="font-size:28px">CLIQUE</span></div>`;
    }
    return page(s + footer("SOURCE: U.S. DEPARTMENT OF JUSTICE, JAN. 2021"));
  },

  doc_treasury: () => page(`
   <div class="a" data-d="0.05" style="position:absolute;left:330px;top:120px;width:1260px;height:840px;background:#ECE7DC;color:#141416;padding:80px 90px;transform:rotate(-1.2deg);box-shadow:0 40px 80px rgba(0,0,0,.6)">
    <div style="font-family:Plex;font-weight:600;font-size:24px;letter-spacing:.25em;color:#555">U.S. DEPARTMENT OF THE TREASURY · OCTOBER 2012</div>
    <div style="height:3px;background:#141416;margin:26px 0 40px"></div>
    <div class="anton" style="font-size:96px;line-height:1">MS-13 DESIGNATED A<br>TRANSNATIONAL CRIMINAL<br>ORGANIZATION</div>
    <div style="font-family:Plex;font-weight:500;font-size:30px;line-height:1.5;margin-top:40px;color:#333">The first street gang to receive the designation.<br>Assets under U.S. jurisdiction can be frozen.</div>
    <div style="position:absolute;left:90px;bottom:60px;font-family:Plex;font-weight:600;font-size:18px;letter-spacing:.14em;color:#777">SOURCE: ICE / TREASURY PRESS RELEASE · EXECUTIVE ORDER 13581</div>
   </div>
   <div class="stamp a" data-d="0.8" data-k="slam" data-base="rotate(-12deg)" style="position:absolute;right:300px;bottom:170px;font-size:44px;background:rgba(236,231,220,.0)">DESIGNATED · TCO</div>
   `),

  raging: (o) => page(`${header("OPERATION RAGING BULL", o.phase === 1 ? "PHASE I · EL SALVADOR" : "PHASE II · UNITED STATES")}
   <div style="position:absolute;left:110px;right:110px;top:330px;display:grid;grid-template-columns:1fr 1fr;gap:60px">
    <div class="a" data-d="0.25" style="border-top:10px solid ${o.phase === 1 ? "#D3212D" : "#3a3a40"};padding-top:30px;opacity:${o.phase === 1 ? 1 : .45}">
      <div class="mono" style="font-size:24px">PHASE I · EL SALVADOR</div>
      <div class="anton" style="font-size:220px;line-height:1">${o.phase === 1 ? `<span class="a" data-d="0.4" data-k="count" data-to="53" data-dur="1">53</span>` : "53"}</div>
      <div class="osw" style="font-size:36px">ARRESTS · 18-MONTH INVESTIGATION</div></div>
    <div class="a" data-d="0.4" style="border-top:10px solid ${o.phase === 2 ? "#D3212D" : "#3a3a40"};padding-top:30px;opacity:${o.phase === 2 ? 1 : .45}">
      <div class="mono" style="font-size:24px">PHASE II · U.S. · OCT 8 – NOV 11, 2017</div>
      <div class="anton" style="font-size:220px;line-height:1">${o.phase === 2 ? `<span class="a" data-d="0.55" data-k="count" data-to="214" data-dur="1.1">214</span>` : "—"}</div>
      <div class="osw" style="font-size:36px">${o.phase === 2 ? "ARRESTS · 93 CRIMINAL CHARGES" : "&nbsp;"}</div></div>
   </div>
   ${o.phase === 2 ? `<div class="osw a" data-d="1.2" style="position:absolute;left:110px;bottom:140px;font-size:56px;color:var(--amber)">TOTAL: 267 ARRESTS</div>` : ""}
   ${footer("SOURCES: ICE, NBC NEWS · NOVEMBER 2017")}`),

  quote: (o) => page(`<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 200px">
    <div class="anton a" data-d="0.05" style="font-size:240px;color:#D3212D;line-height:.6">“</div>
    <div class="osw a" data-d="0.2" style="font-size:92px;line-height:1.1;text-transform:none;letter-spacing:.01em">${o.q.replace(/[“”]/g, "")}</div>
    <div class="mono a" data-d="0.7" style="font-size:26px;margin-top:40px">${o.w}</div></div>`),

  doc_doj: () => page(`
   <div class="a" data-d="0.05" style="position:absolute;left:330px;top:110px;width:1260px;height:860px;background:#ECE7DC;color:#141416;padding:80px 90px;transform:rotate(1deg);box-shadow:0 40px 80px rgba(0,0,0,.6)">
    <div style="font-family:Plex;font-weight:600;font-size:24px;letter-spacing:.25em;color:#555">EASTERN DISTRICT OF NEW YORK · JANUARY 14, 2021</div>
    <div style="height:3px;background:#141416;margin:26px 0 40px"></div>
    <div class="anton" style="font-size:110px;line-height:1">INDICTMENT<br>UNSEALED</div>
    <div style="font-family:Plex;font-weight:500;font-size:32px;line-height:1.5;margin-top:40px;color:#333">Defendants: 14 leaders of the<br><b>Ranfla Nacional</b> — MS-13's top council.<br>Investigated by Joint Task Force Vulcan.</div>
    <div style="position:absolute;left:90px;bottom:60px;font-family:Plex;font-weight:600;font-size:18px;letter-spacing:.14em;color:#777">SOURCE: U.S. DEPARTMENT OF JUSTICE · CHARGES ARE ALLEGATIONS</div>
   </div>
   <div class="stamp a" data-d="0.8" data-k="slam" data-base="rotate(-10deg)" style="position:absolute;right:300px;bottom:150px;font-size:44px">TERRORISM CHARGES</div>
   `),

  charges: () => page(`${header("THE CHARGES", "UNITED STATES v. RANFLA NACIONAL")}
   <div style="position:absolute;left:110px;top:330px">
   ${["Conspiracy to provide material support to terrorists", "Conspiracy to commit acts of terrorism transcending national boundaries", "Conspiracy to finance terrorism", "Narco-terrorism conspiracy"].map((c, i) => `
    <div class="a" data-d="${0.25 + i * 0.25}" style="display:flex;align-items:center;gap:34px;margin-bottom:44px">
     <div class="anton" style="font-size:72px;color:#D3212D;width:80px">0${i + 1}</div>
     <div class="osw" style="font-size:52px;text-transform:none;letter-spacing:.01em">${c}</div></div>`).join("")}
   </div>${footer("ALLEGATIONS · DEFENDANTS PRESUMED INNOCENT UNLESS PROVEN GUILTY")}`),

  fto: () => page(`<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
    <div class="mono a" data-d="0.05" style="font-size:28px">U.S. DEPARTMENT OF STATE · FEBRUARY 20, 2025</div>
    <div class="anton a" data-d="0.25" style="font-size:150px;margin-top:30px;text-align:center;line-height:1">FOREIGN TERRORIST<br>ORGANIZATION</div>
    <div class="stamp a" data-d="0.9" data-k="slam" data-base="rotate(-5deg)" style="font-size:54px;margin-top:50px">MS-13 · DESIGNATED</div></div>
    ${footer("SOURCE: FEDERAL REGISTER, FEBRUARY 2025")}`),

  end: (o) => page(`<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
    <div class="mono a" data-d="0.05" style="font-size:30px">CASE FILE ${o.case || "001"} · ${o.label || "MS-13"}</div>
    <div class="stamp a" data-d="0.4" data-k="slam" data-base="rotate(-6deg)" style="font-size:120px;margin-top:40px;padding:20px 60px;border-width:14px">CLOSED</div>
    <div class="a" data-d="1.2" style="margin-top:80px"><span class="anton" style="font-size:64px">COLD</span> <span class="anton" style="font-size:64px;background:#D3212D;padding:0 14px">WARRANT</span></div>
    <div class="osw a" data-d="1.5" style="font-size:34px;color:var(--amber);margin-top:20px">SUBSCRIBE FOR THE NEXT CASE FILE</div></div>`),

  // ---------- generic builders for future episodes ----------
  doc: (o) => page(`
   <div class="a" data-d="0.05" style="position:absolute;left:330px;top:120px;width:1260px;height:840px;background:#ECE7DC;color:#141416;padding:80px 90px;transform:rotate(${o.rot ?? -1}deg);box-shadow:0 40px 80px rgba(0,0,0,.6)">
    <div style="font-family:Plex;font-weight:600;font-size:24px;letter-spacing:.25em;color:#555">${o.header}</div>
    <div style="height:3px;background:#141416;margin:26px 0 40px"></div>
    <div class="anton" style="font-size:${o.tsize || 96}px;line-height:1">${o.title}</div>
    <div style="font-family:Plex;font-weight:500;font-size:30px;line-height:1.5;margin-top:40px;color:#333">${o.body || ""}</div>
    ${o.source ? `<div style="position:absolute;left:90px;bottom:60px;font-family:Plex;font-weight:600;font-size:18px;letter-spacing:.14em;color:#777">${o.source}</div>` : ""}
   </div>
   ${o.stamp ? `<div class="stamp a" data-d="0.8" data-k="slam" data-base="rotate(-10deg)" style="position:absolute;right:300px;bottom:160px;font-size:44px">${o.stamp}</div>` : ""}
   `),
  list: (o) => page(`${header(o.kicker, o.title)}
   <div style="position:absolute;left:110px;top:${o.items.length > 4 ? 270 : 330}px;right:110px">
   ${o.items.map((c, i) => `<div class="a" data-d="${0.25 + i * 0.22}" style="display:flex;align-items:center;gap:34px;margin-bottom:${o.items.length > 4 ? 12 : 40}px">
     <div class="anton" style="font-size:72px;color:#D3212D;width:90px">${String(i + 1).padStart(2, "0")}</div>
     <div class="osw" style="font-size:50px;text-transform:none;letter-spacing:.01em">${c}</div></div>`).join("")}
   </div>${o.footer ? footer(o.footer) : ""}`),
  phases: (o) => page(`${header(o.kicker, o.title)}
   <div style="position:absolute;left:110px;right:110px;top:330px;display:grid;grid-template-columns:1fr 1fr;gap:60px">
    ${[o.left, o.right].map((c, i) => `<div class="a" data-d="${0.25 + i * 0.15}" style="border-top:10px solid ${o.active === i ? "#D3212D" : "#3a3a40"};padding-top:30px;opacity:${o.active === i || o.active === undefined ? 1 : .45}">
      <div class="mono" style="font-size:24px">${c.label}</div>
      <div class="anton" style="font-size:220px;line-height:1">${c.num}</div>
      <div class="osw" style="font-size:36px">${c.desc}</div></div>`).join("")}
   </div>
   ${o.total ? `<div class="osw a" data-d="1.2" style="position:absolute;left:110px;bottom:140px;font-size:56px;color:var(--amber)">${o.total}</div>` : ""}
   ${o.footer ? footer(o.footer) : ""}`),
  cards3: (o) => page(`${header(o.kicker, o.title)}
   <div style="position:absolute;left:110px;right:110px;top:330px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px">
    ${o.cards.map((c, i) => `<div class="a" data-d="${0.3 + i * 0.25}" style="border-top:8px solid ${["#D3212D", "#ECE7DC", "#E8A33D"][i % 3]};padding-top:30px">
       <div class="anton" style="font-size:${c.size || 110}px;line-height:1">${c.h}</div>
       <div class="osw" style="font-size:38px;margin-top:14px;text-transform:none;letter-spacing:.02em">${c.t}</div>
       <div style="font-family:Plex;font-size:24px;color:#7A8089;margin-top:16px;line-height:1.4">${c.s || ""}</div></div>`).join("")}
   </div>${o.footer ? footer(o.footer) : ""}`),
  timeline: (o) => page(`${header(o.kicker, o.title)}
   <div class="a" data-d="0.2" data-k="wipe" style="position:absolute;left:110px;right:110px;top:560px;height:6px;background:#3a3a40"></div>
   ${o.events.map((e, i) => { const x = 110 + i * (1700 / Math.max(1, o.events.length - 1)); return `<div class="a" data-d="${0.35 + i * 0.2}" style="position:absolute;left:${x - 12}px;top:548px;width:30px;height:30px;border-radius:50%;background:${i === o.events.length - 1 ? "#D3212D" : "#ECE7DC"}"></div>
     <div class="a" data-d="${0.4 + i * 0.2}" style="position:absolute;left:${Math.min(x - 20, 1550)}px;top:${i % 2 ? 610 : 380}px;width:340px"><div class="anton" style="font-size:64px">${e.y}</div><div class="osw" style="font-size:28px;text-transform:none;letter-spacing:.02em">${e.t}</div></div>`; }).join("")}
   ${o.footer ? footer(o.footer) : ""}`),
  map: (o) => page(mapSvg(o.map) + (o.kicker ? header(o.kicker, o.title) : "") + (o.footer ? footer(o.footer) : "")),


  // ---------- added for CASE FILE 002 (generic) ----------
  bars: (o) => { const mx = Math.max(...o.rows.map((r) => r.v)); return page(`${header(o.kicker, o.title)}
   <div style="position:absolute;left:110px;right:110px;top:320px">
   ${o.rows.map((r, i) => `<div style="margin-bottom:46px">
     <div class="a" data-d="${0.2 + i * 0.25}" style="display:flex;justify-content:space-between;align-items:baseline">
       <div class="osw" style="font-size:36px;text-transform:none;letter-spacing:.02em">${r.l}</div>
       <div class="anton" style="font-size:54px;color:${i === o.rows.length - 1 ? "#D3212D" : "#ECE7DC"}">${r.t}</div></div>
     <div class="a" data-d="${0.3 + i * 0.25}" data-k="wipe" data-dur="0.8" style="height:26px;margin-top:10px;width:${(r.v / mx) * 100}%;background:${i === o.rows.length - 1 ? "#D3212D" : "#7A8089"}"></div></div>`).join("")}
   </div>${o.footer ? footer(o.footer) : ""}`); },
  // side-view diagram of a tunnel: o.left/o.right place names, o.mex/o.total feet (border position), o.depth, o.len, o.note
  profile: (o) => { const gy = 420, ty = 780, x0 = 330, x1 = 1720, bx = x0 + (x1 - x0) * (o.mex / o.total);
    let s = `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" style="position:absolute;inset:0">
     <rect x="0" y="${gy}" width="${W}" height="${H - gy}" fill="#141417"/>
     <line x1="0" y1="${gy}" x2="${W}" y2="${gy}" stroke="#7A8089" stroke-width="3"/>
     <line x1="${bx}" y1="${gy - 90}" x2="${bx}" y2="${H - 120}" stroke="#E8A33D" stroke-width="3" stroke-dasharray="14 10" data-d="0.2"/>
     <text x="${bx + 16}" y="${gy + 50}" text-anchor="start" font-size="30" fill="#E8A33D" data-d="0.3">BORDER</text>
     <text x="${bx - 20}" y="${gy - 30}" text-anchor="end" font-size="34" fill="#ECE7DC" data-d="0.4">${o.left}</text>
     <text x="${(bx + x1) / 2}" y="${gy - 30}" text-anchor="middle" font-size="34" fill="#ECE7DC" data-d="0.4">${o.right}</text>
     <path d="M${x0},${gy} L${x0},${ty} L${x1},${ty}" fill="none" stroke="#D3212D" stroke-width="10" data-k="draw" data-d="0.5" data-dur="1.3"/>
     <line x1="${x0 - 60}" y1="${gy}" x2="${x0 - 60}" y2="${ty}" stroke="#7A8089" stroke-width="2" data-d="1.2"/>
     <text x="${x0 - 80}" y="${(gy + ty) / 2 + 12}" text-anchor="end" font-size="40" fill="#ECE7DC" data-d="1.2">${o.depth}</text>
     <text x="${(x0 + x1) / 2}" y="${ty + 80}" text-anchor="middle" font-size="44" fill="#ECE7DC" data-d="1.4">${o.len}</text>
     ${o.note ? `<text x="${(x0 + x1) / 2}" y="${ty + 130}" text-anchor="middle" font-size="24" fill="#7A8089" style="font-family:Plex;letter-spacing:.2em" data-d="1.6">${o.note}</text>` : ""}
     </svg>`;
    return page(s + header(o.kicker, o.title)); },

  // ---------- maps ----------
  map_es: () => page(mapSvg({ bounds: [[-93.5, 16.5], [-86.5, 12.6]], highlight: { 222: "#5a1217" },
    cities: [{ ll: [-89.19, 13.69], name: "SAN SALVADOR", d: 0.5 }],
    labels: [{ ll: [-91.3, 15.6], t: "GUATEMALA" }, { ll: [-87.0, 15.2], t: "HONDURAS" }, { ll: [-90.3, 12.9], t: "PACIFIC OCEAN", size: 26 }] })
    + header("EL SALVADOR", "CIVIL WAR · 1979–1992") + footer("AN ESTIMATED 75,000 KILLED · SOURCE: ENCYCLOPEDIA.COM, SALVADORAN AMERICANS")),
  map_es2: () => page(mapSvg({ bounds: [[-93.5, 16.5], [-86.5, 12.6]], highlight: { 222: "#5a1217" },
    cities: [{ ll: [-89.19, 13.69], name: "SAN SALVADOR", d: 0.5, anchor: "end", dy: -30 }, { ll: [-88.79, 13.6], name: "TECOLUCA", sub: "MEGA-PRISON · 2023", d: 0.8, size: 30, dy: 40 }] })
    + header("EL SALVADOR · MARCH 27, 2022", "STATE OF EXCEPTION")),
  map_route: () => page(mapSvg({ bounds: [[-121, 36], [-84, 11]], highlight: { 222: "#5a1217" },
    topPad: 200, arcs: [{ from: [-89.19, 13.69], to: [-118.24, 34.05], d: 0.3, dur: 1.4, bend: -0.22 }],
    cities: [{ ll: [-118.24, 34.05], name: "LOS ANGELES", d: 1.5 }, { ll: [-89.19, 13.69], name: "SAN SALVADOR", d: 0.2, anchor: "end", dy: 30 }],
    labels: [{ ll: [-102, 24], t: "MEXICO" }, { ll: [-112, 36.5], t: "UNITED STATES" }] })
    + header("1980s", "THE ROAD NORTH") + footer("HUNDREDS OF THOUSANDS OF SALVADORANS FLEE TO THE U.S.")),
  map_spread: () => page(mapSvg({ bounds: [[-121, 36], [-84, 11]], highlight: { 222: "#5a1217", 340: "#5a1217", 320: "#5a1217" }, topPad: 200,
    arcs: [{ from: [-118.24, 34.05], to: [-89.19, 13.69], d: 0.3, bend: 0.2 }, { from: [-118.24, 34.05], to: [-87.19, 14.07], d: 0.5, bend: 0.25 }, { from: [-118.24, 34.05], to: [-90.51, 14.63], d: 0.7, bend: 0.15 }],
    cities: [{ ll: [-118.24, 34.05], name: "LOS ANGELES", d: 0.1 }, { ll: [-89.19, 13.69], name: "SAN SALVADOR", d: 1.3, size: 30, anchor: "end", dy: 34 }, { ll: [-87.19, 14.07], name: "TEGUCIGALPA", d: 1.5, size: 30, dy: 10 }, { ll: [-90.51, 14.63], name: "GUATEMALA CITY", d: 1.7, size: 30, anchor: "end", dy: -26 }] })
    + header("1990s", "DEPORTED — AND REBUILT")),
  map_us: () => page(mapSvg({ useUS: true, usHighlight: ["06", "48", "51", "24", "36"],
    cities: [{ ll: [-118.24, 34.05], name: "LOS ANGELES", d: 0.2 }, { ll: [-95.37, 29.76], name: "HOUSTON", d: 0.5 }, { ll: [-77.3, 38.85], name: "NORTHERN VIRGINIA", d: 0.7, anchor: "end", size: 30 }, { ll: [-76.85, 38.6], name: "MARYLAND", d: 0.85, size: 30 }, { ll: [-73.2, 40.79], name: "LONG ISLAND", d: 1.0, size: 30 }] })
    + header("2000s", "THE GANG SPREADS ACROSS THE U.S.")),
};

const spec = JSON.parse(fs.readFileSync(process.argv[2]));
const outdir = process.argv[3];
fs.mkdirSync(outdir, { recursive: true });
const browser = await chromium.launch();
const pg = await browser.newPage({ viewport: { width: W, height: H } });
for (const g of spec) {
  const dir = path.join(outdir, g.key);
  fs.mkdirSync(dir, { recursive: true });
  const html = B[g.name](g.opts || {});
  const f = path.join(dir, "index.html");
  fs.writeFileSync(f, html);
  await pg.goto("file://" + f);
  await pg.evaluate(() => document.fonts.ready);
  const n = Math.round((g.intro || 1.8) * 30);
  for (let i = 0; i <= n; i++) {
    await pg.evaluate((t) => window.setT(t), i / 30);
    await pg.screenshot({ path: path.join(dir, `f${String(i).padStart(4, "0")}.jpg`), type: "jpeg", quality: 92 });
  }
  console.log("rendered", g.key, n + 1, "frames");
}
await browser.close();
