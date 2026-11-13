// COLD WARRANT thumbnail v2 — "trend" style (owner 2026-11-14: maximally bright, aggressive).
// usage: node thumb2.mjs <thumb2.json> <out_dir>   → thumb_A.jpg, thumb_B.jpg, thumb_C.jpg (whatever keys exist)
// thumb2.json: {"image":"/abs/frame.jpg","pos":"50% 50%","zoom":100,
//   "A":{"l1":"4 BOATS","l2":"15 MINUTES","c1":"y","c2":"w","circle":{"x":980,"y":330,"r":120},"arrow":{"x":760,"y":560,"rot":-35},
//        "inset":{"image":"/abs/mugshot_or_haul.jpg","x":930,"y":40,"w":300,"h":360,"label":"SENTENCED"},"tag":"NEW"}, "B":{...}, "C":{...}}
// Circle/arrow: only around a clearly meaningful, fully visible object (owner 2026-11-14) — otherwise leave them out.
// Rules: ≤ 3 words total visible at small size, nothing in the bottom-right 220x90 (duration badge), every word true,
// no gore/blood/bodies, no weapon pointed at camera, faces only from U.S. federal-agency releases. "NEW" tag only if the case is ≤ 7 days old.
import fs from "fs"; import path from "path"; import { createRequire } from "module";
const require = createRequire(import.meta.url); const { chromium } = require("playwright");
const NM = path.resolve("node_modules"); const cfg = JSON.parse(fs.readFileSync(process.argv[2])); const out = process.argv[3];
fs.mkdirSync(out, { recursive: true });
const COL = { y: "#FFD400", w: "#FFFFFF", r: "#FF2A2A" };
const CSS = `@font-face{font-family:Anton;src:url(file://${NM}/@fontsource/anton/files/anton-latin-400-normal.woff2)}
*{margin:0;padding:0;box-sizing:border-box}body{background:#000}
.t{position:relative;width:1280px;height:720px;overflow:hidden;background:#000}
.ph{position:absolute;inset:-2%;background-size:cover;filter:saturate(1.75) contrast(1.28) brightness(1.06)}
.grade{position:absolute;inset:0;background:radial-gradient(ellipse at 70% 45%,rgba(255,140,40,.10),rgba(0,0,0,0) 55%),linear-gradient(90deg,rgba(0,0,0,.72) 0%,rgba(0,0,0,.35) 38%,rgba(0,0,0,0) 60%)}
.vig{position:absolute;inset:0;box-shadow:inset 0 0 160px rgba(0,0,0,.8)}
.txt{position:absolute;top:26px;font-family:Anton;line-height:.92;letter-spacing:-1px;text-transform:uppercase}
.txt div{-webkit-text-stroke:9px #000;paint-order:stroke fill;text-shadow:0 8px 0 #000,0 0 30px rgba(0,0,0,.9)}
.circle{position:absolute;border:12px solid ${COL.r};border-radius:50%;box-shadow:0 0 0 5px #000,inset 0 0 0 4px #000,0 0 30px rgba(255,0,0,.6)}
.arrow{position:absolute;width:190px;height:90px;transform-origin:0 50%}
.inset{position:absolute;border:8px solid #fff;box-shadow:0 0 0 4px #000,0 18px 30px rgba(0,0,0,.7);background-size:cover;background-position:center;transform:rotate(3deg);filter:saturate(1.3) contrast(1.15)}
.inset span{position:absolute;left:50%;bottom:-26px;transform:translateX(-50%) rotate(-3deg);font-family:Anton;font-size:44px;color:#fff;background:${COL.r};padding:2px 16px 0;border:4px solid #000;white-space:nowrap}
.tag{position:absolute;left:34px;bottom:80px;font-family:Anton;font-size:56px;color:#fff;background:${COL.r};padding:4px 22px 0;border:5px solid #000;transform:rotate(4deg)}
.logo{position:absolute;left:34px;bottom:26px;display:flex;gap:8px;font-family:Anton;font-size:34px;color:#fff;align-items:center;-webkit-text-stroke:2px #000;paint-order:stroke fill}.logo i{font-style:normal;background:#D3212D;padding:2px 10px 0;-webkit-text-stroke:0}`;
const arrowSvg = `<svg viewBox="0 0 190 90" width="190" height="90"><path d="M0 30 H120 V0 L190 45 L120 90 V60 H0 Z" fill="${COL.r}" stroke="#000" stroke-width="8" stroke-linejoin="round"/></svg>`;
function news(o) {  // "news" layout (owner 2026-11-14, from 1M+ competitors): split screen — left = face/person (the emotion), right = the event/haul;
  // 2-line headline at the bottom (white / yellow), red tag top-left (true word only: CAUGHT, SEIZED, SENTENCED, RECORD, NEW).
  const L = o.left, R = o.right, split = o.split || 46;
  let h = `<div class="t">`;
  h += `<div class="ph" style="right:auto;width:${split + 2}%;background-image:url(file://${L.image});background-position:${L.pos || "50% 40%"};background-size:${L.zoom || 160}%"></div>`;
  h += `<div class="ph" style="left:${split}%;background-image:url(file://${R.image});background-position:${R.pos || "50% 50%"};background-size:${R.zoom || 140}%"></div>`;
  h += `<div style="position:absolute;left:${split}%;top:0;bottom:0;width:10px;margin-left:-5px;background:#fff;box-shadow:0 0 0 3px #000"></div>`;
  h += `<div style="position:absolute;left:0;right:0;bottom:0;height:46%;background:linear-gradient(0deg,rgba(0,0,0,.92),rgba(0,0,0,.6) 55%,rgba(0,0,0,0))"></div><div class="vig"></div>`;
  if (R.circle) { const c = R.circle; h += `<div class="circle" style="left:${c.x - c.r}px;top:${c.y - c.r}px;width:${2 * c.r}px;height:${2 * c.r}px"></div>`; }
  if (o.tag) h += `<div style="position:absolute;left:0;top:22px;font-family:Anton;font-size:58px;color:#fff;background:${COL.r};padding:6px 26px 0 22px;border:5px solid #000;border-left:0">${o.tag}</div>`;
  const s1 = o.s1 || 104, s2 = o.s2 || s1;
  h += `<div style="position:absolute;left:24px;right:24px;bottom:30px;text-align:center;font-family:Anton;line-height:1;text-transform:uppercase">
    <div style="font-size:${s1}px;color:#fff;-webkit-text-stroke:8px #000;paint-order:stroke fill;text-shadow:0 6px 0 #000">${o.l1}</div>
    <div style="font-size:${s2}px;color:${COL.y};-webkit-text-stroke:8px #000;paint-order:stroke fill;text-shadow:0 6px 0 #000;margin-top:4px">${o.l2 || ""}</div></div>`;
  return h + `<div class="logo" style="top:26px;bottom:auto;left:auto;right:26px"><span>COLD</span><i>WARRANT</i></div></div>`;
}
function html(o) {
  if (o.layout === "news") return news(o);
  const s1 = o.s1 || 210, s2 = o.s2 || Math.round(s1 * 0.62);
  let h = `<div class="t"><div class="ph" style="background-image:url(file://${o.image || cfg.image});background-position:${o.pos || cfg.pos || "50% 50%"};background-size:${o.zoom || cfg.zoom || 100}%"></div><div class="grade" style="${o.side === "right" ? "transform:scaleX(-1)" : ""}"></div><div class="vig"></div>`;
  if (o.inset) { const i = o.inset; h += `<div class="inset" style="left:${i.x}px;top:${i.y}px;width:${i.w}px;height:${i.h}px;background-image:url(file://${i.image})">${i.label ? `<span>${i.label}</span>` : ""}</div>`; }
  if (o.circle) { const c = o.circle; h += `<div class="circle" style="left:${c.x - c.r}px;top:${c.y - c.r}px;width:${2 * c.r}px;height:${2 * c.r}px"></div>`; }
  if (o.arrow) { const a = o.arrow; h += `<div class="arrow" style="left:${a.x}px;top:${a.y - 45}px;transform:rotate(${a.rot || 0}deg)">${arrowSvg}</div>`; }
  h += `<div class="txt" style="${o.side === "right" ? "right:34px;text-align:right" : "left:34px"}"><div style="font-size:${s1}px;color:${COL[o.c1 || "y"]}">${o.l1}</div>${o.l2 ? `<div style="font-size:${s2}px;color:${COL[o.c2 || "w"]};margin-top:6px">${o.l2}</div>` : ""}</div>`;
  if (o.tag) h += `<div class="tag">${o.tag}</div>`;
  return h + `<div class="logo" style="${o.side === "right" ? "top:26px;bottom:auto" : ""}"><span>COLD</span><i>WARRANT</i></div></div>`;
}
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } });
for (const k of ["A", "B", "C"]) {
  if (!cfg[k]) continue;
  const tmp = path.join(path.resolve(out), `_thumb_${k}.html`);  // file:// page so local images load (about:blank blocks them)
  fs.writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${html(cfg[k])}</body></html>`);
  await pg.goto("file://" + tmp);
  await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(250);
  const f = path.join(out, `thumb_${k}.jpg`); await pg.screenshot({ path: f, type: "jpeg", quality: 93 }); console.log("thumb", k, f); fs.unlinkSync(tmp);
}
await b.close();
